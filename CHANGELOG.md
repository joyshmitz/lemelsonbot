# Changelog

All notable changes to Lemelsonbot are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Commit links point to
[github.com/Dicklesworthstone/lemelsonbot](https://github.com/Dicklesworthstone/lemelsonbot).

---

## [Unreleased]

Changes on `main` after the v0.1.0 release (2026-01-22).

### CLI & Workflow Automation

- **`lemelson` CLI script** -- a Python entry point that wraps the full
  validation and extraction workflow into four subcommands:
  - `validate` -- runs all four validation scripts in sequence and reports
    a unified pass/fail.
  - `extract-kernel` -- extracts the triangulated kernel to a standalone
    artifact file (supports `--input` / `--output` overrides).
  - `kickoff-template` -- prints a ready-to-fill invention session kickoff
    pack to stdout.
  - `doctor` -- checks the local toolchain (`python3`, `rg`, `git`, `gh`)
    and reports status in plain text or `--json`.
  ([d56563d](https://github.com/Dicklesworthstone/lemelsonbot/commit/d56563dc36c8fab3a0f6c028b780c21cdc63ebdf))

### Licensing

- Add `LICENSE` file: MIT with OpenAI/Anthropic Rider. The rider restricts
  use by OpenAI, Anthropic, and their affiliates without express written
  permission from Jeffrey Emanuel. The restriction covers copying, hosting,
  benchmarking, training-corpus inclusion, and all derivative works.
  ([d1a527b](https://github.com/Dicklesworthstone/lemelsonbot/commit/d1a527b7de07f9c3944062820fd1ea75f6596dc0))

### CI & Release Infrastructure

- Add release-notes template (`.github/release.yml`) that groups
  auto-generated GitHub release notes by Corpus Updates, Methodology,
  CI/Automation, Docs, and Other categories, with a `skip-release-notes`
  label opt-out.
  ([d81e2de](https://github.com/Dicklesworthstone/lemelsonbot/commit/d81e2ded81f0c41b931120897d855970dc6db725))

### Bug Fixes

- Remove unused `sys` import from `analyze_header.py`.
  ([6afef5c](https://github.com/Dicklesworthstone/lemelsonbot/commit/6afef5c3a70ce1a67059b0aa8625342ceb067695))

### Repository Metadata

- Add GitHub social preview / Open Graph image (`gh_og_share_image.png`,
  1280x640) for consistent link previews when sharing the repository URL.
  ([be67d8d](https://github.com/Dicklesworthstone/lemelsonbot/commit/be67d8d264538fae5002cad0c42b08e6a0adb2df))

---

## [v0.1.0] -- 2026-01-22

First tagged release. The annotated tag points at commit
[`4b72ca3`](https://github.com/Dicklesworthstone/lemelsonbot/commit/4b72ca3a264171a79abf84deb37f975f40671c6a).
A GitHub release was published automatically via the
`softprops/action-gh-release` workflow, attaching a tarball
(`lemelsonbot-v0.1.0.tar.gz`) and `SHA256SUMS.txt`.

**Release page:** <https://github.com/Dicklesworthstone/lemelsonbot/releases/tag/v0.1.0>

### Corpus & Source Data

- **33,198-line cleaned extraction** of Jerome H. Lemelson's invention
  notebooks (`LEMELSON_NOTEBOOKS_EXTRACTED_v1.md`). Smithsonian boilerplate
  headers, repeated metadata, and OCR noise were stripped; notebook
  identifiers and section structure were preserved for searchability.
  ([f95d01d](https://github.com/Dicklesworthstone/lemelsonbot/commit/f95d01d35e0a49fe8338056e6fafcb0bf76121da))
- Raw OCR transcripts split by volume range under
  `corpus/primary/transcripts/`:
  - `lemelson_notebooks_vol_a-3.md` (9,233 lines)
  - `lemelson_notebooks_vol_5-9.md` (8,209 lines)
  - `lemelson_notebooks_vol_10-16.md` (15,752 lines)
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))
- PDF header analysis helper scripts (`analyze_header.py`,
  `debug_extract.py`, `extract_test.py`, `test_extract.py`,
  `test_execution.py`) used during corpus extraction.
  ([f95d01d](https://github.com/Dicklesworthstone/lemelsonbot/commit/f95d01d35e0a49fe8338056e6fafcb0bf76121da))

### Quote Bank & Evidence Traceability

- **Quote bank** (`corpus/quote_bank/quote_bank.md`) built up to 300+
  sourced entries (1,501 lines) across three successive commits. Each entry
  carries a `§n` identifier for deterministic cross-referencing with
  methodology artifacts.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [97568e8](https://github.com/Dicklesworthstone/lemelsonbot/commit/97568e8009dc6dab2782aa415b07e99218638dcc),
  [132ecea](https://github.com/Dicklesworthstone/lemelsonbot/commit/132ecea1d88bc5fc6516e8daa79f0dbbff53a0d5))
- **Provenance graph** (`corpus/specs/provenance_graph.md`) mapping quote
  bank entries to methodology elements so every rule is traceable back to
  notebook evidence.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))

### Methodology Distillation

- **Triangulated kernel v0.3** (`corpus/specs/triangulated_kernel.md`):
  axioms and operators derived by cross-referencing three independent LLM
  distillations. Wrapped in `TRIANGULATED_KERNEL_START`/`END` HTML-comment
  markers for deterministic extraction.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Operator library** (`corpus/specs/operator_library.md`): HTML-comment-
  delimited operator cards, each with definition, when-to-use triggers,
  failure modes, a copy-paste prompt module, canonical tag, and quote-bank
  anchors.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Three independent LLM distillations** (`corpus/distillations/`):
  - `opus_distillation.md` -- Opus analysis
  - `gpt_distillation.md` -- GPT analysis
  - `gemini_distillation.md` -- Gemini analysis
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Metaprompt v0.1** (`corpus/metaprompt_v0.1.md`) for guiding distillation
  sessions.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))

### Reference Specs & Supporting Knowledge

- **Jargon glossary** (`corpus/specs/jargon_glossary.md`) defining
  Lemelson-specific terminology for consistent use across artifacts.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Anti-patterns** (`corpus/specs/anti_patterns.md`) cataloguing common
  invention-notebook pitfalls to avoid.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Decision procedures** (`corpus/specs/decision_procedures.md`) for
  choosing which operator to apply at different invention stages.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Uncertainty queue** (`corpus/specs/uncertainty_queue.md`) tracking open
  questions requiring further evidence.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))

### Session Kickoffs

- **Standard kickoff** (`corpus/specs/session_kickoff.md`) -- primary
  template for starting an invention session.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Adversarial critique kickoff**
  (`corpus/specs/session_kickoff_adversarial.md`) -- session template
  focused on stress-testing claims and finding failure modes.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Test designer kickoff**
  (`corpus/specs/session_kickoff_test_designer.md`) -- session template
  oriented toward designing experiments and sample acquisition plans.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))

### Protocol Specifications & Golden Artifact

Seven formal protocol specs (under `specs/`) defining the contract for
Lemelson-method artifacts:

- `lemelson_artifact_schema_v0.1.md` -- canonical 7-section structure
  (Invention Thread, Conception Record, Variant Slate, Manufacturing
  Notes, Tests & Samples, Disclosure & Partner Log, Adversarial Critique)
  with item-ID and citation rules.
- `lemelson_delta_format_v0.1.md` -- format for incremental updates to
  existing artifacts.
- `lemelson_evaluation_rubric_v0.1.md` -- rubric for scoring artifact
  quality.
- `lemelson_evidence_pack_v0.1.md` -- packaging format for evidence
  bundles.
- `lemelson_excerpt_format_v0.1.md` -- format for quoting corpus excerpts.
- `lemelson_linting_rules_v0.1.md` -- machine-enforceable structural rules.
- `lemelson_role_prompts_v0.1.md` -- role-specific prompt fragments for
  agents.

Plus a **golden example artifact**
(`artifacts/golden-example-lemelson.md`) demonstrating a fully conforming
invention session document.

([7d50a7a](https://github.com/Dicklesworthstone/lemelsonbot/commit/7d50a7a899e8550eed2d181f1f10f1b909a63a72))

### Validation Scripts

- `scripts/validate-corpus.py` -- checks that required corpus files exist,
  the quote bank contains at least 300 entries, and individual quotes fall
  within configured length bounds (80--320 chars).
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [132ecea](https://github.com/Dicklesworthstone/lemelsonbot/commit/132ecea1d88bc5fc6516e8daa79f0dbbff53a0d5))
- `scripts/validate-kernel.py` -- ensures the triangulated kernel has
  start/end HTML-comment markers and meets minimum axiom (5) and operator
  (12) counts.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- `scripts/validate-operators.py` -- checks operator card formatting, tag
  allowlist compliance, and required sections.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- `scripts/validate-kickoffs.py` -- confirms all kickoff files in
  `corpus/specs/` exist and are non-empty.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- `scripts/extract-kernel.py` -- extracts the kernel block between markers
  to a standalone artifact file for downstream consumption.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))

### CI & Release Infrastructure

- **CI workflow** (`.github/workflows/ci.yml`): runs all four validation
  scripts (`validate-corpus`, `validate-kernel`, `validate-operators`,
  `validate-kickoffs`) on push and PR to `main`, using Python 3.12 on
  Ubuntu. Concurrency group cancels in-progress runs.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [241ccde](https://github.com/Dicklesworthstone/lemelsonbot/commit/241ccde8fa866cba8c68ba04227c95b30750dde5),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Release workflow** (`.github/workflows/release.yml`): triggers on
  `v*` tag push, packages the corpus, specs, artifacts, scripts, README,
  and hero image into a tarball, generates SHA256 checksums, and publishes
  a GitHub release via `softprops/action-gh-release@v2`.
  ([4b72ca3](https://github.com/Dicklesworthstone/lemelsonbot/commit/4b72ca3a264171a79abf84deb37f975f40671c6a))
- **Dependabot** (`.github/dependabot.yml`): weekly Sunday scans for
  GitHub Actions dependency updates.
  ([4b72ca3](https://github.com/Dicklesworthstone/lemelsonbot/commit/4b72ca3a264171a79abf84deb37f975f40671c6a))

### Documentation

- Full README with hero image (`docs/lemelsonbot_hero.webp`), CI and
  Corpus badges, TL;DR table, comparison matrix, architecture diagram,
  three installation options (curl / clone / `gh`), command reference,
  configuration defaults, FAQ, troubleshooting, and contribution policy.
  ([c795d77](https://github.com/Dicklesworthstone/lemelsonbot/commit/c795d774b1a86d3493b47a782948e5d65931bc78))

---

## Commit Log (oldest first)

| Hash | Date | Summary |
| ---- | ---- | ------- |
| [`f95d01d`](https://github.com/Dicklesworthstone/lemelsonbot/commit/f95d01d35e0a49fe8338056e6fafcb0bf76121da) | 2026-01-22 | Add cleaned Lemelson notebooks extraction |
| [`bb0c876`](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7) | 2026-01-22 | Operationalize Lemelson notebooks into method artifacts |
| [`df4bef8`](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5) | 2026-01-22 | Expand quote bank and add validation CI |
| [`97568e8`](https://github.com/Dicklesworthstone/lemelsonbot/commit/97568e8009dc6dab2782aa415b07e99218638dcc) | 2026-01-22 | Expand quote bank to 200 and tighten validation |
| [`132ecea`](https://github.com/Dicklesworthstone/lemelsonbot/commit/132ecea1d88bc5fc6516e8daa79f0dbbff53a0d5) | 2026-01-22 | Expand quote bank to 300 and harden validation |
| [`636a411`](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2) | 2026-01-22 | Deepen Lemelson methodology artifacts and validation |
| [`7d50a7a`](https://github.com/Dicklesworthstone/lemelsonbot/commit/7d50a7a899e8550eed2d181f1f10f1b909a63a72) | 2026-01-22 | Add Lemelson protocol specs and golden artifact |
| [`c795d77`](https://github.com/Dicklesworthstone/lemelsonbot/commit/c795d774b1a86d3493b47a782948e5d65931bc78) | 2026-01-22 | Revamp README with hero image |
| [`241ccde`](https://github.com/Dicklesworthstone/lemelsonbot/commit/241ccde8fa866cba8c68ba04227c95b30750dde5) | 2026-01-22 | Harden CI workflow |
| [`4b72ca3`](https://github.com/Dicklesworthstone/lemelsonbot/commit/4b72ca3a264171a79abf84deb37f975f40671c6a) | 2026-01-22 | ci(release): add dependabot and release workflow **(tag: v0.1.0)** |
| [`d81e2de`](https://github.com/Dicklesworthstone/lemelsonbot/commit/d81e2ded81f0c41b931120897d855970dc6db725) | 2026-01-22 | ci(release): add release notes template |
| [`d56563d`](https://github.com/Dicklesworthstone/lemelsonbot/commit/d56563dc36c8fab3a0f6c028b780c21cdc63ebdf) | 2026-01-25 | feat: Add lemelson CLI script for workflow automation |
| [`6afef5c`](https://github.com/Dicklesworthstone/lemelsonbot/commit/6afef5c3a70ce1a67059b0aa8625342ceb067695) | 2026-02-11 | Remove unused sys import from PDF header analysis script |
| [`be67d8d`](https://github.com/Dicklesworthstone/lemelsonbot/commit/be67d8d264538fae5002cad0c42b08e6a0adb2df) | 2026-02-21 | chore: add GitHub social preview image (1280x640) |
| [`d1a527b`](https://github.com/Dicklesworthstone/lemelsonbot/commit/d1a527b7de07f9c3944062820fd1ea75f6596dc0) | 2026-02-21 | chore: update license to MIT with OpenAI/Anthropic Rider |

---

[Unreleased]: https://github.com/Dicklesworthstone/lemelsonbot/compare/v0.1.0...main
[v0.1.0]: https://github.com/Dicklesworthstone/lemelsonbot/releases/tag/v0.1.0
