# WR-II theorem and dependency map — v0.1

## Upstream

WR-II inherits the world-response structure and full response quotient from WR-I v0.3.

- DOI: 10.5281/zenodo.23210258
- inherited objects: W, P, response maps, and the full response quotient
- inherited firewall: response equivalence is operational/model-relative, not ontological identity.

## Core dependency graph

WR-I world-response structure
-> finite realizable images E_A
-> finite-consistency inverse limit C_fin
-> canonical embedding of the WR-I full quotient
-> global realizability defect D_fin

## Result map

### R1 — Finite response inverse system
Restriction maps between finite response images are surjective.

Status: PROVED.

### R2 — Profile representation
The finite-consistency inverse limit is exactly the set of full profiles whose every finite restriction is realizable.

Status: PROVED.

### R3 — Canonical embedding
The full WR-I response quotient embeds injectively into the finite-consistency space, with image equal to the full response image.

Status: PROVED.

### R4 — Profile trichotomy
Every full profile is exactly one of:
1. finitely obstructed;
2. finitely consistent but globally unrealized;
3. globally realized.

Status: PROVED.

### R5 — Finite-family collapse
If the protocol family is finite, the full-finite/global defect is empty.

Status: PROVED.

Interpretation: a genuine full-finite/global gap requires an infinite protocol family. Finite contextuality requires a restricted context family.

### R6 — Explicit global completion defect
Finite-support binary worlds realize every finite binary pattern, but not the infinite all-ones profile.

Status: PROVED COUNTEREXAMPLE.

### R7 — Finite-projection closure
Finite-projection closure is a closure operator and the finite-consistency space is the closure of the full response image under all finite coordinate projections.

Status: PROVED.

### R8 — Closed-image criterion
If the full response image is closed in the product topology, the defect is empty.

Status: PROVED.

### R9 — Compact realization criterion
If the world class is compact, response spaces are Hausdorff, and responses are continuous, the defect is empty.

Status: PROVED.

### R10 — Countable compact nested-fibre existence
For a countable protocol family, nonempty nested closed exact target fibres in a compact world space have a common point.

Status: PROVED.

### R11 — Shrinking-fibre uniqueness
In a complete metric world space, nonempty closed exact target fibres whose diameters tend to zero have exactly one common realization.

Status: PROVED.

### R12 — Context-consistency embedding
For a downward-closed context cover, the full WR-I quotient embeds into the compatible context-response limit.

Status: PROVED.

### R13 — Finite contextual completion defect
For even-parity worlds {000, 011, 101, 110} with pair contexts, the local family 11 / 11 / 11 is overlap-compatible and locally realizable but has no admissible global world.

Status: PROVED COUNTEREXAMPLE.

## Open obligations

- approximate/noisy finite consistency;
- quantitative distance to global realizability;
- obstruction certificates;
- stability under enlargement of the world class;
- relation between finite-projection closure and metric/uniform completion;
- computational algorithms for finite approximations;
- physically motivated context families.

## Claim firewall

No result above implies that:
- the physical Universe is one of several mathematical completions;
- failure inside the declared world class is absolute physical nonexistence;
- the inverse-limit index is time;
- contextual nonextension proves a preferred interpretation of quantum theory.


## Quantitative / noisy extension

### R14 — Finite-to-global residual inequality

For normalized residuals,
[
delta_{mathrm{fin}}(y)ledelta_{mathrm{glob}}(y).
]

Status: PROVED.

### R15 — Compact finite-to-global residual identity

If the world class is compact and protocol residuals are lower semicontinuous, then
[
delta_{mathrm{glob}}(y)=delta_{mathrm{fin}}(y),
]
and the global infimum is attained.

Status: PROVED.

### R16 — Tolerance globalization

Under the compact hypotheses, if every finite bundle can be fitted within the declared protocol tolerances, then one world fits all protocols within those same tolerances.

Status: PROVED.

### R17 — Vanishing-noise exactification

Under the same compact hypotheses,
[
delta_{mathrm{fin}}(y)=0
]
implies an exact global realization.

Status: PROVED.

### R18 — Compact-core residual identity

Global compactness can be weakened: if one finite response bundle has a compact sublevel set above the finite residual radius, then
[
delta_{mathrm{glob}}(y)=delta_{mathrm{fin}}(y)
]
and the global infimum is attained.

Status: PROVED.

Interpretation: a finite protocol bundle can act as a coercive anchor preventing near-optimal witnesses from escaping to infinity.

### R19 — Positive stability-gap example

Finite-support binary worlds with the discrete metric and unit protocol scales satisfy
[
delta_{mathrm{fin}}=0,qquad delta_{mathrm{glob}}=1.
]

Status: PROVED COUNTEREXAMPLE.

### R20 — Zero-margin nonattainment example

For the same world class with scales (sigma_n=n),
[
delta_{mathrm{fin}}=delta_{mathrm{glob}}=0
]
but no exact global realization exists.

Status: PROVED COUNTEREXAMPLE.

Interpretation: zero residual radius does not imply exact realization unless attainment/compactness is available.

## Terminology firewall for the noisy layer

The WR-II noisy construction is **not** called an approximate inverse system.

- the finite-response inverse system remains exactly commutative;
- approximation enters only through target-response residuals and declared protocol scales;
- classical approximate inverse-system theory instead relaxes the bonding-map commutativity itself.

Quantitative contextuality is also prior art in context-restricted probabilistic models. WR-II does not claim novelty for robustness measures of contextuality.


## Sparse moment reconstruction benchmark

### R21 — Exact finite moment consistency

For the class of finitely supported probability measures on R and Gaussian target moments, every finite protocol bundle is matched exactly.

Status: PROVED.

### R22 — No exact global sparse realization

No finitely supported probability measure reproduces the full Gaussian moment sequence.

Status: PROVED.

### R23 — Raw calibration divergence

For sigma_n = 1,
delta_fin = 0 while delta_glob = infinity.

Status: PROVED.

### R24 — Relative calibration positive gap

For sigma_n = max(1, |y_n|),
delta_fin = 0, delta_glob = 1, and Gamma = 1.

Status: PROVED.

### R25 — Factorial calibration nonattainment

For sigma_n = n!,
delta_fin = delta_glob = 0, but no exact global sparse realization exists.

Status: PROVED.

Interpretation: the same exact model-class mismatch can appear as infinite global error, finite positive stability gap, or zero-distance nonattainment under non-uniformly equivalent response calibrations.
