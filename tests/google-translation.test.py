import importlib.util
import json
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('google_translation', Path(__file__).resolve().parent.parent / 'scripts/translate-google.py')
translation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(translation)


class TranslationTests(unittest.TestCase):
    def test_retry_after_seconds_and_date(self):
        self.assertEqual(translation.retry_after('120'), 120)
        self.assertEqual(translation.retry_after('Fri, 09 Oct 2026 08:05:00 GMT', now=1791532800), 300)
        self.assertEqual(translation.retry_after('invalid'), 0)

    def test_prose_extraction_preserves_fenced_code_and_metadata(self):
        source = '---\ntitle: 中文标题\nauthor: 作者\n---\n## 中文标题\n```js\nconst name = "中文代码"\n```\n中文正文 `代码`\n'
        lines, tasks = translation.prepare(source)
        self.assertEqual([task[0] for task in tasks], [1, 4, 8])
        self.assertEqual(lines[6], 'const name = "中文代码"\n')

    def test_changed_links_or_missing_bold_fail_validation(self):
        source = '**中文** [文档](https://example.com)'
        self.assertTrue(translation.valid_translation(source, '**English** [Docs](https://example.com)'))
        self.assertFalse(translation.valid_translation(source, '**English** [Docs](https://changed.com)'))
        self.assertFalse(translation.valid_translation(source, 'English [Docs](https://example.com)'))

    def test_fallback_preserves_emphasis_brackets_and_links(self):
        source = '*中文*【说明】 [文档](https://example.com)'
        protected, values = translation.protect(source)
        restored = translation.restore_fragments([protected.replace('中文', 'English').replace('说明', 'Note').replace('文档', 'Docs')], values)
        self.assertEqual(restored, '*English*【Note】 [Docs](https://example.com)')
        self.assertTrue(translation.valid_translation(source, restored))

    def test_container_type_is_kept_out_of_translation(self):
        _, tasks = translation.prepare(':::tip 注意\n正文\n:::\n')
        self.assertEqual(tasks[0][1], ':::tip ')
        self.assertEqual(tasks[0][3], '注意')

    def test_unquoted_identifier_is_preserved_as_one_span(self):
        protected, values = translation.protect('只读属性 __v_isReadonly')
        restored = translation.restore_fragments([protected.replace('只读属性', 'Readonly property')], values)
        self.assertEqual(restored, 'Readonly property __v_isReadonly')

    def test_nested_list_prefix_is_not_translated(self):
        _, tasks = translation.prepare('- * 什么是逻辑推理\n')
        self.assertEqual(tasks[0][1], '- * ')
        self.assertEqual(tasks[0][3], '什么是逻辑推理')

    def test_translated_numbering_stays_a_paragraph(self):
        self.assertEqual(translation.preserve_paragraph('一、介绍', '1. Introduction'), '1\\. Introduction')
        self.assertEqual(translation.preserve_paragraph('- 列表', '- List'), '- List')

    def test_spaces_inside_emphasis_are_rejected(self):
        self.assertFalse(translation.valid_translation('**介绍**', '** Introduction **'))

    def test_emoji_shortcode_is_kept_in_one_piece(self):
        protected, values = translation.protect('**:small_orange_diamond:介绍**')
        result = translation.restore_fragments([protected.replace('介绍', 'Introduction')], values)
        self.assertEqual(result, '**:small_orange_diamond:Introduction**')

    def test_parser_code_ranges_protect_nested_fences(self):
        source = '- ```sh\n  # 中文代码注释\n  npm search name\n  ```\n中文正文\n'
        _, tasks = translation.prepare(source, {0, 1, 2, 3})
        self.assertEqual([task[0] for task in tasks], [4])

    def test_underscored_emphasis_is_not_a_code_identifier(self):
        self.assertTrue(translation.valid_translation('_斜体文本_', '_italic text_'))
        self.assertTrue(translation.valid_translation('__粗体文本__', '__Bold Text__'))
        self.assertTrue(translation.valid_translation('___粗斜体文本___', '___Bold italic text___'))
        self.assertFalse(translation.valid_translation('属性 foo_bar', 'Property foo_baz'))

    def test_offline_mode_never_sends_a_request(self):
        with self.assertRaisesRegex(RuntimeError, 'offline mode'):
            translation.Translator(20, 2000, offline=True).request('中文')

    def test_google_response_guard_and_length_prefix(self):
        payload = [None, [[[None, None, None, None, None, [['What is TypeScript?']]]]]]
        body = ")]}'\n\n100\n" + json.dumps([['wrb.fr', 'MkEWBc', json.dumps(payload)]])
        self.assertEqual(translation.parse_response(body), 'What is TypeScript?')

    def test_missing_translation_requests_a_cooldown(self):
        body = ")]}'\n\n100\n" + json.dumps([['wrb.fr', 'MkEWBc', None]])
        with self.assertRaises(translation.GoogleResponseError):
            translation.parse_response(body)


if __name__ == '__main__':
    unittest.main()
