# WR-IV theorem and dependency map — v0.4

Active source: [WREH_WR-IV_Mathematical_Spine_v0.4.tex](WREH_WR-IV_Mathematical_Spine_v0.4.tex).
Release status: REVIEWABLE_DRAFT. Earlier v0.1/v0.2/v0.3 sources are historical snapshots.
R identifiers are programme aliases; printed LaTeX numbering is shown below.

## Inherited objects

WR-I supplies response equivalence; WR-II supplies global-completion existence discipline;
WR-III supplies fibre/refinement language and its local-triviality definition of a structural wall. WR-IV declares the historical projection and states the conditional bridge to historical families.

\[
\mathfrak C(D)=\{W\in\mathcal W:W\text{ is compatible with }D\},\quad
\mathfrak H_-(D)=\pi_-(\mathfrak C(D)),\quad
\mathfrak O_-(D)=Q_-(\mathfrak H_-(D)).
\]

Refinement fixes the model, temporal cut, and projection. Empty refined fibres are permitted;
persistence of rigidity requires a nonempty refined fibre.

| Alias | Printed location / label | Statement and required conditions | Provenance |
|---|---|---|---|
| R1 | Proposition 2.3 / prop:world-past | Singleton world fibre has singleton historical image | Elementary image property |
| R2 | Proposition 2.4 / prop:converse | Same past can accompany two distinct worlds; explicit two-world example | Elementary counterexample |
| R3 | Theorem 3.1 / thm:completion-refinement | \(D\preceq D'\Rightarrow\mathfrak C(D')\subseteq\mathfrak C(D)\) and historical image inclusion; fixed model/projection, accumulated hard constraints | Definition consequence |
| R4 | Corollary 3.2 / cor:rigidity-persistence | Past rigidity persists under nonempty refinement | Definition consequence |
| R5 | Proposition 4.1 / prop:observable-rigidity | Observable rigidity iff the historical fibre is nonempty and \(Q_-\) is constant on it; explicit ambiguity counterexample | Elementary image property |
| R6 | Proposition 5.1 / prop:forward-backward | Unique forward orbit; noninjectivity alone does not ensure multiple full backward histories | Elementary dynamics; counterexample supplied |
| R7 | Theorem 6.1 / thm:cantor-pasts | Doubling-map fibre over fixed present state is homeomorphic to \(\{0,1\}^{\mathbb N}\); circle/product topologies and chosen branch labels | Classical dyadic-solenoid benchmark; self-contained proof |
| R8 | Corollary 6.2 / cor:finite-backward | Finitely many fixed bits leave countably infinitely many free bits | Product-space consequence |
| R9 | Remark 8.1 | No bridge identifying inference order with temporal order is specified | Scope convention, not impossibility theorem |
| R10 | Theorem 7.1 / thm:gaussian-contraction | Fixed earlier data law; jointly Gaussian \(X,Z\), \(S\succ0\); \(P_s=P-CS^{-1}C^\top\succeq0\) and \(P_s\preceq P\) | Classical Gaussian conditioning; residual proof |
| R11 | Theorem 7.1 and Definition 7.2 | \(\Delta P=CS^{-1}C^\top\); directional strictness iff \(C^\top v\ne0\) | Classical consequence |
| R12 | Theorem 7.4 / thm:brownian-bridge | Deterministic \(x_0\), fixed \(T>0\), \(\kappa>0\), \(0<t<T\); continuous regular kernel \(K_b\); variance \(2\kappa t(T-t)/T\) | Classical Brownian bridge |
| R13 | Corollary 7.5 / cor:path-nonuniqueness; Remark 7.6 | Brownian bridge is non-Dirac; countable path sets have zero mass; full pre-\(T\) historical image is properly constrained by endpoint limit | Classical bridge plus explicit compatibility interpretation |
| R14 | Proposition 7.7 / prop:noisy-contraction; Remark 7.8 | Independent Gaussian noise \(R>0\); variance \(2\kappa t(1-2\kappa t/(2\kappa T+R))\); positive likelihood preserves path support | Classical conditioning and direct Bayes argument |
| R15 | Proposition 2.5 / prop:realizability-gate; Remark 2.6 / rem:empty-past | For a total historical projection and full-profile data, historical fibre empty iff world fibre empty iff response unrealizable; finite fibres may remain nonempty | Elementary image property plus WR-II §§3–7; no new existence criterion |
| R16 | Proposition 4.2 / prop:wall-transfer; Remark 4.3 / rem:wall-erasure | A homeomorphism of response-indexed families over U transfers local triviality both ways; constant projection can erase a world wall | Elementary conjugation of trivializations; WR-III §§8,10 |

## Explicit application result and its limit

For \(\mathcal W_T=C_{x_0}([0,T],\mathbb R)\), exact endpoint data give
\[
\mathfrak C(x_0,b)=\{w\in\mathcal W_T:w(T)=b\}\subsetneq\mathcal W_T.
\]
For the full past projection \(\pi_-(w)=w|_{[0,T)}\), continuity makes the restriction
injective; the projected class is properly reduced by the limit \(b\) at \(T\).
Residual bridge paths remain nonunique.

For any fixed earlier fragment \([0,\tau]\), \(\tau<T\), compatible fragments are
unchanged: each continuous prefix can be continued to \(b\). The corresponding conditional
state variance still decreases. Thus the application obligation is satisfied for the
declared full pre-endpoint history; it does not establish strict set contraction for every
earlier projection or for noisy path supports.

## Claim and novelty ceiling

R1–R16 are elementary consequences, standard benchmarks, or scope conventions.
No theorem-priority claim is made. WREH organizes world/past/record multiplicity;
originality of the wider classification still needs comparison with observability,
identifiability, natural extensions, smoothing, and partial-observation reconstruction.
No past rewriting, retrocausality, branching ontology, or cosmological inference follows.

## Open next work

- Broader prior-art and cross-manuscript duplication review.
- Several-time linear Gaussian state-space example using the standard RTS backward recursion; explicitly separate historical sets and posterior laws.
- Finite-resolution observable-past equivalence.
- Nonduplicative metric/topological results and HTML demonstration.

Adding observations or a new example does not itself establish research novelty.


## Limits of the new upstream bridges

- R15 concerns the complete profile y. WR-II's finite-support example has empty full
  fibre over (1,1,...) and nonempty fibres for every finite restriction.
- R16 requires a homeomorphism of the total families over the response base. Separate
  fibre homeomorphisms do not by themselves establish this family-level condition.
- A structural wall is a failure of local bundle triviality; it need not, by definition,
  change the number of connected components or describe a physical transition.
- The Brownian dictionary distinguishes the set C(D_b) from the law K_b and the full
  pre-T history from a fixed earlier fragment. Regular conditioning on a null endpoint
  event is distinct from a mathematically empty compatibility fibre.
