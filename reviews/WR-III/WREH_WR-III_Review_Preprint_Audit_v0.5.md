# WR-III review-preprint audit — v0.5

**Document:** WR-III — *Geometry of Admissible World Fibres: Refinement, Rigidity and Realizability Walls*  
**Date:** 2026-10-08  
**Status:** REVIEWABLE_DRAFT

## Claim ceiling

The manuscript is model-relative. It does not identify response fibres with ontological ensembles, protocol refinement with physical time or dynamics, bifurcation values with physical phase transitions, or WREH walls with physical boundaries of spacetime or the Universe.

## Audit findings resolved in v0.5

| ID | Severity | Location | Problem | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|
| V05-01 | C3 | Rigidity sections | Exact/epsilon rigidity was defined twice after successive spine revisions. | Consolidated rigidity definitions and refinement theorem into one section. | clarifies |
| V05-02 | C4 | Upper hemicontinuity | Standard closed-map characterization had been omitted from the carried-forward v0.4 source. | Restored the closed-map iff upper-hemicontinuity theorem and reduced compactness result to a corollary. | narrows |
| V05-03 | C5 | Fibre stability | Earlier Hausdorff-continuity audit patch was not carried into v0.4. | Restored the open-map + compact-carrier Hausdorff-continuity theorem. | clarifies |
| V05-04 | C2 | Realizability-wall boundary | Ambient boundary is pathological when the realizable image is lower-dimensional in an arbitrary product target. | Restrict boundary diagnostic to a declared full-dimensional response manifold/stratum and add an ambient-space firewall. | narrows |
| V05-05 | C4 | Prior-art section | Set-valued, bifurcation, relative-polar, Hardt, identifiability, Reeb, and localization claims needed source-level control. | Added explicit prior-art citations and narrowed novelty to WREH architecture. | narrows |
| V05-06 | C5 | Bibliography | Aubin--Frankowska metadata was stale and several audit references were missing. | Updated edition/DOI and added verified bibliography entries. | none |
| V05-07 | C5 | Release artifact | No unified review PDF existed after v0.4 benchmark integration. | Built and visually audited a 15-page English review PDF. | none |

## Mathematical proof checks

- Refinement inclusion and diameter monotonicity: PASS.
- Pulled-back rigidity monotonicity: PASS.
- Conditional-rank formula: PASS.
- Proper-smooth container for refinement-created walls: PASS under stated hypotheses.
- Closed-map / upper-hemicontinuity criterion: PASS.
- Open-map / lower-hemicontinuity criterion: PASS.
- Diameter upper semicontinuity: PASS.
- Hausdorff continuity under compact + open response map: PASS.
- Proper-smooth Ehresmann regularity theorem: PASS after explicit local-surjectivity repair.
- Cusp wall-creation example: PASS.
- Coarse-wall resolution example: PASS.
- One-/two-/three-anchor localization ladder: PASS.
- Intrinsic-vs-ambient response-image distinction: PASS after v0.5 boundary firewall.

## Novelty boundary

WR-III does **not** claim novelty for:
- set-valued inverse-map continuity;
- open/closed-map criteria;
- Ehresmann local triviality;
- bifurcation or atypical-value sets;
- relative polar varieties/discriminants;
- Thom/Hardt triviality;
- generic fibre geometry in structural identifiability;
- Reeb graph/space constructions;
- trilateration or range-only localization formulas.

The defensible contribution is the WREH-specific organization of these ingredients downstream of WR-I and WR-II, together with:
1. pulled-back rigidity monotonicity under protocol refinement;
2. a metric rigidity-gain diagnostic;
3. conditional-rank localization of refinement-created singularities;
4. the organizational contrast: rigidity is monotone under refinement while structural bifurcation walls need not be;
5. a closed-form range-localization benchmark realizing that contrast.

## Render / publication hygiene

- Source compiled: **yes**
- PDF pages: **15**
- PDF preflight: **pass**
- Fonts embedded: **yes**
- Cross-references resolved: **yes**
- Visual inspection: **yes**
- PDF SHA-256: `daee192a1618928315d1f8493f8a45ed4240152443d37c17038fef142ff0b921`
- LaTeX SHA-256: `0f1ef6877e5e37abdb04349d07873316f4c31da70a1384d7922d7ab97582aae1`

## Remaining gate

The document is ready for an independent external proof review. It is **not** yet a publication candidate and carries an explicit “for audit only; not for citation” notice.

## Final audit block

- unresolved blocking issues: none known at internal-audit stage
- equations/theorems changed: yes
- claim set changed: yes, narrowed
- bibliography verified: partial-to-substantial; primary metadata checked for the newly added sources
- metadata verified: yes
- source compiled: yes
- PDF visually inspected: yes
- release status: REVIEWABLE_DRAFT
