# 学术写作与科研成品：完整能力目录

方法、脚本、参考和模板均按任务加载。本目录用于发现能力，完整操作流程在各 WORKFLOW 内；软件未安装时保留知识并按基础迁移说明补齐。

[实操与联动](references/applied-workflows.md) · [基础与迁移](references/foundation-and-migration.md)

## 主技能自带工具


## dask

[完整工作流](modules/dask/WORKFLOW.md)

Scales pandas, NumPy, and custom Python research workflows beyond memory or across clusters with Dask. Covers DataFrames, Arrays, Bags, Futures, chunking, schedulers, and distributed diagnostics. Use for partitioned file processing, scientific array computation, or parallel tasks whose memory and dependency structure require Dask.

随包脚本 0 项；参考文档 7 项；模板/示例 0 项。

### 参考

- [references/arrays.md](modules/dask/references/arrays.md)
- [references/bags.md](modules/dask/references/bags.md)
- [references/best-practices.md](modules/dask/references/best-practices.md)
- [references/dataframes.md](modules/dask/references/dataframes.md)
- [references/futures.md](modules/dask/references/futures.md)
- [references/review.md](modules/dask/references/review.md)
- [references/schedulers.md](modules/dask/references/schedulers.md)

## exploratory-data-analysis

[完整工作流](modules/exploratory-data-analysis/WORKFLOW.md)

Performs bounded, local exploratory analysis of explicitly supported scientific files. Supports redacted CSV/TSV/JSON profiles; optional NumPy, HDF5, FASTA/FASTQ, and basic image metadata inspection; missingness/leakage audits; outlier and transformation sensitivity; and rigorous EDA report scaffolds. Other domain formats are reference-only and unknown formats fail closed.

随包脚本 13 项；参考文档 7 项；模板/示例 0 项。

### 脚本

- [scripts/__init__.py](modules/exploratory-data-analysis/scripts/__init__.py) — Bounded, local-only helper CLIs for exploratory-data-analysis.
- [scripts/_capabilities.py](modules/exploratory-data-analysis/scripts/_capabilities.py) — Closed capability registry and lightweight format checks for EDA tools.
- [scripts/_common.py](modules/exploratory-data-analysis/scripts/_common.py) — Shared local-only, bounded-I/O helpers for the EDA command-line tools.
- [scripts/_structured.py](modules/exploratory-data-analysis/scripts/_structured.py) — Bounded inspectors for JSON, NumPy containers, and HDF5 metadata.
- [scripts/_tabular.py](modules/exploratory-data-analysis/scripts/_tabular.py) — Bounded, redacted tabular profiling and EDA sensitivity calculations.
- [scripts/capability_manifest.py](modules/exploratory-data-analysis/scripts/capability_manifest.py) — Emit the closed capability matrix or a redacted local-file manifest.
- [scripts/distribution_sensitivity.py](modules/exploratory-data-analysis/scripts/distribution_sensitivity.py) — Bounded distribution, transformation, and outlier sensitivity CLI.
- [scripts/eda_analyzer.py](modules/exploratory-data-analysis/scripts/eda_analyzer.py) — Closed, bounded exploratory analyzer for explicitly supported local formats.
- [scripts/image_inspector.py](modules/exploratory-data-analysis/scripts/image_inspector.py) — Metadata-only PNG/JPEG/TIFF inspector; pixel arrays are never decoded.
- [scripts/missingness_leakage_audit.py](modules/exploratory-data-analysis/scripts/missingness_leakage_audit.py) — Bounded missingness, group structure, and split leakage audit for CSV/TSV.
- [scripts/report_scaffold.py](modules/exploratory-data-analysis/scripts/report_scaffold.py) — Generate a rigorous, redacted EDA Markdown report scaffold.
- [scripts/sequence_inspector.py](modules/exploratory-data-analysis/scripts/sequence_inspector.py) — Bounded FASTA/FASTQ aggregate inspector with no identifier or sequence output.
- [scripts/tabular_profile.py](modules/exploratory-data-analysis/scripts/tabular_profile.py) — Bounded aggregate schema/profile CLI for local CSV and TSV files.

### 参考

- [assets/report_template.md](modules/exploratory-data-analysis/assets/report_template.md)
- [references/bioinformatics_genomics_formats.md](modules/exploratory-data-analysis/references/bioinformatics_genomics_formats.md)
- [references/chemistry_molecular_formats.md](modules/exploratory-data-analysis/references/chemistry_molecular_formats.md)
- [references/general_scientific_formats.md](modules/exploratory-data-analysis/references/general_scientific_formats.md)
- [references/microscopy_imaging_formats.md](modules/exploratory-data-analysis/references/microscopy_imaging_formats.md)
- [references/proteomics_metabolomics_formats.md](modules/exploratory-data-analysis/references/proteomics_metabolomics_formats.md)
- [references/spectroscopy_analytical_formats.md](modules/exploratory-data-analysis/references/spectroscopy_analytical_formats.md)

## humanize-writing

[完整工作流](modules/humanize-writing/WORKFLOW.md)

Remove signs of AI-generated writing from text. Use when the user mentions
'sounds like AI,' 'too robotic,' 'humanize this,' 'make it sound human,'
'de-AI this,' 'sounds like ChatGPT,' 'make it natural,' or 'doesn't sound
like a person wrote it.' Detects and fixes AI writing patterns including
inflated significance, promotional language, formulaic structure, AI vocabulary,
superficial analyses, vague attributions, hedging, robotic rhythm, em dash and
boldface overuse, chatbot artifacts, and missing personality. Based on
Wikipedia's "Signs of AI writing" guide and editorial best practices.


随包脚本 2 项；参考文档 2 项；模板/示例 0 项。

### 脚本

- [install-skill.js](modules/humanize-writing/install-skill.js) — const fs = require("fs");
- [uninstall-skill.js](modules/humanize-writing/uninstall-skill.js) — const fs = require("fs");

### 参考

- [README.md](modules/humanize-writing/README.md)
- [references/ai-tells.md](modules/humanize-writing/references/ai-tells.md)

## latex-posters

[完整工作流](modules/latex-posters/WORKFLOW.md)

Creates research posters in LaTeX using beamerposter, tikzposter, or baposter. Use for conference posters, academic presentations, multi-column scientific layouts, figure integration, typography, compilation, and PDF preflight.

随包脚本 3 项；参考文档 10 项；模板/示例 0 项。

### 脚本

- [scripts/generate_schematic.py](modules/latex-posters/scripts/generate_schematic.py) — Scientific schematic generation using Nano Banana 2. Generate any scientific diagram by describing it in natural language. Nano Banana 2 handles everything automatically with smart
- [scripts/generate_schematic_ai.py](modules/latex-posters/scripts/generate_schematic_ai.py) — AI-powered scientific schematic generation using Nano Banana 2. This script uses a smart iterative refinement approach: 1. Generate initial image with Nano Banana 2 2. AI quality r
- [scripts/review_poster.sh](modules/latex-posters/scripts/review_poster.sh) — Read-only Poppler preflight. Exit 0: automated checks passed; 1: failure;

### 参考

- [assets/poster_quality_checklist.md](modules/latex-posters/assets/poster_quality_checklist.md)
- [references/ai_graphics_for_posters.md](modules/latex-posters/references/ai_graphics_for_posters.md)
- [references/compilation_and_quality_control.md](modules/latex-posters/references/compilation_and_quality_control.md)
- [references/latex_poster_packages.md](modules/latex-posters/references/latex_poster_packages.md)
- [references/latex_poster_reference.md](modules/latex-posters/references/latex_poster_reference.md)
- [references/poster_content_guide.md](modules/latex-posters/references/poster_content_guide.md)
- [references/poster_design_principles.md](modules/latex-posters/references/poster_design_principles.md)
- [references/poster_layout_design.md](modules/latex-posters/references/poster_layout_design.md)
- [references/poster_patterns_and_presentation.md](modules/latex-posters/references/poster_patterns_and_presentation.md)
- [references/README.md](modules/latex-posters/references/README.md)

## matplotlib

[完整工作流](modules/matplotlib/WORKFLOW.md)

Creates and customizes scientific plots with Matplotlib. Used for fine-grained control over plot elements, novel plot types, and scientific workflows. Export to PNG/PDF/SVG for publication. For quick statistical plots use seaborn; for interactive plots use plotly; for publication-ready multi-panel figures with journal styling, use scientific-visualization.

随包脚本 2 项；参考文档 4 项；模板/示例 0 项。

### 脚本

- [scripts/plot_template.py](modules/matplotlib/scripts/plot_template.py) — Matplotlib Plot Template Comprehensive template demonstrating various plot types and best practices. Use this as a starting point for creating publication-quality visualizations. U
- [scripts/style_configurator.py](modules/matplotlib/scripts/style_configurator.py) — Matplotlib Style Configurator Interactive utility to configure matplotlib style preferences and generate custom style sheets. Creates a preview of the style and optionally saves it

### 参考

- [references/api_reference.md](modules/matplotlib/references/api_reference.md)
- [references/common_issues.md](modules/matplotlib/references/common_issues.md)
- [references/plot_types.md](modules/matplotlib/references/plot_types.md)
- [references/styling_guide.md](modules/matplotlib/references/styling_guide.md)

## nature-data

[完整工作流](modules/nature-data/WORKFLOW.md)

Draft or audit manuscript Data/Code Availability statements, dataset access routes, repository plans, and FAIR metadata. Use for 数据可用性声明、数据共享、数据仓库选择 and dataset citations; not general data cleaning or statistical analysis.

随包脚本 0 项；参考文档 12 项；模板/示例 0 项。

### 参考

- [README.md](modules/nature-data/README.md)
- [README_EN.md](modules/nature-data/README_EN.md)
- [references/chinese-author-alignment.md](modules/nature-data/references/chinese-author-alignment.md)
- [references/fair-metadata-checklist.md](modules/nature-data/references/fair-metadata-checklist.md)
- [references/nature-article-requirements.md](modules/nature-data/references/nature-article-requirements.md)
- [references/policy-principles.md](modules/nature-data/references/policy-principles.md)
- [references/repository-and-identifiers.md](modules/nature-data/references/repository-and-identifiers.md)
- [references/source-basis.md](modules/nature-data/references/source-basis.md)
- [references/statement-patterns.md](modules/nature-data/references/statement-patterns.md)
- [static/core/chinese-mode.md](modules/nature-data/static/core/chinese-mode.md)
- [static/core/stance.md](modules/nature-data/static/core/stance.md)
- [static/core/workflow.md](modules/nature-data/static/core/workflow.md)

## nature-figure

[完整工作流](modules/nature-figure/WORKFLOW.md)

Create, revise, audit, and export manuscript scientific figures in Python or R. Use for 论文配图、科研绘图、多面板图 and submission-ready plots, or explicitly requested AI-generated graphical abstracts and mechanism schematics. Not for interactive dashboards, data cleaning, or statistics-only analysis.

随包脚本 11 项；参考文档 28 项；模板/示例 0 项。

### 脚本

- [scripts/audit_figure_collisions.py](modules/nature-figure/scripts/audit_figure_collisions.py) — Audit rendered PDF figures for probable text and graphic collisions. The audit is backend-neutral: Python and R figures are both checked from their final PDF geometry. Reliable col
- [scripts/audit_panel_alignment.py](modules/nature-figure/scripts/audit_panel_alignment.py) — Audit multi-panel figure alignment from rendered layout geometry. The core auditor consumes a small backend-neutral JSON manifest. Matplotlib figures can call :func:`require_matplo
- [scripts/audit_pdf_text.py](modules/nature-figure/scripts/audit_pdf_text.py) — Audit effective text sizes in PDF content streams. The size is ``Tf`` size scaled by the text matrix (``Tm``) and ``cm`` transforms. This dependency-free check catches reduced math
- [scripts/audit_svg_schematic.py](modules/nature-figure/scripts/audit_svg_schematic.py) — Audit a hand-built SVG schematic against final-size journal rules. Checks, using only the standard library: * effective text size at final physical size (font-size, ``scale``/``mat
- [scripts/figure_safety.py](modules/nature-figure/scripts/figure_safety.py) — Small numerical/layout safety helpers for Python publication figures.
- [scripts/generate_openrouter_schematic.py](modules/nature-figure/scripts/generate_openrouter_schematic.py) — Generate manuscript schematic drafts with OpenRouter's Images API.
- [scripts/nature_figure_backend.py](modules/nature-figure/scripts/nature_figure_backend.py) — Read or write the user's default nature-figure plotting backend.
- [scripts/plot_templates.py](modules/nature-figure/scripts/plot_templates.py) — Validated Python templates for five common manuscript-figure families. Subcommands: volcano, roc, dotplot, marginal, and paired. Production runs require a CSV input. Simulated data
- [scripts/validate_figure.py](modules/nature-figure/scripts/validate_figure.py) — Static preflight for publication-figure Python and R source files. The validator is intentionally dependency-free. It checks portable source-level requirements before the selected 
- [tests/test_figure_safety.py](modules/nature-figure/tests/test_figure_safety.py) — SKILL = Path(__file__).parents[1]
- [tests/test_schematic_url_safety.py](modules/nature-figure/tests/test_schematic_url_safety.py) — URL safety tests for generate_openrouter_schematic.py (no network access).

### 参考

- [EXTERNAL_RESOURCES.md](modules/nature-figure/EXTERNAL_RESOURCES.md)
- [README.md](modules/nature-figure/README.md)
- [README_EN.md](modules/nature-figure/README_EN.md)
- [references/ai-graphical-abstract-workflow.md](modules/nature-figure/references/ai-graphical-abstract-workflow.md)
- [references/api.md](modules/nature-figure/references/api.md)
- [references/asset-adaptation.md](modules/nature-figure/references/asset-adaptation.md)
- [references/backend-selection.md](modules/nature-figure/references/backend-selection.md)
- [references/chart-types.md](modules/nature-figure/references/chart-types.md)
- [references/common-patterns.md](modules/nature-figure/references/common-patterns.md)
- [references/demos.md](modules/nature-figure/references/demos.md)
- [references/design-theory.md](modules/nature-figure/references/design-theory.md)
- [references/figure-contract.md](modules/nature-figure/references/figure-contract.md)
- [references/figure-legend-conventions.md](modules/nature-figure/references/figure-legend-conventions.md)
- [references/multipanel-evidence-architecture.md](modules/nature-figure/references/multipanel-evidence-architecture.md)
- [references/nature-2026-observations.md](modules/nature-figure/references/nature-2026-observations.md)
- [references/nature-article-requirements.md](modules/nature-figure/references/nature-article-requirements.md)
- [references/openrouter-image-generation.md](modules/nature-figure/references/openrouter-image-generation.md)
- [references/qa-contract.md](modules/nature-figure/references/qa-contract.md)
- [references/r-template-index.md](modules/nature-figure/references/r-template-index.md)
- [references/r-workflow.md](modules/nature-figure/references/r-workflow.md)
- [references/template-catalog.md](modules/nature-figure/references/template-catalog.md)
- [references/tutorials.md](modules/nature-figure/references/tutorials.md)
- [references/vector-schematic-style-rules.md](modules/nature-figure/references/vector-schematic-style-rules.md)
- [references/vector-schematic-workflow.md](modules/nature-figure/references/vector-schematic-workflow.md)
- [static/core/contract.md](modules/nature-figure/static/core/contract.md)
- [static/core/stance.md](modules/nature-figure/static/core/stance.md)
- [static/fragments/backend/python.md](modules/nature-figure/static/fragments/backend/python.md)
- [static/fragments/backend/r.md](modules/nature-figure/static/fragments/backend/r.md)

## nature-image2ppt

[完整工作流](modules/nature-image2ppt/WORKFLOW.md)

Reconstruct slide images, screenshots, scanned PDFs, or image-only PPTX files as object-level editable PowerPoint. Use for 图片转可编辑PPT、截图还原PPT and diagram reconstruction; not authoring a new deck from research notes.

随包脚本 67 项；参考文档 15 项；模板/示例 0 项。

### 脚本

- [cli/image2ppt/__init__.py](modules/nature-image2ppt/cli/image2ppt/__init__.py) — __version__ = "1.1.0"
- [cli/image2ppt/cli.py](modules/nature-image2ppt/cli/image2ppt/cli.py) — def main() -> None:
- [cli/image2ppt/runtime/__init__.py](modules/nature-image2ppt/cli/image2ppt/runtime/__init__.py) — Deterministic runtime modules behind the public image2ppt CLI.
- [cli/image2ppt/runtime/_input_normalization.py](modules/nature-image2ppt/cli/image2ppt/runtime/_input_normalization.py) — IMG_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff"}
- [cli/image2ppt/runtime/_page_artifacts.py](modules/nature-image2ppt/cli/image2ppt/runtime/_page_artifacts.py) — SCRIPT_DIR = Path(__file__).resolve().parent
- [cli/image2ppt/runtime/build_pptx_from_manifest.py](modules/nature-image2ppt/cli/image2ppt/runtime/build_pptx_from_manifest.py) — EMU_PER_INCH = 914400
- [cli/image2ppt/runtime/configure_image_backend.py](modules/nature-image2ppt/cli/image2ppt/runtime/configure_image_backend.py) — def configured_model() -> str:
- [cli/image2ppt/runtime/deck_run_state.py](modules/nature-image2ppt/cli/image2ppt/runtime/deck_run_state.py) — ACTIVE_PAGE_STATUSES = {"dispatched"}
- [cli/image2ppt/runtime/deck_text_hints.py](modules/nature-image2ppt/cli/image2ppt/runtime/deck_text_hints.py) — Generate text hints for every page of a prepared run. Runs as part of `image2ppt prepare`, after page directories exist: each `pages/page_NNN/` receives canonical `text_hints.json`
- [cli/image2ppt/runtime/finalize_deck_run.py](modules/nature-image2ppt/cli/image2ppt/runtime/finalize_deck_run.py) — SCRIPT_DIR = Path(__file__).resolve().parent
- [cli/image2ppt/runtime/formula_renderer.py](modules/nature-image2ppt/cli/image2ppt/runtime/formula_renderer.py) — Render LaTeX formulas into image assets for page manifests.
- [cli/image2ppt/runtime/image_gen.py](modules/nature-image2ppt/cli/image2ppt/runtime/image_gen.py) — Unified CLI for image2ppt image generation or editing. The CLI prefers local Codex OAuth auth when ~/.codex/auth.json is available. If Codex auth is missing, it falls back to OpenA
- [cli/image2ppt/runtime/main.py](modules/nature-image2ppt/cli/image2ppt/runtime/main.py) — Unified CLI for the image2ppt skill.
- [cli/image2ppt/runtime/make_page_contact_sheet.py](modules/nature-image2ppt/cli/image2ppt/runtime/make_page_contact_sheet.py) — parser = argparse.ArgumentParser(description="Create an origin/preview contact sheet for a page.")
- [cli/image2ppt/runtime/paddle_text_hints.py](modules/nature-image2ppt/cli/image2ppt/runtime/paddle_text_hints.py) — Text hints backed by the PaddleOCR-VL cloud API (experimental). Same contract as `text_hints.py`, with a different detector: the page is sent to the PaddleOCR-VL service, only TEXT
- [cli/image2ppt/runtime/page_job_status.py](modules/nature-image2ppt/cli/image2ppt/runtime/page_job_status.py) — active_pages,
- [cli/image2ppt/runtime/page_text_metrics.py](modules/nature-image2ppt/cli/image2ppt/runtime/page_text_metrics.py) — Shared deterministic ink-analysis helpers for `image2ppt page snap` and `image2ppt page diff`. All functions operate on grayscale numpy arrays (float or uint8, 0..255). "Ink" means
- [cli/image2ppt/runtime/prepare_deck_run.py](modules/nature-image2ppt/cli/image2ppt/runtime/prepare_deck_run.py) — WIDE_SLIDE = {"width": 13.333, "height": 7.5, "size_mode": "wide"}
- [cli/image2ppt/runtime/process_asset_sheet.py](modules/nature-image2ppt/cli/image2ppt/runtime/process_asset_sheet.py) — def configure_default_paths(args):
- [cli/image2ppt/runtime/record_imagegen_result.py](modules/nature-image2ppt/cli/image2ppt/runtime/record_imagegen_result.py) — parser = argparse.ArgumentParser(
- [cli/image2ppt/runtime/record_page_dispatch.py](modules/nature-image2ppt/cli/image2ppt/runtime/record_page_dispatch.py) — page_dir_for,
- [cli/image2ppt/runtime/record_page_result.py](modules/nature-image2ppt/cli/image2ppt/runtime/record_page_result.py) — inside_or_missing,
- [cli/image2ppt/runtime/remove_chroma_key.py](modules/nature-image2ppt/cli/image2ppt/runtime/remove_chroma_key.py) — Remove a solid chroma-key background from an image2ppt slide image. This helper supports the CLI/API transparent fallback workflow: generate an image on a flat key color, then conv
- [cli/image2ppt/runtime/reset_page_job.py](modules/nature-image2ppt/cli/image2ppt/runtime/reset_page_job.py) — Reset a failed or inactive page back to pending so it can be re-dispatched.
- [cli/image2ppt/runtime/runtime_env.py](modules/nature-image2ppt/cli/image2ppt/runtime/runtime_env.py) — Configuration and independent runtime diagnostics for Image2PPT.
- [cli/image2ppt/runtime/split_alpha_components.py](modules/nature-image2ppt/cli/image2ppt/runtime/split_alpha_components.py) — def parse_names(value, option="--names"):
- [cli/image2ppt/runtime/text_hints.py](modules/nature-image2ppt/cli/image2ppt/runtime/text_hints.py) — Measure text line boxes and font sizes from source.png as advisory hints. Run BEFORE writing the page manifest. The output is a reference, not a mutation: the page author reads `te
- [cli/image2ppt/runtime/validate_pptx.py](modules/nature-image2ppt/cli/image2ppt/runtime/validate_pptx.py) — "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
- [scripts/build_page_worker_prompt.py](modules/nature-image2ppt/scripts/build_page_worker_prompt.py) — Build the original two-layer page-worker prompt from local resources.
- [scripts/inspect_arrow_atomicity.py](modules/nature-image2ppt/scripts/inspect_arrow_atomicity.py) — Verify one manifest arrow maps to one named PowerPoint object.
- [scripts/inspect_region_decomposition.py](modules/nature-image2ppt/scripts/inspect_region_decomposition.py) — Validate Image2PPT region evidence against standard manifest objects.
- [scripts/postprocess_manifest_arrows.py](modules/nature-image2ppt/scripts/postprocess_manifest_arrows.py) — Apply Image2PPT arrow extensions to an image2ppt-built PPTX. The local builder remains the sole packager. This script only rewrites the slide XML objects that correspond to arrow-e
- [scripts/render_image2ppt_qa.py](modules/nature-image2ppt/scripts/render_image2ppt_qa.py) — Render Image2PPT output with PowerPoint or project-local LibreOffice fallback.
- [scripts/run_final_image2ppt_qa.py](modules/nature-image2ppt/scripts/run_final_image2ppt_qa.py) — Postprocess and validate the final deck produced by ``image2ppt run finalize``.
- [scripts/run_image2ppt_qa.py](modules/nature-image2ppt/scripts/run_image2ppt_qa.py) — Run Image2PPT's supplemental page gate on standard image2ppt artifacts.
- [scripts/runtime_paths.py](modules/nature-image2ppt/scripts/runtime_paths.py) — Resolve only resources bundled inside the Image2PPT Skill.
- [scripts/visual_review_evidence.py](modules/nature-image2ppt/scripts/visual_review_evidence.py) — Create and validate page-by-page visual review evidence.
- [tests/support.py](modules/nature-image2ppt/tests/support.py) — SKILL_ROOT = Path(__file__).resolve().parents[1]
- [tests/test_console_portability.py](modules/nature-image2ppt/tests/test_console_portability.py) — class ConsolePortabilityTests(unittest.TestCase):
- [tests/test_deck_slide_size.py](modules/nature-image2ppt/tests/test_deck_slide_size.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_dispatch_concurrency.py](modules/nature-image2ppt/tests/test_dispatch_concurrency.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_formula_renderer.py](modules/nature-image2ppt/tests/test_formula_renderer.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_independence.py](modules/nature-image2ppt/tests/test_independence.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_input_normalization_alpha.py](modules/nature-image2ppt/tests/test_input_normalization_alpha.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_input_normalization_opc_targets.py](modules/nature-image2ppt/tests/test_input_normalization_opc_targets.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_isolated_lifecycle.py](modules/nature-image2ppt/tests/test_isolated_lifecycle.py) — class IsolatedLifecycleTests(unittest.TestCase):
- [tests/test_manifest_arrows.py](modules/nature-image2ppt/tests/test_manifest_arrows.py) — complete_visual_review_evidence,
- [tests/test_migration_parity.py](modules/nature-image2ppt/tests/test_migration_parity.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_multi_agent_backend.py](modules/nature-image2ppt/tests/test_multi_agent_backend.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_ocr_http.py](modules/nature-image2ppt/tests/test_ocr_http.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_paddle_result_url_safety.py](modules/nature-image2ppt/tests/test_paddle_result_url_safety.py) — Result-URL safety tests for paddle_text_hints.py (no network access).
- [tests/test_page_hints.py](modules/nature-image2ppt/tests/test_page_hints.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_path_confinement.py](modules/nature-image2ppt/tests/test_path_confinement.py) — class PathConfinementTests(unittest.TestCase):
- [tests/test_pdf_backend.py](modules/nature-image2ppt/tests/test_pdf_backend.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_project_metadata.py](modules/nature-image2ppt/tests/test_project_metadata.py) — class ProjectMetadataTests(unittest.TestCase):
- [tests/test_quality_contracts.py](modules/nature-image2ppt/tests/test_quality_contracts.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_region_decomposition.py](modules/nature-image2ppt/tests/test_region_decomposition.py) — def knowledge_graph_manifest(page: Path, *, distorted: bool = False, flattened: bool = False) -> Path:
- [tests/test_render_guard.py](modules/nature-image2ppt/tests/test_render_guard.py) — class RenderGuardTests(unittest.TestCase):
- [tests/test_runtime_config.py](modules/nature-image2ppt/tests/test_runtime_config.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_runtime_paths.py](modules/nature-image2ppt/tests/test_runtime_paths.py) — sys.path.insert(0, str(SCRIPTS))
- [tests/test_script_inventory.py](modules/nature-image2ppt/tests/test_script_inventory.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_slide_layout.py](modules/nature-image2ppt/tests/test_slide_layout.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_state_e2e.py](modules/nature-image2ppt/tests/test_state_e2e.py) — complete_visual_review_evidence,
- [tests/test_structure_reconstruction.py](modules/nature-image2ppt/tests/test_structure_reconstruction.py) — "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
- [tests/test_thin_profile.py](modules/nature-image2ppt/tests/test_thin_profile.py) — class SingleRuntimeTests(unittest.TestCase):
- [tests/test_visual_review_evidence.py](modules/nature-image2ppt/tests/test_visual_review_evidence.py) — sys.path.insert(0, str(SCRIPTS))
- [tests/test_visual_review_runtime.py](modules/nature-image2ppt/tests/test_visual_review_runtime.py) — sys.path.insert(0, str(SCRIPTS))

### 参考

- [prompts/page-worker-base.md](modules/nature-image2ppt/prompts/page-worker-base.md)
- [prompts/page-worker.md](modules/nature-image2ppt/prompts/page-worker.md)
- [README.md](modules/nature-image2ppt/README.md)
- [README_EN.md](modules/nature-image2ppt/README_EN.md)
- [references/assets-provenance-contract.md](modules/nature-image2ppt/references/assets-provenance-contract.md)
- [references/cli-helper.md](modules/nature-image2ppt/references/cli-helper.md)
- [references/manifest-arrow-extension.md](modules/nature-image2ppt/references/manifest-arrow-extension.md)
- [references/manifest-schema.md](modules/nature-image2ppt/references/manifest-schema.md)
- [references/object-routing.md](modules/nature-image2ppt/references/object-routing.md)
- [references/ocr-text-hints-contract.md](modules/nature-image2ppt/references/ocr-text-hints-contract.md)
- [references/page-decision-tree.md](modules/nature-image2ppt/references/page-decision-tree.md)
- [references/qa-contract.md](modules/nature-image2ppt/references/qa-contract.md)
- [references/region-decomposition.md](modules/nature-image2ppt/references/region-decomposition.md)
- [references/runtime-dependencies.md](modules/nature-image2ppt/references/runtime-dependencies.md)
- [references/workflow.md](modules/nature-image2ppt/references/workflow.md)

## nature-paper-to-patent

[完整工作流](modules/nature-paper-to-patent/WORKFLOW.md)

Turn research papers or inventor materials into evidence-grounded Chinese invention patent drafts and technical disclosures. Use for 技术交底书、专利撰写、现有技术对比 and Chinese DOCX patent packages; not general manuscript writing.

随包脚本 24 项；参考文档 36 项；模板/示例 0 项。

### 脚本

- [scripts/audit_claims.py](modules/nature-paper-to-patent/scripts/audit_claims.py) — Run deterministic structural checks on Chinese patent claims.
- [scripts/build_patent_package.py](modules/nature-paper-to-patent/scripts/build_patent_package.py) — Build the standard split Chinese patent application package.
- [scripts/disclosure/cnipa_epub_crawler.py](modules/nature-paper-to-patent/scripts/disclosure/cnipa_epub_crawler.py) — 中国专利公布公告网站点：http://epub.cnipa.gov.cn/ —— **首页「公布公告查询」** 检索（#indexForm / #searchStr）。 须安装 **Playwright + Chromium**。若只需内存中解析、不落盘 HTML，优先用同目录 **`cnipa_epub_search.py`**； 本文件侧重 **写出结果
- [scripts/disclosure/cnipa_epub_parse.py](modules/nature-paper-to-patent/scripts/disclosure/cnipa_epub_parse.py) — 解析 http://epub.cnipa.gov.cn/ 检索结果页 HTML，提取公布公告列表中的标题、公开号、详情链接、摘要（若有）。 与 `cnipa_epub_crawler.py` / **`cnipa_epub_search.py`**（一步检索+解析）配合：爬虫落盘 HTML 后可用本模块单独再解析；也可被其它脚本 import。
- [scripts/disclosure/cnipa_epub_search.py](modules/nature-paper-to-patent/scripts/disclosure/cnipa_epub_search.py) — 国知局公布站「检索 + 解析」一步完成：内存中持有结果页 HTML，**默认不落盘**。 内部调用 ``cnipa_epub_crawler.search_epub_keyword``（等同先 ``fetch_epub_result_html`` 再 ``parse_search_result_html``）。 **输出约定**（便于 Agent 抓取且不触
- [scripts/disclosure/docx_to_md.py](modules/nature-paper-to-patent/scripts/disclosure/docx_to_md.py) — 将 Word（.docx）转为 Markdown，并把内嵌图片抽取到磁盘，便于 Step 2 扫描与 Agent Read。 依赖 mammoth（见仓库根目录 requirements.txt）。 用法: python docx_to_md.py --input design.docx --output outputs/case/design.md pyt
- [scripts/disclosure/iteration_dialog_log.py](modules/nature-paper-to-patent/scripts/disclosure/iteration_dialog_log.py) — 在案件目录追加「交底书修订对话记录.md」一条：含记录时间（本地 + UTC）、用户说明摘要、交付文件名、合并/纠正摘要摘录。
- [scripts/disclosure/math_render.py](modules/nature-paper-to-patent/scripts/disclosure/math_render.py) — 将 Markdown 中的 LaTeX 公式渲染为 PNG（matplotlib mathtext），**保留 `$...$` / `\(...\)` / `$$...$$` / `\[...\]` 原文**， 图片引用写入 HTML 注释 ``<!-- ![...](path) -->``（预览不显示图，Word 仍嵌入）。 支持（失败时**保留原文**，
- [scripts/disclosure/md_to_docx.py](modules/nature-paper-to-patent/scripts/disclosure/md_to_docx.py) — 将 Markdown 转为 Word（.docx），按标题层级映射为 Word 内置「标题 1–9」样式， 便于交底书交付代理人或所内流程。 支持：ATX 标题 (#–######)、段落、**粗体**、行内 `代码`、无序/有序列表、 围栏代码块、简单 GFM 表格、引用块（>）、水平线（---）、行内图片 ``![](path.png)`` （在最大宽、
- [scripts/disclosure/mermaid_render.py](modules/nature-paper-to-patent/scripts/disclosure/mermaid_render.py) — 将 Markdown 中的 **mermaid** 围栏与（默认）**LaTeX 公式** 转为 PNG，再写定稿 `.md` 并默认生成 Word。 **公式**：默认先调用同目录 **`math_render.py`**（``matplotlib``；``--no-math`` 可跳过）。**Mermaid** 围栏块逐块渲染为 PNG，**保留** `
- [scripts/disclosure/pptx_to_md.py](modules/nature-paper-to-patent/scripts/disclosure/pptx_to_md.py) — 将 PowerPoint（.pptx）按页导出为 Markdown，并抽取幻灯片中的嵌入图片，便于 Step 2 扫描与 Agent Read。 依赖 python-pptx（见仓库根目录 requirements.txt）。 用法: python pptx_to_md.py --input review.pptx --output outputs/case
- [scripts/extract_pdf_text.py](modules/nature-paper-to-patent/scripts/extract_pdf_text.py) — Extract searchable text from one PDF or a directory of PDFs.
- [scripts/init_patent_project.py](modules/nature-paper-to-patent/scripts/init_patent_project.py) — Create an agent-neutral paper-to-patent project workspace.
- [scripts/math_to_omml.py](modules/nature-paper-to-patent/scripts/math_to_omml.py) — Convert a LaTeX equation into editable Word Office Math (OMML).
- [scripts/render_flowchart_svg.py](modules/nature-paper-to-patent/scripts/render_flowchart_svg.py) — Render patent-style black-and-white flowchart SVGs from draft JSON.
- [scripts/render_patent_docx.py](modules/nature-paper-to-patent/scripts/render_patent_docx.py) — Render a structured Chinese patent draft JSON file as DOCX.
- [scripts/validate_patent_draft.py](modules/nature-paper-to-patent/scripts/validate_patent_draft.py) — Validate traceability, completeness, and quality gates in a patent draft.
- [tests/test_audit_claims.py](modules/nature-paper-to-patent/tests/test_audit_claims.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_inline_math_paren.py](modules/nature-paper-to-patent/tests/test_inline_math_paren.py) — ROOT = Path(__file__).resolve().parents[1] / "scripts" / "disclosure"
- [tests/test_math_to_omml_superscript.py](modules/nature-paper-to-patent/tests/test_math_to_omml_superscript.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_md_to_docx_source_overwrite.py](modules/nature-paper-to-patent/tests/test_md_to_docx_source_overwrite.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_mermaid_render.py](modules/nature-paper-to-patent/tests/test_mermaid_render.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_validation.py](modules/nature-paper-to-patent/tests/test_validation.py) — ROOT = Path(__file__).resolve().parents[1]
- [tests/test_validation_figure_node_ids.py](modules/nature-paper-to-patent/tests/test_validation_figure_node_ids.py) — class FigureNodeIdValidationTests(unittest.TestCase):

### 参考

- [README.md](modules/nature-paper-to-patent/README.md)
- [README_EN.md](modules/nature-paper-to-patent/README_EN.md)
- [references/cn-patent-drafting-guide.md](modules/nature-paper-to-patent/references/cn-patent-drafting-guide.md)
- [references/corpus-derived-patterns.md](modules/nature-paper-to-patent/references/corpus-derived-patterns.md)
- [references/corpus-pair-audit.md](modules/nature-paper-to-patent/references/corpus-pair-audit.md)
- [references/disclosure/correction_handler.md](modules/nature-paper-to-patent/references/disclosure/correction_handler.md)
- [references/disclosure/disclosure_builder.md](modules/nature-paper-to-patent/references/disclosure/disclosure_builder.md)
- [references/disclosure/disclosure_preview.md](modules/nature-paper-to-patent/references/disclosure/disclosure_preview.md)
- [references/disclosure/disclosure_self_check.md](modules/nature-paper-to-patent/references/disclosure/disclosure_self_check.md)
- [references/disclosure/intake.md](modules/nature-paper-to-patent/references/disclosure/intake.md)
- [references/disclosure/iteration_context.md](modules/nature-paper-to-patent/references/disclosure/iteration_context.md)
- [references/disclosure/merger.md](modules/nature-paper-to-patent/references/disclosure/merger.md)
- [references/disclosure/patent_points_analyzer.md](modules/nature-paper-to-patent/references/disclosure/patent_points_analyzer.md)
- [references/disclosure/prior_art_search.md](modules/nature-paper-to-patent/references/disclosure/prior_art_search.md)
- [references/disclosure/project_scan.md](modules/nature-paper-to-patent/references/disclosure/project_scan.md)
- [references/disclosure/template_reference.md](modules/nature-paper-to-patent/references/disclosure/template_reference.md)
- [references/disclosure/tooling.md](modules/nature-paper-to-patent/references/disclosure/tooling.md)
- [references/draft-schema.md](modules/nature-paper-to-patent/references/draft-schema.md)
- [references/patent-figure-guide.md](modules/nature-paper-to-patent/references/patent-figure-guide.md)
- [static/core/output-contract.md](modules/nature-paper-to-patent/static/core/output-contract.md)
- [static/core/principles.md](modules/nature-paper-to-patent/static/core/principles.md)
- [static/core/workflow.md](modules/nature-paper-to-patent/static/core/workflow.md)
- [static/fragments/invention/algorithm-software.md](modules/nature-paper-to-patent/static/fragments/invention/algorithm-software.md)
- [static/fragments/invention/apparatus-system.md](modules/nature-paper-to-patent/static/fragments/invention/apparatus-system.md)
- [static/fragments/invention/mixed.md](modules/nature-paper-to-patent/static/fragments/invention/mixed.md)
- [static/fragments/invention/process-material.md](modules/nature-paper-to-patent/static/fragments/invention/process-material.md)
- [static/fragments/source/mixed-project.md](modules/nature-paper-to-patent/static/fragments/source/mixed-project.md)
- [static/fragments/source/pasted-text.md](modules/nature-paper-to-patent/static/fragments/source/pasted-text.md)
- [static/fragments/source/pdf-text.md](modules/nature-paper-to-patent/static/fragments/source/pdf-text.md)
- [static/fragments/source/scanned-pdf.md](modules/nature-paper-to-patent/static/fragments/source/scanned-pdf.md)
- [static/fragments/task/claim-set.md](modules/nature-paper-to-patent/static/fragments/task/claim-set.md)
- [static/fragments/task/disclosure-analysis.md](modules/nature-paper-to-patent/static/fragments/task/disclosure-analysis.md)
- [static/fragments/task/disclosure-iteration.md](modules/nature-paper-to-patent/static/fragments/task/disclosure-iteration.md)
- [static/fragments/task/full-draft.md](modules/nature-paper-to-patent/static/fragments/task/full-draft.md)
- [static/fragments/task/paper-patent-audit.md](modules/nature-paper-to-patent/static/fragments/task/paper-patent-audit.md)
- [static/fragments/task/technical-disclosure.md](modules/nature-paper-to-patent/static/fragments/task/technical-disclosure.md)

## nature-paper2ppt

[完整工作流](modules/nature-paper2ppt/WORKFLOW.md)

Create or improve a Chinese academic PPTX from a scientific paper or research reading notes, with source figures and speaker notes. Use for 论文做PPT、文献汇报、组会PPT and paper-based conference or defense presentations.

随包脚本 1 项；参考文档 15 项；模板/示例 0 项。

### 脚本

- [scripts/audit_pptx_quality.py](modules/nature-paper2ppt/scripts/audit_pptx_quality.py) — Lightweight PPTX QA for nature-paper2ppt outputs. The script intentionally uses only the Python standard library so it can run in minimal environments. It inspects PPTX XML for com

### 参考

- [README.md](modules/nature-paper2ppt/README.md)
- [README_EN.md](modules/nature-paper2ppt/README_EN.md)
- [references/design-and-layout.md](modules/nature-paper2ppt/references/design-and-layout.md)
- [references/figure-assets.md](modules/nature-paper2ppt/references/figure-assets.md)
- [references/self-review.md](modules/nature-paper2ppt/references/self-review.md)
- [static/core/output-and-quality.md](modules/nature-paper2ppt/static/core/output-and-quality.md)
- [static/core/principles.md](modules/nature-paper2ppt/static/core/principles.md)
- [static/core/toolchain.md](modules/nature-paper2ppt/static/core/toolchain.md)
- [static/core/workflow.md](modules/nature-paper2ppt/static/core/workflow.md)
- [static/fragments/paper_type/clinical.md](modules/nature-paper2ppt/static/fragments/paper_type/clinical.md)
- [static/fragments/paper_type/discovery.md](modules/nature-paper2ppt/static/fragments/paper_type/discovery.md)
- [static/fragments/paper_type/materials.md](modules/nature-paper2ppt/static/fragments/paper_type/materials.md)
- [static/fragments/paper_type/methods.md](modules/nature-paper2ppt/static/fragments/paper_type/methods.md)
- [static/fragments/paper_type/resource.md](modules/nature-paper2ppt/static/fragments/paper_type/resource.md)
- [static/fragments/paper_type/review.md](modules/nature-paper2ppt/static/fragments/paper_type/review.md)

## nature-paper2word

[完整工作流](modules/nature-paper2word/WORKFLOW.md)

Compile an academic Markdown manuscript into a journal- or school-compliant Word (.docx): declared typography, native OMML equations, three-line tables, cross-references, per-section page numbers, CSL bibliographies (GB/T 7714, APA, Nature, IEEE), and pre/post-export quality gates. 把学术论文的 Markdown 稿件导出为符合期刊或学位论文规范的 Word：摘要、公式编号、三线表、题注、交叉引用、目录域、参考文献。Use when the user wants a submission-ready .docx — 论文转 Word、学位论文排版、期刊投稿排版、prepare submission docx — or a readable copy of a manuscript. Not for PDF, HTML or LaTeX output, and not for slide decks or grant forms.

随包脚本 0 项；参考文档 2 项；模板/示例 0 项。

### 参考

- [README.md](modules/nature-paper2word/README.md)
- [README_EN.md](modules/nature-paper2word/README_EN.md)

## nature-polishing

[完整工作流](modules/nature-polishing/WORKFLOW.md)

Polish, translate, or tighten existing academic prose while preserving facts, terminology, and evidence boundaries. Use for 论文润色、学术翻译、正文精简, or manuscript LaTeX layout fixes. Use nature-writing when the main task is drafting new sections or rebuilding the manuscript argument.

随包脚本 0 项；参考文档 30 项；模板/示例 0 项。

### 参考

- [README.md](modules/nature-polishing/README.md)
- [README_EN.md](modules/nature-polishing/README_EN.md)
- [references/latex-layout.md](modules/nature-polishing/references/latex-layout.md)
- [references/nat-comms-2025-diction.md](modules/nature-polishing/references/nat-comms-2025-diction.md)
- [references/phrasebank-playbook.md](modules/nature-polishing/references/phrasebank-playbook.md)
- [references/published-article-patterns.md](modules/nature-polishing/references/published-article-patterns.md)
- [references/section-moves.md](modules/nature-polishing/references/section-moves.md)
- [references/style-guardrails.md](modules/nature-polishing/references/style-guardrails.md)
- [references/writing-strategy.md](modules/nature-polishing/references/writing-strategy.md)
- [static/core/failure-modes.md](modules/nature-polishing/static/core/failure-modes.md)
- [static/core/output-format.md](modules/nature-polishing/static/core/output-format.md)
- [static/core/stance.md](modules/nature-polishing/static/core/stance.md)
- [static/fragments/journal/generic.md](modules/nature-polishing/static/fragments/journal/generic.md)
- [static/fragments/journal/nat-comms.md](modules/nature-polishing/static/fragments/journal/nat-comms.md)
- [static/fragments/journal/nat-mach-intell.md](modules/nature-polishing/static/fragments/journal/nat-mach-intell.md)
- [static/fragments/journal/nature.md](modules/nature-polishing/static/fragments/journal/nature.md)
- [static/fragments/language/en.md](modules/nature-polishing/static/fragments/language/en.md)
- [static/fragments/language/zh-to-en.md](modules/nature-polishing/static/fragments/language/zh-to-en.md)
- [static/fragments/paper_type/algorithmic.md](modules/nature-polishing/static/fragments/paper_type/algorithmic.md)
- [static/fragments/paper_type/hypothesis.md](modules/nature-polishing/static/fragments/paper_type/hypothesis.md)
- [static/fragments/paper_type/methods.md](modules/nature-polishing/static/fragments/paper_type/methods.md)
- [static/fragments/paper_type/research.md](modules/nature-polishing/static/fragments/paper_type/research.md)
- [static/fragments/paper_type/review.md](modules/nature-polishing/static/fragments/paper_type/review.md)
- [static/fragments/section/abstract.md](modules/nature-polishing/static/fragments/section/abstract.md)
- [static/fragments/section/conclusion.md](modules/nature-polishing/static/fragments/section/conclusion.md)
- [static/fragments/section/discussion.md](modules/nature-polishing/static/fragments/section/discussion.md)
- [static/fragments/section/intro.md](modules/nature-polishing/static/fragments/section/intro.md)
- [static/fragments/section/methods.md](modules/nature-polishing/static/fragments/section/methods.md)
- [static/fragments/section/results.md](modules/nature-polishing/static/fragments/section/results.md)
- [static/fragments/section/title.md](modules/nature-polishing/static/fragments/section/title.md)

## nature-proposal-writer

[完整工作流](modules/nature-proposal-writer/WORKFLOW.md)

Compose, revise, or audit research proposals, opening reports, and research plans from supporting evidence. Use for 研究计划、开题报告、科研项目申请书. Invoked as researchwrite for compatibility; use nature-writing for general manuscript sections.

随包脚本 3 项；参考文档 30 项；模板/示例 8 项。

### 脚本

- [scripts/build_proposal_docx.py](modules/nature-proposal-writer/scripts/build_proposal_docx.py) — Convert researchwrite proposal markdown to properly formatted .docx. Usage: python3 scripts/build_proposal_docx.py <input.md> [output.docx] Formatting standard for academic proposa
- [tests/test_source_preservation.py](modules/nature-proposal-writer/tests/test_source_preservation.py) — SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_proposal_docx.py"
- [tests/test_table_delimiters.py](modules/nature-proposal-writer/tests/test_table_delimiters.py) — SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_proposal_docx.py"

### 参考

- [README.md](modules/nature-proposal-writer/README.md)
- [README_EN.md](modules/nature-proposal-writer/README_EN.md)
- [references/chinese-review-writing-style.md](modules/nature-proposal-writer/references/chinese-review-writing-style.md)
- [references/compose-mode.md](modules/nature-proposal-writer/references/compose-mode.md)
- [references/evaluation-rubric.md](modules/nature-proposal-writer/references/evaluation-rubric.md)
- [references/export-archive.md](modules/nature-proposal-writer/references/export-archive.md)
- [references/foundation-files.md](modules/nature-proposal-writer/references/foundation-files.md)
- [references/gpt-handoff-revision-brief.md](modules/nature-proposal-writer/references/gpt-handoff-revision-brief.md)
- [references/hybrid-mode.md](modules/nature-proposal-writer/references/hybrid-mode.md)
- [references/partial-proposal-scope.md](modules/nature-proposal-writer/references/partial-proposal-scope.md)
- [references/professor-dispatch.md](modules/nature-proposal-writer/references/professor-dispatch.md)
- [references/project-structure.md](modules/nature-proposal-writer/references/project-structure.md)
- [references/ref-renumbering-cascade.md](modules/nature-proposal-writer/references/ref-renumbering-cascade.md)
- [references/research-anti-slop.md](modules/nature-proposal-writer/references/research-anti-slop.md)
- [references/review-critique-methodology.md](modules/nature-proposal-writer/references/review-critique-methodology.md)
- [references/review-paper-framework.md](modules/nature-proposal-writer/references/review-paper-framework.md)
- [references/revise-mode.md](modules/nature-proposal-writer/references/revise-mode.md)
- [references/stopping-rules.md](modules/nature-proposal-writer/references/stopping-rules.md)
- [references/validation-checklist.md](modules/nature-proposal-writer/references/validation-checklist.md)
- [references/within-approved-proposal.md](modules/nature-proposal-writer/references/within-approved-proposal.md)
- [references/worked-example-quaternary-proposal.md](modules/nature-proposal-writer/references/worked-example-quaternary-proposal.md)
- [references/降承诺提案模式.md](modules/nature-proposal-writer/references/降承诺提案模式.md)
- [templates/00_scope.md](modules/nature-proposal-writer/templates/00_scope.md)
- [templates/01_research_canon.md](modules/nature-proposal-writer/templates/01_research_canon.md)
- [templates/02_evidence_table.md](modules/nature-proposal-writer/templates/02_evidence_table.md)
- [templates/03_argument_map.md](modules/nature-proposal-writer/templates/03_argument_map.md)
- [templates/04_section_contracts.md](modules/nature-proposal-writer/templates/04_section_contracts.md)
- [templates/05_style_guide.md](modules/nature-proposal-writer/templates/05_style_guide.md)
- [templates/qa_report.md](modules/nature-proposal-writer/templates/qa_report.md)
- [templates/revision_brief.md](modules/nature-proposal-writer/templates/revision_brief.md)

### 模板与示例

- [templates/00_scope.md](modules/nature-proposal-writer/templates/00_scope.md)
- [templates/01_research_canon.md](modules/nature-proposal-writer/templates/01_research_canon.md)
- [templates/02_evidence_table.md](modules/nature-proposal-writer/templates/02_evidence_table.md)
- [templates/03_argument_map.md](modules/nature-proposal-writer/templates/03_argument_map.md)
- [templates/04_section_contracts.md](modules/nature-proposal-writer/templates/04_section_contracts.md)
- [templates/05_style_guide.md](modules/nature-proposal-writer/templates/05_style_guide.md)
- [templates/qa_report.md](modules/nature-proposal-writer/templates/qa_report.md)
- [templates/revision_brief.md](modules/nature-proposal-writer/templates/revision_brief.md)

## nature-response

[完整工作流](modules/nature-response/WORKFLOW.md)

Draft, audit, or revise responses to peer review, revision cover letters, and marked-manuscript or LaTeX revision packages. Use for 审稿意见回复、逐点回复、返修信、 rebuttals and edits to existing response drafts. Initial-submission materials belong to nature-writing; simulated peer review belongs to nature-reviewer.

随包脚本 3 项；参考文档 29 项；模板/示例 3 项。

### 脚本

- [scripts/check_package_consistency.py](modules/nature-response/scripts/check_package_consistency.py) — Check mechanical consistency across a LaTeX revision package.
- [tests/test_package_consistency.py](modules/nature-response/tests/test_package_consistency.py) — SCRIPT = Path(__file__).parents[1] / "scripts" / "check_package_consistency.py"
- [tests/test_response_instruction_contracts.py](modules/nature-response/tests/test_response_instruction_contracts.py) — ROOT = Path(__file__).parents[1]

### 参考

- [examples/conflicting-reviewers.md](modules/nature-response/examples/conflicting-reviewers.md)
- [examples/major-revision-with-missing-evidence.md](modules/nature-response/examples/major-revision-with-missing-evidence.md)
- [examples/minor-revision.md](modules/nature-response/examples/minor-revision.md)
- [README.md](modules/nature-response/README.md)
- [README_EN.md](modules/nature-response/README_EN.md)
- [references/action-mapping.md](modules/nature-response/references/action-mapping.md)
- [references/chinese-author-alignment.md](modules/nature-response/references/chinese-author-alignment.md)
- [references/comment-taxonomy.md](modules/nature-response/references/comment-taxonomy.md)
- [references/difficult-cases.md](modules/nature-response/references/difficult-cases.md)
- [references/intake-and-routing.md](modules/nature-response/references/intake-and-routing.md)
- [references/latex-templates.md](modules/nature-response/references/latex-templates.md)
- [references/package-consistency-audit.md](modules/nature-response/references/package-consistency-audit.md)
- [references/qa-checklist.md](modules/nature-response/references/qa-checklist.md)
- [references/response-structure.md](modules/nature-response/references/response-structure.md)
- [references/source-basis.md](modules/nature-response/references/source-basis.md)
- [references/tone-and-stance.md](modules/nature-response/references/tone-and-stance.md)
- [static/core/stance.md](modules/nature-response/static/core/stance.md)
- [static/core/workflow.md](modules/nature-response/static/core/workflow.md)
- [tests/conflicting-reviewers.md](modules/nature-response/tests/conflicting-reviewers.md)
- [tests/defensive-draft-audit.md](modules/nature-response/tests/defensive-draft-audit.md)
- [tests/evaluation-summary.md](modules/nature-response/tests/evaluation-summary.md)
- [tests/impossible-experiment.md](modules/nature-response/tests/impossible-experiment.md)
- [tests/local-edit-without-decision.md](modules/nature-response/tests/local-edit-without-decision.md)
- [tests/major-revision-missing-evidence.md](modules/nature-response/tests/major-revision-missing-evidence.md)
- [tests/minor-revision.md](modules/nature-response/tests/minor-revision.md)
- [tests/reviewer-visibility.md](modules/nature-response/tests/reviewer-visibility.md)
- [tests/rubric.md](modules/nature-response/tests/rubric.md)
- [tests/task-status-tracking.md](modules/nature-response/tests/task-status-tracking.md)
- [tests/unclear-decision-type.md](modules/nature-response/tests/unclear-decision-type.md)

### 模板与示例

- [templates/cover-letter.tex](modules/nature-response/templates/cover-letter.tex)
- [templates/response-to-reviewers.tex](modules/nature-response/templates/response-to-reviewers.tex)
- [templates/revised-manuscript-redline.tex](modules/nature-response/templates/revised-manuscript-redline.tex)

## nature-reviewer

[完整工作流](modules/nature-reviewer/WORKFLOW.md)

Provide evidence-grounded mock peer review of scientific manuscripts or excerpts, covering significance, validity, and major/minor concerns. Use for 模拟审稿、投稿前自审、审稿人视角评估; not author rebuttal drafting.

随包脚本 1 项；参考文档 17 项；模板/示例 0 项。

### 脚本

- [tests/test_reviewer_instruction_contracts.py](modules/nature-reviewer/tests/test_reviewer_instruction_contracts.py) — ROOT = Path(__file__).parents[1]

### 参考

- [CHANGELOG.md](modules/nature-reviewer/CHANGELOG.md)
- [README.md](modules/nature-reviewer/README.md)
- [README_EN.md](modules/nature-reviewer/README_EN.md)
- [references/domain-specific-review-gates.md](modules/nature-reviewer/references/domain-specific-review-gates.md)
- [references/editorial criteria and processes.md](modules/nature-reviewer/references/editorial criteria and processes.md)
- [references/forensic-consistency-audit.md](modules/nature-reviewer/references/forensic-consistency-audit.md)
- [references/qa-checklist.md](modules/nature-reviewer/references/qa-checklist.md)
- [references/report-structure.md](modules/nature-reviewer/references/report-structure.md)
- [references/review-axes.md](modules/nature-reviewer/references/review-axes.md)
- [references/reviewer-workflow.md](modules/nature-reviewer/references/reviewer-workflow.md)
- [references/role-boundaries.md](modules/nature-reviewer/references/role-boundaries.md)
- [references/source-basis.md](modules/nature-reviewer/references/source-basis.md)
- [references/technical-concern-taxonomy.md](modules/nature-reviewer/references/technical-concern-taxonomy.md)
- [tests/punctuation-style.md](modules/nature-reviewer/tests/punctuation-style.md)
- [tests/reviewer-independence.md](modules/nature-reviewer/tests/reviewer-independence.md)
- [tests/severity-tiering.md](modules/nature-reviewer/tests/severity-tiering.md)
- [tests/traceable-review.md](modules/nature-reviewer/tests/traceable-review.md)

## nature-shared

[完整工作流](modules/nature-shared/WORKFLOW.md)

Internal shared-reference support package for installed Nature Skills, including nature-writing, nature-polishing, nature-response, nature-reader, and nature-paper2ppt. Do not invoke it as a standalone user workflow. Load only the specific core or journal-format file requested by another Nature skill.

随包脚本 2 项；参考文档 16 项；模板/示例 0 项。

### 脚本

- [scripts/check_consistency.py](modules/nature-shared/scripts/check_consistency.py) — Find mechanically detectable consistency risks in manuscript text files.
- [tests/test_check_consistency.py](modules/nature-shared/tests/test_check_consistency.py) — SCRIPT = Path(__file__).parents[1] / "scripts" / "check_consistency.py"

### 参考

- [core/consistency-sweep.md](modules/nature-shared/core/consistency-sweep.md)
- [core/discussion-argument-language.md](modules/nature-shared/core/discussion-argument-language.md)
- [core/ethics.md](modules/nature-shared/core/ethics.md)
- [core/main-text-discipline.md](modules/nature-shared/core/main-text-discipline.md)
- [core/nature-abstract.md](modules/nature-shared/core/nature-abstract.md)
- [core/nature-introduction.md](modules/nature-shared/core/nature-introduction.md)
- [core/nature-results-discussion.md](modules/nature-shared/core/nature-results-discussion.md)
- [core/paper-type-taxonomy.md](modules/nature-shared/core/paper-type-taxonomy.md)
- [core/reader-workflow.md](modules/nature-shared/core/reader-workflow.md)
- [core/research-compliance.md](modules/nature-shared/core/research-compliance.md)
- [core/terminology-ledger.md](modules/nature-shared/core/terminology-ledger.md)
- [journal-formats/nat-comms.md](modules/nature-shared/journal-formats/nat-comms.md)
- [journal-formats/nature-machine-intelligence.md](modules/nature-shared/journal-formats/nature-machine-intelligence.md)
- [journal-formats/nature.md](modules/nature-shared/journal-formats/nature.md)
- [README.md](modules/nature-shared/README.md)
- [README_EN.md](modules/nature-shared/README_EN.md)

## nature-statistics

[完整工作流](modules/nature-statistics/WORKFLOW.md)

Audit or improve manuscript statistical reporting, including experimental units, replication, uncertainty, tests, and figure statistics. Use for 统计审查、统计方法小节、图注统计 and reviewer concerns; compute new analyses only when requested with data.

随包脚本 0 项；参考文档 8 项；模板/示例 0 项。

### 参考

- [README.md](modules/nature-statistics/README.md)
- [README_EN.md](modules/nature-statistics/README_EN.md)
- [references/common-failure-modes.md](modules/nature-statistics/references/common-failure-modes.md)
- [references/figure-statistics.md](modules/nature-statistics/references/figure-statistics.md)
- [references/nature-article-requirements.md](modules/nature-statistics/references/nature-article-requirements.md)
- [references/reviewer-checklist.md](modules/nature-statistics/references/reviewer-checklist.md)
- [references/source-basis.md](modules/nature-statistics/references/source-basis.md)
- [references/statistical-reporting.md](modules/nature-statistics/references/statistical-reporting.md)

## nature-writing

[完整工作流](modules/nature-writing/WORKFLOW.md)

Draft or restructure scientific manuscript arguments, sections, and initial-submission materials from author-provided evidence. Use for 论文写作、章节起草、论证重构、正文压缩、首次投稿材料. Use nature-polishing for language-only edits to existing prose and nature-response for post-decision correspondence.

随包脚本 0 项；参考文档 70 项；模板/示例 4 项。

### 参考

- [README.md](modules/nature-writing/README.md)
- [README_EN.md](modules/nature-writing/README_EN.md)
- [references/abstract.md](modules/nature-writing/references/abstract.md)
- [references/article-architecture.md](modules/nature-writing/references/article-architecture.md)
- [references/chinese-author-workflow.md](modules/nature-writing/references/chinese-author-workflow.md)
- [references/conclusion.md](modules/nature-writing/references/conclusion.md)
- [references/examples/abstract/template-a.md](modules/nature-writing/references/examples/abstract/template-a.md)
- [references/examples/abstract/template-b.md](modules/nature-writing/references/examples/abstract/template-b.md)
- [references/examples/abstract/template-c.md](modules/nature-writing/references/examples/abstract/template-c.md)
- [references/examples/abstract-examples.md](modules/nature-writing/references/examples/abstract-examples.md)
- [references/examples/index.md](modules/nature-writing/references/examples/index.md)
- [references/examples/introduction/novel-task-challenge-decomposition.md](modules/nature-writing/references/examples/introduction/novel-task-challenge-decomposition.md)
- [references/examples/introduction/pipeline-not-recommended-abstract-only.md](modules/nature-writing/references/examples/introduction/pipeline-not-recommended-abstract-only.md)
- [references/examples/introduction/pipeline-version-1-one-contribution-multi-advantages.md](modules/nature-writing/references/examples/introduction/pipeline-version-1-one-contribution-multi-advantages.md)
- [references/examples/introduction/pipeline-version-2-two-contributions.md](modules/nature-writing/references/examples/introduction/pipeline-version-2-two-contributions.md)
- [references/examples/introduction/pipeline-version-3-new-module-on-existing-pipeline.md](modules/nature-writing/references/examples/introduction/pipeline-version-3-new-module-on-existing-pipeline.md)
- [references/examples/introduction/pipeline-version-4-observation-driven.md](modules/nature-writing/references/examples/introduction/pipeline-version-4-observation-driven.md)
- [references/examples/introduction/technical-challenge-version-1-existing-task.md](modules/nature-writing/references/examples/introduction/technical-challenge-version-1-existing-task.md)
- [references/examples/introduction/technical-challenge-version-2-existing-task-insight-backed-by-traditional.md](modules/nature-writing/references/examples/introduction/technical-challenge-version-2-existing-task-insight-backed-by-traditional.md)
- [references/examples/introduction/technical-challenge-version-3-novel-task.md](modules/nature-writing/references/examples/introduction/technical-challenge-version-3-novel-task.md)
- [references/examples/introduction/version-1-task-then-application.md](modules/nature-writing/references/examples/introduction/version-1-task-then-application.md)
- [references/examples/introduction/version-2-application-first.md](modules/nature-writing/references/examples/introduction/version-2-application-first.md)
- [references/examples/introduction/version-3-general-to-specific-setting.md](modules/nature-writing/references/examples/introduction/version-3-general-to-specific-setting.md)
- [references/examples/introduction/version-4-open-with-challenge.md](modules/nature-writing/references/examples/introduction/version-4-open-with-challenge.md)
- [references/examples/introduction-examples.md](modules/nature-writing/references/examples/introduction-examples.md)
- [references/examples/method/example-of-the-three-elements.md](modules/nature-writing/references/examples/method/example-of-the-three-elements.md)
- [references/examples/method/method-writing-common-issues-note.md](modules/nature-writing/references/examples/method/method-writing-common-issues-note.md)
- [references/examples/method/module-design-instant-ngp.md](modules/nature-writing/references/examples/method/module-design-instant-ngp.md)
- [references/examples/method/module-motivation-patterns.md](modules/nature-writing/references/examples/method/module-motivation-patterns.md)
- [references/examples/method/module-triad-neural-body.md](modules/nature-writing/references/examples/method/module-triad-neural-body.md)
- [references/examples/method/neural-body-annotated-figure-text.md](modules/nature-writing/references/examples/method/neural-body-annotated-figure-text.md)
- [references/examples/method/overview-template.md](modules/nature-writing/references/examples/method/overview-template.md)
- [references/examples/method/pre-writing-questions.md](modules/nature-writing/references/examples/method/pre-writing-questions.md)
- [references/examples/method/section-skeleton.md](modules/nature-writing/references/examples/method/section-skeleton.md)
- [references/examples/method-examples.md](modules/nature-writing/references/examples/method-examples.md)
- [references/experiments.md](modules/nature-writing/references/experiments.md)
- [references/introduction.md](modules/nature-writing/references/introduction.md)
- [references/method.md](modules/nature-writing/references/method.md)
- [references/nat-comms-2025-corpus.md](modules/nature-writing/references/nat-comms-2025-corpus.md)
- [references/nature-summary-paragraph.md](modules/nature-writing/references/nature-summary-paragraph.md)
- [references/paper-review.md](modules/nature-writing/references/paper-review.md)
- [references/paragraph-flow.md](modules/nature-writing/references/paragraph-flow.md)
- [references/related-work.md](modules/nature-writing/references/related-work.md)
- [references/submission-package.md](modules/nature-writing/references/submission-package.md)
- [static/core/output-format.md](modules/nature-writing/static/core/output-format.md)
- [static/core/stance.md](modules/nature-writing/static/core/stance.md)
- [static/core/workflow.md](modules/nature-writing/static/core/workflow.md)
- [static/fragments/journal/generic.md](modules/nature-writing/static/fragments/journal/generic.md)
- [static/fragments/journal/nat-comms.md](modules/nature-writing/static/fragments/journal/nat-comms.md)
- [static/fragments/journal/nat-mach-intell.md](modules/nature-writing/static/fragments/journal/nat-mach-intell.md)
- [static/fragments/journal/nature-family.md](modules/nature-writing/static/fragments/journal/nature-family.md)
- [static/fragments/journal/nature.md](modules/nature-writing/static/fragments/journal/nature.md)
- [static/fragments/language/en.md](modules/nature-writing/static/fragments/language/en.md)
- [static/fragments/language/zh-to-en.md](modules/nature-writing/static/fragments/language/zh-to-en.md)
- [static/fragments/paper_type/algorithmic.md](modules/nature-writing/static/fragments/paper_type/algorithmic.md)
- [static/fragments/paper_type/hypothesis.md](modules/nature-writing/static/fragments/paper_type/hypothesis.md)
- [static/fragments/paper_type/methods.md](modules/nature-writing/static/fragments/paper_type/methods.md)
- [static/fragments/paper_type/research.md](modules/nature-writing/static/fragments/paper_type/research.md)
- [static/fragments/paper_type/review.md](modules/nature-writing/static/fragments/paper_type/review.md)
- [static/fragments/section/abstract.md](modules/nature-writing/static/fragments/section/abstract.md)
- [static/fragments/section/conclusion.md](modules/nature-writing/static/fragments/section/conclusion.md)
- [static/fragments/section/discussion.md](modules/nature-writing/static/fragments/section/discussion.md)
- [static/fragments/section/experiments.md](modules/nature-writing/static/fragments/section/experiments.md)
- [static/fragments/section/intro.md](modules/nature-writing/static/fragments/section/intro.md)
- [static/fragments/section/method.md](modules/nature-writing/static/fragments/section/method.md)
- [static/fragments/section/related-work.md](modules/nature-writing/static/fragments/section/related-work.md)
- [static/fragments/section/title.md](modules/nature-writing/static/fragments/section/title.md)
- [static/fragments/task/manuscript.md](modules/nature-writing/static/fragments/task/manuscript.md)
- [static/fragments/task/submission-package.md](modules/nature-writing/static/fragments/task/submission-package.md)
- [tests/scoped-drafting.md](modules/nature-writing/tests/scoped-drafting.md)

### 模板与示例

- [templates/submission/declarations-and-reviewers.tex](modules/nature-writing/templates/submission/declarations-and-reviewers.tex)
- [templates/submission/highlights-and-summary.tex](modules/nature-writing/templates/submission/highlights-and-summary.tex)
- [templates/submission/initial-cover-letter.tex](modules/nature-writing/templates/submission/initial-cover-letter.tex)
- [templates/submission/title-page.tex](modules/nature-writing/templates/submission/title-page.tex)

## networkx

[完整工作流](modules/networkx/WORKFLOW.md)

Creates, analyzes, and visualizes complex networks and graphs in Python with NetworkX. Use when working with network/graph data structures, computing graph algorithms (shortest paths, centrality, clustering), detecting communities, generating synthetic networks (random, scale-free, small-world), reading/writing graph file formats, or drawing network topologies. Common applications include social, biological, transportation, and citation networks.

随包脚本 0 项；参考文档 6 项；模板/示例 0 项。

### 参考

- [references/algorithms.md](modules/networkx/references/algorithms.md)
- [references/generators.md](modules/networkx/references/generators.md)
- [references/graph-basics.md](modules/networkx/references/graph-basics.md)
- [references/io.md](modules/networkx/references/io.md)
- [references/review.md](modules/networkx/references/review.md)
- [references/visualization.md](modules/networkx/references/visualization.md)

## office-academic-skill

[完整工作流](modules/office-academic-skill/WORKFLOW.md)

Chinese-first academic Word and PowerPoint workflow for paper reading reports, thesis or group-meeting PPTs, editable DOCX/PPTX generation, Office file inspection, template matching, speaker notes, and layout quality checks. Use when the user asks to read papers into Word reports, create or polish PPT/PPTX, convert paper/thesis materials into slides, edit DOCX/PPTX, inspect Office files, or produce Chinese academic presentation/report deliverables. Preserve English paper titles, formulas, variable names, software commands, and references.

随包脚本 32 项；参考文档 5 项；模板/示例 5 项。

### 脚本

- [references/office-docx/ooxml/scripts/pack.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/pack.py) — Tool to pack a directory into a .docx, .pptx, or .xlsx file with XML formatting undone. Example usage: python pack.py <input_directory> <office_file> [--force]
- [references/office-docx/ooxml/scripts/unpack.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/unpack.py) — Unpack and format XML contents of Office files (.docx, .pptx, .xlsx)
- [references/office-docx/ooxml/scripts/validate.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/validate.py) — Command line tool to validate Office document XML files against XSD schemas and tracked changes. Usage: python validate.py <dir> --original <original_file>
- [references/office-docx/ooxml/scripts/validation/__init__.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/validation/__init__.py) — Validation modules for Word document processing.
- [references/office-docx/ooxml/scripts/validation/base.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/validation/base.py) — Base validator with common validation logic for document files.
- [references/office-docx/ooxml/scripts/validation/docx.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/validation/docx.py) — Validator for Word document XML files against XSD schemas.
- [references/office-docx/ooxml/scripts/validation/pptx.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/validation/pptx.py) — Validator for PowerPoint presentation XML files against XSD schemas.
- [references/office-docx/ooxml/scripts/validation/redlining.py](modules/office-academic-skill/references/office-docx/ooxml/scripts/validation/redlining.py) — Validator for tracked changes in Word documents.
- [references/office-docx/scripts/__init__.py](modules/office-academic-skill/references/office-docx/scripts/__init__.py) — Make scripts directory a package for relative imports in tests
- [references/office-docx/scripts/document.py](modules/office-academic-skill/references/office-docx/scripts/document.py) — Library for working with Word documents: comments, tracked changes, and editing. Usage: from skills.docx.scripts.document import Document # Initialize doc = Document('workspace/unp
- [references/office-docx/scripts/utilities.py](modules/office-academic-skill/references/office-docx/scripts/utilities.py) — Utilities for editing OOXML documents. This module provides XMLEditor, a tool for manipulating XML files with support for line-number-based node finding and DOM manipulation. Each 
- [references/office-pptx/ooxml/scripts/pack.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/pack.py) — Tool to pack a directory into a .docx, .pptx, or .xlsx file with XML formatting undone. Example usage: python pack.py <input_directory> <office_file> [--force]
- [references/office-pptx/ooxml/scripts/unpack.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/unpack.py) — Unpack and format XML contents of Office files (.docx, .pptx, .xlsx)
- [references/office-pptx/ooxml/scripts/validate.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/validate.py) — Command line tool to validate Office document XML files against XSD schemas and tracked changes. Usage: python validate.py <dir> --original <original_file>
- [references/office-pptx/ooxml/scripts/validation/__init__.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/validation/__init__.py) — Validation modules for Word document processing.
- [references/office-pptx/ooxml/scripts/validation/base.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/validation/base.py) — Base validator with common validation logic for document files.
- [references/office-pptx/ooxml/scripts/validation/docx.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/validation/docx.py) — Validator for Word document XML files against XSD schemas.
- [references/office-pptx/ooxml/scripts/validation/pptx.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/validation/pptx.py) — Validator for PowerPoint presentation XML files against XSD schemas.
- [references/office-pptx/ooxml/scripts/validation/redlining.py](modules/office-academic-skill/references/office-pptx/ooxml/scripts/validation/redlining.py) — Validator for tracked changes in Word documents.
- [references/office-pptx/scripts/html2pptx.js](modules/office-academic-skill/references/office-pptx/scripts/html2pptx.js) — * html2pptx - Convert HTML slide to pptxgenjs slide with positioned elements
- [references/office-pptx/scripts/inventory.py](modules/office-academic-skill/references/office-pptx/scripts/inventory.py) — Extract structured text content from PowerPoint presentations. This module provides functionality to: - Extract all text content from PowerPoint shapes - Preserve paragraph formatt
- [references/office-pptx/scripts/rearrange.py](modules/office-academic-skill/references/office-pptx/scripts/rearrange.py) — Rearrange PowerPoint slides based on a sequence of indices. Usage: python rearrange.py template.pptx output.pptx 0,34,34,50,52 This will create output.pptx using slides from templa
- [references/office-pptx/scripts/replace.py](modules/office-academic-skill/references/office-pptx/scripts/replace.py) — Apply text replacements to PowerPoint presentation. Usage: python replace.py <input.pptx> <replacements.json> <output.pptx> The replacements JSON should have the structure output b
- [references/office-pptx/scripts/thumbnail.py](modules/office-academic-skill/references/office-pptx/scripts/thumbnail.py) — Create thumbnail grids from PowerPoint presentation slides. Creates a grid layout of slide thumbnails with configurable columns (max 6). Each grid contains up to cols×(cols+1) imag
- [references/thesis-defense-pptx/scripts/clone_template_deck.ps1](modules/office-academic-skill/references/thesis-defense-pptx/scripts/clone_template_deck.ps1) — $ErrorActionPreference = "Stop"
- [references/thesis-defense-pptx/scripts/dump_pptx_content.py](modules/office-academic-skill/references/thesis-defense-pptx/scripts/dump_pptx_content.py) — Dump every slide's shape/text/table/picture inventory to a Markdown file. 迭代填充时强烈推荐先跑这个脚本拿到模板/骨架的真实文本,再去构造 ``replace_exact_text`` 的 dict 或 ``write_table`` 的二维数组。直接靠肉眼 猜模板里的字符串很容易因为
- [references/thesis-defense-pptx/scripts/export_pptx_png.ps1](modules/office-academic-skill/references/thesis-defense-pptx/scripts/export_pptx_png.ps1) — $ErrorActionPreference = "Stop"
- [references/thesis-defense-pptx/scripts/extract_thesis_context.py](modules/office-academic-skill/references/thesis-defense-pptx/scripts/extract_thesis_context.py) — TEXT_EXTS = {".tex", ".bib", ".md", ".txt"}
- [references/thesis-defense-pptx/scripts/inspect_pptx_overflow.ps1](modules/office-academic-skill/references/thesis-defense-pptx/scripts/inspect_pptx_overflow.ps1) — $ErrorActionPreference = "Stop"
- [references/thesis-defense-pptx/scripts/make_contact_sheet.py](modules/office-academic-skill/references/thesis-defense-pptx/scripts/make_contact_sheet.py) — def slide_number(path: Path) -> int:
- [references/thesis-defense-pptx/scripts/pptx_template_tools.py](modules/office-academic-skill/references/thesis-defense-pptx/scripts/pptx_template_tools.py) — def _brand_red() -> RGBColor:
- [references/thesis-defense-pptx/scripts/scan_pptx_text.py](modules/office-academic-skill/references/thesis-defense-pptx/scripts/scan_pptx_text.py) — Windows 默认 stdout 是 cp936/gbk，遇到 −/✓/Δ 等 Unicode 字符会 UnicodeEncodeError。

### 参考

- [references/office-docx/docx-js.md](modules/office-academic-skill/references/office-docx/docx-js.md)
- [references/office-docx/ooxml.md](modules/office-academic-skill/references/office-docx/ooxml.md)
- [references/office-pptx/html2pptx.md](modules/office-academic-skill/references/office-pptx/html2pptx.md)
- [references/office-pptx/ooxml.md](modules/office-academic-skill/references/office-pptx/ooxml.md)
- [references/report-structure.md](modules/office-academic-skill/references/report-structure.md)

### 模板与示例

- [references/office-docx/scripts/templates/comments.xml](modules/office-academic-skill/references/office-docx/scripts/templates/comments.xml)
- [references/office-docx/scripts/templates/commentsExtended.xml](modules/office-academic-skill/references/office-docx/scripts/templates/commentsExtended.xml)
- [references/office-docx/scripts/templates/commentsExtensible.xml](modules/office-academic-skill/references/office-docx/scripts/templates/commentsExtensible.xml)
- [references/office-docx/scripts/templates/commentsIds.xml](modules/office-academic-skill/references/office-docx/scripts/templates/commentsIds.xml)
- [references/office-docx/scripts/templates/people.xml](modules/office-academic-skill/references/office-docx/scripts/templates/people.xml)

## paper-write

[完整工作流](modules/paper-write/WORKFLOW.md)

本科与硕士学位论文辅助。用于学位论文大纲、学校格式、章节结构、中文学位论文润色及参考文献整理；通用期刊论文起草优先 nature-writing，研究计划与开题报告优先 researchwrite。

随包脚本 0 项；参考文档 27 项；模板/示例 0 项。

### 参考

- [reference/abbreviate.md](modules/paper-write/reference/abbreviate.md)
- [reference/anti-aigc.md](modules/paper-write/reference/anti-aigc.md)
- [reference/check-issues-and-format.md](modules/paper-write/reference/check-issues-and-format.md)
- [reference/en-to-zh.md](modules/paper-write/reference/en-to-zh.md)
- [reference/expand.md](modules/paper-write/reference/expand.md)
- [reference/extract-structured.md](modules/paper-write/reference/extract-structured.md)
- [reference/merge.md](modules/paper-write/reference/merge.md)
- [reference/outline-review-liberal.md](modules/paper-write/reference/outline-review-liberal.md)
- [reference/outline-review-science.md](modules/paper-write/reference/outline-review-science.md)
- [reference/polish-experiment.md](modules/paper-write/reference/polish-experiment.md)
- [reference/polish-liberal.md](modules/paper-write/reference/polish-liberal.md)
- [reference/polish-science-experiment.md](modules/paper-write/reference/polish-science-experiment.md)
- [reference/polish.md](modules/paper-write/reference/polish.md)
- [reference/references.md](modules/paper-write/reference/references.md)
- [reference/structure-imitate-abstract.md](modules/paper-write/reference/structure-imitate-abstract.md)
- [reference/structure-imitate-experiment.md](modules/paper-write/reference/structure-imitate-experiment.md)
- [reference/structure-imitate-general.md](modules/paper-write/reference/structure-imitate-general.md)
- [reference/structure-imitate-introduction.md](modules/paper-write/reference/structure-imitate-introduction.md)
- [reference/structure-imitate-liberal-abstract.md](modules/paper-write/reference/structure-imitate-liberal-abstract.md)
- [reference/structure-imitate-liberal-case-analysis.md](modules/paper-write/reference/structure-imitate-liberal-case-analysis.md)
- [reference/structure-imitate-liberal-introduction.md](modules/paper-write/reference/structure-imitate-liberal-introduction.md)
- [reference/structure-imitate-liberal-literature-review.md](modules/paper-write/reference/structure-imitate-liberal-literature-review.md)
- [reference/structure-imitate-liberal-policy.md](modules/paper-write/reference/structure-imitate-liberal-policy.md)
- [reference/structure-imitate-science-abstract.md](modules/paper-write/reference/structure-imitate-science-abstract.md)
- [reference/structure-imitate-science-experiment.md](modules/paper-write/reference/structure-imitate-science-experiment.md)
- [reference/structure-imitate-science-introduction.md](modules/paper-write/reference/structure-imitate-science-introduction.md)
- [reference/zh-to-en.md](modules/paper-write/reference/zh-to-en.md)

## peer-review

[完整工作流](modules/peer-review/WORKFLOW.md)

Prepares evidence-bounded, constructive peer-review drafts and structured manuscript assessments. Supports authorized review of scientific manuscripts, protocols, preprints, or research proposals; reporting-guideline selection; claim–evidence checks; methods, statistics, reproducibility, ethics, figure/table, and citation critique; or revision-response planning.

随包脚本 8 项；参考文档 7 项；模板/示例 4 项。

### 脚本

- [scripts/_common.py](modules/peer-review/scripts/_common.py) — Shared, dependency-free safety helpers for local peer-review CLIs.
- [scripts/audit_citations.py](modules/peer-review/scripts/audit_citations.py) — Audit Markdown citation keys against a local reference CSV without network use.
- [scripts/audit_statistics_reproducibility.py](modules/peer-review/scripts/audit_statistics_reproducibility.py) — Audit a structured statistics and reproducibility checklist locally.
- [scripts/generate_review_scaffold.py](modules/peer-review/scripts/generate_review_scaffold.py) — Generate a local structured peer-review draft scaffold from validated intake.
- [scripts/lint_review.py](modules/peer-review/scripts/lint_review.py) — Lint a structured review for channel separation, tone, and actionability.
- [scripts/select_reporting_guidelines.py](modules/peer-review/scripts/select_reporting_guidelines.py) — Select bundled reporting guidance and audit checklist coverage locally.
- [scripts/validate_claim_evidence.py](modules/peer-review/scripts/validate_claim_evidence.py) — Validate a bounded claim-evidence alignment matrix without echoing prose.
- [scripts/validate_review_intake.py](modules/peer-review/scripts/validate_review_intake.py) — Validate peer-review scope, authorization, conflicts, and handling controls.

### 参考

- [assets/review_scaffold_template.md](modules/peer-review/assets/review_scaffold_template.md)
- [references/common_issues.md](modules/peer-review/references/common_issues.md)
- [references/ethical_review_practice.md](modules/peer-review/references/ethical_review_practice.md)
- [references/reporting_standards.md](modules/peer-review/references/reporting_standards.md)
- [references/security_validation.md](modules/peer-review/references/security_validation.md)
- [references/statistical_reproducibility.md](modules/peer-review/references/statistical_reproducibility.md)
- [references/tool_reference.md](modules/peer-review/references/tool_reference.md)

### 模板与示例

- [assets/reporting_guidelines.json](modules/peer-review/assets/reporting_guidelines.json)
- [assets/review_intake_template.json](modules/peer-review/assets/review_intake_template.json)
- [assets/statistical_reproducibility_template.json](modules/peer-review/assets/statistical_reproducibility_template.json)
- [assets/study_profile_template.json](modules/peer-review/assets/study_profile_template.json)

## polars

[完整工作流](modules/polars/WORKFLOW.md)

High-performance DataFrame library for Python ETL, analytics, and pandas migration. It supports expression-based data manipulation with lazy query optimization, parallel execution, streaming out-of-core processing, Arrow interoperability, and optional GPU execution.

随包脚本 0 项；参考文档 7 项；模板/示例 0 项。

### 参考

- [references/best_practices.md](modules/polars/references/best_practices.md)
- [references/core_concepts.md](modules/polars/references/core_concepts.md)
- [references/io_guide.md](modules/polars/references/io_guide.md)
- [references/operations.md](modules/polars/references/operations.md)
- [references/pandas_migration.md](modules/polars/references/pandas_migration.md)
- [references/review.md](modules/polars/references/review.md)
- [references/transformations.md](modules/polars/references/transformations.md)

## pptx-posters

[完整工作流](modules/pptx-posters/WORKFLOW.md)

Creates and audits editable scientific posters in macro-free PowerPoint (.pptx) from author-approved local content and assets. Used when the requested deliverable is a PowerPoint research/conference poster and exact physical, printer, accessibility, provenance, and package-security checks are required.

随包脚本 10 项；参考文档 8 项；模板/示例 2 项。

### 脚本

- [scripts/_common.py](modules/pptx-posters/scripts/_common.py) — Shared, dependency-free safety helpers for the poster command-line tools.
- [scripts/_manifest.py](modules/pptx-posters/scripts/_manifest.py) — Strict poster-manifest validation shared by generation and audit tools.
- [scripts/_pptx.py](modules/pptx-posters/scripts/_pptx.py) — Bounded, non-executing PPTX package inspection and layout analysis.
- [scripts/check_layout.py](modules/pptx-posters/scripts/check_layout.py) — Check PPTX shape bounds, overlap, reading order, and final font size.
- [scripts/check_palette.py](modules/pptx-posters/scripts/check_palette.py) — Report declared WCAG contrast and heuristic palette separation.
- [scripts/generate_poster.py](modules/pptx-posters/scripts/generate_poster.py) — Generate one macro-free PPTX poster from approved, strictly local JSON.
- [scripts/inspect_pptx.py](modules/pptx-posters/scripts/inspect_pptx.py) — Inspect a PPTX ZIP/XML package without opening or executing it.
- [scripts/inventory_images.py](modules/pptx-posters/scripts/inventory_images.py) — Build a hashed local-image inventory with final effective DPI.
- [scripts/plan_export.py](modules/pptx-posters/scripts/plan_export.py) — Create a requirement-bound PowerPoint export and print plan.
- [scripts/validate_manifest.py](modules/pptx-posters/scripts/validate_manifest.py) — Validate a fail-closed, author-approved local poster manifest.

### 参考

- [assets/poster_quality_checklist.md](modules/pptx-posters/assets/poster_quality_checklist.md)
- [references/manifest_spec.md](modules/pptx-posters/references/manifest_spec.md)
- [references/poster_content_guide.md](modules/pptx-posters/references/poster_content_guide.md)
- [references/poster_design_principles.md](modules/pptx-posters/references/poster_design_principles.md)
- [references/poster_layout_design.md](modules/pptx-posters/references/poster_layout_design.md)
- [references/pptx_security.md](modules/pptx-posters/references/pptx_security.md)
- [references/security_validation.md](modules/pptx-posters/references/security_validation.md)
- [references/source_ledger.md](modules/pptx-posters/references/source_ledger.md)

### 模板与示例

- [assets/generation_dependencies.json](modules/pptx-posters/assets/generation_dependencies.json)
- [assets/poster_manifest_template.json](modules/pptx-posters/assets/poster_manifest_template.json)

## pymc

[完整工作流](modules/pymc/WORKFLOW.md)

Builds and checks Bayesian models with PyMC, including hierarchical models, NUTS MCMC, variational inference, mutable-data predictions, posterior predictive checks, diagnostics, and PSIS-LOO model comparison. Use for probabilistic modeling and uncertainty inference in PyMC.

随包脚本 4 项；参考文档 5 项；模板/示例 0 项。

### 脚本

- [assets/hierarchical_model_template.py](modules/pymc/assets/hierarchical_model_template.py) — Synthetic hierarchical regression with existing- and new-group predictions. Targets PyMC 6.3.2 / ArviZ 1.3. This model assumes independent group intercept and slope effects. For co
- [assets/linear_regression_template.py](modules/pymc/assets/linear_regression_template.py) — Runnable synthetic PyMC 6.3.2 / ArviZ 1.3 linear regression template. Replace the synthetic data with your measurements, preserve training scaling, and choose priors in outcome uni
- [scripts/model_comparison.py](modules/pymc/scripts/model_comparison.py) — PyMC Model Comparison Script Utilities for comparing multiple Bayesian models using information criteria and cross-validation metrics. Usage: from scripts.model_comparison import c
- [scripts/model_diagnostics.py](modules/pymc/scripts/model_diagnostics.py) — PyMC Model Diagnostics Script Comprehensive diagnostic checks for PyMC models. Run this after sampling to validate results before interpretation. Usage: from scripts.model_diagnost

### 参考

- [references/distributions.md](modules/pymc/references/distributions.md)
- [references/model_patterns.md](modules/pymc/references/model_patterns.md)
- [references/sampling_inference.md](modules/pymc/references/sampling_inference.md)
- [references/standard_workflow.md](modules/pymc/references/standard_workflow.md)
- [references/workflows.md](modules/pymc/references/workflows.md)

## pymoo

[完整工作流](modules/pymoo/WORKFLOW.md)

Solves and validates single-, multi-, and many-objective optimization with pymoo, including NSGA-II, NSGA-III, MOEA/D, constraints, Pareto approximations, reference directions, and ZDT/DTLZ benchmarks for engineering and research problems.

随包脚本 5 项；参考文档 8 项；模板/示例 0 项。

### 脚本

- [scripts/custom_problem_example.py](modules/pymoo/scripts/custom_problem_example.py) — Custom problem definition example using pymoo. This script demonstrates how to define a custom optimization problem and solve it using pymoo.
- [scripts/decision_making_example.py](modules/pymoo/scripts/decision_making_example.py) — Multi-criteria decision making example using pymoo. This script demonstrates how to select preferred solutions from an approximate Pareto front using various MCDM methods.
- [scripts/many_objective_example.py](modules/pymoo/scripts/many_objective_example.py) — Many-objective optimization example using pymoo. This script demonstrates many-objective optimization (4+ objectives) using NSGA-III on the DTLZ2 benchmark problem.
- [scripts/multi_objective_example.py](modules/pymoo/scripts/multi_objective_example.py) — Multi-objective optimization example using pymoo. This script demonstrates multi-objective optimization using NSGA-II on the ZDT1 benchmark problem.
- [scripts/single_objective_example.py](modules/pymoo/scripts/single_objective_example.py) — Single-objective optimization example using pymoo. This script demonstrates basic single-objective optimization using the Genetic Algorithm on the Sphere function.

### 参考

- [references/algorithms.md](modules/pymoo/references/algorithms.md)
- [references/constraints_mcdm.md](modules/pymoo/references/constraints_mcdm.md)
- [references/lifecycle.md](modules/pymoo/references/lifecycle.md)
- [references/operators.md](modules/pymoo/references/operators.md)
- [references/parallelization.md](modules/pymoo/references/parallelization.md)
- [references/problems.md](modules/pymoo/references/problems.md)
- [references/quick_start_workflows.md](modules/pymoo/references/quick_start_workflows.md)
- [references/visualization.md](modules/pymoo/references/visualization.md)

## research-grants

[完整工作流](modules/research-grants/WORKFLOW.md)

Supports research proposal preparation and review for NSF, NIH, DOE, DARPA, and Taiwan NSTC, including opportunity-specific requirements, aims, review criteria, budgets, broader impacts, forms, and resubmissions. Use for investigator-authored grant development, compliance matrices, and proposal critiques.

随包脚本 0 项；参考文档 15 项；模板/示例 0 项。

### 参考

- [assets/budget_justification_template.md](modules/research-grants/assets/budget_justification_template.md)
- [assets/nih_specific_aims_template.md](modules/research-grants/assets/nih_specific_aims_template.md)
- [assets/nsf_project_summary_template.md](modules/research-grants/assets/nsf_project_summary_template.md)
- [references/broader_impacts.md](modules/research-grants/references/broader_impacts.md)
- [references/core_components.md](modules/research-grants/references/core_components.md)
- [references/darpa_guidelines.md](modules/research-grants/references/darpa_guidelines.md)
- [references/doe_guidelines.md](modules/research-grants/references/doe_guidelines.md)
- [references/nih_guidelines.md](modules/research-grants/references/nih_guidelines.md)
- [references/nsf_guidelines.md](modules/research-grants/references/nsf_guidelines.md)
- [references/nstc_guidelines.md](modules/research-grants/references/nstc_guidelines.md)
- [references/proposal_types_and_resubmission.md](modules/research-grants/references/proposal_types_and_resubmission.md)
- [references/README.md](modules/research-grants/references/README.md)
- [references/review_criteria.md](modules/research-grants/references/review_criteria.md)
- [references/specific_aims_guide.md](modules/research-grants/references/specific_aims_guide.md)
- [references/writing_principles.md](modules/research-grants/references/writing_principles.md)

## scholar-evaluation

[完整工作流](modules/scholar-evaluation/WORKFLOW.md)

Provides qualitative-first, evidence-traceable developmental review of scholarly works and audit low-stakes research-assessment rubrics with optional local quality controls. Never use for ranking people or consequential decisions.

随包脚本 8 项；参考文档 5 项；模板/示例 4 项。

### 脚本

- [scripts/_common.py](modules/scholar-evaluation/scripts/_common.py) — Bounded, dependency-free helpers for local scholar-evaluation records.
- [scripts/calculate_scores.py](modules/scholar-evaluation/scripts/calculate_scores.py) — Calculate transparent bounded rubric math for one scholarly work.
- [scripts/check_process.py](modules/scholar-evaluation/scripts/check_process.py) — Check low-stakes assessment governance and bias-process controls.
- [scripts/check_traceability.py](modules/scholar-evaluation/scripts/check_traceability.py) — Check criterion-to-evidence traceability without copying source content.
- [scripts/generate_report_scaffold.py](modules/scholar-evaluation/scripts/generate_report_scaffold.py) — Generate a minimized local JSON scaffold for qualified human review.
- [scripts/summarize_agreement.py](modules/scholar-evaluation/scripts/summarize_agreement.py) — Summarize inter-rater agreement from pseudonymous local CSV ratings.
- [scripts/validate_rubric.py](modules/scholar-evaluation/scripts/validate_rubric.py) — Validate a bounded scholar-evaluation rubric JSON file.
- [scripts/weight_sensitivity.py](modules/scholar-evaluation/scripts/weight_sensitivity.py) — Stress-test rubric weights and report scholarly-work order instability.

### 参考

- [references/evaluation_framework.md](modules/scholar-evaluation/references/evaluation_framework.md)
- [references/local_tooling.md](modules/scholar-evaluation/references/local_tooling.md)
- [references/responsible_assessment.md](modules/scholar-evaluation/references/responsible_assessment.md)
- [references/security_validation.md](modules/scholar-evaluation/references/security_validation.md)
- [references/source_ledger.md](modules/scholar-evaluation/references/source_ledger.md)

### 模板与示例

- [assets/evaluation_template.json](modules/scholar-evaluation/assets/evaluation_template.json)
- [assets/evidence_manifest_template.json](modules/scholar-evaluation/assets/evidence_manifest_template.json)
- [assets/process_checklist_template.json](modules/scholar-evaluation/assets/process_checklist_template.json)
- [assets/rubric_template.json](modules/scholar-evaluation/assets/rubric_template.json)

## scientific-schematics

[完整工作流](modules/scientific-schematics/WORKFLOW.md)

Generates scientific diagram drafts using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.7 Flash for quality review. Refines when the review requests improvement, with at most two generations. Specialized in neural network architectures, system diagrams, flowcharts, biological pathways, and complex scientific visualizations.

随包脚本 3 项；参考文档 2 项；模板/示例 0 项。

### 脚本

- [scripts/example_usage.sh](modules/scientific-schematics/scripts/example_usage.sh) — Example usage of AI-powered scientific schematic generation
- [scripts/generate_schematic.py](modules/scientific-schematics/scripts/generate_schematic.py) — Scientific schematic generation using Nano Banana 2. Generate any scientific diagram by describing it in natural language. Nano Banana 2 handles everything automatically with smart
- [scripts/generate_schematic_ai.py](modules/scientific-schematics/scripts/generate_schematic_ai.py) — AI-powered scientific schematic generation using Nano Banana 2. This script uses a smart iterative refinement approach: 1. Generate initial image with Nano Banana 2 2. AI quality r

### 参考

- [references/best_practices.md](modules/scientific-schematics/references/best_practices.md)
- [references/iterative_refinement.md](modules/scientific-schematics/references/iterative_refinement.md)

## scientific-slides

[完整工作流](modules/scientific-slides/WORKFLOW.md)

Builds slide decks and presentations for research talks. Used for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer.

随包脚本 7 项；参考文档 13 项；模板/示例 0 项。

### 脚本

- [scripts/generate_schematic.py](modules/scientific-slides/scripts/generate_schematic.py) — Scientific schematic generation using Nano Banana 2. Generate any scientific diagram by describing it in natural language. Nano Banana 2 handles everything automatically with smart
- [scripts/generate_schematic_ai.py](modules/scientific-slides/scripts/generate_schematic_ai.py) — AI-powered scientific schematic generation using Nano Banana 2. This script uses a smart iterative refinement approach: 1. Generate initial image with Nano Banana 2 2. AI quality r
- [scripts/generate_slide_image.py](modules/scientific-slides/scripts/generate_slide_image.py) — Slide image generation using Nano Banana 2. Generate presentation slides or visuals by describing them in natural language. Nano Banana 2 handles everything automatically with smar
- [scripts/generate_slide_image_ai.py](modules/scientific-slides/scripts/generate_slide_image_ai.py) — AI-powered slide image generation using Nano Banana 2. This script generates presentation slides or slide visuals using AI: - full_slide mode: Generate complete slides with title, 
- [scripts/pdf_to_images.py](modules/scientific-slides/scripts/pdf_to_images.py) — PDF to Images Converter for Presentations Converts presentation PDFs to images for visual inspection and review. Supports multiple output formats and resolutions. Uses PyMuPDF (fit
- [scripts/slides_to_pdf.py](modules/scientific-slides/scripts/slides_to_pdf.py) — Combine slide images into a single PDF presentation. This script takes multiple slide images (PNG, JPG) and combines them into a single PDF file, maintaining aspect ratio and quali
- [scripts/validate_presentation.py](modules/scientific-slides/scripts/validate_presentation.py) — Presentation Validation Script Validates scientific presentations for common issues: - Slide count vs. duration - LaTeX compilation - File size checks - Basic format validation

### 参考

- [assets/powerpoint_design_guide.md](modules/scientific-slides/assets/powerpoint_design_guide.md)
- [assets/timing_guidelines.md](modules/scientific-slides/assets/timing_guidelines.md)
- [references/beamer_guide.md](modules/scientific-slides/references/beamer_guide.md)
- [references/common_pitfalls.md](modules/scientific-slides/references/common_pitfalls.md)
- [references/data_visualization_slides.md](modules/scientific-slides/references/data_visualization_slides.md)
- [references/presentation_structure.md](modules/scientific-slides/references/presentation_structure.md)
- [references/presentation_workflow.md](modules/scientific-slides/references/presentation_workflow.md)
- [references/prompt_writing.md](modules/scientific-slides/references/prompt_writing.md)
- [references/script_reference.md](modules/scientific-slides/references/script_reference.md)
- [references/slide_capabilities.md](modules/scientific-slides/references/slide_capabilities.md)
- [references/slide_design_principles.md](modules/scientific-slides/references/slide_design_principles.md)
- [references/talk_types_guide.md](modules/scientific-slides/references/talk_types_guide.md)
- [references/visual_review_workflow.md](modules/scientific-slides/references/visual_review_workflow.md)

## scientific-visualization

[完整工作流](modules/scientific-visualization/WORKFLOW.md)

Creates and audits truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn, or Plotly. Use it for figure design, multi-panel layouts, uncertainty and missing-data displays, color/contrast review, image metadata validation, and journal export planning.

随包脚本 8 项；参考文档 5 项；模板/示例 1 项。

### 脚本

- [assets/color_palettes.py](modules/scientific-visualization/assets/color_palettes.py) — Curated sRGB palettes for scientific figures. Sources were checked 2026-10-01. Palette selection alone never establishes accessibility: audit the rendered foreground/background con
- [scripts/_common.py](modules/scientific-visualization/scripts/_common.py) — Shared, network-free safety helpers for visualization command-line tools.
- [scripts/export_plan.py](modules/scientific-visualization/scripts/export_plan.py) — Build and screen against dated publication-export planning snapshots.
- [scripts/figure_export.py](modules/scientific-visualization/scripts/figure_export.py) — Safe Matplotlib export helpers with explicit, auditable settings. This module does not certify journal compliance. Publisher profiles are dated planning snapshots and must be confi
- [scripts/image_metadata.py](modules/scientific-visualization/scripts/image_metadata.py) — Inspect figure/image metadata and screen it against explicit constraints. The tool is network-free. Pillow is loaded only for raster inputs and pypdf is loaded only for PDF inputs.
- [scripts/palette_audit.py](modules/scientific-visualization/scripts/palette_audit.py) — Audit palette contrast and heuristic grayscale distinguishability. WCAG contrast calculations are exact for the supplied sRGB values. Whether a specific WCAG success criterion appl
- [scripts/style_presets.py](modules/scientific-visualization/scripts/style_presets.py) — Scoped Matplotlib style presets for scientific figures. Presets are visual starting points, not journal-compliance profiles. Matplotlib is imported lazily so listing and help work 
- [scripts/style_preview.py](modules/scientific-visualization/scripts/style_preview.py) — Generate a deterministic preview for a bundled scientific figure style.

### 参考

- [references/color_palettes.md](modules/scientific-visualization/references/color_palettes.md)
- [references/journal_requirements.md](modules/scientific-visualization/references/journal_requirements.md)
- [references/matplotlib_examples.md](modules/scientific-visualization/references/matplotlib_examples.md)
- [references/publication_guidelines.md](modules/scientific-visualization/references/publication_guidelines.md)
- [references/sources.md](modules/scientific-visualization/references/sources.md)

### 模板与示例

- [assets/publisher_profiles.json](modules/scientific-visualization/assets/publisher_profiles.json)

## scientific-writing

[完整工作流](modules/scientific-writing/WORKFLOW.md)

Drafts, revises, and audits scientific manuscripts or reports with explicit evidence provenance, reporting-guideline coverage, authorship accountability, confidentiality controls, and local consistency checks. Use for manuscript sections, references, declarations, tables, figures, or submission preparation when scientific accuracy and traceability matter.

随包脚本 9 项；参考文档 14 项；模板/示例 6 项。

### 脚本

- [scripts/_common.py](modules/scientific-writing/scripts/_common.py) — Shared, dependency-free safety helpers for scientific-writing CLIs.
- [scripts/audit_claims.py](modules/scientific-writing/scripts/audit_claims.py) — Audit claim-to-evidence mappings and local citation markers.
- [scripts/check_consistency.py](modules/scientific-writing/scripts/check_consistency.py) — Check numeric and methods-results consistency in a bounded JSON registry.
- [scripts/check_references.py](modules/scientific-writing/scripts/check_references.py) — Check local reference identifiers and duplicates without resolving them.
- [scripts/lint_manuscript.py](modules/scientific-writing/scripts/lint_manuscript.py) — Lint manuscript Markdown for placeholders, language risks, and sensitive content.
- [scripts/scaffold_manuscript.py](modules/scientific-writing/scripts/scaffold_manuscript.py) — Generate a local, explicitly incomplete manuscript workspace.
- [scripts/select_reporting_guidelines.py](modules/scientific-writing/scripts/select_reporting_guidelines.py) — Select reporting guidance and check non-scoring coverage metadata.
- [scripts/validate_authorship.py](modules/scientific-writing/scripts/validate_authorship.py) — Validate human authorship, CRediT roles, accountability, and AI disclosure.
- [scripts/validate_manifest.py](modules/scientific-writing/scripts/validate_manifest.py) — Validate bounded manuscript and source manifests without network access.

### 参考

- [assets/manuscript_scaffold.md](modules/scientific-writing/assets/manuscript_scaffold.md)
- [assets/REPORT_FORMATTING_GUIDE.md](modules/scientific-writing/assets/REPORT_FORMATTING_GUIDE.md)
- [references/authorship_ai_confidentiality.md](modules/scientific-writing/references/authorship_ai_confidentiality.md)
- [references/citation_styles.md](modules/scientific-writing/references/citation_styles.md)
- [references/cli_reference.md](modules/scientific-writing/references/cli_reference.md)
- [references/evidence_workflow.md](modules/scientific-writing/references/evidence_workflow.md)
- [references/figures_tables.md](modules/scientific-writing/references/figures_tables.md)
- [references/imrad_structure.md](modules/scientific-writing/references/imrad_structure.md)
- [references/journal_policies.md](modules/scientific-writing/references/journal_policies.md)
- [references/professional_report_formatting.md](modules/scientific-writing/references/professional_report_formatting.md)
- [references/reporting_guidelines.md](modules/scientific-writing/references/reporting_guidelines.md)
- [references/research_integrity_open_science.md](modules/scientific-writing/references/research_integrity_open_science.md)
- [references/source_ledger.md](modules/scientific-writing/references/source_ledger.md)
- [references/writing_principles.md](modules/scientific-writing/references/writing_principles.md)

### 模板与示例

- [assets/authorship_template.json](modules/scientific-writing/assets/authorship_template.json)
- [assets/consistency_manifest_template.json](modules/scientific-writing/assets/consistency_manifest_template.json)
- [assets/manuscript_manifest_template.json](modules/scientific-writing/assets/manuscript_manifest_template.json)
- [assets/reporting_coverage_template.json](modules/scientific-writing/assets/reporting_coverage_template.json)
- [assets/reporting_guidelines.json](modules/scientific-writing/assets/reporting_guidelines.json)
- [assets/source_manifest_template.json](modules/scientific-writing/assets/source_manifest_template.json)

## scikit-learn

[完整工作流](modules/scikit-learn/WORKFLOW.md)

Supports machine learning in Python with scikit-learn. Applies when working with supervised learning (classification, regression), unsupervised learning (clustering, dimensionality reduction), model evaluation, hyperparameter tuning, preprocessing, or building ML pipelines. Provides comprehensive reference documentation for algorithms, preprocessing techniques, pipelines, and best practices.

随包脚本 2 项；参考文档 8 项；模板/示例 0 项。

### 脚本

- [scripts/classification_pipeline.py](modules/scikit-learn/scripts/classification_pipeline.py) — Complete classification pipeline example with preprocessing, model training, hyperparameter tuning, and evaluation.
- [scripts/clustering_analysis.py](modules/scikit-learn/scripts/clustering_analysis.py) — Clustering analysis example with multiple algorithms, evaluation, and visualization.

### 参考

- [references/common_workflows.md](modules/scikit-learn/references/common_workflows.md)
- [references/core_capabilities.md](modules/scikit-learn/references/core_capabilities.md)
- [references/model_evaluation.md](modules/scikit-learn/references/model_evaluation.md)
- [references/pipelines_and_composition.md](modules/scikit-learn/references/pipelines_and_composition.md)
- [references/preprocessing.md](modules/scikit-learn/references/preprocessing.md)
- [references/quick_reference.md](modules/scikit-learn/references/quick_reference.md)
- [references/supervised_learning.md](modules/scikit-learn/references/supervised_learning.md)
- [references/unsupervised_learning.md](modules/scikit-learn/references/unsupervised_learning.md)

## seaborn

[完整工作流](modules/seaborn/WORKFLOW.md)

Creates Seaborn statistical visualizations with pandas integration for distributions, relationships, categorical comparisons, regression displays, pair plots, and heatmaps. Supports function and objects interfaces with explicit aggregation, uncertainty, and missing-data handling. Best suited to static exploratory plots; plotly covers interactive figures and scientific-visualization covers publication styling.

随包脚本 0 项；参考文档 7 项；模板/示例 0 项。

### 参考

- [references/examples.md](modules/seaborn/references/examples.md)
- [references/function_reference.md](modules/seaborn/references/function_reference.md)
- [references/grids_and_levels.md](modules/seaborn/references/grids_and_levels.md)
- [references/objects_interface.md](modules/seaborn/references/objects_interface.md)
- [references/palettes_and_theming.md](modules/seaborn/references/palettes_and_theming.md)
- [references/patterns_and_troubleshooting.md](modules/seaborn/references/patterns_and_troubleshooting.md)
- [references/plotting_functions.md](modules/seaborn/references/plotting_functions.md)

## statistical-analysis

[完整工作流](modules/statistical-analysis/WORKFLOW.md)

Guided statistical analysis for research data - test selection, assumption checking, effect sizes, power analysis, Bayesian alternatives, and APA-formatted reporting. Use whenever a user wants to compare groups, test a hypothesis, analyze experimental or survey data, check statistical assumptions, compute required sample sizes, or write up results - even if they never name a specific test. Covers t-tests, ANOVA, chi-square, correlation, regression, non-parametric and Bayesian methods. For low-level model APIs, see the statsmodels and pymc skills.

随包脚本 1 项；参考文档 5 项；模板/示例 0 项。

### 脚本

- [scripts/assumption_checks.py](modules/statistical-analysis/scripts/assumption_checks.py) — Descriptive diagnostics, not an automatic test selector or proof of assumptions. NaNs are omitted with counts; infinities, malformed arrays, insufficient samples and undefined diag

### 参考

- [references/assumptions_and_diagnostics.md](modules/statistical-analysis/references/assumptions_and_diagnostics.md)
- [references/bayesian_statistics.md](modules/statistical-analysis/references/bayesian_statistics.md)
- [references/effect_sizes_and_power.md](modules/statistical-analysis/references/effect_sizes_and_power.md)
- [references/reporting_standards.md](modules/statistical-analysis/references/reporting_standards.md)
- [references/test_selection_guide.md](modules/statistical-analysis/references/test_selection_guide.md)

## statistical-power

[完整工作流](modules/statistical-power/WORKFLOW.md)

Calculates sample sizes and statistical power for study planning. Applies when someone asks "how many subjects/samples/replicates do I need", wants an a priori power analysis, a minimum detectable effect (MDE), a power curve, or needs to justify a sample size for a grant, IRB protocol, or pre-registration. Covers closed-form power for t-tests, ANOVA, proportions, correlations, chi-square, and regression, plus simulation-based (Monte Carlo) power for complex designs — logistic/Poisson regression, mixed models, cluster-randomized trials, survival, and interactions. Also handles requests that only mention an effect size, alpha, or "80% power" without saying "power analysis" explicitly. For laying out the study (randomization, blocking, factorial/DOE, crossover, sequential designs) use experimental-design; for analyzing data already collected and reporting it use statistical-analysis.

随包脚本 2 项；参考文档 3 项；模板/示例 0 项。

### 脚本

- [scripts/power.py](modules/statistical-power/scripts/power.py) — Unified closed-form power / sample-size interface over statsmodels and scipy. One function each for the three things people actually want: - sample_size(...) : solve for n given ef
- [scripts/simulate_power.py](modules/statistical-power/scripts/simulate_power.py) — Monte Carlo power when analytical assumptions do not match the design. Simulation can represent features omitted by simple analytical approximations for logistic/Poisson regression

### 参考

- [references/closed_form_recipes.md](modules/statistical-power/references/closed_form_recipes.md)
- [references/effect_sizes.md](modules/statistical-power/references/effect_sizes.md)
- [references/simulation_based_power.md](modules/statistical-power/references/simulation_based_power.md)

## statsmodels

[完整工作流](modules/statsmodels/WORKFLOW.md)

Fits and diagnoses Python statistical models including OLS, GLM, discrete and mixed models, ARIMA and SARIMAX. Supports coefficient inference, marginal effects, model comparison and time series forecasting with explicit design and uncertainty checks. Used for econometrics and statistical modeling; for guided test selection with APA reporting, see statistical-analysis.

随包脚本 0 项；参考文档 9 项；模板/示例 0 项。

### 参考

- [references/discrete_choice.md](modules/statsmodels/references/discrete_choice.md)
- [references/glm.md](modules/statsmodels/references/glm.md)
- [references/linear_models.md](modules/statsmodels/references/linear_models.md)
- [references/model_selection.md](modules/statsmodels/references/model_selection.md)
- [references/modeling_capabilities.md](modules/statsmodels/references/modeling_capabilities.md)
- [references/quick_start_guide.md](modules/statsmodels/references/quick_start_guide.md)
- [references/review.md](modules/statsmodels/references/review.md)
- [references/stats_diagnostics.md](modules/statsmodels/references/stats_diagnostics.md)
- [references/time_series.md](modules/statsmodels/references/time_series.md)

## sympy

[完整工作流](modules/sympy/WORKFLOW.md)

Performs exact symbolic mathematics with SymPy for algebra, calculus, equation solving, symbolic linear algebra, physics, and lambdify or LaTeX code generation. Use when a task needs symbolic results, explicit assumptions, or exact arithmetic; use NumPy or SciPy for purely numerical workloads.

随包脚本 0 项；参考文档 7 项；模板/示例 0 项。

### 参考

- [references/advanced-topics.md](modules/sympy/references/advanced-topics.md)
- [references/code-generation-printing.md](modules/sympy/references/code-generation-printing.md)
- [references/core-capabilities.md](modules/sympy/references/core-capabilities.md)
- [references/core_capabilities.md](modules/sympy/references/core_capabilities.md)
- [references/matrices-linear-algebra.md](modules/sympy/references/matrices-linear-algebra.md)
- [references/physics-mechanics.md](modules/sympy/references/physics-mechanics.md)
- [references/review.md](modules/sympy/references/review.md)

## venue-templates

[完整工作流](modules/venue-templates/WORKFLOW.md)

Prepares journal manuscripts, conference papers, research posters, and grant documents using venue-specific formatting guidance and bundled LaTeX scaffolds. Supports selecting an official template, checking current page or anonymity rules, adapting academic writing to a venue, or inspecting a submission PDF.

随包脚本 3 项；参考文档 16 项；模板/示例 0 项。

### 脚本

- [scripts/customize_template.py](modules/venue-templates/scripts/customize_template.py) — Customize Template Script Customize LaTeX templates with author information and project details. Usage: python customize_template.py --template nature_article.tex --output my_paper
- [scripts/query_template.py](modules/venue-templates/scripts/query_template.py) — List and query the templates actually bundled with venue-templates. Examples: python scripts/query_template.py --list-all python scripts/query_template.py --venue NeurIPS --require
- [scripts/validate_format.py](modules/venue-templates/scripts/validate_format.py) — Inspect a submission PDF using a verified limit or an explicit source. This tool does not infer where references or appendices begin and cannot prove margin or font-size compliance

### 参考

- [assets/examples/cell_summary_example.md](modules/venue-templates/assets/examples/cell_summary_example.md)
- [assets/examples/medical_structured_abstract.md](modules/venue-templates/assets/examples/medical_structured_abstract.md)
- [assets/examples/nature_abstract_examples.md](modules/venue-templates/assets/examples/nature_abstract_examples.md)
- [assets/examples/neurips_introduction_example.md](modules/venue-templates/assets/examples/neurips_introduction_example.md)
- [references/cell_press_style.md](modules/venue-templates/references/cell_press_style.md)
- [references/conferences_formatting.md](modules/venue-templates/references/conferences_formatting.md)
- [references/cs_conference_style.md](modules/venue-templates/references/cs_conference_style.md)
- [references/current_sources.md](modules/venue-templates/references/current_sources.md)
- [references/grants_requirements.md](modules/venue-templates/references/grants_requirements.md)
- [references/journals_formatting.md](modules/venue-templates/references/journals_formatting.md)
- [references/medical_journal_styles.md](modules/venue-templates/references/medical_journal_styles.md)
- [references/ml_conference_style.md](modules/venue-templates/references/ml_conference_style.md)
- [references/nature_science_style.md](modules/venue-templates/references/nature_science_style.md)
- [references/posters_guidelines.md](modules/venue-templates/references/posters_guidelines.md)
- [references/reviewer_expectations.md](modules/venue-templates/references/reviewer_expectations.md)
- [references/venue_writing_styles.md](modules/venue-templates/references/venue_writing_styles.md)
