# WR-IV theorem and dependency map — complete preprint v0.6

Active source: [shared bilingual body](preprint-v0.6/wriv-body.tex), with English and Russian entry points in the same directory. Printed numbering is identical between languages.

Release status: PUBLICATION_READY for a complete expository, unpeer-reviewed preprint; Zenodo deposit is prepared, not published. Earlier versions are snapshots. R1–R16 remain programme aliases rather than claims of new theorem priority.

## Inherited interface

WR-I owns response equivalence; WR-II owns finite/global existence discipline; WR-III owns generic response-fibre geometry and local-triviality walls. WR-IV declares a history projection, with fixed carrier/cut/projection under refinement, and distinguishes image sets from probability laws.

| Alias | Printed v0.6 location / label | Conditions and statement | Provenance |
|---|---|---|---|
| R1 | Proposition 2.2 / prop:world-past | Singleton world fibre implies singleton historical image | Elementary image property |
| R2 | Proposition 2.2 / prop:world-past, converse example | Two worlds may carry the same past | Elementary counterexample; merged exposition |
| R3 | Theorem 3.1 / thm:completion-refinement | Accumulated hard constraints on fixed model/cut/projection give nested C(D), H_-(D) | Definition consequence |
| R4 | Corollary 3.2 / cor:rigidity-persistence | Past rigidity persists only for nonempty refined fibre | Definition consequence |
| R5 | Proposition 3.4 / prop:observable-rigidity | Observable rigidity iff nonempty historical image has constant record map | Elementary projection |
| R6 | Proposition 5.1 / prop:forward-backward | Unique forward orbit; noninjectivity need not supply a full backward history over every present | Standard dynamics; explicit counterexample |
| R7 | Theorem 6.1 / thm:cantor-pasts | Fixed-present doubling-map fibre is homeomorphic to the binary product Cantor space | Classical natural extension; self-contained coding |
| R8 | Corollary 6.2 / cor:finite-backward | Finitely fixed bits leave infinitely many free bits | Product-space consequence |
| R9 | §11.2 | Evidence order does not specify a physical-time bridge | Scope convention, not impossibility theorem |
| R10 | Theorem 7.2 / thm:gaussian-contraction | Joint Gaussian law at fixed earlier data; S positive definite; P_s=P−CS⁻¹Cᵀ is PSD and no larger than P | Classical Gaussian residual argument |
| R11 | Theorem 7.2, equation (8) | Directional strictness iff Cᵀv≠0; residual can be singular | Classical consequence |
| R12 | Theorem 8.2 / thm:brownian-bridge | Fixed x₀, κ,T>0, 0<t<T; all-endpoint kernel; variance 2κt(T−t)/T | Classical bridge |
| R13 | Corollary 8.3 / cor:path-nonuniqueness; Proposition 8.4 / prop:prefix-sets | Non-Dirac law; countable path sets null; full pre-T image constrained while each fixed earlier prefix set is unchanged | Classical law plus explicit image interpretation |
| R14 | Propositions 9.1–9.2 / prop:noisy-contraction, prop:noisy-equivalence | Independent Gaussian noise R>0; explicit mean/variance; equivalent posterior path measure. Admissible bounded noise instead restricts endpoint compatibility | Classical conditioning and Bayes |
| R15 | Proposition 2.3 / prop:realizability-gate; Example 2.4; Remark 2.5 | Total historical projection and full-profile data: empty history iff empty world fibre iff response unrealizable | WR-II gate; elementary image property |
| R16 | Proposition 4.1 / prop:wall-transfer; Example 4.2 / ex:wall-erasure | Homeomorphism of total families over base transfers local triviality; constant historical projection can erase wall | Conjugation of trivializations; WR-III example |

## Additional complete exposition in v0.6

These supporting results do not establish new programme ownership or priority:

- Definition 7.1 / def:rcd: regular conditional distributions and almost-everywhere version discipline.
- Proposition 7.3 / prop:total-variance: average conditional-variance contraction; Example 7.4 disproves arbitrary pointwise contraction.
- Proposition 8.1 / prop:bridge-kernel, equations (11)–(12): explicit weakly continuous regular path kernel and covariance, valid for every endpoint.
- Proposition 8.5 / prop:prefix-equivalence, equation (15): positive transition-density derivative makes fixed-prefix laws equivalent despite reduced covariance.
- §9.2, equation (19): finite-resolution endpoint data give a mixture of bridges; distinct from bounded-noise likelihoods.
- §10, equations (20)–(22): classical scalar filtering/RTS model, proof, exact two-observation example and independent batch conditioning.

## Scientific and release limits

Compatibility sets, projected images, null events, measure supports, means and covariance are different objects. Shrinking covariance does not imply strict set shrinkage. A full-profile WR-II defect is not a defect of every finite restriction. The historical image family is not assumed to be a pullback bundle. Structural walls are local-triviality failures, not universal component-count or physical-transition claims.

The source audit maps 11 references and the relevant deposited upstream interfaces in [SOURCE_MAP.md](preprint-v0.6/SOURCE_MAP.md). No theorem-priority or exhaustive originality claim is made. The WR-II gap Gamma alone cannot measure information gain: it vanishes for finite protocol families with positive smoothing gain.

## Validation and next research

The bilingual PDFs share 62 numbered labels and 22 equations. Eighty RTS cases match independent batch conditioning. The offline HTML illustrates four declared benchmarks and passes desktop/mobile checks.

Further research requires a genuinely nonduplicative theorem or calibrated information model and a broader literature review appropriate to that claim. This preprint does not merge PR #5 or open WR-V.
