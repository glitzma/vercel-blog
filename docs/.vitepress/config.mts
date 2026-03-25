import { defineConfig } from "vitepress";
import { nav } from "./nav";
import { sidebar } from "./sidebar";
// import tailwindcss from '@tailwindcss/vite'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  vite: {
    // plugins: [tailwindcss()]
  },
  lastUpdated: false,
  title: "Glittering's blog",
  description: "A VitePress Site",
  themeConfig: {
    search: {
      provider: "local",
    },
    // https://vitepress.dev/reference/default-theme-config
    nav,
    sidebar,

    socialLinks: [{ icon: "github", link: "https://github.com/happy760690" }],

    footer: {
      // message: 'Released under the MIT License.',
      copyright: "Copyright © 2026",
    },
  },
});
