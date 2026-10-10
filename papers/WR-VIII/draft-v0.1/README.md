# WR-VIII v0.1 — review package

**The Cosmological Fibre: Universes Compatible with Our Universe Today**

Distance responses, curvature completion and global ambiguity.

A. A. Malachevsky; ORCID 0009-0008-6009-3196; WREH; 9 October 2026.

Status: **REVIEWABLE_DRAFT**. English 9 pages; full Russian translation 10 pages. Seven self-contained proof blocks, 18 numbered equations, 38 shared labels, 12 bibliography entries. This is a kinematic cosmological response model and synthetic benchmark. No observational fit, fixed-matter admissibility, exhaustive novelty certificate, independent peer review or WR-VIII DOI is asserted.

## Contents and reproduction

The two entry points share `wrviii-body.tex` and `wrviii-preamble.tex`. Figures are analytic, not measurements. The bilingual HTML is self-contained and makes no network requests. Its curvature display uses an explicitly supplied synthetic prior q∈[-0.4,0.4]; it is not the unrestricted theoretical fibre.

From the repository root, run sequentially:

```bash
python papers/WR-VIII/draft-v0.1/scripts/reproduce.py
python papers/WR-VIII/draft-v0.1/scripts/figure.py
python papers/WR-VIII/draft-v0.1/scripts/build.py
node papers/WR-VIII/draft-v0.1/scripts/verify_demo.cjs
python papers/WR-VIII/draft-v0.1/scripts/package.py --output /tmp/WREH_WR-VIII_Review_Package_v0.1_EN-RU.zip
```

Dependencies: Python with numpy, scipy, sympy, matplotlib, pypdf; XeLaTeX with Russian hyphenation and Nimbus fonts; Node with Playwright. Set `WREH_CHROME_PATH` to a local Chromium executable and `WREH_SCREENSHOT_DIR` to a temporary directory for browser screenshots. The build puts intermediates in a temporary directory. Regenerated build/browser reports intentionally reset visual review to PENDING until the new output is inspected.

`verification.json` records four symbolic identities, 360 independent curved-distance integrations, 90 inverse checks, 45 finite-difference Jacobians, 135 interval inversions, 26,595 admissible candidate checks, 540 joint scale checks, 46,800 finite lattice witnesses and four smooth future histories. Three rate intervals require clipping at the separate open global branch boundary. Finite checks accompany, rather than replace, the proofs. `demo-verification.json` records 442 scenarios including nonzero positive/negative curvature, EN/RU, desktop/mobile, incompatible rates and a rejected branch.

`package.py` uses a fixed file list and timestamps, checks every SHA-256 digest and verifies exact ZIP membership. `SHA256SUMS` covers content files; it does not hash itself. Identical inputs produce an identical archive. ZIP files and TeX intermediates are intentionally not committed.

## Reading and review

- [Result and dependency map](THEOREM_MAP.md)
- [Technical audit](../../../reviews/WR-VIII/WREH_WR-VIII_Technical_Audit_v0.1_RU.md)
- [Primary-source preflight](../../../reviews/WR-VIII/WREH_WR-VIII_Source_Preflight_v0.1.md)
- [External review request](../../../reviews/WR-VIII/REVIEW_REQUEST_v0.1.md)
- [Deposit instructions](PREPRINT_DEPOSIT.md)

The targeted preflight attributes established FLRW/curvature and topology tools. The title does not certify compatibility with current catalogues. Exact D includes a controlled derivative; rates used for selection must be independently calibrated. Bounds are deterministic, not confidence regions unless separately calibrated. The global torus witness covers declared classical patch protocols; no universal horizon or quantum-state equivalence is inferred.

WR-VII DOI 10.5281/zenodo.23264253 is author-reported. Its public record, deposited version, files and hashes remain pending direct verification; see the separate post-publication report. Earlier versioned sources are frozen. WR-IX remains planned. Content and original figures CC BY 4.0; executable scripts and HTML code MIT.
