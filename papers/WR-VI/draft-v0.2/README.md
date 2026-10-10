# WR-VI mathematical draft v0.2

Date: 9 October 2026. Author: A. A. Malachevsky; ORCID 0009-0008-6009-3196. Programme and community: WREH. Status: REVIEWABLE_DRAFT. No DOI or deposit. A supplied v0.1 review has been addressed; its independence and formal external peer-review status are unverified.

## Read and reproduce

The EN/RU PDFs share the common source `wrvi-body.tex`. Open the bilingual HTML locally; it makes no external requests. Its candidate is selected for display, not obtained by an additional measurement. It displays the exact-response benchmark; the response-tolerance family is explained separately.

```bash
python3 scripts/reproduce.py
python3 scripts/build.py
```

Reproduction uses Python's standard library and exact fractions. It enumerates 4,147 feasible symmetric stochastic matrices on an edge lattice with denominator 24, checks seven exact-response lattice matrices and 301 continuous-fibre points, 601 activity caps, 15 tolerance witnesses and 140 cap-quantifier cases. It verifies irreducibility, the explicit dual certificate at ν=3/20 and the mean-energy counterexample. The v0.2 concrete case N=[1/6,1/4] also checks both endpoint matrices, interval length 1/24, cap width 1/12, and the demo centre 5/24 with half-width 1/24. These are finite checks, not proof replacements.

Build dependencies: Python with `pypdf`; XeLaTeX, `fontspec`, `polyglossia`, Cyrillic hyphenation (`texlive-lang-cyrillic`), AMS packages, `microtype`, `booktabs`, `tabularx`, `enumitem` and Nimbus OTF fonts. The script compiles three passes per language, rejects warnings and compares actual label/equation/reference numbering. Rendering and visual review are separate checks.

Optional browser QA needs Node, Playwright and Chromium:

```bash
node scripts/verify_demo.cjs
```

Set `WRVI_BROWSER` to a compatible Chromium binary and `WRVI_QA_DIR` to a temporary screenshot directory when needed. It checks 192 combinations of cap, cap uncertainty, strict assumption and candidate position, both languages, keyboard input and desktop/mobile layout. It also checks the concrete N=[1/6,1/4] preset and its right endpoint. The UI half-width uses ρ; the manuscript δ in Proposition 6.2 is the full interval width.

```bash
python3 scripts/package.py --output /tmp/WREH_WR-VI_Review_Package_v0.2_EN-RU.zip
```

This creates a fixed-membership, fixed-timestamp review archive and SHA-256 manifest. From the repository root or the extracted `WREH_WR-VI_v0.2_review` root, verify `sha256sum -c papers/WR-VI/draft-v0.2/SHA256SUMS`. The manifest excludes itself and the ZIP. Only immutable versioned draft/review files are archived; active project entry points are excluded so later routing updates cannot invalidate this version's manifest. TeX rebuild bytes can differ because build metadata are recorded.

Content is CC BY 4.0; code is MIT. Copies of scope notices are included. Third-party books, browser binaries and intermediate renders are excluded.

## Review scope

See the [result map](THEOREM_MAP.md), [source preflight](../../../reviews/WR-VI/WREH_WR-VI_Prior_Art_Preflight_v0.1.md), [technical audit](../../../reviews/WR-VI/WREH_WR-VI_Technical_Audit_v0.2_RU.md) and [reviewer prompt](../../../reviews/WR-VI/REVIEW_REQUEST_v0.2.md). See the [point-by-point review response](../../../reviews/WR-VI/WREH_WR-VI_Response_to_Review_v0.2_RU.md). The revision preserves all seven proofs, twelve numbered equations and seven bibliography entries. It adds the WR-II v0.5 Example 10.19 nonattainment analogy, the WR-V v0.3 §9 handoff, and a concrete uncertain-cap case. The matrices already contained all three rows; their source now puts one row on each line, and rendering is checked separately.

This draft does not certify exhaustive novelty, external peer review, a real physical constraint, statistical coverage or journal readiness.
