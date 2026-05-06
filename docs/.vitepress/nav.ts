import type { DefaultTheme } from 'vitepress'

export const nav: DefaultTheme.NavItem[] = [
  { text: 'Home', link: '/' },
  {
    text: 'Basic knowledge',
    items: [
      { text: 'CSS', link: '/basic-knowledge/CSS/00.css-tutorials-and-tips' },
      { text: 'Tailwind CSS', link: '/basic-knowledge/tailwind-css/23.tailwind-css-basics' },
      { text: 'TypeScript', link: '/basic-knowledge/typescript-learn/01.data-types/02.intro-typescript-data-types' },
      { text: 'Vue3', link: '/basic-knowledge/vue3/02.vue3-learning-path' },
      { text: 'React', link: '/basic-knowledge/react/01.react-basics/05.react-basics' },
      { text: 'Git', link: '/basic-knowledge/git/10.manual/00.git-common-commands' },
      { text: 'Vite', link: '/basic-knowledge/vite/41.vite-intro-to-mastery' },
      { text: 'AI-related', link: '/basic-knowledge/AI-related/60.agent-skills' },
      { text: 'SEO', link: '/basic-knowledge/seo/85.seo-learning' },
      { text: 'GIS', link: '/basic-knowledge/gis/69.gis-fundamentals' },
      { text: 'Postgres', link: '/basic-knowledge/postgres/83.postgres-basics' },
    ],
  },
  {
    text: 'Other',
    items: [
      { text: 'Algorithms', link: '/other/04.algorithms/02.seek' },
      { text: 'Work Notes', link: '/other/05.work-notes/01.timezone-offset' },
      { text: 'Tech Docs', link: '/other/01.tech-docs/01.nginx-proxy' },
      { text: 'Practical Tips', link: '/other/10.practical-tips/01.github-search-tips' },
    ],
  },
]
