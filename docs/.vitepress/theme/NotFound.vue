<script setup lang="ts">
import { useData, withBase } from 'vitepress'

const { theme, lang } = useData()
</script>

<template>
  <div class="not-found">
    <div class="container">
      <h1 class="error-code">404</h1>
      <h2 class="error-title">{{ theme.notFound.title }}</h2>
      <p class="error-desc">{{ theme.notFound.quote }}</p>
      <a :href="withBase(lang === 'zh-CN' ? '/zh/' : '/')" class="back-home">{{ theme.notFound.linkText }}</a>
    </div>
  </div>
</template>

<style scoped>
.not-found {
  min-height: calc(100vh - var(--vp-nav-height) - 100px);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  background: var(--vp-c-bg);
}

.container {
  max-width: 400px;
}

.error-code {
  font-size: 6rem;
  font-weight: 800;
  color: var(--vp-c-brand-1);
  margin: 0;
  line-height: 1;
}

.error-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0.5rem 0;
  color: var(--vp-c-text-1);
}

.error-desc {
  font-size: 1rem;
  color: var(--vp-c-text-2);
  margin: 0 0 2rem;
}

.back-home {
  display: inline-block;
  padding: 0.6rem 1.5rem;
  background: var(--vp-c-brand-1);
  color: var(--vp-c-white);
  border-radius: 6px;
  text-decoration: none;
  font-weight: 500;
  transition: background-color 0.2s;
}

.back-home:hover {
  background: var(--vp-c-brand-2);
}
</style>
