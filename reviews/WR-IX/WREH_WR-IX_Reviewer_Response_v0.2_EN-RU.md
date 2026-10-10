# WR-IX v0.2 — response to the supplied review / ответ на предоставленную рецензию

10 October 2026. Reviewed source: WR-IX v0.1, commit ab79c05433dd50a6a51385709492e26e6e9a3cfc. Revision: papers/WR-IX/preprint-v0.2/wrix-body.tex.

The input calls itself an independent review and uses the descriptive title “Resource Horizons and the Order of Quantifiers in Cosmology”. The canonical manuscript title remains **Epistemic Horizons: What Can an Observer Inside a World Ever Distinguish?** Reviewer authorship, independence, source access and method are not independently verified. This response records the scientific handling of the text, not an external-review certification.

Входной текст назван независимой рецензией и использует описательное заглавие «Resource Horizons and the Order of Quantifiers in Cosmology». Каноническое заглавие статьи сохранено: **«Эпистемические горизонты: что наблюдатель внутри мира вообще может различить?»** Авторство рецензии, независимость, доступ к источникам и метод проверки независимо не установлены. Ответ фиксирует научную обработку замечаний, а не сертификацию внешнего рецензирования.

## English response

| Review point | Decision | Exact location and patch | Reason and claim-set effect |
|---|---|---|---|
| 2.1–2.2: certificate and exponential formulas | Accepted as a check of the stated ideal model | Prop. 5.1, Cor. 5.2, Eqs. (5)–(7) unchanged | Inclusive detector/deadline endpoints and strict causal endpoint retained. Physical apparatus feasibility is not established. none |
| 2.3 and 3.2: quantified resources | Partly accepted | Prop. 7.1 / Example 7.2, Eqs. (11)–(12) unchanged; new final paragraph of §7 | No uniform finite time/launch-energy budget for this declared probe and family. This does not exclude every possible detector or redefine WR-II global realizability. clarifies |
| 4.1: cross-paper bridge | Partly accepted; proposed sentence rejected | §7 after Example 7.2 cites WR-II v0.5 **Example 10.19** and WR-VI v0.2 **Corollary 5.3** | WR-II has an unattained zero residual; WR-VI excludes the minimum-activity matrix by irreducibility; IX has resources unbounded above. These are related certification issues, not identical results. clarifies |
| 4.2: winding topology | Accepted with a narrower example | §4 after Eq. (4) and the existing prior-art paragraph; WR-VIII v0.2 **§7** cited | Explicit cubic quotient and Euclidean cover. The VIII patch condition is not the IX winding condition. No Poincaré-space construction is added. clarifies |
| 4.3: Figure 2 units | Accepted with a dimensional correction | §4 after Eq. (4); Figure 2 caption; tail-figure axes; demo legend | \(S(t)\) is a length-valued comoving path, \(S(t)/c\) a conformal-time interval. Axes show \(Ht\) and \(HS(t)/c\). Neither is shortest torus separation. clarifies |
| 4.4: cycle-closing sentence | Partly accepted | §8 after the first-cycle-status paragraph | The conclusion is restricted to declared models/protocols; a complete physical protocol class needs separate justification. clarifies |
| Final request to close the cycle | Accepted for the technical drafting cycle | §8, active registry and deposit guide | Technical preprint readiness remains distinct from deposit, independent review and integration of open PRs. clarifies |

The proposed phrase “the infimum of required resources … is not attained” is false for Example 7.2. In fact,

\[
\inf_{n\ge2}E_{\mathrm{req},n}=2E_d,\qquad
\inf_{n\ge2}T_n=\frac{2\log2}{H_0},
\]

and both minima are attained at \(n=2\). For \(f(n)=n\log n/(n-1)\), \(f'(n)=(n-1-\log n)/(n-1)^2>0\) when \(n>1\). The obstruction to one uniform budget is instead \(\sup_n T_n=\sup_n E_{\mathrm{req},n}=+\infty\). The unattained infimum in IX is \(\inf_n S_\infty^{(n)}=L\). The corrected manuscript keeps these objects separate.

No numerical score in the input is used as evidence of physical realism or novelty. Its proof checks cover selected results, not every numbered claim. Existing analytical proofs remain the basis of the manuscript; numerical checks do not prove infinite-tail divergence.

## Ответ на русском языке

| Пункт рецензии | Решение | Точное место и исправление | Основание и влияние на утверждения |
|---|---|---|---|
| 2.1–2.2: сертификат и экспоненциальные формулы | Принято в пределах идеальной модели | Утверждение 5.1, следствие 5.2, формулы (5)–(7) сохранены | Равенства на конечных порогах включены, причинный предел исключён; реализуемость прибора не установлена. none |
| 2.3 и 3.2: порядок кванторов | Частично принято | Утверждение 7.1, пример 7.2 и формулы (11)–(12) сохранены; добавлен последний абзац §7 | Исключён общий конечный бюджет данного протокола в объявленном семействе, а не любой мыслимый детектор. Глобальная реализуемость WR-II не переопределяется. clarifies |
| 4.1: связь с WR-II и WR-VI | Частично принято; предложенная фраза отклонена | После примера 7.2: WR-II v0.5, **пример 10.19**; WR-VI v0.2, **следствие 5.3** | Недостижимый нулевой остаток, исключённый минимум активности и неограниченные ресурсы — разные математические объекты. clarifies |
| 4.2: топология обхода | Принято с ограничением примера | §4 после формулы (4) и абзаца о предшествующих инструментах; ссылка на WR-VIII v0.2, **§7** | Явный кубический тор и евклидово накрытие; условие участка WR-VIII отлично от критерия обхода WR-IX. Пространство Пуанкаре не добавлено. clarifies |
| 4.3: размерности рисунка 2 | Принято с размерностной поправкой | §4, подпись и оси рисунка 2, легенда демонстрации | \(S(t)\) — сопутствующий путь с размерностью длины; \(S(t)/c\) — интервал конформного времени. Оси нормированы как \(Ht\) и \(HS(t)/c\). clarifies |
| 4.4: завершающая фраза | Частично принято | §8 после абзаца о статусе первого цикла | Вывод ограничен объявленными моделями и протоколами; полнота физического класса наблюдений требует отдельного обоснования. clarifies |
| Закрытие цикла | Принято для технической подготовки | §8, активный реестр, руководство по депозиту | Завершение текста отделено от депонирования, независимого рецензирования и объединения открытых PR. clarifies |

В примере 7.2 инфимумы требуемых ресурсов достигаются: минимальная энергия равна \(2E_d\), минимальное время — \(2\log2/H_0\), оба при \(n=2\). Для функции \(f(n)=n\log n/(n-1)\) производная \((n-1-\log n)/(n-1)^2\) положительна при \(n>1\). Общий конечный бюджет исключён из-за неограниченности ресурсов сверху. Недостижимый инфимум относится к оставшемуся пути \(S_\infty^{(n)}\), а не к требуемым времени и энергии.

Оценки «10/10» не принимаются за доказательство физической реалистичности или научной новизны. Входной proof-review охватывает выбранные результаты. Восемь исходных доказательств, двенадцать нумерованных формул и все нумерованные утверждения в v0.2 сохранены дословно; изменены пояснения, связи с источниками, подпись и оси рисунка, версия и статус технического комплекта.

Release status: **PUBLICATION_READY** for the technical preprint package after the recorded checks and render audit. No IX deposit/DOI or independent external scientific peer review is asserted by this response.

Статус: **PUBLICATION_READY** для технического комплекта препринта после документированных проверок и аудита вёрстки. Этот ответ не заявляет фактический депозит, DOI WR-IX или установленное независимое внешнее научное рецензирование.
