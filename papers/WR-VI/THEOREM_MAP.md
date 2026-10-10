# WR-VI v0.2 — result and dependency map

Common source: `draft-v0.2/wrvi-body.tex`. EN/RU share labels and assigned numbers.

| Label | Object/result | Assumptions | Provenance and scope |
|---|---|---|---|
| `eq:completion`, `def:record` | Constraint-conditioned completion and constraint record | Declared carrier, data map, structural class, hard bounds and uncertainty | WREH interface; physical justification is a separate obligation |
| `prop:energy` | Mean balance differs from pathwise conservation | Finite stochastic matrix; full-support distribution for the squared criterion | Elementary nonnegative sum and stationary identity; no new conservation law |
| `eq:flows`, `eq:response` | Shared reversible edge variables and calibrated responses | Known positive π, supplied detailed balance and allowed graph | Standard reversible chains; couples formerly independent WR-V rows |
| `prop:dual` | Sufficient infeasibility certificate | Nonnegative coordinates, finite exact linear equalities/inequalities | Classical certificate; converse not claimed by this proposition |
| `thm:interval` | Complete three-state exact-response interval | Symmetric stochastic matrix, uniform π, f=(0,1/2,1), q=(1/4,1/2,3/4) | Direct affine elimination; worked benchmark, no priority claim |
| `thm:threshold` | Empty/singleton/nonunique classes under activity cap | All interval assumptions; externally supplied ν≥0; irreducibility not imposed | Exact interval intersection and certificate α≥1/6 |
| `cor:irreducible` | Infimum unchanged, attainment and selection changed | Additional irreducibility on the same finite carrier | Graph connectivity excludes the left endpoint; not a thermodynamic phase |
| `prop:tolerance` | Every positive response tolerance defeats the singleton | Symmetry and ν=1/6; sup-norm response tolerance | Explicit contained family; not a full noisy-fibre parameterization |
| `eq:quantifiers`, `prop:quantifiers` | Robust uniqueness does not identify an unknown-cap model | Nested scalar upper caps in an attained closed interval; exact responses | Elementary ∀/∃ distinction; no Bayesian or general robust-optimization novelty |

Dependency chain: declared carrier → structural rows and source check → exact probe fibre → activity certificate → strict-assumption audit → tolerance and cap-uncertainty audit. Physical application additionally needs independent evidence for the constraint record.

Inherited WR-V uniform/pointwise identification results are cited as tools, not reintroduced as WR-VI results. Projected/world uniqueness remains the WR-I/IV distinction. Finite infeasibility is not the WR-II full-finite defect. No computation supplies a premise of a general proof.

## v0.2 clarifications

No new numbered result or strengthened theorem. Corollary 5.3 is related to WR-II v0.5 Example 10.19 through nonclosed admissibility and unattained infima; no isomorphism is asserted. Proposition 6.2 is illustrated by N=[1/6,1/4], robust {P*}, possible t∈[−1/12,−1/24], with interval length 1/24. The introductory handoff identifies WR-V v0.3 §9.
