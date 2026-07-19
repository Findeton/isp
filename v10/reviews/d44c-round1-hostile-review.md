# D44c (successor 3) — round 1 hostile review: multi-author arbitration vs order-dimension

**Object:** `v10/code/d44c_arb_dimension_exact.py` (1,427 lines) +
`v10/data/d44c_arb_dimension_exact.out` (15/15 PASS), pin + amendments
`v10/note-d44c-multiauthor-arb-dimension.md` (§1–4 pin, §5 A1–A6), LOG #351,
HEAD 6d8a74b.
**Standard:** receipt review under the d43d-round-1 precedent (that round inverted a
width-blind dimension headline; this receipt was treated with equal suspicion). Every
census number recomputed from the committed d42b3 layer by an independent
implementation; the enumerator checked against a strict syntactic-superset generator;
the register-word dedup audited DENSELY (exact C-matrix identity over every class
member — all 1,131,500 arb-containing histories — not the receipt's 1-in-97 verdict
sampling); the oracle cross-validated against a definition-level brute-force
two-linear-extension checker; the five-clause law re-gated independently and
stress-tested with three STRONGER referee clauses; the crown hunted beyond the
receipt's caps (exhaustive width-3 no-idle depth 8; random deep probes at widths 4–6
to 14 events; the idle-containing depth-7/8 stratum; 27,600 triple-pool attempts);
the F-CROSS census reproduced cell-for-cell; six mutants; determinism ×2 hash seeds.
**Review instruments** (session scratchpad, reproducible; appendix §7):
`ref_layer.py`, `scriptA_enum_completeness.py`, `scriptB_census_dedup_laws.py`,
`scriptC_beyond_caps.py`, `scriptD_crowns.py`, `scriptE_fcross_recount.py`,
`mut/mut1..mut6`.

**Verdict: REVISE — 0 BLOCKER / 1 MAJOR / 2 minor / 3 nit.** Every number in the
`.out` is verified true; every census, mass, class count, width table, and death
census reproduces exactly under independent reimplementation; the dedup is
unconditionally sound on the swept families (dense audit, zero mismatches); the
enumerator is complete against a strictly larger syntactic event space; all six
mutants exit 1 at their intended gates; the run is byte-identical under
PYTHONHASHSEED 0/7. The headline — arbitration structure alone does not generate
order-dimension > 2 at the tested scales; the mechanism is the component-confinement
law — **stands, and this review STRENGTHENS it** (§4): the five clauses are in fact
all-scale theorems of the committed layer, a sixth stronger clause holds (incomparable
arbs have NO common upper bound — 0 violations over all 21,149 register-word
classes), and from it the referee proves S3-crown impossibility at EVERY width and
depth, not just the tested ones. All referee crown attempts died; all beyond-cap
probes green. The one MAJOR is a decision-procedure defect: the pre-registered
WITNESS horn is unreachable at exit 0 — had a witness existed, this receipt would
have exited 1 labeled "anchor/port breakage". It did not bite (the obstruction horn
is the true one) but it contradicts the receipt's own banner and the pin's
either-horn pre-registration.

---

## 1. MAJOR finding

### F1 — MAJOR (CONFIRMED, by code path analysis): the pre-registered witness horn
### cannot exit 0 — the banner's exit-semantics sentence is false in the witness
### branch, and the witness verdict print is dead code

The banner (receipt lines 22–24; printed banner, `.out` lines 8–10) declares:

> "Exit 1 ONLY on anchor/port breakage or internal inconsistency; the dimension
> outcome itself is pre-registered open — either horn exits 0 with its verdict
> printed."

The code cannot honor this. A dim ≤ 2 failure anywhere would raise `Witness`
(lines 424–425, 458–460), abort the sweep, and then FAIL the very PASS conditions
of the census gates: AG1 gates `st1['witness'] is None and fails1 == 0` (line 580),
AG1b line 615, AG2b line 897; a cross success fails AG2c (`len(cross_successes) == 0`,
line 1168); an F-LAM dim failure fails AG2d (`lam_dimfail == 0`, line 1294) and AG3
(line 1347). Any witness therefore drives `FAIL >= 1`, and the final block
(lines 1396–1400) prints

> `[VERDICT] FAIL — anchor/port breakage or internal inconsistency; exit 1 by design`

and exits 1 BEFORE the `any_witness` branch (lines 1401–1405) can run. Three
defects: (a) the banner sentence is false as written — the witness horn exits 1,
not 0; (b) that exit would carry a false label ("anchor/port breakage") for what the
pin §1 declares a deliverable RESULT ("a WITNESS: ... — arbitration is a SECOND
dimension mechanism"); (c) because `Witness` aborts the sweep mid-DFS, the census
anchors would also fail with truncated totals, burying the witness block under a
cascade of census FAILs. The `[VERDICT] d44c WITNESS HORN` print is unreachable
in every witness world.

No false result was delivered — the obstruction horn is real (independently
confirmed here at and beyond the caps). But this program's pre-registration
discipline is exactly what the two prior dimension-headline inversions traded on,
and a receipt whose witness branch mechanically self-reports as breakage does not
implement its own pre-registration.

**Prescribed fix** (receipt frozen; the program's standard forward-correction
route): a LOG row noting that the banner's "either horn exits 0" sentence is
WRONG of the committed code — the true semantics are "a witness aborts the hunt
and exits 1 with the `[WITNESS ...]` block printed and the census gates failed";
any successor receipt reusing this harness should either (a) condition the census
anchors and the witness-is-None conjuncts on the no-witness branch and let
`any_witness` exit 0 through its own verdict, or (b) pin the witness horn's exit
code as 1-with-witness-block and say so in the banner.

---

## 2. minor findings

### F2 — minor (CONFIRMED): "1,213,372 label-level histories" double-counts —
### 88,488 of the checks are repeats of the same 44,244 label sequences; distinct
### histories = 1,124,884

The verdict (`.out` line 217), AG3's gate label (line 210), and LOG #351 all read
"zero dim<=2 failures across 1,213,372 label-level p/r/n histories (AG1 551,928 +
AG1b 224,580 + AG2b 436,864)". The sum is transparent, but the three families
overlap: every no-idle width-3 history of depth ≤ 6 (44,244 label sequences:
6+30+180+1,356+7,176+35,496) is a member of AG1's full grammar, of AG1b, AND —
because the committed 2-arg `admissible()` is universe-free (the receipt's own
A3 note) — of AG2b's family over (A,B,C,D) as the identical label sequence.
Distinct histories = 551,928 + 180,336 + (436,864 − 44,244) = **1,124,884**;
1,213,372 is the number of history-CHECKS. As a count of evidence it is inflated
~7.9% by triple-counted objects. (Verified: my independent sweeps reproduce all
three family censuses exactly, and the 44,244 overlap count is exact arithmetic
on the anchored level counts.)

**Prescribed fix:** forward-correct to "1,213,372 history-checks over 1,124,884
distinct label-level histories (the 44,244 no-idle width-3 histories of depth ≤ 6
lie in all three families)" at the next LOG touch; successor receipts should
report the distinct count.

### F3 — minor (CONFIRMED, then closed by this review): the verdict claims
### "zero dim<=2 failures across ... every constructor state at widths 3..6",
### but the 340 F-CROSS post-X states were never dim-checked — the receipt's own
### AG2c label says so

Verdict (`.out` line 217 / receipt lines 1407–1413): "zero dim<=2 failures across
1,213,372 ... and every constructor state at widths 3..6." But the F-CROSS state
table's own label (`.out` line 108 / receipt lines 1125–1129) reads "no dim
evidence is drawn from these states — they are death exhibits". The 340 cached
post-X states are constructor states at widths 2..6, and no `dim_le_2` call ever
touches them in the receipt (code path: `cross_run` computes `width_of` only,
line 1075). So the verdict sentence asserts a check the receipt did not run for
340 of its constructor states — a claim/label tension inside one artifact.

**Referee closure:** I rebuilt all 340 states per the receipt's construction
(scriptD CR-0; state count 340, width table {2:15, 3:80, 4:150, 5:60, 6:35} both
exactly reproduced) and dim-checked every one: **zero failures**. The sentence is
true; it was unbacked at commit time. **Prescribed fix:** forward-correct the
verdict wording to the dim-checked constructor set (P1/P2/P5 + all 1,597 F-LAM
layouts), citing this round for the 340-state closure — or gate the 340 in a
successor.

---

## 3. nits

- **n1 — AG5 is `check(True, ...)`** (receipt line 1391): a disclosure gate with a
  hard-coded condition, counted in "15 PASS". Same class as d43d NG4, which LOG
  #348 records as "round-1-disclosed, corpus-tolerated"; items (a) and (d) of its
  text are backed by real gates elsewhere (AG0's 219/4,231; the printed cap
  tables), items (c)/(e) are ungated text. Tolerated per corpus precedent;
  flagged for the record.
- **n2 — ungated label narration in AG1b** (lines 606–607): "two-level mint towers
  reached (root + child + grandchild structures at depth 7)" is asserted in the
  check label but nothing gates it. Referee-verified TRUE: e.g.
  `[pA0, pB1, r{A,B}@V0, pA@v1, pB@v1, r{A,B}@v1, pA@v2]` is admissible at
  depth 7 (root arb, child arb, grandchild proposal). Harmless; should have been
  a gated existence bit.
- **n3 — clause (iv) is gated once per register-word class, not "every history
  checked at creation"** as AG3's preamble says (`.out` line 203): the chain-law
  counter lives inside `class_handle` (receipt lines 452–456) and runs only for
  new classes; clauses (i)(ii)(iii)(v) do run per history. Because both the
  word and the poset are class functions — now DENSELY verified (§5.2) — the
  per-class check is mathematically equivalent; the wording overstates the
  mechanism slightly.

Plumbing notes (no findings): run-from-repo-root is required and documented
(docstring line 25); from `v10/` the receipt dies loudly (FileNotFoundError,
exit 1) — same convention as the reviewed-and-terminal d43d. Working tree clean;
commit 6d8a74b touches exactly the four D44c files; the terminal d43d artifacts
are untouched since 7b76312 and the d42b3 layer since 171c75a (git verified).

---

## 4. The structural result the round should keep: the law is STRONGER than gated,
## and the S3 crown is impossible at ALL scales — referee proof + mechanical gates

The receipt gates the five clauses empirically at the tested scales. They are in
fact all-scale theorems of the committed `d42b3` layer, by short arguments the
next unit should record (each mechanically re-gated by this review at zero
violations over all 21,149 register-word classes and 1,131,500 arb-containing
histories — scriptB):

1. **(iv) is definitional.** `event_poset` chains every event above the previous
   event touching any shared register, so the events touching one register form a
   chain; every event touches ≥ 1 actor register; hence register-sharing events
   are comparable, per-actor events form chains, and width ≤ actor count — at
   every depth, every width.
2. **Propose-on-mint ⟹ pool membership.** `holdings` admits a base only via an
   arb IN THE PROPOSER'S OWN CHAIN whose pool contains the proposer; so pools on
   a mint are subsets of the minting pool, and a never-arbed actor can pool only
   on V0.
3. **(iii) nesting is forced.** An actor's non-superseded held base is always
   exactly its last mint (its own arbs supersede their bases in its view), so
   successive arb bases climb the actor's own mint chain and pools shrink along
   it. (i)/(ii) follow: two pools sharing an actor are both in that actor's arb
   chain, hence nested; a same-base repeat is blocked because the new arb's OWN
   past cone (the view `admissible()` uses is `pred[j]` of the new event) always
   contains every pool member's chain, hence the earlier resolver, hence the
   resolved proposal is not live and the component cannot match.
4. **(v) is structural**: minted vnames are never re-touched by `regs_of` of any
   later event (a child arb's register is its OWN new vname), so vname registers
   are one-shot; this is also exactly why the register-word dedup is exact (§5.2).
5. **NEW, STRONGER CLAUSE (referee): two incomparable arbs have NO common upper
   bound at all.** Every event strictly above an arb R touches only pool(R)'s
   actor registers (induction using 1–3: the first step out of R is a pool
   actor's event; any later arb containing a pool actor is nested inside that
   actor's previous pool ⊆ pool(R)). Incomparable arbs are pool-disjoint by
   (iv), so their up-sets are register-disjoint and no event can sit in both.
   Gated: 0 violations over every class in AG1/AG1b/AG2b (scriptB "T2"), plus
   the up-cone-confinement form ("T3") separately at 0.

**Referee funnel lemma (S3 impossibility, all scales).** In any admissible p/r/n
history, the up-set of ANY event B funnels: up(B) = (a chain segment of B's
author(s)) ∪ up(c(B)) where c(B) is the first arb after B on the author's chain
(for a proposal, its unique consuming arb — an actor has at most one live
proposal, and only the consuming arb ever contains it). Two incomparable tops
above B must therefore both lie in up(c(B)). For an S3 crown with bottoms
B1,B2,B3: if two bottoms are arbs, clause 5 kills their common top; otherwise
each bottom's tops live in up(R_j) for its consumer R_j, tops-in-common force the
R_j pairwise comparable (else clause 5), so the R_j form a chain R_a < R_b < R_c
— and then every element of up(R_c) sits above ALL THREE bottoms, so no top can
avoid its forbidden bottom. Mixed cases collapse the bottoms' incomparability the
same way. Hence **no admissible p/r/n event poset contains S3 as an induced
subposet, at any width or depth** — the pin §2 component-law horn is not merely
"gated at the tested scales" for the S3 pattern; it is a theorem. What remains
genuinely scale-limited — and why the receipt's "at the tested scales" scoping
stays correct and must not be widened — is dim > 2 via NON-S3 3-irreducible
patterns (chevron etc.); the referee's hand analysis kills the chevron too, but
no full classification was attempted, and the receipt claims none.

**Recommendation** (not a defect): the successor that writes this up (the D44
synthesis or paper-31-class successor) should state the law as all-scale theorems
1–5 + the funnel lemma, with the enumerative census demoted from "evidence for
the law" to "consistency exhibit + non-S3 coverage at the caps". That is the
correctly-scoped strengthening this round's brief asked for.

---

## 5. Independent-recomputation inventory (all EXACT matches unless noted)

Instruments: independent reimplementation over the committed layer exec'd from
`v10/code/d42b3_placement_exact.py` — same single source as the receipt; my dim
oracle additionally cross-validated at the definition level.

| Object | Receipt anchor | Referee recomputation | Match |
|---|---|---|---|
| AG1 totals d1..6 | 9/75/639/5,865/54,489/490,851 | scriptB independent DFS | EXACT |
| AG1 arb-containing | 0/6/186/3,264/41,016/426,294 (Σ 470,766) | same | EXACT |
| AG1 canon / word classes / w-dist | 32,288 / 3,309 / {15, 780, 2514} | same | EXACT |
| AG1 masses | 435951/2048, 3144195/4096, ratio 96878/349355 | exact Fractions | EXACT |
| AG1b totals/arb/classes | 6/30/180/1,356/7,176/35,496/180,336; 224,502; 10,049/5,904/{18,936,4950} | same | EXACT |
| AG1b mass | 8613/32768 = all-arb, ratio 1 | same | EXACT |
| AG2b totals/arb/classes | 8/56/448/4,864/48,896/382,592; 436,232; 16,273/11,936/{20,876,5568,5472} | same | EXACT |
| AG2b mass | 2749/1024 = all-arb | same | EXACT |
| AG4 evidence strata | 2,034 / 4,596 / 9,000 | same | EXACT |
| Enumerator completeness | "every admissible history" | scriptA: syntactic SUPERSET (all bases × bits × n × ALL ckey⊆all-proposals-ever incl. resolved/mixed-base × all wkeys × all initiators) filtered by committed `admissible()` vs `candidates_for()`: all 1,237 nodes at depths 0–3 of both families + 340 sampled depth-4/5 nodes | 0 missed, 0 extra, 0 weight diffs |
| A2 dedup soundness | 1-in-97 verdict sampling (11,664 = 4,853+2,314+4,497, 0 mismatches) | DENSE: exact C-matrix equality of EVERY member vs class rep — 470,766 + 224,502 + 436,232 histories | 0 mismatches |
| Oracle | ported g2 | brute-force two-linear-extension checker: all 219 n=4 + all 4,231 n=5 posets + 900 sampled class reps; S3 rejected by both | 0 disagreements |
| Law clauses (i)(ii)(iv) | 0 violations | per-class independent recheck | 0 |
| Law clauses (iii)(v) | 0 violations | PER-HISTORY independent recheck (all 1.13M arb-containing) | 0 |
| Referee clauses T2/T3 (§4.5) | — (not in receipt) | 0 violations everywhere | new, stronger |
| F-CROSS pairs / census | 840; {direct 840p+840r, global 840p+1680r, parent 840p+1680r, interleaved 840p+840r} = 8,400 | scriptE independent protocol implementation | EXACT, 0 successes |
| F-CROSS width-3 gate | status-identical, global excluded | independent | True |
| Width-4 bit sweep | 1,920 attempts / 0 successes | independent | EXACT |
| 340 post-X states + width table | {2:15, 3:80, 4:150, 5:60, 6:35} | scriptD CR-0 rebuild | EXACT + all 340 dim ≤ 2 (closes F3) |
| F-LAM | 1,597 layouts, 0 dead, 0 dim failures | `.out` shape census re-summed (86 rows → 1,597, no DEAD) + byte-identical rerun | consistent |
| AG0b vs committed record | below 8, wsum 1037/64, 512/1037; [19/64, 25/64]; 4735/14016; 23595/66368; FAM 1,191 | committed `d43d...out` NG2 line ("8/1037/64"), d43d review F3 (med = 21/64), `d42b3...out` ("family: 1191") | EXACT; terminal d43d untouched (git) |
| Transport contrast | "4 actors / 6 events (d43d NG3b W4)" | W4 in committed d43d source: 6 events, 4 actors, 2 proposals + 4 deliveries, NO idles — scale-matched to AG2b (width 4, ≤ 6 events, no-idle); no hidden work in the no-idle qualifier | correct citation |
| Determinism | "seeds 0/7 + unseeded byte-identical" | PYTHONHASHSEED=0 and =7 reruns, exit 0 | both byte-identical to committed `.out` |
| LOG #351 vs artifacts | — | all quantitative claims traced | accurate except F2/F3 wordings (shared with the receipt verdict) |

## 5b. Beyond-cap probes (all green — the obstruction horn holds past the declared caps)

| Probe | Scope | Result |
|---|---|---|
| Exhaustive width-3 NO-IDLE **depth 8** (the receipt's declined cap) | depth-8 count = **954,288 — the receipt's declared growth-table estimate verified exactly**; 1,178,868 histories total, 18,603 word classes dim-checked | ZERO dim failures |
| Random width-4 no-idle depth 8 | 4,000 arb-biased samples → 3,143 classes (996 at width 4) | 0 failures |
| Random width-5 no-idle depth 11 | 4,000 samples → 3,987 classes (938 at width 5) | 0 failures |
| Random width-6 no-idle depth 14 | 2,500 samples → 2,500 classes (447 at width 6, n = 14) | 0 failures |
| Width-3 FULL grammar (IDLES) depths 7–8 — the stratum between AG1's cap and AG1b's no-idle scope | 5,724 distinct classes, 5,139 idle-containing | 0 failures |

---

## 6. Referee crown-construction attempts (all dead; the mechanism held everywhere)

1. **Triple-pool crowns (the construction space the pair-template does not
   parameterize):** all 2,300 pairwise-overlapping non-nested triples of 2/3-pools
   over 6 actors, executed in all 6 orders × {direct, global} × every available
   base (27,600 pool placements; scriptD CR-2). **No attempt ever placed even TWO
   overlapping pools** (census: all died at pool 2); the crown needs three.
2. **View-delayed cover-two (the sharpest manual route):** after a {A,B,C} mint,
   place A/B/C proposals on the mint, then arb {A,B} while C's conflicting
   proposal is LIVE but view-invisible — **admissible** (the receipt never
   exhibits this: cover-two with a live third conflictor on the same base). The
   crown then needs a second cover of B's consumed proposal: the full committed
   `candidates_for` offers only C's self-arb; zero {B,C} candidates — the
   single-consumption funnel (§4) exactly. Greedy arb-rich extension to n = 14,
   width 5: dim ≤ 2.
3. **Temporal variants** (mint-first, delayed proposals, interleavings) — covered
   exhaustively by AG1/AG1b/AG2b at caps and by my beyond-cap probes; the
   receipt's P3/P4/P5 death points reproduce.
4. **wkey-choice invariance of the constructed-arb convention (A4):** at a 3-pool
   state with 2 admissible wkeys, the full Y-fate vector is identical under both
   (scriptD CR-5) — the first-admissible-wkey convention loses no crossing route.

Outcome: no witness; the confinement mechanism (now the funnel lemma) explains
every death.

---

## 7. Mutation table (all six exit 1 — no silent greens)

| Mutant | Edit | Expected bite | Observed |
|---|---|---|---|
| mut1_lawiv_invert | clause-(iv) chain check inverted (counts comparable pairs) | AG3 law gate | [FAIL] AG3, exit 1 |
| mut2_s3_corrupt | AG0 S3 matrix corrupted (full bipartite) | AG0 anchor | [FAIL] AG0, exit 1 |
| mut3_dedup_coarse | dedup word = initiator only (arb co-authors dropped) | class-count anchors + soundness sampler | [FAIL] AG1 + AG1b, exit 1 |
| mut4_census_anchor | AG1 expected total 490,851 → 490,852 | census anchor | [FAIL] AG1, exit 1 |
| mut5_ag0b_strict | AG0b `d <= med` → `d < med` (the exact d43d-F3 bug class) | AG0b anchor (below 8 → 0) | [FAIL] AG0b, exit 1 |
| mut6_p1_bit_tilt | P1's F-proposal bit 1 → 0 (no conflict edge) | AG2a-P1 program | [FAIL] AG2a-P1 (+P3), exit 1 |

Anchored-expectation audit: every census dict/list/mass in AG1/AG1b/AG2b/AG2c/AG2d
sits inside a `check()` ok-condition (mut3/mut4 prove they bite); the single
uncensused check is AG5 (n1).

---

## 8. Reproduction appendix

- Environment: repo root `/Users/felixrobles/workspace/isp`, HEAD 6d8a74b, clean
  tree; python3; all commands run from repo root (required — see plumbing note).
- Committed run reproduced: `PYTHONHASHSEED=0 python3
  v10/code/d44c_arb_dimension_exact.py` → exit 0, byte-identical to
  `v10/data/d44c_arb_dimension_exact.out`; same with PYTHONHASHSEED=7.
- Referee scripts (session scratchpad
  `/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/`):
  `ref_layer.py` (layer loader + independent brute dim oracle);
  `scriptA_enum_completeness.py` (superset-vs-enumerator, 0 mismatches);
  `scriptB_census_dedup_laws.py` (independent censuses; dense dedup; laws +
  T1/T2/T3; oracle cross-check);
  `scriptC_beyond_caps.py` (W3 no-idle d8 exhaustive; W4 d8 / W5 d11 / W6 d14
  random probes); `scriptD_crowns.py` (340-state rebuild + dim; 27,600
  triple-pool attempts; view-delayed cover-two; wkey invariance);
  `scriptE_fcross_recount.py` (F-CROSS full census recount); `mut/mut1..mut6.py`
  (mutants; run from repo root so the layer path resolves).
- Cross-checks against committed ancestry: `v10/data/d43d_dstar_generated_exact.out`
  (NG2 "8/1037/64" line; NG3b W4/W6), `v10/code/d43d_dstar_generated_exact.py`
  (W4 = 6-event, 4-actor, no-idle), `v10/data/d42b3_placement_exact.out`
  ("family: 1191"), `v10/reviews/d43d-round1-hostile-review.md` (F3 median
  forensics; width doctrine), LOG #348 (print-repair assignment; check(True)
  tolerance), LOG #351 (claims audit).
- git: `git show --stat 6d8a74b` (4 files, all D44c); last commits touching
  d43d artifacts = 7b76312, d42b3 = 171c75a (both pre-D44c; frozen receipts
  untouched).

## 9. Scorecard vs the round's attack surfaces

1. Enumeration completeness — HELD (superset test, 0 missed; censuses exact).
2. Register-word dedup — HELD, upgraded from sampled to DENSE (0/1,131,500).
3. The law — HELD and STRENGTHENED (all-scale theorems + funnel lemma; S3
   impossible at every scale; scoping of the dim verdict stays as committed).
4. F-CROSS design — HELD; referee triples/temporal/wkey extensions all dead;
   340 states now dim-checked (F3).
5. Transport contrast — correctly cited, scale-matched.
6. AG0b print repair — exact against the committed record; d43d frozen.
7. Mutations — 6/6 exit 1.
8. Determinism / anchors / banner — byte-identical ×2; anchors bite; ONE banner
   falsity = F1 (the witness-horn exit semantics).

**Round-1 disposition: REVISE** — apply F1–F3 as LOG forward-corrections (no
receipt edit; the artifact is frozen and its numbers are all true); n1–n3 at the
author's discretion. On application this review expects delta-clean: the
headline, the law, and every number survive hostile recomputation; the review's
own contribution (funnel lemma + dense dedup + beyond-cap sweeps) is offered for
the successor's use.
