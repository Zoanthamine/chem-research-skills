---
name: spectrum-analyzer
description: "数值谱图文件处理后端。用于格式识别、二列数据或受支持 JCAMP 的读入、轴单位核对、峰候选及数值图导出；实验解谱和多谱结构归属优先 huangjt-spectral-structure-analysis。"
---

# 本地谱图分析

运行本地脚本前用 `& "E:/OpenAI/ChatGPT-Codex/codex-home/tools/science/science.ps1" core <script.py> <args>`；粉末 XRD 用 `xrd`，逆合成用 `retro`。环境状态和边界见 [本机后端](../../references/runtime.md)。

1. 先检查文件格式与元数据；`spectrum_analyzer.detect_spectrum_type` 只提供类型线索。
2. 文本 NMR/IR/UV/CD/色谱可用 `analyze_spectrum(path, output_dir=...)`；Bruker/Varian 原始 NMR 优先 `nmrglue`，质谱匹配可用 `matchms`。数据必须绑定真实文件和方法参数。
3. `.mnova` 等专有格式先检查可导出数据、脚本或 API；确需桌面方式时简短说明原因后使用已授权的电脑操控工具。默认 `use_gui_automation=false`，后台调用不会启动桌面程序。
4. 结构绘图用 `organic-chemistry-assistant` 的 RDKit 后端；CIF 的正式诊断与精修用 `scxrd-refinement`。
5. 上游自动官能团/峰归属属于启发式建议。不能把文件名、阈值匹配或模板输出作为结构确证、定量浓度或绝对构型证据。

上游接口细节按需查 [原工作流](references/upstream-workflow.md)，其中 GUI 优先和指定商业软件的要求已由本机后台优先流程替代。


## Validated 1D numeric backend

Two-column CSV/TXT/XY/ASC and single real processed JCAMP spectra use `profile_backend.py` through `analyze_spectrum`. Supply `spectrum_type` when known; `auto_detect=False` requires it. The declared type takes precedence over filename inference. Do not treat all sampled points as peaks.

`input_kind="profile"` performs numerical prominence-based peak picking; use `input_kind="peaks"` only for an actual peak list. IR requires `signal_kind="absorbance"` or `"transmittance"` unless declared in JCAMP metadata. NMR axes must already be ppm; Hz/FID data require calibrated processing first. Text axes are assumed to match the explicitly supplied type; this assumption is included in the report. 2D NMR, vendor raw directories and proprietary formats are separate workflows, not two-column profiles.

Example: `analyze_spectrum(path, output_dir=out, spectrum_type="IR", auto_detect=False, signal_kind="transmittance")`. Outputs preserve decoded points, peak candidates, SVG/PNG plot, source SHA-256 and JSON. No automatic functional-group assignment, absolute-configuration, purity or concentration claim follows from this numerical backend. Visual review is required before delivering a plot.

CLI: `science.ps1 science <this-skill>/profile_backend.py <input> --type IR --signal-kind transmittance --output <new-output-directory>`. Use a fresh output directory per analysis to preserve prior results.


## 联合波谱结构鉴定与案例归档
真实小分子NMR/HRMS联合归属、重叠峰、计算J/位移与NOE比较，使用相邻的 [huangjt-spectral-structure-analysis](../../SKILL.md)。本技能原有专门后端边界继续适用。
