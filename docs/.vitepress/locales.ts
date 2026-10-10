import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import type { DefaultTheme } from 'vitepress'
import { nav } from './nav'
import { sidebar } from './sidebar'

const labels: Record<string, string> = {
  Home: '首页',
  'Basic knowledge': '基础知识',
  Other: '其他',
  Algorithms: '算法',
  'Work Notes': '工作笔记',
  'Tech Docs': '技术文档',
  'Practical Tips': '实用技巧',
  'AI-related': 'AI 相关',
  'AI Related': 'AI 相关',
  'RAG Course': 'RAG 入门系列',
  'Practice Pack': '配套资料包',
  'RAG Week 1: Foundations': '第 1 周：建立基本认识',
  'RAG Week 2: Documents and Retrieval': '第 2 周：资料与检索',
  'RAG Week 3: Evidence-based Answers': '第 3 周：依据资料回答',
  'RAG Week 4: Evaluation and Improvement': '第 4 周：评估与改进',
  'Data Types': '数据类型',
  'Practical Applications': '实际应用',
  'React Basics': 'React 基础',
  'React Principles': 'React 原理',
  'React Ecosystem': 'React 生态',
  Manual: '使用手册',
  'Docs Notes': '文档笔记',
}

function articleTitle(link: string, fallback: string): string {
  const file = fileURLToPath(new URL(`../zh${link}.md`, import.meta.url))
  const source = readFileSync(file, 'utf8')
  const title = source.match(/^title:\s*(.+)$/m)?.[1]
    ?? source.match(/^#\s+(.+)$/m)?.[1]
  return title?.trim().replace(/^['"]|['"]$/g, '').replace(/\*\*|`/g, '').replace(/:beginner:/g, '🔰') || labels[fallback] || fallback
}

function translateSidebar(items: DefaultTheme.SidebarItem[]): DefaultTheme.SidebarItem[] {
  return items.map(item => ({
    ...item,
    text: item.link && !item.items ? articleTitle(item.link, item.text || '') : labels[item.text || ''] || item.text,
    ...(item.link ? { link: `/zh${item.link}` } : {}),
    ...(item.items ? { items: translateSidebar(item.items) } : {}),
  }))
}

export const chineseSidebar: DefaultTheme.Sidebar = Object.fromEntries(
  Object.entries(sidebar).map(([path, items]) => [
    `/zh${path}`,
    translateSidebar(Array.isArray(items) ? items : items.items),
  ]),
)

export const chineseNav: DefaultTheme.NavItem[] = nav.map(item => {
  if ('link' in item) {
    return { ...item, text: labels[item.text] || item.text, link: `/zh${item.link}` }
  }
  if ('items' in item) {
    return {
      ...item,
      text: labels[item.text] || item.text,
      items: item.items.map(child => ({
        ...child,
        text: labels[child.text || ''] || child.text,
        ...('link' in child ? { link: `/zh${child.link}` } : {}),
      })),
    }
  }
  return item
})

export const chineseTheme: DefaultTheme.Config = {
  nav: chineseNav,
  sidebar: chineseSidebar,
  outline: { label: '本页目录' },
  lastUpdated: { text: '最后更新', formatOptions: { dateStyle: 'medium', forceLocale: true } },
  docFooter: { prev: '上一篇', next: '下一篇' },
  darkModeSwitchLabel: '外观',
  lightModeSwitchTitle: '切换到浅色模式',
  darkModeSwitchTitle: '切换到深色模式',
  sidebarMenuLabel: '菜单',
  returnToTopLabel: '返回顶部',
  langMenuLabel: '切换语言',
  skipToContentLabel: '跳转到内容',
  footer: { copyright: '版权所有 © 2015 - 2026' },
  notFound: {
    title: '页面未找到',
    quote: '抱歉，您访问的页面不存在或已被移除。',
    linkLabel: '返回首页',
    linkText: '返回首页',
  },
}

export const chineseSearch = {
  button: { buttonText: '搜索', buttonAriaLabel: '搜索文档' },
  modal: {
    displayDetails: '显示详细列表',
    resetButtonTitle: '清除搜索',
    backButtonTitle: '关闭搜索',
    noResultsText: '没有找到相关结果',
    footer: {
      selectText: '选择',
      selectKeyAriaLabel: '回车键',
      navigateText: '切换',
      navigateUpKeyAriaLabel: '向上箭头',
      navigateDownKeyAriaLabel: '向下箭头',
      closeText: '关闭',
      closeKeyAriaLabel: 'Esc 键',
    },
  },
}
