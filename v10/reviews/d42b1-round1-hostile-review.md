# D42b1 round 1 — hostile review (pin + receipt + out)

**Reviewer round:** 2026-07-18, against HEAD 1624c4c. Objects: the pin
`v10/note-d42b1-transport-and-reconciliation.md` (P1–P5, §§2–5), the receipt
`v10/code/d42b1_transport_exact.py`, the output
`v10/data/d42b1_transport_exact.out`, read against the settled d42a grammar
(`note-d42a` + A1–A8/A7', #289), the d42a round-1 review + delta (its gate
standards govern this round), and LOG #290–#291. Method: 4 reruns under
varied `PYTHONHASHSEED` (0, 1, 42, 31337); a clean-room re-implementation of
the ENTIRE grammar from the pin texts (own wire/past construction, own
holdings/supersession/components/MIS/K1, own admission, own wider-universe
generator, own BFS — not the receipt's loops) cross-compared per history
against the receipt; a targeted hostile-probe omission sweep; four
constructed counterexample/verification chains driven through BOTH engines;
the d42a-delta-standard mechanical ladder sweep; four mutation runs.
Scripts in the session scratchpad (`indep.py`, `indep_lib.py`, `witness.py`,
`witness2.py`, `mutant1/2/3.py`, `mutant_regs.py`); nothing in the repo was
modified except this file.

## VERDICT: 1 BLOCKER / 2 MAJOR / 2 minor / 2 nit

Every printed number reproduces exactly in the clean-room rebuild — the
enumerator/admission split that convicted d42a round 1 is HEALED at the
generator level (candidate-set equality at all 7,393 histories over a
strictly wider universe; 0 omissions, 0 spurious, 0 engine disagreements).
The BLOCKER is the same conviction class one layer up: the PRICING now
contains two inequivalent notions of the arb-and-merge opportunity —
`admissible()` (the A7 admission relation) versus the own-view availability
bit and merge denominator inside the weight law — and they disagree on
admissible records five events deep. At such points the receipt's own
per-actor sums leave the pinned 1+k/4 ladder DOWNWARD (3/4 at depth 5, 7/8
at depth 11), so the P5 headline "the 1+k/4 ladder survives" is a theorem of
the CAPPED CENSUS only, refuted by constructed chains of exactly the kind
the receipt itself uses to carry P2/P3/P4. Under the pin-faithful
(admission-based) pricing both witnesses re-price to exactly 1 — the repair
is minimal, in-family invisible, and pre-verified.

---

## F1 — BLOCKER (CONFIRMED): the weight law's availability/denominator layer
## is not the admission relation; the 1+k/4 ladder (P5) dies off-cap under
## the receipt's own pricing

**Witness 1 (depth 5, three actors — every event admissible per the
receipt's own `admissible()`, equal q in my engine):**

```
h5 = [('p','A',v0,0), ('p','B',v0,1), ('d','B','C',v0), ('d','C','A',v0),
      ('r','B',{tB},{tB})]          # B's blind self-seal, relayed knowledge
per-actor candidate sums (receipt's candidates_for): A = 3/4, B = 1, C = 1
receipt's own on_ladder(3/4) = False
```

A's own view (chain past through the C-relay) holds the LIVE pair component
{tA, tB} — `arb_components_in_view(own_view, A)` is nonempty, so the idle
docks the arb-and-merge 1/4 — yet **zero admissible arb or merge events
exist for A**: the singleton ckey {tA} fails the component match (A sees the
pair), and the pair ckey {tA,tB} joins B's wire, sees B's blind self-seal,
and fails (tB resolved). Probed directly: both `(False, None)`. The pinned
budget's "idle absorbs every unavailable total" is violated by the
receipt's own arithmetic: the sector is unavailable (no enabled event) and
its 1/4 is destroyed, not absorbed. Note the physics: this is exactly P2's
starvation/relay structure — the phenomenon the round celebrates is the
phenomenon that breaks the receipt's pricing.

**Witness 2 (depth 11 — the merge-denominator side; every event admissible,
both engines, equal q):**

```
h11 = SIG-FM[:6] + [('p','B',v1,0), ('p','A',v1,1), ('d','A','C',v1),
      ('d','C','B',vC), ('r','A',{tAv1},{tAv1})]   # blind foreign seal + relay
per-actor sums: A = 1, B = 7/8, C = 1     (7/8 is OFF the quarter ladder)
B sector totals: p = 1/4, d = 1/4, m = 1/8, idle = 1/4
```

B's own view holds one live component ({tBv1, tAv1}) AND one enabled merge
pair (v1, vC), so the merge prices at D_own = 2 → 1/16 per winner; but the
component's arb half is dead in join view (A's blind self-seal of its v1
fork, invisible to B, resolves tAv1 and supersedes v1 there — both arb
probes `False`). The arb-and-merge sector is genuinely AVAILABLE (the merge
is admissible) yet totals 1/8 ≠ 1/4. No idle-side reading rescues this one:
the sector's 1/4 is split against an opportunity that does not exist.
(For the record: the variant where A pair-arbs B's proposal SELF-HEALS —
the arb rides B's wire and supersedes v1 in B's view, sums all 1. The
counterexample requires the blind-seal + third-party-relay route; verified
printed in `witness.py` W2.)

**Where the pin stands.** Pin §2 prices the sector "over enabled conflict
components (join view, A4) PLUS enabled merge pairs (initiator view)", and
A7 (retained) defines the opportunity set as "the past-local admission
relation ... and NOTHING ELSE. Any enumeration must be a superset generator
filtered by admission." The receipt's generator obeys A7; its `has_am`
availability bit and its merge denominator do NOT — they count OWN-VIEW
components never filtered by admission. Under the pin-faithful reading
(sector availability = an admissible arb exists or an enabled pair exists;
merge D = #distinct admissible arb ckeys + #enabled pairs; arb events
unchanged — their own past IS the A4 join view), I re-priced both
witnesses: **all sums = 1**, and the change is invisible in-family
(0 deviations at 500 sampled history×actor points; the blind 5/4–7/4
spectra arise from the arb events' per-event join denominators, untouched).
Pre-verified in `witness2.py` X1.

**Why the census could not see it.** In-family the two notions coincide —
my mechanical sweep at all 18,210 actor-points (d42a delta standard):
propose sector ≡ 1/4·[open], deliver ≡ 1/4·[open], every admissible-ckey
group ≡ 1/4, own-view-open ⟺ m ≥ 1, sum ≡ 1+(m−1)/4 — **0 violations**.
The divergence needs an actor to SEE a live conflict whose resolution rides
a wire it has not joined: with 2 actors impossible (any delivery joins both
chains); with 3 actors it needs 5 events — outside the receipt's tuned caps
(4/3) AND outside the pin's §3 caps (5/4, since the witness lives on the
3-actor arm). So the cap tuning did not hide it; no enumeration at either
cap could reach it. But the receipt's OWN standard (RF1/RF5: constructed
admission-exact chains carry the deep physics — the entire warrant for
P2/P3/P4) is precisely the standard under which h5/h11 refute P5's ladder
half. G9's label ("the 1+k/4 ladder survives the extension (P5)"), the
.out verdict line ("L1 and the ladder stable"), pin §1 P5, and LOG #291
("the 1+k/4 ladder holds ... deliver/merge sectors never blind") are all
unscoped — headline wider than computation, and false as law under the
receipt's implemented pricing.

**Classification:** not wrong-computation (every number reproduces); a
hidden-inequivalent-relation defect (the standing conviction class, now in
the pricing layer after d42a evicted it from the generator layer) plus
claim-wider-than-computation on P5/G9. Repair R1 below, pre-verified.

## F2 — MAJOR (CONFIRMED): the battery omits two branches the pin
## explicitly lists; pin §2's "the battery gates these exactly" is false

Pin §2: "Baseline idle at genesis is therefore 1/2 ... and **1/4 when all
three sectors are open — the battery gates these exactly**." Pin §4 G7:
"genesis idle 1/2; **all-open idle 1/4**; ... **merge q with and without
value conflict**". The receipt's battery (10 lines, all values correct —
each re-derived by hand and by my independent admission):

- The **all-open idle 1/4 line is absent** — and the branch is REACHABLE at
  the receipt's own signature chain: `('n','B')` at SIG-FM[:6] (props open
  on v1/vC, the merge pair open, deliver open). Both engines: exactly
  **1/4**. Nothing in the receipt ever evaluates an idle ≠ 1/2.
- The **equal-values merge branch is absent**: only the conflicted pair
  (1/2 click) is gated. The 'both' single-option branch verified admissible
  at exactly **1/4** on the third-fork chain (F3/W4 below), both engines.

LOG #291's battery description "(genesis idle 1/2, **all-open lines**,
merge/delivery/rescue qs)" misdescribes the battery. Repair R2,
pre-verified values above.

## F3 — MAJOR (CONFIRMED): pinned censuses and ports not discharged — the
## receipt is narrower than the pin at 8+ points, none declared

The merge machinery is enumeration-VACUOUS at these caps — my rebuild:
**0 merge events in all 7,393 histories and 0 enabled merge pairs at every
actor-point** (nobody ever holds two forks in-family; corollary verified:
delivery-free ⟹ co-participated creations are wire-comparable ⟹ no pair —
reconciliation demand REQUIRES transport). So every merge-sector claim
rides constructed chains alone; RF1 declares that for P2/P3/P4, but the
following pinned obligations are simply not in the receipt:

1. **§2 chained reconciliation — "Declared, censused":** no census, no
   fixture. Pre-verified for the repair (`witness.py` W4): the 9-event
   third-fork chain (3 blind seals, 2 deliveries, merge, late delivery) is
   admissible end-to-end in both engines; post-merge `merge_pairs(B)` is
   exactly {(vC0, v_m)}; the equal-values branch gives the single 'both'
   option at 1/4, the conflicted branch two clicks at 1/8 — the pin's
   recursion clause works as stated.
2. **RF2 double-merge — "censused, declared":** no census. Pre-verified
   (W5): both merges of the SAME pk by different holders admissible,
   incomparable, distinct records, canon-separated. Sharper: mutant
   `mutant_regs.py` (X4) restores the receipt's DEAD first `regs_of`
   (carrier `('v','m',pk)` without initiator) — the double-merge chain
   becomes INADMISSIBLE (shared wire chains the merges), i.e. RF2's fork
   species dies — **and the mutated receipt still passes 14/14**. The merge
   carrier choice is protected by zero gates.
3. **G3 "pair-arb (ported)":** no pair-arb iff-sweep anywhere.
4. **G3 RESCUE iff:** gated as a 2-point before/after exhibit on SIG-KR,
   not the pinned iff-sweep — although SIG-KR is IN-FAMILY (verified), so a
   family sweep domain existed.
5. **G4 "staleness ported":** the d42a causal-vs-authentication-only
   exhibit and the orphan censuses are absent.
6. **P2's pinned in-family census** ("the in-family census of such pasts
   (> 0 where depth allows...)"): the full-family two-arb census is never
   computed or printed. My rebuild: **0** at these caps (depth does not
   allow — a two-arb past needs 5 events), so nothing false is hidden; the
   census line is simply missing.
7. **P4 "Gates: both exact, on constructed chains + family sweeps":** no
   family sweep.
8. **G9's pinned decomposition** ("k from blind arb layers ONLY"): the gate
   checks quarter-grid membership of the sums and nothing else; it cannot
   attribute k to arb blindness (a deliver-sector mispricing that landed on
   the grid would pass). My W6 sweep supplies the pinned decomposition
   in-family (0 violations, 18,210 points) — true but ungated.

Individually items 3–7 are minor; the pattern — an unqualified GREEN
"14/14" over a receipt that discharges materially less than the pin's gate
list, with two "censused" claims in the pin text pointing at censuses that
do not exist — is the d42a "headline wider than computation" class at the
document level. Repair R3, largely pre-verified.

## F4 — minor (CONFIRMED): P3's iff loop never evaluates the full 8-event
## history

`for k in range(len(SIG_FM))` sweeps prefixes [:0]..[:7]; the full record
(post-rescue) is never option-swept. Verified both engines: merge options
at SIG-FM[:8] = **0** (pairs superseded by the merge; the re-proposal
creates nothing) — the gap is benign in value, but the "prefix-exact iff"
label reads as full-chain coverage. G1/G1b do include the full prefix in
their invariance domain (`range(4, len+1)`), so only the OPTION-SET iff has
the hole. One-line repair, pre-verified. (P2/P3/P4 scope honesty is
otherwise clean: printed sentences attribute the deep facts to SIG-FM /
SIG-KR by name, the delivery-free zero is labeled in-family, and RF1
declares that enumeration cannot reach the signature chain.)

## F5 — minor (CONFIRMED): near-cannot-fail gates in the G6/G8 slots

- G6's assertion is `join_arbs + join_dels > 0` — trivially true in any
  family containing one delivery; the censused VALUES (384 / 8,250, both
  anchored by my rebuild) are the content, the gate is a printer.
- G8's three "separations" are event-tuple-embedding truisms (canon embeds
  the typed op; distinct ops can never share a canon), as in d42a F6 —
  there the delta accepted them with an explicit honesty declaration; here
  no such declaration is printed.
- Against the conviction-class checklist, the OTHER gates are genuinely
  falsifiable: M1 (wrong expectation) → 13/1 exit 1; M2 (holdings leak:
  participation filter dropped) → P1 fires with 800 violations (plus
  P3/G5 collapse) exit 1; M3 (supersession blockers dropped) → P2's
  delivery-free sweep fires (violations = 4: re-arb chains on one wire)
  exit 1. So P1's sweep and P2's zero-side are NOT vacuous — though note
  their in-family power at these caps is limited to supersession/holdings
  discipline (structural two-arb pasts need depth 5 regardless).

## F6 — nit (CONFIRMED): duplicated `regs_of`; the dead twin is a wrong law

Lines 71–79 define `regs_of` with merge carrier
`mname(op[2],None,op[1])[:2] + (op[2],)` = `('v','m',pk)` — no initiator —
then lines 81–89 redefine it (shadowing) with `('mw', a, pk)`. The dead
first version is not just clutter: it is the carrier law under which RF2's
double-merge fork species is grammatically impossible (X4), and since no
gate covers that physics (F3.2), deleting the WRONG def is
indistinguishable from deleting the right one at 14/14. Delete lines 71–79;
land the RF2 census so the choice is gated.

## F7 — nit: latent mixed-type sort fragilities (no in-family hazard)

The two version-tuple shapes (arb `('v', base, vals, authors, init)` vs
merge `('v','m',pk,val,init)`) never meet a raw comparison: every sort over
version objects or option pairs uses `key=repr` (receipt lines 191–196,
241, 252, 318, 330, 344, 347, 434 — audited). `sorted(ckey)` at lines
204/215 is raw but safe (ckeys are single-base by construction; comparison
resolves at the payload before reaching the base slot) — same
crash-not-corrupt class as d42a F9. `next(iter(op[2]))[1]` base extraction
relies on single-base ckeys — guaranteed by the component construction.
Byte-identical output across 4 hash seeds confirms no ordering leak.

---

## ASSIGNED SOFT SPOTS — disposition

- **(a) the prior blocker's ghost (candidates_for vs admissible):** CLEAN
  at the generator level, convicted at the pricing level (F1). Evidence for
  the clean half: my independent enumerator probes a strictly wider
  universe per history (proposals on every version held or not; arb ckeys
  over ALL proposal subsets, live or RESOLVED; every winner subset, MIS or
  not; merges over every version pair incl. non-held, superseded,
  cross-lineage, wrong-w; deliveries of unheld versions) and its
  per-history admissible (event, weight) sets EQUAL the receipt's at all
  7,393 histories; families equal as sets. Targeted second sweep with
  self-deliveries and an alien receiver 'Z' over 314 histories (all SIG-FM
  and SIG-KR prefixes, the counterexample chains, 300 family histories):
  9,168 probes — 0 admissible-but-omitted, 0 generated-but-inadmissible,
  0 my-engine/receipt disagreements. The specific worries: full-view
  holdings = own-view holdings (holdings-bearing events all ride the
  holder's wire — theorem, and probed); full-live arb generation loses
  nothing (a resolver carries the proposer's wire — the A8 carrier
  argument survives delivery unchanged, since deliveries alter no arb
  carriers); merges over full holdings are complete for the same reason.
- **(b) the three view rules:** `own_view` IS the sender's chain-past
  (regs {a} idle appended; verified structurally and by set-equality).
  Deliver is never blind and never double-priced: sender-view = event-view
  for the option set (wire-locality), and the sector prices exactly
  1/4·[open] at all 18,210 actor-points. Merge events price in the
  initiator view (single-wire, matches pin). The generalized ladder law
  verified mechanically in-family (W6, 0 violations across all four
  clauses); its OFF-cap failure is F1 — and it is an arb-sector
  availability/denominator failure, not a deliver/merge blindness (the
  pin's "blindness still comes from join-view arb layers only" is true;
  what the pin missed is that the same knowledge-asymmetry now UNDERPAYS).
- **(c) P2's gate:** obs_two = 3 verified by hand and mechanically — the
  events holding both arbs are dC (the second delivery), mB, and the
  rescue re-proposal; keyed per-base correctly. The delivery-free sweep is
  capable of failing (M3). No printed sentence claims in-family
  observation of the constructed structure (RF1 declared). Missing census
  line: F3.6.
- **(d) P3's iff:** option sets verified independently at every k
  (including both engines' agreement on the 2-option window at exactly
  k = 6 and emptiness at k = 7); k = 8 untested by the receipt (F4,
  benign); m_after is exactly the PK pair with winners {v1, vC} (W9), so
  G10's "exactly the pair merges" is discharged. Chained third-fork
  reconciliation: NOT censused (F3.1), works when probed (W4).
- **(e) P4:** the kill's sole blocker IS supersession-in-past — code-path
  isolated (tB stays unresolved; the live {tB} component exists and is
  base-filtered) and controlled: a knowledge-free delivery (C→B of v0,
  empty C chain) leaves B's blind self-seal admissible at 1/4 (X2) —
  delivery per se does not kill; the carried supersession does. Rescue
  arithmetic verified: v0 superseded (excluded), v1 fresh → 2 options →
  q = 1/8 exactly; enabled exactly at the delivery (False→True across dA).
  SIG-KR is in-family (the pinned family sweep was feasible — F3.7).
- **(f) P1:** the sweep covers every delivery-free history of both arms
  (1,915 of 7,393; ARM-2 actor scoping is safe — C-less histories give C
  only v0, which the loop skips). The merge branch of the participation
  predicate ({initiator} only) matches the pin's single-participant
  carrier — and is dead code in the sweep's domain (delivery-free ⟹ no
  merges, the mini-theorem above). Mutation M2 proves a holdings leak is
  caught (800 violations). The theorem side is sound: holdings clauses are
  participation-or-delivery only, in both the receipt's code and mine.
- **(g) L1/A8 under delivery — PROVED at all depths:** any resolver of
  ('p',a,b,·) is an arb whose ckey contains the triple, so its carriers
  include a's wire (A6 semantics unchanged by this pin: deliveries alter
  no arb carriers); hence every resolution of a's proposal is VISIBLE on
  a's own wire. A later ('p',a,b,·): prior live in a's view → A3 blocks;
  prior resolved → the resolving arb superseded b in a's view → blocked.
  Delivery adds holdings and knowledge only; resolution/supersession are
  monotone along a's chain; merge-supersession only adds blockers. The
  feared route — resolution by an arb NOT on a's wire — is structurally
  impossible (resolution is DEFINED by ckey membership; carriers derive
  from the ckey). Empirical: triple-level 0/7,393 (receipt + mine),
  PAIR-level 0 (my stronger census, X3), 0 on all constructed chains.
  P5's L1 half STANDS.
- **(h) battery:** all 10 shipped values re-derived by hand and by my
  independent admission (exact); the genesis-idle-1/2 and
  post-proposal-idle-1/2 derivations confirmed (deliver sector open at
  every point with ≥ 2 actors since v0 is always deliverable — which is
  also why no idle in this grammar is ever 3/4 in-family). The pinned
  all-open 1/4 branch is REACHABLE and untested (F2); the pinned
  equal-values merge branch untested (F2).
- **(i) depth-cap honesty:** banner declares the tuned caps (4/3 vs pin
  §3's 5/4) — RF3 licenses exactly this; no label claims deeper
  enumeration; G0 printed MEASURED with "round to anchor" — **anchored by
  this round** (independent enumerator: 3,969 / 3,424 exact, including the
  empty history per the receipt's family convention). Verified: the F1
  witnesses are unreachable at the PIN's caps too, so the tuning hid
  nothing.

## PLUMBING, SEEDS, DETERMINISM, LOG

- **Exit-1 by design:** CONFIRMED (M1: one wrong expectation → "13 PASS /
  1 FAIL", exit 1).
- **Seed-independence:** CONFIRMED — PYTHONHASHSEED ∈ {0, 1, 42, 31337}
  all byte-identical to the committed .out, exit 0, ~10.5 s each
  (consistent with LOG #291's 0/41 claim).
- **Determinism:** audited (F7) — all mixed-shape sorts repr-keyed; family
  and census values order-independent; the two version-tuple shapes never
  hit a raw comparison in-family.
- **LOG #290–#291 vs code:** #290 matches the pin. #291 overstates twice:
  "G7 battery 10/10 (genesis idle 1/2, **all-open lines**, ...)" — no
  all-open line exists (F2); "P5 ... the 1+k/4 ladder holds ...
  deliver/merge sectors never blind" — unscoped (F1). The rest (families,
  spectra, censuses, P1–P4 wording, seed count, runtime) matches.

## WHAT SURVIVES (all verified independently)

Anchored by clean-room rebuild (my own enumerator; candidate-set equality
at every history):
- Families ARM-1T = **3,969**, ARM-2T = **3,424** (MEASURED → now
  ANCHORED); L1 tripwire **0/7,393** (and pair-level 0, stronger);
  ladder spectra ARM-1T {1: 7,514, 5/4: 424}, ARM-2T {1: 9,588, 5/4: 576,
  3/2: 72, 7/4: 36} — plus the full mechanical decomposition at all
  18,210 actor-points (sector exactness, ckey groups = 1/4, own-open ⟺
  m ≥ 1, sum = 1+(m−1)/4) — the receipt's numbers are right and in-family
  the strong law holds;
- joins: arb **384** / delivery **8,250**; G1 slice **3,638** distinct /
  **7,509** resequencings (my own extension counter); depth-2 conflict
  census **4**; mu(seed) **1/64**; star kernel **{B,C} 2/3 vs {A} 1/3**
  (hand: 4/6 vs 2/6 over 3! orders); merge clicks **1/8 + 1/8** at
  SIG-FM[:6], pk exactly PK; delivery-free two-arb pasts **0** (and
  full-family **0**, my census); P1 sweep **0** over 1,915 delivery-free
  histories.
- SIG-FM admissible end-to-end (8/8, equal q both engines); obs_two = 3
  (dC, mB, rescue); SIG-KR admissible, IN-FAMILY, kill True→False with
  supersession isolated as sole blocker (control chain X2), rescue
  False→True at exactly q = 1/8.
- P1 as a THEOREM (holdings = participation-or-delivery, both codebases);
  P5's L1 half as a theorem at all depths (proof in (g) above); the
  delivery-free ⟹ no-merge-pairs corollary (transport is necessary for
  reconciliation demand — a clean strengthening of the round's physics).
- P2's headline PHYSICS: the two-arb observer past is real, admissible,
  and delivery-only — the d42a G4c theorem is indeed the starved special
  case. P3's window (absent → 2 options → gone) exact at k ≤ 7. P4's
  one-delivery kill+rescue exact. The battery's 10 shipped values.
- Chained third-fork reconciliation and RF2 double-merge WORK as pinned
  (my constructed chains, both engines) — unverified by the receipt but
  true, so F3's repairs are confirmatory, not corrective.
- Generator completeness (A7 discipline) on the wider universe; exit-1
  plumbing; seed-independence; banner-cap honesty.

NOT surviving as stated: P5's ladder half as a law of the extended grammar
under the receipt's implemented pricing (F1 — counterexamples 3/4 and 7/8);
"the battery gates these exactly" (F2); the pin's two "censused" claims and
the ported-gate list (F3).

## PRESCRIBED REPAIRS

- **R1 (F1, the blocker).** Make the pricing layer's opportunity notions
  THE ADMISSION RELATION, as A7 already commands for enumeration:
  (i) idle docks the arb-and-merge 1/4 iff an admissible arb event OR an
  enabled merge pair exists for the initiator; (ii) the merge denominator
  becomes D = #distinct admissible arb ckeys + #enabled pairs; (iii) arb
  events unchanged (their own past is the A4 join view). PRE-VERIFIED
  (`witness2.py` X1): h5 → sums (1, 1, 1); h11 → (1, 1, 1); in-family
  invisible (0/500 sampled deviations; spectra, battery, censuses
  unchanged). Declare the joint-record dependence of the repaired idle as
  the d34b placement face (A4 precedent — the availability bit, like the
  component, first exists at the join). Add h5 and h11 as constructed
  regression gates (sum = 1 exactly), re-word G9/P5/verdict to "ladder
  verified in-family at caps + witnesses healed"; a general-depth ladder
  theorem remains OPEN for d42b3 and must be labeled so. The alternative
  arm — re-pin own-view pricing as law — forfeits the ladder (sums 3/4,
  7/8 become grammar facts) and P5's headline with it; not recommended.
- **R2 (F2).** Add the two battery lines: `('n','B')` at SIG-FM[:6]
  (all-open idle) = **1/4**, and an equal-values 'both' merge = **1/4**
  (third-fork chain, or any equal-payload pair fixture). Both values
  pre-verified in both engines. Fix the LOG wording at next entry.
- **R3 (F3).** Discharge the pinned censuses/ports: chained-reconciliation
  census (my 9-event chain: pairs = {(vC0, v_m)}, 'both' 1/4 / conflicted
  1/8 — pre-verified); RF2 double-merge census (pre-verified admissible,
  incomparable, distinct, canon-separated) — this also gates the merge
  carrier against the F6 fossil (X4 shows 14/14 cannot currently tell
  them apart); pair-arb iff port; rescue iff family sweep (domain exists —
  SIG-KR is in-family); staleness/auth-only port + orphan censuses; print
  the P2 full-family census (**0** at caps, pre-verified) with the depth
  note; add the P4 family sweep; print the merge-sector vacuity (0 merge
  events, 0 enabled pairs in-family) in the banner; upgrade G9 to the
  mechanical decomposition gate (my W6 loop is a drop-in; 0 violations
  today).
- **R4 (F4).** Extend the P3 loop to k ≤ 8 (pre-verified: 0 options at
  the full history).
- **R5 (F6).** Delete dead `regs_of` (lines 71–79).
- **R6 (F7).** Optional: `key=repr` on the two raw `sorted(ckey)` sites or
  a single-base comment; defensive only.

## Reproduction inventory

- Reruns: `PYTHONHASHSEED={0,1,42,31337} python3
  v10/code/d42b1_transport_exact.py` → byte-identical to
  `v10/data/d42b1_transport_exact.out`, exit 0 (~10.5 s).
- Clean-room rebuild + candidate-set equality + all censuses/spectra +
  battery + G1 recount + all-open-idle gap: scratchpad `indep.py`
  (library form `indep_lib.py`) — all lines [OK].
- Witnesses: `witness.py` — W1 h5 (sums 3/4/1/1, probes, on_ladder False),
  W2 h11 (7/8; self-healing pair-arb variant recorded), W3 P3 k=8, W4
  chained reconciliation (both value branches), W5 double-merge, W6 the
  18,210-point mechanical ladder sweep (0 violations), W7 the 9,168-probe
  hostile omission sweep (0/0/0), W8 duplicate check, W9 P3 exactness.
- `witness2.py` — X1 minimal-repair re-pricing (h5/h11 → all 1; 0/500
  in-family deviations), X2 P4 sole-blocker control, X3 pair-level L1,
  X4 dead-regs_of hazard (mutated receipt passes 14/14; double-merge dies).
- Mutations: `mutant1.py` (expectation 4→5 → 13/1, exit 1), `mutant2.py`
  (holdings leak → P1 800 violations + P3/G5, exit 1), `mutant3.py`
  (supersession blockers dropped → P2 violations 4 + P4 + G7, exit 1),
  `mutant_regs.py` (F6/X4).
