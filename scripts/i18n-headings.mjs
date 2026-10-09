import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'

const project = fileURLToPath(new URL('..', import.meta.url))
const sourceRoot = path.join(project, 'docs/zh')
const output = path.join(project, 'docs/.vitepress/cache/i18n/headings.json')
const md = await createMarkdownRenderer(sourceRoot)
const headings = {}
const hardBreaks = {}
const codeRanges = {}

async function visit(directory) {
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name)
    if (entry.isDirectory()) await visit(filename)
    else if (entry.name.endsWith('.md')) {
      const source = await fs.readFile(filename, 'utf8')
      const frontmatter = source.match(/^---\r?\n[\s\S]*?\r?\n---(?:\r?\n|$)/)?.[0] || ''
      const offset = frontmatter.split('\n').length - 1
      const tokens = md.parse(source.slice(frontmatter.length), { path: filename, relativePath: path.relative(sourceRoot, filename) })
      headings[path.relative(sourceRoot, filename)] = Object.fromEntries(tokens
        .filter(token => token.type === 'heading_open' && token.map)
        .map(token => [token.map[0] + offset, token.attrGet('id')]))
      hardBreaks[path.relative(sourceRoot, filename)] = tokens
        .filter(token => token.type === 'inline' && token.map && token.children?.some(child => child.type === 'hardbreak'))
        .flatMap(token => token.content.split('\n').flatMap((line, index) =>
          /(?: {2,}|\\)$/.test(line) ? [token.map[0] + offset + index] : []))
      codeRanges[path.relative(sourceRoot, filename)] = tokens
        .filter(token => ['fence', 'code_block'].includes(token.type) && token.map)
        .map(token => token.map.map(line => line + offset))
    }
  }
}

await visit(sourceRoot)
await fs.mkdir(path.dirname(output), { recursive: true })
await fs.writeFile(output, JSON.stringify(headings))
await fs.writeFile(path.join(path.dirname(output), 'hard-breaks.json'), JSON.stringify(hardBreaks))
await fs.writeFile(path.join(path.dirname(output), 'code-ranges.json'), JSON.stringify(codeRanges))
console.log(`Prepared source heading anchors for ${Object.keys(headings).length} pages.`)
