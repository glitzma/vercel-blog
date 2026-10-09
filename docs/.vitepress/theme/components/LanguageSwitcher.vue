<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useData, useRoute, withBase } from 'vitepress'
import { localizedPath } from '../locale-links'

const { lang, hash, site } = useData()
const route = useRoute()
const mounted = ref(false)
onMounted(() => { mounted.value = true })
const isChinese = computed(() => lang.value === 'zh-CN')
const link = computed(() => {
  const path = '/' + route.path.slice(site.value.base.length)
  const query = mounted.value ? window.location.search : ''
  const anchor = mounted.value ? hash.value : ''
  return withBase(localizedPath(path + query + anchor, isChinese.value ? 'en' : 'zh'))
})
</script>

<template>
  <a
    class="language-switcher"
    :href="link"
    target="_self"
    :lang="isChinese ? 'en' : 'zh-CN'"
    :hreflang="isChinese ? 'en-US' : 'zh-CN'"
    :aria-label="isChinese ? 'Switch to English' : '切换到中文'"
    :title="isChinese ? 'Switch to English' : '切换到中文'"
  >
    <span class="vpi-languages" aria-hidden="true" />
    {{ isChinese ? 'English' : '中文' }}
  </a>
</template>

<style scoped>
.language-switcher {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin: 0 12px;
  padding: 6px 8px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  color: var(--vp-c-text-1);
  font-size: 13px;
  line-height: 20px;
  transition: color .2s, border-color .2s;
}
.language-switcher:hover {
  color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
}
.language-switcher:focus-visible {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 3px;
}
@media (max-width: 767px) {
  .language-switcher { margin: 0 4px; }
}
</style>
