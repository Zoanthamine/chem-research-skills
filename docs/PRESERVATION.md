# 保留、恢复与迁移对照

上一版公开包确有内容收缩：七个模块的参考、模板和脚本曾只剩通用方法页。本版核实原始来源后恢复七个完整模块，补回 48 项脚本/程序模板，并为所有主技能建立逐文件入口。减少重复的 SKILL 注册不等于删除知识或代码。

## 模块级对照

| 模块 | 主技能 | 本地原模块文件 | 上版公开文件 | 当前公开脚本 | 处理 |
|---|---|---:|---:|---:|---|
| solve-single-crystal | scxrd-refinement | 13 | 1 | 0 | 完整知识重新整理；主技能等效工具＋原件固定来源；本地原件保留 |
| hpc-gaussian | huangjt-computational-chemistry | 14 | 1 | 1 | 恢复完整模块、脚本、参考与模板 |
| hpc-gromacs | huangjt-computational-chemistry | 15 | 1 | 1 | 恢复完整模块、脚本、参考与模板 |
| hpc-orchestration | huangjt-computational-chemistry | 31 | 1 | 13 | 恢复完整模块、脚本、参考与模板 |
| molecular-dynamics | huangjt-computational-chemistry | 3 | 3 | 0 | 保留完整运行方法与工具 |
| rdkit-conf | huangjt-computational-chemistry | 2 | 1 | 1 | 恢复完整模块、脚本、参考与模板 |
| matchms | huangjt-spectral-structure-analysis | 8 | 8 | 1 | 保留完整运行方法与工具 |
| nmrglue | huangjt-spectral-structure-analysis | 4 | 4 | 1 | 保留完整运行方法与工具 |
| pyopenms | huangjt-spectral-structure-analysis | 24 | 24 | 17 | 保留完整运行方法与工具 |
| spectrum-analyzer | huangjt-spectral-structure-analysis | 30 | 29 | 21 | 保留完整运行方法与工具 |
| analytical-method-validation | organic-chemistry-reasoning | 17 | 17 | 8 | 保留完整运行方法与工具 |
| datamol | organic-chemistry-reasoning | 10 | 10 | 0 | 保留完整运行方法与工具 |
| experimental-design | organic-chemistry-reasoning | 7 | 7 | 2 | 保留完整运行方法与工具 |
| hypothesis-generation | organic-chemistry-reasoning | 27 | 27 | 8 | 保留完整运行方法与工具 |
| medchem | organic-chemistry-reasoning | 4 | 4 | 1 | 保留完整运行方法与工具 |
| openbabel | organic-chemistry-reasoning | 1 | 1 | 0 | 保留完整运行方法与工具 |
| organic-chemistry-assistant | organic-chemistry-reasoning | 7 | 1 | 0 | 恢复完整模块、脚本、参考与模板 |
| rdkit | organic-chemistry-reasoning | 9 | 9 | 3 | 保留完整运行方法与工具 |
| scientific-brainstorming | organic-chemistry-reasoning | 10 | 10 | 4 | 保留完整运行方法与工具 |
| scientific-critical-thinking | organic-chemistry-reasoning | 9 | 9 | 0 | 保留完整运行方法与工具 |
| uncertainty-and-units | organic-chemistry-reasoning | 15 | 15 | 7 | 保留完整运行方法与工具 |
| academic-research-suite | huangjt-academic-research | 2657 | 1470 | 502 | 保留运行模块；维护评测原件保留获取方式 |
| bgpt-paper-search | huangjt-academic-research | 1 | 1 | 0 | 保留完整运行方法与工具 |
| citation-management | huangjt-academic-research | 22 | 22 | 8 | 保留完整运行方法与工具 |
| exa-search | huangjt-academic-research | 5 | 5 | 2 | 保留完整运行方法与工具 |
| literature-review | huangjt-academic-research | 12 | 12 | 5 | 保留完整运行方法与工具 |
| nature-academic-search | huangjt-academic-research | 58 | 57 | 27 | 保留完整运行方法与工具 |
| nature-citation | huangjt-academic-research | 17 | 17 | 3 | 保留完整运行方法与工具 |
| nature-downloader | huangjt-academic-research | 71 | 69 | 51 | 保留完整运行方法与工具 |
| nature-literature-pipeline | huangjt-academic-research | 12 | 12 | 0 | 保留完整运行方法与工具 |
| nature-paper-card | huangjt-academic-research | 24 | 24 | 4 | 保留完整运行方法与工具 |
| nature-paper-trans | huangjt-academic-research | 13 | 13 | 5 | 保留完整运行方法与工具 |
| nature-paper-xray | huangjt-academic-research | 7 | 7 | 0 | 保留完整运行方法与工具 |
| nature-reader | huangjt-academic-research | 20 | 20 | 1 | 保留完整运行方法与工具 |
| nature-ref-verifier | huangjt-academic-research | 6 | 6 | 0 | 保留完整运行方法与工具 |
| nature-shared | huangjt-academic-research | 21 | 21 | 2 | 保留完整运行方法与工具 |
| paper-lookup | huangjt-academic-research | 24 | 24 | 5 | 保留完整运行方法与工具 |
| parallel-web | huangjt-academic-research | 8 | 8 | 0 | 保留完整运行方法与工具 |
| pyzotero | huangjt-academic-research | 15 | 15 | 0 | 保留完整运行方法与工具 |
| research-lookup | huangjt-academic-research | 5 | 5 | 2 | 保留完整运行方法与工具 |
| dask | huangjt-academic-writing | 8 | 8 | 0 | 保留完整运行方法与工具 |
| exploratory-data-analysis | huangjt-academic-writing | 21 | 21 | 13 | 保留完整运行方法与工具 |
| humanize-writing | huangjt-academic-writing | 8 | 7 | 2 | 保留完整运行方法与工具 |
| latex-posters | huangjt-academic-writing | 17 | 17 | 3 | 保留完整运行方法与工具 |
| matplotlib | huangjt-academic-writing | 7 | 7 | 2 | 保留完整运行方法与工具 |
| nature-data | huangjt-academic-writing | 15 | 15 | 0 | 保留完整运行方法与工具 |
| nature-figure | huangjt-academic-writing | 130 | 59 | 11 | 完整主运行模块；论文图形示例原件保留获取方式 |
| nature-image2ppt | huangjt-academic-writing | 91 | 90 | 67 | 保留完整运行方法与工具 |
| nature-paper-to-patent | huangjt-academic-writing | 69 | 69 | 24 | 保留完整运行方法与工具 |
| nature-paper2ppt | huangjt-academic-writing | 19 | 19 | 1 | 保留完整运行方法与工具 |
| nature-paper2word | huangjt-academic-writing | 6 | 6 | 0 | 保留完整运行方法与工具 |
| nature-polishing | huangjt-academic-writing | 33 | 33 | 0 | 保留完整运行方法与工具 |
| nature-proposal-writer | huangjt-academic-writing | 36 | 36 | 3 | 保留完整运行方法与工具 |
| nature-response | huangjt-academic-writing | 38 | 38 | 3 | 保留完整运行方法与工具 |
| nature-reviewer | huangjt-academic-writing | 21 | 21 | 1 | 保留完整运行方法与工具 |
| nature-shared | huangjt-academic-writing | 21 | 21 | 2 | 保留完整运行方法与工具 |
| nature-statistics | huangjt-academic-writing | 11 | 11 | 0 | 保留完整运行方法与工具 |
| nature-writing | huangjt-academic-writing | 77 | 77 | 0 | 保留完整运行方法与工具 |
| networkx | huangjt-academic-writing | 7 | 7 | 0 | 保留完整运行方法与工具 |
| office-academic-skill | huangjt-academic-writing | 123 | 1 | 32 | 恢复完整模块、脚本、参考与模板 |
| paper-write | huangjt-academic-writing | 28 | 1 | 0 | 恢复完整模块、脚本、参考与模板 |
| peer-review | huangjt-academic-writing | 24 | 24 | 8 | 保留完整运行方法与工具 |
| polars | huangjt-academic-writing | 8 | 8 | 0 | 保留完整运行方法与工具 |
| pptx-posters | huangjt-academic-writing | 21 | 21 | 10 | 保留完整运行方法与工具 |
| pymc | huangjt-academic-writing | 10 | 10 | 4 | 保留完整运行方法与工具 |
| pymoo | huangjt-academic-writing | 14 | 14 | 5 | 保留完整运行方法与工具 |
| research-grants | huangjt-academic-writing | 16 | 16 | 0 | 保留完整运行方法与工具 |
| scholar-evaluation | huangjt-academic-writing | 19 | 19 | 8 | 保留完整运行方法与工具 |
| scientific-schematics | huangjt-academic-writing | 6 | 6 | 3 | 保留完整运行方法与工具 |
| scientific-slides | huangjt-academic-writing | 24 | 24 | 7 | 保留完整运行方法与工具 |
| scientific-visualization | huangjt-academic-writing | 18 | 18 | 8 | 保留完整运行方法与工具 |
| scientific-writing | huangjt-academic-writing | 31 | 31 | 9 | 保留完整运行方法与工具 |
| scikit-learn | huangjt-academic-writing | 11 | 11 | 2 | 保留完整运行方法与工具 |
| seaborn | huangjt-academic-writing | 8 | 8 | 0 | 保留完整运行方法与工具 |
| statistical-analysis | huangjt-academic-writing | 7 | 7 | 1 | 保留完整运行方法与工具 |
| statistical-power | huangjt-academic-writing | 6 | 6 | 2 | 保留完整运行方法与工具 |
| statsmodels | huangjt-academic-writing | 10 | 10 | 0 | 保留完整运行方法与工具 |
| sympy | huangjt-academic-writing | 8 | 8 | 0 | 保留完整运行方法与工具 |
| venue-templates | huangjt-academic-writing | 32 | 32 | 3 | 保留完整运行方法与工具 |

## 仍单独获取的脚本

本地模块合计 979 项脚本/程序模板；当前公开模块合计 940 项。差异 39 项由以下部分组成，并非静默删除：

- 单晶辅助原件 5 项：主技能已包含输入盘点、配体准备、交付核查三项同用途工具；格式诊断与配体 shell 启动原件可 fetch-source crystal，方法与边界写入对应 WORKFLOW。
- figures4papers 27 项特定论文示例脚本：作者原仓库的第三方声明保留独立权利条件；保留绘图类型知识和固定上游获取路径，可 fetch-source nature 取得原资源。
- ARS 维护测试/评测 7 项 Python 文件：不作为日常执行前提；可 fetch-source ars 取得，不删研究工作流。

以上本地原件全部保留，个人完整迁移包同时收录。公开版不会将未分发的脚本宣称为已经安装；完整原件获取后检查实际依赖和用途。

## 原技能库其他条目

原始 252 条处理记录另见 catalog/original-library.json，包含原名、职责、当前归属和脚本索引。78 个原技能融合为内部模块；两个化学辅助和通用能力保留；不相关领域与粉末 XRD 继续归档，原件不删除、不因整理卸载程序。该索引用于发现已有方法，不把归档重新注册成大量活动入口。
