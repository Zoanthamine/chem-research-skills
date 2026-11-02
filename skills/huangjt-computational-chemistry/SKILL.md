---
name: huangjt-computational-chemistry
description: "计算化学主技能。用于核磁计算、化学位移和 J 耦合、标度法内标外标、构象搜索、动力学退火、Gaussian ORCA xTB GROMACS、前线轨道、TS IRC，以及本地或集群任务构建、提交前检查与计算经验沉淀。"
---

# Computational chemistry: knowledge, local, cluster

## Choose the smallest mode that fulfills the request

|Mode|Use when|Load|
|---|---|---|
|`knowledge`|Explain/review methods, spectra, inputs, costs or failures; execution not requested|[Common principles](references/common.md), then relevant topic only|
|`local`|User requests local sampling, optimization, NMR/J or local file post-processing|Common + [local runtime](references/local-runtime.md) + [conformers](references/local-conformers.md) and/or [NMR/J](references/nmr-coupling.md)|
|`cluster`|User requests remote jobs, scheduler checks, Gaussian/ORCA precision refinement or TS/IRC|Common + [cluster workflow](references/cluster-workflow.md); add NMR/J only if needed|

The user may explicitly say “knowledge only”, “use local xTB”, or “use cluster”. Otherwise infer mode from the requested action; clarify only a material ambiguity. Knowledge-only mode does not probe programs, load a compute backend, connect SSH, install software or submit jobs. Reading supplied files/local references is allowed. Local and cluster execution require the user's task to authorize that work; loading this skill alone grants no compute authorization.

## Chinese trigger phrases and execution gate

Select this skill in computational-chemistry context for: 计算、核磁计算、提交计算/提交任务、本地提交、集群提交、构建/建立本地任务、准备集群任务、检查任务/检查输入/提交前检查、构象/构象搜索、动力学搜索、模拟退火/退火搜索、GROMACS、xTB、Gaussian/高斯、ORCA、过渡态/IRC、耦合常数/同碳耦合、标度法/校准，以及内标/外标。Common speech-to-text variants such as “标注法” can mean 标度法; infer only when context supports it. Inner/external referencing and computed scaling are different concepts; clarify a material ambiguity instead of silently applying a fit. Bare generic words like 计算 or 提交 outside chemistry do not trigger this skill.

Before **every local computational launch or cluster submission**, including retries and changed decks, follow [task preflight](references/task-preflight.md) and save the result with the project. This is mandatory input/scope/resource/duplicate-job checking, not a new confirmation requirement. Do not launch before relevant checks pass. Reuse valid evidence without needlessly repeating costly tests.

When asked to “沉淀、记住、总结这次计算、更新技能、整理成skill、下次照此流程”, follow [experience maintenance](references/experience-maintenance.md), classify verified lessons into shared/local/cluster topics, and update the existing skill and maintained shareable package. A maintenance request does not resume calculations or monitoring.

## Common workflow

1. Identify endpoint and inspect actual structure, atom map, charge/spin, solvent, temperature, selected method and conformer/resource cap.
2. Load only necessary references. Installed local software, chemistry MCP/plugin, SSH and proprietary licenses are separate capabilities; never imply they exist from skill installation.
3. Prepare a manifest and stage-specific inputs. Preserve original structures/logs/IDs. Review the concrete action before execution where required; do not invent new permission gates for already-authorized routine steps.
4. Validate chemical identity and program results before the next stage. Keep electronic energies, thermal corrections, Gibbs energies, shieldings, shifts and J values distinct.
5. Deliver original files, mapping, raw and processed values, method/solvent/calibration/weights and limitations. Record incomplete work and actual last-check time.

## Optional modules and reusable assets

- [NMR and coupling](references/nmr-coupling.md): Bally general H–H, DU4 CH2 geminal ²JHH, exact basis assets, per-method scaling/weighting; do not combine the two estimators.
- [Gaussian and scheduler pitfalls](references/operations-lessons.md): negligible-force termination, blank lines, CRLF hashes, unknown qsub acceptance, TS validation.
- [Portable post-processing CLI](references/postprocess-cli.md): standard-library Python script, explicit raw FC CSV and chemical-environment mapping, optional normalized weights; no Gaussian/xTB required.
- `assets/basis/` contains verified C/H/O Gaussian Gen basis blocks for the two FC fits; `assets/local-profile.example.json` is a portable configuration example, not live credentials or a job submission.
- A separate teaching/retrieval layer `huangjt-computational-chemistry-assistant` may retrieve local literature if installed; it should obey this skill's selected execution mode and does not replace input inspection.

## Budget and scientific boundaries

- Preserve the active conformer cap (Huangjt project convention: at most 6 DFT candidates unless changed by the user). Fine clustering does not lift that cap.
- Favor existing verified workflows and requested simple keywords; do not silently expand method cost or cancel endpoints when changing a TS approach.
- A minimum requires convergence and appropriate frequency evidence; a quick optimization without frequency must be labeled unverified as a minimum. A TS requires one relevant imaginary mode and correct path/endpoints.
- Capped conformer coverage is within the computed ensemble, not proof of global completeness. Lowest closed-shell conformer does not establish the globally lowest derived radical.
- Match calibration to method, basis, geometry protocol, solvent and shielding conventions. Use “shielding only” when a matching calibration is missing.


## 协作与分享

任务涉及跨领域判断或需要迁移分享时，读 [协作与迁移](references/system-integration.md)。保持一个主工作流，按证据需要衔接其他模块。

## 已融合的专业能力

先读 [融合方法](references/integrated-methods.md) 选择会改变当前判断的分析；具体工具和详细流程见 [内部模块](references/absorbed-modules.md)。模块按需加载，不再把源技能当作独立任务入口。自然语言场景见 [任务说法](references/task-language.md)。

## Codex 与 DSH

两个宿主共用本技能的方法、证据与工具。迁移或工具名称不同先读 [宿主适配](references/host-compatibility.md)，按实际文件、命令、检索及文档能力完成任务，不依赖Codex私有API。

## 完整方法、工具与迁移

需要找回旧模块、选择实际脚本、模板或迁移软件时，读 [完整能力目录](CAPABILITIES.md)；需要把专业方法连成当前任务时，读 [实操与联动](references/applied-workflows.md)。新电脑和结构基础能力先读 [基础与迁移](references/foundation-and-migration.md)。保留原有方法、工具和资料，按需读取相关分支；减少的是重复入口。

## 本核心的基础工作流

处理实际数据、构象/核磁任务或有机分析时，先按 [基础功能与联动](references/core-workflows.md) 定位输入和可执行入口；[完整目录](CAPABILITIES.md) 同时列出本主技能自己的方法、脚本和内部扩展。
