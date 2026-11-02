# 单晶解析与精修：完整能力目录

方法、脚本、参考和模板均按任务加载。本目录用于发现能力，完整操作流程在各 WORKFLOW 内；软件未安装时保留知识并按基础迁移说明补齐。

[实操与联动](references/applied-workflows.md) · [基础与迁移](references/foundation-and-migration.md)

## 主技能自带工具

- [01_diagnose.py](scripts/01_diagnose.py) — 01_diagnose.py — SCXRD 数据与模型诊断（动手精修之前必跑） 检查内容： 1. 目录清点：ins / res / hkl / lst / cif 是否齐全，res/lst 是否 0 字节 2. 修复隐患：EXTI+SWAT 冲突、TITL 与 LATT 空间群不一致、UNIT 与原子表不匹配 3. 数据质量：Rint / Rsigma /
- [03_run.py](scripts/03_run.py) — 03_run.py — 精修运行器（议题驱动 + 归档留痕） 核心设计（议题驱动的精修流程）： * 每轮 = 一个议题（氢修正/空间群/无序/权重/孪晶/ADP 稳定性），不是机械重跑 * SHELXL 在【本地临时目录】运行，结束后把产物拷回归档目录 —— 避开 Synology/OneDrive 同步锁造成的 "ReplaceFileW EIO" * 保
- [04_summarize.py](scripts/04_summarize.py) — 04_summarize.py — 汇总所有精修轮次，生成可读的"精修历程表" 读取归档目录下的 history.csv（由 03_run.py 写）或直接扫描各轮 lst， 输出： * 控制台表格 * refinement_history.md（含结论段模板） * refinement_history.csv（可直接进 SI） 用法: python 04_
- [06_hydrogen_plan.py](scripts/06_hydrogen_plan.py) — 06_hydrogen_plan.py — 依据连接性自动规划氢原子（HFIX 分组） 来自多次模型精修与交付实践： * 按共价阈值建连接表 * 每个碳按 价键数 + 是否不饱和（C=O/C=C 等）推断应有的 H 数 * 生成 HFIX 分组：13(叔 CH) / 23(仲 CH2) / 43(芳或烯 CH) / 137(甲基，最优取向) * 交叉核对 U
- [07_symmetry_check.py](scripts/07_symmetry_check.py) — 07_symmetry_check.py — 空间群与伪对称判定（竞争精修的定量判据） 来自多次对称初筛与模型比较实践： 仅凭 wR2 判断空间群常常被过度参数化误导，需先做几何层面的定量检验： 1. 反演中心扫描：网格搜索最优平移 tau，使 -r+tau 与另一原子（同元素） 的匹配率最高。匹配率高（>80% within 0.5 A）-> 强烈提示中心
- [08_cif.py](scripts/08_cif.py) — CIF tools: validate (limited consistency checks), prepare (Gemmi metadata merge), upload (explicit diagnostic copy only). Missing metadata stays unknown. prepare --res/--lst are re
- [09_checkcif.py](scripts/09_checkcif.py) — Submit checkCIF, record actual mode/input hashes, and create evidence-free VRF drafts. Network fallback may produce CIF-only validation; inspect the saved report.
- [10_delivery.py](scripts/10_delivery.py) — 10_delivery.py — 交付打包：文件归集 + SHA256 + 交付说明 + zip 来自多次模型精修与交付实践： * 把定稿文件按固定命名归集到 01_upload / 02_validation / 03_refinement_records * 计算 SHA256 并写入 DELIVERY_SHA256.csv * 生成 DELIVERY_
- [dials_absorption.py](scripts/dials_absorption.py) — Verify physical-model components and report absorption-only relative factor limits.
- [dials_audit.py](scripts/dials_audit.py) — Dataset mapping, geometry residuals and diagnostic equivalent-intensity agreement.
- [dials_common.py](scripts/dials_common.py) — DIALS identifier validation and input provenance; import DIALS only on demand.
- [dials_screen.py](scripts/dials_screen.py) — Flag observations using joint position/intensity evidence; optionally filter unscaled data.
- [dials_stage.py](scripts/dials_stage.py) — Run one explicitly chosen DIALS command in a new, audited directory.
- [inventory_crystal_input.py](scripts/inventory_crystal_input.py) — Read-only inventory. Frame candidates do not establish reintegration capability.
- [prepare_ligand.py](scripts/prepare_ligand.py) — Validate one ligand; optional derived reference geometry is not experimental data.
- [test_dials_helpers.py](scripts/test_dials_helpers.py) — Offline behavioral tests with synthetic observations; no private data or network.
- [test_regressions.py](scripts/test_regressions.py) — Offline regression checks: no scientific model selection and no network calls.
- [test_solution_helpers.py](scripts/test_solution_helpers.py) — Synthetic integration tests; no diffraction data, GUI, or network.
- [utf8_console.py](scripts/utf8_console.py) — Use UTF-8 for CLI logs on Windows and redirected host streams.
- [validate_crystal_package.py](scripts/validate_crystal_package.py) — Audit files, basenames, ABIN/include dependencies and optional recorded hashes. This does not validate a structure, report scientific acceptance or run external programs.
- [xtal_core.py](scripts/xtal_core.py) — xtal_core.py — SCXRD 精修工具箱的通用核心库 设计原则：不硬编码任何化合物相关常量（晶胞、元素、原子名）， 全部从 ins / res / cif / hkl 文件读取。 主要能力： * 解析 SHELXL 的 ins/res 原子记录（正确处理 '=' 续行） * 从 ins 的 SFAC/UNIT/LATT/SYMM 读取元素、计数、

## solve-single-crystal

[完整工作流](modules/solve-single-crystal/WORKFLOW.md)

单晶辅助知识与原始工具获取

随包脚本 0 项；参考文档 0 项；模板/示例 0 项。
