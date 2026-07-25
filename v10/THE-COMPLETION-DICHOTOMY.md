# THE COMPLETION DICHOTOMY

### A self-contained brief: why the record law cannot normalize itself, exactly how that is forced, and everything already established about the one escape

**Compiled 2026-07-25.**  Corpus: `~/workspace/isp`, v10 line.
Author of the research programme: Felix Robles Elvira (ORCID
0009-0009-2017-4394).

---

## 0. How to read this document

**This file is written to be read alone.**  A reader — human or
agent — who has never seen the corpus should be able to finish it
understanding what the dichotomy is, why it is not a gap in the
work but a theorem, and precisely what is and is not known about
escaping it.  Every corpus fact is given with its source and a
provenance label.  Nothing here is new research; it is a brief.

**Provenance labels, used throughout and load-bearing:**

| label | meaning |
|---|---|
| `[THEOREM]` | proved, with the proof in the cited place |
| `[EXACT]` | computed in exact rational arithmetic by a committed receipt that exits 0 |
| `[MEASURED]` | computed, but at a declared finite scope only |
| `[EVIDENCE]` | supports a claim without being a premise of any proof |
| `[REFEREE-CARRIED]` | established in a frozen hostile-review record, not in a receipt |
| `[POSITED]` | an interpretive choice, not derived |
| `[MY READING]` | interpretation added in this brief, not a corpus claim |

**Two disciplines a new reader must obey.**  (1) *Green-unreviewed
work is not citable.* Units that have not passed a hostile review
round are marked so, and no paper may lean on them. (2) *Scope
labels are part of the claim.* "At d42a scope", "at tested scale",
"delivery-free" are not hedges; dropping them changes a true
statement into a false one.

---

## PART I — THE OBJECTS

You need five objects. They are simple; the difficulty is entirely
in how they interact.

### 1.1 Actors

An **actor** is the framework's primitive holder of history. It is
defined purely by what it does:

- it is **sequential** — all of one actor's events are totally
  ordered among themselves; an actor never branches;
- it has **its own version chain** — when an actor writes a new
  version, that version must descend from the last version *that
  same actor* wrote (the **mint chain**);
- it is **addressable** — actors deliver to one another;
- it is **the source of width** — the framework's parallelism is
  bounded by the number of actors.

**Nothing in the corpus identifies an actor with anything
physical.** Not a particle, not a region, not a degree of freedom.
It is an uninterpreted primitive, deliberately. Every attempt to
attach it to a laboratory object is currently blocked (§9.3).

### 1.2 Records

A **record line** is one actor's trace: the succession of versions
it has written. The **record** is the whole generated structure —
all lines plus the events that couple them. Actor is to record line
as particle is to worldline.

Actors and lines are in strict one-to-one correspondence, which is
why the corpus sometimes slides between the two words. That
correspondence is not a convention — see §9.2.

### 1.3 The event grammar (the "click law", what CAN happen)

At the base scope, called **d42a**, there are three event types.
Receipt: `v10/code/d42b3_placement_exact.py`.

| event | meaning |
|---|---|
| `('p', a, base, k)` | actor `a` **proposes** value-bit `k` on version `base` |
| `('r', a, C, w)` | **arbitration**: initiator `a`, conflict component `C`, winner `w`. The arbitration event *is* acceptance — it creates the successor version |
| `('n', a)` | actor `a` **idles** |

The extended scope, **d42b1** (`v10/code/d42b1_transport_exact.py`),
adds two:

| event | meaning |
|---|---|
| `('d', s, r, v)` | **delivery** of version `v` from `s` to `r`; carriers `{s, r}`; a *join* of knowledge; re-delivery is admissible and physical |
| `('m', a, pk, w)` | **merge** by the holder of both versions of a pair |

**Admission is past-local.** Which events are available is a
function of the history so far, and this is fully specified and
executable: `candidates_for(history, actors)` returns exactly the
admissible next events, with a weight for each. This part of the
theory is unambiguous, single-source, exhaustively enumerable, and
exact.

**Everything in Parts III–VIII is about the weights, not the
admissibility.**

### 1.4 Cuts, and the cut complex

A **cut** is a slice through a record — a "now". There is no
preferred slicing; that is the point of a relativistic setting. A
**foliation** is a sequence of cuts, i.e. one linear extension of
the record's causal order.

The **cut complex** is the graph whose vertices are cuts and whose
edges are single admissible steps. At the worked scope — the
**depth-4 two-actor family** — it has: `[EXACT]`

- **1,191 histories**
- **427 canonical classes** (histories identified up to the
  grammar's gauge)
- **202 canonical diamonds**

### 1.5 Diamonds

A **diamond** is the smallest loop in the cut complex: two
elementary steps performed in either order, arriving at the same
cut. Nothing more exotic than a commuting square.

Diamonds exist to test **path-independence**. If you assign
numbers to the record and want them to define a consistent
potential, then traversing any diamond both ways must agree. Since
diamonds are the *smallest* loops, agreement on all of them is the
whole condition — this is standard discrete cohomology: flat on all
2-cells ⟹ a potential exists.

> **Warning on vocabulary.** "Diamond" is overloaded in this
> corpus. The 202 above are **cells of the cut complex**. Paper 3
> uses "diamond" for the *marked-support amalgamation figure*
> (where the result is that amalgamation is composition, not
> carrier birth). Paper 29 uses "flat squares on diamonds" at the
> action level. These are different jobs for the same shape. The
> 202 are **not** Alexandrov intervals between two events.

### 1.6 The weight system — and why it is NOT a probability law

Each admissible event carries an exact rational weight. The
structure of these weights is itself a result: per-initiator weight
sums sit on the exact **quarter-integer ladder `1 + k/4`**, where
`k` counts causally blind join layers, at every record point of the
enumerated families `[EXACT]`. One constructed configuration
(`h12`) lies off the ladder, and the general-depth ladder is
**false** under current pricing — its reconciliation is carried
into the completion problem.

**The critical fact.** The weights do not sum to 1. Menus sum to
**2** or **5/2**. The transport layer says so in its own docstring,
quoted verbatim from `d42b1_transport_exact.py`:

> *Weight-system level only (RF4): no measure claim; the placement
> front (d42b3) owns normalization; the `1+k/4` ladder is censused
> per A7/A7'.*

So the framework specifies **what can happen** and **relative
weights**, and does *not* specify **what does happen**. Turning the
weight system into a probability law is called **completion**, and
it is the subject of this document.

---

## PART II — THE COMPLETION PROBLEM, STATED PRECISELY

A **completion** supplies positive cut data `Z > 0` and defines the
completed conditional

```
q'(e | h)  =  q(e | h) · Z(h + e) / Z(h)
```

Three demands are natural. Each is independently reasonable.

- **(a) PER-CUT NORMALIZED.** `Σ_e q'(e | h) = 1` for every
  history `h`. Without this you have no probabilities at all.
- **(b) FOLIATION-INVARIANT.** The completed conditional is a
  function of the record alone — *class-constant* — equivalently,
  chain products agree across **every** linear extension of every
  history. Without this, "the probability" depends on which slicing
  you chose to compute it in, which is exactly what a relativistic
  theory may not tolerate.
- **(c) WITHIN-CUT RATIO-PRESERVING.** The relative weights of
  alternatives at a cut are untouched by completion. Without this,
  completion is not merely *normalizing* the law — it is
  *changing* it.

The existence of a globally consistent `Z` is the **discrete
Tomonaga–Schwinger integrability condition** for the record
functional. Per diamond, the two-path constraint is solvable and
underdetermined; the global question is whether the ladder excess
of §1.6 is a **coboundary** on the cut complex.

**On the depth-4 complex the condition is DECIDED.** What follows
is that decision.

---

## PART III — THE DICHOTOMY, AND EXACTLY HOW IT IS FORCED

### 3.1 The theorem: (a) + (b) + (c) is impossible

> **`[THEOREM]` Ratio-preserving completions do not exist.**
> Ratio preservation forces `Z(h+e)/Z(h) = 1/N(h)`. No cut
> function has these increments, because `N`'s chain products are
> foliation-dependent: **36 of the 202 canonical diamonds refute
> integrability** `[EXACT]`, the violations lying in **two
> diamond-connected components** `[REFEREE-CARRIED]`.

Source: paper 30 §5.2 (`relativistic-isp-v10-paper30-the-generated-record-and-its-completion.md`),
receipt-gated; and `note-d42b3-placement-and-the-discrete-ts-condition.md` D1.

**The forcing, step by step.** This is the heart of the document.

1. Demand (c) fixes `Z`'s increments completely. If relative
   weights within a cut must survive, then the only freedom
   completion has is an overall factor per cut, and demand (a)
   pins that factor: it must be `1/N(h)`, where `N(h)` is the
   frontier sum of raw weights. **`Z = N` is forced — there is no
   choice left.**
2. So the question collapses to a single yes/no: *is `N` a
   discrete gradient on the cut complex?* Equivalently, is
   `log N`'s increment a coboundary?
3. **It is not.** `N` is genuinely cut-attached data — it is
   constant on all 427 canonical classes, and this is gated
   `[EXACT]` — but being cut-attached is not enough. A gradient
   must have path-independent chain products, and `N`'s are
   **foliation-dependent**.
4. **The mechanism, named:** `N` **double-counts the blind join
   layer** along exactly those foliations that expose it. Two
   slicings of the same record disagree about how much frontier
   mass a causally blind layer contributes, so the products come
   out different.
5. **The certificate:** 36 diamonds where the two paths give
   different products. Not one pathological case — a census, in
   two connected components, with paper 30 §4.3's witness pair as
   one certificate among them.

> **A correction on the record, worth reproducing** because it
> shows the finding survived its own audit. An earlier statement
> that "`N` is NOT cut-attached data" was **FALSE** and was
> withdrawn: `N` *is* constant on all 427 canonical classes. The
> true and stronger statement is that `N` is cut-attached **but
> not a discrete gradient**. The no-go was generalized from one
> witness to the 36-diamond census in the same repair.
> (`note-d42b3...` D2.)

### 3.2 The dichotomy

Since (a) is non-negotiable (no probabilities otherwise) and (b) is
non-negotiable (no relativistic theory otherwise), **(c) must go.**

> **THE DICHOTOMY.** Either
>
> **(I)** the completion **deforms within-cut ratios** — it
> imports something that is not in the local weights, and the
> import is visible as a tilt in relative probabilities; **or**
>
> **(II)** no completion is needed at each finite depth because a
> **root-free** completion exists — which requires a strictly
> positive harmonic function on the *infinite-volume* state space.
>
> There is no third option at this scope. This is not a gap in the
> work; it is a decided trilemma.

Paper 30's one-sentence form: *per-cut normalized,
foliation-invariant, and within-cut ratio-preserving is classically
impossible; dropping the third demand makes the problem solvable at
every finite depth, and the deformation of within-cut ratios is
exactly what solving it costs.*

### 3.3 One escape was tried and closed

A **zero-class counterterm** (the own-view component filter) does
restore sums ≡ 1 — by exactly `k·(1/4)`, the ladder excess — and is
gauge-invariant. It refutes the no-go **as originally worded**.

It also **kills ALL join arbitration.** `[EXACT]`

So the no-go was repaired rather than abandoned: it holds for
**support-preserving (strictly positive)** counterterms, by a
nesting argument (subset candidates, equal shared weights, positive
extra mass) which is now printed and gated. The zero class is
**declared excluded**, on the stated ground that *a completion
which abolishes joint arbitration abolishes the physics it was
meant to normalize.* (`note-d42b3...` D3.)

**A new reader should treat this as the template for the corpus's
style:** the no-go was not defended, it was narrowed until true,
and the narrowing is on the record with its reason.

---

## PART IV — HORN (I): WHAT SURVIVES, AND EXACTLY WHAT IT COSTS

### 4.1 Gradient completions exist at every finite depth `[EXACT]`

A **gradient (`h`-transform) completion** runs the backward
recursion

```
Z(h)  =  Σ_e  q(e | h) · Z(h + e)
```

from any strictly positive boundary at terminal depth. At the unit
boundary, on the depth-4 two-actor object:

| quantity | value |
|---|---|
| `Z(empty)` | **`1037/64`** (reciprocal convention: `64/1037`; every ratio-level quantity identical) |
| positivity | throughout |
| per-cut normalization | at **all 215 interior histories** — the recursion's defining identity |
| the §4.3 witness pair | **equalizes at `1/2074`** under both orders |
| boundary freedom | **313-dimensional** `[REFEREE-CARRIED, LOG #302]` |

**This is a Doob `h`-transform.** The corpus names it as such
(`note-d43-corpus-audit-and-the-next-step.md`: "*completion is a
Doob h-transform*"; `note-d40-where-the-action-cocycle-lives.md`:
"*the K-flat shape is an `h`-ratio/Doob completion form*").

`[MY READING]` That identification is the interpretive centre of
the whole issue. A Doob `h`-transform is what you get when you
condition a process on its future behaviour: each step's relative
weights are tilted by a function of where the process is heading.
The 313 parameters are the choice of that function. So horn (I)
says the framework's probabilities are **forward-local rules plus a
boundary object**, and the boundary object is not derivable from
the rules.

### 4.2 The unavoidable cost `[EXACT]`

> **Within-cut ratio deformation at 21 of the 114 interior cut
> classes, the root included. No boundary choice avoids the
> deformation.**

At the root, the successor normalizers are not constant across
candidates. The extremes:

| convention | extreme values |
|---|---|
| completed weights | `133/2074` vs `771/2074` |
| successor normalizers (reciprocal) | `16/133` vs `32/257` |

**The root being included is the sharp point.** A deformation
confined to the deep interior might be dismissed as a truncation
artifact. One that reaches the root is a statement about the
theory's beginning.

### 4.3 What is invariant with no completion at all

Two positive laws hold before any completion, and any completion
must respect them. The gradient class does.

- **RATIO LOCALITY.** `μ`-ratios of histories are stable under
  common admissible extensions with identical past-views — the
  ratios-only structure of paper 28, recovered as the weight
  system's invariant content. At this depth the swept corner
  (proposal branches) has every extension factor exactly `1/8`,
  which makes the law a `[THEOREM]` there; the census is kept as a
  tripwire (**28 tested, 0 violations**) `[EXACT]`. The law's
  *empirical* content begins where factors vary — the idle and
  arbitration branches — and this is declared.
- **THE DENSITY LAW** of paper 30 §4.2.

`[MY READING]` This is the most under-appreciated fact in the file.
**Ratios are law; absolute probabilities are not.** The
completion problem is precisely the problem of going from a
ratio-structure to a measure, and the dichotomy says that step
cannot be taken locally.

### 4.4 The flatness ladder, and what actually separates the levels

Gated on all 202 canonical diamonds `[EXACT]`:

| level | diamond violations |
|---|---|
| weight (`μ` factor products) | **0** |
| naive cut-normalized | **36** — exactly the census of §3.1 |
| gradient-completed | **0** |

And a `[THEOREM]` that prevents the obvious misreading: the
gradient leg's flatness is a **telescoping theorem** — *any*
cut-attached, class-constant `Z` gives flat diamond products
identically, because the chain product telescopes to boundary
values. The receipt gates this with an **arbitrary non-harmonic
class-constant probe passing 0/202** `[EXACT]`.

> **Therefore the separating content is CLASS-CONSTANCY — gauge
> invariance of the completion — and NOT harmonicity.**

A sequence-attached, non-class-constant `Z` does fail the diamond
check (**51 failing diamonds** for the receipt's deterministic
sequence probe; the count is representative-dependent because such
a probe is gauge-breaking by design, unlike the class-invariant
36) `[EXACT]`.

`[MY READING]` This is a trap the flatness result would otherwise
set. "The completed measure passes the action-level check that the
naive normalization fails" is true but says less than it appears:
flatness is buying you *gauge invariance*, not *harmonicity*. Do
not read the flat gradient leg as evidence that the gradient
completion is the right one.

---

## PART V — WHY THE QUANTUM LIFT DOES NOT ESCAPE

It is natural to hope that a quantum-mechanical formulation escapes
a classical obstruction. **It does not, and paper 30 says so
outright.**

The quantum lift *does* preserve ratios and normalize globally —
i.e. it appears to satisfy all three demands. But:

> the quantum lift ... **is the classical gradient completion at
> the `1/k` boundary in Hilbert dress** — the class and sequence
> bases are the two classical boundary choices ... **the quantum
> completion problem therefore begins exactly where the classical
> one stopped.**

So Hilbert space supplies no new resource here: it is *one
particular boundary choice*, re-expressed. The two natural bases
are exactly the two classical boundary choices.

**And its own step operator faces a three-horn obstruction** at the
arbitration layer:

1. **cut-independent** operators reproduce the arbitration-killing
   zero class (the same failure as §3.3);
2. **cut-dependent** operators require carrier overlap with the
   blind wire;
3. **dilations** re-import cut data.

**What the lift does establish**, and these are real results:

- the **kernel-layer lift is exact**: the arbitration click
  structure lifts exactly, `2/3`–`1/3` `[EXACT]`;
- a complete **fine-versus-coarse instrument pair**: order
  coherence exactly `1/6` under coarse sealing, `0` under fine
  `[EXACT]` — a discriminating observable;
- the operational D23 identifiability fiber.

A second grammar (ternary payloads) lifts the structural forms
tested — **two-of-two grammars, and no more is claimed** — exposes
the values as **toy-relative**, and shows kernel discrimination is
component-shape-dependent.

---

## PART VI — HORN (II): THE ROOT-FREE ROUTE, AND WHAT IT REDUCES TO

Truncated completions are **rooted**: the backward recursion needs
a terminal boundary, and that boundary is the imported object of
§4.1.

To avoid it you need a completion with no root — a positive
solution on the unbounded structure. Paper 30 reduces this, **one
way**, to a single question:

> **RESIDUE 1.** Does a strictly positive harmonic function exist
> on the **infinite-volume bisimulation quotient**? (17 states at
> the decided depth.)

That is the entire content of horn (II). If yes, the framework can
normalize itself without a boundary. If no, horn (I) is forced and
something boundary-like is part of the physics.

`[MY READING]` The dichotomy is therefore genuinely a fork in the
physics, not a technical inconvenience: **either the law is
forward-complete, or the world has a boundary condition.** The
mathematics forces one of the two and the corpus has not yet
determined which.

---

## PART VII — EVERY ADVANCE MADE ON RESIDUE 1

This is where the real work has gone. Sources:
`note-d44a-renewal-pumping-closure-theorem.md`,
`note-d46a-h1-structural-lemma.md`,
`note-d46b-martin-at-transport.md`, papers 30–32.

### 7.1 The change of enumeration space (the key move)

Instead of enumerating histories (which grows without bound),
enumerate a **bounded local-state abstraction** `sigma(h)`: the
abstraction of the full view of `h`, modulo base renaming. It
records

- the **per-actor holdings pattern** — which actors hold which
  non-superseded versions, as a partition-with-multiplicity over
  renamed bases (genesis base and renewal bases identified by the
  renaming);
- the **live-proposal structure** — per renamed base, the multiset
  of `(proposer, value-bit)` data of live proposals, with the
  edge/conflict structure of their components;
- the **superseded-base pattern**, restricted to bases still
  carrying any of the above. Dead structure no menu can see is
  dropped.

`sigma` is finite-valued **if** the dropped structure is truly
menu-invisible. **That invisibility is checked, never assumed** —
and it is exactly where the remaining gap lives (§7.5).

### 7.2 What is gated `[EXACT]`

- **Menu factorization on the cache:** `menu(h)`, as an
  event-multiset up to renaming with exact weights, is a function
  of `sigma(h)` on the **entire depth-6 cache (34,375 histories)**;
  census re-anchored `[1, 7, 39, 215, 1191, 6471, 34375]`. Zero
  exceptions.
- **Transition determinism on the cache:** `sigma(h + [e])` is a
  function of `(sigma(h), e-up-to-renaming)`, verified
  exhaustively.
- **The depth-free closure (CG3a):** breadth-first search on
  `sigma`-space from `sigma([])` closes at **36 states, 176
  edges** — a *frontier-exhausted* search, so no transition leaves
  the closed set.
- **The intrinsic partition:** `P_0` = menu shape, `P_{t+1}` = one
  probabilistic-bisimulation refinement under the committed
  per-candidate `(weight, target-class)`-multiset operator. Fixed
  point trajectory `[4, 5, 6, 6]` — reached at lookahead `t = 2`
  and stable thereafter — giving **SIX classes** with transfer
  `T_REF`.
- **The Perron package on the quotient:** `lambda = 2`;
  `f = (4, 4, 3, 7, 3, 3)/3` unique up to scale; **root = renewal**
  as one `sigma`-state; `pi = (1, 1, 2)/4` with mass transport
  exact.
- All three hypothesis laws verified exhaustively **through depth
  7, 179,783 histories, zero exceptions** — and this verification
  is explicitly labelled `[EVIDENCE]`, **never a premise** of the
  argument.

### 7.3 The conditional theorem

Three depth-indexed laws, **none implying another**:

- **(H0)** the view invariants hold at every depth: own-view alive
  holding a singleton; non-superseded holdings inside it; live
  proposals on the proposer's base; conflicting live pairs
  incomparable.
- **(H1) MENU FACTORIZATION at every depth.** `menu(h)`, as a
  renamed event-multiset with exact weights, is a function of
  `sigma(h)`. **Nontrivial because admissibility runs on OWN
  VIEWS that lag the full view `sigma` records** — the lag
  provably exists (the W2 witness exhibits it).
- **(H2) TRANSITION DETERMINISM at every depth.** Explicitly
  **NOT** a consequence of (H1).

> **`[THEOREM, conditional]` Assume (H0)–(H2). Then residue 1 is
> DECIDED at all depths at d42a scope**: `sigma` takes exactly 36
> values on histories of every depth; the intrinsic partition is
> at every depth the pullback of the abstract chain's
> bisimilarity; and the Perron package of §7.2 is the completion
> decision at every depth. QED (conditional).

**Declared verification scope**, which a reader must carry:
blockwise equality of the pullback with the committed intrinsic
partition is computed **in-receipt at length ≤ 4** and **at length
≤ 5 by the frozen round's referee** `[REFEREE-CARRIED]`; the
**four minlen-6 `sigma`-states are classified only via the
conditional argument.** No minimality is claimed for `sigma`'s
superseded marks or serialization. An earlier "pumping" route is
**retired** and is not a mechanism of this proof.

### 7.4 Scope boundary

The H1 lemma is **DELIVERY-FREE scope only** (D44b terminal). At
transport scope the objects change and must be re-established.

### 7.5 The remaining gap: H1 is NOT discharged

This is the current frontier, and the most recent attempt
**failed and was corrected under review**. D46a targeted H1 and
its own review refuted the framing:

> **`tau` is NOT an own-view object.** The **menu view strictly
> exceeds the noop cone on 1,016 of 12,942 actor-histories at
> depth ≤ 5 (7.9%)**, with at most 4 extra events, and in **ALL
> 1,016** cases the extra events are **OPPONENT-AUTHORED**. The
> menu view is idempotent (`0/12,942`).

Consequences, all on the record: the pin's target framing is
superseded; **(H1) is NOT discharged**; (H0) was restored after
being wrongly dropped; and a claim that "H2 is subsumed" was
withdrawn as inverted.

**So: residue 1 is decided at verified depth, conditional on
(H0)–(H2), and (H1) — the depth-free structural lemma — is residue
1's final named gap.**

### 7.6 Transport-scope advances, including three reversals

`note-d46b-martin-at-transport.md`, after review:

- **`root = renewal` DOES transfer** at matched horizon. An earlier
  "does not transfer" claim was a **horizon-mismatch artifact** and
  was withdrawn.
- **The pinned sector-normalized conditional is EXACTLY
  horizon-stable at the root** — reported as a negative before
  review, corrected to a positive.
- **Contraction is TRUE and strengthened** — but it is **not a
  constant rate**: the sequence is `0.738, 0.399, 0.086`.
- Deliveries **REDUCE** branching (the earlier claim had the sign
  wrong; peak at `D = 5`, down at `D = 6`).

`[MY READING]` The relevant language is Martin-boundary / R-theory:
harmonic functions, boundaries, `h`-transforms. The corpus has
independently arrived there, which is a good sign that horn (II) is
posed in the right vocabulary.

---

## PART VIII — WHAT IS OPEN, AND WHAT WOULD CLOSE IT

Ranked by leverage.

1. **`(H1)` — the depth-free menu-factorization lemma.** Closing
   it decides residue 1 at d42a scope outright and therefore
   decides which horn of the dichotomy holds at that scope. The
   route through own-view abstractions `tau` is **refuted**
   (§7.5); a new route is needed.
2. **`(H2)` — transition determinism at every depth.** May reduce
   to `(H1) + (H0)` or may need its own argument. **Currently
   undetermined and must be declared as such.**
3. **Is the ratio deformation PHYSICAL?** Horn (I) is
   mathematically available. Whether a theory whose completion
   deforms its own ratios at the root is acceptable *as physics* is
   an open question the corpus explicitly records rather than
   settles.
4. **The actor-factored intermediate class** — a declared
   round-2-decidable target between the refuted ratio-preserving
   class and the costly gradient class. **Not yet attempted.**
5. **The general-depth `1 + k/4` ladder is FALSE under current
   pricing** (with `h12` off-ladder), and its reconciliation is
   carried *into* the completion problem. This is unfinished
   business upstream of everything above.
6. **A known internal pricing divergence:** the D2H merge prices
   `1/16` under the embedded head versus `1/24` under the terminal
   d42b1 grammar. Exhibited and recorded; form-level results
   unaffected; not reconciled.
7. **Reading-relativity.** Which channel reading is physically
   privileged (D46e) and which sky definition is privileged (D47)
   are both open, and both are the same class of question: the
   corpus has structures whose conclusions depend on a
   representation choice nobody has justified.

---

## PART IX — THREE THINGS A NEW READER WILL OTHERWISE GET WRONG

### 9.1 The dichotomy is not a to-do item

It is a decided trilemma with a 36-diamond certificate. "Just
normalize the weights" is provably impossible without giving
something up. Any proposal that claims all three of (a), (b), (c)
is refuted before it is read.

### 9.2 "How many actors" is not a modelling choice

D48 (`note-d48-composite-line-pin.md`, LOG #413/#414/#415, round 1
terminal) tested whether actors can be merged:

- The **labelled record does not aggregate.** Non-injective actor
  maps send a positive fraction of admissible records to
  inadmissible images (admissible fractions 50%, 50%, 74%, 18%
  across four maps), and the fraction **falls with record length**
  (100% → 88% → 70% → 48%). The obstruction is the **mint chain**.
  Controls held: identity and bijective renaming are both 100%, so
  this is about how many actors there *are*, not what they are
  called.
- But the **causal order does aggregate**: of the failing images,
  **100%** have a causal poset realized by some admissible coarse
  record (10,608/10,608 at cap 4; 196,304/196,304 at cap 5
  `[REFEREE-CARRIED]`).
- **The obstruction is LOSS**, not impossibility: fine (4-actor)
  causal poset classes run `1, 2, 4, 9` at lengths 1–4 against
  coarse (2-actor) `1, 2, 3, 5`, widening to **19 vs 8** at length
  5.

**Do not conclude that the coarse description is meaningless.** Two
gates forbid that reading.

### 9.3 No laboratory number may be quoted through any of this

The bridge from corpus quantities to laboratory observables is
**BLOCKED** (`note-d41c-step3-bridge-declarations.md`, LOG #405).
The blocking reasons, all recorded:

- a **scale gap** of ~20 orders of magnitude (at Planck spacing, a
  proton rescaled to 1 mm record spacing is of order ten
  light-years);
- **the corpus cannot fix that scale** — paper 57's unified no-go
  gives exactly one record length with Newton's `G` provably
  un-fixable, so the record scale is a free parameter;
- a **layer gap**: records → background → quantum fields → atomic
  structure is at least three constructed layers, and **none of
  them is built**;
- and now §9.2's **loss** result, which re-founded the block.

The eight bridge correspondences are `[POSITED]`, **unsigned**, and
the sign-off block is **sealed**. `[MY READING]` — and this is the
practical upshot for anyone tempted to look for a prediction — **a
theory that has not chosen its measure cannot produce a rate.** The
completion dichotomy is upstream of every empirical claim, which is
the real reason it deserves the next campaign.

---

## PART X — WHERE EVERYTHING LIVES

**Papers** (in `v10/`):

| file | relevance |
|---|---|
| `relativistic-isp-v10-paper30-the-generated-record-and-its-completion.md` | **the primary source.** §1 grammar; §4 the ladder; §5.1–5.5 the whole completion decision; §6 the quantum lift |
| `relativistic-isp-v10-paper31-four-decisions-at-the-joints.md` | the residue ledger this work executes |
| `relativistic-isp-v10-paper32-the-boundary-of-closure.md` | residue 1 at verified depth; the dimension ladder; §6 the current residue ledger |
| `relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md` | the *other* diamond sense — do not confuse |

**Notes:**

| file | relevance |
|---|---|
| `note-d42b3-placement-and-the-discrete-ts-condition.md` | the decision in its sharpest form (D1–D4), incl. the D2 and D3 corrections |
| `note-d44a-renewal-pumping-closure-theorem.md` | `sigma`, the 36-state closure, the Perron package, the (H0)–(H2) conditional theorem |
| `note-d46a-h1-structural-lemma.md` | the H1 attempt and its refutation |
| `note-d46b-martin-at-transport.md` | Martin/`h`-transform structure at transport scope, with three reversals |
| `note-d43-corpus-audit-and-the-next-step.md` | names the completion a Doob `h`-transform |
| `note-d40-where-the-action-cocycle-lives.md` | the K-flat shape as an `h`-ratio/Doob form |
| `note-d41c-step3-bridge-declarations.md` | why no laboratory number may be quoted |
| `note-d48-composite-line-pin.md` | the actor-aggregability question |

**Receipts** (in `v10/code/`, outputs in `v10/data/`): all exact
rational arithmetic, standard library only, exit 0 required.

| receipt | what it gates |
|---|---|
| `d42b3_placement_exact.py` | the p/r/n admission layer + the completion decision |
| `d42b1_transport_exact.py` | delivery and merge; **the "no measure claim" disclaimer** |
| `d44a_closure_theorem_exact.py` | the closure theorem |
| `d46a_h1_lemma_exact.py` | the H1 attempt |
| `d46b_martin_transport_exact.py` | Martin-at-transport |
| `d48_composite_line_exact.py` | actor aggregability |

**The ledger:** `v10/LOG.md` — append-only, numbered, with
forward-corrections only. Never silently edited. Entries #300–#415
cover everything in Parts VII–IX.

**Review records:** `v10/reviews/*.md` — frozen; a round is
followed by repairs and a delta, and only then is a unit terminal.

---

## XI — THE ONE-PARAGRAPH SUMMARY

The framework specifies exactly what can happen next and the
*relative* weights of the options, and provably cannot turn those
into probabilities without giving something up. Demanding
normalization, foliation-invariance and untouched ratios together
is refuted by a 36-of-202-diamond certificate, because the natural
normalizer double-counts the causally blind join layer along
foliations that expose it. What survives is a Doob `h`-transform:
it works at every finite depth, with 313 parameters of boundary
freedom, and unavoidably tilts relative weights at 21 of 114 cut
classes including the root. The quantum lift does not escape this —
it *is* that classical completion at one particular boundary, in
Hilbert dress. The only alternative is a root-free completion,
which requires a strictly positive harmonic function on the
infinite-volume quotient; that is residue 1, it is decided at
verified depth on a six-state chain with `lambda = 2` and
`root = renewal`, and it is one lemma — (H1), whose most recent
attempted proof was refuted under review — from being closed. So
the open question is sharp: **is the record law forward-complete,
or does the world carry a boundary condition?** The mathematics
forces one of the two, and nobody yet knows which.
