# D45b — round 1 hostile review: the S_n ladder / polyhedral confinement

**Object:** `v10/code/d45b_sn_ladder_exact.py` (879 lines) +
`v10/data/d45b_sn_ladder_exact.out` (372 lines, 40 PASS / 0 FAIL / 9 outcomes),
pin + amendments `v10/note-d45b-sn-ladder-polyhedral-confinement.md` (§1 doctrine,
§2–5 pin, §6 A1–A5), LOG #358, commit 4a304ce.
**Standard:** receipt review under the d43d/d44c-round precedent (two prior
dimension-headline inversions in this line; this receipt treated with equal
suspicion). Every witness rebuilt from scratch; every family re-admitted through
the committed d42b1 layer; the poset semantics re-implemented independently;
dimension adjudicated at DEFINITION level wherever feasible; widths PROVEN by dual
certificates; the ZG1 claim attacked on its scheduling freedom — where it broke.
**Review instruments** (session scratchpad, reproducible; appendix §8):
`verify_main.py`, `verify_sweep.py`, `diag_s3c.py`, `full_marked_sweep.py`,
`run_mutants.sh` + `mut/mut1..mut7`.

**Verdict: REVISE — 0 BLOCKER / 1 MAJOR / 3 minor / 3 nit.**
The unit's PRIMARY deliverable — the witness horn — is TRUE and survives every
attack this review could mount: the n = 3, 4, 5, 6 witnesses were rebuilt from
scratch (independent poset semantics, independent S_n references, every pairwise
relation audited, every event re-admitted, every weight re-derived from the d42b1
budget rule), the widths 2n−1 are now PROVEN (not just measured) by verified
chain-partition + antichain certificate pairs, the schema closed forms and
prefix-blindness check out, and the run is byte-identical under reruns and hash
seeds. The MAJOR is in the ZG1 arm: **"DIMENSION-SILENT" and "her f(N) = N route
is closed by the fused-join back-flow" are SCHEDULE-SPECIFIC facts presented as
pattern-level facts, and they are FALSE as generalized** — this referee exhibits
fully admissible reorderings of Charron-Bost's own message multiset (with the
pattern's own marks) at 4 and 5 actors whose whole posets have order dimension
> 2, confirmed at definition level. What survives ZG1 (and this review proves it
exhaustively at N = 4) is sharper and smaller: her designated-mark CROWN dies
under EVERY schedule, and no schedule of the bare deliveries escapes two clocks —
but the grammar at N ≥ 4 actors is NOT dimension-confined even on her own message
multiset. The pin's §1 scoping doctrine is fully complied with (no
Minkowski/spacetime claim anywhere; every mention is a disclaimer).

---

## 1. MAJOR finding

### F1 — MAJOR (CONFIRMED by referee counterexample, definition-level): the ZG1
### "dimension-silent / route closed by semantics" claims are schedule-specific
### and false as generalized — 248 of 40,320 marked schedules of CB(4) are
### admissible with order dimension > 2 at four actors

**The claims as committed.**
- Receipt lines 866–872 / `.out` line 372 (verdict): "The Charron-Bost port
  (ZG1) is fully admissible yet dimension-silent at N = 3, 4, 5 actors — her
  f(N) = N route is closed by the fused-join back-flow, NOT by an admission
  clause."
- Receipt lines 813–822 / `.out` line 365 (ZG5 prose): "the transport grammar
  REFUSES that route (ZG1: … all events admissible, **order confined to
  dim <= 2 at N = 3, 4, 5 actors**)".
- Note §6 A1: "Charron-Bost's pattern is FULLY ADMISSIBLE at N = 3, 4, 5 … yet
  DIMENSION-SILENT … The divergence with her model is SEMANTIC, not
  legislative."
- LOG #358: "the Charron-Bost port is FULLY ADMISSIBLE at N = 3, 4, 5 yet
  DIMENSION-SILENT … her f(N) = N route is closed by the grammar's two-carrier
  JOIN BACK-FLOW semantics" (repeated in the 4a304ce commit subject).

**The refutation.** The receipt ran ONE schedule per N (sequential rounds).
Her asynchronous model has no round barrier; the pattern is the message
multiset + the marks. This referee swept ALL 8! = 40,320 orderings of CB(4)'s
8 fused deliveries with the pattern's own marks placed exactly as the port
places them (4 min idles first; each round's upper idle immediately after that
round's last delivery; the identity ordering reproduces the receipt's CB(4)
history event-for-event). Result:

- **248 of 40,320 marked schedules have whole-poset order dimension > 2**, every
  one re-verified at DEFINITION level (all linear extensions streamed; no
  realizing pair exists; 0 oracle-vs-definition disagreements), NOT an oracle
  artifact.
- Every such history is **fully admissible** under the committed `admissible()`
  with exactly the ZG1 weights (idles 1/2, deliveries 1/12) — same actors, same
  messages, same marks, different interleaving.
- The exemplar (schedule (6,3,1,2,0,7,4,5); 16 events, 4 actors, reproduced in
  appendix §8) has dimension **exactly 3** (a 3-realizer was found; dim > 2 by
  exhaustion of all 6,432 LEs).
- At N = 5: 582 of 4,000 sampled marked schedules are dim > 2 (~15%).
- At N = 3: all 6 schedules are 2D — the N = 3 silence is real (and consistent
  with d43d's exhaustive 3-actor-2D-through-10).

So "order confined to dim <= 2 at N = 3, 4, 5 actors" is false at 4 and 5
actors; "DIMENSION-SILENT" is a property of the ported schedule, not of the
pattern, the actor count, or the semantics. A further sting: the receipt's own
ZG1 constructor with the hub mirrored (P_{i+1} for P_{i−1} — referee mutant
MUT7) yields a CB(5) poset with dim<=2 = False, and the receipt still passes
40/40 (see F2).

**The mechanism attribution is also confounded.** The ZG1 outcome texts say the
violated pairs "are precisely the back-flow edges" of the two-carrier join, and
the preamble says "In her one-way-message model this family forces dimension N"
(receipt lines 361–375, `.out` line 30). Referee check: splitting every fused
delivery into send;receive **under the same schedule** produces IDENTICAL
violated-pair sets at N = 3, 4, 5 — the crown failure of the ported object is a
SCHEDULE fact that her own one-way model reproduces verbatim. What her model has
and the grammar lacks is the sends-before-receives schedule (referee-verified:
it realizes the crown exactly in the one-way model at N = 3, 4), which the fused
join makes INEXPRESSIBLE. That is the true, defensible semantic divergence — the
receipt's back-flow prose gestures at it but attributes the violated pairs to
fusion rather than to the schedule fusion forces.

**What survives — referee-strengthened, and worth keeping:**
1. Her designated-mark crown NEVER survives: minimum crown violations over all
   40,320 marked N = 4 schedules is 4 (> 0); at N = 3, minimum 3 over all 6.
2. NO induced S3 exists in ANY of the 40,320 marked N = 4 schedules (including
   all 248 dim>2 ones — their dimension is carried by a non-crown
   3-irreducible). The crown route at f(4) = 4 actors, ≤ 16 events of this
   multiset, is genuinely closed.
3. The BARE deliveries never escape: all 6 (N=3) and all 40,320 (N=4) orderings
   and 5,000 sampled N=5 orderings of the delivery multisets alone are dim ≤ 2
   with VERIFIED realizer certificates. The idle marks are load-bearing for the
   escape — a structural fact the receipt never surfaces.
4. ZG1's gated facts (admissibility, weights, the three ported posets' 2D-ness,
   the single-N-antichain census, 5/9/14 violations) are all TRUE of the ported
   objects — independently reproduced here.

**Prescribed fix** (receipt frozen; record-level, the program's
forward-correction route): (a) a LOG row rescoping ZG1: "dimension-silent /
route-closed / order-confined" hold FOR THE PORTED SEQUENTIAL-ROUND SCHEDULES
ONLY; at N ≥ 4 actors the same admissible multiset+marks under other schedules
reaches order dimension 3 (referee counterexample, definition-level verified;
248/40,320 exhaustive at N = 4; 582/4,000 sampled at N = 5; N = 3 exhaustively
silent); (b) carry the referee's sharpened positive statement (items 1–3 above)
as the honest ZG1 result: the CROWN route is closed schedule-independently, the
DIMENSION claim is not; (c) the conversion note must not repeat A1's
"DIMENSION-SILENT" without the schedule scope; (d) optional delta gate: an
in-receipt sweep gate anchoring items 1–3.

---

## 2. minor findings

### F2 — minor (CONFIRMED by mutation): the ZG1 arm's scientific content is
### gate-free — a port-structure corruption with a DIMENSION FLIP runs 40/40
### GREEN at exit 0 under the same witness-horn verdict

ZG1.Na gates only admissibility + weights + prober consistency (receipt lines
489–494). ZG1.Nb's condition `(hit is None) == d2 or (not d2)` (lines 535–541)
PASSES WHENEVER d2 is False — a dimension flip in a CB poset trips nothing. The
violated-pair counts, the antichain census, and the 2D verdicts live only in
prints and outcome text. Referee mutant MUT7 (hub `P[(i+1) % N]` for
`P[(i-1) % N]`): **exit 0, 40 PASS / 0 FAIL, verdict "THE WITNESS HORN"**, with
CB(5) now dim<=2 = **False** — and the ZG1 N=5 outcome line would print the
internally contradictory "the whole 25-event poset has dim<=2 = False, so NO
induced subposet of any dimension > 2 exists (monotonicity)" — confirmed
verbatim in the mutant's output. Detection is byte-diff-only (107 changed
lines). Contrast ZG0.3, where the W6 witness IS
anchored. **Prescribed fix:** at delta or in the conversion receipt, anchor the
ZG1 structural facts as gates: expected event lists (or hub map), expected
violated-pair SETS per N, antichain census == 1, and d2 == True per ported N
(with the F1 rescope, d2's expected value is a schedule-specific anchor, which
is exactly why it should be gated).

### F3 — minor (CONFIRMED): ZG6.2 and ZG6.3 are literal `check(..., True)`
### prose gates — 2 of the 40 PASS are vacuous

Receipt lines 835–848: ZG6.2 ("scoping discipline …", `True, "scope held by
construction"`) and ZG6.3 ("exit design …", `True, "wired as stated"`) assert
nothing mechanically; they inflate the PASS tally that LOG #358 headlines
("GREEN 40/40"). The scoping fact itself is true (referee grep: every
Minkowski/spacetime token in receipt and `.out` is a disclaimer — banner,
docstring, ZG6.2's own label; zero positive claims), and the exit design is
genuinely wired (MUT1/MUT4). **Prescribed fix:** demote both to printed notes
(the honest tally is 38 mechanical gates), or make ZG6.2 a mechanical self-scan
with a disclaimer allowlist.

### F4 — minor (CONFIRMED true but unreceipted, mechanism misdescribed): A2's
### "the single-hop hub design PROVABLY LEAKS through sender-wire reuse
### (comparabilities among uppers)"

No proof and no receipt exists anywhere in the record (the receipt contains no
single-hop construction; the ZG2 preamble mentions it only in passing; LOG #358
repeats "provably leaks" as fact). Referee test of the natural single-hop
rendering (MIN_j; then (m_j → h_i) for j ≠ i; then U_i = (h_i → t_i)): the
crown DOES fail — but the observed leak is on the crown DIAGONAL (n = 3: 1
violation, n = 4: 2 violations, all a_j < u_i diagonal-type via m-wire →
h-wire back-chains), with **zero upper–upper comparabilities**. The uppers stay
pairwise incomparable; A2's parenthetical names the wrong mechanism (or an
undocumented different single-hop variant). **Prescribed fix:** at conversion,
either exhibit the intended single-hop design + its leak as a small gated
construction, or correct A2's parenthetical to the diagonal leak and mark the
claim referee-verified rather than "provably".

---

## 3. nits

- **N1.** Pin §4 ZG6 pre-registers "determinism gated"; the receipt has no
  determinism gate (no seed run, no double-run comparison in-receipt).
  Discharged only by the builder's pre-commit claim in LOG #358 — which this
  review independently confirms (3 reruns: unseeded, PYTHONHASHSEED=0, =7, all
  byte-identical to the committed `.out`). Record the gap or gate it next time.
- **N2.** The proof-note pointer is inconsistent: pin §4 ZG3 says "the §6 proof
  note", the receipt prints "the SS6 proof note" (line 783), but §6 of the note
  is now the A1–A5 amendments; LOG #358 says "the §7 proof note". Fix the
  pointer at conversion (§7).
- **N3.** ZG6.1's boolean verifies far less than its label claims (only
  "W widths non-None + CB count == 3"); the brute-vs-matching cross-gate it
  recites happened inline in ZG0.2/ZG0.4/ZG1.Nc. Also for the record: NO W(n)
  poset ever receives a brute width check (all are > 16 elements) — the width
  headline rested on the Koenig/Dilworth implementation alone. No damage: this
  review PROVES the widths (see §4), but the label should not imply a
  cross-gate that never ran on the objects it matters for.

Observation, no finding: from `v10/` the run dies with a raw FileNotFoundError
traceback (relative anchor paths; docstring declares repo-root). Same shape as
the committed d43d ancestor; acceptable as declared.

---

## 4. Independent-verification inventory (what was rebuilt, what was checked)

**Witnesses (headline 1) — REBUILT FROM SCRATCH, all confirmed:**
- Event lists: parsed from the committed `.out` AND regenerated independently
  from the documented constructor schema; identical for CB(3/4/5) and W(3/4/5/6).
- Admission: every one of the 172 W-events and 50 CB-events re-run through the
  committed `admissible()` with full prefixes — all admitted; weights re-derived
  from the d42b1 budget rule (deliver 1/4 split over the sender-view option set;
  pure-genesis holdings stay {v0}, so |opts| = A−1): 1/68, 1/108, 1/156, 1/212
  at A = 18, 28, 40, 54 — and W6's 1/20 at A = 6 confirms the same formula on
  the committed precedent. `.out` q-values match exactly.
- Posets: MY OWN builder (transitive closure of the share-a-carrier relation,
  my own regs semantics) == committed `event_poset` on every family.
- Crowns: induced 2n×2n matrices on (first n, last n) events == MY OWN S_n
  references (standard example: upper_i > min_j iff j ≠ i, nothing else; the
  n = 3 case is the 6-element three-crown — confirmed NOT a chevron or other
  3-irreducible), with explicit pairwise audits: 28/28 pairs at n = 4 and 66/66
  at n = 6, zero deviations. W6 == my S3 reference (regression confirmed).
- Crown carrier discipline: implied and re-checked (pairwise-disjoint pairs).
- Monotonicity use: correct in both directions (ZG2: dim ≥ n from induced S_n;
  ZG1: dim ≤ 2 excludes induced dim>2 subposets). dim(S_n) = n correctly cited
  (Dushnik–Miller standard examples, n ≥ 3).
- Dimension, independent of the ported oracle: S3, S4, S5 dim > 2 by EXHAUSTIVE
  definition-level search (all 48 / 720 / 17,280 linear extensions; no realizing
  pair); W6 likewise (48 LEs); S6 via the verified induced-S4-in-S6 monotonicity
  chain; whole W(n) posets dim > 2 forced by the verified crowns + monotonicity,
  with the ported oracle agreeing. CB(3/4/5) dim ≤ 2 = True verified by
  CHECKING THE ORACLE'S REALIZERS as certificates (C[i][j] iff both orders
  increase; all pairs), CB(3) also by definition (10 LEs). Zero
  oracle-vs-definition disagreements anywhere in this review (including all 248
  + 26 dim>2 sweep posets re-proved by exhaustion).
- Widths: PROVEN by dual certificates (my own matching → verified chain
  partition of size w; my own König construction → verified antichain of size
  w): W(n) = 2n−1 exactly (5/7/9/11), CB(N) = N, S_n = n, W6 = 3. The receipt's
  "measured 2n−1" is now a theorem-grade number at the base cases.
- ZG1 facts: exactly ONE N-antichain per CB(N) (it is the minima block);
  violated-pair sets recomputed and IDENTICAL to the `.out` listings (5/9/14;
  diagonal i ≥ 2 + full upper chain; all FORBIDDEN-type, none missing).
- Schema: closed forms (n²+3n, 2n², crown = first/last n) re-derived;
  prefix-blindness verified beyond the receipt (22 permutations of W(4)'s 32
  events incl. reversal and uppers-first: every event admissible at 1/108).
- Port fidelity: `is_comparability`, `topo_rank`, `dim_le_2`, `all_posets`,
  `width_brute` line-identical to the committed d43d source.
- Anchors: d42b1 marker char 16129, 959 lines; 219 labeled 4-posets recomputed;
  the 4,231 n=5 citation matches the committed d43d `.out` (NG1); "3-actor 2D
  through 10 events" matches d43d NG3b verbatim; W6 event list matches d43d's.
- Determinism: 3 reruns byte-identical to the committed `.out` (unseeded,
  PYTHONHASHSEED=0, =7); working tree clean at 4a304ce; `.out` tallies
  internally consistent (40/0/9 counted).
- LOG #358 audit: every claim accurate against the artifacts EXCEPT the F1
  sentence (and the A2 "provably leaks" repetition, F4); "n = 6 uncapped",
  "closed forms 4/4", "prefix-blind schema", "#354 binding wired by mutation"
  all check out.

**The attack that landed (F1):** exhaustive 40,320-schedule marked sweep at
N = 4 + 4,000-schedule sample at N = 5 + one-way-model schedule cross-exam
(§1 above).

---

## 5. Mutation table (referee's own battery; all runs from repo root on
## scratchpad copies; committed files untouched)

| # | mutation | expected per receipt design | observed | verdict |
|---|----------|------------------------------|----------|---------|
| MUT1 | courier rewire: `SH(0,1) → h1` at n=4 | ZG4 ceiling outcome, exit 0 | exit 0; 36 PASS / 0 FAIL; "OBSTRUCTION (order) … deviates from S_4 at 2 pairs"; verdict flips to THE CEILING ARM | as designed (#354); byte-diff catches |
| MUT2 | weight tilt: q_exp = 1/(4A) | exit 1 breakage | exit 1 at ZG2.3a | correct gate |
| MUT3 | S_n reference break: crown diagonal added | exit 1 | exit 1 at ZG0.1 (first anchor) | correct gate |
| MUT4 | crown index swap: ups[0]↔ups[1] | ZG4 ceiling, exit 0 | exit 0; 4× OBSTRUCTION; verdict THE CEILING ARM; 0 FAIL | as designed (#354); a designation bug presents as the ceiling horn — discrimination is verdict-text/byte-diff, per the pre-registered both-horns-exit-0 design (d44d M5/M8 precedent) |
| MUT5 | oracle sabotage: dim_le_2 ≡ True | exit 1 | exit 1 at ZG0.1 | correct gate |
| MUT6 | W6 anchor corrupt: receiver E→D | exit 1 | exit 1 at ZG0.3 | correct gate |
| MUT7 | CB hub off-by-one: P_{i+1} for P_{i−1} | (none — hole) | **exit 0; 40 PASS / 0 FAIL; verdict THE WITNESS HORN; CB(5) dim<=2 flips to False unpunished (107-line text diff only)** | SILENT-GREEN at gate level → F2 |

A5's claims are verified: constructor corruption → ZG4-at-exit-0 (MUT1, MUT4);
oracle/weight corruption → exit 1 (MUT5, MUT2). The #354 witness-branch binding
is genuinely wired: both horns are reachable exit-0 delivered outcomes, and the
ceiling outcome, when it fires, truthfully reports the induced-matrix deviation
it found. The hole is MUT7's arm (F2), not the branch design.

---

## 6. The referee counterexample (carried for the record)

Fully admissible pure-transport history, 4 actors (P1..P4), 16 events — CB(4)'s
exact message multiset with the pattern's marks, schedule (6,3,1,2,0,7,4,5) of
the receipt's own msgs order; weights: idles 1/2, deliveries 1/12:

```
e00 ('n','P1')  e01 ('n','P2')  e02 ('n','P3')  e03 ('n','P4')
e04 ('d','P1','P3',v0)   e05 ('d','P4','P1',v0)   e06 ('d','P3','P4',v0)
e07 ('d','P3','P1',v0)   e08 ('n','P1')           e09 ('d','P2','P4',v0)
e10 ('n','P4')           e11 ('d','P2','P3',v0)   e12 ('n','P3')
e13 ('d','P1','P2',v0)   e14 ('d','P4','P2',v0)   e15 ('n','P2')
```

Properties (all referee-verified): every event admitted by the committed
`admissible()`; whole-poset order dimension EXACTLY 3 (dim > 2 by exhaustion of
all 6,432 linear extensions — no realizing pair; a 3-realizer exists); NO
induced S3 (8 three-antichains, no disjoint crown pair); its own designated
marks still violate the crown (5 pairs). One of 248 such schedules among all
40,320 (exhaustive; every one definition-level confirmed).

---

## 7. What this round settles

- Headline 1 (the witness horn) — VERIFIED, unbroken, now carrying
  referee-proven widths. The strongest result of the unit stands exactly as
  committed.
- Headline 2 (the all-n schema) — verified at the base cases; honestly scoped
  as [THEOREM candidate]; prefix-blindness independently confirmed and is a
  real feature of the pure-genesis sector.
- Headline 3 (ZG1) — REFUTED AS GENERALIZED (F1); survives only as the
  schedule-scoped statement plus the referee's sharpened crown-closure facts.
- Headline 4 (mutation sanity / #354 wiring) — verified, with one gate-free arm
  found (F2).

---

## 8. Reproduction appendix

Scratchpad: `/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/`

- `verify_main.py` — R1–R10: parse+regenerate families; re-admit everything;
  independent poset builder + crown audits; definition-level dim checks
  (LE-mask); CB realizer certificates; antichain census + violated-pair
  identities; dual width certificates; prefix-blind probe; single-hop leak
  test; one-way schedule cross-exam; anchor checks. (Two R-FAILs in its raw
  output are the harness's own LE-cap on S6, closed by `verify_sweep.py` S1.)
- `verify_sweep.py` — S1 S6-monotonicity closure; S2 fused-vs-one-way
  violated-pair identity; S3a/b/d bare-delivery ordering sweeps (exhaustive
  N=3,4; sampled N=5) with certificates; S3c the marked-schedule sample that
  first fired; S4 port-fidelity diff (its width_brute line is a harness regex
  artifact; the manual body diff confirms verbatim identity).
- `diag_s3c.py` — first failing marked schedule: admissibility, definition-level
  dim, S3 hunt, crown violations.
- `full_marked_sweep.py` — the exhaustive 40,320 marked N=4 sweep (248 dim>2, 0
  oracle-vs-definition defects, 0 induced S3, min crown violations 4), N=3
  exhaustive (0), N=5 sample (582/4,000), exemplar exact dimension 3.
- `run_mutants.sh`, `mut/mut1..7.{py,out}` — the mutation battery of §5.
- Determinism: `python3 v10/code/d45b_sn_ladder_exact.py` from repo root, plus
  PYTHONHASHSEED=0 and 7 — all byte-identical to
  `v10/data/d45b_sn_ladder_exact.out` (~1 s each).

*Round 1 closed. Disposition requested: forward-correction row for F1 (rescope +
referee-carried counterexample and sharpened positive facts), F2/F3/F4 repairs at
delta or conversion, nits at the author's discretion. The receipt itself can
stay frozen: every gated number in it is true.*

---

# DELTA VERIFICATION — round-1 repairs (commit c686ff2, LOG #365)

**Round-1 body above: untouched (byte-verified — the committed review file is the
referee's round-1 text verbatim; working tree clean at HEAD).**

## Verdict: DELTA-CLEAN — d45b may convert to TERMINAL

Every discharge verified by execution; the two declared deviations adjudicated
(one now closed outright by delta-time verification, one confirmed in-scope);
zero new findings above nit. The mechanical diff 4a304ce → c686ff2 on the d45b
paths (LOG +46, receipt +372/−73, .out +60, note +86 → 240 total, + this review
file committed verbatim) was read in full and contains exactly the enumerated
repairs — no arithmetic, no ZG0/ZG2/ZG3/ZG4 gate logic touched.

## D1 — discharge verification

- **F1 (MAJOR) — DISCHARGED, receipt-gated.** ZG1S reproduces the referee sweep
  in-receipt from an independent implementation of the mark rule: ZG1S.1
  identity-reproduction gate (ported CB(4) event-for-event, marks [6,9,12,15] —
  matches the referee's rule by construction and by outcome); ZG1S.2 **exactly
  248/40,320** (the referee's number, reproduced); ZG1S.3 min crown violations
  == 4; ZG1S.4 248/248 S3-free by direct search + monotonicity for the 40,072;
  ZG1S.5 the frozen-appendix exemplar reproduced event-for-event, re-admitted
  event-by-event at the ZG1 weights, dim<=2 == False, 5 violations; ZG1S.6/7
  bare-delivery sweeps (40,320 + 6) and the N = 3 marked sweep (6) all 2D —
  idles load-bearing, N = 3 genuinely silent; N = 5's 582/4,000 correctly kept
  REVIEW-CARRIED (RNG-free receipt). All numbers match the frozen round exactly.
  The rescopes landed everywhere the round named them: the three ZG1 outcome
  texts, ZG5's prose, the final verdict (both F1-quoted sentences replaced), and
  LOG #365 forward-corrects #358's two sentences BY NAME.
- **F1 mechanism story — FAITHFUL.** The rewritten N = 3 dichotomy outcome now
  states precisely the round's finding: the violated pairs are SCHEDULE facts
  (one-way split under the same schedule reproduces the violation sets verbatim,
  referee-verified at N = 3, 4, 5 — correctly scoped); the true divergence is
  EXPRESSIBILITY (sends-before-receives realizes the crown in her model at
  N = 3, 4, referee-verified — correctly scoped; inexpressible under fusion).
  No residue of the "back-flow edges" attribution anywhere.
- **F2 — DISCHARGED and delta-mutation-verified.** ZG1.Nd anchors (events
  9/16/25; violations 5/9/14; ported-schedule dim<=2 == True as explicitly
  SCHEDULE-SPECIFIC anchors — the right epistemic status post-F1; census == 1;
  no induced crown). **Delta MUT7 rerun (hub mirror, P_{i+1} for P_{i−1}): exit
  1 with 4 named FAILs — ZG1.3d, ZG1.4d, ZG1.5d, ZG1S.5.** The round's
  silent-green hole is closed.
- **F3 — DISCHARGED and delta-mutation-verified.** ZG6.2 is a live token-level
  self-scan (4 token lines, 0 undisclaimed; split-literal tokens avoid
  self-trigger). **Delta MUT8 (an added undisclaimed line "…estimates the
  Minkowski dimension of the universe"): exit 1 at ZG6.2** — the scan genuinely
  fires. ZG6.3 demoted to a printed note, no longer counted; every remaining
  PASS is mechanical. Tally arithmetic checks: 40 − 1 (ZG6.3) + 3 (ZG1.Nd) + 7
  (ZG1S) = 49.
- **F4 + nits — DISCHARGED.** Note §7 records the A2 correction with the
  referee's actual mechanism (crown-DIAGONAL leak, n=3: 1 / n=4: 2, ZERO
  upper–upper; "provably" downgraded to referee-verified, honestly marked
  REFEREE-CARRIED/unreceipted); banner determinism line added (N1); proof-note
  pointer fixed to §8 in receipt, note, and LOG (N2); ZG6.1 label aligned to its
  boolean, with the no-brute-width-on-W(n) fact now stated in-gate (N3).

## D2 — deviations adjudicated

1. **Per-schedule admissibility not re-gated in the 40,320 sweep: ACCEPTED —
   and now CLOSED.** The in-receipt justification (idle absorption is
   unconditional in the committed layer; genesis deliveries are prefix-blind,
   with the schema gated mechanically at all 172 base-case events) is sound,
   and the exemplar is re-gated event-by-event. Beyond acceptance, this delta
   MECHANICALLY re-admitted every event of ALL 248 dim>2 schedules through the
   committed `admissible()`: **248/248 fully admissible, every event at the
   ZG1 weights (idles 1/2, deliveries 1/12)**. The deviation is thereby
   discharged outright, not merely carried. (Annotation, nit-level: LOG #365's
   parenthesis "the referee verified all 248" was, at round-1 time, exact for
   the definition-level DIMENSION verdicts; admissibility was
   exemplar-mechanical + schema-semantic. As of this delta it is exact for
   admissibility too.)
2. **ZG5 prose + final verdict rescoped beyond the enumerated task list: NOT
   OVERREACH.** Both sentences were quoted verbatim in round-1 F1 and their
   rescope was explicitly prescribed there ("the ZG5 prose, the verdict
   sentence"); leaving them would have left the refuted claim standing in the
   committed record. The new texts are faithful to the round.

## D3 — mechanical verification

- Reruns from repo root: unseeded + PYTHONHASHSEED=0 + PYTHONHASHSEED=7 — all
  three BYTE-IDENTICAL to the committed `.out`; exit 0; 49 PASS / 0 FAIL / 10
  delivered outcomes; ~29 s (matches the declared runtime).
- Diff scope: exactly the five files above; no d45b artifact touched after
  c686ff2 (verified against HEAD 33ab0ef).
- LOG #365's summary of the round is faithful (verdict counts, the F1 story,
  the witness-horn inventory, the forward-correction), with the one nit-level
  annotation in D2.1. "note §7 (240 lines)" = the note's new total length —
  correct (240).
- Wording audit of the new claims: "reach dimension 3 at N = 4" is
  exemplar-witnessed (the round pinned the exemplar at EXACTLY 3; all 248 are
  gated dim > 2) — accurate as stated.

## D4 — new findings

**None above nit.** The two nit-level annotations (D2.1 LOG parenthesis; D3
wording note) require no action.

## D5 — terminal endorsement

The stamped terminal condition is MET: MUT7-class corruption is caught (exit 1,
four named anchors), the sweep gates reproduce the frozen round exactly, the
mechanism story is faithful, both deviations are adjudicated (one closed, one
in-scope), and no new findings above nit exist. The referee endorses conversion
to TERMINAL with the coordinator's stamped statement, each clause of which this
round and delta verified: the S_n witness ladder by the uniform courier-firewall
constructor (actors n²+3n, events 2n², width 2n−1 — widths certificate-proven in
round 1); unbounded order dimension at the tested ladder as ORDER dimension only
(§1 doctrine held, now mechanically scanned); the all-n schema with the §8 proof
note at conversion; the Charron-Bost comparison schedule-resolved (crown dead
under every schedule; sends-first inexpressible under fusion; dimension route
open at N ≥ 4, 248/40,320 receipt-gated, idles load-bearing); the ceiling horn
did not fire.

*Delta closed. — the d45b round-1 referee*
