# D44b round 1 — hostile review: invariance at transport scope (the campaign-final unit)

**Object:** unit D44b as committed at 4c2c308 (LOG #371):
`note-d44b-transport-scope-invariance.md` (pin §1–3 + §4 A1–A3),
`code/d44b_transport_invariance_exact.py` (668 lines, 13 PASS /
0 FAIL, ~7 s), `data/d44b_transport_invariance_exact.out`.
Ancestry read in full: d42b1 receipt + committed .out (#304), d43b
receipt (#344, the per-candidate operator + relocation clause),
d44a note §7–8 + LOG #366/#368 (the H1 conditional), LOG #366
(the per-candidate lesson), LOG #371. **Referee:** independent
hostile session, 2026-07-20. Every headline number below re-derived
from an INDEPENDENT implementation of the partition machinery
(different data structures: partition-as-labeled-signature over
explicit per-window domains, Fraction keys instead of str, own
diverged/reconverged classifiers); scripts in the session
scratchpad (reproduction appendix, §6). No committed file touched.

## VERDICT: REVISE — 0 BLOCKER / 1 MAJOR / 3 minor / 3 nit

Every gated number in the receipt is right, and every one of the
five claimed headlines survives independent rebuild: the |P_t|
tables [2,2,2,2]/[5,6,6]/[9,11]/[13] and the t = 1, 2 blockwise
agreements; the six len <= 2 classes and the split pair; TG2's
two-level verdict 0/6 vs 2/9 (and it is NOT a window artifact —
the referee's matched-window run makes it stronger, §2 F-obs1);
the 3-event 1/256 reconvergence witness with the 124/1,044
censuses; the 68-transition / 5-class escape with its exhibit; the
TG0 censuses against the committed d42b1 .out; TG6's 0/3,969 (and
the ungated parenthetical "deliveries are always enabled" is true:
0 of 3,969 menus lack a d-candidate); and the closing scope
statement is adjudicated sentence-by-sentence CLEAN (§4). The
partition operator is the d43b code verbatim (§1). The receipt is
deterministic (seeds 0/7, two cwds, byte-identical to the
committed .out, exit 0 each time), has no check(True), and the
conditional TG4/TG5 branch is GENUINE: the referee extracted the
literal `if FIRE:` block from the committed file and drove it on
two synthetic closed chains — the rational-root path delivers
lambda and an exact left eigenvector, the irrational-root path
delivers a certified exact bracket around sqrt(2) with the TG5
reason recorded. Dead at cap by measurement, alive by construction
— exactly as pinned.

What does not survive is one piece of gate armor and some prose.
The TG6 negative control — a named headline gate of the
campaign-final unit — is VACUOUSLY SATISFIABLE: a mutant that
empties the d42a shape set (`shapes0 = set()`) passes all 13 gates
and exits 0, because the control-set size (4) is printed but never
gated (F1, MAJOR — the one-line fix is prescribed). And the
note/LOG census phrasing "124 reconverging pairs among / 1,044
diverged histories" is strictly false as a subset claim: the
referee verified that ALL 124 pair-histories are NON-diverged at
full length, and that 124 counts (history, position) pairs with
suffix-extension multiplicity — the distinct-reconvergence census
is 84 prefixes, 4 of them minimal at len 3, all four at weight
exactly 1/256 (F3, minor). Hence REVISE, not PASS-AS-RESCOPED; the
repairs are small and no physics number moves.

## 1. The partition machinery (attack surface 1) — VERIFIED

**Verbatim claim checked by diff.** d44b lines 153–162 against
d43b lines 91–100: identical token-for-token modulo `CACHE`→`C1`,
`FAM`→`ARM1`, and the window constant `5`→`CAP1 - 1` (the declared
window adjustment; with d43b's cap 6 the constant is cap−1 in both
files — the same operator). The refinement signature is
`tuple(sorted((str(q), P[t][successor]) for e, q in menu))` — the
PER-CANDIDATE (weight, target-class) multiset, one entry per
candidate, NOT a per-class aggregate. The #366 F2 lesson is
faithfully carried.

**Independent rebuild.** The referee reimplemented the operator
from the pin text (explicit per-window domains DOM[t] = {len <=
4−t}; Fraction weights, not strings; own relabeling) and got:
tables cutoff-1..4 = [2,2,2,2] / [5,6,6] / [9,11] / [13];
agreement {0: False, 1: True, 2: True, 3: True}; |P_1| on
len <= 2 = 6; the split pair [pA0] vs [pA0, d(A→B,v0)] with
IDENTICAL menu shapes, same P_0 class, split at P_1 — all equal to
the committed values. Domain hygiene checked: every table entry
and every agreement comparison stays inside P_t's window (t <=
4−c throughout); no out-of-domain lookups.

**Scoping of the "echo of the d42a six".** Receipt check text:
"a transport-scope six-state signal echoing the d42a count, but a
DIFFERENT object (TG6 ...)"; note A1: "a transport-scope echo of
the d42a six, a DIFFERENT object"; LOG #371 likewise. No sentence
identifies the two objects; TG6 gates the non-identification.
CLEAN.

## 2. TG2's two-level verdict (attack surface 4) — VERIFIED, AND STRONGER THAN CLAIMED

Referee rebuild: level-0 (menu-shape classes, len <= 3 parents):
2/9 failing; level-1 (P_1 classes, len <= 2 parents): 0/6 failing;
the committed first-failing exhibit ([pB1,n,d(B→A,v0)] vs
[pB1,n,n]) confirmed: equal menus, same P_0 class, rows differing.
The "deepest well-defined window" claims are correct on both
levels: P_1 rows on len <= 3 parents would need P_1 at len 4,
which is not computable at cap (successors of len-4 histories are
uncached) — the window choice is forced, not chosen.

**F-obs1 (referee observation, favorable).** The contrast is NOT
an artifact of the two different windows: on the MATCHED window
(len <= 2 parents), the menu-shape level ALREADY fails — 1/5
classes non-constant — while P_1 is 0/6 on the very same parents.
So the intrinsic refinement genuinely repairs a same-window
failure; the committed claim is conservative. Recorded so round 2
need not re-litigate the window choice.

## 3. TG3, the escape, TG0, TG6 (attack surfaces 2, 3, 5) — ALL NUMBERS VERIFIED

**TG3 (own classifiers).** Referee's diverged classifier
(non-superseded holdings of A vs B under the layer's full view —
the d43b MG6 holdings semantics, checked against d43b's
`(holdings ∩) − superseded` usage) gives 1,044 diverged histories;
124 (history, delivery-position) reconverging pairs; shortest
chain = [pA0, self-arb, d(A,B,v1)] exactly as committed; its
weight re-derived by the budget rules by hand: p at 1/4 over 2
options = 1/8; sole-component self-arb at 1/4 · 1 = 1/4; delivery
at 1/4 over 2 sender-view options (V0, v1) = 1/8; product 1/256.
All four minimal (len-3) reconverging chains carry the same
weight 1/256. TG3c's row [(1/4, →9, still-div), (1/8, →8,
NON-div), (1/8, →9, still-div)] reproduced (the referee's
independent relabeling even lands on the same class numbers).
The structural-unreproducibility gate's content is real: the
witness prefix is a len-2 member of the window six, diverged, and
its menu — a cap-independent layer fact — carries a 1/8 delivery
into a non-diverged successor, so no transfer respecting the
layer's per-candidate weights can hold an absorbing purely-
diverged sector containing this configuration. The d42a absorption
row is unreproducible in exactly that sense; the receipt's
sentence is scoped to it. CLEAN (but see F3 on the census prose).

**The escape (attack surface 3).** Referee recount: 68 escaping
transitions from len <= 2 parents; exactly 5 target classes; each
of the 5 has NO member of length <= 2 (min member length 3,
verified per class); the exhibit [pA0, pB0] --self-arb q=1/4-->
class 6 confirmed with the cache weight. The escape/
non-stabilization distinction is genuine and correctly framed:
stabilization = refinement fixed-point on windows (measured TRUE
at t = 1, 2), closure = class-set invariance under the transfer
(measured FALSE) — different predicates, both gated. Depth-5+
honesty checked by grep: every non-closure sentence carries "at
cap"/"at the depth-4 cap"/"at the feasible caps"; TG7 declares
transport-scope closure OPEN; no sentence predicts either horn
above cap. CLEAN.

**TG0 (attack surface 5).** All four committed d42b1 .out anchors
re-derived independently: orphans 464/72 (.out line 30), depth-2
conflict histories 4 (line 20), arb joins 384 and delivery joins
8,250 (line 31), family sizes 3,969/3,424 (line 11). The
cumulative vectors [1,9,69,521,3969] / [1,16,235,3424] are NEW
anchors (not in the d42b1 .out), correctly labeled "re-derived
from the exec'd committed layer"; referee enumeration agrees.
TG6a's d42a census [1,7,39,215,1191] equals the d43b MG0 prefix.
TG6b: 4 distinct d42a shapes, 0 with a d-kind, 0/3,969 transport
menus matching any d42a shape — all reproduced; additionally the
referee verified the ungated parenthetical: 0 of 3,969 ARM-1T
menus lack a delivery candidate ("deliveries are always enabled at
transport scope" is TRUE).

## 4. The closing scope statement and LOG #371 (attack surface 8)

The TG7 scope statement (.out line 59) adjudicated clause by
clause: "D44a's decision is at d42a scope (delivery-free),
exhaustively verified through depth 7, all-depth conditional on
H1" — matches #368's settled statement verbatim in content (H1 =
the depth-free structural lemma, d44a note §8). "THIS receipt
shows its class structure does NOT transfer" — carried by TG3
(absorption broken) + TG6 (classifier alien), both gated. "the
transport intrinsic chain, though window-consistent at six classes
with well-defined rows (TG1/TG2), is NOT CLOSED at the feasible
cap (TG4's escape)" — every clause gated. "The closure theorem
covers exactly the delivery-free grammar; transport-scope closure
is OPEN" — correct in both directions: coverage = d44a's own
declared scope, openness = this unit's measured escape with no
above-cap claim. CLEAN — the sentence that will be quoted says no
more than the caps reach.

LOG #371 checked line by line against the artifacts:
"REOPENING CONFIRMED" is qualified "IN-FAMILY" at first use;
"STRUCTURALLY UNREPRODUCIBLE at transport scope (… — gated)"
matches TG3c's actual scope; "dead at this cap BY MEASUREMENT" is
true (FIRE is computed from measured STAB/wd1/ESC, and the branch
is live — §5 probe). Note §4: A1 accurate; A2 accurate (~7 s
measured by the referee; ARM-2T runs census+purity+menu-count
only, as stated; the < 600 s boolean is as printed); A3 accurate
EXCEPT the "among" phrasing (F3). Two prose defects only (F3, N2).

## 5. Findings

**F1 (MAJOR — the TG6 negative control is vacuously satisfiable;
silent-green mutant).** Mutant m5 replaces line 584
(`shapes0 = {menu_shape(C0[tuple(h)]) for h in FAM0}`) with
`shapes0 = set()`: ALL 13 gates pass, exit 0. TG6b's condition
(line 599–600: `shpW not in shapes0 … and n_d0 == 0 and
all_alien == 0`) is satisfied by an EMPTY control set — every
conjunct is vacuous or trivially true when the d42a shapes are
lost downstream of TG6a's census gate. The control-set size (4)
appears only in the ungated detail string. On the campaign's own
standard (d43b: "every delivered count is an anchored expectation
that can fail"; the three check(True)-class convictions), a
negative control whose non-vacuity is not mechanically enforced is
a gate-armor defect in a headline gate — and this is the unit
whose TG6 blocks silent reuse of the d42a result. Detection today
is only by byte-diff against the committed .out (the detail string
changes), not by any gate. **Fix (one line):** add
`and len(shapes0) == 4` (and, belt-and-braces, `and shapes0`) to
the TG6b condition; anchor 4 is referee-verified against the
committed d42b3 layer at depth 4.

**F2 (minor — headline counts printed but not anchored).** Four
delivered numbers quoted in LOG #371/note §4 are print-only:
1,044 diverged (TG3a gates only `n_div > 0`, line 345), 124
reconverging pairs (detail string of TG3b, line 377), the ARM-2T
menu-shape count 11 (line 259–263), and the d42a shape count 4
(F1). Corruptions that move these while preserving the gated
witness properties exit 0 (mutant class demonstrated by m5; m6
shows the classifier's outputs are .out-protected only). Violates
the program's anchored-expectation standard (d43b NC1, d44a F4
precedents). **Fix:** gate `n_div == 1044`, `len(recon) == 124`,
`n_shapes2 == 11`, `len(shapes0) == 4`.

**F3 (minor — the reconvergence census prose is wrong as a subset
claim, and the pair count carries suffix multiplicity).** Note A3:
"124 reconverging pairs among 1,044 diverged histories"; LOG #371:
"124 reconverging pairs / 1,044 diverged histories". The 124
(history, position) pairs are NOT among the 1,044: referee-
verified, ALL 124 pair-histories are non-diverged at full length
(they end reconverged — that is the point). And 124 double-counts
each physical reconvergence once per suffix extension: the
distinct-reconverging-prefix census is 84; minimal chains: 4, all
of length 3, all at weight exactly 1/256. The receipt's own detail
string ("(history, delivery) pairs") is precise; the note/LOG
compressions are not. **Fix:** forward-correct in the round record
(committed note/LOG untouched per house convention): "124
(history, delivery-position) pairs (84 distinct reconverging
prefixes; 4 minimal, len 3, each at weight 1/256); separately,
1,044 of 3,969 histories end diverged."

**F4 (minor — stabilization criterion drift, undeclared).** d43b's
round-1 F-B5 repair made the parent's stabilization criterion
THREE consecutive blockwise agreements (its MG2b). d44b's STAB
(line 195–196) is coded as >= 2 agreements at t >= 1, and the
second (t = 2) lives on a 9-history window. The weakening is
forced by the depth-4 cap (only t <= 2 is nontrivially
computable), and the receipt does hedge ("their (shallow)
windows", "NOT refinement-tested beyond these lookaheads"), but
nowhere states that the parent's own criterion is unmeetable at
this cap. One declaring sentence in the note (or round record)
suffices. **Fix:** declare: "the d43b three-agreement criterion is
not computable at cap; window-consistent = the two computable
nontrivial agreements (69 h, 9 h)."

**N1 (nit — tautological conjuncts dressed as checks).**
`FIRE == (STAB and wd1 and not ESC)` inside the TG5 check (line
573) and the TG7 check (line 636) restates FIRE's definition (line
420) — always true by construction; likewise
`dict(C1[tuple(ESC[0][0])])[ESC[0][1]] == ESC[0][2]` in the TG4
check (line 568) re-reads the cache the ESC entry came from. The
checks' other conjuncts ((not FIRE), the 68/5 anchors, the
min-length-3 domain check, `set(reasons)`) carry the real content,
so this is decoration, not a check(True) violation — but the
labels' "consistency: the firing flag equals the measured
conjunction" phrasing oversells a tautology.

**N2 (nit — the split-pair diagnostic prints SET-symmetric
difference of MULTISET rows).** Lines 231–233 (`set(r1) ^
set(r2)`): the rows differ as multisets by (1/8, class 2) →
(1/8, class 3) (referee Counter-diff), but the printed set
difference shows only [('1/8', 3)] because ('1/8', 2) survives in
both sets at different multiplicities. The GATE is multiset-exact
(full sorted-tuple inequality, line 254), so soundness is
unaffected; but the diagnostic could print an EMPTY difference for
rows differing only in multiplicity — a latent exhibit bug — and
LOG #371's "rows differing in exactly (1/8, class 3)" describes
the set view. Fix opportunistically at next touch.

**N3 (nit — the per-class aggregate operator is extensionally null
at this cap; recorded to prevent overreading).** Mutant m1
(refinement signature aggregated per target class) produces a
BYTE-IDENTICAL .out: the two fixed points coincide on the ARM-1T
depth-4 cache, exactly as d44a's CG3f found at d42a scope. The
receipt claims only that it RUNS the per-candidate operator
(true, verbatim — §1), never that the distinction bites here; no
committed sentence overreads. Recorded so no successor cites d44b
as evidence that per-candidate refinement is load-bearing AT
TRANSPORT SCOPE — the load-bearing contrast here is intrinsic vs
menu-shape (TG2), not per-candidate vs aggregate.

## 6. Independent-recomputation inventory

| Object | Committed | Referee (independent impl.) |
|---|---|---|
| ARM-1T / ARM-2T cumulative | [1,9,69,521,3969] / [1,16,235,3424] | equal |
| orphans / d2-conflicts / arb joins / delivery joins | 464/72, 4, 384, 8250 | equal (and equal to the committed d42b1 .out) |
| \|P_t\| tables cutoff 1–4 | [2,2,2,2]/[5,6,6]/[9,11]/[13] | equal |
| blockwise agreement | {0:F, 1:T, 2:T, 3:T} | equal |
| classes on len<=2 (P_1) | 6 | 6 |
| split pair (equal menus, P_1-split) | [pA0] vs [pA0,dABv0] | confirmed; multiset diff (1/8,c2)→(1/8,c3) |
| TG2 level-0 / level-1 | 2/9, 0/6 | equal; matched window level-0 = 1/5 (new, favorable) |
| diverged census / recon pairs | 1,044 / 124 | equal; +84 distinct prefixes, 4 minimal |
| witness + weight | [pA0, self-arb, dABv1], 1/256 | equal; budget re-derived by hand; all 4 minimal chains at 1/256 |
| TG3c delivery row | [(1/4,→div),(1/8,→NONdiv),(1/8,→div)] | equal |
| escapes / escape classes / exhibit | 68 / 5 / [pA0,pB0]—r@1/4→c6 | equal; all 5 classes min-length 3 |
| d42a shapes / with-d / menus matched | 4 / 0 / 0 of 3,969 | equal; + 0 menus lack a d-candidate |
| operator verbatim vs d43b | claimed | confirmed by diff (lines 153–162 vs 91–100) |
| TG7 H1 sentence vs #368 | claimed | matches the settled statement |
| determinism | seeds 0/7 byte-identical | 4 runs (plain, seed 0, seed 7, cwd=/) all byte-identical to committed .out, exit 0, ~7 s |
| conditional branch liveness | claimed genuine | literal `if FIRE:` block extracted and driven on 2 synthetic closed chains: exact lambda=1 + pi=(1,1); certified bracket at sqrt(2) + TG5 reason |
| check(True) / floats / RNG | claimed none | grep + read: none (docstring mention only) |

## 7. Mutation table (8 mutants, referee-built)

| # | Corruption | Result | Verdict |
|---|---|---|---|
| m1 | per-candidate signature → per-class aggregate | exit 0, .out BYTE-IDENTICAL | extensionally null at cap (N3) — not a missed tripwire |
| m2 | witness weight tilt (first event's factor dropped) | exit 1, TG3b FAIL | caught |
| m3 | orphan classifier inverted | exit 1, TG0b FAIL | caught |
| m4 | q=1/4 escaping transitions dropped | exit 1, TG4 FAIL (68 anchor) | caught |
| m5 | d42a shape set emptied (TG6 control dropped) | **exit 0, 13 PASS** — only the detail string differs | **SILENT-GREEN → F1 (MAJOR)** |
| m6 | diverged classifier's superseded filter dropped | exit 0; all gated numbers identical, only exhibit display lines differ | near-null at cap; F2 notes the census gates it would need |
| m7 | partition window off-by-one | exit 1 (KeyError) | caught (loudly, if inelegantly) |
| m8 | layer weight tilt (root candidate q doubled post-load) | exit 1, 3 FAILs (TG1, TG2, +) | caught |

## 8. Reproduction appendix

Scratchpad scripts (session
`82d34949-…/scratchpad/`): `probe_rebuild.py` (the full independent
rebuild: censuses, partition, TG2 both windows + matched window,
TG3 classifiers + prefix census, escape recount, TG6 + the
d-enabled probe); `probe_branch.py` (extracts the literal
`if FIRE:` block from the committed receipt and runs it on the two
synthetic closed chains); `mut/m1…m8` (the mutants, built by exact
string replacement on the committed source, run beside copies of
the two ancestry layers). Receipt reruns: `python3
v10/code/d44b_transport_invariance_exact.py` plain, with
`PYTHONHASHSEED=0` and `=7`, and from `cwd=/` — all four
byte-identical to `v10/data/d44b_transport_invariance_exact.out`,
exit 0, ~7 s each. Verbatim-operator diff: d44b lines 153–162 vs
d43b lines 91–100. Anchors cross-read: `v10/data/
d42b1_transport_exact.out` lines 11, 20, 30, 31; LOG #366/#368/
#371; d44a note §7–8 (H1).

## 9. Disposition

REVISE. Apply F1 (one line) and F2 (four anchors); record F3's
corrected census sentence and F4's criterion declaration in the
round record; N1/N2 at next touch. No headline moves: the third
horn, the two-level TG2 verdict, the 1/256 reopening witness, the
escape, and the closing scope statement all survive independent
rebuild unchanged. After F1/F2 this referee expects
PASS-AS-RESCOPED on the delta; the campaign can close on this
boundary with its armor matching its prose.

---

# DELTA VERDICT (appended 2026-07-20; round-1 body above untouched): DELTA-CLEAN — TERMINAL ENDORSED

**Object:** the round-1 repairs as committed at 6182b35 (LOG #373).
Diff base verified against the TRUE parent f642a6f (the earlier
4c2c308..6182b35 span also contains the d44f #372 commit — not
this unit's; the repair commit itself touches ONLY d44b paths plus
LOG #373 plus the frozen round-1 review). Every discharge verified
by execution.

## D1. Discharge verification, by round-1 label

- **F1 (MAJOR) — DISCHARGED BY THE REFEREE'S OWN MUTANT.** TG6b now
  gates `len(shapes0) == 4` (line 610). The m5 mutant
  (`shapes0 = set()`) was REBUILT from the repaired source and
  rerun: **exit 1, TG6b [FAIL]** — the silent-green conviction is
  closed by the prescribed one-line fix.
- **F2 — DISCHARGED.** All four anchors present and equal to the
  referee's round-1 numbers: `n_div == 1044` (TG3a),
  `len(recon) == 124` (TG3b), ARM-2T shapes `== 11` (the new TG1s
  gate — a print became a gate, 13 -> 14 PASS), d42a shapes `== 4`
  (TG6b).
- **F3 — DISCHARGED, decomposition INDEPENDENTLY RECOUNTED.** The
  new TG3b conjuncts gate: 124 pairs; 84 distinct diverged
  prefixes `{h[:j]}`; 4 distinct minimal 3-event chains
  `{h[:j+1] : j+1 == 3}`. Referee recount (own classifiers):
  124 / 84 / 4 EQUAL, plus: the 4 minimal chains all carry weight
  exactly 1/256, and 44 of the 124 pairs share them (the
  coordinator's parenthetical checks). One definitional note for
  the record: the gate's 84 counts diverged prefixes `h[:j]`; the
  round-1 review's 84 counted reconverging chains `h[:j+1]` — the
  referee verified BOTH censuses equal 84 at this cap (the
  chain -> prefix map is count-preserving here), so gate, review,
  and terminal statement are mutually consistent as worded. Note §5
  B3 and LOG #373's forward-correction of #371 state exactly the
  round's finding (including that all pairs END non-diverged), and
  §5 B3 honestly records the repair-time pairs-vs-distinct slip
  that the new gate itself caught (exit 1 until corrected) — the
  anchor did its job before the referee ever saw it.
- **F4 — DISCHARGED.** The criterion drift is declared at the STAB
  definition site (code comment, lines 195–198) and in note §5 B4:
  two agreements, the second on a 9-history window; the d43b F-B5
  three-consecutive standard unmeetable at cap.
- **N1 — DISCHARGED.** The tautological `FIRE == (STAB and wd1 and
  not ESC)` conjuncts are removed from the TG5 and TG7 checks; the
  values survive only in detail strings (correct place). N2/N3
  recorded in §5 B5, including verbatim the warning this referee
  required: no successor may cite d44b as proof the per-candidate
  distinction bites at transport scope.

## D2. Mechanical verification

`git diff f642a6f 6182b35` on the d44b code = exactly the
enumerated repairs (F4 comment; TG1s gate; TG3a/TG3b/TG6b
anchors; the two tautology removals) — nothing else moved; the
.out diff is the three corresponding lines plus SUMMARY 13 -> 14.
Reruns: plain + PYTHONHASHSEED 0 + 7, all exit 0, 14 PASS /
0 FAIL, all three BYTE-IDENTICAL to the committed .out. The
committed round-1 review is byte-identical to this referee's
frozen text (0-line diff). LOG #373 checked line-by-line against
this review: every attributed round-1 fact is accurately quoted
(the hand-derived 1/8 x 1/4 x 1/8, the min-length-3 verification,
the two-toy branch probe, the matched-window 1/5 observation).

## D3. The terminal statement, adjudicated

Every clause of the stamped terminal statement is gated and
referee-verified: the census sentence uses the corrected
decomposition (124 pairs over 84 prefixes, 4 minimal at 1/256);
"an echo of, not identical to, the d42a six" carries TG6; the
escape clause is capped ("at the feasible caps");
"live-but-unfired by measurement" is proven by the round-1 branch
probe; "menu-shape factorization fails at transport scope" is an
existence claim carried by a cap-independent exhibit (admissible
as worded); the closing scope statement is the round-1-adjudicated
CLEAN sentence. No clause says more than the caps reach.
**DELTA-CLEAN. d44b TERMINAL ENDORSED.**

## D4. Flags for the campaign synthesis note (requested)

MUST INCLUDE wherever the corresponding result is cited:
(i) the caps — every six-class/escape/TG2 fact is ARM-1T
depth <= 4 (ARM-2T is census-only, depth 3, intrinsic program NOT
run); (ii) D44a's all-depth side is CONDITIONAL ON H1 whenever the
closure theorem is quoted, and its coverage sentence must travel
as the pair (covers exactly the delivery-free grammar) + (transport
closure OPEN, [I1] Martin/R-theory the named successor);
(iii) the escape/non-stabilization distinction — the transport
result is "window-consistent BUT not closed", two different
measured predicates; (iv) the precise scope of "structurally
unreproducible": no transfer respecting the layer's per-candidate
weights can hold an absorbing purely-diverged sector containing
the witness configuration — not a statement about arbitrary
coarse-grainings; (v) the #373 census sentence (never #371's
"among" form), with the fact that all 124 pair-histories end
non-diverged.

MUST AVOID: (a) citing d44b as evidence the per-candidate-vs-
aggregate distinction bites at transport scope (extensionally null
at cap — m1 byte-identical; §5 B5); (b) "stabilizes at six states"
without the window qualifier — the d43b three-agreement standard is
unmeetable at cap and was NOT met; (c) merging the transport six
and the d42a six into one "six-state chain" narrative (TG6 gates
their alienness); (d) any depth-5+ prediction about transport
closure in either direction; (e) treating the 11 len <= 3 classes
or the 13 depth-4 menu shapes as refinement-tested objects (they
are not, beyond the stated lookaheads).

**Referee tallies after delta: 0 BLOCKER / 0 MAJOR open / 0 minor
open / 2 nit (N2 diagnostic set-vs-multiset, N3 recorded-null —
both recorded in §5 B5, neither blocking). The campaign's final
unit closes with its armor matching its prose.**
