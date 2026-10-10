# World Realizability & Epistemic Horizons (WREH)

**World Realizability & Epistemic Horizons (WREH)** is an interdisciplinary research programme and research community studying how physically admissible observations constrain classes of possible global realizations.

> **Founding principle:** Responses constrain worlds; they do not automatically identify one.

WREH develops a mathematically explicit language for response-defined world spaces, identifiability, refinement, global realizability, model non-uniqueness, and epistemic horizons while maintaining strict separation between theorem, model, physical hypothesis, interpretation, and open question.

## Current status

- **Programme:** ACTIVE
- **Repository:** public programme repository
- **Founding document:** WREH-00 — *Manifesto and Research Programme*
- **Published and frozen:** WR-I v0.3, WR-II v0.5, WR-III v0.6, WR-IV v0.6, WR-VI v0.2
- **Latest author-reported publication:** WR-VII, DOI [10.5281/zenodo.23264253](https://doi.org/10.5281/zenodo.23264253); deposited record/version/files pending direct verification
- **Current technical work:** WR-VIII v0.2 — **PREPRINT_READY (technical package)**; bilingual publication files prepared, no VIII DOI yet; upstream WR-V v0.3 remains a separate review draft
- **Next scientific gate:** external scientific review of the explicit FLRW distance/rate completion, calibration and restricted global lifts; real catalogue/covariance, matter and perturbation inputs are needed for observational inference

## Quick navigation

### Founding documents

- [WREH-00 manifesto](docs/WREH-00/)
- [Programme register](registry/PROGRAMME_REGISTER.md)
- [Claim firewalls](registry/CLAIM_FIREWALLS.md)

### WR-I — Response-Defined World Spaces

**Full title:** *Response-Defined World Spaces: Response Equivalence, Finite-Resolution Separation, and Identifiability of Global Realizations*

- [WR-I project page](papers/WR-I/README.md)
- [LaTeX source v0.3](papers/WR-I/WREH_WR-I_Preprint_Candidate_v0.3.tex)
- [PDF v0.3](papers/WR-I/WREH_WR-I_Preprint_Candidate_v0.3.pdf)
- [WR-I changelog](papers/WR-I/CHANGELOG.md)
- [Publication metadata](papers/WR-I/metadata/publication_metadata.yaml)
- [Interactive demo](demos/WR-I/WREH_WR-I_Response_Defined_Worlds_Demo_v0.1.html)

### Latest work

- [WR-IV — published bilingual preprint](papers/WR-IV/README.md)
- [WR-IV publication identity and metadata check](reviews/WR-IV/WREH_WR-IV_Post_Publication_Check_v0.6.md)
- [WR-V — experimental transition draft](papers/WR-V/README.md)
- [WR-V result/dependency map](papers/WR-V/THEOREM_MAP.md)
- [WR-VI — The Aquarium Bounds](papers/WR-VI/README.md)
- [WR-VI result/dependency map](papers/WR-VI/THEOREM_MAP.md)
- [WR-VI publication identity check](reviews/WR-VI/WREH_WR-VI_Post_Publication_Check_v0.2.md)
- [WR-VII — Energy-Time Frontiers](papers/WR-VII/README.md)
- [WR-VII result/dependency map](papers/WR-VII/THEOREM_MAP.md)
- [WR-VII publication check status](reviews/WR-VII/WREH_WR-VII_Post_Publication_Check_2026-10-09.md)
- [WR-VIII — The Cosmological Fibre](papers/WR-VIII/README.md)
- [WR-VIII result/dependency map](papers/WR-VIII/THEOREM_MAP.md)

## Core mathematical idea

For a declared class of admissible global realizations `\mathcal W`, a family of admissible protocols `\mathcal P`, and response maps

$$
R_P:\mathcal W\to\mathcal Y_P,
$$

a protocol family `\mathcal A\subseteq\mathcal P` induces exact response equivalence

$$
W_1\sim_{\mathcal A}W_2
\quad\Longleftrightarrow\quad
R_P(W_1)=R_P(W_2)
\quad\text{for every }P\in\mathcal A.
$$

The corresponding response-defined world space is

$$
\mathcal Q_{\mathcal A}=\mathcal W/\!\sim_{\mathcal A}.
$$

WREH does **not** infer from this construction that response-equivalent realizations are ontologically identical.

## Methodological lineage

A direct methodological precursor is:

**A. A. Malachevsky,** *Boundary Compensation XI: The Inverse Isotypic Gap Problem and Finite-Resolution Response Equivalence Classes*, Zenodo (2026). DOI: **10.5281/zenodo.20748061**.

The bridge is methodological:

```text
hidden structures
    -> BC-XI: finite-resolution response-equivalence classes
    -> WR-I: response-defined classes of admissible global realizations
```

Boundary Compensation (BC) and WREH remain distinct programmes. No finite-dimensional BC gap, wall, fibre, atlas, or parameter flow is automatically interpreted as physical energy, spacetime, cosmological structure, time, or dynamics.

## Planned technical sequence

1. **WR-I** — Response-Defined World Spaces
2. **WR-II** — Finite Consistency and Global World Realizability
3. **WR-III** — Geometry of Admissible World Fibres
4. **WR-IV** — Response-Conditioned Global Completion and the Status of the Past
5. **WR-V** — Experiment and Realization Selection
6. **WR-VI** — The Aquarium Bounds
7. **WR-VII** — Energy-Time Frontiers of World Realizability
8. **WR-VIII** — The Cosmological Fibre
9. **WR-IX** — Epistemic Horizons

The sequence is obligation-driven. Numbering does not by itself authorize a new paper or claim.

## Contribution discipline

WREH welcomes critical and constructive contributions, including negative results. Contributions should identify their status explicitly as one of:

- **THEOREM**
- **MODEL**
- **NUMERICAL EVIDENCE**
- **PHYSICAL HYPOTHESIS**
- **INTERPRETATION**
- **OPEN QUESTION**

See [CONTRIBUTING.md](CONTRIBUTING.md) for the working rules.

## Author

**A. A. Malachevsky**  
ORCID: **0009-0008-6009-3196**

## Citation

Repository-level citation metadata are provided in [CITATION.cff](CITATION.cff). Individual papers maintain their own citation metadata in their paper directories.

## Licence status

Research content is [CC BY 4.0](LICENSE-CONTENT.md); executable scripts and HTML are [MIT](LICENSE-CODE.txt), subject to the stated scopes and third-party exclusions. See [LICENSES.md](LICENSES.md).

---

**Repository:** https://github.com/AIDevelopersMonster/WREH  
**State:** ACTIVE — 2026-10-09
