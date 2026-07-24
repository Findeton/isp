# D46a + D46c — round 1, hostile review (one round, two units)

**Reviewer:** independent referee (fresh session; no build context).
**Date:** 2026-07-24.  **Objects under review (both GREEN-UNREVIEWED,
first round):**

- **UNIT 1 — D46a (LOG #380):** `v10/note-d46a-h1-structural-lemma.md`,
  `v10/code/d46a_h1_lemma_exact.py`, `v10/data/d46a_h1_lemma_exact.out`.
- **UNIT 2 — D46c (LOG #382):** `v10/note-d46c-minkowski-certificates.md`,
  `v10/code/d46c_minkowski_certificates_exact.py`,
  `v10/data/d46c_minkowski_certificates_exact.out`.

Nothing in this review edits a committed file.  Every number below was
recomputed by the referee unless explicitly marked as a citation check.

---

## COMBINED VERDICT

| unit | verdict | BLOCKER | MAJOR | minor | nit |
|---|---|---|---|---|---|
| **D46a** — the H1 structural lemma | **REVISE — the mechanical core stands, the headline claim does not** | 2 | 4 | 6 | 1 |
| **D46c** — Minkowski certificates | **REVISE — the headline STANDS (independently reconfirmed); one control blocker; the declared OPEN is DISCHARGED in the unit's favour** | 1 | 4 | 6 | 1 |

**One-line each.**

- **D46a.** Every mechanical gate reproduces byte-identically and every
  cited D44a anchor checks out; the joint closure and the injectivity
  verdict are real.  But the §5 assembly does **not** follow from the
  two structural facts it names: the arrow `tau -> menus` is an
  undeclared THIRD conditional, and the referee has a machine-checked
  independence witness (mutant a9) in which both named facts hold and
  menu factorization fails.  D44a's (H0) is also silently dropped from
  the conditional list.  "RESIDUE 1 DECIDED OUTRIGHT" is not earned;
  what *is* delivered is a genuine reduction of H1 to a coarser,
  restricted factorization claim plus H2-under-a-new-name.
- **D46c.** The W6 headline is **true** — the referee rebuilt the poset,
  the coordinates and the checker from scratch and confirmed all 30
  ordered pairs, and independently confirmed order dimension exactly 3
  (so "beyond the two-clock rung" is earned).  But there is no control
  anywhere exercising the *spacelike* half of the checker, and a
  one-directional checker passes all 11 gates **while manufacturing a
  false positive headline**; and the OPEN it declared on W(3) is wrong
  in substance — the referee found an exact rational certificate for the
  full 18-event record in seconds, which falsifies the "difficulty
  localization" narrative attached to it in A3/§5/LOG #382.

---

# UNIT 1 — D46a (LOG #380), the H1 structural lemma

## 1.1 What the referee confirms (independent recomputation)

| claim | source | referee finding |
|---|---|---|
| receipt reproduces | rerun | **exit 0, 17 PASS / 0 FAIL, byte-identical to `v10/data/d46a_h1_lemma_exact.out`**; ~2:51 wall (LOG says ~2:11 — different machine, nit) |
| enumeration anchor `[1,7,39,215,1191,6471,34375]` | LG0a vs `d44a_closure_theorem_exact.out` | matches verbatim |
| 36 sigma states; growth `[11,19,28,32,36]` | LG0b vs D44a SG1 | matches verbatim |
| 36 joint states / 176 edges / spectrum `{0:1,1:4,2:6,3:8,4:9,5:4,6:4}` | LG1b vs D44a CG3a | matches verbatim |
| 160 keys; +16 at 6->7 = 176 | LG1a/LG3a/LG3b vs D44a CG2/CG7c | matches verbatim |
| 27,904 parents / 145,408 children / 179,783 total | LG1d vs D44a CG7 | matches verbatim |
| **cone-locality (structural fact (i))** | referee reading of `d42b3_placement_exact.py` | **GENUINE code-reading theorem.** `admissible(acts,e)` (lines 160-164) builds `View(acts2, pred, pred[j])` from the *candidate's past cone alone*; and `event_poset`'s `last[r]` bookkeeping restricted to a downward-closed subset containing that cone is provably unchanged (the last writer of every register in the cone is itself in the cone).  This is the unit's one genuinely discharged structural fact. |
| menu-view idempotence | referee probe (depth <= 5) | `sub_of(sub_of(h,a),a) == sub_of(h,a)` on **0/12,942** counterexamples — the menu-view family is closed under the construction, which is what makes the residual (below) a well-posed successor |

## 1.2 Findings

### BLOCKER A1 — the §5 assembly does not follow from the two facts it names; there is an undeclared THIRD conditional

**Where.** `note-d46a-h1-structural-lemma.md` §5 ("Given (i) + (ii):
sigma determines (tau_A, tau_B) (LG1 injectivity ...), tau_a determines
a's menu (LG2), hence sigma determines menus at ALL depths — H1");
receipt docstring lines 39-50; receipt verdict lines 849-858; LOG #380
("conditional on cone-locality + the abstract-update law ... sigma ->
tau -> menus discharges H1 AND H2 depth-free").

**The defect.** Fact (i) yields only `menu(h,a) = menu(sub_of(h,a),a)`.
Fact (ii) yields only that sigma determines `(tau_A, tau_B)` at all
depths.  Neither yields the second arrow, "**tau_a determines a's
menu**".  That arrow is LG2b/LG2c — a census over depths <= 7 — and it
is a genuinely independent hypothesis, namely **H1 restricted to the
menu-view sub-history family** (well posed, because that family is
closed: idempotence above).  It is nowhere listed among the conditionals.

**Machine-checked independence witness (referee mutant a9).** Replace the
layer's weight by another **cone-local** weight,
`q -> q * (1 + (|cone(e)| mod 2))`.  Cone-locality is preserved by
construction, and the abstract-update law is untouched (sigma and tau
read no weights at all — `sigma_raw` returns
`(hold, live, comps, refs, sup)`).  Result:

```
LG0a/b/c PASS   TG1 PASS   LG1a PASS   LG1b PASS   LG1c PASS
LG2a PASS       LG3a PASS  LG1d PASS   LG3b PASS
LG2b FAIL       LG2c FAIL                              exit = 1
```

Every gate that censuses facts (i) and (ii) — including the joint BFS
closure, the injectivity verdict and both sigma-keyed determinism gates
— **passes**, while menu factorization **fails**.  So `(i) + (ii)` do not
entail H1.  The assembly as written is invalid.

**Prescribed fix.** Restate §5 (and the receipt docstring/verdict, and a
forward-correcting LOG entry) as: *H1 REDUCES to (ii) [the abstract-update
law] + (iii) [menu factorization through tau on the menu-view family],
with (i) discharged as a code-reading theorem.*  Strike "closes H1 AND H2
at every depth" and every unqualified use of "DECIDED OUTRIGHT".  Name
(iii) as the successor target and record that it is strictly weaker than
H1 (restricted family, 8 tau values per actor rather than 36 sigma
values) — that weakening is the unit's real and defensible contribution.

### BLOCKER A2 — (H0) is silently dropped from the standing conditional list

**Where.** §5 "conditional on two structural facts"; LOG #380 likewise.

**The defect.** D44a §8's conditional theorem is explicitly *"Assume
(H0)-(H2)"* — (H0) being the SG2 view invariants **at every depth**.
D46a re-anchors those invariants only on the depth-<=6 cache (LG0c,
34,375 histories) and does not derive them from (i) or (ii): nothing in
the abstract-update law forces the raw view data of an arbitrary
depth-8+ history to satisfy SG2.  So invoking "the D44a §8 assembly" to
conclude "RESIDUE 1 DECIDED OUTRIGHT" while listing only two conditionals
understates the standing hypothesis set.

**Prescribed fix.** Restore (H0) explicitly: the honest conditional set
after D46a is **(H0) + (ii) + (iii)**, of which all three are
census-verified through depth 7 and none is discharged.  D44a's count of
undischarged depth-free laws was three; it is still three — what changed
is that the hardest of them (H1) has been replaced by a strictly weaker
one (iii).  Say exactly that.

### MAJOR A3 — "H2 SUBSUMED" is inverted: H2 is assumed under a new name, not discharged

**Where.** Receipt `[LG3 DECLARATION]` (lines 549-559), verdict
("H2 is subsumed by the same joint closure — one abstract-update law
powers both"), note §5 ("H2 rides the same closure"), LOG #380
("H2 SUBSUMED by the one joint closure").

**The defect.** The "abstract-update law" (ii), restricted to the sigma
coordinate, **is** (H2).  D44a §8 states in terms that (H2) is "NOT a
consequence of (H1)".  Folding both into one conditional is legitimate
bookkeeping; describing the result as H2 being *subsumed* reads as
elimination, which it is not.  Further, LG3a's content is, given LG1c's
injectivity, *mathematically identical* to D44a's CG2 — same 160 keys,
same 16 new keys at 6->7, target merely decorated with tau.  It carries
zero new information.

**Prescribed fix.** Replace "H2 SUBSUMED" with "H1 and H2 are now carried
by ONE undischarged conditional, which is H2 extended to tau"; label
LG3a as a re-anchor of D44a CG2 rather than a new result.

### MAJOR A4 — tau is not an own-view object; the "own-view lag" narrative is corpus-inconsistent

**Where.** Pin §2 ("the lemma must show the lag is MENU-INVISIBLE:
whatever full-view data an actor has not yet witnessed cannot change any
candidate it is offered or its weight"); pin §3 R-A ("own-view
determination"); receipt `[DEF]` block; LG1c's label and the verdict
("the own-view lag (D44a W2) is sigma-invisible ... what an actor has not
witnessed is FORCED by what sigma records"); LOG #380 same.

**The defect.** `sub_of(hk, a)` (receipt lines 244-257) calls
`cands_of(hk)` on the **full history** to find a's admissible
r-candidates and unions their past cones into the view.  Referee census
on the depth-<=5 cache (12,942 actor-histories):

- the menu view **strictly exceeds** a's own (noop) cone on **1,016**
  actor-histories (7.9%), max 4 extra events;
- in **1,016 / 1,016** of those the extra events are **not authored by
  a** — i.e. opponent events a has not witnessed in the D44a own-view
  sense.  This is precisely the *"join-view data the actor cannot see"*
  of the committed d42b3 **G-T1** result that amendment A1 itself cites;
- **104 of 2,224** own-view classes carry **different menus** — so pin
  §2's stated target, "the lag is MENU-INVISIBLE", is **false**, and the
  receipt does not establish it.

None of this breaks H1 (an intermediate abstraction need not be an own
view).  It breaks the *description* of what was proved.  The delivered
result is: the bare own view does **not** determine menus; the **menu
view** does, and the menu view's abstraction is sigma-determined.  The
prose says something stronger and different.

On the referee's charge "does tau smuggle in future information?" —
**no**: every event in the menu view is an event of `h`, reached through
past cones only, and the family is idempotent.  The object is past-only
but it is **not** a's own view, and it is not computable from a's noop
cone (that is exactly A1's reason for widening it).

**Prescribed fix.** Rename throughout: "menu view", never "own-view
abstraction"/"own-view determination"/"own-view sufficiency"; amend pin
§2's target statement (currently refuted by the unit's own A1 and by the
census above); restate LG1c's headline as "sigma determines the
menu-view abstraction", and delete "what an actor has not witnessed is
FORCED by what sigma records" or qualify it to the menu-view data.

### MAJOR A5 — LG2a cannot fail; it is a tautology of `sub_of`'s definition, and the design choice it protects has no control

**Where.** LG2a (lines 481-489), LG2c's extension, and the verdict's
"cone-locality made mechanical (436,316 comparisons)".

**The defect.** `sub_of(h,a)` is *defined* as the union of exactly the
cones `admissible()` consumes for a's admissible candidates.  Given the
cone-locality reading (confirmed above), (1) no a-admissible candidate at
`h` can be missing from the run on `sub` — its cone is in `sub` by
construction — and (2) no extra candidate can appear, since `sub ⊆ h` and
`candidates_for` enumerates from the full view.  So LG2a's outcome is
forced.  It is a mechanical restatement of fact (i), not evidence for it,
and 436,316 comparisons of a tautology is not 436,316 comparisons of
anything.  Compounding this, the receipt's **single most load-bearing
design choice** — A1's widening of tau's view from the noop cone to the
menu view — has **no in-receipt control**: A1's claim that the bare-cone
variant "would fail LG2 at depth 2" is asserted, never gated.  (Referee
mutant a1 supplies that control; see the mutation table.)

**Prescribed fix.** Relabel LG2a as "the mechanical restatement of fact
(i)"; drop the comparison count from the headline; promote A1's
bare-cone refutation to a gated in-receipt negative control.

### MAJOR A6 — three "independent anchors" are one fact restated

**Where.** LG1a's "160 distinct abstract keys (EXACTLY the D44a CG2
count: the joint keys do not outnumber the sigma keys)"; LG1b's
"adjoining tau to sigma creates NO new abstract states"; LG3a's "the
joint table adds no keys beyond the sigma table".

**The defect.** All three are immediate consequences of LG1c's
injectivity: once tau is a function of sigma, the joint state space, the
joint transition table and the sigma table are literally the same object
relabelled.  Presenting them as three corroborations of the closure
inflates the apparent evidence.

**Prescribed fix.** Mark them as corollaries of injectivity in their
labels.

### minors

- **a-m1.** The note has **two `## 4` headings** (line 61 "Gates
  (pre-registered)", line 97 "First-run amendments") and **two `## 5`
  headings** (line 90 "Scope", line 115 "The proof note").  Every
  citation of "§4 A1-A3" and "the §5 proof note" — including from the
  LOG and from this review — is therefore ambiguous.  Renumber.
- **a-m2.** LG5a's allow-list includes `str`, and the delivered
  abstraction values (`SIG`, `TAU`, `JREP` keys, `JT`/`ST` values) **are
  strings** (`repr(...)` of the canonical form).  A float that leaked
  into `sigma_raw` would be laundered into a clean `str` leaf and pass.
  The 21,088,527-leaf anchor protects the candidate cache's Fractions,
  not the abstraction.  State that scope, or serialize abstractions as
  tuples.
- **a-m3.** LG5b scans for exactly one literal pattern (`"check(Tr"+"ue"`).
  `check(lbl, 1 == 1)`, `check(lbl,  True)` (double space) or
  `check(lbl, not False)` all pass it.
- **a-m4.** A3 downgrades LG4b to a cache-level demonstration rather
  than a full variant BFS, so **no in-receipt control exercises the
  joint BFS closure itself** — the very step that carries the depth-free
  claim.  *Acquitted on substance:* referee mutant a6 (representatives of
  length >= 5 never expanded — D44a's own F4 mutant, re-armed on the
  joint system) is caught by LG1b/LG1c/LG1d, so the F4 frontier-exhaustion
  repair does carry over.  The gap is coverage, not soundness; add a6 as
  a gated control.
- **a-m5.** The R-B counterexample branch (`LG1c'`, lines 432-453) is
  dead code in the delivered run and is exercised by no control, so the
  "delivered-outcome discipline" is untested machinery.
- **a-m6 (a demonstrated-null silent green).** Referee mutant a8 drops
  the superseded marks from `ser`'s serialization: **17 PASS / 0 FAIL,
  exit 0** — every gate, including LG0b's `[11,19,28,32,36]` / 36-value
  anchors and LG1c's injectivity, is untouched, so the induced partition
  is blockwise identical.  This is not a missed tripwire: it is the
  **same nullity D44a already adjudicated at F3 (mutant m2)**, now shown
  to extend to the JOINT/tau system as well.  Record it — the marks are
  defensive over-specification for D46a too — and cite F3 so a future
  round does not re-litigate it as a live corruption.

### nit

- **a-n1.** LOG #380 records "~2:11"; the referee measures ~2:51 on this
  machine.  Harmless, but wall-clock claims in the LOG should carry the
  machine or be dropped.

## 1.3 Answers to the round's specific charges

- **(a) Is the MENU-VIEW the right object; does it smuggle future
  information?**  No future information (past cones only, idempotent
  family).  But it is **not** computable from a's own past at the moment
  of choice, and it is not "a's own view" — see MAJOR A4 with the 7.9% /
  1,016-of-1,016 census.  Convicted on the *label*, acquitted on
  *soundness*.
- **(b) Rebuild the joint BFS and re-verify injectivity.**  The receipt
  reruns byte-identically and every D44a anchor it re-anchors matches
  the committed `d44a_closure_theorem_exact.out` verbatim.  Injectivity
  is real, and mutant a9 shows it survives even when menu factorization
  is destroyed — which is the point of BLOCKER A1: injectivity is not
  the whole of H1.
- **(c) Is "H2 SUBSUMED" sound?**  The *census* is sound and is not an
  artifact of table construction (`ST` is keyed by `canon_pair` and
  conflict-checked).  The *word* is not: see MAJOR A3.
- **(d) Are the two structural facts code-reading theorems?**  (i) yes —
  confirmed against `d42b3` source.  (ii) **no** — it is a nontrivial
  mathematical claim about a canonical abstraction, of exactly the
  difficulty class of the original H1/H2, census-verified only through
  depth 7.  Bundling them as "two structural facts ... to be written as
  code-reading theorems" is a category error that materially understates
  the remaining gap.
- **(e) Mutations.**  See the table below.
- **(f) Hygiene.**  No `check(True)`; anchors are numeric and computed;
  reruns byte-identical; `__file__`-anchored layer path (cwd-robust —
  the house pattern, which D46c fails to follow).

## 1.4 Mutation battery — D46a (9 mutants; silent-green is a conviction)

Every mutant is the committed receipt with one textual substitution; the
layer path is repointed to the committed `v10/code` so mutants run from
the scratch tree.  "Result" is the mutant's own summary line.

| # | mutation | result | exit | verdict |
|---|---|---|---|---|
| a1 | `sub_of` -> **bare noop cone** (drop the r-candidate cones; the pin's pre-A1 definition) | TG1, LG2a, LG2b FAIL, then `KeyError` | 1 | **fires** — confirms A1's untested assertion that the bare own view cannot factor the menu |
| a2 | `sub_of` -> **the whole history** (tau := sigma; degenerate) | 12 PASS / 5 FAIL (TG1, LG2b, LG2c, LG4a, ...) | 1 | fires |
| a3 | **tau coarsened to a constant** | 12 PASS / 5 FAIL (TG1, LG2b, LG2c, LG4b, ...) | 1 | fires |
| a4 | **poison one joint transition target** (transposed tau pair on transition #17) | 15 PASS / 2 FAIL (LG1a, LG3a) | 1 | fires |
| a5 | **kill the renaming minimisation** in `canon_sigma` (take the first serialization) | 10 PASS / 7 FAIL (LG0b, LG1a, LG1b, LG1c, ...) | 1 | fires |
| a6 | **cap the joint BFS** (never expand representatives of length >= 5) — D44a's F4 mutant re-armed | 13 PASS / 4 FAIL (LG1b, LG1c, LG1d, LG5a) | 1 | fires — the F4 frontier-exhaustion repair carries over |
| a7 | **silently truncate the depth-7 extension** to the first 1,000 children | 13 PASS / 4 FAIL (LG1d, LG2c, LG3b, LG5a) | 1 | fires |
| a8 | **drop the superseded marks** from `ser` | **17 PASS / 0 FAIL** | **0** | *silent green* — **demonstrated null**, the D44a F3/m2 nullity extended to the joint system (see a-m6) |
| **a9** | **cone-local weight change** `q -> q*(1 + \|cone(e)\| mod 2)` — the BLOCKER A1 independence witness | LG0a-c, TG1, LG1a, LG1b, **LG1c**, **LG2a**, LG3a, LG1d, LG3b **PASS**; **LG2b, LG2c FAIL** | 1 | **the decisive mutant**: facts (i) and (ii) hold, H1 fails |

Eight of nine mutants exit 1; the ninth is a nullity already on the
corpus record.  The battery is healthy — the receipt's gates are not
vacuous.  What a9 shows is not a broken gate but a **broken argument**.

---

# UNIT 2 — D46c (LOG #382), the M^{2+1} certificates

## 2.1 What the referee confirms (independent recomputation)

The referee rebuilt the W6 poset, the crown alignment, the coordinates
and the causal checker **from scratch**, importing nothing from the
receipt, and then re-ran the resulting certificate through the receipt's
*own* `poset_of` / `verify` as a cross-check.

| claim | referee finding |
|---|---|
| **W6's event poset** | Own last-writer poset builder (`regs_of` for a delivery = `{sender, receiver}`) gives `preds = [[], [], [], [1,2], [0,2], [0,1]]` — **matches the committed d43d NG3b anchor verbatim**, and is exactly the crown S_3 |
| **W6's order dimension** | Independently computed over all 48 linear extensions: **not <= 2, is <= 3 => exactly 3.**  So "beyond the two-clock rung" is *earned* (1+1 embeddability <=> order dim <= 2, note-d45b §1 / Meyer) |
| **THE HEADLINE — W6 certified in M^{2+1}** | **CONFIRMED.**  Referee coordinates `a_j = (0, d_j)`, `u_i = (3/2, -d_i)` with `d = [(1,0), (-28/53, 45/53), (-28/53, -45/53)]`; own exact checker; **all 30 ordered pairs, 0 violations, both directions** |
| S_3..S_6 crowns | `M = 3136/2809, 2, 98/37, 162/53`; `T = 3/2, 3/2, 5/3, 7/4`; `T^2 >= M` and `T^2 < 4` in every case — all reproduced exactly |
| A2's "smallest-denominator T" | Independently searched: the minimal denominator admitting a rational in `[sqrt(M), 2)` is `2, 2, 3, 4` — exactly the denominators of the delivered `T`.  **A2 holds** |
| A3's tuple counts | family A = **3,840**, family B = **9,396**, total **13,236** — exact (family A's `be <= al` skip and family B's `T <= tc` skip both reproduce) |
| W(3) rebuild | 18 events over 18 actors, uniform weight **1/68** (matches the d45b ZG2 census), crown induced subposet **= S_3** |
| the crown-shape detector | **Sound, and in any case not load-bearing.**  `crown_shape` verifies the full `mins x uppers` incidence pattern and, since minima have no predecessors and maxima no successors, the min-min / up-up / up-min relations are forced; `mins` and `ups` are disjoint with `2n = N`, so they exhaust the poset.  And even a wrong alignment cannot transport a bogus certificate: `verify(CW6, pts6)` re-checks **all 30 ordered pairs against the poset itself** |
| floats (A1) | **Confirmed, and stronger than declared.**  `spread()`'s float `atan2` ordering touches nothing gated; every selected vector is an exact rational unit vector.  Indeed the equal-spacing heuristic is not needed at all — *any* `n` distinct rational unit directions give `M = 2 + 2 max d_i·d_j < 4` |
| determinism | rerun byte-identical; `PYTHONHASHSEED=0` and `=7` both byte-identical; exit 0; ~6 s |
| doctrine (KG3-b) | No negative-embeddability assertion appears anywhere in source or OPEN text — the *substance* of KG3 holds (the *scan* does not; see c-m4) |

## 2.2 Findings

### BLOCKER C1 — nothing controls the spacelike direction, and a one-directional checker silently manufactures a false headline

**Where.** `verify()` (lines 65-74) and KG0-c, the unit's only negative
control (lines 165-172).

**The defect.** KG0-c perturbs one certificate point by `+7` in `t`,
which breaks a pair that the poset requires to be **causal**.  It
therefore exercises only the `order => causal` half.  **No control
anywhere exercises `incomparable => spacelike`** — the half that makes a
certificate a certificate rather than a mere monotone map.

**Referee mutant c6** weakens `verify()` to
`if C[i][j] and not causal(...)` (order => causal only).  The receipt
then reports:

```
[PASS] KG0-c THE CHECKER FIRES (negative control) ...
[PASS] KG2-b THE COMMITTED W(3) COURIER RECORD IS CERTIFIED IN M^{2+1}:
       ... receives an EXACT rational certificate on ALL 306 ordered
       pairs ...            (parameters searched = 3862)
[SUMMARY] 11 PASS / 0 FAIL  (0 declared OPEN outcome(s))
```

Exit 0, every gate green, the OPEN silently gone, and a **false positive
headline** printed in the campaign's own voice.  A single deleted
condition converts a declared OPEN into a fabricated certificate with no
tripwire firing anywhere.  Per the campaign's own discipline
(silent-green = conviction) this is a blocker.

*The delivered run is not wrong* — the referee verified the real W6
certificate in both directions independently.  The blocker is that
nothing in the receipt would have noticed if it were.

**Prescribed fix.** Add a gated negative control that satisfies every
`order => causal` constraint and violates exactly one incomparability —
e.g. the S_3 crown at `T = 2` (then `T^2 = 4 = |2 d_i|^2`, so each upper
becomes causally above its own non-dominated minimum while all required
relations survive).  Gate it to FAIL.  Referee mutant c2 (`T` forced to
2) shows KG1 does catch that construction, so the control is one line.

### MAJOR C2 — the OPEN is DISCHARGED: an exact M^{2+1} certificate for the full 18-event W(3) record exists, and the "difficulty localization" is false

**Where.** §4 A3, §5 ("The full 18-event W(3) courier record is OPEN"),
the `declare_open("KG2-b", ...)` text, LOG #382.

**What the referee did.** 40 random restarts of a penalty hill-climb in
floats (times seeded from the poset's height function), then
**rationalized at denominator 64 and verified EXACTLY**.  Result: a
certificate on **all 306 ordered pairs, 0 violations**, confirmed twice —
under the referee's own checker and under **the receipt's own
`poset_of` / `verify`** (`ok = True, witness = None`).  Coordinates in
Appendix B.  Wall time: seconds.

**Consequence.** The OPEN itself was correctly *scoped* (never a negative
claim — KG3 held), but the interpretation bolted onto it is wrong:

> "the census localizes the difficulty: the dominant first-violations are
> CHAIN-ACCUMULATION pairs ... the courier firewall's own signature"

There is no difficulty and no firewall signature.  Both searched families
are simply over-constrained in the same two ways: they pin all three
minima at `t = 0` on the unit circle, and they force all three uppers to
a **common** height `T`.  A certificate needs neither.  The referee's
solution has minima at distinct negative times spread over `[-55/64,
-1/4]` and uppers at three different heights (`187/32`, `393/64`, `5`).

**Prescribed fix.** Convert KG2-b from OPEN to **CERTIFIED**, carrying the
referee's parameters (or a re-derived rational family) into the receipt
as a gated certificate; delete the chain-accumulation localization from
A3, §5 and the LOG; record the actual lesson — the two families' shared
symmetry assumptions, not the record's structure, were the obstruction.

### MAJOR C3 — the first-violation census is scan-order biased and cannot localize anything

**Where.** `key = (w[0] // 3 * 3, w[1] // 3 * 3, w[2])` (lines 397, 464)
and the printed bucket table.

**The defect.** `verify()` returns the **first** failing ordered pair in
lexicographic `(i, j)` order, so element 0 dominates by construction —
and indeed all four printed buckets have `i`-block 0.  Referee
recomputation on the receipt's own family A:

```
FIRST-violation buckets (the receipt's method):
  [(0,12,True):1772, (0,9,True):1100, (0,3,True):920, (0,12,False):48]
ALL-violation buckets (unbiased):
  [(3,12,True):18336, (6,12,True):11488, (0,12,True):10476,
   (3,6,True):10240, (3,9,True):9952, (0,9,True):9084]
```

The genuinely dominant violated pairs are **L-layer vs C-layer**,
involving no minimum at all.  Separately, the receipt's own top printed
bucket, `((0,15,False), 5664)`, is a **minimum vs UPPER pair required
SPACELIKE** — the crown diagonal — which is *not* what "a minimum
required below a LATE member of a hub chain" describes; and it comes
**entirely from family B** (family A produces none of it).  So the
narrative does not even match the numbers it cites.

**Prescribed fix.** If a census is kept at all, census **all** violated
pairs, and label the buckets by layer name rather than by index blocks.

### MAJOR C4 — KG0-b silently deviates from the pin

**Where.** Pin §2 KG0: *"regression: the 1+1 two-clock certificates of the
committed 2D chains (SIG_KR, h5, CH or a subset — light-cone coordinates
from their realizer pairs)"*.  Receipt lines 149-163.

**The defect.** The receipt regresses an **ad-hoc 5-element realizer
pair** (`REAL1 = a,b,c,d,e`, `REAL2 = b,a,d,c,e`, i.e. the poset
`{a,b} < {c,d} < e`) and touches **no committed object**.  SIG_KR, h5 and
CH appear nowhere in the source.  No amendment in §4 (A1-A4) declares the
deviation; §5 quietly says "a realizer pair", so the note is honest while
the pin is unmet.

**Prescribed fix.** Either regress at least one committed 2D chain
(`SIG_KR(n=4)` or `h5(n=5)` from d43d, whose two-clock `(b, chi)` ranks
are already committed), or declare the deviation as amendment **A5** with
the reason.

### MAJOR C5 — KG4-a's anchored leaf count is wrong (mutable-default accumulator)

**Where.** `def walk(o, n=[0])` (lines 562-572) and
`LEAVES += walk(obj)` (line 577).

**The defect.** `n=[0]` is a **mutable default shared across all calls**,
and `walk` returns the *running total*, not the count for the object just
walked.  The caller then *adds* those running totals, producing a
triangular accumulation.  Referee recomputation: the true per-object leaf
counts are `[15, 108, 6, 136, 16]`, **true total 281**; the accumulation
reproduces the printed **813** exactly.  The purity *property* is
unaffected (an impure leaf raises `TypeError` and flips `pure`), but the
anchored census number is false — and the campaign treats anchored counts
as tripwires.  Additionally, KG4-a never walks the headline's own
certificate `pts6`, nor the W(3) points.

**Prescribed fix.** `def walk(o)` with a local counter (or reset `n[0]`
per object); re-anchor at **281**; add `pts6` to the walked objects.

### minors

- **c-m1 (cwd-fragile).** Line 243, `_SRC = 'v10/code/d42b1_transport_exact.py'`
  is a **relative** path.  Run from anywhere but the repo root the
  receipt dies with `FileNotFoundError` (verified).  D46a's
  `__file__`-anchored pattern is the house standard; adopt it.
- **c-m2 (dead / lossy search bookkeeping).** Family B's success tuple
  `(T, e, f, tl, dm, tc, pts)` **drops `dc`** — had family B fired, the
  printed parameters would not reproduce the certificate.  `FAMILY = 'B'`
  is assigned and never read.  The print's `len(found) == 7` predicate is
  true for both families and conveys nothing.
- **c-m3 (mismatched console count).** The console line reads "no
  certificate in the searched family — **3840** exact parameter tuples"
  while the buckets it prints on the same line merge families A **and** B
  (13,236).  Only the OPEN text gets it right.
- **c-m4 (near-vacuous doctrine scan).** KG3-a inspects **3 of 614**
  source lines — only those containing `"spacetime"` or
  `"minkowski dimension"`, while the receipt writes `M^{2+1}` throughout
  — and its marker list includes `'no '` and `'not '`, which almost any
  English prose satisfies.  It cannot detect the claim it is designed to
  detect.  Scan for `M^{`/`2+1`/`causal order` too, and require a
  positive scope marker, not a stopword.
- **c-m5 (two demonstrated-null mutants).** Referee mutants c3
  (`dt <= 0` -> `dt < 0`, i.e. admitting the zero-interval coincident
  point) and c4 (`crown_shape` returns the **unaligned** `ups`) both pass
  all 11 gates.  c3 is null because no two certificate points coincide;
  **c4 is null only by luck** — for W6 the index order `[3,4,5]` happens
  to equal the crown alignment `[3,4,5]`, so the alignment logic, the
  only computational content of the "transport" step, is exercised by
  nothing.  Add a witness whose alignment is a non-identity permutation.
- **c-m6 (half the headline is imported, not gated).** "Beyond the
  two-clock rung" rests on W6 **not** embedding in `M^{1+1}`, i.e. order
  dimension > 2 — imported from d43d's `dim<=2 = False` and never
  re-derived in-receipt.  The referee re-derived it (dimension exactly
  3), and it is a ~10-line check over linear extensions.  Add it, so the
  sandwich (not 1+1, yes 2+1) is closed inside one receipt.

### nit

- **c-n1.** `spread()`'s docstring justifies equal spacing by
  "maximising the slack `2 - max|d_i+d_j|`".  Unnecessary: the
  construction succeeds for **any** `n` distinct rational unit
  directions, since `|d_i+d_j|^2 = 2 + 2 d_i·d_j < 4` whenever
  `d_i != d_j`.  Saying so makes A1's float declaration stronger — the
  floats are not merely ungated, they are inessential.

## 2.3 Answers to the round's specific charges

- **(a) Verify the W6 certificate independently.**  Done, from scratch,
  poset and coordinates and checker: **0 violations on all 30 ordered
  pairs**, with order dimension independently pinned at exactly 3.  **No
  false headline here** — this one is real.
- **(b) Is `crown_shape` sound / could it transport a bogus certificate?**
  Sound (see the table in §2.1), and structurally incapable of causing a
  false certificate because `verify` re-checks every ordered pair against
  the poset.  Its alignment branch is nonetheless untested (c-m5).
- **(c) The S_n certificates and the T search.**  All reproduced exactly,
  including the minimal-denominator property.
- **(d) Do floats touch anything gated?**  No — confirmed, and the
  heuristic they implement is not even needed (c-n1).
- **(e) Is the OPEN properly scoped; could a third family succeed?**
  Scoped correctly (no negative claim anywhere).  And yes — a third
  family succeeds **immediately**; see MAJOR C2 and Appendix B.
- **(f) Mutations + hygiene + LOG fidelity.**  See the table below.  LOG
  #382's numbers all check out (`T = 3/2, 3/2, 5/3, 7/4`; 30 pairs;
  13,236 tuples; 813 leaves — the last being wrong in the receipt, not in
  the LOG's transcription); LOG #382 does repeat the false
  chain-accumulation localization and so needs the same forward
  correction as A3/§5.

## 2.4 Mutation battery — D46c (6 mutants)

| # | mutation | result | exit | verdict |
|---|---|---|---|---|
| c1 | corrupt W6 (`('d','E','F')` -> `('d','E','B')`, destroying the crown) | 10 PASS / 1 FAIL (KG2-a) | 1 | fires |
| c2 | force the crown height `T = 2` (`T^2 = 4`, diagonal becomes causal) | KG1 FAIL, then crash | 1 | fires |
| c3 | `causal`: `dt <= 0` -> `dt < 0` | 11 PASS / 0 FAIL | **0** | *silent green* — **demonstrated null** (no two certificate points coincide in space) |
| c4 | `crown_shape` returns the **unaligned** `ups` | 11 PASS / 0 FAIL | **0** | *silent green* — **null by coincidence** for W6 (c-m5) |
| c5 | uppers placed at `+d_i` instead of the antipode `-d_i` | 9 PASS / 2 FAIL (KG1, KG2-a) | 1 | fires |
| **c6** | `verify` checks **only** `order => causal` | **11 PASS / 0 FAIL, 0 OPEN, false W(3) headline** | **0** | **BLOCKER C1** |

---

# CROSS-CUT — cited facts checked against the committed sources

| citation | in | committed source | status |
|---|---|---|---|
| `[1,7,39,215,1191,6471,34375]` | D46a LG0a | `d44a_closure_theorem_exact.out` (SG0) | OK |
| 36 sigma values; `[11,19,28,32,36]` | D46a LG0b | d44a SG1 | OK |
| 36 states / 176 edges / spectrum `{0:1,1:4,2:6,3:8,4:9,5:4,6:4}` | D46a LG1b | d44a CG3a | OK |
| 160 keys | D46a LG1a, LG3a | d44a CG2 | OK |
| 16 new keys at 6->7, 176 total | D46a LG3b | d44a CG7c | OK |
| 27,904 / 145,408 / 179,783 | D46a LG1d | d44a CG7 | OK |
| (H0)/(H1)/(H2) "none implies another"; "(H2) NOT a consequence of (H1)" | D44a §8 | note-d44a §8 | OK — and **contradicts** D46a's "H2 SUBSUMED" framing (MAJOR A3) |
| W2 own-view lag witness | D46a §2, LG1c | note-d44a §7 (F1) | OK as a citation; **misapplied** (MAJOR A4) |
| d42b3 G-T1 / D3 "own views equal, menus differ" | D46a A1 | `d42b3_placement_exact.out` lines 9-10 — *"the excess lives in join-view data the actor cannot see"* | OK, and it is the corpus's own refutation of the "own-view" label (MAJOR A4) |
| D44b = delivery-free scope boundary | D46a header | note-d44b §3 | OK |
| W6: 6 deliveries, 6 actors, each admissible at 1/20, poset exactly S_3, `dim<=2 = False` | D46c KG2-a | `d43d_dstar_generated_exact.out` NG3b | OK — referee-reproduced independently |
| W(3): 18 events, 18 actors, weight 1/68, crown subposet S_3 | D46c KG2-b0 | `d45b_sn_ladder_exact.out` ZG2 | OK |
| "order dim <= 2 <=> 1+1 embeddability (Meyer); dim-3 orders exist that embed; order dimension is never a spacetime-dimension estimator" | D46c §1/KG3 | note-d45b §1 doctrine | OK — D46c complies with the binding doctrine |
| LOG #380 numbers (36/176, 179,783, 436,316, 160+16=176, 21,088,527 leaves, 17/17) | LOG | receipt output | OK (wall time ~2:11 vs referee ~2:51 — nit) |
| LOG #382 numbers (`T = 3/2,3/2,5/3,7/4`; 30 pairs; 13,236 tuples; 11/11 + 1 OPEN; 813 leaves) | LOG | receipt output | transcription OK; **813 is wrong at source** (MAJOR C5), and the chain-accumulation localization is **false** (MAJOR C2/C3) |

---

# APPENDIX A — independent-recomputation inventory

Everything the referee computed independently, with the artifact that
produced it (all under the session scratchpad, none committed):

| # | check | script | outcome |
|---|---|---|---|
| R1 | D46a rerun vs committed `.out` | direct | byte-identical, exit 0, ~2:51 |
| R2 | D46c rerun vs committed `.out`, `PYTHONHASHSEED` 0 / 7 / unseeded | direct | all byte-identical, exit 0, ~6 s |
| R3 | D46c cwd-robustness | run from `/tmp` | **FileNotFoundError** (c-m1) |
| R4 | W6 poset rebuilt from scratch; order dimension | `indep_d46c.py` | `[[],[],[],[1,2],[0,2],[0,1]]`; dim not<=2, is<=3 => **3** |
| R5 | W6 certificate rebuilt + checked with own checker | `indep_d46c.py` | **0 violations / 30 ordered pairs** |
| R6 | S_3..S_6 `M`, `T`, minimal-denominator property | `indep_d46c.py` | reproduced exactly |
| R7 | family A / B tuple counts | `indep_d46c.py` | 3,840 / 9,396 / 13,236 |
| R8 | W(3) rebuild; crown induced subposet | `indep_d46c.py` | 18 events, S_3 |
| R9 | **W(3) third placement family** (hill-climb + rationalize) | `w3_family_c.py` | **exact certificate found**, 306/306 |
| R10 | that certificate under the **receipt's own** `poset_of`/`verify` | `confirm_w3.py` | `ok = True, witness = None` |
| R11 | first-violation vs all-violation census on family A | `w3_family_c.py` | scan-order bias demonstrated (MAJOR C3) |
| R12 | KG4-a true leaf count; reproduction of 813 | `confirm_w3.py` | true 281; 813 reproduced from the accumulator bug |
| R13 | KG3-a scan coverage | `confirm_w3.py` | 3 of 614 lines |
| R14 | D46a menu-view vs own (noop) cone census, depth <= 5 | `tau_provenance.py` | strictly larger on **1,016 / 12,942** (7.9%), max 4 extra events |
| R15 | are the extra events opponent-authored? | `tau_provenance.py` | **1,016 / 1,016** yes |
| R16 | menu-view idempotence | `tau_provenance.py` | **0 / 12,942** violations |
| R17 | do equal own views force equal menus? | `tau_provenance.py` | **no** — 104 / 2,224 own-view classes split (refutes pin §2's target) |
| R18 | cone-locality as a code-reading fact | source reading of `d42b3` lines 160-164 + `event_poset` | **holds** |
| R19 | D44a anchor cross-check (8 numbers) | grep of `d44a_closure_theorem_exact.out` | all match |
| R20 | mutation batteries | `mut_d46a.py`, `mut_a9.py`, `mut_d46c.py` | 9 + 6 mutants, tables above |

---

# APPENDIX B — the referee's W(3) certificate (discharges KG2-b's OPEN)

Poset: `W_build(3)` — 18 events, indices 0-2 = `MIN_j` (`m_j -> M_j`),
3-8 = the `L` layer (`m_j -> c_ij`, `LIDX` order), 9-14 = the `C` layer
(`c_ij -> h_i`), 15-17 = the uppers (`h_i -> t_i`).  Exact rational
`(t, x, y)`; verified on **all 306 ordered pairs, both directions**, by
the referee's checker *and* by the receipt's own `verify`:

```
e0  = (-1/4,    13/64,   75/32)     e9  = (3/4,     55/16,   61/32)
e1  = (-7/16,   241/64,  153/64)    e10 = (329/64,  187/64, -77/32)
e2  = (-55/64, -37/16,  -165/32)    e11 = (233/64,  11/64,  -25/32)
e3  = (27/64,   211/64,  127/64)    e12 = (81/16,  -29/64,  -95/64)
e4  = (11/64,  -3/2,    -295/64)    e13 = (259/64, -1/16,   -1/8)
e5  = (69/64,   53/64,   87/64)     e14 = (149/32, -23/64,   5/16)
e6  = (3,      -43/64,  -137/64)    e15 = (187/32,  201/64, -195/64)
e7  = (127/64,  13/8,    65/64)     e16 = (393/64, -89/64,  -125/64)
e8  = (55/64,   3,       127/64)    e17 = (5,      -19/32,   31/64)
```

Method: penalty hill-climb in floats (seed 20260724, 40 restarts, times
initialized from the poset height function), first exact solution at
trial 6; rationalized at denominator 64; then checked in Fractions.  The
floats are search-only — the certificate above is verified exactly, and
the receipt's own `verify` accepts it.  Note it breaks **both**
symmetries the committed families impose: the minima sit at three
different (negative) times rather than all at `t = 0`, and the uppers sit
at three different heights rather than a common `T`.

---

# APPENDIX C — reproduction

All referee scripts live in the session scratchpad
`.../scratchpad/rw/` and import nothing from each other:

```
# receipts, as committed
cd /Users/felixrobles/workspace/isp
python3 v10/code/d46a_h1_lemma_exact.py     # 17 PASS / 0 FAIL, ~2:51
python3 v10/code/d46c_minkowski_certificates_exact.py   # 11 PASS + 1 OPEN, ~6 s
PYTHONHASHSEED=0 python3 v10/code/d46c_minkowski_certificates_exact.py
cd /tmp && python3 /Users/felixrobles/workspace/isp/v10/code/d46c_minkowski_certificates_exact.py
                                            # FileNotFoundError (c-m1)

# referee scripts
python3 <scratch>/indep_d46c.py       # R4-R8: W6 poset, dimension, certificate, S_n, counts
python3 <scratch>/w3_family_c.py      # R9, R11: the third family + the census-bias test
python3 <scratch>/confirm_w3.py       # R10, R12, R13: cross-check under the receipt's own verify
python3 <scratch>/tau_provenance.py   # R14-R17: the menu-view provenance census (~40 s)
python3 <scratch>/mut_d46c.py         # c1-c6 (~40 s total)
python3 <scratch>/mut_d46a.py         # a1-a8 (4-way parallel, ~10 min)
python3 <scratch>/mut_a9.py           # the BLOCKER A1 independence witness (~3 min)
```

Mutant sources are written to `<scratch>/mut_c*.py` and
`<scratch>/muta_a*.py`; each is the committed receipt with a single
textual substitution (D46a mutants additionally repoint `_here` to
`/Users/felixrobles/workspace/isp/v10/code` so they can run outside the
repo tree — this repointing is inert with respect to every gate).

---

# WHAT THE REFEREE WOULD ACCEPT AT THE NEXT ROUND

**D46a.**  Keep every gate.  Rewrite the claim.  The delivered,
defensible result is: *cone-locality is a code-reading theorem; sigma
determines the menu-view abstractions tau_A, tau_B (36-state closure,
injective projection, zero exceptions through depth 7); and menus factor
through tau (zero exceptions through depth 7).  Hence H1 REDUCES to the
abstract-update law (= H2 extended) plus menu factorization through tau
on the menu-view family — a strictly weaker residue than H1 itself, on a
family with 8 values per actor instead of 36.  Residue 1 remains decided
at every verified depth and conditional above it, on (H0) + (ii) +
(iii).*  That is a real step and it survives every attack in this round.
"Outright" does not.

**D46c.**  The headline is safe and should be stated more precisely
("W6's causal order is the crown S_3 — committed at d43d — and S_3 is
certified in M^{2+1} by an exact rational antipodal construction; W6 has
order dimension 3, so it does not embed in M^{1+1}").  Add the spacelike
negative control (C1), convert the W(3) OPEN to CERTIFIED (C2), delete
the localization narrative (C2/C3), declare or repair the KG0-b pin
deviation (C4), and fix the leaf-count anchor (C5).  With those, D46c is
the stronger of the two units.

---
---

# DELTA — round-1 repairs (commit `b1323f5`; LOG #394 conversions, #395 receipt repairs)

Reviewed 2026-07-24 against the committed tree.  Round-1 body above is
untouched.  Everything below was re-executed by the referee.

## DELTA VERDICT

| unit | delta verdict | round-1 items closed | residual |
|---|---|---|---|
| **D46c** | **DELTA CLEAN — converts to TERMINAL** | C1, C2, C3, C4, C5 + all 4 assigned minors | 2 recorded non-blocking nulls (c-m5), c-n1 cosmetic |
| **D46a** | **DELTA NOT CLEAN — 1 BLOCKER, 1 minor; do not convert until D1 is applied** | A4, A5, A6 (receipt); A1, A2, A3 (note §6 + LOG #394) | **D1: the receipt's own prose still asserts everything §6 retracts** |

---

## D46c — verification of the repairs

**Reproduction.** 14 PASS / 0 FAIL, **0 declared OPEN**, exit 0, ~26 s;
rerun **byte-identical** to the committed `.out`.

### C1 (BLOCKER) — CLOSED
I reran **my own c6 mutant** (unchanged, only the `_HERE` anchor
repointed so it runs outside the repo) against the repaired receipt:

```
c6_one_direction_only   exit=1   13 PASS / 1 FAIL
      [FAIL] KG0-d THE SPACELIKE HALF IS LOAD-BEARING ...
```

Exactly as the applier reported.  KG0-d is well built and does what the
finding asked: the S_3 crown at `T = 2` satisfies **every** required
`order => causal` relation (`M = 3136/2809 < 4 = T^2`) and violates
**only** the three incomparabilities (each upper sits exactly on its own
non-dominated minimum's light cone, `|2 d_i|^2 = 4 = T^2`), and the gate
asserts *both* halves — the crippled one-directional checker **accepts**
it, the real `verify` **rejects** it at `(0, 3, False)`.  The
blocker's exact failure mode is now a tripwire.

### C2 (MAJOR) — CLOSED; provenance is honest
- **The embedded `W3_CERT` is mine, verbatim.**  Programmatic comparison
  against Appendix B: **`True`, all 18 triples**, max denominator 64.
- **Nothing claims in-receipt discovery.**  Docstring lines 30-37: *"The
  round's referee found ... (penalty hill-climb in floats, seed
  20260724, 40 restarts) ... with the review cited as their provenance"*;
  source comment at line 763: *"PROVENANCE: those coordinates, verbatim.
  METHOD (theirs, search-only)"*; verdict: *"on coordinates supplied by
  the round's referee and verified in exact Fractions by this receipt's
  own checker"*.  The division of labour — referee found, receipt gates —
  is stated in three places and overstated in none.  **Honest.**
- The gate carries the two symmetry-breaking facts (minima at three
  distinct negative times, uppers at three heights), which is the right
  content: it records *why* the two families could not contain it.
- The OPEN ledger is empty (`open outcomes recorded = 0`) and the
  chain-accumulation / courier-firewall reading is **explicitly withdrawn
  as false** inside KG2-b-exhibit.

### C3 (MAJOR) — CLOSED
KG2-b-exhibit now censuses **all** violated ordered pairs (306,049 over
13,236 tuples, 13 buckets), states in its own label that it is *"not
scan-order biased"* and that it *"localizes nothing about the RECORD"*,
and names the two shared symmetry assumptions instead.  This matches my
R11 finding and draws the correct conclusion from it.

### C4 (MAJOR) — CLOSED
KG0-b now regresses the **committed** d43d chain **CH** (10 events, width
3, realizer computed in-receipt, 90 ordered pairs, witness `None`).  The
pin is met, not merely declared around.

### C5 (MAJOR) — CLOSED; **368 confirmed correct**
The mutable default is gone and the anchor is per-object.  I re-derived
the total component-wise for the **new** object list:

```
CH 1+1 certificate   10 x 3 =  30
S_3..S_6           (6+8+10+12) x 3 = 108
W6 (pts6)             6 x 3 =  18
W(3) (W3_CERT)       18 x 3 =  54
W(3) direction set    3 x 2 =   6
unit-vector pool     68 x 2 = 136
Pythagorean seeds     8 x 2 =  16
                              ---
                              368
```

**368 is right.**  My round-1 figure of 281 was right for the *old*
object list (`pts2d` 15 + crowns 108 + D3 6 + POOL 136 + PYTH 16); the
list grew by CH's certificate replacing the 5-element realizer (+30-15),
`pts6` (+18) and `W3_CERT` (+54).  Both headline certificates are now
walked, as asked.

### New gate KG2-a2 — verified, matches my R4 exactly
48 linear extensions, `dim <= 2 = False`, `dim <= 3 = True` => order
dimension exactly 3, re-derived in-receipt rather than cited from d43d.
c-m6 closed; both halves of the sandwich now live in one receipt.

### assigned minors — verified
`_SRC` is `__file__`-anchored (c-m1: my mutants had to be repointed,
which is the proof); family-B `dc` carried; console count 13,236; the
doctrine scan widened from 3 to 32 of 974 lines (c-m4 — no longer
decorative, though `'no '`/`'not '` remain in the marker list).

### residuals I do NOT consider blocking
- **c-m5 (unapplied).**  Mutants **c3** (`dt <= 0` -> `dt < 0`) and
  **c4** (`crown_shape` returns the unaligned `ups`) still run
  **14 PASS / 0 FAIL, exit 0**.  Neither can produce a false certificate,
  because `verify` re-checks every ordered pair against the poset — c3 is
  null because no two certificate points coincide in space, c4 because
  W6's crown alignment happens to be the identity.  Recommended, not
  required: add a crown witness whose alignment is a non-identity
  permutation, so the transport step's only computational content is
  exercised.
- **c-n1 (unapplied).**  Cosmetic.

**D46c delta verdict: CLEAN.**  I endorse the stamped terminal condition
as written, including its "ORDER-dimension scope only" qualifier and its
"(referee-found, receipt-gated)" attribution for W(3).

---

## D46a — verification of the repairs

**Reproduction.** 21 PASS / 0 FAIL, exit 0, ~2:10; rerun **byte-identical**
to the committed `.out`.

### A4 (MAJOR) — CLOSED; the census reproduces me exactly
New gates **TG2a / TG2b / TG2c** hard-anchor my numbers:

| my round-1 figure | gated value |
|---|---|
| 1,016 of 12,942 actor-histories (7.9%), max 4 extra events | TG2a: `12942 / 1016 (7.9%) / max 4` (+ 2,192 total extra events) |
| 1,016 / 1,016 opponent-authored | TG2b: `1016/1016` |
| 104 of 2,224 own-view classes carry different menus | TG2c: `2224 / 104` |

TG2a's label states the conclusion correctly and without hedging: *"tau
is therefore an intermediate abstraction of a WIDER-THAN-OWN view, not an
own-view object ... no future information, but it is not computable from
what a has witnessed"*; TG2c states that pin §2's target *"is FALSE as
written and is NOT what this receipt establishes."*  That is the finding,
owned.

### A5 (MAJOR) — CLOSED, and better than asked
LG2a is relabelled *"THE MECHANICAL RESTATEMENT OF FACT (i) ... this gate
CANNOT fail on the delivered definition and is NOT evidence for
cone-locality ... its comparison count is not evidence of anything."*
And the missing control now exists and fires: **LG2a-ctl** — bare noop
cone, **248 violations in 2,382 comparisons, first violating depth 2, by
depth `{2: 8, 3: 48, 4: 192}`** — which converts amendment A1's ungated
assertion into a gated fact and independently corroborates my mutant a1.

### A6 (MAJOR) — CLOSED
LG1a / LG1b / LG3a relabelled as corollaries of LG1c's injectivity.

### A1 / A2 / A3 (BLOCKERs + MAJOR) — the AUTHORSHIP retraction is complete **in the note and the LOG**
- **Note §6 B1-B6** retires §5's assembly by name: the `tau -> menus`
  arrow is identified as the undeclared third conditional (citing my
  cone-local weight-swap mutant), (H0) is restored to the hypothesis set,
  "H2 SUBSUMED" is withdrawn as inverted, tau is declared not an
  own-view object with pin §2's target refuted, and B6 states what
  survives.  Accurate on every point.
- **LOG #394** forward-corrects #380's sentence *by quotation* and
  restores residue 1 to "DECIDED AT EVERY VERIFIED DEPTH (D44a #368)".
  Leaving #380 itself intact as the historical record is correct practice.

### **D1 (BLOCKER, new) — the RECEIPT still asserts everything §6 retracts**

The coordinator's own check condition is that *no surviving line in
receipt, note, or LOG asserts H1 discharged or the two-fact assembly*.
It fails in the receipt.  Live, unqualified, in the committed source and
printed verbatim into the committed `.out`:

- `d46a_h1_lemma_exact.py` **lines 686-696**, `[LG3 DECLARATION]` (=
  `.out` line 47): *"H2 ... needs NO separate closure argument at d42a
  scope ... **H2 is subsumed** by the same joint-closure conditional that
  powers LG1: the pin-§5 note **discharges H1 and H2** from ONE
  abstract-update law, not two."*
- `d46a_h1_lemma_exact.py` **lines 975-995**, `[VERDICT]` (= `.out`
  line 63): *"... so **H2 is subsumed** by the same joint closure — one
  abstract-update law powers both ... depth-free H1 now rests on
  **exactly two structural facts** ... **Given (i)+(ii), sigma -> (tau_A,
  tau_B) -> menus closes H1 AND H2 at every depth and the D44a §8
  assembly decides residue 1 OUTRIGHT at d42a scope**."*

That last sentence is the precise proposition BLOCKER A1 refutes with a
machine-checked witness, and the precise sentence LOG #394 declares
withdrawn.  The gates were repaired; the prose that reports them was not.
A reader who opens the artifact of record (`v10/data/d46a_h1_lemma_exact.out`)
sees the retracted claim, in the receipt's own voice, with a 21/21 green
banner above it and no pointer to §6.

**Prescribed fix (must apply before conversion).** Rewrite the
`[LG3 DECLARATION]` and the final `[VERDICT]` block to the §6/B-corrected
form — H2 not subsumed (it *is* the abstract-update law); one
undischarged conditional set, not "two structural facts"; the
`tau -> menus` arrow named as the third conditional; (H0) restored;
"OUTRIGHT" struck; a pointer to note §6 B1-B6 and LOG #394 — then
regenerate the `.out`.  No gate changes, so the 21/21 stands.

### D2 (minor) — the note's superseded text has no in-place stamp
§6's supersession notice sits *after* the text it supersedes.  A reader
who stops earlier meets, as live claims: §1's `[TARGET]` (*"H1 closes
residue 1 outright at d42a scope"*), and §5 at lines 127, 130, 141
(*"H2 is SUBSUMED"*, *"conditional on two structural facts"*, *"RESIDUE 1
DECIDED OUTRIGHT AT d42a SCOPE"*).  I am **not** asking for deletion —
keeping superseded text is corpus convention.  Add an inline
`[SUPERSEDED — see §6 B1/B2]` stamp at the head of §5 and on §1's
`[TARGET]` clause.

### unapplied round-1 items — my judgement on each

| item | must apply before conversion? |
|---|---|
| **a-m1** (two `## 4` and two `## 5` headings) | **YES.**  §6 B1/B2, LOG #394 and this review all cite "§5" and "pin §2"; with two §5s the retraction's own references are ambiguous, and a retraction that cannot be located unambiguously is not a retraction.  Renumber. |
| a-m2 (`str` in LG5a's allow-list launders a float inside a serialized abstraction) | No — recommended.  Worth one sentence of declared scope in the gate label. |
| a-m3 (single-pattern `check(True)` scan) | No. |
| a-m4 (no in-receipt joint-BFS control; my a6 shows the gate would fire) | No. |
| a-m5 (the R-B horn is untested dead code) | No. |
| a-m6 (mutant a8 silent-green = the D44a F3/m2 nullity, now shown to extend to the joint/tau system) | No — but **record it** in note §7 with the F3 cross-reference, so a later round does not re-litigate a settled nullity as a live corruption. |
| a-n1 (LOG wall-clock) | No.  For the record, this machine now measures **2:10**, matching #380's "~2:11". |

**D46a delta verdict: NOT CLEAN.**  Apply **D1** (and **a-m1**); D2 and
a-m6 are cheap and recommended in the same pass.  With D1 applied I
endorse the stamped terminal condition as written — it is an accurate,
honest statement of what this unit delivered and of what it does not.

## Delta mutation re-runs

| mutant (unchanged from round 1) | round 1 | after repairs |
|---|---|---|
| c6 — one-directional `verify` | 11 PASS / 0 FAIL, **exit 0**, false W(3) headline | **13 PASS / 1 FAIL at KG0-d, exit 1** |
| c1 W6 corrupted | exit 1 | exit 1 (now also fails KG2-a2) |
| c2 `T = 2` | exit 1 | exit 1 |
| c5 uppers not antipodal | exit 1 | exit 1 |
| c3 `dt <= 0` -> `dt < 0` | silent green (null) | silent green (null) — c-m5 unapplied |
| c4 unaligned `ups` | silent green (null) | silent green (null) — c-m5 unapplied |

---

# DELTA-2 — D46a only (commit `33d23a3`; LOG #396)

D46c converted TERMINAL at #396 on the clean delta above; no further
D46c review here.  Everything below re-executed by the referee.

## DELTA-2 VERDICT — **NOT CLEAN: 1 MAJOR, 1 minor.**  The terminal
## condition's SUBSTANCE is met; two label-only items remain before the
## `.out` is safe to freeze as the artifact of record.  No gate changes.

### D1 (BLOCKER) — **CLOSED, and closed better than I asked**

I swept both the source and the committed `.out` myself for
`outright` / `two structural facts` / `subsumed` / `discharges H1` /
`closes H1`.  **Every surviving occurrence is inside an explicit
withdrawal.**  There is no residual assertion.

- **`.out` line 47** (`[LG3 DECLARATION]`) now ends: *"ROUND-1 CORRECTION
  (note §6 B3; LOG #394): the earlier reading — that H2 is SUBSUMED and
  that ONE abstract-update law discharges H1 and H2 together — is
  WITHDRAWN AS INVERTED.  The abstract-update law IS H2 (D44a §8: H2 is
  not a consequence of H1); these gates establish that H2 HOLDS AT EVERY
  VERIFIED DEPTH by census, not that it is discharged as a law."*
  Correct on every clause.
- **`.out` line 63** (`[VERDICT]`) now carries the full correction: the
  `tau -> menus` arrow named as an **undeclared third conditional**
  (crediting the cone-local weight-swap witness), (H0) restored, *"the
  honest hypothesis set is (H0) + the abstract-update law + the
  tau -> menus arrow — THREE, none discharged"*, and *"RESIDUE 1 STANDS
  WHERE D44a #368 AND PAPER 32 PUT IT: decided at EVERY VERIFIED DEPTH,
  the H1 gap open and sharpened."*
- **The module docstring** — the fourth site, which the applier found and
  I had missed: its "WHAT REMAINS" paragraph is replaced by a five-bullet
  correction block covering H1-not-discharged, (H0), the inverted
  subsumption, tau-not-an-own-view-object, and residue 1's placement.
  **Credit where due: that catch is the applier's, not the referee's.**

### a-m1 (my must-apply) — CLOSED
Headings are now `1..9`, no collisions: pre-round amendments -> §6, the
proof note -> §7, round-1 amendments -> §8, repairs -> §9, with the
in-note cross-references updated (`§5 -> §7` inside B1/B2).

### D2 — CLOSED
`[SUPERSEDED — see §8 B1/B2 ...]` stamped on §7's heading, and
`[TARGET — H1; SUPERSEDED AS WRITTEN — §8 B4 refutes the own-view
framing, and H1 is NOT discharged]` on §1's target.  A reader who stops
before §8 is no longer misled.

### a-m2 — CLOSED
LG5a's label now declares the `str` allow-listing and its consequence
(exactness rides on the Fraction arithmetic that builds the
serializations, not on that gate).  Exactly the scope sentence asked for.

---

## WHAT REMAINS

### **MAJOR D3 (new; must apply before conversion) — A4's WORDING half was never applied, and LG1c now contradicts the same artifact's own correction**

A4's substance is closed (TG2a/b/c gate my census exactly).  A4's
*prescribed fix* had a second clause, which was not applied:

> "restate LG1c's headline as 'sigma determines the menu-view
> abstraction', and **delete** 'what an actor has not witnessed is FORCED
> by what sigma records' **or qualify it** to the menu-view data."

Live in the committed `.out`:

- **line 39, `LG1c`'s label**: *"... the own-view lag (D44a W2) is
  sigma-invisible at the abstraction level: **what an actor has not
  witnessed is FORCED by what sigma records**."*
- **line 63, `[VERDICT]`**: *"tau_A/tau_B (sigma applied to the
  **menu-view own-view sub-histories**) ..."* and *"The own-view lag (W2)
  is sigma-invisible at abstraction level."*

The same artifact therefore asserts, in its gate list, precisely the
proposition its docstring, TG2a/b/c and the closing sentence of its own
verdict refute — and "menu-view own-view" is a contradiction in a single
noun phrase.  This is not a substantive regression (the census stands and
the verdict self-corrects three lines later); it is an internal
contradiction in the document of record, and the campaign's convention is
that the `.out` is what gets read.

**Fix (labels only, no gate changes, ~4 lines).**  LG1c ->
*"sigma determines the MENU-VIEW abstractions tau_A, tau_B (tau constant
on sigma, 36/36, zero exceptions) — note this is NOT the own-view lag:
tau is not an own-view object (TG2a/b/c)."*  Strike "own-view" from
"menu-view own-view sub-histories" and from the verdict's "own-view lag
is sigma-invisible" sentence.  LG2c's "own-view sufficiency holds on all
145,408 depth-7 histories" should become "menu-view sufficiency"
(LG2a was relabelled at delta-1; LG2c was not, so the pair is now
inconsistent with each other as well).

### minor D4 — the GREEN-UNREVIEWED banner is now false in both units

`d46a_h1_lemma_exact.out` carries it **twice** (opening banner and the
`[VERDICT]` prefix): *"GREEN-UNREVIEWED — the hostile round is deferred
per the D46 program pin (token budget); this receipt must not be cited as
review-hardened until its round converts (paper-32's round precedes it)."*
The round has converted — this is the conversion.  `d46c`'s `.out`
carries one surviving occurrence too, and D46c is already TERMINAL at
#396, so this one is retrospective housekeeping there.  Restamp both to
the frozen-review form (paper 32's precedent: "status stamped with the
frozen review"), e.g. *"ROUND 1 CONVERTED — reviews/
d46ac-round1-hostile-review.md (REVISE; repairs at LOG #395/#396)."*

---

## Answers to the two questions put to me

1. **Old -> new §-mapping line in the note: YES, add it.**  My round-1
   body, my delta section above, and LOG #394's B-item references all
   cite the OLD numbering (`§5` = the proof note, `§6` = the round-1
   amendments).  #396 records the mapping, but a reader of the note does
   not read the LOG.  One line under §8's heading —
   *"(Renumbering at #396: old §4-pre-round -> §6, old §5-proof-note ->
   §7, old §6-round-1 -> §8, old §7-repairs -> §9; citations in LOG #394
   and in the frozen review use the old numbers.)"* — makes the
   retraction self-locating, which was the entire point of a-m1.
2. **a-m6: yes, please add it.**  One note-level line in §9: *"Referee
   mutant a8 (superseded marks dropped from `ser`) runs 21 PASS / 0 FAIL
   — a DEMONSTRATED NULL, the same nullity D44a adjudicated at F3/m2,
   now shown to extend to the joint/tau system; recorded so a later round
   does not re-litigate it as a live corruption."*  Cheap, and it retires
   the only silent-green in D46a's battery on the record rather than by
   memory.

---

## Reproduction (delta-2)

`python3 v10/code/d46a_h1_lemma_exact.py` -> **21 PASS / 0 FAIL**, exit 0,
~2:55 measured here, rerun **byte-identical** to the committed `.out`.
(Wall-clock spread across my three runs of this receipt: 2:51 / 2:10 /
2:55 on the same machine — a-n1's point, harmless.)  Source and
`.out` swept for `outright` / `two structural facts` / `subsumed` /
`discharges H1` / `closes H1`: **zero surviving assertions**, all hits
inside withdrawals.  Note headings `1..9`, no duplicates.

## Standing on the terminal condition

The stamped text —

> "the joint (sigma, tau) closure at 36 states/176 edges projects
> injectively onto sigma with zero exceptions over 179,783 histories, and
> menus factor through tau — but H1 is NOT discharged: the tau->menus
> arrow is an undeclared conditional, (H0) is required, and tau is not an
> own-view object; residue 1 stands DECIDED AT EVERY VERIFIED DEPTH per
> D44a #368, with the H1 gap sharpened and open."

— is **accurate, and the receipt now says all of it**.  I endorse it
unchanged.  **On D3 applied (and D4 restamped), D46a converts TERMINAL
with my clean.**  Nothing else remains: a-m3/a-m4/a-m5/a-n1 stay
unapplied by my own judgement, and c-m5/c-n1 stay unapplied on the
already-terminal D46c without prejudice.
