# Independent probability review of Paper 13D

Date: 2026-08-20

Seat: probability, global evaluation, cuts, records, and erasure

Status: **ACCEPT / MATHEMATICS ONLY / NO IMPLEMENTATION REVIEWED**

## 1. Corpus authentication

I authenticated and read the complete frozen pin and candidate law before
adjudicating. I also read the construction note and hostile-review protocol.
I did not inspect either sibling Paper 13D report, and I used no evaluator,
fixture, Rust source, Python source, or generated result.

| artifact | commit | independently reproduced SHA-256 | authenticated size |
|---|---|---|---|
| physics pin | `a20c52a` | `722dc3bfe528fc3a52f2d2f5afcaba2c7858250e63d24439e43d0a17ab5c049e` | 459 LF lines / 14,240 bytes |
| candidate law | `efe9d97` | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | 1,285 LF lines / 42,928 bytes |
| construction note | `efe9d97` | `93f1e84444d60365fe729d73058dae1f3dede63a87bf1663d4865511255b50bb` | 203 LF lines / 9,792 bytes |
| hostile-review protocol | `04f503e` | `4754f89b01c7975ef79de2d9465e54304bbcf2d6e02b942f9957062a63c9eba3` | 301 LF lines / 13,009 bytes |

The corpus therefore passes the integrity gate.

## 2. Verdict and first decisive counterexample

**Verdict: ACCEPT.**

I found no reproducible semantic counterexample affecting a registered product
coordinate. Consequently there is no decisive counterexample to report.

The previously dangerous cases now have genuinely different types. The
invariant $t=h$ belongs to $B_2^r$, the stable entry copies it to the new field
$t^+$ in $B_3^r$, and $F_t$ acts only on that unconstrained later field. The
eraser is a normalized deterministic arrow $B_2^r\to B_3^e$ in
$\mathsf{Exec}_D$ and is absent from $\mathsf{Fut}_{\rm stable}$. It destroys
perfect future-boundary record readability while retaining the past source
entry in the complete trace. Those are distinct, well-typed statements.

Acceptance means only that the frozen candidate is mathematically defined and
the assigned probability claims follow. It neither selects this candidate as
the fundamental law nor authorizes implementation before separate terminal
adjudication.

## 3. Independent reconstruction summary

### 3.1 Exact numerical law

Squaring the declared rotation gives

$$
R^2=\frac1{25}
\begin{pmatrix}-7&-24\\24&-7\end{pmatrix}.
$$

The absolute squares therefore give

$$
B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix},
\qquad
C=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix}.
$$

The map $\beta$ retains its input for 9 of 25 uniform seeds and flips it for
16. The map $\kappa$ retains it for 49 of the 625 ordered seed pairs and flips
it for 576. Two independent $\beta$ transitions give

$$
B^2=\frac1{625}
\begin{pmatrix}
9^2+16^2&2(9)(16)\\
2(9)(16)&9^2+16^2
\end{pmatrix}
=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix}.
$$

With the paper's column-stochastic convention,

$$
B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix},
$$

so direct multiplication yields

$$
CB^{-1}=\frac1{175}
\begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
$$

Its columns sum to one, but its negative off-diagonal entries rule out a
positive continuation.

### 3.2 Generator normalization and traces

For every finite occurrence set, each source factor, occurrence seed, process
seed, and unordered-pair seed is normalized. The process generators are
deterministic pushforwards of those finite products. $D$ and $R_c$ draw only
fresh $u_2$ and bond seeds; stable maps and the eraser are deterministic;
fusion draws exactly one normalized seed for each new cross pair. Identities
are point masses. When the occurrence set is empty, all products are empty
products of mass one and every atomic boundary has its unique empty value.

A generator trace contains its physical source and target. Composition glues
the unique shared boundary and retains it, tensor retains a component-indexed
family of traces, and fusion retains both the tensor source and fused target.
Thus for a glued trace $H_f\star_yH_g$,

$$
\Gamma_{g\circ f}(H_f\star_yH_g\mid z)
=\Gamma_f(H_f\mid z)\Gamma_g(H_g\mid y).
$$

The intermediate $y$ is unique because it remains in the trace. Marginalizing
it produces ordinary convolution, but the defining law is the stronger
trace-valued identity.

For $D\circ Q_J^0$, direct expansion of independent $u_1,u_2$ gives

$$
P(m,q_2\mid q_0)=B_{mq_0}B_{q_2m}.
$$

The prefix also carries $(h,a)$, the continuation copies those fields and sets
$t=h$, and fresh pair seeds generate each endpoint bond conditional on the
copied colors. This is exactly the categorical convolution on every complete
trace. The $R_c\circ Q_J^r$ calculation is identical with the indicators
$r=m$ at the first leg and exact carrying of $r$ at the second. Hence the
direct seed expansion and categorical law agree on all fields, records, and
bonds, not only on the $B^2$ endpoint marginal.

### 3.3 Context, tensor, fusion, and quotient normalization

A consistent source cylinder fixes a compatible finite collection of public
binary coordinates and has strictly positive mass. Conditioning its normalized
product law is unique. An inconsistent cylinder denotes the empty event and is
refused before evaluation. Later-boundary sources are exact values and require
no posterior reconstruction.

Finite tensor products of normalized factor laws normalize, including the
empty deterministic unit. Fusion is deterministic at sorts without bonds. At
bond-carrying sorts, each new cross-pair Bernoulli factor has probabilities
$9/25,16/25$ or their complements and hence sums to one. The empty, singleton,
and multi-component fusion cases all normalize; no cross-pair factor exists
when fewer than two nonempty components provide a pair.

For the physical quotient, stabilizer orbits partition the presented history
fiber. Summing labeled mass over each entire orbit therefore preserves total
mass one. As a concrete multiplicity test, take a two-occurrence unmarked
experiment fixed by occurrence exchange. A history with distinct transported
local packets has a two-element orbit $(H,\sigma H)$ with equal labeled masses
$p$, so its physical cell has mass $2p$. A completely symmetric history is a
fixed point and has orbit size one. Assigning only representative mass would
replace $2p$ by $p$ on every nontrivial orbit and under-normalize; the frozen
orbit pushforward counts both cases correctly.

### 3.4 Native cut and all-size negativity

Fixing the complete common exterior leaves the process seeds independent. The
query carrier has first-leg law $B^{\otimes I}$, whereas the primitive
unqueried endpoint has law $C^{\otimes I}$. Because $B$ is invertible, the
only candidate continuation is

$$
K_I=C^{\otimes I}(B^{\otimes I})^{-1}
=(CB^{-1})^{\otimes I}.
$$

For every nonempty $I$, choose one factor equal to $-176/175$ and all other
factors equal to the positive diagonal value $351/175$. Their product is a
negative matrix entry. Thus no positive normalized continuation exists through
the frozen carrier at any nonempty finite size.

The relational packet in that carrier does not evade the obstruction. Once a
common exterior is fixed, its distribution is independent of $q_0$. Averaging
any hypothetical positive complete continuation over that packet would give a
positive process kernel $\bar K(q_2\mid m)$ satisfying $C=\bar K B$, which is
impossible. Enlarging the carrier by $q_0$ does evade it, as it must, but is a
different cut.

### 3.5 Divisions, stable records, and erasure

At complete $B_1^0=(m,h,a)$ and $B_1^r=(m,r=m,h,a)$ frontiers, every future
coin is fresh and every deterministic future clause reads only the supplied
frontier. Equal complete boundary values therefore have equal future laws.
The trace calculation above supplies exact direct/cut equality. Both queried
frontiers are complete divisions; only the latter carries a record.

The record-only restriction is insufficient. Holding $r$ fixed while changing
$h$ changes the mandatory endpoint $t=h$. Holding $r,h$ fixed while changing
the relational color can change the bond profile. These positive-mass pasts
have different future laws despite the same record.

For each stable generator, the output record is either unchanged, translated
bijectively by $F_r$, concatenated canonically under tensor/fusion, or carried
deterministically through $R_c$ and $\iota$. Consequently

$$
P^T_{\sigma_F(\rho)}F=FP^S_\rho.
$$

Tensor uses product label maps, fusion uses disjoint-union labels and draws
only record-independent cross-bond seeds, and composition multiplies label
bijections. Induction proves the equation for every finite word in the stable
subcategory.

The eraser is a deterministic normalized Exec arrow and is not a stable arrow.
For one occurrence, fix $q_0=0$, one positive relational packet, $q_2=0$, and
one positive bond assignment. The paths

$$
m=r=0\quad\text{and}\quad m=r=1
$$

have respective positive process factors $81/625$ and $256/625$, while their
$B_2^r$ endpoints can agree in every field except $r$. $E_r$ maps those two
endpoint values to the same $B_3^e$ value. Thus it erases perfect
future-boundary sector readability on reachable support. It does not delete
the $B_2^r$ source entry from the retained past trace.

### 3.6 Response and contrast measures

Each aligned intervention law is normalized on the common intersection-
stabilizer fiber. Therefore every signed comparison measure satisfies

$$
\sum_C\Delta_\chi(C)=1-1=0.
$$

Reader pushforward preserves that zero total. It can combine positive and
negative cells and display a zero, but it cannot remove the complete comparison
measure retained by the contrast object.

The Boolean evaluator independently gives:

- at fixed $Y,E$, changing $X$ flips $e'=E\oplus X\oplus Y$;
- at fixed $X,Y$, changing $E$ flips both $(x',y')$;
- without an $E'$ override, $z_Y=E\oplus X$, while fixing $E'$ removes the
  $X$ dependence;
- $P(y=1\mid x=1)=(16^2+9^2)/625=337/625$, but under
  `set(X,1)` the untouched $Y$ remains fair;
- parity $x'\oplus y'$ is blind to the $E$ flip while the complete pair is not;
- the `set(X,1)` minus `set(X,0)` effect on $u_X=1$ is $+1$ at $c=0$ and
  $-1$ at $c=1$;
- $q_0$ is absent from every relational truth function and is a registered
  spectator context contrast; and
- toggling one endpoint color changes a bond probability by $+7/25$ in an
  equal-color context and $-7/25$ in an unequal-color context.

These reconstruct both reciprocal response rows and every displayed control.

## 4. Registered attacks P1–P22

| attack | verdict | evidence |
|---|---|---|
| P1 exact $R,B,C,B^2,\beta,\kappa$ | PASS | §3.1 derives all values from the rotation and threshold counts. |
| P2 normalization of every atomic generator | PASS | Every generator is a deterministic pushforward of normalized finite factors; empty occurrence products have mass one. |
| P3 trace-valued composition | PASS | The retained shared boundary makes the glued-trace factorization pointwise, before endpoint marginalization. |
| P4 direct expansion versus convolution | PASS | Both queried paths agree on $m,h,a,q_2,t,r$ and every bond seed, not only on $B^2$. |
| P5 source cylinders | PASS | Every compatible partial public assignment has positive mass and a unique conditional law; the inconsistent empty event refuses. |
| P6 tensor and fusion normalization | PASS | Tensor is factorwise; fusion adds a normalized product only over fresh cross pairs, including all empty cases. |
| P7 orbit multiplicity | PASS | The two-occurrence swap example gives mass $2p$ on a nonfixed orbit and $p$ on a fixed point; representative mass undercounts. |
| P8 column-convention $CB^{-1}$ | PASS | The unique matrix is $\frac1{175}[[351,-176],[-176,351]]$. |
| P9 all-$I$ uniqueness/negativity | PASS | Invertibility gives the tensor candidate uniquely; one negative factor and positive diagonals give a negative entry for every nonempty $I$. |
| P10 mandatory nonkills | PASS | $(m,q_0)$ supports a positive restart, $C=CI=IC$ uses other cuts, and the empty process is the tensor unit. |
| P11 carrier smuggling | PASS | $q_0$, seeds, traces, control phases, and caches are absent from $B_1$; adding any one changes the boundary species. |
| P12 full-field future sufficiency | PASS | Complete $B_1$ values determine all copied fields and all subsequent deterministic/fresh-seed kernels. |
| P13 record-only insufficiency | PASS | Equal $r$ with opposite $h$ gives opposite $t$; omitted packet colors also alter bond profiles. |
| P14 stochastic $R_c$ projector carrying | PASS | $R_c$ randomizes only $q_2$ and bonds and carries $r$ deterministically, so the kernel is block-diagonal in record sectors. |
| P15 arbitrary stable composition | PASS | Every generator, tensor, fusion, and braiding has an exact record-label bijection; composition multiplies those bijections. |
| P16 reachable erasure pair | PASS | The explicit $81/625$ and $256/625$ branches can agree at the endpoint except for $r$ and are identified by $E_r$. Retained fields may still allow imperfect inference. |
| P17 executable normalized eraser | PASS | $E_r:B_2^r\to B_3^e$ is a deterministic Exec generator with mass one and is absent from Fut. |
| P18 deletion/extension | PASS | Restriction deletes exactly the incident occurrence and pair factors; extension exposes the same unordered finite seed set in either order. |
| P19 response controls | PASS | §3.6 reconstructs common cause, mediation, cancellation, reversal, spectator, bond sign, and both reciprocal rows. |
| P20 signed-measure normalization | PASS | Each contrast is probability minus probability and has total zero; complete comparison cells remain alongside coarse pushforwards. |
| P21 static refactorization | PASS | Moving a mechanism response while retaining observational mass changes a $J$-indexed generator value and hence defines another executable function. |
| P22 shortcut attacks | PASS | Structural recursion is defined on every legal source and complete history, including zero-mass cells; support, one coordinate, or selected inputs cannot replace it. |

## 5. Fresh probability countermodels

The following countermodels were constructed independently as attacks. They
clarify why the frozen constructors are needed; none repairs or defines the
candidate.

### F1 — alternative-dependent stabilizer

Take two otherwise exchangeable occurrences and a base program writing
$X_2=0$. Compare the aligned alternatives $X_1=0$ and $X_1=1$. In the first
experiment, exchanging the two occurrences can be an accidental symmetry of
the complete program; in the second it is not. Quotienting each law separately
and subtracting cells by name is ill-defined. The ordered contrast's
intersection stabilizer is the common subgroup and gives a normalized shared
comparison fiber, exactly as frozen.

### F2 — correlated retained-field erasure

For $q_0=0$, after the eraser the retained value $q^+=0$ still favors the
erased sector $r=1$:

$$
P(r=1\mid q^+=0)=\frac{256}{337}.
$$

Thus statistical information about the old record can remain in correlated
fields. Nevertheless both sectors have positive probability at the same
$q^+=0$ and identical remaining endpoint fields, so no future-boundary reader
recovers $r$ perfectly. This separates perfect record erasure from deletion of
all statistical evidence and matches the candidate's scoped claim.

### F3 — positive enlarged-carrier restart

On the enlarged carrier $(m,q_0)$ define

$$
K_+(q_2\mid m,q_0)=C_{q_2q_0}.
$$

It is positive, normalized, and reconstructs $C$ immediately. It does not
contradict native nondivision because it carries the exact source input that
the frozen $B_1$ species excludes.

### F4 — observational postselection counterfeit

Define a counterfeit `set(X,1)` by conditioning the empty-program law on
$x=1$. It predicts $P(y=1)=337/625$. The executable write keeps the $Y$
mechanism unchanged and predicts $1/2$. Both are normalized but disagree, so a
static chain-rule/postselection recipe is a different executable law.

### F5 — coarse-reader annihilation

Let the reader return only $x'\oplus y'$. The two $E$ interventions then have
identical reader laws even though their complete $(x',y')$ measures are
distinct. The signed total remains zero in both cases; a coarse zero is not a
zero comparison measure.

### F6 — representative-mass loss

On a two-element stabilizer orbit with labeled masses $p,p$, assigning $p$ to
the physical cell discards half its actual mass. Fixed points lose nothing, so
no global scalar correction repairs all cells. Stabilizer-orbit pushforward,
not representative mass, is required.

### F7 — support-only false equality

Two Bernoulli laws with parameters $9/25$ and $16/25$ have identical support
$\{0,1\}$ but different probabilities and opposite bond-response signs in
the two color contexts. Support equality therefore cannot replace the exact
all-cell response theorem.

## 6. Full product vector

```text
referent    P13D-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED
law         P13D-ONE-TYPED-EXECUTABLE-GAMMA-CONSTRUCTED
experiment  P13D-TYPED-EXPERIMENT-CATEGORY-CONSTRUCTED
nondivision P13D-NATIVE-B1-CUT-NONDIVISIBLE
record      P13D-TYPED-STABLE-FUTURE-CATEGORY-CONSTRUCTED
eraser      P13D-EXECUTABLE-ERASER-CONTROL-CONSTRUCTED
division    P13D-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13D-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13D-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13D-ACTUALIZATION-UNCONSTRUCTED
```

The `law` coordinate means one candidate executable function is fully defined;
it does not mean that nature or the preceding papers uniquely select it.

## 7. Semantic versus code classification

This was exclusively a mathematical-semantic review. The accepted claims were
derived from finite probability measures, typed boundary maps, structural
recursion, and exact orbit pushforward. No ownership, mutability, lifetime,
iterator, serialization, CLI, transaction, memory, cache, or performance issue
was considered. A later defect in any of those areas could be code-only only if
the frozen mathematical values remain unchanged. A changed kernel, boundary,
future generator, eraser, seed law, or quotient would be semantic and would
not be covered by this acceptance.

## 8. Scope and ontology walls

The record result is grammar-relative exact recoverability, not absolute
permanence. Erasure means loss of perfect distinguishability at the future
boundary, not deletion of the retained past trace and not necessarily removal
of every statistical correlation. A complete division is a sufficient typed
restart frontier; it is not synonymous with a local record or happening.
Native nondivision is relative to the frozen carrier and does not establish
absolute nonfactorizability, incomplete reality, or physical memory.

Relational response is sensitivity of the declared executable probabilities.
It is not by itself causal influence, chronology, a signal cone, geometry
response, backreaction, energy flow, gravity, or spacetime. The size family is
not growth time, event count, volume, duration, or a hidden clock. No possible
history is selected as actual.

Nothing here constructs actuality, chronology, causal order, dimension,
signature, topology, measure, duration, scale, metric, connection, curvature,
stress-energy, entropy, gravity, general relativity, a continuum limit, quantum
field theory, particles, or phenomenology.

## 9. Bounded wording clarifications

No mathematical repair is required. Three nonbinding clarifications would make
the existing scope still harder to misread without moving any law value:

1. In the source-context clause, say explicitly that a “consistent cylinder”
   is the conjunction of a compatible finite partial assignment of public
   coordinates. This is the constructor used by the normalization proof.
2. In the stable-record theorem, replace “both record sectors” by “all record
   words for nonempty $I$”; for $I=\varnothing$ the unique empty sector is the
   correct monoidal unit.
3. Whenever the tensor product identity is written on physical orbit laws,
   state that equality is through the canonical symmetric-monoidal/orbit
   identification. This prevents an ordered presentation of identical factors
   from being mistaken for extra physical labels.

These are explanatory scope refinements only. They change no probability,
boundary set, morphism, group action, reader, or product coordinate.

## 10. Report integrity

The final ordinary SHA-256, LF line count, and byte count are computed only
after the last byte of this report is frozen and are supplied with the review
delivery. Embedding the file's own final digest inside itself would change the
digest. The delivered checksum therefore binds this exact report in the same
ordinary manner as the reviewed corpus.
