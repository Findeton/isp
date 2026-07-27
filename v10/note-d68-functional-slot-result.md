# D68 — result: **the generated law admits a functional level, and the record demands do not price it.** Existence is trivial (the classical diagonal member); the space is enormous; and under the only reading that bites, coherence survives **exactly** between histories whose *parents* were already record-identical — killed everywhere else by a **singleton** cylinder-consistency row. **F-III at every truncation depth ≥ 3, in both C1 readings; F-II at depth 2 under the block reading, where the member is unique.**

**Status: GREEN-UNREVIEWED, 2026-07-27.**  No independent round has
been run.  Every number below is machine-produced by
`v10/code/d68_functional_slot_exact.py`, output
`v10/data/d68_functional_slot_exact.out` — **25 PASS / 0 FAIL, exit 0,
116.0 s wall clock, 1.36 GB peak** (run from the repo root),
byte-identical under `PYTHONHASHSEED` variation — default / 7 / 12345,
verified by diff, with the only differences being the timing fields
(the per-configuration `sec` column and the `t = …` / wall-clock
lines).  Pin `note-d68-functional-slot-pin.md`
(STRICT, frozen and committed before any computation ran); its
question §1, gates F0–F6, pre-registered outcomes F-I…F-IV and scope
§4 are honoured as written and the pin's declared lean — *none* — is
respected: the receipt reports what the algebra says, under **both**
C1 conventions, with C4 **on and off**, and with C3 read **one-step
(the pin's literal)** and **full-chain**.

Parents: paper 29 §3/§3.1 (refined cylinders and what Theorem 1 does
*not* say), §4.1–§4.3 (class operators, the Gram functional
`D(α,β) = ⟨v_α, v_β⟩`, strong positivity, the five durable-record
hypotheses), §5 (the D34c lesson — *the record instrument is part of
the click law*); D65 (DC3(2): the generated line has **no** functional
level, and that is where the missing map is widest; `μ_Ẑ` genuinely
descends; the repair-cone method); D62/D61 (the closed law); d44a and
d42b3 (the committed layers, text-sliced and AST-gated, never
re-implemented).

**Scope, non-negotiable and load-bearing in every sentence below:
TWO-ACTOR, DELIVERY-FREE, d42a, CLOSED SCOPE, the truncations D = 2…6
of the exhaustive depth-6 family** (census `[1, 6, 32, 176, 976, 5280,
27904]`, 36 σ states, 176 transition keys, **5,548 record classes**
`[1, 6, 23, 84, 313, 1138, 3983]`).  Nothing here transfers to the
identified (action-line) click law: **no member computed here is
claimed to BE the action line's functional.**  The map is an
identification problem; this unit answered an existence/dimension
question on the generated side only.

---

## 1. What was actually computed

Over the depth-`D` history layer, the set of forms `D(h,h')` with

* **C1**, in **both** pinned readings, right-hand side `μ_Ẑ` — the
  measure D65 gated as genuinely descending, here recomputed from the
  committed λ = 2 transfer eigenvector (`f` with values `{1, 4/3, 7/3}`
  and multiplicities `{29, 5, 2}` = D49's `f`), normalised so that it
  is a probability measure on **every** depth cut, so the C1 data at
  different depths are one object seen at different cuts and no
  normalisation is chosen by hand:
  * **(sum)** `Σ_{h,h' ∈ r} D(h,h') = μ_Ẑ(r)` — the decoherent-sum
    reading, and it is paper 29 §3.1's own pushforward convention
    `(q_*μ)(ω̄) = Σ_{q(ω)=ω̄} μ(ω)` applied to the class;
  * **(block)** `D(h,h') = 0` whenever `record(h) ≠ record(h')`, and
    `Σ_{h ∈ r} D(h,h) = μ_Ẑ(r)` — the record algebra is exactly
    decoherent and the block **trace** carries the mass.
* **C2** positive semidefiniteness (paper 29 §4.2's strong
  positivity).
* **C3**, operationalised and printed: a depth-`d` history `g` denotes
  the cylinder of its depth-`D` extensions, so the restricted form is
  `R^(d)(g,g') = Σ_{a ⊐ g, b ⊐ g'} D(a,b)` (paper 29 §4.2's additive
  restriction), and C3 demands that `R^(D−1)` satisfy **the same
  convention's C1** at depth `D−1`.  Gated (F1(a)) to reduce to the
  classical marginal on diagonal members — for `μ_Ẑ` **and** for a
  deliberately non-classical index-weighted diagonal, so the check
  cannot pass on `μ`'s own symmetry.
* **C4** equivariance under the renaming group, **computed rather than
  assumed** (F0(i)): the four label maps (actor swap) × (value flip),
  each verified on the whole family to be a weight-preserving
  bijection that carries record classes to record classes bijectively
  and preserves `μ_Ẑ`.  The group is **not** trivial and **not** free
  — over the 34,375 histories the value flip fixes 127 of them and the
  actor swap fixes only the empty one.  C4 is imposed *by
  construction*, the variables being the group's orbits of pairs.
  `μ_Ẑ` is constant on all **5,548** record classes, re-gated here.

Headline space real symmetric over **Q**; the **Hermitian extension**
(`D = S + iA`) is carried as a separate column throughout.
Dimensions are `variables − EXACT rational rank` by sparse elimination
over **Q** (D65 round-1's standard).  Positivity is certified by exact
strict diagonal dominance and exact 2×2 determinants — never a float,
never an eigenvalue (F0(c) is an AST gate on this receipt's own syntax
tree: zero inexact literals, zero `float`/`complex` calls, zero
inexact-library imports).

### 1.1 The fact that gives C3 its content — and then leaves something over

**The record functor does not commute with taking prefixes** (F1(b)).
`canon` identifies two histories when they are two serialisations of
one *labelled event DAG*; two such serialisations have **different**
prefixes, so the depth-`D` record partition is not the pullback of the
depth-`(D−1)` one and C1 at depth `D` carries no C1 at depth `D−1`.
C3 is therefore an independent demand, not bookkeeping.  But the
splitting is **partial**: of the multi-member record classes, some
have members with different parent records and some do not — and that
second set is exactly what survives in §3.  Also gated: **no two
siblings share a record** (F1(c), zero exceptions), so every
within-class off-diagonal entry connects two histories with *distinct*
parents.

---

## 2. F2/F3 — existence, and the dimension

**F-I and F-IV are both EXCLUDED, and by the same one-line fact.**
The **classical diagonal functional** `D = diag(μ_Ẑ(h))` satisfies C1
in both readings, C2, C3 in both readings and C4 — in **all 32
configurations**, verified by exact residual against every row, not by
construction — and it is **positive definite** (smallest diagonal
entry `1/16777216` at depth 6).  So the generated law *does* admit a
paper-29-shaped functional level at this scope; **existence was never
the obstruction, and this note declines to sell it as a result.**

**C2 removes no dimension.**  Because the classical member is positive
*definite* it is an **interior** point of the PSD cone, so the
PSD-feasible set has the same dimension as the affine solution space
in every configuration (F3(a)).  The dimension table therefore *is*
the answer.

### The pinned configuration — C4 on, C3 one-step

| D | **sum**: vars / rank / **dim** | coh / **cohdim** | **block**: vars / rank / **dim** | coh / **cohdim** |
|---|---|---|---|---|
| 2 | 146 / 10 / **136** | 4 / **4** | 13 / 13 / **0** | 4 / **0** |
| 3 | 3,968 / 30 / **3,938** | 35 / **35** | 81 / 51 / **30** | 35 / **13** |
| 4 | 119,592 / 105 / **119,487** | 390 / **390** | 638 / 303 / **335** | 390 / **189** |
| 5 | 3,487,568 / 369 / **3,487,199** | 3,792 / **3,792** | 5,120 / 2,118 / **3,002** | 3,792 / **2,032** |
| 6 | 97,343,616 / 1,292 / **97,342,324** | 36,447 / **36,447** | 43,439 / 17,861 / **25,578** | 36,447 / **19,847** |

### C4 off — the same table on the full form space

| D | **sum**: vars / rank / **dim** | coh / **cohdim** | **block**: vars / rank / **dim** | coh / **cohdim** |
|---|---|---|---|---|
| 2 | 528 / 29 / **499** | 9 / **9** | 41 / 37 / **4** | 9 / **0** |
| 3 | 15,576 / 107 / **15,469** | 134 / **134** | 310 / 190 / **120** | 134 / **50** |
| 4 | 476,776 / 397 / **476,379** | 1,491 / **1,491** | 2,467 / 1,135 / **1,332** | 1,491 / **744** |
| 5 | 13,941,840 / 1,451 / **13,940,389** | 15,058 / **15,058** | 20,338 / 8,394 / **11,944** | 15,058 / **8,074** |
| 6 | 389,330,560 / 5,121 / **389,325,439** | 145,018 / **145,018** | 172,922 / 70,850 / **102,072** | 145,018 / **79,168** |

**C3 full-chain** (every depth step down to the root; computed at
D ≤ 4, where the depth-0 row is a dense sum over the whole layer)
subtracts very little: sum/C4-on `135 / 3,935 / 119,476`;
sum/C4-off `498 / 15,462 / 476,349`; block/C4-on `0 / 25 / 301`
with coherence `0 / 9 / 163`; block/C4-off `4 / 106 / 1,212` with
coherence `0 / 41 / 651`.  **Reading C3 all the way down instead of
one step costs the block reading about 3 % of its coherence and the
sum reading nothing at all.**

**Three structural facts inside the table, worth naming on their own.**

1. **Under the sum reading with C4 off, the constraint rows are
   linearly independent at every depth** — rank equals the row count
   exactly (`29, 107, 397, 1451, 5121`).  The 3,983 depth-6 class rows
   and the 1,138 depth-5 restriction rows impose 5,121 *independent*
   conditions on 389 million variables.
2. **The sum reading's dimension is essentially the whole space.**  At
   depth 6 it is 97,342,324 of 97,343,616 (C4 on).  The
   decoherent-sum record demand is, dimensionally, almost nothing.
3. **The block reading is the one that bites**, cutting 43,439 → 25,578
   at depth 6 with C4, and it is the only reading under which the
   coherence question has a non-trivial answer.

---

## 3. F4 — THE COHERENCE QUESTION: **permitted, and the forcing constraint is named**

**Under the decoherent-sum reading, coherence is priced at ZERO**
(F4(a)): in every one of the 16 `sum` configurations, at every depth,
`cohdim = coh`.  The projection of the solution space onto the
within-class off-diagonal coordinates is *everything*.  No within-class
coherence is constrained at all.

**Under the block reading the answer is a proper subset, and the
mechanism is elementary** (F4(b)).  A within-class entry `D(h,h')`
survives into the restriction as a term of `R^(D−1)(g,g')` with `g, g'`
the two (distinct, by F1(c)) parents.  When the parents carry
**different** records, the block reading demands `R^(D−1)(g,g') = 0` —
and **every one of those rows is a SINGLETON**:

```
      R^(D-1)(g, g')  =  D(h, h')  =  0
```

one term, no cancellation, no conspiracy.  The forced set is therefore
*exactly* the within-class pairs whose parents carry different
records, and the surviving coherence dimension equals, on the nose,
the number of within-class pairs whose parents carry the **same**
record:

(counts below are on the **full** form space, C4 off; the
renaming-invariant counts are the C4-on column of §2)

| D | within-class off-diagonals | parents' records **differ** → FORCED to 0 | parents' records **agree** → FREE | off-block rows / all singletons |
|---|---|---|---|---|
| 2 | 9 | 9 | **0** | 9 / yes |
| 3 | 134 | 84 | **50** | 84 / yes |
| 4 | 1,491 | 747 | **744** | 747 / yes |
| 5 | 15,058 | 6,984 | **8,074** | 6,984 / yes |
| 6 | 145,018 | 65,850 | **79,168** | 65,850 / yes |

and `cohdim` reproduces the "free" column exactly at every depth
(`0, 50, 744, 8074, 79168`).  **The record instrument reaches back one
step and decoheres precisely what it could already tell apart at the
previous cut.**  That is the D34c lesson (paper 29 §5) recovered at
the generated law's own scope, from the generated side, with no
quantum input: *the record instrument is part of the click law, and
here it is the only thing that removes a phase.*

**F-II fires at depth 2, and only there** (F4(c)).  At `D = 2` single
events are their own records, so every within-class pair has parents
of different record, every off-block row is a singleton, and
`cohdim = 0`: quantum structure is **forbidden**.  With C4 imposed the
solution space has dimension **zero** — the classical diagonal member
is the *unique* form satisfying C1(block) + C2 + C3 + C4 at depth 2.
It does not survive the next depth.

**The witness** (F4(d)): for every configuration with `cohdim > 0` at
depth ≤ 4, an exact member is built by perturbing the classical member
along a kernel direction with value 1 at a free coherence coordinate,
at a scale **derived** from the member itself
(`t = min diagonal / (2 × max |row-sum| of the direction)`), verified
against **every** row with zero residual and certified positive
definite by exact strict diagonal dominance.  20 witnesses, zero
failures.  The pinned one (`D = 3`, block, C4 on, one-step,
`t = 1/8192`) sits on a record class of size 3:

```
   h  = ( ('n','B'), ('n','A'), ('p','A',v0,0) )
   h' = ( ('n','A'), ('n','B'), ('p','A',v0,0) )
   mu_Zhat(h) = mu_Zhat(h') = 9/1024,  class mass 27/1024

   block:   [ 9/1024   1/8192      0    ]
            [ 1/8192   9/1024      0    ]
            [   0        0      9/1024  ]

   the (h,h') minor has determinant 5183/67108864 > 0
```

Two idles in either order, then a proposal: the two orderings are one
labelled DAG, their parents (`n_B` then `n_A`, versus `n_A` then
`n_B`) are **two serialisations of the same two-idle DAG** and hence
record-identical, and the entry between them is free.  **This is the
whole finding in one 3×3 block.**

### 3.1 The Hermitian column

**The decoherent-sum demands are blind to the imaginary part**
(F4(e)).  Every C1 and C3 row in the sum reading is a sum over a
**symmetric** set of index pairs, so it annihilates the antisymmetric
part identically: the constraint rank on the imaginary part is
**zero** at every depth and the entire antisymmetric space survives
(e.g. 3,482,288 of 3,482,288 free at depth 5, C4 on).  *A record
measure of that shape cannot see a phase, so no amount of C1/C3 could
ever select one.*  Under the block reading the imaginary part meets
exactly the same singleton off-block rows and, with one-step C3, its
coherence dimension equals the real one on the nose
(`0, 13, 189, 2032` with C4; `0, 50, 744, 8074` without).  With
full-chain C3 the two come apart slightly (`12` vs `9` at depth 3,
`166` vs `163` at depth 4, C4 on) because the lower rows are symmetric
sums that bite the two parts differently; the numbers are printed
rather than smoothed.

*(This is also the one place a real construction bug was found and
fixed before delivery: keying the off-block rows by the **unordered**
parent pair sums `R(g,g')` and `R(g',g)`, which is twice the same
constraint on the real part but **identically zero** on the imaginary
part — the constraint would have silently vanished from the Hermitian
column and the imaginary coherence would have been reported as
totally free.  The receipt now keys one row per **ordered** parent
pair and says so at the site.)*

---

## 4. F5 — the controls

**The perturbed measure** (F5(a)).  Each depth-`D` record class's mass
in turn multiplied by `101/100`, the depth-`(D−1)` right-hand sides
left alone, feasibility decided **exactly** by the syzygies (the
left-null vectors of the coefficient matrix, harvested from the same
elimination): a right-hand side is attainable exactly when every
syzygy annihilates it.  The response is three-sided and all three
sides are reported:

* the true `μ_Ẑ` is **attainable in every configuration**;
* under the **block** reading **every** perturbation is **rejected as
  infeasible**, at every depth, with C4 on *and* off (23/23, 84/84,
  313/313) — the block traces at depth `D` and the restricted traces
  at depth `D−1` tie the classes together and a lone class cannot
  move;
* under the **sum** reading with **C4 off** there are **no syzygies at
  all** (rank = rows), so nothing can be rejected on linear grounds.
  There the response is **disjointness**, gated separately (F5(a')):
  the perturbed C1 row demands a different value of the *same* linear
  functional, so no form satisfies both systems.  With C4 on the sum
  reading rejects 22/23, 84/84, 312/313 — the survivors are classes
  the renaming group fixes (orbit size 1).

**The pure-diagonal comparator** (F5(b)).  The same pipeline with the
variables restricted to the diagonal — the strictly classical layer
through the identical rank machinery — has strictly positive dimension
everywhere except at depth 2 with the block reading and C4, where it
is zero: `4 / 70 / 588` (C4 off, one-step, D = 2/3/4) and
`0 / 17 / 146` (C4 on).  **`μ_Ẑ` is one point of a classical polytope
before it is one point of a quantum cone**; the record demands do not
even pin the per-history weights.  This is the honest baseline against
which the coherence dimensions should be read.

---

## 5. Licensed claims — and the ones this unit forbids

**Licensed, at two-actor delivery-free d42a closed scope, at the
truncation depths 2–6 of the exhaustive depth-6 family, with `canon`
as the record functor:**

1. **The generated law admits a paper-29-shaped functional level.**
   The classical diagonal functional `diag(μ_Ẑ)` satisfies C1 (both
   readings), C2, C3 (both readings) and C4 in all 32 configurations
   and is positive definite.  **F-I and F-IV are excluded.**
2. **The space of such levels is enormous under the decoherent-sum
   reading and merely large under the block reading** — the two tables
   in §2 are the numbers.  C2 removes no dimension because the
   classical member is interior.
3. **F-III is the outcome at every truncation depth ≥ 3 under both C1
   readings.**  Superposition between histories the record cannot
   distinguish is **PERMITTED**, and an exact PSD witness with
   non-zero within-class coherence is exhibited (20 of them, zero
   failures).
4. **F-II fires at depth 2 under the block reading only**, and there
   totally: `cohdim = 0`, and with C4 the member is **unique**.
5. **The forcing constraint is named and elementary.**  Under the
   block reading a within-class coherence is killed **iff** the two
   histories' parents carry different records, and it is killed by a
   **singleton** cylinder-consistency row.  What survives is exactly
   the coherence between serialisations whose parents were already
   record-identical: `0 / 50 / 744 / 8,074 / 79,168` at depths 2–6 on
   the full form space (C4 off), `0 / 13 / 189 / 2,032 / 19,847` on
   the renaming-invariant one (C4 on).
6. **The record demands are blind to the imaginary part** under the
   decoherent-sum reading (constraint rank zero on the antisymmetric
   part at every depth), and see it exactly as they see the real part
   under the block reading with one-step C3.
7. **The constraint system responds to a wrong measure**, and how hard
   it responds is itself a convention fact (§4).
8. **Even the classical layer is under-determined** by C1 + C3 + C4
   (F5(b)).

**Explicitly NOT licensed (do not quote):**

* that any member computed here **is** the action line's decoherence
  functional, or is related to it — **the map is untouched**; this
  unit answered existence and dimension on the generated side only;
* any Hilbert-space ontology.  `D` is a form on a finite set.  That
  every PSD member is a Gram matrix is linear algebra, not a claim
  about carriers, and **no class operators are constructed** — paper
  29 §4.1's operator level remains unbuilt;
* "the generated law is quantum", or "permits superposition", without
  the convention, the depth and the record-functor clauses — under the
  block reading at depth 2 it forbids it outright;
* "the record demands force coherence" — they never do; F-IV is
  excluded;
* the coherence dimensions as depth-free numbers.  They are truncation
  dimensions, exactly as D65's 573 and 3,053 were;
* the `sum`-reading dimensions as evidence of anything *physical*;
  they are evidence that the decoherent-sum reading is a very weak
  demand;
* any of the above at three-actor scope, at transport scope, with
  delivery, or beyond depth 6;
* D65's DC3(2) as **discharged**.  It is not.  DC3(2) says the
  generated line *has no functional level*; this unit shows a large
  space of objects that *could serve as one* under C1–C4 and shows
  that those conditions do not select among them.  **Building a
  functional level means deriving one, not measuring the space of
  candidates.**

---

## 6. Residues

1. **The unit is a measurement, not a construction.**  D65's residue 1
   — the map's functional segment — is *narrowed*, not closed: the
   generated line still has no derived class operators and no derived
   Gram functional.  What is now known is the shape of the slot: what
   C1–C4 can and cannot pin.  The successor obligation is a *dynamical*
   or *operator* demand, since the record demands demonstrably do not
   suffice.
2. **Which C1 reading is "the" record demand is undecided, and it is
   D50 again on a new level.**  The pin asked for both and this unit
   delivers both; the answers differ by five orders of magnitude in
   dimension and by everything in the coherence question.  Choosing
   between the decoherent-sum and the block reading is a **form
   choice**, exactly the object D50 priced and D65 priced again.
3. **The truncation.**  Every dimension is a truncation dimension.  The
   pattern (forced ⇔ parents' records differ; all such rows singletons)
   held at every depth 2–6 with zero exceptions, but there is **no
   lean and no proof** — the pin declines to bet and so does this note.
   A depth-free statement is open.
4. **The record functor is interpretive.**  `canon` was *chosen* as the
   generated line's record identity (the D65 precedent, residue 3
   there).  A coarser or finer functor changes which pairs are
   within-class at all, and therefore changes every number in §3.
5. **The renaming group is the LABEL-MAP group.**  It is computed and
   gated, not assumed — but an automorphism of the weighted layer not
   of label-map form would enlarge C4 and shrink the tables.  None was
   searched for.
6. **C2 is untested where it could bite.**  Positivity removes no
   dimension here *only because* every record class has strictly
   positive mass, making the classical member interior.  At a scope
   with a null record class, or on the boundary of the cone, PSD would
   be a genuine constraint and none of §2 transfers.
7. **C3 is a consistency condition, not a law.**  Nothing here says how
   a form *evolves*; the depth steps are restrictions of one object,
   not a dynamics.  A composition/interchange demand at the operator
   level (paper 29 §4.1) is exactly what is missing and would be the
   first thing to try against these numbers.
8. **Three actors, transport, delivery** — out of scope, as always.

---

## 7. Gate ledger and where the evidence sits

25 gates, 25 PASS, 0 FAIL, exit 0.  **A clean sheet is not evidence of
a positive result** — the negatives here (F-II at depth 2, the
sum reading's emptiness of content, the blindness to phase, the
under-determined classical comparator) are registered as *passing
gates that assert them*.  The falsifiable, substantive gates are:

* **anchors** F0(d) history census, F0(e) record-class census (5,548),
  F0(f) 36 states / 176 keys / single successor, F0(g) the λ = 2
  spectrum, F0(h) `μ_Ẑ`'s descent and normalisation, F0(i) the
  renaming group;
* **definitions** F1(a) the marginal reduction, F1(b) prefix
  non-commutation (two-sided), F1(c) no siblings share a record;
* **the result** F2 existence, F4(a) sum-reading freedom, F4(b) the
  singleton forcing mechanism, F4(c) the depth-2 negative, F4(d) the
  witnesses, F4(e) the Hermitian column;
* **controls** F5(a), F5(a'), F5(b); **determinism** F6(a).

Structural/hygiene gates on the file itself: F0(a) AST single sources,
F0(b) AST exit-freedom, F0(c) AST inexactness scan, F6(b) AST
hash-order scan.  **Entailed or declarative, and marked as such:**
F3(a) (a convexity corollary of F2's positive-definiteness, not an
independent measurement) and F6(c) (a declaration auditable against
the source).

Reproduce: `python3 v10/code/d68_functional_slot_exact.py` from the
repo root (optional argument = family depth, default 6).
