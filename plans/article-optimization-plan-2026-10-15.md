# 全站其它文章优化长计划

日期：2026-10-15。范围由用户确认：工作笔记以外的全站栏目。本文件保留初始审查与长计划；按后续授权，已完成 30 篇优先文章及 4 篇关联文章的中英文微调。实际修订和验证范围见 [修订记录](./article-fixes-2026-10-15.md)。

## 1. 范围、方法与结论边界

全站统计到 199 篇正文，工作笔记 34 篇沿用此前的审查与修订记录；本轮覆盖其它 14 个栏目、165 篇中文原文及其英文对应版本的后续工作安排，共 49,971 行中文 Markdown。首页和两个框架示例页不在正文统计内。

已完成的是全量目录、标题元数据、章节结构和风险表述初筛，以及重点片段阅读、官方资料核对和 6 个最小场景复现。扫描识别到 2,419 个代码块、608 处外部链接引用。没有逐一执行全部代码块，也没有逐一验证外部链接状态；HTML/Vue 形式的图片、无扩展名站内路由与实际页面效果仍需专门检查。普通 Markdown 本地图片/显式 .md 链接扫描没有发现缺失文件，这不代表全站资源全部正常。

已形成 30 篇优先队列：7 篇 P1、23 篇 P2。P1 中 6 篇有本地复现，HTTP 文有规范核对证据。P2 中既有确认问题，也有需要补来源或执行验证的候选。其余 135 篇保留逐篇复核任务，不能视为已证明正确，也不预设必须修改。

另有 22 篇旧资料没有文章标题 frontmatter；这属于元数据整理候选，本身不是 Markdown 语法错误。较新的 RAG 系列及已有修订的算法资料优先做回归，避免无依据地重复改写。

## 2. 栏目覆盖清单

| 栏目 | 篇数 | 优先队列 | 后续重点 |
| --- | ---: | ---: | --- |
| AI 与 RAG | 30 | 2 | 核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| CSS | 29 | 6 | 核对规范边界、兼容条件与可运行效果 |
| GIS | 8 | 3 | 固定库版本，验证坐标、数据来源和交互示例 |
| Git | 16 | 1 | 临时仓库复核命令，核对历史服务能力与重叠内容 |
| PostgreSQL | 2 | 0 | 补最小建表与数据，验证 SQL 输出及查询前提 |
| React | 17 | 2 | 区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| SEO | 2 | 2 | 以 Google/框架官方说明核对抓取、索引、指标与元数据 |
| Tailwind CSS | 6 | 2 | 标注 v3/v4 范围，验证生成 CSS 和 token 覆盖语义 |
| TypeScript | 14 | 1 | 固定编译器和 tsconfig，区分正确示例与预期错误 |
| Vite | 9 | 5 | 核对开发、构建、HMR 和虚拟模块生命周期 |
| Vue 3 | 10 | 2 | 验证响应式/生命周期示例，注明源码版本及教学省略项 |
| 技术文档 | 12 | 2 | 按平台和版本分段，核对旧命令与配置示例 |
| 算法 | 4 | 0 | 补输入边界与输出回归，保留已经修正的内容 |
| 实用技巧 | 6 | 2 | 核对搜索语法、工具版本、用途和链接可用性 |

优先级：P1 为运行失败或会明显误导实践的基础错误；P2 为概念边界、版本兼容、证据或关键示例问题；P3 为结构、可读性、练习和维护性改进。证据状态分别记录为“已复现”“资料核对”“已定位”“需补证据”“待验证”。后两类不当作已经证实的技术错误。

## 3. 已复现的六个场景

复现环境：Node.js v22.14.0、Vite 5.4.21、VitePress 1.6.4。这里只证明表中场景，不能替代完整页面和发布包验证。两个 Mini-Vue 场景直接执行了文中 setup/响应式片段，尚未运行完整 DOM 编译器。

| 编号 | 直接结果 | 说明 |
| --- | --- | --- |
| A01 | 构建配置的 plugins 中找不到设置 apply:serve 的示例插件 | 配置解析阶段已筛除，尚未运行完整示例包 |
| A02 | Identifier ref has already been declared | 已导入 ref 的源文件被再插入同名 import |
| A03 | TypeError: Cannot set properties of undefined (setting mode) | 通过本地 Vite resolveConfig 执行示例 configResolved |
| A04 | count：0 → 调用 inc → 0 | setup 对外返回了 state 展开的数值快照 |
| A05 | show：true → toggle → true；msg 在 inc 后仍为初始值 | setup 返回的布尔和字符串没有保持响应式读取 |
| A06 | I/O 回调中得到 nextTick → immediate → timeout | 这是固定优先级链的一个反例，不是另一条通用顺序 |

## 4. 三十篇优先队列与逐项验收

以下问题与证据保留为修复前记录；30 篇均已修订，验证与限制见修订记录。行号对应初次审查位置。

### A01 · P1 · 已复现 · [vite可发布npm的虚拟插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/57.vite-publishable-plugin.md:209)

问题：文章声称 dev/build 都支持，但插件设置 apply: serve；构建时插件会被筛除，注释称构建仍调用相关钩子也不成立。

计划：让插件按实际目标参与构建，核对 resolveId/load/buildStart；同步调整“可发布”的承诺。

验收：开发环境和生产构建都能导入两个虚拟模块；消费者项目能够构建；npm pack 检查导出入口和类型文件。不要实际发布。

依据：[Vite 插件启用条件](https://vite.dev/guide/api-plugin#conditional-application)。

### A02 · P1 · 已复现 · [vite自动导入api插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/43.vite-auto-import-plugin.md:83)

问题：按 code.includes 识别 API 并前置 import，会给已有 ref 导入再次声明 ref，生成语法错误；注释和普通字符串也可能误命中。

计划：最小修复先识别已有绑定；完整示例再使用语法解析，区分普通模块、Vue SFC 和带查询参数的模块 ID。

验收：已有导入、别名导入、局部同名变量、字符串和注释、Vue script/setup 均有清晰行为，生成代码通过语法检查。

依据：[Vite transform 钩子](https://vite.dev/guide/api-plugin)。

### A03 · P1 · 已复现 · [Vite虚拟模块插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/50.vite-virtual-module.md:108)

问题：configResolved 通过 this.mode/this.clientEnv 保存状态。在本仓库 Vite 5.4.21 的配置解析中，this 为 undefined，初始化直接报错。

计划：用插件工厂闭包保存 mode/env；补齐变量优先级与虚拟模块失效流程，删除未经验证的“生产级、完整可运行”承诺。

验收：固定目标版本后，配置解析、模块导入、构建、环境文件修改均通过；本地执行失败的场景先转为回归用例。

依据：[Vite 插件 API](https://vite.dev/guide/api-plugin)、[环境变量规则](https://vite.dev/guide/env-and-mode)。

### A04 · P1 · 已复现 · [写一个Mini-vue](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/27.write-a-mini-vue.md:431)

问题：Counter 的 setup 返回 { ...state, inc, dec }，把 count 复制为普通数值；调用 inc 后对外 count 仍为 0，不能支撑计数演示。

计划：保留响应式读取链路，修正 setup 到渲染上下文的桥接；把简化的响应式实现边界写清。

验收：在真实页面点击加减按钮会更新显示；连续更新不重复挂载；另列嵌套 effect、依赖清理等教学省略项。

### A05 · P1 · 已复现 · [Mini-vue template增强版](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/28.mini-vue-template-enhanced.md:460)

问题：setup 返回的 msg/show 是初始快照；调用 toggle/inc 后返回的 show/msg 不变。组件解析函数还需要验证是否递归处理子节点。

计划：先修复响应式上下文，再逐项核对 v-if、v-for、事件和子组件演示；明确教学版与 Vue 正式实现的差异。

验收：计数、切换子组件、删除列表项和事件修饰符都有实际浏览器演示；移除后不再残留旧组件。

### A06 · P1 · 已复现 · [nextTick](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/18.learn-node2.md:16)

问题：写成 nextTick > setTimeout > setImmediate > 异步 IO 的固定优先级；在本次 I/O 回调内实测为 nextTick → immediate → timeout。另有 npmlist、unistall 等命令拼写。

计划：改成事件循环阶段和具体调用场景；区分 CJS/ESM 与 Node 版本，逐条校正命令。

验收：主模块、I/O 回调、Promise/nextTick 三类示例给出适用条件；不再把一种运行结果写成通用顺序。

依据：[Node 事件循环](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick)。

### A07 · P1 · 资料核对 · [HTTP协议详解](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/04.http.md:2)

问题：仍称 HTTP/1.1 正在规范化，并把“一连接只处理一请求”当作 HTTP 通用特征；后文将 no-cache 当成不能缓存，还出现错误的 CORS 响应头名称。

计划：保留基础消息示例，按 HTTP 语义与具体版本分开表述；纠正 no-cache/no-store、CONNECT 和 CORS 名称。

验收：请求与响应示例语法正确；版本范围明确；缓存例子能区分存储、验证和直接复用。

依据：[HTTP 语义 RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)、[缓存 RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2.4)。

### A08 · P2 · 资料核对 · [BFC和IFC](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/03.bfc-and-ifc.md:37)

问题：把 flex/grid 容器直接列成创建 BFC 的条件，且 overflow 非 visible 的条件遗漏 clip 例外。

计划：区分块、Flex、Grid 格式化上下文，补充 flow-root；保留清除浮动示例并注明副作用。

验收：浮动包含、margin 折叠和 overflow:clip 反例能解释清楚。

依据：[MDN 格式化上下文](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)。

### A09 · P2 · 资料核对 · [null和undefined](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/11.typescript-null-undefined.md:42)

问题：把 strict:true 与仅开启 strictNullChecks:true 写成“等价”，忽略 strict 包含的其他检查；“99% 项目”缺乏出处。

计划：改成包含关系，注明示例所用编译配置，移除无法核对的比例。

验收：两个配置的最小对照示例展示差异，故意报错的代码有预期诊断。

依据：[TypeScript strict](https://www.typescriptlang.org/tsconfig/strict)。

### A10 · P2 · 已定位 · [Tailwind结合 H5 rem/vw 的配置方案](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/27.tailwind-css-adaptation.md:77)

问题：声称不覆盖默认 spacing，但在 extend.spacing 中重新定义 4、8 等现有键，会改变已有工具类语义。

计划：使用独立的 H5 token 名称，或明确声明这是有意覆盖；区分 Tailwind v3 与 v4 的接入方式。

验收：编译默认与自定义 p-4 等类进行对照，现有页面的间距变化可以解释。

依据：[Tailwind v3 主题扩展](https://v3.tailwindcss.com/docs/theme#extending-the-default-theme)、[v4 升级](https://tailwindcss.com/docs/upgrade-guide)。

### A11 · P2 · 已定位 · [H5 Tailwind preset](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/28.tailwind-preset.md:78)

问题：preset 再次覆盖既有 spacing、fontSize、borderRadius 等键，却称“不覆盖 Tailwind 默认值”；未标明适用版本。

计划：统一 preset 的命名与覆盖策略，提供明确版本下的导入和编译方式。

验收：默认类与 H5 类的生成 CSS 有可复查对照；示例不依赖未列出的配置。

依据：[Tailwind v3 主题](https://v3.tailwindcss.com/docs/theme)、[v4 升级](https://tailwindcss.com/docs/upgrade-guide)。

### A12 · P2 · 资料核对 · [通过nextjs学习seo](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/seo/85.seo-learning.md:185)

问题：Core Web Vitals 表仍使用 FID；把 Open Graph 与用于搜索结构化数据的 JSON-LD 混列，SSR/SSG 的 SEO 优劣也写得过于绝对。

计划：改成 LCP/INP/CLS；分别说明社交分享元数据、搜索结构化数据和渲染方式的作用。

验收：指标名称与 Google 文档一致；页面示例区分 metadata、JSON-LD 和 Open Graph。

依据：[Google Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)。

### A13 · P2 · 资料核对 · [搜索引擎工作原理](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/seo/86.search-engine-principles.md:30)

问题：robots.txt、meta、X-Robots-Tag 被写成固定覆盖顺序；分页 canonical 可指向第一页的建议会误导不同内容页面的处理。

计划：区分抓取许可与索引指令，解释规则冲突；分页按独立内容采用合适的自引用 canonical。

验收：noindex 页面可以被抓取以读取指令；分页示例符合 Google 指南，不把第 2 页当作第 1 页副本。

依据：[Robots 指令](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)、[分页指南](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)。

### A14 · P2 · 资料核对 · [React的hooks基础总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/11.react-hooks-summary.md:84)

问题：useLayoutEffect 被写成 DOM 渲染前执行，混淆 DOM 提交与浏览器绘制；单次 useRef(fn) 示例也没有展示更新 current 的完整过程。

计划：改成提交后、绘制前的时序，明确 effect 清理；完善需要读取最新回调的示例。

验收：用 DOM 测量和变更依赖两个例子验证，能解释开发 StrictMode 的额外 setup/cleanup。

依据：[React useLayoutEffect](https://react.dev/reference/react/useLayoutEffect)、[useEffect](https://react.dev/reference/react/useEffect)。

### A15 · P2 · 资料核对 · [Zustand 实战总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/03.react-ecosystem/03.zustand-practice.md:83)

问题：安装命令未锁版本，但示例沿用 create 返回 hook 的第二个 shallow 参数；这属于 v4 写法，v5 的 create 不支持该自定义比较参数。

计划：注明 v4 范围，或提供 v5 的 useShallow/createWithEqualityFn 方案。

验收：固定版本下组件可以运行；对象选择器输出稳定，状态更新不会造成异常循环。

依据：[Zustand v5 迁移](https://github.com/pmndrs/zustand/blob/main/docs/reference/migrations/migrating-to-v5.md)。

### A16 · P2 · 资料核对 · [模拟 Vite 内置env](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/53.vite-simulate-env.md:187)

问题：用 mode 推导 DEV/PROD，并宣称完整模拟内置 env；遗漏已有进程变量优先级和变量展开，把自定义 HMR 与 Vite 内置行为混在一起。

计划：改成教学子集；按目标版本核对 NODE_ENV 与 mode，说明 .env 更改后的重启要求；代码替换处理字符串和注释。

验收：测试自定义 mode、NODE_ENV、已有变量和字符串字面量，分别列出与内置行为的差别。

依据：[Vite env 与 mode](https://vite.dev/guide/env-and-mode)。

### A17 · P2 · 需补证据 · [Flex 布局的性能讲透](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/18.flex-layout-performance.md:311)

问题：给出 Block/Flex/Grid 的毫秒对比与复杂度结论，但没有对应实验代码、浏览器版本、机器和统计方法。

计划：保留可验证的性能影响因素；数字补出处或改成示意，避免按布局名称直接排名。

验收：保留一个可运行基准，区分布局、绘制与总耗时，多次采样并记录条件。

### A18 · P2 · 需补证据 · [LayoutNG 是如何优化 Flex 的](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/24.layoutng-flex-optimization.md:289)

问题：将 20%～40%、极端 2x、复杂度变化归于 Chromium 测试，但文中没有测试出处。

计划：逐条补官方材料，无法追溯的数字撤回；区分架构描述、算法规范与实测结果。

验收：每个保留的数字都对应原始测试或自建复现；不把单个案例推广为普遍增益。

### A19 · P2 · 需补证据 · [min-content 仍然是 Flex和Grid 最大的性能风险](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/25.min-content-perf-risk.md:337)

问题：8/25/40ms 表没有实验信息，“最大性能风险”“改变 1px 必须重算”等结论缺少条件。

计划：缩小标题和结论范围，核对 intrinsic size、自动最小尺寸、缓存与 flex-basis 的关系。

验收：固定宽度、自动基准和 min-content 的对照可复现，保留必要的 min-width/内容条件。

### A20 · P2 · 已定位 · [字体font-weight相关知识](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/05.font-weight.md:32)

问题：前面只列 100～900 且 100 步进，后面又给可变字体 537，结尾仍把范围压回 100～900，章节口径不一致。

计划：统一合法数值、字体实际支持范围与字重回退的区别，说明示例字体。

验收：默认字体与可变字体各有一个例子，解释设置值为何不一定对应独立字形。

### A21 · P2 · 已定位 · [CSS 实现打字机效果](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/33.css-typewriter-effect.md:71)

问题：多行方案说明称“控制高度逐步展开”，实际关键帧只改变 width；文字重排不等于逐行打字。

计划：让说明与实际实现一致，分别列单行裁切和多行逐行显示的限制。

验收：浏览器中验证换行与光标，补 reduced-motion 处理，避免把文本重新排版当作逐字输出。

### A22 · P2 · 资料核对 · [Agent Skills是什么？跟MCP Workflow Command Prompt的关系。](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/60.agent-skills.md:189)

问题：把 Skill 描述成固定三部分，并把 MCP 近似当成工具集合；可选资源和协议能力边界交代不足。

计划：注明 Skill 的最小必需文件及可选脚本/资料；分别介绍 MCP 的 tools、resources、prompts，不把概念画成必经层级。

验收：一个最小 Skill 与一个无脚本例子可以解释；概念图明确协议、文件约定、编排模式分别属于什么。

依据：[Agent Skills 规范](https://agentskills.io/specification)、[MCP 服务端概念](https://modelcontextprotocol.io/docs/learn/server-concepts)。

### A23 · P2 · 资料核对 · [从cnn到transformer全解大模型](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/61.cnn-transformer.md:61)

问题：将“语言是序列”作为 CNN 不适合语言的理由过于绝对；全文线性进化路线容易被读作技术出现顺序。

计划：加入一维卷积和卷积序列模型反例，区分教学路线与历史时间线；规模、能力与未公开模型信息逐条加来源。

验收：读者能解释不同架构的取舍；对未知架构/参数不填猜测值。

依据：[卷积序列学习原始论文](https://arxiv.org/abs/1705.03122)。

### A24 · P2 · 已定位 · [100 万点地图怎么渲染？](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/71.render-1m-map-points.md:27)

问题：把 DOM、SVG、Canvas 一并等同“100 万节点直接崩”，混淆 DOM 节点数、绘制点数与数据条数；“必须 GPU”缺少条件。

计划：按数据加载、可视点数量、绘制方式和交互需求说明选择，补运行环境和性能预算。

验收：同一数据集比较抽样、聚合、分块与渲染方式；报告可见点数、内存和帧时间。

### A25 · P2 · 资料核对 · [git基础配置](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/112.git-basic-config.md:56)

问题：仍声称 GitHub 免费服务只能创建公开仓库，已不符合当前服务能力。

计划：更新托管能力的表述，把自建服务器的理由改成实际需求；SSH 部分补系统与密钥示例版本。

验收：平台功能说明有核对日期与官方来源，命令在临时练习目录解释。

依据：[GitHub 账户能力](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)。

### A26 · P2 · 资料核对 · [GitHub高级搜索技巧](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/01.github-search-tips.md:51)

问题：按 fork 数筛仓库的示例写成 fork:>100，正确的数量限定词是 forks。

计划：改正限定词并拆开括号式缩写，区分仓库搜索和代码搜索；修复未闭合强调标记。

验收：每条示例对应明确搜索类型，官方语法能核对。

依据：[GitHub 仓库搜索](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)。

### A27 · P2 · 待验证 · [说明](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/02.chrome-plugin.md:6)

问题：正文主要是 Tampermonkey 用户脚本脚手架，却使用 Chrome 插件这一大标题；依赖安装未锁版本，历史 CommonJS 示例需验证。

计划：明确用户脚本与浏览器扩展的区别，固定旧教程依赖，按目标版本运行最小项目。

验收：从空目录按文中命令可完成初始化；不能复现的历史流程有明确版本说明。

### A28 · P2 · 待验证 · [OpenLayers 从零到精通：2025-2026实战指南](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/74.openlayers-guide.md:40)

问题：以 2025–2026“最新版本特点”介绍，但 CDN URL 未固定版本，示例与版本对应关系需要复核。

计划：固定验证版本与依赖，逐一核对导入、投影、瓦片和点击交互；避免用年份替代版本证据。

验收：一个固定版本的完整入口能运行，关键 API 连接到该版本官方文档。

### A29 · P2 · 待验证 · [Mapbox GL JS 从零到精通：2025-2026实战指南](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/75.mapbox-complete-guide.md:47)

问题：把多项能力统列成当前 v3 新特性，需区分首次引入版本与示例使用版本；尚未执行地图集成示例。

计划：逐条核对发布说明、样式与 token 前提，统一依赖版本与示例。

验收：地图、聚合和三维示例的前置条件明确，运行结果与固定版本一致。

### A30 · P2 · 待验证 · [vite一体化虚拟模块插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/55.vite-unified-virtual-plugin.md:91)

问题：HMR 直接使用 getModuleById 的结果；虚拟模块未被导入、API 文件新增/删除等情况尚未验证，不能把完整可靠作为既定结论。

计划：补空模块分支，核对新增/删除监听和导出扫描边界，明确支持的文件语法与构建阶段。

验收：未导入模块时更改文件不会报错；新增、删除、重名导出和生产构建的行为都有结果记录。

## 5. 分阶段执行安排

### 阶段 0：建立可追踪基线（本轮已完成）

- [x] 统计 165 篇其它栏目文章，保留 34 篇工作笔记的既有检查范围。
- [x] 初筛标题、章节、代码块、风险表述和引用；登记 22 篇标题元数据候选。
- [x] 对 A01—A06 做最小场景复现；对部分结论核对官方文档。
- [x] 建立 30 篇优先队列与完整 165 篇逐篇清单。
- [x] 完成 30 篇优先文章及 4 篇关联文章的中英文修订；未把全站深度复核标为完成。

产出：本计划、优先顺序、复现环境与未覆盖事项。

### 阶段 1：先修七篇 P1，分两个小批次

第一批处理 A01、A02、A03：可发布插件、自动导入、虚拟 env。每篇先保留一个失败输入，再修最小实现；插件必须分别验证开发与构建，不能用“开发能跑”代替构建成功。

第二批处理 A04、A05、A06、A07：两个 Mini-Vue、Node 事件循环和 HTTP。先把演示恢复到文章承诺的基本效果，再改结论。教学实现不追求补成完整框架。

产出：7 对中英文修订稿、各自的复现与验证记录。完成条件：上表中的直接失败已消失，新增版本前提写入正文，原章节链接仍有效。

### 阶段 2：纠正基础概念与读者容易记错的结论

- [ ] CSS：A08 的 BFC/Flex/Grid 边界；A20 的字重范围与字体支持。
- [ ] TypeScript：A09 的 strict 包含关系；连带核对空值、可选属性和断言示例。
- [ ] React：A14 的 DOM 提交/绘制/effect 时序；在其它 Hooks 文章中检索同类表述，避免只修一篇。
- [ ] SEO：A12、A13 的 INP、抓取与索引控制、分页 canonical；同一结论不在多处保留不同版本。

产出：带最小反例的术语说明与互链。完成条件：同一概念跨文章口径一致，建议与标准要求分别说明。

### 阶段 3：给工具教程建立明确版本边界

- [ ] Vite 9 篇：区分公开插件 API、当前实现和教学伪代码；对照 A16、A30；开发与构建使用同一套已验证依赖。
- [ ] Tailwind 6 篇：保留有价值的 v3 示例，标清范围；补充 v4 的配置加载和主题方式；先处理 A10/A11 的 token 冲突。
- [ ] Zustand：按 A15 固定版本，改掉未锁版本安装与旧 API 混用。
- [ ] GIS：A28/A29 先固定 OpenLayers/Mapbox 版本，按发布说明核对“新特性”，不要靠标题里的年份证明最新。
- [ ] React 原理系列 8 篇：为内部变量、调度和 Hooks 链表说明注明目标版本或源码定位；不能把简化伪代码写成所有版本均如此。

产出：每组一个版本与验证环境说明，必要的迁移对照表。完成条件：按指定版本从空目录操作能复现；旧版本内容不因更新而失去上下文。

### 阶段 4：重做性能论证，不先改成另一组结论

范围：A17、A18、A19，以及 CSS 动画性能、布局比较和 GIS 百万点文中的同类表述。

- [ ] 每个性能数字登记来源、浏览器、设备、数据规模和测量项目。
- [ ] 原始实验不可追溯时，删除确定数值或明确为示意；不填补估算出来的“真实数据”。
- [ ] 为布局选三类代表案例：简单列表、嵌套布局、长文本自动尺寸；记录内容和 CSS 条件。
- [ ] 区分首次布局、重复布局、绘制、合成、交互响应与总体时间；保存 trace 和采样方法。
- [ ] GPU、contain、will-change、flex-basis 等建议写清触发条件与代价，不按属性名称断言普遍更快。

产出：少量可运行对照例子及有边界的结论。完成条件：保留数字都能复查，没有测试证据的比较只表述为待测假设。

### 阶段 5：补齐示例的输入、依赖和预期结果

- [ ] TypeScript 14 篇：按独立示例块建立编译环境，记录 tsconfig；正常示例应通过，错误示例应出现指定错误，不能把示范错误统一当成缺陷。
- [ ] Vue 3 的响应式与编译器：基础对象、数组长度、Map/Set、新旧值与嵌套副作用分别挑典型场景；写清省略项。
- [ ] React 实战：验证状态连续更新、订阅清理、闭包与最新值、异步请求取消/失败分支；公开 API 与内部原理分开。
- [ ] GIS 8 篇：统一坐标系、最小数据集、样式和资源前提；地图显示、点击、聚合、坐标转换各有最小闭环。
- [ ] PostgreSQL 2 篇：补对应 DDL 和少量数据，验证 DISTINCT ON、递归 CTE、JSONB、窗口函数；相同时间的排序与递归环等边界按示例需要补充。
- [ ] CSS 演示：优先验证 A21 的多行效果，再回归省略号、暗色模式、图片预留比例、H5 适配。

产出：能从文中复制运行的最小例子；只为复杂行为保留有意义的回归，纯文字与格式调整不新增机械测试。

### 阶段 6：整理 AI 概念与学习路径

- [ ] A22：用官方约定校准 Skill/MCP；区分文件约定、协议能力与应用编排。
- [ ] A23：区分架构取舍、教学路线与历史；对规模、性能和“理解机制”补可追溯来源。
- [ ] 其余 AI 概念文：检查模型能力的绝对化表述，注明解释性比喻与已知机制的区别。
- [ ] 新 RAG 系列 20 课、配套资料包和学习计划：以片段 A—H、十题标准、来源与前后课互链一致性为主；抽查未知题的评估口径，不因本次整理而扩写成偏离零基础目标的大型代码教程。
- [ ] 保留读者最终能完成的练习和交付物；推荐资源记录核对日期。

产出：概念文的证据补充与清晰互链，新课程的回归记录。完成条件：能力边界清楚，案例内部规则一致，资料外问题不会被练习答案擅自补全。

### 阶段 7：复核旧技术资料、Git、算法与工具教程

- [ ] 技术文档 12 篇：Nginx、Shell、Linux 标注发行版和运行环境；HTTP/Node 先沿用阶段 1 的修订，再核对 npm/package.json、YAML 与 Markdown 示例。
- [ ] Nginx 配置在隔离样例中做语法检查；Shell 命令区分 Bash/zsh 和可执行命令/终端输出，不能把说明文字放成可执行行。
- [ ] Git 16 篇与旧 Git 使用手册：先修 A25；对 reset、rebase、force push 等行为用临时仓库演示结果；明确不同命令影响的工作区、暂存区和提交历史。
- [ ] 算法 4 篇：本轮没有直接认定其需要重写。字符串篇已有独立修订记录；复核空输入、重复值、边界下标、稳定性、复杂度前提与图例/代码一致性。
- [ ] 实用技巧 6 篇：先修 A26，验证 A27；搜索技巧、快捷键、组件库与收藏网站记录适用平台和最后核对日期。

产出：保留历史信息但不冒充现行默认行为的旧资料；关键命令与算法有对应输入输出。

### 阶段 8：处理结构、元数据、引用和重复内容

- [ ] 逐项检查 22 篇无标题 frontmatter 的资料实际页面标题，再决定补齐 title/description；缺元数据不等于页面一定显示错误。
- [ ] 将文件名式标题改成读者能理解的名称；保留原文件路径、permalink 与已有章节 ID。
- [ ] 长文只在内容确实独立时拆分，并保留旧入口或链接；Git/Node/CSS 重叠内容先加互链和范围说明，不直接删除。
- [ ] 608 处外部链接引用先去重后检查；超时、403、429 与真正 404 分开记录，人工复核后再替换。
- [ ] 检查原始 HTML/Vue 图片引用、外链图片、锚点和无扩展名内部路由；补充有效 alt 和图例说明。
- [ ] 标明转载来源、原作者和适用年代，优先引用技术规范、官方文档、源码或论文。
- [ ] 统一术语与夸张标签，删掉无实质信息的“生产级/最强/必然”等承诺，保留有价值的个人经验。

产出：可读标题、来源清楚的引用和能导航的知识结构。完成条件：不存在为了整齐而破坏旧链接或丢失历史上下文的改动。

### 阶段 9：双语与最终验收

- [ ] 每次正文修改同时维护英文对应文件；人工翻译并保留相同显式章节 ID。
- [ ] 代码、链接、图片和 Markdown 结构保持成对一致；不以自动翻译覆盖已经修订的例子。
- [ ] 每个小批次检查改动差异和受影响例子；涉及行为变更时复测失败场景。
- [ ] 运行 npm run docs:validate-i18n、npm run test:i18n 和 npm run docs:build；构建按批次收尾，避免无新改动时重复全量运行。
- [ ] 抽查中英文切换、旧锚点、手机布局及动态演示。
- [ ] 在逐篇台账中标记“已核验无须修改”或“已修订并验证”，记录目标版本、来源和剩余限制。

最终交付：按小批次可审阅的中英文修订、必要的示例验证和完成台账。完成标准是 165 篇都有审查结论，而不是 165 篇都产生文本改动。

建议顺序：阶段 0 → 阶段 1 → 阶段 2；之后按 Vite/Tailwind、Vue/React、CSS、GIS/SQL、旧资料分别推进阶段 3—8。阶段 9 的双语与受影响验证贯穿每个批次，最后再做全量收尾。每批一般 3—8 篇；长插件或编译器文章可单独成批。第一批完成后按实际验证成本排后续日期，本计划不预设未经测量的总工时。

## 6. 第一批可以直接开始的具体任务

- [ ] A03：将 virtual env 插件状态改为闭包；先复测初始化异常。
- [ ] A01：纠正 serve-only 与 build 支持的矛盾，验证实际消费者构建。
- [ ] A02：先消除重复导入，再明确语法扫描的支持范围。
- [ ] 三篇都写清验证版本，配对更新英文并保留原章节链接。
- [ ] 完成针对性例子验证，再运行双语校验与一次文档构建。
- [ ] 更新本计划中的状态，保留无法覆盖的 HMR、SFC 或导出边界。

这批聚焦插件生命周期，方便共用最小 Vite 例子。下一批再处理两个 Mini-Vue，避免把两套复杂示例同时改乱。

## 7. 完整逐篇台账：165 篇

下列条目全都已纳入目录、结构和风险词初筛。有 A 编号的文章见上面的证据及验收；其它文章仍需按指定阶段逐节核验。阶段 8、9 的元数据/引用/双语检查对所有文章适用。表中“待复核”不表示已经确认有错误。

### AI 与 RAG（30 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [Agent Skills是什么？跟MCP Workflow Command Prompt的关系。](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/60.agent-skills.md) | P2 · A22 · 已修订，验证见记录 | 阶段 6：注明 Skill 的最小必需文件及可选脚本/资料；分别介绍 MCP 的 tools、resources、prompts，不把概念画成必经层级。 |
| [从cnn到transformer全解大模型](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/61.cnn-transformer.md) | P2 · A23 · 已修订，验证见记录 | 阶段 6：加入一维卷积和卷积序列模型反例，区分教学路线与历史时间线；规模、能力与未公开模型信息逐条加来源。 |
| [什么是 Encoder 和 Decoder 结构](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/62.encoder-decoder.md) | P3 · 初筛后待复核 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [GPT 为什么能“看懂”问题](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/63.gpt-understands-language.md) | P3 · 初筛后待复核 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [GPT 是怎么学会数学的](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/64.gpt-learns-math.md) | P3 · 初筛后待复核 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [RAG 和 Agent的区别](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/65.rag-vs-agent.md) | P3 · 初筛后待复核 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [context engineering 技术介绍](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/66.context-engineering.md) | P3 · 初筛后待复核 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [HarnessEngineering 驾驭工程的概念](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/67.harness-engineering.md) | P3 · 初筛后待复核 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [RAG 学习计划：零基础 4 周入门](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/68.rag-learning-plan.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 01 课：大模型能做什么，为什么也会答错](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/01.llm-capabilities.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 02 课：Prompt 和 Context，怎样让模型理解你的要求](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/02.prompt-and-context.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 03 课：为什么大模型需要外部资料](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/03.external-knowledge.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 04 课：用一次图书馆问答理解 RAG](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/04.rag-workflow.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 05 课：RAG、模型训练和 Agent 有什么关系](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/05.rag-training-and-agents.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 06 课：怎样准备一份适合问答的资料](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/06.prepare-documents.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 07 课：文档切分，一篇文章应该怎样拆](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/07.chunking.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 08 课：Embedding，文字为什么能变成数字](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/08.embeddings.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 09 课：关键词搜索与语义搜索](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/09.keyword-and-semantic-search.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 10 课：索引、Top-k 和来源信息](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/10.index-top-k-and-sources.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 11 课：怎样提出适合知识库回答的问题](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/11.ask-answerable-questions.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 12 课：先检查资料是否找对，再看答案](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/12.check-retrieved-evidence.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 13 课：写一份依据资料回答的提示词](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/13.evidence-based-prompts.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 14 课：资料不足或互相矛盾时怎么办](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/14.missing-and-conflicting-evidence.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 15 课：完成一次可复查的 RAG 实验](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/15.auditable-rag-experiment.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 16 课：为 RAG 准备一套测试题](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/16.build-a-test-set.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 17 课：怎样判断检索效果](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/17.evaluate-retrieval.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 18 课：怎样判断生成答案的质量](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/18.evaluate-answers.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 19 课：混合检索与重排为什么有用](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/19.hybrid-search-and-reranking.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [第 20 课：从失败案例出发改进 RAG](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/20.improve-from-failures.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |
| [RAG 入门配套资料包：资料、测试题与记录模板](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/AI-related/rag-course/materials.md) | P3 · 保持结构，做一致性回归 | 阶段 6：核对概念边界、来源与例子；新 RAG 系列以一致性回归为主 |

### CSS（29 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [CSS教程和技巧收藏](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/00.css-tutorials-and-tips.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [css块元素和行内元素](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/01.css-block-inline.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [盒子模型](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/02.css-box-model.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [BFC和IFC](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/03.bfc-and-ifc.md) | P2 · A08 · 已修订，验证见记录 | 阶段 2、4：区分块、Flex、Grid 格式化上下文，补充 flow-root；保留清除浮动示例并注明副作用。 |
| [字体font-weight相关知识](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/05.font-weight.md) | P2 · A20 · 已修订，验证见记录 | 阶段 2、4：统一合法数值、字体实际支持范围与字重回退的区别，说明示例字体。 |
| [CSS-function汇总](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/06.css-functions-overview.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [CSS3之has函数的使用](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/07.css3-has-function-usage.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [CSS3之transition过渡](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/08.css3-transition.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [CSS3之animation动画](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/09.css3-animation.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [css动画性能优化](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/10.css3-animation-performance.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [flex布局语法](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/15.flex-layout-syntax.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [flex布局案例](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/16.flex-layout-examples.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [Grid布局语法](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/17.grid-layout-syntax.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [Flex 布局的性能讲透](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/18.flex-layout-performance.md) | P2 · A17 · 已修订，验证见记录 | 阶段 2、4：保留可验证的性能影响因素；数字补出处或改成示意，避免按布局名称直接排名。 |
| [flex布局和grid布局的区别](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/19.flex-vs-grid-layout.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [「布局技巧」图片未加载前自动撑开元素高度](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/20.img-auto-expand-height.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [shadcn/ui学习笔记](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/21.shad-ui-learning.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [shadcn/ui CVA 是什么](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/22.shad-ui-cva.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [shadcn/ui radix ui 讲解](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/23.shad-ui-radix-ui.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [LayoutNG 是如何优化 Flex 的](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/24.layoutng-flex-optimization.md) | P2 · A18 · 已修订，验证见记录 | 阶段 2、4：逐条补官方材料，无法追溯的数字撤回；区分架构描述、算法规范与实测结果。 |
| [min-content 仍然是 Flex和Grid 最大的性能风险](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/25.min-content-perf-risk.md) | P2 · A19 · 已修订，验证见记录 | 阶段 2、4：缩小标题和结论范围，核对 intrinsic size、自动最小尺寸、缓存与 flex-basis 的关系。 |
| [h5适配方案](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/30.h5-adaptation-solution.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [前端1px的几种实现方案](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/31.frontend-1px-solutions.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [文字在一行或多行时超出显示省略号](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/32.text-overflow-ellipsis.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [CSS 实现打字机效果](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/33.css-typewriter-effect.md) | P2 · A21 · 已修订，验证见记录 | 阶段 2、4：让说明与实际实现一致，分别列单行裁切和多行逐行显示的限制。 |
| [水平垂直居中的几种方式-案例](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/40.centering-methods-examples.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [如何根据系统主题自动响应CSS深色模式](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/45.css-auto-dark-mode.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [工作中遇到的css问题记录](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/46.css-summary.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |
| [今天总结一下用到的css吧](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/CSS/47.learn-css.md) | P3 · 初筛后待复核 | 阶段 2、4：核对规范边界、兼容条件与可运行效果 |

### GIS（8 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [GIS 基础三件套](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/69.gis-fundamentals.md) | P3 · 初筛后待复核 | 阶段 3、5：固定库版本，验证坐标、数据来源和交互示例 |
| [GIS必会知识点](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/70.gis-key-concepts.md) | P3 · 初筛后待复核 | 阶段 3、5：固定库版本，验证坐标、数据来源和交互示例 |
| [100 万点地图怎么渲染？](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/71.render-1m-map-points.md) | P2 · A24 · 已修订，验证见记录 | 阶段 3、5：按数据加载、可视点数量、绘制方式和交互需求说明选择，补运行环境和性能预算。 |
| [GIS空间索引的实现](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/72.gis-spatial-index.md) | P3 · 初筛后待复核 | 阶段 3、5：固定库版本，验证坐标、数据来源和交互示例 |
| [Cesium 从入门到精通：实战指南](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/73.cesium-practical-guide.md) | P3 · 初筛后待复核 | 阶段 3、5：固定库版本，验证坐标、数据来源和交互示例 |
| [OpenLayers 从零到精通：2025-2026实战指南](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/74.openlayers-guide.md) | P2 · A28 · 已修订，验证见记录 | 阶段 3、5：固定验证版本与依赖，逐一核对导入、投影、瓦片和点击交互；避免用年份替代版本证据。 |
| [Mapbox GL JS 从零到精通：2025-2026实战指南](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/75.mapbox-complete-guide.md) | P2 · A29 · 已修订，验证见记录 | 阶段 3、5：逐条核对发布说明、样式与 token 前提，统一依赖版本与示例。 |
| [Cesium、OpenLayers 和 Mapbox GL JS 的关系、区别](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/gis/76.cesium-ol-mapbox-compare.md) | P3 · 初筛后待复核 | 阶段 3、5：固定库版本，验证坐标、数据来源和交互示例 |

### Git（16 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [常用Git命令清单](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/10.manual/00.git-common-commands.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git变基合并](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/10.manual/03.git-rebase-merge.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git命令思维导图](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/10.manual/06.git-commands-mindmap.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git基础与命令](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/10.git-basics-commands.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git工具-重写历史](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/100.git-rewrite-history.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git工具-重置揭密](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/110.git-reset-demystified.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [git基础配置](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/112.git-basic-config.md) | P2 · A25 · 已修订，验证见记录 | 阶段 7：更新托管能力的表述，把自建服务器的理由改成实际需求；SSH 部分补系统与密钥示例版本。 |
| [创建git服务器](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/113.git-server.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git分支-分支基本操作](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/20.git-branch-basics.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git分支的新建与合并-分支操作](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/30.git-branch-create-merge.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git分支管理-查看分支](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/40.git-branch-management.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git分支开发工作流](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/50.git-branching-workflows.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git-远程仓库管理](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/60.git-remote-management.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git分支-变基](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/70.git-branch-rebase.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git工具-查看修订版本](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/80.git-revision-selection.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |
| [Git工具-交互式暂存](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/git/20.docs-notes/90.git-interactive-staging.md) | P3 · 初筛后待复核 | 阶段 7：临时仓库复核命令，核对历史服务能力与重叠内容 |

### PostgreSQL（2 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [Postgres基础知识学习](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/postgres/83.postgres-basics.md) | P3 · 初筛后待复核 | 阶段 5：补最小建表与数据，验证 SQL 输出及查询前提 |
| [Postgres查询相关知识](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/postgres/84.postgres-query.md) | P3 · 初筛后待复核 | 阶段 5：补最小建表与数据，验证 SQL 输出及查询前提 |

### React（17 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [React重要阶段的特性](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/05.react-basics.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [Vue3 → React18对照学习表](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/06.vue-to-react-comparison.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [class和hooks选哪个好](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/07.class-vs-hooks.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [四个常用Hook作用和区别](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/10.hooks-overview.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [React的hooks基础总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/11.react-hooks-summary.md) | P2 · A14 · 已修订，验证见记录 | 阶段 2、3、5：改成提交后、绘制前的时序，明确 effect 清理；完善需要读取最新回调的示例。 |
| [React的hooks实战应用总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/01.react-basics/12.react-hooks-practice.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [Vue3 effect vs react hooks](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/08.vue3-effect-vs-react-hooks.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [Fiber是什么](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/09.what-is-fiber.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [renderWithHooks是怎么挂到Fiber](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/10.renderWithHooks-on-fiber.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [mount/update为什么能切换](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/11.hooks-dispatcher-switch.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [React 更新系统的“回路闭合点”](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/12.setstate-back-to-fiber.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [为什么hooks不能写在条件里](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/13.why-hooks-no-conditions.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [为啥hooks要用全局变量（而不是参数传递）](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/14.why-hooks-global-vars.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [React的hooks需要知道的问题](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/02.react-principles/15.react-hooks-faq.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [react全家桶概览](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/03.react-ecosystem/01.react-ecosystem-overview.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [redux介绍](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/03.react-ecosystem/02.redux-usage.md) | P3 · 初筛后待复核 | 阶段 2、3、5：区分公开 API、源码伪代码与目标版本，复核 effect 和状态示例 |
| [Zustand 实战总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/react/03.react-ecosystem/03.zustand-practice.md) | P2 · A15 · 已修订，验证见记录 | 阶段 2、3、5：注明 v4 范围，或提供 v5 的 useShallow/createWithEqualityFn 方案。 |

### SEO（2 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [通过nextjs学习seo](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/seo/85.seo-learning.md) | P2 · A12 · 已修订，验证见记录 | 阶段 2：改成 LCP/INP/CLS；分别说明社交分享元数据、搜索结构化数据和渲染方式的作用。 |
| [搜索引擎工作原理](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/seo/86.search-engine-principles.md) | P2 · A13 · 已修订，验证见记录 | 阶段 2：区分抓取许可与索引指令，解释规则冲突；分页按独立内容采用合适的自引用 canonical。 |

### Tailwind CSS（6 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [Tailwind CSS基础知识](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/23.tailwind-css-basics.md) | P3 · 初筛后待复核 | 阶段 3：标注 v3/v4 范围，验证生成 CSS 和 token 覆盖语义 |
| [Tailwind CSS Config](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/24.tailwind-css-config.md) | P3 · 初筛后待复核 | 阶段 3：标注 v3/v4 范围，验证生成 CSS 和 token 覆盖语义 |
| [Tailwind 插件机制](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/25.tailwind-css-plugins.md) | P3 · 初筛后待复核 | 阶段 3：标注 v3/v4 范围，验证生成 CSS 和 token 覆盖语义 |
| [Tailwind 底层生成机制 & purge 原理](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/26.tailwind-generation-purge.md) | P3 · 初筛后待复核 | 阶段 3：标注 v3/v4 范围，验证生成 CSS 和 token 覆盖语义 |
| [Tailwind结合 H5 rem/vw 的配置方案](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/27.tailwind-css-adaptation.md) | P2 · A10 · 已修订，验证见记录 | 阶段 3：使用独立的 H5 token 名称，或明确声明这是有意覆盖；区分 Tailwind v3 与 v4 的接入方式。 |
| [H5 Tailwind preset](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/tailwind-css/28.tailwind-preset.md) | P2 · A11 · 已修订，验证见记录 | 阶段 3：统一 preset 的命名与覆盖策略，提供明确版本下的导入和编译方式。 |

### TypeScript（14 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [初识typescript及数据类型](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/02.intro-typescript-data-types.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [类](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/03.typescript-classes.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [接口](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/04.typescript-interfaces.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [泛型](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/05.typescript-generics.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [结构类型系统](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/06.typescript-structural-types.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [类型保护](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/07.typescript-type-guards.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [类型变换](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/08.typescript-type-transforms.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [模块和命名空间](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/09.typescript-modules-namespaces.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [类型声明](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/10.typescript-type-declarations.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [null和undefined](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/01.data-types/11.typescript-null-undefined.md) | P2 · A09 · 已修订，验证见记录 | 阶段 2、5：改成包含关系，注明示例所用编译配置，移除无法核对的比例。 |
| [keyof和typeof](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/02.practical-applications/01.keyof-and-typeof.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [映射类型](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/02.practical-applications/02.mapped-types.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [extends的约束、条件、分发](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/02.practical-applications/03.extend-usage.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |
| [infer关键字（TS的灵魂）](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/typescript-learn/02.practical-applications/04.infer-keyword.md) | P3 · 初筛后待复核 | 阶段 2、5：固定编译器和 tsconfig，区分正确示例与预期错误 |

### Vite（9 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [vite从入门到精通](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/41.vite-intro-to-mastery.md) | P3 · 初筛后待复核 | 阶段 1、3：核对开发、构建、HMR 和虚拟模块生命周期 |
| [vite插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/42.vite-plugins.md) | P3 · 初筛后待复核 | 阶段 1、3：核对开发、构建、HMR 和虚拟模块生命周期 |
| [vite自动导入api插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/43.vite-auto-import-plugin.md) | P1 · A02 · 已修订，验证见记录 | 阶段 1、3：最小修复先识别已有绑定；完整示例再使用语法解析，区分普通模块、Vue SFC 和带查询参数的模块 ID。 |
| [Vite 开发服务器核心原理讲解](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/44.vite-core-modules.md) | P3 · 初筛后待复核 | 阶段 1、3：核对开发、构建、HMR 和虚拟模块生命周期 |
| [Vite HMR源码级讲解](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/45.vite-hmr-source.md) | P3 · 初筛后待复核 | 阶段 1、3：核对开发、构建、HMR 和虚拟模块生命周期 |
| [Vite虚拟模块插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/50.vite-virtual-module.md) | P1 · A03 · 已修订，验证见记录 | 阶段 1、3：用插件工厂闭包保存 mode/env；补齐变量优先级与虚拟模块失效流程，删除未经验证的“生产级、完整可运行”承诺。 |
| [模拟 Vite 内置env](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/53.vite-simulate-env.md) | P2 · A16 · 已修订，验证见记录 | 阶段 1、3：改成教学子集；按目标版本核对 NODE_ENV 与 mode，说明 .env 更改后的重启要求；代码替换处理字符串和注释。 |
| [vite一体化虚拟模块插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/55.vite-unified-virtual-plugin.md) | P2 · A30 · 已修订，验证见记录 | 阶段 1、3：补空模块分支，核对新增/删除监听和导出扫描边界，明确支持的文件语法与构建阶段。 |
| [vite可发布npm的虚拟插件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vite/57.vite-publishable-plugin.md) | P1 · A01 · 已修订，验证见记录 | 阶段 1、3：让插件按实际目标参与构建，核对 resolveId/load/buildStart；同步调整“可发布”的承诺。 |

### Vue 3（10 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [vue3学习路径](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/02.vue3-learning-path.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [vue3的hooks基础总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/03.vue3-hooks.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [Vue3 hooks 实战场景总结](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/04.vue3-hooks-practice.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [Vue3 hooks 对比](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/05.vue3-hooks-comparison.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [Vue3 Virtual DOM & 渲染机制](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/23.vue3-virtual-dom-render.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [Vue3 响应式核心](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/24.vue3-reactivity-core.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [Vue3数组、Map、Set 特殊处理](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/25.vue3-reactivity-special.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [Vue3与vue2响应式处理的不同](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/26.vue3-vs-vue2-reactivity.md) | P3 · 初筛后待复核 | 阶段 1、5：验证响应式/生命周期示例，注明源码版本及教学省略项 |
| [写一个Mini-vue](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/27.write-a-mini-vue.md) | P1 · A04 · 已修订，验证见记录 | 阶段 1、5：保留响应式读取链路，修正 setup 到渲染上下文的桥接；把简化的响应式实现边界写清。 |
| [Mini-vue template增强版](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/basic-knowledge/vue3/28.mini-vue-template-enhanced.md) | P1 · A05 · 已修订，验证见记录 | 阶段 1、5：先修复响应式上下文，再逐项核对 v-if、v-for、事件和子组件演示；明确教学版与 Vue 正式实现的差异。 |

### 技术文档（12 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [nginx相关知识](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/01.nginx-proxy.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [shell相关知识](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/02.linux-shell.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [Linux基础及文件](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/03.linux.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [HTTP协议详解](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/04.http.md) | P1 · A07 · 已修订，验证见记录 | 阶段 1、7：保留基础消息示例，按 HTTP 语义与具体版本分开表述；纠正 no-cache/no-store、CONNECT 和 CORS 名称。；核对标题元数据 |
| [Markdown使用教程](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/05.markdown-guide.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [npm常用命令](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/06.npm-commands.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [Git使用手册](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/08.git-manual.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [npm package.json属性详解](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/10.npm-package-json.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [yaml语言教程](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/15.yaml-guide.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [简介](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/16.modern-frontEnd-technology.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [REPL(交互式解释器)](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/17.learn-node.md) | P3 · 初筛后待复核 | 阶段 1、7：按平台和版本分段，核对旧命令与配置示例；核对标题元数据 |
| [nextTick](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/01.tech-docs/18.learn-node2.md) | P1 · A06 · 已修订，验证见记录 | 阶段 1、7：改成事件循环阶段和具体调用场景；区分 CJS/ESM 与 Node 版本，逐条校正命令。；核对标题元数据 |

### 算法（4 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [查找的基本概念](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/04.algorithms/02.seek.md) | P3 · 初筛后待复核 | 阶段 7：补输入边界与输出回归，保留已经修正的内容；核对标题元数据 |
| [排序算法分类](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/04.algorithms/03.sort.md) | P3 · 初筛后待复核 | 阶段 7：补输入边界与输出回归，保留已经修正的内容；核对标题元数据 |
| [图的定义](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/04.algorithms/04.chart.md) | P3 · 初筛后待复核 | 阶段 7：补输入边界与输出回归，保留已经修正的内容；核对标题元数据 |
| [:beginner:字符串模式匹配](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/04.algorithms/05.string.md) | P3 · 已有修订记录，做回归 | 阶段 7：补输入边界与输出回归，保留已经修正的内容；核对标题元数据 |

### 实用技巧（6 篇）

| 文章 | 优先级 / 当前状态 | 执行安排 |
| --- | --- | --- |
| [GitHub高级搜索技巧](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/01.github-search-tips.md) | P2 · A26 · 已修订，验证见记录 | 阶段 7、8：改正限定词并拆开括号式缩写，区分仓库搜索和代码搜索；修复未闭合强调标记。；核对标题元数据 |
| [说明](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/02.chrome-plugin.md) | P2 · A27 · 已修订，验证见记录 | 阶段 7、8：明确用户脚本与浏览器扩展的区别，固定旧教程依赖，按目标版本运行最小项目。；核对标题元数据 |
| [mac快捷键](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/03.mac-shortcuts.md) | P3 · 初筛后待复核 | 阶段 7、8：核对搜索语法、工具版本、用途和链接可用性；核对标题元数据 |
| [UI 组件库](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/08.frontend-libs.md) | P3 · 初筛后待复核 | 阶段 7、8：核对搜索语法、工具版本、用途和链接可用性；核对标题元数据 |
| [个人收藏夹](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/09.websites.md) | P3 · 初筛后待复核 | 阶段 7、8：核对搜索语法、工具版本、用途和链接可用性；核对标题元数据 |
| [技巧1：排除干扰项](/Users/mamingjuan/Documents/学习/vercel-blog/docs/zh/other/10.practical-tips/10.search-engine-tips.md) | P3 · 初筛后待复核 | 阶段 7、8：核对搜索语法、工具版本、用途和链接可用性；核对标题元数据 |

## 8. 执行记录模板

每篇后续记录：文章路径；审查结论（无须修改／微调／补例子／需要重构）；问题编号与行号；目标版本；支持来源；实际修改；验证输入与输出；双语与旧锚点结果；剩余限制。行号按本次 2026-10-15 快照定位，修改后应更新。

保持原始发表日期；如果需要新增核对日期，应单独标注，不把历史文章伪装成新发布。每个修订只扩展到解决已证实问题所需的范围。

