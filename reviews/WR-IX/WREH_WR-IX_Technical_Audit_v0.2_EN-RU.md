# WR-IX v0.2 — technical prepublication audit / технический предпубликационный аудит

10 October 2026. Source: `papers/WR-IX/preprint-v0.2/wrix-body.tex`. This is an AI-assisted technical/adversarial audit by the drafting assistant, with separate finite symbolic, numerical and boundary calculations. It is **not independent external scientific peer review**. No reviewer identity or external endorsement is asserted.

Это техническая проверка с помощью ИИ, выполненная тем же помощником, который готовил текст. Отдельные вычисления не создают независимости рецензента. Независимое внешнее научное рецензирование не установлено.

## Claim ceiling / граница утверждений

Fixed model and observer access record; complete finite protocols with common feasibility; scalar exact/bounded-error certificates; finite adaptive conditional laws; ideal tagged first-return pulse in a known-axis cubic torus; declared geometric-optics redshift and detector; positive FLRW future kinematics. No universal physically complete protocol class, physical realization, actual observational fit, new cosmological law, ontology or broad novelty certificate.

Фиксированные модель и условия доступа наблюдателя; полные конечные протоколы с общей выполнимостью; скалярные точные сертификаты и ограниченная ошибка; конечные адаптивные условные законы; идеальный меченый импульс в торе с известной осью; заданные красное смещение и детектор; положительная будущая кинематика FLRW. Универсального физически полного класса протоколов, физической реализации, анализа реальных данных, нового закона или онтологического вывода нет.

## Findings and minimal repairs / замечания и минимальные исправления

Findings are premise traps tested during preparation and resolved in the delivered draft, not a claim that an earlier released IX version contained these defects.

| ID | Severity | Location | Problem / контрпример | Why it matters | Minimal repair in LaTeX | Claim-set effect |
|---|---|---|---|---|---|---|
| IX-01 | C1 | §2, (1) | Feasible/cost labels can depend on world; intersecting them can remove informative failures | A conservative shared class is not every physical action | Declare common feasibility, include failure as an outcome, costs of full policies, disclose model-dependent extension | narrows |
| IX-02 | C1 | Prop.3.1, (2)–(3) | At gap=2ε the two closed intervals touch; ε=0 still requires a positive witness | Non-strict threshold gives a false worst-case certificate | `g_\infty>2\varepsilon`; scalar closed error intervals; single complete protocol | clarifies |
| IX-03 | C1 | Prop.3.2 | Equal fair one-bit marginals with equal versus opposite second bits give different transcripts | Static marginal equality does not survive arbitrary adaptation | State equality of every conditional law at common history; finite depth; policy randomness independent of W | narrows |
| IX-04 | C2 | Example3.3 | Parameters θ≥T* all remain unresolved at deadline T*, although each distinct pair separates later | Pairwise finite witnesses do not imply a universal finite budget | Retain noncompact example; cite WR-I compact result rather than silently dropping compactness | clarifies |
| IX-05 | C1 | Thm4.1, (4) | L=S∞ is approached but not reached at any finite time; L=0 is a degenerate quotient | Endpoint and existence/uniqueness condition | `L>0` and `L<S_\infty`; positivity and C¹ a; monotone S proof | clarifies |
| IX-06 | C1 | §4 | A torus axis loop has length L; L/2 is injectivity radius; arbitrary direction may not close | Confusing topology scales yields the wrong return time | Known lattice axis; first positive lattice point L; restrict response family | narrows |
| IX-07 | C1 | Prop5.1, Cor5.2, (5)–(7) | At x=1/2, Hτ=log2, Emax=2Ed both finite equalities detect; x=1 never returns | Different endpoint conventions and division/log domains | Ed>0; inclusive finite thresholds; x∈(0,1); empty set Emax<Ed or zero cap | clarifies |
| IX-08 | C2 | §5 | A photon redshift law alone does not guarantee whole-packet capture, negligible diffraction or surviving observer | Kinematic resource bound is not apparatus feasibility | Explicit ideal collection/threshold assumptions; launch cap excludes overhead; list open physical bridges | narrows |
| IX-09 | C1 | Thm6.1, (8)–(10) | VIII compact bumps preserve eventual tail convergence type | Compact perturbations do not prove finite-versus-infinite future access | Construct noncompact smooth positive h− tail with dimensionless switch (t−T*)/δ; add Prop6.2 | clarifies |
| IX-10 | C1 | §6 after Thm6.1 | Matching background D alone does not copy the torus's current classical patch | Current topology compatibility has an additional spatial bound | Add `L>2cZ/H`; choose `L>\max\{c/H,2cZ/H\}` and preserve the explicit patch-copy premise | narrows |
| IX-11 | C1 | Prop7.1, Example7.2, (11)–(12) | Every S∞n>L while inf S∞n=L; TLn and En diverge | Strict infimum test and ∀∃→∃∀ swap are false | Pointwise strict comparison for every γ; supremum for exclusion; explicit n-family and no uniform budget claim | clarifies |
| IX-12 | C3 | §§1,3,8 | Repeated generic quotient/compact proof would duplicate WR-I; launch energy is not VII spectral diameter | Numbering is not new ownership | Supporting elementary lemma only; exact anti-duplication/source map; distinct carriers | clarifies |
| IX-13 | C4 | §8, bibliography [8]–[9] | VII DOI remains author-reported; VIII is now a verified deposit; IX has no DOI | Avoid false publication/review status | Qualified VII annotation; verified VIII version DOI; IX PUBLICATION_READY (technical preprint package); no made-up DOI | clarifies |
| IX-14 | C5 | Proof5.1, bibliography, RU paragraph8 | Long inline formula caused an overfull RU line; long DOI caused loose lines | Reproducible bilingual PDF hygiene | Unnumbered shared display for detector inequality; same-font breakable VIII DOI; ragged bibliography | none |

## Proof audit / проверка доказательств

- Prop.3.1: both supremum inequalities follow from union membership; positive/above-threshold witness does not need maximum attainment. Empty family convention and ε=0 handled. Closed scalar intervals give the strict >2ε criterion. No joint probabilistic claim.
- Prop.3.2: finite history recursion preserves probabilities; stopping is an absorbing common action. Impossible histories do not create mass. Conditional laws, policy and feasibility must remain common. Finite products are classical; no adaptive theorem priority.
- Thm4.1: lifted null ray x(T)=S(T); S′>0 gives injectivity; IVT gives existence below the limit. Positive future tail rules out equality at finite time. Nontrivial return requires lattice distance L.
- Prop.5.1/Cor.5.2: detector redshift condition is E0≥Ed a(TL); exact choice attains a closed energy cap. Exponential inverse uses log(1−x), valid only 0<x<1. Energy cap and finite time each cut detectable L. Units checked separately.
- Thm6.1: smooth switch denominator >0; exponential flatness at joins; h−>0; a−=exp∫h− is positive, normalized and smooth; reciprocal linear tail diverges logarithmically. Both histories share the entire supplied past and all jets at the switch. No compact-tail or prescribed-matter claim.
- Prop.6.2: positive continuous denominators have positive minima on compact prefix; common tail decides convergence, not the finite numerical value.
- Prop.7.1/Example7.2: componentwise theorem yields exact supremum exclusion including unattained supremum. Every finite return need not have common bounded resources; example preserves the difference between uncertain current H and exact shared-past construction.

Проверены все восемь блоков доказательств, области логарифмов и деления, строгие и включённые границы, существование и единственность первого возвращения, размерности, конечные и бесконечные кванторы. Общая адаптивная и физическая полнота сверх объявленного класса не предполагается.

## Novelty and realism / новизна и реалистичность

Classical prior tools: response equivalence, disjoint scalar error intervals, finite conditional products, flat torus covering, null propagation, FLRW redshift, event-horizon integral, smooth flat cutoff and reciprocal tail convergence. They are attributed or proved as elementary tools. The draft's programme-specific contribution is the explicit access record, coupled detection frontier, and a noncompact-tail counterexample connecting VIII compatibility to IX future accessibility. No priority over all literature is certified. Two targeted external cosmology primary sources support the specific formulas; a complete embedded-observer/decision/information literature survey remains necessary for a broader novelty claim.

Предшествующие инструменты не выдаются за открытия. Заявленный вклад ограничен условиями доступа и ресурсов и конкретными свидетельствами внутри программы. Математическая совместимость не удостоверяет физической реалистичности. Для универсальных выводов нужны обоснование полноты протоколов, теория материи и гравитации, глобальные поля/квантовые состояния, приборы и жизнь наблюдателя, направление, потери и статистика. Это самостоятельные открытые задачи.

## Verification / проверки

Machine reports accompany the source: three symbolic identities; 160 independently integrated/root-found return cases; 6,400 resource comparisons; 251 independent ODE tail points; 25 adversarial checks; 505 browser cases across EN/RU desktop/mobile. Infinite convergence is established by proof, not by finite numerical samples. Clean three-pass XeLaTeX and matching labels/bibliography are required; final rendering/browser inspections are recorded in release reports.

## Final audit block

- Unresolved mathematical blocking issues within the stated carrier: none found by this technical audit.
- Scientific choices outside the carrier: remain open; not repaired by stronger prose.
- Numbered equations/theorems changed after initial draft: none; assumptions/scope and one unnumbered proof display clarified before release.
- Claim set: explicitly limited at initial release; no inherited paper's frozen scientific claim set changed.
- Bibliography: targeted primary formula sources and stated programme maps verified; exhaustive novelty and VII deposited-file verification remain partial.
- Metadata: IX author/title/date/licences/absence of DOI checked; VIII version deposit verified; Zenodo VIII metadata corrections prepared, not submitted.
- Compilation/render inspection: see `build-verification.json`; browser check: see `demo-verification.json`.
- Release status: **PUBLICATION_READY (technical preprint package)**. This is a complete review package, not a claimed independently externally reviewed or published IX article.


## Revision audit / аудит редакции 0.2

Scope: reviewer-proposed prose was audited before adoption. All numbered statements, all eight proof blocks and all twelve equations remain byte-identical to the v0.1 common source. The release status concerns a scoped technical preprint, not a realistic cosmology or verified external review.

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| IX-R01 | C4 | Reviewer title / manuscript identity | Review uses another title | Prevent silent programme rename | Retain canonical Epistemic Horizons title; record descriptive reviewer title in response | clarifies |
| IX-R02 | C0 | Proposed §7 bridge | Resource infimum said to be unattained | Both resource minima are attained at n=2; suprema diverge | Reject sentence; distinguish unattained infimum of S∞ from unbounded Tn and En | clarifies |
| IX-R03 | C4 | Proposed WR-II reference | Example 10.16 is incorrect | Cited example is 10.19 in v0.5 source | Cite Example 10.19 and VI Corollary 5.3, with limited analogy | clarifies |
| IX-R04 | C2 | Reviewer universal detector / realizability interpretation | No uniform launch budget becomes no possible detector | Unspecified detectors and all conceivable futures lie outside the example | Retain declared probe/family; distinguish WR-II existence from IX uniform certificate | clarifies |
| IX-R05 | C5 | Figure 2 caption | S called conformal time | S has length units; S/c has time units | Correct caption, normalize axes Ht and HS/c; add cover-path clarification | clarifies |
| IX-R06 | C2 | Suggested final sentence | Universal world/observer intersection claim | Finite declared tools do not certify every physical observation | Add conditional conclusion and separate completeness obligation | clarifies |
| IX-R07 | C4 | Reviewer independence / score | Title and scores do not establish independent review | Identity and method unverified; partial proof selection | Disclose supplied text status and avoid external-review certification | clarifies |

Минимальные исправления ограничены пояснениями. Ошибочная фраза об инфимуме ресурсов не перенесена: при n=2 достигаются T₂=2 log 2/H₀ и E₂=2E_d, тогда как супремумы ресурсов бесконечны. Точная ссылка WR-II — пример 10.19. Внешнее научное рецензирование не удостоверяется заголовком входного текста или выставленными баллами.

Final release gate: no unresolved C0–C4 within the declared claim ceiling; all C5 checks must pass in the final build/render reports. Broader novelty and physical protocol completeness are expressly not claimed. Equations/statements/proofs unchanged; explanatory scope clarified; upstream versioned sources preserved. Bibliography verification is targeted primary-source verification, not an exhaustive novelty review. Metadata is prepared; IX DOI absent. Release status: **PUBLICATION_READY** (technical preprint package).
