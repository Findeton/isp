# D42a round 1 — hostile review (pin + receipt + out)

**Reviewer round:** 2026-07-18, against HEAD 2b8c300. Objects: the pin
`v10/note-d42a-proposal-grammar-and-conflict-fixture.md` (§§1–5 + A1–A5 + A5'),
the receipt `v10/code/d42a_generated_conflict_exact.py`, the output
`v10/data/d42a_generated_conflict_exact.out`, read against
`v10/note-d42-conflict-generating-law-pin.md`, paper 25 §§10–11, and LOG
#281–#284. Method: 4 reruns under varied `PYTHONHASHSEED` (0, 1, 42, 31337);
a clean-room re-implementation of the entire enumeration + every census
(my own poset/component/MIS/K1/K2/extension-count code, written from the pin
text, not the receipt's loops); a pin-faithful second enumerator; a
pin-literal carrier variant; two mutation runs (exit-plumbing and G3i
sensitivity); and a driver that runs the receipt's own `admissible()` against
its own `candidates_for()`. Scripts in the session scratchpad
(`d42a_counterexample.py`, `d42a_independent_verify.py`, `addendum2.py`,
`mutant_plumbing.py`, `mutant_enum.py`); nothing in the repo was modified
except this file.

## VERDICT: 1 BLOCKER / 2 MAJOR / 4 minor / 2 nit

Every printed number reproduces exactly in a clean-room rebuild of the
receipt's semantics — the arithmetic is not the problem. The BLOCKER is the
sixth instance of the standing conviction class: the receipt contains two
inequivalent definitions of "the generated arbitration opportunity" —
`admissible()` (past-local, matches pin §2) and `candidates_for()`
(global-record-view) — which provably disagree at 1,016 points of the ARM-1
family alone, and the family, every family census, G3i's sweep domain, and
the verdict line are built on the second while the pin, the mu factors, G1,
and the battery are built on the first. The receipt's own docstring asserts
they coincide ("superset generation + past-relative admission filter"); that
assertion is false.

---

## F1 — BLOCKER (CONFIRMED): the enumerator and the admission relation
## define different grammars; the family is not the pinned grammar's family

**The witnesses (all produced by the receipt's OWN functions, loaded
byte-identically and driven from outside):**

Witness 1 — an admissible event the enumerator never generates. With
`pA0 = ('p','A',V0,0)`, `pB1 = ('p','B',V0,1)`,
`selfA = ('r','A',{('A',V0,0)},{('A',V0,0)})` (A's uncontested self-arb of
its own singleton, per A5(ii)):

```
admissible([pA0,pB1], selfA)  = (True, Fraction(1, 4))
selfA in candidates_for([pA0,pB1])  = False
selfA in candidates_for([pA0])      = True
```

`admissible()` implements pin §2 as amended: in past(e) = A's wire, A's
proposal is live, its component is the singleton, "C maximal in past(e)"
holds, v0 unsuperseded, w is the MIS. A5(ii)'s own words: "A singleton live
proposal IS a (trivial) component, so its proposer may self-arbitrate."
`candidates_for()` denies the option because it draws arb candidates only
from the components of the FULL-record view, where B's causally disjoint
proposal has glued A's proposal into the pair. Sweeping the whole enumerated
ARM-1 family: **1,016 admissible-but-omitted arb events** (singleton
self-arbs suppressed by globally visible conflicts). The omission is
confined to the arb sector (the proposal loop ranges over all full-view
bases and filters by `admissible`, hence is complete; idle is always
offered).

Witness 2 — the family is not closed under linear extensions.
`[pA0, selfA, pB1]` IS in ARM-1; its linear extension `[pA0, pB1, selfA]`
is NOT, although both have the same canonical typed DAG (`canon` equal),
the same mu (1/256), and every factor of the excluded order is admissible
per the receipt's own `admissible()` — G1's machinery itself verifies those
factors. So "enumeration interleaving is bookkeeping" (pinned G1, D33
incomparable-order-gauge) is true of the factors and FALSE of the family's
support: whether a record is reachable depends on the gauge order in which
causally incomparable events are interleaved.

Witness 3 — a hidden normalization the pin disclaims. At `[pA0,pB1]` the
enumerated options per initiator sum to exactly 1 (pair-arb 1/8 + 1/8 +
idle 3/4), and this holds at **11,502 of 11,502** actor-points across the
enumerated ARM-1 family. Under the pinned law the sum at that point is
**5/4** (the admissible blind self-arb adds 1/4), and over the pin-faithful
family per-initiator sums exceed 1 at 1,016 actor-points (all with value
5/4). The pin (A4) says global normalization is NOT claimed (d34b
inherited); the receipt's family nevertheless exhibits an unclaimed,
undeclared per-initiator normalization — purchased entirely by the unpinned
global-view filter. This answers the A4-smuggling question: nothing is
smuggled inside the A4 denominators themselves, but the enumerator quietly
restores the very normalization the pin disclaims, masking the true size of
the placement problem (which under the pinned law already breaks
per-initiator sub-normalization at depth 2, not merely joint placement).

**Quantified consequences (my pin-faithful enumerator vs the receipt):**

| quantity | receipt prints | pinned-grammar value (mine) |
|---|---|---|
| ARM-1 family (depth ≤ 5) | 5,751 | 6,471 |
| ARM-2 family (depth ≤ 4) | 5,761 | 6,589 |
| fork (history,base) pairs, ARM-2 | 48 | 72 |
| fork pairs, ARM-1 | not printed | 424 (receipt-family: 288) |
| orphan census, ARM-2 | 1,128 | 2,088 |
| join census, both arms | 2,808 | 3,096 |

Invariant under the repair (verified on the pin-faithful family):
L1 (0 duplicates over 13,060), per-observer fork-freeness (0 violations),
the depth-2 conflict census (4), mu(seed pair) = 1/64, the G5 kernel block
(2/3, 1/3; 1/2, 1/2; TV 1/6; 1/3072; 1/4096), the battery (7/7), and the
G3i pair-iff (0 violations over the pin-faithful ARM-1). Witness 2's
asymmetry heals: both orders are in the pin-faithful family.

**Where the pin itself is implicated.** Original §4-G3 said "the arb option
is enabled at H iff its component is in the record" — a record-level
(global) phrase — while §2's admission is past(e)-relative and A5(ii)
grants self-arb to any live singleton. The receipt implements the global
reading for generation and the local reading for admission and never says
two notions are in play. Under the global reading the batch is closed by
the full record — which is precisely paper 25 §11.1's batch-close mark, now
computed from the global record rather than supplied, and gauge-dependent
(witness 2). Under the local reading (§2, A5(ii)) the enumerator is simply
incomplete. Either way the round's headline — ".out: the batch, the
conflict, the arbitration opportunity ... GENERATED from the record under
the pinned grammar" — is wider than the computation: what was computed is
the family of one specific global-view generator that the pin never
licenses and the docstring misdescribes.

**Classification:** the family-level numbers are not arithmetically wrong
for what the code computes (all reproduce in clean-room); the claims
attached to them ("the pinned grammar's family", "family-wide", the verdict
line) are wider than the computation, and the docstring's superset claim is
a false statement about the code. G3i is NOT a cannot-fail gate (see M2
below) — its miss is object confinement (pair option only) plus domain bias
(it sweeps only the enumerator's own family), not vacuity.

## F2 — MAJOR (CONFIRMED): pin §2's arb carrier list contradicts A2 and
## G4c; the receipt implements an unpinned carrier set

Pin §2: arbitration "Carriers: C's proposers + base + the new version."
The receipt's `regs_of` gives an arb the carriers proposers + new version —
**no base wire**. This is not pedantry: under the pinned d34a wire closure,
if the base were a carrier, any two arbs on the same base would share the
base wire and be chained into comparability, so the second would see the
first's supersession and be inadmissible — forks would be grammatically
impossible. Verified by running the enumeration with base-in-arb-carriers:
ARM-2 fork census = **0** (vs 48 printed; family size 5,713). So under the
pin's literal carrier text, A2's "incomparable arbs on one base are
grammatical" is false and G4c's `forks > 0` gate FAILS. A2 asserts forks
are grammatical "because admission is past-relative" — but past-relativity
does not rescue it; only dropping the base from the carrier set does, and
no amendment ever did that. The receipt silently implements the fix.
Classification: pin-internal inconsistency + receipt deviating from the pin
text it claims to run strictly against. Repair R2 below.

## F3 — MAJOR (CONFIRMED): pinned G1's "every enabled-set ... INVARIANT"
## clause is not discharged, and for the operative enumerator it is false

Pinned G1: "every enabled-set and every mu factor recomputed along every
linear extension of every enumerated history is INVARIANT." The gate as
coded recomputes admission and the mu factor of the history's own events
plus the canonical DAG — it never recomputes an enabled-SET (the option
set at a prefix). The check label honestly describes what it computes
("admission, every mu factor, and the canonical typed DAG"), so this is a
pin-clause-vs-gate gap, not a label lie. But the gap is load-bearing:
for `admissible()` the enabled-set at a record point is past-local and
order-invariant; for `candidates_for()` — the function that actually builds
the family — reachability of the very same typed DAG depends on the
interleaving (F1 witness 2). The one gate pinned to catch scheduler
residue in the opportunity structure was pointed at the factors, where the
law is clean, and not at the option sets, where the residue lives.
Classification: gate does not exercise the object named by the pin's gate
text (the standing conviction class); repaired for free by R1+R3.

## F4 — minor (CONFIRMED): G3ii's "family-wide sweep" is ARM-1 only

The G3ii loop is `for h in ARM1:`; ARM-2 is never swept, while the printed
label says "family-wide sweep" immediately after the banner establishes the
family as ARM-1 + ARM-2. Headline wider than computation (the conviction
class), though the fact survives: I ran the same sweep over ARM-2 —
**0 violations** (repair pre-verified). Also note the sweep checks
list-order precedence ("strictly earlier in the record"), which is the
right check here since admission already forces causal precedence.

## F5 — minor (CONFIRMED): fork census mis-scoped; ARM-1's forks and
## orphans are uncensused

The .out's G4c detail "forked histories = 48" and LOG #284's "forks 48"
are unqualified; the loop is ARM-2 only. The enumerated ARM-1 family
contains **288** forked (history,base) pairs (my rebuild; 424 under the
pinned grammar) and **1,376** orphan instances (2,088/1,960 pin-faithful
ARM-2/ARM-1), none censused. A2's obligation is "incomparable forks are
CENSUSED"; discharged only for ARM-2. (G4b's own label honestly says "in
ARM-2"; G4c's number line does not.) ARM-1 in-family observer violations:
0 (verified), so nothing false is admitted — the census scope is simply
narrower than the printed sentence. Pre-verified numbers above for the
repair.

## F6 — minor (CONFIRMED): G8 gates 3 of the 7 pinned distinctions

Pinned G8 declares distinctions (proposer, base, payload, component,
winner set, authors, initiator) with gate "declared-distinct histories
yield distinct typed DAGs." The receipt tests payload, initiator, winners,
plus the gauge identity. Proposer, base, and component separations are
untested. I pre-verified all three separate `canon` trivially (canon embeds
the full typed event tuple, so any event-data distinction separates).
The check's claim sentence lists only what it tests (honest); the detail
line recites all seven and reads as if gated. Low risk, cheap repair (R6).

## F7 — minor (CONFIRMED): L1 is relied on at all depths but only
## censused; it is in fact a theorem — upgrade it

`View.live` resolves proposals by triple membership at every admission
call, at every depth, including hand-fed G1/G4 events — the receipt's
comment says the triple-identity is "asserted globally by the L1 census,"
but a census over 11,512 histories asserts nothing globally. The reliance
is nevertheless sound at ALL depths:

**Theorem (live-triple uniqueness).** No history of the grammar (§2 +
A1–A3, receipt carrier semantics) contains two proposals `('p',a,b,·)` —
hence live triples are unique. *Proof.* A proposal by `a` carries `{a}`
(A1), so a first proposal p1 = ('p',a,b,x1) lies on a's wire and is in
past(e) of any later a-event e = ('p',a,b,x2). Case 1: p1 unresolved in
past(e) — the A3 blocker rejects e. Case 2: p1 resolved in past(e) — the
resolving arb r has p1's triple in its ckey, so r's base is b and r
supersedes b; r ∈ past(e), so b is superseded in past(e) and admission
rejects e. QED. (Verified empirically: 0 duplicates over the receipt's
11,512 AND over the pin-faithful 13,060.) Repair R7: record the proof;
keep the census as a tripwire. Note the proof uses A1 (carriers {a}) and
single-base ckeys — both receipt semantics — so it survives R1 unchanged.

## F8 — nit (CONFIRMED): G1's "761 histories" double-counts SIG1

SIG1 is already in the depth-4-arb slice of ARM-1 and is appended again:
761 entries = 760 distinct histories (SIG1 twice), 2,421 resequencings
include SIG1's 2 extensions twice. Harmless re-testing; the printed count
misdescribes distinct coverage by one.

## F9 — nit: latent fragility, no in-family hazard

`sorted(ckey)` over triples relies on distinct first elements (proposers)
to avoid a mixed-type str-vs-tuple comparison; guaranteed in-family by the
L1 theorem. `next(iter(op[2]))[1]` extracts the base from an arbitrary
ckey member; deterministic only because ckeys are single-base by
construction. Malformed hand-fed events would crash (loudly), not corrupt.
Defensive note only.

---

## GATE-QUALITY AUDIT (the assigned soft spots)

- **(a) candidates_for / G3i:** convicted — F1. On sensitivity: mutation
  M2 (drop all multi-member arb candidates from `candidates_for`) makes
  G3i FAIL ("sweep over 4071 histories" — note the family itself shrank)
  and G6 FAIL, exit 1. So G3i genuinely compares the enumerator against an
  independent record predicate and can fail — for the PAIR object. Its two
  blind spots: it never asks about non-pair options (where the 1,016
  disagreements live), and its sweep domain is the enumerator's own family.
  My independent iff-sweep with the cleaner predicate (both triples
  unresolved in the full view) also passes 0/5,751, and 0 on the
  pin-faithful family — the pair-level iff itself is solid.
- **(b) A4 denominator split:** internally clean — the propose candidate's
  own past IS the initiator's view (carriers {a}), so no choice is being
  made there; the arb denominator counts components in the join's past,
  as pinned. What the printed "joint-placement not claimed" under-declares
  is that under the pinned law even per-initiator sub-normalization fails
  (5/4 at depth 2) — currently masked by F1's filter (witness 3). Honest
  post-R1 wording must say so.
- **(c) L1:** sound at all depths; proof supplied (F7). Nothing downstream
  breaks at depth 6+.
- **(d) auth_only / G4a:** real, two-sided. My own causal admissibility
  rejects the stale re-proposal `(False, None)`; my independent
  re-implementation of issuance-validity (base exists + prior freed)
  admits it. A broken causal check that admits ⇒ `not ok_causal` fails the
  gate; a broken auth_only that rejects ⇒ the conjunction fails. The
  contrast event (winner re-proposing the opposite payload on the dead
  base, prior freed by A3) isolates supersession as the sole causal
  blocker, as labeled. Limitation: single-point exhibit, not a sweep —
  acceptable for an exhibit gate; the family-level staleness work is done
  by G4b/G4c.
- **(e) G3i's live_both:** extensionally correct over ARM-1. The
  `set(e[2]) & set(SIG_CK)` proxy catches resolution of either proposal
  and (in ARM-1, where every v0-arb ckey ⊆ {tA,tB} by the L1 theorem) all
  v0 supersession; singleton-arb histories such as `[pA0, selfA, pB1]`
  (which ARE in-family) are correctly classified; created-version
  components neither intersect nor block. The proxy would need care in a
  three-actor sweep (a `{tC}` arb intersects nothing while forking v0),
  but there the pair option genuinely persists in the initiators' pasts —
  and G3i is ARM-1-scoped and printed as such.
- **(f) K1 fidelity (RF3):** faithful. My independent tally over the 3!
  orders: {P,R} 4/6 = 2/3, {Q} 2/6 = 1/3, exactly paper 25 §10.2;
  normalization total = |C|! exact; kernel applied component-locally, and
  the winner draw enters mu as ONE factor per arb (the composite click,
  RF3). Paper 25's "participants remain unused" greedy is the D36-carrier
  conflict relation; d42a's conflict-graph greedy is the correct
  abstraction of it and reproduces the paper's numbers on the fixture.
  Battery line 5 correctly uses the direct edge law (1/2), not the
  restricted path law — consistent with §11.2.
- **(g) depth-cap honesty (RF5):** the banner's caps are the caps used
  (ARM-1 5, ARM-2 4, G1 = depth≤3 full + depth-4-arb + signatures —
  verified against the code). Label-wider-than-loop instances: F4 (G3ii),
  F5 (fork census line), F6 (G8 detail line), and the receipt comment in
  F7.
- **(h) A5' arithmetic:** CONFIRMED three ways. From the pinned law by
  hand: after `[pA0]`, v0 is a's only held base and carries a live prior
  (A3), so the propose sector is empty and its 1/4 is absorbed; the
  singleton component keeps the arb sector open; idle = 1 − 1/4 = 3/4.
  My independent `q_of` battery reproduces all 7 values. In-family idle
  census: the ONLY idle weight reached in either arm is 3/4 — confirming
  A5's 1/2 was false and A5''s unreachability declaration (1/2 and 1) is
  true at fixture depths. §2-as-amended is unambiguous here: "absorbs each
  unavailable total" admits no split-over-zero reading.

## PLUMBING, SEEDS, DETERMINISM, LOG

- **Exit-1 by design:** CONFIRMED. Mutation M1 (one wrong expectation,
  G2a 4→5) → "[SUMMARY] 14 PASS / 1 FAIL", "[VERDICT] FAIL — exit 1 by
  design", exit code 1. A single failing gate among 14 passes exits 1.
- **Seed-independence:** CONFIRMED for 4 seeds (PYTHONHASHSEED 0, 1, 42,
  31337): byte-identical to the committed .out, exit 0, ~3.6 s each.
  (LOG #284 claims 0/17; consistent with, though wider than, my check.)
- **Determinism hazards:** audited — every printed quantity is
  hash-order-independent (bases and options repr-sorted; components built
  from insertion-ordered dicts keyed by deterministic history order;
  censuses are sums; G5a prints sorted). The F9 fragilities would crash,
  not silently vary.
- **LOG #281–#284 vs code:** narrative matches the code and .out,
  including the two pre-round self-repairs (G7 identity-gate, G4c vacuous
  in-family sweep) and the A5' story (battery line 3 is the branch that
  would have caught A5's 1/2). Overstatements: "forks 48" unqualified
  (F5) and the receipt-vs-pin gap of F1/F2 — #284's "runs 15/15 against
  the pin + A1-A5'" is exactly what this review disputes.

---

## WHAT SURVIVES (verified)

Enumerator-independent — survive unconditionally:
- Depth-2 conflict census = 4 (hand: the 4 ordered lists of {pA0,pB1},
  {pA1,pB0}); identical in the pin-faithful family.
- mu(seed pair) = 1/64 = (1/4 · 1/2)² — hand-derived from the pinned law;
  my independent mu agrees.
- The kernel block, all exact: K1({P,R}) = 2/3, K1({Q}) = 1/3,
  K2 = 1/2, 1/2, TV = 1/6 — matching paper 25 §10.2–10.3; batch weights
  mu_K1 = 1/512 · 1/4 · 2/3 = 1/3072, mu_K2 = 1/512 · 1/4 · 1/2 = 1/4096.
  The generated seed component is one 3-member path with edges A–B, B–C
  only.
- The 7-branch G7 battery, every value re-derived by hand AND by my
  independent admissibility: 1/8, 3/4, 3/4 (A5'), 3/4, 1/8 (= 1/4 × edge
  law 1/2), 1/8, 3/4. Kernel normalization Σ_w P_K(w|C) = 1 both kernels
  (my rebuild: all 10,832 components).
- G4a's causal-vs-authentication split: causal rejects, issuance-only
  admits — reproduced with fully independent code.
- L1 — now with an all-depths proof (F7), 0 duplicates in both families.
- A5' (3/4) and the unreachability of the 1/2 and 1 idle branches at
  fixture depths.
- Seed-independence, exit-1 plumbing, banner-cap honesty.

Verified as properties of the RECEIPT'S ENUMERATOR'S family (clean-room
rebuild reproduces every one exactly; their attachment to "the pinned
grammar" is F1's dispute): ARM-1 = 5,751; ARM-2 = 5,761; L1 denominator
11,512; conflict histories 2,596; forks (ARM-2) 48; observer violations 0;
orphans (ARM-2) 1,128; joins 2,808; components 10,832; G1 761 histories /
2,421 resequencings (760 distinct, F8); G4c 48 forked / 432 extension
candidates / 0 violations; G3i sweep 0/5,751; G3ii 0 on ARM-1 (and, my
run, 0 on ARM-2).

## PRESCRIBED REPAIRS

- **R1 (F1, the blocker).** Make the candidate universe identical to the
  admission relation. Recommended arm (A): complete `candidates_for` to
  past-local generation (arb candidates from every subset of full-live
  proposals per base; the past-relative component match in `admissible`
  already rejects non-components), matching §2 + A5(ii) and restoring
  linear-extension closure of the family. Pre-verified with my pin-faithful
  enumerator: ARM-1 6,471 / ARM-2 6,589; ARM-2 forks 72; ARM-1 forks 424;
  orphans 2,088/1,960; joins 3,096; L1 0; observer fork-freeness 0;
  depth-2 census, mu seed, kernel block, battery, and the G3i pair-iff all
  unchanged/passing; witness-2 closure healed. The per-initiator 5/4
  exhibit must then be DECLARED (the placement problem's support-level
  face — it is real under the pinned law and currently masked). The
  alternative arm (B) — pin the global-record filter as a batch-close law
  — requires re-wording §2/A5(ii), the docstring, and the SUPPLIED/
  GENERATED split (the opportunity set becomes a global-record,
  gauge-dependent object; witness 2 then contradicts pinned G1's
  bookkeeping principle), and weakens the headline exactly where the D42
  parent pin demands covariance. I recommend A. Either way the .out
  verdict line and family-size line must be recomputed/re-worded.
- **R2 (F2).** Amend the pin (A6): arb carriers = C's proposers + the new
  version; the base enters as event DATA (the ckey triples), not as a
  carrier wire. Pre-verified: base-as-carrier yields ARM-2 forks = 0
  (G4c would fail); the receipt already implements the A6 reading, and
  every surviving number above is under it.
- **R3 (F3).** Post-R1, add the enabled-set gate the pin already
  prescribes: family closure under linear extensions (or, equivalently,
  candidate-set invariance at gauge-equivalent record points). Under R1-A
  this follows from past-locality of admission and passes at the witness
  point (verified); alternatively re-pin G1's text to what is gated.
- **R4 (F4).** Extend G3ii's loop to ARM-1 + ARM-2 (pre-verified:
  0 violations on ARM-2) or scope the label.
- **R5 (F5).** Census forks/orphans in ARM-1 too, and qualify the printed
  lines per arm. Pre-verified values (receipt semantics): ARM-1 forks 288,
  ARM-1 orphans 1,376, ARM-1 observer violations 0. Recompute post-R1.
- **R6 (F6).** Add the proposer/base/component separations to G8 —
  pre-verified: all three separate `canon`.
- **R7 (F7).** Record the L1 proof (given verbatim in F7) in the pin or
  the receipt header; keep the census as a regression tripwire; delete
  "asserted globally by the census."
- **R8 (F8).** Dedup `g1_set` or print "761 checks (SIG1 twice; 760
  distinct)".

## Reproduction inventory

- Reruns: `PYTHONHASHSEED={0,1,42,31337} python3
  v10/code/d42a_generated_conflict_exact.py` → byte-identical to
  `v10/data/d42a_generated_conflict_exact.out`, exit 0.
- Witnesses 1–3 + the 1,016-point sweep: scratchpad
  `d42a_counterexample.py` (drives the receipt's own defs).
- Clean-room rebuild + pin-faithful family + base-carrier variant:
  scratchpad `d42a_independent_verify.py` (all PART A lines reproduce the
  receipt's numbers; PART B/C give the F1/F2 deltas), `addendum2.py`
  (G4a independent, pin-family orphans/joins, witness-2 closure).
- Mutations: `mutant_plumbing.py` (G2a expectation 4→5 → 14/1, exit 1);
  `mutant_enum.py` (drop multi-member arb candidates → G3i and G6 FAIL,
  exit 1, G3i domain shrinks to 4,071 — the family is enumerator-relative).
