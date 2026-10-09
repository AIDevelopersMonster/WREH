# WR-V v0.2 revision notes

Date: 9 October 2026. Base: v0.1 at commit `61b1a9613b745deebcb46e493e8372dbb3ae19a5`. Status: REVIEWABLE_DRAFT.

- Equation (6) is displayed in two aligned lines, with the block matrix and its normalization row explicitly explained. The v0.1 source already had a valid block matrix.
- After Theorem 5.3, the normalization row implies `1ᵀv=0` for every `v∈ker B`; the kernel/cone intersection, not the nonnegativity cone alone, supplies feasible simplex directions.
- `N_+` is retained. It already denoted the number of positive-likelihood rows in v0.1.
- Section 6 declares `k=(k₀,k₁,k₂)` and `k_j=k(s_j)`; (11) contains scalar absolute-error bounds.
- Section 8 defines hard support-based selection and soft posterior concentration separately.
- The abstract/introduction explicitly keep the four labels nonexclusive and acting on different mathematical objects. Full rank characterizes uniform identification, while particular boundary data can identify at deficient rank.
- Section 4 clarifies that calibrated probes are one source of additional information; independently declared admissibility restrictions can also constrain transitions.

All theorem/proposition proofs, symbolic result labels, formula numbering and eight bibliography entries are preserved. Equation (6) changes layout only. The displayed editorial clarifications do not claim a new theorem or physical measurement principle.

The supplied proof-review is recorded in the response and revision audit. Independent external peer-review provenance and exhaustive novelty certification remain open. The version is not automatically a journal-ready submission or an approved monograph.

The review ZIP contains a versioned theorem map and README rather than active project documentation. Its checksum manifest is checked from the archived repository-shaped root. Historical v0.1 files and the originally saved archive remain unchanged.
