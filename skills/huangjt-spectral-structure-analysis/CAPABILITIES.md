# 解谱与结构鉴定：方法与工具

本目录同时列出本主技能自身内容及内部模块。按实际任务选入口；统计用于定位资料。

## 主技能方法

- [absorbed-modules.md](<references/absorbed-modules.md>)
- [applied-workflows.md](<references/applied-workflows.md>)
- [candidate-comparison.md](<references/candidate-comparison.md>)
- [core-workflows.md](<references/core-workflows.md>)
- [experimental-workflow.md](<references/experimental-workflow.md>)
- [foundation-and-migration.md](<references/foundation-and-migration.md>)
- [host-compatibility.md](<references/host-compatibility.md>)
- [integrated-methods.md](<references/integrated-methods.md>)
- [portability.md](<references/portability.md>)
- [runtime.md](<references/runtime.md>)
- [system-integration.md](<references/system-integration.md>)
- [task-language.md](<references/task-language.md>)
- [upstream-integration.md](<references/upstream-integration.md>)

## 主技能脚本

- [evidence_cli.py](<scripts/evidence_cli.py>) — Portable numerical evidence helpers. No automatic structural assignment.
- [legacy-profile_backend.py](<scripts/legacy-profile_backend.py>) — Bounded local 1D profile/peak-list analysis. No chemical assignments inferred.
- [process_1d.py](<scripts/process_1d.py>) — Process a calibrated complex 1D FID; no acquisition settings are inferred.
- [read_spectral_file.py](<scripts/read_spectral_file.py>) — Read supported NMR/MS files into a new evidence directory; retain acquisition metadata. Reading is separate from phasing, assignment, quantitation and identification. Bruker/Varian

## matchms

[完整流程](<modules/matchms/WORKFLOW.md>)

任务：质谱 串联质谱 MSMS 谱库 相似性 预处理

### 工具

- [scripts/library_search.py](<modules/matchms/scripts/library_search.py>)

### 参考

- [references/filtering.md](<modules/matchms/references/filtering.md>)
- [references/importing_exporting.md](<modules/matchms/references/importing_exporting.md>)
- [references/migration.md](<modules/matchms/references/migration.md>)
- [references/similarity.md](<modules/matchms/references/similarity.md>)
- [references/sources.md](<modules/matchms/references/sources.md>)
- [references/workflows.md](<modules/matchms/references/workflows.md>)

## nmrglue

[完整流程](<modules/nmrglue/WORKFLOW.md>)

任务：核磁 氢谱 碳谱 FID 傅里叶 基线 相位 Bruker NMRPipe

### 工具

- [scripts/process_1d.py](<modules/nmrglue/scripts/process_1d.py>)

### 参考

- [references/acquisition-and-validation.md](<modules/nmrglue/references/acquisition-and-validation.md>)

## pyopenms

[完整流程](<modules/pyopenms/WORKFLOW.md>)

任务：质谱 色谱 LCMS 特征 峰识别 保留时间

### 工具

- [scripts/_common.py](<modules/pyopenms/scripts/_common.py>)
- [scripts/accurate_mass_search.py](<modules/pyopenms/scripts/accurate_mass_search.py>)
- [scripts/align_link_quantify.py](<modules/pyopenms/scripts/align_link_quantify.py>)
- [scripts/consensus_to_matrix.py](<modules/pyopenms/scripts/consensus_to_matrix.py>)
- [scripts/convert_format.py](<modules/pyopenms/scripts/convert_format.py>)
- [scripts/detect_adducts.py](<modules/pyopenms/scripts/detect_adducts.py>)
- [scripts/detect_features_centroided.py](<modules/pyopenms/scripts/detect_features_centroided.py>)
- [scripts/detect_features_metabo.py](<modules/pyopenms/scripts/detect_features_metabo.py>)
- [scripts/digest_protein.py](<modules/pyopenms/scripts/digest_protein.py>)
- [scripts/export_gnps_sirius.py](<modules/pyopenms/scripts/export_gnps_sirius.py>)
- [scripts/extract_chromatograms.py](<modules/pyopenms/scripts/extract_chromatograms.py>)
- [scripts/inspect_ms_data.py](<modules/pyopenms/scripts/inspect_ms_data.py>)
- [scripts/mass_calculator.py](<modules/pyopenms/scripts/mass_calculator.py>)
- [scripts/plot_ms_data.py](<modules/pyopenms/scripts/plot_ms_data.py>)
- [scripts/process_identifications.py](<modules/pyopenms/scripts/process_identifications.py>)
- [scripts/process_spectra.py](<modules/pyopenms/scripts/process_spectra.py>)
- [scripts/theoretical_spectrum.py](<modules/pyopenms/scripts/theoretical_spectrum.py>)

### 参考

- [references/data_structures.md](<modules/pyopenms/references/data_structures.md>)
- [references/feature_detection.md](<modules/pyopenms/references/feature_detection.md>)
- [references/file_io.md](<modules/pyopenms/references/file_io.md>)
- [references/identification.md](<modules/pyopenms/references/identification.md>)
- [references/metabolomics.md](<modules/pyopenms/references/metabolomics.md>)
- [references/signal_processing.md](<modules/pyopenms/references/signal_processing.md>)

## spectrum-analyzer

[完整流程](<modules/spectrum-analyzer/WORKFLOW.md>)

任务：解谱 看谱 峰表 连续谱 红外 紫外 拉曼 数值 数据处理

### 工具

- [__init__.py](<modules/spectrum-analyzer/__init__.py>)
- [chem3d_api.py](<modules/spectrum-analyzer/chem3d_api.py>)
- [chemdraw_gui.py](<modules/spectrum-analyzer/chemdraw_gui.py>)
- [chemistry_drawing_api.py](<modules/spectrum-analyzer/chemistry_drawing_api.py>)
- [db_query.py](<modules/spectrum-analyzer/db_query.py>)
- [gui_automation.py](<modules/spectrum-analyzer/gui_automation.py>)
- [main_controller.py](<modules/spectrum-analyzer/main_controller.py>)
- [main_controller_gui.py](<modules/spectrum-analyzer/main_controller_gui.py>)
- [mestrenova_api.py](<modules/spectrum-analyzer/mestrenova_api.py>)
- [mestrenova_gui.py](<modules/spectrum-analyzer/mestrenova_gui.py>)
- [multi_spectrum_analyzer.py](<modules/spectrum-analyzer/multi_spectrum_analyzer.py>)
- [profile_backend.py](<modules/spectrum-analyzer/profile_backend.py>)
- [spartan_api.py](<modules/spectrum-analyzer/spartan_api.py>)
- [spartan_gui.py](<modules/spectrum-analyzer/spartan_gui.py>)
- [specdis_api.py](<modules/spectrum-analyzer/specdis_api.py>)
- [spectrum_analyzer.py](<modules/spectrum-analyzer/spectrum_analyzer.py>)
- [spectrum_parser.py](<modules/spectrum-analyzer/spectrum_parser.py>)
- [spectrum_type_detector.py](<modules/spectrum-analyzer/spectrum_type_detector.py>)
- [structure_elucidator.py](<modules/spectrum-analyzer/structure_elucidator.py>)
- [test_multi_type.py](<modules/spectrum-analyzer/test_multi_type.py>)
- [test_syntax.py](<modules/spectrum-analyzer/test_syntax.py>)

### 参考

- [AGENT_GUIDE.md](<modules/spectrum-analyzer/AGENT_GUIDE.md>)
- [README.md](<modules/spectrum-analyzer/README.md>)
- [references/upstream-workflow.md](<modules/spectrum-analyzer/references/upstream-workflow.md>)
