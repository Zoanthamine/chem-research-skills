# 学术检索与阅读：完整能力目录

方法、脚本、参考和模板均按任务加载。本目录用于发现能力，完整操作流程在各 WORKFLOW 内；软件未安装时保留知识并按基础迁移说明补齐。

[实操与联动](references/applied-workflows.md) · [基础与迁移](references/foundation-and-migration.md)

## 主技能自带工具


## academic-research-suite

[完整工作流](modules/academic-research-suite/WORKFLOW.md)

Use for ARS workflows, systematic reviews, meta-analysis, study screening, or research-to-paper orchestration; prefer dedicated Nature skills for a single paper reading, polishing, citation, or response task.

随包脚本 502 项；参考文档 577 项；模板/示例 31 项。

### 脚本

- [ars/hooks/run_guard.sh](modules/academic-research-suite/ars/hooks/run_guard.sh) — version: 1.1.0
- [ars/pi/wrapper.integration.test.mjs](modules/academic-research-suite/ars/pi/wrapper.integration.test.mjs) — const packageRoot = process.env.PI_CODING_AGENT_ROOT;
- [ars/pi/wrapper.js](modules/academic-research-suite/ars/pi/wrapper.js) — const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
- [ars/pi/wrapper.test.mjs](modules/academic-research-suite/ars/pi/wrapper.test.mjs) — const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
- [ars/scripts/_block_parser.py](modules/academic-research-suite/ars/scripts/_block_parser.py) — Shared block parser for the diff/patch revision mode toolchain (#89 Item 7 Slice A). Normative source: `docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md` §3.1 (block seg
- [ars/scripts/_calibration_pdf_text.py](modules/academic-research-suite/ars/scripts/_calibration_pdf_text.py) — Shared manuscript hashing for the reviewer-calibration suite (#653). The corpus assembler (freeze / verify) and the isolated dispatcher must hash the SAME bytes for `pdf_sha256` an
- [ars/scripts/_claim_audit_constants.py](modules/academic-research-suite/ars/scripts/_claim_audit_constants.py) — Shared constants for v3.8 claim-faithfulness audit. Single source of truth for the literals + regexes that appear in BOTH the lint (`check_claim_audit_consistency.py`) and the pipe
- [ars/scripts/_e4_evidence.py](modules/academic-research-suite/ars/scripts/_e4_evidence.py) — Shared filesystem primitives for the E4 evidence boundary (#616).
- [ars/scripts/_eval_threshold_gate.py](modules/academic-research-suite/ars/scripts/_eval_threshold_gate.py) — Absolute-threshold verdict for the eval harness (#184 Delta 3 / Fix 1). Phase 1b has no ``main`` baseline, so the CI gate is an ABSOLUTE-threshold check, not a lift comparison. Thi
- [ars/scripts/_markdown_lint_util.py](modules/academic-research-suite/ars/scripts/_markdown_lint_util.py) — Shared markdown rendering semantics for the defrift lints (#771). Single authority for one question: what does GitHub render from this markdown? Inline code spans render literally 
- [ars/scripts/_next_verified_at_ms.py](modules/academic-research-suite/ars/scripts/_next_verified_at_ms.py) — Strict-monotonic verified_at helper for ARS v3.6.7 Step 6 (spec §5.4). Every orchestrator-side verdict.verified_at write — Path B8d normal merges, another_round re-merges, ship_wit
- [ars/scripts/_passport_yaml.py](modules/academic-research-suite/ars/scripts/_passport_yaml.py) — Shared ruamel.yaml round-trip configuration for passport migration tools. For tools that **mutate and re-emit** passport YAML (preserving comments, key order, quoting). Read-only v
- [ars/scripts/_skill_lint.py](modules/academic-research-suite/ars/scripts/_skill_lint.py) — Shared helpers for SKILL.md frontmatter linting + cross-lint H2-section literal checks. Frontmatter helpers (check_data_access_level.py, check_task_type.py) validate that every top
- [ars/scripts/_text_similarity.py](modules/academic-research-suite/ars/scripts/_text_similarity.py) — Shared title-similarity + retry-budget helpers for the v3.9.0 cross-index triangulation clients. Previously triple-implemented byte-equivalently in `semantic_scholar_client.py`, `o
- [ars/scripts/adapters/_common.py](modules/academic-research-suite/ars/scripts/adapters/_common.py) — Shared helpers for ARS reference adapters. These helpers are used by folder_scan.py, zotero.py, and obsidian.py. They are also what a user-written adapter would copy and adapt.
- [ars/scripts/adapters/folder_scan.py](modules/academic-research-suite/ars/scripts/adapters/folder_scan.py) — folder_scan: produce a literature_corpus passport from a directory of files (typically PDFs). Parses citation metadata from filenames using best-effort conventions. Never parses PD
- [ars/scripts/adapters/obsidian.py](modules/academic-research-suite/ars/scripts/adapters/obsidian.py) — obsidian: produce a literature_corpus passport from an Obsidian vault. Convention A (preferred): frontmatter carries citekey/title/authors/year/... Convention B (Karpathy-style): f
- [ars/scripts/adapters/tests/conftest.py](modules/academic-research-suite/ars/scripts/adapters/tests/conftest.py) — pytest configuration + shared fixtures for adapter tests. Provides: - `repo_root` : Path to the ARS repo root - `adapters_dir` : Path to scripts/adapters/ - `examples_dir` : Path t
- [ars/scripts/adapters/tests/test_check_corpus_consumer_protocol.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_check_corpus_consumer_protocol.py) — Tests for scripts/check_corpus_consumer_protocol.py. Each L1-L9 invariant has at least one positive test (passing case) and one negative test (failing case). The lint is manifest-d
- [ars/scripts/adapters/tests/test_check_literature_corpus_schema.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_check_literature_corpus_schema.py) — Tests for the CI lint that validates passport/rejection-log examples against their schemas and enforces citation_key uniqueness.
- [ars/scripts/adapters/tests/test_common.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_common.py) — Tests for the shared helpers used by every reference adapter.
- [ars/scripts/adapters/tests/test_conftest.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_conftest.py) — Self-tests for the shared adapter test fixtures. T7-T9 will use clean_timestamps and load_yaml extensively, so verify their behavior here before downstream tests depend on them.
- [ars/scripts/adapters/tests/test_folder_scan.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_folder_scan.py) — Tests for scripts/adapters/folder_scan.py.
- [ars/scripts/adapters/tests/test_literature_corpus_entry_schema.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_literature_corpus_entry_schema.py) — Validates literature_corpus_entry.schema.json self-consistency and round-trips a known-good example entry against it.
- [ars/scripts/adapters/tests/test_obsidian.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_obsidian.py) — Tests for scripts/adapters/obsidian.py.
- [ars/scripts/adapters/tests/test_rejection_log_schema.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_rejection_log_schema.py) — Validates rejection_log.schema.json self-consistency and example round-trip.
- [ars/scripts/adapters/tests/test_sync_adapter_docs.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_sync_adapter_docs.py) — Tests for sync_adapter_docs.py: schema → overview.md drift detector.
- [ars/scripts/adapters/tests/test_zotero.py](modules/academic-research-suite/ars/scripts/adapters/tests/test_zotero.py) — Tests for scripts/adapters/zotero.py.
- [ars/scripts/adapters/zotero.py](modules/academic-research-suite/ars/scripts/adapters/zotero.py) — zotero: produce a literature_corpus passport from a Better BibTeX Extension JSON export. Reads only local files; does not call the Zotero Web API. See design doc §5.3. Users who wa
- [ars/scripts/adjudication_activity.py](modules/academic-research-suite/ars/scripts/adjudication_activity.py) — Deterministic, advisory-only cross-run adjudication activity recorder. The runtime intentionally has no default paths, clock, network, model, judge, directory scan, or environment-
- [ars/scripts/announce-ars-loaded.sh](modules/academic-research-suite/ars/scripts/announce-ars-loaded.sh) — version: 1.5.0
- [ars/scripts/ars_anchorize_draft.py](modules/academic-research-suite/ars/scripts/ars_anchorize_draft.py) — Anchorize a draft: stamp block markers + emit the block manifest. #89 Item 7 Slice A. Normative source: `docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md` §3.1. What thi
- [ars/scripts/ars_apply_revision_patch.py](modules/academic-research-suite/ars/scripts/ars_apply_revision_patch.py) — Apply a revision patch to an anchored draft — two-phase, fail-closed. #89 Item 7 Slice A. Normative source: `docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md` §3.3 (dete
- [ars/scripts/ars_cache_invalidate.py](modules/academic-research-suite/ars/scripts/ars_cache_invalidate.py) — /ars-cache-invalidate CLI — drop cached verification entries for a citation. Backs the `/ars-cache-invalidate <citation_key>` slash command (Delta 2, deliverable 6). Removes every 
- [ars/scripts/ars_mark_read.py](modules/academic-research-suite/ars/scripts/ars_mark_read.py) — ARS /ars-mark-read + /ars-unmark-read CLI implementation. Implements v3.6.8 spec §3.6 + Step 7 (round-2 R2-002, round-5 R5-003 amends). The command writes a peer file `<passport-st
- [ars/scripts/ars_update_check.sh](modules/academic-research-suite/ars/scripts/ars_update_check.sh) — version: 1.0.0
- [ars/scripts/ars_write_scope_guard.py](modules/academic-research-suite/ars/scripts/ars_write_scope_guard.py) — ARS write-scope guard — PreToolUse hook (#134 Slice 1, the MVP). Spec: docs/design/2026-06-01-ars-134-conductor-rescope-deterministic-write-guard-spec.md Blocks out-of-scope file w
- [ars/scripts/arxiv_client.py](modules/academic-research-suite/ars/scripts/arxiv_client.py) — Minimal arXiv API client wrapper. Implements the lookup contract documented at `deep-research/references/arxiv_api_protocol.md`. arXiv-ID-first with title cross-check (ID_MISMATCH 
- [ars/scripts/assemble_calibration_corpus.py](modules/academic-research-suite/ars/scripts/assemble_calibration_corpus.py) — Gold-corpus manifest assembly for the reviewer-calibration suite (#653). The calibration protocol's resolved design decisions REJECT shipping a built-in gold set (domain-coverage b
- [ars/scripts/audit_panel_claims.py](modules/academic-research-suite/ars/scripts/audit_panel_claims.py) — Check the panel's findings against the manuscript (#1002, part 2). An advisory attachment to the Editorial Decision Letter, written after the decision is final (``academic-paper-re
- [ars/scripts/audit_snapshot.py](modules/academic-research-suite/ars/scripts/audit_snapshot.py) — audit_snapshot.py — ARS v3.6.7 Step 6 Phase 6.1 byte-exact snapshot helper. Reads bundle files (primary deliverable + supporting context + audit template + optional previous-findin
- [ars/scripts/bibliographic_integrity_signals.py](modules/academic-research-suite/ars/scripts/bibliographic_integrity_signals.py) — Canonical #678 bibliographic-integrity signal helpers and migration CLI. The migration is deliberately additive. It writes ``bibliographic_integrity_signals`` while preserving ever
- [ars/scripts/bootstrap_timeline_yaml.py](modules/academic-research-suite/ars/scripts/bootstrap_timeline_yaml.py) — v3.9.4 opt-in bootstrap script — populate timeline.yaml from literature_corpus[]. Walks the corpus and: 1. For each entry with `doi`: calls Crossref API to populate published_date.
- [ars/scripts/build_calibration_measurement_row.py](modules/academic-research-suite/ars/scripts/build_calibration_measurement_row.py) — Build the `heldout-measurement/1.1` row for a reviewer-calibration run (#653). The scorer (`score_calibration_run.py`) produces the mechanical metrics; the dispatcher's `manifest` 
- [ars/scripts/build_claim_standing_candidate_ledger.py](modules/academic-research-suite/ars/scripts/build_claim_standing_candidate_ledger.py) — Build or replay-validate the offline #655 Track A candidate ledger. The runtime consumes only explicitly named local JSON files containing a frozen query plan and already-returned 
- [ars/scripts/build_claim_standing_query_plan.py](modules/academic-research-suite/ars/scripts/build_claim_standing_query_plan.py) — Consent-surface builder for the #655 claim-standing probe (design §3.1/§3.2). Turns one Phase E Claim Registry row plus explicit researcher decisions into a schema-valid `claim-sta
- [ars/scripts/build_content_coverage_advisory.py](modules/academic-research-suite/ars/scripts/build_content_coverage_advisory.py) — Finalize, replay-validate, and render the bounded #681 LLM advisory. The runtime consumes evaluator judgments only as explicit input. It performs no model call, prose classificatio
- [ars/scripts/build_cross_document_consistency_advisory.py](modules/academic-research-suite/ars/scripts/build_cross_document_consistency_advisory.py) — Build, replay-validate, and render the hermetic #672 advisory. The semantic observations are explicit untrusted inputs. This module performs only closed-contract validation, exact-
- [ars/scripts/build_review_pathway_rule_trace.py](modules/academic-research-suite/ars/scripts/build_review_pathway_rule_trace.py) — Build, replay-validate, and render a deterministic #669 pathway rule trace. The runtime opens only caller-named JSON artifacts. It never chooses or ranks a pathway, determines appr
- [ars/scripts/build_submission_packet_manifest.py](modules/academic-research-suite/ars/scripts/build_submission_packet_manifest.py) — Build a deterministic, pointer-only human-subjects packet manifest. This checker observes only explicitly inventoried regular files. It does not scan a packet, interpret document p
- [ars/scripts/check_215_field_norm.py](modules/academic-research-suite/ars/scripts/check_215_field_norm.py) — Static lint for #215 field-norm severity coverage across the three reviewer surfaces. Issue: #215 (field-norm severity calibration, Kim et al. 2026 arXiv:2605.20668v1 W1/§F.3.4). E
- [ars/scripts/check_216_surface_form.py](modules/academic-research-suite/ars/scripts/check_216_surface_form.py) — Static lint for the #216 Surface-Form Parity self-check on the Devil's Advocate surface. Issue: #216 (reviewer-type / surface-form asymmetry, Kim et al. 2026 arXiv:2605.20668v1 §F.
- [ars/scripts/check_268_nested_commitment_ledger.py](modules/academic-research-suite/ars/scripts/check_268_nested_commitment_ledger.py) — #268 nested-object Commitment Ledger lint. Enforces the structural invariants of the Schema 11 Commitment Ledger after the parallel-list -> nested-object refactor (#268). Runs alon
- [ars/scripts/check_390_revision_patch_discipline.py](modules/academic-research-suite/ars/scripts/check_390_revision_patch_discipline.py) — #390 Slice B revision-mode patch-adoption lint (#424). Block-scoped string checks per repo convention (check_394 pattern) on the prompt surfaces that carry the patch protocol, plus
- [ars/scripts/check_392_citation_verification_intake.py](modules/academic-research-suite/ars/scripts/check_392_citation_verification_intake.py) — #392 lint — citation-verification intake question stays wired and byte-equivalent. Step 13 of the intake interview surfaces the `terminal_policies.citation_existence` choice (mark 
- [ars/scripts/check_394_submission_policy.py](modules/academic-research-suite/ars/scripts/check_394_submission_policy.py) — #394 slice-4 submission-package terminality lint. Runs alongside the other policy lints (check_v3_10_policy.py pattern). Verifies the slice-4 contract across the terminal-policies 
- [ars/scripts/check_439_format_profile.py](modules/academic-research-suite/ars/scripts/check_439_format_profile.py) — #439 format_profile contract lint (spec docs/design/2026-06-15-439-format-profile-design.md). Guards the scholar-declared layout profile schema (Slice A). The schema is a RENDERER 
- [ars/scripts/check_619_disclosure_closeout.py](modules/academic-research-suite/ars/scripts/check_619_disclosure_closeout.py) — Fail-closed focused guard for issue #619 disclosure closeout surfaces.
- [ars/scripts/check_630_codex_subscription_transport.py](modules/academic-research-suite/ars/scripts/check_630_codex_subscription_transport.py) — Static integration guard for the contained #630 citation transport.
- [ars/scripts/check_669_review_pathway_rule_trace.py](modules/academic-research-suite/ars/scripts/check_669_review_pathway_rule_trace.py) — Check the static #669 schemas, runtime, lint surface, and consumer wiring.
- [ars/scripts/check_670_revision_roadmap_integration.py](modules/academic-research-suite/ars/scripts/check_670_revision_roadmap_integration.py) — Static integration guard for the #670 non-ranking revision contract. The executable runtimes own artifact replay. This guard pins the pieces that could otherwise drift independentl
- [ars/scripts/check_673_adjudication_activity.py](modules/academic-research-suite/ars/scripts/check_673_adjudication_activity.py) — Deterministic static integration guard for #673 adjudication activity. This checker deliberately does not execute the recorder. It pins the closed schemas, exact renderer language,
- [ars/scripts/check_684_review_criteria_binding.py](modules/academic-research-suite/ars/scripts/check_684_review_criteria_binding.py) — Static integration guard for #684 review-criteria consumer binding.
- [ars/scripts/check_acronyms.py](modules/academic-research-suite/ars/scripts/check_acronyms.py) — Deterministic acronym check for a manuscript (#849). Reads one Markdown or plain-text file and never changes it. No model call. It checks three rules in each scope (the body, the E
- [ars/scripts/check_agents_mirror_sync.py](modules/academic-research-suite/ars/scripts/check_agents_mirror_sync.py) — Lint: plugin-root agents/ mirrors stay byte-identical REAL files (#413). agents/ held relative symlinks into deep-research/agents/ from v3.7.0 Phase 2.1 until #413: on Windows chec
- [ars/scripts/check_audit_artifact_consistency.py](modules/academic-research-suite/ars/scripts/check_audit_artifact_consistency.py) — check_audit_artifact_consistency.py — ARS v3.6.7 Step 6 Phase 6.3 lint. Implements every row of spec §3.7 invariant families A-F (cross-artifact contract for the audit-artifact lif
- [ars/scripts/check_benchmark_report.py](modules/academic-research-suite/ars/scripts/check_benchmark_report.py) — Validate an ARS benchmark report against benchmark_report.schema.json. Usage: python scripts/check_benchmark_report.py path/to/report.json Exit 0 on pass (warnings may still be pri
- [ars/scripts/check_bibliographic_integrity_signals.py](modules/academic-research-suite/ars/scripts/check_bibliographic_integrity_signals.py) — Drift guard for the #678 bibliographic-integrity signal contract.
- [ars/scripts/check_calibration_tiers.py](modules/academic-research-suite/ars/scripts/check_calibration_tiers.py) — Static contract for bounded reviewer calibration tiers.
- [ars/scripts/check_changelog_covers_merges.py](modules/academic-research-suite/ars/scripts/check_changelog_covers_merges.py) — Pre-tag lint: every release-worthy commit since the previous release tag must be referenced in CHANGELOG.md ABOVE the previous release's own section (the pre-tag coverage window: [
- [ars/scripts/check_ci_pytest_manifest.py](modules/academic-research-suite/ars/scripts/check_ci_pytest_manifest.py) — Drift guard for the unified pytest invocation manifest (issue #156). Validates `scripts/_ci_pytest_manifest.toml` and the surrounding workflow: 1. every manifest entry's `path` exi
- [ars/scripts/check_claim_audit_consistency.py](modules/academic-research-suite/ars/scripts/check_claim_audit_consistency.py) — check_claim_audit_consistency.py — ARS v3.8 claim-faithfulness audit lint. Enforces the 39 cross-field invariants spanning the six aggregates that claim_ref_alignment_audit_agent p
- [ars/scripts/check_claim_standing_candidate_ledger_integration.py](modules/academic-research-suite/ars/scripts/check_claim_standing_candidate_ledger_integration.py) — Static, hermetic integration guard for #655 Track A.
- [ars/scripts/check_claim_standing_freshness.py](modules/academic-research-suite/ars/scripts/check_claim_standing_freshness.py) — §7 freshness checker for the #655 claim-standing probe (gate 13). The probe identity binds the exact claim text, consent receipt, query plan, adapter registry, candidate ledger, an
- [ars/scripts/check_claim_standing_transmissions.py](modules/academic-research-suite/ars/scripts/check_claim_standing_transmissions.py) — Transmission-ledger builder/validator for the #655 claim-standing probe. Implements the design §6 transmission accounting and the §9 gate-14 check: every authorized transmission at
- [ars/scripts/check_collaboration_depth_rubric.py](modules/academic-research-suite/ars/scripts/check_collaboration_depth_rubric.py) — Validate the Collaboration Depth Observer artifacts (ARS v3.5). Usage: python scripts/check_collaboration_depth_rubric.py [--path REPO_ROOT] Exit codes: 0 all checks pass; 1 at lea
- [ars/scripts/check_command_frontmatter_name.py](modules/academic-research-suite/ars/scripts/check_command_frontmatter_name.py) — CI lint: every commands/*.md declares an explicit frontmatter `name` equal to its filename stem (#633). Since Claude Code v2.1.216, a plugin command's frontmatter `name` keeps the 
- [ars/scripts/check_command_skill_dispatch.py](modules/academic-research-suite/ars/scripts/check_command_skill_dispatch.py) — Check plugin command entry points and rooted skill references (#857). This is a static packaging check, not evidence of model invocation. Runtime acceptance also inspects Skill cal
- [ars/scripts/check_committee_correspondence.py](modules/academic-research-suite/ars/scripts/check_committee_correspondence.py) — Validate a #668 committee-correspondence bundle. This checker proves byte transport, source-comment accounting, degraded/profile semantics, and response-skeleton coverage. It does 
- [ars/scripts/check_compliance_report.py](modules/academic-research-suite/ars/scripts/check_compliance_report.py) — Validate an ARS compliance report against compliance_report.schema.json. Usage: python scripts/check_compliance_report.py path/to/report.json Exit 0 on pass (warnings may still be 
- [ars/scripts/check_content_coverage_advisory_integration.py](modules/academic-research-suite/ars/scripts/check_content_coverage_advisory_integration.py) — Check the static #681 advisory boundary and cross-file wiring. The executable runtimes own row/report replay. This guard pins the pieces that can otherwise drift independently: the
- [ars/scripts/check_control_availability.py](modules/academic-research-suite/ars/scripts/check_control_availability.py) — Defrift lint for docs/CONTROL_AVAILABILITY.md (#757). The control-availability matrix is a hand-maintained claim-adjudication surface: users consult it to decide whether an integri
- [ars/scripts/check_corpus_consumer_protocol.py](modules/academic-research-suite/ars/scripts/check_corpus_consumer_protocol.py) — Lint corpus consumer protocol per spec §5.2 (v3.6.5). Enforces nine invariants L1–L9. Manifest-driven for L3–L6. Exit 0 on pass, exit 1 on fail. Prints aggregated failure list.
- [ars/scripts/check_cross_document_consistency_advisory_integration.py](modules/academic-research-suite/ars/scripts/check_cross_document_consistency_advisory_integration.py) — Check the hermetic #672 cross-document advisory integration boundary. Behavioral tests own byte replay and finalization semantics. This guard keeps the independently editable surfa
- [ars/scripts/check_cross_model_handoff_contract.py](modules/academic-research-suite/ars/scripts/check_cross_model_handoff_contract.py) — Defrift lock for the #527 cross-model handoff contract. #523 moved the blind-checkpoint transport to the dispatching layer, but left the owner → dispatcher → owner path enforced by
- [ars/scripts/check_cross_model_verification_sync.py](modules/academic-research-suite/ars/scripts/check_cross_model_verification_sync.py) — Doc-sync lint for the cross-model grounding guards (#346 / #349). The contract-bearing jq for the cross-model verifier lives in canonical files under `scripts/cross_model_verificat
- [ars/scripts/check_data_access_level.py](modules/academic-research-suite/ars/scripts/check_data_access_level.py) — Lint: every top-level SKILL.md declares the PINNED data_access_level. Single pass per skill, one violation per problem: frontmatter must parse, the skill must be registered in EXPE
- [ars/scripts/check_data_flows.py](modules/academic-research-suite/ars/scripts/check_data_flows.py) — Defrift lint for docs/DATA_FLOWS.md (#758). The data-flow map claims to be the exhaustive user-facing inventory of the network touchpoints and local stores the suite's own scripts 
- [ars/scripts/check_decision_contract.py](modules/academic-research-suite/ars/scripts/check_decision_contract.py) — Pin the four-value decision enum and its per-mode authority. Threat model: accidental drift. Historical records and design documents are excluded deliberately; they may truthfully 
- [ars/scripts/check_degradation_registry.py](modules/academic-research-suite/ars/scripts/check_degradation_registry.py) — Degradation-registry lint (#511 Part A). Pins shared/contracts/degradation_registry.json — the machine-readable INDEX of ARS's graceful-degradation mechanisms — to the repo state i
- [ars/scripts/check_distribution_surface_claims.py](modules/academic-research-suite/ars/scripts/check_distribution_surface_claims.py) — Distribution-surface claim discipline lint (#753). The #745 capability matrix pins README claim anchors, and version-consistency invariant 8 binds the plugin.json agent-count numbe
- [ars/scripts/check_domain_evidence_profile.py](modules/academic-research-suite/ars/scripts/check_domain_evidence_profile.py) — Lint domain evidence profile documentation surface (#259). Seven documentation-surface checks C1-C7. Honest about reach: verifies presence/ shape of required text, NOT runtime sema
- [ars/scripts/check_e4_promotion.py](modules/academic-research-suite/ars/scripts/check_e4_promotion.py) — Verify that an E4 record and raw bundle were promoted byte-for-byte. This checker validates only the copy boundary. It never reinterprets model output, checker verdicts, adjudicati
- [ars/scripts/check_evals_gold_set.py](modules/academic-research-suite/ars/scripts/check_evals_gold_set.py) — Validator for evals/gold/<task>/ gold subsets. Enforces 9 invariants documented in docs/design/2026-05-21-v3.10-184-extend-eval-harness-spec.md implementation plan (Task 4 of #184 
- [ars/scripts/check_evidence_row_integration.py](modules/academic-research-suite/ars/scripts/check_evidence_row_integration.py) — Static integration guard for the #656 shared evidence-row contract. The executable runtime owns dynamic row validation and rendering. This guard owns the cross-file pointers and no
- [ars/scripts/check_experiment_provenance.py](modules/academic-research-suite/ars/scripts/check_experiment_provenance.py) — Validate a Material Passport YAML's `experiment_provenance[]` entry SHAPE (#260). Usage: python scripts/check_experiment_provenance.py path/to/passport.yaml Standalone shape-only v
- [ars/scripts/check_field_norm_severity.py](modules/academic-research-suite/ars/scripts/check_field_norm_severity.py) — Integrity + provenance validator for the #215 field-norm severity gold set. This gold set is a first-party REGRESSION FIXTURE, not a detector calibration set. There is no determini
- [ars/scripts/check_firm_rules_sync.py](modules/academic-research-suite/ars/scripts/check_firm_rules_sync.py) — Firm-rules sync + collision lint (v3.10 PR-A). Pins two things against regression: 1. **Sync** (R-CIM-* only): the canonical R-CIM-* (claim-manifest) firm-rule wording in `shared/r
- [ars/scripts/check_heldout_measurement_report.py](modules/academic-research-suite/ars/scripts/check_heldout_measurement_report.py) — Validate ARS held-out measurement reports against the #654/#664 contract. Layers: 1. JSON Schema (evals/heldout/measurement_report.schema.json) — shape, enums, const attestations (
- [ars/scripts/check_human_subjects_output_contract.py](modules/academic-research-suite/ars/scripts/check_human_subjects_output_contract.py) — Lint the #665 human-subjects readiness/authorization output boundary. This is a prompt/reference contract lint, not an authorization engine. It pins the load-bearing output grammar
- [ars/scripts/check_human_subjects_reference_migration.py](modules/academic-research-suite/ars/scripts/check_human_subjects_reference_migration.py) — Lint the bounded #680 human-subjects reference migration. This checker reads only the named migration references/consumers and the local #666 registry. It is a hermetic prose/regis
- [ars/scripts/check_indirect_prompt_injection_no_call.py](modules/academic-research-suite/ars/scripts/check_indirect_prompt_injection_no_call.py) — AST guard for the #675 offline-only Phase-2 envelope.
- [ars/scripts/check_instruction_data_boundary.py](modules/academic-research-suite/ars/scripts/check_instruction_data_boundary.py) — Instruction-vs-data boundary lint (#272 guidance layer). Guards the "retrieved external content is data, not instructions" standing principle against silent removal or gutting. Thi
- [ars/scripts/check_judge_prompt_version.py](modules/academic-research-suite/ars/scripts/check_judge_prompt_version.py) — Judge-prompt-version drift guard (#361). The judge cache key includes a `prompt_version` component so a judge-prompt revision invalidates stale cache entries automatically (issue #
- [ars/scripts/check_literature_corpus_schema.py](modules/academic-research-suite/ars/scripts/check_literature_corpus_schema.py) — Validate literature_corpus_entry.schema.json and rejection_log.schema.json self-consistency, and validate adapter example output against them. Usage: python scripts/check_literatur
- [ars/scripts/check_method_weaknesses_sync.py](modules/academic-research-suite/ars/scripts/check_method_weaknesses_sync.py) — Per-source method-weaknesses sync lint (#916). `shared/references/per_source_method_weaknesses.md` holds the canonical method-weakness rules for reading outputs and lists the surfa
- [ars/scripts/check_model_tiering.py](modules/academic-research-suite/ars/scripts/check_model_tiering.py) — Model-tiering classification drift guard (#517). The tiering mechanism (shared/model_tiering.md) is prose + manifest: agent files are never edited, so the only thing that can rot i
- [ars/scripts/check_panel_synthesis.py](modules/academic-research-suite/ars/scripts/check_panel_synthesis.py) — Validate Schema 13.2 reviewer cards and recompute panel synthesis. Schema 13.2 removes per-seat failure-condition decisions. This checker parses role-scoped dimension scores, evalu
- [ars/scripts/check_passport_reset_contract.py](modules/academic-research-suite/ars/scripts/check_passport_reset_contract.py) — Enforce the ARS v3.6.3 passport-reset-boundary co-location contract. Contract: any text file that mentions the env-flag token `ARS_PASSPORT_RESET` MUST also contain a reference to 
- [ars/scripts/check_pattern_eval_manifest.py](modules/academic-research-suite/ars/scripts/check_pattern_eval_manifest.py) — Validate ARS v3.6.7 Step 8 pattern-eval fixture manifests. Spec: docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md §7.2 (micro-fixture schema) + §7.3 (integration
- [ars/scripts/check_persuasion_invariance_fixtures.py](modules/academic-research-suite/ars/scripts/check_persuasion_invariance_fixtures.py) — Integrity lint for evals/heldout/re_review_persuasion_invariance/ (#576 Spec B §14). Structure-only fixture gate (the #574 E4 `check_seeded_defect_fixtures.py` precedent): it valid
- [ars/scripts/check_phase_conformance.py](modules/academic-research-suite/ars/scripts/check_phase_conformance.py) — Fail-closed Phase 1 -> Phase 2 conformance checker for reviewer Schema 13.2. Usage: python scripts/check_phase_conformance.py --contract C.json --role eic --phase1 eic.phase1.md --
- [ars/scripts/check_pipeline_boundary_semantics.py](modules/academic-research-suite/ars/scripts/check_pipeline_boundary_semantics.py) — Defrift lock for the four #528 pipeline-boundary resolutions. The 2026-07 Mode-A structural replay (#528) surfaced four inconsistencies / under-specified boundaries across the acad
- [ars/scripts/check_pipeline_integrity.py](modules/academic-research-suite/ars/scripts/check_pipeline_integrity.py) — Advisory verifier for ARS pipeline phase scope (v3.9.2). Spec: docs/design/2026-05-18-ars-v3.9.2-phase-boundary-spec.md Phase 4 Issue: #133 (phase scope inflation hot-fix) Forward 
- [ars/scripts/check_policy_anchor_protocol.py](modules/academic-research-suite/ars/scripts/check_policy_anchor_protocol.py) — #108 policy_anchor_disclosure_protocol.md static lint. Decision Doc reference: docs/design/2026-05-14-ai-disclosure-schema-decision.md §4.1 (item 6) + §4.3 invariants + §4.4 11 ope
- [ars/scripts/check_policy_anchor_table.py](modules/academic-research-suite/ars/scripts/check_policy_anchor_table.py) — #108 policy_anchor_table.md static lint. Decision Doc reference: docs/design/2026-05-14-ai-disclosure-schema-decision.md §4.1 (item 6a) + §4.3 invariants. Implementation spec refer
- [ars/scripts/check_preprint_venues_consistency.py](modules/academic-research-suite/ars/scripts/check_preprint_venues_consistency.py) — #105 lint — PREPRINT_VENUES 10-server list must agree across files. v3.7.3 spec §3.2 Vector 1 fixes the closed list at 10 preprint servers (gemini review F6 / codex F13 expansion f
- [ars/scripts/check_prisma_trAIce_freshness.py](modules/academic-research-suite/ars/scripts/check_prisma_trAIce_freshness.py) — Warn when shared/prisma_trAIce_protocol.md is older than 180 days. Non-blocking: exit 0 even on stale, but print warning to stderr. Exit 1 only on parse error (missing or malformed
- [ars/scripts/check_promotion_bakeoff_preregistration.py](modules/academic-research-suite/ars/scripts/check_promotion_bakeoff_preregistration.py) — Create and verify sealed Promotion Bakeoff preregistrations (#789). The public pre-fleet artifact is a closed commitment containing only a probe fixture digest and the fixed 30-row
- [ars/scripts/check_ranking_lift.py](modules/academic-research-suite/ars/scripts/check_ranking_lift.py) — Ranking-method lift gate (#184 Delta 4 / E-V4). Reads a baseline and a compare ``run_evals`` report (single-run shape, with ``per_task[].aggregate_metric`` + ``per_class``) and com
- [ars/scripts/check_re_review_synthesis.py](modules/academic-research-suite/ars/scripts/check_re_review_synthesis.py) — Recompute the #576 Spec B three-gate re-review contract from its artifacts. Stdlib-only, same architecture class as ``check_panel_synthesis.py`` (#510: recompute every layer from t
- [ars/scripts/check_receipt_enum_sync.py](modules/academic-research-suite/ars/scripts/check_receipt_enum_sync.py) — Defrift lint for the #610 arithmetic-receipt closed enums. The receipt grammar spells its four closed enums in three places: the `methodology-receipt` canonical prompt fragment (wh
- [ars/scripts/check_repro_lock.py](modules/academic-research-suite/ars/scripts/check_repro_lock.py) — Validate a Material Passport YAML's `repro_lock` sub-block. Usage: python scripts/check_repro_lock.py path/to/passport.yaml - Missing `repro_lock` key (not even null): ERROR, exit 
- [ars/scripts/check_review_form_note_sync.py](modules/academic-research-suite/ars/scripts/check_review_form_note_sync.py) — Review-form note sync lint (#921). `shared/references/review_form_note.md` holds the canonical review-form note: the rules for when ARS reminds the author that a literature review 
- [ars/scripts/check_review_pathway_output.py](modules/academic-research-suite/ars/scripts/check_review_pathway_output.py) — Lint only explicitly named #669 generated output surfaces. The checker never scans a directory or repository. A pathway term is allowed only in the exact candidate-name JSON field 
- [ars/scripts/check_reviewer_data_fences.py](modules/academic-research-suite/ars/scripts/check_reviewer_data_fences.py) — Reviewer data-fence lint (#574 A6 / PR #578 follow-up, shipped with the behavior batch). Pins the `<paper_content>` + `<phase1_output>` data-fence contract across every surface PR 
- [ars/scripts/check_reviewer_finding_contract.py](modules/academic-research-suite/ars/scripts/check_reviewer_finding_contract.py) — Reviewer finding-contract lint (#574 behavior batch: A1/A2/A3/B1). Pins the behavior batch's prompt surfaces so the drift classes it retired cannot silently return: - A1 — finding 
- [ars/scripts/check_reviewer_role_label.py](modules/academic-research-suite/ars/scripts/check_reviewer_role_label.py) — Pin #611's public Journal-Fit Reviewer name and frozen eic/EIC tokens.
- [ars/scripts/check_reviewer_scoring_honesty.py](modules/academic-research-suite/ars/scripts/check_reviewer_scoring_honesty.py) — Guard criterion-bound reviewer judgement and calibration honesty. This lint protects current runtime/documentation surfaces. Historical design records and unrelated scoring systems
- [ars/scripts/check_reviewer_sprint_prompt_sync.py](modules/academic-research-suite/ars/scripts/check_reviewer_sprint_prompt_sync.py) — Exact sync lint for the #611 reviewer sprint-prompt canonical source. The dispatcher sends each reviewer's Phase 1/Phase 2 H3 body verbatim. A file pointer cannot replace those byt
- [ars/scripts/check_revision_claim_drift_suite_v2.py](modules/academic-research-suite/ars/scripts/check_revision_claim_drift_suite_v2.py) — Hermetic contract guard for revision_claim_drift suite v2 (#679). This checker never invokes a model, judge, adjudicator, network API, or eval runner. It validates repository-owned
- [ars/scripts/check_revision_token_conservation.py](modules/academic-research-suite/ars/scripts/check_revision_token_conservation.py) — Deterministic token-conservation audit between revision rounds (#570). Compares the multisets of numeric tokens, citation tokens (`<!--ref:-->` / `<!--anchor:-->` markers, brackete
- [ars/scripts/check_risk_register.py](modules/academic-research-suite/ars/scripts/check_risk_register.py) — Defrift lint for docs/RISK_REGISTER.md (#759). The risk register is a hand-maintained index linking each standing risk to its existing controls, its evidence status, and its residu
- [ars/scripts/check_role_scoped_contract.py](modules/academic-research-suite/ars/scripts/check_role_scoped_contract.py) — Pin Schema 13.2 role-scoped reviewer delivery surfaces. Threat model: accidental well-intentioned drift. Adversarial repository editors are out of scope because they can edit this 
- [ars/scripts/check_routing_core_sync.py](modules/academic-research-suite/ars/scripts/check_routing_core_sync.py) — Routing-core sync lint (#892). `shared/references/routing_core.md` holds the cross-skill routing core and says which files carry it and why. This lint keeps the verbatim copies in 
- [ars/scripts/check_rq_framing_patterns.py](modules/academic-research-suite/ars/scripts/check_rq_framing_patterns.py) — Calibration checker for the #257 Socratic wording-pattern advisory. The detector is intentionally lexical and conservative. It is not a novelty model and does not judge research qu
- [ars/scripts/check_rubric_weight_consistency.py](modules/academic-research-suite/ars/scripts/check_rubric_weight_consistency.py) — Compatibility entrypoint for the retired rubric-weight lint. Reviewer weights and aggregate scores no longer exist. Keep this filename so older CI invocations fail closed through t
- [ars/scripts/check_seeded_defect_fixtures.py](modules/academic-research-suite/ars/scripts/check_seeded_defect_fixtures.py) — Integrity lint for evals/heldout/reviewer_seeded_defects/ (#574/#610 v0.2). Structure-only fixture gate (the field_norm_severity precedent): it validates that the ground-truth mani
- [ars/scripts/check_setup_cross_model_parity.py](modules/academic-research-suite/ars/scripts/check_setup_cross_model_parity.py) — SETUP cross-model example parity lint (#491 fold-in). The quick-setup bash blocks in docs/SETUP.md + docs/SETUP.zh-TW.md hardcode verifier model IDs (`ARS_CROSS_MODEL="..."`) becau
- [ars/scripts/check_skill_description_length.py](modules/academic-research-suite/ars/scripts/check_skill_description_length.py) — Enforce the Agent Skills description limit on parsed Unicode text (#864). Count Python len(description), not source bytes, and never trim or normalize before counting. Preserve the
- [ars/scripts/check_skill_inventory_parity.py](modules/academic-research-suite/ars/scripts/check_skill_inventory_parity.py) — Lint: the skill inventory is identical on every surface that lists it (#809). Triage of an external PR that added a fifth top-level skill directory showed that the existing invento
- [ars/scripts/check_spec_consistency.py](modules/academic-research-suite/ars/scripts/check_spec_consistency.py) — if __package__:  # Package import in tests.
- [ars/scripts/check_sprint_contract.py](modules/academic-research-suite/ars/scripts/check_sprint_contract.py) — Validate an ARS sprint contract against sprint_contract.schema.json. Usage: python scripts/check_sprint_contract.py path/to/contract.json [--ars-version vX.Y.Z] Exit 0 on pass (war
- [ars/scripts/check_stage_capability_matrix.py](modules/academic-research-suite/ars/scripts/check_stage_capability_matrix.py) — Stage capability/evidence matrix lint + renderer (#745). Pins shared/contracts/capability/stage_capability_matrix.json — the single machine-readable source for what each pipeline s
- [ars/scripts/check_submission_packet_manifest_integration.py](modules/academic-research-suite/ars/scripts/check_submission_packet_manifest_integration.py) — Check the static #667 submission-packet contract and consumer wiring.
- [ars/scripts/check_surface_form_parity.py](modules/academic-research-suite/ars/scripts/check_surface_form_parity.py) — Integrity + provenance validator for the #216 surface-form parity gold set. Issue: #216 (reviewer-type / surface-form asymmetry, Kim et al. 2026 arXiv:2605.20668v1 §F.3.6). This go
- [ars/scripts/check_task_type.py](modules/academic-research-suite/ars/scripts/check_task_type.py) — Lint: every top-level SKILL.md must declare metadata.task_type. Legal values: open-ended | outcome-gradable.
- [ars/scripts/check_tools_allowlist.py](modules/academic-research-suite/ars/scripts/check_tools_allowlist.py) — Lint: pin the #514 tools-allowlist CONTENT on the three plugin agents (#524). #521 shipped `tools: Read, Write, Edit, Grep, Glob` on the three top-level plugin agents (deep-researc
- [ars/scripts/check_tortured_phrase_screening_integration.py](modules/academic-research-suite/ars/scripts/check_tortured_phrase_screening_integration.py) — Check the hermetic #660 tortured-phrase screening integration boundary. The matcher tests own behavioral replay. This static guard prevents the four contract layers from drifting i
- [ars/scripts/check_v3_10_134_write_scope.py](modules/academic-research-suite/ars/scripts/check_v3_10_134_write_scope.py) — Static lint for the ARS #134 Slice 1 write-scope guard — three-way name cross-check. Spec: docs/design/2026-06-01-ars-134-conductor-rescope-deterministic-write-guard-spec.md (§3.4)
- [ars/scripts/check_v3_10_policy.py](modules/academic-research-suite/ars/scripts/check_v3_10_policy.py) — v3.10 policy-layer lint (#127 PR-B). Runs ALONGSIDE check_v3_9_0_triangulation.py (NOT a rename — per spec §3 PR-B item 14 / checkpoint open decision resolved to "alongside"). Veri
- [ars/scripts/check_v3_6_6_ab_manifest.py](modules/academic-research-suite/ars/scripts/check_v3_6_6_ab_manifest.py) — Enforce the v3.6.6 A/B evidence fixture manifest contract per §6.2 schema + §6.5 git-tracked invariants per design doc 2026-04-27-ars-v3.6.6-generator-evaluator-contract-design.md.
- [ars/scripts/check_v3_6_7_pattern_protection.py](modules/academic-research-suite/ars/scripts/check_v3_6_7_pattern_protection.py) — Static audit for ARS v3.6.7 downstream-agent pattern protection. Spec: docs/design/2026-04-29-ars-v3.6.7-downstream-agent-pattern-protection-spec.md Greps the v3.6.7 reference file
- [ars/scripts/check_v3_6_8_audit_scope_block.py](modules/academic-research-suite/ars/scripts/check_v3_6_8_audit_scope_block.py) — ARS v3.7.1 Step 2 — D2 audit Scope Report block lint. Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md §3.2 (D2 — Audit scope coverage non-di
- [ars/scripts/check_v3_6_8_cite_provenance_pipeline.py](modules/academic-research-suite/ars/scripts/check_v3_6_8_cite_provenance_pipeline.py) — ARS v3.7.1 Step 3b — Cite-Time Provenance Finalizer (academic-pipeline mode). Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md § Step 3b — Pi
- [ars/scripts/check_v3_6_8_frontmatter_trust_schema.py](modules/academic-research-suite/ars/scripts/check_v3_6_8_frontmatter_trust_schema.py) — ARS v3.7.1 trust-chain frontmatter lint (spec § 3.1 firm rules). Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md § 3.1 D1 — Frontmatter trus
- [ars/scripts/check_v3_6_8_mark_read_commands.py](modules/academic-research-suite/ars/scripts/check_v3_6_8_mark_read_commands.py) — CI lint for the /ars-mark-read + /ars-unmark-read plugin commands. Per v3.6.8 spec §3.6 + Step 7 (round-2 R2-002 amend) acceptance criteria: the 2 commands must exist, carry the va
- [ars/scripts/check_v3_6_8_pattern_protection.py](modules/academic-research-suite/ars/scripts/check_v3_6_8_pattern_protection.py) — ARS v3.7.1 byte-equivalence SHA gate + Step 3a Two-Layer Citation Emission invariants. Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md § Ste
- [ars/scripts/check_v3_7_3_three_layer_citation.py](modules/academic-research-suite/ars/scripts/check_v3_7_3_three_layer_citation.py) — v3.7.3 Three-Layer Citation lint. External motivation: Zhao et al. arXiv:2605.07723 (2026-05) — corpus-scale audit of LLM hallucinations finds the L3 claim-faithfulness gap unaddre
- [ars/scripts/check_v3_8_annotation_literal_sync.py](modules/academic-research-suite/ars/scripts/check_v3_8_annotation_literal_sync.py) — ARS v3.8 §3.6 + §5 — annotation literal sync lint. The 8-row finalizer matrix in `scripts/claim_audit_finalizer.py` emits five HIGH-WARN annotation classes that the formatter's ter
- [ars/scripts/check_v3_9_0_triangulation.py](modules/academic-research-suite/ars/scripts/check_v3_9_0_triangulation.py) — Cross-version contamination-suffix lint: finalizer suffix table contract + formatter allowlist + refusal-list guard. NOTE ON NAMING: this file is named for v3.9.0 (where the triang
- [ars/scripts/check_v3_9_2_phase_boundary.py](modules/academic-research-suite/ars/scripts/check_v3_9_2_phase_boundary.py) — Static lint for ARS v3.9.2 phase boundary coverage (#133 hot-fix). Spec: docs/design/2026-05-18-ars-v3.9.2-phase-boundary-spec.md Phase 5 Classification: docs/design/2026-05-18-ars
- [ars/scripts/check_v3_9_4_temporal_verification.py](modules/academic-research-suite/ars/scripts/check_v3_9_4_temporal_verification.py) — v3.9.4 spec lint — temporal verification sidecar conformance. Enforces 8 invariants from spec §7: 1. timeline.yaml schema conformance against timeline.schema.json 2. supersession c
- [ars/scripts/check_venue_disclosure_policies.py](modules/academic-research-suite/ars/scripts/check_venue_disclosure_policies.py) — Structural guard for the 15-entry venue disclosure policy database.
- [ars/scripts/check_version_consistency.py](modules/academic-research-suite/ars/scripts/check_version_consistency.py) — Lint: version labels stay aligned across .claude/CLAUDE.md, SKILL.md frontmatter, and CHANGELOG.md. Invariants enforced: 1. Every skill listed in .claude/CLAUDE.md Skills Overview 
- [ars/scripts/check_workflow_classification.py](modules/academic-research-suite/ars/scripts/check_workflow_classification.py) — Defrift lint for the CI workflow classification table (#755). docs/ARCHITECTURE.md §7.1 claims to classify EVERY workflow's enforcement strength — a completeness claim that silentl
- [ars/scripts/chinese_literature_client.py](modules/academic-research-suite/ars/scripts/chinese_literature_client.py) — Chinese-language literature resolver client. Implements the lookup contract documented at `deep-research/references/chinese_literature_api_protocol.md`. WHY THIS EXISTS (#595): `ap
- [ars/scripts/citation_verification_summary.py](modules/academic-research-suite/ars/scripts/citation_verification_summary.py) — Citation verification summary reducer (Delta 4) — SINGLE SOURCE OF TRUTH. Reduces per-resolver outcomes to the 3-class `lookup_verified` value using the v3.11 narrowed-false defini
- [ars/scripts/claim_audit_calibration.py](modules/academic-research-suite/ars/scripts/claim_audit_calibration.py) — Calibration runner for v3.8 claim_ref_alignment_audit_agent. This module is the operational entrypoint that the agent prompt at `academic-pipeline/agents/claim_ref_alignment_audit_
- [ars/scripts/claim_audit_finalizer.py](modules/academic-research-suite/ars/scripts/claim_audit_finalizer.py) — ARS v3.8 claim-faithfulness finalizer — 8-row matrix annotations + Stage 6 histogram. Implements the orchestrator `§3.6 Claim-Faithfulness Audit Gate (v3.8)` matrix table in `pipel
- [ars/scripts/claim_audit_pipeline.py](modules/academic-research-suite/ars/scripts/claim_audit_pipeline.py) — claim_audit_pipeline — Python implementation of the §4 Step 1-6 pipeline. This module is the executable face of `claim_ref_alignment_audit_agent.md`. The agent prompt narrates the 
- [ars/scripts/claim_registry_coverage.py](modules/academic-research-suite/ars/scripts/claim_registry_coverage.py) — Build and replay-validate a bounded E1 Claim Registry coverage report. The detector enumerates citation-bearing and quantitative sentence candidates, records their bounded lexical 
- [ars/scripts/claim_standing_discovery.py](modules/academic-research-suite/ars/scripts/claim_standing_discovery.py) — Live discovery adapters for the #655 claim-standing probe (Track A head). Turns a consent-bound `claim-standing-query-plan/1.0` into a `claim-standing-retrieval-input/1.0` record: 
- [ars/scripts/claim_standing_stance_runner.py](modules/academic-research-suite/ars/scripts/claim_standing_stance_runner.py) — Stance runner for the #655 claim-standing probe (Track B execution). Consumes a finalized candidate ledger under a `retrieval_plus_stance` query-plan-1.1 consent and produces one `
- [ars/scripts/claim_standing_stance_scorer.py](modules/academic-research-suite/ars/scripts/claim_standing_stance_scorer.py) — Mechanical stance scorer for the #655 claim-standing seed set. Compares one subject run's frozen enum outputs against adjudicated expert labels, without asking any model to reinter
- [ars/scripts/claim_strength_drift_disposition.py](modules/academic-research-suite/ars/scripts/claim_strength_drift_disposition.py) — Build and validate explicit author dispositions for detected E6 drift. The runtime is hermetic: it opens only explicitly named local artifacts, never calls a model or network servi
- [ars/scripts/contamination_signals.py](modules/academic-research-suite/ars/scripts/contamination_signals.py) — #105 v3.7.3 contamination_signals resolvers. Pure functions implementing v3.7.3 spec §3.2 Vector 1 + Vector 2 for use by the migration tool. bibliography_agent computes these at in
- [ars/scripts/cross_model_codex_transport.py](modules/academic-research-suite/ars/scripts/cross_model_codex_transport.py) — Contained ChatGPT-subscription transport for one citation verification (#630). The model receives one closed citation-data object, no caller-authored prompt. The runtime drives Cod
- [ars/scripts/cross_model_codex_verify.sh](modules/academic-research-suite/ars/scripts/cross_model_codex_verify.sh) — Bash 3.2-compatible entry point for the #630 citation-only transport.
- [ars/scripts/cross_model_handoff.py](modules/academic-research-suite/ars/scripts/cross_model_handoff.py) — Reference grammar + routing for the #527 cross-model handoff envelope. `shared/cross_model_verification.md` § Cross-model handoff envelope (#527) names this module as the NORMATIVE
- [ars/scripts/cross_model_smoke_test.sh](modules/academic-research-suite/ars/scripts/cross_model_smoke_test.sh) — Live smoke test for the OpenAI grounded cross-model verifier route.
- [ars/scripts/cross_model_smoke_test_codex.sh](modules/academic-research-suite/ars/scripts/cross_model_smoke_test_codex.sh) — Manual LIVE smoke test. CI must never invoke this file.
- [ars/scripts/cross_model_verification/normalize_compat_verdict.py](modules/academic-research-suite/ars/scripts/cross_model_verification/normalize_compat_verdict.py) — Normalize an OpenAI-compatible provider's citation-verification response to ONE status. Compatible providers (MiMo / DeepSeek / MiniMax / self-hosted) expose no hosted web-search t
- [ars/scripts/cross_model_verification/openai_effort_guard.sh](modules/academic-research-suite/ars/scripts/cross_model_verification/openai_effort_guard.sh) — Canonical per-model reasoning-effort vocabulary for the first-party OpenAI
- [ars/scripts/crossref_client.py](modules/academic-research-suite/ars/scripts/crossref_client.py) — Minimal Crossref API client wrapper. Implements the lookup contract documented at `deep-research/references/crossref_api_protocol.md`. DOI-first with title cross-check (DOI_MISMATC
- [ars/scripts/dispatch_calibration_panel.py](modules/academic-research-suite/ars/scripts/dispatch_calibration_panel.py) — Isolated dispatch of ONE reviewer-calibration panel (#653). The calibration protocol (`academic-paper-reviewer/references/calibration_mode_protocol.md`) reuses the pre-v3.6.2 singl
- [ars/scripts/dispatch_e4_panel.py](modules/academic-research-suite/ars/scripts/dispatch_e4_panel.py) — Dispatch one E4 seeded-defect panel with the evidence contract enforced. `reviewer-e4/2026-08-06` (superseding `reviewer-e4/2026-07-27` with the #610 step-5 methodology three-call 
- [ars/scripts/dispatch_panel_claim_audit.py](modules/academic-research-suite/ars/scripts/dispatch_panel_claim_audit.py) — Dispatch and score the panel-claim factuality audit (#1002). The suite lives in ``evals/heldout/panel_claim_factuality/``; its README gives the order of the steps and ``plan.json``
- [ars/scripts/evidence_rows.py](modules/academic-research-suite/ars/scripts/evidence_rows.py) — Build, validate, page, and inertly render ARS shared evidence rows. The module is deliberately standard-library-only and hermetic. Builders may inspect only the ``session_source_or
- [ars/scripts/extract_panel_claims.py](modules/academic-research-suite/ars/scripts/extract_panel_claims.py) — Extract the claims a review panel makes, for the factuality audit (#1002). Reads E4 raw panel bundles (``evals/heldout/reviewer_seeded_defects/runs/raw``) and never changes them. N
- [ars/scripts/fetch_calibration_corpus.py](modules/academic-research-suite/ars/scripts/fetch_calibration_corpus.py) — Authenticated OpenReview fetch for the #653 reviewer-calibration corpus. Operator tool (network, needs an OpenReview account; no CI path). Reads OPENREVIEW_USERNAME / OPENREVIEW_PA
- [ars/scripts/file_lock.py](modules/academic-research-suite/ars/scripts/file_lock.py) — Shared advisory file locking for ARS scripts (#845). One backend per host, chosen at import time and published as ``BACKEND``: * ``"fcntl"`` (POSIX): ``flock``. Shared and exclusiv
- [ars/scripts/human_read_attestation_resolver.py](modules/academic-research-suite/ars/scripts/human_read_attestation_resolver.py) — Deterministically resolve USER_ATTESTED_READ coverage for one citation. The ledger is a user declaration. This resolver never infers that reading or comprehension occurred; it only
- [ars/scripts/ideation_diversity_assignment_gate.py](modules/academic-research-suite/ars/scripts/ideation_diversity_assignment_gate.py) — Closed first-round assignment-ledger gate for the #659 blind bundle. The #659 no-call envelope freezes 48 arm-blind judge packets but explicitly does not implement the assignment-l
- [ars/scripts/inquiry_branch_ledger.py](modules/academic-research-suite/ars/scripts/inquiry_branch_ledger.py) — Validate, replay, and durably publish inquiry-branch-ledger/1.0 (#743). The ledger is an opt-in, event-sourced user-project artifact. This module is deliberately manuscript-blind a
- [ars/scripts/legacy/ars_apply_revision_patch_v1_0.py](modules/academic-research-suite/ars/scripts/legacy/ars_apply_revision_patch_v1_0.py) — Apply a revision patch to an anchored draft — two-phase, fail-closed. #89 Item 7 Slice A. Normative source: `docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md` §3.3 (dete
- [ars/scripts/legacy/check_re_review_synthesis_v1_0.py](modules/academic-research-suite/ars/scripts/legacy/check_re_review_synthesis_v1_0.py) — Recompute the #576 Spec B three-gate re-review contract from its artifacts. Stdlib-only, same architecture class as ``check_panel_synthesis.py`` (#510: recompute every layer from t
- [ars/scripts/migrate_literature_corpus_to_v3_10.py](modules/academic-research-suite/ars/scripts/migrate_literature_corpus_to_v3_10.py) — #127 v3.10 terminal-policy-layer seed migration tool. Seeds the passport-level `terminal_policies` block on v3.9.0-onward passports. This is a PURE LOCAL YAML transform — it needs 
- [ars/scripts/migrate_literature_corpus_to_v3_7_3.py](modules/academic-research-suite/ars/scripts/migrate_literature_corpus_to_v3_7_3.py) — #105 v3.7.3 contamination_signals backfill migration tool. Re-runs the v3.7.3 spec §3.2 contamination_signals check post-hoc on pre-v3.7.3 literature_corpus[] entries. Per spec §3.
- [ars/scripts/migrate_literature_corpus_to_v3_9_0.py](modules/academic-research-suite/ars/scripts/migrate_literature_corpus_to_v3_9_0.py) — #102 v3.9.0 cross-index triangulation backfill migration tool. Re-runs the v3.9.0 spec §3.4 + §3.5 OpenAlex + Crossref lookups post-hoc on v3.7.3 literature_corpus[] entries that h
- [ars/scripts/openalex_client.py](modules/academic-research-suite/ars/scripts/openalex_client.py) — Minimal OpenAlex API client wrapper. Implements the lookup contract documented at `deep-research/references/openalex_api_protocol.md`. DOI-first with title cross-check (DOI_MISMATC
- [ars/scripts/parse_audit_verdict.py](modules/academic-research-suite/ars/scripts/parse_audit_verdict.py) — parse_audit_verdict.py — ARS v3.6.7 Step 6 Phase 6.1 Reads a codex CLI 0.125+ --json JSONL event stream and converts the structured Section 6 verdict text (from the LAST agent_mess
- [ars/scripts/pdf_content_classifier_worker.py](modules/academic-research-suite/ars/scripts/pdf_content_classifier_worker.py) — Isolated optional PDF content-classifier worker. This process is the only place that imports or invokes ``pdf_inspector``. It receives the exact bytes already hashed by ``pdf_read_
- [ars/scripts/pdf_read_preflight.py](modules/academic-research-suite/ars/scripts/pdf_read_preflight.py) — PDF read-integrity preflight (#512). Guards the LOCAL EXTRACTION CHANNEL behind v3.7.3 `page` anchors: PDF readers silently truncate documents with malformed cross-reference tables
- [ars/scripts/policy_anchor_disclosure_referee.py](modules/academic-research-suite/ars/scripts/policy_anchor_disclosure_referee.py) — #108 policy-anchor disclosure renderer — executable spec / referee. This module is **not** the production renderer. The production renderer is LLM-prose at runtime when the user in
- [ars/scripts/recompute_receipts.py](modules/academic-research-suite/ars/scripts/recompute_receipts.py) — #610 step-5 deterministic arithmetic-receipt calculator. Consumes one gate-validated ``## Recompute Extraction`` artifact (the isolated numeric input surface: typed manuscript valu
- [ars/scripts/render_claim_standing_view.py](modules/academic-research-suite/ars/scripts/render_claim_standing_view.py) — Deterministic presentation of a #655 claim-standing probe (design §5.3/§5.4). Renders the three inseparable parts — consent/recorded-search metadata, the complete candidate ledger 
- [ars/scripts/render_eval_comment.py](modules/academic-research-suite/ars/scripts/render_eval_comment.py) — Render a ``run_evals`` report as the eval-harness PR comment markdown. Display layer ONLY (#184 follow-up): the workflow used to paste the whole ``eval_report.json`` into the PR co
- [ars/scripts/render_harness_retirement_issue.py](modules/academic-research-suite/ars/scripts/render_harness_retirement_issue.py) — Render the monthly harness-retirement tracking issue (#617). The Bucket A inventory comes only from ``ars_phase_scope_manifest.json``. Keeping scope assembly out of the workflow pr
- [ars/scripts/repro_lock_validation.py](modules/academic-research-suite/ars/scripts/repro_lock_validation.py) — Canonical repro_lock field set — single source of truth (#260). The `repro_lock` block is declared in two places: 1. The standalone passport-level validator (`scripts/check_repro_l
- [ars/scripts/research_workflow_profile.py](modules/academic-research-suite/ars/scripts/research_workflow_profile.py) — Validate and apply the research-workflow-profile/1.0 contract (#742). The runtime is deliberately manuscript-blind. It reads only explicitly supplied profile/receipt/inventory path
- [ars/scripts/resolve_human_subjects_authority.py](modules/academic-research-suite/ars/scripts/resolve_human_subjects_authority.py) — Resolve explicit human-subjects authority profiles without inferring jurisdiction. The runtime is standard-library-only. It reads only the paths named on the command line, performs
- [ars/scripts/resolve_review_target_context.py](modules/academic-research-suite/ars/scripts/resolve_review_target_context.py) — Resolve an author-confirmed review target against a versioned criteria registry. The resolver is intentionally blind to manuscript content. It opens only the two explicit input pat
- [ars/scripts/resume_e4_record.py](modules/academic-research-suite/ars/scripts/resume_e4_record.py) — Re-emit an E4 record from a preserved post-dispatch evidence bundle. This is recovery after record emission failed. It never constructs a model transport, continues an interrupted 
- [ars/scripts/retraction_status.py](modules/academic-research-suite/ars/scripts/retraction_status.py) — Deterministic #651 retraction-status resolver and policy helper. The module consumes already-returned OpenAlex/Crossref metadata. It performs no network I/O and never judges whethe
- [ars/scripts/review_criteria_binding.py](modules/academic-research-suite/ars/scripts/review_criteria_binding.py) — Build and validate #684 review-criteria consumer bindings. The tool is deterministic and stdlib-only. It reads only explicitly named paths, never invokes a model or network service
- [ars/scripts/review_panel_provenance.py](modules/academic-research-suite/ars/scripts/review_panel_provenance.py) — Build and replay-validate typed reviewer_full panel provenance. The artifact deliberately has no binary ``independent`` field. Role/persona separation, context freshness, output bl
- [ars/scripts/revision_roadmap.py](modules/academic-research-suite/ars/scripts/revision_roadmap.py) — Validate and replay the #670 revision-authority contract. The runtime is hermetic. It opens only explicitly named local artifacts, never calls a model or network service, never rea
- [ars/scripts/run_ci_pytest_manifest.py](modules/academic-research-suite/ars/scripts/run_ci_pytest_manifest.py) — Unified runner for the pytest invocations CI exercises (issue #156). Reads `scripts/_ci_pytest_manifest.toml` and executes `python -m pytest <path> <args...> -v` for each entry. Ea
- [ars/scripts/run_codex_audit.sh](modules/academic-research-suite/ars/scripts/run_codex_audit.sh) — version: 1.0.0
- [ars/scripts/run_evals.py](modules/academic-research-suite/ars/scripts/run_evals.py) — ARS multi-task eval harness (#184 Delta 2, Phase 1b). Discovers every ``evals/gold/<task>/manifest.yaml``, runs the measurement for each task, and emits a report shaped by ``shared
- [ars/scripts/run_ideation_diversity_no_call.py](modules/academic-research-suite/ars/scripts/run_ideation_diversity_no_call.py) — Offline-only execution envelope for #659. The command set creates and validates files. It has no provider transport, dispatch, probe, actor, subject, judge, or adjudicator executio
- [ars/scripts/run_indirect_prompt_injection_no_call.py](modules/academic-research-suite/ars/scripts/run_indirect_prompt_injection_no_call.py) — Offline-only Phase-2 envelope for #675. This CLI can freeze, materialize, validate, ingest externally recorded evidence, and prepare isolated blind-session packets. It has no provi
- [ars/scripts/run_indirect_prompt_injection_probe.py](modules/academic-research-suite/ars/scripts/run_indirect_prompt_injection_probe.py) — Validate, materialize, and mechanically inspect the #675 seed set. This CLI never dispatches a model and has no network/provider transport. It is a behavioral evaluation probe, not
- [ars/scripts/run_ledger.py](modules/academic-research-suite/ars/scripts/run_ledger.py) — ARS pipeline run ledger (#887): write and check the handoff record. The ledger is a peer file of the Material Passport, named ``<passport-stem>_run_ledger.yaml`` and kept beside it
- [ars/scripts/run_review_criteria_constructive_value.py](modules/academic-research-suite/ars/scripts/run_review_criteria_constructive_value.py) — Contained subscription-CLI runner for the #684 paired measurement. CI exercises asset validation, prompt sealing, fake-Codex dispatch, blinding, and expert-record assembly. No comm
- [ars/scripts/run_role_topology_utility_dry_run.py](modules/academic-research-suite/ars/scripts/run_role_topology_utility_dry_run.py) — Validate and materialize the offline #582 role-topology seed. This module has no dispatch command, model/provider transport, network access, or measurement writer. ``dry-run`` is i
- [ars/scripts/score_calibration_run.py](modules/academic-research-suite/ars/scripts/score_calibration_run.py) — Deterministic scoring for the reviewer-calibration full-tier run (#653). Joins gold labels to frozen panel outputs ONLY here — after every panel record exists — implementing the pr
- [ars/scripts/score_review_criteria_constructive_value.py](modules/academic-research-suite/ars/scripts/score_review_criteria_constructive_value.py) — Reduce a completed #684 paired expert-adjudication record. This stdlib-only scorer reads one explicit local file. It performs no subject or judge dispatch, network/API/model call, 
- [ars/scripts/semantic_scholar_client.py](modules/academic-research-suite/ars/scripts/semantic_scholar_client.py) — Minimal Semantic Scholar API client wrapper. Implements the lookup contract documented at `deep-research/references/semantic_scholar_api_protocol.md` for the v3.7.3 contamination-s
- [ars/scripts/slr_lineage.py](modules/academic-research-suite/ars/scripts/slr_lineage.py) — #111 slr_lineage resolver — pure function over state_tracker.stages. Pipeline plumbing helper for the `deep-research systematic-review → academic-paper full → disclosure --policy-a
- [ars/scripts/sync_adapter_docs.py](modules/academic-research-suite/ars/scripts/sync_adapter_docs.py) — sync_adapter_docs: keep academic-pipeline/references/adapters/overview.md field tables in lockstep with literature_corpus_entry.schema.json. Markers in overview.md: <!-- GENERATED:
- [ars/scripts/temporal_integrity_audit.py](modules/academic-research-suite/ars/scripts/temporal_integrity_audit.py) — v3.9.4 Phase 4 → 5 boundary temporal integrity verifier. 5 passes per spec §3.2: P1 — Mode 1 future-as-past arithmetic (TEMPORAL-ARITHMETIC-IMPOSSIBLE) P2 — Mode 2 version-as-evide
- [ars/scripts/test_431_exact_or_bust.py](modules/academic-research-suite/ars/scripts/test_431_exact_or_bust.py) — #431 — exact-title-or-bust acceptance regression tests. The v5 architecture pivot (spec docs/design/2026-06-13-431-title-match-hardening-spec.md §0.12): a NON-exact title is never 
- [ars/scripts/test__eval_threshold_gate.py](modules/academic-research-suite/ars/scripts/test__eval_threshold_gate.py) — Tests for scripts/_eval_threshold_gate.py (#184 Delta 3 / Fix 1; #328 per-class gate). The absolute-threshold gate must fail a PR when ANY declared binding threshold regresses — ag
- [ars/scripts/test__markdown_lint_util.py](modules/academic-research-suite/ars/scripts/test__markdown_lint_util.py) — Direct tests for the shared markdown grammar (#771). The consumer lints' mutation suites pin their invariants end-to-end; this suite pins the grammar itself once, so a grammar chan
- [ars/scripts/test__next_verified_at_ms.py](modules/academic-research-suite/ars/scripts/test__next_verified_at_ms.py) — Unit tests for scripts/_next_verified_at_ms.py (ARS v3.6.7 Step 6 Phase 6.4). Per spec §5.4 strict-monotonic helper: def _next_verified_at_ms(passport_audit_artifacts: list) -> str
- [ars/scripts/test_adjacent_framing_probe_lint.py](modules/academic-research-suite/ars/scripts/test_adjacent_framing_probe_lint.py) — Lint tests for the opt-in Socratic adjacent-framing probe. Target spec: docs/design/2026-06-18-socratic-adjacent-framing-probe-spec.md. File-content lints (read bytes + regex, no L
- [ars/scripts/test_adjudication_activity.py](modules/academic-research-suite/ars/scripts/test_adjudication_activity.py) — Hermetic black-box and library tests for #673 adjudication activity.
- [ars/scripts/test_ars_anchorize_draft.py](modules/academic-research-suite/ars/scripts/test_ars_anchorize_draft.py) — Tests for ars_anchorize_draft.py (#89 Item 7 Slice A, spec §8.1). Pins the three §8.1 anchorize properties — idempotent (second run byte-identical), content-neutral (output minus m
- [ars/scripts/test_ars_apply_revision_patch.py](modules/academic-research-suite/ars/scripts/test_ars_apply_revision_patch.py) — Tests for ars_apply_revision_patch.py (#89 Item 7 Slice A, spec §8.2 + §8.3). Covers: per-op positive/negative paths, the two-phase fail-closed contract (any failure → whole patch 
- [ars/scripts/test_ars_cache_invalidate.py](modules/academic-research-suite/ars/scripts/test_ars_cache_invalidate.py) — Tests for the /ars-cache-invalidate CLI shim (Delta 2, deliverable 6). Spec: docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md §2 Delta 2.
- [ars/scripts/test_ars_mark_read.py](modules/academic-research-suite/ars/scripts/test_ars_mark_read.py) — Unit tests for scripts/ars_mark_read.py. Per v3.6.8 spec §3.6 + Step 7 (round-2 R2-002, round-5 R5-003 amends). Covers: - 4 fail-fast modes (no active passport / passport not found
- [ars/scripts/test_ars_update_check.py](modules/academic-research-suite/ars/scripts/test_ars_update_check.py) — Tests for scripts/ars_update_check.sh (#544) and its announce integration. Hermetic: the remote is a file:// URL fixture, the state dir is a tmpdir, CLAUDE_PLUGIN_ROOT is a fixture
- [ars/scripts/test_ars_write_scope_guard.py](modules/academic-research-suite/ars/scripts/test_ars_write_scope_guard.py) — TDD test suite for the ARS write-scope guard PreToolUse hook (#134 Slice 1). Spec: docs/design/2026-06-01-ars-134-conductor-rescope-deterministic-write-guard-spec.md (§3.4). The ho
- [ars/scripts/test_arxiv_client.py](modules/academic-research-suite/ars/scripts/test_arxiv_client.py) — Tests for arXiv client per deep-research/references/arxiv_api_protocol.md. Mirrors test_crossref_client.py. arXiv API differs from Crossref in three ways the tests exercise: (1) th
- [ars/scripts/test_assemble_calibration_corpus.py](modules/academic-research-suite/ars/scripts/test_assemble_calibration_corpus.py) — Mutation tests for assemble_calibration_corpus.py (#653).
- [ars/scripts/test_audit_panel_claims.py](modules/academic-research-suite/ars/scripts/test_audit_panel_claims.py) — Tests for scripts/audit_panel_claims.py (#1002, part 2). Synthetic reports only.
- [ars/scripts/test_audit_schemas.py](modules/academic-research-suite/ars/scripts/test_audit_schemas.py) — Phase 6.2 acceptance tests for the four v3.6.7 Step 6 audit schemas. Per spec §10 verification gate: 1. All four schemas parse as valid JSON Schema 2020-12. 2. Example payloads in 
- [ars/scripts/test_audit_snapshot_render_section_0.py](modules/academic-research-suite/ars/scripts/test_audit_snapshot_render_section_0.py) — Render-side regression test for v3.7.1 Step 2 — Section 0 Scope Report. Codex round-1 review of PR #78 surfaced a P1 architectural finding: the static Section 0 block was prepended
- [ars/scripts/test_block_parser.py](modules/academic-research-suite/ars/scripts/test_block_parser.py) — Tests for the shared block parser (#89 Item 7 Slice A, spec §8.1). Covers: segmentation per supported block class, marker attachment, the §3.1 malformed-state rejections (duplicate
- [ars/scripts/test_bootstrap_timeline_yaml.py](modules/academic-research-suite/ars/scripts/test_bootstrap_timeline_yaml.py) — Tests for bootstrap_timeline_yaml.py (opt-in Crossref + pdftotext).
- [ars/scripts/test_build_calibration_measurement_row.py](modules/academic-research-suite/ars/scripts/test_build_calibration_measurement_row.py) — Mutation tests for build_calibration_measurement_row.py (#653 / #828).
- [ars/scripts/test_build_claim_standing_candidate_ledger.py](modules/academic-research-suite/ars/scripts/test_build_claim_standing_candidate_ledger.py) — Hermetic conformance and mutation tests for #655 Track A.
- [ars/scripts/test_build_claim_standing_query_plan.py](modules/academic-research-suite/ars/scripts/test_build_claim_standing_query_plan.py) — #655 PR-C: consent-surface builder tests (design §3.1 trigger + §3.2 consent). Gate 1 (§9): only exact high-impact registry rows are eligible; RANDOM / TOP-UP / NOT-SELECTED / ALL 
- [ars/scripts/test_build_submission_packet_manifest.py](modules/academic-research-suite/ars/scripts/test_build_submission_packet_manifest.py) — Hermetic contract, replay, and adversarial tests for issue #667.
- [ars/scripts/test_check_215_field_norm.py](modules/academic-research-suite/ars/scripts/test_check_215_field_norm.py) — Unit tests for check_215_field_norm.py (#215). The lint reads the three real reviewer surfaces. These tests (a) assert the shipped files pass, and (b) monkey-patch the file reader 
- [ars/scripts/test_check_216_surface_form.py](modules/academic-research-suite/ars/scripts/test_check_216_surface_form.py) — Mutation tests for check_216_surface_form.py (#216). The lint reads the real Devil's Advocate agent surface. These tests (a) assert the shipped file passes, and (b) monkey-patch th
- [ars/scripts/test_check_268_nested_commitment_ledger.py](modules/academic-research-suite/ars/scripts/test_check_268_nested_commitment_ledger.py) — Mutation tests for check_268_nested_commitment_ledger. Each invariant is exercised against a deliberately-mutated in-memory fixture to confirm it FAILs — guarding against a trivial
- [ars/scripts/test_check_390_revision_patch_discipline.py](modules/academic-research-suite/ars/scripts/test_check_390_revision_patch_discipline.py) — Tests for check_390_revision_patch_discipline.py (#390 Slice B, #424). Mutation discipline: every invariant has a passing case against the real tree artifacts and a failing case pr
- [ars/scripts/test_check_392_citation_verification_intake.py](modules/academic-research-suite/ars/scripts/test_check_392_citation_verification_intake.py) — Unit tests for check_392_citation_verification_intake.py (#392 lint).
- [ars/scripts/test_check_394_submission_policy.py](modules/academic-research-suite/ars/scripts/test_check_394_submission_policy.py) — Tests for check_394_submission_policy.py (#394 slice 4, plan D5). Mutation discipline: every invariant has a passing case against the real tree artifacts and a failing case proving
- [ars/scripts/test_check_439_format_profile.py](modules/academic-research-suite/ars/scripts/test_check_439_format_profile.py) — Tests for check_439_format_profile.py (#439 Slice A). Mutation discipline: every invariant has a passing case against the real schema and a failing case proving the check fires whe
- [ars/scripts/test_check_619_disclosure_closeout.py](modules/academic-research-suite/ars/scripts/test_check_619_disclosure_closeout.py) — Focused mutation coverage for the #619 disclosure closeout.
- [ars/scripts/test_check_630_codex_subscription_transport.py](modules/academic-research-suite/ars/scripts/test_check_630_codex_subscription_transport.py) — Mutation tests for the #630 integration guard.
- [ars/scripts/test_check_669_review_pathway_rule_trace.py](modules/academic-research-suite/ars/scripts/test_check_669_review_pathway_rule_trace.py) — ROOT = Path(__file__).resolve().parents[1]
- [ars/scripts/test_check_670_revision_roadmap_integration.py](modules/academic-research-suite/ars/scripts/test_check_670_revision_roadmap_integration.py) — Hermetic mutation tests for the static #670 integration guard.
- [ars/scripts/test_check_673_adjudication_activity.py](modules/academic-research-suite/ars/scripts/test_check_673_adjudication_activity.py) — Hermetic mutation tests for the static #673 integration guard.
- [ars/scripts/test_check_684_review_criteria_binding.py](modules/academic-research-suite/ars/scripts/test_check_684_review_criteria_binding.py) — def _texts() -> dict[Path, str]:
- [ars/scripts/test_check_acronyms.py](modules/academic-research-suite/ars/scripts/test_check_acronyms.py) — Tests for scripts/check_acronyms.py (#849). Every fixture is synthetic. The small cases below give one manuscript per token rule and exclusion in the issue; the full manuscript und
- [ars/scripts/test_check_agents_mirror_sync.py](modules/academic-research-suite/ars/scripts/test_check_agents_mirror_sync.py) — Tests for check_agents_mirror_sync.py (#413). Mutation discipline: every invariant has a passing case (green fixture tree + the real repo tree) and a failing case proving the check
- [ars/scripts/test_check_audit_artifact_consistency.py](modules/academic-research-suite/ars/scripts/test_check_audit_artifact_consistency.py) — Phase 6.3 acceptance tests for ARS v3.6.7 §3.7 invariant lint. Every row in spec §3.7 families A-F gets at least one positive (valid fixture passes) and one negative (deliberately-
- [ars/scripts/test_check_benchmark_report.py](modules/academic-research-suite/ars/scripts/test_check_benchmark_report.py) — Unit tests for check_benchmark_report.py.
- [ars/scripts/test_check_bibliographic_integrity_signals.py](modules/academic-research-suite/ars/scripts/test_check_bibliographic_integrity_signals.py) — Tests for the #678 canonical bibliographic-integrity signal carrier.
- [ars/scripts/test_check_calibration_tiers.py](modules/academic-research-suite/ars/scripts/test_check_calibration_tiers.py) — Mutation tests for the bounded reviewer calibration contract.
- [ars/scripts/test_check_changelog_covers_merges.py](modules/academic-research-suite/ars/scripts/test_check_changelog_covers_merges.py) — Unit tests for check_changelog_covers_merges.py.
- [ars/scripts/test_check_ci_pytest_manifest.py](modules/academic-research-suite/ars/scripts/test_check_ci_pytest_manifest.py) — Unit tests for scripts/check_ci_pytest_manifest.py (issue #156). Lint guards 6 failure modes on the unified pytest manifest: 1. manifest entry path does not exist on disk 2. duplic
- [ars/scripts/test_check_claim_standing_candidate_ledger_integration.py](modules/academic-research-suite/ars/scripts/test_check_claim_standing_candidate_ledger_integration.py) — Mutation tests for the static #655 Track A integration guard.
- [ars/scripts/test_check_claim_standing_freshness.py](modules/academic-research-suite/ars/scripts/test_check_claim_standing_freshness.py) — #655 PR-C: §7 freshness tests (gate 13: drift makes an old result stale). The probe identity binds claim text, consent receipt, query plan, adapter registry, candidate ledger, and 
- [ars/scripts/test_check_collaboration_depth_rubric.py](modules/academic-research-suite/ars/scripts/test_check_collaboration_depth_rubric.py) — Unit tests for check_collaboration_depth_rubric.py (ARS v3.5).
- [ars/scripts/test_check_command_frontmatter_name.py](modules/academic-research-suite/ars/scripts/test_check_command_frontmatter_name.py) — Mutation tests for check_command_frontmatter_name.py (#633). Each test builds a synthetic repo root under a TemporaryDirectory and runs the lint as a subprocess, mirroring CI invoc
- [ars/scripts/test_check_command_skill_dispatch.py](modules/academic-research-suite/ars/scripts/test_check_command_skill_dispatch.py) — Regressions for lost command dispatch and cwd-dependent references.
- [ars/scripts/test_check_committee_correspondence.py](modules/academic-research-suite/ars/scripts/test_check_committee_correspondence.py) — Schema, mutation, and end-to-end tests for #668 correspondence accounting.
- [ars/scripts/test_check_compliance_report.py](modules/academic-research-suite/ars/scripts/test_check_compliance_report.py) — Unit tests for check_compliance_report.py (Schema 12 validator).
- [ars/scripts/test_check_content_coverage_advisory_integration.py](modules/academic-research-suite/ars/scripts/test_check_content_coverage_advisory_integration.py) — Mutation tests for the static #681 advisory integration guard.
- [ars/scripts/test_check_control_availability.py](modules/academic-research-suite/ars/scripts/test_check_control_availability.py) — Mutation tests for check_control_availability.py (#757). Strategy: copy the real surfaces into a tmp repo root, verify the baseline passes, then apply one mutation per test and ass
- [ars/scripts/test_check_cross_document_consistency_advisory_integration.py](modules/academic-research-suite/ars/scripts/test_check_cross_document_consistency_advisory_integration.py) — Mutation tests for the static #672 integration guard.
- [ars/scripts/test_check_cross_model_handoff_contract.py](modules/academic-research-suite/ars/scripts/test_check_cross_model_handoff_contract.py) — Mutation tests for check_cross_model_handoff_contract.py (#527). One failing witness per invariant branch, on in-memory mutations of the committed surfaces.
- [ars/scripts/test_check_cross_model_verification_sync.py](modules/academic-research-suite/ars/scripts/test_check_cross_model_verification_sync.py) — Tests for the cross-model grounding-guard doc-sync lint (#346 / #349). Mutation-style: confirm the lint PASSES the real tree and FAILS on each violation class it exists to catch, s
- [ars/scripts/test_check_data_access_level.py](modules/academic-research-suite/ars/scripts/test_check_data_access_level.py) — Unit + mutation tests for check_data_access_level.py. Two layers, matching the lint's shape after the #756 single-pass rewrite: - CLI-level tests (subprocess via `--path`, preservi
- [ars/scripts/test_check_data_flows.py](modules/academic-research-suite/ars/scripts/test_check_data_flows.py) — Mutation tests for check_data_flows.py (#758). Two layers: - the real tree must pass (baseline), and - a synthetic fixture repo exercises each invariant's fire/no-fire edge without
- [ars/scripts/test_check_decision_contract.py](modules/academic-research-suite/ars/scripts/test_check_decision_contract.py) — Mutation tests for check_decision_contract.py.
- [ars/scripts/test_check_degradation_registry.py](modules/academic-research-suite/ars/scripts/test_check_degradation_registry.py) — Mutation tests for scripts/check_degradation_registry.py (#511 Part A). One failing witness per invariant branch (repo lint-test convention): each test mutates a copy of the shippe
- [ars/scripts/test_check_distribution_surface_claims.py](modules/academic-research-suite/ars/scripts/test_check_distribution_surface_claims.py) — Mutation tests for check_distribution_surface_claims.py (#753).
- [ars/scripts/test_check_domain_evidence_profile.py](modules/academic-research-suite/ars/scripts/test_check_domain_evidence_profile.py) — Mutation suite for check_domain_evidence_profile.py (#259). Per the iron law: positive + negative tests for every check. Each negative fixture mutates ONE artifact so exactly one c
- [ars/scripts/test_check_e4_promotion.py](modules/academic-research-suite/ars/scripts/test_check_e4_promotion.py) — Mutation tests for the #616 E4 promotion-copy boundary.
- [ars/scripts/test_check_evals_gold_set.py](modules/academic-research-suite/ars/scripts/test_check_evals_gold_set.py) — Mutation tests for scripts/check_evals_gold_set.py. Each test mutates the clean fixture to violate one invariant and asserts the validator catches it. Plus one positive test on the
- [ars/scripts/test_check_evidence_row_integration.py](modules/academic-research-suite/ars/scripts/test_check_evidence_row_integration.py) — Mutation tests for the #656 cross-file integration guard.
- [ars/scripts/test_check_field_norm_severity.py](modules/academic-research-suite/ars/scripts/test_check_field_norm_severity.py) — Unit tests for check_field_norm_severity.py (#215). The #215 gold set is a first-party REGRESSION FIXTURE, not a detector calibration set: there is no deterministic predictor for f
- [ars/scripts/test_check_firm_rules_sync.py](modules/academic-research-suite/ars/scripts/test_check_firm_rules_sync.py) — Mutation tests for check_firm_rules_sync.py (v3.10 PR-A). Confirms the lint is not a trivial accept-all: each mutation that breaks the sync or reintroduces the ID collision MUST ma
- [ars/scripts/test_check_heldout_measurement_report.py](modules/academic-research-suite/ars/scripts/test_check_heldout_measurement_report.py) — Mutation tests for scripts/check_heldout_measurement_report.py (#654). Discipline mirrors the repo's other checker test suites: one valid fixture must pass with zero errors, and ev
- [ars/scripts/test_check_human_subjects_output_contract.py](modules/academic-research-suite/ars/scripts/test_check_human_subjects_output_contract.py) — Mutation tests for the #665 human-subjects output boundary.
- [ars/scripts/test_check_human_subjects_reference_migration.py](modules/academic-research-suite/ars/scripts/test_check_human_subjects_reference_migration.py) — Hermetic mutation tests for the bounded #680 reference migration.
- [ars/scripts/test_check_instruction_data_boundary.py](modules/academic-research-suite/ars/scripts/test_check_instruction_data_boundary.py) — Mutation test for check_instruction_data_boundary.py (#272 guidance layer). Confirms the lint is not a trivial accept-all: each mutation that removes, guts, weakens, duplicates, or
- [ars/scripts/test_check_judge_prompt_version.py](modules/academic-research-suite/ars/scripts/test_check_judge_prompt_version.py) — Tests for check_judge_prompt_version (#361 drift guard). The clean fixture must PASS; a prompt edit that does not re-pin the hash must FAIL (the core #361 backstop); a correct re-p
- [ars/scripts/test_check_method_weaknesses_sync.py](modules/academic-research-suite/ars/scripts/test_check_method_weaknesses_sync.py) — Tests for check_method_weaknesses_sync.py (#916). The marker grammar is tested once in test_skill_lint_marker_block.py (#923). These tests check the wiring: the clean repository pa
- [ars/scripts/test_check_model_tiering.py](modules/academic-research-suite/ars/scripts/test_check_model_tiering.py) — Mutation tests for check_model_tiering.py (#517 classification drift guard).
- [ars/scripts/test_check_panel_synthesis.py](modules/academic-research-suite/ars/scripts/test_check_panel_synthesis.py) — Schema 13.2 panel checker tests, including exhaustive decision profiles.
- [ars/scripts/test_check_passport_reset_contract.py](modules/academic-research-suite/ars/scripts/test_check_passport_reset_contract.py) — Unit tests for check_passport_reset_contract.py (ARS v3.6.3 lint). Enforces the contract: every text file that mentions the env-flag token `ARS_PASSPORT_RESET` must co-locate a ref
- [ars/scripts/test_check_pattern_eval_manifest.py](modules/academic-research-suite/ars/scripts/test_check_pattern_eval_manifest.py) — Tests for scripts/check_pattern_eval_manifest.py. Covers: - Micro schema positive validation against a synthetic well-formed manifest. - Integration schema positive validation agai
- [ars/scripts/test_check_persuasion_invariance_fixtures.py](modules/academic-research-suite/ars/scripts/test_check_persuasion_invariance_fixtures.py) — Mutation tests for check_persuasion_invariance_fixtures.py (#576 Spec B §14 v0.1). Runs the checker against a synthetic fixture tree (never the real one, so the tests stay hermetic
- [ars/scripts/test_check_phase_conformance.py](modules/academic-research-suite/ars/scripts/test_check_phase_conformance.py) — Tests for the six Schema 13.2 phase-conformance check families.
- [ars/scripts/test_check_pipeline_boundary_semantics.py](modules/academic-research-suite/ars/scripts/test_check_pipeline_boundary_semantics.py) — Mutation tests for check_pipeline_boundary_semantics.py (#528 defrift lock). One failing witness per invariant branch: each test mutates exactly one pinned surface fragment and ass
- [ars/scripts/test_check_pipeline_integrity.py](modules/academic-research-suite/ars/scripts/test_check_pipeline_integrity.py) — Unit tests for check_pipeline_integrity.py (v3.9.2 advisory verifier).
- [ars/scripts/test_check_policy_anchor_protocol.py](modules/academic-research-suite/ars/scripts/test_check_policy_anchor_protocol.py) — Mutation tests for scripts/check_policy_anchor_protocol.py.
- [ars/scripts/test_check_policy_anchor_table.py](modules/academic-research-suite/ars/scripts/test_check_policy_anchor_table.py) — Mutation tests for scripts/check_policy_anchor_table.py. Each test mutates a known-good anchor-table snippet in a known-bad way and asserts the validator reports the expected viola
- [ars/scripts/test_check_prisma_trAIce_freshness.py](modules/academic-research-suite/ars/scripts/test_check_prisma_trAIce_freshness.py) — Unit tests for check_prisma_trAIce_freshness.py.
- [ars/scripts/test_check_promotion_bakeoff_preregistration.py](modules/academic-research-suite/ars/scripts/test_check_promotion_bakeoff_preregistration.py) — Focused mutation tests for the #789 sealed bakeoff lifecycle.
- [ars/scripts/test_check_ranking_lift.py](modules/academic-research-suite/ars/scripts/test_check_ranking_lift.py) — Tests for scripts/check_ranking_lift.py (#184 Delta 4 lift gate). The OPEN-issue check is always monkeypatched; no test touches the network.
- [ars/scripts/test_check_re_review_synthesis.py](modules/academic-research-suite/ars/scripts/test_check_re_review_synthesis.py) — Mutation suite for scripts/check_re_review_synthesis.py (#576 Spec B §13). Convention (Spec A §13 witness style): three hand-pinned golden scenarios pass end-to-end; each invariant
- [ars/scripts/test_check_receipt_enum_sync.py](modules/academic-research-suite/ars/scripts/test_check_receipt_enum_sync.py) — Mutation tests for the #610 receipt closed-enum defrift lint.
- [ars/scripts/test_check_repro_lock.py](modules/academic-research-suite/ars/scripts/test_check_repro_lock.py) — Unit tests for check_repro_lock.py.
- [ars/scripts/test_check_review_form_note_sync.py](modules/academic-research-suite/ars/scripts/test_check_review_form_note_sync.py) — Tests for check_review_form_note_sync.py (#921). The marker grammar is tested once in test_skill_lint_marker_block.py (#923). These tests check the wiring (the clean repository pas
- [ars/scripts/test_check_reviewer_data_fences.py](modules/academic-research-suite/ars/scripts/test_check_reviewer_data_fences.py) — Mutation test for check_reviewer_data_fences.py (#574 A6 / PR #578 fence pin). Confirms the lint is not a trivial accept-all: removing, weakening, or duplicating a fence on any pin
- [ars/scripts/test_check_reviewer_finding_contract.py](modules/academic-research-suite/ars/scripts/test_check_reviewer_finding_contract.py) — Mutation test for check_reviewer_finding_contract.py (#574 behavior batch). Each retired drift class, re-introduced, must make the lint FAIL: quota restoration (A1), receipt/contra
- [ars/scripts/test_check_reviewer_role_label.py](modules/academic-research-suite/ars/scripts/test_check_reviewer_role_label.py) — Mutation tests for the #611 Journal-Fit Reviewer display-name contract.
- [ars/scripts/test_check_reviewer_scoring_honesty.py](modules/academic-research-suite/ars/scripts/test_check_reviewer_scoring_honesty.py) — Mutation tests for check_reviewer_scoring_honesty.py.
- [ars/scripts/test_check_reviewer_sprint_prompt_sync.py](modules/academic-research-suite/ars/scripts/test_check_reviewer_sprint_prompt_sync.py) — Mutation tests for the #611 reviewer sprint-prompt canonical source.
- [ars/scripts/test_check_revision_claim_drift_suite_v2.py](modules/academic-research-suite/ars/scripts/test_check_revision_claim_drift_suite_v2.py) — Bounded mutation tests for the hermetic revision-claim-drift v2 guard (#679).
- [ars/scripts/test_check_revision_token_conservation.py](modules/academic-research-suite/ars/scripts/test_check_revision_token_conservation.py) — Mutation tests for check_revision_token_conservation.py (#570). Covers: numeric-token multiset conservation (decimals, percentages, thousands separators, signs, en-dash ranges), Un
- [ars/scripts/test_check_risk_register.py](modules/academic-research-suite/ars/scripts/test_check_risk_register.py) — Mutation tests for check_risk_register.py (#759). Strategy: build a tmp repo root that mirrors the real register, README, and capability matrix, materialize every path the real reg
- [ars/scripts/test_check_role_scoped_contract.py](modules/academic-research-suite/ars/scripts/test_check_role_scoped_contract.py) — Mutation tests for check_role_scoped_contract.py.
- [ars/scripts/test_check_routing_core_sync.py](modules/academic-research-suite/ars/scripts/test_check_routing_core_sync.py) — Tests for check_routing_core_sync.py and the announce's routing core (#892). The marker grammar is tested once in test_skill_lint_marker_block.py (#923). These tests check the wiri
- [ars/scripts/test_check_rq_framing_patterns.py](modules/academic-research-suite/ars/scripts/test_check_rq_framing_patterns.py) — REPO_ROOT = Path(__file__).resolve().parents[1]
- [ars/scripts/test_check_rubric_weight_consistency.py](modules/academic-research-suite/ars/scripts/test_check_rubric_weight_consistency.py) — Compatibility tests for the retired rubric-weight checker filename.
- [ars/scripts/test_check_seeded_defect_fixtures.py](modules/academic-research-suite/ars/scripts/test_check_seeded_defect_fixtures.py) — Mutation tests for check_seeded_defect_fixtures.py (#574/#610 v0.2). Runs the checker against a synthetic fixture tree (never the real one, so the tests stay hermetic) and asserts 
- [ars/scripts/test_check_setup_cross_model_parity.py](modules/academic-research-suite/ars/scripts/test_check_setup_cross_model_parity.py) — Unit tests for check_setup_cross_model_parity.py (#491 fold-in).
- [ars/scripts/test_check_skill_description_length.py](modules/academic-research-suite/ars/scripts/test_check_skill_description_length.py) — Parsed-string boundary and invalid-frontmatter regressions for #864.
- [ars/scripts/test_check_skill_inventory_parity.py](modules/academic-research-suite/ars/scripts/test_check_skill_inventory_parity.py) — Mutation tests for check_skill_inventory_parity.py (#809). A synthetic root carries two skills on all four surfaces. Each test breaks exactly one surface in one direction and asser
- [ars/scripts/test_check_spec_consistency.py](modules/academic-research-suite/ars/scripts/test_check_spec_consistency.py) — Unit tests for check_spec_consistency.py. Pre-#171, check_spec_consistency.py uses module-level ROOT + ERRORS state. These tests monkey-patch ROOT into a TemporaryDirectory contain
- [ars/scripts/test_check_sprint_contract.py](modules/academic-research-suite/ars/scripts/test_check_sprint_contract.py) — Schema 13.2 validator tests.
- [ars/scripts/test_check_stage_capability_matrix.py](modules/academic-research-suite/ars/scripts/test_check_stage_capability_matrix.py) — Mutation tests for scripts/check_stage_capability_matrix.py (#745). One failing witness per invariant branch (repo lint-test convention): each test mutates a copy of a valid matrix
- [ars/scripts/test_check_submission_packet_manifest_integration.py](modules/academic-research-suite/ars/scripts/test_check_submission_packet_manifest_integration.py) — Mutation tests for the static #667 integration boundary.
- [ars/scripts/test_check_surface_form_parity.py](modules/academic-research-suite/ars/scripts/test_check_surface_form_parity.py) — Tests for check_surface_form_parity.py (#216). Three layers: 1. shipped gold set passes, 2. mutation tests — each integrity/provenance/pair invariant goes RED when broken (non-vacu
- [ars/scripts/test_check_task_type.py](modules/academic-research-suite/ars/scripts/test_check_task_type.py) — Unit tests for check_task_type.py lint script.
- [ars/scripts/test_check_tools_allowlist.py](modules/academic-research-suite/ars/scripts/test_check_tools_allowlist.py) — Tests for check_tools_allowlist.py (#524). Mutation discipline: every invariant branch has a passing case (green fixture tree + the real repo tree) and a failing case proving the c
- [ars/scripts/test_check_tortured_phrase_screening_integration.py](modules/academic-research-suite/ars/scripts/test_check_tortured_phrase_screening_integration.py) — Mutation tests for the hermetic #660 integration guard.
- [ars/scripts/test_check_v3_10_134_write_scope.py](modules/academic-research-suite/ars/scripts/test_check_v3_10_134_write_scope.py) — Mutation tests for check_v3_10_134_write_scope.py (the fail-open guard lint). feedback_schema_mutation_test_for_constraints: after a lint passes on the real repo, inject deliberate
- [ars/scripts/test_check_v3_10_policy.py](modules/academic-research-suite/ars/scripts/test_check_v3_10_policy.py) — Tests for the v3.10 policy-layer lint (#127 PR-B). Two halves: A. Marker-grammar parser fixtures (spec §3 PR-B item 6): terminal co-emit / non-terminal advisory / non-terminal clea
- [ars/scripts/test_check_v3_6_7_pattern_protection.py](modules/academic-research-suite/ars/scripts/test_check_v3_6_7_pattern_protection.py) — Unit tests for check_v3_6_7_pattern_protection.py (ARS v3.6.7 lint). Mutation evidence preserved from codex review rounds R3-R5 (B2 phase). Each test mutates a v3.6.7 PATTERN PROTE
- [ars/scripts/test_check_v3_6_8_audit_scope_block.py](modules/academic-research-suite/ars/scripts/test_check_v3_6_8_audit_scope_block.py) — Mutation tests for ARS v3.7.1 Step 2 — D2 audit Scope Report lint. Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md §3.2 (D2 — Audit scope co
- [ars/scripts/test_check_v3_6_8_cite_provenance_pipeline.py](modules/academic-research-suite/ars/scripts/test_check_v3_6_8_cite_provenance_pipeline.py) — Mutation tests for ARS v3.7.1 Step 3b — Cite-Time Provenance Finalizer. Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md § Step 3b — Pipeline
- [ars/scripts/test_check_v3_6_8_frontmatter_trust_schema.py](modules/academic-research-suite/ars/scripts/test_check_v3_6_8_frontmatter_trust_schema.py) — Tests for ARS v3.7.1 trust-chain frontmatter lint (Step 1 of v3.7.1 impl). Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md § 3.1 D1, § Step 
- [ars/scripts/test_check_v3_6_8_mark_read_commands.py](modules/academic-research-suite/ars/scripts/test_check_v3_6_8_mark_read_commands.py) — Unit tests for check_v3_6_8_mark_read_commands.py. Per v3.6.8 spec §3.6 Step 7 acceptance criteria. The lint asserts that the 2 commands (mark-read, unmark-read) exist, carry the v
- [ars/scripts/test_check_v3_6_8_pattern_protection.py](modules/academic-research-suite/ars/scripts/test_check_v3_6_8_pattern_protection.py) — Mutation tests for ARS v3.7.1 byte-equivalence SHA gate. Spec: docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md § Step 0 — Lint manifest separation
- [ars/scripts/test_check_v3_7_3_three_layer_citation.py](modules/academic-research-suite/ars/scripts/test_check_v3_7_3_three_layer_citation.py) — Tests for v3.7.3 Three-Layer Citation lint. Spec: docs/design/2026-05-12-ars-v3.7.3-claim-faithfulness-and-contaminated-source-spec.md §3.1 External motivation: Zhao et al. arXiv:2
- [ars/scripts/test_check_v3_8_annotation_literal_sync.py](modules/academic-research-suite/ars/scripts/test_check_v3_8_annotation_literal_sync.py) — Unit tests for v3.8 annotation-literal sync lint. The lint enforces that every `ANNOTATION_HIGH_WARN_*` constant in `scripts/claim_audit_finalizer.py` has a matching bracket-prefix
- [ars/scripts/test_check_v3_9_0_triangulation.py](modules/academic-research-suite/ars/scripts/test_check_v3_9_0_triangulation.py) — Tests for check_v3_9_0_triangulation.py lint per spec v3.9.0 §3.8.
- [ars/scripts/test_check_v3_9_2_phase_boundary.py](modules/academic-research-suite/ars/scripts/test_check_v3_9_2_phase_boundary.py) — Unit tests for check_v3_9_2_phase_boundary.py.
- [ars/scripts/test_check_v3_9_4_temporal_verification.py](modules/academic-research-suite/ars/scripts/test_check_v3_9_4_temporal_verification.py) — Tests for v3.9.4 temporal verification spec lint + schema conformance. Per docs/design/2026-05-18-ars-v3.9.4-temporal-verification-spec.md §7.
- [ars/scripts/test_check_version_consistency.py](modules/academic-research-suite/ars/scripts/test_check_version_consistency.py) — Unit tests for check_version_consistency.py.
- [ars/scripts/test_check_workflow_classification.py](modules/academic-research-suite/ars/scripts/test_check_workflow_classification.py) — Mutation tests for check_workflow_classification.py (#755).
- [ars/scripts/test_chinese_literature_client.py](modules/academic-research-suite/ars/scripts/test_chinese_literature_client.py) — Tests for the Chinese-literature resolver client (#595). Per `deep-research/references/chinese_literature_api_protocol.md`. Structure mirrors `test_arxiv_client.py` (per-client uni
- [ars/scripts/test_citation_existence_policy.py](modules/academic-research-suite/ars/scripts/test_citation_existence_policy.py) — Tests for the citation-existence terminal policy (Delta 3 + INVARIANT C-V6). Renamed from the original `test_default_blocking_gate.py` (the v3.10 blocking-default form was withdraw
- [ars/scripts/test_citation_verification_summary.py](modules/academic-research-suite/ars/scripts/test_citation_verification_summary.py) — Tests for citation_verification_summary — schema + reducer (Delta 4). Spec: docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md §2 Delta 4 + §0(4a) / INVARIANT C-V6(a) (
- [ars/scripts/test_claim_audit_calibration.py](modules/academic-research-suite/ars/scripts/test_claim_audit_calibration.py) — Calibration-mode test for v3.8 claim_ref_alignment_audit_agent (T-C1..T-C3). Per spec §7.7 in docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md. Three-tier acceptance:
- [ars/scripts/test_claim_audit_finalizer.py](modules/academic-research-suite/ars/scripts/test_claim_audit_finalizer.py) — Finalizer integration tests for v3.8 claim_ref_alignment_audit_agent (T-F1a..h + T-F2..T-F5). Per spec §7.5 in docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md. These
- [ars/scripts/test_claim_audit_pipeline.py](modules/academic-research-suite/ars/scripts/test_claim_audit_pipeline.py) — Audit-pipeline unit tests for v3.8 claim_ref_alignment_audit_agent (T-P1..T-P11). Per spec §7.2 in docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md. These tests pin t
- [ars/scripts/test_claim_audit_schema.py](modules/academic-research-suite/ars/scripts/test_claim_audit_schema.py) — Schema-validation tests for v3.8 claim_ref_alignment_audit_agent (T-S1..T-S8). Per spec §7.1 in docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md. The test plan sectio
- [ars/scripts/test_claim_intent_manifest.py](modules/academic-research-suite/ars/scripts/test_claim_intent_manifest.py) — Manifest tests for v3.8 claim_ref_alignment_audit_agent (T-M1, T-M2, T-M3). Per spec §7.3 in docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md. These tests pin manifes
- [ars/scripts/test_claim_registry_coverage.py](modules/academic-research-suite/ars/scripts/test_claim_registry_coverage.py) — Regression and adversarial tests for #737 Claim Registry coverage.
- [ars/scripts/test_claim_standing_discovery.py](modules/academic-research-suite/ars/scripts/test_claim_standing_discovery.py) — ROOT = Path(__file__).resolve().parent.parent
- [ars/scripts/test_claim_standing_pipeline_wiring.py](modules/academic-research-suite/ars/scripts/test_claim_standing_pipeline_wiring.py) — #655 PR-C: pipeline-wiring noninterference tests (design §9 gate 12). Running the wiring layer changes no Phase E verdict, gate, manuscript, citation, or read-ledger byte — proven 
- [ars/scripts/test_claim_standing_stance_assets.py](modules/academic-research-suite/ars/scripts/test_claim_standing_stance_assets.py) — ROOT = Path(__file__).resolve().parent.parent
- [ars/scripts/test_claim_standing_stance_contracts.py](modules/academic-research-suite/ars/scripts/test_claim_standing_stance_contracts.py) — ROOT = Path(__file__).resolve().parent.parent
- [ars/scripts/test_claim_standing_stance_runner.py](modules/academic-research-suite/ars/scripts/test_claim_standing_stance_runner.py) — _rehash_plan,
- [ars/scripts/test_claim_standing_transmissions.py](modules/academic-research-suite/ars/scripts/test_claim_standing_transmissions.py) — #655 PR-C: transmission-ledger contract and gate-14 allowlist tests. Design authority: docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md §6 (separate transmi
- [ars/scripts/test_claim_strength_drift_disposition.py](modules/academic-research-suite/ars/scripts/test_claim_strength_drift_disposition.py) — FINAL_DRAFT_RAW = b"# Exact revised draft\n\nBound manuscript bytes.\n"
- [ars/scripts/test_claim_verification_coverage_contract.py](modules/academic-research-suite/ars/scripts/test_claim_verification_coverage_contract.py) — Static regression contract for #737 coverage-bounded claims language.
- [ars/scripts/test_codex_router_policy.py](modules/academic-research-suite/ars/scripts/test_codex_router_policy.py) — Codex router policy regression tests. These tests guard adapter-only routing rules in `skills/academic-research-suite/SKILL.md`. They are intentionally static: runtime skill routin
- [ars/scripts/test_contamination_signals.py](modules/academic-research-suite/ars/scripts/test_contamination_signals.py) — #105 v3.7.3 contamination_signals resolver tests. Tests the two pure-function signals defined in v3.7.3 spec §3.2 that the migration tool uses to backfill pre-v3.7.3 literature_cor
- [ars/scripts/test_content_coverage_advisory.py](modules/academic-research-suite/ars/scripts/test_content_coverage_advisory.py) — Hermetic replay, aggregation, renderer, and security tests for #681.
- [ars/scripts/test_cross_document_consistency_advisory.py](modules/academic-research-suite/ars/scripts/test_cross_document_consistency_advisory.py) — except ModuleNotFoundError:
- [ars/scripts/test_cross_model_codex_transport.py](modules/academic-research-suite/ars/scripts/test_cross_model_codex_transport.py) — Hermetic contract and runtime tests for the #630 Codex subscription transport.
- [ars/scripts/test_cross_model_handoff.py](modules/academic-research-suite/ars/scripts/test_cross_model_handoff.py) — Deterministic owner → dispatcher → owner fixtures for the #527 envelope. Fake transport only — no external API, no manuscript upload. These fixtures pin the normative grammar in sc
- [ars/scripts/test_cross_model_verification_guards.py](modules/academic-research-suite/ars/scripts/test_cross_model_verification_guards.py) — Behavioral tests for the cross-model grounding guards (#346 / #349). The grounding guards in `shared/cross_model_verification.md` are the load-bearing safety boundary of the cross-
- [ars/scripts/test_crossref_client.py](modules/academic-research-suite/ars/scripts/test_crossref_client.py) — Tests for Crossref client per deep-research/references/crossref_api_protocol.md.
- [ars/scripts/test_dispatch_calibration_panel.py](modules/academic-research-suite/ars/scripts/test_dispatch_calibration_panel.py) — Mutation tests for dispatch_calibration_panel.py (#653). Offline via ScriptedTransport.
- [ars/scripts/test_dispatch_e4_panel.py](modules/academic-research-suite/ars/scripts/test_dispatch_e4_panel.py) — Hermetic tests for the E4 dispatch harness (#608). Every case runs on a scripted transport, so the whole evidence contract is exercised without a model call. The valid Phase 1 and 
- [ars/scripts/test_dispatch_panel_claim_audit.py](modules/academic-research-suite/ars/scripts/test_dispatch_panel_claim_audit.py) — Tests for scripts/dispatch_panel_claim_audit.py (#1002). No model call: transports are replaced by a fake runner, and claims and pairs are synthetic.
- [ars/scripts/test_e2e_claim_audit.py](modules/academic-research-suite/ars/scripts/test_e2e_claim_audit.py) — End-to-end claim-faithfulness audit test (spec §7.6 + §13 step 9). Wires `detect_uncited_assertions` → `run_audit_pipeline` → `apply_finalizer` against a synthetic 5-citation paper
- [ars/scripts/test_eval_harness_workflow.py](modules/academic-research-suite/ars/scripts/test_eval_harness_workflow.py) — Tests for .github/workflows/eval-harness.yml (#184 Delta 3 / Fix 1). These assert the *structure and honesty* of the gate workflow, not GitHub's runtime behaviour: it must strict-l
- [ars/scripts/test_evals_citation_extraction.py](modules/academic-research-suite/ars/scripts/test_evals_citation_extraction.py) — Tests for the citation_extraction self-reducer + full gold-set run. Pins the #182 Delta 4 reducer branches and the end-to-end accuracy against the shipped gold set (which was autho
- [ars/scripts/test_evals_lift_report_schema.py](modules/academic-research-suite/ars/scripts/test_evals_lift_report_schema.py) — Schema tests for shared/evals_lift_report.schema.json (#184 Delta 2). Includes the mandatory TRIVIAL-ACCEPT-ALL mutation: swapping the schema for ``{}`` must make a known-bad repor
- [ars/scripts/test_evidence_rows.py](modules/academic-research-suite/ars/scripts/test_evidence_rows.py) — Hermetic contract, security, replay, renderer, and CLI tests for #656. The fixtures contain synthetic text only. The suite deliberately supplies source text as an in-memory value a
- [ars/scripts/test_excluded_source_entry_schema.py](modules/academic-research-suite/ars/scripts/test_excluded_source_entry_schema.py) — Schema tests for Material Passport excluded_sources[] entries (#936).
- [ars/scripts/test_experiment_alignment_overclaim_fixtures.py](modules/academic-research-suite/ars/scripts/test_experiment_alignment_overclaim_fixtures.py) — Fixture guard for evals/heldout/experiment_alignment_overclaim (#915). The two passports are subject-visible inputs for the #260 C4 check. These tests keep them valid against the p
- [ars/scripts/test_experiment_provenance.py](modules/academic-research-suite/ars/scripts/test_experiment_provenance.py) — Tests for #260 Experiment Provenance Intake + claim->experiment alignment. Covers the two new schemas, the seven new cross-array invariants (EP-INV-1..5 / EA-INV-1..2 in check_clai
- [ars/scripts/test_extract_panel_claims.py](modules/academic-research-suite/ars/scripts/test_extract_panel_claims.py) — Tests for scripts/extract_panel_claims.py (#1002). Synthetic bundles only.
- [ars/scripts/test_file_lock.py](modules/academic-research-suite/ars/scripts/test_file_lock.py) — Tests for the shared advisory file-lock helper (#845). The real backend on the CI host is ``fcntl``. The ``msvcrt`` branch is exercised through ``tests.fake_msvcrt`` (the documente
- [ars/scripts/test_human_read_attestation_resolver.py](modules/academic-research-suite/ars/scripts/test_human_read_attestation_resolver.py) — Regression tests for #738 USER_ATTESTED_READ resolution.
- [ars/scripts/test_ideation_diversity_assignment_gate.py](modules/academic-research-suite/ars/scripts/test_ideation_diversity_assignment_gate.py) — ROOT = Path(__file__).resolve().parent.parent
- [ars/scripts/test_indirect_prompt_injection_behavior_probe.py](modules/academic-research-suite/ars/scripts/test_indirect_prompt_injection_behavior_probe.py) — GUIDANCE_BLOCK = (
- [ars/scripts/test_inquiry_branch_ledger.py](modules/academic-research-suite/ars/scripts/test_inquiry_branch_ledger.py) — Hermetic contract/replay/storage tests for inquiry-branch-ledger/1.0 (#743).
- [ars/scripts/test_migrate_literature_corpus_to_v3_10.py](modules/academic-research-suite/ars/scripts/test_migrate_literature_corpus_to_v3_10.py) — Tests for the #127 v3.10 terminal-policy-layer seed migration tool. Pure local YAML transform — NO API client / mock (codex consult 2026-05-31 Q3: carrying the v3.9.0 client fixtur
- [ars/scripts/test_migrate_literature_corpus_to_v3_7_3.py](modules/academic-research-suite/ars/scripts/test_migrate_literature_corpus_to_v3_7_3.py) — #105 v3.7.3 contamination_signals backfill migration tool tests. Tests scripts/migrate_literature_corpus_to_v3_7_3.py — the CLI that backfills `contamination_signals` on pre-v3.7.3
- [ars/scripts/test_migrate_literature_corpus_to_v3_9_0.py](modules/academic-research-suite/ars/scripts/test_migrate_literature_corpus_to_v3_9_0.py) — #102 v3.9.0 cross-index triangulation backfill migration tool tests. Tests scripts/migrate_literature_corpus_to_v3_9_0.py — the CLI that backfills `openalex_unmatched` and `crossre
- [ars/scripts/test_normalize_compat_verdict.py](modules/academic-research-suite/ars/scripts/test_normalize_compat_verdict.py) — Tier-1 behavioral guard for the OpenAI-compatible verdict normalization (#453). The security invariant: an ungrounded compatible provider can never launder a positive VERIFIED into
- [ars/scripts/test_openalex_client.py](modules/academic-research-suite/ars/scripts/test_openalex_client.py) — Tests for OpenAlex client per deep-research/references/openalex_api_protocol.md.
- [ars/scripts/test_output_language_pair.py](modules/academic-research-suite/ars/scripts/test_output_language_pair.py) — Unit tests for the #862 Phase-1 output-language-pair contract helpers. The helpers under test live in `scripts/check_spec_consistency.py`; the registry itself lives in `shared/outp
- [ars/scripts/test_passport_yaml.py](modules/academic-research-suite/ars/scripts/test_passport_yaml.py) — Tests for `scripts/_passport_yaml.py` — shared ruamel.yaml round-trip configuration extracted from `migrate_literature_corpus_to_v3_7_3.py` and `migrate_literature_corpus_to_v3_9_0
- [ars/scripts/test_pattern_eval_runtime.py](modules/academic-research-suite/ars/scripts/test_pattern_eval_runtime.py) — Test harness for ARS v3.6.7 Step 8 pattern-eval fixtures. Spec: docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md §7.4 This harness exercises §5.6 Path B's verdic
- [ars/scripts/test_pdf_read_preflight.py](modules/academic-research-suite/ars/scripts/test_pdf_read_preflight.py) — Tests for scripts/pdf_read_preflight.py (#512 PDF read-integrity preflight). Fixtures are synthetic PDFs assembled in-test with correct xref offsets (no binary fixture files): a fl
- [ars/scripts/test_phase_e_cited_version.py](modules/academic-research-suite/ars/scripts/test_phase_e_cited_version.py) — #1006 fixture: Phase E rows for a cited published version. The manuscript cites the published version of an article. Only a working-paper version of the same work is readable, and 
- [ars/scripts/test_policy_anchor_disclosure.py](modules/academic-research-suite/ars/scripts/test_policy_anchor_disclosure.py) — #108 policy-anchor disclosure renderer conformance tests. Reference impl: scripts/policy_anchor_disclosure_referee.py The referee is an executable specification of the disclosure d
- [ars/scripts/test_reading_probe_lint.py](modules/academic-research-suite/ars/scripts/test_reading_probe_lint.py) — Lint tests for the v3.5.1 opt-in Socratic reading-check probe. Target spec: docs/design/2026-04-22-ars-v3.7.3-reading-check-probe-design.md §5.1. These are file-content lints (grep
- [ars/scripts/test_recompute_receipts.py](modules/academic-research-suite/ars/scripts/test_recompute_receipts.py) — Tests for the #610 step-5 deterministic arithmetic-receipt calculator. Three families: (1) distribution-tail accuracy pinned against published critical values and cross-family iden
- [ars/scripts/test_render_claim_standing_view.py](modules/academic-research-suite/ars/scripts/test_render_claim_standing_view.py) — _rehash_input,
- [ars/scripts/test_render_eval_comment.py](modules/academic-research-suite/ars/scripts/test_render_eval_comment.py) — Tests for scripts/render_eval_comment.py (eval-harness PR comment renderer). Display layer only: these tests pin the comment SHAPE (verdict line, table rows, folded raw JSON). The 
- [ars/scripts/test_render_harness_retirement_issue.py](modules/academic-research-suite/ars/scripts/test_render_harness_retirement_issue.py) — Tests for the manifest-backed harness-retirement issue renderer (#617).
- [ars/scripts/test_repro_lock_validation_drift.py](modules/academic-research-suite/ars/scripts/test_repro_lock_validation_drift.py) — Drift guard: the nested repro_lock sub-shape in experiment_provenance_entry.schema.json MUST stay in sync with the canonical field set in scripts/repro_lock_validation.py (#260 D1 
- [ars/scripts/test_research_workflow_profile.py](modules/academic-research-suite/ars/scripts/test_research_workflow_profile.py) — Contract, fallback, selection, and correction tests for issue #742.
- [ars/scripts/test_resolve_human_subjects_authority.py](modules/academic-research-suite/ars/scripts/test_resolve_human_subjects_authority.py) — Hermetic contract, resolver, and mutation tests for issue #666.
- [ars/scripts/test_resolve_review_target_context.py](modules/academic-research-suite/ars/scripts/test_resolve_review_target_context.py) — Contract, resolver, digest, and blind-boundary tests for issue #683.
- [ars/scripts/test_resume_e4_record.py](modules/academic-research-suite/ars/scripts/test_resume_e4_record.py) — Fail-closed recovery tests for #616 resume-from-bundle.
- [ars/scripts/test_retraction_status.py](modules/academic-research-suite/ars/scripts/test_retraction_status.py) — Hermetic acceptance matrix for #651 retraction status.
- [ars/scripts/test_review_criteria_binding.py](modules/academic-research-suite/ars/scripts/test_review_criteria_binding.py) — REPO = Path(__file__).resolve().parents[1]
- [ars/scripts/test_review_panel_provenance.py](modules/academic-research-suite/ars/scripts/test_review_panel_provenance.py) — Contract and replay tests for typed review-panel provenance.
- [ars/scripts/test_review_pathway_rule_trace.py](modules/academic-research-suite/ars/scripts/test_review_pathway_rule_trace.py) — ContractError,
- [ars/scripts/test_revision_roadmap.py](modules/academic-research-suite/ars/scripts/test_revision_roadmap.py) — Hermetic mutation tests for the #670 non-ranking revision contract.
- [ars/scripts/test_run_ci_pytest_manifest.py](modules/academic-research-suite/ars/scripts/test_run_ci_pytest_manifest.py) — Unit tests for scripts/run_ci_pytest_manifest.py (issue #156). The runner reads scripts/_ci_pytest_manifest.toml and invokes pytest for each entry. Behavior contract: - runs `pytho
- [ars/scripts/test_run_codex_audit_e2e.py](modules/academic-research-suite/ars/scripts/test_run_codex_audit_e2e.py) — End-to-end dispatch test for scripts/run_codex_audit.sh (Phase 6.1 deferred gate). Spec: docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md §4.1 (Bash 4+ guard) + 
- [ars/scripts/test_run_evals.py](modules/academic-research-suite/ars/scripts/test_run_evals.py) — Tests for scripts/run_evals.py (#184 Delta 2, Phase 1b harness).
- [ars/scripts/test_run_guard_launcher.py](modules/academic-research-suite/ars/scripts/test_run_guard_launcher.py) — Launch-layer tests for hooks/run_guard.sh (#454 Windows Python hook portability). The existing test_ars_write_scope_guard.py drives the guard via [sys.executable, guard] — it never
- [ars/scripts/test_run_ideation_diversity_no_call.py](modules/academic-research-suite/ars/scripts/test_run_ideation_diversity_no_call.py) — ROOT = Path(__file__).resolve().parent.parent
- [ars/scripts/test_run_indirect_prompt_injection_no_call.py](modules/academic-research-suite/ars/scripts/test_run_indirect_prompt_injection_no_call.py) — MODULE_PATH = Path(runner.__file__)
- [ars/scripts/test_run_ledger.py](modules/academic-research-suite/ars/scripts/test_run_ledger.py) — Tests for scripts/run_ledger.py (#887). Design: docs/design/2026-09-23-887-handoff-integrity-design.md. The six scenarios in HandoffScenarioTest are the deterministic fixture that 
- [ars/scripts/test_run_review_criteria_constructive_value.py](modules/academic-research-suite/ars/scripts/test_run_review_criteria_constructive_value.py) — Hermetic runner, blinding, and human-label tests for #684.
- [ars/scripts/test_run_role_topology_utility_dry_run.py](modules/academic-research-suite/ars/scripts/test_run_role_topology_utility_dry_run.py) — ROOT = Path(__file__).resolve().parents[1]
- [ars/scripts/test_score_calibration_run.py](modules/academic-research-suite/ars/scripts/test_score_calibration_run.py) — Mutation tests for score_calibration_run.py (#653). Synthetic runs, offline.
- [ars/scripts/test_score_review_criteria_constructive_value.py](modules/academic-research-suite/ars/scripts/test_score_review_criteria_constructive_value.py) — REPO = Path(__file__).resolve().parents[1]
- [ars/scripts/test_semantic_scholar_client.py](modules/academic-research-suite/ars/scripts/test_semantic_scholar_client.py) — Tests for the minimal Semantic Scholar client backing #105 CLI. Mocks urllib at the transport layer (no real network). Verifies the client honors the protocol's DOI-first + title-s
- [ars/scripts/test_skill_lint_marker_block.py](modules/academic-research-suite/ars/scripts/test_skill_lint_marker_block.py) — Tests for the shared marker-block sync helpers in _skill_lint.py (#923). check_routing_core_sync, check_method_weaknesses_sync, and check_review_form_note_sync all call these helpe
- [ars/scripts/test_slr_lineage_emission.py](modules/academic-research-suite/ars/scripts/test_slr_lineage_emission.py) — #111 slr_lineage emission conformance tests. Tests the pipeline plumbing that lets `disclosure --policy-anchor=prisma-trAIce` dispatch automatically after `deep-research systematic
- [ars/scripts/test_socratic_rq_non_generation_contract.py](modules/academic-research-suite/ars/scripts/test_socratic_rq_non_generation_contract.py) — Contract tests for Socratic research-question authorship boundaries. These are file-content tests: they pin the default non-generation fallback and the visible transition required 
- [ars/scripts/test_sr_screener_pipeline.py](modules/academic-research-suite/ars/scripts/test_sr_screener_pipeline.py) — End-to-end regression test for the sr-screener scripts on synthetic records. Runs the skill's own scripts (sr-screener/scripts/) as a user would: parse and de-duplicate exports, ge
- [ars/scripts/test_standing_constraint_entry_schema.py](modules/academic-research-suite/ars/scripts/test_standing_constraint_entry_schema.py) — Schema tests for Material Passport standing_constraints[] entries (#927).
- [ars/scripts/test_temporal_integrity_audit.py](modules/academic-research-suite/ars/scripts/test_temporal_integrity_audit.py) — Tests for v3.9.4 temporal_integrity_audit.py 5-pass verifier.
- [ars/scripts/test_text_similarity.py](modules/academic-research-suite/ars/scripts/test_text_similarity.py) — Tests for `scripts/_text_similarity.py` — shared title-similarity helpers extracted from `semantic_scholar_client.py` / `openalex_client.py` / `crossref_client.py` to prevent sibli
- [ars/scripts/test_title_fuzzy_false_positive.py](modules/academic-research-suite/ars/scripts/test_title_fuzzy_false_positive.py) — Resolver-boundary pin for #250 / #430 / #431 — distinct-work rejection. #250 recorded a regression the citation-extraction gold set cannot catch: a resolver's title fallback *accid
- [ars/scripts/test_tortured_phrase_screening.py](modules/academic-research-suite/ars/scripts/test_tortured_phrase_screening.py) — Hermetic conformance and mutation tests for issue #660.
- [ars/scripts/test_transport_fixture_citation_gate.py](modules/academic-research-suite/ars/scripts/test_transport_fixture_citation_gate.py) — #511 Part B — hermetic transport-fixture integration test for the citation gate. The four per-client unit suites mock at the transport boundary one client at a time, and the citati
- [ars/scripts/test_uncited_assertion.py](modules/academic-research-suite/ars/scripts/test_uncited_assertion.py) — D4-c uncited-assertion token-detector tests (T-U1..T-U5). Per spec §7.4 in docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md. Spec §7 names the file `tests/test_uncite
- [ars/scripts/test_v3_6_7_phase_6_6.py](modules/academic-research-suite/ars/scripts/test_v3_6_7_phase_6_6.py) — Static checks for ARS v3.6.7 Step 6 Phase 6.6 — orchestrator prompt §3.5 Audit Artifact Gate subsection. Spec: docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md I
- [ars/scripts/test_validate_compliance_fixtures.py](modules/academic-research-suite/ars/scripts/test_validate_compliance_fixtures.py) — Unit tests for validate_compliance_fixtures.py.
- [ars/scripts/test_validate_ideation_diversity_assets.py](modules/academic-research-suite/ars/scripts/test_validate_ideation_diversity_assets.py) — ROOT = Path(__file__).resolve().parent.parent
- [ars/scripts/test_venue_disclosure_contract.py](modules/academic-research-suite/ars/scripts/test_venue_disclosure_contract.py) — Deterministic venue-track contract coverage for issue #615.
- [ars/scripts/test_verification_cache.py](modules/academic-research-suite/ars/scripts/test_verification_cache.py) — Tests for the persistent verification cache (Delta 2). Spec: docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md §2 Delta 2. The cache is a local SQLite-backed store key
- [ars/scripts/test_verification_gate.py](modules/academic-research-suite/ars/scripts/test_verification_gate.py) — Tests for the verification_gate API (Delta 5). Spec: docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md §2 Delta 5. verify_citation composes the four resolvers, maps ea
- [ars/scripts/test_verify_panel_recommendations.py](modules/academic-research-suite/ars/scripts/test_verify_panel_recommendations.py) — Tests for scripts/verify_panel_recommendations.py (#1001). Resolver clients are MagicMocks, so no test makes a network call. Reports are synthetic text written to tmp_path.
- [ars/scripts/test_verify_passport_cli.py](modules/academic-research-suite/ars/scripts/test_verify_passport_cli.py) — Tests for the verify_passport CLI (Delta 5 ad-hoc entry point). Spec: docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md §2 Delta 5 (`python -m scripts.verify_passport 
- [ars/scripts/test_verify_submission_package.py](modules/academic-research-suite/ars/scripts/test_verify_submission_package.py) — Tests for verify_submission_package — #394 Slice 1 (CLI skeleton + Family C). Spec: docs/design/2026-06-10-394-submission-package-verifier-spec.md §3.3 / §5.1 / §7.3 / §8. Mutation
- [ars/scripts/test_version_records_schema.py](modules/academic-research-suite/ars/scripts/test_version_records_schema.py) — Tests for Kong #258 version_records sidecar schema.
- [ars/scripts/tortured_phrase_screening.py](modules/academic-research-suite/ars/scripts/tortured_phrase_screening.py) — Hermetic tortured-phrase risk-marker screening for issue #660. The runtime consumes only explicitly named local inputs. It never downloads a phrase list, dereferences a corpus poin
- [ars/scripts/uncited_assertion_detector.py](modules/academic-research-suite/ars/scripts/uncited_assertion_detector.py) — D4-c uncited-assertion token-rule detector. Implements the three-condition rule pinned in `academic-pipeline/agents/claim_ref_alignment_audit_agent.md` §"Uncited-assertion detector
- [ars/scripts/validate_claim_standing_stance_assets.py](modules/academic-research-suite/ars/scripts/validate_claim_standing_stance_assets.py) — Offline validator for the #655 claim-standing stance seed set. Validates `evals/heldout/claim_standing_probe/heldout_stance_set.json` against its closed schema and the structural i
- [ars/scripts/validate_compliance_fixtures.py](modules/academic-research-suite/ars/scripts/validate_compliance_fixtures.py) — Validate all compliance_report YAML fixtures against Schema 12. Loads each examples/compliance/fixture_*.yaml in-process and runs it through scripts.check_compliance_report.validat
- [ars/scripts/validate_ideation_diversity_assets.py](modules/academic-research-suite/ars/scripts/validate_ideation_diversity_assets.py) — Offline validator for the #659 Phase-1 design and synthetic role seed. This CLI has no subject, actor, judge, provider, or network transport. It may materialize the frozen non-prod
- [ars/scripts/venue_disclosure_contract_harness.py](modules/academic-research-suite/ars/scripts/venue_disclosure_contract_harness.py) — Deterministic test oracle for the venue disclosure contract. This module exists only to exercise the documentation-owned contract in CI. It is deliberately not imported by the disc
- [ars/scripts/verification_cache.py](modules/academic-research-suite/ars/scripts/verification_cache.py) — Persistent verification cache for the bibliographic resolvers (Delta 2). A local SQLite-backed cache so the same paper cited across multiple drafts does not re-hit Crossref / OpenA
- [ars/scripts/verification_gate/__init__.py](modules/academic-research-suite/ars/scripts/verification_gate/__init__.py) — verification_gate — citation existence verification API (Delta 5). Public functions: - verify_citation(entry, clients, *, ref_slug, anchor=None, cache=None) -> CitationVerification
- [ars/scripts/verify_panel_recommendations.py](modules/academic-research-suite/ars/scripts/verify_panel_recommendations.py) — Check the references a review panel suggests (#1001). Reads saved reviewer reports and never changes them. No model call. Domain Reviewer (R2) and Perspective Reviewer (R3) list ea
- [ars/scripts/verify_passport.py](modules/academic-research-suite/ars/scripts/verify_passport.py) — verify_passport CLI — ad-hoc citation existence verification (Delta 5). python -m scripts.verify_passport <passport.yaml> Loads a Material Passport YAML, runs verification_gate.ver
- [ars/scripts/verify_submission_package.py](modules/academic-research-suite/ars/scripts/verify_submission_package.py) — verify_submission_package CLI — deterministic submission-package verifier (#394; slices 1-2 shipped: Family C reference integrity + Family B venue limits). python scripts/verify_su
- [ars/sr-screener/scripts/build_outputs.py](modules/academic-research-suite/ars/sr-screener/scripts/build_outputs.py) — Phase 6 (Reporter): build the screening deliverables from merged decisions. Usage: python build_outputs.py --work W --out OUT_DIR [--stage ta|ft] [--config screening_config.json] [
- [ars/sr-screener/scripts/build_workflow.py](modules/academic-research-suite/ars/sr-screener/scripts/build_workflow.py) — Generate a ready-to-run Workflow script (or plain prompt files) for a screening run. Usage: python build_workflow.py ta --work W --protocol screening_protocol.md --config screening
- [ars/sr-screener/scripts/merge_decisions.py](modules/academic-research-suite/ars/sr-screener/scripts/merge_decisions.py) — Merge reviewer decisions into final screening decisions and list what is still pending. Usage: python merge_decisions.py --work W --from PATH [PATH ...] [--config screening_config.
- [ars/sr-screener/scripts/prepare_fulltext.py](modules/academic-research-suite/ars/sr-screener/scripts/prepare_fulltext.py) — Full-text stage, step 1: match the PDFs of advanced records. Usage: python prepare_fulltext.py --work W --pdf-dir PDFS [--config screening_config.json] [--map map.csv] Takes every 
- [ars/sr-screener/scripts/prepare_records.py](modules/academic-research-suite/ars/sr-screener/scripts/prepare_records.py) — Phase 1 (Records Librarian): parse exports, remove duplicates, write screening batches. Usage: python prepare_records.py --inputs EXPORTS_DIR_OR_FILES... --work WORK_DIR [--config 
- [ars/sr-screener/scripts/srlib.py](modules/academic-research-suite/ars/sr-screener/scripts/srlib.py) — Shared helpers for the sr-screener scripts (Python 3.9+, standard library only). Covers: reading bibliographic exports (RIS, PubMed/MEDLINE .nbib, Web of Science plain text, CSV), 
- [ars/sr-screener/templates/workflows/ft_screening.template.js](modules/academic-research-suite/ars/sr-screener/templates/workflows/ft_screening.template.js) — export const meta = {
- [ars/sr-screener/templates/workflows/ta_screening.template.js](modules/academic-research-suite/ars/sr-screener/templates/workflows/ta_screening.template.js) — export const meta = {
- [ars/tools/release-discipline/scripts/_release_doc_alignment_schema.py](modules/academic-research-suite/ars/tools/release-discipline/scripts/_release_doc_alignment_schema.py) — Manifest schema loading and validation. Cross-repo agnostic per INVARIANT 12. No domain assumptions, no language literals (INVARIANT 3, 20). Pure schema + path safety logic; no net
- [ars/tools/release-discipline/scripts/check_command_invariants.py](modules/academic-research-suite/ars/tools/release-discipline/scripts/check_command_invariants.py) — Validate command-list invariants per a per-repo manifest TOML. A repo that packages a set of commands (one definition file per command, discovered by glob) often also maintains han
- [ars/tools/release-discipline/scripts/check_release_doc_alignment.py](modules/academic-research-suite/ars/tools/release-discipline/scripts/check_release_doc_alignment.py) — Validate release-doc alignment per a per-repo manifest TOML. Cross-repo agnostic per INVARIANT 12. See docs/design/2026-05-21-manifest-validator-spec.md for the full design (in the
- [ars/tools/release-discipline/scripts/sync-toolkit.sh](modules/academic-research-suite/ars/tools/release-discipline/scripts/sync-toolkit.sh) — release-discipline-toolkit vendoring helper. v0.3.2: --version <V>; vendors
- [codex/scripts/ars_codex_full_runtime.py](modules/academic-research-suite/codex/scripts/ars_codex_full_runtime.py) — Codex full-runtime planner for the Academic Research Suite adapter. The planner is intentionally deterministic and side-effect free. It does not switch models, spawn agents, or exe
- [codex/scripts/ars_codex_hook.py](modules/academic-research-suite/codex/scripts/ars_codex_hook.py) — Safe Codex hook wrapper for ARS. The wrapper is read-only by design. It prints adapter metadata and does not inspect environment variables, network, shell history, or user files.
- [codex/scripts/ars_codex_quality_gates.py](modules/academic-research-suite/codex/scripts/ars_codex_quality_gates.py) — Static quality gates for the ARS-Codex full-runtime adapter.
- [codex/scripts/ars_codex_topology_experiment.py](modules/academic-research-suite/codex/scripts/ars_codex_topology_experiment.py) — Freeze, execute, and validate the exploratory issue #37 topology pilot. The runner materializes only each task's allowlisted input bundle in a temporary directory. Held-out labels 
- [codex/tests/test_full_runtime_adapter.py](modules/academic-research-suite/codex/tests/test_full_runtime_adapter.py) — CODEX_ROOT = Path(__file__).resolve().parents[1]
- [codex/tests/test_hook_wrapper.py](modules/academic-research-suite/codex/tests/test_hook_wrapper.py) — CODEX_ROOT = Path(__file__).resolve().parents[1]
- [codex/tests/test_indirect_prompt_manifest_fallback.py](modules/academic-research-suite/codex/tests/test_indirect_prompt_manifest_fallback.py) — SUITE_ROOT = Path(__file__).resolve().parents[2]
- [codex/tests/test_model_runtime_policy.py](modules/academic-research-suite/codex/tests/test_model_runtime_policy.py) — Model-selection boundaries: recommendation, override, and observed execution.
- [codex/tests/test_reviewer_seat_coverage.py](modules/academic-research-suite/codex/tests/test_reviewer_seat_coverage.py) — Full reviewer coverage cannot pass after a functional seat is omitted.
- [codex/tests/test_topology_experiment.py](modules/academic-research-suite/codex/tests/test_topology_experiment.py) — CODEX_ROOT = Path(__file__).resolve().parents[1]
- [codex/tests/test_v3_22_2_packaging.py](modules/academic-research-suite/codex/tests/test_v3_22_2_packaging.py) — The Codex loader carries the 3.22.2 routing core and description contract.
- [codex/tests/test_v3_22_2_routing.py](modules/academic-research-suite/codex/tests/test_v3_22_2_routing.py) — Codex boundaries for the v3.22.2 routing and caller contracts. These tests exercise deterministic planning and prompt packaging, not live model compliance with the workflow instruc
- [codex/tests/test_v3_22_alignment.py](modules/academic-research-suite/codex/tests/test_v3_22_alignment.py) — Release parity and Spanish routing boundaries introduced in ARS 3.22.
- [codex/tests/test_v3_23_1_patch.py](modules/academic-research-suite/codex/tests/test_v3_23_1_patch.py) — ARS 3.23.1 import behavior and Codex/provider execution boundaries.
- [codex/tests/test_v3_23_screening.py](modules/academic-research-suite/codex/tests/test_v3_23_screening.py) — Explicit screening activation and Codex execution boundaries for ARS 3.23.
- [codex/tests/test_v3_24_0_patch.py](modules/academic-research-suite/codex/tests/test_v3_24_0_patch.py) — ARS 3.24.0 review-letter attachments and Codex execution boundaries.

### 参考

- [ars/.github/copilot-instructions.md](modules/academic-research-suite/ars/.github/copilot-instructions.md)
- [ars/.github/pull_request_template.md](modules/academic-research-suite/ars/.github/pull_request_template.md)
- [ars/academic-paper/agents/abstract_bilingual_agent.md](modules/academic-research-suite/ars/academic-paper/agents/abstract_bilingual_agent.md)
- [ars/academic-paper/agents/argument_builder_agent.md](modules/academic-research-suite/ars/academic-paper/agents/argument_builder_agent.md)
- [ars/academic-paper/agents/citation_compliance_agent.md](modules/academic-research-suite/ars/academic-paper/agents/citation_compliance_agent.md)
- [ars/academic-paper/agents/draft_writer_agent.md](modules/academic-research-suite/ars/academic-paper/agents/draft_writer_agent.md)
- [ars/academic-paper/agents/formatter_agent.md](modules/academic-research-suite/ars/academic-paper/agents/formatter_agent.md)
- [ars/academic-paper/agents/intake_agent.md](modules/academic-research-suite/ars/academic-paper/agents/intake_agent.md)
- [ars/academic-paper/agents/literature_strategist_agent.md](modules/academic-research-suite/ars/academic-paper/agents/literature_strategist_agent.md)
- [ars/academic-paper/agents/peer_reviewer_agent.md](modules/academic-research-suite/ars/academic-paper/agents/peer_reviewer_agent.md)
- [ars/academic-paper/agents/revision_coach_agent.md](modules/academic-research-suite/ars/academic-paper/agents/revision_coach_agent.md)
- [ars/academic-paper/agents/socratic_mentor_agent.md](modules/academic-research-suite/ars/academic-paper/agents/socratic_mentor_agent.md)
- [ars/academic-paper/agents/structure_architect_agent.md](modules/academic-research-suite/ars/academic-paper/agents/structure_architect_agent.md)
- [ars/academic-paper/agents/visualization_agent.md](modules/academic-research-suite/ars/academic-paper/agents/visualization_agent.md)
- [ars/academic-paper/examples/chinese_paper_example.md](modules/academic-research-suite/ars/academic-paper/examples/chinese_paper_example.md)
- [ars/academic-paper/examples/clinical_citation_verification_checklist.md](modules/academic-research-suite/ars/academic-paper/examples/clinical_citation_verification_checklist.md)
- [ars/academic-paper/examples/clinical_epistemic_status_example.md](modules/academic-research-suite/ars/academic-paper/examples/clinical_epistemic_status_example.md)
- [ars/academic-paper/examples/commitment_ledger_example.md](modules/academic-research-suite/ars/academic-paper/examples/commitment_ledger_example.md)
- [ars/academic-paper/examples/imrad_hei_example.md](modules/academic-research-suite/ars/academic-paper/examples/imrad_hei_example.md)
- [ars/academic-paper/examples/literature_review_example.md](modules/academic-research-suite/ars/academic-paper/examples/literature_review_example.md)
- [ars/academic-paper/examples/plan_mode_guided_writing.md](modules/academic-research-suite/ars/academic-paper/examples/plan_mode_guided_writing.md)
- [ars/academic-paper/examples/revision_mode_example.md](modules/academic-research-suite/ars/academic-paper/examples/revision_mode_example.md)
- [ars/academic-paper/examples/revision_recovery_example.md](modules/academic-research-suite/ars/academic-paper/examples/revision_recovery_example.md)
- [ars/academic-paper/examples/version_family_reconciliation_example.md](modules/academic-research-suite/ars/academic-paper/examples/version_family_reconciliation_example.md)
- [ars/academic-paper/references/abstract_writing_guide.md](modules/academic-research-suite/ars/academic-paper/references/abstract_writing_guide.md)
- [ars/academic-paper/references/academic_writing_style.md](modules/academic-research-suite/ars/academic-paper/references/academic_writing_style.md)
- [ars/academic-paper/references/anti_leakage_protocol.md](modules/academic-research-suite/ars/academic-paper/references/anti_leakage_protocol.md)
- [ars/academic-paper/references/apa7_chinese_citation_guide.md](modules/academic-research-suite/ars/academic-paper/references/apa7_chinese_citation_guide.md)
- [ars/academic-paper/references/apa7_extended_guide.md](modules/academic-research-suite/ars/academic-paper/references/apa7_extended_guide.md)
- [ars/academic-paper/references/changelog.md](modules/academic-research-suite/ars/academic-paper/references/changelog.md)
- [ars/academic-paper/references/citation_format_switcher.md](modules/academic-research-suite/ars/academic-paper/references/citation_format_switcher.md)
- [ars/academic-paper/references/committee_correspondence_protocol.md](modules/academic-research-suite/ars/academic-paper/references/committee_correspondence_protocol.md)
- [ars/academic-paper/references/credit_authorship_guide.md](modules/academic-research-suite/ars/academic-paper/references/credit_authorship_guide.md)
- [ars/academic-paper/references/disclosure_mode_protocol.md](modules/academic-research-suite/ars/academic-paper/references/disclosure_mode_protocol.md)
- [ars/academic-paper/references/domain_evidence_profiles.md](modules/academic-research-suite/ars/academic-paper/references/domain_evidence_profiles.md)
- [ars/academic-paper/references/failure_paths.md](modules/academic-research-suite/ars/academic-paper/references/failure_paths.md)
- [ars/academic-paper/references/funding_statement_guide.md](modules/academic-research-suite/ars/academic-paper/references/funding_statement_guide.md)
- [ars/academic-paper/references/hei_domain_glossary.md](modules/academic-research-suite/ars/academic-paper/references/hei_domain_glossary.md)
- [ars/academic-paper/references/intro_title_rhetoric_guide.md](modules/academic-research-suite/ars/academic-paper/references/intro_title_rhetoric_guide.md)
- [ars/academic-paper/references/journal_submission_guide.md](modules/academic-research-suite/ars/academic-paper/references/journal_submission_guide.md)
- [ars/academic-paper/references/latex_template_reference.md](modules/academic-research-suite/ars/academic-paper/references/latex_template_reference.md)
- [ars/academic-paper/references/mode_selection_guide.md](modules/academic-research-suite/ars/academic-paper/references/mode_selection_guide.md)
- [ars/academic-paper/references/paper_structure_patterns.md](modules/academic-research-suite/ars/academic-paper/references/paper_structure_patterns.md)
- [ars/academic-paper/references/plan_mode_protocol.md](modules/academic-research-suite/ars/academic-paper/references/plan_mode_protocol.md)
- [ars/academic-paper/references/policy_anchor_disclosure_protocol.md](modules/academic-research-suite/ars/academic-paper/references/policy_anchor_disclosure_protocol.md)
- [ars/academic-paper/references/policy_anchor_table.md](modules/academic-research-suite/ars/academic-paper/references/policy_anchor_table.md)
- [ars/academic-paper/references/revision_patch_protocol.md](modules/academic-research-suite/ars/academic-paper/references/revision_patch_protocol.md)
- [ars/academic-paper/references/statistical_visualization_standards.md](modules/academic-research-suite/ars/academic-paper/references/statistical_visualization_standards.md)
- [ars/academic-paper/references/venue_disclosure_policies.md](modules/academic-research-suite/ars/academic-paper/references/venue_disclosure_policies.md)
- [ars/academic-paper/references/vlm_figure_verification.md](modules/academic-research-suite/ars/academic-paper/references/vlm_figure_verification.md)
- [ars/academic-paper/references/workflow_phase_details.md](modules/academic-research-suite/ars/academic-paper/references/workflow_phase_details.md)
- [ars/academic-paper/references/writing_judgment_framework.md](modules/academic-research-suite/ars/academic-paper/references/writing_judgment_framework.md)
- [ars/academic-paper/references/writing_quality_check.md](modules/academic-research-suite/ars/academic-paper/references/writing_quality_check.md)
- [ars/academic-paper/templates/bilingual_abstract_template.md](modules/academic-research-suite/ars/academic-paper/templates/bilingual_abstract_template.md)
- [ars/academic-paper/templates/case_study_template.md](modules/academic-research-suite/ars/academic-paper/templates/case_study_template.md)
- [ars/academic-paper/templates/conference_paper_template.md](modules/academic-research-suite/ars/academic-paper/templates/conference_paper_template.md)
- [ars/academic-paper/templates/credit_statement_template.md](modules/academic-research-suite/ars/academic-paper/templates/credit_statement_template.md)
- [ars/academic-paper/templates/funding_statement_template.md](modules/academic-research-suite/ars/academic-paper/templates/funding_statement_template.md)
- [ars/academic-paper/templates/imrad_template.md](modules/academic-research-suite/ars/academic-paper/templates/imrad_template.md)
- [ars/academic-paper/templates/literature_review_template.md](modules/academic-research-suite/ars/academic-paper/templates/literature_review_template.md)
- [ars/academic-paper/templates/policy_brief_template.md](modules/academic-research-suite/ars/academic-paper/templates/policy_brief_template.md)
- [ars/academic-paper/templates/revision_tracking_template.md](modules/academic-research-suite/ars/academic-paper/templates/revision_tracking_template.md)
- [ars/academic-paper/templates/theoretical_paper_template.md](modules/academic-research-suite/ars/academic-paper/templates/theoretical_paper_template.md)
- [ars/academic-paper-reviewer/agents/devils_advocate_reviewer_agent.md](modules/academic-research-suite/ars/academic-paper-reviewer/agents/devils_advocate_reviewer_agent.md)
- [ars/academic-paper-reviewer/agents/domain_reviewer_agent.md](modules/academic-research-suite/ars/academic-paper-reviewer/agents/domain_reviewer_agent.md)
- [ars/academic-paper-reviewer/agents/editorial_synthesizer_agent.md](modules/academic-research-suite/ars/academic-paper-reviewer/agents/editorial_synthesizer_agent.md)
- [ars/academic-paper-reviewer/agents/eic_agent.md](modules/academic-research-suite/ars/academic-paper-reviewer/agents/eic_agent.md)
- [ars/academic-paper-reviewer/agents/field_analyst_agent.md](modules/academic-research-suite/ars/academic-paper-reviewer/agents/field_analyst_agent.md)
- [ars/academic-paper-reviewer/agents/methodology_reviewer_agent.md](modules/academic-research-suite/ars/academic-paper-reviewer/agents/methodology_reviewer_agent.md)
- [ars/academic-paper-reviewer/agents/perspective_reviewer_agent.md](modules/academic-research-suite/ars/academic-paper-reviewer/agents/perspective_reviewer_agent.md)
- [ars/academic-paper-reviewer/examples/hei_paper_review_example.md](modules/academic-research-suite/ars/academic-paper-reviewer/examples/hei_paper_review_example.md)
- [ars/academic-paper-reviewer/examples/interdisciplinary_review_example.md](modules/academic-research-suite/ars/academic-paper-reviewer/examples/interdisciplinary_review_example.md)
- [ars/academic-paper-reviewer/examples/subclaim_decomposition_example.md](modules/academic-research-suite/ars/academic-paper-reviewer/examples/subclaim_decomposition_example.md)
- [ars/academic-paper-reviewer/references/calibration_mode_protocol.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/calibration_mode_protocol.md)
- [ars/academic-paper-reviewer/references/changelog.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/changelog.md)
- [ars/academic-paper-reviewer/references/editorial_decision_standards.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/editorial_decision_standards.md)
- [ars/academic-paper-reviewer/references/guided_mode_protocol.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/guided_mode_protocol.md)
- [ars/academic-paper-reviewer/references/integration_guide.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/integration_guide.md)
- [ars/academic-paper-reviewer/references/quality_rubrics.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/quality_rubrics.md)
- [ars/academic-paper-reviewer/references/re_review_mode_protocol.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/re_review_mode_protocol.md)
- [ars/academic-paper-reviewer/references/review_criteria_framework.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/review_criteria_framework.md)
- [ars/academic-paper-reviewer/references/review_panel_provenance_protocol.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/review_panel_provenance_protocol.md)
- [ars/academic-paper-reviewer/references/review_quality_thinking.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/review_quality_thinking.md)
- [ars/academic-paper-reviewer/references/reviewer_sprint_prompt_source.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/reviewer_sprint_prompt_source.md)
- [ars/academic-paper-reviewer/references/sprint_contract_protocol.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/sprint_contract_protocol.md)
- [ars/academic-paper-reviewer/references/statistical_reporting_standards.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/statistical_reporting_standards.md)
- [ars/academic-paper-reviewer/references/top_journals_by_field.md](modules/academic-research-suite/ars/academic-paper-reviewer/references/top_journals_by_field.md)
- [ars/academic-paper-reviewer/templates/editorial_decision_template.md](modules/academic-research-suite/ars/academic-paper-reviewer/templates/editorial_decision_template.md)
- [ars/academic-paper-reviewer/templates/peer_review_report_template.md](modules/academic-research-suite/ars/academic-paper-reviewer/templates/peer_review_report_template.md)
- [ars/academic-paper-reviewer/templates/revision_response_template.md](modules/academic-research-suite/ars/academic-paper-reviewer/templates/revision_response_template.md)
- [ars/academic-pipeline/agents/claim_ref_alignment_audit_agent.md](modules/academic-research-suite/ars/academic-pipeline/agents/claim_ref_alignment_audit_agent.md)
- [ars/academic-pipeline/agents/collaboration_depth_agent.md](modules/academic-research-suite/ars/academic-pipeline/agents/collaboration_depth_agent.md)
- [ars/academic-pipeline/agents/integrity_verification_agent.md](modules/academic-research-suite/ars/academic-pipeline/agents/integrity_verification_agent.md)
- [ars/academic-pipeline/agents/pipeline_orchestrator_agent.md](modules/academic-research-suite/ars/academic-pipeline/agents/pipeline_orchestrator_agent.md)
- [ars/academic-pipeline/agents/state_tracker_agent.md](modules/academic-research-suite/ars/academic-pipeline/agents/state_tracker_agent.md)
- [ars/academic-pipeline/examples/full_pipeline_example.md](modules/academic-research-suite/ars/academic-pipeline/examples/full_pipeline_example.md)
- [ars/academic-pipeline/examples/integrity_failure_recovery.md](modules/academic-research-suite/ars/academic-pipeline/examples/integrity_failure_recovery.md)
- [ars/academic-pipeline/examples/mid_entry_example.md](modules/academic-research-suite/ars/academic-pipeline/examples/mid_entry_example.md)
- [ars/academic-pipeline/references/adapters/overview.md](modules/academic-research-suite/ars/academic-pipeline/references/adapters/overview.md)
- [ars/academic-pipeline/references/ai_research_failure_modes.md](modules/academic-research-suite/ars/academic-pipeline/references/ai_research_failure_modes.md)
- [ars/academic-pipeline/references/changelog.md](modules/academic-research-suite/ars/academic-pipeline/references/changelog.md)
- [ars/academic-pipeline/references/claim_audit_calibration_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/claim_audit_calibration_protocol.md)
- [ars/academic-pipeline/references/claim_verification_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/claim_verification_protocol.md)
- [ars/academic-pipeline/references/external_review_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/external_review_protocol.md)
- [ars/academic-pipeline/references/integrity_review_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/integrity_review_protocol.md)
- [ars/academic-pipeline/references/literature_corpus_consumers.md](modules/academic-research-suite/ars/academic-pipeline/references/literature_corpus_consumers.md)
- [ars/academic-pipeline/references/mode_advisor.md](modules/academic-research-suite/ars/academic-pipeline/references/mode_advisor.md)
- [ars/academic-pipeline/references/passport_as_reset_boundary.md](modules/academic-research-suite/ars/academic-pipeline/references/passport_as_reset_boundary.md)
- [ars/academic-pipeline/references/pipeline_state_machine.md](modules/academic-research-suite/ars/academic-pipeline/references/pipeline_state_machine.md)
- [ars/academic-pipeline/references/plagiarism_detection_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/plagiarism_detection_protocol.md)
- [ars/academic-pipeline/references/process_summary_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/process_summary_protocol.md)
- [ars/academic-pipeline/references/progress_dashboard_template.md](modules/academic-research-suite/ars/academic-pipeline/references/progress_dashboard_template.md)
- [ars/academic-pipeline/references/reinforcement_content.md](modules/academic-research-suite/ars/academic-pipeline/references/reinforcement_content.md)
- [ars/academic-pipeline/references/reproducibility_audit.md](modules/academic-research-suite/ars/academic-pipeline/references/reproducibility_audit.md)
- [ars/academic-pipeline/references/score_trajectory_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/score_trajectory_protocol.md)
- [ars/academic-pipeline/references/team_collaboration_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/team_collaboration_protocol.md)
- [ars/academic-pipeline/references/two_stage_review_protocol.md](modules/academic-research-suite/ars/academic-pipeline/references/two_stage_review_protocol.md)
- [ars/academic-pipeline/templates/pipeline_status_template.md](modules/academic-research-suite/ars/academic-pipeline/templates/pipeline_status_template.md)
- [ars/agents/report_compiler_agent.md](modules/academic-research-suite/ars/agents/report_compiler_agent.md)
- [ars/agents/research_architect_agent.md](modules/academic-research-suite/ars/agents/research_architect_agent.md)
- [ars/agents/screening_reviewer_agent.md](modules/academic-research-suite/ars/agents/screening_reviewer_agent.md)
- [ars/agents/synthesis_agent.md](modules/academic-research-suite/ars/agents/synthesis_agent.md)
- [ars/audits/575-scope-closure-audit-2026-08-24.md](modules/academic-research-suite/ars/audits/575-scope-closure-audit-2026-08-24.md)
- [ars/audits/575-source-backed-proving-set-2026-08-24.md](modules/academic-research-suite/ars/audits/575-source-backed-proving-set-2026-08-24.md)
- [ars/audits/684-expert-readiness-2026-08-24.md](modules/academic-research-suite/ars/audits/684-expert-readiness-2026-08-24.md)
- [ars/audits/ars-researcher-blindspot-audit-2026-06-10.md](modules/academic-research-suite/ars/audits/ars-researcher-blindspot-audit-2026-06-10.md)
- [ars/audits/bakeoff-gpt-5-6-sol-codex-2026-08-19.md](modules/academic-research-suite/ars/audits/bakeoff-gpt-5-6-sol-codex-2026-08-19.md)
- [ars/audits/external-contribution-audit-prompt.md](modules/academic-research-suite/ars/audits/external-contribution-audit-prompt.md)
- [ars/audits/harness-retirement-2026-06-10.md](modules/academic-research-suite/ars/audits/harness-retirement-2026-06-10.md)
- [ars/audits/harness-retirement-2026-07-04.md](modules/academic-research-suite/ars/audits/harness-retirement-2026-07-04.md)
- [ars/audits/harness-retirement-2026-07.md](modules/academic-research-suite/ars/audits/harness-retirement-2026-07.md)
- [ars/audits/harness-retirement-2026-08.md](modules/academic-research-suite/ars/audits/harness-retirement-2026-08.md)
- [ars/audits/harness-retirement-2026-09-model-update.md](modules/academic-research-suite/ars/audits/harness-retirement-2026-09-model-update.md)
- [ars/audits/harness-retirement-2026-09-opus-5-5.md](modules/academic-research-suite/ars/audits/harness-retirement-2026-09-opus-5-5.md)
- [ars/audits/harness-retirement-2026-09.md](modules/academic-research-suite/ars/audits/harness-retirement-2026-09.md)
- [ars/audits/iso42001-spirit-gap-assessment-2026-08-17.md](modules/academic-research-suite/ars/audits/iso42001-spirit-gap-assessment-2026-08-17.md)
- [ars/audits/rq-advisory-505-exemption-sharpening-2026-07-11.md](modules/academic-research-suite/ars/audits/rq-advisory-505-exemption-sharpening-2026-07-11.md)
- [ars/audits/rq-advisory-heldout-measurement-2026-07-11.md](modules/academic-research-suite/ars/audits/rq-advisory-heldout-measurement-2026-07-11.md)
- [ars/CHANGELOG.md](modules/academic-research-suite/ars/CHANGELOG.md)
- [ars/commands/ars-3w.md](modules/academic-research-suite/ars/commands/ars-3w.md)
- [ars/commands/ars-abstract.md](modules/academic-research-suite/ars/commands/ars-abstract.md)
- [ars/commands/ars-cache-invalidate.md](modules/academic-research-suite/ars/commands/ars-cache-invalidate.md)
- [ars/commands/ars-citation-check.md](modules/academic-research-suite/ars/commands/ars-citation-check.md)
- [ars/commands/ars-disclosure.md](modules/academic-research-suite/ars/commands/ars-disclosure.md)
- [ars/commands/ars-format-convert.md](modules/academic-research-suite/ars/commands/ars-format-convert.md)
- [ars/commands/ars-full.md](modules/academic-research-suite/ars/commands/ars-full.md)
- [ars/commands/ars-lit-review.md](modules/academic-research-suite/ars/commands/ars-lit-review.md)
- [ars/commands/ars-mark-read.md](modules/academic-research-suite/ars/commands/ars-mark-read.md)
- [ars/commands/ars-outline.md](modules/academic-research-suite/ars/commands/ars-outline.md)
- [ars/commands/ars-plan.md](modules/academic-research-suite/ars/commands/ars-plan.md)
- [ars/commands/ars-rebuttal-audit.md](modules/academic-research-suite/ars/commands/ars-rebuttal-audit.md)
- [ars/commands/ars-reviewer.md](modules/academic-research-suite/ars/commands/ars-reviewer.md)
- [ars/commands/ars-revision-coach.md](modules/academic-research-suite/ars/commands/ars-revision-coach.md)
- [ars/commands/ars-revision.md](modules/academic-research-suite/ars/commands/ars-revision.md)
- [ars/commands/ars-unmark-read.md](modules/academic-research-suite/ars/commands/ars-unmark-read.md)
- [ars/CONTRIBUTING.md](modules/academic-research-suite/ars/CONTRIBUTING.md)
- [ars/deep-research/agents/bibliography_agent.md](modules/academic-research-suite/ars/deep-research/agents/bibliography_agent.md)
- [ars/deep-research/agents/devils_advocate_agent.md](modules/academic-research-suite/ars/deep-research/agents/devils_advocate_agent.md)
- [ars/deep-research/agents/editor_in_chief_agent.md](modules/academic-research-suite/ars/deep-research/agents/editor_in_chief_agent.md)
- [ars/deep-research/agents/ethics_review_agent.md](modules/academic-research-suite/ars/deep-research/agents/ethics_review_agent.md)
- [ars/deep-research/agents/meta_analysis_agent.md](modules/academic-research-suite/ars/deep-research/agents/meta_analysis_agent.md)
- [ars/deep-research/agents/monitoring_agent.md](modules/academic-research-suite/ars/deep-research/agents/monitoring_agent.md)
- [ars/deep-research/agents/report_compiler_agent.md](modules/academic-research-suite/ars/deep-research/agents/report_compiler_agent.md)
- [ars/deep-research/agents/research_architect_agent.md](modules/academic-research-suite/ars/deep-research/agents/research_architect_agent.md)
- [ars/deep-research/agents/research_question_agent.md](modules/academic-research-suite/ars/deep-research/agents/research_question_agent.md)
- [ars/deep-research/agents/risk_of_bias_agent.md](modules/academic-research-suite/ars/deep-research/agents/risk_of_bias_agent.md)
- [ars/deep-research/agents/socratic_mentor_agent.md](modules/academic-research-suite/ars/deep-research/agents/socratic_mentor_agent.md)
- [ars/deep-research/agents/source_verification_agent.md](modules/academic-research-suite/ars/deep-research/agents/source_verification_agent.md)
- [ars/deep-research/agents/synthesis_agent.md](modules/academic-research-suite/ars/deep-research/agents/synthesis_agent.md)
- [ars/deep-research/agents/timeline_extraction_agent.md](modules/academic-research-suite/ars/deep-research/agents/timeline_extraction_agent.md)
- [ars/deep-research/examples/exploratory_research.md](modules/academic-research-suite/ars/deep-research/examples/exploratory_research.md)
- [ars/deep-research/examples/fact_check_mode.md](modules/academic-research-suite/ars/deep-research/examples/fact_check_mode.md)
- [ars/deep-research/examples/handoff_to_paper.md](modules/academic-research-suite/ars/deep-research/examples/handoff_to_paper.md)
- [ars/deep-research/examples/idea_diversity_coverage_gap_advisory.md](modules/academic-research-suite/ars/deep-research/examples/idea_diversity_coverage_gap_advisory.md)
- [ars/deep-research/examples/policy_analysis.md](modules/academic-research-suite/ars/deep-research/examples/policy_analysis.md)
- [ars/deep-research/examples/review_mode.md](modules/academic-research-suite/ars/deep-research/examples/review_mode.md)
- [ars/deep-research/examples/socratic_guided_research.md](modules/academic-research-suite/ars/deep-research/examples/socratic_guided_research.md)
- [ars/deep-research/examples/systematic_review.md](modules/academic-research-suite/ars/deep-research/examples/systematic_review.md)
- [ars/deep-research/references/apa7_style_guide.md](modules/academic-research-suite/ars/deep-research/references/apa7_style_guide.md)
- [ars/deep-research/references/argumentation_reasoning_framework.md](modules/academic-research-suite/ars/deep-research/references/argumentation_reasoning_framework.md)
- [ars/deep-research/references/arxiv_api_protocol.md](modules/academic-research-suite/ars/deep-research/references/arxiv_api_protocol.md)
- [ars/deep-research/references/changelog.md](modules/academic-research-suite/ars/deep-research/references/changelog.md)
- [ars/deep-research/references/chinese_literature_api_protocol.md](modules/academic-research-suite/ars/deep-research/references/chinese_literature_api_protocol.md)
- [ars/deep-research/references/cross_agent_quality_definitions.md](modules/academic-research-suite/ars/deep-research/references/cross_agent_quality_definitions.md)
- [ars/deep-research/references/crossref_api_protocol.md](modules/academic-research-suite/ars/deep-research/references/crossref_api_protocol.md)
- [ars/deep-research/references/equator_reporting_guidelines.md](modules/academic-research-suite/ars/deep-research/references/equator_reporting_guidelines.md)
- [ars/deep-research/references/ethics_checklist.md](modules/academic-research-suite/ars/deep-research/references/ethics_checklist.md)
- [ars/deep-research/references/failure_paths.md](modules/academic-research-suite/ars/deep-research/references/failure_paths.md)
- [ars/deep-research/references/interdisciplinary_bridges.md](modules/academic-research-suite/ars/deep-research/references/interdisciplinary_bridges.md)
- [ars/deep-research/references/irb_decision_tree.md](modules/academic-research-suite/ars/deep-research/references/irb_decision_tree.md)
- [ars/deep-research/references/literature_monitoring_strategies.md](modules/academic-research-suite/ars/deep-research/references/literature_monitoring_strategies.md)
- [ars/deep-research/references/logical_fallacies.md](modules/academic-research-suite/ars/deep-research/references/logical_fallacies.md)
- [ars/deep-research/references/methodology_patterns.md](modules/academic-research-suite/ars/deep-research/references/methodology_patterns.md)
- [ars/deep-research/references/mode_selection_guide.md](modules/academic-research-suite/ars/deep-research/references/mode_selection_guide.md)
- [ars/deep-research/references/openalex_api_protocol.md](modules/academic-research-suite/ars/deep-research/references/openalex_api_protocol.md)
- [ars/deep-research/references/preregistration_guide.md](modules/academic-research-suite/ars/deep-research/references/preregistration_guide.md)
- [ars/deep-research/references/semantic_scholar_api_protocol.md](modules/academic-research-suite/ars/deep-research/references/semantic_scholar_api_protocol.md)
- [ars/deep-research/references/socratic_mode_protocol.md](modules/academic-research-suite/ars/deep-research/references/socratic_mode_protocol.md)
- [ars/deep-research/references/socratic_questioning_framework.md](modules/academic-research-suite/ars/deep-research/references/socratic_questioning_framework.md)
- [ars/deep-research/references/source_quality_hierarchy.md](modules/academic-research-suite/ars/deep-research/references/source_quality_hierarchy.md)
- [ars/deep-research/references/systematic_review_protocol.md](modules/academic-research-suite/ars/deep-research/references/systematic_review_protocol.md)
- [ars/deep-research/references/systematic_review_toolkit.md](modules/academic-research-suite/ars/deep-research/references/systematic_review_toolkit.md)
- [ars/deep-research/templates/evidence_assessment_template.md](modules/academic-research-suite/ars/deep-research/templates/evidence_assessment_template.md)
- [ars/deep-research/templates/literature_matrix_template.md](modules/academic-research-suite/ars/deep-research/templates/literature_matrix_template.md)
- [ars/deep-research/templates/preregistration_template.md](modules/academic-research-suite/ars/deep-research/templates/preregistration_template.md)
- [ars/deep-research/templates/prisma_protocol_template.md](modules/academic-research-suite/ars/deep-research/templates/prisma_protocol_template.md)
- [ars/deep-research/templates/prisma_report_template.md](modules/academic-research-suite/ars/deep-research/templates/prisma_report_template.md)
- [ars/deep-research/templates/research_brief_template.md](modules/academic-research-suite/ars/deep-research/templates/research_brief_template.md)
- [ars/docs/ARCHITECTURE.md](modules/academic-research-suite/ars/docs/ARCHITECTURE.md)
- [ars/docs/changelog-archive/es-ES.md](modules/academic-research-suite/ars/docs/changelog-archive/es-ES.md)
- [ars/docs/changelog-archive/ja-JP.md](modules/academic-research-suite/ars/docs/changelog-archive/ja-JP.md)
- [ars/docs/changelog-archive/ko-KR.md](modules/academic-research-suite/ars/docs/changelog-archive/ko-KR.md)
- [ars/docs/changelog-archive/zh-CN.md](modules/academic-research-suite/ars/docs/changelog-archive/zh-CN.md)
- [ars/docs/changelog-archive/zh-TW.md](modules/academic-research-suite/ars/docs/changelog-archive/zh-TW.md)
- [ars/docs/CONTROL_AVAILABILITY.md](modules/academic-research-suite/ars/docs/CONTROL_AVAILABILITY.md)
- [ars/docs/cross-paper-workflow.md](modules/academic-research-suite/ars/docs/cross-paper-workflow.md)
- [ars/docs/DATA_FLOWS.md](modules/academic-research-suite/ars/docs/DATA_FLOWS.md)
- [ars/docs/design/2026-04-20-v3.4-prisma-trAIce-raise-readcheck-design.md](modules/academic-research-suite/ars/docs/design/2026-04-20-v3.4-prisma-trAIce-raise-readcheck-design.md)
- [ars/docs/design/2026-04-22-ars-v3.7.3-reading-check-probe-design.md](modules/academic-research-suite/ars/docs/design/2026-04-22-ars-v3.7.3-reading-check-probe-design.md)
- [ars/docs/design/2026-04-23-ars-v3.6.2-sprint-contract-design.md](modules/academic-research-suite/ars/docs/design/2026-04-23-ars-v3.6.2-sprint-contract-design.md)
- [ars/docs/design/2026-04-23-ars-v3.6.4-literature-corpus-adapters-design.md](modules/academic-research-suite/ars/docs/design/2026-04-23-ars-v3.6.4-literature-corpus-adapters-design.md)
- [ars/docs/design/2026-04-23-ars-v3.6.4-literature-corpus-adapters-plan.md](modules/academic-research-suite/ars/docs/design/2026-04-23-ars-v3.6.4-literature-corpus-adapters-plan.md)
- [ars/docs/design/2026-04-26-ars-v3.6.5-consumer-integration-design.md](modules/academic-research-suite/ars/docs/design/2026-04-26-ars-v3.6.5-consumer-integration-design.md)
- [ars/docs/design/2026-04-27-ars-v3.6.5.1-setup-fix-implementation-brief.md](modules/academic-research-suite/ars/docs/design/2026-04-27-ars-v3.6.5.1-setup-fix-implementation-brief.md)
- [ars/docs/design/2026-04-27-ars-v3.6.5.2-claude-ai-method-4a-scope-implementation-brief.md](modules/academic-research-suite/ars/docs/design/2026-04-27-ars-v3.6.5.2-claude-ai-method-4a-scope-implementation-brief.md)
- [ars/docs/design/2026-04-27-ars-v3.6.6-generator-evaluator-contract-design.md](modules/academic-research-suite/ars/docs/design/2026-04-27-ars-v3.6.6-generator-evaluator-contract-design.md)
- [ars/docs/design/2026-04-29-ars-v3.6.7-downstream-agent-pattern-protection-spec.md](modules/academic-research-suite/ars/docs/design/2026-04-29-ars-v3.6.7-downstream-agent-pattern-protection-spec.md)
- [ars/docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md](modules/academic-research-suite/ars/docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md)
- [ars/docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md](modules/academic-research-suite/ars/docs/design/2026-04-30-ars-v3.6.8-trust-provenance-and-drift-transparency-spec.md)
- [ars/docs/design/2026-04-30-ars-v3.7.0-plugin-packaging-roadmap.md](modules/academic-research-suite/ars/docs/design/2026-04-30-ars-v3.7.0-plugin-packaging-roadmap.md)
- [ars/docs/design/2026-05-05-phase-6.6-scoping-note.md](modules/academic-research-suite/ars/docs/design/2026-05-05-phase-6.6-scoping-note.md)
- [ars/docs/design/2026-05-10-ars-v3.7.2-trust-provenance-hardening-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-10-ars-v3.7.2-trust-provenance-hardening-spec.md)
- [ars/docs/design/2026-05-12-ars-v3.7.3-claim-faithfulness-and-contaminated-source-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-12-ars-v3.7.3-claim-faithfulness-and-contaminated-source-spec.md)
- [ars/docs/design/2026-05-13-ai-disclosure-schema-discovery.md](modules/academic-research-suite/ars/docs/design/2026-05-13-ai-disclosure-schema-discovery.md)
- [ars/docs/design/2026-05-14-ai-disclosure-impl-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-14-ai-disclosure-impl-spec.md)
- [ars/docs/design/2026-05-14-ai-disclosure-schema-decision.md](modules/academic-research-suite/ars/docs/design/2026-05-14-ai-disclosure-schema-decision.md)
- [ars/docs/design/2026-05-15-issue-103-claim-alignment-audit-decision.md](modules/academic-research-suite/ars/docs/design/2026-05-15-issue-103-claim-alignment-audit-decision.md)
- [ars/docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-15-issue-103-claim-alignment-audit-spec.md)
- [ars/docs/design/2026-05-15-issue-105-contamination-signals-backfill-design.md](modules/academic-research-suite/ars/docs/design/2026-05-15-issue-105-contamination-signals-backfill-design.md)
- [ars/docs/design/2026-05-15-issue-111-slr-lineage-emission-design.md](modules/academic-research-suite/ars/docs/design/2026-05-15-issue-111-slr-lineage-emission-design.md)
- [ars/docs/design/2026-05-17-ars-v3.9.0-cross-index-triangulation-measurement-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-17-ars-v3.9.0-cross-index-triangulation-measurement-spec.md)
- [ars/docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md](modules/academic-research-suite/ars/docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md)
- [ars/docs/design/2026-05-18-ars-v3.9.2-phase-boundary-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-18-ars-v3.9.2-phase-boundary-spec.md)
- [ars/docs/design/2026-05-18-ars-v3.9.4-temporal-verification-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-18-ars-v3.9.4-temporal-verification-spec.md)
- [ars/docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md)
- [ars/docs/design/2026-05-21-v3.10-183-epistemic-status-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-21-v3.10-183-epistemic-status-spec.md)
- [ars/docs/design/2026-05-21-v3.10-184-extend-eval-harness-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-21-v3.10-184-extend-eval-harness-spec.md)
- [ars/docs/design/2026-05-28-kong-257-idea-diversity-coverage-gap-advisory.md](modules/academic-research-suite/ars/docs/design/2026-05-28-kong-257-idea-diversity-coverage-gap-advisory.md)
- [ars/docs/design/2026-05-28-kong-258-version-family-reconciliation.md](modules/academic-research-suite/ars/docs/design/2026-05-28-kong-258-version-family-reconciliation.md)
- [ars/docs/design/2026-05-29-kong-259-domain-evidence-profiles-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-29-kong-259-domain-evidence-profiles-spec.md)
- [ars/docs/design/2026-05-30-kong-259-domain-evidence-profiles-plan.md](modules/academic-research-suite/ars/docs/design/2026-05-30-kong-259-domain-evidence-profiles-plan.md)
- [ars/docs/design/2026-05-31-ars-268-schema11-nested-commitment-ledger-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-31-ars-268-schema11-nested-commitment-ledger-spec.md)
- [ars/docs/design/2026-05-31-ars-v3.10-policy-layer-rescope-spec.md](modules/academic-research-suite/ars/docs/design/2026-05-31-ars-v3.10-policy-layer-rescope-spec.md)
- [ars/docs/design/2026-06-01-ars-134-conductor-rescope-deterministic-write-guard-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-01-ars-134-conductor-rescope-deterministic-write-guard-spec.md)
- [ars/docs/design/2026-06-02-co-scientist-220-l1-hidden-ranking.md](modules/academic-research-suite/ars/docs/design/2026-06-02-co-scientist-220-l1-hidden-ranking.md)
- [ars/docs/design/2026-06-02-co-scientist-221-l2-feedback-propagation.md](modules/academic-research-suite/ars/docs/design/2026-06-02-co-scientist-221-l2-feedback-propagation.md)
- [ars/docs/design/2026-06-02-co-scientist-222-l3-transfer-matrix.md](modules/academic-research-suite/ars/docs/design/2026-06-02-co-scientist-222-l3-transfer-matrix.md)
- [ars/docs/design/2026-06-02-co-scientist-223-l4-control-plane-ownership.md](modules/academic-research-suite/ars/docs/design/2026-06-02-co-scientist-223-l4-control-plane-ownership.md)
- [ars/docs/design/2026-06-06-213-subclaim-decomposition-design.md](modules/academic-research-suite/ars/docs/design/2026-06-06-213-subclaim-decomposition-design.md)
- [ars/docs/design/2026-06-07-272-instruction-data-boundary-design.md](modules/academic-research-suite/ars/docs/design/2026-06-07-272-instruction-data-boundary-design.md)
- [ars/docs/design/2026-06-08-214-synthesizer-subclaim-design.md](modules/academic-research-suite/ars/docs/design/2026-06-08-214-synthesizer-subclaim-design.md)
- [ars/docs/design/2026-06-08-255-kong-meta-negative-scope-and-design-lessons.md](modules/academic-research-suite/ars/docs/design/2026-06-08-255-kong-meta-negative-scope-and-design-lessons.md)
- [ars/docs/design/2026-06-08-260-experiment-provenance-intake-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-08-260-experiment-provenance-intake-spec.md)
- [ars/docs/design/2026-06-08-262-cross-paper-contradiction-design.md](modules/academic-research-suite/ars/docs/design/2026-06-08-262-cross-paper-contradiction-design.md)
- [ars/docs/design/2026-06-08-273-rubric-aware-calibration-note-design.md](modules/academic-research-suite/ars/docs/design/2026-06-08-273-rubric-aware-calibration-note-design.md)
- [ars/docs/design/2026-06-08-274-concise-pressure-guidance-design.md](modules/academic-research-suite/ars/docs/design/2026-06-08-274-concise-pressure-guidance-design.md)
- [ars/docs/design/2026-06-08-kong-255-l1-copilot-not-auto-research.md](modules/academic-research-suite/ars/docs/design/2026-06-08-kong-255-l1-copilot-not-auto-research.md)
- [ars/docs/design/2026-06-08-kong-255-l2-advisory-not-generation.md](modules/academic-research-suite/ars/docs/design/2026-06-08-kong-255-l2-advisory-not-generation.md)
- [ars/docs/design/2026-06-09-216-surface-form-parity-design.md](modules/academic-research-suite/ars/docs/design/2026-06-09-216-surface-form-parity-design.md)
- [ars/docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md)
- [ars/docs/design/2026-06-10-394-family-d-repro-lock-assessment.md](modules/academic-research-suite/ars/docs/design/2026-06-10-394-family-d-repro-lock-assessment.md)
- [ars/docs/design/2026-06-10-394-submission-package-verifier-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-10-394-submission-package-verifier-spec.md)
- [ars/docs/design/2026-06-13-431-author-agree-removal-impact.md](modules/academic-research-suite/ars/docs/design/2026-06-13-431-author-agree-removal-impact.md)
- [ars/docs/design/2026-06-13-431-title-match-hardening-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-13-431-title-match-hardening-spec.md)
- [ars/docs/design/2026-06-13-changelog-covers-merges-release-gate-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-13-changelog-covers-merges-release-gate-spec.md)
- [ars/docs/design/2026-06-15-439-format-profile-design.md](modules/academic-research-suite/ars/docs/design/2026-06-15-439-format-profile-design.md)
- [ars/docs/design/2026-06-16-448-infra-protection-plugin-root-scope-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-16-448-infra-protection-plugin-root-scope-spec.md)
- [ars/docs/design/2026-06-16-453-provider-agnostic-cross-model-verifier-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-16-453-provider-agnostic-cross-model-verifier-spec.md)
- [ars/docs/design/2026-06-17-454-windows-python-hook-portability-design.md](modules/academic-research-suite/ars/docs/design/2026-06-17-454-windows-python-hook-portability-design.md)
- [ars/docs/design/2026-06-18-socratic-adjacent-framing-probe-spec.md](modules/academic-research-suite/ars/docs/design/2026-06-18-socratic-adjacent-framing-probe-spec.md)
- [ars/docs/design/2026-07-12-517-model-tiering-spec.md](modules/academic-research-suite/ars/docs/design/2026-07-12-517-model-tiering-spec.md)
- [ars/docs/design/2026-07-12-518-cross-model-gate-hardening-spec.md](modules/academic-research-suite/ars/docs/design/2026-07-12-518-cross-model-gate-hardening-spec.md)
- [ars/docs/design/2026-07-15-510-panel-synthesis-checker-design.md](modules/academic-research-suite/ars/docs/design/2026-07-15-510-panel-synthesis-checker-design.md)
- [ars/docs/design/2026-07-15-511-degradation-registry-design.md](modules/academic-research-suite/ars/docs/design/2026-07-15-511-degradation-registry-design.md)
- [ars/docs/design/2026-07-18-544-update-reminder-spec.md](modules/academic-research-suite/ars/docs/design/2026-07-18-544-update-reminder-spec.md)
- [ars/docs/design/2026-07-20-512-pdf-read-preflight-spec.md](modules/academic-research-suite/ars/docs/design/2026-07-20-512-pdf-read-preflight-spec.md)
- [ars/docs/design/2026-07-20-513-read-scope-attestation-spec.md](modules/academic-research-suite/ars/docs/design/2026-07-20-513-read-scope-attestation-spec.md)
- [ars/docs/design/2026-07-25-574-spec-a-role-scoped-scoring-decision-contract-spec.md](modules/academic-research-suite/ars/docs/design/2026-07-25-574-spec-a-role-scoped-scoring-decision-contract-spec.md)
- [ars/docs/design/2026-07-27-576-spec-b-re-review-precommitment-contract-spec.md](modules/academic-research-suite/ars/docs/design/2026-07-27-576-spec-b-re-review-precommitment-contract-spec.md)
- [ars/docs/design/2026-08-02-610-statistical-recompute-baseline-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-02-610-statistical-recompute-baseline-spec.md)
- [ars/docs/design/2026-08-06-610-step5-script-adapter-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-06-610-step5-script-adapter-spec.md)
- [ars/docs/design/2026-08-08-651-retraction-status-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-08-651-retraction-status-spec.md)
- [ars/docs/design/2026-08-08-668-committee-correspondence-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-08-668-committee-correspondence-spec.md)
- [ars/docs/design/2026-08-08-683-review-target-context-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-08-683-review-target-context-spec.md)
- [ars/docs/design/2026-08-09-656-shared-evidence-row-contract-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-09-656-shared-evidence-row-contract-spec.md)
- [ars/docs/design/2026-08-09-666-human-subjects-authority-contract-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-09-666-human-subjects-authority-contract-spec.md)
- [ars/docs/design/2026-08-09-667-submission-packet-manifest-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-09-667-submission-packet-manifest-spec.md)
- [ars/docs/design/2026-08-09-680-human-subjects-reference-migration-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-09-680-human-subjects-reference-migration-spec.md)
- [ars/docs/design/2026-08-09-681-authority-content-coverage-advisory-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-09-681-authority-content-coverage-advisory-spec.md)
- [ars/docs/design/2026-08-10-658-outcome-level-evaluation-design.md](modules/academic-research-suite/ars/docs/design/2026-08-10-658-outcome-level-evaluation-design.md)
- [ars/docs/design/2026-08-10-660-tortured-phrase-screening-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-10-660-tortured-phrase-screening-spec.md)
- [ars/docs/design/2026-08-10-670-non-ranking-revision-roadmap-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-10-670-non-ranking-revision-roadmap-spec.md)
- [ars/docs/design/2026-08-10-672-cross-document-consistency-advisory-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-10-672-cross-document-consistency-advisory-spec.md)
- [ars/docs/design/2026-08-10-673-cross-run-adjudication-activity-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-10-673-cross-run-adjudication-activity-spec.md)
- [ars/docs/design/2026-08-10-679-revision-claim-drift-suite-v2-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-10-679-revision-claim-drift-suite-v2-spec.md)
- [ars/docs/design/2026-08-11-630-codex-subscription-citation-transport-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-11-630-codex-subscription-citation-transport-spec.md)
- [ars/docs/design/2026-08-11-669-review-pathway-rule-trace-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-11-669-review-pathway-rule-trace-spec.md)
- [ars/docs/design/2026-08-11-684-review-criteria-consumer-binding-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-11-684-review-criteria-consumer-binding-spec.md)
- [ars/docs/design/2026-08-13-512-pdf-content-classification-sandbox-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-13-512-pdf-content-classification-sandbox-spec.md)
- [ars/docs/design/2026-08-13-582-role-topology-utility-design.md](modules/academic-research-suite/ars/docs/design/2026-08-13-582-role-topology-utility-design.md)
- [ars/docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md](modules/academic-research-suite/ars/docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md)
- [ars/docs/design/2026-08-13-659-within-session-ideation-diversity-design.md](modules/academic-research-suite/ars/docs/design/2026-08-13-659-within-session-ideation-diversity-design.md)
- [ars/docs/design/2026-08-13-675-indirect-prompt-injection-behavior-eval-spec.md](modules/academic-research-suite/ars/docs/design/2026-08-13-675-indirect-prompt-injection-behavior-eval-spec.md)
- [ars/docs/design/2026-08-17-742-research-family-profile-contract-design.md](modules/academic-research-suite/ars/docs/design/2026-08-17-742-research-family-profile-contract-design.md)
- [ars/docs/design/2026-08-17-743-inquiry-branch-ledger-design.md](modules/academic-research-suite/ars/docs/design/2026-08-17-743-inquiry-branch-ledger-design.md)
- [ars/docs/design/2026-08-24-744-alternative-explanation-register-design.md](modules/academic-research-suite/ars/docs/design/2026-08-24-744-alternative-explanation-register-design.md)
- [ars/docs/design/2026-09-23-887-handoff-integrity-design.md](modules/academic-research-suite/ars/docs/design/2026-09-23-887-handoff-integrity-design.md)
- [ars/docs/design/2026-09-23-890-instruction-data-boundary-extension.md](modules/academic-research-suite/ars/docs/design/2026-09-23-890-instruction-data-boundary-extension.md)
- [ars/docs/design/2026-09-24-894-instruction-data-boundary-tool-calls.md](modules/academic-research-suite/ars/docs/design/2026-09-24-894-instruction-data-boundary-tool-calls.md)
- [ars/docs/migration/v3.7.3-contamination-signals-backfill.md](modules/academic-research-suite/ars/docs/migration/v3.7.3-contamination-signals-backfill.md)
- [ars/docs/PERFORMANCE.md](modules/academic-research-suite/ars/docs/PERFORMANCE.md)
- [ars/docs/PERFORMANCE.zh-TW.md](modules/academic-research-suite/ars/docs/PERFORMANCE.zh-TW.md)
- [ars/docs/RISK_REGISTER.md](modules/academic-research-suite/ars/docs/RISK_REGISTER.md)
- [ars/docs/ROADMAP-v3.11.md](modules/academic-research-suite/ars/docs/ROADMAP-v3.11.md)
- [ars/docs/ROADMAP-v3.20.1-v3.22.md](modules/academic-research-suite/ars/docs/ROADMAP-v3.20.1-v3.22.md)
- [ars/docs/SETUP.md](modules/academic-research-suite/ars/docs/SETUP.md)
- [ars/docs/SETUP.zh-TW.md](modules/academic-research-suite/ars/docs/SETUP.zh-TW.md)
- [ars/docs/STAGE_CAPABILITY_MATRIX.md](modules/academic-research-suite/ars/docs/STAGE_CAPABILITY_MATRIX.md)
- [ars/examples/contradiction_pairs_example.md](modules/academic-research-suite/ars/examples/contradiction_pairs_example.md)
- [ars/examples/figure_table_trace_example.md](modules/academic-research-suite/ars/examples/figure_table_trace_example.md)
- [ars/examples/pi/model-portability.md](modules/academic-research-suite/ars/examples/pi/model-portability.md)
- [ars/examples/pi/README.md](modules/academic-research-suite/ars/examples/pi/README.md)
- [ars/examples/pi/run-log.md](modules/academic-research-suite/ars/examples/pi/run-log.md)
- [ars/examples/pi/stage-01/revised-research-report.md](modules/academic-research-suite/ars/examples/pi/stage-01/revised-research-report.md)
- [ars/examples/pi/stage-02/course-paper-draft.md](modules/academic-research-suite/ars/examples/pi/stage-02/course-paper-draft.md)
- [ars/examples/pi/stage-02.5/focused-reverification-report.md](modules/academic-research-suite/ars/examples/pi/stage-02.5/focused-reverification-report.md)
- [ars/examples/pi/stage-03/editorial-decision-and-revision-roadmap.md](modules/academic-research-suite/ars/examples/pi/stage-03/editorial-decision-and-revision-roadmap.md)
- [ars/examples/pi/stage-03p/verification-review-report.md](modules/academic-research-suite/ars/examples/pi/stage-03p/verification-review-report.md)
- [ars/examples/pi/stage-04/response-to-reviewers.md](modules/academic-research-suite/ars/examples/pi/stage-04/response-to-reviewers.md)
- [ars/examples/pi/stage-04.5/final-integrity-verification-report.md](modules/academic-research-suite/ars/examples/pi/stage-04.5/final-integrity-verification-report.md)
- [ars/examples/pi/stage-04p/validation-report.md](modules/academic-research-suite/ars/examples/pi/stage-04p/validation-report.md)
- [ars/examples/pi/stage-05/cite-time-gate-refusal-report.md](modules/academic-research-suite/ars/examples/pi/stage-05/cite-time-gate-refusal-report.md)
- [ars/examples/pi/stage-05/full-checkpoint.md](modules/academic-research-suite/ars/examples/pi/stage-05/full-checkpoint.md)
- [ars/examples/pi/stage-05/package/format-validation.md](modules/academic-research-suite/ars/examples/pi/stage-05/package/format-validation.md)
- [ars/examples/pi/stage-05/package/paper.md](modules/academic-research-suite/ars/examples/pi/stage-05/package/paper.md)
- [ars/examples/pi/stage-06/process-record-en.md](modules/academic-research-suite/ars/examples/pi/stage-06/process-record-en.md)
- [ars/examples/pi/stage-06/terminal-checkpoint.md](modules/academic-research-suite/ars/examples/pi/stage-06/terminal-checkpoint.md)
- [ars/examples/showcase/README.md](modules/academic-research-suite/ars/examples/showcase/README.md)
- [ars/experiment-agent/agents/code_runner_agent.md](modules/academic-research-suite/ars/experiment-agent/agents/code_runner_agent.md)
- [ars/experiment-agent/agents/study_manager_agent.md](modules/academic-research-suite/ars/experiment-agent/agents/study_manager_agent.md)
- [ars/experiment-agent/CHANGELOG.md](modules/academic-research-suite/ars/experiment-agent/CHANGELOG.md)
- [ars/experiment-agent/docs/plans/2026-05-02-session-resume-implementation.md](modules/academic-research-suite/ars/experiment-agent/docs/plans/2026-05-02-session-resume-implementation.md)
- [ars/experiment-agent/docs/specs/2026-05-02-session-resume-design.md](modules/academic-research-suite/ars/experiment-agent/docs/specs/2026-05-02-session-resume-design.md)
- [ars/experiment-agent/README.md](modules/academic-research-suite/ars/experiment-agent/README.md)
- [ars/experiment-agent/README.zh-TW.md](modules/academic-research-suite/ars/experiment-agent/README.zh-TW.md)
- [ars/experiment-agent/references/ars_integration_guide.md](modules/academic-research-suite/ars/experiment-agent/references/ars_integration_guide.md)
- [ars/experiment-agent/references/irb_ethics_checklist.md](modules/academic-research-suite/ars/experiment-agent/references/irb_ethics_checklist.md)
- [ars/experiment-agent/references/reproducibility_protocol.md](modules/academic-research-suite/ars/experiment-agent/references/reproducibility_protocol.md)
- [ars/experiment-agent/references/stall_detection_protocol.md](modules/academic-research-suite/ars/experiment-agent/references/stall_detection_protocol.md)
- [ars/experiment-agent/references/statistical_interpretation_guide.md](modules/academic-research-suite/ars/experiment-agent/references/statistical_interpretation_guide.md)
- [ars/experiment-agent/references/study_state_protocol.md](modules/academic-research-suite/ars/experiment-agent/references/study_state_protocol.md)
- [ars/experiment-agent/templates/code_experiment_plan.md](modules/academic-research-suite/ars/experiment-agent/templates/code_experiment_plan.md)
- [ars/experiment-agent/templates/output_formats.md](modules/academic-research-suite/ars/experiment-agent/templates/output_formats.md)
- [ars/experiment-agent/templates/study_protocol.md](modules/academic-research-suite/ars/experiment-agent/templates/study_protocol.md)
- [ars/experiment-agent/templates/study_state.example.md](modules/academic-research-suite/ars/experiment-agent/templates/study_state.example.md)
- [ars/experiment-agent/templates/study_state.md](modules/academic-research-suite/ars/experiment-agent/templates/study_state.md)
- [ars/GOVERNANCE.md](modules/academic-research-suite/ars/GOVERNANCE.md)
- [ars/MODE_REGISTRY.md](modules/academic-research-suite/ars/MODE_REGISTRY.md)
- [ars/NOTICE.md](modules/academic-research-suite/ars/NOTICE.md)
- [ars/pi/README.md](modules/academic-research-suite/ars/pi/README.md)
- [ars/plugin-evals/01-journal-mixed-format-zh/graders/all-9-covered.md](modules/academic-research-suite/ars/plugin-evals/01-journal-mixed-format-zh/graders/all-9-covered.md)
- [ars/plugin-evals/01-journal-mixed-format-zh/graders/no-rewrite.md](modules/academic-research-suite/ars/plugin-evals/01-journal-mixed-format-zh/graders/no-rewrite.md)
- [ars/plugin-evals/01-journal-mixed-format-zh/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals/01-journal-mixed-format-zh/graders/skill-fired.md)
- [ars/plugin-evals/01-journal-mixed-format-zh/prompt.md](modules/academic-research-suite/ars/plugin-evals/01-journal-mixed-format-zh/prompt.md)
- [ars/plugin-evals/02-decision-letter-email-en/graders/all-covered.md](modules/academic-research-suite/ars/plugin-evals/02-decision-letter-email-en/graders/all-covered.md)
- [ars/plugin-evals/02-decision-letter-email-en/graders/no-rewrite.md](modules/academic-research-suite/ars/plugin-evals/02-decision-letter-email-en/graders/no-rewrite.md)
- [ars/plugin-evals/02-decision-letter-email-en/graders/pushback-flagged.md](modules/academic-research-suite/ars/plugin-evals/02-decision-letter-email-en/graders/pushback-flagged.md)
- [ars/plugin-evals/02-decision-letter-email-en/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals/02-decision-letter-email-en/graders/skill-fired.md)
- [ars/plugin-evals/02-decision-letter-email-en/prompt.md](modules/academic-research-suite/ars/plugin-evals/02-decision-letter-email-en/prompt.md)
- [ars/plugin-evals/03-iclr-rebuttal-en/graders/no-committee-branch.md](modules/academic-research-suite/ars/plugin-evals/03-iclr-rebuttal-en/graders/no-committee-branch.md)
- [ars/plugin-evals/03-iclr-rebuttal-en/graders/no-fabrication.md](modules/academic-research-suite/ars/plugin-evals/03-iclr-rebuttal-en/graders/no-fabrication.md)
- [ars/plugin-evals/03-iclr-rebuttal-en/graders/pushback-per-reviewer.md](modules/academic-research-suite/ars/plugin-evals/03-iclr-rebuttal-en/graders/pushback-per-reviewer.md)
- [ars/plugin-evals/03-iclr-rebuttal-en/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals/03-iclr-rebuttal-en/graders/skill-fired.md)
- [ars/plugin-evals/03-iclr-rebuttal-en/prompt.md](modules/academic-research-suite/ars/plugin-evals/03-iclr-rebuttal-en/prompt.md)
- [ars/plugin-evals/04-ethics-committee-letter-zh/graders/no-severity-words.md](modules/academic-research-suite/ars/plugin-evals/04-ethics-committee-letter-zh/graders/no-severity-words.md)
- [ars/plugin-evals/04-ethics-committee-letter-zh/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals/04-ethics-committee-letter-zh/graders/skill-fired.md)
- [ars/plugin-evals/04-ethics-committee-letter-zh/graders/tracker-covers-5.md](modules/academic-research-suite/ars/plugin-evals/04-ethics-committee-letter-zh/graders/tracker-covers-5.md)
- [ars/plugin-evals/04-ethics-committee-letter-zh/prompt.md](modules/academic-research-suite/ars/plugin-evals/04-ethics-committee-letter-zh/prompt.md)
- [ars/plugin-evals/05-terse-contradictory-zh/graders/contradiction-surfaced.md](modules/academic-research-suite/ars/plugin-evals/05-terse-contradictory-zh/graders/contradiction-surfaced.md)
- [ars/plugin-evals/05-terse-contradictory-zh/graders/no-rewrite.md](modules/academic-research-suite/ars/plugin-evals/05-terse-contradictory-zh/graders/no-rewrite.md)
- [ars/plugin-evals/05-terse-contradictory-zh/graders/scope-creep-flagged.md](modules/academic-research-suite/ars/plugin-evals/05-terse-contradictory-zh/graders/scope-creep-flagged.md)
- [ars/plugin-evals/05-terse-contradictory-zh/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals/05-terse-contradictory-zh/graders/skill-fired.md)
- [ars/plugin-evals/05-terse-contradictory-zh/prompt.md](modules/academic-research-suite/ars/plugin-evals/05-terse-contradictory-zh/prompt.md)
- [ars/plugin-evals/06-neg-existing-rebuttal-draft-zh/graders/missed-item-named.md](modules/academic-research-suite/ars/plugin-evals/06-neg-existing-rebuttal-draft-zh/graders/missed-item-named.md)
- [ars/plugin-evals/06-neg-existing-rebuttal-draft-zh/graders/no-new-skeleton.md](modules/academic-research-suite/ars/plugin-evals/06-neg-existing-rebuttal-draft-zh/graders/no-new-skeleton.md)
- [ars/plugin-evals/06-neg-existing-rebuttal-draft-zh/prompt.md](modules/academic-research-suite/ars/plugin-evals/06-neg-existing-rebuttal-draft-zh/prompt.md)
- [ars/plugin-evals/07-neg-landlord-letter-zh/graders/helpful-reply.md](modules/academic-research-suite/ars/plugin-evals/07-neg-landlord-letter-zh/graders/helpful-reply.md)
- [ars/plugin-evals/07-neg-landlord-letter-zh/graders/no-reviewer-template.md](modules/academic-research-suite/ars/plugin-evals/07-neg-landlord-letter-zh/graders/no-reviewer-template.md)
- [ars/plugin-evals/07-neg-landlord-letter-zh/graders/skill-not-called.md](modules/academic-research-suite/ars/plugin-evals/07-neg-landlord-letter-zh/graders/skill-not-called.md)
- [ars/plugin-evals/07-neg-landlord-letter-zh/prompt.md](modules/academic-research-suite/ars/plugin-evals/07-neg-landlord-letter-zh/prompt.md)
- [ars/plugin-evals/README.md](modules/academic-research-suite/ars/plugin-evals/README.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/content-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/content-caught.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/format-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/format-caught.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/honest-unverified.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/honest-unverified.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/no-false-positive.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/no-false-positive.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/no-overreach.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/no-overreach.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/orphan-named.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/orphan-named.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/graders/skill-fired.md)
- [ars/plugin-evals-citation-check/01-apa-en-misattribution/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/01-apa-en-misattribution/prompt.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/agent-loaded.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/agent-loaded.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/content-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/content-caught.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/format-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/format-caught.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/honest-unverified.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/honest-unverified.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/locale-guide-loaded.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/locale-guide-loaded.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/no-false-positive.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/no-false-positive.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/no-overreach.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/no-overreach.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/report-in-chinese.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/report-in-chinese.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/graders/skill-fired.md)
- [ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/02-apa-zh-mixed-overclaim/prompt.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/graders/content-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/graders/content-caught.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/graders/format-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/graders/format-caught.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/graders/honest-unverified.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/graders/honest-unverified.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/graders/no-false-positive.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/graders/no-false-positive.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/graders/no-overreach.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/graders/no-overreach.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/graders/orphan-named.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/graders/orphan-named.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/graders/skill-fired.md)
- [ars/plugin-evals-citation-check/03-ieee-en-prose/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/03-ieee-en-prose/prompt.md)
- [ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/content-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/content-caught.md)
- [ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/format-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/format-caught.md)
- [ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/honest-unverified.md](modules/academic-research-suite/ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/honest-unverified.md)
- [ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/no-false-positive.md](modules/academic-research-suite/ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/no-false-positive.md)
- [ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/no-overreach.md](modules/academic-research-suite/ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/no-overreach.md)
- [ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/graders/skill-fired.md)
- [ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/04-vancouver-en-terse-retraction/prompt.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/content-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/content-caught.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/format-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/format-caught.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/honest-unverified.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/honest-unverified.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/locale-respected.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/locale-respected.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/no-chinese-chars.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/no-chinese-chars.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/no-false-positive.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/no-false-positive.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/no-overreach.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/no-overreach.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/orphan-named.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/orphan-named.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/graders/skill-fired.md)
- [ars/plugin-evals-citation-check/05-apa-es-locale/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/05-apa-es-locale/prompt.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/content-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/content-caught.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/format-caught.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/format-caught.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/honest-unverified.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/honest-unverified.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/no-false-positive.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/no-false-positive.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/no-overreach.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/no-overreach.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/orphan-named.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/orphan-named.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/graders/skill-fired.md)
- [ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/06-chicago-nb-en-footnotes/prompt.md)
- [ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/graders/is-conversion.md](modules/academic-research-suite/ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/graders/is-conversion.md)
- [ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/graders/not-audit-report.md](modules/academic-research-suite/ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/graders/not-audit-report.md)
- [ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/graders/numbered-in-order.md](modules/academic-research-suite/ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/graders/numbered-in-order.md)
- [ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/07-neg-convert-apa-to-ieee/prompt.md)
- [ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/code-level-answer.md](modules/academic-research-suite/ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/code-level-answer.md)
- [ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/names-hashlib.md](modules/academic-research-suite/ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/names-hashlib.md)
- [ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/names-os.md](modules/academic-research-suite/ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/names-os.md)
- [ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/skill-not-called.md](modules/academic-research-suite/ars/plugin-evals-citation-check/08-neg-python-unused-imports/graders/skill-not-called.md)
- [ars/plugin-evals-citation-check/08-neg-python-unused-imports/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-check/08-neg-python-unused-imports/prompt.md)
- [ars/plugin-evals-citation-check/README.md](modules/academic-research-suite/ars/plugin-evals-citation-check/README.md)
- [ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/agent-loaded.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/agent-loaded.md)
- [ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/keep-two-authors.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/keep-two-authors.md)
- [ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/skill-fired.md)
- [ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/stroke-inversion.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/graders/stroke-inversion.md)
- [ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/09-zh-stroke-inversion-two-authors/prompt.md)
- [ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/agent-loaded.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/agent-loaded.md)
- [ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/preserve-disambiguation.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/preserve-disambiguation.md)
- [ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/preserve-reference-authors.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/preserve-reference-authors.md)
- [ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/graders/skill-fired.md)
- [ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/10-zh-disambiguation-preserve-authors/prompt.md)
- [ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/graders/agent-loaded.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/graders/agent-loaded.md)
- [ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/graders/honor-venue-order.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/graders/honor-venue-order.md)
- [ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/graders/skill-fired.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/graders/skill-fired.md)
- [ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/prompt.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/11-zh-venue-romanization-order/prompt.md)
- [ars/plugin-evals-citation-locale/README.md](modules/academic-research-suite/ars/plugin-evals-citation-locale/README.md)
- [ars/POSITIONING.md](modules/academic-research-suite/ars/POSITIONING.md)
- [ars/QUICKSTART.md](modules/academic-research-suite/ars/QUICKSTART.md)
- [ars/README.es-ES.md](modules/academic-research-suite/ars/README.es-ES.md)
- [ars/README.ja-JP.md](modules/academic-research-suite/ars/README.ja-JP.md)
- [ars/README.ko-KR.md](modules/academic-research-suite/ars/README.ko-KR.md)
- [ars/README.md](modules/academic-research-suite/ars/README.md)
- [ars/README.zh-CN.md](modules/academic-research-suite/ars/README.zh-CN.md)
- [ars/README.zh-TW.md](modules/academic-research-suite/ars/README.zh-TW.md)
- [ars/scripts/adapters/examples/obsidian/input_fixture/vault/_templates/tmpl.md](modules/academic-research-suite/ars/scripts/adapters/examples/obsidian/input_fixture/vault/_templates/tmpl.md)
- [ars/scripts/adapters/examples/obsidian/input_fixture/vault/chen2024ai.md](modules/academic-research-suite/ars/scripts/adapters/examples/obsidian/input_fixture/vault/chen2024ai.md)
- [ars/scripts/adapters/examples/obsidian/input_fixture/vault/invalid.md](modules/academic-research-suite/ars/scripts/adapters/examples/obsidian/input_fixture/vault/invalid.md)
- [ars/scripts/adapters/examples/obsidian/input_fixture/vault/wang2023formative.md](modules/academic-research-suite/ars/scripts/adapters/examples/obsidian/input_fixture/vault/wang2023formative.md)
- [ars/scripts/adapters/README.md](modules/academic-research-suite/ars/scripts/adapters/README.md)
- [ars/scripts/fixtures/audit_artifact_consistency/README.md](modules/academic-research-suite/ars/scripts/fixtures/audit_artifact_consistency/README.md)
- [ars/scripts/fixtures/committee_correspondence/16fd83f6aec7/response_skeleton.md](modules/academic-research-suite/ars/scripts/fixtures/committee_correspondence/16fd83f6aec7/response_skeleton.md)
- [ars/scripts/fixtures/cross_document_consistency/accepted_draft.md](modules/academic-research-suite/ars/scripts/fixtures/cross_document_consistency/accepted_draft.md)
- [ars/scripts/fixtures/cross_document_consistency/preregistration.md](modules/academic-research-suite/ars/scripts/fixtures/cross_document_consistency/preregistration.md)
- [ars/scripts/fixtures/cross_document_consistency/README.md](modules/academic-research-suite/ars/scripts/fixtures/cross_document_consistency/README.md)
- [ars/scripts/fixtures/revision_claim_drift_v2/README.md](modules/academic-research-suite/ars/scripts/fixtures/revision_claim_drift_v2/README.md)
- [ars/scripts/fixtures/submission_package/clean/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/clean/paper.md)
- [ars/scripts/fixtures/submission_package/fallback_authoryear/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/fallback_authoryear/paper.md)
- [ars/scripts/fixtures/submission_package/marker_no_join/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/marker_no_join/paper.md)
- [ars/scripts/fixtures/submission_package/orphan_intext/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/orphan_intext/paper.md)
- [ars/scripts/fixtures/submission_package/summary_join/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/summary_join/paper.md)
- [ars/scripts/fixtures/submission_package/uncited_reference/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/uncited_reference/paper.md)
- [ars/scripts/fixtures/submission_package/venue_clean/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/venue_clean/paper.md)
- [ars/scripts/fixtures/submission_package/venue_violations/paper.md](modules/academic-research-suite/ars/scripts/fixtures/submission_package/venue_violations/paper.md)
- [ars/scripts/fixtures/tortured_phrase_screening/own_draft.md](modules/academic-research-suite/ars/scripts/fixtures/tortured_phrase_screening/own_draft.md)
- [ars/scripts/fixtures/transport_bodies/chinese_literature/README.md](modules/academic-research-suite/ars/scripts/fixtures/transport_bodies/chinese_literature/README.md)
- [ars/scripts/fixtures/transport_bodies/README.md](modules/academic-research-suite/ars/scripts/fixtures/transport_bodies/README.md)
- [ars/SECURITY.md](modules/academic-research-suite/ars/SECURITY.md)
- [ars/shared/agents/compliance_agent.md](modules/academic-research-suite/ars/shared/agents/compliance_agent.md)
- [ars/shared/artifact_reproducibility_pattern.md](modules/academic-research-suite/ars/shared/artifact_reproducibility_pattern.md)
- [ars/shared/benchmark_report_pattern.md](modules/academic-research-suite/ars/shared/benchmark_report_pattern.md)
- [ars/shared/bibliographic_integrity_signals.md](modules/academic-research-suite/ars/shared/bibliographic_integrity_signals.md)
- [ars/shared/collaboration_depth_rubric.md](modules/academic-research-suite/ars/shared/collaboration_depth_rubric.md)
- [ars/shared/compliance_checkpoint_protocol.md](modules/academic-research-suite/ars/shared/compliance_checkpoint_protocol.md)
- [ars/shared/contracts/README.md](modules/academic-research-suite/ars/shared/contracts/README.md)
- [ars/shared/cross_model_verification.md](modules/academic-research-suite/ars/shared/cross_model_verification.md)
- [ars/shared/ground_truth_isolation_pattern.md](modules/academic-research-suite/ars/shared/ground_truth_isolation_pattern.md)
- [ars/shared/handoff_schemas.md](modules/academic-research-suite/ars/shared/handoff_schemas.md)
- [ars/shared/mode_spectrum.md](modules/academic-research-suite/ars/shared/mode_spectrum.md)
- [ars/shared/model_tiering.md](modules/academic-research-suite/ars/shared/model_tiering.md)
- [ars/shared/output_language_pair.md](modules/academic-research-suite/ars/shared/output_language_pair.md)
- [ars/shared/policy_data/nature_policy.md](modules/academic-research-suite/ars/shared/policy_data/nature_policy.md)
- [ars/shared/prisma_trAIce_protocol.md](modules/academic-research-suite/ars/shared/prisma_trAIce_protocol.md)
- [ars/shared/raise_framework.md](modules/academic-research-suite/ars/shared/raise_framework.md)
- [ars/shared/references/authority_content_coverage_advisory_protocol.md](modules/academic-research-suite/ars/shared/references/authority_content_coverage_advisory_protocol.md)
- [ars/shared/references/claim_standing_candidate_ledger_protocol.md](modules/academic-research-suite/ars/shared/references/claim_standing_candidate_ledger_protocol.md)
- [ars/shared/references/claim_strength_ladder.md](modules/academic-research-suite/ars/shared/references/claim_strength_ladder.md)
- [ars/shared/references/cross_document_consistency_advisory_protocol.md](modules/academic-research-suite/ars/shared/references/cross_document_consistency_advisory_protocol.md)
- [ars/shared/references/evidence_row_protocol.md](modules/academic-research-suite/ars/shared/references/evidence_row_protocol.md)
- [ars/shared/references/firm_rules.md](modules/academic-research-suite/ars/shared/references/firm_rules.md)
- [ars/shared/references/human_subjects_authority_protocol.md](modules/academic-research-suite/ars/shared/references/human_subjects_authority_protocol.md)
- [ars/shared/references/intent_clarification_protocol.md](modules/academic-research-suite/ars/shared/references/intent_clarification_protocol.md)
- [ars/shared/references/irb_terminology_glossary.md](modules/academic-research-suite/ars/shared/references/irb_terminology_glossary.md)
- [ars/shared/references/per_source_method_weaknesses.md](modules/academic-research-suite/ars/shared/references/per_source_method_weaknesses.md)
- [ars/shared/references/protected_hedging_phrases.md](modules/academic-research-suite/ars/shared/references/protected_hedging_phrases.md)
- [ars/shared/references/psychometric_terminology_glossary.md](modules/academic-research-suite/ars/shared/references/psychometric_terminology_glossary.md)
- [ars/shared/references/review_criteria_consumer_protocol.md](modules/academic-research-suite/ars/shared/references/review_criteria_consumer_protocol.md)
- [ars/shared/references/review_form_note.md](modules/academic-research-suite/ars/shared/references/review_form_note.md)
- [ars/shared/references/review_pathway_rule_trace_protocol.md](modules/academic-research-suite/ars/shared/references/review_pathway_rule_trace_protocol.md)
- [ars/shared/references/routing_core.md](modules/academic-research-suite/ars/shared/references/routing_core.md)
- [ars/shared/references/submission_packet_manifest_protocol.md](modules/academic-research-suite/ars/shared/references/submission_packet_manifest_protocol.md)
- [ars/shared/references/word_count_conventions.md](modules/academic-research-suite/ars/shared/references/word_count_conventions.md)
- [ars/shared/style_calibration_protocol.md](modules/academic-research-suite/ars/shared/style_calibration_protocol.md)
- [ars/shared/templates/codex_audit_multifile_template.md](modules/academic-research-suite/ars/shared/templates/codex_audit_multifile_template.md)
- [ars/sr-screener/agents/protocol_architect_agent.md](modules/academic-research-suite/ars/sr-screener/agents/protocol_architect_agent.md)
- [ars/sr-screener/agents/qc_auditor_agent.md](modules/academic-research-suite/ars/sr-screener/agents/qc_auditor_agent.md)
- [ars/sr-screener/agents/reporter_agent.md](modules/academic-research-suite/ars/sr-screener/agents/reporter_agent.md)
- [ars/sr-screener/agents/screening_reviewer_agent.md](modules/academic-research-suite/ars/sr-screener/agents/screening_reviewer_agent.md)
- [ars/sr-screener/examples/example_protocol_dta.md](modules/academic-research-suite/ars/sr-screener/examples/example_protocol_dta.md)
- [ars/sr-screener/examples/quick_screen_example.md](modules/academic-research-suite/ars/sr-screener/examples/quick_screen_example.md)
- [ars/sr-screener/references/decision_rules.md](modules/academic-research-suite/ars/sr-screener/references/decision_rules.md)
- [ars/sr-screener/references/failure_paths.md](modules/academic-research-suite/ars/sr-screener/references/failure_paths.md)
- [ars/sr-screener/references/orchestration.md](modules/academic-research-suite/ars/sr-screener/references/orchestration.md)
- [ars/sr-screener/references/protocol_template.md](modules/academic-research-suite/ars/sr-screener/references/protocol_template.md)
- [ars/sr-screener/references/quality_control.md](modules/academic-research-suite/ars/sr-screener/references/quality_control.md)
- [ars/sr-screener/references/reporting_and_handoff.md](modules/academic-research-suite/ars/sr-screener/references/reporting_and_handoff.md)
- [ars/sr-screener/references/reviewer_roles.md](modules/academic-research-suite/ars/sr-screener/references/reviewer_roles.md)
- [ars/sr-screener/templates/prompts.md](modules/academic-research-suite/ars/sr-screener/templates/prompts.md)
- [ars/THIRD_PARTY.md](modules/academic-research-suite/ars/THIRD_PARTY.md)
- [ars/tools/release-discipline/README.md](modules/academic-research-suite/ars/tools/release-discipline/README.md)
- [codex/agents/academic-paper-team.md](modules/academic-research-suite/codex/agents/academic-paper-team.md)
- [codex/agents/academic-pipeline-orchestrator.md](modules/academic-research-suite/codex/agents/academic-pipeline-orchestrator.md)
- [codex/agents/deep-research-team.md](modules/academic-research-suite/codex/agents/deep-research-team.md)
- [codex/agents/experiment-team.md](modules/academic-research-suite/codex/agents/experiment-team.md)
- [codex/agents/paper-reviewer-panel.md](modules/academic-research-suite/codex/agents/paper-reviewer-panel.md)
- [codex/agents/sr-screener-team.md](modules/academic-research-suite/codex/agents/sr-screener-team.md)
- [codex/audits/2026-09-06-model-alignment.md](modules/academic-research-suite/codex/audits/2026-09-06-model-alignment.md)
- [codex/compatibility-matrix.md](modules/academic-research-suite/codex/compatibility-matrix.md)
- [codex/hooks/README.md](modules/academic-research-suite/codex/hooks/README.md)
- [codex/model-runtime-policy.md](modules/academic-research-suite/codex/model-runtime-policy.md)
- [codex/README.md](modules/academic-research-suite/codex/README.md)
- [codex/tests/fixtures/reviewer_full_independent_sections.md](modules/academic-research-suite/codex/tests/fixtures/reviewer_full_independent_sections.md)
- [codex/topology-experiment/README.md](modules/academic-research-suite/codex/topology-experiment/README.md)
- [codex/topology-experiment/results/REPORT.md](modules/academic-research-suite/codex/topology-experiment/results/REPORT.md)
- [codex/topology-experiment/rubrics/pipeline-audit.md](modules/academic-research-suite/codex/topology-experiment/rubrics/pipeline-audit.md)
- [codex/topology-experiment/rubrics/reviewer.md](modules/academic-research-suite/codex/topology-experiment/rubrics/reviewer.md)
- [EXTERNAL_RESOURCES.md](modules/academic-research-suite/EXTERNAL_RESOURCES.md)

### 模板与示例

- [ars/academic-paper/templates/bilingual_abstract_template.md](modules/academic-research-suite/ars/academic-paper/templates/bilingual_abstract_template.md)
- [ars/academic-paper/templates/case_study_template.md](modules/academic-research-suite/ars/academic-paper/templates/case_study_template.md)
- [ars/academic-paper/templates/conference_paper_template.md](modules/academic-research-suite/ars/academic-paper/templates/conference_paper_template.md)
- [ars/academic-paper/templates/credit_statement_template.md](modules/academic-research-suite/ars/academic-paper/templates/credit_statement_template.md)
- [ars/academic-paper/templates/funding_statement_template.md](modules/academic-research-suite/ars/academic-paper/templates/funding_statement_template.md)
- [ars/academic-paper/templates/imrad_template.md](modules/academic-research-suite/ars/academic-paper/templates/imrad_template.md)
- [ars/academic-paper/templates/latex_article_template.tex](modules/academic-research-suite/ars/academic-paper/templates/latex_article_template.tex)
- [ars/academic-paper/templates/literature_review_template.md](modules/academic-research-suite/ars/academic-paper/templates/literature_review_template.md)
- [ars/academic-paper/templates/policy_brief_template.md](modules/academic-research-suite/ars/academic-paper/templates/policy_brief_template.md)
- [ars/academic-paper/templates/revision_tracking_template.md](modules/academic-research-suite/ars/academic-paper/templates/revision_tracking_template.md)
- [ars/academic-paper/templates/theoretical_paper_template.md](modules/academic-research-suite/ars/academic-paper/templates/theoretical_paper_template.md)
- [ars/academic-paper-reviewer/templates/editorial_decision_template.md](modules/academic-research-suite/ars/academic-paper-reviewer/templates/editorial_decision_template.md)
- [ars/academic-paper-reviewer/templates/peer_review_report_template.md](modules/academic-research-suite/ars/academic-paper-reviewer/templates/peer_review_report_template.md)
- [ars/academic-paper-reviewer/templates/revision_response_template.md](modules/academic-research-suite/ars/academic-paper-reviewer/templates/revision_response_template.md)
- [ars/academic-pipeline/templates/pipeline_status_template.md](modules/academic-research-suite/ars/academic-pipeline/templates/pipeline_status_template.md)
- [ars/deep-research/templates/evidence_assessment_template.md](modules/academic-research-suite/ars/deep-research/templates/evidence_assessment_template.md)
- [ars/deep-research/templates/literature_matrix_template.md](modules/academic-research-suite/ars/deep-research/templates/literature_matrix_template.md)
- [ars/deep-research/templates/preregistration_template.md](modules/academic-research-suite/ars/deep-research/templates/preregistration_template.md)
- [ars/deep-research/templates/prisma_protocol_template.md](modules/academic-research-suite/ars/deep-research/templates/prisma_protocol_template.md)
- [ars/deep-research/templates/prisma_report_template.md](modules/academic-research-suite/ars/deep-research/templates/prisma_report_template.md)
- [ars/deep-research/templates/research_brief_template.md](modules/academic-research-suite/ars/deep-research/templates/research_brief_template.md)
- [ars/experiment-agent/templates/code_experiment_plan.md](modules/academic-research-suite/ars/experiment-agent/templates/code_experiment_plan.md)
- [ars/experiment-agent/templates/output_formats.md](modules/academic-research-suite/ars/experiment-agent/templates/output_formats.md)
- [ars/experiment-agent/templates/study_protocol.md](modules/academic-research-suite/ars/experiment-agent/templates/study_protocol.md)
- [ars/experiment-agent/templates/study_state.example.md](modules/academic-research-suite/ars/experiment-agent/templates/study_state.example.md)
- [ars/experiment-agent/templates/study_state.md](modules/academic-research-suite/ars/experiment-agent/templates/study_state.md)
- [ars/shared/templates/codex_audit_multifile_template.md](modules/academic-research-suite/ars/shared/templates/codex_audit_multifile_template.md)
- [ars/sr-screener/templates/prompts.md](modules/academic-research-suite/ars/sr-screener/templates/prompts.md)
- [ars/sr-screener/templates/screening_config.template.json](modules/academic-research-suite/ars/sr-screener/templates/screening_config.template.json)
- [ars/sr-screener/templates/workflows/ft_screening.template.js](modules/academic-research-suite/ars/sr-screener/templates/workflows/ft_screening.template.js)
- [ars/sr-screener/templates/workflows/ta_screening.template.js](modules/academic-research-suite/ars/sr-screener/templates/workflows/ta_screening.template.js)

## bgpt-paper-search

[完整工作流](modules/bgpt-paper-search/WORKFLOW.md)

Searches BGPT scientific papers by topic or DOI and retrieves claim-level evidence extracted from full text, including experiments, reported statistics, scope, limitations, and provenance. Use for literature reviews, evidence synthesis, and finding experimental details beyond abstracts.

随包脚本 0 项；参考文档 0 项；模板/示例 0 项。

## citation-management

[完整工作流](modules/citation-management/WORKFLOW.md)

Comprehensive citation management for academic research. Search OpenAlex, PubMed, and Google Scholar for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries. This skill should be used when you need to find papers, verify citation information, convert DOIs to BibTeX, or ensure reference accuracy in scientific writing.

随包脚本 8 项；参考文档 12 项；模板/示例 0 项。

### 脚本

- [scripts/_common.py](modules/citation-management/scripts/_common.py) — Shared BibTeX parsing and rendering for the citation-management scripts. Standard library only. The parser here is brace-depth aware. That matters more than it sounds: a regular ex
- [scripts/doi_to_bibtex.py](modules/citation-management/scripts/doi_to_bibtex.py) — DOI to BibTeX Converter Convert DOIs to BibTeX through DOI content negotiation (Crossref/DataCite/mEDRA).
- [scripts/extract_metadata.py](modules/citation-management/scripts/extract_metadata.py) — Metadata Extraction Tool Extract citation metadata from DOI, PMID, arXiv ID, or URL using various APIs.
- [scripts/format_bibtex.py](modules/citation-management/scripts/format_bibtex.py) — BibTeX Formatter and Cleaner Format, clean, sort, and deduplicate BibTeX files. Writing is opt-in: pass --output to write elsewhere, or --in-place to overwrite the input. Neither f
- [scripts/search_google_scholar.py](modules/citation-management/scripts/search_google_scholar.py) — Google Scholar Search Tool Search Google Scholar and export results. Note: This script requires the 'scholarly' library. Install with: uv pip install scholarly
- [scripts/search_openalex.py](modules/citation-management/scripts/search_openalex.py) — OpenAlex Search Tool Search OpenAlex and export results as JSON or BibTeX. OpenAlex provides a documented REST API. Casual keyless requests are supported; set OPENALEX_API_KEY for 
- [scripts/search_pubmed.py](modules/citation-management/scripts/search_pubmed.py) — PubMed Search Tool Search PubMed using E-utilities API and export results.
- [scripts/validate_citations.py](modules/citation-management/scripts/validate_citations.py) — Citation Validation Tool Validate BibTeX files for accuracy, completeness, and format compliance.

### 参考

- [assets/citation_checklist.md](modules/citation-management/assets/citation_checklist.md)
- [references/api_contracts.md](modules/citation-management/references/api_contracts.md)
- [references/best_practices.md](modules/citation-management/references/best_practices.md)
- [references/bibtex_formatting.md](modules/citation-management/references/bibtex_formatting.md)
- [references/citation_validation.md](modules/citation-management/references/citation_validation.md)
- [references/core_workflow.md](modules/citation-management/references/core_workflow.md)
- [references/example_workflows.md](modules/citation-management/references/example_workflows.md)
- [references/google_scholar_search.md](modules/citation-management/references/google_scholar_search.md)
- [references/metadata_extraction.md](modules/citation-management/references/metadata_extraction.md)
- [references/pubmed_search.md](modules/citation-management/references/pubmed_search.md)
- [references/script_reference.md](modules/citation-management/references/script_reference.md)
- [references/search_strategies.md](modules/citation-management/references/search_strategies.md)

## exa-search

[完整工作流](modules/exa-search/WORKFLOW.md)

Searches scientific and technical web content with Exa and extracts page or PDF text from URLs in batches. Supports scholarly discovery with the publication category and academic domain filters. Applies to requests to search the web, look up current research, fetch a page, or extract an article using Exa.

随包脚本 2 项；参考文档 2 项；模板/示例 0 项。

### 脚本

- [scripts/exa_extract.py](modules/exa-search/scripts/exa_extract.py) — Fetch and extract content from URLs using Exa's /contents endpoint. Example: uv run exa_extract.py \ https://arxiv.org/abs/2401.04088 \ https://www.nature.com/articles/s41586-024-0
- [scripts/exa_search.py](modules/exa-search/scripts/exa_search.py) — Run an Exa web search and write results to JSON. Uses the Exa Python SDK. Auth via the EXA_API_KEY environment variable. Example: uv run exa_search.py "transformer architectures" \

### 参考

- [references/web-extract.md](modules/exa-search/references/web-extract.md)
- [references/web-search.md](modules/exa-search/references/web-search.md)

## literature-review

[完整工作流](modules/literature-review/WORKFLOW.md)

Conducts systematic, scoping, and narrative literature reviews using PubMed, arXiv, bioRxiv, Semantic Scholar, and other appropriate sources. Use for research synthesis, reproducible literature searches, screening, citation checking, or preparing Markdown and PDF reviews. Tracks search coverage, records versus studies, and evidence limitations; supports meta-analysis planning but does not supply a meta-analysis engine.

随包脚本 5 项；参考文档 6 项；模板/示例 0 项。

### 脚本

- [scripts/generate_pdf.py](modules/literature-review/scripts/generate_pdf.py) — Render reviewed Markdown with Pandoc/XeLaTeX and optional local CSL bibliography.
- [scripts/generate_schematic.py](modules/literature-review/scripts/generate_schematic.py) — Scientific schematic generation using Nano Banana 2. Generate any scientific diagram by describing it in natural language. Nano Banana 2 handles everything automatically with smart
- [scripts/generate_schematic_ai.py](modules/literature-review/scripts/generate_schematic_ai.py) — AI-powered scientific schematic generation using Nano Banana 2. This script uses a smart iterative refinement approach: 1. Generate initial image with Nano Banana 2 2. AI quality r
- [scripts/search_databases.py](modules/literature-review/scripts/search_databases.py) — Literature Database Search Script Processes normalized search records locally; does not query databases.
- [scripts/verify_citations.py](modules/literature-review/scripts/verify_citations.py) — Check DOI registration and retrieve Crossref metadata for manual citation review. Registration does not establish that a citation supports a claim. Crossref does not cover all DOI 

### 参考

- [assets/review_template.md](modules/literature-review/assets/review_template.md)
- [references/citation_styles.md](modules/literature-review/references/citation_styles.md)
- [references/core_workflow.md](modules/literature-review/references/core_workflow.md)
- [references/database_strategies.md](modules/literature-review/references/database_strategies.md)
- [references/example_workflow.md](modules/literature-review/references/example_workflow.md)
- [references/search_and_citation.md](modules/literature-review/references/search_and_citation.md)

## nature-academic-search

[完整工作流](modules/nature-academic-search/WORKFLOW.md)

Search literature across sources, verify or manage citations, and build MeSH strategies or citation-impact audits. Use for 文献检索、引文核对、参考文献管理、严格他引 and evidence-backed citer profiles; not for translating a paper or drafting manuscript prose.

随包脚本 27 项；参考文档 17 项；模板/示例 0 项。

### 脚本

- [install.sh](modules/nature-academic-search/install.sh) — Academic Search Skill + MCP Server Installer for Claude Code
- [mcp-server/academic_search_server.py](modules/nature-academic-search/mcp-server/academic_search_server.py) — Academic search MCP server. Unified entry point exposing multi-source search and source-specific tools for CrossRef, PubMed, arXiv, Scopus, and ScienceDirect.
- [mcp-server/sources/__init__.py](modules/nature-academic-search/mcp-server/sources/__init__.py) — Data source modules for academic search.
- [mcp-server/sources/arxiv.py](modules/nature-academic-search/mcp-server/sources/arxiv.py) — arXiv data source via REST API (Atom XML feed).
- [mcp-server/sources/crossref.py](modules/nature-academic-search/mcp-server/sources/crossref.py) — CrossRef data source for academic search.
- [mcp-server/sources/elsevier_common.py](modules/nature-academic-search/mcp-server/sources/elsevier_common.py) — Shared helpers for pybliometrics-backed Elsevier sources.
- [mcp-server/sources/pubmed.py](modules/nature-academic-search/mcp-server/sources/pubmed.py) — PubMed data source via NCBI E-utilities API.
- [mcp-server/sources/sciencedirect.py](modules/nature-academic-search/mcp-server/sources/sciencedirect.py) — ScienceDirect data source via pybliometrics.
- [mcp-server/sources/scopus.py](modules/nature-academic-search/mcp-server/sources/scopus.py) — Scopus data source via pybliometrics.
- [mcp-server/tests/__init__.py](modules/nature-academic-search/mcp-server/tests/__init__.py) — Tests for academic search server.
- [mcp-server/tests/test_arxiv_error_entries.py](modules/nature-academic-search/mcp-server/tests/test_arxiv_error_entries.py) — arXiv error entries must not become fake papers.
- [mcp-server/tests/test_citation_errors.py](modules/nature-academic-search/mcp-server/tests/test_citation_errors.py) — Error and missing-data handling for citation output (no network access).
- [mcp-server/tests/test_elsevier_live.py](modules/nature-academic-search/mcp-server/tests/test_elsevier_live.py) — Live API tests for Scopus and ScienceDirect. These tests intentionally call Elsevier APIs through the local pybliometrics configuration. They are not mocked.
- [mcp-server/tests/test_format_converter_hardening.py](modules/nature-academic-search/mcp-server/tests/test_format_converter_hardening.py) — Hardening regression tests for format-converter.py (no network access).
- [mcp-server/tests/test_mcp_tools.py](modules/nature-academic-search/mcp-server/tests/test_mcp_tools.py) — MCP dispatch tests for academic_search_server tools.
- [mcp-server/tests/test_pubmed_parsing.py](modules/nature-academic-search/mcp-server/tests/test_pubmed_parsing.py) — PubMed article parsing edge cases (no network access).
- [mcp-server/tests/test_scopus_empty_result.py](modules/nature-academic-search/mcp-server/tests/test_scopus_empty_result.py) — A Scopus empty result set must not become a fake paper.
- [mcp-server/tests/test_script_converters.py](modules/nature-academic-search/mcp-server/tests/test_script_converters.py) — Regression tests for the stand-alone converter scripts (no network access).
- [mcp-server/tests/test_sources.py](modules/nature-academic-search/mcp-server/tests/test_sources.py) — Unit tests for academic search source modules and ID detection. All external HTTP calls are mocked -- no network access required.
- [mcp-server/utils/__init__.py](modules/nature-academic-search/mcp-server/utils/__init__.py) — Utility modules for academic search.
- [mcp-server/utils/config.py](modules/nature-academic-search/mcp-server/utils/config.py) — Configuration management for academic search server.
- [mcp-server/utils/errors.py](modules/nature-academic-search/mcp-server/utils/errors.py) — Unified error types for academic search operations.
- [mcp-server/utils/logging.py](modules/nature-academic-search/mcp-server/utils/logging.py) — Structured logging for academic search operations.
- [scripts/academic_search.py](modules/nature-academic-search/scripts/academic_search.py) — No-MCP fallback search for nature-academic-search (OpenAlex, stdlib only). This is the graceful-degradation path for agents/environments that do not mount the MCP server (plain CLI
- [scripts/converters.py](modules/nature-academic-search/scripts/converters.py) — Format converters for academic citations. Supports: MEDLINE/.nbib -> RIS/BibTeX/ENW, CrossRef JSON -> RIS/BibTeX/ENW, arXiv XML -> RIS/BibTeX/ENW. Each converter accepts parsed dat
- [scripts/format-converter.py](modules/nature-academic-search/scripts/format-converter.py) — Multi-source citation downloader with format conversion. Sources: PubMed (NCBI E-utilities), CrossRef (REST API), arXiv (Atom API). Outputs: .nbib (PubMed only), .ris, .bib, .enw. 
- [scripts/preflight.py](modules/nature-academic-search/scripts/preflight.py) — Pre-flight API endpoint connectivity checker. Verifies that the 3 direct API endpoints used by format-converter.py are reachable. Uses urllib.request.urlopen (stdlib) for consisten

### 参考

- [mcp-server/.pytest_cache/README.md](modules/nature-academic-search/mcp-server/.pytest_cache/README.md)
- [mcp-server/README.md](modules/nature-academic-search/mcp-server/README.md)
- [README.md](modules/nature-academic-search/README.md)
- [README_EN.md](modules/nature-academic-search/README_EN.md)
- [references/citation-parser.md](modules/nature-academic-search/references/citation-parser.md)
- [references/dedup-engine.md](modules/nature-academic-search/references/dedup-engine.md)
- [references/ris-bibtex-format.md](modules/nature-academic-search/references/ris-bibtex-format.md)
- [references/search-strategy.md](modules/nature-academic-search/references/search-strategy.md)
- [references/source-tiers.md](modules/nature-academic-search/references/source-tiers.md)
- [references/workflows/wf1-multi-source-search.md](modules/nature-academic-search/references/workflows/wf1-multi-source-search.md)
- [references/workflows/wf2-citation-verification.md](modules/nature-academic-search/references/workflows/wf2-citation-verification.md)
- [references/workflows/wf3-mesh-strategy.md](modules/nature-academic-search/references/workflows/wf3-mesh-strategy.md)
- [references/workflows/wf4-citation-file-mgmt.md](modules/nature-academic-search/references/workflows/wf4-citation-file-mgmt.md)
- [references/workflows/wf5-reference-mgmt.md](modules/nature-academic-search/references/workflows/wf5-reference-mgmt.md)
- [references/workflows/wf6-strict-other-citation-impact-audit.md](modules/nature-academic-search/references/workflows/wf6-strict-other-citation-impact-audit.md)
- [static/core/routing-and-ops.md](modules/nature-academic-search/static/core/routing-and-ops.md)
- [static/core/tools.md](modules/nature-academic-search/static/core/tools.md)

## nature-citation

[完整工作流](modules/nature-citation/WORKFLOW.md)

Find and verify Nature/CNS-family literature supporting manuscript claims, with claim-to-source mapping and reference-manager export. Use for Nature系列引用、CNS支撑文献、分段补引用 when this journal scope is requested; use broader literature search for unrestricted sources.

随包脚本 3 项；参考文档 9 项；模板/示例 0 项。

### 脚本

- [scripts/nature_citation.py](modules/nature-citation/scripts/nature_citation.py) — Segment manuscript text, search strict Nature/CNS-family citation candidates, and export a reference-manager file. By default the script writes one inspectable `.ris` file. Optiona
- [tests/test_author_exports.py](modules/nature-citation/tests/test_author_exports.py) — SCRIPT = Path(__file__).parents[1] / "scripts" / "nature_citation.py"
- [tests/test_journal_scope.py](modules/nature-citation/tests/test_journal_scope.py) — SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "nature_citation.py"

### 参考

- [README.md](modules/nature-citation/README.md)
- [README_EN.md](modules/nature-citation/README_EN.md)
- [references/journal-scope.md](modules/nature-citation/references/journal-scope.md)
- [references/ris-endnote.md](modules/nature-citation/references/ris-endnote.md)
- [references/script-usage.md](modules/nature-citation/references/script-usage.md)
- [references/search-strategy.md](modules/nature-citation/references/search-strategy.md)
- [static/core/chinese-mode.md](modules/nature-citation/static/core/chinese-mode.md)
- [static/core/principles.md](modules/nature-citation/static/core/principles.md)
- [static/core/workflow.md](modules/nature-citation/static/core/workflow.md)

## nature-downloader

[完整工作流](modules/nature-downloader/WORKFLOW.md)

Use when a user needs lawful academic full text, CNKI institutional access, English OA retrieval, publisher API access, institutional browser fallback, or supporting information downloads.

随包脚本 51 项；参考文档 6 项；模板/示例 0 项。

### 脚本

- [scripts/batch_download.mjs](modules/nature-downloader/scripts/batch_download.mjs) — // Institution-neutral literature downloader.
- [scripts/browser_pdf_downloader.mjs](modules/nature-downloader/scripts/browser_pdf_downloader.mjs) — DEFAULT_PROXY,
- [scripts/cdp_open_url.mjs](modules/nature-downloader/scripts/cdp_open_url.mjs) — function usage() {
- [scripts/configure_credentials.py](modules/nature-downloader/scripts/configure_credentials.py) — Configure publisher API credentials without echoing secrets.
- [scripts/configure_school.py](modules/nature-downloader/scripts/configure_school.py) — Command line helper for literature-downloader school configuration.
- [scripts/extract_pdf_text.py](modules/nature-downloader/scripts/extract_pdf_text.py) — def configure_utf8_stdio():
- [scripts/lib/anti-bot.mjs](modules/nature-downloader/scripts/lib/anti-bot.mjs) — // Automatic verification challenge handler for the literature downloader.
- [scripts/lib/cdp-utils.mjs](modules/nature-downloader/scripts/lib/cdp-utils.mjs) — // Shared CDP proxy client for nature-downloader scripts.
- [scripts/lib/cnki.mjs](modules/nature-downloader/scripts/lib/cnki.mjs) — waitForComplete,
- [scripts/lib/credentials.mjs](modules/nature-downloader/scripts/lib/credentials.mjs) — const PROVIDERS = new Set(PUBLISHER_PROVIDERS);
- [scripts/lib/direct-download.mjs](modules/nature-downloader/scripts/lib/direct-download.mjs) — export function safeArticleBasename(title = "", doi = "") {
- [scripts/lib/manifest.mjs](modules/nature-downloader/scripts/lib/manifest.mjs) — const SECRET_KEY_RE = /(?:api[_-]?key|secret|password|cookie|session|authtoken|insttoken|access[_-]?token|authorization)/i;
- [scripts/lib/metadata.mjs](modules/nature-downloader/scripts/lib/metadata.mjs) — export function normalizeDoi(value = "") {
- [scripts/lib/open-access-provider.mjs](modules/nature-downloader/scripts/lib/open-access-provider.mjs) — findPmcCandidates,
- [scripts/lib/open-access.mjs](modules/nature-downloader/scripts/lib/open-access.mjs) — export function normalizeTitle(title = "") {
- [scripts/lib/pdf-utils.mjs](modules/nature-downloader/scripts/lib/pdf-utils.mjs) — // PDF fetch + disk-streaming helpers for nature-downloader.
- [scripts/lib/provider-registry.mjs](modules/nature-downloader/scripts/lib/provider-registry.mjs) — const file = new URL("../../data/publishers.json", import.meta.url);
- [scripts/lib/provider-utils.mjs](modules/nature-downloader/scripts/lib/provider-utils.mjs) — const LOGIN_RE = /\b(?:log[ -]?in|sign[ -]?in|password|authentication required|access denied|forbidden)\b|登录|统一身份认证|无权访问/i;
- [scripts/lib/publisher-providers.mjs](modules/nature-downloader/scripts/lib/publisher-providers.mjs) — export const PROVIDER_CONFIG_URLS = Object.freeze(Object.fromEntries(
- [scripts/lib/routing.mjs](modules/nature-downloader/scripts/lib/routing.mjs) — export function parseSiChoice({ si = false, noSi = false } = {}) {
- [scripts/lib/school-config.mjs](modules/nature-downloader/scripts/lib/school-config.mjs) — export const DEFAULT_DISCOVERY_URL = "https://www.webofscience.com/wos/woscc/basic-search";
- [scripts/lib/settings.mjs](modules/nature-downloader/scripts/lib/settings.mjs) — export function settingsPathFromEnv(env = process.env) {
- [scripts/lib/status-codes.mjs](modules/nature-downloader/scripts/lib/status-codes.mjs) — // Status codes for nature-downloader.
- [scripts/lib/wos-supporting-information.mjs](modules/nature-downloader/scripts/lib/wos-supporting-information.mjs) — const SUPPLEMENT_LABEL = /(?:supporting\s+information|supplement(?:ary|al)?(?:\s+(?:information|material|data|file|table|figure|video))?|source\s+data|\bmmc\d+\b)/i;
- [scripts/retry_elsevier_api.mjs](modules/nature-downloader/scripts/retry_elsevier_api.mjs) — // Deprecated compatibility wrapper. The canonical Elsevier implementation is
- [src/config.py](modules/nature-downloader/src/config.py) — 配置读写模块。 负责 school.json 的读取、写入、校验、备份。 配置路径：~/.config/lit-dl/school.json
- [src/health_check.py](modules/nature-downloader/src/health_check.py) — 连通性自检模块。 下载前对配置做轻量可达性探测，结果缓存 10 分钟。 失败时给出具体排查建议。
- [src/schools_loader.py](modules/nature-downloader/src/schools_loader.py) — Optional user-maintained institution preset loader. The distributed schools.yaml is intentionally empty.
- [src/validators.py](modules/nature-downloader/src/validators.py) — 字段校验模块。 对用户填写的配置字段做实时可达性探测： - sso_domain: DNS 解析 + TCP 443 + HTTPS 证书 - carsi_entry: HTTP GET 探测 - ezproxy_url: HTTP GET 探测登录表单 所有校验函数返回 (ok: bool, message: str)。
- [src/wizard.py](modules/nature-downloader/src/wizard.py) — 配置向导模块。 7 步交互式配置流程，供 AI 调用。 每一步返回一个 prompt 给用户，并接收用户输入进行校验。 使用方式（AI 调用）： from wizard import Wizard w = Wizard() # Step 1 prompt = w.start() # 返回给用户的提问 # 用户回答后 result = w.handle_ste
- [tests/python/test_config_credentials.py](modules/nature-downloader/tests/python/test_config_credentials.py) — ROOT = Path(__file__).resolve().parents[2]
- [tests/python/test_config_wizard.py](modules/nature-downloader/tests/python/test_config_wizard.py) — ROOT = Path(__file__).resolve().parents[2]
- [tests/python/test_credential_validation.py](modules/nature-downloader/tests/python/test_credential_validation.py) — SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "configure_credentials.py"
- [tests/python/test_springer_services.py](modules/nature-downloader/tests/python/test_springer_services.py) — SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "configure_credentials.py"
- [tests/unit/batch-cli.test.mjs](modules/nature-downloader/tests/unit/batch-cli.test.mjs) — describe("batch CLI contract", () => {
- [tests/unit/cnki.test.mjs](modules/nature-downloader/tests/unit/cnki.test.mjs) — DEFAULT_CNKI_URL,
- [tests/unit/credentials.test.mjs](modules/nature-downloader/tests/unit/credentials.test.mjs) — credentialsPathFromEnv,
- [tests/unit/direct-download-collision.test.mjs](modules/nature-downloader/tests/unit/direct-download-collision.test.mjs) — function pdfResponse(text) {
- [tests/unit/generic-package.test.mjs](modules/nature-downloader/tests/unit/generic-package.test.mjs) — const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
- [tests/unit/manifest.test.mjs](modules/nature-downloader/tests/unit/manifest.test.mjs) — test("manifest records route and SI choice without secrets", () => {
- [tests/unit/metadata.test.mjs](modules/nature-downloader/tests/unit/metadata.test.mjs) — describe("metadata normalization", () => {
- [tests/unit/open-access-provider.test.mjs](modules/nature-downloader/tests/unit/open-access-provider.test.mjs) — describe("OA provider waterfall", () => {
- [tests/unit/open-access.test.mjs](modules/nature-downloader/tests/unit/open-access.test.mjs) — exactTitleMatch,
- [tests/unit/pdf-utils-atomic-write.test.mjs](modules/nature-downloader/tests/unit/pdf-utils-atomic-write.test.mjs) — describe("browser download file writes", () => {
- [tests/unit/provider-utils.test.mjs](modules/nature-downloader/tests/unit/provider-utils.test.mjs) — classifyFullTextContent,
- [tests/unit/publisher-providers.test.mjs](modules/nature-downloader/tests/unit/publisher-providers.test.mjs) — function response(body, { status = 200, contentType = "application/pdf" } = {}) {
- [tests/unit/routing.test.mjs](modules/nature-downloader/tests/unit/routing.test.mjs) — classifyPublisher,
- [tests/unit/school-config.test.mjs](modules/nature-downloader/tests/unit/school-config.test.mjs) — configPathFromEnv,
- [tests/unit/springer-services.test.mjs](modules/nature-downloader/tests/unit/springer-services.test.mjs) — const article = { doi: "10.1007/example", title: "Springer services" };
- [tests/unit/status-codes.test.mjs](modules/nature-downloader/tests/unit/status-codes.test.mjs) — // Unit tests for scripts/lib/status-codes.mjs and scripts/lib/pdf-utils.mjs
- [tests/unit/wos-supporting-information.test.mjs](modules/nature-downloader/tests/unit/wos-supporting-information.test.mjs) — articleBundleDirectory,

### 参考

- [docs/nature-downloader-reference-research-2026-07-15.md](modules/nature-downloader/docs/nature-downloader-reference-research-2026-07-15.md)
- [docs/superpowers/plans/2026-06-21-nature-downloader-merge.md](modules/nature-downloader/docs/superpowers/plans/2026-06-21-nature-downloader-merge.md)
- [README.md](modules/nature-downloader/README.md)
- [README_EN.md](modules/nature-downloader/README_EN.md)
- [references/delivery-verification-and-failures.md](modules/nature-downloader/references/delivery-verification-and-failures.md)
- [references/institutional-browser-workflow.md](modules/nature-downloader/references/institutional-browser-workflow.md)

## nature-literature-pipeline

[完整工作流](modules/nature-literature-pipeline/WORKFLOW.md)

Complete automated literature discovery pipeline: multi-source search → six-dimension scoring → fine reading → formatted delivery → archival.
Combines a configurable engine with daily cron-driven application layer. Works with Feishu, Telegram, or any messaging platform.


随包脚本 0 项；参考文档 9 项；模板/示例 1 项。

### 参考

- [README.md](modules/nature-literature-pipeline/README.md)
- [README_EN.md](modules/nature-literature-pipeline/README_EN.md)
- [references/cron-setup.md](modules/nature-literature-pipeline/references/cron-setup.md)
- [references/gap-analysis.md](modules/nature-literature-pipeline/references/gap-analysis.md)
- [references/note-template.md](modules/nature-literature-pipeline/references/note-template.md)
- [references/push-format.md](modules/nature-literature-pipeline/references/push-format.md)
- [references/review-compilation-workflow.md](modules/nature-literature-pipeline/references/review-compilation-workflow.md)
- [references/scoring-system.md](modules/nature-literature-pipeline/references/scoring-system.md)
- [templates/literature-push-template.md](modules/nature-literature-pipeline/templates/literature-push-template.md)

### 模板与示例

- [templates/literature-push-template.md](modules/nature-literature-pipeline/templates/literature-push-template.md)

## nature-paper-card

[完整工作流](modules/nature-paper-card/WORKFLOW.md)

Build a structured deep-reading Paper Card for one scientific paper, analysing methods, experiment-to-claim evidence, limitations, and research ideas. Use for 论文精读卡、方法拆解、证据链分析; not full-paper bilingual translation or formal peer review.

随包脚本 4 项；参考文档 16 项；模板/示例 0 项。

### 脚本

- [scripts/audit_paper_card.py](modules/nature-paper-card/scripts/audit_paper_card.py) — Audit a Paper Card against its source bundle and output contract.
- [scripts/prepare_paper.py](modules/nature-paper-card/scripts/prepare_paper.py) — Prepare a stable source bundle for the nature-paper-card workflow.
- [tests/test_audit_page_ranges.py](modules/nature-paper-card/tests/test_audit_page_ranges.py) — SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_paper_card.py"
- [tests/test_prepare_paper.py](modules/nature-paper-card/tests/test_prepare_paper.py) — Regression tests for source-map page-locator normalization.

### 参考

- [README.md](modules/nature-paper-card/README.md)
- [README_EN.md](modules/nature-paper-card/README_EN.md)
- [references/card-schema.md](modules/nature-paper-card/references/card-schema.md)
- [references/evidence-and-provenance.md](modules/nature-paper-card/references/evidence-and-provenance.md)
- [references/nature-paper-card-tutorial.md](modules/nature-paper-card/references/nature-paper-card-tutorial.md)
- [references/nature-paper-card-tutorial_EN.md](modules/nature-paper-card/references/nature-paper-card-tutorial_EN.md)
- [references/research-idea-gates.md](modules/nature-paper-card/references/research-idea-gates.md)
- [static/core/output-contract.md](modules/nature-paper-card/static/core/output-contract.md)
- [static/core/principles.md](modules/nature-paper-card/static/core/principles.md)
- [static/core/workflow.md](modules/nature-paper-card/static/core/workflow.md)
- [static/fragments/paper_type/clinical.md](modules/nature-paper-card/static/fragments/paper_type/clinical.md)
- [static/fragments/paper_type/discovery.md](modules/nature-paper-card/static/fragments/paper_type/discovery.md)
- [static/fragments/paper_type/materials.md](modules/nature-paper-card/static/fragments/paper_type/materials.md)
- [static/fragments/paper_type/methods.md](modules/nature-paper-card/static/fragments/paper_type/methods.md)
- [static/fragments/paper_type/resource.md](modules/nature-paper-card/static/fragments/paper_type/resource.md)
- [static/fragments/paper_type/review.md](modules/nature-paper-card/static/fragments/paper_type/review.md)

## nature-paper-trans

[完整工作流](modules/nature-paper-trans/WORKFLOW.md)

将英文论文 PDF 的指定页面或全文逐页翻译为简体中文图片型 PDF，尽量保留原文的版式、分栏、图表和公式；最终仅交付中文 PDF。用于论文阅读翻译，不用于可编辑 Word 重建或逐字审校。

随包脚本 5 项；参考文档 3 项；模板/示例 0 项。

### 脚本

- [scripts/pages.py](modules/nature-paper-trans/scripts/pages.py) — Prepare reference pages and assemble externally generated images; never call AI.
- [tests/test_json_channel.py](modules/nature-paper-trans/tests/test_json_channel.py) — SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "pages.py"
- [tests/test_pages.py](modules/nature-paper-trans/tests/test_pages.py) — Exercise isolated page jobs with temporary PDFs/PNGs; never call image generation.
- [tests/test_pdf_publication.py](modules/nature-paper-trans/tests/test_pdf_publication.py) — SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "pages.py"
- [tests/test_review_gate.py](modules/nature-paper-trans/tests/test_review_gate.py) — SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "pages.py"

### 参考

- [README.md](modules/nature-paper-trans/README.md)
- [README_EN.md](modules/nature-paper-trans/README_EN.md)
- [references/image-translation-prompt.md](modules/nature-paper-trans/references/image-translation-prompt.md)

## nature-paper-xray

[完整工作流](modules/nature-paper-xray/WORKFLOW.md)

Read one supplied paper closely enough to reconstruct how its authors actually got there, rather than restating what the abstract claims. Use for 精读论文, 讲透这篇论文, 把这篇读懂, 作者为什么这么设计, 这个公式怎么推出来的, paper x-ray, and deep single-paper comprehension before building on, reviewing, presenting, or citing that paper. Recovers the real starting point and the bet the authors placed, separates load-bearing design from decoration, grounds each key formula in a worked micro-example with concrete numbers, and checks how far the evidence actually reaches, including where the authors are confident and where the paper does not report something. Delivers a structured Markdown long-read by default. Not a summary, not a translation, not a peer review.

随包脚本 0 项；参考文档 4 项；模板/示例 0 项。

### 参考

- [README.md](modules/nature-paper-xray/README.md)
- [README_EN.md](modules/nature-paper-xray/README_EN.md)
- [references/deep-reading-protocol.md](modules/nature-paper-xray/references/deep-reading-protocol.md)
- [references/evidence-boundary.md](modules/nature-paper-xray/references/evidence-boundary.md)

## nature-reader

[完整工作流](modules/nature-reader/WORKFLOW.md)

Create source-grounded Chinese-English paper readers with aligned text, figures, tables, and equations. Use for 全文翻译、中英文对照、论文精读 or source-linked questions about a paper; respect a requested excerpt or question without generating a full reader.

随包脚本 1 项；参考文档 15 项；模板/示例 0 项。

### 脚本

- [scripts/validate_reader_math.py](modules/nature-reader/scripts/validate_reader_math.py) — Validate equation rendering and traceability in a nature-reader bundle.

### 参考

- [README.md](modules/nature-reader/README.md)
- [README_EN.md](modules/nature-reader/README_EN.md)
- [references/article-anatomy.md](modules/nature-reader/references/article-anatomy.md)
- [references/equation-handling.md](modules/nature-reader/references/equation-handling.md)
- [references/figure-extraction.md](modules/nature-reader/references/figure-extraction.md)
- [references/grounding-rules.md](modules/nature-reader/references/grounding-rules.md)
- [references/output-spec.md](modules/nature-reader/references/output-spec.md)
- [static/core/output-contract.md](modules/nature-reader/static/core/output-contract.md)
- [static/core/principles.md](modules/nature-reader/static/core/principles.md)
- [static/core/workflow.md](modules/nature-reader/static/core/workflow.md)
- [static/fragments/source/doi-arxiv.md](modules/nature-reader/static/fragments/source/doi-arxiv.md)
- [static/fragments/source/html.md](modules/nature-reader/static/fragments/source/html.md)
- [static/fragments/source/pasted-text.md](modules/nature-reader/static/fragments/source/pasted-text.md)
- [static/fragments/source/pdf-text.md](modules/nature-reader/static/fragments/source/pdf-text.md)
- [static/fragments/source/scanned-pdf.md](modules/nature-reader/static/fragments/source/scanned-pdf.md)

## nature-ref-verifier

[完整工作流](modules/nature-ref-verifier/WORKFLOW.md)

对学术文献逐条执行多源交叉验证，逐字段对比作者、标题、年份、卷期、页码， 标记卷年/DOI年冲突、作者顺序异常、页码偏差等问题，输出结构化验证报告。 可批量处理整篇论文/开题报告的参考文献列表，也可单条校验，支持与 Zotero 同步修正。

随包脚本 0 项；参考文档 3 项；模板/示例 0 项。

### 参考

- [README.md](modules/nature-ref-verifier/README.md)
- [README_EN.md](modules/nature-ref-verifier/README_EN.md)
- [references/common-patterns.md](modules/nature-ref-verifier/references/common-patterns.md)

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

## paper-lookup

[完整工作流](modules/paper-lookup/WORKFLOW.md)

Searches 18 scholarly APIs for papers, preprints, citations, open-access full text, repository records, and journal OA status, and returns results with reproducible provenance. Covers PubMed, PMC, Europe PMC, bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall, OpenCitations, PubTator3, Zenodo, Figshare, ROR, BioStudies, and DOAJ. Use when searching for papers, citations, DOI/PMID/arXiv lookups, abstracts, full text, open-access PDFs, preprints, citation graphs, author publications, biomedical entity annotations, deposited records (Zenodo, Figshare, BioStudies), institution ROR IDs, or any scholarly literature query. Triggers on mentions of any supported database or requests like "find papers on X", "look up this DOI", "who cites this paper", or "get me the PDF".

随包脚本 5 项；参考文档 18 项；模板/示例 0 项。

### 脚本

- [scripts/_common.py](modules/paper-lookup/scripts/_common.py) — Shared helpers for the paper-lookup scripts. Standard library only. Three concerns are factored out here because all four CLIs need them and getting any of them subtly wrong is how
- [scripts/arxiv_atom.py](modules/paper-lookup/scripts/arxiv_atom.py) — Parse arXiv Atom XML into JSON records, catching arXiv's HTTP-200 failures. arXiv has no JSON output, and its Atom feed has four traps that make hand-rolled parsing quietly wrong (
- [scripts/jats_to_text.py](modules/paper-lookup/scripts/jats_to_text.py) — Turn PMC / Europe PMC JATS XML into sectioned text, refusing metadata-only XML. The failure this exists to stop: NCBI eFetch returns **HTTP 200** and a well-formed `<pmc-articleset
- [scripts/openalex_abstract.py](modules/paper-lookup/scripts/openalex_abstract.py) — Reconstruct OpenAlex abstracts from `abstract_inverted_index`. OpenAlex never returns an abstract as a string. It returns `{"word": [positions], ...}`, and the caller has to invert
- [scripts/paginate.py](modules/paper-lookup/scripts/paginate.py) — Bounded, rate-limited, count-reconciling pagination for this skill's APIs. The five database adapters here paginate differently -- absolute record offsets or opaque cursors -- and 

### 参考

- [references/arxiv.md](modules/paper-lookup/references/arxiv.md)
- [references/biorxiv.md](modules/paper-lookup/references/biorxiv.md)
- [references/biostudies.md](modules/paper-lookup/references/biostudies.md)
- [references/core.md](modules/paper-lookup/references/core.md)
- [references/crossref.md](modules/paper-lookup/references/crossref.md)
- [references/doaj.md](modules/paper-lookup/references/doaj.md)
- [references/europepmc.md](modules/paper-lookup/references/europepmc.md)
- [references/figshare.md](modules/paper-lookup/references/figshare.md)
- [references/medrxiv.md](modules/paper-lookup/references/medrxiv.md)
- [references/openalex.md](modules/paper-lookup/references/openalex.md)
- [references/opencitations.md](modules/paper-lookup/references/opencitations.md)
- [references/pmc.md](modules/paper-lookup/references/pmc.md)
- [references/pubmed.md](modules/paper-lookup/references/pubmed.md)
- [references/pubtator.md](modules/paper-lookup/references/pubtator.md)
- [references/ror.md](modules/paper-lookup/references/ror.md)
- [references/semantic-scholar.md](modules/paper-lookup/references/semantic-scholar.md)
- [references/unpaywall.md](modules/paper-lookup/references/unpaywall.md)
- [references/zenodo.md](modules/paper-lookup/references/zenodo.md)

## parallel-web

[完整工作流](modules/parallel-web/WORKFLOW.md)

Uses Parallel CLI for web search, URL extraction, deep research, structured data enrichment, entity discovery, and recurring web monitoring. Best for requests that explicitly need current web evidence, academic-source discovery, repeated entity lookups, exhaustive reports, or ongoing change tracking.

随包脚本 0 项；参考文档 7 项；模板/示例 0 项。

### 参考

- [references/api-contracts.md](modules/parallel-web/references/api-contracts.md)
- [references/data-enrichment.md](modules/parallel-web/references/data-enrichment.md)
- [references/deep-research.md](modules/parallel-web/references/deep-research.md)
- [references/findall.md](modules/parallel-web/references/findall.md)
- [references/monitor.md](modules/parallel-web/references/monitor.md)
- [references/web-extract.md](modules/parallel-web/references/web-extract.md)
- [references/web-search.md](modules/parallel-web/references/web-search.md)

## pyzotero

[完整工作流](modules/pyzotero/WORKFLOW.md)

Manages Zotero reference libraries using the pyzotero Python client: retrieves, creates, updates, and deletes items, collections, tags, and attachments via the Zotero Web API v3 or local API. Applies when working with Zotero libraries programmatically, managing bibliographic references, exporting citations, searching library contents, uploading PDF attachments, or building research automation workflows that integrate with Zotero.

随包脚本 0 项；参考文档 14 项；模板/示例 0 项。

### 参考

- [references/authentication.md](modules/pyzotero/references/authentication.md)
- [references/cli.md](modules/pyzotero/references/cli.md)
- [references/collections.md](modules/pyzotero/references/collections.md)
- [references/error-handling.md](modules/pyzotero/references/error-handling.md)
- [references/exports.md](modules/pyzotero/references/exports.md)
- [references/files-attachments.md](modules/pyzotero/references/files-attachments.md)
- [references/full-text.md](modules/pyzotero/references/full-text.md)
- [references/mcp.md](modules/pyzotero/references/mcp.md)
- [references/pagination.md](modules/pyzotero/references/pagination.md)
- [references/read-api.md](modules/pyzotero/references/read-api.md)
- [references/saved-searches.md](modules/pyzotero/references/saved-searches.md)
- [references/search-params.md](modules/pyzotero/references/search-params.md)
- [references/tags.md](modules/pyzotero/references/tags.md)
- [references/write-api.md](modules/pyzotero/references/write-api.md)

## research-lookup

[完整工作流](modules/research-lookup/WORKFLOW.md)

Compiles current scholarly evidence for a scientific manuscript or research brief when the user explicitly asks to gather literature, references, background evidence, competing findings, or a manuscript research packet. Uses Parallel Search by default, Parallel Extract for source retrieval, Parallel Research for explicitly deep/exhaustive work, optional explicit Parallel Chat, and optional Perplexity only when requested or allowed as a failure fallback.

随包脚本 2 项；参考文档 2 项；模板/示例 0 项。

### 脚本

- [scripts/manuscript_packet.py](modules/research-lookup/scripts/manuscript_packet.py) — Pure helpers for building manuscript-ready research packets.
- [scripts/research_lookup.py](modules/research-lookup/scripts/research_lookup.py) — Parallel-first research retrieval for manuscript evidence compilation. The public ``ResearchLookup`` class and CLI remain backward compatible while ordinary queries use Parallel Se

### 参考

- [README.md](modules/research-lookup/README.md)
- [references/api-contracts.md](modules/research-lookup/references/api-contracts.md)
