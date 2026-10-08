# Независимый предпубликационный аудит WR-IV v0.2

Дата: 8 октября 2026 года.
Объект: AIDevelopersMonster/WREH, PR #5, открытый draft.
Проверенный commit: 05bfaaa64fda81b95f326faaa099e966dd103642.
Исходник: papers/WR-IV/WREH_WR-IV_Mathematical_Spine_v0.2.tex, 354 строки.
Дополнительно прочитаны README, THEOREM_MAP, PROGRAMME_REGISTER и оба внутренних аудита WR-IV на том же commit.
Аудит не вносит изменения в GitHub и не закрывает программные обязательства автоматически.

## Заключение

Формулы Gaussian conditioning, Brownian bridge и noisy endpoint корректны. Ошибка центрального результата не установлена. Однако текущий текст не готов к публикации: остаются недостаточно явные математические конструкции, слишком широкие интерпретации некоторых формулировок и неполная опора на источники.

Release status: **BLOCKED_SOURCE_SUPPORT**.
Этот единственный итоговый статус сопровождается блокирующими замечаниями C1/C2; он не означает, что источники — единственная проблема.
Разрешённый следующий этап: исправленный review draft, затем повторный аудит ограниченного набора исправлений и проверка PDF. Статус PUBLICATION_READY сейчас не обоснован.

## Потолок утверждений и архитектура

WREH — самостоятельные программа и сообщество. WR-IV добавляет историческую проекцию к совместимым глобальным завершениям; она не переоткрывает WR-II existence или WR-III generic fibre geometry. BC не используется как сообщество или источник новых результатов WR-IV.

Допустимый вклад этой версии — организация различий world/past/observable-past и соединение этой организации с классическими примерами. Математическая приоритетная новизна R1–R14 не установлена. R1–R5 — элементарные свойства образов множеств, R6–R8 — стандартная динамика/inverse limits, R9 — соглашение о типах объектов, R10–R14 — стандартное гауссовское условливание/smoothing. Новый термин или классификация сами по себе не доказывают новый математический результат.

## Таблица замечаний

| ID | Класс | Место | Проблема | Значение | Минимальное исправление | Claim-set effect |
|---|---|---|---|---|---|---|
| A01 | C1 | §7.2, 198–254 | Не указан выбранный регулярный условный закон при X_T=b | Событие имеет вероятность ноль; RCD определён только почти всюду до выбора версии | Ввести явное continuous bridge kernel K_b и доказать disintegration | clarifies |
| A02 | C1 | §7.1, 124–164 | Ранние данные упомянуты неформально; доказательство нижней PSD-границы опущено | Сравнивать нужно законы при одном фиксированном наборе прежних данных | Ввести A=a, Gaussian residual E и его ковариацию | clarifies |
| A03 | C2 | §7.1, 173–177 | “what shrinks … covariance or credible regions” | Сдвиг среднего не даёт вложенности posterior/prior областей | Говорить о directional variance и размерах выбранных областей, не вложенности | narrows |
| A04 | C1/C2 | §7.2, 250–260 | Не задана связь path law и множества C(D); положительная дисперсия не доказывает все пространственные свойства множества | Non-Dirac law, support и hard-constraint fibre — разные объекты | Определить W_T=C_{x0}([0,T]); endpoint fibre; отдельно обосновать uncountability | clarifies |
| A05 | C1/C2 | §4, 85 | Равенство Q(h1)=Q(h2) не обеспечивает rigidity произвольного всего P(D) | При наличии h3 с другим record observable fibre не singleton | Требовать Q constant на P(D), либо дать двухмировой counterexample | narrows |
| A06 | C1/C5 | §5–6, 88–108 | Не разделены весь inverse limit и fibre; деление точки R/Z на 2 без representative не определено однозначно | Тезис верен, запись и доказательство требуют уточнения | Определить widehat X и p0; выбрать r in [0,1), доказать continuous bijection compact→Hausdorff | clarifies |
| A07 | C2 | Abstract 22; Conclusion 329 | “shrinks” может читаться как строгое уменьшение; “later observations strictly reduce” вне условий | Refinement даёт subseteq; независимые Gaussian data C=0 ничего не сокращают | “is contained in”; строгую редукцию привязать к diffusion endpoint benchmark | narrows |
| A08 | C2/C6 | §8, 309–314; R9 | Различие типов подано как теорема с доказательством | Разные типы не исключают возможной связи между ними | Remark о том, что bridge не задан; не impossibility theorem | clarifies |
| A09 | C4 | §5–6, §9, bibliography | Нет ссылок для natural extension/inverse limits; нет source-level mapping | Утверждение об established subjects не закрывает prior-art obligation | Добавить проверяемые источники рядом с результатами; расширить таблицу provenance | clarifies |
| A10 | C4 | §7, bibliography | RTS — первичная статья; книги — последующие систематизации; источник bridge/RCD не привязан к конкретному месту | Общая ссылка на книгу не свидетельствует проверки именно требуемой конструкции | Разделить primary research и expository sources, указать доступные locator | clarifies |
| A11 | C3/C4 | THEOREM_MAP, Benchmark role | Обязательство “reduce set of historical trajectories” объявлено закрытым без явного projected set | Pinning whole path сокращает fibre, но support interior state остаётся R | Закрывать только после явного выбора пространства историй и проекции | clarifies |
| A12 | C5 | README, THEOREM_MAP, PROGRAMME_REGISTER | Заголовки v0.1 при v0.2; в Markdown повреждены backslashes/formula delimiters | Управляющие документы трудно проверять; R13 допускает чтение как theorem о любых diffusions | Синхронизировать версии, формулы и область R13: только Brownian diffusion | clarifies |
| A13 | C5 | LaTeX abstract/bibliography | Overfull 1.73865pt и underfull bibliography | Незначительная вёрстка, не научный дефект | Переформулировать abstract; повторно собрать и визуально проверить | none |

C0 для центральных вероятностных формул не обнаружен. A05 нельзя оставлять как универсальный критерий: при таком прочтении утверждение ложно. A06 — дефект определения в записи доказательства, а не опровержение Cantor-fibre theorem.

## Проверка доказательств

### R1–R5: images, refinement, rigidity

R1 и R2 верны. Counterexample R2 желательно завершить явным выбором W={(h0,0),(h0,1)}, C(D)=W.
R3 верен для фиксированных W и pi_- и действительно накопительных hard constraints. При смене модели, временного среза или замене прежних данных новыми inclusion не следует.
R4 верен благодаря явно указанной непустоте C(D'). Условия consistent refinement нельзя убрать.
R5 — корректный existential counterexample, но текст §4 должен указать весь fibre. Точный критерий:
|Q_-(P(D))|=1 iff P(D)≠empty и Q_- constant на P(D).
Два совпадающих records не обеспечивают это для остальных историй.

### R6–R8: backward histories

Детерминированность T даёт единственную forward orbit. Noninjectivity не гарантирует full backward histories над каждым x0. Например T:N0→N0, T(0)=1, T(n)=n при n≥1 неинъективен, но над 0 история отсутствует, а над 1 единственная бесконечная история (1,1,...): predecessor 0 не продолжается назад. В тексте слово “may” сохраняет корректность; его нельзя усиливать до “must”.

Для doubling map theorem о каждом fibre верен. На фиксированном fibre выбор representatives допустим; не нужны глобальные непрерывные inverse branches на окружности. Каждая finite coordinate зависит от конечного числа bits, поэтому coding continuous. Compactness bit space и Hausdorff property fibre дают continuity inverse. Идентификация зависит от маркировки ветвей: “homeomorphic after a choice of branch labels” точнее, чем “naturally homeomorphic”.

Finite-bit corollary верен для любого конечного фиксированного набора координат bits: оставшиеся свободные координаты образуют countably infinite product. Для initial block остаток — fibre над последним известным predecessor.

### R10–R11: conditional Gaussian covariance

Фиксируем прежние данные A=a. Пусть условно на них (X,Z) jointly Gaussian с means m_X,m_Z и covariance blocks P,C,S; S positive definite. Положим
E=X-m_X-CS^{-1}(Z-m_Z).
Тогда Cov(E,Z|A=a)=0. Gaussianity даёт независимость E и Z при A=a. Поэтому conditional law имеет mean m_X+CS^{-1}(z-m_Z) и covariance P-CS^{-1}C^T.

Нижняя PSD-граница следует потому, что это Cov(E|A=a). Верхняя — из PSD CS^{-1}C^T.
Directional strictness эквивалентна C^T v≠0. Строгая матричная редукция во всех ненулевых направлениях требует rank C=n; такого условия в статье нет и оно не нужно для directional statement.
Остаточная covariance может быть singular или нулевой: общая гауссовская теорема не утверждает noncollapse. Noncollapse доказывается отдельно для diffusion benchmark.

Вне Gaussian setting pointwise monotonicity conditional variance не следует. Закон полной дисперсии даёт сокращение в среднем, а отдельный результат наблюдения может повысить conditional variance. В тексте нельзя стирать Gaussian qualification.

### R12–R14: diffusion

При deterministic x0, fixed T>0 и diffusivity D>0:
Cov(X_s,X_t)=2D min(s,t).
Bridge mean m_b(t)=x0+t(b-x0)/T.
Bridge covariance 2D(min(s,t)-st/T).
При s=t получаем 2Dt(T-t)/T.
При 0<t<T она положительна и меньше prior 2Dt; reduction=2Dt²/T.
При t=0 и t=T variance=0. При D=0 noncollapse исчезает. Эти cases не относятся к строгим inequalities.

Для независимого Gaussian measurement noise с variance R>0:
Var(X_t|Y_T)=2Dt-(2Dt)²/(2DT+R).
Это положительно, меньше 2Dt и больше точной bridge variance при 0<t<T.
Limits: R→0 даёт bridge; R→∞ даёт prior.
Mean=x0+[2Dt/(2DT+R)](y-x0), поэтому posterior region меняет положение.

Положительная Gaussian interior variance доказывает не только non-Dirac path law: single trajectory имеет conditional probability ноль, потому что её значение в фиксированной interior точке имеет probability ноль. Countable family trajectories также имеет probability ноль. Это обосновывает uncountability любого full-measure carrier; не следует отождествлять carrier, topological support и список физически возможных exact paths.

Размерности согласованы: D имеет [length²/time], R — [length²], B_t — Brownian time scaling; обе дисперсии имеют [length²]. Data D и diffusivity D используют одну букву: редакционно лучше переименовать коэффициент в kappa.

## Точные рекомендуемые LaTeX-вставки

Все вставки ниже — предложения для следующего review draft, а не утверждение о внесённых изменениях.

### P1 — фиксированная модель перед Completion refinement

~~~latex
Throughout evidence refinement, the admissible world class \Wcal,
the reference temporal cut, and the projection \pi_- are fixed.
The order D\preceq D' means addition of hard constraints;
it does not include a change of model or replacement of previous data.
Refinement may leave the completion set unchanged.
~~~

### P2 — заменить последнее предложение §4

~~~latex
Observable-past rigidity holds precisely when \Pcal(D) is nonempty
and Q_- is constant on \Pcal(D). It can coexist with hidden-past
ambiguity: take \Pcal(D)=\{h_1,h_2\}, with h_1\ne h_2 and
Q_-(h_1)=Q_-(h_2).
~~~

### P3 — заменить определение history space в §5 и доказательство §6

~~~latex
Define
\[
\widehat X=\{(x_0,x_{-1},\ldots)\in X^{\mathbb N_0}:
T(x_{-n})=x_{-(n-1)},\ n\ge1\},
\qquad p_0(\widehat x)=x_0.
\]
Histories ending at a fixed x_0 form the fibre p_0^{-1}(x_0).
For the topological benchmark, X carries its circle topology and
\widehat X the subspace topology of the product.
~~~

~~~latex
\begin{proof}
Fix the representative r_0\in[0,1) of x_0. Given
\epsilon\in\{0,1\}^{\mathbb N}, recursively put
\[
r_n=(r_{n-1}+\epsilon_n)/2,\qquad x_{-n}=[r_n].
\]
Every history has unique representatives r_n\in[0,1), and recovers
the bits by \epsilon_n=2r_n-r_{n-1}\in\{0,1\}.
Thus the coding is bijective. Each coordinate depends only on a
finite prefix of the bit sequence, so the coding is continuous.
The bit space is compact and the fibre is Hausdorff; hence this
continuous bijection is a homeomorphism.
\end{proof}
~~~

Убрать слово “naturally” либо оговорить dependence on branch labels. Не утверждать непрерывность half-open representative map на всей окружности.

### P4 — Gaussian theorem: параметры и proof

Перед covariance matrix:

~~~latex
Fix previously observed data A=a and work throughout under that
conditional law. Let m_X and m_Z be the corresponding means.
Assume (X,Z) is jointly Gaussian under this law and S\succ0.
The formulas below use the continuous Gaussian conditional kernel.
~~~

Начало proof заменить:

~~~latex
Set E=X-m_X-CS^{-1}(Z-m_Z).
Then E and Z are jointly Gaussian and
\operatorname{Cov}(E,Z)=0, hence independent. Consequently,
\[
X\mid Z=z\sim\mathcal N
\bigl(m_X+CS^{-1}(z-m_Z),\,P-CS^{-1}C^\top\bigr).
\]
In particular, P-CS^{-1}C^\top=\operatorname{Cov}(E)\succeq0.
~~~

Сохранить существующий directional proof. Все ковариации здесь относятся к выбранному A=a; для случайного A statement применяется almost surely там, где условный Gaussian kernel и S(A)>0 существуют.

### P5 — заменить remark о credible regions

~~~latex
The reduction concerns conditional covariance. It does not imply
inclusion of posterior support in a smaller support, or nesting of
posterior and prior credible regions: their means may differ.
For the scalar nondegenerate Gaussian benchmark, central credible
intervals of a fixed probability have smaller length after
conditioning, but need not be contained in the prior interval.
~~~

### P6 — строгая конструкция Brownian endpoint kernel

Вставить перед theorem Brownian bridge, указав fixed x0 in R, T>0:

~~~latex
Work on the Polish path space
\[
\Wcal_T=\{w\in C([0,T],\mathbb R):w(0)=x_0\}
\]
with the uniform topology and its Borel sigma-field.
For every b\in\mathbb R, define K_b as the law of
\[
U_t^{\,b}=x_0+\frac{t}{T}(b-x_0)
+\sqrt{2D}\left(B_t-\frac{t}{T}B_T\right),
\qquad 0\le t\le T.
\]
The centered Gaussian bridge B_t-tB_T/T is independent of B_T:
its covariance with B_T vanishes at every t, and finite-dimensional
Gaussian independence extends to the path sigma-field.
Thus K_b is a regular conditional law of X given X_T=b:
\[
\mathbb P(X\in A,\ X_T\in E)
=\int_E K_b(A)\,\mathbb P_{X_T}(db)
\]
for Borel A\subseteq\Wcal_T and E\subseteq\mathbb R.
Although an arbitrary regular conditional law is determined only
\mathbb P_{X_T}-almost everywhere, this explicit weakly continuous
kernel selects a version for every b.
The notation X\mid X_T=b refers to this kernel, not to division
by the probability of the zero-probability event \{X_T=b\}.
~~~

Далее добавить covariance формулу 2D(min(s,t)-st/T). Это минимальная конструкция, обеспечивающая process-level statement, а не только marginal formula. Она совместима с классической residual construction; см. [S3].

### P7 — мост к completion sets и nonuniqueness

Заменить path-level remark:

~~~latex
For this benchmark, define hard endpoint compatibility by
\[
\Ccal(x_0)=\Wcal_T,\qquad
\Ccal(x_0,b)=\{w\in\Wcal_T:w(T)=b\}.
\]
Then \Ccal(x_0,b)\subsetneq\Ccal(x_0).
Both sets are compatibility classes, not sets of paths with
positive singleton probability. The kernel K_b is concentrated
on \Ccal(x_0,b).
For any fixed t_*\in(0,T), its evaluation marginal has a
nondegenerate Gaussian law. Hence K_b assigns probability zero
to every single path and to every countable family of paths.

If the historical projection retains an interval [0,t_*],
endpoint evidence need not shrink its compatible path set:
every continuous prefix starting at x_0 can be continued
continuously to b. Nevertheless the projected conditional law
has reduced variance at t_*.
~~~

Последний абзац важен: сужение whole path fibre не гарантирует строгое сужение historical image. Если “past” определён всем [0,T], это нужно назвать явно. Full support bridge на pinned continuous paths можно добавить только с отдельным доказательством/источником; вставка выше его не предполагает.

### P8 — noisy support и augmented worlds

~~~latex
For a noisy endpoint measurement y, the likelihood on \Wcal_T is
\[
L_y(w)=(2\pi R)^{-1/2}
\exp\!\left[-\frac{(y-w(T))^2}{2R}\right]>0.
\]
Thus the posterior path measure is equivalent to the prior path
measure and has the same topological support.
If worlds include measurement noise, exact observation gives
the constraint w(T)+\eta=y on the augmented space, while its
projection onto w still contains all of \Wcal_T.
~~~

Строго положительный likelihood и конечная нормировка обеспечивают mutual absolute continuity; additional source не требуется для приведённого прямого Bayes argument.

### P9 — inference order

~~~latex
\begin{remark}[Inference order and temporal order]
The definitions provide an evidence-refinement order and,
separately, a declared temporal model. They specify no map
identifying these orders. Any physical identification requires
an additional stated bridge; no general impossibility theorem
is asserted here.
\end{remark}
~~~

### P10 — Abstract / Conclusion / attribution

Заменить “Additional evidence shrinks the completion class” на:
“Accumulated hard constraints give nested completion classes, possibly equal.”

Заменить обобщённое “later observations strictly reduce uncertainty” на:
“In the declared Brownian endpoint benchmark, a later observation strictly reduces interior-state variance.”

Добавить в Prior-art boundary:

~~~latex
The propositions about images and refinement are elementary
consequences of the definitions. The doubling-map fibre and
the Gaussian smoothing results are classical benchmarks.
The present contribution is their organization within the WREH
history-projection framework; no new theorem-priority claim is made.
~~~

Это консервативное уточнение текущего claim ceiling, а не сертификат оригинальности framework.

## Носитель, множество и вероятность

| Объект | Exact endpoint | Gaussian noisy endpoint |
|---|---|---|
| Whole path hard-constraint fibre | w(T)=b, строгое подмножество W_T | На augmented (w,eta): w(T)+eta=y |
| Проекция noisy augmented fibre на paths | Не относится к exact model | Все paths: eta=y-w(T) |
| Interior-state support | R, несмотря на меньшую variance | R |
| Prefix compatibility при t_*<T в continuous-path model | Может оставаться всем C_{x0}([0,t_*]) | Также не исключает prefixes |
| Условная covariance | 2Dt(T-t)/T | 2Dt-(2Dt)²/(2DT+R) |
| Уникальность hidden path | Нет | Нет |
| Credible region | Меньшая длина при фиксированной probability, новое среднее | То же; nesting не гарантирован |

Контрпример к nesting: x0=0,D=1,T=1,t=1/2,b=10. Prior X_t=N(0,1), posterior=N(5,1/2). Приблизительные центральные 95% интервалы [-1.96,1.96] и [3.61,6.39] не вложены. Это аналитический пример аудитора, не результат WR-IV.

Чтобы превратить пример в строгое finite-resolution historical-set refinement, можно рассмотреть данные X_T∈[b-epsilon,b+epsilon] и явно выбранную temporal projection. Это возможное последующее развитие; оно не внесено и не требуется для исправления endpoint formula. Нельзя считать такое расширение уже доказанным в v0.2.

## Аудит источников

[S1] Rauch, Tung, Striebel (1965), Maximum Likelihood Estimates of Linear Dynamic Systems, AIAA Journal 3(8), 1445–1450, DOI 10.2514/3.3166.
Прочитан оригинальный журнальный текст в архивной копии, прежде всего §§2–3 и conclusion. Совпадают title, year, volume/pages и DOI. Это primary research для linear Gaussian smoothing. Он не служит единственной ссылкой на disintegration Brownian endpoint; continuous-time appendix прямо описывает формальный limit, не rigorous proof этого перехода.
URL: https://archive.org/download/wikipedia-scholarly-sources-corpus/10.2514.zip/10.2514%252F3.3166.pdf

[S2] Särkkä, Svensson (2023), Bayesian Filtering and Smoothing, 2nd ed., Cambridge, DOI 10.1017/9781108917407.
Publisher metadata и оглавление подтверждены; гл.12 “Bayesian Smoothing Equations and Exact Solutions”, pp.253–266 — релевантный locator. Полный author-hosted PDF получить не удалось; точный номер theorem/equation не заявляю проверенным. Это современная систематизация, не первичная статья 1965 года.
URL: https://www.cambridge.org/core/books/bayesian-filtering-and-smoothing/F88740E8D25010CF3119A5CA379FA37A

[S3] James W. Pitman, lecture 22 “Brownian Bridge”, Stat205B, Spring 2003; scribe Tianbing Chen.
Прочитан текст pp.22-2: Theorem 22.1 содержит B(t)-tB(1) и independence endpoint; remark обсуждает conditioning через shrinking endpoint bands, включая convergence in C[0,1]. Хорошая открытая проверка bridge construction; это lecture notes, не исторический первоисточник изобретения Brownian bridge и не замена отдельной проверки общего RCD theorem.
URL: https://www.stat.berkeley.edu/~pitman/s205s03/b_bridge.pdf

[S4] Karatzas, Shreve, Brownian Motion and Stochastic Calculus, 2nd ed., DOI 10.1007/978-1-4612-0949-2.
Publisher confirms authors, edition, DOI; показывает ©1998 и softcover publication 1991. Поэтому “1998” нельзя объявлять ошибкой автоматически: нужно указать используемый printing/edition. Полный текст и точный locator RCD/bridge не проверены. Для физических random-motion утверждений textbook background не заменяет проверку применимости модели к конкретному эксперименту.
URL: https://link.springer.com/book/10.1007/978-1-4612-0949-2

[S5] Clark and Fokkink, Embedding Solenoids, author-hosted research text.
Прочитаны §1 и начало §2: inverse limits covering maps, dyadic solenoid z→z², profinite fibre structure. Это primary research по solenoids, пригодное для соседнего prior-art context. Не выдаю его за исторически первый источник natural extension.
URL: https://cos.unt.edu/math/~alexc/E110.pdf

[S6] McCord, Inverse limit sequences with covering maps, Trans. AMS 114 (1965), 197–209.
Metadata подтверждены AMS annual index и references [14] в [S5]. Direct AMS article PDF returned 403; theorem-level coverage не проверено. DOI 10.1090/S0002-9947-1965-0173237-0 найден в каталоге, но publisher DOI-page в этом аудите не проверена; включать после издательской сверки. Не считать source obligation закрытым одной этой записью.
AMS index: https://www.ams.org/journals/tran/1965-120-03/tran-120-3-print-matter.pdf

[S7] Kolmogorov / projective extension.
В v0.2 projective-limit theory упоминается, но theorem extension не используется в доказательствах: Brownian motion уже принят существующим. Полный первоисточник в этом аудите недоступен. Минимальный путь — исключить неиспользуемое projective-extension утверждение из scope этой статьи либо добавить проверенную точную ссылку и отделить existence of process от conditional path law. Не приписывать Kolmogorov extension то, что доказывает bridge kernel.

[S8] WR-I/II/III.
DOIs согласованы между bibliography и прочитанным programme register. Zenodo pages не получены; внешняя проверка авторства, полного title и version/concept DOI не завершена. Прочитаны только текущие WREH control documents, не полный текст WR-I–III; поэтому глубокая проверка дублирования с ними остаётся частичной.
Все три bibliography items не имеют \cite в body текущего LaTeX. Добавить явные upstream citations и полные названия.

Неустановленного источника или недоступного locator нельзя обозначать PASS. Историческое первенство всех использованных методов этим аудитом не сертифицировано.

## Границы научной новизны

Фраза “physical inverse benchmark” оправдана как аналитический diffusion model с физической мотивацией. Это не новая экспериментальная inverse problem, не валидация конкретного устройства и не применение к космологии.
Endpoint-conditioned Brownian motion — простой полностью решаемый benchmark. Если цель следующего этапа — новая математическая research paper, одного его недостаточно для доказанной технической новизны.
Если цель — review/conceptual synthesis WREH с transparent provenance, текущий материал можно довести до неё указанными исправлениями.
Расширение до нескольких observations может усилить пример, но само по себе остаётся classical smoothing и автоматически novelty не создаёт.
Заявка о приоритете новой классификации требует сравнения с observability, identifiability, hidden-state inference, partial-observation reconstruction и natural-extension literature; такого exhaustive comparison здесь нет.

## Формальная проверка

Точный исходник собран два раза pdflatex -interaction=nonstopmode -halt-on-error.
Результат: 6 страниц; fatal errors отсутствуют; после второго прохода undefined citations/references отсутствуют.
Остаются overfull hbox 1.73865pt в abstract и underfull bibliography paragraph.
PDF визуально не проверен; publication render gate открыт.
R1–R14 — локальные labels theorem map, не одинаковая нумерация environments LaTeX. Обновить map с указанием section/label и действительно используемых условий.
README и THEOREM_MAP описывают v0.1 рядом с добавленными v0.2 results. В THEOREM_MAP и PROGRAMME_REGISTER видны сломанные TeX delimiters/commands: их нужно исправить отдельно от научного текста.

## Release gates

1. Внести P1–P10 и синхронизировать theorem map. Никакой новой physical claim не добавлять.
2. Закрыть source mapping для используемых Gaussian/bridge/inverse-limit results; обозначить недоступные первоисточники как open.
3. Явно определить historical projection, для которой application obligation считается выполненным. Не подменять strict history-set shrinkage уменьшением variance.
4. Сформулировать contribution как framework exposition/application of classical results, пока новый технический результат не доказан и prior-art comparison не выполнен.
5. Собрать corrected source, проверить ссылки и визуально проверить PDF.

Итоговый блок:
- Неразрешённые блокеры: A01–A11; version/formal defects A12–A13.
- Equations/theorems changed: в GitHub нет; предложены уточнения условий и proofs, центральные variance formulas сохранены.
- Claim set changed: в источнике нет; предложенные правки clarifies/narrows, без расширения.
- Bibliography verified: partial.
- Metadata verified: partial.
- Source compiled: yes, original at pinned commit, два прохода.
- PDF visually inspected: no.
- Release status: BLOCKED_SOURCE_SUPPORT.
