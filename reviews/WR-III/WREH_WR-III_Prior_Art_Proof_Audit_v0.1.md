# WR-III prior-art and proof audit — v0.1

Date: 2026-10-08
Status: REVIEWABLE_DRAFT

## Executive finding

WR-III is viable, but its novelty must be narrower than the v0.1 wording suggests. The mathematical language of inverse fibres, upper/lower hemicontinuity, local triviality, bifurcation values, stratified triviality, and fibre topology is mature prior art. The defensible WREH contribution is architectural: placing these tools downstream of WR-I identifiability and WR-II realizability, then studying protocol refinement together with fibre-size/rigidity diagnostics under an explicit claim firewall.

## Audit findings

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| A01 | C1 | Proper smooth theorem | Ehresmann proof does not explicitly establish a surjective neighborhood U contained in the image before applying the fibration theorem. | Proper submersion theorem requires the local map onto the chosen base. | Use the submersion theorem at a point of the regular fibre to obtain U0 inside the image, intersect with a critical-value-free neighborhood, then apply Ehresmann. | clarifies |
| A02 | C4 | Structural wall terminology | Failure of local fibre triviality is standardly described by bifurcation or atypical-value sets. | Calling it a wall without prior-art control risks renaming an established object. | State that Sigma_str is WREH vocabulary for a bifurcation locus; make no priority claim. | narrows |
| A03 | C4 | Set-valued continuity | Upper/lower hemicontinuity of inverse multifunctions is classical. | Core v0.1 propositions are infrastructure rather than novelty. | Cite set-valued analysis and identify open/closed-map criteria as prior art. | narrows |
| A04 | C4 | Beyond smooth proper maps | Thom isotopy and Hardt triviality already provide stratified/semialgebraic local-triviality frameworks. | WR-III must not rediscover tame triviality as a new wall theorem. | Treat stratified/Hardt theory as the next comparison layer. | narrows |
| A05 | C4 | Identifiability geometry | Parameter-fibre dimension/components are already used in structural-identifiability geometry. | Fibre geometry itself is not new. | Make novelty depend on WREH handoff + refinement + rigidity architecture, not generic fibre invariants. | narrows |
| A06 | C6 | Wall vocabulary | The word wall may suggest codimension one. | No such theorem exists in v0.1. | State explicitly that a wall need not be a hypersurface or manifold. | clarifies |
| A07 | C6 | Fibre diameter | Diameter is metric-dependent. | Physical meaning requires declared geometry. | Keep metric dependence explicit and seek invariant/normalized alternatives later. | clarifies |

## Prior-art boundary

1. Set-valued analysis: inverse multifunction continuity, compact-valued correspondences, upper/lower hemicontinuity.
2. Ehresmann / bifurcation theory: proper submersions are locally trivial; nonproper maps may have bifurcation values at infinity.
3. Thom / Hardt: stratified and semialgebraic maps admit local or piecewise triviality under standard hypotheses.
4. Identifiability geometry: generic fibre dimension, degree, and components are established diagnostics.
5. Reeb-space literature: connected components of fibres and their topology are already organized by quotient constructions.

## Novelty claim permitted after audit

WR-III may claim a WREH-specific organization of nonempty response fibres downstream of WR-I and WR-II, protocol-refinement shrinkage, metric finite-resolution rigidity, and a controlled response-space bifurcation/wall vocabulary. It may not claim invention of fibre geometry, bifurcation sets, local triviality, or set-valued continuity.

## Recommended new theorem target

The next genuinely programme-specific result should concern how protocol refinement transforms rigidity loci or bifurcation loci. Elementary fibre inclusion and diameter monotonicity alone are too close to standard inverse-image geometry to carry the paper.

## Release assessment

Unresolved blocking issues: A01 proof hypothesis/argument repair and prior-art integration.
Claim set changed: narrows.
Bibliography verified: partial.
Metadata verified: yes for WR-I/WR-II inheritance.
Source compiled: not yet after audit patches.
PDF visually inspected: not yet.
Release status: REVIEWABLE_DRAFT.