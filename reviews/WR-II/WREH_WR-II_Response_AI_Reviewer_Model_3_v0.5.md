# Response to AI Reviewer Model 3 — WR-II v0.5

Date: 2026-10-07

## Overall decision

The comments are useful and are incorporated selectively.

## 1. Scalar notation in the moment benchmark

**Decision: ACCEPTED / ALREADY SATISFIED IN SOURCE.**

The current WR-II source uses scalar absolute values `|\cdot|` rather than norm bars in the raw-, relative-, and factorial-calibration formulas. No claim change.

## 2. Factorial-calibration tail estimate

**Decision: ACCEPTED AND STRENGTHENED.**

The proof has been replaced by an explicit uniform tail argument. For
[
a_{N,m}=(C\sqrt N)^{2m}/(2m)!,
]
the ratio
[
a_{N,m+1}/a_{N,m}
=
C^2N/((2m+2)(2m+1))
]
is less than one for all (m\ge N) once (N) is large. Hence the tail supremum is controlled at (m=N), and Stirling's formula gives (a_{N,N}\to0). The Gaussian normalized tail (1/(2^m m!)) is treated separately.

Effect on claim set: none; proof strengthened.

## 3. Tchakaloff positivity and probability normalization

**Decision: ACCEPTED.**

The proof now states explicitly that Tchakaloff yields a finitely supported positive measure matching all polynomials through the required degree, and because the constant polynomial (1) is included, the atomic measure has total mass one and therefore belongs to the declared probability-measure model class.

Effect on claim set: none; admissibility argument made explicit.

## 4. Moment-matrix / SOS obstruction certificates

**Decision: ACCEPTED AS OPEN-DIRECTION SUPPORT, NOT AS A COMPLETED WR-II RESULT.**

The Open Obligations section now records:
- negative eigenvalues of truncated Hankel/moment matrices as finite non-realizability certificates for positive representing measures;
- flat-extension/rank conditions as stronger finite-atomic certificates;
- moment-SOS/Lasserre hierarchies as a broader semidefinite route.

Citations added: Curto–Fialkow and Lasserre.

## 5. Super-resolution bridge

**Decision: ACCEPTED AS A BRIDGE, NOT AS AN IDENTIFICATION.**

The Open Obligations section now points to super-resolution and sparse recovery when the response map is Fourier- or moment-based, with Candès–Fernandez-Granda cited. WR-II does not claim that its general response architecture is equivalent to super-resolution theory.

## 6. Remez / alternation algorithms

**Decision: PARTIALLY ACCEPTED.**

Semi-infinite exchange methods are retained as natural candidates for finite-dimensional parametrizations. Remez-type alternation is explicitly restricted to settings with additional linear/Chebyshev approximation structure; it is not claimed as a generic WR-II algorithm.

## 7. L-curve / discrepancy principle comparison

**Decision: ACCEPTED AS A FUTURE NUMERICAL BENCHMARK.**

The Open Obligations section now asks for comparison of WR-II radii against standard data-fidelity and regularization diagnostics, including discrepancy-principle and L-curve behavior where mathematically appropriate.

## Release effect

WR-II v0.5 remains a **REVIEWABLE_DRAFT** intended for external proof review. No publication freeze or DOI is requested at this stage.
