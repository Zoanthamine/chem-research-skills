# 解谱与结构鉴定：完整能力目录

方法、脚本、参考和模板均按任务加载。本目录用于发现能力，完整操作流程在各 WORKFLOW 内；软件未安装时保留知识并按基础迁移说明补齐。

[实操与联动](references/applied-workflows.md) · [基础与迁移](references/foundation-and-migration.md)

## 主技能自带工具

- [evidence_cli.py](scripts/evidence_cli.py) — Portable numerical evidence helpers. No automatic structural assignment.
- [legacy-profile_backend.py](scripts/legacy-profile_backend.py) — Bounded local 1D profile/peak-list analysis. No chemical assignments inferred.
- [process_1d.py](scripts/process_1d.py) — Process a calibrated complex 1D FID; no acquisition settings are inferred.

## matchms

[完整工作流](modules/matchms/WORKFLOW.md)

Processes, cleans, compares, and searches tandem mass spectra with matchms. Use for MS/MS file I/O, metadata harmonization, peak filtering, spectral similarity, library matching, score matrices, and molecular-similarity networks. Use pyopenms instead for LC-MS feature detection or proteomics pipelines.

随包脚本 1 项；参考文档 6 项；模板/示例 0 项。

### 脚本

- [scripts/library_search.py](modules/matchms/scripts/library_search.py) — Search query MS/MS spectra against a reference library with matchms. Examples: uv run python library_search.py queries.mgf library.msp hits.csv uv run python library_search.py quer

### 参考

- [references/filtering.md](modules/matchms/references/filtering.md)
- [references/importing_exporting.md](modules/matchms/references/importing_exporting.md)
- [references/migration.md](modules/matchms/references/migration.md)
- [references/similarity.md](modules/matchms/references/similarity.md)
- [references/sources.md](modules/matchms/references/sources.md)
- [references/workflows.md](modules/matchms/references/workflows.md)

## nmrglue

[完整工作流](modules/nmrglue/WORKFLOW.md)

Processes calibrated one-dimensional complex NMR free-induction decays with nmrglue into phased spectra, peak candidates, and signed integration regions. Use for raw 1D NMR processing, ppm-axis verification, apodization, Fourier transformation, manual phasing, baseline correction, or reproducible spectral integration.

随包脚本 1 项；参考文档 1 项；模板/示例 1 项。

### 脚本

- [scripts/process_1d.py](modules/nmrglue/scripts/process_1d.py) — Process a calibrated complex 1D FID; no acquisition settings are inferred.

### 参考

- [references/acquisition-and-validation.md](modules/nmrglue/references/acquisition-and-validation.md)

### 模板与示例

- [assets/processing.json](modules/nmrglue/assets/processing.json)

## pyopenms

[完整工作流](modules/pyopenms/WORKFLOW.md)

Processes mass spectrometry data with pyOpenMS. Supports proteomics and metabolomics workflows—feature detection, peptide/protein identification, label-free quantification, adduct/accurate-mass annotation, and complex LC-MS/MS pipelines. Supports extensive file formats and algorithms. For simple spectral comparison and small-molecule library matching use matchms.

随包脚本 17 项；参考文档 6 项；模板/示例 0 项。

### 脚本

- [scripts/_common.py](modules/pyopenms/scripts/_common.py) — Input checks shared by the two centroided feature detectors.
- [scripts/accurate_mass_search.py](modules/pyopenms/scripts/accurate_mass_search.py) — Accurate Mass Search (Metabolite Annotation) Annotate detected features with putative metabolite identities by matching accurate masses against the bundled HMDB databases using Acc
- [scripts/align_link_quantify.py](modules/pyopenms/scripts/align_link_quantify.py) — Multi-Sample Align, Link, and Quantify End-to-end untargeted quantification across multiple LC-MS samples: 1. Detect features in each mzML (FeatureFindingMetabo) [or load .featureX
- [scripts/consensus_to_matrix.py](modules/pyopenms/scripts/consensus_to_matrix.py) — Consensus Map to Quantification Matrix Convert a consensusXML into analysis-ready tables: a wide intensity matrix (consensus features x samples) joined with feature metadata (RT, m
- [scripts/convert_format.py](modules/pyopenms/scripts/convert_format.py) — Convert Between MS File Formats Convert spectral data between mzML, mzXML, and MGF, with optional MS-level and RT/intensity filtering. Uses FileHandler for transparent format detec
- [scripts/detect_adducts.py](modules/pyopenms/scripts/detect_adducts.py) — Adduct Detection / Feature Decharging Group features that are different ionization forms (adducts/charge variants) of the same neutral compound using MetaboliteFeatureDeconvolution
- [scripts/detect_features_centroided.py](modules/pyopenms/scripts/detect_features_centroided.py) — Peptide/Centroided Feature Detection Detect features in centroided (peak-picked) LC-MS data using FeatureFinderAlgorithmPicked -- the modern replacement for the removed FeatureFind
- [scripts/detect_features_metabo.py](modules/pyopenms/scripts/detect_features_metabo.py) — Untargeted Metabolomics Feature Detection Run the standard OpenMS small-molecule feature-finding pipeline on centroided LC-MS data: MassTraceDetection -> ElutionPeakDetection -> Fe
- [scripts/digest_protein.py](modules/pyopenms/scripts/digest_protein.py) — In-Silico Protein Digestion Digest protein sequences (FASTA or a single sequence) with a configurable protease, producing theoretical peptides with masses and m/z. Useful for targe
- [scripts/export_gnps_sirius.py](modules/pyopenms/scripts/export_gnps_sirius.py) — Export for GNPS (FBMN) and SIRIUS Generate the input files required by downstream annotation tools: gnps Feature-Based Molecular Networking: writes an MGF of MS2 spectra (from a co
- [scripts/extract_chromatograms.py](modules/pyopenms/scripts/extract_chromatograms.py) — Extract Ion Chromatograms (XIC/EIC) and TIC/BPC Build chromatograms from MS1 data: total ion chromatogram (TIC), base peak chromatogram (BPC), and extracted ion chromatograms (XIC)
- [scripts/inspect_ms_data.py](modules/pyopenms/scripts/inspect_ms_data.py) — Inspect Mass Spectrometry Data Load any supported MS file (mzML, mzXML, featureXML, consensusXML, idXML) and print a structured summary: spectrum counts by MS level, RT/m/z ranges,
- [scripts/mass_calculator.py](modules/pyopenms/scripts/mass_calculator.py) — Mass & Chemistry Calculator Compute masses and isotope distributions for peptides (amino-acid sequences), empirical formulas, or both. Reports monoisotopic and average mass, m/z fo
- [scripts/plot_ms_data.py](modules/pyopenms/scripts/plot_ms_data.py) — Visualize MS Data Quick plots for inspecting MS data and results: spectrum single MS spectrum (peak/stick plot) by index or RT tic total ion chromatogram featuremap 2D feature map 
- [scripts/process_identifications.py](modules/pyopenms/scripts/process_identifications.py) — Process Peptide/Protein Identifications Post-process search-engine results (idXML): optionally re-index peptides against a protein FASTA (assigns target/decoy + protein accessions)
- [scripts/process_spectra.py](modules/pyopenms/scripts/process_spectra.py) — Signal Processing for Spectra Apply a configurable chain of signal-processing steps to all (or selected MS-level) spectra in an MS file: smoothing, centroiding (peak picking), norm
- [scripts/theoretical_spectrum.py](modules/pyopenms/scripts/theoretical_spectrum.py) — Theoretical Fragment Spectrum Generator Generate a theoretical fragment-ion spectrum (b/y, optionally a/c/x/z and losses) for a peptide using TheoreticalSpectrumGenerator. Prints a

### 参考

- [references/data_structures.md](modules/pyopenms/references/data_structures.md)
- [references/feature_detection.md](modules/pyopenms/references/feature_detection.md)
- [references/file_io.md](modules/pyopenms/references/file_io.md)
- [references/identification.md](modules/pyopenms/references/identification.md)
- [references/metabolomics.md](modules/pyopenms/references/metabolomics.md)
- [references/signal_processing.md](modules/pyopenms/references/signal_processing.md)

## spectrum-analyzer

[完整工作流](modules/spectrum-analyzer/WORKFLOW.md)

数值谱图文件处理后端。用于格式识别、二列数据或受支持 JCAMP 的读入、轴单位核对、峰候选及数值图导出；实验解谱和多谱结构归属优先 huangjt-spectral-structure-analysis。

随包脚本 21 项；参考文档 3 项；模板/示例 0 项。

### 脚本

- [__init__.py](modules/spectrum-analyzer/__init__.py) — AI 智能识谱工具 — spectrum-analyzer Skill ============================================== 模拟天然药物化学研究者思路，自动化分析谱图数据并推导化合物结构 主要模块: - spectrum_parser.py : 谱图数据类型识别与解析 - mestrenova_api.py : Me
- [chem3d_api.py](modules/spectrum-analyzer/chem3d_api.py) — chem3d_api.py — Chem3D / 通用分子绘制接口模块 功能： 1. 从 SMILES / 分子式 / 原子坐标生成 2D 结构式 2. 生成 3D 分子结构 (MOL / SDF / CML 格式) 3. 调用 Chem3D / RDKit 进行结构绘制 4. 输出结构式图像文件 (PNG / SVG) 5. NMR 信号编号标注 工作流程
- [chemdraw_gui.py](modules/spectrum-analyzer/chemdraw_gui.py) — chemdraw_gui.py — ChemDraw 2022 GUI 自动化操作模块 功能： - 根据 SMILES 自动绘制分子结构 - 自动保存为 CDXML / PNG / SVG / MOL / SDF - 自动原子编号 - 结构优化与美化 - 批量结构绘制 依赖： - gui_automation.py（核心自动化模块） - pywinauto,
- [chemistry_drawing_api.py](modules/spectrum-analyzer/chemistry_drawing_api.py) — chemistry_drawing_api.py — 综合分子结构绘制模块 **支持的绘制引擎（按优先级自动选择）**： 1. RDKit — Python 开源库，首选（无需安装商业软件） 2. ChemDraw — 业界标准的 2D 结构式绘制软件（PerkinElmer ChemOffice） 3. Chem3D — 3D 分子建模软件（PerkinE
- [db_query.py](modules/spectrum-analyzer/db_query.py) — db_query.py — 在线化学数据库查询模块 功能： 1. PubChem (REST API) — 分子式/分子量/CAS号/SMILES/结构检索 2. SDBS (日本光谱数据库) — 标准谱图比对 3. ChemSpider — 结构检索 / 文献引用 4. 分子式 -> 可能结构候选列表 5. 精确质量 -> 候选分子式列表（高分辨质谱匹配）
- [gui_automation.py](modules/spectrum-analyzer/gui_automation.py) — gui_automation.py — GUI 自动化核心模块 功能： - 窗口查找与激活 - 键盘快捷键模拟 - 菜单导航（Alt 键序列） - 鼠标点击（坐标/控件定位） - 截图与图像识别 - 弹窗处理与错误恢复 - 剪贴板操作 依赖： pip install pywinauto pyautogui pyperclip Pillow opencv-py
- [main_controller.py](modules/spectrum-analyzer/main_controller.py) — main_controller.py — AI 智能识谱工具主控制器 职责：协调整个分析流程，将各模块组合成完整的端到端自动化系统 工作流程： 1. spectrum_parser — 识别谱图类型、解析数据 2. mestrenova_api — 调用 Mestrenova 处理 NMR 原始数据（如可用） 3. db_query — 查询 PubChem
- [main_controller_gui.py](modules/spectrum-analyzer/main_controller_gui.py) — main_controller_gui.py — AI 智能识谱工具 GUI 自动化版主控制器 功能： - 通过 GUI 自动化控制化学软件（Mestrenova / ChemDraw / Spartan / Specdis） - 模拟人工操作完成谱图分析 - 全自动结构推导与绘制 依赖： - gui_automation.py（核心自动化） - mestr
- [mestrenova_api.py](modules/spectrum-analyzer/mestrenova_api.py) — mestrenova_api.py — Mestrenova 软件接口模块 功能： 1. 调用本地 Mestrenova 软件自动处理 .mnova 文件 2. 执行峰拾取 (peak picking)、积分 (integration) 3. 提取 NMR 信号表（化学位移、积分面积、多重性、耦合常数） 4. 支持多种调用方式：命令行 / Python 脚本
- [mestrenova_gui.py](modules/spectrum-analyzer/mestrenova_gui.py) — mestrenova_gui.py — Mestrenova 15 GUI 自动化操作模块 功能： - 自动打开 .mnova 文件 - 自动峰识别（Peak Picking） - 自动积分（Integration） - 导出峰列表到文本/CSV - 生成谱图图片 - 自动处理各类对话框 依赖： - gui_automation.py（核心自动化模块） - 
- [multi_spectrum_analyzer.py](modules/spectrum-analyzer/multi_spectrum_analyzer.py) — multi_spectrum_analyzer.py — 多类型谱图分析模块 支持以下谱图类型的分析： - 1D NMR (1H, 13C, 19F, 31P) - 2D NMR (COSY, HSQC, HMBC, NOESY, ROESY) - MS (低分辨/高分辨) - IR - UV-Vis - CD - X-ray CIF - 色谱 (HPLC,
- [profile_backend.py](modules/spectrum-analyzer/profile_backend.py) — Bounded local 1D profile/peak-list analysis. No chemical assignments inferred.
- [spartan_api.py](modules/spectrum-analyzer/spartan_api.py) — spartan_api.py — Spartan 软件接口模块（量子化学计算） 功能： 1. 调用 Spartan 执行分子力学优化 (MMFF) 2. 调用 Spartan 执行 DFT 几何优化 (B3LYP/6-31G*) 3. NMR 化学位移预测 (GIAO 方法) 4. ECD/ORD 圆二色谱计算 (TD-DFT) 5. 构象搜索（蒙特卡洛/分
- [spartan_gui.py](modules/spectrum-analyzer/spartan_gui.py) — spartan_gui.py — Spartan '14 V1.1.4 GUI 自动化操作模块 功能： - 从 SMILES/MOL 文件导入分子结构 - 运行几何优化（DFT, MMFF, etc.） - 运行 NMR 化学位移预测 - 运行 ECD/ORD 手性光谱计算 - 构象搜索与分析 - 导出计算结果 依赖： - gui_automation.py
- [specdis_api.py](modules/spectrum-analyzer/specdis_api.py) — specdis_api.py — Specdis 软件接口模块（手性光谱分析） 功能： 1. 导入实验 ECD/ORD 谱 2. Boltzmann 加权平均计算谱（多构象） 3. 实验谱 vs 计算谱比对（相关系数 R²） 4. 绝对构型确定（对映体打分） 5. 生成 Specdis 输入文件 工作流程模拟天然药物化学研究者： "收集构象 → DFT 计算
- [spectrum_analyzer.py](modules/spectrum-analyzer/spectrum_analyzer.py) — spectrum_analyzer.py — AI 智能识谱工具（通用版，v3.0.0） 支持谱图类型： - 1D NMR (1H, 13C, 19F, 31P) - 2D NMR (COSY, HSQC, HMBC, NOESY, ROESY, TOCSY) - MS (质谱 - 高分辨/低分辨) - IR (红外光谱) - UV-Vis (紫外-可见) 
- [spectrum_parser.py](modules/spectrum-analyzer/spectrum_parser.py) — spectrum_parser.py — 谱图数据类型识别与解析模块 功能： 1. 自动识别谱图数据类型（NMR / IR / MS / UV / ECD / ORD） 2. 自动检测文件格式（.mnova / .jdx / .csv / .txt / .sp） 3. 提取关键数据特征（化学位移、峰位、m/z、波数等） 工作流程模拟天然药物化学研究者： "拿
- [spectrum_type_detector.py](modules/spectrum-analyzer/spectrum_type_detector.py) — spectrum_type_detector.py — 谱图类型自动识别模块 功能： - 根据文件扩展名、内容自动识别谱图类型 - 支持 NMR (1D/2D), MS, IR, UV-Vis, CD, X-ray 等 支持的格式： - .mnova → Mestrenova 项目文件 - .mzML, .mzXML → 质谱 (Mass Spectrome
- [structure_elucidator.py](modules/spectrum-analyzer/structure_elucidator.py) — structure_elucidator.py — 化合物结构推导核心引擎 功能：模拟天然药物化学研究者的完整思考过程： 1. 从谱图数据（NMR/IR/MS/UV/ECD）提取关键信息 2. 确定分子式（基于 HRMS + 元素分析） 3. 计算不饱和度 Ω，判断骨架类型 4. 分析 ¹H-NMR：识别结构片段（芳香/烯氢/脂肪氢/活泼氢） 5. 分析 ¹
- [test_multi_type.py](modules/spectrum-analyzer/test_multi_type.py) — 测试多类型谱图识别
- [test_syntax.py](modules/spectrum-analyzer/test_syntax.py) — test_syntax.py — 语法完整性验证 安装 Skill 后运行此脚本，验证所有 Python 文件语法正确且完整。 如果有文件被截断或损坏，会立即报错。 用法: python test_syntax.py

### 参考

- [AGENT_GUIDE.md](modules/spectrum-analyzer/AGENT_GUIDE.md)
- [README.md](modules/spectrum-analyzer/README.md)
- [references/upstream-workflow.md](modules/spectrum-analyzer/references/upstream-workflow.md)
