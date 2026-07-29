# v12 W6 — RECORD CO-REFERENCE AND EFFECTIVE DESCENT

**Status:** GREEN-UNREVIEWED, 2026-07-29.
**Pin:** `v12/note-w6-record-coreference-pin.md` (STRICT, commit 2efd05e),
adopted from [REV4] at LOG #29–#30.
**Binding antecedents:** paper 0 v2.2 §5 (the four-gate rule; the withdrawn
global $(E,\prec)$; T5″); W7 TERMINAL (LOG #24 — its scope engraving: *all of
W7 is one-chart mathematics; the co-reference bridge is W6's*); W3′ (LOG #14 —
the record hypotheses and the decision criterion, anchored, not re-proved).
**Receipts:** `v12/code/w6_coreference_exact.py` → `v12/code/w6_output.txt`.
137 rows (16 ANCHOR, 121 GATE), 137 pass, 0 fail, runtime under 3 s.
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

> **Fact co-reference descends; event-token co-reference descends exactly
> where the chart's generating structure — not its record law — distinguishes
> the tokens; and where an automorphism of the committed data exchanges two
> tokens, the honest object is a groupoid, not a set.**

**Three** of the six pre-registered outcomes obtain, on disjoint parts of the
material: **W6-FACT-DESCENT**, **W6-SET-AMALGAM** (scoped) and
**W6-GROUPOID-AMALGAM**. The other three do not: neither **W6-NO-DESCENT** nor
**W6-UNDERDETERMINED** obtains on any physical family — both appear only in the
declared detector-validation branch, whose purpose is to prove the test can
fail — and **W6-BLOCKED-AT-⟨referent⟩** does not obtain either.

Three measurements carry most of the weight, and two of them cut against the
comfortable reading:

1. On the committed two-frame Bell model, a fact-candidate map exists on
   **exactly the 56 of 144** ordered chart pairs whose final laws agree — and
   **32 of those 56 are different experiments**. Value-and-probability
   agreement is not fact identity; the common-extension test is (§W6-A).
2. On the same model the fact level leaves a **two-fold** ambiguity at *every*
   setting — the wing exchange preserves the whole final law — and only the
   generating structure cuts it to one. **Provenance is not optional**
   (§W6-B).
3. **Disclosed against our own reading:** at the two symmetric settings the
   entire *stochastic* history from the initial configuration is wing-exchange
   symmetric. What breaks the tie there is an amplitude sign. At those
   settings the base's token labelling is fixed by fibre data (THE DISCLOSURE, below).

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
  support of the later leg lies in one sector.
- `v12/paper1_code/sec4_records.py:53` — `h_corr`, (H-corr): for every column
  of the writing leg the live alternatives lie in distinct sectors.
- `v12/paper1_code/sec4_records.py:62` — `merge_partition`, $M(U_2)$.
- `v12/paper1_code/sec4_records.py:81` — `criterion`, the decision procedure.
- `v12/paper1_code/sec4_records.py:176` — the declared dim-4 record
  `part = [0,1,0,1]`; `:198`, `:199` its two committed hypothesis values.

**W6's typing.** A **record token** $t$ = (a partition of the chart's
configurations, a declared **value** on each sector, the index of the leg that
writes it, a provenance tuple). Two status bits are *computed*, not
stipulated:

$$\textbf{occurred}(t) \;=\; \text{(H-corr) at the writing leg},\qquad
\textbf{available}(t)\;=\;\text{(H-avail) under the declared later legs}.$$

A chart's record tokens are exactly the candidates with `occurred = True`. The
**record algebra** $\mathcal{R}_a$ is the finite Boolean algebra on the
**actual** (positive-probability) value tuples of the chart's tokens, carrying
the exact joint law computed from the declared initial configuration.

**When the law is read.** At the time every token has been written — not at
the final time. For an *available* record the two agree, which is what
availability means, and the choice changes no measurement anywhere else in
this unit. For an *erased* token they do not: after erasure the later legs
have moved amplitude across the record sectors, so the final distribution is
not the record's law. Reading at the final time would make the erasure
control test the wrong thing.

*Gates.* `census/record algebra atoms` $=[(\texttt{0}),(\texttt{1})]$;
`census/record algebra law` $=[1/2,1/2]$; `census/record occurred` $=$ True;
`census/record available` $=$ True; anchors at `sec4_records.py:198`, `:199`.

**Why only actual values.** T5″ forbids inferring a global actuality object,
and the pin's W6-SET-AMALGAM clause restricts any amalgam to actual stable
records, never unperformed measurements. Zero-probability value tuples are
therefore not atoms. This is not cosmetic: at the two settings where the
singlet law is perfectly anticorrelated the algebra has **2** atoms, not 4, and
that is what makes the Boolean item of the preservation list bite
(`M3/list item 1 … (4, 2, 0)`).

### 2. The overlap object — CONSTRUCTED, and derived rather than postulated

The pin allows an overlap object to be declared. It does not have to be. Given
two charts, define a **frame-isomorphism** $\psi : b \to a$: a bijection of
configurations carrying $b$'s initial configuration to $a$'s, $b$'s leg
**multiset** to $a$'s under some matching, and each of $b$'s record partitions
to one of $a$'s. The **overlap object** is the set of token maps so induced.

*Four gates.*

- **Referent.** Definable from committed primitives only: the declared legs,
  the declared initial configuration, and the record partitions of census §1.
  No new
  primitive; no shared substrate is presupposed — a bijection is searched for,
  not assumed.
- **Necessity.** The withdrawn global $(E,\prec)$ presupposed cross-chart event
  identity (paper 0 §5). Something must supply it or the atlas has no bridge.
  Measured necessity: on the committed model the fact level admits **two**
  identifications at every setting and the overlap object cuts it to one
  (`M3/|Phi_A| exceeds |Phi_B| at every setting` = True).
- **No-smuggling.** The definition contains no cross-chart identity: it
  quantifies over bijections and keeps only those that carry one chart's own
  declared structure onto the other's. It cannot manufacture an identification
  where the structures differ — measured: **0** of the 120 cross-setting
  ordered pairs admit one.
- **Discriminator.** The count itself (census §6). A declared identification that the
  object does not return is an insertion; M9 exhibits a declaration whose
  triangle is inconsistent and the solver returns NO-DESCENT.

**The corpus's own declaration, reproduced.** `model_composite.py:26-28`
declares the two frames to be *"the same two local events in the two orders, on
one configuration space"*. The derived object reproduces exactly that
declaration and nothing more: at every setting the unique induced token map is
the identity (`M3/amplitude-level frame-isomorphism token maps, per setting`
$=[[(0,1)]]\times 6$), and the token-overlap graph on the twelve committed
charts has **6 components of size 2** — one per setting.

**The leg matching must be order-free**, and this is forced by the mandatory
controls, not chosen: two frames of one experiment differ *exactly* by the
order of two commuting legs. Measured: if leg order were required,
`M3/frame-isomorphisms if leg ORDER were required` $=[0,0,0,0,0,0]$ — the
committed model would have no frame-isomorphism at all and control 3 could not
be met at the token level.

### 3. The candidate co-reference map $\varphi_{ab}$ — CONSTRUCTED

$\varphi_{ab}$ is presented as a **token bijection** $\tau$ from $b$'s tokens
to $a$'s, extended to the unique Boolean isomorphism of the generated algebras.

*Four gates.*

- **Referent.** A map of finite Boolean algebras with state, availability and
  provenance; all four data are census §1's, all committed.
- **Necessity.** Fact identity cannot be read off values (two detectors may
  read $+1$ by accident — measured at M7), nor off provenance alone (redundant
  copies carry one fact on two tokens — measured at M2). A map with a
  preservation list is the minimal object that separates the two.
- **No-smuggling.** $\varphi$ is *not* allowed to be declared. It is
  enumerated: every token bijection is tested against the list and the survivors
  are counted. Nothing chooses among survivors.
- **Discriminator.** Census §6.

### 4. The preservation list — and where each item bites

Five of the six items are measured to reject a candidate that the other items
would pass. The sixth is disclosed as subsumed rather than claimed
independent.

| # | item | where the item rejects a candidate the other items would pass | receipt |
|---|---|---|---|
| 1 | Boolean operations / atom count | SP-A ← SP-E (4 atoms vs 2) | `M3/list item 1 … (4, 2, 0)` |
| 2 | definite record values | SP-E: the joint law *is* bijection-supported, but the bijection reverses values | `M4/ROUTE-EXT at SP-E …` $=$ (False, 2, True) |
| 3 | probabilities on the shared algebra | SP-A ← SP-B (same values, different law) | `M3/list item 3 … ` $=0$ |
| 4 | persistence / availability | the eraser against the preserving chart — isolated by a positive control: the two carry the *same* record law, and forcing availability equal turns the 0 into a 1 | `M5/|Phi_A(historical)| P<-E` $=0$; `M5/availability forced equal …` $=1$ |
| 5 | causal / process provenance | the two-frame wing tie; the redundant copies | `M3/|Phi_B| …` $=[1]\times 6$; `M2/|Phi_B|` $=0$ |
| 6 | original vs copy | **not a separate test** — carried by the frame-isomorphism, which preserves write-times; M2 exhibits the differing lineages that make its two tokens distinct occurrences, and the rejection there is effected by item 5 | `M2/lineage original vs copy` |

**PHASE IS NOT ON THE LIST.** No item consults an amplitude phase, a Bargmann
or Haagerup four-cycle product, or any W7 invariant. Control M8 measures the
consequence.

### 5. The declared gauge — CONSTRUCTED

The declared gauge is **configuration relabelling**: a chart may be presented
on any labelling of its configuration set. Coherence is judged modulo this and
nothing else. Measured: relabelling leaves the record algebra pointwise fixed
while genuinely changing the presentation — `M1/law invariant under relabelling`
$=$ (True, True) with `M1/legs actually differ` $=$ (True, True). Because the
gauge acts trivially on the base, the triple law is judged **on the nose**.

W7's boundary gauge (vertex switching on $\Gamma$; the K-vertex switching
seam torsor, W7 §14) is **not** in W6's gauge. It acts on the fibre.

### 6. The insertion-vs-co-reference discriminator — CONSTRUCTED

$$|\Phi_{ab}| = 0 \;\Rightarrow\; \textbf{absent};\qquad
|\Phi_{ab}| = 1 \;\Rightarrow\; \textbf{forced (genuine)};\qquad
|\Phi_{ab}| \ge 2 \;\Rightarrow\; \textbf{any named single map is inserted}.$$

This is GW1's kill inherited: a proposal that names one map where the data
admit several has added structure. All three values are realized in the table
below, and the third is realized on committed material (M3's fact level, M7).

### 7. Provenance — CONSTRUCTED, and then made derived

$$\mathrm{prov}(t) = (\text{generating interaction},\ \text{local support},\
\text{causal ancestry},\ \text{copying lineage},\ \text{erasure history}).$$

*Four gates.* **Referent** — every field is read off the chart's own declared
leg list. **Necessity** — measured twice: without it the two frames' wing
labels stay two-fold ambiguous, and the redundant copies collapse into one
token. **No-smuggling** — provenance is chart-local; it contains no
cross-chart identity, and the cross-chart part is supplied only by census §2's
search-derived overlap object. **Discriminator** — M2 (provenance differs, one
fact) against M5 (provenance survives erasure).

**The strengthening.** Rather than *comparing declared provenance strings*
across charts — which would be circular, since the labels are exactly what is
in question — W6-B admits only token maps **induced by a frame-isomorphism**.
Provenance is then preserved automatically, because $\psi$ carries the whole
generating structure. Nothing is compared by name.

### Census verdict

**PASSES.** Six objects typed: one LOCATED (census §1), five CONSTRUCTED from
committed primitives (census §2–§6), one primitive re-derived rather than
declared (census §7). No new postulate was needed. **W6-BLOCKED-AT-⟨referent⟩ does not
obtain.**

---

## W6-A — FACT CO-REFERENCE

**Definition.** Two local records carry the **same fact** iff a candidate map
exists *and* is certified by one of the pin's two routes:

- **ROUTE-EXT** — in a declared common record-preserving extension the two
  record variables are perfectly correlated **along the identity of values**:
  the joint law is supported on the graph of a value-preserving bijection.
- **ROUTE-WIT** — a specified common-record witness is perfectly correlated
  with both.

**The candidate level is not the criterion.** This is the unit's sharpest
negative and it is measured on committed material. Over the 144 ordered pairs
of the twelve committed charts:

| quantity | value |
|---|---|
| ordered pairs whose final laws agree | **56** |
| ordered pairs admitting a fact-candidate map | **56** (biconditional exact) |
| of those, pairs that are the *same* experiment | **24** |
| **accidental agreements** (different settings, identical law) | **32** |

The final-law classes have sizes $\{2,4,6\}$: the six settings collapse to
three laws, because the singlet law depends only on the product of the two
outcomes and on $\cos(a-b)$. SP-A, SP-C and SP-D are three different
experiments with one law. On the accidental pairs the only available common
extension is the product of two independent runs, and there the joint law has
**16** positive entries — not bijection-supported. ROUTE-EXT fails; the pairs
are not the same fact (`M7/ROUTE-EXT on the product extension` $=$
(False, False)).

**Where the certificate succeeds** it rests on a measured fact, not on a
construction: at a fixed setting the two frames assign **all 36** final
configurations the same probability (the final propagator is literally
identical in both frames), so reading the same configuration through either
frame's record map gives a diagonal joint law:
`M3/ROUTE-EXT same-setting frames` $=$ (True, 4, True).

**ROUTE-WIT** is exercised on a four-qubit three-copy model: the joint law is
$\{(0,0,0),(1,1,1)\}$ and the third token certifies the first two
(`M2/ROUTE-WIT t1 vs witness`, `t2 vs witness` both (True, 2, True)).

**Value preservation is load-bearing.** At SP-E the two wings' outcomes are
perfectly anticorrelated, so the joint law *is* supported on a bijection — but
a value-reversing one. "A's outcome is $+$" and "B's outcome is $-$" are
different facts even when perfectly anticorrelated, and the list rejects the
map: (False, 2, True).

---

## W6-B — EVENT-TOKEN CO-REFERENCE

**Definition.** Two tokens denote the **same occurrence** iff the token map is
induced by a frame-isomorphism (census §2). Provenance — generating interaction,
local support, causal ancestry, copying lineage, erasure history — is then
carried, not compared by name.

**Measured separation from W6-A.**

- **Redundant copies (M2).** One process writes the same alternative twice, at
  two different legs. The two charts have *identical* record laws and
  ROUTE-EXT certifies one fact — yet $|\Phi_B| = 0$: no bijection of
  configurations carries the second copy's partition onto the first's while
  fixing the leg multiset. One fact, two occurrences. This is exactly the
  pin's mandated outcome for control 2, and it is **derived**, not stipulated.
  *The negative is not an empty search.* Positive control: the same search
  returns the identity on each chart against itself; and the register swap
  **does** carry the second copy's partition onto the first's while **not**
  fixing the leg multiset. The leg structure — the temporal and causal
  decomposition — is precisely what refuses the identification.
- **The two-frame wing tie (M3).** $|\Phi_A| = 2$ at every setting: the final
  law is invariant under exchanging the two wings (it depends only on the
  product of outcomes). $|\Phi_B| = 1$ at every setting. The generating
  structure — which leg wrote which pointer, on which local support — is what
  cuts two to one.
- **Erasure (M5).** Occurrence and availability are different predicates and
  the formalism keeps them apart. Three charts: preserving, erased, and one
  where the record was never written. Historical token counts $(1,1,0)$;
  available token counts $(1,0,0)$. The erased token is **not** identified with
  "no event": $|\Phi_B(\text{historical})|$ for erased ← never-written $=0$.
  The available algebras of those two charts are both trivial, so at the
  availability level the comparison is *vacuous* — and that is precisely why
  the historical level must exist. The preserving and erased charts carry the
  **same record law**, and forcing their availability bits equal turns
  $|\Phi_A(\text{historical})| = 0$ into $1$: availability, and nothing else,
  is what separates them.

**What W6-B is not.** It does not deliver a co-reference rule for *unrecorded*
configurations. That is O4-A's price (paper 0 §5) and remains open; WHAT THIS
UNIT HANDS OVER, below, states what this unit hands to it.

---

## W6-C — EFFECTIVE DESCENT

**The coherence laws.** $\varphi_{aa} = \mathrm{id}$;
$\varphi_{ba} = \varphi_{ab}^{-1}$;
$\varphi_{ab}\circ\varphi_{bc} = \varphi_{ac}$ on triple overlaps, modulo the
declared gauge only — which, by census §5, is trivial on the base.

**The solver.** Enumerate every selection of one $\varphi$ per edge; keep the
selections satisfying every triple law (**coherent families**); act on them by
$\prod_x \mathrm{Aut}(x)$ via
$(g\cdot\varphi)_{xy} = g_x\circ\varphi_{xy}\circ g_y^{-1}$; count orbits;
build the colimit and check each chart injects. The classification:

| condition | verdict |
|---|---|
| some $\Phi_{ab} = \emptyset$ | ABSENT-PAIR |
| no coherent family | **W6-NO-DESCENT** |
| one family, all $\mathrm{Aut}$ trivial | **W6-SET-AMALGAM** |
| one gauge orbit, some $\mathrm{Aut}$ nontrivial | **W6-GROUPOID-AMALGAM** |
| several gauge orbits | **W6-UNDERDETERMINED** |

This is the standard shape for a groupoid-valued gain graph — cycle holonomy
modulo vertex switching — cited from [GG] (Zaslavsky; paper 0's reference
list), not claimed as ours; the gain group here is the symmetric group of
record tokens rather than $U(1)$.

**Two soundness properties of the solver are gated, not assumed.** The
coherence law $\varphi_{ba} = \varphi_{ab}^{-1}$ is imposed by construction, so
it must be checked that the inverse is itself admissible: the preservation list
is symmetric and every $\Phi$ set is inverse-closed (M1, M6). And
$\varphi_{aa} = \mathrm{id}$ requires the identity to lie in every
automorphism set — it does (M1, M6). Where $|\mathrm{Aut}| > 1$ the identity is
a *member* of $\Phi_{aa}$ but not its only member; that is the groupoid case,
reported as such.

**All five branches are exercised**, so no branch is untested:
SET-AMALGAM (M1, M2, M3-B, M9-consistent), GROUPOID-AMALGAM (M6,
M3-A), NO-DESCENT (M9-twisted, 0 coherent families), UNDERDETERMINED
(M9's two-family / trivial-automorphism instance, orbits $=2$), ABSENT-PAIR
(M9's empty $\Phi$).

**The scope limit, stated plainly.** The committed atlas contains **no
nonvacuous triple overlap**: the token-overlap graph on the twelve committed
charts is 6 components of size 2 (`M3/committed charts in a nonvacuous triple
overlap` $= 0$). Triple coherence is therefore **untested by committed
structures**; every triple-level result below is carried by a constructed
family. The committed material decides pairwise descent only.

**Disclosed:** the "committed triple" of the descent table is
$\{F_1, F_2, F_2^\pi\}$ — the third chart is $F_2$ presented on a relabelled
configuration set. Because the declared gauge acts trivially on the record
algebra (census §5), its record data *are* $F_2$'s. That triple therefore
tests the triple law against the gauge, not against a third independent
experiment, and it is reported as such. The corpus contains no third chart
that would do better.

**M9 is a detector, not a physics claim.** Its twisted declaration pins two
edges to the identity and the third to the transposition — each a legitimate
member of its own $\Phi$ set — and the triangle has holonomy. The solver
returns NO-DESCENT with 0 coherent families; the *same three charts* under the
consistent declaration return SET-AMALGAM. What this shows is that the triple
law has power and that descent is a property of the identification system, not
of the charts separately. It is not evidence that any committed atlas fails to
descend.

---

## THE DESCENT TABLE

Every cell is carried by an exact model and by at least one gate.

| model | A (fact) | B (event token) | C (effective descent) |
|---|---|---|---|
| **M1** relabelled same record | SUCCEEDS-FORCED $|\Phi_A|=1$ | SUCCEEDS-FORCED $|\Phi_B|=1$ | **SET-AMALGAM** (1 family, 1 orbit, 6 triples, amalgam size 1, injective) |
| **M2** redundant copies | SUCCEEDS-FORCED, ROUTE-EXT **and** ROUTE-WIT | **FAILS-ABSENT** $|\Phi_B|=0$ | SET-AMALGAM at the fact level; the token level has no edges |
| **M3** two-frame final outcomes | SUCCEEDS, $|\Phi_A|=2$ (wing tie); candidate map on exactly 56/144 | SUCCEEDS-FORCED $|\Phi_B|=1$ at all six settings | **SET-AMALGAM** at level B (amalgam size 2, injective); **GROUPOID-AMALGAM** at level A (4 families, 1 orbit) |
| **M4** intermediate frame content | NOT FORCED — overlap subalgebra trivial; a probability-preserving map exists and is rejected | FAILS-ABSENT | vacuous (no shared written token) |
| **M5** record erasure | availability split: vacuous at the available level, $0$ at the historical level | FAILS-ABSENT $|\Phi_B|=0$ | not applicable (no triple) |
| **M6** symmetric duplicate | SUCCEEDS-FORCED (one fact) | **UNDERDETERMINED** $|\Phi_B|=2$ | **GROUPOID-AMALGAM** (4 of 8 selections coherent, 1 orbit, $|\mathrm{Aut}|=2$ each) |
| **M7** accidental agreement *(added)* | **FAILS ROUTE-EXT** though $|\Phi_A|=2$ | FAILS-ABSENT | not applicable |
| **M8** phase blindness *(added)* | SUCCEEDS-FORCED $|\Phi_A|=1$; a phase-consulting map returns 0 | not applicable | not applicable (criterion test) |
| **M9** detector validation *(added)* | not applicable | not applicable | **NO-DESCENT** (twisted) / SET-AMALGAM (consistent) / UNDERDETERMINED / ABSENT-PAIR |

### The six mandatory controls, against what the pin demanded

1. **Relabelled same record — co-reference MUST succeed.** It does, forced, at
   both levels, with a set-level amalgam over three charts. ✔
2. **Redundant copies — A succeeds, B fails.** Exactly, and B's failure is
   derived from the leg structure rather than declared. ✔
3. **Two-frame final outcomes — fact descent succeeds exactly where the final
   laws agree.** Biconditional over all 144 ordered pairs: 56 = 56, no
   exceptions. ✔
4. **Intermediate frame content — must NOT be forced identical.** The overlap
   subalgebra at the intermediate slice is trivial at every setting, and the
   intermediate propagators genuinely differ ($[270, 270, 432, 432, 108, 432]$
   entries). A probability-preserving map exists — both marginals are uniform —
   and is rejected. Frame-relativity respected. ✔
5. **Record erasure — erased token $\neq$ "no event".** Historical counts
   $(1,1,0)$ against available counts $(1,0,0)$. ✔
6. **Symmetric duplicate — the honest outcome is groupoid.** The exchanging
   automorphism preserves the leg exactly, the initial configuration, the Born
   shadow, **and all 784 four-cycle phase invariants** (0 violations). No
   invariant rule may choose; $|\Phi_B| = 2$; the descent verdict is
   GROUPOID-AMALGAM with one gauge orbit. ✔

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
- $|\Phi_A| = 1$ — fact co-reference succeeds and is forced;
- had phase been on the preservation list, $|\Phi_A|$ would be **0**.

A phase-consulting fact criterion therefore returns *absent* exactly where the
record level returns *forced*. That is the category error the pin names, and
it is now measured rather than asserted. **Architecture confirmed at the base:
W6 builds the base of shared record referents; W7's loop data are the fibre.**

---

## WHAT GROUNDS A TOKEN LABEL — the disclosure

The two-frame wing tie is broken by the generating structure. It is worth
asking *which layer of the committed data* does the breaking, and the answer
is not the comfortable one. Testing the wing-exchange permutation against
nested layers of the committed model:

| layer | wing exchange is a symmetry? |
|---|---|
| the final record law | **yes, at every one of the six settings** |
| the whole Born-level history from the initial configuration | **yes at SP-E and SP-F** ($a = b$), no at the other four |
| the amplitude-level history from the initial configuration | no, at every setting |
| the full declared legs (amplitude or Born) | no, at every setting |
| the legs restricted to the reachable configurations | no, at every setting — reachable sizes $(21,21,35,35,9,27)$, one isomorphism each |

**The disclosure.** At the two symmetric settings, every *stochastic* datum of
the committed model — the entire Born-level history from the declared initial
configuration, and the final record law — is invariant under exchanging the two
wings. What breaks the tie there is the singlet's antisymmetry, an **amplitude
sign**, together with leg data off the initial column.

This does not violate the phase rule: a real amplitude sign is not a phase
invariant, and it is used to fix a *token label*, never to decide fact
identity. But it is a genuine tension with the clean base/fibre separation,
and it is the unit's own result against its own preferred reading: **at the
symmetric settings the base's event-token labelling is not fixed by base-level
data.** The reachable-subprocess control rules out the obvious deflation — the
groundedness is not an artifact of `U_prep`'s arbitrary orthogonal completion,
since restricting every leg to the configurations reachable from $j_0$ leaves
exactly one isomorphism at every setting.

The physically intended datum — the two wings are spatially separated — is not
part of the committed formal data at all. Paper 0 §5 already prices this under
O4-A ("BC2 shows the current slice-indexed composite formalism does not provide
that rule"); W6 now measures where the gap bites and how wide it is.

---

## THE VERDICTS (pre-registered; combinable)

**W6-FACT-DESCENT — OBTAINS.** Shared record propositions glue. The fact
level supports a forced identification on every relabelling pair (M1), on the
redundant-copy pair by both of the pin's routes (M2), and on every
same-experiment frame pair (M3); the fact-level triple law holds on the
constructed families, with a set-level colimit into which every chart injects.
Event-token identity is *not* everywhere determined by it — M6 leaves it
two-fold, and M2 shows one fact on two occurrences — which is exactly the
outcome's clause.

**W6-SET-AMALGAM — OBTAINS, SCOPED.** Where the committed generating
structure distinguishes the tokens, co-reference is unique and the stable
record tokens form a set-level atlas object: M1's three-chart family (amalgam
size 1, injective), M2 at the fact level, and each of the six components of the
committed two-frame atlas (amalgam size 2, injective). **The scope is
T5″-safe and stated as such:** the amalgam covers **actual stable records
only** — the positive-probability atoms of census §1 — never unperformed
measurements; it is not a global present, not a global configuration history,
and not a counterfactual value table. It is six disjoint two-chart components,
not one global object; the committed atlas has no triple overlap to glue
across.

**W6-GROUPOID-AMALGAM — OBTAINS.** M6: two tokens exchanged by an
automorphism that preserves the leg exactly, the initial configuration, the
Born shadow and all 784 four-cycle phase invariants. $|\mathrm{Aut}| = 2$ per
chart; 4 of 8 selections are coherent; the gauge acts transitively (1 orbit).
The actuality object there is a groupoid, and any rule naming one of the two
identifications inserts structure no committed datum supplies. The committed
model reaches the same shape at its fact level (M3: 4 families, 1 orbit).

**W6-UNDERDETERMINED — DOES NOT OBTAIN** on any committed or constructed
physical family. It is realized only in the declared detector-validation
branch (two coherent families with trivial automorphisms, 2 orbits), whose
purpose is to prove the classification's fourth branch reachable.

**W6-NO-DESCENT — DOES NOT OBTAIN** on committed structures. It is realized
in M9's twisted declaration (0 coherent families). Two honest qualifications:
the committed atlas has no nonvacuous triple overlap, so it could not have
failed; and M9's failure is a property of an inconsistent *declaration*, not of
any chart.

**W6-BLOCKED-AT-⟨referent⟩ — DOES NOT OBTAIN.** Every object typed; no new
postulate introduced.

---

## SCOPE AND NON-CLAIMS

1. **No claim about nature.** Every result is a statement about declared
   finite models, a declared gauge, and declared finite search scopes.
2. **The permutation scopes are declared.** For the dimension 4 and 8 models
   the frame-isomorphism search is **exhaustive** over all $4!$ resp. $8!$
   configuration permutations. For the 36-configuration composite model it
   runs over a **declared 72-element** scope (wing exchange × pointer 3-cycles
   on each wing × the two qubit flips). Negatives there are negatives at that
   scope, and are labelled so wherever they are used.
3. **The amalgam covers actual stable records only** (T5″). Descent does not
   give a global present; it does not give a value table; and what descends
   here is six disjoint two-chart components.
4. **Triple coherence is untested by committed structures** — no committed
   triple overlap exists. All triple-level verdicts rest on constructed
   families.
5. **W3′'s theorem is anchored, not re-proved**; its hypotheses are sufficient
   and never necessary, its own engraving carried. W7's record-descent limit
   is anchored, not re-derived.
6. **M9's models are synthetic detector validations**, declared as such, and
   support no physical claim.
7. **W6 does not treat unrecorded configurations.** The O4 fork's
   discriminator — *does a covariant co-reference structure for unrecorded
   local configurations exist?* — is not answered here.
8. Paper 0 v2.2 §6's non-claims stand unmodified.

---

## WHAT THIS UNIT HANDS OVER

- **To paper 0 §5.** The withdrawn global $(E,\prec)$ can now be replaced by a
  *typed, derived* object at the recorded level: the co-reference groupoid of
  census §2, with $|\Phi|$ as its discriminator. What it earns is strictly less than
  an event set: six disjoint two-chart components on the committed material,
  covering actual stable records only. The four gates for it are written out
  in census §2 and census §7 above.
- **To the O4 discriminator (queued next).** A sharpened question. W6 shows
  that at the *recorded* level the co-reference rule exists and is derivable
  from chart-local structure — except at the symmetric settings, where the
  stochastic layer alone underdetermines it and an amplitude sign decides. If
  the recorded level already needs fibre data to label its tokens, O4-A's
  demand for a covariant rule for *unrecorded* configurations is under more
  pressure, not less.
- **To v13's GW2 regional descent census.** The base is built: record
  algebras, a derived overlap object, a six-item preservation list five of
  whose items are measured to bite independently (the sixth disclosed as
  subsumed), and a five-branch descent classification with all five branches
  exercised. The one thing v13 must supply that W6 could not
  find in the corpus is a family with a **nonvacuous triple overlap**.
- **To W7.** The architecture holds at the base: no fact-identity decision in
  this unit consults a phase invariant, and M8 measures that a criterion which
  did would return *absent* exactly where the record level returns *forced*.

---

## ANTECEDENTS (cited, not claimed)

- **W3′** (LOG #14) — the record hypotheses (H-avail), (H-corr), the
  $O(n^2)$ decision criterion, and the dim-4 eraser control. Anchored here at
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
