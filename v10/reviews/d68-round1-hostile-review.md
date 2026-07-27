# D68 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-27.
**Unit under review:** D68 "the functional slot" —
`note-d68-functional-slot-pin.md` (STRICT, committed at `2e83abf`, before the
receipt), `note-d68-functional-slot-result.md` (GREEN-UNREVIEWED),
`code/d68_functional_slot_exact.py` + `data/d68_functional_slot_exact.out`
(25 PASS / 0 FAIL, exit 0), LOG #479 (`b866c97`).
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`base.py`, `layer.py`, `sys_.py`, `run1.py`, `run2.py`,
`geo.py`, `med.py`, `medwit.py`, `forced.py`, `gauge.py`, `symcheck2.py`,
`gaugedim.py`, `wit.py`, `ctrl.py`, `diag.py`, `meas.py`, `meas2.py`,
`c5.py`, `d6.py`, `d6s.py`, `d6c4.py`, scratch under
`/private/tmp/claude-501/.../scratchpad/d68rev/`): my own breadth-first family
enumerator, my own record grouping, **my own σ normal form** (nested sorted
tuples, no `repr` serialisation, no d44a port), my own state closure, my own
transfer operator, my own `Ẑ`/`μ_Ẑ`, my own label-map group, my own
constraint rows (built over *ordered* index pairs and then folded onto
symmetric/antisymmetric coordinates — a different normal form from the unit's
canonical-pair-key emission), my own sparse elimination **pivoting on the
largest column** (the unit pivots on the smallest), and a coherence dimension
computed by the identity `dim(W ∩ span COH) = rank(W) − rank(W minus the COH
columns)` (the unit counts pivots in a COH-last block). The only object I
share with the unit is the layer under test (`d42b3`'s `candidates_for` /
`admissible` / `event_poset` / `View` / `triples` / `vname` / `canon` / `V0`).
Calibration: `reviews/d65-round1-hostile-review.md` + its DELTA,
`reviews/d67-round1-hostile-review.md` header + DELTA; paper 29 §3–§5;
`note-d65-descent-conditions-result.md`.

**VERDICT: REVISE. 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT.**

**The arithmetic is flawless. Every single number reproduces.** From my own
instrument: the census `[1, 6, 32, 176, 976, 5280, 27904]` = 34,375; the
record-class census `[1, 6, 23, 84, 313, 1138, 3983]` = **5,548**; 36 σ
states; `dim ker(T − 2I) = 1` with a strictly positive generator taking
`{1: 29, 4/3: 5, 7/3: 2}`; `μ_Ẑ` strictly positive, constant on all 5,548
classes, marginal-consistent at every one of the 6,471 interior histories,
probability mass 1 on every cut; the four label maps with the fixed-point
census (`vflip` fixes 127, `swap` fixes 1); **the entire 32-row dimension
table** at depths 2, 3, 4 and 5 (every `vars/rows-rank/dim/coh/cohdim` and
every `asym` column, including the full-chain split `166` vs `163` at depth
4), and at depth 6 the block reading both ways (`172922/70850/102072`,
`145018/79168`; `43439/17861/25578`, `36447/19847`) and the sum reading both
ways (`389330560/5121/389325439`; `97343616/1292/97342324`); all 65,850
depth-6 off-block rows singletons; the geography counts
`0 / 50 / 744 / 8,074 / 79,168` and their complements
`9 / 84 / 747 / 6,984 / 65,850`; F1(b)'s `73,674` and `88,036`; F1(c)'s zero;
the pinned witness (0 residual against all 594 of *my* rows, strictly
diagonally dominant, minor `5183/67108864`); the F5 controls (`μ_Ẑ`
attainable everywhere, block rejects 23/23 and 84/84, sum/C4-off rejects
0 with rank = rows, sum/C4-on rejects 22/23 and 84/84); F5(b)'s `4/70/588`
and `0/17/146`. The receipt reruns 25 PASS / 0 FAIL, exit 0, identical modulo
embedded timings at `PYTHONHASHSEED` default / 7 / 12345, and the note's
unreceipted `1.36 GB` is real (`peak memory footprint 1,364,005,544` under
`/usr/bin/time -l`; 133.8 s real on my machine).

**The BLOCKER is the operationalization, and it is the target the pin's own
residue 2 half-identifies.** Paper 29 §4.3's load-bearing hypothesis is
*decoherence of the queried record algebra*, i.e. of the **coarse-grained**
functional `D̄(r,r') = Σ_{h∈r, h'∈r'} D(h,h')`. The unit computed the two
readings that bracket that condition and skipped the condition itself: the
**sum** reading imposes only `D̄(r,r) = μ(r)` and never asks the algebra to
decohere at all; the **block** reading imposes vanishing **entry by entry at
the fine level**, which is strictly stronger than `D̄(r,r') = 0`. I computed
the faithful middle reading. Under it, **at every depth, in every C4/C3
variant, `cohdim = coh` — no within-class coherence is forced anywhere**;
the depth-2 F-II cell evaporates (`9/9` free, not `0/9`); an exact PSD member
carries coherence between two histories whose **parents carry different
records** — the entries the unit's headline says are "killed by a singleton
row"; and the constraint rank on the **antisymmetric block is 3,739, not
zero**. The sharpest sentence of the deliverable — *the record instrument is
the exact boundary of permitted coherence* — and its companion — *records
cannot see a phase* — are both artifacts of the two conventions chosen, and
both reverse under the one paper 29 actually states.

---

## BLOCKER 1 — neither C1 reading is paper 29's decoherence condition; the faithful reading reverses the coherence geography *and* phase blindness

**Where.** Pin §1 C1 (both readings); note title, §1 bullet 1, §2 tables, §3
(the whole coherence geography), §3.1, §5 licensed claims 3, 4, 5, 6; the
receipt's printed verdict block; LOG #479's title and the sentences "**the
record instrument is the exact boundary of permitted coherence**" and "**a
record measure of this shape cannot see a phase**".

**Defect.** Paper 29 §4.3 lists five load-bearing hypotheses; number 2 is
"**decoherence of the queried record algebra**", and §3.1 supplies the
pushforward `(q_*μ)(ω̄) = Σ_{q(ω)=ω̄} μ(ω)` for the atom masses. Written on
the fine layer, that pair of demands is exactly

```
    D̄(r,r')  =  Σ_{h∈r, h'∈r'} D(h,h')  =  δ_{rr'} · μ_Ẑ(r)          (C1-coarse)
```

— the coarse-grained functional on the record algebra is diagonal and its
diagonal is the record measure. This is medium decoherence in the ordinary
consistent-histories sense, and it is the condition that licenses a scalar
probability for a record class.

Neither of the unit's readings is that condition, and they fail it in
opposite directions:

* **sum** keeps only the `r = r'` half. It never asks the queried algebra to
  decohere, so by §4.3's own bookkeeping the object it constrains is one for
  which no scalar record probability is licensed at all. "Coherence is priced
  at zero under the sum reading" is therefore a statement about the wrong
  object — and its `10⁸`-dimensional solution spaces are exactly what a
  no-decoherence demand should produce.
* **block** demands `D(h,h') = 0` for every *fine* pair with
  `record(h) ≠ record(h')`. That implies C1-coarse but is far stronger: it
  forbids the cancellations that coarse decoherence explicitly permits. The
  entire §3 mechanism (a "SINGLETON" off-block row, "no cancellation, no
  conspiracy") exists **because** the convention removed the possibility of
  cancellation by hand, one level down, before the row was written.

So the unit's answer to its own sharpest question is bracketed by two
conventions and never evaluated at the condition in between.

**Recomputation (mine).** `medium` = C1-coarse at depth `D`, and C3 = "the
restricted form satisfies C1-coarse at depth `D−1`" (one-step and
full-chain), same variables as `sum`, same elimination:

```
  D  C4    C3    | vars    rows  rank   dim   | coh  cohdim | asym  arank  acohdim
  2  off   one   |   528    297   296    232  |   9      9  |  496    268       9
  2  off   full  |   528    298   296    232  |   9      9  |  496    268       9
  2  on    one   |   146    297    88     58  |   4      4  |  114     60       1
  3  off   one   | 15576   3846  3845  11731  | 134    134  |15400   3739     134
  3  off   full  | 15576   3868  3865  11711  | 134    134  |15400   3754     134
  3  on    one   |  3968   3846  1006   2962  |  35     35  | 3792    900      35
  3  on    full  |  3968   3868  1013   2955  |  35     35  | 3792    902      35
```

Three things die here.

1. **The geography.** `cohdim = coh` at every depth and in every variant: the
   record demand, read as paper 29 states it, forces **no** within-class
   coherence to zero — not the ones with different parent records, not any.
   The identity "cohdim = the parents-record-identical count" is a property of
   the block convention, not of the record instrument.
2. **The one F-II cell.** At depth 2 the medium reading leaves `9/9` (C4 off)
   and `4/4` (C4 on) coherence free. "F-II fires at depth 2, and only there"
   is "F-II fires under the block reading at depth 2".
3. **Phase blindness.** The medium rows have *asymmetric* index supports
   (`r × r'` with `r ≠ r'`), so they see the antisymmetric part: constraint
   rank **268** at depth 2 and **3,739** at depth 3, against the sum
   reading's zero. A record demand of paper 29's shape sees a phase.

And the forbidden entries are explicitly realisable. At depth 3, medium,
C4 off, one-step, an exact member built by perturbing `diag(μ_Ẑ)` along a
kernel direction (support 16, scale `t = 1/81920` derived as the unit derives
it) has **zero residual against every row** and is positive definite by
strict diagonal dominance over `Q`, with

```
  h  = ( ('p','A',v0,0), ('r','A',{(A,v0,0)},{(A,v0,0)}), ('p','B',v0,0) )
  h' = ( ('p','A',v0,0), ('p','B',v0,0), ('r','A',{(A,v0,0)},{(A,v0,0)}) )
  record(h) = record(h'),  mu = 3/8192 each
  record(parent h) != record(parent h')        <-- the unit's "forced to 0"
  D(h,h') = 1/81920 != 0
```

The full-chain variant gives the same member at `t = 1/98304`. This is the
unit's own §3 display with the verdict inverted: the two parents *are*
distinguishable at the previous cut, and the coherence survives anyway.

**What I am not saying.** F2 stands: `diag(μ_Ẑ)` satisfies C1-coarse too, so
F-I and F-IV remain excluded and the medium reading is a genuine third data
column, not a wall. The dimension is genuinely priced there (rank 296 of 528
at depth 2 against the sum reading's 29), so the medium reading is also the
only one of the three whose *dimension* is informative. **The repair is to
run it and re-derive §3, §5.3–§5.6 and the LOG headline from it** — not to
delete the two bracketing columns, which are worth keeping as bounds.

---

## MAJOR 1 — "records cannot see a phase" is a one-line theorem about row supports, true of any partition and any measure, and false as soon as any other paper-29 demand is switched on

**Where.** Note §3.1 and its title clause, licensed claim 6, receipt gate
F4(e) and the printed verdict ("A record measure cannot see a phase, so no
amount of C1/C3 can select one"), LOG #479 title ("RECORDS CANNOT SEE A
PHASE").

**Defect.** Let `D = S + iA` with `S` symmetric and `A` antisymmetric. Any
linear row whose coefficient function `c(i,j)` satisfies `c(i,j) = c(j,i)`
annihilates `A` identically, because `Σ c_ij A_ij = 0` term by transposed
term. **Every** sum-reading row is `Σ_{(i,j) ∈ C × C} D(i,j)` for a set `C`
— a product set, hence swap-symmetric by construction. Therefore the
constraint rank on the antisymmetric block is zero **at every depth, for any
record partition, for any measure, on any layer, without computing
anything**. The receipt's F4(e) verifies a tautology of the constraint shape;
it carries no information about records, about `μ_Ẑ`, or about this layer.

The note's own §3.1 states the mechanism ("every C1 and C3 row in the sum
reading is a sum over a **symmetric** set of index pairs") — the disclosure is
there — and then the licensed claim and both headline surfaces sell it as a
finding about record measures.

It is also false the moment any other demand in the pin's own list is
switched on:

* **C2 (strong positivity), which is a pinned constraint,** does see `A`:
  positive semidefiniteness of a Hermitian matrix bounds `|A_ij|²` by
  `D_ii D_jj − S_ij²`. The linear system is phase-blind; the constraint set
  C1–C4 is not.
* **C1-coarse** (BLOCKER 1) has asymmetric supports and constrains `A` with
  rank 268 / 3,739 at depths 2 / 3.
* Even inside the unit, the **block** reading's off-block rows have
  asymmetric support and see `A` exactly (rank 84 at depth 3) — which is why
  the unit's own `acohdim` column tracks the real one.

**Recomputation (mine).** The lemma needs none; I confirmed the two positive
statements above by computing the antisymmetric rank of the medium system
(268, 3739, 3754) and by exhibiting `[[1, i], [−i, 1]] ⪰ 0` as the standing
counterexample to any reading of "cannot see a phase" that includes C2.

**Repair.** Demote F4(e) to a stated lemma ("all sum-reading rows have
swap-symmetric support, hence rank 0 on `A` — no computation required"), and
delete or re-scope every sentence of the form "a record measure cannot see a
phase". The honest sentence is: *the linear part of the two chosen readings
cannot see a phase because both were built out of product-set sums.*

---

## MAJOR 2 — the entire dimension/geography result is measure-independent: `μ_Ẑ` is used nowhere in F2/F3/F4, and existence holds for any positive cut-consistent weight

**Where.** Note title ("**what quantum layers does the generated law
admit?**"), §1 (the `μ_Ẑ` recomputation and its normalisation paragraph),
F0(g)/F0(h) as anchors, licensed claim 1 ("**the generated law** admits a
paper-29-shaped functional level"), LOG #479 ("the space of paper-29-shaped
functionals **over the generated law**").

**Defect.** Every coefficient in every row of every configuration is `0` or
`1`. `μ_Ẑ` appears **only** on the right-hand side. Rank, dimension,
coherence dimension, the singleton census, the antisymmetric ranks and the
whole 32-row table are therefore functions of exactly three combinatorial
objects — the truncated history tree, `canon`'s partition at depths `D` and
`D−1`, and the prefix map — and of **nothing** the generated law contributes.
D49's `λ = 2` completion and D65's descent (the two facts F0(g)/F0(h) work
hard to re-gate, and the reason `μ_Ẑ` is the corpus's distinguished measure)
are load-bearing for **no number in §2 or §3**.

Existence is weaker still. `diag(w)` satisfies C1 (both readings), C3 (both
readings) and C4 for **any** strictly positive weight `w` whose cylinder
marginals are consistent — record-constancy is not needed either, because the
C1 right-hand side is the *class mass* of whatever measure is supplied.

**Recomputation (mine).** I built a second measure with none of `μ_Ẑ`'s
distinguishing properties: `ν(h) = Π_k 1/|menu|` (uniform on each menu).
`ν` is strictly positive, exactly marginal-consistent (0 violations), a
probability measure on every cut, and **not** record-constant (4,156 of the
5,548 classes carry two or more `ν` values); it differs from `μ_Ẑ` on 34,374
of 34,375 histories. Running the unit's F2 with `ν`:

```
  classical diagonal member diag(nu), depths 2/3/4, conv in {sum, block,
  medium}, chain in {one, full}:   rows checked 148,290 — rows violated 0
```

and the dimension table is *identical*, because the coefficient matrix never
saw either measure.

**Consequence.** "The generated law admits a paper-29-shaped functional
level" is true of every law on this layer, including laws the corpus has
spent D49–D65 excluding. The unit's own §5 de-licenses the sum dimensions as
"evidence of anything physical"; the same de-licensing is owed to the phrase
"the generated law" throughout. The honest title of §2/§3 is *what `canon`
and the prefix map permit*, and the honest successor question is the one
residue 1 names: a demand that reads the law.

---

## MAJOR 3 — "cohdim equals the parents-record-identical count" is one-step-specific, and the unit's own full-chain column breaks it while the note calls the difference "about 3 %"

**Where.** Note §3 (the table and "`cohdim` reproduces the 'free' column
exactly at every depth"), §2's full-chain paragraph ("subtracts very little
… costs the block reading about 3 % of its coherence"), licensed claim 5,
gate F4(b), LOG #479 ("cohdim reproduces the parents-record-identical count
exactly at every depth").

**Defect.** The claimed identity holds only for one-step C3. Under the pin's
alternative C3 — which the unit itself computes and prints — the coordinate
statement survives and the **dimension** statement fails, and the note
reports the numbers without noticing that its headline identity has broken.

**Recomputation (mine).** Depth 3, block, C4 off. For each of the 134
within-class coordinates I tested whether the solution space pins it, by
`rank(rows) == rank(rows ∪ {e_k})`:

```
  one-step C3 :  determined coordinates 84,  free 50,  cohdim 50   -> identity holds
  full-chain  :  determined coordinates 84,  free 50,  cohdim 41   -> identity fails
```

The nine missing dimensions are **not** coordinate forcings: the same 50
coordinates remain individually unpinned, and the projection is a proper
41-dimensional subspace of their 50-dimensional span, cut out by linear
relations *among free coherences*. So under full-chain C3 there is no "IFF …
by a singleton row" story at all — the killing is exactly the cancellation
the note says does not happen ("one term, no cancellation, no conspiracy").

Worse for the slogan: **no pair of distinct histories in one record class
agrees on its whole ancestor record chain.**

```
  D  | within-class pairs | parents agree | ALL ancestor records agree
  2  |        9           |      0        |        0
  3  |      134           |     50        |        0
  4  |     1491           |    744        |        0
  5  |    15058           |   8074        |        0
  6  |   145018           |  79168        |        0
```

Two serialisations of one DAG always differ in their first event, hence in
their depth-1 record. So "coherence survives exactly where records cannot
reach" (LOG title) is false for the record instrument read as a *filtration*:
what survives one-step C3 is coherence between histories the record **could**
tell apart, two cuts back. The geography tracks *how far down the record
chain the convention looks*, not the record instrument.

**Repair.** State the identity with its convention ("under the block reading
with **one-step** C3"), and add the full-chain sentence the numbers force:
the identity does not survive the pin's own alternative C3, and the
all-ancestors count is 0 at every depth.

---

## MAJOR 4 — the permitted coherence is exactly the indiscernibility of the one-step constraint data; C4 (order 4) is a tiny subgroup of the system's real symmetry group, and the honest quotient shrinks every headline number by 4–15×

**Where.** Pin §1 C4 and §2 F0(i); note §1 bullet C4, §2 (the "renaming-
invariant" column is presented as the canonical one), §3, residue 5 ("an
automorphism of the weighted layer not of label-map form would enlarge C4 and
shrink the tables. **None was searched for.**").

**Defect.** The relevant group for an equivariance demand is the automorphism
group of the **constraint data**, not the group of label renamings. The
constraint data at one-step depth `D` is (record partition at `D`; the parent
map; record partition at `D−1`; the class masses). It has an obvious and
large symmetry group the unit never looked for, and — the sharp part — **the
coherences the unit reports as permitted are precisely the orbits of that
group**.

**Recomputation (mine).** For two depth-`(D−1)` histories `g, g'` with the
same record, the map that exchanges their children by matching records
(well-defined: I checked that same-record parents always carry the same
child-record set — 9/134/1491 pairs at depths 3/4/5, zero exceptions; and
F1(c) makes the matching unique) is an **exact symmetry of the one-step
system** in all three conventions:

```
  D = 3, 9 such transpositions, applied to every row of every convention:
     sum/one-step     : 0 non-symmetry instances     sum/full-chain     : 18
     block/one-step   : 0                             block/full-chain  : 27
     medium/one-step  : 0                             medium/full-chain : 99
```

and every permitted coherence pair is an orbit pair of it:

```
  D = 3 : 50 free pairs,  50 of them exchanged by a symmetry of the system
  D = 4 : 744 free pairs, 744 exchanged
  D = 5 : 8074 free pairs, 8074 exchanged
```

So §3's "coherence survives exactly between serialisations whose parents were
already record-identical" reads, without loss, as *the system is silent
exactly where it cannot tell the two histories apart* — and the full-chain
columns (0 → 18/27/99 violations above) are exactly the reading in which the
symmetry is broken and the dimension drops. That is the mechanism behind
MAJOR 3, and it is a deflation of the physics claim.

Imposing the full equivariance (the parent-swap group together with the four
label maps) instead of the arbitrary order-4 subgroup:

```
  D = 3, block, one-step : orbit-vars 57 (was 310)  rank 40  dim 17 (was 120,
                           or 30 with C4)  | coherence orbits 24, cohdim 13
  D = 4, block, one-step : orbit-vars 231 (was 2467) rank 144 dim 87 (was 1332,
                           or 335 with C4) | coherence orbits 113, cohdim 71
  D = 3, sum,  one-step  : orbit-vars 2101 (was 15576) dim 2071 (was 15469)
  D = 4, sum,  one-step  : orbit-vars 27395 (was 476776) dim 27290 (was 476379)
```

The parent-swap group alone has order ≥ `2⁹ = 512` at depth 3 against C4's 4.
"The renaming group has order 4" is true and correctly gated; "the
renaming-invariant column" is not a canonical quotient, and the cone's
advertised size is dominated by relabelings the constraint system cannot see.

---

## MAJOR 5 — the unasked computation: the permitted/forbidden split is invisible to the closed law's own state space, and one natural dynamical demand kills every coherence at every depth

**Where.** Note residue 1 ("the successor obligation is a *dynamical* or
*operator* demand, since the record demands demonstrably do not suffice"),
residue 7 ("a composition/interchange demand … would be the first thing to
try against these numbers"), §5 claim 3 (F-III as *the* outcome at every
depth ≥ 3), LOG #479's headline.

**Defect.** The unit names the successor demand and does not spend the ten
lines it costs. It is cheap, and it reverses the headline.

**Recomputation (mine), ansatz-free part.** Take the block/one-step split
into permitted (parents record-identical) and forbidden (parents' records
differ) within-class pairs, and push both through D62's closed state map `σ`
(36 states):

```
  D = 3 :  50 permitted pairs on 15 sigma-state pairs ; 84 forbidden on 15 ;
           state pairs permitted AND NOT forbidden = 0
  D = 4 : 744 permitted on 28 ; 747 forbidden on 28 ; disjoint remainder = 0
  D = 5 : 8074 permitted on 32 ; 6984 forbidden on 32 ; disjoint remainder = 0
```

**Every σ-state pair that carries a permitted coherence also carries a
forbidden one.** The geography is not a function of the closed law's state
variables at all; it is a function of the serialisation labels that `canon`
identifies and the prefix map does not.

**Consequence (the demand).** Write `D = diag(μ_Ẑ) + E` and impose the
natural (H2)/D62-compatibility demand — *the coherence excess is generated by
the closed law*: `E(h,h') = μ(h)μ(h')·K(σ(h), σ(h'))` for a symmetric kernel
`K` on the 36 states, zero on the diagonal. The classical member is `K = 0`,
so the demand is fair (it excludes nothing the unit exhibits as existence);
the block trace rows and the C3 trace rows are satisfied automatically
(siblings never share a record, F1(c)); and every off-block singleton row
forces `K = 0` on its state pair. By the census above:

```
  C1(block) + C3(one-step) + C5(state-generated coherence)
      cohdim = 0 at D = 3, 4 and 5   (was 50 / 744 / 8074)
```

**F-III does not survive the first dynamical demand the unit itself names.**
Under one further, entirely natural condition the pre-registered outcome at
every depth ≥ 3 is F-II, not F-III. This does not make the unit's F-III
wrong — it is correct for C1–C4 — but it makes "superposition is PERMITTED
and priced" a statement about a constraint set the unit's own residues call
insufficient, and it settles the open question of what such a demand costs:
everything.

---

## MINOR 1 — the F5(a′) disjointness gate is vacuous, and under the sum reading the falsifier provably does not bite

`F5(a')`'s predicate reduces to `MUC[D][c] * 101/100 != MUC[D][c]` — i.e. to
`101/100 ≠ 1`. It holds for any perturbation of any consistent linear system
and cannot distinguish a discriminating constraint system from one that
accepts every measure. And the sum/C4-off system *is* the latter: rank = row
count at every depth (29, 107, 397, 1451, 5121 — I reproduce all five), so
**every** right-hand side is attainable and no measure whatever can be
rejected. The note discloses this; the gate's framing ("'The system accepts
anything' is false in the only sense that matters") does not survive the
observation that the sense that matters for a falsifier is precisely the one
in which it *is* true here. For the record, the reading the unit skipped has
the control response the unit wanted: medium rejects 23/23 at depth 2 and
84/84 at depth 3, C4 on and off.

## MINOR 2 — dimension is the wrong currency for "how quantum": positivity bounds the size of the coherence and nothing measures it

F3(a) is correct — the classical member is positive definite, hence interior,
hence the PSD-feasible set has the affine dimension — but the affine space is
unbounded while the PSD body is not, and the unit reports only dimensions.
The pinned witness carries `D(h,h') = 1/8192` against a PSD ceiling of
`9/1024` on that entry: **1/72 of the maximum**. Nothing in the receipt
measures how much coherence a member may carry, which is the quantity a
reader will take "a large cone" to be about.

## MINOR 3 — headline over-reach on the two depth-2 clauses

The note's title says "F-II at depth 2 under the block reading, **where the
member is unique**" — unique only with C4 on; with C4 off the depth-2 block
solution space has dimension 4 (§2's own table). And "F-III at every
truncation depth ≥ 3, in both C1 readings" reads as though depth 2 were
uniformly F-II: under the sum reading depth 2 has `cohdim = coh = 4` (C4 on)
and `9` (C4 off), i.e. F-III fires there too. The body is correct in both
places; the title is not.

## MINOR 4 — `1.36 GB` and the wall clock are note-only numbers

Neither appears in `data/d68_functional_slot_exact.out`; the note and LOG
#479 both quote `1.36 GB` and `116 s`. I verified both externally
(`peak memory footprint 1,364,005,544`; 133.8 s real, 116.5 s user on my
machine), so the numbers are true — but a receipt-quoted figure that the
receipt does not print is exactly the kind of number this campaign gates.

## MINOR 5 — C3's "the restriction satisfies C1 one depth down" is the unit's construction, not paper 29's demand, and under the block reading it applies the over-imposition twice

Paper 29 §4.2 asserts that additive restrictions are stable ("future
exhaustive alternatives do not change the earlier restricted functional"); it
nowhere asks a restricted functional to reproduce a lower-depth record
measure. That extra demand is defensible and the unit gates it honestly
(F1(a)/F1(b)) — but it should be labelled a construction, and its
block-reading form inherits BLOCKER 1's over-imposition a second time: the
singleton mechanism is what you get by applying the strongest available
reading of C1 to the restriction as well as to the top layer.

## MINOR 6 — the "transportable" mechanism is asserted on one record functor

§5 claim 5 and the receipt's verdict call the singleton mechanism "the
transportable part", while residue 4 concedes that a coarser or finer functor
"changes every number in §3". No second functor was tried, and the mechanism
depends on precisely the property that makes `canon` special here (records
identify serialisations, so within-class pairs have distinct parents —
F1(c)). One control on a coarsening (e.g. records that forget the last
event's actor) would settle whether anything transports.

## MINOR 7 — "20 witnesses, zero failures" is one construction run 20 times

All 20 witnesses are `classical + t · (kernel direction at the first free
coherence column in a fixed column order)` with the same derived `t`. That is
a sound existence proof and I verified the pinned one exactly; but the count
reads as 20 independent pieces of evidence, and the receipt should say that
it is one algorithm at 20 configurations.

## NIT 1 — "precisely" / "exactly", again

D65's round flagged the same word in the same position. "The record
instrument … decoheres **precisely** what it could already tell apart at the
previous cut" is true as a coordinate statement under one-step C3, false as a
dimension statement under full-chain C3 (MAJOR 3), and empty under C1-coarse
(BLOCKER 1).

## NIT 2 — the pinned witness display under-reports its own support

"direction support 1 coordinate(s)" is in C4-orbit coordinates; the exhibited
member perturbs the whole orbit — 8 ordered pairs, 4 unordered — and the
printed `3×3` block shows one of them. Harmless, but a reader comparing the
block to `cohdim = 13` will mis-count.

## NIT 3 — LOG #479 is the least hedged surface in the deliverable

The note carries its convention clauses; the LOG title
("COHERENCE SURVIVES EXACTLY WHERE RECORDS CANNOT REACH; RECORDS CANNOT SEE
A PHASE") carries none, and it is the sentence the book will inherit.

## NIT 4 — the note contains the refutation of its own headline and does not act on it

§3.1's parenthesis states the swap-symmetry lemma (MAJOR 1); §2's full-chain
paragraph prints the numbers that break the identity (MAJOR 3); residue 2
identifies the C1 reading as an unadjudicated form choice (BLOCKER 1);
residue 7 names the dynamical demand (MAJOR 5). The unit's honesty is real
and is why this review took hours rather than days — but four of the five
findings above are visible from the note's own residues, which is what a
round is supposed to catch before delivery.

---

## Checked and CLEAN

Everything below I recomputed independently and it holds exactly.

* **Anchors.** Family census `[1, 6, 32, 176, 976, 5280, 27904]`, 34,375
  histories; record-class census `[1, 6, 23, 84, 313, 1138, 3983]` = 5,548;
  the class-size census; 36 σ states from my own normal form and my own
  closure; `dim ker(T − 2I) = 1`, strictly positive, values `{1: 29, 4/3: 5,
  7/3: 2}`; `μ_Ẑ` strictly positive, constant on all 5,548 classes, cut mass
  1 at all seven cuts, cylinder-marginal exact at all 6,471 interior
  histories.
* **The group.** The four label maps are weight-preserving bijections of the
  whole family, act bijectively on record classes, preserve `μ_Ẑ`, are
  pairwise distinct as permutations (order exactly 4 as claimed), and the
  fixed-point census matches (`vflip` fixes 127, `swap` and `both` fix only
  the empty history). The Burnside variable counts (`146 / 3968 / 119592 /
  3487568 / 97343616` and the `asym` column) match my direct orbit
  enumeration everywhere, including the 21 self-reversing coherence orbits at
  depth 4.
* **The dimension table.** All 32 configurations at depths 2–5 and the four
  depth-6 rows, every column, including `rank = rows` for sum/C4-off at
  depths 2–6 (`29, 107, 397, 1451, 5121`) and the antisymmetric columns
  (`0` rank under sum at every depth; `13/189/2032`, `50/744/8074`, and the
  full-chain `12` vs `9`, `166` vs `163`).
* **The geography arithmetic.** `0/50/744/8074/79168` and
  `9/84/747/6984/65850`; every off-block row a singleton at every depth 2–6
  (65,850 of 65,850 at depth 6); F1(b)'s `73,674` / `88,036` and its two-sided
  structure; F1(c)'s zero same-parent within-class pairs.
* **F2/F3.** `diag(μ_Ẑ)` satisfies every row of every configuration
  (including my medium reading); minimum diagonal `1/16777216`; interiority.
* **The pinned witness.** `μ_Ẑ(h) = μ_Ẑ(h') = 9/1024`, class mass `27/1024`,
  parents record-identical, `t = 1/8192`, zero residual against all 594 rows
  of my own build, strictly diagonally dominant (min slack `1/4096`), minor
  `5183/67108864`.
* **F5.** `μ_Ẑ` attainable in every configuration (augmented rank = rank);
  block rejects 23/23 and 84/84 with C4 on and off; sum/C4-off has no
  syzygies and rejects nothing; sum/C4-on rejects 22/23 (survivor an
  orbit-size-1 class) and 84/84. F5(b)'s diagonal comparator: `4 / 70 / 588`
  (C4 off) and `0 / 17 / 146` (C4 on), zero at depth-2 block-with-C4.
* **Hygiene.** Pin `2e83abf` committed before the receipt `b866c97`; rerun
  25 PASS / 0 FAIL, exit 0; identical modulo embedded timings at
  `PYTHONHASHSEED` default, 7 and 12345; no float anywhere in the file (I
  re-ran the AST census myself); exit protocol honoured (substantive negatives
  exit 0); the ordered-vs-unordered parent-pair fix is real and load-bearing —
  keying by the unordered pair does cancel the antisymmetric row identically,
  and the receipt keys and documents it correctly at the site.
* **Discipline.** Measurement-not-construction is stated and kept; DC3(2) is
  explicitly *not* claimed discharged; no Hilbert ontology; no class operators
  claimed; the truncation bound, the interpretive status of `canon` and the
  scope clauses (two-actor, delivery-free, closed, depths 2–6) are carried in
  every licensed claim. The de-licensing of the sum-reading dimensions as
  "evidence of anything physical" is exactly right and should be extended, per
  MAJOR 2, to the phrase "the generated law".

---

# DELTA — adjudication and repairs (campaign side, 2026-07-27)

**Verification.**  The repair pass rebuilt the FAITHFUL C1 system
independently and reproduced EVERY cell of the round's table (and
extended it: depth-4/5 by an exact two-partition rank identity,
cross-gated against generic elimination — D5 cohdim 15,058, still
cohdim = coh).  The round's cross-parent-record PSD witness rebuilt
at the same pair, zero residual.  The dynamical demand (C5) gated:
**cohdim = 0 at depths 2, 3, 4, 5**, where C1-C4 alone left
0/50/744/8,074; the invisibility census exact (permitted-but-not-
forbidden sigma-pairs = 0 everywhere).  Phase ranks: sum-reading 0
= a SHAPE TAUTOLOGY (gated over an unrelated mod-7 partition);
faithful reading 268/3,739 — records DO constrain phases.  One
incidental non-match documented (a kernel-scale from pivot choice;
both members exact and PSD).

**Repairs applied (receipt 39 PASS / 0 FAIL, 271 s):** the faithful
reading is the headline; the block reading labelled
forbids-cancellation-by-hand; the sum reading labelled
drops-decoherence; "the record instrument is the exact boundary of
permitted coherence" and "records cannot see a phase" VERBATIM-
STRUCK in §9; the geography's measure-independence gated; the
cohdim identity scoped to one-step+block; C4 labelled the label-map
group (the real symmetry order >= 512); F-III demoted to "the
consistency cone is large"; **the loaded cell is the dynamical
F-II — the first fair dynamical demand eliminates all coherence at
every truncation tried — with its scope stated and THE DEMAND'S
UNIQUENESS as the new residue**; all MINORs/NITs applied.

**Verdict after repairs: the unit stands as restated — consistency
does not structure coherence; the first dynamical demand eliminates
it; at closed scope a quantum layer cannot be both state-generated
and coherent, and where superposition enters (transport scope, a
different joint, or a different fair demand) is the program's
sharpest open question.**  TERMINAL for round 1.
