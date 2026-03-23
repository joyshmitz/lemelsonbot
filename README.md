# Lemelsonbot

<div align="center">
  <img src="docs/lemelsonbot_hero.webp" alt="Lemelsonbot - invention notebook corpus and methodology">
</div>

<div align="center">

[![Corpus](https://img.shields.io/badge/corpus-lemelsonbot-blue)](LEMELSON_NOTEBOOKS_EXTRACTED_v1.md)

</div>

Operationalized corpus and methodology distilled from Jerome H. Lemelson's invention notebooks.

<div align="center">
<h3>Quick Install</h3>

```bash
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/lemelsonbot/main/LEMELSON_NOTEBOOKS_EXTRACTED_v1.md -o LEMELSON_NOTEBOOKS_EXTRACTED_v1.md
```

</div>

---

## TL;DR

**The Problem**
- The notebooks are scanned PDFs with Smithsonian headers and repeated metadata.
- OCR output is inconsistent and hard to search at scale.

**The Solution**
- A single cleaned corpus file plus a structured methodology distillation that is machine-parseable.

**Why Use Lemelsonbot?**

| Feature | What you get | Why it matters |
| --- | --- | --- |
| Cleaned corpus | `LEMELSON_NOTEBOOKS_EXTRACTED_v1.md` with boilerplate removed | Search without noise |
| Evidence traceability | Quote bank and provenance graph | Every rule points back to sources |
| Methodology distillation | Triangulated kernel and operator library | Reusable invention heuristics |
| Validation scripts | `scripts/validate-*.py` | Prevents drift and regressions |
| Machine markers | HTML comment markers for kernels/operators | Easy downstream parsing |

## Quick Example

```bash
rg -n "feedback" LEMELSON_NOTEBOOKS_EXTRACTED_v1.md | head
python3 scripts/validate-corpus.py
python3 scripts/validate-kernel.py
python3 scripts/extract-kernel.py --in corpus/specs/triangulated_kernel.md --out artifacts/triangulated_kernel.md
rg -n "OPERATOR_CARD_START" corpus/specs/operator_library.md | head
python3 scripts/validate-operators.py
python3 scripts/validate-kickoffs.py
```

## Design Philosophy

- Evidence first: Every operator is anchored to corpus excerpts and quote IDs.
- Stable artifacts: Kernel, operator library, and specs are versioned and linted.
- Machine-parseable by default: Markers make extraction deterministic.
- Progressive disclosure: Glossary and kickoffs let roles work at different depth.
- Validation in CI: Scripts encode the contract so changes fail fast.

## Comparison

| Approach | Cleaned text | Methodology distillation | Validation | Machine markers |
| --- | --- | --- | --- | --- |
| Lemelsonbot | Yes | Yes | Yes | Yes |
| Raw PDFs | No | No | No | No |
| OCR dump only | Partial | No | No | No |
| General note archive | Partial | Partial | No | No |

## Installation

No build step is required. Choose the path that matches how you want to use the data.

### Option 1: Download the corpus only (curl)

```bash
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/lemelsonbot/main/LEMELSON_NOTEBOOKS_EXTRACTED_v1.md -o LEMELSON_NOTEBOOKS_EXTRACTED_v1.md
```

### Option 2: Clone the full repo

```bash
git clone https://github.com/Dicklesworthstone/lemelsonbot.git
cd lemelsonbot
```

### Option 3: GitHub CLI

```bash
gh repo clone Dicklesworthstone/lemelsonbot
cd lemelsonbot
```

**Requirements**
- Python 3.10+ for validation scripts
- `rg` (ripgrep) for fast searching (optional)

## Quick Start

1. Get the corpus or clone the repo.
2. Search for a topic:

```bash
rg -n "sensor" LEMELSON_NOTEBOOKS_EXTRACTED_v1.md | head
```

3. Validate the corpus and kernel:

```bash
python3 scripts/validate-corpus.py
python3 scripts/validate-kernel.py
```

4. Inspect the methodology artifacts:

```bash
less corpus/specs/triangulated_kernel.md
less corpus/specs/operator_library.md
```

5. Export the kernel for downstream use:

```bash
python3 scripts/extract-kernel.py --in corpus/specs/triangulated_kernel.md --out artifacts/triangulated_kernel.md
```

## Command Reference

### Validate corpus structure

Checks required files and quote bank rules.

```bash
python3 scripts/validate-corpus.py
```

### Validate triangulated kernel

Ensures markers and minimum counts for axioms/operators.

```bash
python3 scripts/validate-kernel.py
```

### Validate operator library

Checks operator card formatting and tag rules.

```bash
python3 scripts/validate-operators.py
```

### Validate session kickoffs

Confirms kickoff files exist and are non-empty.

```bash
python3 scripts/validate-kickoffs.py
```

### Extract the kernel

Outputs the kernel block to a standalone file.

```bash
python3 scripts/extract-kernel.py --in corpus/specs/triangulated_kernel.md --out artifacts/triangulated_kernel.md
```

## Configuration

No runtime config is required. The repository is convention-based. If you want
to change thresholds, edit the constants in `scripts/validate-*.py`.

Documented defaults (not parsed by code):

```ini
# lemelsonbot.defaults.ini
[corpus]
min_quote_count = 300
min_quote_len = 80
max_quote_len = 320

[kernel]
min_axioms = 5
min_operators = 12
```

## Architecture

```text
pdf_originals/ --> extraction --> LEMELSON_NOTEBOOKS_EXTRACTED_v1.md
                                   |
                                   v
                               corpus/primary
                                   |
                                   v
distillations/ --> triangulated_kernel --> operator_library --> artifacts/
          \                         |
           \-> quote_bank ---------/
                    |
                    v
              provenance_graph
```

## Troubleshooting

- `validate-corpus.py` fails with quote count errors: ensure `corpus/quote_bank/quote_bank.md` has at least 300 entries.
- `validate-kernel.py` fails on markers: check `corpus/specs/triangulated_kernel.md` for the start/end comments.
- `validate-operators.py` fails on tags: confirm operator cards use allowed tags and required sections.
- `validate-kickoffs.py` fails: verify all kickoff files in `corpus/specs/` are present and non-empty.
- `rg` is missing: install with `sudo apt install ripgrep` or use `grep`.

## Limitations

- The repo does not include the original scanned images.
- The methodology distillation is interpretive, not a definitive historical record.
- There is no automated re-OCR pipeline in this repository.
- Validation scripts enforce structure, not historical accuracy.

## FAQ

**Q: Is the full corpus in one file?**  
A: Yes. `LEMELSON_NOTEBOOKS_EXTRACTED_v1.md` is the single cleaned corpus file.

**Q: Can I cite the extracted text?**  
A: Cite the Smithsonian source and the original notebook identifiers listed in the corpus.

**Q: How do I parse the operator library programmatically?**  
A: Use the HTML comment markers that wrap each operator card and the kernel block.

**Q: Why does the corpus remove Smithsonian boilerplate?**  
A: It keeps identifiers but removes repeated metadata so searches are meaningful.

**Q: Do I need Python to read the corpus?**  
A: No. Python is only required for the validation and extraction scripts.

## About Contributions

> *About Contributions:* Please don't take this the wrong way, but I do not accept outside contributions for any of my projects. I simply don't have the mental bandwidth to review anything, and it's my name on the thing, so I'm responsible for any problems it causes; thus, the risk-reward is highly asymmetric from my perspective. I'd also have to worry about other "stakeholders," which seems unwise for tools I mostly make for myself for free. Feel free to submit issues, and even PRs if you want to illustrate a proposed fix, but know I won't merge them directly. Instead, I'll have Claude or Codex review submissions via `gh` and independently decide whether and how to address them. Bug reports in particular are welcome. Sorry if this offends, but I want to avoid wasted time and hurt feelings. I understand this isn't in sync with the prevailing open-source ethos that seeks community contributions, but it's the only way I can move at this velocity and keep my sanity.

## License

No license specified. All rights reserved.
