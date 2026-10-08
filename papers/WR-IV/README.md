# WR-IV — Response-Conditioned Global Completion and the Status of the Past

**Programme and community:** World Realizability & Epistemic Horizons (WREH)  
**Upstream:** WR-I DOI 10.5281/zenodo.23210258; WR-II DOI 10.5281/zenodo.23224154; WR-III DOI 10.5281/zenodo.23228682  
**State:** ACTIVE / MATHEMATICAL SPINE v0.4  
**Release status:** REVIEWABLE_DRAFT

## Current files

- [v0.4 LaTeX](WREH_WR-IV_Mathematical_Spine_v0.4.tex)
- [v0.4 PDF](WREH_WR-IV_Mathematical_Spine_v0.4.pdf)
- [Theorem and dependency map](THEOREM_MAP.md)
- [Independent v0.2 audit](../../reviews/WR-IV/WREH_WR-IV_v0.2_Independent_Audit_RU.md)
- [v0.3 repair and source audit](../../reviews/WR-IV/WREH_WR-IV_Repair_Audit_v0.3.md)

- [Reviewer 1 response and v0.4 audit](../../reviews/WR-IV/WREH_WR-IV_Reviewer_1_Response_v0.4_RU.md)

The v0.1/v0.2/v0.3 sources and earlier audits are retained as dated snapshots.

## Declared objects

\[
\mathfrak C(D)=\{W\in\mathcal W:W\text{ is compatible with }D\},
\qquad
\mathfrak H_-(D)=\pi_-(\mathfrak C(D)).
\]

WR-IV separates global-world multiplicity, hidden-past multiplicity and observable-record
multiplicity. Hard-constraint refinement keeps the model, temporal cut and projection fixed.

## Explicit upstream bridges

The WR-II gate applies to a full response profile: an empty world fibre has an empty
historical image. A defect of the full profile does not make every finite-data fibre
empty, and it implies no disappearance of a physical past.

WR-III structural walls transfer when the response-indexed world and history families
are homeomorphic over the response base. A constant historical projection of the
WR-III sphere-height example erases the world-fibre wall. A response map is not thereby
identified with physical dynamics.

## Benchmarks

The doubling-map fibre is a classical Cantor family of full pasts with a deterministic future.
Gaussian smoothing and Brownian bridges are classical retrospective-inference benchmarks.

For an exact diffusion endpoint, the full pre-endpoint historical class is properly constrained.
A fixed earlier fragment may retain the same compatibility set while its conditional variance
decreases. Gaussian noisy endpoint data preserve path-measure support.
A regular conditional kernel is constructed explicitly for every endpoint value.
Section 7.2 gives a WREH dictionary separating carrier, fibre, historical projections
and the conditional path law. The several-time application remains open and explicitly
uses the classical linear Gaussian RTS recursion.

## Claim ceiling and publication gate

No past creation or rewriting, retrocausality, branching ontology, emergent time, or
cosmological conclusion is claimed. The current results are elementary consequences
and classical benchmarks organized within WREH; no new theorem priority is claimed.

The manuscript is ready for renewed review, not publication clearance. Broader prior-art
comparison and cross-manuscript duplication review remain open. No merge or WR-V transition
is authorized by this repaired draft.

## Reproduce the PDF

From this directory:

~~~sh
pdflatex -interaction=nonstopmode -halt-on-error WREH_WR-IV_Mathematical_Spine_v0.4.tex
pdflatex -interaction=nonstopmode -halt-on-error WREH_WR-IV_Mathematical_Spine_v0.4.tex
~~~

Required packages include amsmath, amssymb, amsthm, geometry, hyperref, microtype, booktabs and tabularx.

