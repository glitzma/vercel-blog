# 文章微调修复记录

日期：2026-10-15。已处理 30 篇优先文章及 4 篇 Tailwind 关联文章，共 34 篇、68 个中英文文件。保留原路径、permalink 和已有章节锚点。

## 修订清单

概念和措辞以局部调整为主；Vite 与 Mini-Vue 的运行失败涉及互相依赖的代码，因此替换了相应教学实现。

| 编号 | 文章 | 已处理内容 |
| --- | --- | --- |
| A01 | [vite可发布npm的虚拟插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/57.vite-publishable-plugin.md) | 修复 build 启用、env、导出扫描、监听和声明打包路径；明确 tree-shaking 条件。 |
| A02 | [vite自动导入api插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/43.vite-auto-import-plugin.md) | AST 与作用域识别自由变量，保留 Vue 模板/样式，避免重复声明。 |
| A03 | [Vite虚拟模块插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/50.vite-virtual-module.md) | 闭包保存配置，复用 loadEnv，补虚拟模块失效与环境文件监听。 |
| A04 | [写一个Mini-vue](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/27.write-a-mini-vue.md) | 保留响应式上下文，修复模板作用域、组件解析、文本与卸载。 |
| A05 | [Mini-vue template增强版](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/28.mini-vue-template-enhanced.md) | 修复状态快照、列表、事件表达式、静态属性与子组件切换。 |
| A06 | [nextTick](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/18.learn-node2.md) | 按场景解释事件循环，取消固定优先级，修正命令拼写。 |
| A07 | [HTTP协议详解](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/04.http.md) | 修正版本、连接、缓存/CORS、消息示例和代码围栏，标明旧记录。 |
| A08 | [BFC和IFC](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/03.bfc-and-ifc.md) | 区分 BFC/Flex/Grid，补 overflow:clip 例外与 flow-root。 |
| A09 | [null和undefined](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/11.typescript-null-undefined.md) | strict 与 strictNullChecks 改为包含关系，撤回无出处比例。 |
| A10 | [Tailwind结合 H5 rem/vw 的配置方案](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/27.tailwind-css-adaptation.md) | H5 间距改用独立键，补插件接入，修正 rem/JS、vw 与横屏边界。 |
| A11 | [H5 Tailwind preset](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/28.tailwind-preset.md) | H5 字号、间距、圆角使用独立 token；说明高级片段的合并要求。 |
| A12 | [通过nextjs学习seo](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/seo/85.seo-learning.md) | FID 更新为 INP，区分 OG/JSON-LD，收紧渲染方式与 SEO 的结论。 |
| A13 | [搜索引擎工作原理](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/seo/86.search-engine-principles.md) | 区分抓取与索引指令，修正分页 canonical、sitemap 和 CSR 前提。 |
| A14 | [React的hooks基础总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/11.react-hooks-summary.md) | 更正 DOM 提交/绘制/effect 时序，更新最新回调引用。 |
| A15 | [Zustand 实战总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/03.react-ecosystem/03.zustand-practice.md) | 固定 Zustand 5，使用 useShallow，修正 subscribe 签名和退订。 |
| A16 | [模拟 Vite 内置env](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/53.vite-simulate-env.md) | 限定 env 教学子集，复用 loadEnv，按 isProduction 判断，改用 AST。 |
| A17 | [Flex 布局的性能讲透](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/18.flex-layout-performance.md) | 撤回无来源性能表和普遍复杂度结论，保留影响因素与测量建议。 |
| A18 | [LayoutNG 是如何优化 Flex 的](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/24.layoutng-flex-optimization.md) | 撤回不可追溯百分比/倍数，区分引擎架构与实测结果。 |
| A19 | [min-content 的布局成本与优化边界](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/25.min-content-perf-risk.md) | 缩小标题，修正固有尺寸、缓存、flex-basis 与测量次数。 |
| A20 | [字体font-weight相关知识](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/05.font-weight.md) | 统一合法数值、相对字重、匹配规则、可变字体支持范围与 FOIT。 |
| A21 | [CSS 实现打字机效果](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/33.css-typewriter-effect.md) | 说明 width 重排不等于真正逐行打字，限定 ch 和换行场景。 |
| A22 | [Agent Skills是什么？跟MCP Workflow Command Prompt的关系。](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/60.agent-skills.md) | 说明 SKILL.md 与可选资源，补 MCP 的 tools/resources/prompts。 |
| A23 | [从cnn到transformer全解大模型](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/61.cnn-transformer.md) | 加入卷积序列模型反例，区分教学路线与历史，收紧规模推断。 |
| A24 | [100 万点地图怎么渲染？](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/71.render-1m-map-points.md) | 区分数据量、DOM 节点和绘制点，撤回必须 GPU 等绝对结论。 |
| A25 | [git基础配置](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/112.git-basic-config.md) | 更新 GitHub Free 私有仓库说明；SSH 示例改为 Ed25519 并标系统范围。 |
| A26 | [GitHub高级搜索技巧](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/01.github-search-tips.md) | 修正 forks、stars、pushed 语法示例和强调标记。 |
| A27 | [说明](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/02.chrome-plugin.md) | 标明历史 CommonJS 范围；修复异步渲染、npm cwd 和失败传播。 |
| A28 | [OpenLayers 从零到精通：2025-2026实战指南](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/74.openlayers-guide.md) | 固定 OpenLayers 10.11.0，统一导入、样式与容器高度。 |
| A29 | [Mapbox GL JS 从零到精通：2025-2026实战指南](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/75.mapbox-complete-guide.md) | 修正 #map 选择器；明确 Mapbox 版本与特性引入范围。 |
| A30 | [vite一体化虚拟模块插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/55.vite-unified-virtual-plugin.md) | 保护未加载模块，监听新增/删除，AST 扫描函数，明确显式导入与刷新。 |

额外同步：Tailwind 23–26 四篇增加 v3 JavaScript 配置 / v4 CSS 优先配置及 @config 的版本范围。

## 验证结果

- `npm run docs:validate-i18n`：199 对文章的行数、结构、代码、链接、图片、中英文锚点及英文正文检查通过。
- 原锚点回归：68 个修改文件的原有章节 ID 均保留。
- `npm run test:i18n`：3 个 Node 测试与 15 个 Python 测试通过。
- `npm run docs:build`：站点构建通过，保留既有大包提示和 mjs 高亮回退提示。
- Vite 5.4.21：四个虚拟模块插件通过开发导入和 staging 模式生产构建；公开变量隔离、未用 API 移除、监听 add/change/unlink 和清理通过。监听测试调用真实回调，未做浏览器 WebSocket 端到端测试。
- 自动导入：已有绑定、别名、局部变量、注释/字符串/属性、TS 断言、Vue script setup、template/style 与生产构建通过。
- 发布示例：TypeScript 5.9.3 + Rollup 构建、ESM/CJS 加载、消费方虚拟模块声明编译通过；npm pack --dry-run 确认运行及声明入口齐全，没有执行发布。
- Mini-Vue：linkedom 0.18.12 DOM 模拟测试通过挂载、计数、删除列表项、空状态、子组件保留/切换和静态样式；未完成真实浏览器验证。
- Tailwind 3.4.19：默认 p-4 和 H5 类同时生成；preset 保留默认字号与圆角。
- Zustand 5.0.15：useShallow 导出、subscribe 及退订通过。
- Node.js 22.14.0：CJS 的 I/O 示例输出 nextTick → promise → immediate → timeout。
- TypeScript：strictNullChecks 与 strict 的诊断对照通过，后者额外报告隐式 any。
- 历史脚手架：CommonJS 依赖可加载；两个 Metalsmith 模板均完成异步替换；子进程 cwd 与失败传播通过。
- OpenLayers 10.11.0：最小地图构建、CSS 和 CDN 所需 dist/ol.js 包路径通过。

## 验证边界

本次修复已知问题并撤回无证据的确定结论，不代表全站 165 篇其它栏目文章的所有代码都经过逐段执行。长计划中的其余深度复核与资源巡检仍保留。

Mapbox 在线 token/底图、地图真实交互、字体和动画的跨浏览器效果、历史脚手架完整远程模板流程及 Mini-Vue 真实浏览器交互尚未逐项端到端验证。测试依赖与夹具位于临时目录，没有改动站点 package.json 或 lockfile。
