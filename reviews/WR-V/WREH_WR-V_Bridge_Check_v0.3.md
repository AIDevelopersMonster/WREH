# WR-V v0.3 — targeted bridge and source check

Date: 9 October 2026. Baseline: WR-V v0.2, commit `ef8d584a1e6c68d274503f0b81d72044e34e95ed`. WREH is an independent programme and community; published WR-I–IV remain frozen.

## Corpus actually inspected

| Source | Access and exact location | What was checked |
|---|---|---|
| WR-II v0.5, DOI 10.5281/zenodo.23224154 | Repository source `papers/WR-II/WREH_WR-II_Preprint_Draft_v0.5.tex`, §§3–6 | Full finite consistency, defect definition, profile trichotomy and finite-family collapse |
| WR-IV v0.6, DOI 10.5281/zenodo.23248138 | Common source `papers/WR-IV/preprint-v0.6/wriv-body.tex`, §2; published EN PDF, p.4 | Total historical projection; Proposition 2.3 and Remark 2.5, not the numbers suggested in the review |
| WR-V v0.2 | Common source, §§2,5–9; original numbering and bibliography | Declared input projection, independently declared successor carrier, probe fibre, finite Bayes support and Blackwell attribution |
| IBM Quantum Learning, Channel representations | [Official text](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/quantum-channels/representations-of-channels), sections on Kraus representations and reset channels; read 9 October 2026 | General matrix-sum update, normalization and potentially different input/output spaces; used only to check the proposed diagonal-operator sentence |

The eight manuscript bibliography entries are unchanged. The v0.1 preflight remains the record of original source access and its limitations. The IBM page is supplementary support for this response, not an exhaustive literature or quantum-instrument novelty audit.

## Finite obstruction versus full-finite defect

WR-II defines its full-finite defect as profiles whose **every finite restriction** is realizable but whose full profile has no realization. For a finite complete protocol family, the full bundle itself is finite, so the defect is empty. A finite probe bundle outside `BΔ(S)` is already a finite obstruction; calling it the same defect would erase the quantifier that distinguishes WR-II.

The shared logical rule is narrower: feasibility precedes discussion of singleton versus multiple completions. WR-IV Proposition 2.3 and Remark 2.5 express that rule for historical images. Neither paper infers physical nonexistence from model-relative emptiness.

In WR-V's two-probe example, `m=1/4` and `n₂=1/2` are separately valid probabilities. Together they yield the unique affine candidate `(1,-1/2,1/2)`, which is not nonnegative. Full rank does not guarantee existence; this data bundle has an empty fibre.

## Projection, support and completion types

WR-IV uses `π₋(C(D))`. WR-V declares `ρ₋:C(D)→X` and separately declares `S` and an instrument array. The support `Γ_e ⊂ X×R_e×S`, the probe completion class of laws `F(B,b) ⊂ Δ(S)` and a complete-world fibre `R⁻¹(y)` do not have the same carrier. An interpretation through a global trajectory space requires that space, maps and lift/compatibility conditions to be supplied. None follows merely from naming finite labels.

## Quantum-scope correction

The official Kraus representation has update `Φ(ρ)=Σ_j A_jρA_j†`, with `Σ_j A_j†A_j=I` for a channel. From that formula, if every `A_j` is diagonal in a fixed input/output basis, a basis state remains supported on itself. Thus diagonal operators cannot implement, for example, the classical transition `0→1` in that basis. Diagonal states or effects therefore do not imply diagonal transition operators. This is a direct algebraic check, not a result claimed by WR-V; an explicit general embedding is deferred.

## Likelihood support and decisions

With a positive prior on fixed finite hypotheses and a possible finite record, exact selection is equivalent to a positive accumulated likelihood for exactly one candidate. A realized likelihood vector `(1,0,1/2)` retains two candidates. Combining it with `(1,1/2,0)` retains one. A zero for some hypothesis is necessary to remove it, but one removal need not give singleton support. Improvement of a decision risk is a separate criterion.

The original manuscript cites Blackwell's *Equivalent comparisons of experiments*, DOI 10.1214/aoms/1177729032. The review's Chernoff attribution is not adopted; no Chernoff reference is added.

## Feedback provenance

Attachment: `Вставленный текст(20261009-010545).txt`. SHA-256: `05eebd701baf276c902a30146f0d18c1043b6497d24827d9c6515aaba4441617`. The attached text is not edited. Its heading describes it as independent; reviewer identity, procedure and external independence are not established. The supplied verdict and this editor's verifications are separate.

Status: REVIEWABLE_DRAFT. No journal selection, submission, deposit, WR-V DOI or new downstream branch is produced by this revision.
