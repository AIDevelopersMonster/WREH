# WR-IV v0.3 repair and source audit

Date: 2026-10-08.
Base: PR #5 head 05bfaaa64fda81b95f326faaa099e966dd103642.
Active manuscript: papers/WR-IV/WREH_WR-IV_Mathematical_Spine_v0.3.tex.
Release status: **REVIEWABLE_DRAFT**.
This is an implementation-response audit, not a second independent referee opinion.

## Result

The v0.2 audit findings have been addressed in v0.3. Central Gaussian, Brownian bridge
and noisy-endpoint variance formulas are unchanged, except that diffusivity is now kappa
rather than the evidence symbol D. Claims are clarified or narrowed, not expanded into
new physical or priority claims. The historical v0.2 audit remains attached to its pinned
source; its historical BLOCKED_SOURCE_SUPPORT status is not a status of the repaired v0.3.

## Finding-to-repair map

| Finding | v0.3 repair | Effect / disposition |
|---|---|---|
| A01 C1 | Explicit Polish path space, weakly continuous regular kernel K_b, disintegration identity and residual/endpoint independence | CLOSED; conditional-law construction clarified |
| A02 C1 | Fixed earlier data value A=a; Gaussian residual proof also proves the lower PSD bound | CLOSED; conditions and proof clarified |
| A03 C2 | Covariance contraction separated from support and credible-region nesting | CLOSED; wording narrowed |
| A04 C1/C2 | Explicit hard endpoint fibre, full pre-T projection, early-prefix qualification, countable-path zero-mass proof | CLOSED; path-law/set connection clarified |
| A05 C1/C2 | Q_- must be constant on the whole nonempty historical fibre; two-history counterexample | CLOSED; criterion corrected |
| A06 C1/C5 | Whole inverse limit separated from p0 fibre; representatives and compact-to-Hausdorff coding proof | CLOSED; definitions/proof corrected |
| A07 C2 | Nested classes may be equal or empty; directional Gaussian strictness qualified by C | CLOSED; overbroad prose narrowed |
| A08 C2/C6 | Inference/temporal-order claim now a remark and scope convention | CLOSED; no impossibility claim |
| A09 C4 | Cited dyadic-solenoid research context; no unused projective-extension theorem invoked | CLOSED for statements actually used; broader comparison remains open |
| A10 C4 | Primary RTS article, exact Gaussian textbook locators, explicitly labelled Brownian lecture notes; no historical-priority claim | CLOSED for benchmark source coverage; no assertion of oldest-source exhaustiveness |
| A11 C3/C4 | The application explicitly fixes full pre-T histories and distinguishes unchanged fixed prefixes | CLOSED in the stated model; does not establish arbitrary projected-set shrinkage |
| A12 C5 | README/theorem map/register updated to v0.3; malformed current register equations repaired; R9 relabelled scope convention | CLOSED |
| A13 C5 | microtype and revised abstract; final two-pass build has no LaTeX warning or overfull/underfull box | CLOSED; final pages inspected |

## Mathematical review of the repairs

- The Gaussian residual has zero cross-covariance with Z and is independent of it.
  Its covariance is the nonnegative Schur complement; subtraction is directional-strict
  exactly when C^T v is nonzero. General Gaussian conditioning need not leave nonzero residual
  covariance; this distinction is explicit.
- The Brownian residual B_t-tB_T/T is independent of B_T as a continuous path random element,
  using Gaussian finite-dimensional independence and rational-time evaluations.
  Translating its law defines a measurable, weakly continuous endpoint kernel for every b.
- The bridge covariance is 2 kappa(min(s,t)-st/T), with positive interior marginal variance.
  Every countable set of paths has zero mass.
- Restriction of continuous full paths to [0,T) is injective. Pinning the endpoint thus gives
  a proper historical-image subset determined by the limit at T.
- Every continuous prefix on [0,tau], tau<T, has an extension to any endpoint b.
  The prefix compatibility class is unchanged; its conditional law is changed.
- A strictly positive Gaussian endpoint likelihood makes posterior and prior path measures
  equivalent. Augmenting worlds by noise constrains (w,eta), while path projection remains
  unrestricted. No support inclusion is claimed from a covariance inequality.

## Verified sources and scope

| Source | Evidence read / locator | Supported use | Limit |
|---|---|---|---|
| Rauch, Tung, Striebel, AIAA Journal 3(8), 1965, 1445–1450; DOI 10.2514/3.3166 | Original journal text in archival copy, §§2–3, §3.2, conclusion | Primary linear Gaussian retrospective smoothing | Not relied on for a rigorous continuous-time bridge construction |
| Särkkä, Svensson, Bayesian Filtering and Smoothing, 2nd ed., 2023; DOI 10.1017/9781108917407 | Author-hosted complete prepublication PDF; Appendix A.1, Lemma A.3, pp.355–356; §12.2, Theorem 12.2, pp.255–257; publisher metadata | Gaussian conditioning and RTS context | Textbook exposition, not claimed as earliest research; no third-party PDF redistributed |
| Pitman, Brownian Bridge, Stat205B lecture 22, Spring 2003; scribe T. Chen | Theorem 22.1 and subsequent remarks, p.22-2 | Residual bridge construction and endpoint independence | Lecture notes; not claimed as historical first source |
| Clark, Fokkink, Embedding solenoids, Fund. Math. 181(2), 2004, 111–124; DOI 10.4064/fm181-2-2 | Publisher article PDF, §1, pp.111–112; publisher metadata | Dyadic inverse-limit context and profinite/Cantor-fibre setting | Self-contained fibre coding supplied; no attribution of natural-extension invention |
| Karatzas, Shreve, Brownian Motion and Stochastic Calculus, 2nd ed.; DOI 10.1007/978-1-4612-0949-2 | Publisher metadata | General Brownian background | No exact theorem locator asserted; publisher shows ©1998 and a 1991 softcover publication date |
| WR-I/II/III, DOIs 10.5281/zenodo.23210258 / 23224154 / 23228682 | Zenodo record API: titles, authors, ORCID, deposited v0.3/v0.5/v0.6 file names; repository register | Upstream bibliographic identity | Full cross-manuscript proof/duplication audit remains separate |

Source URLs:

- https://archive.org/download/wikipedia-scholarly-sources-corpus/10.2514.zip/10.2514%252F3.3166.pdf
- https://users.aalto.fi/~ssarkka/pub/bfs_book_2023_online.pdf
- https://www.cambridge.org/core/books/bayesian-filtering-and-smoothing/F88740E8D25010CF3119A5CA379FA37A
- https://www.stat.berkeley.edu/~pitman/s205s03/b_bridge.pdf
- https://www.impan.pl/shop/en/publication/transaction/download/product/88376
- https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/181/2
- https://link.springer.com/book/10.1007/978-1-4612-0949-2
- https://zenodo.org/api/records/23210258
- https://zenodo.org/api/records/23224154
- https://zenodo.org/api/records/23228682

The McCord 1965 publisher PDF returned 403. It is not relied upon as an inspected source,
and has not been inserted into the manuscript as if verified. The historical source task
is narrowed to what this version actually states; no projective-extension result is used.

## Novelty and remaining programme obligations

Current contribution: framework exposition and use of elementary/classical results in a
declared history-projection setting. No new theorem priority or experimental validation
is claimed. The paper remains in WREH; BC is not its community.

Still open:
- broader comparison with observability, identifiability, natural extensions and partial-observation reconstruction;
- full comparison against frozen upstream manuscripts;
- any future claim to a genuinely new technical result;
- richer several-time, finite-resolution and metric/topological examples and the planned HTML demo.

These obligations do not invalidate the repaired benchmark, but prevent treating it as
an already certified original technical publication. No merge, publication or next-paper
transition is performed here.

## Reproducibility and final render check

Commands:
~~~sh
pdflatex -interaction=nonstopmode -halt-on-error WREH_WR-IV_Mathematical_Spine_v0.3.tex
pdflatex -interaction=nonstopmode -halt-on-error WREH_WR-IV_Mathematical_Spine_v0.3.tex
pdftoppm -r 100 -png WREH_WR-IV_Mathematical_Spine_v0.3.pdf page
~~~

Final PDF: 8 pages. Final LaTeX log: no warnings, undefined citations/references, overfull
or underfull boxes. All 8 pages visually inspected. One intermediate page PNG was truncated;
that page was rendered separately to JPEG and inspected. The PDF itself is valid.
Stable LaTeX labels are mapped to printed numbers in THEOREM_MAP.md.

## Final audit block

- Unresolved C0/C1/C2 defects in the repaired stated benchmark: none identified by this repair check.
- Broader novelty/cross-manuscript review: open; originality not certified.
- Equations changed: notation D→kappa; central variance formulas preserved.
- Claims: clarified/narrowed; no new physical or theorem-priority assertion.
- Bibliography verified: benchmark source mapping yes; historical-priority exhaustiveness no.
- Metadata verified: authors/ORCID, upstream deposited version filenames, source date and repository licence yes.
- Source compiled: yes, final two-pass build.
- PDF visually inspected: yes, all 8 pages.
- Release status: REVIEWABLE_DRAFT.
