# 可选方法：保留知识，按需恢复

这 32 项资料退出默认写作包，原始完整内容保留在 v1.1.0 固定版本及本地原件。日常科研写作由七个默认模块负责；具体统计、图形、海报或专利任务出现时再恢复相应方法与工具。

| 可选模块 | 原有能力与触发范围 |
|---|---|
| dask | 并行 数据 大数据；Scales pandas, NumPy, and custom Python research workflows beyond memory or across clusters with Dask. Covers DataFrames, Arrays, Bags, Futures, chunking, schedulers, and distributed diagnostics. Use for partitioned file processing, scienti |
| exploratory-data-analysis | 探索性数据分析 数据质量 分布 异常；Performs bounded, local exploratory analysis of explicitly supported scientific files. Supports redacted CSV/TSV/JSON profiles; optional NumPy, HDF5, FASTA/FASTQ, and basic image metadata inspection; missingness/leakage audits; outlier and  |
| humanize-writing | 润色 自然表达 保留原意；Remove signs of AI-generated writing from text. Use when the user mentions
'sounds like AI,' 'too robotic,' 'humanize this,' 'make it sound human,'
'de-AI this,' 'sounds like ChatGPT,' 'make it natural,' or 'doesn't sound
like a person wrot |
| latex-posters | 学术海报 LaTeX；Creates research posters in LaTeX using beamerposter, tikzposter, or baposter. Use for conference posters, academic presentations, multi-column scientific layouts, figure integration, typography, compilation, and PDF preflight. |
| matplotlib | 绘图 坐标 图例 图形导出；Creates and customizes scientific plots with Matplotlib. Used for fine-grained control over plot elements, novel plot types, and scientific workflows. Export to PNG/PDF/SVG for publication. For quick statistical plots use seaborn; for inter |
| nature-data | 数据整理 分析 表格；Draft or audit manuscript Data/Code Availability statements, dataset access routes, repository plans, and FAIR metadata. Use for 数据可用性声明、数据共享、数据仓库选择 and dataset citations; not general data cleaning or statistical analysis. |
| nature-figure | 科研图 绘图 图表 示意图 图形摘要；Create, revise, audit, and export manuscript scientific figures in Python or R. Use for 论文配图、科研绘图、多面板图 and submission-ready plots, or explicitly requested AI-generated graphical abstracts and mechanism schematics. Not for interactive dashbo |
| nature-image2ppt | 图片 转PPT 可编辑 幻灯片；Reconstruct slide images, screenshots, scanned PDFs, or image-only PPTX files as object-level editable PowerPoint. Use for 图片转可编辑PPT、截图还原PPT and diagram reconstruction; not authoring a new deck from research notes. |
| nature-paper-to-patent | 论文 专利 技术交底；Turn research papers or inventor materials into evidence-grounded Chinese invention patent drafts and technical disclosures. Use for 技术交底书、专利撰写、现有技术对比 and Chinese DOCX patent packages; not general manuscript writing. |
| nature-paper2ppt | 论文 汇报 PPT 演示；Create or improve a Chinese academic PPTX from a scientific paper or research reading notes, with source figures and speaker notes. Use for 论文做PPT、文献汇报、组会PPT and paper-based conference or defense presentations. |
| nature-paper2word | 论文 Word DOCX 排版；Compile an academic Markdown manuscript into a journal- or school-compliant Word (.docx): declared typography, native OMML equations, three-line tables, cross-references, per-section page numbers, CSL bibliographies (GB/T 7714, APA, Nature, |
| nature-reviewer | 模拟审稿 评审 独立评价；Provide evidence-grounded mock peer review of scientific manuscripts or excerpts, covering significance, validity, and major/minor concerns. Use for 模拟审稿、投稿前自审、审稿人视角评估; not author rebuttal drafting. |
| nature-statistics | 统计 模型 检验 实验单位；Audit or improve manuscript statistical reporting, including experimental units, replication, uncertainty, tests, and figure statistics. Use for 统计审查、统计方法小节、图注统计 and reviewer concerns; compute new analyses only when requested with data. |
| networkx | 网络 图论 关系图 路径；Creates, analyzes, and visualizes complex networks and graphs in Python with NetworkX. Use when working with network/graph data structures, computing graph algorithms (shortest paths, centrality, clustering), detecting communities, generati |
| peer-review | 同行评审 审稿 检查；Prepares evidence-bounded, constructive peer-review drafts and structured manuscript assessments. Supports authorized review of scientific manuscripts, protocols, preprints, or research proposals; reporting-guideline selection; claim–eviden |
| polars | 表格 数据处理；High-performance DataFrame library for Python ETL, analytics, and pandas migration. It supports expression-based data manipulation with lazy query optimization, parallel execution, streaming out-of-core processing, Arrow interoperability, a |
| pptx-posters | 学术海报 PowerPoint；Creates and audits editable scientific posters in macro-free PowerPoint (.pptx) from author-approved local content and assets. Used when the requested deliverable is a PowerPoint research/conference poster and exact physical, printer, acces |
| pymc | 贝叶斯 推断 后验 模型；Builds and checks Bayesian models with PyMC, including hierarchical models, NUTS MCMC, variational inference, mutable-data predictions, posterior predictive checks, diagnostics, and PSIS-LOO model comparison. Use for probabilistic modeling  |
| pymoo | 多目标 优化 Pareto；Solves and validates single-, multi-, and many-objective optimization with pymoo, including NSGA-II, NSGA-III, MOEA/D, constraints, Pareto approximations, reference directions, and ZDT/DTLZ benchmarks for engineering and research problems. |
| research-grants | 基金 申请 研究计划；Supports research proposal preparation and review for NSF, NIH, DOE, DARPA, and Taiwan NSTC, including opportunity-specific requirements, aims, review criteria, budgets, broader impacts, forms, and resubmissions. Use for investigator-author |
| scholar-evaluation | 研究评价 论证质量；Provides qualitative-first, evidence-traceable developmental review of scholarly works and audit low-stakes research-assessment rubrics with optional local quality controls. Never use for ranking people or consequential decisions. |
| scientific-schematics | 科学示意图 机制图 流程图；Generates scientific diagram drafts using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.7 Flash for quality review. Refines when the review requests improvement, with at most two generations. Specialized in neural network  |
| scientific-slides | 科研汇报 幻灯片 PPT；Builds slide decks and presentations for research talks. Used for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design tem |
| scientific-visualization | 科研可视化 图表 绘图；Creates and audits truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn, or Plotly. Use it for figure design, multi-panel layouts, uncertainty and missing-data displays, color/contrast review, image metadata v |
| scientific-writing | 写作 一致性 论文 报告规范；Drafts, revises, and audits scientific manuscripts or reports with explicit evidence provenance, reporting-guideline coverage, authorship accountability, confidentiality controls, and local consistency checks. Use for manuscript sections, r |
| scikit-learn | 机器学习 交叉验证 回归 分类；Supports machine learning in Python with scikit-learn. Applies when working with supervised learning (classification, regression), unsupervised learning (clustering, dimensionality reduction), model evaluation, hyperparameter tuning, prepro |
| seaborn | 统计绘图 分布 比较 热图；Creates Seaborn statistical visualizations with pandas integration for distributions, relationships, categorical comparisons, regression displays, pair plots, and heatmaps. Supports function and objects interfaces with explicit aggregation, |
| statistical-analysis | 统计 分析 检验 置信区间；Guided statistical analysis for research data - test selection, assumption checking, effect sizes, power analysis, Bayesian alternatives, and APA-formatted reporting. Use whenever a user wants to compare groups, test a hypothesis, analyze e |
| statistical-power | 统计功效 样本量；Calculates sample sizes and statistical power for study planning. Applies when someone asks "how many subjects/samples/replicates do I need", wants an a priori power analysis, a minimum detectable effect (MDE), a power curve, or needs to ju |
| statsmodels | 统计模型 回归 方差分析；Fits and diagnoses Python statistical models including OLS, GLM, discrete and mixed models, ARIMA and SARIMAX. Supports coefficient inference, marginal effects, model comparison and time series forecasting with explicit design and uncertain |
| sympy | 符号计算 方程 推导；Performs exact symbolic mathematics with SymPy for algebra, calculus, equation solving, symbolic linear algebra, physics, and lambdify or LaTeX code generation. Use when a task needs symbolic results, explicit assumptions, or exact arithmet |
| venue-templates | 期刊 模板 格式 投稿；Prepares journal manuscripts, conference papers, research posters, and grant documents using venue-specific formatting guidance and bundled LaTeX scaffolds. Supports selecting an official template, checking current page or anonymity rules,  |

恢复命令（在有机核心中运行）：

```text
python scripts/workbench.py search 海报 --optional
python scripts/workbench.py restore-optional pptx-posters --skills-root 当前宿主的技能目录
```

恢复时从 v1.1.0 ZIP 校验原始文件，只补选中的内部模块，不注册新的平级技能、不执行源安装器，也不覆盖已存在原件。保持安装源目录不变；目标指向已安装的 skills。
