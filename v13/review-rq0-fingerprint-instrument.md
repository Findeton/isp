# R3 — INSTRUMENT / SUFFICIENCY HOSTILE REVIEW

## Branch C, the Nomological Fingerprint Hunt (RQ0-L4) — K4 primary

**Status:** `DELIVERED, FROZEN ON DELIVERY`  **Date:** 2026-08-06

**Protocol:** `v13/note-rq0-fingerprint-hostile-protocol.md` (commit `c120ea3`),
lens R3 — K4 primary: the C1 disqualification's honesty; **the freeze audit**;
the per-candidate kills re-run natively; the 11 deviations; anchor fidelity.

**Object (verified at their committed SHAs):**
paper `8fdae62b423dc78215721db0d4cc2dd3a6737fc747ffa7cda49bb89aceb80ef9`;
code `203570c51e988efc5a136b3a3fa615849b96710aeebda9bcff3125ebbd702741`;
output `f67b98ac…`; receipt `0d014138…`.  Pin `b4fc87c`; base `a5cb096`.

**Method.** All arithmetic re-derived in R3's own code
(`scratchpad/r3fp/`, `/opt/homebrew/bin/python3.13`, exact `Fraction` and
scaled-integer only), importing **nothing** from the unit and nothing from the
base modules: the 52-record lattice, the five committed laws, `Pres`, ε, ω,
`ker`, `comp`, the stabilizers, the orbits, the 687-law census, the 745
identity-free side and all six candidates were rebuilt from their stated
definitions. **23 recomputation blocks, ~40 independent quantities. Zero
mismatches against the paper and zero against the receipt.**

---

## 1. Verdict

$$\boxed{\textbf{ACCEPT-WITH-FIXES}}$$

**No computed number moved.** Every value in §4.3, §4.4, §4.5, §5, §7.1, §7.4
and the census tables reproduces exactly on an independent route. The
substantive results — CLASS-IMPOSSIBILITY, the amnesty kill of C4a, the
structural collapses of C2/C3/C4b, and the disqualification of C1 — all stand.

**Three claims do not hold as written**, and none of them is a number:

1. **The freeze certificate does not certify** (F1, major). The barrier's own
   claim is measurably false, and the mechanism cannot detect what it asserts.
   The freeze *was* honored — I verified that by the check that actually works
   (source inspection) — but "the receipt's gate order is the proof" is not
   earned.
2. **Theorem 6.1's hypothesis is measured off-fixture and its conclusion is
   about the fixture chain** (F2, moderate). As written the inference is a
   non sequitur. The conclusion survives because the extension holds when
   measured; it is not proved.
3. **The "inherited" gate 1 is an interpretation presented as inheritance**
   (F3, moderate). The verbatim anchor is faithful; what it says is ambiguous,
   and the unit's either-direction reading is the unit's own — well justified
   by the unit's own erasure finding, but not by the quotation.

### Per-rung confirmations (protocol §Verdict vocabulary)

| rung | confirmation |
|---|---|
| (a) CLASS-IMPOSSIBILITY (12-orbit theorem) | **CONFIRMED** — stabilizers 24/24/24/24/**1**, orbits 12/12/12/12/52, orbit ⟺ shape over all 52×52 pairs at the four symmetric laws, all re-derived (R1 is primary) |
| (b) the freeze discipline | **CONFIRMED IN SUBSTANCE, REJECTED AS PROVED** — see F1 |
| (c) the per-candidate kills | **CONFIRMED** — all exact, 0 mismatches |
| (d) the amnesty sweep | **CONFIRMED** — 1276/2017/**1552**; 4844/1/0; 4692/153/0; 4845/0/0 |
| (e) the C1 disqualification | **CONFIRMED on grounds 2, 3, 4**; ground 1 is non-probative and is over-weighted in the prose |
| (f) the fingerprint dichotomy | **CONFIRMED as measured over the declared family**; it is not a theorem about the declared data, and the only construction that breaks it is a fixture-tuned one — i.e. it rests on the freeze (F1) |
| (g) the corridor-hole adjudication | **CONFIRMED as disclosed** — the disclosure is exemplary; the attribution needs F3's repair |

---

## 2. The numbers table — R3's independent recomputations

All rebuilt from definitions; `=` means exact agreement with paper **and**
receipt.

| # | quantity | paper / receipt | R3 | |
|---|---|---|---|---|
| 1 | record lattice at 1..5 configurations | 1, 2, 5, 15, 52 | 1, 2, 5, 15, 52 | = |
| 2 | off-fixture population | 48 | 48 | = |
| 3 | committed law sizes DET / FUNNEL / REV / F-CLOSURE / COUNTER-LAW | 3125 / 21 / 120 / 3006 / 120 | idem | = |
| 4 | \|Pres_DET\| at 2+1+1, 2+2, tomographic, carrier algebra | 240, 420, 1280, 120 | idem | = |
| 5 | ε at the committed triple | 1/16, 1/8, 3/16 | idem | = |
| 6 | ε spectrum multiplicities (Stirling row) | 1, 10, 25, 15, 1 | idem | = |
| 7 | ω under DET: instances, non-zero | 1612, 0 | 1612, 0 | = |
| 8 | the refinement chain 2+1+1 ≺ 2+2 ≺ tomographic | true ×3 | true ×3 | = |
| 9 | **C1 at the COUNTER-LAW** (2+1+1, 2+2, **legit**, erasure) | 95/8, 93/8, **45/4**, 0 | idem | = |
| 10 | **C1 at FUNNEL** | 14, 13, **23/2**, 0 | idem | = |
| 11 | **C1 pointwise** over the 31 preparations, per law | 0, **12**, 0, 0, **3** | idem | = |
| 12 | **C2 = ε** at the fixture (+ total erasure) | 1/16, 1/8, 3/16, 1/4 | idem | = |
| 13 | **C2 vs ε off-fixture** (240 instances) | 0 disagreements | 0 | = |
| 14 | ker(Pres_L(π)) discrete at identity-containing laws | 0 exceptions / 240 | 0 | = |
| 15 | **C3 fan-in at the committed triple**, over the declared population | ≡ 1 at all five laws | ≡ 1 | = |
| 16 | C3 fan-in off-fixture (5 laws × 48 records) | constant | distinct values = {1} | = |
| 17 | the declared 5-configuration law population | **2847** | 2842 single-generated + 5 committed = **2847** | = |
| 18 | census at three configurations: laws / identity-containing / proper-boundary | 687 / 259 / 428 | idem | = |
| 19 | census fan-in: keys / >1 law / exactly 1 / worst | 874 / 175 / 699 / 428 | idem | = |
| 20 | **C4a at the fixture** (all five laws) | 1/4, 1/4, **0**, erasure 0 | idem | = |
| 21 | C4b at DET/REV/F-CL and at FUNNEL/COUNTER-LAW | 1,1,1 and 0,0,0 | idem | = |
| 22 | **C4c at the fixture** | −2, −4, **−12**, erasure **−20** | idem | = |
| 23 | **amnesty C4a** (each of the five laws) | 1276 / 2017 / **1552** | idem | = |
| 24 | amnesty C1 at FUNNEL | 4844 / 1 / **0** | idem | = |
| 25 | amnesty C1 at the COUNTER-LAW | 4692 / 153 / **0** | idem | = |
| 26 | amnesty C4c | 4845 / 0 / **0** | idem | = |
| 27 | admitted isomorphisms per law | 24, 24, 24, 24, **1** | idem | = |
| 28 | orbits of the 52 records | 12, 12, 12, 12, 52 | idem | = |
| 29 | orbit invariant ⟺ shape profile, over 52×52 | yes at the four symmetric laws | yes (and **False** at the counter-law, as the paper marks vacuous) | = |
| 30 | orbit sizes of the committed triple | 6, 3, 1 | 6, 3, 1 | = |
| 31 | triple related by an admitted isomorphism? | no | no | = |
| 32 | the three shape profiles | §7.4 | identical multisets | = |
| 33 | identity-free admissible patches; those with ε ≠ 0 | 745; 0 | 745; 0 | = |
| 34 | **G6 distinct values on the 745** (C1…C4c) | 3, 1, 12, 2, 2, 2 | idem | = |
| 35 | corridor gate matrix (6 candidates × 5 laws) | §4.5 / receipt | 30/30 rows identical | = |
| 36 | corridor survivors, pinned vs inherited G1 | {C1 @ COUNTER-LAW} vs ∅ | idem | = |
| 37 | law-blindness: distinct value triples | 3, 1, 1, 1, 2, 1 | idem | = |
| 38 | A08 every-state inversion: grid; ε-separating states | 4845; **0** | 4845; **0** | = |
| 39 | A06 state map at ρ and at the selective-amnesty state | (1/16,1/8,3/16); (0,0,1/2) | idem | = |
| 40 | reproduction: exit code; rendering vs committed artifact | 0; byte-identical | 0; byte-identical (only the wall-clock stdout line differs, which is not in the artifact) | = |

**Two quantities R3 measured that the unit does not report** (both new):

| # | quantity | R3 |
|---|---|---|
| 41 | pre-barrier candidate evaluations **at a committed boundary**, per candidate | **144** (36 at each of the four symmetric laws: 20 at the forged 2+1+1, 16 at the forged 2+2) — **864** across the six declared candidates |
| 42 | (off-fixture record, admitted isomorphism) pairs mapping onto the **legitimate** boundary | **0** at every committed law — the tomographic minimum's orbit is a singleton |

---

## 3. K4(a) — the C1 disqualification, adjudicated

**The question put to R3:** is discounting the counter-law survivor correct —
its covariance gate being vacuous because that law's isomorphism group is
trivial (no content) — versus the reading that it passed a real gate at a real
law? All four grounds re-verified natively.

| ground | measured by R3 | true? | weight as a disqualification |
|---|---|---|---|
| 1. vacuous covariance | stabilizer at the COUNTER-LAW = **1**; at the other four = 24 | yes | **non-probative** — see below |
| 2. order-entailment | C1 **anti-monotone** off-fixture at FUNNEL and the counter-law (and, checked separately, anti-monotone over **all 52** records); committed triple is a chain with the legitimate patch coarsest | yes | **decisive, independently sufficient** |
| 3. total erasure at the separating tolerance | one-atom boundary at **0** against the legitimate **45/4** (counter-law) and **23/2** (FUNNEL) | yes | **decisive, independently sufficient** |
| 4. identity-free-side split | C1 takes **3** distinct values on the 745 where ε takes **1** | yes | moderate — collateral, not spuriousness |

**Adjudication.** *The disqualification is honest and correct — but it is
carried by grounds 2 and 3, not by ground 1, and the prose leans hardest on
ground 1.*

The K4 dichotomy as posed is a false alternative, and the resolution is the
third option: C1 **did** formally pass gate 5 at a real, committed law — the
counter-law is Cycle B Prop 4.12's law, 120 admitted operations, no less real
than DET — and that pass **carries no information**. A vacuous universal
quantification is satisfied, not evaded; nothing about C1 was tested. So the
correct accounting is not "C1 failed a gate" but "**C1 was screened by four
gates, not five**". The paper's own §7.5 states this correctly ("Theorem 7.2 is
*silent* where the declared data has no symmetry"), and deviation 8 refuses to
treat the vacuous pass as a pass. Both are right.

What is not right is the **weight** the abstract and §9 put on it. "The one
corridor survivor survives at the one committed law whose declared data has no
symmetry at all … and it is the honest shape of the positive result" reads as
if the absence of symmetry were itself disqualifying. It is not: a
symmetry-free configuration is a perfectly admissible configuration, and a
reader is entitled to answer "then covariance simply has nothing to say here,
and you still have a separator." The answer to that reader is grounds 2 and 3 —
C1's separation is entailed by the boundary's position in the refinement order,
and the very threshold that admits the legitimate chart admits the boundary
that forgets the entire carrier. Those are what close the case, and they close
it at *every* law, symmetric or not. Lead with them.

One further check, in C1's favour and worth stating: **C1 is the only candidate
that is not law-blind** (3 distinct value triples across the five committed
laws, against 1 for C2/C4a/C4c and 2 for C4b) — so §6.3's "yes, the law
supplies content" is measured, not rhetorical. The content is coarseness; the
paper says so.

---

## 4. K4(b) — THE FREEZE AUDIT

**Verdict: the freeze discipline was honored. The mechanism that claims to
prove it proves nothing. `ACCEPT-WITH-FIXES` turns on this item.**

### 4.1 The claim, and what is measured against it

The paper claims, in three places:

- Abstract: "a freeze-barrier gate certifies from recorded per-gate provenance
  flags that **no corridor gate evaluated any candidate at any committed
  boundary**. The receipt's gate order is the proof."
- §3(2): "**The committed boundaries appear in no corridor computation.**"
- §11: "**The gate order is the freeze proof.**"

And gate `L4-FREEZE` asserts it in the receipt: "*NONE of them evaluated ANY
declared candidate at ANY of the four committed boundaries.*"

**Measured, in R3's own code: false.** Corridor gate **G5** (covariance) is
computed as `fn(act_part(p, g)) == fn(p)` for every off-fixture record `p` and
every admitted isomorphism `g`. Seven off-fixture records lie in the orbits of
the two forged boundaries, so the relabelled argument **is** a committed
boundary:

| law | (p ∈ OFF, g ∈ group) pairs landing on a committed boundary | which |
|---|---|---|
| DET | 36 | 20 at the forged 2+1+1, 16 at the forged 2+2 |
| FUNNEL | 36 | idem |
| REV | 36 | idem |
| FUNNEL-CLOSURE | 36 | idem |
| COUNTER-LAW | 0 | (trivial group) |
| **total per candidate** | **144** | **864 across the six declared candidates** |

All 864 occur **above** the barrier, inside gates `L4-CC1`…`L4-CC4c`, and every
one of those gates records `fixture_touched_when_fired: false` in the committed
receipt. The pre-barrier derivation gate `L4-X5` does the same for C4c.

Two of the four committed boundaries — **both forged ones** — are therefore
evaluated by every declared candidate during the corridor.

### 4.2 Why the flag cannot see it

`_TOUCHED_FIXTURE` is set only by explicit calls to `touch(part)`. There are
exactly three live call sites in the whole file (lines 868, 901, 1122): the
`freeze-lax` mutant, `run_fixture`, and `L4-COV2`. **`touch()` is never called
from any candidate evaluation, from `act_part`, or from anywhere inside the
corridor.** The "per-gate fixture-provenance flag" is therefore an
author-maintained annotation, not an instrument: it records what the author
declared, not what the run did. The `freeze-lax` mutant confirms only that a
*manual* `touch(PTOMO)` before the barrier is caught — which is not the threat
model.

### 4.3 Could a candidate have been tuned to the committed pairs without
### tripping it? — **Yes. Constructively.**

R3 built two statistics from the unit's own declared material and ran the
unit's own gate battery on them:

- **D = C4a + C1/1000** — a sum of two *declared candidates*, containing **no
  fixture reference whatever**.
- **TUNE = D − 1000·1[π = the legitimate tomographic boundary]** — the same
  statistic with one explicit read of the committed legitimate boundary.

| | G3 | monotonicity type | pinned G1 | **inherited G1** | G2a | G2b | G5 | pinned corridor | inherited corridor | separates | amnesty sweep |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **D** @ COUNTER-LAW | y | **neither** | y | **y** | y | y | y (vacuous) | **PASS** | **PASS** | YES | 3183 / 110 / **1552 inverting** → killed |
| **TUNE** @ COUNTER-LAW | y | **neither** | y | **y** | y | y | y (vacuous) | **PASS** | **PASS** | YES | 4845 / 0 / **0** → **SURVIVES** |

`TUNE` would be registered by the unit's own machinery as
`RQ0-L4-NOMOLOGICAL-FINGERPRINT`; it is **not** order-entailed (type "neither"
off-fixture) and **not** sweep-killed, so it would **break the fingerprint
dichotomy of Theorem 8.1**; and `L4-00` and `L4-FREEZE` would both be green,
because — measured — **no admitted isomorphism carries any off-fixture record
onto the legitimate boundary at any committed law (0 pairs; its orbit is a
singleton)**. The separation predicate is `legit < forged`, so the single value
a tuner must move is precisely the one value no pre-barrier gate can see.

### 4.4 What the freeze actually rests on — and it holds

The check that works is source inspection, and R3 ran it: the eight
candidate-definition functions (`c1_counterfactual_occupancy`, `c1_profile`,
`c2_generation_mismatch`, `c3_law_fan_in`, `c4a_state_alignment`,
`c4a_route2`, `c4b_reach_alignment`, `c4c_pair_resolution`) contain **zero**
references to `PI1`, `P22`, `PTOMO`, `DISC5`, `ONEATOM5`, `FIXTURE` or
`PROVENANCE`. Every one is a generic function of `(part, law, prep, rho, n)`.
Together with the definition SHA-256s of `L4-00` — which make the inspected
text the text the receipt commits to — **the freeze is honored and is
checkable.** It is checkable *by reading the definitions*, not by the gate
order.

**The fix is to claim the check that works.** Replace the certification with:
(i) the definition hashes, which bind the receipt to inspectable source; (ii)
the measured statement that **no corridor gate reads a committed boundary's
value into any verdict** — true, because G5 only compares candidate values for
equality and never uses the ordering; (iii) the disclosure that G5 does
evaluate candidates at the two forged boundaries, 144 times per candidate, and
that this is harmless for exactly that reason; (iv) the honest limit — no
in-script barrier can prove authoring order, and the freeze is warranted by
declaration and by inspectable definitions.

There is one genuine consolation the paper should claim and does not: at the
four symmetric laws, G5 *would* catch fixture-special-casing at the two forged
boundaries, because a special case there breaks covariance. The tuning gap is
exactly (legitimate boundary) ∪ (counter-law) — and C1 lives at the counter-law.
That is a sharper statement of §4.2's honesty than the one currently made.

---

## 5. K4(c) — the per-candidate kills, re-run natively

All re-derived from definitions; every value exact.

- **C1.** Counter-law **95/8, 93/8 vs 45/4**; FUNNEL **14, 13 vs 23/2**;
  pointwise **12/31** at FUNNEL and **3/31** at the counter-law, **0/31** at
  DET, REV and the funnel closure. Constant off-fixture at DET, REV and the
  funnel closure (ω ≡ 0 over all 1612 DET instances). Anti-monotone at FUNNEL
  and the counter-law. **Confirmed, including the disqualification measurements.**
- **C2 = ε.** Fixture **1/16, 1/8, 3/16** (erasure 1/4) — the terminal spectrum,
  reproduced on an independent route; **0 disagreements with ε over all 240
  off-fixture instances**; ker(Pres) discrete at every one of the 240 (all five
  committed laws contain the identity — verified). Monotone off-fixture ⇒ dies
  at G1 with G2a behind it. **Confirmed.**
- **C3.** Population rebuilt: **2842** laws generated by one admitted
  single-valued operation, **plus the five committed laws** (none of which is
  single-generated) = **2847**, correctly named a population. Fan-in **≡ 1** at
  the committed triple at all five laws, and the off-fixture value set is
  exactly {1} — constant, so G3 kills it. Census resource independently
  confirmed real one arity down: **874** keys, **175** from more than one law,
  **699** from exactly one, worst **428**. **Confirmed.**
- **C4a.** 1/4, 1/4 vs **0** at all five laws; erasure 0; a function of the
  shape off-fixture (G2b fails); type "neither"; amnesty **1276 / 2017 /
  1552**. **Confirmed** — including that C4a is the *only* separator that is
  not order-entailed and the *only* one the sweep touches.
- **C4b.** Reachability classes trivial under DET, REV and the funnel closure ⇒
  value 1 at every boundary but the one-atom one ⇒ a function of ε off-fixture
  (G2a); constant under FUNNEL and the counter-law (G3). Both kills
  **confirmed**.
- **C4c.** −2, −4, **−12**, erasure **−20**; anti-monotone at all five laws
  (provably: refinement never increases Σ|r|(|r|−1)); amnesty 4845/0/0.
  **Confirmed.**

---

## 6. K4(d) — the eleven declared deviations, adjudicated

| # | deviation | adjudication |
|---|---|---|
| 1 | G2 in two readings (G2a / G2b) | **FIX-REAL, load-bearing.** Verified the split does work: C4a passes G2a at every law and fails G2b at every law; C1 passes G2a at FUNNEL but fails G2b there and passes both only at the counter-law. G2a alone would admit block-profile statistics. Correctly declared. |
| 2 | G1 in two readings, pinned first | **FIX-REAL, the most consequential.** The disclosure discipline is exemplary. But the attribution needs repair — see F3. |
| 3 | orientation fixed (admitted iff small) | **FIX-REAL.** Necessary: with the orientation free, ε itself separates the triple in the reversed direction (3/16 > 1/8 > 1/16), which is what stage-5 §5.3 warns against. |
| 4 | the corridor decided on an off-fixture population | **FIX-REAL as a design; its stated rationale is falsified.** The population choice is good and costs nothing. The justification given — "makes the freeze *checkable* — the barrier gate reads recorded provenance flags rather than trusting the ordering" — is exactly the claim F1 refutes. Rewrite the rationale, keep the design. |
| 5 | two post-barrier diagnostics (`L4-ENT`, `L4-ERASE`), neither gating a kill | **NEEDS A CLAUSE.** True as stated of the *pinned corridor verdicts*: every kill in §4.5 is by a pinned gate. False of the *paper's headline*: `L4-ENT` gates Theorem 8.1 and is disqualification ground 2, and `L4-ERASE` is ground 3. They eliminate no candidate but they carry the verdict on C1. Say so. (Minor and in the unit's favour: the one-atom boundary is itself an **off-fixture** record, so the erasure column is off-fixture data, not fixture truth at all — a stronger position than the deviation claims.) |
| 6 | G6 as constancy on the identity-free side | **FIX-REAL.** Strictest defensible reading, declared as such; verified 5 of 6 fail, with counts 3/1/12/2/2/2. |
| 7 | C3's constructed 5-configuration population | **FIX-REAL.** Verified 2842 + 5 = 2847, never called a census, and the negative shipped alongside the census numbers that show the resource is real at arity three. Clean. |
| 8 | the counter-law's vacuous covariance reported, not absorbed | **FIX-REAL, and the paper's best honesty move.** Verified: `L4-COV0` measures 24/24/24/24/1. |
| 9 | a qualified positive in the registered outcome list | **FIX-REAL.** The pin's letter is met; the parenthetical intent is measured false; four qualifications ship. Consistent with the stage-5 precedent it cites. |
| 10 | census slot instantiated as `BLOCKED-AT-THE-REFINEMENT-ORDER` | **COSMETIC** (naming), and the object named is the one measured. |
| 11 | Lean none; no new primitive | **COSMETIC** (compliance). Accurate. |

**Tally: 8 fix-real, 2 cosmetic, 1 (#5) requiring a clause; and #4's rationale
must be rewritten.** The deviations list is complete — R3 found no undeclared
deviation from the pin.

---

## 7. Anchor fidelity to the stage-5 terminal values

**13 of the 16 anchors were re-derived by R3 on independent routes and all 13
are exact:** A01 (1,2,5,15,52), A02 (3125, 120), A03 (240, 420, 1280, 120),
A04 (1/16, 1/8, 3/16), A05 (spectrum + 1,10,25,15,1), A06 (state map at ρ and
at the selective-amnesty state: (1/16,1/8,3/16) and (0,0,1/2)), A07 (1612, 0),
A08 (4845 grid; **forward separating set empty**), A09 (687, 259, 428), A10
(745, 0), A11 (874, 175, 428), A13 (the chain), A16 (the verbatim quote).

**A16 is faithful.** Checked against the immutable stage-5 paper: §10 reads
"*no refinement-monotone statistic whatever — not merely no function of the
quadruple, and not even one that could read provenance — can separate them by
a threshold. Any successor must be non-monotone in the refinement order, or
must live on the atlas rather than on the patch.*" The unit's §2.1 ellipsis
elides only the strengthening clause; the quotation does not misrepresent.
**What the quotation does not settle is the reading** — see F3.

Not independently re-derived by R3 (not K4-critical; R1/R2 territory): A12
(the cost tower), A14 (the collision), A15 (route agreement — R3's entire
recomputation is an independent instance of the same check and agrees).

---

## 8. Findings, ranked

**F1 — MAJOR (fix-real). The freeze certificate does not certify.** §4 above.
Measured: 864 pre-barrier candidate evaluations at committed boundaries with
every flag recording `false`; `touch()` never called from a candidate
evaluation; and a constructive `TUNE` that passes the pinned *and* inherited
corridor, separates, survives the sweep 4845/0/0, breaks the dichotomy, and
leaves `L4-00`/`L4-FREEZE` green. **Mitigation, verified: the freeze was
substantively honored — zero fixture references in all eight candidate
definitions.** Fix: claim the check that works, disclose the G5 evaluations,
and state the honest limit.

**F2 — MODERATE (fix-real). Theorem 6.1's hypothesis does not reach its
conclusion.** The hypothesis is "monotone … *as measured on the off-fixture
comparable pairs*"; the conclusion is about the committed triple, which is not
in that population. Off-fixture monotonicity does not entail monotonicity
across the fixture chain. R3 measured the extension and it holds — off-fixture
type equals all-52 type in all nine (candidate, law) cases checked (C1, C4a,
C4c × DET, FUNNEL, COUNTER-LAW; 224 off-fixture vs 306 all-52 comparable
pairs) — so **no number moves**. But the theorem must either take the all-52
measurement as its hypothesis or say plainly that the extension is measured,
not proved. Load-bearing: it is C1's ground 2 and arm 1 of the dichotomy.

**F3 — MODERATE (attribution). The inherited G1 is the unit's reading, not the
terminal cycle's words.** Stage-5's first clause rules out only the monotone
direction; "non-monotone in the refinement order" is genuinely ambiguous. The
unit's either-direction reading is *correct and well-motivated* — and the unit
itself supplies the missing argument (`L4-ERASE`: an anti-monotone separator's
tolerance admits total erasure, so it grades coarseness just as a monotone one
does) — but §2.1's "the inherited G1 excludes **either** direction" states an
interpretation as an inherited fact. Fix: present the strong reading as the
unit's extension, justified by the unit's own erasure measurement.

**F4 — MINOR (fix-real).** §11: "45 gates, of which 15 are must-pass
**derivation** gates". Only 7 of the 15 are derivation-class (X1–X7); the rest
are freeze (2), amnesty (1) and covariance (5). Drop "derivation".

**F5 — MINOR (scope).** §9's "a non-monotone, non-covariant statistic at an
asymmetric law is not excluded by either — it is **only unexhibited**" is
falsified by **D = C4a + C1/1000**, built from two declared candidates with no
fixture reference: measured type "neither", it passes the full pinned *and*
inherited corridor at the counter-law. It dies at the amnesty sweep (1552
inversions, inherited from C4a), so the verdict is untouched and in fact
**strengthened** — the class is exhibited and the sweep kills it. Also
"non-covariant" is the wrong word at the counter-law, where every statistic is
vacuously covariant. Related: the declared family is not closed under sums, and
a sum of two declared candidates passes gates neither passes alone — worth one
sentence, because it bounds what "the declared family contains none" buys.

**F6 — MINOR (clarity).** The one-atom boundary is *in* the 48-record
off-fixture population (it is not one of the four committed boundaries). The
paper calls it "the diagnostic boundary" and treats its value as a fixture
column; it is off-fixture data. This helps the unit (deviation 5) but will
confuse a reader counting populations.

**F7 — no finding, stated for the record.** Reproduction is clean: re-run under
a no-op mutant exits 0 with 16/16 anchors, 45 gates, 0 must-pass failures, and
the rendering is byte-identical to the committed `_output.txt`; no repo file
was modified. No float in any substantive path. No forbidden vocabulary outside
the scope box's own disclaimers and the non-claims. Every impossibility
sentence in §7.2, §7.5, §9 and §10 carries its configuration- and
law-quantifier. Single-threaded: the paper narrates no correction rounds.

---

## 9. Sentences to rewrite

1. **Abstract**, "…a freeze-barrier gate certifies from recorded per-gate
   provenance flags that no corridor gate evaluated any candidate at any
   committed boundary. **The receipt's gate order is the proof**, and it is the
   deliverable the pin asked for first." → the gate order is not the proof.
   Replace with the definition hashes + the measured statement that no corridor
   gate reads a committed boundary's value into any verdict, and disclose the
   G5 evaluations.
2. **§3(2)**, "**The committed boundaries appear in no corridor computation.**"
   → false as measured (144 evaluations per candidate at the two forged
   boundaries). Rewrite as: the corridor's *decisions* are functions of the 48
   off-fixture records and the 745 census patches; gate G5 additionally
   evaluates each candidate at the two forged boundaries as images of
   off-fixture records under the admitted isomorphisms, and uses only equality
   with the off-fixture value.
3. **§3(3)**, "`L4-FREEZE` passes only if every gate above it has that flag
   false." → say what the flag is: an author-declared annotation set at the
   fixture stage, not an instrumented detector; and state that no in-script
   barrier can establish authoring order.
4. **§11**, "**The gate order is the freeze proof.**" → same repair as 1.
5. **§11**, "45 gates, of which 15 are must-pass **derivation** gates" → "15
   must-pass gates (7 derivation, 5 covariance, 2 freeze, 1 amnesty)".
6. **Theorem 6.1**, "Let $f$ be monotone in the refinement order in either
   direction, *as measured on the off-fixture comparable pairs*." → either take
   the hypothesis over all comparable pairs (which R3 confirms holds for C1 and
   C4c) or state the conclusion as measured rather than entailed.
7. **§2.1**, "The pin's G1 excludes the monotone direction only; **the
   inherited G1 excludes either direction.**" → attribute the either-direction
   reading to this unit, and justify it by `L4-ERASE` rather than by the quote.
8. **§9**, "…is not excluded by either — it is **only unexhibited**, and the
   declared family contains none." → exhibited by C4a + C1/1000 at the
   counter-law, and killed by the sweep; say so, and drop "non-covariant".
9. **Abstract / §9**, the ordering of C1's four qualifications → lead with
   order-entailment and total erasure; demote the vacuous covariance to what it
   is, a statement that one of five gates did not test C1 at all.
10. **Appendix A, deviation 4**, the "makes the freeze checkable … reads
    recorded provenance flags rather than trusting the ordering" rationale →
    replace; the design is right, the reason given is the one that fails.
11. **Appendix A, deviation 5**, "They explain the separations; **they do not
    eliminate any candidate.**" → add: they eliminate none, but `L4-ENT` gates
    Theorem 8.1 and both carry the disqualification of C1.

---

## 10. What R3 did not test

The 12-orbit theorem's *edge* (K1) and the dichotomy attacked by construction
inside the declared data (K3) are R1's and R2's primaries; R3 re-derived the
orbit census, the 52×52 shape identification and the stabilizer orders as
inputs to the K4 adjudication but did not press their proofs. R3 did not
adjudicate which reading of the corridor binds (K2) beyond F3's attribution
point. Anchors A12 and A14 were not independently re-derived. No claim is made
about statistics outside the declared family beyond the two constructions D and
TUNE reported in §4.3.

---

## 11. Bottom line

The unit's arithmetic is sound — forty-odd quantities, two independent
implementations, zero disagreements — and its central negative results are
correct and correctly scoped. Its most valuable habits are its own disclosures:
the corridor hole, the vacuous covariance gate, the qualified positive. The
defect is that its single most emphasized methodological claim — that the
receipt's gate order *proves* the freeze — is the one claim in the paper that
does not survive being measured. The freeze held; the proof of it did not. Fix
the claim, repair Theorem 6.1's hypothesis and the inherited-G1 attribution,
and the unit is publishable at its stated scope.

$$\boxed{\textbf{ACCEPT-WITH-FIXES}\quad\text{— no number moved; three claims
rewritten; the freeze certificate replaced by the check that works.}}$$
