# 有机化学推断与结构工具：完整能力目录

方法、脚本、参考和模板均按任务加载。本目录用于发现能力，完整操作流程在各 WORKFLOW 内；软件未安装时保留知识并按基础迁移说明补齐。

[实操与联动](references/applied-workflows.md) · [基础与迁移](references/foundation-and-migration.md)

## 主技能自带工具

- [structure_cli.py](scripts/structure_cli.py) — Portable structure normalization, drawing, conversion and offline image recognition. Uses RDKit for chemistry and optional MolVec for local OCSR. Recognition produces a candidate; 
- [workbench.py](scripts/workbench.py) — Find bundled capabilities and configure a small, machine-local chemistry workbench. Default commands inspect/plan only. setup --apply installs the selected profile; optional solver

## analytical-method-validation

[完整工作流](modules/analytical-method-validation/WORKFLOW.md)

Plans, executes, and documents validation, verification, and transfer of analytical procedures under the governing framework - ICH Q2(R2) and Q14, USP <1220>/<1225>/<1226>, ICH M10 bioanalytical, CLSI EP, or ISO/IEC 17025. Use for HPLC, LC-MS/MS, GC, CE, ICP-MS, dissolution, qNMR, qPCR, NIR, and ligand binding or cell-based assays whenever the question is whether a procedure is fit for its intended purpose. Triggers include "method validation", "analytical method validation", "AMV", "validation protocol", "acceptance criteria", "linearity", "reportable range", "accuracy and precision", "repeatability", "intermediate precision", "recovery", "LOD", "LOQ", "detection limit", "quantitation limit", "specificity", "robustness", "method transfer", "method comparison", "Deming", "Passing-Bablok", "Bland-Altman", "equivalence testing", "OOS investigation", "ICH Q2", "Q2(R2)", "Q14", "USP 1225", "ICH M10", "incurred sample reanalysis", "ISR", "CLSI EP", and any request to show that an assay works.

随包脚本 8 项；参考文档 8 项；模板/示例 0 项。

### 脚本

- [scripts/_catalog.py](modules/analytical-method-validation/scripts/_catalog.py) — Framework catalogue for analytical method validation. Content sourced 2026-09-30 from the freely published ICH guidelines, which ICH licenses for reuse with acknowledgement. Compen
- [scripts/_common.py](modules/analytical-method-validation/scripts/_common.py) — Shared statistics and I/O for analytical method validation checks. Standard library only. Every distribution function here is implemented from the regularised incomplete beta and g
- [scripts/check_accuracy_precision.py](modules/analytical-method-validation/scripts/check_accuracy_precision.py) — Evaluate accuracy and precision per ICH Q2(R2) 3.3. Accuracy is reported as mean recovery with a confidence interval, which is what Q2(R2) 3.3.1.4 asks for -- a bare mean is not su
- [scripts/check_bioanalytical_run.py](modules/analytical-method-validation/scripts/check_bioanalytical_run.py) — Apply ICH M10 acceptance criteria to a bioanalytical run or an ISR dataset. Chromatographic assays and ligand binding assays carry DIFFERENT numeric criteria in ICH M10, and confla
- [scripts/check_detection_limits.py](modules/analytical-method-validation/scripts/check_detection_limits.py) — Estimate DL and QL with supported approaches from ICH Q2(R2) 3.2.3. Supported estimates can disagree because they use different response-variation data. Reporting one number withou
- [scripts/check_response.py](modules/analytical-method-validation/scripts/check_response.py) — Evaluate a calibration response (linearity) the way ICH Q2(R2) 3.2.2 asks. Reports what the guideline asks to be reported -- slope, intercept, coefficient of determination, and an 
- [scripts/compare_methods.py](modules/analytical-method-validation/scripts/compare_methods.py) — Compare two analytical procedures for a transfer, bridging, or bias study. Uses the regressions that belong to method comparison -- Deming and Passing-Bablok, which allow error in 
- [scripts/plan_validation.py](modules/analytical-method-validation/scripts/plan_validation.py) — Design a validation study: which framework, which tests, what study layout. Answers the first question of any validation exercise -- what am I required to demonstrate, and with how

### 参考

- [assets/validation-protocol-template.md](modules/analytical-method-validation/assets/validation-protocol-template.md)
- [assets/validation-report-template.md](modules/analytical-method-validation/assets/validation-report-template.md)
- [references/compendial-and-clsi.md](modules/analytical-method-validation/references/compendial-and-clsi.md)
- [references/framework-selection.md](modules/analytical-method-validation/references/framework-selection.md)
- [references/ich-m10-bioanalytical.md](modules/analytical-method-validation/references/ich-m10-bioanalytical.md)
- [references/ich-q2r2.md](modules/analytical-method-validation/references/ich-q2r2.md)
- [references/source-ledger.md](modules/analytical-method-validation/references/source-ledger.md)
- [references/statistics.md](modules/analytical-method-validation/references/statistics.md)

## datamol

[完整工作流](modules/datamol/WORKFLOW.md)

Pythonic wrapper around RDKit with simplified interface and sensible defaults. Preferred for standard drug discovery including SMILES parsing, standardization, descriptors, fingerprints, clustering, 3D conformers, parallel processing. Returns native rdkit.Chem.Mol objects. For advanced control or custom parameters, use rdkit directly.

随包脚本 0 项；参考文档 9 项；模板/示例 0 项。

### 参考

- [references/conformers_module.md](modules/datamol/references/conformers_module.md)
- [references/core_api.md](modules/datamol/references/core_api.md)
- [references/core_workflows.md](modules/datamol/references/core_workflows.md)
- [references/descriptors_viz.md](modules/datamol/references/descriptors_viz.md)
- [references/fragments_scaffolds.md](modules/datamol/references/fragments_scaffolds.md)
- [references/io_module.md](modules/datamol/references/io_module.md)
- [references/reactions_data.md](modules/datamol/references/reactions_data.md)
- [references/review.md](modules/datamol/references/review.md)
- [references/workflow_patterns.md](modules/datamol/references/workflow_patterns.md)

## experimental-design

[完整工作流](modules/experimental-design/WORKFLOW.md)

Designs experiments and studies BEFORE data is collected — choosing a design, randomizing, blocking, and laying out treatment combinations so results are interpretable. Use whenever someone is planning a study, asks how to assign subjects/samples to groups, mentions randomization, blocking, stratification, controls, factorial or fractional-factorial designs, design of experiments (DOE), screening many factors, response-surface optimization, crossover or repeated-measures or split-plot designs, cluster/group randomization, Latin squares, plate layouts, batch/run-order effects, replication vs. pseudoreplication, or sequential/adaptive/group-sequential designs. Trigger even for informal phrasings like "how should I set up this experiment", "how do I avoid confounding", "what's the best way to test these 6 factors", or "assign these mice to conditions". For computing the sample size or power once the design is chosen, use statistical-power; for analyzing data already collected, use statistical-analysis.

随包脚本 2 项；参考文档 4 项；模板/示例 0 项。

### 脚本

- [scripts/doe_designs.py](modules/experimental-design/scripts/doe_designs.py) — Design-of-experiments (DOE) matrices as labeled, decoded pandas DataFrames. pydoe returns designs in *coded* units (-1/+1, or 0..k-1). Researchers want the design in *real* factor 
- [scripts/randomization.py](modules/experimental-design/scripts/randomization.py) — Reproducible randomization / allocation schedules for experiments and trials. Randomization is what licenses causal inference: it breaks the link between treatment assignment and a

### 参考

- [references/design_types.md](modules/experimental-design/references/design_types.md)
- [references/factorial_and_doe.md](modules/experimental-design/references/factorial_and_doe.md)
- [references/randomization_and_blocking.md](modules/experimental-design/references/randomization_and_blocking.md)
- [references/sequential_and_adaptive.md](modules/experimental-design/references/sequential_and_adaptive.md)

## hypothesis-generation

[完整工作流](modules/hypothesis-generation/WORKFLOW.md)

Formulates evidence-bounded scientific questions, candidate hypotheses, rival explanations, causal or associational claims, discriminating predictions, measurements, and preregistration-ready analysis plans. Used when turning observations or preliminary findings into transparent, testable research plans without treating hypotheses as facts.

随包脚本 8 项；参考文档 11 项；模板/示例 4 项。

### 脚本

- [scripts/_common.py](modules/hypothesis-generation/scripts/_common.py) — Shared, dependency-free safety helpers for local hypothesis CLIs.
- [scripts/audit_evidence_ledger.py](modules/hypothesis-generation/scripts/audit_evidence_ledger.py) — Audit a local evidence ledger and dated search boundary without networking.
- [scripts/check_falsification_controls.py](modules/hypothesis-generation/scripts/check_falsification_controls.py) — Audit falsifiers, discriminating tests, nulls, and controls without scoring.
- [scripts/check_operationalization.py](modules/hypothesis-generation/scripts/check_operationalization.py) — Audit a local operationalization and measurement checklist without scoring.
- [scripts/generate_preregistration_scaffold.py](modules/hypothesis-generation/scripts/generate_preregistration_scaffold.py) — Generate a deterministic local Markdown preregistration scaffold.
- [scripts/lint_causal_claims.py](modules/hypothesis-generation/scripts/lint_causal_claims.py) — Lexically lint causal versus associational claims in bounded Markdown.
- [scripts/validate_hypothesis_schema.py](modules/hypothesis-generation/scripts/validate_hypothesis_schema.py) — Validate a structured hypothesis record without judging scientific merit.
- [scripts/validate_prediction_matrix.py](modules/hypothesis-generation/scripts/validate_prediction_matrix.py) — Validate a prediction/rival-hypothesis CSV without ranking candidates.

### 参考

- [assets/preregistration_scaffold_template.md](modules/hypothesis-generation/assets/preregistration_scaffold_template.md)
- [references/causal_inference_and_claims.md](modules/hypothesis-generation/references/causal_inference_and_claims.md)
- [references/concepts_and_workflow.md](modules/hypothesis-generation/references/concepts_and_workflow.md)
- [references/ethics_safety_and_ai.md](modules/hypothesis-generation/references/ethics_safety_and_ai.md)
- [references/experimental_design_patterns.md](modules/hypothesis-generation/references/experimental_design_patterns.md)
- [references/hypothesis_quality_criteria.md](modules/hypothesis-generation/references/hypothesis_quality_criteria.md)
- [references/literature_search_strategies.md](modules/hypothesis-generation/references/literature_search_strategies.md)
- [references/preregistration_and_open_science.md](modules/hypothesis-generation/references/preregistration_and_open_science.md)
- [references/security_validation.md](modules/hypothesis-generation/references/security_validation.md)
- [references/source_ledger.md](modules/hypothesis-generation/references/source_ledger.md)
- [references/tool_reference.md](modules/hypothesis-generation/references/tool_reference.md)

### 模板与示例

- [assets/falsification_controls_template.json](modules/hypothesis-generation/assets/falsification_controls_template.json)
- [assets/hypothesis_record_template.json](modules/hypothesis-generation/assets/hypothesis_record_template.json)
- [assets/operationalization_template.json](modules/hypothesis-generation/assets/operationalization_template.json)
- [assets/search_boundary_template.json](modules/hypothesis-generation/assets/search_boundary_template.json)

## medchem

[完整工作流](modules/medchem/WORKFLOW.md)

Applies medicinal chemistry filters for compound triage, using drug-likeness rules (Lipinski, Veber, CNS), structural alert catalogs (PAINS, NIBR, ChEMBL), complexity metrics, and the medchem query language for library filtering.

随包脚本 1 项；参考文档 2 项；模板/示例 0 项。

### 脚本

- [scripts/filter_molecules.py](modules/medchem/scripts/filter_molecules.py) — Batch molecular filtering using the medchem library. Usage: uv run python filter_molecules.py input.csv --rules rule_of_five,rule_of_cns --pains --output filtered.csv uv run python

### 参考

- [references/api_guide.md](modules/medchem/references/api_guide.md)
- [references/rules_catalog.md](modules/medchem/references/rules_catalog.md)

## openbabel

[完整工作流](modules/openbabel/WORKFLOW.md)

A versatile CLI tool for converting molecular file formats, generating 3D atomic coordinates from SMILES, rendering 2D chemical structure images, and preparing or extracting structures for computational workflows. USE WHEN you need to convert between chemical file formats (e.g., xyz, pdb, mol, smi, gjf), generate 3D structures from SMILES using `--gen3d`, render molecule images (PNG/SVG), or extract geometries from simulation logs to build new inputs.


随包脚本 0 项；参考文档 0 项；模板/示例 0 项。

## organic-chemistry-assistant

[完整工作流](modules/organic-chemistry-assistant/WORKFLOW.md)

本地 codex-chem CLI MCP 工具接口。用于明确需要结构标准化、SMILES SDF 转换、分子绘图、结构编辑或化学工具数值操作的任务；有机机理和实验结果讨论优先 organic-chemistry-reasoning。

随包脚本 0 项；参考文档 2 项；模板/示例 3 项。

### 参考

- [references/mechanism-graphics.md](modules/organic-chemistry-assistant/references/mechanism-graphics.md)
- [references/mechanism-spec.md](modules/organic-chemistry-assistant/references/mechanism-spec.md)

### 模板与示例

- [assets/cyclohexanone.mechanism.json](modules/organic-chemistry-assistant/assets/cyclohexanone.mechanism.json)
- [assets/sn2.mechanism.json](modules/organic-chemistry-assistant/assets/sn2.mechanism.json)
- [assets/sn2_skeletal.mechanism.json](modules/organic-chemistry-assistant/assets/sn2_skeletal.mechanism.json)

## rdkit

[完整工作流](modules/rdkit/WORKFLOW.md)

Cheminformatics toolkit for fine-grained molecular control. SMILES/SDF parsing, descriptors (MW, LogP, TPSA), fingerprints, substructure search, 2D/3D generation, similarity, reactions. For standard workflows with simpler interface, use datamol (wrapper around RDKit). Use rdkit for advanced control, custom sanitization, specialized algorithms.

随包脚本 3 项；参考文档 5 项；模板/示例 0 项。

### 脚本

- [scripts/molecular_properties.py](modules/rdkit/scripts/molecular_properties.py) — Molecular Properties Calculator Calculate comprehensive molecular properties and descriptors for molecules. Supports single molecules or batch processing from files. Usage: python 
- [scripts/similarity_search.py](modules/rdkit/scripts/similarity_search.py) — Molecular Similarity Search Perform fingerprint-based similarity screening against a database of molecules. Supports multiple fingerprint types and similarity metrics. Usage: pytho
- [scripts/substructure_filter.py](modules/rdkit/scripts/substructure_filter.py) — Substructure Filter Filter molecules based on substructure patterns using SMARTS. Supports inclusion and exclusion filters, and custom pattern libraries. Usage: python substructure

### 参考

- [references/api_reference.md](modules/rdkit/references/api_reference.md)
- [references/core_capabilities.md](modules/rdkit/references/core_capabilities.md)
- [references/descriptors_reference.md](modules/rdkit/references/descriptors_reference.md)
- [references/smarts_patterns.md](modules/rdkit/references/smarts_patterns.md)
- [references/workflows_and_best_practices.md](modules/rdkit/references/workflows_and_best_practices.md)

## scientific-brainstorming

[完整工作流](modules/scientific-brainstorming/WORKFLOW.md)

Facilitates evidence-aware scientific ideation with independent generation, structured discussion, explicit assumptions, transparent evaluation, adversarial review, and decision logs. Use for early-stage research brainstorming or prioritizing candidate directions; hand off empirical validation, study design, ethics or regulatory review, and clinical questions to appropriate experts or skills.

随包脚本 4 项；参考文档 5 项；模板/示例 0 项。

### 脚本

- [scripts/_common.py](modules/scientific-brainstorming/scripts/_common.py) — Shared standard-library safety helpers for brainstorming CLIs.
- [scripts/evaluate_matrix.py](modules/scientific-brainstorming/scripts/evaluate_matrix.py) — Calculate a transparent weighted idea matrix with sensitivity analysis.
- [scripts/session_scaffold.py](modules/scientific-brainstorming/scripts/session_scaffold.py) — Generate a deterministic JSON scaffold for a brainstorming session.
- [scripts/validate_register.py](modules/scientific-brainstorming/scripts/validate_register.py) — Validate brainstorming idea and assumption registers structurally.

### 参考

- [references/brainstorming_methods.md](modules/scientific-brainstorming/references/brainstorming_methods.md)
- [references/facilitation_workflows.md](modules/scientific-brainstorming/references/facilitation_workflows.md)
- [references/idea_evaluation.md](modules/scientific-brainstorming/references/idea_evaluation.md)
- [references/responsible_ai.md](modules/scientific-brainstorming/references/responsible_ai.md)
- [references/sources.md](modules/scientific-brainstorming/references/sources.md)

## scientific-critical-thinking

[完整工作流](modules/scientific-critical-thinking/WORKFLOW.md)

Evaluates scientific claims and evidence quality. Applies to experimental design validity, biases and confounders, statistical interpretation, evidence grading frameworks (GRADE, Cochrane Risk of Bias), and teaching critical analysis. Supports evidence appraisal and identifying flaws; formal peer review writing belongs to peer-review.

随包脚本 0 项；参考文档 8 项；模板/示例 0 项。

### 参考

- [references/common_biases.md](modules/scientific-critical-thinking/references/common_biases.md)
- [references/core_capabilities.md](modules/scientific-critical-thinking/references/core_capabilities.md)
- [references/evidence_hierarchy.md](modules/scientific-critical-thinking/references/evidence_hierarchy.md)
- [references/experimental_design.md](modules/scientific-critical-thinking/references/experimental_design.md)
- [references/logical_fallacies.md](modules/scientific-critical-thinking/references/logical_fallacies.md)
- [references/review_sources.md](modules/scientific-critical-thinking/references/review_sources.md)
- [references/scientific_method.md](modules/scientific-critical-thinking/references/scientific_method.md)
- [references/statistical_pitfalls.md](modules/scientific-critical-thinking/references/statistical_pitfalls.md)

## uncertainty-and-units

[完整工作流](modules/uncertainty-and-units/WORKFLOW.md)

Tracks physical units and propagates measurement uncertainty in scientific calculations using pint and uncertainties. Use for unit conversion and dimensional checking, GUM uncertainty budgets, Type A and Type B evaluation, coverage factors and expanded uncertainty, Monte Carlo propagation, significant-figure and plus-minus reporting, error propagation through curve fits, CODATA constants, auditing Python code for stripped units or broken uncertainty propagation, and order-of-magnitude plausibility checks using dimensionless groups (Reynolds, Peclet, Damkohler, Knudsen, Biot, Womersley), characteristic scales such as diffusion time or Debye length, and observed magnitude ranges. Trigger on "is this number physically reasonable", "sanity check these units", "what regime is this flow in", or a result that looks off by orders of magnitude.

随包脚本 7 项；参考文档 7 项；模板/示例 0 项。

### 脚本

- [scripts/_common.py](modules/uncertainty-and-units/scripts/_common.py) — Shared, standard-library-first helpers for the uncertainty and unit CLIs.
- [scripts/audit_units.py](modules/uncertainty-and-units/scripts/audit_units.py) — Scan Python source for the unit and uncertainty defects that stay silent. The heuristic rules identify code that warrants review, not a proof of error: a stripped unit, a rescaled 
- [scripts/check_plausibility.py](modules/uncertainty-and-units/scripts/check_plausibility.py) — Test a set of quantities against dimensionless groups and known physical scales. Unit bookkeeping proves a calculation is dimensionally consistent. It cannot say whether the answer
- [scripts/convert_units.py](modules/uncertainty-and-units/scripts/convert_units.py) — Convert a quantity between units, including the conversions that need a context. Wavelength to photon energy, mass to amount of substance, and energy to temperature are not dimensi
- [scripts/format_result.py](modules/uncertainty-and-units/scripts/format_result.py) — Round and render a measurement result the way JCGM 100:2008 7.2 requires. The uncertainty is rounded to one or two significant digits first, and the value is then rounded to that s
- [scripts/propagate_uncertainty.py](modules/uncertainty-and-units/scripts/propagate_uncertainty.py) — Propagate uncertainty through a measurement model two ways and compare them. The GUM uncertainty framework (JCGM 100:2008) linearizes the model about the best estimates. A Monte Ca
- [scripts/uncertainty_budget.py](modules/uncertainty-and-units/scripts/uncertainty_budget.py) — Turn a list of uncertainty components into a GUM uncertainty budget. Each component arrives the way it is actually stated on a certificate, a data sheet, or a repeatability workshe

### 参考

- [references/domain-conversions.md](modules/uncertainty-and-units/references/domain-conversions.md)
- [references/gum-methodology.md](modules/uncertainty-and-units/references/gum-methodology.md)
- [references/pint-recipes.md](modules/uncertainty-and-units/references/pint-recipes.md)
- [references/plausibility-scales.md](modules/uncertainty-and-units/references/plausibility-scales.md)
- [references/reporting-rules.md](modules/uncertainty-and-units/references/reporting-rules.md)
- [references/review.md](modules/uncertainty-and-units/references/review.md)
- [references/uncertainties-recipes.md](modules/uncertainty-and-units/references/uncertainties-recipes.md)
