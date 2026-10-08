# WR-III refinement theorem audit — v0.3

Date: 2026-10-08
Status: REVIEWABLE_DRAFT

## Audit summary

The new refinement layer is mathematically coherent after internal proof check. The strongest programme-specific statement is the contrast between monotone rigidity and non-monotone structural bifurcation under added protocols. The conditional-rank formula is correct but has direct relatives in relative polar / augmented-map singularity theory and must not be presented as a new singularity-theory construction.

## Findings

| ID | Severity | Location | Problem | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|
| R01 | C4 | Conditional-rank theorem | Criticality of an added observable along coarse fibres is close to relative polar geometry. | Add explicit prior-art note and remove novelty implication. | narrows |
| R02 | C6 | Refinement asymmetry remark | 'genuinely WREH-specific' could be read as theorem-priority. | Rephrase as programme-level organizing contrast. | narrows |
| R03 | C6 | Wall examples | Creation/resolution examples compare different response spaces and should be read existentially, not as a canonical wall map. | Keep statement at non-monotonicity level only. | clarifies |

## Proof checks

- Pulled-back rigidity monotonicity: PASS.
- Conditional-rank formula: PASS.
- Proper-smooth wall container: PASS under the repaired Ehresmann wall theorem.
- Cusp example: PASS; map is proper and surjective; critical image satisfies 27 v^2 = 4 u^3.
- Wall-resolution example: PASS as a topological bundle example.
- Refinement asymmetry theorem: PASS as an existential organizational theorem.

## Remaining obligations

- Source-level citation for relative polar varieties / augmented-map critical loci.
- One non-toy inverse or identifiability application.
- Extension to a tame/stratified category.
- Render audit after promotion to preprint.

## Release status

REVIEWABLE_DRAFT