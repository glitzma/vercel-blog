<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import { useData } from 'vitepress'
import NotFound from './NotFound.vue'
import { computed } from 'vue'

const { page } = useData()

const formatDate = (dateStr: string) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return date.toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric' })
}

const lastUpdatedDate = computed(() => {
  return page.value.lastUpdated ? new Date(page.value.lastUpdated).toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric' }) : null
})
</script>

<template>
  <NotFound v-if="page.isNotFound"/>
  <DefaultTheme.Layout v-else>
    <template #doc-before>
      <div class="doc-date-info" v-if="page.frontmatter.date || page.lastUpdated" style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--vp-c-divider);">
        <span v-if="page.frontmatter.date">创建时间: {{ formatDate(page.frontmatter.date) }}</span>
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