# WR-III range-localization benchmark audit — v0.4

Date: 2026-10-08
Status: REVIEWABLE_DRAFT

## Benchmark identity

Planar range-only localization of one unknown point from squared distances to fixed anchors.

## Mathematical checks

| ID | Check | Result |
|---|---|---|
| L01 | One-anchor fibre is a circle of radius sqrt(u), singleton at u=0 | PASS |
| L02 | Two-anchor inverse formulas x=(u-v)/(4a), y^2=q(u,v) | PASS |
| L03 | Two-anchor fibre diameter D=2 sqrt(q) | PASS |
| L04 | Jacobian determinant det dR=8ay | PASS |
| L05 | Structural wall q=0 equals collapse of two sheets to one | PASS |
| L06 | Conditional derivative dr2 on coarse-fibre tangent equals 4ay | PASS |
| L07 | Third noncollinear squared-range response determines y uniquely | PASS |
| L08 | Three-anchor differential has rank two everywhere | PASS |
| L09 | Three-anchor map is proper injective immersion, hence embedding | PASS |
| L10 | Structural wall is empty relative to intrinsic three-anchor image | PASS |

## Prior-art boundary

Distance-based sensor/network localization and trilateration are established subjects. Aspnes et al. (2006) develop network-localization theory using distance constraints and rigidity; Anderson et al. (2010) state the standard role of three or more noncollinear anchors in planar localizability and analyze noisy distance measurements.

WR-III therefore makes no novelty claim for one-/two-/three-anchor trilateration. The application is a benchmark for the WREH refinement architecture.

## New information supplied by the benchmark

1. It gives a physically recognizable inverse problem where fibre diameter decreases under added protocols.
2. It realizes the conditional-rank defect as failure of a new range measurement to vary along the coarse circular fibre.
3. It shows the structural wall can change from a point to a fold curve and then disappear under further refinement.
4. It exposes the distinction between intrinsic response-image regularity and ambient target-space rank: the three-anchor image is a two-dimensional embedded surface in R^3.

## Claim ceiling

- No claim that the localization formulas are new.
- No claim that fold walls are physical phase transitions.
- No claim that range protocols model all inverse problems.
- No physical interpretation is assigned to fibre diameter without the Euclidean position metric.

## Release effect

The non-toy application obligation is now satisfied at benchmark level. Remaining gates are detailed prior-art citation integration, promotion from spine to preprint, compilation/render audit, and external review.

Release status: REVIEWABLE_DRAFT