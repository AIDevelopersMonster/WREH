# WR-III theorem and dependency map — v0.1

## Upstream

WR-III inherits:

- WR-I response maps, response equivalence, and response-defined quotients — DOI 10.5281/zenodo.23210258;
- WR-II realizable response images, nonempty compatible fibres, and finite/global realizability discipline — DOI 10.5281/zenodo.23224154.

WR-III starts only after realizability. Its new object is the variation of nonempty inverse fibres over response space.

## Core object

For a declared geometric realization carrier \(X\) and protocol bundle \(\mathcal A\),
\[
\Phi_{\mathcal A}(e)=R_{\mathcal A}^{-1}(e),
\qquad
e\in E_{\mathcal A}=R_{\mathcal A}(X).
\]

## Result map

### R1 — Refinement inclusion

If \(\mathcal A\subseteq\mathcal B\), then
\[
\Phi_{\mathcal B}(e_{\mathcal B})
\subseteq
\Phi_{\mathcal A}(\rho_{\mathcal B\mathcal A}e_{\mathcal B}).
\]

Status: PROVED.

### R2 — Fibre-diameter monotonicity

On a fixed metric realization carrier,
\[
D_{\mathcal B}(e_{\mathcal B})
\le
D_{\mathcal A}(\rho_{\mathcal B\mathcal A}e_{\mathcal B}).
\]

Status: PROVED.

### R3 — Refinement preserves exact and epsilon-rigidity

A nonempty finer fibre contained in a singleton or sub-epsilon coarser fibre preserves the corresponding rigidity property.

Status: PROVED.

### R4 — Compact-carrier upper hemicontinuity

For a continuous surjection from compact \(X\) to Hausdorff response image \(E\), the inverse-fibre correspondence is compact-valued and upper hemicontinuous.

Status: PROVED.

### R5 — Openness criterion for lower hemicontinuity

For a surjection \(R:X\to E\), the inverse correspondence is lower hemicontinuous iff \(R\) is open.

Status: PROVED.

### R6 — Fibre-diameter upper semicontinuity

For compact metric \(X\), metric \(E\), and continuous surjective \(R\),
\[
D(e)=\operatorname{diam}R^{-1}(e)
\]
is upper semicontinuous.

Status: PROVED.

### R7 — Open finite-resolution rigidity loci

For every \(\varepsilon>0\),
\[
\{e:D(e)<\varepsilon\}
\]
is open.

Status: PROVED.

### R8 — Exact rigidity is G-delta

\[
\{e:D(e)=0\}
=
\bigcap_{n\ge1}\{e:D(e)<1/n\}.
\]

Status: PROVED.

### R9 — Proper smooth regularity

For a proper smooth response map between manifolds, realizable regular values are structurally regular by Ehresmann local triviality.

Status: PROVED, subject to detailed proof audit of the local-surjectivity step.

### R10 — Rigidity is not structural regularity

Sphere-height response gives singleton fibres exactly at singular wall points.

Status: PROVED EXAMPLE.

## New wall vocabulary

- **structural wall:** failure locus of local fibre triviality inside realizable response space;
- **attainable-response boundary:** topological boundary of the realizable image in a declared ambient response space;
- **realizability wall:** union of the two.

All three are model-relative mathematical objects.

## Open obligations

- prior-art audit against set-valued analysis, singularity theory, stratified maps, and identifiability geometry;
- proof audit of smooth/proper wall theorem;
- useful invariants beyond diameter;
- wall-distance and wall-stability notions;
- refinement effects on walls;
- non-toy inverse-problem benchmark;
- interactive demo.
