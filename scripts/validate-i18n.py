"""Check that English pages contain no untranslated Chinese prose."""
import importlib.util
from pathlib import Path
import sys
import json
import subprocess

scripts = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('google_translation', scripts / 'translate-google.py')
translation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(translation)
docs = scripts.parent / 'docs'
subprocess.run(['node', str(scripts / 'i18n-headings.mjs')], check=True, cwd=scripts.parent)
code_ranges = json.loads((docs / '.vitepress/cache/i18n/code-ranges.json').read_text(encoding='utf8'))
failures = []
pages = 0

for source in sorted((docs / 'zh').rglob('*.md')):
    relative = source.relative_to(docs / 'zh')
    if relative.parts[0] not in ('basic-knowledge', 'other'):
        continue
    target = docs / relative
    ignored_lines = {line for start, end in code_ranges.get(relative.as_posix(), []) for line in range(start, end)}
    _, tasks = translation.prepare(target.read_text(encoding='utf8'), ignored_lines)
    failures.extend(f'{relative}:{task[0] + 1}: {task[3][:100]}' for task in tasks)
    pages += 1

if failures:
    print('\n'.join(failures), file=sys.stderr)
    sys.exit(1)
print(f'All {pages} English articles have translated titles and prose. Code and metadata are excluded.')
