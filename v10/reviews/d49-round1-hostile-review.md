# D49 round 1 — hostile review

**Frozen 2026-07-25.** Unit under review: `d49_dichotomy_settlement_exact.py`
+ `note-d49-completion-dichotomy-settlement-{pin,result}.md` + the
`THE-COMPLETION-DICHOTOMY.md` amendment, all created at LOG #418.
Status of the unit at review time: **GREEN-UNREVIEWED** — and, per finding
M4, already cited into the corpus's entry-point document.

**VERDICT: REVISE. 2 BLOCKER / 4 MAJOR / 3 MINOR / 1 NIT.**
Every number below was recomputed by the referee against the committed
d42a layer; nothing is taken from the unit's own printout.

**What survives the round, stated first so the repairs are not misread.**
The unit's *headline question* is answered and the answer holds:
**a root-free completion exists** — paper 30 §5.7 declared exactly that
`[OPEN, declared]`, and `Zhat(h) = 2^(-|h|) . f(class(sigma(h)))` is one,
strictly positive, per-cut normalized, class-constant, support-preserving.
**Horn (II) holds.** What does *not* survive is the unit's account of *why
it is the only one*, and one arithmetic interpretation that is simply wrong.

---

## BLOCKER B1 — the rank-84 result is real; its interpretation is FALSE, and the paper-30 erratum it queues must be withdrawn

The note §3.4, LOG #418 sharpening (i), and brief §12.4 all assert:

> "**229 of the 313 boundary dimensions act TRIVIALLY on the
> completion**. 313 is a correct count of boundary parameters and a
> **WRONG count of completions**."

**Refuted `[EXACT]`.** The referee took the computed 229-dimensional
kernel of the boundary → interior-potential map, perturbed the uniform
boundary along one kernel direction by `eps = 1/1000` (staying strictly
inside the positive cone), and compared:

- interior potentials under `b1` and `b2`: **identical at every one of the
  215 interior histories**, as the unit claims;
- completed transfers: **the depth-3 transfers DIFFER.** Witness `1/16`
  versus `1001/16000`. (The *number* differing is kernel-direction
  dependent — 10 for the referee's chosen direction, 2 for the one the
  repaired receipt selects deterministically; the gate asserts `> 0`,
  which is the whole content.)

The reason is elementary and the unit missed it: a completion is the
transfer at *every* interior cut, and the transfer at a depth-3 cut is
`q . Z(h+e)/Z(h)` with `|h+e| = 4` — **it reads the boundary directly.**
The kernel is invisible to the interior *potential*, not to the
completion.

**Consequences.**
1. Paper 30 §5.3's "the boundary freedom is 313-dimensional" is a
   statement about boundary freedoms and is **correct**. The queued
   erratum is **unwarranted and must be withdrawn** — the corpus was
   about to receive a correction it does not need, on green-unreviewed
   evidence, which is exactly the failure mode the citation discipline
   exists to prevent.
2. The unit's own pin §6 A2 congratulates itself for turning a wrong
   pinned rank into "the RESULT". The rank is right; the result was the
   interpretation, and the interpretation is wrong.

**What survives, and it is worth keeping.** The boundary → interior-potential
map has rank **exactly 84 = the number of depth-3 cut classes** (layer
census `1/6/23/84/313`) — the `<=` is forced (shallower layers are
determined by the depth-3 layer), so the content is surjectivity onto that
layer. The correct corollary: **the completed transfer at cuts of depth
`<= 2` depends on the boundary only through an 84-dimensional image**,
while the depth-3 layer sees all 313. That is a genuine addendum to
paper 30 §5.3 and not a correction of it.

---

## BLOCKER B2 — "among completions that do not distinguish record points the law identifies, there is exactly one" is FALSE as stated

The note §4(b) and brief §12.5 present uniqueness as the consequence of an
*invariance demand*, in a display block, as the settlement's honest core:

> "Among completions that do not distinguish record points the law
> identifies, there is exactly one, and it needs no boundary."

The referee measured how much freedom each candidate reading of that
demand actually leaves, at depth-4 truncation, by a tangent-space count at
`b*` (the conditions are bilinear in the boundary; this is a *local*
dimension count and is labelled `[MEASURED]`, a lower bound on freedom):

| demand imposed on the completion | constraints | rank | boundary directions still FREE |
|---|---|---|---|
| agreement on the root/renewal matched pair | 6 | 5 | **308 of 313** |
| bisimulation-invariance of the completed class-to-class transfer at every interior cut | 589 | 194 | **119 of 313** |
| paper 30 §5.7's FORM (`Z` a depth-graded state function on the closed chain) | — | — | **0** (one ray) |

**Neither invariance demand delivers uniqueness.** What delivers it is the
**form** — the assumption that `Z` factors as a state function times
`lambda^(-depth)`. Uniqueness is therefore a theorem *about a postulated
shape for Z*, not a consequence of "respecting what the law cannot
distinguish". The unit sells the second and proves the first.

This propagates to the headline. **"The record law is FORWARD-COMPLETE"**
is defensible only with the form named in the same breath. The referee's
required restatement, or one materially equivalent:

> Within paper 30 §5.7's stationary class — completions of the form
> `Z(h) = f(state(h)) . lambda^(-depth(h))` — a completion exists, is
> unique up to scale, and requires no boundary input. The stationary form
> is a postulate about the shape of `Z`; weaker invariance demands do not
> single `Zhat` out at finite depth (308 and 119 free directions
> respectively).

**Explicitly NOT withdrawn:** the existence result. Paper 30 §5.7 asked
whether a root-free completion exists and declined to claim either way.
It does. Horn (II) holds. The dichotomy's settlement is unaffected by
B2; only the uniqueness rhetoric is.

---

## MAJOR M1 — the gate count overstates the evidence: 13 of the 25 gates are theorem-passes or derived

The note, the LOG entry and the brief all lead with "25 PASS / 0 FAIL" and
enumerate the gates as though each were an independent test. Verified
otherwise:

- **D1 is arithmetic.** Referee computation: the class-aggregated menu row
  is constant across every history of a class at depth `<= 5` (0
  violations), and `row . f = 2 f` for every class. Given d44a CG1+CG2
  (menu factorization, transition determinism) and d43b MG3 (`Tf = 2f`),
  per-cut normalization on histories **cannot fail**. D1 tests the
  *construction*, not the theory.
- **E2 is a theorem-pass.** Given d44a SG3 — `sigma(H3 + sub(h)) =
  sigma(h)` on all 215 root-tree members, already gated — plus
  `sigma`-measurability of `Zhat`, the matched menus are identical by
  construction. The referee re-derived E2 by a route using **no event
  serialization at all** (0 sigma-mismatches, 0 completed-weight-multiset
  mismatches over 215 nodes), which both confirms the A4 determinism
  repair (finding on attack 7: clean) and confirms the gate is not
  evidence for `Zhat` specifically. **The "healing" is a property of the
  sigma-measurability demand, not of the Perron vector**, and the unit's
  most-quoted number (`1/16` = `1/16`) is a consequence of the demand.
- **D4** is the telescoping theorem of paper 30 §5.5; the receipt's own G3
  says so and then D4 is presented as a certificate anyway.
- **D5, D7, G5 are algebraic identities.** `q' = q f'/(2f)` with `q > 0`
  and `f > 0` makes D5 immediate; D7 follows from D1 by induction; **G5 is
  the definition of `q'` rearranged and has zero empirical content in
  both of its arms** — its 77,541 pairs are a restatement, not a sweep.

**REPAIR REQUIRED:** every gate labelled in-receipt as one of
`[SUBSTANTIVE]` / `[DERIVED]` / `[THEOREM-PASS]` / `[ANCHOR]`, the verdict
line reporting the substantive count separately, and the note and LOG
entry withdrawing "25 independent gates" framing. The substantive set is
C1, F1, F3 (restated per B1), F5, G1, G2 — with E1 as an instrument
anchor. **That is a smaller unit than advertised, and it is still a unit.**

---

## MAJOR M2 — the deformation comparison is cherry-picked

Note §4(a), LOG and brief §12.4 compare `Zhat`'s 50/114 deformed cut
classes **only** against the unit boundary's 21/114, conceding "MORE".
The referee computed all three, including the *other* canonical boundary
paper 30 uses `[EXACT]`:

| completion | deformed cut classes | worst within-cut ratio distortion | median |
|---|---|---|---|
| unit boundary | 21 / 114 | `23/16` (1.4375) | 1.0000 |
| class-`1/k` boundary | **103 / 114** | `4` | 2.0000 |
| `Zhat` | 50 / 114 | `7/3` (2.3333) | 1.0000 |

`Zhat` sits **inside** the range spanned by the two canonical boundaries,
with the same median distortion as the better of them. The count is not a
scalar figure of merit, and quoting only the most favourable comparator is
a presentational defect — in this instance one that makes the unit look
*worse* than the evidence supports, which is not a defence. Publish the
three-way table.

---

## MAJOR M3 — the root-exclusion is toy-relative and is not labelled

"The root is not deformed", used to claim paper 30 §5.3's sharp point is
**removed**, holds for exactly one reason, verified: `f(class 0) =
f(class 1) = 4/3`, and the root's menu leads only into classes 0 and 1.
In any grammar where those two Perron weights differ, the root deforms.
Two-of-two breadth discipline applies and is missing: the claim must be
scoped to this grammar, and "removed" downgraded to "does not occur in
this grammar".

---

## MAJOR M4 — a green-unreviewed unit was cited into the entry-point document in the same ledger entry that created it

`THE-COMPLETION-DICHOTOMY.md` gained a top-of-document banner reading
"**the dichotomy has been SETTLED**", four forward-correction blocks, a new
Part XII and a rewritten §XI — all at #418, with D49 having passed no
hostile round. **Green-unreviewed work is not citable**; this is the
discipline's central rule and the unit broke it on the corpus's own entry
point, where a reader is least able to detect it.

Compounding: the banner carries **no scope at all**. It states horn (II)
and "forward-complete" without "d42a delivery-free" or "conditional on
(H0)–(H2), H1 undischarged" — both of which appear only in §12.7, some 900
lines further down. A reader who reads only the banner — which is what a
banner is for — receives an unscoped, unreviewed claim.

**REPAIR REQUIRED:** scope in the banner; a review-status marker; and the
B1/B2 restatements carried into §12.4 and §12.5.

---

## MINOR m1 — attribution, and the archaeology claim (which stands)

The `Z(h) = f(state) . lambda^(-depth)` form was pinned in **d42b56 A3**
(#319/#321), *before* paper 30 §5.7; the note credits §5.7 alone.

The unit's archaeology claim was checked and **holds**: `d42b56`'s receipt
builds `Z` only by backward recursion from three boundaries (unit,
class-`1/k`, menu-reciprocal) and constructs no eigenvector; `d43b` and
`d44a` build `f` on states only. **No unit built `Zhat` on histories.**
No record-fidelity defect here.

## MINOR m2 — pin ordering

The pin was written concurrently with the receipt rather than strictly
before it. §6 records four first-run deviations honestly, but the ordering
deviation itself is undeclared. Declare it.

## MINOR m3 — anti-vacuity scan and dead witness branches

No AST anti-vacuity scan (LOG #403 MA-2). The `sing` / `sing2`
singular-matrix branches in F2/F5 are dead code, never exercised
(LOG #354 F1: witness branches live AND exercised).

## NIT n1 — vacuous members inside large pass counts

D2's "5,548 canonical classes, 0 violations": **813 (14.7%) are
singletons**, where class-constancy is vacuous — effective count 4,735.
D3's 427 classes: **137 (32.1%) have a single linear extension** —
effective count 290. D6's 28 sigma-classes all have `>= 2` members (clean).
Report effective counts alongside totals.

---

# DELTA — repairs verified, 2026-07-25

**Appended late.**  LOG #419 and the brief's banner both recorded this
round as "repaired and delta'd" / TERMINAL while this file carried **no
delta at all**.  That is a record-fidelity defect of the same class as
LOG #390 (a ledger entry claiming an edit that had not landed), and it
is forward-corrected at LOG #420 rather than silently closed.  The
repairs themselves were real and are verified below; only the record of
them was missing.

**Independent re-verification by the reviewer of record:** the repaired
receipt runs **31 PASS / 0 FAIL, exit 0**, reproduced from a clean
process.

**B1 — REPAIRED, and the blocker is STRONGER than this round stated it.**
The round refuted "229 boundary dimensions act trivially" with a
perturbation witness (identical interior potentials, differing depth-3
transfers, `1/16` vs `1001/16000`).  **It is not merely a witness — it is
a theorem.**  A kernel direction satisfies `Σ_e q(e|h)·δb(h+e) = 0` at
every depth-3 cut, so `Z(h)` is unchanged there; the transfer at that cut
is `q·Z(h+e)/Z(h)` with `|h+e| = 4`, i.e. **the boundary itself**.  With
the denominator fixed, the transfer is unchanged **iff `δb` vanishes on
every child of `h`**.  A nonzero `δb` is nonzero at some terminal
history, which is a child of some depth-3 cut; that cut's transfer
therefore moves.  Hence **every** nonzero kernel direction changes some
depth-3 transfer, and the witness-dependence the round conceded
("kernel-direction dependent, the gate asserts > 0") is unnecessary.
The paper-30 erratum is **withdrawn**, and correctly: §5.3's
313-dimensional boundary freedom stands.

**B2 — REPAIRED.**  Uniqueness is restated everywhere as holding **within
paper 30 §5.7's stationary FORM**, with the measured freedoms carried
(renewal-pair agreement 308/313 free; bisimulation-invariance 119/313)
and "forward-complete" barred from quotation without the form named.

**M1–M4, m1–m3, n1 — REPAIRED** as recorded at LOG #419: gates typed
`[SUBSTANTIVE]`/`[ANCHOR]`/`[DERIVED]`/`[THEOREM-PASS]` at **15/5/6/5**
and AST-anchored; the three-way deformation table published; the
root-exclusion downgraded to "does not occur in this grammar"; scope and
review status placed in the brief's banner; attribution to d42b56 A3
added; pin-ordering deviation declared; AST scan added and labelled to
what it enforces; the dead singular-matrix branches now exercised every
run; vacuous members split out of the large pass counts.

**What survives, restated because it is the point of the unit:** a
root-free completion **EXISTS** — precisely what paper 30 §5.7 declared
`[OPEN, declared]` — and `Zhat` is one.  **Horn (II) holds.**  Every
existence-side certificate is untouched by both blockers.

**TERMINAL** for round 1, now legitimately.

**RESIDUE created by this round, and it is the successor:** B2 shows
uniqueness rests on a postulated SHAPE for `Z`, not on any invariance
principle.  **Is the stationary form a law or a choice?**  The measured
freedoms are finite-depth; whether they shrink to a single ray as depth
grows is open, decidable-looking, and pinned as D50.
