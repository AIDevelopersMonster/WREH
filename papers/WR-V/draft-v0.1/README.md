# WR-V mathematical draft v0.1

Date: 8 October 2026. Author: A. A. Malachevsky; ORCID 0009-0008-6009-3196. WREH is the programme and community. The English and Russian PDFs are parallel manifestations of this draft, not successive versions. No WR-V DOI or deposit is claimed.

## Read and reproduce

Open the EN/RU PDFs or the self-contained `WREH_WR-V_Demo_v0.1_EN-RU.html` locally. The HTML makes no network requests. Its second measurement is explicitly generated from the displayed candidate; it demonstrates a mathematical identification problem, not observed experimental data.

Run from this folder:

```bash
python3 scripts/reproduce.py
python3 scripts/build.py
```

`reproduce.py` uses the standard library and exact rational arithmetic. It independently enumerates 861 simplex points, checks 891 response-fibre points, the same-outcome instrument example, a null-vector witness, finite-resolution perturbation, parity assignments and the exact posterior 729/730. These are benchmark checks, not replacements for proofs.

Build dependencies: Python with `pypdf`; XeLaTeX, `fontspec`, `polyglossia`, Cyrillic hyphenation patterns (`texlive-lang-cyrillic` on Debian/Ubuntu), AMS packages, `microtype`, `booktabs`, `tabularx`, `enumitem` and Nimbus OTF fonts. `build.py` uses temporary output directories, makes three passes per language and checks matching result and bibliography numbering. It writes the two PDFs and `build-verification.json` here. PDF rendering/visual QA is a separate mandatory audit.

Optional browser QA requires Node, Playwright and a compatible Chromium:

```bash
node scripts/verify_demo.cjs
```

Set `WRV_BROWSER` to a Chromium executable if the Playwright default browser is unavailable. Set `WRV_QA_DIR` to keep screenshots in a chosen temporary directory. Browser binaries, screenshots and third-party full texts are excluded from the draft archive.

`scripts/package.py` creates a fixed-timestamp review archive from an explicit file list and generates SHA-256 checksums. The archive is a review package, not a prepared Zenodo publication release.

```bash
python3 scripts/package.py --output /tmp/WREH_WR-V_Review_Package_v0.1_EN-RU.zip
```

Verify `SHA256SUMS` from the repository root (or the extracted archive's `WREH_WR-V_v0.1_review` folder): `sha256sum -c papers/WR-V/draft-v0.1/SHA256SUMS`. The manifest excludes itself and the ZIP to avoid self-reference. Archive membership, timestamps and permissions are fixed for given input bytes; PDF rebuild bytes may differ because TeX records build metadata.

## Scientific limitations

Release status: REVIEWABLE_DRAFT. No external peer review or exhaustive originality audit. The source map states the exact extent of source inspection; it does not assert full-text inspection where access was unavailable. Quantities are model-level probabilities, not exact finite-sample frequencies. Calibration errors, physical admissibility, unknown-input averaging, quantum instruments and microscopic hidden lifts need additional work.

Content is CC BY 4.0 and executable supplements are MIT, under the repository's scope notices. Copies of those notices are included for standalone reuse. Cited third-party works are not included.
