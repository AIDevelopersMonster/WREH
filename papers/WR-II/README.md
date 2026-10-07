# WR-II — Finite Consistency and Global World Realizability

**Programme:** World Realizability & Epistemic Horizons (WREH)  
**Upstream:** WR-I v0.3 — DOI: 10.5281/zenodo.23210258  
**Status:** REVIEWED_CLEAN / PREPRINT DRAFT v0.3

## New mathematical target

WR-II studies a question not answered by WR-I:

> If every finite bundle of admissible responses is realizable by at least one
> admissible global realization, must there exist one admissible global
> realization realizing all responses simultaneously?

The answer is generally **no** without additional hypotheses.

WR-II therefore distinguishes:

1. **finite obstruction** — some finite response bundle is already unrealizable;
2. **global completion defect** — every finite bundle is realizable and compatible, but no single admissible global realization realizes all of them;
3. **global realizability** — one admissible global realization realizes the entire response profile.

## Core object

For the WR-I world-response structure
\[
\mathbf W=(\mathcal W,\mathcal P,\{R_P\}_{P\in\mathcal P}),
\]
let \(\operatorname{Fin}(\mathcal P)\) be the directed set of finite protocol bundles. For each finite
bundle \(\mathcal A\), define the realizable finite-response image
\[
E_{\mathcal A} := R_{\mathcal A}(\mathcal W).
\]

Restriction maps make \((E_{\mathcal A})\) an inverse system. Its inverse limit
\[
\mathfrak C_{\mathrm{fin}}(\mathbf W)
=
\varprojlim_{\mathcal A\in\operatorname{Fin}(\mathcal P)} E_{\mathcal A}
\]
is the **finite-consistency space**.

The full WR-I response quotient
\[
\mathcal Q_{\mathcal P}=\mathcal W/\!\sim_{\mathcal P}
\]
embeds canonically into \(\mathfrak C_{\mathrm{fin}}\). WR-II defines the
**global realizability defect** as the complement of that embedded image.

## Claim ceiling

WR-II does **not** claim that:

- a profile outside the declared world class is physically impossible;
- mathematical finite consistency implies physical existence;
- a global completion is unique unless uniqueness hypotheses are proved;
- a failure of global realizability means that the physical Universe does not exist;
- inverse-limit order is physical time or dynamics;
- a formal completion point is itself a physical world.

## Prior-art boundary

Finite-to-global extension is classical across many fields:

- compactness in first-order logic;
- inverse/projective limits and Mittag-Leffler conditions;
- Kolmogorov extension of finite-dimensional probability laws;
- Vorob'ev extension problems for consistent marginals;
- sheaf-theoretic contextuality and global-section obstructions;
- acyclicity criteria for global consistency in databases and positive semirings.

WR-II does not claim novelty for these theorems. Its target is the specific
WREH architecture: admissible global realizations, finite response images,
canonical embedding of the full response quotient into the finite-consistency
inverse limit, and the resulting model-relative global-realizability defect.

## Current preprint state

1. Formalize the finite-consistency inverse system.
2. Prove the canonical embedding of the WR-I full-response quotient.
3. Characterize global realizability as surjectivity / closedness.
4. Prove compactness-based existence criteria.
5. Prove a countable shrinking-fibre uniqueness criterion.
6. Build explicit positive and negative examples.
7. Audit against compactness, extension, contextuality, and local-to-global literature.


## v0.3 quantitative layer

For a target profile y, WR-II defines the finite fitting radius and global one-world fitting radius. Their difference is the finite-to-global stability gap.

The v0.3 draft proves:
- finite/global residual inequality;
- quantitative finite-family collapse;
- compact globalization with attainment;
- compact-core/coercivity globalization;
- stability under uniformly equivalent protocol scales;
- positive-gap and zero-radius-nonattainment counterexamples.

The quantitative layer is not an "approximate inverse system": the response inverse system remains exact. Approximation enters only through response-space residuals and declared protocol scales.

## Current gate

Before WR-II can be frozen for publication, the required next steps are:
1. independent external proof review;
2. at least one non-toy application;
3. final source/bibliography audit;
4. bilingual publication package and DOI deposition.
