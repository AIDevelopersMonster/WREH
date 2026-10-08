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

For a proper smooth response map between manifolds, realizable regular values are structurally regular by Ehresmann local triviality. The proof now explicitly establishes a response neighborhood contained in the image before applying Ehresmann.

Status: PROVED / AUDIT REPAIRED.

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


## Audit consequence

The phrase **structural wall** is WREH vocabulary for a standard bifurcation / atypical-value locus: failure of local fibre triviality. No theorem-priority claim is made for that object.

The next genuinely programme-specific obligation is not another generic fibre theorem. It is to determine how **protocol refinement transforms rigidity and bifurcation loci**.

Prior-art controls now explicitly include:
- set-valued inverse maps and hemicontinuity;
- Ehresmann and bifurcation sets;
- Thom / stratified isotopy and Hardt semialgebraic triviality;
- identifiability fibre geometry;
- Reeb-type fibre topology summaries.


## Refinement theorem layer

### R11 — Pulled-back rigidity monotonicity

For every epsilon >= 0,
[
E_{mathcal B}cap
ho_{mathcal Bmathcal A}^{-1}(mathcal R_{mathcal A}^{epsilon})
subseteq
mathcal R_{mathcal B}^{epsilon}.
]

Status: PROVED.

Interpretation: protocol refinement cannot destroy exact or finite-resolution rigidity already present at the coarser response.

### R12 — Rigidity gain

On a fixed metric realization carrier,
[
G_{mathcal Bmidmathcal A}
=
D_{mathcal A}circho_{mathcal Bmathcal A}
-
D_{mathcal B}
ge 0.
]

Status: DEFINED / NONNEGATIVITY PROVED.

### R13 — Conditional-rank formula

For a smooth refinement
[
R_{mathcal B}=(R_{mathcal A},S)
]
at a point where (dR_{mathcal A}) is surjective,
[
operatorname{rank}dR_{mathcal B}
=
dim Y_{mathcal A}
+
operatorname{rank}
left(dS|_{ker dR_{mathcal A}}ight).
]

Status: PROVED.

Prior-art note: in analytic/algebraic singularity theory, closely related critical loci of augmented maps are organized by relative polar varieties. No novelty claim is made for the underlying rank-defect object.

### R14 — Container for refinement-created walls

For a proper smooth refinement above a coarse regular value, every refined structural-wall value lies in the image of the conditional rank-defect set.

Status: PROVED.

### R15 — Refinement can create a wall

The map
[
(x,y)mapsto (x,y^3-xy)
]
refines the wall-free coarse map (x) and creates a semicubical cusp bifurcation set.

Status: PROVED EXAMPLE.

### R16 — Refinement can resolve a wall

The coarse map
[
(x,	heta)mapsto x^2
]
on ([-1,1]	imes S^1) has a branch wall at zero, while the refinement
[
(x,	heta)mapsto (x^2,x)
]
is globally a trivial (S^1)-bundle over its response image.

Status: PROVED EXAMPLE.

### R17 — Refinement asymmetry

Rigidity loci are monotone under pullback by protocol refinement, whereas structural bifurcation walls are not monotone: refinement can create or resolve them.

Status: PROVED as an organizational contrast by R11, R15, and R16.

Claim ceiling: this is a WREH organizational theorem, not a priority claim over singularity theory or relative polar geometry.


## Range-only localization benchmark

### R18 — One-anchor circular ambiguity

For one planar squared-range protocol, the fibre at range-squared u>0 is a circle of diameter
[
D_1(u)=2sqrt u,
]
while u=0 is a singleton structural wall.

Status: PROVED.

### R19 — Two-anchor exact fibre geometry

For anchors (-a,0) and (a,0), the realizable response pair (u,v) satisfies
[
q(u,v)
=
rac{u+v}{2}-a^2-rac{(u-v)^2}{16a^2}
ge0.
]
Interior fibres have two mirror-related points and
[
D_{12}(u,v)=2sqrt{q(u,v)}.
]
Boundary fibres q=0 are singletons.

Status: PROVED.

### R20 — Two-anchor fold wall

The two-anchor structural wall is exactly
[
q(u,v)=0.
]
The Jacobian determinant is
[
8ay,
]
so the anchor baseline is the critical set and maps to the fold wall.

Status: PROVED.

### R21 — Conditional-rank realization in localization

For the refinement from the first range to the second,
[
dr_2|_{ker dr_1}=0
]
exactly on the anchor baseline away from the inherited coarse singular point. Thus the conditional-rank mechanism reproduces the fold wall.

Status: PROVED.

### R22 — Three-anchor exact rigidity

Adding a third noncollinear anchor makes the planar squared-range map an embedding into its intrinsic response image. Every fibre is a singleton and the intrinsic structural wall is empty.

Status: PROVED.

### R23 — Localization refinement ladder

The standard range-only inverse problem exhibits
[
	ext{circle ambiguity}
	o
	ext{mirror-pair ambiguity with fold wall}
	o
	ext{exact localization with no intrinsic wall}.
]

Status: PROVED APPLICATION BENCHMARK.

Prior-art note: the localization/trilateration facts are classical. The WREH contribution is their organization through fibre diameter, rigidity gain, conditional rank, and bifurcation-wall diagnostics.
