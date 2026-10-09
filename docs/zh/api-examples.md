---
outline: deep
---

# 运行时 API 示例 {#runtime-api-examples}

本页展示 VitePress 提供的运行时 API 的用法。

通过 `useData()` 可以访问当前页面的站点、主题和页面数据，它可以用于 `.md` 和 `.vue` 文件：

```md
<script setup>
import { useData } from 'vitepress'

const { theme, page, frontmatter } = useData()
</script>

## 结果

### 主题数据
<pre>{{ theme }}</pre>

### 页面数据
<pre>{{ page }}</pre>

### 页面 Frontmatter
<pre>{{ frontmatter }}</pre>
```

<script setup>
import { useData } from 'vitepress'

const { site, theme, page, frontmatter } = useData()
</script>

## 结果 {#results}

### 主题数据 {#theme-data}
<pre>{{ theme }}</pre>

### 页面数据 {#page-data}
<pre>{{ page }}</pre>

### 页面 Frontmatter {#page-frontmatter}
<pre>{{ frontmatter }}</pre>

## 更多 {#more}

查看文档，了解 [运行时 API 的完整列表](https://vitepress.dev/reference/runtime-api#usedata)。
