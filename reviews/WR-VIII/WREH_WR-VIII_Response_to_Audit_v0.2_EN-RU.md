# WR-VIII v0.2 — response to the prepublication audit

Audited parent: `6120d9b37196f9cee4f00bebc2ec1d84d43d44f0` (WR-VIII v0.1, PR #9). Revision date: 9 October 2026. The audit used separate mathematical derivations, boundary/adversarial witnesses and reruns of the author's scripts. It was an AI-assisted automated audit, not established independent external scientific peer review. The author's instruction now authorizes bilingual publication preparation.

| Finding | Class / location | Resolution in v0.2 |
|---|---|---|
| A01 | C2, abstract / Theorem 3.1 | Replace “every strictly increasing” by D∈C²[0,Z], D(0)=0, D′>0 throughout in EN and RU. The theorem itself already had these hypotheses. D(z)=ℓz³ is strictly increasing but D′(0)=0, requiring infinite H(0) in the flat completion; the widened abstract was invalid. |
| A02 | C1, equation (9), §4 | State 0<z≤Z and D_L>0 for the magnitude response. At z=0, log(D_L/10pc) has no finite value. No equation numbering changes. |
| A03 | C1 clarification, Proposition 6.1 / equation (14) | Specify that the joint rate admissibility set is the Cartesian product of the stated intervals. This is a deterministic model premise, not a statistical independence or coverage claim. A marginal box may be only an outer screen for a correlated joint set. |
| A04 | C2 clarification, Theorem 7.1 / equation (17) | Say “injective and a local isometry”, preserving the restricted metric tensor. Add R=1, L=3, x=±e₁: Euclidean distance 2, global torus distance 1; the wrapped shortcut leaves the stipulated patch. Local classical protocol equality is retained. |
| A05 | C2 clarification, Proposition 8.1 / equation (18) | State that the C∞ baseline is an additional premise. The C² distance inversion supplies C² a, not automatically C∞ a. Fixed matter dynamics are still not imposed. |
| A06 | C4 positioning, §4 / reference [13] | Attribute earlier low-redshift ruler/candle/clock calibration work to Heavens, Jimenez and Verde, PRL 113 (2014), 241302, DOI 10.1103/PhysRevLett.113.241302; arXiv:1409.6217v2. References [1]–[12] retain their numbering. No new cosmological priority is asserted. |
| A07 | C3 repository integration | Preserve the exact v0.1 parent and upstream WR-VII source f011aec8546705be1e6bd2bd0c5925da96861179. PR #9 remains stacked on open PR #8. All seven mathematical results are self-contained, so upstream merging is not a proof premise or a preprint-deposit prerequisite. Integration must be rechecked before merging into main. |

The strict curvature endpoint κ<D(Z)⁻² remains unchanged. For D(z)=z on [0,1] (c=1 and a fixed length unit), κ=1 gives H(1)=0 and is excluded. H(0)=c/D′(0) does not select curvature; a positive-redshift rate must be independently calibrated and pass the global cap. The rank result stays conditional on the exact three-parameter family. Scale symmetry is a kinematic response symmetry with free calibrations, not a symmetry of one fixed matter law. No theorem, equation or label number is silently renumbered; there are seven proof blocks, eighteen numbered equations and thirty-eight labels.

## Ответ на русском языке

Все обязательные замечания A01–A02 исправлены одновременно в английском тексте и полном русском переводе. Уточнения A03–A05 включены в условия и пояснения соответствующих результатов. A06 закрыто добавлением первоисточника о совместной калибровке линеек, свечей и часов; прежние библиографические номера сохранены. A07 обработано фиксацией происхождения исходника и разделением депонирования самодостаточного препринта и интеграции ветвей GitHub.

Математическое ядро не расширено: строгая граница кривизны сохранена, независимость калибровки скоростей требуется явно, интервальные сертификаты относятся к заданному совместному множеству, тор сохраняет локальный метрический тензор при ограниченных путях, гладкое будущее требует отдельной гладкой базы. Ни единственность физической Вселенной, ни решения одного фиксированного закона материи не заявляются. Автоматизированный аудит и техническая готовность файлов не являются внешним научным рецензированием, журнальным принятием или уже состоявшимся депонированием.
