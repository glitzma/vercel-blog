import assert from 'node:assert/strict'
import { test } from 'node:test'
import { localizedPath } from '../docs/.vitepress/theme/locale-links.ts'

test('home pages switch in both directions', () => {
  assert.equal(localizedPath('/', 'zh'), '/zh/')
  assert.equal(localizedPath('/zh/', 'en'), '/')
  assert.equal(localizedPath('/zh', 'en'), '/')
})

test('article, query and anchor survive a round trip', () => {
  const article = '/basic-knowledge/CSS/02.css-box-model.html?ref=search#' + encodeURIComponent('盒模型')
  const chinese = localizedPath(article, 'zh')
  assert.equal(chinese, '/zh' + article)
  assert.equal(localizedPath(chinese, 'en'), article)
})

test('switching to the current language does not duplicate the prefix', () => {
  assert.equal(localizedPath('/zh/other/04.algorithms/02.seek.html', 'zh'), '/zh/other/04.algorithms/02.seek.html')
  assert.equal(localizedPath('/zhihu.html', 'en'), '/zhihu.html')
})
