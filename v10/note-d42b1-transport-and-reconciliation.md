# D42b1 — the transport-and-reconciliation grammar (fronts 1–3)

**Status:** CAMPAIGN PIN (strict; the receipt runs only against this
text), 2026-07-18. Parent: note-d42a TERMINAL at #289 (the settled
past-local grammar + the declared 1+k/4 support face). This pin
executes d42b fronts 1 (delivery events), 2 (merge/reconciliation),
3 (orphan starvation) as ONE extension — they are one physics: forks
and orphans are information-starvation phenomena, and delivery is the
information channel. Receipt: `v10/code/d42b1_transport_exact.py`.

## 1. Pinned predictions (stated BEFORE the receipt)

- **P1 (starvation theorem).** In the delivery-free sub-grammar (=
  d42a), a non-participant of an arb NEVER holds its created version —
  provable from A1/A6 carriers (holdings propagate only through
  participation). Gate: in-family sweep 0 exceptions + the proof cited.
- **P2 (fork-freeness is an artifact — the load-bearing prediction).**
  With delivery, per-observer-past fork-freeness DIES: an observer
  receiving deliveries from two incomparable fork branches holds BOTH
  same-base arbs in its past. The A2/G4c theorem of d42a is a theorem
  OF THE STARVED SUB-GRAMMAR only. Gate: an exact admission-checked
  chain exhibiting the two-arb observer past, and the in-family census
  of such pasts (> 0 where depth allows; the delivery-free sub-family
  stays at 0).
- **P3 (reconciliation is generated).** Exactly at a two-fork observer
  past, the MERGE opportunity is enabled — the record generates its own
  reconciliation demand, continuing d42a's opportunity-generation
  claim. Gate: iff-sweep (merge enabled ⟺ two same-base unsuperseded
  incomparable versions held).
- **P4 (orphans are informational).** Delivery resolves orphan
  starvation both ways: delivering the supersession KILLS the orphan
  (unarbitrable in the enlarged past — knowledge is fatal), and
  delivering the successor version RESCUES the proposer (the
  re-proposal opportunity on v' is enabled exactly at the delivery
  record). Gates: both exact, on constructed chains + family sweeps.
- **P5 (stability).** L1 (live-triple uniqueness) survives verbatim —
  the A8 proof only needs: a same-base prior is either live (A3
  blocks) or resolved by an arb riding the proposer's own wire
  (supersession blocks); delivery only ADDS knowledge, and blocking is
  monotone in knowledge. The 1+k/4 ladder FORM survives (the deliver
  sector is initiator-view priced, hence never blind; blindness still
  comes from join-view arb layers only). Gates: census + ladder check.

## 2. The grammar extension [POSITED; d42a §2 + A1-A8 retained]

New events (typed; initiator in the type):

- `('d', s, r, v)` — delivery: sender s transmits version v to
  receiver r. **Carriers {s, r}** (the one two-wire event class beside
  arbs — a delivery IS a join of knowledge). Admission: s holds v in
  past(e); r != s. Re-delivery is ADMISSIBLE and physical (it still
  joins the wires — knowledge transmission is the point; holdings are
  idempotent); censused. After delivery, r holds v (holdings rule
  extended: r holds every v delivered TO r in its past), and r's past
  contains s's chain up to the delivery — supersessions travel with
  the join, not as payload.
- `('m', a, pkey, w)` — merge: a locally reconciles two versions
  v1, v2 it holds. pkey = the sorted pair (v1, v2). **Carriers
  {a, v_m}** — merge is a SINGLE-participant event (the holder of both
  reconciles; the git analogy is exact). Admission: both v1, v2 held
  by a in past(e); both created by arbs (or merges) ON THE SAME BASE
  b; their creating events INCOMPARABLE in past(e); neither v1 nor v2
  superseded in past(e). If value(v1) != value(v2): w in {v1, v2}, a
  RECORDED kernel click at uniform 1/2 (the pair kernel; K1 = K2 on a
  pair). If values equal: w = the canonical co-authored union, single
  option. Creates v_m = ('v', 'm', pkey, value(w), a); v_m supersedes
  BOTH v1 and v2 (merge-supersession is pair-scoped: it closes pkey's
  members, not other forks of b).

**Budgets (#152, extended):** propose-total 1/4 (initiator view, as
d42a); **arb-and-merge total 1/4** split equally over enabled conflict
components (join view, A4) PLUS enabled merge pairs (initiator view —
a holds both, so merges are never blind); **deliver-total 1/4** split
equally over enabled (r, v) pairs in the SENDER'S view (all held
versions x other participants; never blind); idle absorbs every
unavailable total. Baseline idle at genesis is therefore **1/2**
(propose + deliver open, arb closed), and 1/4 when all three sectors
are open — the battery gates these exactly.

**Supersession with merges:** a base b superseded by an arb stays
superseded; a version superseded by a merge is closed for proposals
and further merges; UNMERGED third forks of b remain mergeable with
v_m (chained reconciliation) — v_m's creating event is comparable
with its pkey ancestors but may be incomparable with a third fork's
arb, so the merge admission recurses naturally. Declared, censused;
full multi-fork confluence is NOT claimed (a d42b2+ question if the
census shows structure).

## 3. Fixtures

**ARM-1T (two actors, depth <= 5):** delivery + rescue minimal chains.
**ARM-2T (three actors, depth <= 4):** fork genesis under delivery.
**SIG-FM (the fork-merge signature chain, constructed, ~8 events):**
pA0, pC0' (C proposes payload 0 on v0), arb_A(singleton A) -> v1,
arb_C(singleton C) -> vC (incomparable fork), ('d','A','B',v1),
('d','C','B',vC) — B now holds both forks with both arbs in its past
(P2's witness) — then ('m','B',(v1,vC),w) (P3), and B's re-proposal
on v_m. Every event admission-checked and priced exactly; every
prefix's option set gated. Enumeration depth caps declared in the
banner; the signature chain carries the deep gates (RF5-honest).

## 4. Gates

G0 family sizes (printed MEASURED on first run; anchored by the
round). G1/G1b closure + (event, weight) gauge invariance (ported).
G2 conflict genesis (ported; new-family censuses printed). G3 the
opportunity iff-sweeps: pair-arb (ported), RESCUE (re-proposal on a
delivered version enabled iff the delivery is in the proposer's past),
MERGE (P3's iff). G4 staleness ported + P4's kill-and-rescue exact
chains + P1's starvation sweep (delivery-free sub-family: created
holdings only via participation; 0 exceptions) + P2's two-arb observer
census (full family > 0 at the signature chain; delivery-free
sub-family = 0). G5 kernel block ported + the merge pair-click = 1/2
exact. G6 joins: arbs AND deliveries censused; D23/NSE/D25/D27 +
Hegerfeldt remain d42b-lift obligations (declared). G7 the extended
battery (>= 9 branches, all hand-derived: genesis idle 1/2; all-open
idle 1/4; post-proposal idle 1/2 = 1 - merge/arb 1/4 - deliver 1/4;
delivery q values; merge q with and without value conflict; ported
d42a lines re-derived under the new sectors). G8 record basis + new
distinctions (sender, receiver, delivered version, merge pair,
merge winner). G9 the ladder on the extended grammar: sums on
1 + k/4, k from blind arb layers ONLY (deliver/merge sectors
initiator-view); spectra printed MEASURED. G10 P2/P3 combined: the
constructed observer past with two same-base arbs is admissible and
the merge option set there is exactly {the pair merges}; the
delivery-free theorem side at exact 0.

## 5. Fronts and risks

RF1 depth: the signature chain is 8 events — enumeration cannot reach
it; constructed-chain gates carry P2/P3/P4 (declared, per RF5
honesty). RF2 merge-vname collisions: v_m identity includes pkey +
initiator (incomparable double-merges of the same pair by different
holders are distinct records — a NEW fork species at the merge level;
censused, declared, its reconciliation recurses). RF3 the deliver
sector enlarges branching ~2x; caps tuned and printed. RF4 no measure
claim: everything stays at weight-system level; the placement front
(d42b3) owns normalization. RF5 the elementary-click refinement of
kernel draws (front 4) is d42b2's, running in parallel; its result
binds the merge click too.

## 6. Round-1 amendments (2026-07-18; round frozen at #299)

**C1 (F1 — the pricing layer IS the admission relation).** A7's
command ("the opportunity set is the past-local admission relation
and NOTHING ELSE") binds the PRICING layer, not only the generator:
(i) the idle docks the arb-and-merge 1/4 iff an ADMISSIBLE arb event
or an enabled merge pair exists for the initiator; (ii) the merge
denominator D = #distinct admissible arb ckeys + #enabled merge
pairs; (iii) arb events unchanged (their own past is already the A4
join view). §2's own-view availability reading is SUPERSEDED — it
destroyed budget off-cap (h5: a sector open with zero admissible
events, sum 3/4; h11: a live merge split against a join-dead arb
half, sum 7/8; both referee-constructed, both healed to exactly 1 by
this amendment, in-family invisible at 0/500). DECLARED (the A4
precedent): the availability bit, like the component, first exists
at the join — the repaired idle has JOINT-RECORD dependence; this is
the d34b placement face appearing in the pricing layer, censused not
hidden. **P5's ladder claim RE-SCOPED: verified in-family at the
declared caps + the constructed witnesses healed; a general-depth
ladder theorem is OPEN and belongs to d42b3's constraint set.**
Physics note, recorded: the refuting mechanism IS P2's relay
structure — knowledge transported past a blind seal. Transport
breaks starvation AND naive pricing at once.

**C2 (F2/F3 — the pin's discharge list corrected).** §2's "the
battery gates these exactly" was false (two listed branches missing;
now gated: all-open idle 1/4 at SIG-FM[:6]; equal-values merge 1/4).
§2's "chained reconciliation ... censused" and RF2's "censused"
pointed at censuses that did not exist — now they do (the 9-event
third-fork chain: post-merge pairs exactly {(vC0, v_m)}, both value
branches; the double-merge fork species: admissible, incomparable,
canon-distinct — this census also GATES the merge carrier choice,
under which the F6 fossil law dies). The merge sector is
enumeration-VACUOUS at caps (0 merge events in-family; corollary,
recorded: delivery-free ⟹ co-participated creations are
wire-comparable ⟹ no pairs — RECONCILIATION DEMAND REQUIRES
TRANSPORT); declared in the banner. P2's in-family census printed
(0 at caps; a two-arb past needs 5 events). G9 upgraded to the
mechanical decomposition gate (the d42a delta standard).
