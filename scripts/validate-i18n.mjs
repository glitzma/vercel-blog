import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'

const project = fileURLToPath(new URL('..', import.meta.url))
const docs = path.join(project, 'docs')
const chinese = path.join(docs, 'zh')
const md = await createMarkdownRenderer(docs)
const failures = []
let pages = 0

function parse(source, filename) {
  const body = source.replace(/^---\r?\n[\s\S]*?\r?\n---(?:\r?\n|$)/, '')
  return md.parse(body, { path: filename, relativePath: path.relative(docs, filename) })
}

function snapshot(tokens) {
  return {
    structure: tokens.map(token => [token.type, token.tag, token.nesting]),
    headings: tokens.filter(token => token.type === 'heading_open').map(token => token.attrGet('id')),
    code: tokens.filter(token => ['fence', 'code_block'].includes(token.type)).map(token => [token.type, token.info, token.content]),
    inlineCode: tokens.flatMap(token => (token.children || []).filter(child => child.type === 'code_inline').map(child => child.content)).sort(),
    links: tokens.flatMap(token => (token.children || []).filter(child => child.type === 'link_open' && child.markup !== 'linkify').map(child => child.attrGet('href'))).sort(),
    images: tokens.flatMap(token => (token.children || []).filter(child => child.type === 'image').map(child => child.attrGet('src'))),
    formatting: tokens.flatMap(token => (token.children || []).filter(child => !['text', 'softbreak'].includes(child.type) && child.markup !== 'linkify').map(child => [child.type, child.tag, child.nesting])).sort(),
  }
}

async function visit(directory) {
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name)
    if (entry.isDirectory()) await visit(filename)
    else if (entry.name.endsWith('.md')) {
      const relative = path.relative(chinese, filename)
      const english = path.join(docs, relative)
      try {
        const [original, translated] = await Promise.all([fs.readFile(filename, 'utf8'), fs.readFile(english, 'utf8')])
        assert.equal(translated.split('\n').length, original.split('\n').length, 'line count changed')
        const before = snapshot(parse(original, filename))
        const after = snapshot(parse(translated, english))
        for (const field of Object.keys(before)) {
          if (field !== 'formatting') {
            assert.deepEqual(after[field], before[field], `${field} changed`)
            continue
          }
          // English punctuation can make originally intended emphasis valid.
          // Preserve every rendered emphasis span and compare other syntax exactly.
          const count = values => values.reduce((result, value) => {
            const key = JSON.stringify(value)
            result[key] = (result[key] || 0) + 1
            return result
          }, {})
          const original = count(before[field]), translated = count(after[field])
          for (const key of new Set([...Object.keys(original), ...Object.keys(translated)])) {
            const type = JSON.parse(key)[0]
            if (/^(?:strong|em|s)_(?:open|close)$/.test(type)) {
              assert.ok((translated[key] || 0) >= (original[key] || 0), `${type} was lost`)
            } else {
              assert.equal(translated[key] || 0, original[key] || 0, `${type} changed`)
            }
          }
        }
      } catch (error) {
        failures.push({ page: relative, error: error.message.split('\n')[0] })
      }
      pages++
    }
  }
}

await visit(path.join(chinese, 'basic-knowledge'))
await visit(path.join(chinese, 'other'))
console.log(`Checked Markdown structure, code, links, images and heading anchors for ${pages} article pairs.`)
if (failures.length) {
  console.error(JSON.stringify(failures, null, 2))
  process.exitCode = 1
} else {
  console.log('All article pairs preserve their source structure.')
}
