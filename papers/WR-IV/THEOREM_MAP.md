# WR-IV theorem and dependency map — v0.1

## Upstream

WR-IV inherits WR-I response equivalence, WR-II nonempty global-completion discipline, and WR-III fibre/refinement language. It adds a declared historical projection layer.

## Core objects

\[\mathfrak C(D)=\{W\in\mathcal W: W\text{ is globally compatible with }D\},\]

\[\mathfrak H_-(D)=\pi_-(\mathfrak C(D)).\]

Optional observable-past projection:

\[\mathfrak O_-(D)=Q_-(\mathfrak H_-(D)).\]

## R1 — World rigidity implies past rigidity

If \(\mathfrak C(D)\) is a singleton, then \(\mathfrak H_-(D)\) is a singleton.

Status: PROVED.

## R2 — Converse fails

Past rigidity does not imply world rigidity.

Status: PROVED BY COUNTEREXAMPLE.

## R3 — Completion refinement

If \(D\preceq D'\), then
\[\mathfrak C(D')\subseteq\mathfrak C(D)\]
and
\[\mathfrak H_-(D')\subseteq\mathfrak H_-(D).\]

Status: PROVED.

## R4 — Past rigidity persists under consistent refinement

A nonempty refined subset of a singleton past-completion set is the same singleton.

Status: PROVED.

## R5 — Observable-past rigidity can coexist with hidden-past ambiguity

\[|\mathfrak O_-(D)|=1\]
does not imply
\[|\mathfrak H_-(D)|=1.\]

Status: PROVED BY COUNTEREXAMPLE.

## R6 — Forward uniqueness does not imply backward uniqueness

A deterministic map \(T:X\to X\) gives a unique forward orbit, while noninjectivity may leave several full backward histories.

Status: PROVED.

## R7 — Doubling-map Cantor past

For \(T(x)=2x\pmod1\) on the circle, the natural-extension fibre over any present state is homeomorphic to \(\{0,1\}^{\mathbb N}\).

Status: PROVED.

## R8 — Finite backward records leave infinite past ambiguity

Fixing finitely many backward branch choices leaves a Cantor family of older compatible histories.

Status: PROVED.

## R9 — Construction order is not internal time

The order \(D\mapsto\mathfrak C(D)\) is an inference/construction order and does not define temporal order inside a completed world without an explicit bridge.

Status: PROVED AS TYPE-SEPARATION STATEMENT.

## Claim firewall

No physical past creation, past rewriting, retrocausality, branching ontology, or emergent-time claim follows from R1-R9.

## Main open obligation

Find a nontrivial application where later/current observations reduce the set of compatible historical trajectories while leaving a mathematically controlled residual past ambiguity.