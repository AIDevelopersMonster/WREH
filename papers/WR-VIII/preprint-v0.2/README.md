# WR-VIII v0.2 — bilingual publication package

**The Cosmological Fibre: Universes Compatible with Our Universe Today**  
**Космологический слой: вселенные, совместимые с нашей Вселенной сегодня**

A. A. Malachevsky; ORCID 0009-0008-6009-3196; World Realizability & Epistemic Horizons (WREH); 9 October 2026.

English: **9 pages**. Full Russian translation: **10 pages**, including translated labels inside both figures. Seven self-contained proof blocks, 18 numbered equations, 38 shared labels and 13 bibliography entries. Mathematical equations and numbering are unchanged from v0.1; prose inside equations (4) and (17) is also translated into Russian. Version v0.2 incorporates the prepublication audit; see `CHANGELOG.md` and the bilingual response.

Status: **PREPRINT_READY (technical publication package)**. The author requested bilingual publication preparation. No actual Zenodo deposit or WR-VIII DOI is recorded yet. The separately reproduced automated audit does not establish independent external scientific peer review. Empirical survey fitting and one fixed matter dynamics law are outside the declared kinematic model.

## Read the editions

- [English preprint](WREH_WR-VIII_Preprint_v0.2_EN.pdf)
- [Полный русский препринт](WREH_WR-VIII_Preprint_v0.2_RU.pdf)
- [Common bilingual LaTeX body](wrviii-body.tex)
- [Autonomous EN/RU demo](WREH_WR-VIII_Demo_v0.2_EN-RU.html)
- [Result and dependency map](THEOREM_MAP.md)
- [Deposit description in both languages](DEPOSIT_DESCRIPTION_EN-RU.md)
- [Deposit instructions](PREPRINT_DEPOSIT.md)
- [Response to audit](../../../reviews/WR-VIII/WREH_WR-VIII_Response_to_Audit_v0.2_EN-RU.md)
- [Targeted source preflight](../../../reviews/WR-VIII/WREH_WR-VIII_Source_Preflight_v0.2.md)
- [External review request](../../../reviews/WR-VIII/REVIEW_REQUEST_v0.2.md)

## Reproduce

From the repository root or the extracted archive's repository-like root, run in order:

```bash
python papers/WR-VIII/preprint-v0.2/scripts/reproduce.py
python papers/WR-VIII/preprint-v0.2/scripts/audit_checks.py
python papers/WR-VIII/preprint-v0.2/scripts/figure.py
python papers/WR-VIII/preprint-v0.2/scripts/build.py
node papers/WR-VIII/preprint-v0.2/scripts/verify_demo.cjs
python papers/WR-VIII/preprint-v0.2/scripts/package.py --output /tmp/WREH_WR-VIII_Publication_Package_v0.2_EN-RU.zip
```

Dependencies: Python with numpy, scipy, sympy, matplotlib and pypdf; XeLaTeX with polyglossia, **Russian hyphenation**, Nimbus fonts and the standard packages in the preamble; Node with Playwright and a local Chromium executable. Set `WREH_CHROME_PATH` when needed and `WREH_SCREENSHOT_DIR` for screenshots. Intermediates stay outside the source tree. New build/browser runs intentionally reset visual review to PENDING until their new outputs are inspected. They do not inherit a previous visual PASS.

`verification.json`: four symbolic identities, 360 independent curved-distance integrations, 90 finite inversions, 45 finite-difference Jacobians, 135 interval endpoints, 26,595 candidate equivalence checks, 540 scale checks, 46,800 finite lattice witnesses and four future histories. `independent_verification.json`: separately derived CBL/rank/scale identities, 48 nonpolynomial inversions with clock checks, strict-cap and magnitude/abstract domain witnesses, joint-versus-marginal error constraints, torus shortcuts and future curvature differences. These finite checks accompany the proofs; they do not replace them or certify observational adequacy.

`build-verification.json` records clean three-pass EN/RU builds, shared numbering and bibliography. `demo-verification.json` records 442 scenarios, EN/RU, desktop/mobile, invalid branches and conflicting rates, without page errors or network requests. `architecture-verification.json` records fixed provenance and release consistency. The HTML display's q∈[−0.4,0.4] is a supplied synthetic prior, not the entire theoretical curvature fibre.

`package.py` has fixed membership, fixed timestamps, complete SHA-256 checking and exact ZIP verification. `SHA256SUMS` covers payload files and does not hash itself. ZIPs and TeX intermediates are not committed. Identical payload bytes produce an identical ZIP. Regeneration of PDF containers may change bytes while preserving scientific content; compare new checksums rather than assuming byte identity.

## Scope and provenance

The inverse assumes calibrated D∈C², D(0)=0 and D′>0, an increasing first branch and κ<D(Z)⁻². Selecting rates must be independently calibrated. Interval sufficiency requires the declared joint Cartesian box. The torus witness preserves a restricted local metric and copied classical fields with all used paths inside the patch; global shortest paths may leave it. The future construction additionally assumes a C∞ baseline and does not solve one fixed supplied matter law.

Parent snapshot: 6120d9b37196f9cee4f00bebc2ec1d84d43d44f0. Historical v0.1 is preserved. Upstream WR-VII source: f011aec8546705be1e6bd2bd0c5925da96861179; its DOI 10.5281/zenodo.23264253 is author-reported, with deposited files/version pending direct verification. PR #9 is still stacked on open PR #8. This publication package does not merge upstream PRs. WREH and Boundary Compensation remain separate programmes. WR-IX remains planned.

Research text, translations and original figures: CC BY 4.0. Executable scripts and HTML: MIT. See `LICENSES.md`.
