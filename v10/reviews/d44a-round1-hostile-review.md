# D44a round 1 — hostile review: the renewal-pumping closure theorem

**Object:** unit D44a as committed at 3995fb8 (LOG #361):
`note-d44a-renewal-pumping-closure-theorem.md` (pin §1–5 + §6
A1–A3), `code/d44a_closure_theorem_exact.py` (24 PASS / 0 FAIL),
`data/d44a_closure_theorem_exact.out`. Ancestry read in full:
d43b receipt + note (§5 A1–A5), d42b3 admission layer,
d43bc-round1 review, LOG #361, note-d44-successor-program.
**Referee:** independent hostile session, 2026-07-19. Every
computation below re-run or re-derived; scripts in the session
scratchpad (reproduction appendix, §6). No committed file touched.

## VERDICT: REVISE — 0 BLOCKER / 2 MAJOR / 5 minor / 3 nit

Every number in the receipt is right. The referee rebuilt sigma from
the pin text with a different serialization and free (not
sigma-tied) canonicalization and got the identical 34,375-history
partition; CG1/CG2/CG3/CG4/CG5/CG6 all reproduce; the Perron
algebra was verified by hand line-by-line; and a full referee
depth-7 sweep (145,408 histories — 4.2x the committed cache) found
ZERO anomalies in any load-bearing gate. The receipt is
deterministic (seeds 0/7, three cwds, byte-identical to the
committed .out), has no check(True) (AST-verified, 24 real
conditions), and the A1/A2 deviations are honestly owned and gated.

What does NOT survive is the headline quantifier. The delivered
proof of "the intrinsic partition at EVERY depth is the pullback of
the abstract chain's bisimilarity" consumes CG1 and CG2 as
universally quantified premises, but they are verified exhaustively
on the depth-6 cache only, and the pumping engine that the pin
designed to discharge the quantifier (CG4) was — correctly — killed
by deviation A2 and replaced by nothing. "Residue 1 DECIDED at d42a
scope, ALL DEPTHS / OUTRIGHT" (receipt verdict, LOG #361, commit
message) is an extrapolation, not a theorem as delivered (F1).
A second, smaller assembly gap: the abstract quotient is computed
with a different refinement operator than the committed intrinsic
partition (aggregated-per-class vs per-candidate weights); the
receipt's "the same operator" label is false and the identification
is ungated — the referee closed it empirically (F2). Both repairs
are concrete and small relative to the unit; hence REVISE, not
REJECT.

## 1. The theorem assembly, reconstructed

The receipt and pin compress the proof into one sentence ("By
CG1+CG2 the intrinsic partition at EVERY depth is the pullback...").
Spelled out, the argument has to be:

- **(L1)** [CG1] sigma(h) = sigma(h') implies canonical-menu(h) =
  canonical-menu(h'), entrywise with weights. *Verified: all 34,375
  histories, depth <= 6.*
- **(L2)** [CG2] sigma(h+e) is a function of (sigma(h), e up to a
  sigma-compatible renaming). *Verified: all 34,374 cached
  transitions, i.e. len(h) <= 5.*
- **(L3)** [CG3a] Granting (L2) at all depths, induction on length
  puts sigma(h) inside the BFS-closed 36 for every h. As executed
  the BFS also concretely verified one-step closure from all 36
  representatives — including the depth-6 representatives, whose
  expansions are depth-7 objects beyond the cache (single witness
  per pair; see F6).
- **(L4)** [required, nowhere stated in the receipt] For every
  lookahead t, P_t factors through sigma: P_t(h) =
  pi_t(sigma(h)). Base: menu shape is a function of the canonical
  menu (L1). Step: sigma-equality gives a weight-preserving menu
  bijection (L1), matched successor sigmas (L2), and — by the
  inductive hypothesis — matched successor P_t classes, hence equal
  per-candidate multisets. **The step at depth D consumes (L1)/(L2)
  at depth D**: the induction needs them at ALL depths.
- **(L5)** pi_t is then a refinement sequence on the FINITE 36-state
  chain — genuinely depth-free — and stabilizes; so P_t stabilizes
  uniformly at every depth at the abstract fixed point's class
  count. This is the correct answer to "could deeper histories
  split the intrinsic partition past 6": they cannot, BECAUSE the
  depth-D refinement data factors through the abstract chain —
  conditional on (L1)/(L2) at depth D.
- **(L6)** [gap] The intrinsic operator (d43b lines 92–100; receipt
  port lines 285–294) refines by the multiset of (weight,
  successor-class) PER CANDIDATE. CG3c (receipt lines 535–540)
  refines by weights AGGREGATED per class. These differ in general
  (two 1/8-candidates into one class vs one 1/4-candidate). The
  fixed point the theorem needs is the per-candidate pi_infinity;
  the receipt delivers the aggregated QPART and never bridges them.
- **(L7)** [CG3c fixed point — verified sound] The trajectory
  4-5-6-6 IS a genuine fixed point: the operator carries QPART[s]
  in the refinement tuple, so it is monotone and count-stability is
  partition-stability; the referee additionally ran one more
  refinement step on the delivered QPART — blocks unchanged.
- **(L8)** [CG3d/SB1/CG3e/CG4c] Window equality: quotient-pullback
  == committed P_2 blockwise on len <= 4; the six separate on the
  window; induced rows constant over all 36 states and == T_REF;
  all six classes realized at len <= 3 (so T_REF's derivation
  window covers every class). *All verified, plus independently
  rebuilt.*
- **(L9)** Conclusion: with (L4)–(L8), intrinsic-at-every-depth =
  pullback of the abstract quotient, six classes, transfer T_REF,
  and the CG5 Perron package transfers.

The chain (L4)->(L9) is correct AS CONDITIONAL LOGIC. The two
unbridged points are the all-depth quantifier on (L1)/(L2) — F1 —
and the (L6) operator identification — F2.

## 2. Findings

### F1 (MAJOR) — the all-depth quantifier is not discharged; the headline overstates the proof status

Receipt verdict (lines 950–953, 963–966), LOG #361 ("THE CLOSURE
THEOREM LANDS — RESIDUE 1 DECIDED AT d42a SCOPE, ALL DEPTHS",
"RESIDUE 1 IS DECIDED AT d42a SCOPE OUTRIGHT"), commit message, and
pin §1 [TARGET] all state an all-depth theorem. The proof's
premises (L1)/(L2) are cache-exhaustive empirical gates (depth <=
6). No structural lemma is delivered that the admission layer's
menu is a FUNCTION of sigma's data — and that lemma is not free:
admissibility runs on OWN views, which lag the full view sigma is
built from. Witness the receipt's own W2 = [pA0, pB0, selfA,
pA(v1,0)]: B's own view still holds V0 unsuperseded with pB0 live
while the full view has V0 superseded. CG1 passes there
empirically; nothing proves the own-view lag is always
sigma-recoverable at depth 7, 8, ...

The pin KNEW this quantifier needed an engine: §1 pins "one
induction; its premises are ... pad-shift NC3 [and] renewal subtree
isomorphism + 144-census MG6" — the pumping route, in which every
deep history is carried into the window and all-depth statements
reduce to window statements. Deviation A2 correctly killed that
route: 17/36 sigma-states have no realization below length 4, the
diverged sector contains no clean-slate truncation points at this
scope (referee-confirmed at chain level: from all 27 hold-diverged
abstract states, the root state is unreachable), and diverged
reduced lengths are unbounded over the full family (the spectrum
max 6 in CG4b is a cache artifact, see F5). CG4c's surviving
content — every intrinsic class realized at len <= 3 — feeds the
window-separation leg (L8), NOT the all-depth leg. Nothing replaced
the engine. The receipt's "By CG1+CG2 ... at EVERY depth" silently
promotes cache gates to universals.

What IS proven, and it is genuinely more than d43b had: decided on
every verified depth, with the abstract 36-chain closed one step
beyond the cache from all 36 representatives; and the referee
extended every load-bearing gate one full level (all 145,408
depth-7 histories: closure into the 36, CG1 menu factorization,
CG2 determinism, SG2 invariants, SG3 renaming invariance on the 976
len-4 substitution pairs, sigma-row constancy for all 36 states
from all their len-6 instances, and P_2-on-len<=5 == pullback,
covering 32/36 states) — ZERO anomalies. The extrapolation is
empirically robust one level beyond the committed evidence. It is
still an extrapolation.

**Prescribed fix (either):**
- **(R1)** Prove and gate the structural menu-factorization lemma:
  a finite case analysis over the layer's code (candidates_for /
  admissible / prop_options / arb_components as functions of the
  sigma data, including recovery of the own-view lag from the
  full-view configuration at 2-actor no-delivery scope). With that
  lemma, (L1)/(L2) hold at all depths by structure and the
  [THEOREM] tag stands as written; or
- **(R2)** Forward-correct the claim (note §6, LOG): "decided at
  every verified depth (now <= 7); the all-depth statement is the
  gated abstract chain plus the explicitly-labeled induction
  premise (CG1/CG2 as depth-free laws — empirical, exhaustive at
  <= 7, unproven beyond)". Under R2 the unit remains a real
  advance, but the residue-1 status line must stop saying OUTRIGHT.

### F2 (MAJOR) — the quotient operator is not the committed one; the identification is ungated

CG3c's label (lines 546–552) says "the same operator that defines
the committed partition, run on the abstract chain". False as
written: the committed operator (d43b lines 92–100; receipt's own
§B port, lines 285–294) refines by PER-CANDIDATE (weight,
successor-class) multisets; CG3c aggregates weight per class (lines
535–540). Per-candidate is finer-or-equal per step; the theorem
needs the per-candidate fixed point pi_infinity, and the receipt
delivers only the aggregated one. CG3d's window equality covers
just the 28/36 states realized at len <= 4, so it does not close
the identification on the other 8 states.

**Referee closure (empirical):** the per-candidate operator run on
the 36-chain has trajectory [4, 5, 6, 6] and lands on blocks
IDENTICAL to the delivered QPART. So no damage to the result — but
the identification must live in the receipt, not in this review.
**Prescribed fix:** add the per-candidate quotient as a gate (~10
lines; anchor: identical blocks to QPART) and correct the CG3c
label, or prove the two operators' fixed points coincide here.

### F3 (minor) — mutation battery: three of the briefed corruption classes are extensionally NULL at this scope; sigma is over-specified

Referee battery (11 mutants, §5). Three named corruptions came back
SILENT GREEN (exit 0, 24/24) — and in each case the nullity is
demonstrated, not assumed: the mutants' induced sigma partitions
and quotient pullbacks are blockwise IDENTICAL to the committed
ones (§5 table):
- **m1** (drop the post-renaming sort in ser's live entry): null —
  the raw-repr presort in sigma_raw plus the <= 2-element renaming
  codomain make the re-sort redundant on this family;
- **m2** (drop the superseded marks entirely): null — the marks on
  referenced bases are RECOVERABLE from the rest of the
  configuration at this scope, i.e. pin §2's bullet-3 datum is
  redundant at d42a scope on the cache;
- **m4** (drop the previous-class component from the quotient
  refinement tuple): null — successor signatures alone already
  separate everything here.

Consequences: (i) sigma is over-specified relative to its own
partition — harmless for soundness (finer-or-equal data, same
blocks) but the pin presents the marks as load-bearing; (ii) no
gate or control demonstrates that the serialization discipline or
the marks matter (CG6 tests an addition and a payload-joint
deletion, never the marks); (iii) any expectation that these
mutants would be "caught by the anchors" is refuted (no such claim
is committed in the repo — checked — but the round brief carried
it; the "7 FAILs" expectation is realized by the TRUE
canonicalization corruption instead — see m10). Genuine
corruptions of the SAME machineries are caught: m10 (kill the
minimization — non-canonical sigma) fails exactly 7 gates
(SG1, SB3, CG1, CG2, CG3a, CG4b, CG6a); m9 (merge two abstract
states) fails 10; m4b (quotient stopped after one step) fails
CG3c/CG3d/CG3e. **Prescribed fix:** either
document the redundancy (marks + sort as defensive over-
specification, with the nullity noted) or slim sigma to the
partition-minimal data and re-gate.

### F4 (minor) — the closure gate is outcome-anchored: a capped (unverified) BFS frontier passes silently

Mutant m6 caps the BFS at representative length < 6 — i.e. the
depth-6 representatives are never expanded, deleting the receipt's
ONLY beyond-cache verification (the depth-6->7 closure steps) —
and every gate stays green (reachable is still 36, max rep len
still 6, set equality still holds). CG3a's text ("no depth cap
appears in the search") is true of the committed code but not
enforced by the gate. **Prescribed fix:** anchor the expansion
count (e.g. gate that every one of the 36 representatives was
expanded, or anchor the total number of BFS-traversed (state,
event) edges).

### F5 (minor) — CG4 is vestigial to the delivered proof; the unit's name and presentation outlive the route

The delivered assembly (L1)–(L9) uses CG4a/CG4b nowhere; only
CG4c's window realization enters (via L8). The "renewal-pumping"
of the title is not in the proof. Also, CG4b's "reduced-length
spectrum ... maximum 6" is a cache artifact and should say so:
over the unbounded family the reduction has unbounded image (the
diverged sector admits no clean-slate truncation points — A2's own
finding), so there is no finite normal-form window, which is
precisely why the pumping route could not power the all-depth step
(F1). **Prescribed fix:** label CG4a/b as independent structural
exhibits (mechanism validity + the A2 obstruction), state the
cache-boundedness of the spectrum, and let CG4c carry the only
assembly load.

### F6 (minor) — in-receipt coverage of the abstract transition relation is thinner than the prose suggests

CG2's 160 keys are the cache transitions only. The BFS's depth-6->7
expansion steps introduce NEW abstract keys — referee count: 16
beyond the 160 — each exercised by a SINGLE witness in the
committed run; likewise the four minlen-6 states' outgoing rows
(WROW) rest on one representative each, and CG3e's row-constancy
consumes those rows. CG3d's blockwise equality covers 28/36 states
(len <= 4 window). Referee closure: at depth 7, all 16 new keys are
deterministic across all instances, all 36 states' rows are
constant over every len-6 instance, and P_2-on-len<=5 extends the
blockwise equality to 32/36 states; the last 4 states would need a
depth-8 intrinsic computation or the F1-R1 lemma. **Prescribed
fix:** state the single-witness coverage in the receipt's CG3a/CG3e
labels, or gate the depth-7 sweep.

### F7 (minor) — pin §4's proof sketch inverts the refinement direction

Pin lines 89–96: "CG1+CG2 (bisimulation) => the intrinsic partition
refines the sigma-partition". Backwards: CG1+CG2 imply sigma-equal
histories are intrinsically equal, i.e. SIGMA REFINES THE INTRINSIC
partition (the receipt's own SB3 states it correctly, and the
delivered route depends on the correct direction). The pin sketch
is the proof plan of record; fix the direction in the §6 forward
corrections at conversion.

### N1 (nit) — pinned CG6b was unexecutable as written

Dropping ONLY the conflict-edge/component structure while keeping
payload triples would NOT fail CG1: at this scope the edges are
derivable from the live triples plus SG2's gated incomparability
invariant, so the pinned control was vacuous as specified. The
delivered joint-drop variant is the correct nearest non-vacuous
control and §6 A3 owns the substitution accurately. Record only.

### N2 (nit) — CG6a's "61" is a budget artifact, not a tuned pass

The 61 is just cap+1 under deterministic BFS order. Referee re-ran
the dead-keeping variant at budget 200: still open at 201 states —
the divergence is genuine, the budget not tuned. Suggest the label
say "cut at budget".

### N3 (nit) — dead code / defensive residue

`sys.setrecursionlimit(400000)` is vestigial at these depths;
`own_alive` silently proceeds via `sorted(alive, key=repr)[0]` on a
non-singleton (the SG2 counter does gate it family-wide — but a
depth-7+ violation would mis-compute sigma silently rather than
crash; under F1-R1 this becomes an assertion).

**Positives, for the record.** Paper-31 execution gating respected
(#349 terminal precedes the wave-1 builds); pins-before-receipts
held; the A1 obstruction is a genuine discovery (the witness pair
is real: both intrinsic class 2, menus one-token vs two-token —
referee-recomputed from the layer — and the one-line impossibility
inference from the gated witness is airtight: any CG1-sound sigma
must separate what the committed six merges); A2's recounts are
exact to the last unit (17 = 9+4+4 states, 23,463 = 3,727+5,828+
6,708+7,200, 1,832 gap histories, spectrum sums to 34,375); the
pre-registered failure-mode discipline was actually honored under
fire — the pin's CG3 clause triggered its ">6 states" branch and
the deviation is argued (correctly) not to be the reversal mode
since no seventh INTRINSIC class exists; no check(True); byte-
identical determinism.

## 3. Independent recomputation inventory

All referee-side, none reusing the receipt's sigma/canonicalization
code except where testing THEIR abstraction's own properties:

1. Census [1,7,39,215,1191,6471,34375] re-derived from the layer.
2. **Sigma rebuilt from the pin text** — different serialization
   (marks-first format, integer holds, differently-keyed sorts),
   free minimization: induced partition blockwise IDENTICAL to the
   receipt's on all 34,375; 36 values; windows [11,19,28,32,36].
3. **CG1 with free (not sigma-tied) canonicalization** of menus:
   constant on every class, 0 violations (a strictly different
   canonicalization convention than the receipt's).
4. **CG2 with joint free canonicalization** of (config, event):
   34,374 transitions, 160 keys, 0 violations.
5. **BFS re-run on my sigma:** closes at 36, max rep len 6,
   reachable == cache-realized.
6. **Per-candidate quotient of the 36-chain** (the F2 closure):
   trajectory [4,5,6,6], blocks == QPART.
7. **QPART fixed-point re-check:** one further aggregated
   refinement leaves the blocks unchanged.
8. **Intrinsic P_2 re-implemented;** blocks == receipt CLS ==
   QPART-pullback on len <= 4 (1,191).
9. **Transfer re-derived from my P_2** on all 215 len <= 3 members:
   well-defined, == T_REF.
10. **Perron package by hand AND machine:** row sums of the
    dominant block = 2 (so f|dom = (1,1,1) is immediate); T f = 2 f
    on all six rows by hand; det(2I - M_t) = 3/32 by cofactors;
    the anchored resolvent verified by MATRIX PRODUCT (A * R == I,
    entrywise nonnegative — the M-matrix certificate); forced
    extension (4/3, 4/3, 7/3) by hand; conflict row {1/7, 3/4,
    3/28} and its sum 1 by hand; pi T = 2 pi and exact q'
    stationarity by hand. (First referee script pass had a sign
    slip in one cofactor — det 5/32 — caught against the hand
    derivation and fixed; receipt value confirmed. Recorded for
    honesty.)
11. **Divergence-absorbing at chain level:** 27 of 36 states are
    hold-diverged; root unreachable from every one (transitive
    closure) — A2's no-renewal-in-the-diverged-sector claim.
12. **A1 witness from the layer:** menus and classes recomputed;
    CLS(W1) = CLS(W2) = 2, canonical menus differ, sigma differs.
13. **A2 recounts** (minlen census, 17, spectrum, 23,463, 1,832).
14. **CG6a at budget 200** (not tuned); **CG6b weights** N = 2 vs
    5/2 recomputed from the layer.
15. **Depth-7 sweep** (§4): every load-bearing gate, one level up.
16. Receipt mechanics: rerun byte-identical to committed .out;
    PYTHONHASHSEED 0/7 byte-identical; cwds /, /private, v10/code;
    AST scan — 24 real gates, no constant conditions.

## 4. The referee depth-7 extension probe (new evidence, both ways)

All 145,408 depth-7 histories (children of the 27,904 depth-6
cache members), ~80 s:

| probe | result |
|---|---|
| P1 closure: sigma(depth-7) in the 36 | 145,408/145,408, 0 out |
| P2 CG2 at 6->7 | 16 NEW keys beyond the 160; 0 determinism violations; 0 mismatches vs cached keys |
| P3 sigma-row constancy, all len-6 instances vs WROW | 0 violations (closes the single-witness rows of the 4 minlen-6 states) |
| P4 CG1 at depth 7: canonical menu == class menu | 145,408 menus, 0 violations |
| P5 SG2 invariants at depth 7 | 0/0/0/0 |
| P6 renaming invariance, 976 len-4 substitution pairs (depth-7 images) | 0 mismatches |
| P7 P_2 on len <= 5 (needs depth-7 data) vs QPART-pullback | blockwise EQUAL (32/36 states covered) |

Read: the F1 extrapolation survives its first out-of-sample level
completely — and the probe also demonstrates concretely that the
committed gates did NOT cover this level (16 new abstract keys).

## 5. Mutation table (11 mutants, scratchpad copies; repo untouched)

| mutant | corruption | exit | gates failed | verdict |
|---|---|---|---|---|
| m1 | drop post-renaming sort in ser (live entry) | 0 | none — 24/24 | SILENT GREEN, **null demonstrated**: sigma partition + quotient pullback blockwise identical to committed |
| m2 | drop superseded marks entirely | 0 | none — 24/24 | SILENT GREEN, **null demonstrated**: identical partition — marks cache-redundant (F3) |
| m3 | tilt T_REF (row 0: 1/2 -> 1/4) | 1 | SB2, CG3e | caught |
| m4 | quotient refinement drops previous-class component | 0 | none — 24/24 | SILENT GREEN, **null demonstrated**: identical quotient (F3) |
| m4b | quotient stopped after ONE refinement step | 1 | CG3c, CG3d, CG3e | caught |
| m5 | Perron anchor f tilt (7/3 -> 5/2) | 1 | CG5b, CG5d | caught |
| m6 | BFS capped below rep len 6 (frontier unverified) | 0 | none — 24/24 | SILENT GREEN, **real content deleted** undetected (F4) |
| m7 | CG2 key drops the event | 1 | CG2 | caught |
| m8 | unsub_v non-recursive (the d43b mutant class) | 1 | CG4a, CG4b | caught |
| m9 | merge two abstract sigma states post hoc | 1 | 10 gates (SG1, SB3, CG1, CG2, CG3a, CG3c, CG3d, CG3e, CG4b, CG6a) | caught |
| m10 | kill the minimization (first bijection — non-canonical sigma) | 1 | 7 gates (SG1, SB3, CG1, CG2, CG3a, CG4b, CG6a) | caught |

Summary: every mutation that actually changes the delivered
mathematical object is caught with exit 1. The four silent greens
split into three proven-null mutations (F3 — over-specification,
not missed tripwires) and one genuine gate-design hole (m6, F4).

## 6. Reproduction appendix

Scratchpad: `/private/tmp/claude-501/-Users-felixrobles-workspace/
82d34949-326c-4269-8dd0-587362126fa5/scratchpad/d44a/`.

- `run1.out`, `run_seed0.out`, `run_seed7.out` — receipt reruns
  (cwds v10/code, /, /private; PYTHONHASHSEED unset/0/7), all
  byte-identical to `v10/data/d44a_closure_theorem_exact.out`;
  exit 0; ~24-33 s wall.
- `indep_rebuild.py` -> `indep.out` — inventory items 1–14 (the
  one [REFEREE-FAIL] printed there is the referee's own cofactor
  sign slip, item 10; corrected check: det 3/32, A*R == I).
- `depth7_probe.py` -> `depth7.out` — §4 probes P1–P7; ~80 s.
- `mutate.py` -> `mutants.out`, `mutate2.py` -> `mutants2.out`,
  `nullity_check.py` -> `nullity.out` — §5 battery + blockwise
  nullity confirmations; mutants live in `mutants/` beside a copy
  of the committed d42b3 layer.
- Object verified against 3995fb8 (`git diff 3995fb8 --` on the
  three artifacts: empty); working-tree edits elsewhere in the repo
  ignored per round brief.

**Round-1 disposition:** REVISE. R1-or-R2 on F1 decides whether the
[THEOREM] tag survives as written or forward-corrects to
verified-depth scope; F2's gate is ten lines; F3–F7, N1–N3 are
text/gate hygiene. The computations need no repair.

---

# DELTA — round-1 repairs at 33ab0ef (LOG #366), referee verification

**Date:** 2026-07-19 (same referee; round-1 body above untouched).
**Object:** commit 33ab0ef; d44a paths verified unchanged between
33ab0ef and current HEAD.

## DELTA VERDICT: ONE RESIDUAL (D1, minor) — NOT YET CLEAN; terminal conversion endorsed CONDITIONAL on a one-line repair + one LOG sentence correction

Every discharge verified except F4's: the round's m6 mutant STILL
passes the repaired receipt (D1 below — refuting LOG #366's "the
round's m6 capped-BFS mutant now fails" and the delta request's own
stamped terminal condition "m6 caught"). Materiality is LOW because
CG7a now subsumes the deleted verification content; the fix is one
line. Nothing else above nit.

## Discharge verification, item by item

**F1 / route R2 (CG7a–e): DISCHARGED.** Every anchor equals my
round-1 sweep number exactly: 145,408 depth-7 histories from 27,904
depth-6 parents (== my P1 census); 0 new sigma-states (P1); CG7b 0
menu exceptions against the depth-6 class menus (P4); CG7c 0
determinism violations, 16 new abstract keys, 176 total (P2); CG7e
0 row violations with all 36 states covered by their len-6
instances (P3 — closes the single-witness rows of the four minlen-6
states). CG7d: gate enforces min witnesses >= 2; printed min 1,200
— referee recount CONFIRMS: 36 states, minimum 1,200 (three
smallest 1,200/1,200/1,200), total 179,783. Total exhaustively
verified histories now 34,375 + 145,408 = 179,783, receipt-carried
— the terminal statement's number is exact.

**F1 quantifier rescope: DISCHARGED.** The receipt verdict and .out
carry "ALL depths" only inside the explicit conditional ("IF the
lemma holds ... — stated as the conditional it is"); the structural
menu-factorization lemma is the NAMED RESIDUAL with the own-view-
lag nontriviality stated. Grep of receipt/.out/note: the remaining
unconditioned occurrences are confined to frozen pin history — note
§1 [TARGET], §4 sketch, §6 A1 (all pre-round text, superseded by §7
per the house pins-frozen/forward-correction convention; §7 F1
names and retires "ALL DEPTHS / OUTRIGHT" explicitly). No live
unconditioned claim survives. LOG #366 forward-corrects #361 by
name, including the commit message.

**F2 (CG3f): DISCHARGED.** The committed PER-CANDIDATE operator now
gated on the 36-chain: trajectory [4, 5, 6, 6], blocks == QPART —
matching my independent per-candidate run exactly; CG3c's label
corrected to "AGGREGATED PER CLASS ... NOT the committed
partition's operator".

**F4 (CG3a): PARTIAL — see D1.** The new anchors (n_expanded == 36,
empty frontier, rep-length spectrum {0:1, 1:4, 2:6, 3:8, 4:9, 5:4,
6:4} == the abstract minlen census, set equality) are all correct
and strictly strengthen the round-1 gate, and they DO catch
budget-stop corruption (referee mutant m6b — break after 32 pops —
exits 1 at CG3a, 29/1). They do not catch the round's actual
mutant class (depth cap).

**F5: DISCHARGED.** CG4a/CG4b relabeled [MECHANISM EXHIBIT — off
the assembly route]; CG4b's "maximum 6" now marked a CACHE
artifact with the unbounded-image reason stated.

**F3 / F7 (note §7): DISCHARGED.** The nullity results recorded as
demonstrated (partition-null on the cache), with the correct
retain-don't-slim justification (marks may matter beyond scope; the
genuine corruptions m10/m9 fail 7/10 gates); the pin §4
refinement-direction inversion owned.

**N2 / N3: DISCHARGED.** CG6a at budget 200, still open at 201 —
matches my round-1 budget-200 verification; label now says cut at
budget. The vestigial recursionlimit removed.

**Mechanical: DISCHARGED (with D1's caveat on one LOG sentence).**
git diff 3995fb8 -> 33ab0ef on the d44a paths = exactly the
enumerated repairs; NO round-1 gate condition weakened (checked
against the removed-lines diff: only docstring/label text, the
recursionlimit, and the CG6a budget change — CG3a strictly
stronger, CG6a equivalent-strength); 30 = 24 committed + CG3f +
CG7a-e; fresh rerun exit 0, 30 PASS / 0 FAIL, BYTE-IDENTICAL to
the committed .out; PYTHONHASHSEED=0 and PYTHONHASHSEED=7 both
byte-identical (cwds v10/code and /private); ~2 min 17 s wall
confirmed. LOG
#366's account of the round is faithful (verdict counts, F1/F2
attribution, forward-correction of #361) EXCEPT the m6 sentence
(D1).

## D1 (minor; blocks the stamped terminal condition): the F4 repair gates queue POPS, not expansions — the round's m6 mutant still exits 0

The repaired CG3a increments `n_expanded` at POP time, before the
loop body a depth-cap mutant skips; the traversed-edge count (176)
is PRINT-ONLY. The faithful reproduction of round-1 m6 against
33ab0ef (`if len(hk) >= 6: continue` inserted after the increment —
identical semantics: the four length-6 representatives are never
expanded) runs to **exit 0, 30 PASS / 0 FAIL**, printing "traversed
edges = 160" in its CG3a detail line versus the committed 176 —
the deficit of 16 is exactly CG7c's 16 depth-6->7 keys: visibly
wrong in stdout, invisible to the exit code. LOG #366's "the
round's m6 capped-BFS mutant now fails" is therefore FALSE and
needs a forward correction at next touch. (The budget-stop variant
m6b IS caught: exit 1 at CG3a.)

Materiality is LOW: CG7a now verifies sigma-closure over ALL
145,408 depth-7 histories — a strict superset of the checks the
capped BFS deletes — so the defect is a TRIPWIRE gap, not an
evidence gap (this is also why I rate D1 minor rather than major).
**Prescribed one-line fix:** promote the edge count to a gated
anchor — `n_bfs_edges == 176` — optionally noting 176 == CG7c's
total key count (a nontrivial cross-consistency: every abstract
(state, event) pair is traversed exactly once from the
representatives).

## For the §8 conditional-assembly proof note (requested guidance)

MUST include:
1. **The hypothesis as a conjunction.** "Menu factorization from
   sigma" names only CG1's form. State the lemma as: *sigma is a
   CONGRUENCE for the admission layer at every depth* — (H0) the
   SG2 invariants hold at every depth (own-alive singleton, live
   proposals on the proposer's own alive base, conflict
   incomparability: without these sigma is not even well-defined);
   (H1) sigma-equal implies canonical-menu-equal, entrywise with
   weights; (H2) successor sigma is a function of (sigma, event up
   to renaming). H2 is NOT a consequence of H1; the current §7 and
   verdict sentence "IF the lemma holds, CG1/CG2 become depth-free
   laws" silently folds H0/H2 into H1's name — the §8 statement
   must not.
2. **The induction stated explicitly** (round-1 review §1, L4):
   base = menu shape is a function of the canonical menu; step at
   depth D consumes H1/H2 at depth D; conclusion P_t = pi_t o
   sigma for every t, with pi_t the PER-CANDIDATE refinement on
   the 36-chain.
3. **The quotient in the statement must be CG3f's per-candidate
   fixed point**, with CG3c cited as coinciding (not the reverse).
4. **Direct-verification scope stated:** blockwise intrinsic
   equality is computed at len <= 4 in-receipt (CG3d, 28/36
   states) and len <= 5 by the referee (32/36); the four minlen-6
   states' intrinsic classifications at their own depths follow
   only from the conditional argument — say so.
5. **The uniform-lookahead fact** that P_t(h) depends only on h's
   t-step subtree (this is what makes pi_t well-defined on the
   abstract chain and why no depth-window dependence survives in
   the pullback).

MUST avoid: any unconditioned all-depth sentence anywhere in the
note; "renewal-pumping" as the operative mechanism (historical
unit label only, with the A2 obstruction cited); treating CG7's
depth-7 evidence as a premise of the proof (it is out-of-sample
evidence, not part of the conditional derivation); minimality
claims for sigma's marks or serialization (the F3 nullity record
stands).

## Terminal statement

The stamped terminal statement is accurate as worded (179,783 =
34,375 + 145,408, receipt-carried; six-class per-candidate quotient
with T_REF; full Perron package; the lemma as residue 1's final
named gap with the conclusion exactly conditional on it; pumping
retired for the closure-quotient route). **Conversion is endorsed
as soon as the two D1 micro-repairs land:** (i) gate
`n_bfs_edges == 176` in CG3a; (ii) forward-correct LOG #366's m6
sentence. Everything else is DELTA-CLEAN.

## Delta reproduction appendix

Same scratchpad as round 1: `delta_run1.out` / `delta_seed0.out` /
`delta_seed7.out` (reruns; diffed against the committed .out),
`delta_m6.out` + `m6_delta_full.out` (the D1 mutant, regenerated
from the 33ab0ef source), `delta_finish.out` (seed7 + m6b
budget-stop + witness recount), `mutants/m6_delta_bfs_cap.py`,
`mutants/m6b_delta_budget_stop.py`.
