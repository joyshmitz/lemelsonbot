# Changelog

All notable changes to Lemelsonbot are documented in this file.

Commit links point to
[github.com/Dicklesworthstone/lemelsonbot](https://github.com/Dicklesworthstone/lemelsonbot).

---

## [Unreleased]

Changes on `main` after v0.1.0.

### CLI & Tooling

- **`lemelson` CLI script** for workflow automation: subcommands `validate`,
  `extract-kernel`, `kickoff-template`, `doctor` (with `--json` output).
  ([d56563d](https://github.com/Dicklesworthstone/lemelsonbot/commit/d56563dc36c8fab3a0f6c028b780c21cdc63ebdf))

### Bug Fixes

- Remove unused `sys` import from `analyze_header.py`.
  ([6afef5c](https://github.com/Dicklesworthstone/lemelsonbot/commit/6afef5c3a70ce1a67059b0aa8625342ceb067695))

### CI & Release Infrastructure

- Add release-notes template (`.github/release.yml`) grouping entries by
  Corpus Updates, Methodology, CI/Automation, and Docs labels.
  ([d81e2de](https://github.com/Dicklesworthstone/lemelsonbot/commit/d81e2ded81f0c41b931120897d855970dc6db725))

### Repository Metadata

- Add GitHub social preview image (1280x640 `gh_og_share_image.png`).
  ([be67d8d](https://github.com/Dicklesworthstone/lemelsonbot/commit/be67d8d264538fae5002cad0c42b08e6a0adb2df))
- Add LICENSE: MIT with OpenAI/Anthropic Rider restricting use by
  OpenAI, Anthropic, and their affiliates without express written permission
  from Jeffrey Emanuel.
  ([d1a527b](https://github.com/Dicklesworthstone/lemelsonbot/commit/d1a527b7de07f9c3944062820fd1ea75f6596dc0))

---

## [v0.1.0] - 2026-01-22

First tagged release. Published via GitHub Actions
(`softprops/action-gh-release`) with a tarball
(`lemelsonbot-v0.1.0.tar.gz`) and `SHA256SUMS.txt`.

**Tag:** [`v0.1.0`](https://github.com/Dicklesworthstone/lemelsonbot/releases/tag/v0.1.0)

### Corpus

- **33 198-line cleaned extraction** of Jerome H. Lemelson's invention
  notebooks (`LEMELSON_NOTEBOOKS_EXTRACTED_v1.md`), with Smithsonian
  boilerplate stripped while preserving notebook identifiers.
  ([f95d01d](https://github.com/Dicklesworthstone/lemelsonbot/commit/f95d01d35e0a49fe8338056e6fafcb0bf76121da))
- Raw OCR transcripts split by volume range:
  `lemelson_notebooks_vol_a-3.md`, `vol_5-9.md`, `vol_10-16.md`
  (under `corpus/raw_responses/transcripts/`).
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))

### Quote Bank & Evidence

- Quote bank built up across three commits to 300+ sourced entries
  (1 501 lines in `corpus/quote_bank/quote_bank.md`).
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [97568e8](https://github.com/Dicklesworthstone/lemelsonbot/commit/97568e8009dc6dab2782aa415b07e99218638dcc),
  [132ecea](https://github.com/Dicklesworthstone/lemelsonbot/commit/132ecea1d88bc5fc6516e8daa79f0dbbff53a0d5))
- Provenance graph mapping quotes to methodology elements
  (`corpus/specs/provenance_graph.md`).
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))

### Methodology Distillation

- **Triangulated kernel** (`corpus/specs/triangulated_kernel.md`): axioms and
  operators extracted by cross-referencing three independent LLM
  distillations.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- **Operator library** (`corpus/specs/operator_library.md`): HTML-comment-
  delimited operator cards with tags, preconditions, and evidence anchors.
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- Three independent LLM distillations: Opus, GPT, and Gemini
  (`corpus/distillations/`).
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- Jargon glossary (`corpus/specs/jargon_glossary.md`).
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))
- Anti-patterns list (`corpus/specs/anti_patterns.md`).
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))
- Decision procedures (`corpus/specs/decision_procedures.md`).
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- Uncertainty queue (`corpus/specs/uncertainty_queue.md`).
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- Metaprompt v0.1 (`corpus/metaprompt_v0.1.md`).
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))

### Session Kickoffs

- Standard session kickoff (`corpus/specs/session_kickoff.md`).
  ([bb0c876](https://github.com/Dicklesworthstone/lemelsonbot/commit/bb0c876c6ee61f9ea8d870f4a5dd6739e81ccef7))
- Adversarial critique kickoff (`corpus/specs/session_kickoff_adversarial.md`).
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- Test designer kickoff (`corpus/specs/session_kickoff_test_designer.md`).
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))

### Protocol Specs & Artifacts

- Lemelson artifact schema v0.1, delta format v0.1, evaluation rubric v0.1,
  evidence pack v0.1, excerpt format v0.1, linting rules v0.1, and role
  prompts v0.1 (under `specs/`).
  ([7d50a7a](https://github.com/Dicklesworthstone/lemelsonbot/commit/7d50a7a899e8550eed2d181f1f10f1b909a63a72))
- Golden example artifact (`artifacts/golden-example-lemelson.md`).
  ([7d50a7a](https://github.com/Dicklesworthstone/lemelsonbot/commit/7d50a7a899e8550eed2d181f1f10f1b909a63a72))

### Validation Scripts

- `scripts/validate-corpus.py` -- checks required files, quote bank entry
  count (min 300), and quote length constraints.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [132ecea](https://github.com/Dicklesworthstone/lemelsonbot/commit/132ecea1d88bc5fc6516e8daa79f0dbbff53a0d5))
- `scripts/validate-kernel.py` -- ensures start/end markers and minimum
  axiom/operator counts in the triangulated kernel.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- `scripts/validate-operators.py` -- checks operator card formatting, tag
  allowlist, and required sections.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5))
- `scripts/validate-kickoffs.py` -- confirms kickoff files exist and are
  non-empty.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))
- `scripts/extract-kernel.py` -- extracts the kernel block to a standalone
  artifact file.
  ([636a411](https://github.com/Dicklesworthstone/lemelsonbot/commit/636a4118f4b219eec85875957f1c7aeb684efaf2))

### CI & Release Infrastructure

- CI workflow (`.github/workflows/ci.yml`): runs all four validation scripts
  on push/PR to `main` using Python 3.12.
  ([df4bef8](https://github.com/Dicklesworthstone/lemelsonbot/commit/df4bef8e02bed8a8cda4adfe63f44e332f1e83e5),
  [241ccde](https://github.com/Dicklesworthstone/lemelsonbot/commit/241ccde8fa866cba8c68ba04227c95b30750dde5))
- Release workflow (`.github/workflows/release.yml`): packages corpus,
  specs, artifacts, and scripts into a tarball with SHA256 checksums on
  `v*` tag push.
  ([4b72ca3](https://github.com/Dicklesworthstone/lemelsonbot/commit/4b72ca3a264171a79abf84deb37f975f40671c6a))
- Dependabot configuration for GitHub Actions dependency updates
  (`.github/dependabot.yml`).
  ([4b72ca3](https://github.com/Dicklesworthstone/lemelsonbot/commit/4b72ca3a264171a79abf84deb37f975f40671c6a))

### Documentation & Utilities

- Full README with hero image, badges (CI, Corpus), architecture diagram,
  installation options, command reference, configuration defaults, FAQ,
  and troubleshooting.
  ([c795d77](https://github.com/Dicklesworthstone/lemelsonbot/commit/c795d774b1a86d3493b47a782948e5d65931bc78))
- PDF header analysis helper scripts (`analyze_header.py`,
  `debug_extract.py`, `extract_test.py`, `test_extract.py`,
  `test_execution.py`).
  ([f95d01d](https://github.com/Dicklesworthstone/lemelsonbot/commit/f95d01d35e0a49fe8338056e6fafcb0bf76121da))

---

## Commit Log (oldest-first)

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

[Unreleased]: https://github.com/Dicklesworthstone/lemelsonbot/compare/v0.1.0...main
[v0.1.0]: https://github.com/Dicklesworthstone/lemelsonbot/releases/tag/v0.1.0
