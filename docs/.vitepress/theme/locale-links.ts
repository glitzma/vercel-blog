export type Language = 'en' | 'zh'

/** Keep the current article, query and anchor when changing language. */
export function localizedPath(path: string, language: Language): string {
  const url = new URL(path, 'https://blog.local')
  const pathname = url.pathname.replace(/^\/zh(?=\/|$)/, '') || '/'
  return `${language === 'zh' ? '/zh' : ''}${pathname}${url.search}${url.hash}`
}
