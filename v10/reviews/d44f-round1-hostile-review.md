# D44f round 1 — hostile review (foliation face + measure side)

**Object:** `v10/code/d44f_foliation_measure_exact.py` (27/27, exit 0) +
`v10/data/d44f_foliation_measure_exact.out` + `v10/note-d44f-foliation-and-measure.md`
(§1–3 pin, §4 A1–A5), committed at LOG #369 (d1f468f).
**Reviewer stance:** hostile; every headline independently recomputed from the
committed d42b3 layer; new tilt directions constructed against the MG1 battery;
7 mutants run; determinism and hygiene checked.

## VERDICT: REVISE — 1 BLOCKER / 1 MAJOR / 3 minor / 4 nit

The FG2 resolution (the foliation face = the initiator datum) SURVIVES this
round intact: I rebuilt both advance orders from the layer with my own advance
rule and reproduced the 3-branch ensembles, the 1-of-3 unerased match, the 3/3
initiator-erased equality, and the winner-marginal invariance exactly; A1 and
A3 are ACQUITTED by my own scans; the MG2 anchors all reproduce, and my
depth-5-horizon recomputation strengthens MG2's horizon story. What does NOT
survive is MG1's universal forcing phrasing: I constructed four non-trivial
tilt directions that slip ALL FOUR committed gates (the sign sector), which
refutes the pin's "EVERY non-trivial tilt violates at least one committed
gate" and falsifies MG1-d's gate-label sentence about the surviving freedom.
The measure-forcing conclusion itself survives rescoping (all four slipping
tilts carry exactly zero squared-amplitude content — verified at 1e-40), which
is why this is REVISE and not REJECT.

---

## Findings

### BLOCKER-1 — MG1's sweep does not span its declared tilt space: the sign sector slips all four gates

Receipt lines 517–533 (TILTS), 484–515 (battery), 586–594 (MG1-d); pin §2 MG1;
note §4 A4; LOG #369 lines 7071–7076.

Using the receipt's OWN `battery` and `tilt_family` (exec'd unmodified), the
following non-trivial tilts fire NO gate:

| new tilt | construction | fired | max \|amp²\| dev from committed |
|---|---|---|---|
| N1 cut-symmetric singleton sign | `tilt_family(f1=-1, g1=-1)` | [] | 0.0 |
| N2 within-pair relative sign | pair = (−1/√2, +1/√2) | [] | 0.0 |
| N3 pair global sign | pair = (−1/√2, −1/√2) | [] | 0.0 |
| N4 joint sign (N1 × pair-B sign) | f1=g1=−1, pair=(1/√2, −1/√2) | [] | 0.0 |

N1 is literally T5's partner — the receipt already treats signs as in-scope
tilt directions (T5 = `tilt_family(f1=-1)`), so "re-weighting" cannot be
retro-read as positive-scale-only. The full characterization (referee): BORN
forces every squared branch amplitude, ISO then kills off-support rows, CUTIND
ties the singleton across cuts — the battery's solution set is exactly the
committed family modulo the sign group {±1}³ (singleton cut-symmetric sign ×
two pair branch signs): SEVEN non-trivial gate-passing tilts exist.

Consequences, precisely:
1. Pin §2 MG1's claim "EVERY non-trivial tilt violates at least one committed
   gate" is FALSE as a lemma. By the receipt's own A4 no-silent-acceptance
   standard (which added CUTIND when T5 slipped three gates), a tilt slipping
   all four gates fails the sweep — had any N-direction been pinned, MG1-a
   would FAIL and the receipt would exit 1. MG1's green is an artifact of the
   pinned list omitting the sign directions, i.e. the "spanning the component
   index at both cuts" claim is not met for the tilt space the receipt itself
   uses (signs included via T5).
2. MG1-d's PASSED gate label (lines 586–594) asserts "the only surviving
   freedom is the global scale, which MG2-e cancels" — false twice over:
   (a) the global amplitude scale does NOT survive (ISO/BORN convict it: T1,
   T2, T6 all fire ISO); (b) what actually survives is the sign group, which
   MG2-e does NOT cancel — MG2-e's λ scales the z MULTIPLIERS (a different
   object entirely). A false sentence inside a green gate label.

Mitigation, stated honestly (this is why the unit is not rejected): all four
slipping tilts have exactly zero measure content — every squared amplitude and
hence every Born/menu/weight datum is unchanged (max deviation 0.0 at 1e-40,
verified) — so "the operator layer forces the classical cross-component
WEIGHTS" survives, and FG2 / MG2 are untouched (a sign-flipped family flips
both orders' ensemble amplitudes identically). But the receipt never made that
argument; it claimed universal conviction instead.

**Prescribed fix:** (i) rescope MG1's forcing claim to squared-amplitude
content: "every tilt that changes ANY squared branch amplitude is convicted";
(ii) add an MG1-e sign-sector gate: enumerate the 8-element sign family, gate
that all 8 pass the battery, that the non-trivial 7 have zero \|amp²\|
deviation (Born-invisible), and that the fixture has no interference path that
could see a relative sign; (iii) correct MG1-d's label (the surviving freedom
is the sign group, not the global scale; nothing "cancels" it — it is
measure-invisible); (iv) forward-correct LOG #369's MG1 sentence.

### MAJOR-1 — "the physics is foliation-invariant" (LOG #369 lines 7067–7068) overreaches the program's own ontology

LOG: "the physics (winners, weights, amplitudes) is foliation-invariant at
fixture scale." In this grammar RECORDS ARE THE PHYSICS (the corpus's own
doctrine — the record is the object; paper 27: the boundary is made of
records), the initiator tag is record data, and this very receipt PROVES the
two terminal record ensembles differ (FG2-a). The parenthetical quietly
redefines "the physics" as the initiator-erased marginals. Moreover the datum
is not inert bookkeeping: it names the winner's version register
(`vname(..., init)`), and I verified that the post-arbitration PROPOSAL menus
at the terminal cuts differ exactly in that register's init slot — the choice
propagates into every downstream menu. The receipt's own wording (FG2-b:
"records differ only in WHO initiates ... and hence which version register
carries the winner") is honest; the LOG sentence is not.

**Prescribed fix:** forward-correct to: "the initiator-ERASED content
(winners, weights, amplitudes) is foliation-invariant; the residual foliation
datum is itself record data — it names the winner's version register and
propagates into all downstream menus." "EXACTLY ONE DATUM" may stand, since
the register name is derived from that one choice.

### minor-1 — MG2-d's absolute q' values are horizon-bound; only the sector-normalized object is horizon-stable

q' = (2/23, 1/23, 1/23) uses Z(H2) = 23/4 from the DEPTH-4 unit-boundary
recursion; those absolute numbers are horizon artifacts. Referee
recomputation at the depth-5 horizon: family 6471, Z(empty) = 2101/64, all six
join arb successors Z = 4 (component-constancy PERSISTS), early Z = 8, and the
sector-normalized conditionals are IDENTICAL: (1/2, 1/4, 1/4). So the
uniqueness upgrade's stable content is the sector-conditional object, and
MG2-b's component-constancy — verified in-receipt only at the depth-4
horizon — holds at depth 5 too (this review's record). The revision should say
the forced object is the sector-normalized conditional (horizon-stable), not
the horizon-bound absolute q'; and should note component-constancy is a
per-horizon fact, gated at 4 (now also 5).

### minor-2 — MG2-f is thin: the depth bound 7 is a narrative constant

MG2-f (lines 759–766) gates `len(H1)==1 and len(H2)==2` (lengths of literal
lists) plus a re-AND of the already-gated red_ok/scale_ok; the "≤ 7" is
hardcoded prose, not read from any D44a artifact. Not a check(True) — the
conjuncts can fail — but the gate's named content ("in scope") rests on
narration. Suggest anchoring the D44a depth constant from its receipt/out or
demoting MG2-f's scope sentence to print.

### minor-3 — LOG #369 files new-in-receipt numbers under "committed anchors reproduced"

"committed anchors reproduced (Z(genesis) = 1037/64; root completed weight
133/2074 ...; q' = (2/23, 1/23, 1/23) ...; lambda = 7/3 cancels)". The first
two ARE committed anchors (verified against paper 30 §5.3 lines 604–617 and
d42b3). q' appears nowhere in the corpus before this receipt, and λ = 7/3 is
an arbitrary probe constant. Wording: move them out of the "committed
anchors" list in any forward text.

### nit-1 — FG2-c gates 4 of the 8 ordered mutual-exclusion pairs

First-movers PAIRB and BPAIRA are untested in-receipt. Referee ran all 8
ordered pairs: all blocked (each order's second event inadmissible). "4/4" is
accurate to what was computed; make it 8/8 in the revision for free.

### nit-2 — FG1-b's multiset entries carry amplitudes as mp.nstr(...,45) strings

The record/weight comparison is structural (frozenset/Fraction ==, verified);
the amplitude slot inside the tuples is a 45-digit string. Soundness is
carried by the separate numeric amp_dev < 1e-40 check, so no finding beyond
the note.

### nit-3 — the battery is real-only, so "phase tilt" is untestable in it

`iso_defect` uses M.T (not conjugate transpose) and `born_of` squares without
modulus: a genuinely unitary complex-phase family, e.g. pair = (i/√2, 1/√2),
is spuriously convicted (fires ISO+BORN+MENU despite correct Born moduli —
verified live). No committed claim is wrong (the d43c family is real), but the
only phases the battery can honestly adjudicate are signs — which is exactly
the sector BLOCKER-1 shows it does not sweep. Also generic: conviction is at
1e-40 on squared quantities, so entry deviations ≤ 1e-20 slip by tolerance.

### nit-4 — MENU gate checks A's menu rows only

B's mirror menu (m2B) is anchored in FG0-c but not re-checked in the tilt
battery. Equivalent under the |C|-indexed family; note only.

---

## Acquittals (attack surfaces that did NOT convict)

- **A1 (arb-sector-only advance) is FORCED, not a convenience.** Referee
  enumeration of the FULL candidate menu at H2: proposal candidates = [] (both
  actors' only base v0 already carries their live proposal), idle = 3/4 each
  (contentless, unboundedly repeatable). The only branchable content sector at
  the join cut IS the arb sector; no interleaved-proposal branch exists to be
  dropped. The unadvanced sector content at the terminal cuts (proposal menus
  on the winner version) differs between orders exactly in the vname init
  slot — i.e., the same single datum, confirming rather than breaking FG2-b.
- **The ensembles are right.** My independent advance rule (recursive,
  actor-sequenced, written from the pin without reading `ensemble()`)
  reproduces both trees exactly: 3 branches each, weights (1/8, 1/8, 1/16),
  totals 5/16 = 5/16; the self-then-self branch is genuinely ONE canonical
  record (disjoint registers ⇒ poset-incomparable); unerased match 1/3;
  initiator-erased match 3/3 (my own erasure implementation); winner marginals
  equal. Pair arbitration resolves the whole component, so the other actor's
  arb menu is empty — verified, no dropped arb branches.
- **A3's vacuity claim is TRUE at this depth.** Scan of all 1191 depth-≤4
  histories: zero (history, actor) points with ≥ 2 own-view arb components;
  zero posable same-initiator arb order-swap pairs. Sequential same-initiator
  order choice is unposable as declared.
- **A4's necessity story is TRUE.** T5 under the reduced {ISO, BORN, MENU}
  battery: fired = [] (verified live in-receipt at MG1-c AND by mutant M5,
  which fails MG1-a/b/d and exits 1). CUTIND's provenance as a committed d43c
  gate confirmed (PG3-E5, d43c receipt lines 250–262).
- **MG2's reduction is identification, not analogy, at its disclosed scope.**
  The correspondence is restricted to the arb sector and sector-normalized —
  disclosed in MG2-c's own label. Given the three gated inputs (q = share ×
  Born from the layer, FG0-d; Z component-constant at the cuts, MG2-b; share
  constancy), the entrywise equality is algebraically forced — the content
  lives in the gated inputs, all of which I reproduced from the layer. The
  completion's FULL normalizer (Z(H2) = 23/4, all sectors) is not claimed to
  be matched — only the sector collapse via Born-sum = 1, which is exact.
- **Uniqueness-upgrade scope is honest everywhere I looked.** Receipt print,
  MG2-f label, and LOG #369 all carry "at verified-depth scope ... conditional
  on H1"; fixture cuts at depths 1, 2; no all-depth claim anywhere.

## Independent recomputation inventory

All from the committed d42b3 layer, referee code only
(`scratchpad/ref_fg.py`, `ref_tilts.py`, `mutate.py`):

1. Both advance-order ensembles + erased equality + marginals (above).
2. 8-way mutual exclusion: 8/8 blocked.
3. Menus: H2 arb menu = {A-self 1/4, A-pair 1/8+1/8, B-self 1/4, B-pair
   1/8+1/8}; H2 proposal menu empty; idles 3/4.
4. Z recursion, depth-4 horizon: Z(∅) = 1037/64, Z(H1) = 133/16, Z(H2) =
   23/4, root q = 1/8, root completed = 133/2074 (= paper 30 §5.3's printed
   extreme, checked against the paper text), six join successors Z = 2, early
   Z = 4, family = 1191. All match.
5. Z recursion, depth-5 horizon (NEW): successors 4 (component-constant),
   early 8, sector-normalized (1/2, 1/4, 1/4) unchanged.
6. Seven pinned tilts re-run through the receipt's battery: convictions match
   the .out row for row (T0 [] … T6 ISO+BORN+MENU+CUTIND).
7. FG3 anchors: two singleton components at [pA0, pB0], commute, mu = 1/1024;
   FG4: one canonical record, mu = 1/256 both orders.
8. A3 vacuity scans (item above).

## New-tilt attempts (per-direction record)

- N1–N4 sign tilts: SLIP ALL FOUR GATES (BLOCKER-1); zero measure content.
- Off-support singleton [0,1]ᵀ: convicted (BORN). Row-2 leakage [1, ε]:
  convicted (ISO) for ε² ≥ 1e-40; slips below tolerance (generic, nit-3).
- Pair support moved to rows 1–2: convicted (BORN forces rows 0,3; ISO kills
  the rest). No non-sign escape exists for the given shapes — the solution
  set is the sign coset, which is the repair lemma MG1-e should gate.
- Complex phase (i/√2, 1/√2): convicted, but spuriously (real-only battery;
  nit-3) — not a battery pass, and not honestly a battery test either.

## Mutation table

| mutant | target | result |
|---|---|---|
| M1 erase_init = identity (initiator kept) | FG2-b equality gate | CAUGHT — FG2-b, FG2-d FAIL, exit 1 |
| M2 one A-first branch weight ×2 | FG1 weights | CAUGHT — FG1-a (and FG1-b) FAIL, exit 1 |
| M3 winner tag swapped in one A-first pair record | winner content | CAUGHT — FG2-b, FG2-d FAIL, exit 1 |
| M4 one join successor's Z ×2 | MG2 multipliers | CAUGHT — MG2-b, MG2-d FAIL, exit 1 |
| M5 CUTIND dropped from default battery | MG1 sweep | CAUGHT — MG1-a, MG1-b, MG1-d FAIL, exit 1 (confirms A4/MG1-c live) |
| M6 initiator-blind canon | canonical form | CAUGHT — FG1-b, FG2-a, FG2-b FAIL, exit 1 (EQUAL horn forged ⇒ anchor fires) |
| M7 purity allow-list widened (float, mpf) | MG3 walk | CAUGHT — MG3-c trip control FAILs, exit 1 |

7/7 caught; zero silent greens. `check(True` grep: absent (receipt and both
ancestry receipts).

## Reproduction appendix

- `python3 v10/code/d44f_foliation_measure_exact.py` → exit 0, 27/27, ~0.45 s,
  BYTE-IDENTICAL to `v10/data/d44f_foliation_measure_exact.out`.
- `PYTHONHASHSEED=0` and `=7`, run from a foreign cwd (scratchpad):
  byte-identical to the committed .out (cwd-robust via `__file__` anchoring).
- Check-call census: 27 `check(` sites = 27 PASS lines (FG0 5, FG1 2, FG2 4,
  FG3 2, FG4 1, MG1 4, MG2 6, MG3 3).
- Referee scripts (scratchpad, not committed): `ref_fg.py` (ensembles,
  exclusion, A3 scan, Z at both horizons, FG3/FG4), `ref_tilts.py` (pinned
  re-run + N1–N4 + complex probe), `mutate.py` (M1–M7).
- LOG #369 cross-check: 27/27, ~0.5 s, seeds, no-check(True), A1–A5 listing —
  all accurate; the two wording findings are MAJOR-1 and minor-3.

## Disposition

REVISE. BLOCKER-1 requires: the MG1 rescope + MG1-e sign-sector gate + the
corrected MG1-d label + LOG forward-correction of the MG1 sentence. MAJOR-1
requires one forward-corrected LOG sentence. The FG2 resolution, the FG3/FG4
controls, the reduction dictionary, and the uniqueness upgrade's conditional
scope all survived hostile recomputation unchanged; with the MG1 rescope the
unit's delivered physics (weights forced; foliation datum = initiator) stands.

---

# DELTA VERIFICATION (round 1 → repairs at LOG #370, commit fdb85e9)

**Round-1 body above untouched.** Same referee; every repair re-verified by
independent computation (scratchpad `delta_checks.py` + reruns).

## Delta verdict: CLEAN except ONE residual minor (r-m1) — TERMINAL ENDORSED
## conditional on the one-line MG2-e label micro-repair

### Mechanical verification — all clean

- `git diff d1f468f fdb85e9` touches exactly the five d44f paths (receipt,
  .out, note §5, LOG #370, this review file committed verbatim — head/tail
  byte-checked against my round-1 text); the LOG delta is #370 only.
- Rerun: exit 0, **29 PASS / 0 FAIL**, BYTE-IDENTICAL to the committed .out;
  PYTHONHASHSEED 0 and 7 from a foreign cwd: byte-identical.
- LOG #370 is faithful to the round record (1B/1M/3m/4n, the acquittal list,
  the forward-corrections by name), and self-discloses the applier's N2
  construction slip — see D2 below, where I reproduce that slip and confirm
  MG1-e catches it.

### BLOCKER-1 repair — VERIFIED, and the new gate is non-foolable

- MG1-d rescoped to squared-amplitude content; the false global-scale clause
  is gone FROM MG1-d; MG1-e adopts the four sign tilts with the dual
  condition (all four gates slipped AND |amp²| dev = 0 at 1e-40). The .out
  rows match my round-1 table exactly.
- Adoption fidelity note: N4 as committed is `f1=g1=-1, f2=-1` (= N1·N3),
  not my round-1 N4 (N1 × pair-branch-B sign) — not "verbatim," but
  immaterial: I verified the adopted {N1, N2, N3, N4} generate the FULL sign
  group {±1}³, so sector coverage is intact.
- Non-foolability, tested as requested (delta mutants, all from the committed
  source):
  | delta mutant | result |
  |---|---|
  | D1 nonzero-\|amp²\| admixture pinned as an N-tilt (`f1=-9/10`) | CAUGHT — MG1-e FAILs (fired = ISO+BORN+MENU+CUTIND ≠ [], dev = 0.19), exit 1: a measure-carrying tilt cannot be smuggled into the sign sector |
  | D2 the applier's reported slip reproduced (N2 = `pair_matrix(-1, 1)`, spurious √2) | CAUGHT — MG1-e FAILs, exit 1: confirms the pre-commit catch reported in LOG #370 was real |
  | D3 zero-dev conjunct dropped from the MG1-e wiring | exits 0 — EXPECTED, not a finding: the mutant is semantics-preserving on the committed inputs (the four tilts genuinely have dev 0). The conjunct is belt-and-suspenders: a gate-slipping tilt with nonzero \|amp²\| cannot exist (BORN pins the support entries, ISO kills off-support rows at tolerance), so its load is carried jointly with the fired==[] conjunct, which D1 exercises |

### MAJOR-1 repair — VERIFIED

Grep over receipt / .out / note / LOG #370: the only surviving occurrence of
"foliation-invariant" in the d44f artifacts is note §5 B2 QUOTING the retired
sentence in order to correct it. LOG #370's corrected form matches my
prescribed sentence. No overreaching foliation-invariance sentence survives.

### minors — VERIFIED, including my own depth-5 numbers

- MG2-d relabel (horizon-bound absolute q'; sector conditional = the
  horizon-stable forced object): present and correct.
- MG2-d2 vs my independent depth-5 recomputation: family 6,471 ✓; all six
  join successors Z = 4 ✓; early Z = 8 ✓; sector-normalized (1/2, 1/4, 1/4)
  identical ✓; and the NEW committed number — absolute q'₅ = (8/101, 4/101,
  4/101) — I verified from the layer: Z₅(H2) = 101/8, q'₅ exactly as
  printed, ≠ depth-4 q'. All match.
- MG2-f's depth-7 constant now labeled as cited-not-computed ✓; #369's
  anchors-clause corrected at #370 ✓.

### nits — dispositions CONFIRMED

§5 B4 records all four with the referee-carried verifications correctly
attributed (FG2-c 8/8; string-compare backed by the numeric 1e-40 check;
real-only battery scope now declared in MG1-e's label; MENU/B-menu symmetry).

### Residual findings

**r-m1 (minor — the one item blocking an unconditional DELTA-CLEAN).**
MG2-e's PASSED gate label (receipt line 814; .out line 89) still reads "the
global scale lambda — the ONLY freedom MG1's sweep leaves the operator
layer — cancels...". Round 1's BLOCKER-1 diagnosis named this exact
conflation (MG2-e's λ scales the z MULTIPLIERS, a different object; MG1's
sweep leaves the SIGN sector, gated three gates earlier). The repair retired
the clause in MG1-d but left its twin in MG2-e, so two green labels now
contradict each other about what MG1's sweep leaves. Zero numerical content
is affected (λ-cancellation on z is true and gated). **Prescribed micro-
repair (one line + .out regen):** "the global scale lambda on the
MULTIPLIERS — the residual dictionary-side freedom after MG1's rescoped
sweep (whose amplitude-side residue is the sign sector, MG1-e) — cancels...".

**r-n1 (nit).** MG1-a's label still says "EVERY non-trivial tilt IS
convicted" — list-scoped in context by its own detail string (T1–T6) and now
disambiguated by MG1-e two rows below; "EVERY pinned" would close it.

**r-n2 (nit).** The final [VERDICT] paragraph still says weights "FORCED to
the decided completion's values"; MG2-d/d2 now establish the forced object
is the SECTOR CONDITIONAL — the verdict prose lags the gates it summarizes.

**r-n3 (nit — on the proposed terminal statement).** "the sign/phase gauge
sector as the exactly-characterized surviving freedom": the receipt GATES
membership + zero-measure-content of four generators of {±1}³; the
EXHAUSTIVENESS of the characterization (solution set = committed family mod
{±1}³) is referee-carried analysis (BORN pins support, ISO kills
off-support), not a gate. Carry it as referee-carried, mirroring the FG2-c
8/8 convention, or phrase "with the sign sector gated as surviving freedom
(exact characterization referee-carried)".

## Disposition

DELTA-CLEAN on every commissioned check: the sign-sector gate is correct and
non-foolable in both directions (D1, D2), no overreaching sentence survives,
MG2-d2 matches the referee's own depth-5 numbers to the fraction, mechanics
byte-clean, LOG #370 faithful. One residual minor (r-m1): the BLOCKER-1 fix
was applied to MG1-d but its twin clause in MG2-e's label was missed —
wording only, no computation affected. **TERMINAL ENDORSED conditional on
the r-m1 one-line micro-repair (+ .out regeneration and rerun), per the
campaign's established micro-repair convention (cf. #368's D1 pattern);
r-n1–r-n3 at the applier's discretion.** With r-m1 applied, the stamped
terminal statement is accurate to the artifacts, subject to r-n3's
"referee-carried" phrasing on exhaustiveness.
