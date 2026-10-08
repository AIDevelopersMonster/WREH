# WR-IV v0.6 — bilingual Zenodo preprint

**Author:** A. A. Malachevsky · [ORCID 0009-0008-6009-3196](https://orcid.org/0009-0008-6009-3196)  
**Programme:** World Realizability & Epistemic Horizons (WREH)  
**Date:** 8 October 2026  
**Status:** PUBLICATION_READY for an explicitly expository, unpeer-reviewed preprint. Not yet deposited; no WR-IV DOI has been assigned.

## Read

- `WREH_WR-IV_Preprint_v0.6_EN.pdf` — complete English text, 16 pages.
- `WREH_WR-IV_Preprint_v0.6_RU.pdf` — complete Russian translation, 18 pages.
- `WREH_WR-IV_Demo_v0.6_EN-RU.html` — optional offline bilingual demonstration; open directly in a browser.
- `AUDIT_RU.md` — mathematical, bibliographic and publication audit.
- `SOURCE_MAP.md` — primary-source locations and claim provenance.
- `ZENODO_DEPOSIT.md` — deposit instructions and the prepared metadata fields.

The two PDFs are language manifestations of the same work. They share theorem labels, equations, figures and bibliography, generated from a common source. They are not two successive versions.

## Scope

This preprint distinguishes compatible global worlds, projected histories, observable records, posterior laws, measure support and covariance. It supplies explicit assumptions and self-contained proofs, including a regular Brownian-bridge kernel, prefix-law equivalence and a several-observation RTS example.

Set-image results are elementary; natural extensions, Gaussian conditioning, Brownian bridges, Bayesian likelihoods and RTS smoothing are classical. WREH provides the declared comparison framework. No theorem priority, new smoothing method, physical rewriting of the past, retrocausality, branching ontology or derivation of physical time is claimed. A comprehensive originality certification is not supplied.

## Reproduce

Requirements: Python 3.10+, NumPy, Matplotlib, pypdf; XeLaTeX with Cyrillic language support, URW Base35 OpenType fonts and the packages listed in `wriv-preamble.tex`; Poppler (`pdftotext`). On a TeX Live system, relevant packages include `texlive-xetex`, `texlive-lang-cyrillic`, `texlive-latex-extra`, `fonts-urw-base35` and `poppler-utils`.

```sh
python3 scripts/reproduce.py
python3 scripts/build.py
python3 scripts/package.py
```

`reproduce.py` regenerates analytic figures and checks 80 independently conditioned Gaussian models against the RTS recursion. `build.py` builds both PDFs and validates warnings, corresponding labels, equations and references. `package.py` makes the distributable ZIP from a fixed file list and writes SHA-256 checksums. None of these scripts accesses the network.

Optional browser QA requires Node.js, Playwright and a compatible Chromium installation:

```sh
node scripts/verify_demo.cjs
```

Set `WRIV_BROWSER` to an executable path if Playwright's default browser is unavailable. Browser QA generates local `qa/` screenshots; these are not part of the archive. The HTML itself needs no Node.js, Python, server or external library. Paths drawn on a finite grid are illustrations; the paper's proofs do not depend on Monte Carlo sampling.

PDF byte hashes can differ after recompilation because of TeX/font/library versions and timestamps. The supplied checksums describe the delivered files, rather than guaranteeing bitwise reproducibility on every system.

## Licence

Research text, translations, documentation and figures: **CC BY 4.0** (`LICENSE-CONTENT.md`). Executable scripts and the executable part of the HTML: **MIT** (`LICENSE-CODE.txt`). Third-party publications are cited but not redistributed. Preserve the notices when reusing the mixed HTML file.

## Русское пояснение

Архив содержит полный английский препринт и полный русский перевод одной работы. Формулы, нумерация результатов и библиография согласованы. HTML открывается локально и переключается между языками. Статус готовности относится к депонированию содержательного препринта с ограниченными заявлениями о вкладе; внешнее рецензирование и подтверждение исследовательской новизны не заявлены. Публикация в Zenodo ещё не выполнена.
