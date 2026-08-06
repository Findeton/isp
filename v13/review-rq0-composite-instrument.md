# R3 — SUFFICIENCY / INSTRUMENT LENS HOSTILE REVIEW

## RQ0-L1 Cycle B′ — composite boundaries and the de-smuggling arena

**Reviewer:** R3 (sufficiency/instrument), primary **K4** + **K3(ii)** support.
**Protocol:** `v13/note-rq0-composite-hostile-protocol.md` (commit `612b149`),
FROZEN before dispatch. Judged against that protocol only. No cross-reading
of the R1 or R2 reviews.
**Object, SHA-verified at review time (all four match the protocol):**

| artifact | sha256 prefix | protocol | match |
|---|---|---|---|
| `v13/paper-rq0-composite-boundaries.md` | `fc94524d6ef2` | `fc94524d6ef2` | yes |
| `v13/code/rq0_l1_composite_exact.py` | `52809c240345` | `52809c240345` | yes |
| `v13/code/rq0_l1_composite_output.txt` | `cb520b01c1df` | `cb520b01c1df` | yes |
| `v13/code/rq0_l1_composite_receipt.json` | `73dbdc4a1d5f` | `73dbdc4a1d5f` | yes |

**Method.** Every number below was recomputed in code written from scratch in
`…/scratchpad/r3bp/` (`r3_native.py`, `r3_native2.py`). Nothing was imported
from the unit; the committed primitives it relies on (the Givens-rotated PVM
construction, the matched dephasing and its range by exact elimination, the
centre-dimension computation, the reprepare closure, the partition lattice)
were re-implemented from their committed descriptions. Exact
`fractions.Fraction` arithmetic throughout; no float anywhere in my path. The
unit was **not executed**, to guarantee no repo mutation.

---

# VERDICT

> ## ACCEPT-WITH-FIXES

**Not a single load-bearing number is wrong.** Nineteen independently
recomputed quantities matched the paper and receipt exactly, zero mismatches,
including all six constructed-boundary anchors, the atom map, the counter-law
triple and both sharpness controls. The one divergence I found in my first
battery (counter-law records fixed) was **my own** meet-convention error, not
the unit's; corrected, the unit's 52 is right. The discriminator does fire in
both directions exactly as claimed, and the top-of-lattice guard escape is
real and reproduces.

The fixes are **not numerical — they are scope.** Two of the three pillars the
paper leans on to make `RQ0-L1-DESCENT-SELECTOR` mean more than a one-boundary
criterion are, at the declared arena, **non-binding**:

1. the independence gate **could not have failed** at the arena (F1), and
2. the co-reference clause (D2) **removes zero records** from every context in
   the arena (F3),

and the adversarial pair that K3(ii) asks about **exists and is constructible
from committed machinery** (F2). None of this is disclosed. The rung survives,
but only in a form the paper does not currently state.

---

# 1. Findings, ranked

## F1 — MAJOR (K4 primary). The arena's independence certificate is cardinality-forced: the gate could not have failed.

The gate (`independence`, unit line 1072) accepts when no admitted relabelling
σ satisfies `family_image(F_A, σ) == F_B`. At the declared arena it is run on

- `F_eraser`, **cardinality 2**  (unit line 1168)
- `F_man`, **cardinality 2**  (unit line 1179)
- `F_address`, **cardinality 6**  (unit line 1169)

Every σ is a bijection, so `|family_image(F, σ)| ≤ |F|`. Hence for **every one
of the 120 relabellings**, `|image| ≤ 2 < 6 = |F_address|`, and the equality
test is **structurally unsatisfiable**. Recomputed natively:

```
max_sigma |image(F_eraser)| = 2 ;  |F_address| = 6  -> equality impossible for EVERY sigma
max_sigma |image(F_man)|    = 2 ;  |F_address| = 6  -> equality impossible for EVERY sigma
any sigma with |image| == |F_address| ?  False
```

Proposition 5.4's certificate ("none carries… the gate returns independent
with an empty witness list") is **true, and vacuous**: it reports the absence
of a witness that no choice of the two families' *contents* could have
produced. The independence of the arena's two contexts is decided by a
cardinality mismatch between two hand-declared sets, not by any structural
feature of the task families.

The paper's own "**The gate bites**" paragraph does not repair this — it makes
it worse rhetorically. That control (H2-03) compares `F_eraser` (2) with
`F_relabelled` (2): **equal cardinality**, so it genuinely can fail, and it
does, naming six carrying isomorphisms (I reproduce all six exactly, below).
The paper then writes "A gate that could not fail would prove nothing; this
one fails exactly where it must." The gate that fails and the gate that
certifies the arena are run on **different cardinality regimes**, and only the
first could ever have failed. The credibility earned by the control is
transferred to a certificate that did not earn it.

This is the K4 kill-shot landing. It is not that the paper treats
measured-independence as law-independent — Definition 5.3 says "of the law"
and Proposition 5.5 states law-relativity explicitly (see §2). It is that the
measurement, at the arena where the positive rung is claimed, **has no
discriminating power at all**, and this is nowhere said.

## F2 — MAJOR (K3(ii)). The adversarial pair exists. Construction supplied, from committed machinery only.

K3(ii) asks: under which committed laws could an adversary manufacture **both**
contexts so the pair passes the independence gate **and** the forged record
descends? The protocol says the paper need not solve this but must not
foreclose it, and that supplying a construction would be a MAJOR finding.

**The construction.** The decisive structural fact is that the declared task
**family** and the **boundary** it supposedly presents are *decoupled* in the
instantiation: `F_eraser` and `F_address` are hand-declared constants (unit
lines 1168–1169), and **no gate anywhere in the unit checks that a declared
family induces the boundary it is paired with**. The independence gate
constrains families; descent constrains boundaries, through incidence. An
adversary therefore controls the two independently.

Take both contexts to be the **aligned manufactured boundary** — the paper's
own §7.6 object, the Cycle B construction with the rotation deleted, i.e. a
PVM *chosen to match a preselected measure*. Declare the two families with
different cardinalities. Recomputed natively:

```
context 1 = ALIGNED(2,1,1)   incidence [[0,1],[2],[3],[4]]
context 2 = ALIGNED(2,1,1)   incidence [[0,1],[2],[3],[4]]
forged record = context 1's TOP (the atom instrument of its own boundary) = [[0],[1],[2],[3]]
  (D1) transports without collision : True
  (D3) non-vacuous                  : True
  (D2) realized in context 2        : True
  => forged record CERTIFIED : True     (certified set size 14)
independence gate, |F_1| = 2 vs |F_2| = 6, all 120 relabellings : INDEPENDENT, witnesses []
   max_sigma |image(F_1)| = 2 < 6  ->  the gate CANNOT fail
```

So: **both contexts manufactured, the pair passes the independence gate, and
the manufactured record descends.** A variant avoiding the identical-copy
objection — context A = ALIGNED(2,1,1), context B = ALIGNED(2,2), two
*different* manufactured boundaries — also certifies four non-vacuous records
of A against B, including `[[0],[1,2],[3]]` and `[[0,1,2],[3]]`.

**Adjudication.** The paper does **not** foreclose this: no sentence claims the
pair is impossible, and §7.6 honestly concedes the descent half ("descent does
not certify 'not chosen to match a measure'"). But it does not *name* it
either. §8's "The next obstruction, named" names only arena-comparison ("A
record certified in one arena and a record certified in another have not been
compared"). The adversarial-pair question is the nearer obstruction and it is
missing. Worse, the un-conceded half is the one that matters: §7.6 concedes
that descent tolerates manufacture, while §1.4's no-smuggling gate and Prop 5.4
imply that *independence* is the thing standing between the arena and a forged
pair. F1 shows it is not standing at all.

**This does not trigger `RQ0-L1-SMUGGLING-SURVIVES-DESCENT`.** The pre-registered
escalation is scoped to *the constructed (rotated) manufactured record*, and
that record still fails (D1) in every case — I reproduce all three failures.
The arc does not halt. What is required is disclosure, not escalation.

## F3 — MAJOR (instrument). The declared second context *is* the declared overlap; clause (D2) does no work at the declared arena.

`ctx["ADDRESS"]` is `boundary_from_blocks("ADDRESS", (1,1,1,1,1))` (unit line
1129) and the overlap is `overlap_atoms_diagonal(5)` (line 1105). Recomputed:

```
ADDRESS atoms == overlap atoms, atom for atom : True
ADDRESS incidence map = [[0],[1],[2],[3],[4]]   (the identity)
|facts realized by ADDRESS| = 52  ==  |all partitions of the overlap| = 52   (equal: True)
```

Because ADDRESS *is* the overlap, its incidence is the identity, every one of
its 52 records transports without collision, and its realized fact set is
**every partition of the overlap**. Clause (D2) — "some record of the second
context has the same fact content" — is therefore **satisfied automatically**
by anything that already passes (D1) and (D3). Measured directly:

| context | \|D1∧D3 only\| | \|D1∧D2∧D3 vs ADDRESS\| | records D2 removes |
|---|---|---|---|
| MAN211 | 1 | 1 | **0** |
| MAN22 | 1 | 1 | **0** |
| MAN1111 | 1 | 1 | **0** |
| ERASER | 51 | 51 | **0** |
| ALIGNED211 | 14 | 14 | **0** |

**Co-reference across two independently declared contexts — the paper's
central conceptual move, the thing that is supposed to change the carrier and
escape the one-boundary obstruction — is inert at the declared arena.** At the
arena, descent = (D1) ∧ (D3): a criterion evaluated on **one** context and
**one** overlap. The second context contributes nothing.

D2 becomes binding only against TOMO, where `|facts realized| = 2` — and there
the positive direction collapses (51 → 1, §7.6). So on the arena where the
positive rung is earned, D2 is vacuous; on the arena where D2 bites, the
positive rung is withdrawn. The paper reports the second fact (honestly, in
§7.6) and never the first.

This also weakens Theorem 6.2's escape in interpretation, though not in fact.
The escape is genuine — the certified set really does omit ⊤, I reproduce it
for all three contexts, and the carrier really is a pair structure of size 1
with the candidate absent. But the *reason* ⊤ is omitted is (D1), a
single-context collision test at a declared overlap, not the two-context
co-reference the paper foregrounds.

## F4 — MODERATE (K4). Under the counter-law the gate is degenerate, and Prop 5.5 under-discloses it.

Recomputed natively (own closure of the reprepare futures):

```
admitted sector maps = 120 ;  reversible = 1 ;  records fixed = 52 of 52
the reversible admitted maps: [(0, 1, 2, 3, 4)]      <- the identity, alone
relabelled context independent UNDER COUNTER-LAW = True
under the counter-law the gate fails on 4 of 16 ordered family pairs
   -- exactly the diagonal, i.e. only when A == B literally
```

Prop 5.5 says "the cyclic shift is not admitted, so the relabelled context…
**passes** the independence gate there," and draws the (correct) moral that
independence must be certified per law. Both halves are true. But the measured
fact is stronger and is not stated: since the counter-law admits **exactly one**
isomorphism, the identity, the gate under that law reduces to the test
`F_A ≠ F_B`. It is not a weaker independence criterion — it is **not an
independence criterion at all**; it cannot distinguish a relabelled copy from
anything else.

Relatedly, Prop 5.5's recitation of "one hundred and twenty admitted sector
maps" is decorative for the gate: `isos_R = rev` (unit line 1515), so the
search space under the counter-law is **1**, not 120. The 120 is correct as a
property of the law (anchor L20, which I reproduce) but it is not what the
gate searches, and the sentence places the two numbers adjacently in a way
that implies otherwise.

## F5 — MODERATE. The "positive control, the identity overlap" is the same computation as the headline it is supposed to control.

H2-09 sets the overlap to ERASER's own core and the partner to a copy, and
reports 51 of 52. The H2-07 headline reports ERASER certified 51 of 52 against
ADDRESS. Recomputed:

```
H2-09 self-overlap incidence      = [[0],[1],[2],[3],[4]]
H2-07 ERASER-vs-ADDRESS incidence = [[0],[1],[2],[3],[4]]
identical incidence data : True
H2-09 certified = 51        H2-07 certified = 51
```

By F3 (ADDRESS = the overlap, identity incidence) the two are **the same
computation on the same data**, not a control and a result. A control that
cannot come apart from the claim it controls provides no evidence. §7.1's
"The selector fires when it should, and the one exclusion is the clause that
excludes it" is, at the declared arena, a restatement of §6.4 direction two.

## F6 — MODERATE. §2 and deviation (2) assert an exhibit the declared family does not contain.

Definition 2.2's follow-up sentence: "Section 4 exhibits a declared task where
the two partitions have the same number of blocks and are nevertheless
different." Deviation (2) repeats it: "One declared task has equal block counts
on the two sides and different partitions; a count-based gap would have missed
it."

The unit's own `joint_tasks` table refutes both. Across all eight declared
tasks, `core_AB` vs `product_core` are: 4/4, 4/4, 4/1, 4/1, 4/1, 2/1, 2/1, 2/2
— with `gap_opens` = false, false, true, true, true, true, true, false. **Every
task whose gap opens has unequal block counts, and every task with equal block
counts has a closed gap.** No declared task has equal counts and different
partitions.

The *definitional* choice (gap = partition inequality, not count difference) is
correct and worth keeping — it is the right definition regardless. But the
justification offered for it, twice, is an exhibit that does not exist in the
declared family. (The H1 recomputation is R1's primary; this finding is
adjudicated purely from the unit's own committed receipt table, which is
decisive on it.)

## F7 — MINOR. The law qualifier is missing where it matters most: the abstract and the verdict.

Definition 5.3 ("no admitted isomorphism **of the law**") and Prop 5.5 carry
law-relativity correctly, and gate H2-11's text states it outright. But:

- **Abstract:** "independence measured, not asserted, by searching all one
  hundred and twenty admitted relabellings" — no law qualifier, and the
  abstract never mentions law-relativity at all.
- **§1.4, Object 2, No-smuggling row:** "independence of the two contexts is
  measured rather than declared" — no qualifier.
- **§8, `RQ0-L1-DESCENT-SELECTOR` scope line:** "*Scope:* finite; one declared
  arena; exhaustive over all records of every context in it" — the scope line
  does **not** record that the independence certificate is relative to the
  standard law, and the "What is nevertheless not earned" paragraph does not
  mention law-relativity either.

No sentence *asserts* law-independence, so K4's narrow question ("does any
sentence quietly treat measured-independence as law-independent?") answers
**no**. But the qualifier is absent from the three places a reader takes the
claim from.

## F8 — MINOR. H2-01's boolean under-tests its own claim.

The gate text says "the declared overlap is reached by every atom of **every
declared context**"; its printed `contexts` value lists all seven. The boolean
quantifies over four (`MAN211, ERASER, ADDRESS, TOMO`; unit line 1153),
omitting MAN22, MAN1111 and ALIGNED211. I verified all seven do satisfy
reach-and-cover, so **the claim is true** — this is a testing-scope/reporting
mismatch, not a false claim.

## F9 — COSMETIC. One forbidden-vocabulary token outside the permitted zones.

The full sweep (`locality|topology|causal|spacetime|QFT|gravity|manifold|
Lorentz`) returns six hits: lines 111–112 (scope box), 688–692 (non-claims),
and **line 204** — §1.4's no-smuggling row, "the definition mentions no
correlation, no entanglement, no factorization and no locality". It is a
negation, so it is harmless in substance, but it sits outside the scope box and
non-claims list where the protocol licenses negations.

---

# 2. The K4 adjudication

**K4 asks three things. My answers:**

**(i) What grounds the law choice for the gate?** *Nothing in the paper.* The
arena is declared with "the standard law" (Prop 5.4) and no argument is offered
for that choice over any other. Prop 5.5 demonstrates the choice *matters* — the
same relabelled context is dependent under one law and independent under the
other — and then stops. This is a genuine open, and the paper should say so
rather than leave the reader to infer it from a control.

**(ii) Is the gate's meaning scoped correctly everywhere?** *Mostly, but not in
the abstract or the verdict.* See F7. The definition and the proposition are
correct; the three summary locations drop the qualifier.

**(iii) Does any sentence quietly treat measured-independence as
law-independent?** **No.** I checked every occurrence of "independent",
"independence" and "admitted isomorphism" in the paper. Definition 5.3 binds it
to the law; Prop 5.5 states the relativity; the non-claims describe it as "a
measured statement about which **admitted** isomorphisms exist", and "admitted"
is defined per-law in §2 ("Admission is measured per law and is never inferred
from algebraic existence"). The Cycle B counter-law pass **is** disclosed, in
Prop 5.5, §7.4 and §7.5, and disclosed correctly as far as it goes.

**But K4 lands anyway, from the other side.** The kill-shot the protocol
anticipated was a law-independence leak. What is actually wrong is worse and
undisclosed: under the **standard** law the gate is cardinality-forced (F1),
and under the **counter-law** it is degenerate to literal equality (F4). The
gate is law-relative *and* non-binding under both committed laws. "Independence
measured, not asserted" is the paper's phrase; what is measured is
non-binding, which the paper never says.

---

# 3. Required recomputations — results

## 3.1 The declared-before-both overlap ordering — **VERIFIED**

`overlap_atoms_diagonal(5)` is constructed at unit line 1105, **before** any
context (contexts begin line 1110), and its constructor takes no context as
input — it depends only on the carrier dimension. The ordering claim of
deviation (6) is sound as stated.

**However** (F3): "declared before both" is satisfied while "independent of
both" is not, because the second context is subsequently declared to *be* the
overlap. The no-smuggling gate's force comes from the conjunction, and the
conjunction does not hold.

## 3.2 The 120-relabelling independence sweep, re-run natively — **REPRODUCED, and shown non-binding**

```
|perms| = 120
eraser vs address : independent = True,  witnesses = []
man    vs address : independent = True,  witnesses = []
```
Matches H2-02 exactly. See F1 for why the empty witness list carries no
information here.

## 3.3 The relabelled control's six carrying isomorphisms — **REPRODUCED EXACTLY**

```
(1, 2, 3, 4, 0)   (1, 2, 4, 3, 0)   (1, 3, 2, 4, 0)
(1, 3, 4, 2, 0)   (1, 4, 2, 3, 0)   (1, 4, 3, 2, 0)
```
Identical, as a set and elementwise, to H2-03's `carrying_isomorphism` value.
The cyclic shift `(1,2,3,4,0)` is among them, as the gate requires. All six
fix σ(0)=1 and σ(4)=0 and permute {1,2,3}→{2,3,4} in all 3! = 6 ways — the
correct stabilizer structure for carrying `F_eraser` onto its shift image.

## 3.4 The counter-law pass disclosure — **CORRECTLY DISCLOSED, UNDER-DISCLOSED IN DEPTH**

Recomputed: 120 admitted sector maps, exactly 1 reversible (the identity), 52
of 52 records fixed. All three match anchors L20/L21/L22. The pass **is**
reported, in three places. What is not reported is F4's degeneracy.

*Correction to my own first pass:* my battery-1 run reported "1 of 52 records
fixed", which would have contradicted L22. That was **my** error — I had
implemented `meet_of_parts` as the common refinement, whereas the predecessor
defines it as the transitive closure of the union of equivalences
(`rq0_l0_fixed_point_exact.py` line 614). With the predecessor's convention my
native code returns **52 of 52**, agreeing with the unit. The unit is correct;
I record the error here so the review is auditable.

## 3.5 The sharpness controls, re-run — **BOTH REPRODUCED EXACTLY**

**Aligned manufacture descends:**
```
ALIGNED211 incidence = [[0,1],[2],[3],[4]]
top record transports = True ; certified vs ADDRESS = True
certified count vs ADDRESS = 14
```
Matches H2-08 (`aligned_manufactured_record_certified: true`) and H2-08b's 14.

**The coarser context withdraws the certificate (51 → 1):**
```
|facts realized by TOMO| = 2  ->  {((0,1,2,3),(4,)), ((0,1,2,3,4),)}
ERASER      cert vs ADDRESS = 51   cert vs TOMO = 1   top certified vs TOMO = False
ALIGNED211  cert vs ADDRESS = 14   cert vs TOMO = 1   top certified vs TOMO = False
MAN211      cert vs ADDRESS =  1   cert vs TOMO = 1   top certified vs TOMO = False
```
Matches H2-08b exactly. The withdrawal is real and the framing in §7.6 is
honest: the negative direction is robust across both second contexts, the
positive is not. I confirm the mechanism the paper gives — TOMO realizes only
one non-vacuous fact, `({0,1,2,3},{4})`, so nothing with finer fact content can
co-refer.

One framing note: §7.6 and H2-08b say the coarser context "leaves the
manufactured rejection untouched". True for the **top** record (the manufactured
record proper), which is what the discriminator is about. But MAN211's
*certified count* vs TOMO is 1, not 0 — the same single record
`[[0,1,2],[3]]`, the sink split, that it certifies against ADDRESS. The counts
table makes this visible; the prose could be misread as "nothing is certified".

## 3.6 Anchor fidelity to Cycle B's constructed boundaries and the #103/#111 fixtures — **ALL REPRODUCED**

Rebuilt the constructed manufactured boundaries from the committed recipe
(exact Pythagorean Givens rotations 3-4-5, 5-12-13, 8-15-17 composed in the
(0,1),(1,2),(2,3) planes; matched dephasing; A_P by exact elimination; retained
sink adjoined):

| quantity | committed | R3 native |
|---|---|---|
| centre dim, manufactured 2+1+1 with sink | 4 | **4** |
| centre dim, manufactured 2+2 with sink | 3 | **3** |
| centre dim, manufactured 1+1+1+1 with sink | 5 | **5** |
| PVM rank multisets | (2,1,1), (2,2), (1,1,1,1) | **identical** |
| rotation unitary; PVM complete | true | **true** |
| atom map carried by (W⊕1)V | [4,0,1,2,3] | **[4,0,1,2,3]** |
| overlap atoms moved by that map | 4 of 5 | **4 of 5** (only w₀ fixed) |
| record lattice sizes n=1..5 | 1,2,5,15,52 | **1,2,5,15,52** |

The centres 4/3/5 and the atom map are exact. The covariance-non-transfer
argument (Thm 6.3) rests on the map moving the overlap, and it does: four of
the five declared address projections are sent to non-diagonal elements.

**Incidences — all seven contexts reproduced elementwise**, matching the
receipt's `incidence` table:

```
ADDRESS    [[0],[1],[2],[3],[4]]           ALIGNED211 [[0,1],[2],[3],[4]]
ERASER     [[0],[1],[2],[3],[4]]           TOMO       [[0,1,2,3],[4]]
MAN211     [[0,1,2],[0,1,2,3],[0,1,2,3],[4]]
MAN22      [[0,1,2],[0,1,2,3],[4]]
MAN1111    [[0,1],[0,1,2],[0,1,2,3],[0,1,2,3],[4]]
```

## 3.7 The deviations appendix (1)–(10), each adjudicated

| # | deviation | adjudication |
|---|---|---|
| 1 | entanglement witness corrected, not merely earned | **FIX-REAL, exemplary.** A pre-registered headline refuted by its own control, demoted in the theorem, the verdict, the receipt's CORRECTED HEADLINE and the abstract. This is the disclosure standard the rest of the paper should meet. |
| 2 | gap = partition inequality, not count difference | **Definition FIX-REAL; justification UNSUPPORTED.** The definition is right and should stay. The stated warrant — a declared task with equal block counts and different partitions — does not exist in the declared family. See **F6**. |
| 3 | `Core(A)⊗Core(B)` = the one-factor-readable splits | **FIX-REAL.** A genuine instantiation choice the pin left open, disclosed, and the right one: it keeps both sides partitions of the same set so the comparison is well typed. |
| 4 | paper-1 model numbers cited, not reused | **FIX-REAL and correctly executed.** I checked all 31 anchors: none claims a paper-1 Bell-model number. L01/L02 anchor #111 objects (rank J(id)=1; ⟨ψ⁻\|J(P)\|ψ⁻⟩ = −1/2), not paper 1's model values. The non-claim at §9 matches. |
| 5 | one candidate slot + one fixed second context | **FIX-REAL, but its consequence is undisclosed.** The reasoning given (with both candidates in one pair neither can be tested) is sound. What is not said is that the "fixed independently declared second context" was then instantiated *as the overlap itself*, which is what makes D2 vacuous. See **F3**. |
| 6 | overlap declared before both | **FIX-REAL, verified** (§3.1). Correctly flagged as permitted-but-not-required, with the right reason. |
| 7 | sharpness control added, not requested | **FIX-REAL, exemplary.** Both limits re-run and reproduced (§3.5), and both are carried into the verdict rather than buried in a control section. |
| 8 | top-of-lattice theorem re-verified natively (160 families) | **FIX-REAL.** 160 = 4 atom counts × 40 seeded draws; measuring the guard's premise inside the unit rather than citing it is the right call. (The closure re-verification itself is R2's primary; I confirm the certified set omits ⊤ for all three manufactured contexts, and the carrier of size 1 with the candidate absent.) |
| 9 | product-law sweep capped at carrier dim 20 (65 of 81) | **FIX-REAL, honestly scoped.** The cap is in the receipt (`carrier_cap: 20, pairs: 65`), the `[PAIR-20]` tag, the claim text and the verdict scope line, with the 16 excluded pairs explicitly carried by the proved lemma. (Lemma reach is R1's primary.) |
| 10 | hostile wing in both orders, five partners | **FIX-REAL, strengthening.** Ten composites rather than the pin's one; costs nothing and closes the promotion question in both orders. |

**Summary:** ten genuine disclosures, no cosmetic padding, and one — (2) — whose
justifying exhibit does not exist. The deviations appendix is the strongest
part of the paper's discipline; the shipped-with-delivery rule is working.

## 3.8 Load-bearing numbers — 19 recomputed, **0 mismatches**

| # | quantity | paper / receipt | R3 native | ✓ |
|---|---|---|---|---|
| 1 | centre dim, constructed manufactured 2+1+1 | 4 | 4 | ✓ |
| 2 | centre dim, constructed manufactured 2+2 | 3 | 3 | ✓ |
| 3 | centre dim, constructed manufactured 1+1+1+1 | 5 | 5 | ✓ |
| 4 | admitted relabellings searched | 120 | 120 | ✓ |
| 5 | carrying isomorphisms, relabelled control | 6 | 6 | ✓ |
| 6 | counter-law admitted sector maps | 120 | 120 | ✓ |
| 7 | counter-law reversible maps | 1 | 1 | ✓ |
| 8 | counter-law records fixed | 52 | 52 | ✓ |
| 9 | ERASER certified vs ADDRESS | 51 | 51 | ✓ |
| 10 | ERASER certified vs TOMO | 1 | 1 | ✓ |
| 11 | MAN211 certified vs ADDRESS | 1 | 1 | ✓ |
| 12 | MAN22 record count | 5 | 5 | ✓ |
| 13 | MAN211 record count | 15 | 15 | ✓ |
| 14 | MAN1111 record count | 52 | 52 | ✓ |
| 15 | identity-overlap positive control certified | 51 | 51 | ✓ |
| 16 | descent-order carrier size | 1 | 1 | ✓ |
| 17 | overlap atoms moved by the carrying map | 4 | 4 | ✓ |
| 18 | ALIGNED211 certified vs ADDRESS | 14 | 14 | ✓ |
| 19 | ALIGNED211 certified vs TOMO | 1 | 1 | ✓ |
| + | atom map | [4,0,1,2,3] | [4,0,1,2,3] | ✓ |
| + | all seven incidence vectors | receipt table | elementwise identical | ✓ |
| + | descent-order maximal element | {{0,1,2},{3}} / {{0,1,2,3},{4}} | identical | ✓ |
| + | the one certified record per manufactured context | sink split ×3 | identical ×3 | ✓ |

**New numbers this review contributes** (not in the paper, all exact):
`|F_eraser| = 2`, `|F_man| = 2`, `|F_address| = 6`,
`max_σ |image(F_eraser)| = 2`, `|facts realized by ADDRESS| = 52 = all
partitions`, `|facts realized by TOMO| = 2`, `records removed by D2 = 0` for
all five contexts, `counter-law gate failures = 4 of 16 ordered pairs`,
`adversarial-pair certified set size = 14`, `variant certified count = 4`.

## 3.9 Common gates

| gate | disposition |
|---|---|
| paper-vs-receipt number sweep (≥10) | **PASS** — 19 + 3 structures, 0 mismatches |
| scope tags everywhere | **PASS** — all 15 numbered results carry `[FIN]` plus the applicable `[PAIR-20]`/`[DECL-8]`/`[ARENA]`; carrier caps printed in receipt and stated at the claim |
| exhaustive vs lemma-carried vs declared distinguished | **PASS** — 65 measured / 16 carried is explicit in the claim, the tag and the verdict |
| forbidden vocabulary | **PASS with one cosmetic** — see F9 |
| no arena-independent selector claim | **PASS** — §8 and §9 both deny it explicitly; the receipt carries it as a NOT EARNED line |
| prose vs gates | **FAIL in three places** — F1 (Prop 5.4 prose implies a discriminating measurement the gate cannot make), F3 (§6.1/§7.1 prose implies D2 is load-bearing when it removes nothing), F6 (§2 and deviation 2 assert a nonexistent exhibit) |
| deviations appendix present and complete | **PASS** — ten, all genuine (§3.7) |
| mutants / determinism / floats | **PASS** — 9 mutants (6 anchor, 3 derivation) with the derivation mutants naming the gates they break, including the discriminator; no wall-clock in receipt or rendered output (timing appears only on the progress stream via `prog()`); I ran my own AST sweep over **both** the unit and the imported predecessor and found **zero float literals and zero `float()` calls in either** — the only `/` operators are pathlib path joins (unit lines 48–49) and exact `Fraction` divisions. The exactness claim is sound, and its scoping ("this unit's own source"; predecessor terminal with its own gate) is honestly stated. |
| paper single-threaded | **PASS** — no correction-round narration; the corrections appear as results (Thm 4.3) and as the deviations appendix, which is the house form |
| anchors exit-1-only | **PASS** — `anchor()` raises `SystemExit(1)` on mismatch (line 274); 31/31 pass |

---

# 4. Per-rung confirmations

**(a) The factorization/support-space lemma, carrier-≤20 + lemma-carried scope
— CONFIRMED as scoped** (lemma reach is R1's primary; not re-proved here). The
65/81 split, the cap of 20 and the 16 lemma-carried pairs are stated at the
claim, tagged `[PAIR-20]`, printed in the receipt and repeated in the verdict
scope line. No leak from measured to carried.

**(b) The corrected witness — CONFIRMED, with F6 attached.** The parity
refutation is real and correctly demotes the pre-registered form: PARITY has
separable rank-two atoms (`atoms_are_product_projections: [false,false]`,
`has_entangled_atom: false`) and opens the gap, so gap-alone is
joint-readability. The correction is carried in Thm 4.3, the abstract, the
verdict and the receipt headline. The *rotated-product* control (PRODROT, gap
closed) genuinely separates "rotated" from "entangled". **But** the
equal-block-count exhibit claimed in §2 and deviation (2) is absent from the
declared family (F6).

**(c) The discriminator both ways at the declared arena — CONFIRMED, reproduced
independently.** Negative: all three constructed manufactured contexts fail
(D1) — `top_transports_without_collision = False` for MAN211, MAN22, MAN1111 —
and each certifies exactly one record (1 of 15, 1 of 5, 1 of 52), in every case
the sink split, "precisely the part of its boundary that was not manufactured".
Positive: ERASER's top transports, fact content is the discrete partition of
the five overlap atoms, and a co-referring record is exhibited. **Caveat:** the
positive direction's force is reduced by F3 — the second context contributes
nothing to it.

**(d) The top-of-lattice guard escape — CONFIRMED.** The certified set omits ⊤
for all three manufactured contexts (recomputed); the carrier is the
pair-plus-overlap structure; the carrier for MAN211 × ADDRESS has exactly one
element, `{{0,1,2},{3}}` / `{{0,1,2,3},{4}}`, and the candidate is **absent**
from it, not merely non-maximal. The Theorem 6.2 proof (fixed-point sets
contain ⊤ by extensivity; the certified set does not) is valid and the escape
is real, not renaming. The covariance obstruction genuinely does not transfer
(4 of 5 overlap atoms moved).

**(e) The measured limits honestly framed — PARTIAL.** The two limits the paper
names (aligned manufacture descends; coarser context withdraws 51→1) are
measured, reproduced exactly, and correctly carried into the verdict. That is
honest work. But a **third** limit of the same kind is unmeasured and unstated:
independence is non-binding at the arena (F1) and D2 is vacuous there (F3).
Two of three limits framed.

**(f) The verdict rungs as correct pre-registered instantiations — PARTIAL.**
`RQ0-L1-COMPOSITE-BOUNDARY` and `RQ0-L1-ENTANGLEMENT-WITNESS` (corrected form)
are correctly instantiated. `RQ0-L1-DESCENT-SELECTOR` is earned **as a fact**
— the selector does reject all three manufactured records and certify the
legitimate one — but its stated scope overclaims what makes it work. It must
be rescoped per §5. `RQ0-L1-SMUGGLING-SURVIVES-DESCENT` correctly does not
occur; F2 does **not** trigger it, since the constructed rotated record still
fails (D1).

---

# 5. Sentences to rewrite

**(1) Abstract, "independence measured, not asserted, by searching all one
hundred and twenty admitted relabellings"** → must not stand. Replace with
something like: *"independence measured under the declared standard law — a
measurement whose two declared families differ in cardinality, so that at this
arena the gate is passed necessarily rather than contingently"*, or drop the
claim from the abstract entirely and let §5 carry it.

**(2) Prop 5.4, "The gate bites. … A gate that could not fail would prove
nothing; this one fails exactly where it must."** → must be split. The control
(equal cardinality) can fail; the arena certificate (2 vs 6) cannot. Add,
adjacent to the certificate: *"At the declared arena the two families differ in
cardinality (2 and 6), so no relabelling could have carried one onto the other;
the certificate is therefore necessary, not contingent, and the control below
establishes only that the gate is capable of failing at equal cardinality."*

**(3) §1.4, Object 2, No-smuggling row, "independence of the two contexts is
measured rather than declared"** → add the qualifier and the limitation: measured
under the standard law, and non-binding at this arena.

**(4) §6.1 / Definition 6.1 (D2), and §7.1** → must disclose F3. Add at the
definition or immediately after §5.2: *"At the arena run here the second
context ADDRESS coincides with the declared overlap, so it realizes every
partition of the overlap and clause (D2) excludes no record that (D1) and (D3)
admit; (D2) is binding only against the coarser TOMO context, where the
positive certificate is withdrawn."*

**(5) §7.1, "The selector fires when it should, and the one exclusion is the
clause that excludes it."** → the identity-overlap control is the headline
computation (F5). Either replace it with a control whose data differ from the
headline's, or state that it is a consistency check, not independent evidence.

**(6) §2, "Section 4 exhibits a declared task where the two partitions have the
same number of blocks and are nevertheless different"**, and **deviation (2)'s
second sentence** → delete or replace. No such task is in the declared family.
Keep the definitional choice; justify it on well-typedness (which deviation (3)
already does) rather than on a nonexistent exhibit.

**(7) Prop 5.5** → add the degeneracy: *"Under that law exactly one isomorphism
is admitted — the identity — so the gate there reduces to the test that the two
declared families are unequal, and has no power to detect a relabelled copy at
all."* Also clarify that the gate searches the 1 reversible map, not all 120
sector maps.

**(8) §8, `RQ0-L1-DESCENT-SELECTOR` scope line** → must gain: relative to the
standard law; independence non-binding at this arena; (D2) inert at this
arena.

**(9) §8, "What is nevertheless not earned"** → must gain a third sentence
naming the adversarial pair: *"Nor is an adversary excluded who declares both
contexts. The independence gate constrains the declared task families, while
descent constrains the boundaries through incidence, and nothing here ties a
declared family to the boundary it presents; a pair of aligned manufactured
contexts passes the gate and certifies a manufactured record. Whether the two
can be coupled is open."*

**(10) §8, "The next obstruction, named"** → the adversarial pair is nearer than
arena-comparison and should be named first, or alongside.

---

# 6. What I did not find

Stated plainly, because a hostile review that reports only hits is not a
measurement:

- **No false numerical result anywhere.** 19 independent recomputations, 0
  mismatches. The one apparent discrepancy was mine.
- **No fabricated anchor.** All six constructed-boundary anchors and the atom
  map reproduce exactly from the committed recipe.
- **No float, no wall-clock, no nondeterminism** — verified by my own AST sweep
  over both modules, stricter than the unit's own (which scopes to its own
  source).
- **No arena-independent selector claim**, anywhere. The paper is disciplined
  about this in §8 and §9 and in the receipt.
- **No spatial reading of "independence"** leaking anywhere. The non-claims are
  firm and the vocabulary sweep is clean but for one negation outside its
  licensed zone.
- **No law-independence leak** — K4's narrow question answers *no* (§2).
- **The escalation outcome genuinely does not occur.** The constructed
  manufactured record fails (D1) in all three cases. The arc should not halt.
- **The guard escape is real**, not a renaming.

---

# 7. Verdict, restated

## ACCEPT-WITH-FIXES

`RQ0-L1-COMPOSITE-BOUNDARY` — no objection from this lens (R1 owns the lemma).

`RQ0-L1-ENTANGLEMENT-WITNESS` (corrected form) — sound; fix F6's unsupported
justification sentence.

`RQ0-L1-DESCENT-SELECTOR` — **earned as a fact, overclaimed as a mechanism.**
The discriminator fires both ways; the guard escape is real; the numbers are
right. But at the declared arena the independence gate could not have failed
and the co-reference clause excludes nothing, so what is actually demonstrated
is that **a collision test at a declared overlap, plus non-vacuity, separates
the constructed manufactured records from the legitimate one** — a genuine and
non-trivial result, and a narrower one than the paper states. Rescope per §5
(items 1–4, 7–10).

`RQ0-L1-SMUGGLING-SURVIVES-DESCENT` — correctly does not occur. F2 does not
trigger it.

The fixes are disclosure and scope, not recomputation. No number needs to move.

---

*R3 review of record. Frozen on delivery.*
