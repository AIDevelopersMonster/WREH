# WR-VII v0.2 — review package

**Energy-Time Frontiers of World Realizability**
*Calibrated quantum responses, action bounds and generator ambiguity*
A. A. Malachevsky · ORCID 0009-0008-6009-3196 · 9 October 2026.

Status: **REVIEWABLE_DRAFT**. English article (9 pages) and complete Russian translation (9 pages). No WR-VII DOI, deposit, external peer review, priority certificate or journal-readiness assertion.

## Scientific obligation

A response-and-resource interface with actual joules and seconds, after WR-VI's dimensionless activity example. Closed finite-dimensional pure unitary dynamics, a prepared state, a calibrated projector and a hard Hamiltonian spectral-diameter cap are declared assumptions. This is a new quantum carrier, not an undeclared embedding of the classical WR-V/VI kernels.

The self-contained action proof gives `arcsin(sqrt(p)) <= integral(D)/(2*hbar)`. Under `D <= E`, the qubit frontier `E*tau >= 2*hbar*arcsin(sqrt(p))` is sharp. Constant-qubit generators have explicitly enumerated revival windows. Even the exact frontier retains a circle of Hamiltonians. At complete transfer, final-state tomography cannot distinguish them; calibrated intermediate-time probes on fresh preparations do so within that restricted family. Deterministic intervals and fixed independent repetitions have different feasibility and coverage certificates.

## Files and verification

- `WREH_WR-VII_Draft_v0.2_EN.pdf` / `_RU.pdf`: common result, equation and bibliography numbering.
- `wrvii-body.tex`, `wrvii-preamble.tex`, two entry points: common bilingual source.
- `figures/frontiers.pdf` / `.png`: analytic unit-bearing frontiers and separated phase windows.
- `WREH_WR-VII_Demo_v0.2_EN-RU.html`: offline, bilingual, mobile-compatible constant-qubit model. Predictions are not new measurements.
- `verification.json`: symbolic witnesses, independent matrix exponentials, noncommuting 4D controls and exact binomial coverage.
- `qsl-positioning-verification.json`: three static matrix-exponential witnesses comparing diameter, state spread and mean energy above ground.
- `build-verification.json`: actual assigned labels, page counts and warnings.
- `demo-verification.json`: 64 UI scenarios, two languages, desktop/mobile and no external requests.
- `architecture-verification.json`: byte preservation of all upstream scientific snapshots.
- `THEOREM_MAP.md`: assumptions, dependencies and claim ceilings.
- `zenodo_metadata.json`, `PREPRINT_DEPOSIT.md`, `CITATION.cff`: prepared descriptive metadata only.
- `SHA256SUMS`: content hashes. It excludes itself and the archive.

Reviews are in `reviews/WR-VII`: point-by-point response, revision audit, targeted primary-source preflight, input provenance and external review request. The two supplied input files are byte-identical: one distinct review, not two established independent reviews. This internal audit is not independent peer review. Available earlier reviews were consulted for architectural restrictions, not automatically transferred to these new results.

## Rebuild

Python 3 with NumPy, SciPy, SymPy, Matplotlib and pypdf; XeLaTeX, Nimbus fonts and Russian hyphenation. Node with Playwright and a compatible Chromium installation for UI verification. No external assets are used in the HTML.

```bash
python scripts/reproduce.py
python scripts/compare_resources.py
python scripts/figure.py
python scripts/build.py
WREH_CHROME_PATH=/absolute/path/to/chromium node scripts/verify_demo.cjs
python scripts/package.py --output /absolute/path/WREH_WR-VII_Review_Package_v0.2_EN-RU.zip
```

Run from this draft directory; each script resolves its input paths independently. `WREH_SCREENSHOT_DIR` optionally stores browser QA images outside the package. The package script has fixed membership and fixed archive timestamps. Recompilation may change PDF metadata and consequently hashes; use the shipped PDFs for exact snapshot verification. The ZIP carries repository-relative paths under `WREH_WR-VII_v0.2_review/`.

Content and analytic figures: CC BY 4.0. Executable scripts and HTML code: MIT. Dependencies retain their own licences and are not redistributed. See `LICENSES.md`.
