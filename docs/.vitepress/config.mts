import { defineConfig } from "vitepress";
import { nav } from "./nav";
import { sidebar } from "./sidebar";
import { chineseSearch, chineseTheme } from "./locales";
// import tailwindcss from '@tailwindcss/vite'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  vite: {
    // plugins: [tailwindcss()]
  },
  lastUpdated: true,
  title: "Maggie's blog",
  lang: "en-US",
  description: "Notes, guides, and deep dives on modern frontend engineering",
  markdown: {
    config(md) {
      const fence = md.renderer.rules.fence!;
      md.renderer.rules.fence = (tokens, index, options, env, self) => {
        const html = fence(tokens, index, options, env, self);
        return env.localeIndex === "zh"
          ? html.replace('<button title="Copy Code"', '<button title="复制代码"')
          : html;
      };
      const labels = {
        tip: ["TIP", "提示"],
        info: ["INFO", "说明"],
        warning: ["WARNING", "警告"],
        danger: ["DANGER", "危险"],
        details: ["Details", "详情"],
      };
      for (const [kind, [english, chinese]] of Object.entries(labels)) {
        const rule = `container_${kind}_open`;
        const render = md.renderer.rules[rule]!;
        md.renderer.rules[rule] = (tokens, index, options, env, self) => {
          const html = render(tokens, index, options, env, self);
          return env.localeIndex === "zh" && tokens[index].info.trim() === kind
            ? html.replace(`>${english}</`, `>${chinese}</`)
            : html;
        };
      }
    },
  },
  locales: {
    root: { label: "English", lang: "en-US" },
    zh: {
      label: "简体中文",
      lang: "zh-CN",
      title: "Maggie 的博客",
      description: "现代前端工程的学习笔记、实用指南与原理解析",
      themeConfig: chineseTheme,
    },
  },
  themeConfig: {
    search: {
      provider: "local",
      options: {
        locales: { zh: { translations: chineseSearch } },
      },
    },
    // https://vitepress.dev/reference/default-theme-config
    nav,
    sidebar,
    lastUpdated: {
      text: "Last updated",
      formatOptions: { dateStyle: "medium", forceLocale: true },
    },
    notFound: {
      title: "Page not found",
      quote: "Sorry, this page does not exist or has been removed.",
      linkLabel: "Go to home",
      linkText: "Back to home",
    },

    socialLinks: [{ icon: "github", link: "https://github.com/happy760690" }],

    footer: {
      // message: 'Released under the MIT License.',
      copyright: "Copyright © 2015 - 2026",
    },
  },
});
