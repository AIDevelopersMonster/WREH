# WREH — First technical cycle / Первый технический цикл

**Closed / Published / Integrated — 10 October 2026.**

World Realizability & Epistemic Horizons (WREH) is both the research programme and community. Its first technical cycle consists of nine deposited preprints. Observations constrain classes of admissible global realizations; a compatible model need not be the unique world or a physically realized world. WREH remains distinct from Boundary Compensation.

Первый технический цикл завершён: девять статей опубликованы, все ветки интегрированы в `main`, текущие статусы и DOI согласованы. Внешнее независимое научное рецензирование не установлено. Закрытие репозитория не означает решения всех научных вопросов программы.

## Publications / Публикации

| Article | Frozen version | Title / предмет | Zenodo |
|---|---|---|---|
| [WR-I](../../papers/WR-I/README.md) | v0.3 | Response-Defined World Spaces: Response Equivalence, Finite-Resolution Separation, and Identifiability of Global Realizations. Отклики, классы эквивалентности и идентифицируемость миров. | [10.5281/zenodo.23210258](https://doi.org/10.5281/zenodo.23210258) |
| [WR-II](../../papers/WR-II/README.md) | v0.5 | Finite Consistency and Global World Realizability. Различие конечной согласованности и глобальной реализуемости. | [10.5281/zenodo.23224154](https://doi.org/10.5281/zenodo.23224154) |
| [WR-III](../../papers/WR-III/README.md) | v0.6 | Geometry of Admissible World Fibres: Refinement, Rigidity and Realizability Walls. Геометрия непустых слоёв совместимых миров и уточнение протоколов. | [10.5281/zenodo.23228682](https://doi.org/10.5281/zenodo.23228682) |
| [WR-IV](../../papers/WR-IV/README.md) | v0.6 | Response-Conditioned Global Completion and the Status of the Past. Совместимые истории прошлого и ретроспективное условное уточнение. | [10.5281/zenodo.23248138](https://doi.org/10.5281/zenodo.23248138) |
| [WR-V](../../papers/WR-V/README.md) | v0.3 | Experiment and Realization Selection: Branch, Contextualize, Select, or Remain a Class. Исход эксперимента, переход состояния и выбор модели. | [10.5281/zenodo.23251956](https://doi.org/10.5281/zenodo.23251956) |
| [WR-VI](../../papers/WR-VI/README.md) | v0.2 | The Aquarium Bounds: Physical Constraints as Boundaries of World Space. Независимо заданные ограничения, недостижимость и неопределённые пределы. | [10.5281/zenodo.23254619](https://doi.org/10.5281/zenodo.23254619) |
| [WR-VII](../../papers/WR-VII/README.md) | v0.2 | Energy-Time Frontiers of World Realizability. Энергия, длительность, квантовый отклик и неоднозначность генераторов. | [10.5281/zenodo.23264253](https://doi.org/10.5281/zenodo.23264253) |
| [WR-VIII](../../papers/WR-VIII/README.md) | v0.2 | The Cosmological Fibre: Universes Compatible with Our Universe Today. FLRW-инверсия, калибровка, масштаб, топология и продолжения. | [10.5281/zenodo.23266980](https://doi.org/10.5281/zenodo.23266980) |
| [WR-IX](../../papers/WR-IX/README.md) | v0.2 | Epistemic Horizons: What Can an Observer Inside a World Ever Distinguish?. Доступ наблюдателя, причинные и ресурсные горизонты, порядок кванторов. | [10.5281/zenodo.23272637](https://doi.org/10.5281/zenodo.23272637) |

English and Russian are language manifestations of each same article/version. The public Zenodo record is authoritative for deposited files; historic draft/candidate names and pre-deposit wording do not negate a later publication. [Machine-readable publication registry](../../registry/FIRST_CYCLE_PUBLICATIONS.json).

## Final video / Финальное видео

[WREH: какие миры совместимы с наблюдениями? Девять статей о границах познания](https://youtu.be/yf_N_LX28E0)

The link was supplied by the author on 10 October 2026 as the first-cycle finale. The video is an explanatory companion, not a substitute for manuscripts, proofs or review.

## Repository closure / Интеграция

| PR / branch | Final integration |
|---|---|
| [#6 — WR-V](https://github.com/AIDevelopersMonster/WREH/pull/6) | Merged into main: `f01792cb8296caf59a6aedd0172e04d59c3339eb` |
| [#7 — WR-VI](https://github.com/AIDevelopersMonster/WREH/pull/7) | Merged into main: `6652e9eb181f2a18e387ba4e953483c32c66e1f7` |
| [#8 — WR-VII](https://github.com/AIDevelopersMonster/WREH/pull/8) | Merged into original VI base: `289e82b0c1745474d0d45945d6d7b0656c0eea58`; history subsequently included in main |
| [#11 — WR-VII](https://github.com/AIDevelopersMonster/WREH/pull/11) | Same VII head merged into main: `05d551f4334d5ecf24b1193d5e3ade9ba2934f7d` |
| [#9 — WR-VIII](https://github.com/AIDevelopersMonster/WREH/pull/9) | Merged into main: `587a503fa0d47fba2ec027c6ec2484ce8a1ce294` |
| [#10 — WR-IX](https://github.com/AIDevelopersMonster/WREH/pull/10) | Merged into main: `948462e155308b9fe437f3f5bf1a685997fc4369` |
| Historical I audit / III / intermediate VI merge | Included as parents of `fa52ae33697d915078f7e2f07cb673a55a7f5a89`; tree identical to main after #10 |

The old I audit branch contains superseded release/overview/licence wording and earlier candidate title/PDF metadata. The current published v0.3 files are retained. III scientific files match the integrated snapshot. All branch heads are ancestors of the closure baseline, so no branch has outstanding commits outside main. Historical branches are retained as references; their existence is not an unmerged obligation.

## Validation / Проверка

- Nine existing reproduction/adversarial/source-alignment scripts pass on an isolated copy (IV–IX). These checks support reproducibility, not independent external peer review or a new full proof audit.
- Versioned scientific files match the pre-integration IX snapshot byte-for-byte. Current project pages, the programme register, publication pointers and new closure material are the only changed content.
- Every frozen, version-local checksum entry is verified. Historical manifests also include mutable project README/result/request pointers; their expected hashes apply at the original packaging commit, not to later active pages. They are preserved, not silently regenerated.
- The new [integration manifest](SHA256SUMS) covers 381 frozen scientific/package files: versioned packages, manuscript sources/PDFs, demos and founding PDFs. Active project pointers and new closure metadata are outside this manifest. [Verification report](verification.json).
- IX public metadata, four file checksums and the frozen archive comparison are recorded in the [publication identity check](../../reviews/WR-IX/WREH_WR-IX_Post_Publication_Check_v0.2_2026-10-10.md).

Older deposited descriptions can omit an explicit version, contain spelling/keyword imperfections or retain pre-deposit status. The canonical article/version/DOI map above resolves repository identity. Earlier audit reports remain historical evidence; they do not authorize silent replacement of already deposited files. Any later metadata correction must preserve the published scientific snapshot and be recorded separately.

## Next-stage handoff / Монография и второй этап

These are explicitly open research/evaluation questions, not unfinished first-cycle merges. None is claimed solved by this closure.

| Obligation | Possible next object | Required inputs / success or failure criterion |
|---|---|---|
| Independent scientific assessment | Named external reviews, broader claim-specific prior-art audit | Verify reviewer independence; resolve or record objections; no automatic novelty/priority certification |
| Unified exposition | RU/EN monograph or synthesis | One notation/interface map; exact citation/version discipline; separate inherited/classical results from new contributions; no new theorem by compilation alone |
| Empirical inverse problem | Survey/application work package | Real observations, covariance/joint likelihood, calibration and nuisance/selection models; assess coverage and falsifiable fit, not exact derivative data alone |
| Physically realizable cosmological futures | Declared matter/dynamical carrier | Require one justified evolution law, stability and units; kinematic compatibility alone is insufficient |
| Actual observer/apparatus access | Resource certification benchmark | Specify complete protocols, joint costs, detector noise, calibration and admissible control; test uniform bounds across the declared model family |
| Nonduplicative technical continuation | Separately chartered second-cycle article | New mathematical obligation, upstream handoff, primary-source comparison, theorem hypotheses and an accepted negative/failure result; numbering alone opens nothing |

Старт второго этапа требует отдельного утверждения предмета и нового проверяемого результата. Монография может усилить общую нотацию, связность доказательств, учебное изложение и карту ограничений. Применения требуют реальных данных и физически обоснованных носителей. Математическая совместимость, физическая реалистичность и эмпирическое подтверждение остаются разными уровнями.

[Classified closure audit](CLOSURE_AUDIT.md). Re-run the repository checks with `python docs/FIRST-CYCLE/verify.py`; the script does not mutate scientific files.

**Closure boundary:** repository/publication integration is complete; no journal acceptance, universal epistemic horizon, complete-world identification, new gravity theory or proven physical existence is asserted.
