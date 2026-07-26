# D56 — a bounded abstraction at TRANSPORT scope: PROBE / ADVISORY

> **STATUS: PROBE, ADVISORY, UNCOMMITTED.**  This is not a corpus unit.
> There is no pin, no ledger entry, and nothing here is citable.  Every
> claim below must be independently re-derived before any pinned unit
> relies on it.  The deliverables are
> `v10/code/d56_transport_sigma_probe.py` (exit 0, 283 s) and
> `v10/data/d56_transport_sigma_probe.out`.
> Scope everywhere: the **committed `d42b1_transport_exact.py`
> admission layer**, exec'd path-anchored (admission and pricing are
> never re-implemented), **two actors** unless a line says otherwise.

---

## 0. The answer in four lines

1. **[EXACT, depth-free] There is NO bounded menu-exact local-state
   abstraction at transport scope — for any design.**  Not "this sigma
   blew up": the *menu itself* is an unbounded function of the history,
   so no abstraction that determines menus can be finite.
2. **[MEASURED]** A properly quotiented, menu-exact `sigma` was built
   and verified (0 factorisation violations on all 30,729 histories to
   depth 5); it takes **1, 5, 17, 61, 191, 541, 1567** values at depths
   0..6 and its BFS is **NOT CLOSED at the 20,000-state cap** (level 9).
3. **[MEASURED]** The design this probe was *instructed* to use — D51's
   four projections on the FULL view — is **too coarse at transport
   scope** (3,656 menu-factorisation violations).  It had to be refined
   to a **join-view lattice**.  This is a finding about D51, not a
   detail of implementation.
4. **[MEASURED, correction]** D52's own probe table is reproduced
   exactly, but **its reading was wrong**: `cumulative == per-depth`
   holds because the per-depth state sets are **nested**, i.e.
   recurrence is *total*, not absent.

---

## 1. What had to be built, and why the instructed design failed

### 1.1 What the admission layer actually reads

Read off `d42b1_transport_exact.py`, not assumed:

| candidate | view `admissible()` builds | extra reads |
|---|---|---|
| `('p',a,b,x)` | `O_a` (a's own wire past, inclusive) | — |
| `('n',a)` | `O_a` | `admissible_arb_ckeys` on the **FULL** view |
| `('d',s,r,v)` | (built and discarded) — decision uses `own_view(s)` = `O_s` | — |
| `('m',a,pk,w)` | `O_a` | `admissible_arb_ckeys` (FULL) |
| `('r',a,C,W)` | the **join** `⋃_{a'∈props(C)} O_{a'}` | — |

So the object a menu is a function of is not one view but the **join
semilattice of own-views**, `V_S = View(h, pred, ⋃_{a∈S} O_a)` for
`∅ ≠ S ⊆ actors`.  At two actors that is exactly three views:
`V_A`, `V_B`, `V_{AB}` (and `V_{AB}` = the full view, because every
event carries an actor register).

**[MEASURED, depth ≤ 5]** `243,768` candidate views were compared with
the join predicted for their actor set: **0 exceptions**, and **0**
occurrences of the one structural escape I could identify (the arb
event's *new-version register*, which can join to an earlier arb that
minted the same name — a "renewal" collision).  The lattice is complete
on this window; **it is not proved complete at all depths** (§6, caveat
C3).

### 1.2 The instructed design, measured and refuted

The guidance specified: full view, D51's four projections
(`holdings(a)`, `superseded`, `live`/`props`, `components()`), plus
what deliveries need.  That design is implemented verbatim as
`sigma(mode='full0')` (with the same renaming quotient), and **M2
refutes it**: 3,656 violations over 30,454 equal-sigma pairs.

The minimal counterexample the run printed (idle padding trimmed):

```
h1 = [ p(B,v0,1), selfarb(B) ]
h2 = [ p(B,v0,1), selfarb(B), d(B→A, v0) ]
```

Both have **identical full-view four projections** — the delivery moves
no holding (A already holds `v0`), mints nothing, supersedes nothing.
It moves only **who knows**.  The menus differ:

| entry | h1 | h2 |
|---|---|---|
| `('n','A')` | 1/2 | 3/4 |
| `('p','A',w0,0)`, `('p','A',w0,1)` | 1/8 each | absent |

Before the delivery A's own view has not seen `v0` superseded, so A can
still propose on it; after the delivery it has.  **The full view cannot
see a delivery that only transports knowledge, and transport pricing is
exactly about knowledge.**  Hence the deviation from the guidance is
forced, and is the reason for §1.1.

> **[MEASURED] D51's four-projection reduction does not lift to
> transport scope.**  Any pinned unit that reuses it will be measuring
> a non-object.

---

## 2. `sigma` as built (the primary object), and its quotient

For every `∅ ≠ S ⊆ actors`, on the join view `V_S`:

* `holdings(a)` for `a ∈ S` — **the whole set, superseded members
  included** (delivery pricing reads them; this is not optional);
* `superseded`, restricted to referenced versions;
* the live-proposal triples `(proposer, base, payload)`;
* the conflict components `(base, members=(proposer,payload)*, edges)`
  — the committed `components()`/`edges()`, so poset-incomparability of
  live pairs survives as edge data;
* `merge_pairs(a)` for `a ∈ S`, as unordered version pairs (this is the
  form the admission layer reads; it already encodes "created in this
  view", "not superseded", "same base lineage", "incomparable
  creations").

**The version layer and THE QUOTIENT.**  Let `R` = every version named
anywhere above, and `R* = R ∪ {immediate bases / merge-pair members of
R}`.  Each `u ∈ R` keeps only renaming-invariant content —
`(kind, value, authors, initiator)` (actor names are **never**
renamed) — plus **pointers** `base→` (arb) or `pk→,pk→` (merge) into
`R*`.  Each `u ∈ R*\R` becomes an **opaque node: identity only, all
content and all of its own pointers dropped.**

Canonical form: 1-WL colour refinement on `R*` using only
renaming-invariant data (descriptors, per-view membership bits, live and
component decorations, merge-pair incidences, pointer colours in both
directions), then the **lexicographic minimum** of the
post-renaming-sorted serialization over all permutations *within* the
residual colour classes.  Genesis and "renewal" versions are identified
when and only when the state cannot tell them apart.

**[MEASURED]** On the whole family to depth 6 the refinement was already
discrete: **max colour class 1, max residual permutations 1, 0
permutation-cap hits** (cap 720, printed).  Canonicity is therefore not
in question on this window, and `|Aut| = 1` everywhere.

### 2.1 What is DROPPED (exactly)

1. **Lineage depth.**  The base of a version that nothing else
   references becomes an opaque node with no parent.  A chain
   `v0←v1←v2←…` is remembered only as far as the state actually names
   it.  *This is the quotient D52's T1 asked for.*
2. **Superseded marks** on versions nothing else references.
3. **Content of `R*\R` nodes** — names, values, authors, initiators.
   Nothing in the menu reads them (their only role is `base_of`
   equality, which needs identity, not content).
4. **`holdings`/`merge_pairs` of non-members** of `S` inside `V_S`.
5. **`created` as a separate projection** — `merge_pairs` is the form
   admission reads.
6. **All event indices and all order information** beyond what survives
   as component edges and merge-pair incomparability.

### 2.2 What is deliberately NOT dropped, and why it is fatal

`holdings(a)` keeps its **superseded** members, because
`deliver_options_in_view` enumerates `(receiver, version)` over the
*whole* holdings set.  §4 shows this single fact decides the question.

---

## 3. M1–M5

### M1 — exhaustive two-actor family, depth 6 [MEASURED, EXACT]

Anchors reproduced from the committed census: cumulative
`[1, 9, 69, 521, 3969, 30729]` and **243,769** to depth 6 — both MATCH.
Depth 6 is **exhaustive**; no sampling, no cut.

| depth | histories | distinct sigma | cumulative | NEW | recurring | nested? |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 0 | yes |
| 1 | 8 | 5 | 5 | 4 | 1 | yes |
| 2 | 60 | 17 | 17 | 12 | 5 | yes |
| 3 | 452 | 61 | 61 | 44 | 17 | yes |
| 4 | 3,448 | 191 | 191 | 130 | 61 | yes |
| 5 | 26,760 | 541 | 541 | 350 | 191 | yes |
| 6 | 213,040 | 1,567 | 1,567 | 1,026 | 541 | yes |

**Recurrence is total and it is not evidence of anything.**  The
per-depth sets are nested because appending `('n',a)` changes no
projection whatsoever, so every state reappears at every greater depth.
The only informative column is **NEW**, which grows by a factor ≈ 2.9
per level with no sign of turning over.

**The same correction applies to D52.**  Its table (reproduced exactly
below) has `cumulative == per-depth` for the *same* reason —
nestedness — and D52 read it as "no state ever recurs".  That reading is
backwards.

| depth | histories | D52 naive states | nested? |
|---|---|---|---|
| 0..5 | 1, 8, 60, 452, 3448, 26760 | 1, 5, 13, 39, 107, 275 | yes at every depth |

### M2 — menu factorisation [MEASURED, mandatory]

| abstraction | classes | equal-sigma pairs checked | violations |
|---|---|---|---|
| `sigma` (join-view lattice, §2) | 541 | 30,188 | **0** |
| `full0` (D51 four projections, full view only) | 275 | 30,454 | **3,656** |

Menus are compared as **renamed event multisets with exact `Fraction`
weights**, under the canonical label maps (over the whole automorphism
orbit; here trivial).  The `full0` row is also the **anti-vacuity
control**: the instrument does detect coarseness when it is there.

**Verdict: `sigma` is menu-exact on the entire depth-5 family.  It was
NOT menu-exact in its first (instructed) form; the refinement is
recorded in §1.2 with its counterexample.**

### M3 — transition determinism, and BFS [MEASURED]

`sigma(h+[e])` is a function of `(sigma(h), renamed e)`: **1,540
(state, event) pairs over 30,728 transitions, depth ≤ 4 exhaustive, 0
nondeterministic pairs.**  So the d44a BFS method is legitimate here.

Frontier-exhausted BFS on sigma-space, **hard cap 20,000 states / 480 s
(both printed)**:

```
level:  1     2     3     4     5     6     7      8       9
states: 5    17    61   191   541  1567  4679  14413  20000 (CAP)
```

**NOT CLOSED.**  The frontier at the cap still had 5,587 unexpanded
states.

### M4 — growth diagnosis: which component moves [MEASURED]

Distinct values per component of `sigma`, by depth (each component
canonicalised under the same label map):

| depth | vers | hold | sup | live | comps | mergepairs | holdings-counts | sigma |
|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 5 | 5 | 1 | 1 | 5 |
| 2 | 5 | 3 | 3 | 13 | 13 | 1 | 3 | 17 |
| 3 | 9 | 4 | 4 | 33 | 33 | 1 | 4 | 61 |
| 4 | 21 | 8 | 8 | 65 | 67 | 1 | 6 | 191 |
| 5 | 47 | 12 | 14 | 142 | 144 | 3 | 8 | 541 |
| 6 | 123 | 25 | 24 | 284 | 288 | 4 | 13 | 1,567 |

Structural maxima over each level:

| depth | max\|holdings\| | max\|R\| | max #live | max #comps | max #mergepairs |
|---|---|---|---|---|---|
| 4 | 3 | 3 | 2 | 2 | 0 |
| 5 | 3 | 3 | 2 | 2 | 1 |
| 6 | 4 | 4 | 3 | 3 | 1 |

**Reading, and it is a two-part answer:**

* At the *reachable depths*, the fastest-growing component is the
  **per-view live-proposal / component structure** (`live`, `comps`:
  284/288 distinct at depth 6) — i.e. **the knowledge lag between the
  three views**, which is precisely the coordinate that does not exist
  at d42a scope.  The version layer (`vers`, 123) is second.  The
  holdings *counter* is the slowest (13 distinct count-vectors).
* At *depth-free* level the ranking reverses: the counter is the one
  that is provably unbounded (§4).  The others are merely large here.

So a pinned unit must attack **both**: the view-product structure (which
is what explodes early) and the holdings counter (which is what makes
finiteness impossible at all).

### M5 — three actors, deterministic-walk spot check [MEASURED, SAMPLED]

200 walks, depth 10, LCG `x ← (1103515245x + 12345) mod 2^31`, **seed
20260726 printed**, candidates sorted by `repr` before indexing.
Sampled counts are **lower bounds**.

| depth | distinct (sampled) | cumulative | NEW | max\|holdings\| |
|---|---|---|---|---|
| 1 | 7 | 7 | 7 | 1 |
| 4 | 100 | 115 | 53 | 2 |
| 7 | 166 | 360 | 97 | 3 |
| 10 | 192 | 673 | 116 | 3 |

New states per depth are still ≈ 100 at depth 10 with no turn-over, and
`max|holdings|` still climbing.  The three-actor ladder (§4) has
`(n−1)·|H|` delivery options: `4, 6, 8, 10, 12` options at
`1/16, 1/24, 1/32, 1/40, 1/48`, sector total exactly `1/4` throughout.
**The two-actor conclusion looks width-stable.**

---

## 4. THE OBSTRUCTION — why this is a no-go and not a growth rate

**Construction (the self-arbitration ladder).**  `v_0 = genesis`; rung
`k+1` is `('p','A',v_k,0)` then the blind self-arb
`('r','A',{(A,v_k,0)},{(A,v_k,0)})`, which mints
`v_{k+1} = vname(v_k, {(A,v_k,0)}, 'A')`.

**[EXACT, mechanically verified for k = 1..10 in the committed layer]**

| rung | \|holdings(A)\| | delivery options | weight each | sector total | non-delivery menu = previous? |
|---|---|---|---|---|---|
| 1 | 2 | 2 | 1/8 | 1/4 | — |
| 2 | 3 | 3 | 1/12 | 1/4 | yes |
| 3 | 4 | 4 | 1/16 | 1/4 | yes |
| … | … | … | … | … | yes |
| 10 | 11 | 11 | 1/44 | 1/4 | yes |

Every rung admissible; `|holdings(A)| = k+1` exactly; the ten weights
pairwise distinct; delivery sector total exactly `1/4` at every rung.

**[EXACT, depth-free] Induction.**  `v_{j+1}` has strictly greater
nesting depth than `v_j`, so `v_0..v_k` are pairwise distinct.  `A`
proposed in every rung's ckey, so `holdings(A) ⊇ {v_0,…,v_k}`.  Only
`v_0..v_{k-1}` are superseded, so `('p','A',v_k,0)` is admissible and
the ladder extends for every `k`.  `deliver_options_in_view` reads the
**whole** holdings set, so A's delivery sector has exactly `k+1`
options, each priced `1/4 / (k+1)`.

**Therefore** the menu takes infinitely many values — in its
*cardinality* and in its *multiset of rational weights*, neither of
which any renaming can move.  If `sigma` is menu-exact then
`sigma(h) ↦ menu(h)` is well defined, so `sigma` has at least as many
values as there are menus:

> **[EXACT] No bounded menu-exact local-state abstraction exists at
> transport scope, for any design.  D52's T2 is answered: BLOW-UP, and
> by an obstruction, not by a growth curve.**

**Why d42a escapes it.**  Delivery-free, holdings are read only through
`prop_options_in_view`, which **skips superseded versions**, and the
non-superseded holding is a singleton (d44a SG2).  The unbounded
coordinate exists there too — it is simply invisible to the menu.
Transport makes it visible.  *The 36-state closure is a starvation
artifact of the same kind d42b1's P2 found for fork-freeness.*

---

## 5. What survives: sector totals and the lumped chain [MEASURED]

The no-go bites the *intra-sector split*, not the sector.  Measured
consequences:

* the delivery sector total is exactly `1/4` at every ladder rung, and
  the **non-delivery part of the menu is constant from rung 2 on**;
* define `lump` = `sigma` with each holdings set replaced by (its
  non-superseded part, `min(|holdings|, T)`).  Then, on the whole
  depth-5 family: **the non-delivery menu factors through `lump`
  exactly** (T=2: 0 violations / 30,236 pairs; T=3: 0 / 30,228);
* and the **delivery-LUMPED step distribution** (non-delivery events
  kept individually, the entire delivery sector aggregated by successor
  lump-state) **is a function of the lump state** — 0 violations over
  3,782 same-state pairs at depth ≤ 4, 187 lump states.  That is
  probabilistic bisimulation for the lumped chain, on that window.

**But the lumped chain does not close either, within the caps:** BFS,
T=2, cap 20,000/480 s → `1, 5, 17, 61, 187, 493, 1223, 3099, 8241,
20000 (CAP)` at level 9.  **[MEASURED, not decided]**

So: killing the counter is necessary and **not sufficient**.  The
residual explosion is the view-product structure of M4.

---

## 6. Caveats (binding)

* **C1.** The no-go is about **menu-exact** abstractions — exact
  weights *and* exact renamed event identity.  It does not exclude
  coarser objects (sector-level descriptions, lumped chains, level-
  structured / QBD or R-matrix descriptions).  It *does* exclude the
  finite transfer matrix that Perron theory needs at d42a.
* **C2.** `sigma` is menu-exact but **not proved minimal**.  Its
  measured curve is an **upper bound** on the minimal menu-exact state
  count at each depth.  The *lower* bound that matters is the ladder's:
  infinite.  The qualitative verdict is therefore design-independent;
  the growth *numbers* are not.
* **C3.** Join-view completeness (§1.1) is **[MEASURED to depth 5]**,
  0/243,768 exceptions.  The arb-renewal register escape is a real
  structural possibility that this window did not exhibit; a pinned
  unit must either rule it out or add those views.
* **C4.** M2 and M3 are finite-depth evidence (depth ≤ 5 and ≤ 4
  respectively), never premises.  M5 is a **sample**: lower bounds only.
* **C5.** Determinism: run with `PYTHONHASHSEED=0`; every canonical form
  is a post-renaming-**sorted** plain-tuple serialization (no raw
  frozenset reprs — the D49 A4 lesson).  All caps are printed by the
  script: exhaustive depth 6, menus to depth 5, permutation cap 720
  (0 hits), BFS 20,000 states / 480 s, 200 × depth-10 walks, seed
  20260726.
* **C6.** Nothing here is committed to git; no LOG entry was made.  The
  three files are untracked working-tree artifacts.
* **C7.** The script was run twice (the second run adds only the named
  witness of §1.2); **every count, curve and violation number was
  byte-identical between runs.**  That is reproducibility evidence, not
  a proof of order-independence.

---

## 7. What a pinned unit should gate

Pre-registered gates I would put in a D57-style pin, in this order:

1. **G1 (the no-go, first — it reframes everything else).**  Re-derive
   the ladder independently: for `k = 1..K` (K printed, ≥ 10) every rung
   admissible; `|holdings(A)| = k+1`; delivery options `= k+1` with
   pairwise-distinct weights `1/(4(k+1))`; sector total `= 1/4`.  Gate
   the **induction statement** as text, the arithmetic as a receipt.
   *Expected: PASS.*  If it fails, everything below is void.
2. **G2 (the D51 lift is dead).**  Gate the full-view four-projection
   abstraction as **NOT** menu-exact at transport scope, with the two
   printed histories as a named witness, and gate the join-view lattice
   as the replacement (`V_S` for all `∅ ≠ S ⊆ actors`).
3. **G3 (lattice completeness).**  Every candidate view built by
   `admissible()` equals the join of its actors' own views, at the
   declared depth — **or** the arb-renewal escape is exhibited and the
   lattice extended.  Do not assume it.
4. **G4 (menu-exactness of whatever sigma is proposed).**  Renamed
   event multisets **with exact weights**, all histories at the declared
   depth, zero violations, plus a *negative control* that the check can
   fail (the `full0` row serves).
5. **G5 (the D52 correction).**  Gate `nested(depth d) ⊆ (depth d+1)`
   and report NEW-per-depth, so that no future note reads
   `cumulative == per-depth` as "no recurrence" again.
6. **G6 (the honest replacement object).**  Since the finite chain is
   gone, pre-register *which* object replaces it before measuring:
   * the **delivery-lumped chain** — gate (a) non-delivery menu
     factorisation through the lump, (b) lumped-step probabilistic
     bisimulation, (c) its BFS with the cap printed.  This probe found
     (a) and (b) clean and (c) **not closed at 20,000**;
   * or a **level-structured (QBD / R-matrix / Martin-boundary)**
     description with `|holdings|` as the level — which connects to the
     already-built d46b transport-scope Martin/R-theory machinery rather
     than to Perron.
7. **G7 (scope hygiene).**  State that D49/D50's dichotomy settlement
   and d44a's 36-state closure remain **d42a, delivery-free, two
   actors**, that (H1) is still undischarged there (D51), and that
   D52's T3 branch ("only if T2 closes") is now **unreachable as
   written** — T4 is the live branch.

**And one thing a pin should NOT do:** do not pre-register an
expectation of closure or non-closure for a *coarser-than-menu-exact*
object.  D52 was right to record none; the ladder decides only the
menu-exact question.
