# WR-V v0.3 — result and dependency map

Common source: `wrv-body.tex`; English/Russian result numbers match.

| Source label | Object/result | Essential assumptions | Provenance / dependency |
|---|---|---|---|
| `def:instrument` | Finite outcome-plus-successor instrument | Finite nonempty carriers; nonnegative normalized array | Classical instrument distinction; Davies–Lewis supplies historical provenance, not a proof of this finite definition |
| `def:images` | Input and successor compatibility images | Positive-probability outcome; full-support prior for law/support equivalence | Direct finite support projections; WR-IV type discipline |
| `ex:swap` | Changing a projected state does not violate global refinement | Fixed complete trajectory carrier; two different cut projections | Elementary counterexample; inherited fixed-carrier refinement |
| `thm:marginal` | Fixed likelihood instrument class is a product of simplices | No cross-row, conservation or dynamical constraints; exclude conditional rows with zero likelihood | Direct factorization; no novelty claim |
| `ex:same-outcome` | Same immediate outcomes, different successor models | Common input/outcome/successor carriers | Explicit finite witness to outcome-only non-identification |
| `def:fibre` | Calibrated probe completion fibre | Probe response depends only on declared successor; repeat preparations; ideal probabilities | New transition carrier; inherited response-fibre language |
| `thm:rank` | Uniform injectivity iff full column rank; every interior law ambiguous otherwise | Normalization row in B; whole simplex admissible | Elementary linear algebra |
| `thm:cone` | Pointwise uniqueness iff kernel has no nonzero one-sided feasible direction | Finite coordinates; feasibility; zero-coordinate signs; normalization in kernel | Standard nonnegative feasibility criterion; adjacent Donoho–Tanner theory |
| `prop:functional` | Uniformly identifiable linear functionals are exactly row(B) | Quantification over all nonempty simplex fibres | Linear algebra specialization of WR-I identifiability |
| `ex:midpoint` | Distinct responses of pure states do not identify mixtures | Mixtures admitted; one detector (0,1/2,1) | Direct example; independently rationally checked |
| `eq:second` | Two probes identify the finite successor law | Second detector (0,0,1); exact calibrated probabilities; feasible data | Explicit invertible 3×3 system |
| `eq:resolution`, `eq:error` | Boundary uniqueness is not finite-resolution uniqueness; affine error bound | Given response error bounds; fixed calibrated matrices | Direct perturbation and triangle inequality; no statistical coverage assertion |
| `ex:triangle` | Pairwise overlap compatibility without global bit assignment/law | Three identified binary variables; perfect pairwise anti-correlation | Established contextuality/global-section pattern; WR-II owns generic extension question |
| `prop:positive` | Finite adaptive records with positive likelihood do not select a persistent latent hypothesis | Full-support prior; every realized conditional likelihood positive for each input; policy uses only recorded history | Finite Bayes products; extension of WR-IV positivity discipline |

No computation is used as a premise of a general theorem. The reproduction script checks the supplied finite witnesses and inverse formulas. The draft's claim ceiling is finite classical experiment models; physical branching, collapse and quantum realization are excluded.

Revision v0.3 preserves every symbolic label and proof. The normalization explanation makes explicit that `ker(B) ∩ T_k`, rather than `T_k` alone, supplies feasible simplex directions. Rank is a uniform criterion; boundary selection depends on data and support.

Revision v0.3 preserves those results. Finite probe infeasibility is the finite-obstruction case, not the full-finite WR-II defect. WR-IV references are Proposition 2.3 and Remark 2.5 in v0.6. Instrument support and completion fibres have different carriers; global trajectory lifts and quantum embeddings remain open obligations. The provenance table does not attribute the exact cone theorem to adjacent prior art.
