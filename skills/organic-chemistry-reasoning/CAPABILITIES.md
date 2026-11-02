# 有机化学推断与结构工具：方法与工具

本目录同时列出本主技能自身内容及内部模块。按实际任务选入口；统计用于定位资料。

## 主技能方法

- [absorbed-modules.md](<references/absorbed-modules.md>)
- [applied-workflows.md](<references/applied-workflows.md>)
- [core-workflows.md](<references/core-workflows.md>)
- [crystal.md](<references/crystal.md>)
- [experiment-analysis.md](<references/experiment-analysis.md>)
- [formula-ms.md](<references/formula-ms.md>)
- [foundation-and-migration.md](<references/foundation-and-migration.md>)
- [geometry-sterics.md](<references/geometry-sterics.md>)
- [host-compatibility.md](<references/host-compatibility.md>)
- [integrated-methods.md](<references/integrated-methods.md>)
- [literature-mechanism.md](<references/literature-mechanism.md>)
- [nmr-identification.md](<references/nmr-identification.md>)
- [research-decisions.md](<references/research-decisions.md>)
- [runtime.md](<references/runtime.md>)
- [sources.md](<references/sources.md>)
- [system-integration.md](<references/system-integration.md>)
- [task-language.md](<references/task-language.md>)

## 主技能脚本

- [structure_cli.py](<scripts/structure_cli.py>) — Portable structure normalization, drawing, conversion and offline image recognition. Uses RDKit for chemistry and optional MolVec for local OCSR. Recognition produces a candidate; 
- [workbench.py](<scripts/workbench.py>) — Find bundled capabilities and configure a small, machine-local chemistry workbench. Default commands inspect/plan only. setup --apply installs the selected profile; optional solver

## analytical-method-validation

[完整流程](<modules/analytical-method-validation/WORKFLOW.md>)

任务：分析方法验证 定量 校准 回收率 精密度 检出限

### 工具

- [scripts/_catalog.py](<modules/analytical-method-validation/scripts/_catalog.py>)
- [scripts/_common.py](<modules/analytical-method-validation/scripts/_common.py>)
- [scripts/check_accuracy_precision.py](<modules/analytical-method-validation/scripts/check_accuracy_precision.py>)
- [scripts/check_bioanalytical_run.py](<modules/analytical-method-validation/scripts/check_bioanalytical_run.py>)
- [scripts/check_detection_limits.py](<modules/analytical-method-validation/scripts/check_detection_limits.py>)
- [scripts/check_response.py](<modules/analytical-method-validation/scripts/check_response.py>)
- [scripts/compare_methods.py](<modules/analytical-method-validation/scripts/compare_methods.py>)
- [scripts/plan_validation.py](<modules/analytical-method-validation/scripts/plan_validation.py>)

### 参考

- [assets/validation-protocol-template.md](<modules/analytical-method-validation/assets/validation-protocol-template.md>)
- [assets/validation-report-template.md](<modules/analytical-method-validation/assets/validation-report-template.md>)
- [references/compendial-and-clsi.md](<modules/analytical-method-validation/references/compendial-and-clsi.md>)
- [references/framework-selection.md](<modules/analytical-method-validation/references/framework-selection.md>)
- [references/ich-m10-bioanalytical.md](<modules/analytical-method-validation/references/ich-m10-bioanalytical.md>)
- [references/ich-q2r2.md](<modules/analytical-method-validation/references/ich-q2r2.md>)
- [references/source-ledger.md](<modules/analytical-method-validation/references/source-ledger.md>)
- [references/statistics.md](<modules/analytical-method-validation/references/statistics.md>)

## datamol

[完整流程](<modules/datamol/WORKFLOW.md>)

任务：分子 标准化 清洗 转换 数据集

### 参考

- [references/conformers_module.md](<modules/datamol/references/conformers_module.md>)
- [references/core_api.md](<modules/datamol/references/core_api.md>)
- [references/core_workflows.md](<modules/datamol/references/core_workflows.md>)
- [references/descriptors_viz.md](<modules/datamol/references/descriptors_viz.md>)
- [references/fragments_scaffolds.md](<modules/datamol/references/fragments_scaffolds.md>)
- [references/io_module.md](<modules/datamol/references/io_module.md>)
- [references/reactions_data.md](<modules/datamol/references/reactions_data.md>)
- [references/review.md](<modules/datamol/references/review.md>)
- [references/workflow_patterns.md](<modules/datamol/references/workflow_patterns.md>)

## experimental-design

[完整流程](<modules/experimental-design/WORKFLOW.md>)

任务：实验设计 对照 变量 独立重复 批次 交互 DOE

### 工具

- [scripts/doe_designs.py](<modules/experimental-design/scripts/doe_designs.py>)
- [scripts/randomization.py](<modules/experimental-design/scripts/randomization.py>)

### 参考

- [references/design_types.md](<modules/experimental-design/references/design_types.md>)
- [references/factorial_and_doe.md](<modules/experimental-design/references/factorial_and_doe.md>)
- [references/randomization_and_blocking.md](<modules/experimental-design/references/randomization_and_blocking.md>)
- [references/sequential_and_adaptive.md](<modules/experimental-design/references/sequential_and_adaptive.md>)

## hypothesis-generation

[完整流程](<modules/hypothesis-generation/WORKFLOW.md>)

任务：假说 机理推断 可证伪 区分性实验

### 工具

- [scripts/_common.py](<modules/hypothesis-generation/scripts/_common.py>)
- [scripts/audit_evidence_ledger.py](<modules/hypothesis-generation/scripts/audit_evidence_ledger.py>)
- [scripts/check_falsification_controls.py](<modules/hypothesis-generation/scripts/check_falsification_controls.py>)
- [scripts/check_operationalization.py](<modules/hypothesis-generation/scripts/check_operationalization.py>)
- [scripts/generate_preregistration_scaffold.py](<modules/hypothesis-generation/scripts/generate_preregistration_scaffold.py>)
- [scripts/lint_causal_claims.py](<modules/hypothesis-generation/scripts/lint_causal_claims.py>)
- [scripts/validate_hypothesis_schema.py](<modules/hypothesis-generation/scripts/validate_hypothesis_schema.py>)
- [scripts/validate_prediction_matrix.py](<modules/hypothesis-generation/scripts/validate_prediction_matrix.py>)

### 参考

- [assets/preregistration_scaffold_template.md](<modules/hypothesis-generation/assets/preregistration_scaffold_template.md>)
- [references/causal_inference_and_claims.md](<modules/hypothesis-generation/references/causal_inference_and_claims.md>)
- [references/concepts_and_workflow.md](<modules/hypothesis-generation/references/concepts_and_workflow.md>)
- [references/ethics_safety_and_ai.md](<modules/hypothesis-generation/references/ethics_safety_and_ai.md>)
- [references/experimental_design_patterns.md](<modules/hypothesis-generation/references/experimental_design_patterns.md>)
- [references/hypothesis_quality_criteria.md](<modules/hypothesis-generation/references/hypothesis_quality_criteria.md>)
- [references/literature_search_strategies.md](<modules/hypothesis-generation/references/literature_search_strategies.md>)
- [references/preregistration_and_open_science.md](<modules/hypothesis-generation/references/preregistration_and_open_science.md>)
- [references/security_validation.md](<modules/hypothesis-generation/references/security_validation.md>)
- [references/source_ledger.md](<modules/hypothesis-generation/references/source_ledger.md>)
- [references/tool_reference.md](<modules/hypothesis-generation/references/tool_reference.md>)

## medchem

[完整流程](<modules/medchem/WORKFLOW.md>)

任务：药化 筛选 结构警报 分子性质

### 工具

- [scripts/filter_molecules.py](<modules/medchem/scripts/filter_molecules.py>)

### 参考

- [references/api_guide.md](<modules/medchem/references/api_guide.md>)
- [references/rules_catalog.md](<modules/medchem/references/rules_catalog.md>)

## openbabel

[完整流程](<modules/openbabel/WORKFLOW.md>)

任务：结构 格式转换 MOL SDF XYZ SMILES

## organic-chemistry-assistant

[完整流程](<modules/organic-chemistry-assistant/WORKFLOW.md>)

任务：有机 结构识别 画结构 机理 电子箭头 反应式 编辑 SMILES Ketcher

### 参考

- [references/mechanism-graphics.md](<modules/organic-chemistry-assistant/references/mechanism-graphics.md>)
- [references/mechanism-spec.md](<modules/organic-chemistry-assistant/references/mechanism-spec.md>)

## rdkit

[完整流程](<modules/rdkit/WORKFLOW.md>)

任务：结构式 分子式 精确质量 画分子 指纹 亚结构 原子映射

### 工具

- [scripts/molecular_properties.py](<modules/rdkit/scripts/molecular_properties.py>)
- [scripts/similarity_search.py](<modules/rdkit/scripts/similarity_search.py>)
- [scripts/substructure_filter.py](<modules/rdkit/scripts/substructure_filter.py>)

### 参考

- [references/api_reference.md](<modules/rdkit/references/api_reference.md>)
- [references/core_capabilities.md](<modules/rdkit/references/core_capabilities.md>)
- [references/descriptors_reference.md](<modules/rdkit/references/descriptors_reference.md>)
- [references/smarts_patterns.md](<modules/rdkit/references/smarts_patterns.md>)
- [references/workflows_and_best_practices.md](<modules/rdkit/references/workflows_and_best_practices.md>)

## scientific-brainstorming

[完整流程](<modules/scientific-brainstorming/WORKFLOW.md>)

任务：科研思路 脑暴 研究问题 创新

### 工具

- [scripts/_common.py](<modules/scientific-brainstorming/scripts/_common.py>)
- [scripts/evaluate_matrix.py](<modules/scientific-brainstorming/scripts/evaluate_matrix.py>)
- [scripts/session_scaffold.py](<modules/scientific-brainstorming/scripts/session_scaffold.py>)
- [scripts/validate_register.py](<modules/scientific-brainstorming/scripts/validate_register.py>)

### 参考

- [references/brainstorming_methods.md](<modules/scientific-brainstorming/references/brainstorming_methods.md>)
- [references/facilitation_workflows.md](<modules/scientific-brainstorming/references/facilitation_workflows.md>)
- [references/idea_evaluation.md](<modules/scientific-brainstorming/references/idea_evaluation.md>)
- [references/responsible_ai.md](<modules/scientific-brainstorming/references/responsible_ai.md>)
- [references/sources.md](<modules/scientific-brainstorming/references/sources.md>)

## scientific-critical-thinking

[完整流程](<modules/scientific-critical-thinking/WORKFLOW.md>)

任务：证据 竞争解释 批判性思考 因果

### 参考

- [references/common_biases.md](<modules/scientific-critical-thinking/references/common_biases.md>)
- [references/core_capabilities.md](<modules/scientific-critical-thinking/references/core_capabilities.md>)
- [references/evidence_hierarchy.md](<modules/scientific-critical-thinking/references/evidence_hierarchy.md>)
- [references/experimental_design.md](<modules/scientific-critical-thinking/references/experimental_design.md>)
- [references/logical_fallacies.md](<modules/scientific-critical-thinking/references/logical_fallacies.md>)
- [references/review_sources.md](<modules/scientific-critical-thinking/references/review_sources.md>)
- [references/scientific_method.md](<modules/scientific-critical-thinking/references/scientific_method.md>)
- [references/statistical_pitfalls.md](<modules/scientific-critical-thinking/references/statistical_pitfalls.md>)

## uncertainty-and-units

[完整流程](<modules/uncertainty-and-units/WORKFLOW.md>)

任务：不确定性 单位 有效数字 误差传播

### 工具

- [scripts/_common.py](<modules/uncertainty-and-units/scripts/_common.py>)
- [scripts/audit_units.py](<modules/uncertainty-and-units/scripts/audit_units.py>)
- [scripts/check_plausibility.py](<modules/uncertainty-and-units/scripts/check_plausibility.py>)
- [scripts/convert_units.py](<modules/uncertainty-and-units/scripts/convert_units.py>)
- [scripts/format_result.py](<modules/uncertainty-and-units/scripts/format_result.py>)
- [scripts/propagate_uncertainty.py](<modules/uncertainty-and-units/scripts/propagate_uncertainty.py>)
- [scripts/uncertainty_budget.py](<modules/uncertainty-and-units/scripts/uncertainty_budget.py>)

### 参考

- [references/domain-conversions.md](<modules/uncertainty-and-units/references/domain-conversions.md>)
- [references/gum-methodology.md](<modules/uncertainty-and-units/references/gum-methodology.md>)
- [references/pint-recipes.md](<modules/uncertainty-and-units/references/pint-recipes.md>)
- [references/plausibility-scales.md](<modules/uncertainty-and-units/references/plausibility-scales.md>)
- [references/reporting-rules.md](<modules/uncertainty-and-units/references/reporting-rules.md>)
- [references/review.md](<modules/uncertainty-and-units/references/review.md>)
- [references/uncertainties-recipes.md](<modules/uncertainty-and-units/references/uncertainties-recipes.md>)
