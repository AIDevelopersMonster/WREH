# WR-IV retrospective-smoothing benchmark audit — v0.2

Date: 2026-10-08
Status: REVIEWABLE_DRAFT

## Benchmark

Fixed-interval retrospective smoothing of a linear Gaussian / diffusive state, with Brownian bridge as an exactly solvable physical case.

## Why it fits WR-IV

Later data sharpen inference about an earlier state while leaving residual historical uncertainty. This is exactly the distinction WR-IV needs, without invoking past rewriting or retrocausality.

## Mathematical checks

| ID | Check | Result |
|---|---|---|
| S01 | Gaussian conditional covariance formula | PASS |
| S02 | PSD contraction (P-CS^{-1}C^T\preceq P) | PASS |
| S03 | Directional strictness criterion | PASS |
| S04 | Brownian-bridge conditional mean | PASS |
| S05 | Brownian-bridge conditional variance | PASS |
| S06 | Positive residual interior variance | PASS |
| S07 | Noisy endpoint variance formula | PASS |
| S08 | Exact-set refinement distinguished from probabilistic covariance contraction | PASS |

## Prior-art boundary

Rauch--Tung--Striebel smoothing, Gaussian conditioning, and Brownian bridges are classical. No theorem-priority claim is made. WR-IV uses them as a benchmark for the WREH distinction between response-conditioned historical refinement and unique hidden past.

## Important claim firewall

With Gaussian observation noise, posterior support can remain full-dimensional. Therefore the noisy-smoothing result must not be described as literal set inclusion of supports. The exact WR-IV completion-refinement theorem and the probabilistic covariance-contraction theorem are separate layers.

## Next obligation

Build one richer state-space example with multiple observations, or promote this benchmark into the main review preprint after source-level prior-art verification.

Release status: REVIEWABLE_DRAFT

## Historical snapshot notice

This audit applies to v0.2. The independent v0.2 audit found additional qualifications, implemented in v0.3. The active review record is [WREH_WR-IV_Repair_Audit_v0.3.md](WREH_WR-IV_Repair_Audit_v0.3.md); the earlier PASS rows do not certify the original v0.2 for publication.
