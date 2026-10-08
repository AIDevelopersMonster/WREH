# Response to AI Reviewer Model 2 — WR-III v0.6

**Document:** WR-III — *Geometry of Admissible World Fibres: Refinement, Rigidity and Realizability Walls*  
**Date:** 2026-10-08

## Overall decision

The review is accepted with minor notation-level refinements. No reviewer point requires weakening or changing the principal theorem set.

## 1. Conditional-rank notation

**Decision: ACCEPTED.**

The notation
\[
dS_x|_{\ker dR_{\mathcal A,x}}
\]
was mathematically valid but slightly informal in a rank formula. The v0.6 text now uses
\[
\dim\bigl(dS_x(\ker dR_{\mathcal A,x})\bigr)
\]
and states the submersion criterion as
\[
dS_x(\ker dR_{\mathcal A,x})=T_{S(x)}Z.
\]

**Effect on claim set:** none; notation strengthened.

## 2. Algebraic transparency in the two-anchor benchmark

**Decision: ACCEPTED.**

The v0.6 text now explicitly inserts
\[
x=\frac{u-v}{4a}
\]
into
\[
y^2=u-(x+a)^2
\]
before displaying the simplified expression
\[
q(u,v)
=
\frac{u+v}{2}-a^2-\frac{(u-v)^2}{16a^2}.
\]

**Effect on claim set:** none; exposition improved.

## 3. Explicit two-point set

**Decision: ACCEPTED.**

The fibre for \(q(u,v)>0\) is now written as the explicit two-element set
\[
\left\{
\left(\frac{u-v}{4a},\sqrt{q(u,v)}\right),
\left(\frac{u-v}{4a},-\sqrt{q(u,v)}\right)
\right\}.
\]

**Effect on claim set:** none; notation repaired.

## 4. Bridge from WR-II to WR-III

**Decision: ACCEPTED.**

The upstream section now states explicitly that WR-II supplies conditions under which a response-compatible fibre is nonempty, while WR-III assumes nonemptiness and studies the resulting geometric and topological structure.

**Effect on claim set:** clarifies programme dependency.

## 5. Use of the word fibre

**Decision: ACCEPTED.**

Definition 2.1 now states that WR-III uses “fibre” for the set-theoretic preimage
\[
R_{\mathcal A}^{-1}(e),
\]
anticipating bundle structures studied later; no bundle structure is assumed at the definition stage.

**Effect on claim set:** clarifies terminology.

## 6. Noisy localization and future work

**Decision: DEFERRED TO NEXT TECHNICAL LAYER.**

The reviewer correctly identifies noisy ranges and conditioning near the fold wall as a high-value continuation. That extension changes the mathematical object from exact fibres to uncertainty tubes / approximate fibres and should not be inserted into the present exact-geometry paper without a separate proof layer.

It remains an explicit downstream obligation.

## 7. Interactive HTML presentation

**Decision: ACCEPTED AND IMPLEMENTED.**

In response to Reviewer 1 and reinforced by Reviewer 2, WR-III now includes an interactive HTML companion demonstrating the one-anchor / two-anchor / three-anchor localization refinement ladder and the monotone-rigidity/non-monotone-wall distinction.

## Release effect

The reviewer corrections contain no blocking mathematical issue. After successful compilation/render audit of v0.6, the manuscript may be promoted to REVIEWED_CLEAN and then prepared for bilingual publication.
