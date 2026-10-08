# WR-IV — Response-Conditioned Global Completion and the Status of the Past

**Programme and community:** World Realizability & Epistemic Horizons (WREH)  
**Upstream:** WR-I DOI 10.5281/zenodo.23210258; WR-II DOI 10.5281/zenodo.23224154; WR-III DOI 10.5281/zenodo.23228682  
**State:** ACTIVE / MATHEMATICAL SPINE v0.3  
**Release status:** REVIEWABLE_DRAFT

## Current files

- [v0.3 LaTeX](WREH_WR-IV_Mathematical_Spine_v0.3.tex)
- [v0.3 PDF](WREH_WR-IV_Mathematical_Spine_v0.3.pdf)
- [Theorem and dependency map](THEOREM_MAP.md)
- [Independent v0.2 audit](../../reviews/WR-IV/WREH_WR-IV_v0.2_Independent_Audit_RU.md)
- [v0.3 repair and source audit](../../reviews/WR-IV/WREH_WR-IV_Repair_Audit_v0.3.md)

The v0.1/v0.2 sources and earlier audits are retained as dated snapshots.

## Declared objects

\[
\mathfrak C(D)=\{W\in\mathcal W:W\text{ is compatible with }D\},
\qquad
\mathfrak H_-(D)=\pi_-(\mathfrak C(D)).
\]

WR-IV separates global-world multiplicity, hidden-past multiplicity and observable-record
multiplicity. Hard-constraint refinement keeps the model, temporal cut and projection fixed.

## Benchmarks

The doubling-map fibre is a classical Cantor family of full pasts with a deterministic future.
Gaussian smoothing and Brownian bridges are classical retrospective-inference benchmarks.

For an exact diffusion endpoint, the full pre-endpoint historical class is properly constrained.
A fixed earlier fragment may retain the same compatibility set while its conditional variance
decreases. Gaussian noisy endpoint data preserve path-measure support.
A regular conditional kernel is constructed explicitly for every endpoint value.

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
pdflatex -interaction=nonstopmode -halt-on-error WREH_WR-IV_Mathematical_Spine_v0.3.tex
pdflatex -interaction=nonstopmode -halt-on-error WREH_WR-IV_Mathematical_Spine_v0.3.tex
~~~

Required packages include amsmath, amssymb, amsthm, geometry, hyperref and microtype.
