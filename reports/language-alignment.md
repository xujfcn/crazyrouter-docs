# 按修复时间对齐多语言文档

完成日期：2026-10-24。范围为本地 `crazyrouter-docs`，尚未发布。

已根据各页面实际内容修复的 Git 时间同步六种语言。本轮同步或补译 361 个语言页面；原有 181 个技术差异候选和 104 个疑似英文回退项已处理，复查新增发现的 49 个英文回退页面也已补译。严格检查通过。

## 如何决定采用哪个版本

逐页比较内容修复提交，而不是直接采用文件修改时间，也不固定以中文为最新。最终 142 个页面的内容基准为：中文 127 页、英文 14 页、俄文 1 页。

- 排除创建翻译、更新导航、补充推广外链、重新发布、修正无效 JSX 标签等不改变技术内容的提交。
- 对 2026-06-16 和 2026-06-23 的域名替换提交比较前后正文；仅替换入口域名的改动不覆盖较新的模型可用性、接口行为或停用说明。
- 同一次内容提交涉及多种语言时，优先使用中文，其次英文。
- 本轮开始前已存在且尚未提交的 LiteLLM 指南，按其明确的 2026-10-24 编写日期保留为最新本地版本。
- 页面显示的是内容修复日期；2026-10-24 的翻译日期单独记录在 `alignment-state.json`，不会把历史验证日期改成今天。

每页各语言的提交、时间、选择理由和原始内容哈希见 [alignment-sources.json](alignment-sources.json)。每个译文的来源、内容日期、翻译日期和当前文件哈希见 [alignment-state.json](alignment-state.json)。

## 代表性修复

| 页面 | 采用的内容记录 | 对齐结果 |
| --- | --- | --- |
| `images/flux` | 英文，2026-10-12，`a16de8a` | 将较新的移除 DALL·E 推荐修复同步回中文及其他语言 |
| `openclaw-hermes` | 俄文，2026-10-12，`65c2ac3` | 同步较新版本，页面描述改为兼容模型表述；正文沿用该修复版本 |
| `chat/gemini/image-edit` | 中文，2026-09-28，`414cc94` | 同步统一 Images API、图片输入方式及兼容性说明 |
| `api-endpoint`、`chat/anthropic/completions`、`features/tool-calling`、`token-management/logs-and-costs` | 中文，2026-06-23，`fa9a6b0` | 补齐 Claude 原生工具调用与相关计费说明 |
| `video/sora` | 中文，2026-06-09，`c5117c2` | 保持隐藏公开示例；后来的日文域名替换不代表重新开放 Sora |
| `integrations/litellm` | 本地原有指南，2026-10-24 | 保留并同步较新的 LiteLLM 接入与兼容性说明 |
| `jp/audio/stt`、`ru/integrations/chatbox` 等 | 各自最新内容基准 | 将大段英文正文补译为目标语言 |

复查修正了俄文 Seedance 将人民币单位误译为卢布的问题，统一为人民币 CNY；另修正了日文超时条件的边界表达、Seedance `generate_audio` 的布尔含义、部分俄文元信息字段名及未翻译的产品名称。

## 检查结果

| 项目 | 结果 |
| --- | --- |
| 六种语言页数 | 各 142 页，总计 852 页 |
| 各语言导航 | 137 个不同页面，集合与顺序一致 |
| 缺页、断链、跨语言误跳 | 0 |
| 技术差异候选 | 0 |
| 疑似英文回退正文 | 0 |
| 内容日期不一致 | 0 |
| 本轮译文章节、组件、表格行数差异 | 0 |
| 本轮译文代码块、技术行内字面量差异 | 0 |
| 本轮译文非目标中文残留 | 0（代码块原样保留） |
| YAML 元信息错误 | 0 |
| MDX 编译 | 852 / 852 通过 |
| `git diff --check` | 通过 |

英文回退检测现已排除元信息日期与相关链接区块，避免仅因日期被翻译就把英文正文当成已翻译。技术检查增加了代码示例中的模型和 API 基址字段；翻译期间保留代码块，行内自然语言按逐页映射核对，而不是删除不匹配项来使检查通过。

数值表格检查中剩余 27 个页面的格式提示已逐行检查，均为等价语言表达，例如“单次/1回”“第二/2番目”“三段/3단계”或数字与文字数量。对照原句和译句保存在 [numeric-format-review.json](numeric-format-review.json)。日期本地化、“5 折/50%”以及“百万/100万/1 миллион”的等价换算另经核对。没有改写供应商价格来消除这些格式提示。

完整结果见 [language-alignment.json](language-alignment.json)、[alignment-validation.json](alignment-validation.json)、[mdx-validation.json](mdx-validation.json)。本轮修复前的 181 / 104 项记录保存在 [language-alignment-before-content-sync.json](language-alignment-before-content-sync.json)。

此前新增的 142 页西班牙语、其他语言的 10 个缺页、语言导航和链接修复均保留。原来未展示的 5 页继续不展示：`audio/gpt4o-audio`、`audio/realtime`、`chat/openai/special-models`、`images/flux`、`video/sora`。

## 复查命令

在文档目录执行：

```bash
python scripts/audit_languages.py --strict-content
```

严格模式当前返回 0。以后修改文档时，检查会按逐页来源记录重新比较并报告变化。

本轮对齐的是仓库中最新已记录的修复内容，不代表重新验证了供应商在 2026-10-24 的实时价格或模型能力。已抽查关键接口、计费与状态说明；机器检查不能证明所有自然语言表述完全等价。未进行线上发布或浏览器界面验收。
