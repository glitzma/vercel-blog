# Markdown 扩展示例 {#markdown-extension-examples}

本页展示 VitePress 内置的 Markdown 扩展功能。

## 语法高亮 {#syntax-highlighting}

VitePress 通过 [Shiki](https://github.com/shikijs/shiki) 提供语法高亮，并支持代码行高亮等扩展功能：

**输入**

````md
```js{4}
export default {
  data () {
    return {
      msg: 'Highlighted!'
    }
  }
}
```
````

**输出**

```js{4}
export default {
  data () {
    return {
      msg: 'Highlighted!'
    }
  }
}
```

## 自定义容器 {#custom-containers}

**输入**

```md
::: info
这是一条信息。
:::

::: tip
这是一条提示。
:::

::: warning
这是一条警告。
:::

::: danger
这是一条危险警告。
:::

::: details
这是一个详情区块。
:::
```

**输出**

::: info
这是一条信息。
:::

::: tip
这是一条提示。
:::

::: warning
这是一条警告。
:::

::: danger
这是一条危险警告。
:::

::: details
这是一个详情区块。
:::

## 更多 {#more}

查看文档，了解 [Markdown 扩展的完整列表](https://vitepress.dev/guide/markdown)。
