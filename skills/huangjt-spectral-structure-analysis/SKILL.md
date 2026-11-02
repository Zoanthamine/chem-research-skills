---
name: huangjt-spectral-structure-analysis
description: "解谱与结构鉴定主技能。用于解谱看谱、核磁归属、粗谱、原料或目标峰在哪、杂质副产物、分子式加合离子、同位素、失落碳信号、重叠峰与耦合、NOE 距离及多谱候选对照；含 NMR HRMS LCMS IR UV CD。"
---

# 波谱与结构分析

先查样品来源、实验元数据、软件能力，再选择处理。优先文件/脚本/API；专有格式检查转换器与已授权软件。随包安装不表示商业软件、OCSR模型、数据库或集群已配置。

## 默认触发与使用偏好
用户明确希望：每次化学波谱解读，主动使用本技能或其中适用的方法，不必等待点名。含口语、错别字“解普”，以及“这个峰是什么”“看一下这张谱”“归属一下”“判断是不是目标产物”等有谱图上下文的请求。单纯提到“谱”而实际讨论音乐、族谱等不触发。

先做轻量的样品/格式/轴单位/来源核对，然后只加载任务需要的参考。普通问题可以直接采用方法回答；多谱联合鉴定再展开完整证据链。自动选用不意味着每次启动全部软件、处理全部谱种或生成完整报告。

各谱种按实际能力处理：NMR用直接配对、片段与长程/空间相关；MS用电荷/加合离子/精确质量/碎片；IR与拉曼核对波数、基线、吸收/透过/散射信号定义和振动峰；UV-Vis核对波长、吸光度/透过率、溶剂和浓度条件；CD/ECD保留符号、单位及与UV/构象的联系。NMR的耦合、HMBC和NOE距离方法不能套用到其他谱种。专门后端缺失时使用有支持的检查与定性推理，并说明功能边界。

## 按任务加载
- 实验联合归属、信号增强、重叠分峰和NOE强度：读 [实验流程](references/experimental-workflow.md)。
- 候选结构、计算位移/J、构象与质量对照：读 [候选判断](references/candidate-comparison.md)。
- 新电脑或新增能力：读 [迁移与能力矩阵](references/portability.md)，运行 `python scripts/evidence_cli.py doctor`。
- Chemical-analyses-skills来源与调用边界：读 [上游整合](references/upstream-integration.md)。

## 工作约定
建立原始数据、处理版本、信号ID、结构原子编号、逐证据判断、候选和最终结论的对应关系。实验位置、条件拟合、计算预测、用户确认分列。用户确认可结束候选选择，但不能倒写历史为算法独立确证，也不能把未闭合逐碳归属自动升格。

与现有技能配合：nmrglue负责受支持FID处理；organic-chemistry-assistant负责结构/反应；huangjt-computational-chemistry负责量化方法；spectrum-analyzer负责数值谱图。缺少这些技能时按本包参考与本地数值脚本继续有支持的工作，不伪造外部功能。PPT/XLSX使用目标环境的文档技能；本包不捆绑专属桌面运行时。

## 内置工具
`scripts/evidence_cli.py`提供依赖检查、分子式/加合离子、校准NPZ的双向有符号NOE积分、带权r^-6有效距离和数值自检。运行 `--help`；输入模式见迁移说明。脚本仅执行数值运算，不做结构自动归属。输入文件只读，输出到指定新文件。

## 协作与分享

任务涉及跨领域判断或需要迁移分享时，读 [协作与迁移](references/system-integration.md)。保持一个主工作流，按证据需要衔接其他模块。

## 已融合的专业能力

先读 [融合方法](references/integrated-methods.md) 选择会改变当前判断的分析；具体工具和详细流程见 [内部模块](references/absorbed-modules.md)。模块按需加载，不再把源技能当作独立任务入口。自然语言场景见 [任务说法](references/task-language.md)。

## Codex 与 DSH

两个宿主共用本技能的方法、证据与工具。迁移或工具名称不同先读 [宿主适配](references/host-compatibility.md)，按实际文件、命令、检索及文档能力完成任务，不依赖Codex私有API。

## 完整方法、工具与迁移

需要找回旧模块、选择实际脚本、模板或迁移软件时，读 [完整能力目录](CAPABILITIES.md)；需要把专业方法连成当前任务时，读 [实操与联动](references/applied-workflows.md)。新电脑和结构基础能力先读 [基础与迁移](references/foundation-and-migration.md)。保留原有方法、工具和资料，按需读取相关分支；减少的是重复入口。
