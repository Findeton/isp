# K2 EFFECTUS — hostile review of paper-20 (the coupling unit, the summit)

**Seat:** K2 EFFECTUS, per the frozen panel protocol (v14 ledger #180).
**Objects under review, at `9b1860e`, sha256-12 verified at start and at close:**
`v14/paper-20-coupling.md` **b328a8278fac** · `v14/code/coupling_exact.py`
**9e71cf511ab3** · `v14/code/coupling_output.txt` **3e3d04222782** ·
`v14/code/coupling_receipt.json` **3ca0308b6c19** · pin
`v14/note-coupling-pin.md` **7c6e9e44fc2c**.
**Binding context:** `v14/note-cra-adjudication.md` **b7ce00951e5a**, §THE
PAPER-20 REGISTER (rows R-CRA→20-1..4, taken at their source form in
`review-cra-effectus.md` §3).

**GRADE: AWF (accept with fixes).** Six MAJOR, eleven MINOR.

**Zero delivered numbers moved.** 191 recomputations this seat — 116 delivered
values rebuilt with my own machinery (a from-scratch reimplementation of the
walk, the emission rule, the readout and the censuses, sharing no code and no
literal with `coupling_exact.py`), 75 adversarial computations this seat
originated. Every published number I touched reproduced exactly, including the
two exit probabilities, all twenty branch counts, the inverse participations,
the curvature probabilities, the falsifier's 10, and all seven fiber values.

**The verdict word survives.** `COUPLING-CONSISTENT-NOT-REQUIRED` is the right
word for what was measured, and it survives every attack I could mount on it:
the two `UPDATE-RULE-RESTATED` refusals are principled (§3.1); the one row that
could have flipped the verdict is *not measured at all* as delivered (MAJOR-2),
and when I repaired it and measured it properly the verdict still stands; the
alternative coin order, run here at the **full** horizon, does not change it
either. What does not survive is one head-carried theorem claim (MAJOR-3), and
several rows whose stamp is stronger than their instrument.

---

## 1. THE RECOMPUTATION LEDGER

My rebuild (`k2_walk.py`, scratch): Z[ω] as integer pairs, the Grover
numerators over 3, the +ℓ shift table, the two menu readings, exhaustive
branching, exact `Fraction` weights. Independently reproduced:

| delivered | reproduced |
|---|---|
| A-COUPLED 3, 27, 486, 10527, **284078** | ✔ |
| A-FROZEN 3, 27, 486, 9234, **212382** | ✔ |
| B-COUPLED / B-FROZEN 3, 27, 486, 11664, **314928** | ✔ (both, identical) |
| branch mass = 1 at all 20 levels | ✔ |
| exit (Born menu) `927415552/847288609443` | ✔ |
| exit (record menu) `37440224/5811307335` | ✔ |
| exit = 0 at horizons 1–4, both readings; frozen 0 at all ten rows | ✔ |
| max cell 2, 2, 3, 3, 4 | ✔ |
| det spectrum {0, 3/4, 1, 7/4, 2, 3}; no negative det | ✔ |
| ipr coupled `35971074413334039128803/239299329230617529590083` | ✔ |
| ipr frozen `2306155/14348907` | ✔ |
| posdef distribution {8, 9} | ✔ |
| constant-curvature `7598838656/22876792454961`; frozen 1 | ✔ |
| terminal-condition falsifier kills at **10** (of 36 checks, T = 2) | ✔ |
| fiber iprs: ORDER-GD/ORIENT-±/INIT-0/1 `33596579/129140163`, INIT-2 `27231395/129140163`, ORDER-DG `40411/177147` | ✔ (7 of 7) |
| scalar census: 6 differences, multiplicities all 1; axis [3, 3]; 343 maps, 18 unitary, 0 non-monomial | ✔ |
| coin census: 4 solutions, 2 non-trivial, over the code's declared grid | ✔ (see MAJOR-3) |
| 45157 / 406413 / 406413 / 948297 / 1215681 / 187155 / 2455 | ✔ (re-derived from my own branch counts) |
| 1296 = 3!·(3!)³ | ✔ |

---

## 2. THE LICENSED CLAIM

What this unit is entitled to say, after this seat:

1. **The coupled step is well defined.** Unitarity × column-stochasticity
   compose to total emission mass exactly 1, per branch, per step, per site,
   948,297 checks, 0 violations. LICENSED (with MINOR-9's column caveat).
2. **The coupling is not inert.** 18 of 18 declared-observable rows move against
   the mandatory frozen control; leaves 284,078 vs 212,382. LICENSED.
3. **No requirement witness exists *in the pre-registered battery*.** LICENSED
   with the stamp made explicit: the head's first clause must carry the
   battery scope its parenthetical already carries (MINOR-1).
4. **Staleness blindness.** LICENSED at the quantifier the check carries: *every
   single-time closure that is a property of (ψ, U(n)) uniformly in n* — not
   "every ψ-internal closure" (MINOR-3).
5. **The admissibility exit at horizon exactly 5, to the singular boundary
   det = 0, no indefinite form.** LICENSED and, after my classification of the
   1,316 inadmissible leaves, *strengthened*: **every** exit at this horizon is
   the same arithmetic event — one site carrying three excess events on one
   link, count vector (4,1,1), (1,4,1) or (1,1,4), det exactly 0.
6. **"The frozen stage is safer on the arena's own axiom."** LICENSED as a
   comparative on I7's Sylvester criterion at the declared horizon — but it is
   a *tautology with a measured partner* and must say so (MINOR-5).
7. **The coin register is forced (F3).** LICENSED — the monomial-only theorem is
   correct, and I verified its hypothesis and conclusion independently. The
   scalar shape stays monomial even if a self-loop is added (my scan: offsets
   {0, e₁, e₂, e₁+e₂}, 24 unitary, **0** non-monomial), which strengthens it.
8. **The coin is forced (F4).** **NOT LICENSED as stated** — MAJOR-3.
9. **The law transport is confirmed.** LICENSED, but the sentence naming *which*
   row could have failed is wrong (MINOR-2).

---

## 3. MY ROWS, RULED

### 3.1 The head's licensure — is the ψ-internal class honestly delimited?

**Ruling: the class is PRINCIPLED, not shaped to the outcome — but the deciding
class contained no live candidate, and the paper must say so.**

The taxonomy is declared before the run with a stated criterion per class
(code L1511–1519), and the selector's two filters (PSI-INTERNAL ∧ ¬restated)
are pre-registered. It is not gerrymandered: it has exactly one escape hatch
(a ψ-internal closure that is *history*-dependent), the unit names that hatch,
and §8.3's theorem explains why it is the only one. That is the honest shape.

But measured against the code, **four of the five ψ-internal rows are
n-independent by construction**: K1 (unitarity), K2 (site-block-diagonality),
K3 (G(x,1) = M(x) from the terminal condition), K4 (k = q/M sums to 1; total
mass 1) hold for *every* count field, coupled, frozen or stale, because none of
them reads n. **The fifth (K5) cannot fail at all** (MAJOR-2). So the forward
direction of the requirement gate was empty *before the run*, and NO-WITNESS is
carried by the staleness theorem, not by the battery's coverage. The unit is
half-aware of this ("Why is the witness not there? Not by accident") but the
head reads as a search result. Repair in MAJOR-1.

**The two refusals — both principled; I checked each as a potential flip.**

- `K10-RECORDS-THEOREM` ("total record increment = number of division events"):
  on the frozen stage the increment is identically 0 while 5 events are
  emitted. Its frozen failure is the sentence "the counts do not update"
  read back. **Refusal correct.** Had it been admitted the head would read
  `REQUIRED-K10`, whose content would be "the counts update because the counts
  update".
- `K9-SOURCING` (M_{t+1}(x) − M_t(x) = p_t(x)): on the coupled arm the left side
  *is* the emitted mass at x, which is p(x) because Σ_ℓ k₁ = 1; on the frozen
  arm the left side is identically 0. Same structure. **Refusal correct.**
  And the refusal generalises, which is worth stating: *any* closure that
  equates a record increment with a state quantity fails frozen for the same
  trivial reason, so the RECORD-COUPLED class cannot supply a witness at all.

**Is K5-NO-RETURN really the only buildable history-dependent closure?** As
delivered the question does not arise, because K5 is not a live test
(MAJOR-2). On the substance: the claim "the only history-dependent ψ-internal
row *this unit could build*" is honestly hedged in §8.3 and S-2 concedes the
class may be "merely unexplored" — that hedge is correct and must stay. A
second one is easy to *pose* (e.g. a two-time interference functional
⟨ψ_t, U(n_t)…U(n_s) ψ_s⟩ compared against its frozen-stage counterpart, or a
Loschmidt-echo/return-amplitude at fixed record) and none is built here. The
successor register should say **UNPROBED**, not merely unexplored.

**Does the staleness theorem license "needs history-dependence"?** Yes, at the
quantifier the *argument* carries (a single-time closure that holds for every
admissible n cannot see n), and the machine check is an instance of it, not a
proof of it. As stated in the blockquote and in the head ("EVERY PSI-INTERNAL
CLOSURE") the quantifier exceeds both the argument and the check. MINOR-3.

### 3.2 The reversed horizon-5 reading, and the CR-A reconciliation

**Both licensed sentences hold; the two derivations agree quantitatively, and
the agreement is exact.**

- *"Coupled exits admissibility at exactly 5, frozen never."* The exit is
  positive at 5 and exactly 0 at 1–4 on both readings — reproduced. "Frozen
  never" is true, but it is true **by theorem** (the frozen record is constant
  and admissible), not by the five measured rows; presented as an unbounded
  measurement it overreaches. MINOR-4.
- *"The frozen stage is safer on the arena's own axiom."* The axiom register is
  I7's Sylvester criterion, cited verbatim (V-HA-ADMISSIBLE) — the right
  register, and the comparative is measured on it. But a stage that never
  updates cannot leave the class it began in, so "safer" is a tautology whose
  measured partner is the *horizon at which the updating one leaves*. MINOR-5.

**The reconciliation with R-CRA→20-2 (G-SINGULAR proximity), computed:**

CR-A's register row says the weld arena sits **three diagonal-only events** from
`G-SINGULAR`. I verified the margin exactly and it is *three on any one link*,
not only the diagonal: from n ≡ 1, three excess events on link 1, 2 or 3 give
(4,1,1), (1,4,1), (1,1,4) — det 0 in all three cases, q₁₁ > 0, so
positive-semidefinite rank 1, the singular boundary.

I then classified **all 1,316 inadmissible leaves** of the A-COUPLED horizon-5
frontier (total weight = the delivered exit probability, exactly). Every one of
them has excess-event pattern **(0, 0, 3) at a single site** — 379 of type
(4,1,1), 471 of type (1,4,1), 466 of type (1,1,4). **CR-A's three-event margin
is the walk's exit mechanism, with nothing else in it.**

**Why 5 steps and not 3** — the missing half of the reconciliation, measured
here. The walk emits exactly one division event per coupled step, so three
events on one cell need the walk to carry positive Born mass at that site at
three distinct steps. The +ℓ shift on Z₃² gives the site-support schedule

| step | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| sites with positive mass | (0,0) | 3 | 6 | 8 | 9 |

and the earliest third visit, over all nine sites, is **step 5** — site (0,0) at
{1, 4, 5}, site (1,1) at {2, 3, 5}, every other site at 5. Hence max cell count
2, 2, 3, 3, 4 and exit threshold exactly 5. **The two derivations meet exactly:
CR-A supplies the event budget (3), the return-time of the shift supplies the
step budget (5).** This belongs in §9 — it is currently asserted
("Reaching that needs 5 steps") with no mechanism. MINOR-6.

### 3.3 The transport confirmation's scope — coin-shape contingency

**Ruling: the confirmation is contingent on site-block-diagonality alone, the
contingency is real, it is *not* vacuous, and it is not scope-stamped.**

The mechanism is exactly "the coin does not move mass between sites", which is
weaker than "the coin is ±Grover": *any* site-local unitary (the whole
S₃-covariant family, and much more besides) confirms the transport identically.
A non-block-diagonal coin — any lift that mixes amplitudes across sites before
the menu is read — destroys M(x) = p(x) and would return
`BLOCKED-AT-THE-LAW-TRANSPORT`, the pin's reserved first-class outcome. So the
transport row is **robust across the coin fiber and fragile across the coin
*shape***, and the paper says neither.

The contingency is *not* vacuous even here, because the coin is **not** forced
(MAJOR-3): the confirmation survives the coin fiber for the stated reason
(block-diagonality), but the sentence "because the coin is site-block-diagonal,
which is a property of the walk" needs the successor stamp: **any successor that
leaves the site-local class must re-gate the transport.** MINOR-7.

### 3.4 R-CRA→20 open #4 (no substitute for commutation) — the reconciliation row

**Ruling: CARRIED, NOT DISCHARGED — and the unit hands two measured instruments
forward without naming either as commutation's substitute.**

CR-A's static-geometry theorem says: at the pinned layer, demanding the geometry
move commute with the dynamics forces the move to zero; open #4 says a successor
that wants motion must say what it puts in commutation's place and characterise
the resulting defect. paper-20 wants motion and gets it, so the debt is live.

What the unit supplies instead of commutation is an **ordering**: walk, then
emit, then update; the next step reads the updated n. What it supplies in place
of a *characterisation of the defect* is two measured objects that are exactly
defect measurements, neither labelled as such:

- **The coin-order fiber (F6)** measures the defect of the ordering *inside* one
  step (G·D against D·G). At the full horizon I measure that defect as a factor
  of **3.15 on the unit's own headline observable** (§3.6 below).
- **The staleness-blindness theorem** characterises the defect's *visibility*:
  non-commutation is invisible to every single-time ψ-internal closure. That is
  a genuine partial answer to open #4 — "the defect is real and it is
  unobservable at a single time" — and it is the strongest thing this unit could
  have said in commutation's place.

**Register row, ready to lift:**

> **R-CRA→20-4 (reconciled at the paper-20 panel).** The coupling unit does not
> discharge CR-A's open #4. It replaces commutation with a declared ordering
> and *measures* the ordering's defect twice — the coin-order fiber (a 3.15×
> swing in the admissibility exit probability at the full horizon) and the
> update-semantics fiber — and it characterises the defect's visibility by the
> staleness-blindness theorem (invisible to every single-time ψ-internal
> closure). It names no compatibility notion. **The debt passes to paper-21 with
> its two instruments attached.**

Also on the register: **R-CRA→20-1 is honoured in substance and not in
citation.** The hexagonal reading is barred (§9, §10) and gated, but the paper
attributes the naming to paper-19's S-7 and never carries CR-A's *mechanism* —
that the form is a function of the declared link set and of nothing else, so it
is not physically selected. MINOR-8. **R-CRA→20-3** (the theorem is why the
gate is well-posed) is nowhere in the paper; it is exactly the sentence that
would tell a reader why NO-WITNESS was a live possibility rather than a
foregone one. **R-CRA→20-4** (CR-A's census cannot speak to the emission rule)
is honoured: no such citation is made.

### 3.5 interference-dies-here — licensed as stated?

**The theorem: LICENSED and independently verified. The exhaustive scan that
the head cites as its corroboration: BLIND. The "why interference lives there"
half: TRUE but not measured here.**

I verified the hypothesis (6 nonzero differences of the three declared link
offsets, each realised by exactly one ordered pair) and the conclusion
(each off-diagonal autocorrelation condition is a single product c_v conj(c_w),
forcing a vanishing; the norm condition then forces a monomial). Correct, and
scoped correctly in both prose and head ("on this arena's offset set").

The corroboration is where it fails. Over the declared 7-value alphabet
({0} ∪ {±ω^k}, all of modulus 0 or 1) the scan returns 18 unitary / 0
non-monomial on the link stencil — **and I get exactly the same 18 / 0 on
R4b's axis stencil**, where interference demonstrably survives: the circulant
c = (−1/3, 2/3, 2/3) is exactly unitary and non-monomial there (verified).
An instrument that returns the same answer on both stencils cannot be evidence
for the contrast the head draws with it. MAJOR-4, with the repair measured.

The R4b contrast itself (multiplicity 3 against multiplicity 1) is **measured**
here; "which is precisely why interference survives there" is a **gloss** —
true, but carried by R4b's citation, not by anything this run computes. With
MAJOR-4's repair it becomes measured on both sides in the same run.

### 3.6 The coin-order declared item (F6) — disclosure adequacy

**Ruling: the stamp is right, the fiber is right, the *direction* of the
disclosure is not licensed, and the full-horizon measurement reverses it on the
headline row.**

Disclosed: DECLARED-VERDICT-RELEVANT, fiber 2, both members run at horizon 3,
G·D moves 7 of 9 declared observables against its own frozen control, D·G
moves 5, with the mechanism ("a count phase applied after the coin cannot enter
that step's Born weights at all"). All reproduced. Deviation 4 then says the
alternative is "measurably weaker on the declared observables".

I ran the alternative at the **full** horizon, both arms, reading A:

| | G·D (delivered) | D·G (this seat) |
|---|---|---|
| coupled leaves at T = 5 | 284078 | **226404** |
| frozen leaves | 212382 | 212382 |
| exit probability at T = 5 | `927415552/847288609443` | **`2922723584/847288609443`** |
| exit threshold | 5 (0 below) | **5 (0 below)** |
| constant-curvature probability | `7598838656/22876792454961` | `4747253936/7625597484987` |
| max cell / det spectrum / total emitted | 4 / {0,3/4,1,7/4,2,3} / 5 | 4 / {0,3/4,1,7/4,2,3} / 5 |

**Under the alternative order the record leaves I7's admissible class with over
three times the probability.** "Weaker" is a horizon-3 count of moving rows; on
the unit's own sharpest observable, at the horizon the head reports, the
alternative is *stronger*. The threshold — the part of the finding that is a
structural statement — is order-invariant, which is good news and should be
said. MAJOR-5.

**Is either order privileged by anything measured?** No. Nothing in the arena,
the parents or the pin selects one; the within-step argument offered for G·D
("the phase cannot enter that step's Born weights under D·G") is true and does
not select, because under D·G the phase enters the *next* step's weights — which
is why the full-horizon back-reaction is larger, not smaller. Note also that
under D·G the emission menu at a step is stage-blind (|DGψ|² = |Gψ|²), which is
a genuinely different coupling model and deserves that one sentence.

**Does the head depend on the choice?** The outcome word: no — K1–K4 are
structural under any site-local unitary coin, K5 is vacuous, K9/K10 are refused,
and I confirm the reverse-direction rows still fire under D·G (curvature
inhomogeneous, translation invariance 0, exit positive). The
`ADMISSIBILITY-LADDER` segment's *number*: yes, by 3.15×. Its *threshold*: no.

### 3.7 Choice inventory and prose↔receipt sweep

Twelve items, statuses checked against the code one by one. F1/F2 forced by the
parents ✔. F3 DERIVED ✔ (theorem verified). **F4 DERIVED — WRONG (MAJOR-3).**
F5 DERIVED ✔ (Z₃ from F₃; the disclosure that the walk consumes n mod 3 is
carried in §3.3, §13.1 and S-1 — exemplary). F6 ✔ stamped, direction wrong
(MAJOR-5). F7 both members run ✔ but "inert" is false on the declared set
(MINOR-10). F8 ✔ all three run, and the ipr values reproduce. **F9 MEASURED —
the measurement is a no-op (MAJOR-6).** F10 both readings run and every row
stamped ✔ — this is the best-executed item in the inventory. F11 ✔ ladder
published. F12 ✔ the alternative's consequence *is* the exit probability, a
genuinely honest pricing.

Prose↔receipt: §2, §5, §6, §7, §9 tables all match the receipt and my rebuild.
§14's instrument counts (52 gates evaluated / 40 falsified / 12 waived / 44
mutants / 27 seals / 11 anchors / 16 sources) match the receipt. The three
fenced head blocks appear verbatim in §12 and in the head, as gated. The nine
assembled claims are located. No numeral in the paper is unregistered.

### 3.8 The successor register — what the R = 4 arena inherits

See §6 below.

---

## 4. FINDINGS

### MAJOR-1 — NO-WITNESS is a statement about a search space with no live candidate, and the head does not say so

**Where:** head segment 3, `G-REQUIREMENT`; §8.1–8.2.
**What:** K1–K4 are identities that hold for *every* count field (they never
read n); K5 cannot fail (MAJOR-2). So no ψ-internal row could have failed
frozen, whatever the physics did. The battery's two-way-ness — the property
that makes it "an instrument rather than a list" — is carried entirely by rows
*outside* the deciding class.
**Why it matters:** as written, a reader takes NO-WITNESS as a search that came
back empty. It is a search whose space was empty by construction; what makes
the emptiness *non-arbitrary* is §8.3's theorem, and that is the real result.
**Repair (exact, moves no number):** in §8.2, after the measured sentence, add:
"Every ψ-internal row of this battery is an identity of the construction — K1,
K2, K3 and K4 hold for any count field whatever, because none of them reads the
record. The forward direction was therefore empty before the run, and §8.3 is
the reason that emptiness is forced rather than chosen: at a single time there
is nothing else it could have contained." In §12's read-out, replace "the
requirement gate returns no witness" with "the requirement gate returns no
witness, and the theorem below says no single-time one was available to it."
Head: insert `OF THE 10-ROW PRE-REGISTERED BATTERY` into the first clause of
`G-REQUIREMENT=NO-WITNESS(...)`, so the scope stamp is not carried by the
parenthetical alone.

### MAJOR-2 — `K5-NO-RETURN`, the only history-dependent row, is measured by a predicate that cannot fire

**Where:** code `run_arm` L1277–1279 (`here = set(psi …)`, `repeat_states`);
§8.1 table; §8.3's "it holds on both stages"; head `ALL 5 PSI-INTERNAL ROWS …
HOLD`.
**What:** the amplitudes are carried unnormalised, with Σ|ψ_t|² = 9^t exactly
(this unit's own G-WALK-UNITARY gate asserts it, and I verified it at t = 1…5).
States at different levels therefore differ in norm and can never be equal, so
`here & seen_states` is empty by construction, on both arms, at every horizon.
`repeat_states = 0` is not a measurement.
**Why it matters — this is the row that could have flipped the verdict.** A
correctly scaled K5 *could* have failed frozen and held coupled (the frozen walk
is a single trajectory; the coupled one is not), and it is ψ-internal and not
update-rule-restated, i.e. an admissible witness. The delivered instrument
cannot see that.
**I ran the repair.** Comparing ψ_t/3^t exactly, and rays (dividing by the
first nonzero component in Q(ω)): the frozen walk **does not return within 30
steps** (exact or projective), and the coupled arm has **0 cross-level
normalised repeats** through level 4 (1, 1, 3, 252 distinct states at levels
1–4). **So the repaired row still holds on both stages and the verdict stands.**
**Repair (exact):** compare `tuple(Fraction(a, 3**t), Fraction(b, 3**t))` per
component (and, as a second row, the ray class), and publish the frozen
no-return at a horizon beyond the ladder — 30 steps is cheap and makes §8.3's
"the frozen state never returns either" a measurement rather than a corollary
of a trace argument that only bounds the *operator's* order (6 of 9 sectors
having non-integral trace bounds the sector operators, not the orbit of this
particular initial vector — that gap should also be closed by the direct
measurement).

### MAJOR-3 — "COIN-FORCED-BY-THEOREM … EVERY ONE OF THEM ±GROVER" is false at the generality it is stated in

**Where:** head segment 2; §3.2; §11 item F4 (`DERIVED`, fiber 1); `G-COIN-FORCED`.
**What:** the S₃-covariant unitarity conditions on C = aI + bJ are |a| = 1 and
a·conj(b) + conj(a)·b + 3|b|² = 0, i.e. (writing b = aβ) |β + 1/3| = 1/3 — a
**circle** of solutions, not four points. The code's census scans only
a ∈ {1, −1} and b real rational on a declared grid, where the circle meets the
reals in exactly two points (0 and −2a/3). The paper's §3.2 hedges with "rational
scan"; the head drops the hedge and asserts the solution set.
**This is not an abstract objection — the alternatives live in this unit's own
arithmetic.** Exhaustively, over Z[ω] with a power-of-3 denominator (precisely
the class §14 declares for the amplitudes) there are **36** solutions, **6** up
to a global phase: b/a ∈ {0, −2/3, (−1+ω)/3, (−1−ω)/3, (−2−ω)/3, ω/3}. Only
b/a = −2/3 is Grover. Verified by exact C·C† = I. Over Q(ω) the family is
infinite (78 further examples in a small scan; e.g. a = 1, b = (1+5ω)/21 is
exactly unitary and exactly cyclotomic).
**Why it matters:** F4's fiber is 5 non-trivial coins up to phase, not 1; the
requirement gate was measured at one of them; and "the coin is derived from the
arena's own symmetry rather than declared" is the sentence a successor will
inherit.
**Repair (exact):** (i) head → `COIN-FORCED-BY-THEOREM-AT-REAL-ENTRIES: THE
S_3-COVARIANT UNITARITY CONDITIONS HAVE A CIRCLE OF SOLUTIONS; OVER REAL
RATIONALS 4, 2 NON-TRIVIAL, BOTH +/-GROVER; OVER THIS ARENA'S OWN
POWER-OF-3-DENOMINATOR CYCLOTOMICS 36, SIX UP TO A GLOBAL PHASE`; (ii) §3.2 →
state the circle, state the reality condition as a *declared* restriction, and
say what it buys (a real orthogonal coin, time-reversal-symmetric); (iii) §11
F4 → `DECLARED-UNDER-A-REALITY-CONDITION`, fiber 5 (non-trivial, up to phase),
with the measured alternates listed; (iv) S-1 gains the sentence: whether a
non-Grover cyclotomic coin admits a requirement witness is unmeasured. The
polarity needle P3 ("the coin register is forced") is unaffected — that is F3,
and F3 is sound.

### MAJOR-4 — the exhaustive scalar scan is blind: it returns the same answer on the stencil where interference survives

**Where:** head segment 2 ("343 MAPS SCANNED … 18 UNITARY, 0 NON-MONOMIAL —
AGAINST MULTIPLICITY 3 ON THE AXIS STENCIL WHERE INTERFERENCE SURVIVES");
§3.1; `scalar_shape_census`.
**What:** the alphabet is {0} ∪ {±ω^k} — only moduli 0 and 1. Run on R4b's own
axis stencil it gives **18 unitary, 0 non-monomial**, identical to the link
stencil. The scan cannot distinguish the two cases and therefore corroborates
nothing.
**Repair (exact, cheap, measured here):** widen the alphabet to the values a
Grover-class amplitude can take — {0} ∪ {±(k/3)·ω^j : k = 1, 2, 3}, 19 values,
19³ = 6859 maps. Then: **link stencil 18 unitary / 0 non-monomial; axis stencil
72 unitary / 54 non-monomial** (witness c = (1/3, −2/3, −2/3)). The head's
contrast becomes measured on both sides in one run, and the added row is a
falsifier for the theorem itself.

### MAJOR-5 — F6's disclosure states a direction the full horizon reverses

**Where:** §11 final paragraph; §13 deviation 4; `G-FIBERS`.
**What:** "the alternative member is measurably weaker on the declared
observables" is a horizon-3 row-count. At the full horizon, D·G's admissibility
exit probability is `2922723584/847288609443` against G·D's
`927415552/847288609443` — 3.15× larger — with the threshold still exactly 5
and leaves 226404 (see §3.6's table; all values from my rebuild).
**Repair (exact):** run the F6 alternative at the full horizon for reading A
(≈ the cost of one delivered arm) and publish both exit probabilities;
restate deviation 4 as "the alternative moves fewer of the nine declared
observables at the reduced horizon **and more of the record at the full one**:
the exit probability is 3.15 times larger, while the threshold is unchanged at
5 — the threshold is order-invariant, the magnitude is not." If the run is
declined, the sentence must instead read "no full-horizon comparison was
taken", and §13.4's "measurably weaker" must go.

### MAJOR-6 — `F9-INIT-SITE`'s "MEASURED" row is a no-op, and the comparison it declares would have failed

**Where:** code L1489–1491; §11 item 9 (`MEASURED`, fiber 1); receipt
`fiber_measurements.SITE-TRANSLATION-INVARIANT: True`; `G-FIBERS` evidence
("start-site fiber measured invariant True").
**What:** `base` and `shifted` are the *same run* — `n0=WELDED` is `run_arm`'s
own default, and the start site is hard-coded at (0,0) with no parameter to
move it. The comparison is `x == x`.
**And the declared comparison is the wrong one.** I implemented the translated
start: p_site at start (1,0) is **not** equal to p_site at (0,0) — it is its
image under the corresponding site permutation (verified exactly), which is
what translation *covariance* predicts. Equality of p_site would have returned
False.
**Repair (exact):** parameterise the start site; compare the observable set
*up to the translation permutation* (verified True here), or compare a
translation-invariant summary — the ipr is equal at `33596579/129140163`
(verified). Then F9 may keep its `MEASURED` stamp.

### MINOR-1 — the head's NO-WITNESS clause lacks the battery stamp its parenthetical carries
Repair as in MAJOR-1(iii).

### MINOR-2 — "the transport's content is the row that could have failed" names a row that cannot fail
§4 and `G-LAW-TRANSPORT`. Under reading A, `qrow[i] = Fraction(J[i], den)` and
the check is `M == Fraction(post[s], den)` — that is Σ(Jᵢ/d) against (ΣJᵢ)/d in
exact rational arithmetic, an identity independent of block-diagonality. The
mutant covering the gate (`MUT-TRANSPORT-ASSUMED`) flips the verdict flag, not
the arithmetic. The **substantive** block-diagonality content is the K2 site row
(post[s]·preden = pre[s]·den, 406,413 checks) — the coin not moving mass between
sites. **Repair:** rename the 187,155-check row "the identification, stated per
site", and point "the row that could have failed" at the site row: "the law's
menu is site-local only because the coin preserves each site's mass separately —
406,413 site-branch-steps, 0 violations; a coin that mixed sites would leave the
law without a menu."

### MINOR-3 — the staleness theorem's quantifier exceeds its check
§8.3 blockquote and head say "every ψ-internal closure"; the gate's predicate is
`norm ∧ site ∧ law_native ∧ column` on one stale arm — four of the five rows
(K5 is absent, correctly, since it is not single-time), and 868 of the 2,455
checks. **Repair:** state the theorem for *single-time closures that are
properties of (ψ, U(n)) uniformly in n*, and say the check is an instance over
K1–K4.

### MINOR-4 — "the frozen control never leaves it, at any horizon" is a theorem sold as a measurement
Only horizons 1–5 are run. **Repair:** "…and cannot leave it at any horizon: its
record never changes, and the welded record is admissible."

### MINOR-5 — "safer" is a tautology with a measured partner
**Repair:** append to §9: "Trivially so, in one direction — a stage that never
updates cannot leave the class it began in. What the measurement adds is the
other direction: the horizon at which the updating one does, and that it goes to
the singular boundary rather than through it."

### MINOR-6 — §9's mechanism is asserted, under-general, and missing its step-budget half
Three items: (i) the exit is 3-fold degenerate — (4,1,1), (1,4,1), (1,1,4), not
only "one site's third link"; (ii) all 1,316 inadmissible leaves have pattern
(0,0,3) at one site; (iii) "reaching that needs 5 steps" is the return-time of
the +ℓ shift (earliest third visit at step 5; (0,0) at {1,4,5}, (1,1) at
{2,3,5}). **Repair:** replace the mechanism sentence with the three-line version
in §3.2 above, and cite CR-A's row as the independent derivation of the
three-event margin.

### MINOR-7 — the transport's coin-shape scope is not stamped
**Repair:** §4 gains "the mechanism is site-locality, not the coin's identity:
every member of the coin fiber confirms the transport, and any successor whose
walk moves amplitude between sites before the menu is read must re-gate it —
`BLOCKED-AT-THE-LAW-TRANSPORT` is reserved for exactly that."

### MINOR-8 — CR-A is nowhere cited
R-CRA→20-1 asked for CR-A's non-claim 5 in the walls; R-CRA→20-3 is the
positive reason the requirement gate is well-posed. Neither appears. **Repair:**
§10 gains one clause (the hexagonal form is a function of the declared link set
and of nothing else — CR-A's measured mechanism — so it is not physically
selected), and §1 or §8 gains one sentence carrying R-CRA→20-3.

### MINOR-9 — "Σ_ℓ k₁(ℓ|x) = 1 at each of the nine columns" is not true at every column
At 1,186 site-steps of the two reading-A arms (593 per arm) the site carries no
amplitude, M(x) = 0 and there is no kernel; the gate accepts colsum 0. The
receipt discloses it (kernel 98803 of 99396; 87166 of 87759) but §6 does not.
**Repair:** "at each of the nine columns that carries mass; where the walk has
no amplitude there is no menu, and the column is empty — 1,186 site-steps."

### MINOR-10 — "the orientation fiber … measured inert" is an ipr-only statement
Measured here: under the −ℓ shift, ipr, the determinant spectrum, the maximum
cell count and the curvature homogeneity are unchanged; **p_site and the
emission field differ**. **Repair:** state the four that coincide and the two
that do not.

### MINOR-11 — the class field is reading-dependent for K3 and K4
Under reading B the menu weight *is* the record count n_ℓ(x), so K3 and K4 read
the record and are not ψ-internal in the declared sense, while `BATTERY_SPEC`
assigns one class per row for both readings. Verdict-inert (they hold on both
stages under both readings), taxonomy-relevant. **Repair:** stamp the class per
reading, or note that under reading B K3/K4 are RECORD-COUPLED and the
ψ-internal count there is 3, not 5.

---

## 5. WHAT I ATTACKED AND COULD NOT BREAK

Recorded so the adjudication knows the negative space: the exit probabilities
and both thresholds (independently rebuilt, exact); the four arms' branch
ladders and unit masses; the composition of unitarity with column-stochasticity;
the det-spectrum claim (no indefinite form at this horizon — verified over all
284,078 leaves); the K9/K10 refusals; the monomial theorem itself (and it
survives adding a self-loop: offsets {0, e₁, e₂, e₁+e₂}, 24 unitary, 0
non-monomial); the scope row (split fiber 0 on a count-1 record is immediate);
the walls (the L-1 sentence is absent; no continuum, BHS or KR reading appears;
both resonances are named and gated); the head's byte-level agreement with §12.

---

## 6. THE SUCCESSOR REGISTER — what the R = 4 arena (paper-21) inherits

**S-EF-1 — the monomial-only theorem transports verbatim, and I can say exactly
when it would die.** The theorem is a property of the *offset set*, not of the
record: it holds iff the declared link set is a Sidon set (all differences
distinct). The R = 4 arena keeps the same nine-actor carrier and the same three
declared directions, so multiplicities stay [1,1,1,1,1,1] and **the coin
register stays forced at R = 4**. It dies the moment a fourth direction is
declared: with offsets {e₁, e₂, e₁+e₂, e₁+2e₂} the multiplicities become
[1,1,1,1,1,1,3,3] and I find **54 non-monomial unitary maps** (witness
c = (1/3, 0, −2/3, −2/3), supported on the line {(1,0), (1,1), (1,2)}). The
mechanism is exact: interference returns exactly when the offset set contains a
coset of a subgroup. **Posed, not solved:** paper-21 must state its offset set
before it inherits F3.

**S-EF-2 — the admissibility margin at G-FLAT is narrower and anisotropic, and
one route reaches an indefinite form.** From the welded (1,1,1) every link
class needs 3 events to reach det 0. From **G-FLAT (1,1,2)** — the R = 4
declared record — the diagonal route needs only **2** events ((1,1,4), det 0),
while an axis route needs **5** and lands at **det = −1/4**: negative, i.e. the
indefinite region this unit measures itself never to reach. Combined with the
return-time schedule (earliest *second* visit to a site is step 3), an R = 4
stage of this shape could exit admissibility as early as **horizon 3**, and
could exit *through* the boundary rather than to it. **Two consequences for
paper-21:** its horizon budget is cheaper than paper-20's, and its Lorentzian
naming discipline is *sharper* than paper-20's — the resonance paper-20 names
and refuses is one indefinite determinant away there. Posed, not solved.

**S-EF-3 — the history-dependent ψ-internal class is UNPROBED, not merely
unexplored.** S-2 as written says "this unit could build only one, and it holds
on both stages". After MAJOR-2 the honest form is: the one row built is not a
live test; when repaired it holds on both stages (measured here, 30 frozen
steps and four coupled levels). So the class has **zero** probed members. The
follow-on is: build a two-time functional that reads the record between the two
times — a return amplitude ⟨ψ_s, U(n_{t−1})…U(n_s) ψ_s⟩ or a stage-echo — and
ask whether *it* fails frozen. That is the only door left open by the staleness
theorem, and it is the door the summit question actually turns on.

**S-EF-4 — the coin fiber is 5, not 1.** Whether the requirement gate returns
NO-WITNESS at the four non-Grover cyclotomic coins is unmeasured. Cheap to
settle at the reduced horizon; verdict-relevant if it ever fails.

**S-EF-5 — the ordering defect is now a number.** open #4's substitute is still
unnamed, but the defect is measured: 3.15× on the exit probability between the
two coin orders at the full horizon, threshold invariant. A successor claiming a
compatibility notion must reproduce or explain that number.

**Scope rows that must travel with any of this:** everything above is at this
arena, this connection (n mod 3), this coin, this horizon; nothing here is a
statement about quantum theory; the admissibility exit is not a singularity, a
signature or a causal reading; the frozen control's safety is not an argument
for fixed backgrounds.

---

## 7. GRADE AND DISPOSITION

**AWF.** The verdict word stands and is the right word. Six MAJORs, all with
exact liftable repairs; five of the six move no delivered number (MAJOR-5 adds
numbers, and I have supplied them for cross-check). MAJOR-3 requires an edit to
a **fenced head block**, so the delivered head is not final; MAJOR-2 and MAJOR-6
are instrument repairs whose outcomes I have already measured, so neither can
change a verdict. The unit's best work — the two-way battery's *design*, the
pre-registered polarity, the mandatory frozen control, the F10 double reading,
the n-mod-3 disclosure, the F12 pricing, and above all the staleness-blindness
theorem — is genuine and should be said to be genuine. Its weakest region is the
choice inventory's non-forced rows, where three of the four "measured" or
"derived" stamps are stronger than their instruments.

**Objects re-verified at close (unchanged during this review):**
paper `b328a8278fac` · code `9e71cf511ab3` · output `3e3d04222782` · receipt
`3ca0308b6c19` · pin `7c6e9e44fc2c` · CR-A adjudication `b7ce00951e5a`.
