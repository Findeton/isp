# v12 W6 — RECORD CO-REFERENCE AND EFFECTIVE DESCENT

**Status:** TERMINAL, STRICT, 2026-07-29 (delivered v12 LOG #35; internal audit #36; major repair #38; external hostile round + sub-audit #40, ACCEPT-WITH-FIXES; terminal-fix pass verified and adjudicated terminal at v12 LOG #41).
**Pin:** `v12/note-w6-record-coreference-pin.md` (STRICT), adopted from [REV4]
at LOG #29–#30.
**Binding antecedents:** paper 0 v2.2 §5 (the four-gate rule; the withdrawn
global $(E,\prec)$; T5″); W7 TERMINAL (LOG #24 — its scope engraving: *all of
W7 is one-chart mathematics; the co-reference bridge is W6's*); W3′ (LOG #14 —
the record hypotheses and the decision criterion, anchored, not re-proved).
**Receipts:** `v12/code/w6_coreference_exact.py` → `v12/code/w6_output.txt`.
120 rows (16 ANCHOR, 104 GATE), 120 pass, 0 fail, runtime under 3 s.
**Substrate:** exact arithmetic throughout — $\mathbb{Q}(\zeta_8)$ for the
dimension 4, 8 and 16 models, the totally real quartic field
$\mathbb{Q}(\cos\pi/8)$ for the committed 36-configuration composite model.
No floats in any path.
**Lean:** NONE.

---

## The headline

The census does **not** block. All six referents are typed, five of them
constructed from committed primitives with no new postulate, and the resulting
apparatus decides all three sub-problems on nine exact models.

> **Fact co-reference descends. Event-token co-reference descends exactly
> where the chart's declared generating structure — not its record law —
> distinguishes the tokens; and where an automorphism of the committed data
> exchanges two tokens, the honest object is a groupoid, not a set.**

**Three** of the six pre-registered outcomes obtain, on disjoint parts of the
material: **W6-FACT-DESCENT**, **W6-SET-AMALGAM** (scoped) and
**W6-GROUPOID-AMALGAM**. **W6-NO-DESCENT** and **W6-UNDERDETERMINED** obtain
only in the declared detector-validation branch, whose purpose is to prove the
test can fail; **W6-BLOCKED-AT-⟨referent⟩** does not obtain.

Three measurements carry most of the weight, and the third cuts against the
comfortable reading:

1. On the committed two-frame Bell model a fact-candidate map exists on
   **exactly the 56 of 144** ordered chart pairs whose final laws agree — and
   **32 of those 56 are different experiments**. Value-and-probability
   agreement is not fact identity; the common-extension certificate is
   (§W6-A).
2. On the same model the fact level leaves a **two-fold** ambiguity at *every*
   setting — the wing exchange preserves the whole final law — and only the
   declared generating structure cuts it to one. The cut is made at the
   **Born** level of leg matching, by *dynamical* provenance — the
   frame-isomorphism; the *structural* provenance filter (items 5+6) does none
   of it (§W6-B, measured by decomposition).
3. **Against our own reading:** the *realized* process — every leg restricted
   to the configurations actually occupied at each time — **never admits the
   identity**, at any of the six settings. At the four asymmetric settings it
   admits nothing at all; at the two symmetric settings it admits exactly one
   map, and that map is the **wing swap** — the opposite of what the full
   declared legs force. The token labelling there is fixed by declared
   transitions the process never takes (WHAT GROUNDS A TOKEN LABEL, below).

---

## STEP 0 — THE REFERENT CENSUS

No φ-map and no theorem until every object is typed. Each entry below is
either LOCATED in the committed corpus with `file:line`, or CONSTRUCTED from
committed primitives with the four gates written out.

### 1. The chart-local stable record algebra $\mathcal{R}_a$ — LOCATED

The corpus's record structure is a **label list**: a map from configurations to
sector labels, with the two support hypotheses and an $O(n^2)$ decision
criterion.

- `v12/paper1_code/sec4_records.py:48` — `h_avail`, (H-avail): every row
  support of the later dynamics lies in one sector.
- `v12/paper1_code/sec4_records.py:53` — `h_corr`, (H-corr): for every column
  of the writing leg the live alternatives lie in distinct sectors.
- `v12/paper1_code/sec4_records.py:62` — `merge_partition`, $M(U_2)$.
- `v12/paper1_code/sec4_records.py:176` — the declared dim-4 record
  `part = [0,1,0,1]`; `:198`, `:199` its two committed hypothesis values.

**W6's typing.** A **record token** $t$ = (a partition of the chart's
configurations, a declared **value** on each sector, the index of the leg that
writes it, a provenance tuple). Two status bits are *computed*, not
stipulated, and each is read at the place the corpus defines it:

$$\textbf{occurred}(t) = \text{(H-corr) at the \emph{writing leg}},\qquad
\textbf{available}(t) = \text{(H-avail) under the composition of the declared
later legs}.$$

A chart's record tokens are exactly the candidates with `occurred = True`. The
**record algebra** $\mathcal{R}_a$ is the finite Boolean algebra on the
**actual** (positive-probability) value tuples of the chart's tokens, carrying
the exact joint law computed from the declared initial configuration.

**This typing is not free at the composite scale, and the instrument says so.**
On the 36-configuration model the *pointer alone* is not always a record
structure: wherever the local operator is not diagonal, the other basis
alternative on the same wing is co-live and (H-corr) fails on the pointer
partition. Measured over all six settings and both wings, the pointer-alone
partition satisfies (H-corr) exactly where the measurement angle is $0$ — on
wing A at SP-A, SP-B and SP-E, on wing B at SP-E, and nowhere else — while the
partition by $(q_X, p_X)$ satisfies it at every one of the twelve. The
composite tokens therefore carry the $(q_X,p_X)$ partition with the pointer as
their **value**, and all 24 of them are then *computed* to have occurred and to
be available. The chart law so obtained reproduces the committed `outcome_law`
exactly (gated).

**When the law is read.** At the time every token has been written — not at
the final time. For an *available* record the two agree, which is what
availability means. For an *erased* token they do not: after erasure the later
legs have moved amplitude across the record sectors, so the final distribution
is not the record's law. Reading at the final time would make the erasure
control test the wrong thing.

**Why only actual values.** T5″ forbids inferring a global actuality object,
and the pin's W6-SET-AMALGAM clause restricts any amalgam to actual stable
records. Zero-probability value tuples are therefore not atoms. This is not
cosmetic: at the two settings where the singlet law is perfectly
anticorrelated the algebra has **2** atoms, not 4, and that is what makes the
Boolean item of the preservation list bite.

### 2. The overlap object — CONSTRUCTED, and derived rather than postulated

The pin allows an overlap object to be declared. It does not have to be. Given
two charts, define a **frame-isomorphism** $\psi : b \to a$: a bijection of
configurations carrying $b$'s initial configuration to $a$'s, $b$'s leg
**multiset** to $a$'s under some matching, and each of $b$'s record partitions
to one of $a$'s. The **overlap object** is the set of token maps so induced.

The **matching level** is a declared parameter of the object, because which
level of the data does the work is exactly what W6-B has to measure:
*exact* (amplitudes on the nose), *sign* (amplitudes up to an overall sign per
leg — a real orthogonal propagator and its negative generate one stochastic
process), *Born* (the stochastic layer alone).

*Four gates.*

- **Referent.** Definable from committed primitives only: the declared legs,
  the declared initial configuration, and the record partitions of census §1.
  No new primitive; no shared substrate is presupposed — a bijection is
  searched for, not assumed.
- **Necessity.** The withdrawn global $(E,\prec)$ presupposed cross-chart event
  identity (paper 0 §5). Something must supply it or the atlas has no bridge.
  Measured necessity: on the committed model the fact level admits **two**
  identifications at every setting and the overlap object cuts it to one.
- **No-smuggling.** The definition contains no cross-chart identity: it
  quantifies over bijections and keeps only those carrying one chart's own
  declared structure onto the other's. Measured: **0** of the 120
  cross-setting ordered pairs admit one.
- **Discriminator.** The count itself (census §6).

**The corpus's own declaration, reproduced.** `model_composite.py:26-28`
declares the two frames to be *"the same two local events in the two orders, on
one configuration space"*. The derived object reproduces exactly that and
nothing more: at every setting the unique induced token map is the identity,
and the token-overlap graph on the twelve committed charts — whose components
are computed by breadth-first search **on the measured adjacency**, not by
grouping charts by name — has **6 components of size 2**, one per setting,
with **0 triangles**.

**The leg matching must be order-free**, and this is forced by the mandatory
controls, not chosen: two frames of one experiment differ *exactly* by the
order of two commuting legs. Measured: if leg order were required, the
committed model would have **no** frame-isomorphism at any setting and control
3 could not be met at the token level.

### 3. The candidate co-reference map $\varphi_{ab}$ — CONSTRUCTED

$\varphi_{ab}$ is presented as a **token bijection** $\tau$ from $b$'s tokens
to $a$'s, extended to the unique Boolean isomorphism of the generated
algebras. Where a scope filters tokens — an erased record is present
historically and absent from the available algebra — the admissible maps are
the **restrictions to that scope** of the frame-isomorphism-induced maps. A
regression model is carried in the census for exactly this: an
eight-configuration two-token chart whose second token is erased, on which the
scope-filtered level-B search returns 1, not 0.

*Four gates.* **Referent** — a map of finite Boolean algebras with state,
availability and provenance, all census §1's data. **Necessity** — fact
identity cannot be read off values (M7) nor off structural provenance alone
(M2); a map
with a preservation list is the minimal object separating the two.
**No-smuggling** — $\varphi$ is never declared, it is enumerated: every token
bijection is tested against the list and the survivors are counted; nothing
chooses among survivors. **Discriminator** — census §6.

### 4. The preservation list — and where each item is measured to bite

Each row names a pair on which that item, **on its own**, rejects every
candidate map. The attributions are computed by the instrument
(`bite_profile`), not asserted.

| # | item | where the item alone rejects | receipt |
|---|---|---|---|
| 1 | Boolean operations (the induced map of record atoms is a bijection) | SP-A ← SP-E: 4 atoms against 2 | `M3/items that bite …` |
| 2 | definite record values (the declared value *range* of each token) | SP-A/F1 ← V2, whose ready sector is declared `z` rather than `r`; that sector has probability zero, so the whole law and every realized value are unchanged | `M3/ITEM 2 BITES … (0, 2, ['2 values'])` |
| 3 | probabilities on the shared algebra | SP-A ← SP-B: same atoms, different law | `M3/items that bite …` |
| 4 | persistence / availability | SP-A/F1 ← V4, the same experiment continued by $U_B$ twice more; $U_B^3 = 1$, so the propagator and the law are untouched and only (H-avail) for $R_B$ fails. Also the dim-4 eraser against the preserving chart | `M3/ITEM 4 BITES … (0, 2, ['4 availability'])`; `M5/which item kills P<-E historical` |
| 5+6 | causal/process provenance and original-vs-copy | M2's redundant copies: the structural provenance filter (items 5+6) alone returns 0 | `M2/DECOMPOSITION … (0, 0)` |

Items 5 and 6 are carried by one filter and are **not** claimed independent of
each other: the copying lineage is the datum that separates an original from a
copy, and the erasure history is computed by (H-avail). Both are compared only
as grounds for **rejection**, so the filter can never create an identification.
This filter is what the note calls the **structural provenance filter**; it is
a different object from **dynamical provenance**, and census §7 names the two
apart.

**PHASE IS NOT ON THE LIST.** No item consults an amplitude phase, a Bargmann
or Haagerup four-cycle product, or any W7 invariant. Control M8 constructs the
phase-consulting item and runs it.

### 5. The declared gauge — CONSTRUCTED

The declared gauge is **configuration relabelling**: a chart may be presented
on any labelling of its configuration set. Coherence is judged modulo this and
nothing else. Measured: relabelling changes the legs and the initial
configuration while leaving the record algebra pointwise fixed. Because the
gauge acts trivially on the base, the triple law is judged **on the nose**.

W7's boundary gauge (vertex switching on $\Gamma$; the K-vertex switching seam
torsor, W7 §14) is **not** in W6's gauge. It acts on the fibre.

### 6. The insertion-vs-co-reference discriminator — CONSTRUCTED

$$|\Phi_{ab}| = 0 \Rightarrow \textbf{ABSENT};\quad
|\Phi_{ab}| = 1 \Rightarrow \textbf{FORCED};\quad
|\Phi_{ab}| \ge 2 \Rightarrow \textbf{UNDERDETERMINED}\ \text{(any named
single map is inserted)};$$
$$\text{empty scope} \Rightarrow \textbf{VACUOUS};\qquad
\text{no applicable instrument} \Rightarrow \textbf{NO-INSTRUMENT}.$$

The **emptiness guard** matters. Comparing two charts whose available algebras
are both trivial yields exactly one map — the empty map. Counting it as
*forced* would report agreement where nothing was compared. The discriminator
calls that case VACUOUS. The descent table below uses this vocabulary for
columns A and B; column C uses the descent classification of §W6-C, and both
carry **NO-INSTRUMENT** in every cell for which this unit runs no instrument —
the word is emitted by the discriminator, not typed in. This is GW1's kill
inherited: a proposal naming one map where the data admit several has added
structure.

### 7. Provenance — CONSTRUCTED, and then made derived

$$\mathrm{prov}(t) = (\text{generating interaction},\ \text{local support},\
\text{causal ancestry},\ \text{copying lineage},\ \text{erasure history}).$$

*Four gates.* **Referent** — every field is read off the chart's own declared
leg list. **Necessity** — measured at M2, where the filter alone refuses the
copy. **No-smuggling** — the cross-chart part is supplied only by census §2's
search-derived overlap object; the chart-local part enters only as a ground
for rejection. **Discriminator** — M2 (provenance differs, one fact) against
M5 (provenance survives erasure).

**Two provenance objects, named apart.** The pin's list names provenance
twice over, and W6 keeps the two apart by name everywhere below.
**Dynamical provenance** is census §2's frame-isomorphism: charts matched by
their own declared legs and initial configurations — the pin's "generating
interaction" and "local support". **The structural provenance filter** is
items 5+6 of census §4: copying lineage and erasure history, applied as a
post-filter that can only reject. Wherever this note says which of the two
does a piece of work, it says which by name.

**Names are never compared.** Comparing declared provenance *strings* across
charts would be circular, since the labels are exactly what is in question.
W6-B admits only token maps induced by a frame-isomorphism, then applies the
structural filter (lineage, erasure). M6 measures what the refused
name-comparing rule would do: it would return **1** where the honest apparatus
returns **2**.

### Census verdict

**PASSES.** Six objects typed: one LOCATED (census §1), five CONSTRUCTED from
committed primitives (census §2–§6), one primitive re-derived rather than
declared (census §7). No new postulate was needed. **W6-BLOCKED-AT-⟨referent⟩
does not obtain.**

---

## W6-A — FACT CO-REFERENCE

**Definition.** Two local records carry the **same fact** iff a candidate map
exists *and* is certified by one of the pin's two routes:

- **ROUTE-EXT** — in a declared common record-preserving extension the two
  record variables are perfectly correlated **along the identity of values**:
  the joint law is supported on the graph of a value-preserving bijection.
- **ROUTE-WIT** — a specified common-record witness is perfectly correlated
  with both.

**The candidate level is not the criterion.** Over the 144 ordered pairs of
the twelve committed charts:

| quantity | value |
|---|---|
| ordered pairs whose final laws agree | **56** |
| ordered pairs admitting a fact-candidate map | **56**, with **0** violations of the biconditional |
| of those, pairs that are the *same* experiment | **24** |
| **accidental agreements** (different settings, identical law) | **32** |

The final-law classes have sizes $\{2,4,6\}$: the six settings collapse to
three laws, because the singlet law depends only on the product of the two
outcomes and on $\cos(a-b)$. On the SP-A/SP-C accidental pair the only
available common extension is the product of two independent runs, whose joint
law has **16** positive entries — not bijection-supported. ROUTE-EXT fails; the
pair is not the same fact.

**The biconditional is a fact about the committed twelve, not a property of
the instrument.** On that material items 2 and 4 are constant, so the
biconditional is carried by items 1 and 3 alone — stated, and measured
(`M3/items 2 and 4 are CONSTANT on the committed twelve` $= (1,1)$). Adding
the two variants of census §4 — V2, which changes only a token's declared
value range, and V4, which erases $R_B$ while leaving the propagator and the
law untouched — **breaks** the biconditional at **26** ordered pairs of the
resulting fourteen charts. Agreement of laws is therefore genuinely
insufficient once the other items have anything to say.

**Where the certificate succeeds** it rests on a measured fact: at **SP-A** —
the one frame pair on which ROUTE-EXT is run — the two frames assign every
final configuration the same probability (**0** disagreeing configurations), so
reading each configuration through either frame's own record map gives a
diagonal joint law — (True, 4). The same construction against a **corrupted**
partner — the same process with its two record partitions exchanged — returns
(False, 4, not bijection-supported).

The construction's other branch is exercised too, and it is consequential. The
common extension is built only where both charts give a configuration the same
probability; a partner drawn from a *different* setting disagrees on **4**
configurations, and the four that remain would return a certificate. Reporting
that certificate would be a claim about a sub-support and not about the pair,
so a discarded configuration disqualifies the pair outright: the verdict is
DISAGREEMENT, not the True the remainder offers. The certificate can fail, and
is shown failing in three distinct ways.

**ROUTE-WIT** is exercised on a four-qubit three-copy model: the joint law is
$\{(0,0,0),(1,1,1)\}$ and the third token certifies the first two.

**Value preservation is load-bearing.** At SP-E the two wings' outcomes are
perfectly anticorrelated, so the joint law *is* supported on a bijection — but
a value-reversing one. "A's outcome is $+$" and "B's outcome is $-$" are
different facts even when perfectly anticorrelated, and the list rejects the
map: (False, 2, bijection-supported).

---

## W6-B — EVENT-TOKEN CO-REFERENCE

**Definition.** Two tokens denote the **same occurrence** iff the token map is
induced by a frame-isomorphism (census §2) and survives the structural
provenance filter (census §7).

**Measured separation from W6-A.**

- **Redundant copies (M2).** One process writes the same alternative twice, at
  two different legs. The two charts have *identical* record laws and
  ROUTE-EXT certifies one fact — yet $|\Phi_B| = 0$. The zero is produced
  **twice over, independently**: no bijection of configurations carries the
  second copy's partition onto the first's while fixing the leg multiset, and
  the structural provenance filter alone also refuses (lineage *original*
  against
  *copy-of*). One fact, two occurrences. *The negative is not an empty
  search:* the same search returns the identity on each chart against itself,
  and the register swap **does** carry the second copy's partition onto the
  first's while **not** fixing the leg multiset.
  The full token-level edge set over $\{a, b, c\}$, with $c$ a relabelling of
  $a$, is $(a{\leftarrow}b) = 0$, $(b{\leftarrow}a) = 0$,
  $(b{\leftarrow}c) = 0$, $(c{\leftarrow}b) = 0$, $(a{\leftarrow}c) = 1$,
  $(c{\leftarrow}a) = 1$: the **two** relabelling edges are genuine token
  identifications and the **four** copy edges are not. Descent over that atlas
  is ABSENT-PAIR.
- **The two-frame wing tie (M3).** $|\Phi_A| = 2$ at every setting: the final
  law is invariant under exchanging the wings. $|\Phi_B| = 1$ at every
  setting, and the surviving map is the **identity**. What cuts two to one is
  the frame-isomorphism, and the level at which it cuts is measured:
  $|\Phi_B| = 1$ also when the legs are matched only up to sign, and also when
  they are matched at the **Born** level. Amplitude-level data are not needed.
  What cuts is **dynamical** provenance — the frame-isomorphism; the
  **structural** provenance filter (items 5+6) does none of the cutting here,
  since removing it leaves $|\Phi_B| = 1$ at every setting.
- **Erasure (M5).** Occurrence and availability are different predicates and
  the formalism keeps them apart. Three charts — preserving, erased, and one
  where the record was never written — give historical token counts $(1,1,0)$
  against available counts $(1,0,0)$. The erased token is **not** identified
  with "no event": historically, erased ← never-written is ABSENT at both
  levels. At the *available* level both algebras are empty and the comparison
  is reported **VACUOUS**, which is precisely why the historical level must
  exist. The preserving and erased charts carry the **same record law**, the
  item that kills their identification is measured to be availability and
  nothing else, and forcing the availability bits equal turns the 0 into a 1.

**The scope of every level-B negative is stated where it is used.** On the
36-configuration model the frame-isomorphism search runs over a **declared
72-element** permutation scope (wing exchange × pointer 3-cycles on each wing ×
the two qubit flips). The filter "carries $b$'s initial configuration to $a$'s"
admits **exactly two** of those 72 — the identity and the pure wing exchange —
because the ready pointer state is not fixed by a 3-cycle. Every level-B
statement about the composite model is therefore a statement about a
**two-element search**, and this is gated, not glossed. An **extension** is
also run: adjoining the pointer *transposition* $+\leftrightarrow-$, which does
fix the ready state, gives a 96-element scope of which **8** survive the same
filter. $|\Phi_B| = 1$ at every setting on the wider search too.

**What W6-B is not.** It does not deliver a co-reference rule for *unrecorded*
configurations. That is O4-A's price (paper 0 §5) and remains open.

---

## W6-C — EFFECTIVE DESCENT

**The coherence laws.** $\varphi_{aa} = \mathrm{id}$;
$\varphi_{ba} = \varphi_{ab}^{-1}$;
$\varphi_{ab}\circ\varphi_{bc} = \varphi_{ac}$ on triple overlaps, modulo the
declared gauge only — which, by census §5, is trivial on the base.

**The solver.** Every **ordered** edge that is declared is enumerated
independently, so $\varphi_{ba} = \varphi_{ab}^{-1}$ is a constraint a declared
family can violate rather than an identity the solver imposes; triple equality
is tested on the **full domain**, so a map with missing keys fails in both
directions. Coherent families are then acted on by $\prod_x \mathrm{Aut}(x)$
via $(g\cdot\varphi)_{xy} = g_x\circ\varphi_{xy}\circ g_y^{-1}$; the action's
**closure** — does $g\cdot\varphi$ still lie in the $\Phi$ sets? — and whether
it **moves** any family are reported, not assumed; orbits are counted; the
colimit is built and each chart checked to inject. The classification:

| condition | verdict |
|---|---|
| some $\Phi_{ab} = \emptyset$ | ABSENT-PAIR |
| no coherent family | **W6-NO-DESCENT** |
| one gauge orbit, all $\mathrm{Aut}$ trivial | **W6-SET-AMALGAM** |
| one gauge orbit, some $\mathrm{Aut}$ nontrivial | **W6-GROUPOID-AMALGAM** |
| several gauge orbits | **W6-UNDERDETERMINED** |

This is the standard shape for a groupoid-valued gain graph — cycle holonomy
modulo vertex switching — cited from [GG] (Zaslavsky), not claimed as ours;
the gain group here is the symmetric group of record tokens rather than $U(1)$.

**The solver is validated against four ways of failing** (M9), on declarations
over the same three charts: a **twisted** declaration whose triangle has
holonomy returns NO-DESCENT with 0 coherent families where the consistent one
returns SET-AMALGAM; an **asymmetric** declaration
($\varphi_{ba} \ne \varphi_{ab}^{-1}$) fails; an **inverse-consistent
partial-domain** map — truncated in both directions alike, so that the inverse
law passes and the triple law is what must do the rejecting — fails the
full-domain triple law; and the latent case of one coherent family with
nontrivial automorphisms is classified with its gauge action and closure
reported rather than presumed. All five branches of the classification are
reached. Which law rejects which declaration is itself measured, independently
of the solver's early exit: the asymmetric declaration carries **2** inverse
violations, the truncated one **0** inverse violations and **6** triple
violations.

**The scope limit, stated plainly.** The committed atlas contains **no
nonvacuous triple overlap**: the token-overlap graph on the twelve committed
charts is 6 components of size 2 with 0 triangles. Triple coherence is
therefore untested by the committed twelve alone.

**The third chart is a real object.** M3's descent is measured at **SP-A**,
and there only. The triple is $\{F_1, F_2, F_2^\pi\}$ at that setting, where
$F_2^\pi$ is $F_2$ presented on a relabelled
configuration set (both qubit flips), built as its **own** object: its own
legs, its own initial configuration $j_0 = 27 \ne 0$, its own token objects
with pushed partitions, and its law **recomputed** from the relabelled
process rather than copied. That the recomputed law equals $F_2$'s is a
measurement, not a definition. All six ordered edges of that triple carry a
token-level identification, so the triple law is genuinely exercised.

---

## THE DESCENT TABLE

Vocabulary: **FORCED** $|\Phi| = 1$ · **UNDERDETERMINED** $|\Phi| \ge 2$ ·
**ABSENT** $|\Phi| = 0$ · **VACUOUS** empty scope · **NO-INSTRUMENT** no
measurement available. Columns A and B carry that vocabulary; column C carries
the descent classification of §W6-C, and either column carries NO-INSTRUMENT
where this unit runs no instrument at all. A candidate map that exists but is
refused by ROUTE-EXT/ROUTE-WIT is marked *not certified*: the count and the
certificate are separate questions and the table keeps them separate.

| model | A (fact) | B (event token) | C (effective descent) |
|---|---|---|---|
| **M1** relabelled same record | **FORCED**, certified | **FORCED** | **SET-AMALGAM** (1 family, 1 orbit, 6 triples, gauge-closed; amalgam size 1, injective) |
| **M2** redundant copies | **FORCED**, certified by ROUTE-EXT *and* ROUTE-WIT | **ABSENT** on the four copy edges; **FORCED** on the two relabelling edges | SET-AMALGAM at the fact level (1 family, 6 triples); **ABSENT-PAIR** at the token level |
| **M3** two-frame final outcomes | **UNDERDETERMINED** ($|\Phi_A| = 2$), certified; candidate on exactly 56 of 144 | **FORCED** ($|\Phi_B| = 1$, the identity map, all six settings) | **GROUPOID-AMALGAM** at the fact level (at SP-A: 4 families, 1 orbit, gauge moves them, closed); **SET-AMALGAM** at the token level (at SP-A: 1 family, 6 triples, amalgam size 2, injective) |
| **M4** intermediate frame content | **FORCED but NOT CERTIFIED** — one token each, so $|\Phi_A| = 1$ carries no multiplicity; ROUTE-EXT at $t = 2$ refuses it at every setting | **ABSENT** ($|\Phi_B| = 0$, all six settings) | **NO-INSTRUMENT** — no shared record subalgebra (derived: 0 shared partitions at $t = 2$ against 2 at the final time) |
| **M5** record erasure | **ABSENT** historically; **VACUOUS** on the available scope | **ABSENT** ($|\Phi_B| = 0$) | **NO-INSTRUMENT** — no triple declared |
| **M6** symmetric duplicate | **UNDERDETERMINED** ($|\Phi_A| = 2$); ROUTE-EXT certifies one fact *within* a chart | **UNDERDETERMINED** ($|\Phi_B| = 2$) | **GROUPOID-AMALGAM** (4 of the 8 inverse-consistent selections of 64 are coherent, 1 orbit, $\lvert\mathrm{Aut}\rvert = 2$ each, gauge moves them, gauge-closed) |
| **M7** accidental agreement *(added)* | **UNDERDETERMINED** ($|\Phi_A| = 2$), **NOT CERTIFIED** — the product extension has 16 positive entries | **ABSENT** ($|\Phi_B| = 0$) | **NO-INSTRUMENT** — no token edge |
| **M8** phase blindness *(added)* | **FORCED** with the declared list; **ABSENT** when a phase item is added | **NO-INSTRUMENT** | **NO-INSTRUMENT** — criterion test, no descent claim |
| **M9** detector validation *(added)* | **NO-INSTRUMENT** | **NO-INSTRUMENT** | **NO-DESCENT** (twisted / asymmetric / inverse-consistent partial-domain), SET-AMALGAM (consistent), **UNDERDETERMINED**, ABSENT-PAIR |

### The six mandatory controls, against what the pin demanded

1. **Relabelled same record — co-reference MUST succeed.** It does, forced, at
   both levels, with a set-level amalgam over three charts; and ROUTE-EXT
   fails under a *wrong* relabelling, so the certificate is not automatic. ✔
2. **Redundant copies — A succeeds, B fails.** Exactly, and B's failure is
   derived twice independently (leg structure; provenance filter). ✔
3. **Two-frame final outcomes — fact descent succeeds exactly where the final
   laws agree.** Biconditional over all 144 ordered pairs: 56 = 56, zero
   violations, carried on this material by items 1 and 3; broken at 26 pairs
   once items 2 and 4 are given something to say. ✔
4. **Intermediate frame content — must NOT be forced identical.** The shared
   record subalgebra at $t = 2$ is **derived** to be empty at every setting
   (0 shared partitions, against 2 at the final time); the intermediate
   propagators genuinely differ ($[270, 270, 432, 432, 108, 432]$ entries);
   a probability-preserving map exists — both marginals are uniform — and
   ROUTE-EXT refuses it at every setting, because at $t = 2$ the other wing's
   pointer is still in its ready state. ✔
5. **Record erasure — erased token $\ne$ "no event".** Historical counts
   $(1,1,0)$ against available $(1,0,0)$; the empty-scope comparison is
   reported VACUOUS rather than forced. ✔
6. **Symmetric duplicate — the honest outcome is groupoid.** The exchanging
   automorphism preserves the leg, the initial configuration, the Born shadow,
   **and all 784 four-cycle phase invariants** (0 violations, with the
   $\zeta_8$-perturbed control showing that the sweep can fail);
   $|\Phi_B| = 2$; GROUPOID-AMALGAM with one gauge orbit. ✔

---

## PHASE IS NOT A CRITERION — the rule, measured (M8)

W7's record-descent limit (W7 §23) exhibits a pair that carries a record
structure, whose cut-coherence tensor is fully diagonal, and whose composite
still carries a boundary-gauge phase invariant the tensor cannot see. W6 takes
that pair as two charts.

- every record-level datum agrees: both legs' Born shadows, both composites'
  Born shadows, and the record algebras themselves are **identical**;
- the four-cycle invariants of the two composites **differ** (anchored to
  `sec7_descent.py:242`);
- $|\Phi_A| = 1$ — fact co-reference succeeds and is FORCED;
- **the phase-consulting rule was built and run.** A sixth item comparing the
  charts' composite four-cycle invariants was added to the list and the
  $\varphi$-enumeration re-run: on this pair it returns **0** where the
  declared list returns **1**, and on a pair of charts differing by a
  configuration relabelling it returns **1**, so it is not indiscriminate.

The phase-consulting item constructed here returns 0 on this pair where the
declared list returns 1, and 1 on a relabelling pair — the category error the
pin names, measured on one pair.

M6 measures the same rule from the other side. The swapped build — the same
gates with the two target qubits exchanged — is **measured equal** to the
original, which is a real symmetry of the circuit and not a re-presentation of
it; the two CNOTs commute. The four-cycle invariants are then measured
$\sigma$-invariant: all 784, **0** violations. That this sweep can fail is
shown by running the identical sweep on a leg perturbed at a single entry by
$\zeta_8$ — a perturbation the Born shadow cannot see — where it reports **2**
violations; with the perturbation removed it reports 0.

---

## WHAT GROUNDS A TOKEN LABEL — the measurement, and the tension

The two-frame wing tie is broken by the declared generating structure. Which
*layer* of the declared data does the breaking is a question with an exact
answer, and it is not the comfortable one.

| layer tested against the wing exchange | symmetric? |
|---|---|
| the final record law | **yes, at all six settings** |
| the $j_0$ amplitude history, up to an overall sign | **yes at SP-E and SP-F** ($a = b$), no at the other four |
| the $j_0$ Born history | **yes at SP-E and SP-F**, no at the other four |
| the $j_0$ amplitude history on the nose | no, at every setting |
| the full declared legs (amplitude, up to sign, or Born) | no, at every setting |
| the legs restricted to the configurations reachable from $j_0$ at any time — sizes $(21,21,35,35,9,27)$ | no, at every setting and at every level |
| **the realized process** — each leg restricted to the configurations actually occupied *before and after it* | **yes at SP-E and SP-F**, up to sign and at the Born level |

**Two findings follow, and they point in different directions.**

**First, the base/fibre architecture is not violated — at the scope
measured.** The level at which the frame-isomorphism cuts the wing tie is the
**Born** level: matching the full declared legs by their Born shadows alone
already yields $|\Phi_B| = 1$ at every setting. Amplitude phases play no part;
the **structural provenance filter** (items 5+6) plays no part either, since
removing it changes nothing. What grounds the token label is **dynamical
provenance** — the declared generating dynamics, which is what the pin's
provenance list names first ("generating interaction", "local support"). On the
pin's own terms, matching charts by their declared legs is provenance in that
first sense, and it is legitimate.

*The scope of that adjudication, stated once and not exceeded.* The cut is
made at the Born level. On this model, at these six settings, on the declared
two-element permutation scope (eight on the extension), level-B token
identification is fixed by the legs' Born shadows alone; no amplitude phase and
no W7 invariant enters. Within that scope W6 finds no base/fibre violation.

**Second, a sharper tension takes its place.** Run the same level-B search on
the **realized** legs alone — each leg restricted to the configurations the
process actually occupies before and after it, which is all the model ever does
from its declared initial configuration. Those charts are built through the
ordinary constructor, so their occurrence, availability and law are recomputed
from the restricted legs rather than stipulated; all twelve come out with two
tokens, both available, and the full chart's law. Then:

- **the identity is inadmissible at all six settings.** The realized legs never
  admit it — not at the symmetric settings either. The two frames' time-2
  occupied supports never coincide (measured, at every setting; at SP-E they
  are even the same size and still different sets), which is frame-relativity
  and M4's own content seen from the support side;
- at the four asymmetric settings SP-A, SP-B, SP-C and SP-D **nothing**
  survives: no token map at all, at any matching level, so the realized data
  are silent;
- at **SP-E and SP-F exactly one** token map survives, up to sign and at the
  Born level — the **wing swap**, $R_A \leftrightarrow R_B$, which is the
  *opposite* of the identity the full declared legs force.

What blocks the wing swap on the full legs has been isolated, and it is one
leg: $U_{\text{prep}}$. On the $j_0$ column $w\,U_{\text{prep}}\,w$ is
$-U_{\text{prep}}$ — a match at the sign level, which is the level the search
uses. On the other **35** columns it is neither $+U_{\text{prep}}$ nor
$-U_{\text{prep}}$: 9 of them match the one sign, 8 the other, and no single
sign covers the block. Since $j_0$ is the only configuration the process ever
occupies at time 0, those 35 columns are transitions the process never takes.
The obvious deflation is ruled out: this is not an artifact of
$U_{\text{prep}}$'s arbitrary orthogonal completion, because the
time-independent reachable restriction — the natural way to strip that
completion — still breaks the symmetry at every setting and at every level, and
it does so by carrying the very same unrealized columns. It is the
*time-indexing* that makes the difference.

**The finding, with its exact scope.** *On the committed two-frame model the
realized process never admits the identity: at the four asymmetric settings it
admits no event-token identification at all, and at the two settings where the
measurement angles coincide (SP-E, $a = b = 0$; SP-F, $a = b = \pi/4$) it
admits exactly one, the wing swap — the opposite of the identification W6-B
forces on the full declared legs. What carries that identification is
counterfactual transition structure: $U_{\text{prep}}$'s columns on the 35
configurations the process never occupies.* This is a statement about this
model, this declared permutation scope (two elements after the $j_0$ filter,
eight on the declared extension) and these six settings; nothing is claimed
about nature.

The physically intended datum — the two wings are spatially separated — is not
part of the committed formal data. Paper 0 §5 already prices this under O4-A
("BC2 shows the current slice-indexed composite formalism does not provide that
rule"); W6 now measures where the gap bites and how wide it is.

---

## THE VERDICTS (pre-registered; combinable)

**W6-FACT-DESCENT — OBTAINS.** Shared record propositions glue. The fact level
supports a forced and certified identification on every relabelling pair (M1),
on the redundant-copy pair by *both* of the pin's routes (M2), and on the SP-A
frame pair — the one pair on which ROUTE-EXT is run — with the certificate
failing on a corrupted partner (M3). It is shown failing twice more: under a
wrong relabelling (M1), and on the SP-A/SP-C accidental pair (M7). Event-token identity is *not* everywhere determined by it — M6 leaves it
two-fold and M2 shows one fact on two occurrences — which is exactly the
outcome's clause.

**W6-SET-AMALGAM — OBTAINS, SCOPED.** A set-level amalgam arises in three
places, each measured: M1's three-chart relabelling family (1 coherent family,
trivial automorphisms, amalgam size 1, injective); M2 at the fact level; and
the token level of the committed two-frame atlas at **SP-A** extended by its
gauge relabelling (1 coherent family over 6 ordered edges and 6 triples,
amalgam size 2, injective) — the descent column is measured at that setting and
no other. **The scope is T5″-safe and stated as such:** the amalgam covers
**actual stable records only** — the positive-probability atoms of census §1 —
never unperformed measurements; it is not a global present, not a global
configuration history, and not a counterfactual value table. On the committed
twelve it is six disjoint two-chart components with no triple overlap. **And
one further scope clause, from the measurement above:** at SP-E and SP-F the
token-level amalgam is the one the *full declared* legs force, not the one the
realized process supports.

**W6-GROUPOID-AMALGAM — OBTAINS.** M6: two tokens exchanged by an automorphism
that preserves the leg exactly, the initial configuration, the Born shadow and
all 784 four-cycle invariants — the swapped build measured equal to the
original, and the sweep demonstrated able to fail under a $\zeta_8$
perturbation. $|\mathrm{Aut}| = 2$ per chart; the selection space is
enumerated and its size counted at **64**, of which 8 satisfy the inverse law
and 4 are coherent; the gauge acts, moves them, and $\Phi$ is closed under it
(all measured), giving 1 orbit. Any rule naming one of the two identifications
inserts structure no committed datum supplies — and the only rule that *would*
choose compares provenance strings by name. The committed model reaches the
same shape at its fact level on the real triple at SP-A (4 families, 1 orbit,
gauge moves them, closed).

**W6-UNDERDETERMINED — DOES NOT OBTAIN** as a descent outcome. The
discriminator returns UNDERDETERMINED at the *pair* level on committed material
(M3 at level A, M6 at both levels, M7 at level A), but at the descent level
every physical family here has a single gauge orbit: the competing
identifications are gauge-*equivalent*, which is why the honest object is a
groupoid rather than a plurality of inequivalent structures. Two inequivalent
orbits are realized only in the declared detector-validation branch.

**W6-NO-DESCENT — DOES NOT OBTAIN** on committed structures. It is realized in
M9's twisted, asymmetric and inverse-consistent partial-domain declarations,
and for the latter two which law does the rejecting is itself measured (2
inverse violations against 0 inverse and 6 triple). Three honest
qualifications: the committed atlas has no nonvacuous triple overlap, so it
could not have failed; M9's failures are properties of inconsistent
*declarations*, not of any chart; and M2's token-level atlas returns
ABSENT-PAIR, which is the pairwise maps failing to exist — a different thing
from triple coherence failing.

**W6-BLOCKED-AT-⟨referent⟩ — DOES NOT OBTAIN.** Every object typed; no new
postulate introduced.

---

## SCOPE AND NON-CLAIMS

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared gauge, and declared finite search scopes.
2. **The permutation scopes are declared, and their effective size is gated.**
   For the dimension 4, 8 and 16 models the frame-isomorphism search is
   **exhaustive** over all $4!$ resp. $8!$ configuration permutations. For the
   36-configuration composite model it runs over a declared **72**-element
   scope, of which the initial-configuration filter admits **exactly 2**; a
   declared **96**-element extension admits **8**. Every composite level-B
   negative is a negative at that scope and is labelled so where it is used.
3. **The amalgam covers actual stable records only** (T5″). Descent does not
   give a global present, does not give a value table, and what descends on the
   committed material is six disjoint two-chart components.
4. **Triple coherence is untested by the committed twelve**; the triple that is
   tested is the **SP-A** component extended by the declared gauge, built as a
   distinct object and reported as such. The descent column of M3 is a
   measurement at SP-A and at no other setting.
5. **W3′'s theorem is anchored, not re-proved**; W7's record-descent limit is
   anchored, not re-derived.
6. **M9's models are synthetic detector validations**, declared as such, and
   support no physical claim. So are the V2 and V4 variants of census §4, which
   exist to give items 2 and 4 something to reject.
7. **W6 does not treat unrecorded configurations.** The O4 fork's discriminator
   is not answered here.
8. Paper 0 v2.2 §6's non-claims stand unmodified.

---

## WHAT THIS UNIT HANDS OVER

- **To paper 0 §5.** The withdrawn global $(E,\prec)$ can be replaced by a
  *typed, derived* object at the recorded level: the co-reference groupoid of
  census §2, with $|\Phi|$ and its five-valued vocabulary as discriminator.
  What it earns is strictly less than an event set: six disjoint two-chart
  components on the committed material, covering actual stable records only.
- **To the O4 discriminator.** A sharpened question. At the *recorded* level
  the co-reference rule exists and is derivable from chart-local structure —
  but at the symmetric settings what derives it is declared structure the
  process never realizes — $U_{\text{prep}}$'s columns on the 35 configurations
  never occupied — and where the realized process speaks at all it points the
  other way. If the
  recorded level already needs counterfactual transition data to label its
  tokens, O4-A's demand for a covariant rule for *unrecorded* configurations is
  under more pressure, not less.
- **To v13's GW2 regional descent census.** The base is built: record algebras
  with computed occurrence and availability, a derived overlap object with a
  declared matching level, a preservation list every item of which is measured
  to bite on an exhibited pair, a five-valued discriminator with an emptiness
  guard, and a descent solver validated against four distinct ways of failing.
  The one thing v13 must supply that W6 could not find in the corpus is a
  family with a **nonvacuous triple overlap**.
- **To W7.** On this model, at these six settings, on the declared two-element
  permutation scope (eight on the extension), W6 finds no base/fibre violation.
  No fact-identity decision in this unit consults a phase invariant; the
  phase-consulting item M8 constructs returns 0 on that one pair where the
  declared list returns 1, and 1 on a relabelling pair; and the token-level
  grounding is measured to work at the Born level, so it does not reach into
  the fibre either.

---

## THE RECEIPT

`v12/code/w6_coreference_exact.py` → `v12/code/w6_output.txt`: **120 rows —
16 ANCHOR, 104 GATE — 120 pass, 0 fail, exit 0**, under 3 s, deterministic
across reruns modulo timings. The 16 anchors are exit-1-only and pin committed
lines in `sec4_records.py` (`:198`, `:199`, `:209`, `:505`, `:516`, `:524`,
`:632`–`:635`) and `sec7_descent.py` (`:137`, `:139`, `:239`–`:242`); the
falsification self-test — deliberately altering one anchor, and separately one
gate — exits 1 with a visible FAIL in both cases. No floats appear in any
substantive path, and none in any computed or expected receipt value.

**Gate discipline.** Every row is either an anchor or a measurement whose value
could have come out otherwise.

---

## ANTECEDENTS (cited, not claimed)

- **W3′** (LOG #14) — the record hypotheses (H-avail), (H-corr), the $O(n^2)$
  decision criterion, and the dim-4 eraser control. Anchored at
  `sec4_records.py:198`, `:199`, `:209`, `:632`–`:635`.
- **W7** (LOG #24, TERMINAL) — the cut-coherence tensor and the record-descent
  limit; its one-chart scope engraving is what makes co-reference this unit's.
  Anchored at `sec7_descent.py:137`, `:139`, `:239`–`:242`.
- **Paper 1 / the composite model** — the 36-configuration two-measurement
  two-frame model, `model_composite.py`; its orthogonality, commutation and
  frame declarations anchored at `sec4_records.py:505`, `:516`, `:524` and
  `model_composite.py:26-28`.
- **[GG]** gain graphs / switching classes (Zaslavsky) — the standard shape of
  the descent classification in §W6-C.
- **[B3]** Barandes — the chart notion the atlas postulate (T1) is built on.
- **[REV4]** — the external review whose §5–§11 is this unit's pin.
- Paper 0 v2.2 §5 — the four-gate rule, the withdrawn $(E,\prec)$, T5″, O4.
