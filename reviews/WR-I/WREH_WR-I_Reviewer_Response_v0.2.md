# WR-I — Response to Review, v0.2

**Manuscript:** *Response-Defined World Spaces: Finite-Resolution Equivalence and Identifiability of Global Realizations*  
**Programme:** World Realizability & Epistemic Horizons (WREH)  
**Author:** A. A. Malachevsky  
**Revision date:** 7 October 2026

## Review disposition

### 1. Elementary quotient/factorization proofs

**Decision:** Accepted.

The proofs of the response-quotient representation and identifiable-quantity factorization were compressed to short self-contained arguments. They are retained because the manuscript defines a new programme-level formal interface, but they are no longer presented with disproportionate proof detail and no novelty claim is attached to them.

**Effect on claims:** None. The revision lowers rhetorical emphasis on elementary set-theoretic facts.

---

### 2. Compactness assumption in finite-resolution separation

**Decision:** Accepted with a stronger mathematical repair.

The global assumption that `X = W/G` is compact was removed. The result is now localized to a compact admissible domain `K subset X`, and the proof explicitly uses compactness of

`K_delta^(2) = {(x,y) in K x K : d_X(x,y) >= delta}`.

The manuscript also states the sharper point that compactness of the separated-pair set is sufficient; local compactness of `X` alone is not enough to justify the finite-subcover step globally.

**Effect on claims:** Strengthens applicability while narrowing the theorem to exactly the hypotheses used in the proof.

---

### 3. Structural-identifiability literature

**Decision:** Accepted.

The prior-art discussion now includes mature structural-identifiability sources:

- Saccomani, Audoly & D'Angio (2003), *Automatica*, DOI `10.1016/S0005-1098(02)00302-3`;
- Bellu et al. (2007), *Computer Methods and Programs in Biomedicine*, DOI `10.1016/j.cmpb.2007.07.002`;
- Villaverde, Barreiro & Papachristodoulou (2016), *PLOS Computational Biology*, DOI `10.1371/journal.pcbi.1005153`;
- Meshkat & Sullivant (2014), *Journal of Symbolic Computation*, DOI `10.1016/j.jsc.2013.11.002`.

The manuscript deliberately does **not** claim that these works already formulate the WREH global-realization framework. They are cited for mature input-output identifiability, parameter combinations, and identifiable reparametrization.

**Bibliographic correction:** the 2007 DAISY paper is in *Computer Methods and Programs in Biomedicine*, not *Bioinformatics*.

**Effect on claims:** Narrows and strengthens the novelty boundary.

---

### 4. Continuous-history example

**Decision:** Accepted.

The continuous-history example now contains an explicit counterexample after enlarging the admissible class. Two histories agree on every point of a dense observation set but differ at one unobserved point once discontinuous bounded histories are admitted. This makes the dependence of identifiability on the pair `(admissible realization class, protocol family)` explicit.

**Effect on claims:** None; improves explanatory force.

---

### 5. BC-XI as methodological precursor

**Decision:** Added by author decision.

A dedicated bridge subsection now identifies BC-XI as the methodological precursor of the response-first viewpoint:

`hidden structures -> finite-resolution response classes -> admissible global-realization classes`.

The manuscript explicitly states that this is a genealogical and methodological bridge, not a transfer of Boundary Compensation physical claims into WREH.

Reference added:

A. A. Malachevsky, *Boundary Compensation XI: The Inverse Isotypic Gap Problem and Finite-Resolution Response Equivalence Classes*, Zenodo (2026), DOI `10.5281/zenodo.20748061`.

**Effect on claims:** No strengthening of physical claims. Clarifies programme ancestry and anti-duplication boundary.

---

## Current release assessment

**Status:** `REVIEWED_CLEAN`

The v0.2 draft is mathematically reviewable and the reviewer objections have been addressed at manuscript level. Before a public preprint release, the remaining publication-hygiene tasks are:

1. final independent literature audit for novelty wording;
2. verify all bibliography metadata against primary records;
3. decide licence and repository metadata;
4. final PDF/render audit after any further prose editing;
5. assign the release version only after repository state is frozen.

WR-II should use the stabilized WR-I definitions, but no WR-II theorem should be cited as established by WR-I.
