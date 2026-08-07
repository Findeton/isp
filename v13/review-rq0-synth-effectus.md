# RQ0-SYNTH — HOSTILE REVIEW, EFFECTUS / CATEGORICAL LENS (R2)

**Reviewer:** R2, structural/conceptual lens — what the verdicts MEAN and
whether the definitions carry them.
**Protocol:** `v13/note-rq0-synth-hostile-protocol.md` (frozen, v13 #181),
kill-shots K1–K5. Primary weight K3, K4.
**Object (SHA-256, first 12, all VERIFIED before reading):**

| file | sha256-12 | status |
|---|---|---|
| `v13/paper-rq0-arena-synthesis.md` | `3a03467dd43e` | matches |
| `v13/code/rq0_synth_census_exact.py` | `5a3d5b0b1704` | matches |
| `v13/code/rq0_synth_census_output.txt` | `ee94cc4c6612` | matches |
| `v13/code/rq0_synth_census_receipt.json` | `0dc2c182b66b` | matches |

**Independent recomputations: 53.** Every number below was rebuilt from the
terminal fixtures with my own code in a scratch directory — my own stabilizer,
my own `act_law`, my own partition join by union-find, my own Bayes error, my
own occupancy defect, my own `Q(i,\sqrt 2)` field for `\Delta^B` — never by
re-running the delivered script alone. The delivered script was run only three
times, under mutant flags, as a probe of instrument behaviour (F5, F6).

**Headline of this review.** Every number in the receipt reproduces. I found
**zero arithmetic errors** in the census. What I did find is that the two
results the unit exists to deliver — the seam asymmetry (K4) and the
invariant/artifact split between the generation profile and the certificate —
are **produced by declarations rather than by measurement**, and that Q-OPT is
given an arena verdict without ever being evaluated at more than one arena
(K3). Three of the nine per-quantity verdicts do not survive as stated.

---

## 0. What reproduces (stated first, in full)

| quantity recomputed independently | delivered | mine |
|---|---|---|
| committed law sizes | 3125 / 21 / 120 / 3006 / 120 | same |
| law×state fibers | 65 | 65 |
| admitted relabellings, summed over fibers | 1073 | 1073 |
| family size `3 × 1073 × 512` | 1,648,128 | 1,648,128 |
| named states, and all 13 ε triples vs the L3 committed receipt | 13, all match | 13, all match |
| census instances per quantity | 3219 | 3219 |
| instances where the configuration moves | 2144 | 2144 |
| Q1 / Q3 / Q4 / Q5 / Q6 / Q7 / Q8 distinct values | 5 / 1 / 40 / 123 / 1 / 14 / 75 | identical |
| every per-coordinate max-distinct (patch/law/state), all 8 rows | as tabled | identical |
| A14 seam atoms (chain) | 2 / 2 / 3 | 2 / 2 / 3 |
| §5.2 preserving families at the legitimate patch, five laws | 1280 / 13 / 120 / 1161 / 60 | identical |
| gauge: free vertices, switchings | 3, 512 | 3, 512 |
| carried holonomy moved / unclosed control moved | 0 / 512, 384 / 512 | 0 / 512, 384 / 512 |
| base holonomy (rank, phase, span) | 1, 4, 1 | 1, 4, 1 |
| `SYN-ST-BROKEN` failures | 2772 / 9072 | 2772 / 9072 |
| name-reader control | 728 / 3219 | 728 / 3219 |
| `\Delta^B(H,H)` | `[[1/2,-1/2],[-1/2,1/2]]` | same, in two independent fields |
| lift-family defect split | 384 non-zero / 128 zero | 384 / 128 |
| six §2 commits, against the successors' own declared bases | as tabled | all six verified |
| all sixteen §2 verdict tokens, against the terminal papers | present | all sixteen present |

The `RQ0-SYNTH-CENSUS-COMPLETE` arithmetic is sound. `ACTION-TOO-WEAK`
correctly did not fire. The §2 record table is essentially verbatim-faithful
(one strengthening, F14). This review is about what the numbers are made to
mean, not about the numbers.

---

## 1. Findings

### F1 — `ARENA-INVARIANT-Q8` is definitional, not measured, and survives replacing the seam by its lattice opposite (K4, THE FLAGGED HEADLINE)

**Severity: MAJOR. Blocking for the successor rung.**

**Evidence, three independent strands.**

*(a) Q8 is structurally blind to the coordinates it is said to survive.* An AST
scan of each quantity's body, over the delivered source, gives the parameters
each actually references:

| Q | declared READS | parameters the body references |
|---|---|---|
| Q1 | law | `law_id, law` |
| Q2 | lift family | `lifts` |
| Q3 | law | `law_id, law` |
| Q4 | patch, law | `part, law_id, law` |
| Q5 | patch | `part, law_id, law` |
| Q6 | patch | `part, rho` |
| Q7 | patch | `part, law, rho` |
| **Q8** | **patch** | **`part, sigma`** |

`q8_cross_arena_overlap` never touches `law` or `rho`. Its "does not move with
the law, does not move with the state" is therefore a fact about its signature,
not a measurement — the identical situation the census itself reports as
*structural* rather than measured for the switching coordinate
(`SYN-SWITCH-SCOPE`: "no amplitude object is named in this quantity's
definition"). The instrument applies two standards to the same phenomenon and
applies the flattering one to the headline.

*(b) The three declarations are a chain, so the seam is a lattice maximum.* I
recomputed the join by union-find, independent of `CB.part_meet`, and agree on
all nine declared pairs: `PI1 = 01|2|3|4` refines `P22 = 01|23|4` refines
`PTOMO = 0123|4`. The seam of any two is the coarser one. §5.3 says this
outright. What two declared patches share is then `max` in a three-element
chain — a lattice identity involving no law, no state, no process.

*(c) The verdict is orientation-blind.* Running the delivered instrument under
its own `seam-orient` mutant, which replaces the meet by the join inside Q8
(the seam by its lattice opposite), the census still returns
**`ARENA-INVARIANT-Q8`**, and `SYN-ST-RELABEL` still passes. Only the typed
anchor A14 dies. A verdict that holds for the seam and for its opposite is not
a verdict about the seam.

**Consequence for §5.3, the abstract, and §9.2.** "The seam is the finding worth
carrying forward" and "What two declared patches share does not [move]" claim a
measurement that was not made. §9.2 then licenses "the seam datum" for claims of
physical significance on that basis.

**Repair that would satisfy me.** Re-enter Q8 with its blindness measured and
declared exactly as `SYN-SWITCH-SCOPE` does it: a source scan showing that Q8's
definition names no law and no state object, its law/state columns reported
`structural`, and the verdict restated as `ARENA-INVARIANT-Q8 [structural in
law and state; measured only in the relabelling coordinate]`. Delete "the
finding worth carrying forward" and the §9.2 licensing of the seam, or replace
them with the true statement, which is worth saying plainly: *the shared content
of two declared patches is a boundary-algebra fact, so it cannot be
arena-relative — and that is a definitional observation, not a census result.*
Add a seam-orientation gate (not merely an anchor) so that `seam-orient` kills a
gate.

---

### F2 — Q4 and Q5 read the same two coordinates and share a computed component; the opposite verdicts come from the READS declaration alone (K5, Deviation 3)

**Severity: MAJOR. Blocking for §9.2.**

**Evidence.** Q4's third component is `len(L2.pres_of(law, part))`. Q5's
certificate carries the preserving-family size as `value[1][1]`. The receipt
anchors both to the *same triple*: A18 commits Q4's component to
`[1280, 240, 420]`; A17 commits Q5's to `[1280, 240, 420]`. The AST table in F1
shows both bodies reference `part, law_id, law`. Their dependence profiles agree
exactly, and I reproduced both: patch max-distinct 3, law max-distinct 5.

They are declared oppositely. Q4: `reads = (patch, law)`. Q5: `reads = (patch)`,
`acts = (law, …)`. The verdict rule is
`moved_in_acting = [c for c in acts if dep[c]["moves"]]`. So Q4's law-movement
is invisible to the rule and Q5's is decisive:

- Q4 → `ARENA-INVARIANT-Q4`
- Q5 → `ARENA-ARTIFACT-Q5`

with identical underlying dependence. §3.3's justification — "Q1, Q3 and Q4 are
nomological quantities, so the law is their argument; Q5 … is a patch quantity"
— is a stipulation about two objects that share a component computed by the same
call.

Deviation 3's stated mitigation ("the census measures and prints the full
dependence profile of every quantity over every coordinate, so a reader who
disputes a declaration can read the measurement off the same table") does **not**
mitigate. The profiles are printed and they are the same; what differs is only
the label the rule attaches. And the labels are not inert: §9.2 uses exactly this
split to license Q4 for claims of physical significance and to bar Q5.

**Does a different declaration flip a verdict? Yes, and the pre-registered
controls with it.** Declaring the law to be Q5's argument as it is Q4's turns Q5
`ARENA-INVARIANT`, and `SYN-NEGATIVE-CONTROL` — a must-pass gate — then fails.
Declaring the law *acting* on Q4 as it acts on Q5 turns Q4 `ARENA-ARTIFACT`.
Declaring the law acting on Q1 turns the declared positive control into an
artifact and fails `SYN-POSITIVE-CONTROLS`. The census's entire control structure
is a function of a declaration the pin does not fix and Deviation 3 admits it
does not fix.

**Repair.** Either (i) give a criterion for READS that is decidable from the
quantity's source — as `SYN-SWITCH-SCOPE` already does for the amplitude
coordinate — and apply it uniformly, in which case Q4 and Q5 must receive the
same law-status and one of the two verdicts changes; or (ii) keep the
stipulation and demote §9.2 accordingly: state that the invariant/artifact split
between Q4 and Q5 is a *declaration*, that both quantities move with the law
identically, and that neither is licensed for a physical claim on the strength of
this census.

---

### F3 — Q-OPT is never evaluated at more than one arena; the 576 pairs are a two-line identity; the zero clause is unfalsifiable (K3)

**Severity: MAJOR.**

*(a) The transport is genuinely exact.* I rebuilt `\Delta^B` twice: once through
v12 paper 1's own committed field (`v12/paper1_code/exact.py`, `Cyc(8)`, its own
`born`), and once in a different coordinate system of my own — `Q(i,\sqrt 2)` in
the basis `(1, \sqrt2, i, i\sqrt2)` over Fractions, sharing no code with the
census. Both give `\Delta^B(H,H) = [[1/2,-1/2],[-1/2,1/2]]`, matching the census
and matching v12's committed anchor. **The K3 transport claim is upheld.** No
`BLOCKED-AT-IMPORT` was owed.

*(b) The 576-pair census is vacuous, and not merely because of the named
obstruction.* `run_qopt` builds `Ua`, `Ub` as 0/1 permutation matrices (`Z1`,
`Z0`). For a 0/1 matrix, `B(U) = U` entrywise, and the product of two
permutation matrices is again 0/1, so
`\Delta^B = U_2U_1 - U_2U_1 = 0` identically — for every pair, every carrier
size, no computation required. I confirmed exhaustively over **all 14,400**
pairs (0 non-zero), so the `[SAMP]` disclosure over "576 of the 14,400" mis-states
the epistemic situation: there is no sampling risk, and the sample is not a
sample of anything hard.

*(c) The sweep silently fixes the arena's own phase coordinate.* The admitted
reversible operations' unitary lifts are the **monomial** matrices — permutation
times phases — which is what §8 itself says. The census sweeps only the
phase-trivial ones. The very coordinate the arena family declares as `φ` is held
fixed at zero throughout Q-OPT, undisclosed. (The conclusion survives: I checked
4,000 random phased monomial pairs, all zero — `B` of a monomial unitary is its
permutation matrix, so the defect vanishes for the same one-line reason.)

*(d) No arena coordinate ever varies in Q-OPT.* Neither `d`, `L`, `\rho`,
`\sigma` nor `\varphi` enters the value computation. Consistently, Q-OPT has no
row in §5.1, no distinct-values count, no dependence profile, no equivariance
column — unlike all eight censused quantities. **`ARENA-INERT-Q-OPT`, "at its
neutral value on every admissible arena", is an inference, not a census.**

*(e) The zero clause has no mutant.* `SYN-QOPT-VALUE` is
`nz == 0 and ctrl_nonzero and pairs > 0`. Under `born-lax` (`born(A) = A`) the
defect is `U_2U_1 - U_2U_1 = 0` and `nz` stays 0; the mutant kills the gate only
through the `ctrl_nonzero` conjunct. No declared mutant can falsify the
`nz == 0` clause. That is the RUNBOOK Appendix's "#36" failure — a gate carried
by a table that nothing can break.

**Repair.** State the identity instead of sweeping it: `B` is multiplicative on
monomial unitaries because `B` of a monomial unitary is its underlying
permutation matrix; hence `\Delta^B \equiv 0` on all admitted operations, for all
phases, exhaustively and by proof. Drop the `[SAMP] 576 of 14,400` framing, which
implies a risk that does not exist. Either sweep `\varphi` or declare Q-OPT
phase-fixed. And either give Q-OPT a dependence-profile row like every other
quantity, or say plainly in §8 and §10 that Q-OPT was not censused across arenas.

---

### F4 — the Q-OPT verdict is a vocabulary hybrid the pin does not authorize (K3)

**Severity: MODERATE.**

The pin's four outcomes are `ARENA-INVARIANT` / `ARENA-INERT` /
`ARENA-ARTIFACT` / `BLOCKED-AT-⟨object⟩`, and the paper's own §3.4 defines
`BLOCKED-AT-⟨object⟩` as "**the census cannot be run** for want of a named
object" and asserts "Only the pin's four names are used." §8 then enters, for one
quantity, `ARENA-INERT-Q-OPT` **and**
`BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION`, the second rendered in
verdict-code font as a name rather than as prose. Two of the four names, for one
quantity, one of them repurposed from "cannot be run" to "the obstruction to
content".

The pin reserved `BLOCKED-AT-IMPORT` for transport failure, which did not occur;
that part is compliant (Deviation 4 is honest). What is not authorized is
minting a second `BLOCKED-AT-⟨object⟩` token for a quantity that also carries a
positive verdict. Combined with F3(d) — the census was in fact not run across
arenas for this quantity — the two candidate compliant readings are: keep
`ARENA-INERT-Q-OPT` and demote the obstruction to prose with no code font; or
enter `BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION` alone, which is the
honest reading if F3(d) is accepted. Either is fine. Both is not.

**Repair.** Pick one. If `ARENA-INERT-Q-OPT` is kept, the obstruction sentence
must be plain prose and §3.4's "Only the pin's four names are used" must be
amended to say that one quantity carries an obstruction annotation outside the
vocabulary.

---

### F5 — a wrong value-transport reverses the paper's headline verdict and the §14 self-test still passes (K5)

**Severity: MAJOR.**

`SYN-ST-RELABEL` restricts itself to `inv = [q for q in R if R[q]["verdict"]
.startswith("ARENA-INVARIANT") or …("ARENA-INERT")]` — the self-test's scope is
set by the verdicts it is supposed to audit. Running the delivered instrument
under its own `transport-lax` mutant:

| | delivered | under `transport-lax` |
|---|---|---|
| Q4 | `ARENA-INVARIANT-Q4` | **`ARENA-ARTIFACT-Q4`** |
| Q8 | `ARENA-INVARIANT-Q8` | **`ARENA-ARTIFACT-Q8`** |
| `SYN-ST-RELABEL` | PASS | **PASS** |
| `SYN-CENSUS-COMPLETE` | PASS | **PASS** |
| `SYN-NEGATIVE-CONTROL` | PASS | **PASS** |

The mutant reverses the paper's flagged headline and the §14 self-test does not
notice, because the quantities that fail have been reclassified out of its scope.
The mutant is caught by exactly one gate, `SYN-Q4-NAME-BLIND`, which hard-codes
Q4. Had the pin not independently required name-blindness gated first, a wrong
transport would have produced a fully coherent receipt with reversed verdicts and
zero must-pass failures.

A self-test whose scope shrinks to its own survivors cannot fail. That is
structurally the same defect §14 was written to prevent.

**Repair.** Run `SYN-ST-RELABEL` over **all** quantities, not over the ones the
census already gated fixed, and report per-quantity. Add a per-quantity transport
gate so that a wrong transport kills the quantity's own gate rather than
silently changing its verdict.

---

### F6 — the discrimination counts do not discriminate; four of the six relabelling columns are vacuous (K2, the ω lesson)

**Severity: MODERATE.**

The paper's anti-vacuity device is the count of instances "of which 2,144
actually move the configuration", stated as the reason "a vacuous pass would be
visible". I measured what moves. **No admitted relabelling moves the law
(0 of 1073) and none moves the state (0 of 1073)** — the stabilizer fixes ρ
pointwise and L setwise by construction. So "moves the configuration" means
"moves the patch", and 2,144 is the patch-moving count. Then:

| Q | its relabelling column | what the test actually compares |
|---|---|---|
| Q1 | 0 / 3219 | `L = σ·L`, i.e. the group's own defining property. Tautology. |
| Q2 | 0 / 3219 | the body reads only `lifts`; transport is the identity; the memoised object against itself. **Fully vacuous.** |
| Q3 | 0 / 3219 | the admissible set is the singleton `0\|1\|2\|3\|4` (recomputed), fixed by every permutation. Tautology. |
| Q4 | 0 / 3219 | genuine: branch C's equivariance of the generation profile. **Real content.** |
| Q7 | 0 / 3219 | ω ≡ 0, transport the identity: `0 == 0`. Vacuous. |
| Q8 | 0 / 3219 | genuine: `σ` enters the body and relabels the other declared patches. **Real content.** |

Four of the six are vacuous or tautological, and the discriminating count is
identical (2,144) in all six rows because it counts movement of a coordinate four
of them do not read. A constant function would post the same 2,144.

**Repair.** Report the discrimination per quantity as *instances in which the
quantity's own arguments moved*, not in which the configuration moved. On that
measure Q2's and Q7's columns are 0 and the vacuity is visible, which is what the
device is for.

---

### F7 — §7's self-test is the census's own relabelling column recomputed, presented as an independent check

**Severity: MODERATE.**

19,314 = 6 × 3,219 and 12,864 = 6 × 2,144 (both verified). `run_selftest`(a)
performs the same comparison as `run_census`'s `equi_fail` counter over the same
memoised evaluations; `fixed = tested − equi_fail` identically. The receipt
states the one-computation-two-reports convention explicitly for the gauge sweep
("one computation, reported twice, stated as such") and does **not** state it
here. §7.1 reads as a second, larger measurement.

**Repair.** Say it, as the gauge sweep already does: §7.1 is the census's
relabelling column re-reported across the six quantities gated fixed.

---

### F8 — `SYN-ST-BROKEN`'s stated mechanism cannot bite, and all its teeth are Q8's

**Severity: MODERATE.**

The docstring and §7.3 describe the control as "the patch is relabelled while the
law and the state are left alone, which is the classic transport bug". But the
true action *also* leaves the law and the state alone — necessarily, since no
admitted σ moves either (F6, 0 of 1073 each). The only difference between the
broken path and the true path is the `sigma` argument handed to the quantity
function, which only Q8 reads. Measured, per quantity:

| Q | failures under the broken action |
|---|---|
| Q1 | **0** of 3024 |
| Q4 | **0** of 3024 |
| Q8 | **2772** of 3024 |
| total | 2772 of 9072 (matches) |

So §7.3's "the quantities the census gates invariant fail under it" is one
quantity of the three tested, and the mechanism named is not the mechanism
operating. This is the RUNBOOK's own #38→#40 rule: describe mechanisms as
measured, not as intended.

**Repair.** Restate: the mis-conventioned control is *the other declared patches
left unrelabelled*, it bites on Q8 only, and Q1 and Q4 are insensitive to it by
construction. A second broken action with teeth against Q4 would strengthen the
test considerably.

---

### F9 — Deviation 5's stated characterisation of the 128 is false (K3)

**Severity: MODERATE — a wrong explanatory claim about a computed set.**

Deviation 5: "the remaining 128 are the phase choices whose square is again
non-monomial, where the Born map happens to compose." Measured over the 512-member
declared lift family, in my own field:

| | count | square monomial | square fully unbiased |
|---|---|---|---|
| defect zero | 128 | 0 | **128** |
| defect non-zero | 384 | 128 | **0** |

"Square again non-monomial" holds for **384** of the 512 — it fails to single out
the 128, and **256 non-zero lifts also have a non-monomial square**. The correct
characterisation, which I verified is exact and two-sided, is: `\Delta^B(U,U)=0`
iff `U^2` is again **fully unbiased** — every entry of modulus `2^{-1/2}` — since
`B(U) = B(U)B(U)` is the flat matrix for all 512 and the defect is
`B(U^2)` minus the flat matrix. The second clause of the deviation ("where the
Born map happens to compose") is true but is a restatement of the conclusion, not
a reason.

**Repair.** Replace "non-monomial" with "fully unbiased" and cite the two-sided
count 128/128 and 0/384.

---

### F10 — no quantity is evaluated at more than 3,219 of the 1,648,128 arenas (K1, K2)

**Severity: MODERATE.**

The family size is correct and correctly computed (I reproduce 3 × 1073 × 512),
but each quantity's census sweep is 3,219 arenas — 0.195% of the family — with
the remaining factor of 512 handled by `SYN-SWITCH-SCOPE`'s source-scan argument.
Q2, the only quantity swept over φ, reads none of `d, L, ρ, σ`, and its φ-sweep is
`[SAMP]` over 32 of 512 lifts. So the headline family size indexes nothing that
was computed at that size.

The structural argument is legitimate — a function naming no amplitude object
cannot see φ — and it is disclosed in the gate. What is not disclosed in §5.1,
§7.1 or the abstract is the resulting sweep fraction; the abstract's "3,219
instances per quantity" sits next to "its size is 1,648,128" without the relation
between them being stated.

**Repair.** One sentence in §5.1: each quantity is evaluated at 3,219 of the
1,648,128 arenas; the remaining factor of 512 is argued structurally by
`SYN-SWITCH-SCOPE` and swept only for Q2.

---

### F11 — Q1's nondegeneracy witness is not ambient, and Q8's is a tautology outside the gate (K2, K4)

**Severity: MODERATE.**

§3.4 requires, for `ARENA-INVARIANT`, "a declared **ambient witness outside the
family**". Two of the five witnesses do not meet it.

*Q1.* The witness is "the five committed laws themselves" — inside the family,
being its `L` coordinate. Its value (5 distinct transition data) is Q1's own law
column recomputed. It is not ambient and it is not independent.

*Q8.* The witness is `len({pk(CB.part_meet(p, ONEATOM)) for p in PATCHES}) = 1`.
The meet of any partition with the one-block partition is the one-block
partition, so this is a lattice identity whose value is 1 for any three patches
whatsoever. It is computed with `CB.part_meet` **directly, never through
`q8_cross_arena_overlap`** — a broken Q8 would post the same 1. And it does not
enter the gate: `SYN-NONDEGENERACY`'s boolean is

```
nz > 0 and len(idf) > 0 and proper > 0 and len(amb) > 1
    and wit["Q1"]["distinct_transition_data"] == len(fam["laws"])
```

— Q7, Q3, Q2, Q1 only. **Q8's nondegeneracy is asserted in §5.3 and §6 and gated
nowhere.** By §3.4's own definition of `ARENA-INVARIANT`, the label is
consequently unearned for Q8 independently of F1.

The other three witnesses are sound and I say so: Q7's runs `L4.omega_fast`, the
same function as Q7, over 775 ambient instances (201 non-zero, verified); Q2's
runs `L5.cycle_basis_holonomies`, the same function as Q2, over the ambient
non-unitary phase quadruples (8 values against 1); Q3's uses an independent
route.

**Repair.** Put Q8 in the gate with a witness that runs through
`q8_cross_arena_overlap` and is not a lattice identity — for instance a
non-chain triple of declared boundaries, where the seam is not simply the coarser
member. Replace Q1's witness with an object outside the five committed laws, or
withdraw the nondegeneracy claim for Q1 and record its constancy as
structural.

---

### F12 — §5.2 misnames the clause that does the killing

**Severity: MINOR-MODERATE.**

§5.2: "under `REV` the reachability clause fails where under every other
committed law it holds." Recomputed: `reach` is `[0,1,2,3,4]` at all five laws —
reachability itself does not differ. The clause that fails at `REV` and only at
`REV` is **(ii-b)**, which the terminal B″ paper names **"Occupied"**, via
`unrealized_identifications`. That paper reserves "Reachability" for the order on
configurations and firewalls it explicitly against any spatial, causal or
temporal reading. The synthesis borrows the firewalled word for the wrong clause,
in the one sentence whose content is which clause kills.

**Repair.** "under `REV` the occupancy clause (ii-b) fails".

---

### F13 — the fibration is faithful but nearly law-blind (K1)

**Severity: MINOR.**

K1 asks whether the fibering smuggles arena-dependence into the action. It does
not, but it delivers less than §3.1 implies. Recomputed fiber sizes:

- `DET`, `FUNNEL`, `REV`, `FUNNEL-CLOSURE`: **identical** size vector at all 13
  states — `[24,120,24,6,6,6,6,24,6,1,6,24,12]`, 265 each.
- `COUNTER-LAW`: **trivial (1) at every one of the 13 states**.
- Total 4 × 265 + 13 = 1073. Trivial fibers: 17.

So "a fibered product over the 65 law-state pairs" yields exactly two distinct
fiber patterns, and 98.8% of the relabelling coordinate is the state's stabiliser
alone. The dependence on the law is real (branch C Thm 7.1 is correctly cited)
but degenerate.

On the sharper form of K1's attack — could a quantity be invariant only because
the fiber group is small where it would move? — the answer is no for a specific
reason: the group is trivial exactly at `COUNTER-LAW` and at the asymmetric
full-support state, and the quantities that move (Q5 under law, Q6 under state)
move in coordinates the relabelling coordinate does not touch. No verdict turns
on a small fiber. **K1's smuggling attack fails; the family is sound.**

**Repair.** One clause in §3.1 recording that the fibration yields two distinct
patterns, so the reader knows what the fibering bought.

---

### F14 — one strengthening-in-paraphrase in the §2 record table

**Severity: MINOR-MODERATE.**

I checked all six rows against the terminal papers' own verdict language. Five
are faithful, including the delicate ones: row 1's "the block is law-independent"
is verbatim from the Cycle B paper, which itself separates the law-independent
top-of-lattice block from the law-scoped covariance remark, and the synthesis
does not collapse them; row 3's "impossible" matches Theorem 8.5/6.1; row 6's
"unitarity-forced" matches branch A's "forced by unitarity"; row 4's inverted
ordering and least-positive-defect claim recompute correctly (1/16 is the minimum
positive defect at the committed state and is attained by the 2+1+1 forgery).

Row 5 carries its scope qualifier ("at a full-group configuration") but drops
what the terminal paper attaches to it: "stated over the class it covers and no
wider: the full-group hypothesis is carried by **25 of the 4845** declared states,
and 1200 carry no symmetry at all." The synthesis's gloss — "the coarse present
cannot testify" — is then reused **unqualified** in §1's thesis clause ("not
law-remembered"). That is the thesis sentence, so the strengthening propagates to
the paper's title claim.

**Repair.** Carry the 25-of-4845 scope into row 5 and qualify the §1 clause.

---

### F15 — two minor traceability defects

**Severity: MINOR.**

*(a) A19 does not reach outside v13 as instrumented.* §4: "One anchor reaches
outside v13: `\Delta^B(H,H)` … rebuilt here in exact `Q(\zeta_8)` and equal to
the committed value." The committed side is a **typed literal** in the census
source; nothing reads `v12/paper1_code`. I verified the literal against v12's own
field and it is correct, so no number is wrong — but the cross-corpus check is a
narrative, not an instrument. Repair: import or recompute v12's value, or say
"equal to the value this paper records as v12 paper 1's".

*(b) §5.2 types two numbers the receipt does not carry.* `1161` and `60` (the
preserving families under `FUNNEL-CLOSURE` and the counter-law) appear nowhere in
`rq0_synth_census_receipt.json`. I recomputed all five and all five are correct.
Repair: anchor the five-law preserving-family vector, per RUNBOOK "counts
computed, never typed".

---

## 2. Kill-shot dispositions

| | verdict |
|---|---|
| **K1 — the family** | **SOUND.** 1,073 / 65 / 1,648,128 independently reproduced; the fibration is faithful to branch C Thm 7.1 and no verdict turns on a small fiber. Deviation 1 is correct and the flat product would indeed over-count. One disclosure gap (F13) and one sweep-fraction gap (F10). |
| **K2 — verdict soundness** | **NUMBERS SOUND, TWO CONTENT GATES VACUOUS.** All orbit counts and sweeps reproduce exactly (Q5 = 123 under law, Q6 = 14 under state with 8 at one patch, Q1/Q4 0 of 3219 with name-blindness gated first, Q8 fixed under law and state). No `[SAMP]` hides inside a claimed exhaustive sweep — the three samples are all disclosed in §10, and I confirmed the gauge sweep is exhaustive over 512 switchings. But the nondegeneracy gate omits Q8 and Q1's witness is not ambient (F11), and four of six relabelling columns are vacuous (F6). The INERT/INVARIANT boundary itself is sound: Q7's inertness is genuinely witnessed (201 of 775, through Q7's own function), and the `route2` independent check is real. |
| **K3 — Q-OPT** | **TRANSPORT UPHELD; THE CENSUS REFUTED.** The arithmetic transports exactly, confirmed against v12 paper 1's own committed field and again in a field of my own construction. The 576 pairs are vacuous by a two-line identity, exhaustively confirmed over all 14,400; the sweep silently fixes the arena's φ coordinate; no arena coordinate is ever varied; the `nz == 0` clause is unfalsifiable by any declared mutant. The verdict vocabulary is a hybrid the pin does not authorise (F4). |
| **K4 — the asymmetry** | **REFUTED AS STATED.** Q8's invariance is definitional, not degenerate — it is not "secretly inert", it is *structurally blind* to the coordinates it is said to survive. Q5 and Q8 face the same sweep but not the same sensitivity surface: Q5 reads the law, Q8 cannot. The chain structure does trivialise the seam datum (seam = the coarser member, a lattice maximum), and the verdict survives replacing the seam by its lattice opposite. And the paper claims more than the census shows: "the finding worth carrying forward", and §9.2's licensing of the seam for physical significance. |
| **K5 — instrument integrity** | **CONTROLS PARTLY TOOTHLESS.** All four self-test numbers reproduce exactly (19,314 / 384 of 512 / 2,772 of 9,072 / 728 of 3,219). But 19,314 is the census's own column recomputed (F7); 2,772 is Q8 alone under a mechanism not the one described (F8); `transport-lax` reverses the headline with the self-test passing (F5). Mutant audit: 6 of 20 are self-referential anchor-flips testing only the reporting plumbing; `transport-lax` and `seam-orient` are killed by the wrong gate class; `hol-sign` and `hol-orient` are caught by anchor A09 and **not** by `SYN-ST-SWITCH`, the §14 gauge self-test written for exactly that failure. READS-vs-ACTS does flip verdicts, decisively (F2). The §2 table is verbatim-faithful in five of six rows (F14); all six commits and all sixteen verdict tokens verified. |

---

## 3. What the unit does earn

I want the adjudicator to have this separated out, because it is real and the
findings above should not bury it.

1. **`ARENA-ARTIFACT-Q5` is earned and is the thesis measured.** 123 certificates
   for a fixed declaration, moving with the law, with the five preserving-family
   sizes recomputed and correct. The same declared patch is certified differently
   in different admissible arenas. This is the paper's actual result.
2. **`ARENA-ARTIFACT-Q6` is earned**, 14 values, 8 at one patch under the state
   alone, and its reading as an instrument rather than a conclusion is right.
3. **`ARENA-INVARIANT-Q2` is earned**, and it is the one quantity with a genuine
   symmetry sweep: 512 switchings exhaustively, carried invariant fixed, the
   unclosed control moving on 384 — all independently reproduced, including the
   holonomy value (rank 1, phase 4, span 1).
4. **`ARENA-INERT-Q7` is earned**, with the only nondegeneracy witness in the
   paper that is both ambient and runs through the quantity's own function.
5. **Q4's name-blindness gate is the one gate in the instrument with real teeth**
   — it is what catches `name-reader`, `transport-lax` and `stab-lax`.
6. **The pin's process discipline was followed**: the freeze precedes fixture
   truth with the evaluation counter at zero, the deviations ship, the family
   size is computed and not typed, and no float enters any path.

---

## 4. Required fixes, ranked

| # | fix | blocking? |
|---|---|---|
| 1 | Restate Q8's law/state invariance as **structural**, on the `SYN-SWITCH-SCOPE` model; withdraw "the finding worth carrying forward" and the §9.2 seam licence, or replace with the definitional statement (F1) | **yes — blocks the successor rung** |
| 2 | Resolve the Q4/Q5 READS asymmetry, either by a source-decidable criterion applied uniformly or by demoting §9.2's licensing split to a declaration (F2) | **yes — blocks §9.2** |
| 3 | Restate Q-OPT: prove the monomial identity instead of sampling it; disclose the fixed φ; either censusize Q-OPT across arenas or say it was not censused (F3) | **yes** |
| 4 | Pick one verdict name for Q-OPT (F4) | yes |
| 5 | Run `SYN-ST-RELABEL` over all quantities, not the survivors; add per-quantity transport gates (F5) | yes |
| 6 | Report discrimination against the quantity's own arguments (F6); label §7.1 as the census column re-reported (F7); restate `SYN-ST-BROKEN`'s mechanism and its Q8-only teeth (F8) | no |
| 7 | Correct Deviation 5 to "fully unbiased", with 128/128 and 0/384 (F9) | yes — it is a false claim |
| 8 | Gate Q8's nondegeneracy through Q8 with a non-chain witness; fix or withdraw Q1's non-ambient witness (F11) | yes |
| 9 | Sweep fraction sentence (F10); "occupancy clause (ii-b)" (F12); fiber-pattern clause (F13); row-5 scope and the §1 thesis clause (F14); A19 provenance and the five typed sizes (F15) | no |
| 10 | Add a seam-orientation gate and a `SYN-ST-SWITCH` clause that a holonomy sign/orientation mutant can kill, so §14's own lesson is enforced here | no, but recommended |

---

## Grade

**ACCEPT-WITH-FIXES.**

Every number in the receipt reproduces under independent reconstruction — 53
recomputations, zero arithmetic errors, and the family, the eight orbit counts,
the four self-test counts, the gauge sweep and the `\Delta^B` transport all
survive a hostile rebuild. The instrument is honest about its samples, its
freeze order is genuine, and `ARENA-ARTIFACT-Q5` — the thesis measured — is fully
earned. Nothing needs recomputing.

What needs changing is what the paper claims. Three of the nine verdicts do not
survive as stated: `ARENA-INVARIANT-Q8` is definitional rather than measured and
survives replacement of the seam by its lattice opposite (F1);
`ARENA-INVARIANT-Q4` against `ARENA-ARTIFACT-Q5` is produced by a READS
declaration over two quantities that share a computed component and read the same
coordinates (F2); and `ARENA-INERT-Q-OPT` is inferred from a two-line identity
rather than censused across arenas, under a vocabulary hybrid (F3, F4). Fixes 1,
2, 3, 4, 5, 7 and 8 are mandatory, and fixes 1 and 2 must land before the seam
result feeds any successor rung — as the protocol says it is intended to.

I would move to **REJECT** if the adjudication declines fix 1 or fix 2, since in
that case the paper's abstract, §5.3, and §9.2 would continue to assert
measurements the census did not make.
