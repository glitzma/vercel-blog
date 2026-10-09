"""Generate local English articles from docs/zh, with slow, resumable Google requests.

The Google Translate website does not publish a fixed API quota. These conservative
limits are local safeguards; HTTP 429/Retry-After always take precedence.
No translation service is used by the deployed blog.
"""
import argparse
import email.utils
import hashlib
import http.client
import json
import os
from pathlib import Path
from collections import Counter
import random
import re
import subprocess
import socket
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
CACHE = DOCS / '.vitepress/cache/i18n'
SEPARATOR = '\n|||\n'
CJK = re.compile(r'[\u3400-\u9fff]')
SPAN_PATTERN = r'(`+)(?:(?!\1).)*\1|\]\((?:[^()\n]|\([^()]*\))*\)|<[^>]+>|https?://[^\s<>]+|\{#[^}]+\}|&(?:#\d+|\w+);|\\[\\`*{}_\[\]()#+.!|>-]|:[A-Za-z0-9_+-]+:'
IDENTIFIER_PATTERN = r'(?<![A-Za-z0-9_$])(?:[A-Za-z$][A-Za-z0-9$]*_[A-Za-z0-9_$]+|_+[A-Za-z$][A-Za-z0-9_$]*)(?![A-Za-z0-9_$])'
MARKDOWN_PATTERN = r'\*\*|__|~~|[|\[\]【】*_]'
PROTECTED = re.compile('|'.join((SPAN_PATTERN, IDENTIFIER_PATTERN, MARKDOWN_PATTERN)))
SYNTAX = re.compile('|'.join((SPAN_PATTERN, MARKDOWN_PATTERN)))
IDENTIFIER = re.compile(IDENTIFIER_PATTERN)


def digest(text):
    return hashlib.sha256(text.encode('utf8')).hexdigest()


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf8')
    os.replace(temporary, path)


def retry_after(value, now=None):
    if not value:
        return 0
    try:
        return max(0, float(value))
    except ValueError:
        try:
            return max(0, email.utils.parsedate_to_datetime(value).timestamp() - (now or time.time()))
        except (ValueError, TypeError):
            return 0


class GoogleResponseError(ValueError):
    """A successful HTTP response without usable translation data."""


def parse_response(body):
    """Google's webpage response is length-prefixed JSON with an XSSI guard."""
    for line in body.splitlines():
        if not line.startswith('['):
            continue
        for row in json.loads(line):
            if len(row) > 2 and row[0] == 'wrb.fr' and row[1] == 'MkEWBc' and row[2]:
                try:
                    data = json.loads(row[2])
                    translated = ''.join(part[0] or '' for part in data[1][0][0][5])
                    if translated:
                        return translated
                except (TypeError, IndexError):
                    pass
    raise GoogleResponseError('Google did not return a translation')


def protect(text):
    values = []
    def replace(match):
        token = f'ZXK{len(values)}KXZ'
        values.append(match[0])
        return token
    return PROTECTED.sub(replace, text), values


def restore_fragments(parts, values):
    text = ' '.join(part.strip() for part in parts if part.strip())
    emphasis = {}
    for index, value in enumerate(values):
        marker = f'ZXK{index}KXZ'
        if text.count(marker) != 1:
            raise ValueError('A protected Markdown span was lost')
        if value in ('**', '__', '~~', '*', '_'):
            opening = emphasis.get(value, 0) % 2 == 0
            if opening:
                text = re.sub(re.escape(marker) + r'\s*', lambda _: value, text)
            else:
                text = re.sub(r'\s*' + re.escape(marker), lambda _: value, text)
            emphasis[value] = emphasis.get(value, 0) + 1
        else:
            text = text.replace(marker, value)
    return text.strip()


def prepare(source, ignored_lines=()):
    lines = source.splitlines(keepends=True)
    tasks = []
    fence = None
    frontmatter = bool(lines) and lines[0].strip() == '---'
    script_block = None
    for index, raw in enumerate(lines):
        if index in ignored_lines:
            continue
        line = raw.rstrip('\r\n')
        ending = raw[len(line):]
        if frontmatter:
            if index and line.strip() == '---':
                frontmatter = False
            elif re.match(r'^(title|description):', line) and CJK.search(line):
                key, content = line.split(':', 1)
                tasks.append((index, key + ': ', ending, content.strip().strip('\"\''), True))
            continue
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not line.strip()[len(match[1]):].strip():
                fence = None
            continue
        if match:
            fence = match[1]
            continue
        if script_block:
            if re.search(fr'</{script_block}\s*>', line):
                script_block = None
            continue
        script = re.match(r'^\s*<(script|style)\b', line)
        if script:
            if not re.search(fr'</{script[1]}\s*>', line):
                script_block = script[1]
            continue
        if not CJK.search(line) or re.match(r'^\s*<!--', line):
            continue
        prefix = re.match(r'^\s*(?:>\s*)*(?:(?:#{1,6}|[-+*]|\d+[.)])\s+|:{3,}\s*(?:tip|info|warning|danger|details)\s+)*', line)[0]
        content = line[len(prefix):]
        if CJK.search(PROTECTED.sub('', content)):
            tasks.append((index, prefix, ending, content, False))
    return lines, tasks


def valid_translation(source, translated):
    if not bool(translated.strip()) or CJK.search(PROTECTED.sub('', translated)) or not (
        sorted(match[0] for match in SYNTAX.finditer(source)) ==
        sorted(match[0] for match in SYNTAX.finditer(translated))
    ):
        return False
    original_identifiers = Counter(match[0] for match in PROTECTED.finditer(source) if IDENTIFIER.fullmatch(match[0]))
    translated_identifiers = Counter(match[0] for match in PROTECTED.finditer(translated) if IDENTIFIER.fullmatch(match[0]))
    if any(translated_identifiers[value] < count for value, count in original_identifiers.items()):
        return False
    for marker in ('**', '__', '~~', '*', '_'):
        before = [match for match in SYNTAX.finditer(source) if match[0] == marker]
        after = [match for match in SYNTAX.finditer(translated) if match[0] == marker]
        for opening, closing, new_opening, new_closing in zip(before[::2], before[1::2], after[::2], after[1::2]):
            original = source[opening.end():closing.start()]
            generated = translated[new_opening.end():new_closing.start()]
            if marker in ('_', '__') and opening.start() and source[opening.start() - 1].isalnum() and original and original[0].isalnum():
                continue
            if original and not original[0].isspace() and not original[-1].isspace():
                if not generated or generated[0].isspace() or generated[-1].isspace():
                    return False
    return True


def preserve_paragraph(source, translated):
    """Keep translated Chinese numbering from creating new Markdown blocks."""
    pattern = r'^(?:\d+[.)]|#{1,6}|[-+*])\s+'
    if re.match(pattern, translated) and not re.match(pattern, source):
        translated = re.sub(r'^(\d+)([.)])', r'\1\\\2', translated)
        translated = re.sub(r'^([#+*-])', r'\\\1', translated)
    return translated


class Translator:
    def __init__(self, interval, batch_chars, offline=False):
        self.interval = interval
        self.batch_chars = batch_chars
        self.offline = offline
        self.requests = 0
        self.last_request = 0
        self.progress = {}
        self.state_path = CACHE / 'progress.json'
        if self.state_path.exists():
            self.progress = json.loads(self.state_path.read_text(encoding='utf8'))
            self.requests = self.progress.get('requests', 0)
            elapsed = max(0, time.time() - self.progress.get('lastRequestAt', self.progress.get('updatedAt', 0)))
            self.last_request = time.monotonic() - elapsed

    def status(self, **updates):
        self.progress.update(updates)
        self.progress['requests'] = self.requests
        self.progress['updatedAt'] = time.time()
        save_json(self.state_path, self.progress)

    def cached(self, text):
        path = CACHE / 'segments' / (digest(text) + '.json')
        if path.exists():
            entry = json.loads(path.read_text(encoding='utf8'))
            if entry['source'] == text:
                return entry['translation']
        return None

    def remember(self, source, translated):
        save_json(CACHE / 'segments' / (digest(source) + '.json'), {
            'source': source, 'translation': translated, 'provider': 'Google Translate',
        })

    def request(self, text):
        if self.offline:
            raise RuntimeError('Missing cached translation; offline mode cannot contact Google.')
        cooldown = (self.progress.get('retryAt') or 0) - time.time()
        if cooldown > 0:
            print(f'Resuming after the saved cooldown ({round(cooldown)} seconds).', flush=True)
            time.sleep(cooldown)
        wait = self.interval - (time.monotonic() - self.last_request)
        if wait > 0:
            time.sleep(wait)
        self.last_request = time.monotonic()
        self.requests += 1
        self.status(phase='translating', currentCharacters=len(text), retryAt=None, lastRequestAt=time.time(), error=None)
        rpc = [['MkEWBc', json.dumps([[text, 'zh-CN', 'en', True], [None]], ensure_ascii=False), None, 'generic']]
        form = urllib.parse.urlencode({'f.req': json.dumps([rpc], ensure_ascii=False)}).encode()
        request = urllib.request.Request(
            'https://translate.google.com/_/TranslateWebserverUi/data/batchexecute?rpcids=MkEWBc',
            data=form,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'User-Agent': 'Mozilla/5.0',
                'Origin': 'https://translate.google.com',
                'Referer': 'https://translate.google.com/',
            },
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode('utf8')
            try:
                return parse_response(body)
            except GoogleResponseError:
                save_json(CACHE / 'last-incomplete-response.json', {'body': body})
                raise

    def batch(self, texts):
        results = [self.cached(text) for text in texts]
        missing = list(dict.fromkeys(text for text, result in zip(texts, results) if result is None))
        if missing:
            payload = SEPARATOR.join(missing)
            failures = 0
            while True:
                try:
                    translated = [re.sub(r'\s+', ' ', part).strip() for part in self.request(payload).split('|||')]
                    if len(translated) != len(missing) or any(not part for part in translated):
                        if len(missing) == 1:
                            raise ValueError('Google returned an empty or malformed paragraph')
                        middle = len(missing) // 2
                        self.batch(missing[:middle])
                        self.batch(missing[middle:])
                        break
                    for source, result in zip(missing, translated):
                        self.remember(source, result)
                    break
                except (urllib.error.URLError, TimeoutError, socket.timeout, ConnectionError, http.client.IncompleteRead, GoogleResponseError) as error:
                    code = getattr(error, 'code', None)
                    if code is not None and code not in (429, 500, 502, 503, 504):
                        raise
                    failures += 1
                    minimum = retry_after(error.headers.get('Retry-After')) if isinstance(error, urllib.error.HTTPError) else 0
                    cooldown = max(minimum, min(3600, 300 * (2 ** min(failures - 1, 4)))) + random.uniform(0, 10)
                    self.status(phase='cooldown', retryAt=time.time() + cooldown, error=str(error))
                    print(f'Google requested a pause ({error}); retrying after {round(cooldown)} seconds.', flush=True)
                    # The worker sleeps; the interactive agent stays responsive.
                    time.sleep(cooldown)
            results = [self.cached(text) for text in texts]
        return results

    def translate_all(self, texts, progress_key='Segments'):
        unique = list(dict.fromkeys(texts))
        pending = [text for text in unique if self.cached(text) is None]
        total_key, done_key = 'total' + progress_key, 'completed' + progress_key
        self.status(**{total_key: len(unique), done_key: len(unique) - len(pending)})
        batch = []
        size = 0
        done = len(unique) - len(pending)
        for text in pending:
            added = len(text) + (len(SEPARATOR) if batch else 0)
            if batch and size + added > self.batch_chars:
                self.batch(batch)
                done += len(batch)
                self.status(**{done_key: done})
                print(f'Translated {progress_key}: {done}/{len(unique)}; requests: {self.requests}', flush=True)
                batch, size = [], 0
            if len(text) > self.batch_chars:
                raise ValueError('A single paragraph exceeds the configured character limit')
            batch.append(text)
            size += len(text) + (len(SEPARATOR) if len(batch) > 1 else 0)
        if batch:
            self.batch(batch)
            self.status(**{done_key: len(unique)})

    def resolve(self, source):
        translated = self.cached(source)
        if translated and valid_translation(source, translated):
            return translated
        protected, values = protect(source)
        parts = re.split(r'(ZXK\d+KXZ)', protected)
        needed = [part.strip() for part in parts if CJK.search(part)]
        self.batch(needed)
        for index, part in enumerate(parts):
            if CJK.search(part):
                parts[index] = self.cached(part.strip())
        result = restore_fragments(parts, values)
        if not valid_translation(source, result):
            raise ValueError('Translated prose or protected Markdown did not pass validation')
        self.remember(source, result)
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--interval', type=float, default=20, help='Minimum seconds between requests (default 20, at least 10).')
    parser.add_argument('--batch-chars', type=int, default=2000, help='Maximum source characters per request (default 2000, at most 4500).')
    parser.add_argument('--dry-run', action='store_true', help='Show the workload without contacting Google or changing articles.')
    parser.add_argument('--offline', action='store_true', help='Generate articles only from the existing cache; never contact Google.')
    args = parser.parse_args()
    if args.interval < 10 or not 100 <= args.batch_chars <= 4500:
        parser.error('Use an interval of at least 10 seconds and batches of 100-4500 characters.')

    files = sorted(path for path in (DOCS / 'zh').rglob('*.md')
        if path.relative_to(DOCS / 'zh').parts[0] in ('basic-knowledge', 'other'))
    subprocess.run(['node', str(ROOT / 'scripts/i18n-headings.mjs')], check=True, cwd=ROOT)
    headings = json.loads((CACHE / 'headings.json').read_text(encoding='utf8'))
    hard_breaks = json.loads((CACHE / 'hard-breaks.json').read_text(encoding='utf8'))
    code_ranges = json.loads((CACHE / 'code-ranges.json').read_text(encoding='utf8'))
    prepared = [(path, *prepare(path.read_text(encoding='utf8'), {
        line for start, end in code_ranges.get(path.relative_to(DOCS / 'zh').as_posix(), []) for line in range(start, end)
    })) for path in files]
    texts = [task[3] for _, _, tasks in prepared for task in tasks]
    unique = list(dict.fromkeys(texts))
    print(f'Articles: {len(files)}; unique prose segments: {len(unique)}; source characters: {sum(map(len, unique))}', flush=True)
    if args.dry_run:
        return

    translator = Translator(args.interval, args.batch_chars, args.offline)
    translator.status(totalPages=len(files), completedPages=0)
    translator.translate_all(texts)
    # Collect repairs before writing so they use the same slow, bounded batches.
    fragments = []
    for text in unique:
        if not valid_translation(text, translator.cached(text)):
            protected, _ = protect(text)
            fragments.extend(part.strip() for part in re.split(r'(ZXK\d+KXZ)', protected) if CJK.search(part))
    translator.translate_all(fragments, 'FormattingSegments')
    manifest_path = CACHE / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf8')) if manifest_path.exists() else {}
    for page_number, (source, lines, tasks) in enumerate(prepared, 1):
        relative = source.relative_to(DOCS / 'zh').as_posix()
        for index, prefix, ending, text, is_yaml in tasks:
            result = translator.resolve(text)
            if is_yaml:
                result = json.dumps(result, ensure_ascii=False)
            else:
                result = preserve_paragraph(text, result)
                if str(index) in headings.get(relative, {}) and not re.search(r'\{#[^}]+\}', result):
                    result += ' {#' + headings[relative][str(index)] + '}'
                elif index in hard_breaks.get(relative, []) and not result.endswith('\\'):
                    result += '\\'
            lines[index] = prefix + result + ending
        output = ''.join(lines)
        destination = DOCS / relative
        temporary = destination.with_suffix('.md.tmp')
        temporary.write_text(output, encoding='utf8')
        os.replace(temporary, destination)
        manifest[relative] = {
            'sourceHash': digest(source.read_text(encoding='utf8')),
            'outputHash': digest(output), 'provider': 'Google Translate',
        }
        save_json(manifest_path, manifest)
        translator.status(phase='writing', completedPages=page_number, currentPage=relative)
        print(f'Saved English article: {page_number}/{len(files)} {relative}', flush=True)
    translator.status(phase='complete', completedPages=len(files), currentPage=None, error=None)
    print('All English articles saved. Run npm run docs:build to verify the site.', flush=True)


if __name__ == '__main__':
    main()
