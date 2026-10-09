<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import { useData } from 'vitepress'
import NotFound from './NotFound.vue'
import LanguageSwitcher from './components/LanguageSwitcher.vue'

const { page, lang } = useData()

const formatDate = (dateStr: string) => {
  if (!dateStr) return ''
  const normalized = /^\d{4}-\d{2}-\d{2}/.test(dateStr)
    ? dateStr.slice(0, 10) + 'T00:00:00+08:00'
    : dateStr
  const date = new Date(normalized)
  return date.toLocaleDateString(lang.value, { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'Asia/Shanghai' })
}
</script>

<template>
  <DefaultTheme.Layout>
    <template #nav-bar-content-after>
      <LanguageSwitcher />
    </template>
    <template #not-found>
      <NotFound />
    </template>
    <template #doc-before>
      <div class="doc-date-info" v-if="page.frontmatter.date || page.lastUpdated" style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--vp-c-divider);">
        <span v-if="page.frontmatter.date">{{ lang === 'zh-CN' ? '创建时间' : 'Created' }}: {{ formatDate(page.frontmatter.date) }}</span>
      </div>
    </template>
  </DefaultTheme.Layout>
</template>

<style>
.doc-date-info {
  text-align: right;
  font-size: 14px;
  color: var(--vp-c-text-2);
}
</style>
