# 论文写作技巧速查手册

面向中文母语研究者的英文 ML/AI 论文写作指南。基于 [Paper-Writing-Tips](https://github.com/MLNLP-World/Paper_Writing_Tips) 及多位顶会论文写作经验整理。

---

## 一、Reviewer 视角自查

在提交论文之前，以 reviewer 的视角回答以下五个核心问题。如果任何一个回答不确定，说明论文还需要修改。

### 五个核心问题

1. **10分钟内能否抓到重点，理清逻辑？**
   - 一个忙碌的 reviewer 可能分配给你的论文不到一小时。前10分钟的阅读体验决定了他/她对论文的整体印象。
   - 检查方法：请一位没有参与研究的同事阅读摘要和引言，看他们能否在10分钟内说出你的核心贡献。

2. **Motivation 和 Contribution 之间的逻辑是否成立？**
   - 问题是否自然引出你的解决方案？
   - 因果链条是否完整：问题 → 现有方法的不足 → 你的思路 → 你的方法？
   - 常见错误：motivation 说的是问题 A，但方法解决的是问题 B。

3. **三句话内能否说清楚最重要的亮点（贡献）？**
   - 模板："We [introduce/demonstrate/prove] [what] which [evidence] because [why it matters]."
   - 如果说不清楚，说明贡献还没有结晶化（crystallize），需要回到 Phase 2。

4. **实验是否验证了 motivation 的合理性？**
   - 每个实验是否对应一个明确的问题？
   - 消融实验（ablation）是否覆盖了所有声明的贡献？
   - 实验结果是否真的支持你的 claim？如果某个实验结果不支持，你是否诚实讨论了？

5. **Abstract → Introduction → Method → Experiments 逻辑是否一致？**
   - 各部分讲的是同一个故事，没有矛盾
   - 引言中声明的贡献在实验中都有对应的验证
   - 方法部分描述的每个组件在消融实验中都有体现

---

## 二、写作技巧

### 呈现优先级

**图 > 表 > Algorithm > 公式 > 文字**

- 一图胜千言——能用图说清楚的事情不要用文字
- 复杂流程优先考虑 Algorithm 伪代码
- 公式要有直觉解释，不要只放公式不解释
- 文字描述是最后的选择

### 关键原则

1. **实验篇幅尽量多**
   - 顶会论文中实验部分往往占一半甚至更多篇幅
   - 实验是支撑贡献的核心证据

2. **图和 caption 要有相对独立性**
   - 不看正文，只看图和 caption，也应该能理解这张图在说什么
   - Caption 写"这张图是什么"；正文写"这张图说明了什么"

3. **语言以简明易懂为优**
   - 清晰优先于复杂和华丽
   - 用简单的句式表达复杂的想法
   - 避免一句话超过三行

4. **引言和 case study 中具体的例子很重要**
   - 抽象的描述难以打动 reviewer
   - 一个好的例子可以让 reviewer 立刻理解你在做什么

5. **讲好故事（narrative）**
   - 论文不是实验报告的罗列，而是一个有起承转合的故事
   - 从问题出发 → 现有方法的不足 → 你的 insight → 你的方法 → 实验验证

### 时间分配（来自 Neel Nanda）

在以下四部分上花费大致相同的时间：
1. 摘要（Abstract）
2. 引言（Introduction）
3. 图（Figures）
4. 其他所有内容加在一起

这看起来很极端，但反映了 reviewer 的实际阅读行为：标题 → 摘要 → 引言 → 看图 → 可能再看方法。

---

## 三、论文结构

**标准 IMRAD 结构：**

摘要 → 引言 → （相关工作 / Preliminary）→ 方法 → 实验 → 结论

### 摘要（Abstract）

Sebastian Farquhar（DeepMind）的五句话公式：

1. **你做了什么**："We introduce...", "We prove...", "We demonstrate..."
2. **为什么这很难且重要**
3. **你怎么做的**（包含专业关键词，便于检索）
4. **有什么证据**
5. **最亮眼的数字/结果**

**常见错误：**
- 以泛泛的背景开头："Large language models have achieved remarkable success..." ——删掉，直接说你做了什么
- 摘要太长——会议论文的摘要通常 150-250 词
- 没有具体数字——摘要中至少包含一个关键实验数字

### 引言（Introduction）

**推荐结构（1-1.5 页）：**

1. 研究问题的价值——为什么这个问题重要
2. 前人的主流做法及其缺陷——肯定前人工作的同时指出不足
3. Motivation 的来源——你的灵感来自哪里
4. 提出的方法（粗粒度）——一两句话概括你的方法
5. 具体的例子说明——一个好的例子胜过一段抽象描述
6. 方法的细粒度解释——稍微展开说明
7. 贡献列表——用 bullet points 列出 2-4 个贡献

**注意：** Methods 部分应该在第 2-3 页开始。如果引言写到了第 3 页还没结束，需要精简。

---

## 四、各章节写作要点

### Related Work（相关工作）

**核心目标：**
- 展示你对领域的理解深度
- 明确你的工作与前人的区别
- 承认你构建在谁的基础上，同时指出差距

**组织策略：**

| 策略 | 适用场景 | 结构 |
|------|----------|------|
| 按时间 | 展示领域演进 | 早期 → 近期 → 本文 |
| 按主题 | 涉及多个技术方向 | 分类讨论，最后比较 |
| 按问题 | 技术论文 | 按解决的挑战分组 |

**批判性分析——不要只总结，要定位：**

```
# 弱 - 仅总结
Smith et al. (2022) proposed a transformer model for X.

# 强 - 批判性定位
Smith et al. (2022) demonstrated the effectiveness of transformers for X.
However, their approach requires O(n^2) memory, limiting scalability.
We address this by introducing a linear-complexity alternative.
```

**常见错误：**
- 流水账式罗列（"A did X. B did Y. C did Z."）→ 应按主题分组，建立逻辑关系
- 只说好话不指出局限 → 需要指出每类方法的不足
- 遗漏近期工作 → 提交前检查近 6 个月的 arXiv
- 篇幅：会议论文引用 15-25 篇，重点分析 3-5 篇最相关的

### Methods（方法）

**标准结构：**
1. 问题形式化（Problem Formulation）
2. 方法概述（配架构图）
3. 各组件详细描述
4. 训练/优化细节

**核心方法 vs 实现细节的区分：**

| 放在正文 | 放在附录 |
|----------|----------|
| 关键算法创新 | 硬件配置 |
| 新架构组件 | 随机种子 |
| 损失函数设计 | 完整超参数表 |
| 理论分析 | 辅助实验细节 |

**经验法则：** 如果改变某个细节不会改变论文的科学贡献，它就是实现细节，可以放在附录。

**何时使用伪代码：**
- 复杂的多步骤流程 → 用 Algorithm
- 新颖的算法 → 用 Algorithm
- 标准操作（SGD、Adam）→ 不需要
- 2-3 句话能说清的 → 不需要

### Experiments（实验）

**标准结构：**
1. 实验设置（数据集、基线、评价指标、实现细节）
2. 主要结果（Main Results）
3. 分析（消融实验、案例研究、可视化）
4. 讨论（可选——讨论局限性和意外发现）

**每个实验回答一个问题：**

| 问题 | 实验设计 |
|------|----------|
| 有效吗？ | 与基线对比（Main Results） |
| 为什么有效？ | 消融实验（Ablation Study） |
| 什么情况有效？ | 按类别/数据集/领域分析 |
| 多稳健？ | 敏感性分析、不同超参数 |
| 多高效？ | FLOPs、内存、推理速度 |

**消融实验设计：**
- 每次只移除一个组件
- 包含基线模型（移除所有提出的组件）
- 按影响程度排序（最重要的组件放最前）
- 报告均值和标准差

**统计显著性：**
- 小改进（< 2%）必须报告统计检验
- 至少跑 3-5 次取均值和标准差
- 报告格式：89.3 ± 0.4%
- 使用相同的随机种子集合进行公平对比

**处理负面结果：**

```
# 好 - 诚实且建设性
While our method shows slightly lower performance on small datasets
(Table 3, row 2), it demonstrates significant advantages at scale,
suggesting the approach is most suitable for data-rich scenarios.

# 避免 - 简单承认失败
Our method does not work well on Dataset-C.
```

### Conclusion（结论）

**结构：**
1. 总结做了什么（2-3 句）
2. 关键发现（2-3 句）
3. 意义/影响（1-2 句）
4. 局限性（1-2 句）
5. 未来工作（2-3 句）

**回扣开头——首尾呼应：**

```
# 引言中的问题
"Current methods suffer from O(n^2) complexity, limiting their
applicability to long sequences."

# 结论中的回应
"We have shown that our approach reduces complexity from O(n^2)
to O(n log n), enabling processing of sequences 10x longer than
existing methods while maintaining comparable accuracy."
```

**建设性地表述局限：**

| 局限 | 建设性表述 |
|------|-----------|
| 计算成本高 | "There exists a trade-off between accuracy and efficiency that future work may address." |
| 需要大量标注数据 | "A semi-supervised extension could reduce the annotation requirements." |
| 只在英文上测试 | "Multilingual evaluation remains an important direction for future work." |

**不要包含：**
- 新的结果或新的方法（结论中不应出现新内容）
- 重复摘要的原文
- 过度道歉或过度宣传

**篇幅：** 会议论文通常半栏到一栏。

---

## 五、公式符号规范

### 基本符号约定

| 类型 | 规范 | LaTeX 代码 | 示例 |
|------|------|-----------|------|
| 标量 | 小写斜体 | `$x$`, `$y$` | $x$, $y$ |
| 向量 | 小写加粗 | `$\mathbf{x}$` | **x** |
| 矩阵 | 大写加粗 | `$\mathbf{A}$` | **A** |
| 有结构的值 | `\boldsymbol` | `$\boldsymbol{s}$` | 句子序列、树、图 |
| 集合 | 花体 | `$\mathcal{D}$` | 数据集、空间 |
| 数域/期望 | 双线体 | `$\mathbb{R}$` | 实数域、期望 |

**特别注意：** 用 `\ell` 代替 `l`，避免与数字 1 混淆。

### 多字母变量名

公式中超过一个字母的变量名或算子，必须使用正文字体，否则每个字母会被当作独立变量的乘积：

```latex
% 正确
\textrm{softmax}(x), \textrm{proj}(v), \textrm{enc}(x)

% 错误 - 斜体会让 softmax 看起来像 s×o×f×t×m×a×x
softmax(x), proj(v), enc(x)
```

### 预定义函数命令

```latex
% 使用 LaTeX 内置命令
\arg\max_{x}, \sin(x), \cos(x), \tanh(x), \exp(x), \log(x)
\inf, \sup, \det, \lim_{x \to \infty}

% 自定义常用算子
\DeclareMathOperator{\softmax}{softmax}
\DeclareMathOperator{\ReLU}{ReLU}
\DeclareMathOperator{\KL}{KL}
\DeclareMathOperator*{\argmin}{arg\,min}
```

### 括号匹配

```latex
% 正确 - 括号随内容缩放
\left( \sum_{i=0}^{N-1} \alpha_i \mathbf{h}_i \right)

% 错误 - 括号大小不匹配
( \sum_{i=0}^{N-1} \alpha_i \mathbf{h}_i )

% 条件集合
\left\{ x \middle| x \neq \frac{1}{2} \right\}
```

### 多行公式对齐

```latex
% 推荐 - 等号对齐
\begin{align}
    \mathcal{L} &= \mathcal{L}_{\textrm{cls}} + \lambda \mathcal{L}_{\textrm{reg}} \\
    &= -\sum_{i} y_i \log \hat{y}_i + \lambda \|\mathbf{W}\|_2^2
\end{align}
```

### 公式编号

只对需要在正文中引用的公式编号：

```latex
\begin{align}
    \mathbf{h} &= f(\mathbf{x}) \nonumber \\       % 中间步骤不编号
    \hat{y} &= g(\mathbf{h}) \label{eq:output}      % 需要引用的公式编号
\end{align}
```

---

## 六、LaTeX 排版规范

### 不间断空格（~）

使用 `~` 防止引用和前面的文字被分到不同行：

```latex
Figure~\ref{fig:model}
Table~\ref{tab:results}
Section~\ref{sec:intro}
Equation~\eqref{eq:loss}
BERT~\cite{devlin2019bert}
```

**原则：** 所有 `\ref{}`、`\eqref{}`、`\cite{}` 前面都应该用 `~`。

### 英文引号

```latex
% 正确 - 使用反引号和单引号
``quoted text''
`single quotes'

% 错误 - 不要使用直引号
"quoted text"    % 这是打字机引号，不是排版引号
```

**注意：** 引号只表示"所谓的"（so-called），不表示直接引用。引用他人的表述考虑用斜体 `\textit{}`。

### 引用命令

不同模板使用不同的引用命令：

| 模板 | 作为句子成分 | 括号引用 |
|------|------------|----------|
| ACL/NAACL/EMNLP | `\citet{key}` | `\citep{key}` |
| COLING | `\newcite{key}` | `\cite{key}` |
| AAAI/IJCAI | `\citeauthor{key} \shortcite{key}` | `\cite{key}` |
| NeurIPS/ICML/ICLR | `\citet{key}` | `\citep{key}` |

```latex
% 作为句子成分 - 用 \citet
\citet{vaswani2017attention} propose the Transformer architecture.

% 不作为句子成分 - 用 \citep
Attention mechanisms have shown great success~\citep{vaswani2017attention,devlin2019bert}.
```

### 三线表（Booktabs）

```latex
\usepackage{booktabs}

\begin{table}[t]
    \centering
    \caption{Main results on three benchmarks. Best results in \textbf{bold}.}
    \label{tab:results}
    \begin{tabular}{lcc}
        \toprule
        Method & Accuracy & F1 \\
        \midrule
        Baseline & 85.2 & 84.1 \\
        Previous SOTA & 87.6 & 86.9 \\
        \textbf{Ours} & \textbf{89.3} & \textbf{88.7} \\
        \bottomrule
    \end{tabular}
\end{table}
```

**重要原则：**
- **不要画竖线** —— 三线表只有三条横线
- 使用 `\toprule`（最粗）、`\midrule`（中等）、`\bottomrule`（最粗）
- 多列表头用 `\cmidrule(lr){2-4}` 做局部分隔
- 数值列右对齐，文字列左对齐

### 表格大小调整

```latex
% 缩小字号
{\small
\begin{tabular}{lcc}
...
\end{tabular}
}

% 调整列间距
\setlength{\tabcolsep}{4pt}

% 用 resizebox 缩放到列宽
\resizebox{\columnwidth}{!}{
\begin{tabular}{...}
...
\end{tabular}
}
```

---

## 七、图片规范

### 矢量图优先

```latex
% 推荐 - 矢量图（无损缩放）
\includegraphics[width=0.8\textwidth]{figure.pdf}

% 不推荐 - 位图（缩放会模糊，除非是照片）
\includegraphics[width=0.8\textwidth]{figure.png}
```

### 图片要求

1. **字体大小**：图中文字大小应介于正文字体和 caption 字体之间，且所有图保持一致
2. **颜色数量**：不超过 6 种，避免过亮颜色
3. **黑白友好**：不能仅靠颜色区分——同时使用实线/虚线、不同标记（○ △ □）
4. **简洁**：尽量少用文字，同功能的模块用统一格式
5. **箭头方向**：流程图的箭头应趋于同一方向（通常从左到右或从上到下），避免来回折转
6. **子图引用**：`Figure~\ref{fig:model}(a)` 引用子图

### Figure 1 的特殊重要性

Figure 1 是论文的"视觉摘要"。很多 reviewer 在阅读任何文字之前先看 Figure 1。

**好的 Figure 1 应该：**
- 一目了然地传达核心思想
- 不需要阅读正文就能理解
- 如果是方法图，展示高层流程而非所有细节
- 如果是结果图，展示最亮眼的结果

**常见错误：**
- 塞入太多细节，导致看不清重点
- 字体太小，打印后看不清
- 使用屏幕截图而不是矢量图

---

## 八、写作风格

### 避免缩写

学术论文中不使用缩写形式：

```
# 正确
do not, it is, we have, cannot, does not

# 错误
don't, it's, we've, can't, doesn't
```

### 所有格转换

学术英语中倾向于使用 "of" 结构而非 's 所有格：

```
# 推荐
the performance of the method
the structure of the model
the output of the encoder

# 避免
method's performance
model's structure
encoder's output
```

### 拉丁惯用语

| 表达 | 含义 | 注意事项 |
|------|------|---------|
| `e.g.,` | for example | 后面必须有逗号 |
| `i.e.,` | that is | 后面必须有逗号 |
| `et al.` | and others | 用于多作者引用 |
| `etc.` | and so on | 不用于人，只用于事物 |
| `w.r.t.` | with respect to | 可用，但有的期刊不建议 |
| `cf.` | compare | 表示"参见" |

**注意：** `et al.` 或 `etc.` 在句末时不需要额外的句号（它们自带的句点充当句号）。

### 避免绝对化表述

| 避免使用 | 替换为 |
|---------|--------|
| obvious, clearly | straightforward, we observe that |
| always | generally, typically, in most cases |
| never | rarely, seldom, in few cases |
| prove (非数学证明场景) | demonstrate, show, provide evidence |
| significant (无统计检验) | notable, substantial, considerable |
| outperform (小幅度) | achieve competitive/comparable results |
| novel (过度使用) | 直接描述新在哪里，让 reviewer 自己判断 |
| state-of-the-art (自称) | 用数字说话，让结果自己说明 |

### 冠词（a/an/the）用法

这是中文母语者最常犯的错误之一：

```latex
% a/an 跟着发音走，不是看首字母
an LSTM cell     % L 发音 /el/，元音开头
an F1 score      % F 发音 /ef/，元音开头
a URL            % U 发音 /ju:/，辅音开头
a unified model  % u 发音 /ju:/，辅音开头
an hour          % h 不发音，元音开头

% the 用于特指
the proposed method       % 特指我们提出的方法
the Transformer model     % 特指某个具体模型

% 不加冠词用于泛指
Deep learning is powerful.        % 泛指深度学习这个领域
Neural networks can approximate... % 泛指神经网络
```

**经验法则：** 英文中单数可数名词不能单独出现，必须加 a/an/the 或用复数形式。

### 常见中式英语纠正

| 中式英语 | 正确表达 |
|---------|---------|
| "In recently years" | "In recent years" |
| "have a good performance" | "perform well" / "achieve strong performance" |
| "is very worth" | "is worthwhile" |
| "can be seen that" | "we observe that" / "as shown in" |
| "in this paper, we will" | "in this paper, we" (论文用一般现在时) |
| "as we all know" | 删掉，直接陈述事实 |
| "more and more" | "increasingly" / "a growing number of" |
| "play an important role" | "is critical for" / "contributes to" |

---

## 九、投稿前检查清单

### 内容检查
- [ ] 摘要符合五句话公式，包含具体数字
- [ ] 引言不超过 1.5 页，贡献列表清晰
- [ ] 每个实验明确对应一个 claim
- [ ] 消融实验覆盖所有提出的组件
- [ ] 标题和摘要与投稿系统中填写的一致
- [ ] Limitations 部分完整（ACL/NeurIPS/ICML 必需）
- [ ] 如果有 checklist，逐项认真填写

### 匿名性检查
- [ ] 无作者姓名和机构信息
- [ ] 无个人邮箱地址
- [ ] 代码路径不包含个人信息（如 `/home/zhangsan/`）
- [ ] 致谢（Acknowledgments）已删除或隐藏
- [ ] 图片元数据不包含个人信息
- [ ] 自引使用第三人称（"Zhang et al. (2023) show..." 而不是 "In our previous work..."）

### 格式检查
- [ ] 不超过页数限制（参考文献和附录不计入）
- [ ] 所有图表有 `\label` 并在正文中引用
- [ ] 引用格式统一（会议名称缩写一致）
- [ ] 优先引用正式发表版本，而非 arXiv 预印本
- [ ] 无 TODO、FIXME 或占位文字

### LaTeX 检查
- [ ] 不间断空格（~）使用正确
- [ ] 英文引号格式正确（\`\`...''）
- [ ] 编译无 Warning（特别是 overfull hbox）
- [ ] 使用了 `\usepackage[english]{babel}` 优化断字
- [ ] 未修改 .sty / .cls 文件

### 图表检查
- [ ] 所有图片为矢量格式（PDF），照片除外
- [ ] 图内字体大小一致，打印后可读
- [ ] 颜色不超过 6 种
- [ ] 黑白打印也能区分不同线条/标记
- [ ] 图片两侧无多余空白
- [ ] 表格使用 booktabs 三线表，无竖线

### BibTeX 检查
- [ ] 所有 `\cite{}` 的 key 在 .bib 文件中都有定义
- [ ] 没有未使用的 BibTeX 条目产生的 Warning
- [ ] 会议名称格式一致（不混用全称和缩写）
- [ ] 有 DOI 的论文尽量包含 DOI
- [ ] arXiv 论文已有正式版本的，替换为正式版本

---

## 十、参考工具和资源

### 写作辅助工具

| 工具 | 用途 | 链接 |
|------|------|------|
| Grammarly | 语法和拼写检查 | [grammarly.com](https://app.grammarly.com) |
| Writefull | 学术英语写作检查 | [writefull.com](https://www.writefull.com/) |
| QuillBot | 改写和润色 | [quillbot.com](https://quillbot.com) |
| DeepL Write | 写作改善建议 | [deepl.com/write](https://www.deepl.com/write) |

### BibTeX 工具

| 工具 | 用途 | 链接 |
|------|------|------|
| SimBiber | BibTeX 条目简化 | [github.com/MLNLP-World/SimBiber](https://github.com/MLNLP-World/SimBiber) |
| Rebiber | BibTeX 规范化（arXiv → 正式版） | [github.com/yuchenlin/rebiber](https://github.com/yuchenlin/rebiber) |
| DBLP | 获取标准 BibTeX | [dblp.org](https://dblp.org) |
| Semantic Scholar | 论文搜索和 BibTeX | [semanticscholar.org](https://www.semanticscholar.org) |

### 论文检查工具

| 工具 | 用途 | 链接 |
|------|------|------|
| aclpubcheck | ACL 投稿格式检查 | [github.com/acl-org/aclpubcheck](https://github.com/acl-org/aclpubcheck) |
| arxiv-latex-cleaner | arXiv 提交清理 | [github.com/google-research/arxiv-latex-cleaner](https://github.com/google-research/arxiv-latex-cleaner) |
| ChkTeX | LaTeX 语法检查 | 大多数 TeX 发行版自带 |

### 学习资源

| 资源 | 作者/来源 |
|------|----------|
| [机器翻译学术论文写作方法和技巧](http://nlp.csai.tsinghua.edu.cn/~ly/talks/cwmt14_tut.pdf) | 清华大学刘洋 |
| [如何端到端地写科研论文](https://xpqiu.github.io/slides/20181019-PaperWriting.pdf) | 复旦大学邱锡鹏 |
| [How to Write a Paper](http://www.phontron.com/slides/neubig15paperwriting.pdf) | CMU Graham Neubig |
| [How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) | Neel Nanda (Google DeepMind) |
| [How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) | Sebastian Farquhar (DeepMind) |
| [Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) | Gopen & Swan |
| [Deep Learning Book - Notation](https://www.deeplearningbook.org/contents/notation.html) | Goodfellow et al. |
| [Paper-Writing-Tips](https://github.com/MLNLP-World/Paper_Writing_Tips) | MLNLP 社区 |
