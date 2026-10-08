# WR-III theorem and dependency map — v0.6

## Upstream

WR-III inherits:

- WR-I response maps, response equivalence, and response-defined quotients — DOI 10.5281/zenodo.23210258;
- WR-II realizable response images, nonempty compatible fibres, and finite/global realizability discipline — DOI 10.5281/zenodo.23224154.

WR-II provides conditions under which a response-compatible inverse image is nonempty. WR-III assumes nonemptiness and studies the geometry and topology of that set.

## Core object

For a declared geometric realization carrier \(X\) and protocol bundle \(\mathcal A\),
\[
\Phi_{\mathcal A}(e)=R_{\mathcal A}^{-1}(e),
\qquad
e\in E_{\mathcal A}=R_{\mathcal A}(X).
\]

The word *fibre* is used for this set-theoretic preimage before any fibre-bundle structure is assumed.

## Core exact results

### R1 — Refinement inclusion

If \(\mathcal A\subseteq\mathcal B\), then
\[
\Phi_{\mathcal B}(e_{\mathcal B})
\subseteq
\Phi_{\mathcal A}
\bigl(\rho_{\mathcal B\mathcal A}(e_{\mathcal B})\bigr).
\]

Status: PROVED.

### R2 — Fibre-diameter monotonicity

\[
D_{\mathcal B}(e_{\mathcal B})
\le
D_{\mathcal A}
\bigl(\rho_{\mathcal B\mathcal A}(e_{\mathcal B})\bigr).
\]

Status: PROVED.

### R3 — Pulled-back rigidity monotonicity

For every \(\varepsilon\ge0\),
\[
E_{\mathcal B}\cap
\rho_{\mathcal B\mathcal A}^{-1}
(\mathcal R_{\mathcal A}^{\varepsilon})
\subseteq
\mathcal R_{\mathcal B}^{\varepsilon}.
\]

Status: PROVED.

### R4 — Rigidity gain

\[
G_{\mathcal B\mid\mathcal A}(e_{\mathcal B})
=
D_{\mathcal A}
\bigl(\rho_{\mathcal B\mathcal A}(e_{\mathcal B})\bigr)
-
D_{\mathcal B}(e_{\mathcal B})
\ge0.
\]

Status: DEFINED / NONNEGATIVITY PROVED.

### R5 — Conditional-rank formula

For a smooth refinement
\[
R_{\mathcal B}=(R_{\mathcal A},S)
\]
at a point where \(dR_{\mathcal A,x}\) is surjective,
\[
\operatorname{rank}dR_{\mathcal B,x}
=
\dim Y_{\mathcal A}
+
\dim\bigl(dS_x(\ker dR_{\mathcal A,x})\bigr).
\]

The refined map is a submersion at \(x\) iff
\[
dS_x(\ker dR_{\mathcal A,x})=T_{S(x)}Z.
\]

Status: PROVED.

Prior-art note: related augmented-map critical loci are classical in relative polar geometry. No singularity-theory priority is claimed.

### R6 — Container for refinement-created walls

For a proper smooth refinement above a coarse regular value, every refined structural-wall value lies in the image of the conditional rank-defect set.

Status: PROVED.

## Set-valued and metric stability

### R7 — Closed-map criterion

For a surjection \(R:X\to E\), the inverse correspondence is upper hemicontinuous iff \(R\) is closed.

Status: PROVED / STANDARD PRIOR ART.

### R8 — Open-map criterion

For a surjection \(R:X\to E\), the inverse correspondence is lower hemicontinuous iff \(R\) is open.

Status: PROVED / STANDARD PRIOR ART.

### R9 — Diameter upper semicontinuity

For compact metric \(X\), metric \(E\), and continuous surjective \(R\),
\[
D(e)=\operatorname{diam}R^{-1}(e)
\]
is upper semicontinuous.

Status: PROVED.

### R10 — Open epsilon-rigidity loci

For every \(\varepsilon>0\),
\[
\{e:D(e)<\varepsilon\}
\]
is open.

Status: PROVED.

### R11 — Exact rigidity is \(G_\delta\)

\[
\{e:D(e)=0\}
=
\bigcap_{n\ge1}\{e:D(e)<1/n\}.
\]

Status: PROVED.

### R12 — Hausdorff continuity under an open response map

For compact metric \(X\), metric \(E\), and continuous open surjective \(R\), the compact fibres vary continuously in Hausdorff distance; consequently \(D(e)\) is continuous.

Status: PROVED.

## Structural regularity and walls

### R13 — Proper smooth regularity

For a proper smooth response map between manifolds, realizable regular values are structurally regular by Ehresmann local triviality.

Status: PROVED / AUDIT REPAIRED.

### R14 — Rigidity is not structural regularity

Sphere-height response has singleton fibres at singular wall points.

Status: PROVED EXAMPLE.

### R15 — Refinement can create a wall

\[
(x,y)\mapsto(x,y^3-xy)
\]
refines the wall-free coarse response \(x\) and creates a semicubical cusp bifurcation set.

Status: PROVED EXAMPLE.

### R16 — Refinement can resolve a wall

The coarse map
\[
(x,\theta)\mapsto x^2
\]
on \([-1,1]\times S^1\) has a branch wall at zero, while
\[
(x,\theta)\mapsto(x^2,x)
\]
is a globally trivial \(S^1\)-bundle over its intrinsic response image.

Status: PROVED EXAMPLE.

### R17 — Refinement asymmetry

Rigidity is monotone under protocol refinement after pullback, whereas structural bifurcation walls are not monotone: refinement can create or resolve them.

Status: PROVED as an organizational contrast.

## Range-only localization benchmark

### R18 — One-anchor circular ambiguity

For one planar squared-range protocol, the fibre at \(u>0\) is a circle of diameter
\[
D_1(u)=2\sqrt u,
\]
while \(u=0\) is a singleton structural wall.

Status: PROVED.

### R19 — Two-anchor exact fibre geometry

For anchors \((-a,0)\) and \((a,0)\),
\[
q(u,v)
=
\frac{u+v}{2}
-a^2
-\frac{(u-v)^2}{16a^2}.
\]

For \(q>0\), the fibre is the explicit two-point mirror pair and
\[
D_{12}(u,v)=2\sqrt{q(u,v)}.
\]

For \(q=0\), the fibre is a singleton.

Status: PROVED.

### R20 — Two-anchor fold wall

The two-anchor structural wall is exactly
\[
q(u,v)=0.
\]

The Jacobian determinant is
\[
8ay,
\]
so the anchor baseline is the critical set and maps to the fold wall.

Status: PROVED.

### R21 — Conditional-rank realization in localization

For refinement from the first range to the second,
\[
dr_2(\tau)=4ay
\]
on a tangent direction \(\tau\) to the coarse circular fibre. Conditional rank is lost exactly on the baseline away from the inherited coarse singular point.

Status: PROVED.

### R22 — Three-anchor exact rigidity

Adding a third noncollinear anchor makes the planar squared-range response map an embedding into its intrinsic response image. Every fibre is a singleton and the intrinsic structural wall is empty.

Status: PROVED.

### R23 — Localization refinement ladder

\[
\text{circle ambiguity}
\longrightarrow
\text{mirror-pair ambiguity with fold wall}
\longrightarrow
\text{exact localization with no intrinsic wall}.
\]

Status: PROVED APPLICATION BENCHMARK.

## Claim ceiling

WR-III does not claim novelty for generic fibre geometry, hemicontinuity, Ehresmann/Hardt/Thom triviality, relative polar geometry, Reeb constructions, or trilateration formulas.

The WREH contribution is the programme architecture connecting:
- nonempty response fibres downstream of WR-I/WR-II;
- protocol-refinement shrinkage;
- metric rigidity and rigidity gain;
- conditional rank of added observables along coarse fibres;
- the monotone-rigidity / non-monotone-wall contrast.

## Companion demo

Official review companion:

papers/WR-III/demo/WREH_WR-III_Interactive_Companion_v0.2.html

The demo is explanatory only. Formal claims remain in the manuscript.

## Remaining obligations

- noisy / bounded-uncertainty extension of the localization benchmark;
- useful monotone fibre invariants beyond diameter;
- quantitative distance-to-bifurcation after a metric/regularity class is fixed;
- stratified / semialgebraic extension;
- computable bounds for rigidity gain in a useful model class.

Current release state: **PUBLISHED / FROZEN v0.6** — DOI `10.5281/zenodo.23228682`.
