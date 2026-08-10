# R6b′ — HOSTILE REVIEW, REVIEWER R2 (EFFECTUS / STRUCTURAL LENS)

**Object (hashes verified at open and re-verified at close, all six
unchanged):** paper `68c20d1fdae4`, code `8e188dd3ab70`, output
`42a39fcaf194`, receipt `50f63b3ba362`; pin `17111fd19022`; protocol
`1cf5fc8b3272`.
**Reference standards read:** `v14/note-r6a-adjudication.md`,
`v14/paper-04-refinement-grammar.md` (R6a TERMINAL #53) **and the
delivered R6a paper bytes `af5b7f26e427` that this unit's pin was
frozen against**, `v14/paper-06-stochastic-split.md` (CR-B),
`v14/paper-05-accumulation.md` (CR-A), `RUNBOOK.md` + addenda,
`v14/note-gprep-transport-foundation-pin.md` (read-only, as context
for K3), `v14/note-r4-qft-pin.md`, `v14/PLAN.md`, `v14/LOG.md` #56–#58,
and the S1–S6 primaries.
**Recomputations: 738** (of which 400 are the termwise first-return
comparisons; **338** excluding those). Ledger in §8.
**Sources re-derived by my own route, importing nothing from the unit:**
S1's transfer typed by hand from paper 31 §3.3; the record family typed
from the R6a receipt's own `record_family` block; S2's pattern counts
read from `v11/code/u1b_output.txt` lines 81/108.

## GRADE: **ACCEPT-WITH-FIXES**

All four verdict heads reproduce. Every number in the verdict block is
correct at the arithmetic it states. **Zero false numbers in the verdict
string.** But the paper carries **one false result** (F1, in §7's
re-classification table and its gate, outside the verdict block), and
the campaign-critical number's *denominator* is unscoped in a way the
immediate predecessor had already scoped correctly (F2). Six further
findings qualify claims the heads present unqualified.

---

## 1. Findings, ranked

### F1 — FALSE RESULT (HIGH). `NEW-FRONT-VALUES → fiber 1` is wrong; the fiber is ≥ 2, and the two members provably disagree on every record.

The unit re-classes `NEW-FRONT-VALUES` from class (iii)/infinite to
**FORCED-RELATIVE-TO-THE-SPLIT, fiber `1`**, on the rule
front(new) = front(x) + n₁ (paper §7 table; `G-NEW-FRONTS-RECLASSED`;
`G-R6A-RECLASSIFICATION`).

The rule is **left-anchored**. The right-anchored rule
front(new) = front(x+ℓ) − n₂ is expressible from exactly the same
objects — the interval's other endpoint is a coarse site with a
declared front, and n₂ is the same split datum. The two agree at a new
site **iff** front(x+ℓ) − front(x) = n_ℓ(x): the coboundary condition.

Measured: on (ℤ₃)² the front telescopes to `0` around any 3-cycle while
the count sum is a sum of three strictly positive integers. Over the
7 homogeneous admissible records × 3 link directions × 3 cycles =
**`63` cycles, the count sum is nonzero at `63` of `63`** (minimum
cycle sum `3`; the values run `3, 6, 9, 12, 15, 18, 27, 36, 39`). So on
**every** cycle of **every** record at least one of the three new sites
carries a left/right disagreement. The fiber is at least 2 and the two
members are provably separated — the opposite of fiber 1.

This is not a subtlety the unit could not have seen. **The R6a paper
bytes the pin was frozen against (`af5b7f26e427`, §5.3) say verbatim:**

> "The front at a newly inserted site is not determined by the coarse
> record — by §2's no-potential theorem it cannot be."

and the terminal R6a paper (`paper-04`, §5 inventory and §6.3)
sharpens it to a *measured kill*: "the **cumulative front reading**" is
one of the forcings R6a "**rejected**", excluded twice independently —
"by the coboundary theorem *and*, independently, by the declared
independence of the record from the front", with the front declared
"a site-local advance counter, so **nothing relates a new site's
counter to its neighbours'**".

front(new) = front(x) + n₁ *is* the cumulative reading on the left
half. The unit reinstates the reading R6a killed, and the very theorem
it cites to argue the rule is a *third* rule ("it coincides with the
count-weighted interpolation only where the record's counts are a
coboundary, and R6a's gated theorem is that no record's counts are") is
the theorem that forbids it.

Compounding: the paper calls this "**the unit's one clear gain**" and
supports it with "it forces an integer … integral everywhere on this
unit's grid" against "R6a's … lift is non-integral at `30` of its `81`
cells". Integrality here is **definitional** — the receipt itself says
"INTEGRAL at 647 of 647 cells … **by construction**": a sum of two
integers. A definitional truth is set beside a measured falsity as
though the two were comparable measurements.

Also note: **nothing from the six deep rows enters this rule.** It uses
n₁ (R6a's own split datum) and I7's count semantics. Even if it were
sound it would not be a gain *from the enriched type*; it would be a
forcing available at R6a's own type.

**Internal inconsistency it creates.** §5 classes `I-ORIENT`
**stabilizer-fixed**, on the measured ground that the induced position
law is reversal-invariant. Reversal-invariance of the *position law*
says nothing about the *front assignment*, and §7 then derives a front
rule that is **not** reversal-invariant. One unit, one inventory item,
two incompatible classifications.

**Exact repair (binding).** Withdraw fiber 1. Either (a) re-class as
`FORCED-RELATIVE-TO-(THE-SPLIT AND AN ORIENTATION), fiber 2, the two
members separated at 63 of 63 cycles by the no-potential theorem` —
which makes it a *third* class-(iii) entry, i.e. **the enrichment adds
freedom here too**, aligning it with `THE-LIFT-PAIR`; or (b) withdraw
the re-classification entirely and record `NEW-FRONT-VALUES` unchanged
with the predecessor's kill carried verbatim. (a) is the honest and more
informative option. Either way §7's "the unit's one clear gain"
sentence and the integrality contrast retire.

### F2 — SCOPE (HIGH). The `37 of 201` / `37 of 122` denominators count intervals inside records that admit no subdivision at all.

R6a's split fiber for a record is ∏(n_ℓ−1); a single count-1 interval
zeroes it. Rebuilt independently: **`G-ANISO`, `G-CURVED`, `G-FLAT`
have raw fiber `0`** — they "admit no subdivision at all", which is
**stated in those words in CR-B's own paper (§3)**, the unit's own
predecessor. Those three records carry **`60` of the `201` censused
intervals**, of which only 29 are themselves count-1. So `31`
intervals are classified by the kernel as if a split existed to speak
about, and **`10` of the `37` "COLLAPSED-IN-DISTRIBUTION" intervals
(9 in G-ANISO, 1 in G-CURVED) lie in records whose R6a split fiber is
empty.** On those there is no R6a split fiber to collapse.

Scope-corrected, restricted to the 6 records that admit the move:
**`27` of `141` censused, `27` of `103` carrying a non-trivial fiber**
(vs the delivered 37/201 and 37/122).

The unit is demonstrably capable of this care: `G-R6A-FIBER-REBUILD`
correctly excludes `G-CURVOFF` because its fiber "is not determined by
the printed-site data". The same reasoning, applied one section later,
would have caught this.

**Repair.** Print both numbers with their scopes: `37 of 201` as the
per-interval census fact and `27 of 103` as the collapse fact on the
records the move reaches. The `COVERAGE=` segment should carry the
second, or both.

### F3 — MEANING (HIGH). The observable that carries §4 and §6 — "the distinguished interior position" — is a free choice absent from the choice inventory.

C1's statement is "a record interval of count n is a single
inter-renewal leg of LENGTH n; its n−1 interior positions are the n−1
admissible splits". To turn S2's law on *patterns* into a law on
*splits* one needs a map patterns → positions. The unit uses "the slot
carrying the unique non-proposal event" (`G-S2-PATTERN-POSITION-MAP`).

That map is a construction of this unit. It is not in any pinned row,
and — decisively — **the unit's own type census proves it has no
referent**: an inter-renewal leg contains exactly one division event
(the terminating `r`), so there is no "a-th division event" inside a
leg for a split to sit at. The unit names the type error and then
builds the split-position law across it anyway.

The inventory (7 items for C1) registers `I-TYPE`, `I-LINK`, `I-SITE`,
`I-ORIENT`, `I-POSITION`, `I-SCOPE`, `I-BASIS`. **It has no item for
the pattern→position reading.** Every number in §4 and §6 —
`2/63`, the uniform delivery-free law, the collapse at count 4, the
CR-B simplex `2 → 0`, the `37` — is downstream of it. Under the
alternative "read no distinguished slot" the transport law is uniform
too and `2/63` becomes `0`.

This does not flip `UNMOTIVATED` (C1 already has 3 free items). It
qualifies **KERNEL-DERIVED**: the collapse is derived *at* an
unregistered reading, and the unit's motivation instrument — which is
the whole point of the RSQ standard — did not weigh it.

**Repair.** Add `I-READOUT` ("which pattern-derived observable is the
split") to C1's and C4's inventories, classed FREE with its evidence
(the type census is the evidence), making C1 `forced 3 / stabilizer 1 /
FREE 4`. The verdict's `FREE-ITEMS=` and `DECISIVE=` fields update
accordingly.

### F4 — MEANING (MODERATE-HIGH). The "delivery-free" positional law is a *conditional of the transport census*, not a delivery-free measurement.

`G-POSITION-INDEPENDENCE-AT-DELIVERY-FREE-SCOPE` computes its law by
"the delivery-bearing patterns are deleted" from S2's transport-scope
leaf counts and renormalising. That is the transport law **conditioned
on no delivery occurring**, carrying transport branching weights. It is
not the census the delivery-free grammar would produce.

Evidence that the conditioning is non-trivial: the retained mass is
**`3/7` at leg 1 and `1/3` at leg 2** — the conditioning events have
*different* probabilities at the two cells, so the two conditional laws
coincide (both uniform) as laws conditioned on different events. The
paper prints the retained fractions (honest) but then states the result
as "**At delivery-free scope** it is exactly uniform at both censused
positions" and stamps `SCOPE=DELIVERY-FREE` on the collapse head.

Mitigation, which should be stated: the retained *pattern set*
(`nppr`, `pnpr`, `ppnr`) is exactly the pattern set a delivery-free
length-4 leg admits, so only the weights are transport weights, and the
three are equal in both cells. The result is robust to any reweighting
that keeps them equal — which is unmeasured.

**Repair.** Rename the measurement `NO-DELIVERY-CONDITIONAL` (or
`DELIVERY-FREE-SUB-ENSEMBLE-OF-S2`) throughout, and state in one clause
that the weights are transport weights and the equality of the three
retained patterns' weights is what carries the uniformity.

### F5 — UNSOUND ARGUMENT (MODERATE). The det-blindness leg of the extremal kill does not establish what it is said to establish, and contradicts the arena's own admissibility predicate.

§8: "The **record-intrinsic test** fails at a second, independent
point. … `I = q⁻¹(det q)^w` at `w = 0` … so the declared readout is
det-blind. Max-det optimises a functional **the declared record does
not read**."

Two problems. (i) **Terminological self-contradiction**: three
sentences earlier max-det is one of "`4` record-intrinsic functionals —
each computed from the record alone". It cannot both be record-intrinsic
and fail the record-intrinsic test. (ii) **Substantively false as
stated**: det q *is* computed from the record alone — q is reconstructed
from the three counts (q₁₁ = n₁, q₂₂ = n₂, q₁₂ = (n₃−n₁−n₂)/2) — and
the arena's **admissibility predicate is positive-definiteness, which
is exactly q₁₁ > 0 ∧ det q > 0**. The declared record reads
sign(det q) at every site. Verified: at the (2,2,4) site the three
splits give det = `3/4`, `1`, `3/4`, all record-computable.

What w = 0 actually says is narrower and true: det does not enter the
declared *density* readout I. That is a fact about the density weight,
not about record-intrinsicality.

The verdict is unaffected — the bar still dies twice over (F6) — but
one of three named legs is unsound and one of them contradicts CR-B's
declared arena.

**Repair.** Replace with: "det enters the declared readout only through
the admissibility predicate's sign, never through the density weight
(w = 0); a functional the arena reads only by sign is not thereby a
selector of magnitude." And drop "the record-intrinsic test fails".

### F6 — ADJUDICATION (MODERATE). The extremal bar's three kills are given in the wrong order of strength; the decisive one is the one R6a's own lead named.

R6a's reopening lead (ii) registered the criterion in advance:
"max-det selects uniquely 9-of-9 on all six splittable records —
**motivated iff a deeper row declares a variational principle**". The
unit measured `0 of 6`. **That alone discharges the lead by its own
pre-registered condition**, and it is the D12-correct kill: D12's bar
is that "the frozen SHARD premises **plus Q**" must have one class —
max-det passes the uniqueness half (it *does* select) and fails because
**Q is an added premise, not a consequence**, i.e. D12's "selects one
member of a preselected toy family" / "chooses a coefficient after its
support, reference measure, modes, and constraints have been supplied".

See K4 for the full adjudication of whether 3-of-4 is the right kill.

### F7 — CONFOUND, UNDISCLOSED (MODERATE). "Chain-position dependent" rests on two cells drawn from two *different* declared ensembles at two *different* depths.

The leg-1 profile is E2's first cut interval (renewals at 3, 7, 10;
depths 3→7); the leg-2 profile is E3's second (renewals at 3, 6, 10;
depths 6→10). Ordinal position, absolute depth and ensemble identity
move together across the only two data points. The attribution
"chain-position dependent" is one of three readings and the data cannot
separate them.

The unit caps the *delivery-free* claim ("measured at two positions,
not proved at all", §12) but leaves the *transport* claim — the one
carrying the confound and the one in the verdict
(`TV-BETWEEN-CHAIN-POSITIONS-TRANSPORT=2/63`) — uncapped. Asymmetric
disclosure.

**Repair.** One clause in §4 and a `CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2`
qualifier on the TV segment.

### F8 — MECHANISM UNDER-STATED (MODERATE, and it is a *gain*, not a defect). The transport-scope non-uniformity has an exact one-line cause the paper does not print.

Of the six combinatorial possibilities (3 interior slots × {delivery,
idle}), S2 realises **five**: `dppr`, `nppr`, `pnpr`, `ppdr`, `ppnr`.
The missing one is **`(p,d,p,r)` — a delivery in the middle slot**.
Positions 1 and 3 each admit {d, n}; **position 2 admits only {n}**.
That single exclusion *is* the entire transport-scope position
dependence, and deleting the d-patterns restores exactly one pattern
per position, hence exactly uniform.

The chain-position dependence has a second, separable cause: the
delivery multiplicity per slot is `1024/512 = 2` at leg 1 and
`24576/8192 = 3` at leg 2 — one more deliverable message in flight —
which moves (3/7, 1/7, 3/7) → (4/9, 1/9, 4/9) and would push the family
toward (1/2, 0, 1/2) as the multiplicity grows.

This converts "the position dependence is a delivery effect" from a
correlation into a **structural statement**, and it is the single most
transportable thing this unit measured. It also makes the count-5
question *posable*: the answer is "which interior slots of a length-5
leg admit a delivery", which is a question about `d42b1` — Γ-prep's own
T1 row — not about S2.

**Repair.** Print it. Two sentences in §4 and a segment
`MIDDLE-SLOT-ADMITS-NO-DELIVERY` on the SEAM head.

### F9 — PROVENANCE (MODERATE). The "two genuinely independent routes" to S1's chain are two *transcriptions*, not two *derivations*.

Route P parses paper 31's fenced block; route C AST-extracts
`d43b`'s `T_REF` — a **hard-coded reference literal** in that file
(`d43b:153`), not the computed `rows` object that d43b's own gate
checks against it over 215 histories. Both routes read an authored
constant. I confirmed they agree (26 entries), and I confirmed the
constant is right by typing it independently — but a shared
transcription error would pass both routes silently.

`G-S1-ROUTE-PROVENANCE` correctly invokes #219 ("a comparator routed
through the component under test would verify nothing") and correctly
notes distinct artifacts and formats. What it establishes is
**transcription fidelity across two artifacts**, which is worth having;
what the pin asked for was "S1's chain re-derived by a second route".
The genuine second route was available: `d43b`'s `rows` object, built
from `CACHE`/`CLS` by the bisimulation, gated at 215 histories.

**Repair.** Relabel the gate `TWO-INDEPENDENT-TRANSCRIPTIONS` and add
one sentence naming `rows` as the derivation the unit did not run and
why (cost / d43b is TERMINAL and gates it itself).

### F10 — PROSE OVER-CLAIM (LOW-MODERATE). "No functional of the derived law names a split" is false at transport scope.

`G-COLLAPSE-IS-DISTRIBUTION-NOT-VALUE` measures **maximisers**. At
transport scope the law is (3/7, 1/7, 3/7): argmax ties on {1, 3} but
**argmin names `2` uniquely**. "Minimum-probability split" is as much a
functional of the derived law as "maximum". The gate's kill criterion
(count the maximisers) is narrower than the prose claim (no functional).
At delivery-free scope the sentence is true by uniformity.

**Repair.** "No *maximising* functional of the derived law names a
split; at delivery-free scope the law is uniform so no functional of it
does."

### F11 — SEGMENT SEMANTICS (LOW-MODERATE). `SUPPORT-HOLE-AT-2-COSTS-50-OF-201-INTERVALS` costs nothing, and its true content is stronger than "cost".

A count-2 interval has fiber `1` — a single admissible split. There was
nothing to collapse; the unit's own denominator (`122` = counts ≥ 3)
correctly excludes them. So the hole "costs" zero collapse.

The hole's real content is the *opposite* of a gap: under C1 read as a
law, a length-2 leg has probability exactly `0`, so the pushforward
assigns measure zero to **`50` of the `201` declared intervals (24.9 %
of the arena)** — a **refutation of C1 on a quarter of the arena**,
strictly stronger than "3 free items". The unit does not draw it,
presumably guarded by §4's "no frequency in this paper is read as a
kernel probability" — but that disclaimer is about S2's leg lengths,
and if it is extended to cover the arena's counts then the `COSTS`
segment is itself a cross-reading the paper forbids.

**Repair.** Pick one. Either `SUPPORT-HOLE-AT-2-REFUTES-C1-ON-50-OF-201`
(the strong, and I think correct, reading, with the disclaimer scoped),
or drop the segment and state in §6 that count-2 intervals carry fiber 1
and are excluded from the collapse question on that ground alone.

### F12 — DENOMINATOR CARRIED FORWARD UNSCOPED (LOW). `30 of 81`.

The R6a adjudication's repair order 7 explicitly requires "`30 of 81`
**scoped to its record×rule cell**". The R6a receipt carries
`/forced_front_lift/record = G-ANISO2` and
`/cell_shape = "(front, site, link) at one record and one split rule"`.
Paper §7 reproduces "non-integral at `30` of its `81` cells" with the
record and rule unnamed. The unit does add "The two grids are different
objects" and forms no ratio — partial compliance. (Strictly the order is
a repair order on R6a, not a RUNBOOK engraving, so the #313 propagation
compliance row is not violated.) Retires with F1 in any case.

### F13 — DISCLOSURE (LOW; instrument's call). The never-falsified census covers 46 of the 48 gates.

`G-WAIVER-CENSUS` runs over `GATES` as registered at that moment (46);
`G-WAIVER-CENSUS` and `G-GATE-COUNT` are the 47th and 48th. Paper §13
prints "`48` must-pass gates, `0` failures … Never-falsified census:
`0` unwaived" adjacently, reading as coverage of all 48. Structural
self-reference, benign, but undisclosed. Deferred to R3.

---

## 2. What reproduced (the credit side, measured)

Everything below I rebuilt from the primaries with no import from the
unit, and it agrees exactly:

- **S1's chain end to end.** Row sums (2,2,2,5/2,2,2); T f = 2 f at
  f = (4,4,3,7,3,3)/3; q′ = T_ij f_j/(2 f_i) normalises on all six rows;
  the conflict row {0: 1/7, 3: 3/4, 5: 3/28}; all 18 nonzero entries.
- **The defective-renewal arithmetic.** Communicating classes {0,1,3}
  transient / **{2,4,5} closed**; hitting probabilities h(1) = `1/4`,
  h(3) = `4/7`, `0` on the closed class; **return `13/16`, defect
  `3/16`**; visits `16/3`; defective mean `21/16` (I re-derived it in
  closed form: 3/4 + (112+32)/256 = 21/16); conditional mean `21/13`.
- **The first-return law, both routes.** Taboo iteration of q′ to
  n = 400 agrees with (n−2)(3/4)^(n−3)/256 **termwise at all 400
  terms**; f(1) = 3/4, **f(2) = 0 exactly**, f(3) = 1/256, f(4) = 3/512,
  f(5) = 27/4096; mass `13/16` with residual `1.18e-49` < 1e-40.
- **The arena.** `201` intervals; the count census
  {1:29, 2:50, 3:20, 4:37, 5:27, 6:10, 9:9, 10:1, 12:9, 13:9}; `122`
  with count ≥ 3; **`647` = Σ(n−1) over all 201 intervals**; **`67` =
  (record, site) readout cells**; the record family matches the terminal
  R6a receipt at 11 of 11 records and 44 of 44 fields.
- **S2's laws.** (3/7, 1/7, 3/7) and (4/9, 1/9, 4/9); TV = **`2/63`**;
  the no-delivery conditionals uniform at both cells, TV = **`0`**;
  retained mass 3/7 and 1/3; reversal-invariance at all three cells.
- **The S5 comparator.** Binomial (2/7, 3/7, 2/7) from
  C(4,a)/14; TV vs uniform = **`2/21`**, and CR-B's receipt carries
  `tv_uniform_vs_binomial/4 = "2/21"` — the cross-unit reproduction is
  real.
- **G-DIAG2's coverage.** Raw = admissible-at-image = 3 per site,
  3⁹ = **`19683`**, and G-DIAG2 is the **only** record of the six where
  raw = admissible (see K2 for what that costs the claim).
- **The extremal countermodel.** MAX-DET → [2], MAX-BALANCE → [2],
  MAX-LEFT-COUNT → [3], MAX-|q₁₂| → [1,3]: **4 functionals, 3 distinct
  selections**, exactly as printed.
- **The fiber rebuild's care.** Raw fibers agree at 8 of 8 and the
  exclusion of `G-CURVOFF` (no count-1 interval among its printed sites
  ⇒ fiber not determined) is correct and well-reasoned.
- **The cover dissolution.** Sound: rooted, depth-non-stationary arenas
  carry no deck group; 0 of 6 rows pin a cover object.

The unit's exact arithmetic is clean. **I found no arithmetic error
anywhere.** Every finding above is about *meaning* — what a correct
number is a number *of*.

---

## 3. K1 — the kernel's status, against the RSQ/R1 motivation standards

**Verdict: the kernel is DERIVED-FROM-PINNED-LAW, and the era's first
such closure is real — but two of its three headline numbers are
convention-relative and the unit does not say which.**

I applied the unit's own motivation standard to its own construction and
separated support facts from convention facts by re-running the chain
under two alternative normalisations with identical support
(row-normalisation; uniform-on-support):

| fact | h-transform (pinned) | row-normalised | uniform-on-support | status |
|---|---|---|---|---|
| closed class {2,4,5} | yes | yes | yes | **LAW (support)** |
| renewal state transient | yes | yes | yes | **LAW (support)** |
| P(return) < 1, terminates a.s. | yes | yes | yes | **LAW (support)** |
| **f(2) = 0 exactly** | yes | yes | yes | **LAW (support)** |
| P(return) | `13/16` | `25/32` | `7/12` | **CONVENTION** |
| visits | `16/3` | `32/7` | `12/5` | **CONVENTION** |
| f(1) | `3/4` | `3/4` | `1/2` | **CONVENTION** (coincidence at row 0) |
| f(n) for n ≥ 3 | (n−2)(3/4)^(n−3)/256 | different | different | **CONVENTION** |

The completed-chain convention q′ = T_ij f_j/(2f_i) is the Doob
h-transform at the Perron root, and it **is** pinned (paper 31 §3.4,
"The completed transfer", TERMINAL). So the unit imports no *undeclared*
choice here — the convention is S1's, carried correctly. What the unit
does not do is **separate what survives the convention from what does
not**, and the two facts it leans on hardest fall on opposite sides:
`f(2) = 0`, the support hole, is a genuine law of the pinned structure
(there is no length-2 path 0 → j → 0 because T(1,0) = 0), while
`13/16` is a number of the h-transform.

**The first-return reading.** q′(0→0) = 3/4 is a self-loop at the
quiescent class, and the unit counts it as a return, so f(1) = 3/4 and
"most inter-renewal legs have length 1". Whether a quiescent step is a
renewal is a semantic question S1 does not settle; the unit does not
raise it. It is inert for everything downstream (all §4/§6 work happens
at lengths 3 and 4) but it should be disclosed in one clause, because it
is exactly the kind of convention the era's inventory discipline exists
to surface.

**Purity, other imports.** State ordering: inert (I permuted nothing but
verified the class decomposition by transitive closure rather than by
label order — same answer). No other undeclared choice found in §3.

**Two-route independence:** see F9 — transcription, not derivation.

**A structural note that matters for how the head should read.** §3's
kernel (leg lengths, from S1, delivery-free) and §4/§6's positional
profile (interior slots, from S2, transport) are **two different
objects**. The collapse at count 4 is produced entirely by S2's leaf
counts; S1 contributes only the hole at 2 and the defectiveness. The
verdict head welds them: `KERNEL-DERIVED<…|LAW=FIRST-RETURN-…|COLLAPSE=
DISTRIBUTION-UNIFORM-AT-COUNT-4|…>` names the first-return law as `LAW`
and the collapse as its consequence, when the first-return law does not
produce the uniform-at-4 distribution. §6's class table *is* honest
about the per-class source; the head is not.

---

## 4. K2 — the fiber-collapse claim, and the qualifier grading

Each of the four qualifiers graded as **LAW of the pinned structure**
vs **ARTIFACT of S2's census**, with the evidence:

| qualifier | grade | evidence |
|---|---|---|
| **DISTRIBUTION-only** (never a value) | **LAW**, at the pinned rows | The derived law is reversal-invariant at all three measured cells (verified), and it is not a point mass. Any reversal-equivariant functional therefore ties. The *stated* form ("no functional") over-claims — see F10 — but "no equivariant functional names a split" is a law of the measured law, not a census accident. |
| **count-4-only** | **SPLIT VERDICT — one half LAW, one half ARTIFACT** | *Count 3's emptiness is a LAW*: S2 measured that a renewal three events after a renewal **forces** `(p,p,r)` and nothing else (u1b's X2 gate, 453,632 unpruned continuations, one pattern), so the pattern class distinguishes no interior position at length 3 — a grammar fact, not a census cap. *Count ≥ 5's silence is an ARTIFACT*: S2 censuses lengths 3 and 4 only, because it censuses what its cut triples require. Count 4 is the smallest length at which a nontrivial interior structure exists, and it is not the largest at which one could. |
| **delivery-free-only** | **ARTIFACT of the unit's own construction, over a LAW of the pinned rows** | The seam (two rows, two scopes, S1 declaring the class structure unstable across it) is real and pinned. But the *number* stamped `SCOPE=DELIVERY-FREE` is a conditional of the transport census (F4), not a delivery-free measurement. The qualifier names a scope the unit never measured in. |
| **37 of 201 / 37 of 122** | **ARTIFACT (denominator), LAW (numerator)** | The numerator is a correct census fact. Both denominators include 60 intervals in three records that admit no subdivision (F2). The scope-corrected figures are **27 of 141** and **27 of 103**. Additionally the two inhomogeneous records enter at 2 of 9 sites (a declared cap, correctly declared). |

**"Would the collapse extend or die at count 5?"** — **Blocked at
citable scope, and the blocking fact is now nameable.** S2 does not
reach length 5; `u1c` (the depth-15 row that would) is
GREEN-UNREVIEWED / NOT CITABLE and the unit registers it correctly as a
lead with its status printed. But F8 makes the question *precise* rather
than merely open: the count-4 non-uniformity is caused by **one
exclusion — no delivery in the middle interior slot**. At length 5 the
question is which of four interior slots admit a delivery, and that is a
question about the `d42b1` committed layer (Γ-prep's T1), not about S2.
**Measurable at citable scope by a successor that pins T1; blocked for
this unit.** Say so.

**The two sharpening measurements, audited.**

*G-DIAG2's complete coverage.* True and correctly computed (3⁹ =
19683, raw = admissible). But the claim "That is the law CR-B classed
REFUTED-AS-FORCING for want of a declared support — and the support is
now derived rather than chosen" earns less than it sounds. CR-B's
objection was that the raw and admissible-at-images supports "give
measurably different laws at **five of the six** records that admit the
move". **G-DIAG2 is the sixth** — the one record where the two supports
coincide, verified here: raw = admissible = 3 per site at G-DIAG2 and
raw ≠ admissible at all five others (221/288, 3/5, 20/36, 3/5, 54/88,
23/24). So the unit's complete-coverage record is exactly the record
where the predecessor's objection was already vacuous.

*And the derived law is not admissibility-consistent off G-DIAG2.* The
derived kernel is per-interval and factorises; admissibility couples the
three links at a site. Measured, at the three records carrying count-4
intervals inside movable records:

| record | derived marginal on the count-4 link | admissible-uniform marginal |
|---|---|---|
| G-DIAG2 (2,2,4) | (1/3, 1/3, 1/3) | (1/3, 1/3, 1/3) — **same** |
| G-ANISO2 (4,9,13) | (1/3, 1/3, 1/3) | (59/221, 76/221, 86/221) — different |
| G-OFFNEG (3,5,4) | (1/3, 1/3, 1/3) | (7/23, 8/23, 8/23) — different |

So CR-B's own "the uniform law on the admissible fiber fails to
factorise" finding recurs one level down: the derived law selects a
point of CR-B's *per-interval* simplex (correct, and the `2 → 0` claim
is right at that level) but is not the marginal of any uniform law on
the *record's* admissible fiber except at G-DIAG2. Worth one sentence;
it is not a defect of the measurement, it is the scope of it.

*The CR-B simplex `2 → 0`.* Verified against CR-B's own criterion: at
n = 4 the pinned group acts trivially on 3 splits, dimension n−2 = 2;
under the flip, dimension 1; the derived law is flip-invariant and
selects the uniform point. Correct as stated, **at one interval**. It is
not a statement about a record's simplex (G-ANISO2's is
139729451328658254140-dimensional and the derived law touches one of its
three coordinates).

---

## 5. K3 — the defective renewal, THE SEAM, and the Γ-main pin

### (a) The termination arithmetic

Reproduced exactly (§2). Return `13/16`, closed class {2,4,5}, visits
`16/3`, hole at 2, and the a.s.-termination statement. Delivery-free
scope carried at every headline — correctly, and S4's verbatim
`[THEOREM at two-actor delivery-free scope]` tag is real. The one
correction is the law/convention separation in K1's table, and F11 on
what "costs 50 of 201" means.

### (b) The seam's ontological status — the central question

**Adjudication: the seam is genuine, it is deep, and the paper names the
wrong cause for it.**

*Not an artifact of the pin's row selection.* One could ask whether a
single-scope row set was available. It was **not**, for a measured
reason the unit does not cite: paper 32 §2.3 [EXACT] establishes that
the transport-scope window chain **ESCAPES** — 68 transitions from
shallow parents land in 5 classes first realised at length 3; menu-shape
factorisation fails; 0 of 3,969 transport menus match any delivery-free
menu shape. **There is no transport-scope analogue of S1's 6×6 chain to
pin.** The delivery-free chain is pinnable because it closes; the
transport chain is provably not bounded-abstractable at feasible caps.
So the seam is not a bookkeeping accident — it is the shadow of the
escape.

*But the paper attributes it to provenance.* `R6BP-BLOCKED-AT-THE-
SCOPE-SEAM<S1-DELIVERY-FREE|S2-TRANSPORT|…|S1-DECLARES-THE-CLASS-
STRUCTURE-NOT-STABLE-ACROSS-IT>` says: two rows, two scopes, one
declaration. That reads as row selection. The true statement is
stronger and is available from an already-terminal source: *the
transport-scope chain cannot be pinned because it escapes.* Fix the
segment.

*And the deep half of the seam is intra-S2, not cross-scope.* The
paper's best result — "the entire position dependence is carried by the
delivery-bearing patterns" — is a decomposition **within one row, at one
scope**. No scope crossing is required to obtain it. The seam blocks the
*composite kernel*; it does not block the *finding*. The paper locates
its own strongest measurement inside the head that reports a blockage,
where it reads as a caveat rather than as the result it is.

**So: is the position-dependence a deep fact (interaction generates
positional structure) or scope bookkeeping? DEEP** — and F8 gives the
mechanism: **a delivery cannot occupy the middle interior slot.**
Interaction (delivery) is admissible at the ends and inadmissible at the
centre, and that single asymmetry is the whole of the transport-scope
positional structure. Switch interaction off and the stage is exactly
uniform and exactly position-independent. That is not bookkeeping. It is
the smallest measured instance in this corpus of *interaction writing
positional structure onto a stage that has none without it.*

**Does Γ-prep dissolve or confirm the seam? BOTH, and the split is
clean.** Γ-prep pins T1–T8, all transport scope, and terminalizes the
transport-scope foundation. Once it delivers:

- **The seam as a blockage DISSOLVES** for anything built on Γ-prep's
  rows: a transport-scope successor needs no delivery-free row at all,
  and S2 is already at transport scope (`d42b1` — Γ-prep's own T1).
- **The seam as a measurement is CONFIRMED and becomes the substance**:
  the delivery-bearing/delivery-free decomposition is now an
  intra-arena statement about Γ-main's own arena.
- **The seam as an obstruction to a transport-scope *chain* persists**,
  because the escape is terminal-negative. Γ-prep says so in its own
  scope-honesty section ("this unit does NOT re-pose it").
- One honest qualification against the unit: R6b′ excluded d70 as
  "round-1-repaired, NOT terminal", and the Γ-scout established that
  this was a **stale header** — d70 is TERMINAL-AT-ONE-HOSTILE-ROUND
  per v10 LOG #489 (verified). So part of the row selection *was*
  documentation lag. It does not change the verdict, because d70
  supplies horizon kernels, not an interval-positional law, and the
  escape blocks the chain regardless. The pin's own note that "the
  transport-scope arm is a possible follow-up pin" was the right call
  for the wrong stated reason.

### (c) The Γ-main pin — my recommendation

**Recommended verdict structure (four heads, each answering about one
object, with the referent named in the head):**

1. `GMAIN-CONSTRUCTED-<the object; the grain; the arena declared>` /
   `GMAIN-BLOCKED-AT-<named fact>` — the construction, first-class both
   ways.
2. `GMAIN-REQUIREMENTS-<met/unmet/unposable, per requirement>` — computed
   against the three pre-registered lists (CR-B's interval-positional
   kernel; CR-A's geometry-update law; **R6b′'s seam**). Each
   requirement's status computed in-gate, never asserted.
3. `GMAIN-MOTIVATION-<the choice inventory on the construction itself>`
   — the RSQ standard applied to Γ's own construction, **with an
   `I-READOUT`-class item** (F3's lesson: register the observable, not
   only the arguments).
4. `GMAIN-SCOPE-<what the construction is relative to>` — grain,
   cap, completion, and the escape's status.

**Two structural lessons from R6b′ that should be pin text, not
inherited habit:**

- **Do not weld an identification-free result to an
  identification-relative one under one head** (K1's closing note). If
  Γ is constructed without an identification, its construction head must
  not carry a coverage claim that needs one.
- **A verdict segment must carry the restriction that makes it true.**
  R6b′'s heads drop the ensemble-data qualifier, the two-site cap, the
  "at two censused cells" qualifier, and the unmotivated status of the
  identification named in its own KERNEL-DERIVED head (K5).

**Anchors Γ-main should inherit from R6b′ (with their grades):**

| # | anchor | grade | why it binds Γ-main |
|---|---|---|---|
| A1 | **The type census**: n_ℓ counts division events; an inter-renewal leg contains **exactly one**. | LAW | Kills count-match-length as a type-honest reading for Γ too. Any Γ claiming to be "the interval-positional kernel" must say which of the two objects its index is. |
| A2 | **A delivery cannot occupy the middle interior slot** of a length-4 leg; this single exclusion is the entire transport-scope position dependence; the delivery multiplicity is 2 at leg 1 and 3 at leg 2. | LAW (measured, F8) | **This is Γ-main's first falsifiable target.** S2 is at transport scope — Γ-main's own scope. A correct Γ must **reproduce (3/7, 1/7, 3/7) at leg 1 and (4/9, 1/9, 4/9) at leg 2**. Pre-register it. |
| A3 | **f(2) = 0** as a support-level law; defectiveness as a support-level law; `13/16`/`16/3` as h-transform numbers. | LAW / CONVENTION split (K1) | Γ-main must **not** try to reproduce 13/16 — see the relationship below. |
| A4 | `0 of 6` pinned rows declare a variational principle; S6 refutes the class. | LAW (prohibition) | Γ-main may not smuggle an extremal selector to close a fiber. |
| A5 | Cover DISSOLVED: deep arenas rooted and depth-non-stationary, no deck group. | LAW (prohibition) | No cover-lifting route to a canonical Γ. |
| A6 | **The lift freedom GROWS under enrichment** (a third rule). | LAW | The corpus's counter-intuition: importing a deeper layer can *add* freedom. Γ-main should pre-register that its freedoms may grow and measure it either way. F1 says the front entry grows too, so this is 2 of 4, not 1 of 4. |
| A7 | Γ(cut3←cut1) is column-constant at all 176 maps ⇒ DIVISIBLE forced at renewal-cut grain (u1b, and the scout's headline 4). | LAW | **Γ-main must work at a finer grain than renewal cuts, or its object is dead on arrival.** R6b′ reinforces this from the other side: the positional structure lives *inside* the leg, never at the cuts. |
| A8 | **Do NOT inherit**: `37 of 201` as a coverage claim; the `SCOPE=DELIVERY-FREE` stamp on the collapse; the det-blindness argument; `NEW-FRONT-VALUES` fiber 1. | — | F1, F2, F4, F5. |

**The honest relationship between R6b′'s kernel and the transport-scope
Γ (this is the part the pin most needs to say plainly):**

> **Γ does not extend R6b′'s kernel. It replaces one half of it and
> inherits the other half whole.**
>
> R6b′'s kernel is a composite of two halves at two scopes. Its
> **S1 half** — the leg-length law, the closed class {2,4,5}, the defect
> 3/16 — is *delivery-free*, and the pinned corpus declares that
> transport **removes** its central feature: paper 31 §3.5, quoted in
> the unit itself, says "deliveries **reopen the absorbing sector**
> (diverged holdings can reconverge), the class structure of §3.2 is not
> stable under the transport grammar", and paper 32 §2.3 measures the
> reopening exactly (1,044 diverged histories; 124 reconverging pairs
> over 84 prefixes; 4 minimal chains at weight 1/256). **The
> defectiveness is a delivery-free artefact that transport is measured
> to undo.** Γ-main must therefore treat `13/16` as a **control to
> contrast against**, never a target to recover; recovering it would be
> evidence the construction had lost the deliveries.
>
> Its **S2 half** — the interior-position profiles — is already at
> transport scope, which is Γ-main's own scope. That half transfers
> whole, and it is Γ-main's first pre-registered agreement test (A2).
>
> So the derived kernel here is best read not as a first approximation
> to Γ but as **Γ's delivery-free shadow**: the same arena with
> interaction switched off, where the positional law is exactly uniform,
> exactly position-independent, and the renewal chain terminates. That
> contrast — uniform and terminating without interaction; non-uniform
> and (measured) reopening with it — is the single most useful thing
> R6b′ hands Γ-main, and it is worth more than the collapse coverage.

**On the U3 screen and D74's quotient.** Γ-prep carries T5's curvature
group ⟨2,3⟩ "as an anchor, not interpreted". My recommendation for
Γ-main's pin: **make the interpretation a pre-registered gate.** If
Γ(cut′←cut) is constructed on D74's committed quotient, its holonomy
must be *measured* and *compared* to ⟨2,3⟩. Agreement is the claim that
the geometry-update slot's measured occupant and the constructed law are
the same object; disagreement is a first-class negative and must be
statable before the construction runs. Without that gate, "Γ-main
lands" is unfalsifiable at exactly the joint where the campaign's stake
sits.

---

## 6. K4 — the composed heads, the re-classifications, the extremal bar

### The four heads' mutual consistency

**Consistent, but not four coordinate results.** The composition is
really:

- **one identification-free positive result** — the first-return law and
  the defectiveness, derived from S1 alone (KERNEL-DEFECTIVE, and the
  `LAW=` field of KERNEL-DERIVED);
- **one negative result that dominates** — TRANSPORT-UNMOTIVATED and
  BLOCKED-AT-THE-SCOPE-SEAM are **one head, not two**: the verdict's own
  `DECISIVE=I-SCOPE-AND-I-POSITION` says the decisive free item *is* the
  seam, and the SEAM head is that item's evidence;
- **one conditional** — the collapse, which holds *at* an identification
  the dominant head declares unmotivated.

**So yes, one head dominates**, and the paper's own closing sentence
("The stratum exists. Its transport does not.") states it correctly. But
§11's five-clause summary presents the clauses as coordinate when the
fifth conditions the third and fourth. The right final message is the
one the paper almost writes:

> *The stratum exists and is derivable without any identification. Its
> transport requires one, and none is motivated — because the two rows
> that would jointly supply the positional law live at different scopes,
> and the corpus has measured why no single-scope row set exists.*

That formulation also fixes F1's framing damage: with the front
re-classification withdrawn or corrected, **the enrichment adds freedom
at 2 of the 4 R6a entries and removes it at 0** — which is the honest,
and more striking, headline.

**Repair to the heads.** `KERNEL-DERIVED<IDENT=C1-COUNT-MATCH-LENGTH…>`
should read `IDENT=C1-COUNT-MATCH-LENGTH-UNMOTIVATED`, so the head is
self-carrying under the era's composability doctrine.

### The R6a re-classifications

| entry | delivered | my adjudication |
|---|---|---|
| THE-SPLIT → (ii)-in-distribution, count-4, delivery-free, 37/201 | correct in arithmetic | **Correct in kind**, qualified by F2 (denominator), F3 (unregistered readout), F4 (scope label). Scope-corrected: 27 of 103. |
| FREE-TRANSVERSE-LINKS unchanged, 0 of 54 | correct | **Sound, and the reason given is the right one** — "an enrichment indexed by interval counts has no index at all for a link that lies on no interval" is a genuine structural statement, not an accident. Credit. |
| **NEW-FRONT-VALUES → forced, fiber 1** | — | **FALSE (F1).** Real forcing or definitional? **Neither, as stated**: it is definitional *given an unregistered orientation choice*, and it is *excluded* by the predecessor's no-potential theorem in the version the pin froze against. Correct classification: fiber ≥ 2, members separated at 63 of 63 cycles. And it uses none of the six deep rows, so it is not a re-classification *at the enriched type* at all. |
| THE-LIFT-PAIR unchanged and grown | correct | **Sound and valuable.** The coboundary argument for "third rule" is right. |

### The extremal bar's kill criterion — the K4 question answered

**Is 3-distinct-selections-of-4-functionals the right death per D12? It
is a *correct* death but the *wrong lead*, and max-det's 9/9 uniqueness
does not deserve a narrower verdict — it deserves to be left standing,
which the paper does.**

D12's bar is: "the frozen SHARD premises **plus Q** have exactly one
physical equivalence class". Max-det **passes** the uniqueness half — it
selects, uniquely, 9 of 9, and the unit correctly prints
`MAX-DET-UNIQUE=TRUE`. It fails because **Q is an added premise**, which
is D12's "selects one member of a preselected toy family" and "chooses a
coefficient after its support, reference measure, modes, and constraints
have been supplied". The direct evidence for that is
`VARIATIONAL-ROWS-0-OF-6` — **and that is exactly the condition R6a's
reopening lead (ii) pre-registered**: "motivated iff a deeper row
declares a variational principle". The lead was designed to be
discharged by that measurement, and it was.

The functional-multiplicity countermodel is D12-*shaped* (twins the
selector cannot separate) and is genuinely stronger evidence in one
respect — it is *constructive* where the absence claim is a census — but
it is a corollary, not the criterion. Note also that it is not
structurally identical to D12's own witnesses, which are *model* twins
(P_r; iSWAP θ), not *selector* twins.

**Recommendation:** keep `DIES-AT-THE-BAR`; reorder the segment so
`VARIATIONAL-ROWS-0-OF-6` leads and `FUNCTIONALS=4|DISTINCT-SELECTIONS=3`
follows as the constructive corollary; repair the third leg per F5. And
keep `MAX-DET-UNIQUE=TRUE` exactly where it is — a hostile round that
erased it would be erasing a true measurement of the predecessor's.

### The identification census

- **The C1 type error is correctly found and correctly load-bearing.**
  It is the best single piece of reasoning in the unit. (And it is what
  makes F3 fatal to the pattern→position reading: the unit proves the
  split has no referent inside a leg and then reads one anyway.)
- **Could any identification have been motivated at the pinned rows?**
  No, and the reason is structural rather than a count of free items:
  every candidate must supply a scope, and no pinned row supplies one
  (F4/K3). `MOTIVATED 0 of 5` is right; with F3's `I-READOUT` added it
  is 0 of 5 more robustly.
- **The stabilizer-fixed firsts.** *Clock rate*: correct — conditioned
  on the count, Poisson positions are uniform order statistics and the
  rate cancels; correctly scoped as a stabilizer of the S5 comparator's
  observable, inside a candidate that is itself dead. *Orientation*:
  correct **for the position law**, measured at 3 cells — and
  **falsified for the front rule by the unit's own §7** (F1). One item
  cannot be stabilizer-fixed and consequential in the same unit; the
  item must be split per observable, or classed FREE.
- **The negative controls** are genuinely three distinct failure modes
  (unmotivated / refused-at-source / cardinality mismatch), and the
  NC3 arithmetic (n interior positions vs n−1 admissible splits) is
  correct. Credit: the census can fail a move.

---

## 7. K5 at my depth — do the heads and segments carry every measured restriction?

**No. Five restrictions are measured and not carried into any verdict
segment.**

| restriction | measured where | in a segment? |
|---|---|---|
| S2's leg lengths are **ENSEMBLE DATA** | §4, §12; the pin makes this qualifier **mandatory** (pin §4) | **NO** — absent from the verdict block entirely |
| The two inhomogeneous records enter at **2 of 9 sites** | §12 declared cap | **NO** — `COVERAGE=37-OF-201` carries no cap marker |
| `TV-DELIVERY-FREE=0` holds **at 2 censused cells, not proved** | §12 | **NO** — the segment reads as an unconditional 0 |
| Three records **admit no subdivision** (60 intervals, 10 of the 37) | nowhere in the unit; stated in CR-B §3 | **NO** (F2) |
| The identification named in `KERNEL-DERIVED` is **UNMOTIVATED** | the next head | **NO** — the head is not self-carrying |

Carried correctly: `SCOPE=DELIVERY-FREE` on both kernel heads (subject
to F4's renaming); S5's chosen-not-derived disclaimer wherever the
continuous layer is touched (gated, and the verdict does not touch it,
so compliant); the 400-term cap (not needed — the closed form is exact
and the cap applies only to the cross-check); the `EXCLUDED-CITED-0`
control.

Paper↔output↔receipt: I spot-checked the verdict block against the
emitted one (7 of 7 verbatim, confirmed by eye) and every §13 instrument
figure against the totals block (75 = 16+34+24+1; 48; 31; 15; 0). Full
sweep is R3's. F13 is the one gap I saw.

---

## 8. Recomputation ledger — 738

| block | count | contents |
|---|---|---|
| S1 chain | 40 | 6 row sums, 6 harmonic, 6 row-normalisations, 18 q′ entries, 2 class facts, 2 hitting probabilities |
| First-return law | 413 | 400 termwise closed-form comparisons, f(1)–f(5), mass, tail bound, analytic mass, return, defect, visits, defective mean, conditional mean |
| Two-route transcription | 26 | 20 T entries + 6 f entries, paper-31 (typed by hand) vs d43b `T_REF` |
| Convention sensitivity | 18 | 2 alternative normalisations × 9 quantities |
| Arena | 79 | 44 record-family field comparisons, 201, 10 census cells, 9 record fibers, 5 classes, 122, 4 movable classes, 2 corrected ratios, the 10 bad count-4s, 647, 67 |
| S2 laws | 28 | 6+6 law values, 2 TVs, 2 retained masses, 2 multiplicities, 4 binomial, 3 maximiser/minimiser sets, 3 reversal checks |
| Admissibility / marginals | 34 | 11 positive-definiteness, 14 raw-vs-admissible cells, 9 marginal values |
| Extremal | 8 | 4 selections, distinct-count, 3 determinants |
| Front rule (F1) | 73 | 63 cycles, minimum, 9 distinct cycle sums |
| Pattern-slot census (F8) | 12 | 5 patterns × (position, kind), 2 multiplicities |
| CR-B anchors | 7 | tv_uniform_vs_binomial at 6 counts + the count-4 simplex dimension |

**Numerical disagreements with the unit: zero.** Every finding above is
a finding about referent, scope or derivation, not about arithmetic.

---

## 9. Binding fix list (ranked)

1. **F1** — withdraw `NEW-FRONT-VALUES` fiber 1; re-class as fiber ≥ 2
   with the 63/63 separation, or withdraw entirely and carry the
   predecessor's kill. Retire "the unit's one clear gain" and the
   integrality contrast. Split or re-class `I-ORIENT`.
2. **F2** — print `27 of 103` beside `37 of 122`; name the three
   unrefinable records.
3. **F3** — add `I-READOUT` to C1/C4; qualify KERNEL-DERIVED.
4. **F4** — rename the delivery-free measurement as the no-delivery
   conditional; state the weight caveat.
5. **F5** — repair the det leg; drop "the record-intrinsic test fails".
6. **F8** — print the middle-slot exclusion and the delivery
   multiplicities (a *gain*, and Γ-main's target).
7. **K3(b)** — re-state the SEAM head's cause as the escape, citing
   paper 32 §2.3, not row provenance.
8. **K5** — five restrictions into segments; `IDENT=…-UNMOTIVATED`.
9. **F6** — reorder the extremal segment.
10. **F7, F9, F10, F11, F12, F13** — as stated.

---

## 10. The QFT-needs-gravity link audit

The stake (v14 LOG #56): *"if Γ-main lands, 'you cannot have QFT
without gravity' upgrades from structural implication to a THEOREM —
the division event = one mechanism, two faces: where the quantum law
conditions and what the metric counts; back-reaction = interaction
writing geometry; QFT-on-background = the frozen-stage approximation
with a built-in validity domain."* Three links; R6b′ touches all three
and welds none.

**L1 — "one mechanism, two faces" (division event ≡ where the quantum
law conditions ≡ what the metric counts).**
**STRENGTHENED AT THE COUNT LEVEL; LEFT UNWELDED AT THE POSITION
LEVEL — and R6b′ is the first unit to say *where* the weld fails.**
The type census is the contribution: n_ℓ counts division events (the
metric face) and S3 posits division event ≡ renewal (the conditioning
face), and the unit *measures* that the two faces count the same
objects — an inter-renewal leg contains exactly one division event. So
the identity holds as an identity of **counts**. It fails as an identity
of **positions**: the metric face asks where inside an interval the
events sit; the conditioning face has no interior division event to put
there. That is the precise locus of the missing weld, and it is now
named rather than assumed. Note the sting: the *type-honest* reading
(C2) is the *most* unmotivated candidate, 5 free items — the honest
identity is the one the corpus can least justify.

**L2 — "back-reaction = interaction writing geometry".**
**NOT WELDED — the unit explicitly does not construct Γ. One
half-direction earned, and it is the *reverse* direction.** The front
rule (geometry's split forcing the matter-side front) is the only
directional statement, and F1 shows it is wrong as delivered; corrected
to fiber 2 it survives as "geometry constrains the front up to an
orientation", which is a weaker and *reverse-direction* fact.
**Interaction writing geometry is untouched.** What R6b′ *does* supply
is L2's qualitative content in miniature: turning deliveries on changes
the positional law (TV `2/63`) and turning them off makes it exactly
uniform and position-independent (TV exactly `0`). That is
"interaction generates structure on the stage", measured, with the
mechanism isolated (F8: no delivery in the middle slot). It is not
back-reaction — nothing here writes a *metric* — but it is the first
measured instance of the shape.

**L3 — "QFT-on-background = the frozen-stage approximation with a
built-in validity domain".**
**NOT WELDED, but R6b′ delivers the first measured contrast between the
frozen and unfrozen stage, and a candidate for the validity domain's
first coordinate.** The delivery-free sub-ensemble *is* the frozen
stage: exactly uniform, exactly chain-position-independent, and the
renewal chain terminates a.s. The transport ensemble is the unfrozen
one: position-dependent, and the corpus measures the absorbing sector
reopening. The separation between them is `2/63` at leg 1 and grows
toward (1/2, 0, 1/2) as the delivery multiplicity grows — so **the
validity-domain parameter is the delivery multiplicity per interior
slot**, and R6b′ has measured it at two values (2 and 3). That is a
concrete, transportable candidate and it is worth stating as one.
Caveat: F4 means the frozen-stage law is a *conditional* of the
unfrozen census, so the contrast is currently within-ensemble, not
between two independently constructed ensembles. Γ-prep's delivery-free
family (its declared like-for-like contrast) is exactly what would
close that.

**Also relevant and negative.** R6b′ closes two escape routes the QFT
side might have wanted: no variational selector is available (`0 of 6`),
and no cover/de-periodization route exists (rooted, depth-non-stationary
arenas). Both are prohibitions Γ-main and R4 inherit.

**Net.** R6b′ strengthens **L1 at the count level** and supplies **L2's
and L3's qualitative shape as a measurement**. It welds **none** of the
three. The stake is unmoved: it still rides entirely on Γ-main.

---

## 11. Closing statement

This is a careful, honest unit that measured more than it claimed in one
place (the delivery/position mechanism, F8) and claimed more than it
measured in four (F1–F4). Its arithmetic is clean throughout — 738
independent recomputations, zero disagreements — and its two hardest
pieces of reasoning, the type census and the transverse-links
non-reachability, are both correct and both structural.

The one false result is a re-classification that reinstates a reading
the predecessor had already killed twice, and it is presented as the
unit's headline gain. Repairing it does not weaken the paper; it makes
its most interesting pattern legible — **the enrichment grew freedom at
two of four entries and shrank it at none.**

The seam is real, deep, and mis-attributed. Naming its true cause — the
escape — is what turns a blockage into a hand-off.

**GRADE: ACCEPT-WITH-FIXES.**

*Hashes re-verified at close, all six unchanged: paper `68c20d1fdae4`,
code `8e188dd3ab70`, output `42a39fcaf194`, receipt `50f63b3ba362`,
pin `17111fd19022`, protocol `1cf5fc8b3272`. No repo write other than
this file; no git write; scratch only; no live-unit or other-review
file opened.*
