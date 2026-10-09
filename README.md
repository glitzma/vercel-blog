# vitepressblog

## Languages

English pages use the existing URLs. Chinese originals live under `docs/zh` and
are served at `/zh/`. The language switch keeps the current article and heading.
When adding or editing an article, maintain its English and Chinese Markdown
versions at matching relative paths.
Keep matching explicit heading IDs (`{#section-id}`) in both versions when
editing them manually so switching languages keeps the current section.

## Translating articles

`npm run docs:translate` sends Chinese article prose to Google Translate and saves
English Markdown locally. Run this only when you authorize sharing the article
text with Google. Code samples, URLs and Chinese source files are preserved.

The translation worker uses one request at a time, at least 20 seconds apart,
with at most 2,000 source characters per request. These are conservative local
limits, not a guaranteed Google website quota. On HTTP 429 it respects `Retry-After` and waits at least
five minutes, increasing the wait on repeated failures. Local cached segments in
`docs/.vitepress/cache/i18n` let interrupted work resume without resending
completed segments. This is a generation tool; the blog needs no translation
service at runtime.

Use `npm run docs:translate -- --offline` to regenerate pages from an existing
local cache without sending any requests.

```sh
npm run docs:translate -- --dry-run
npm run docs:translate
npm run test:i18n
npm run docs:validate-i18n
npm run docs:build
```

The translator preserves formatting and checks for missing prose. Generated
translations still benefit from human review of technical terminology.
