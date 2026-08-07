# RQ0-SYNTH — HOSTILE REVIEW, OPERATOR / ALGEBRAIC LENS (R1)

**Reviewer:** R1, operator/algebraic lens. **Date:** 2026-08-07.
**Protocol:** `v13/note-rq0-synth-hostile-protocol.md` (sha256-12 `019f1cbf9f5a`),
kill-shots K1–K5 binding. **Pin:** `v13/note-rq0-synth-arena-pin.md`
(`f74a8511b204`). **RUNBOOK §13–§15** read and applied (§14 symmetry self-test,
§15 declared-arena discipline).

**SHA verification, before reading (all four match; none mismatched):**

| object | required | on disk |
|---|---|---|
| `v13/paper-rq0-arena-synthesis.md` | `3a03467dd43e` | `3a03467dd43e` |
| `v13/code/rq0_synth_census_exact.py` | `5a3d5b0b1704` | `5a3d5b0b1704` |
| `v13/code/rq0_synth_census_output.txt` | `ee94cc4c6612` | `ee94cc4c6612` |
| `v13/code/rq0_synth_census_receipt.json` | `0dc2c182b66b` | `0dc2c182b66b` |

The receipt's registered `source_sha256` (`5a3d5b0b17049ef8…`) equals the on-disk
script hash. No git command was run. Delivery mode (`--falsification-selftest`)
was **not** run, so no artifact was written by this review; the one mutant run
performed (`--mutant transport-lax`) writes nothing by the delivered write guard.
All recomputation was done with my own scripts in the scratchpad, built on the
terminal L2–L5 fixture modules, never by re-running the delivered census alone.

**Independent recomputations performed: 142.** Enumerated in §7.

---

## 0. Headline

**Every number in the delivered artifacts is right.** I rebuilt the arena family,
the fibration, all eight census rows, all four self-test controls, all five
nondegeneracy witnesses, the Q-OPT stack and the §2 record table from the
terminal fixtures, and **I could not move a single value.** |𝒜| = 1,648,128 is
correct and the fibration is the correct count of admissible tuples, not a
smuggle (K1 answered in the unit's favour, §1).

What I can move is the **evidentiary layer**. Four of the five kill-shots land
there:

- three of the six "0 failures / 3,219" equivariance rows are `x == x` on the
  same memoized object, and a fourth is `0 == 0` (M1);
- the §14 self-test **survives its own transport mutant** — I ran it (M2);
- the INERT/INVARIANT predicate for the paper's headline quantity Q8 returns
  False when fed Q8's own constructed neutral, so `ARENA-INERT-Q8` is
  unreachable by construction (M3) — the ω lesson, defeated at the one place
  the pin says it must not be;
- `ARENA-INVARIANT-Q4` and `ARENA-ARTIFACT-Q5` rest entirely on an
  undetermined declaration, on identical measured law-dependence (M4);
- the flagged asymmetry compares a law-consuming quantity against a law-blind
  one, on naming-inflated counts one of which the paper discounts and the
  other of which it does not (M5).

None of this makes a stated number false. All of it makes the *verdicts* weaker
than §9.2's physical-significance clause requires of them. **Grade: ACCEPT-WITH-FIXES**
(§8), with eleven named repairs.

---

## 1. K1 — THE FAMILY. Verdict: **SOUND. The fibration does not smuggle.**

I rebuilt every factor from scratch, including a from-first-principles
stabilizer predicate (fix ρ pointwise, fix the preparation setwise, fix the law
setwise under σ·L = {σFσ⁻¹}), and checked it against `L4.stabilizer` on all 65
fibers.

| factor | delivered | my recomputation |
|---|---|---|
| patch declarations | 3 | 3 |
| named states | 13 | 13 (parsed from L3 source; all 13 ε-triples cross-checked against L3's *committed receipt* `the_state_map`) |
| committed laws | 5 (3125, 21, 120, 3006, 120) | 5, same sizes |
| law×state fibers | 65 | 65 |
| Σ over fibers of \|G(L,ρ)\| | 1073 | **1073** |
| fiber-size histogram | {1:17, 6:24, 12:4, 24:16, 120:4} | **identical** |
| free loop vertices / switchings | 3 / 512 | 3 / 512, from the diagram |
| **\|𝒜\|** | **1,648,128** | **3 × 1073 × 512 = 1,648,128** |

My stabilizer agrees with `L4.stabilizer` on **all 65 fibers**, element for
element.

**Is the fibration faithful to the pin's flat wording?** Yes, and it is forced.
The pin writes `× admitted relabelling ∈ the admitted-isomorphism group`, but
that group has no referent until (L, ρ) is named. 3 × Σ|G(L,ρ)| × 512 is exactly
the count of admissible 5-tuples; the union of all fiber groups is only 120, so
a "flat" reading has no defensible number at all. Deviation 1 is correct and
correctly reasoned.

**Does the fibering let a quantity be "invariant" only because the fiber is
small where it would move?** No, and the reason is structural: **the identity
relabelling lies in every one of the 65 fibers** (verified). Therefore the
σ = identity slice *is* the flat 3 × 5 × 13 product, and every declared-acting
coordinate is compared there at full width. I recomputed the entire dependence
profile **on the identity slice alone**:

```
Q    patch moves/max   law moves/max   state moves/max
Q1   False / 1         True / 5        False / 1
Q2   False / 1         False / 1       False / 1
Q3   False / 1         False / 1       False / 1
Q4   True  / 3         True / 5        False / 1
Q5   True  / 3         True / 5        False / 1
Q6   True  / 3         False / 1       True  / 8
Q7   False / 1         False / 1       False / 1
Q8   True  / 3         False / 1       False / 1
```

Row for row identical to the delivered fibered table. **The fibration neither
creates nor suppresses a single patch/law/state `moves` verdict.** K1's central
attack fails.

**Where the fibration does bite (undisclosed — finding D6).** The fibered family
constrains which (realized patch, state) pairs co-occur. ε's range over a flat
product of realized patches × the 13 states is **17 values**; over the fibered
family it is **14** — the delivered number. The fibration therefore suppresses
three ε values that a flat reading would report. This does not change Q6's
verdict, but it is the fibration doing real work on a reported quantity and it
is nowhere disclosed. See F9.

---

## 2. K2 — VERDICT SOUNDNESS. Numbers **all reproduce**; the boundary is **defective**.

### 2.1 The orbit counts and sweeps — all confirmed

My own sweep, my own quantity wrappers, my own canonicalization:

| Q | delivered | mine | patch | law | state | equivariance |
|---|---|---|---|---|---|---|
| Q1 | 5 | **5** | F/1 | T/5 | F/1 | 0 / 3219 |
| Q2 | 1 | **1** | F/1 | F/1 | F/1 | 0 / 3219 |
| Q3 | 1 | **1** | F/1 | F/1 | F/1 | 0 / 3219 |
| Q4 | 40 | **40** | T/3 | T/5 | F/1 | 0 / 3219 |
| Q5 | **123** | **123** | T/3 | T/5 | F/1 | 0 / 3219 |
| Q6 | **14** | **14** | T/3 | F/1 | T/8 | 0 / 3219 |
| Q7 | 1 | **1** | F/1 | F/1 | F/1 | 0 / 3219 |
| Q8 | 75 | **75** | T/3 | F/1 | F/1 | 0 / 3219 |

3,219 = 3 × 1,073 confirmed; "2,144 configurations actually moved" confirmed
(σ fixes the patch in 1,075 of 3,219). Q5's 123 decomposes as 30/30/30/30/3 by
law, and equals the number of distinct realized (patch, law) pairs — the map is
injective. Q6's 14 values recomputed exactly:
0, 1/1000, 1/500, 3/1000, 1/16, 1/8, 3/16, 1/5, 1/4, 3/8, 2/5, 1/2, 3/5, 3/4,
with max 8 in a single state slice. §5.2's five preserving-family sizes at the
legitimate declaration recomputed exactly (DET 1280, FUNNEL 13, REV 120,
FUNNEL-CLOSURE 1161, counter-law 60), and §5.2's clause claim is exactly right:
`ii_b` — the reachability/realization clause (no declared block unoccupied by
the reachable set, no unrealized identification) — is True at DET, FUNNEL,
FUNNEL-CLOSURE and the counter-law, and **False only at REV**.

Self-test numbers: 19,314 = 6 × 3,219 confirmed; 12,864 = 6 × 2,144 confirmed;
2,772 / 9,072 confirmed; 728 / 3,219 confirmed; 384 / 512 confirmed. Witnesses:
201 / 775 confirmed; 745 confirmed; 8 ambient holonomy values (all eight phases
0–7) confirmed; 4,845 grid states confirmed. A19 confirmed against
`v12/paper1-composition-defect.md` line 339.

### 2.2 M1 (MAJOR) — five of the eight equivariance rows cannot fail; three are `x == x`

The delivered table prints an identical "0 failures / 3,219 (2,144
configurations actually moved)" for all eight quantities, which reads as eight
independent equivariance tests with a common discrimination statistic. I measured,
per quantity, the number of instances in which **either side of the equality
actually differs from the base value** — i.e. in which the test could detect
anything:

| Q | reads patch? | transport on the admitted group | instances where either side ≠ base | classification |
|---|---|---|---|---|
| Q1 | **no** | ≡ identity (σ fixes L setwise ⇒ conjugation is trivial) | **0** | **structurally vacuous** |
| Q2 | **no** | declared identity | **0** | **structurally vacuous** |
| Q3 | **no** | ≡ identity (the admissible set is σ-stable) | **0** | **structurally vacuous** |
| Q4 | yes | partition relabelling | 536 | contentful |
| Q5 | yes | certificate relabelling | 2144 | contentful |
| Q6 | yes | declared identity | 0 | contentful — 2,144 genuinely distinct recomputations, all agreeing |
| Q7 | yes | declared identity | 0 | **null on the family** (value ≡ 0) |
| Q8 | yes | partition relabelling | 2688 | contentful |

For Q1, Q2 and Q3 this is provable from the delivered source, not merely
measured: the inner functions memoize on `("q1", law_id)`, `("q2", id(lifts))`
and `("q3", law_id)` — keys that exclude `part`, `rho` **and** `sigma` — so the
recomputed side returns the *identical object* at all 3,219 instances, while the
declared transport is the identity on the admitted group. The comparison is
literally `x == x` on one object. For Q7 the family value is the constant 0, so
the test is `0 == 0`.

Consequence for §7.1 and gate `SYN-ST-RELABEL`: of the 19,314 instances,
**9,657 are structurally vacuous (Q1, Q2, Q3) and a further 3,219 are null
(Q7) — 12,876 of 19,314 carry no information.** Only Q4 and Q8's 6,438 do.
Worse, the statistic offered to make vacuity visible — "12,864 configurations
actually moved" — measures movement of the **patch**, a coordinate Q1, Q2 and Q3
do not read. RUNBOOK §14's requirement that "a vacuous pass would be visible" is
defeated by the very number printed to satisfy it.

In fairness: the `stab-lax` mutant (which replaces the stabilizer by all of S₅)
does kill `SYN-POSITIVE-CONTROLS`, showing the *instrument* would catch a wrong
group. That is a statement about the group, not about the reported 0/3,219 rows.
**Repair F1.**

### 2.3 M3 (MAJOR) — the INERT/INVARIANT boundary is broken for Q8

`_is_neutral`'s Q8 branch and route 2 both decide degeneracy by **string suffix**.
I constructed Q8's own `neutral_value("Q8")` and fed it to both predicates:

```
canon(neutral) = ((0123|4,((0,1,2,3,4)),1),(01|23|4,((0,1,2,3,4)),1),(01|2|3|4,((0,1,2,3,4)),1))
_is_neutral :  all(x.endswith(",1)") for x in v.split("),("))   ->  False
route 2     :  sv.endswith(",1)")                                ->  False
```

Splitting on `"),("` cuts through the seam partitions, so no fragment ends
`,1)`; and the whole canon ends `))`, so route 2 ends `False` unconditionally.
**Both routes return False on the neutral object they exist to recognize.** Had
Q8 been constant at the one-atom seam — precisely the ω failure mode the pin
makes first-class — it would have been gated `ARENA-INVARIANT-Q8`, never
`ARENA-INERT-Q8`. Gate `SYN-DEGENERACY`'s claim that "the set of inert quantities
is therefore a measurement", and that route 2 is "independent of the degeneracy
predicate and of any mutant of it", is false at Q8: route 2 is identically False
there and agrees with the primary route only by coincidence. The
`degeneracy-lax` mutant cannot catch this — it forces `_is_neutral` to False,
which is what the Q8 branch already returns.

Secondary, and structural: for every quantity with more than one raw family
value (Q1 5, Q4 40, Q5 123, Q6 14, Q8 75) the degeneracy test short-circuits on
`len(allv) == 1` and never consults the neutral at all. Since raw values include
the naming, any quantity that is merely equivariant-and-non-constant passes
nondegeneracy automatically. The gate has teeth only for Q2, Q3 and Q7.
**Repair F3.**

### 2.4 Is any `[SAMP]` hiding inside a claimed exhaustive sweep?

Two `[SAMP]`s exist and both are disclosed in §10 — but one is disclosed only at
the receipt, not at the claim, and one is mislabelled:

- **Gauge (finding D5, moderate).** §7.2 says "All 512 checkpoint-phase
  switchings are applied to the whole carried diagram — **every member** of the
  declared admitted lift family switched at once". The delivered sweep is
  `[SAMP]` 32 of 512 lifts. §10 and the receipt scope string say so; §7.2 does
  not (RUNBOOK failure-catalogue row #40: "scope tags at the claim, not just the
  receipt"). **I closed the gap myself:** full **512 lifts × 512 switchings =
  262,144 instances, 0 moved**, with the base-gauge holonomy the single value
  (rank 1, phase 4, span 1) over all 512 lifts. The claim is true; the delivered
  evidence for it was not.
- **Q-OPT (see K3).** `[SAMP] 576 of 14,400` is not a sample: `perms[:24]` is
  `permutations(range(5))`'s first 24 entries = **exactly the point stabilizer
  of 0**, a subgroup of order 24. It is an exhaustive sweep of a designated
  subgroup's square.

All other sweeps are genuinely exhaustive over their declared populations
(3,219 relabelling instances; 775 ω instances; 4,096 ambient phase quadruples;
`laws_of_T3` for the identity-free witness). No hidden `[SAMP]` found.

---

## 3. K3 — Q-OPT. Transport genuinely exact; census **vacuous**; verdict **pre-determined**.

**Is the transport genuinely exact?** Yes. I rebuilt Δᴮ from scratch in
ℚ(ζ₈) as 4-tuples of Fractions mod x⁴+1, independently of the delivered code,
and obtained Δᴮ(H,H) = [[1/2, −1/2], [−1/2, 1/2]], matching
`v12/paper1-composition-defect.md` line 339 exactly. A19 and `SYN-QOPT-T1` are
sound. Deviation 4 is honest: `BLOCKED-AT-IMPORT` was available and correctly
not used.

**Are the 576 pairs a real census?** No — they measure a theorem. For any
monomial U (permutation times diagonal unitary), B(U) = |U|² entrywise = the
underlying permutation matrix, and B is multiplicative on monomials, so
Δᴮ ≡ 0 on every monomial pair. I confirmed this three ways: 0 non-zero over the
delivered **576**; 0 non-zero over the **full 14,400** permutation pairs (so the
"sample" understates nothing, and is not a sample); and 0 non-zero over **200
randomly phased monomial pairs** — which the delivered sweep never touches, since
it builds every U from Z1/Z0 entries only and therefore tests only the
trivial-phase representatives of the admitted reversible lifts. The 384/512
non-monomial control reproduces exactly.

**Is the verdict vocabulary compliant?** Partially, and the deeper problem is
that the verdict was fixed before any fixture was consulted:

```python
verdict = ("ARENA-INERT-Q-OPT" if (t1 and nz == 0 and ctrl_nonzero)
           else "BLOCKED-AT-IMPORT")
```

Only **two** of the pin's four names are reachable for Q-OPT; `ARENA-INVARIANT`
and `ARENA-ARTIFACT` are unreachable by construction. And Q-OPT carries no
READS/ACTS/TRANSPORT declaration at all (the §3.3 row is "—" throughout), so it
never enters the census machinery that could produce them. Each of the three
conjuncts is a theorem, not a measurement: `t1` is the Hadamard identity,
`nz == 0` is the monomial theorem above, `ctrl_nonzero` is a fixed non-monomial
matrix. `ARENA-INERT-Q-OPT` was inevitable.

On vocabulary: the pin defines `BLOCKED-AT-⟨object⟩` as "the census cannot be run
for want of a named object". §8 reports `ARENA-INERT` **plus** an embedded
`BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION` — a fifth outcome shape not in
the pin's list. I do not read this as a fudge; it is the honest description of
the situation, and §8's prose is accurate. But it is a vocabulary extension and
Deviation 4 records only half of it. **Repairs F11 (and F5's scope note).**

---

## 4. K4 — THE ASYMMETRY. **Real, but weaker and differently-shaped than stated.**

**Do Q5 and Q8 face the same action?** Yes, at the declaration level: both are
declared to READ `patch` and to be ACTED ON by `law, state, relabelling,
switching`; both are swept over the same 3,219 instances of the same fibration.
That much of K4 is answered in the unit's favour.

**But (M5, MAJOR) three things undercut the comparison.**

*(a) Q8's law- and state-invariance is definitional, not measured.*
`q8_cross_arena_overlap(part, law_id, law, rho, sigma, lifts)` never reads `law`
or `rho` — verified by source and by measurement (Q8's law-slice and state-slice
maxima are 1 on the flat identity slice as well as on the fibered sweep). Q5, by
contrast, *is* a function of (patch, law). So "the legitimacy of either patch
separately moves with the arena while what they share does not" reduces, at the
operator level, to: the seam functor forgets the law; the certificate does not.

*(b) The chain trivializes the seam datum.* I recomputed the meets: the three
declarations form a 3-chain, PI1 ≺ P22 ≺ PTOMO, with seams `0123|4` (2 atoms),
`0123|4` (2 atoms) and `01|23|4` (3 atoms) — exactly A14. The seam of any two
declared patches is therefore just the coarser of two elements of a fixed
3-chain, which is a fact about three frozen partitions and cannot move under any
coordinate.

*(c) The headline counts are not comparable, and the naming caveat is applied
asymmetrically.* §5.1 correctly discounts the naming for Q8 ("Q8's 75 is the
three declared patches carried through the admitted relabellings") — and does
not do so for Q5. My recomputation of what the 123 is made of:

| slice | distinct Q5 certificates |
|---|---|
| one declared patch, σ = identity, law varying | **5** (at each of the three) |
| all three declarations, σ = identity, law varying | **15** |
| legitimate / 2+1+1 / 2+2 with σ free | 21 / 41 / 61 |
| whole family | 21 + 41 + 61 = **123** |

The abstract's "The legitimacy certificate of a **fixed** patch declaration takes
$123$ distinct values across the family" is wrong twice over: at a fixed
declaration with the naming held it takes **5**; at a fixed declaration with the
naming free it takes 21, 41 or 61; 123 needs all three declarations. The
naming-quotiented comparison is **5 certificates per declared patch (moving with
the law) against 1 seam per ordered pair (not moving)** — the asymmetry *does*
survive the quotient, which I verified, but the boldfaced number does not.

**Is Q8's invariance contentful or secretly inert?** Contentful in fact — the
seams are 2, 2 and 3 atoms, not the one-atom neutral — but the paper's *evidence*
for it is empty on both routes. The degeneracy predicate cannot say `INERT` for
Q8 at all (M3). And the nondegeneracy witness (finding D3, moderate) is both
vacuous and ungated: `wit["Q8"]["one_atom_seams"] = 1` counts distinct meets of
the three patches with the one-atom chart, and I verified
`part_meet(p, ONEATOM) == ONEATOM` for **all 52** partitions of the carrier — the
value is 1 for any input whatsoever. Meanwhile `SYN-NONDEGENERACY`'s pass
condition is `nz > 0 and len(idf) > 0 and proper > 0 and len(amb) > 1 and
wit["Q1"][...] == 5`: **no Q8 term appears.** §6 lists "the one-atom seam for Q8"
alongside four gated witnesses. **Repairs F3, F5.**

---

## 5. K5 — INSTRUMENT INTEGRITY.

### 5.1 M2 (MAJOR) — the §14 self-test survives its own transport mutant. Demonstrated.

I ran the frozen script with `--mutant transport-lax` (no artifacts written) and
read the result:

```
[PASS] SYN-ST-RELABEL
  {"fixed": 12876, "instances": 12876,
   "instances_where_the_configuration_actually_moved": 8576,
   "quantities": ["Q1", "Q2", "Q3", "Q7"]}
VERDICT: ... ARENA-ARTIFACT-Q4 ... ARENA-ARTIFACT-Q8 ...
         RQ0-SYNTH-CENSUS-COMPLETE
TOTALS: 19 anchors, 19 gates, 1 must-pass failures
```

The gate **self-heals**. `SYN-ST-RELABEL` scopes itself over the quantities the
census has *just gated* invariant or inert; the mutant flips Q4 and Q8 to
ARTIFACT; those are exactly the two quantities that gave the gate teeth; the gate
then passes on the four tautological ones — and still reports 8,576
"configurations actually moved", at a moment when it is 100 % vacuous. The only
kill is the Q4-specific `SYN-Q4-NAME-BLIND`. So a wrong value-transport for the
paper's headline quantity silently converts `ARENA-INVARIANT-Q8` — "the finding
worth carrying forward" — into `ARENA-ARTIFACT-Q8`, while the unit still emits
`RQ0-SYNTH-CENSUS-COMPLETE`. **Repair F2.**

Minor rider (m1): the same run prints the hard-coded thesis string "…the
name-blind generation profile and the seam datum do not move at all" underneath
the tags `ARENA-ARTIFACT-Q4` and `ARENA-ARTIFACT-Q8`. `verdict()`'s thesis is a
literal, not derived from `rows`. That is a conclusion typed rather than
computed — the failure-catalogue's #24 rule applied to prose. **Repair F10.**

### 5.2 D4 (MODERATE) — the mis-conventioned control is not the control described

§7.3: "the patch is relabelled while the law and the state are left alone, which
is the classic transport bug … the quantities the census gates invariant fail,
at 2,772 of 9,072 instances." I decomposed it:

| quantity | failures | instances |
|---|---|---|
| Q4 | **0** | 3,024 |
| Q8 | **2,772** | 3,024 |
| Q1 | **0** | 3,024 |
| total | 2,772 | 9,072 |

**Exactly one quantity fails**, and it cannot be otherwise: an admitted σ fixes
the law setwise *and fixes ρ exactly*, so `_broken_action`'s output (σ·d, L, ρ)
is **identical** to the correct action's (σ·d, L, σ·ρ). The described bug is not
a bug under this action. What the test actually perturbs is the `sigma` argument
handed to the quantity function (identity instead of σ), which only
`q8_cross_arena_overlap` consumes — the failure is the seam's *other* patches not
being co-relabelled. The plural "quantities" is false and the stated mechanism is
not the operative one. **Repair F7.**

### 5.3 M4 (MAJOR) — READS-vs-ACTS flips both headline verdicts

Deviation 3 concedes the pin does not fix the READS/ACTS split and offers, as
mitigation, that the full dependence profile is printed. It does not mitigate,
because the *gated output* and §9's operational discipline both key off the
verdict, not the profile. Measured:

- Q4 and Q5 have **identical** law-dependence: `moves = True`, `max distinct
  values in a law slice = 5`, on the fibered sweep and on the flat identity slice
  alike.
- Q4 is declared to READ `law`; Q5 is not. That one word is the entire difference
  between `ARENA-INVARIANT-Q4` and `ARENA-ARTIFACT-Q5`.
- Moving `law` into Q5's READS gives it an empty acting-moves set →
  `ARENA-INVARIANT-Q5`. Moving `law` out of Q4's READS gives acting-moves
  `['patch','law']` → `ARENA-ARTIFACT-Q4`. **Both flip.**

And §9.2 then licenses "claims of physical significance" for the name-blind
generation profile while denying them to the certificate, on a distinction the
census does not measure. Note that the one obvious objective criterion is
available and refutes the split: `q5_legitimacy_certificate(part, law_id, law,
rho, sigma, lifts)` consumes `law` exactly as `q4_name_blind_generation_profile`
does. **Repair F4.**

### 5.4 The mutant table, per-mutant: is each kill the right gate?

20/20 exit 1 with named kills, reproduced from the receipt. Auditing whether the
kill is the *right* gate:

- Right and tight: `anchor-A04/A05/A09/A11/A12/A19` (own anchor);
  `seam-orient` → A14 (the seam's refinement order, caught by the one anchor that
  carries the committed atom counts); `hol-sign`, `hol-orient` → A09 (§14's
  required sign/orientation mutants, caught at the anchor); `srcscan-lax` →
  SYN-SWITCH-SCOPE; `float-lax` → SYN-EXACT; `born-lax` → A19 + both Q-OPT gates;
  `omega-lax` → A16; `eps-lax`, `states-drop` → A11; `degeneracy-lax` →
  SYN-DEGENERACY.
- `name-reader` → SYN-Q4-NAME-BLIND: right gate, and the one place a
  stat-label-style reader is caught.
- `stab-lax` → A07 + SYN-Q4-NAME-BLIND + SYN-POSITIVE-CONTROLS: correct, and
  informative — it shows Q1's equivariance test *would* bite outside the
  stabilizer.
- **`transport-lax` → SYN-Q4-NAME-BLIND only.** Should also kill
  SYN-ST-RELABEL. It does not (M2).
- **`action-weaken` → nine kills (m2, minor)**, including A11 and A13, which
  are about the state count and the law count, not the strength of the action.
  The designed kills (SYN-NEGATIVE-CONTROL, SYN-ACTION-NOT-TOO-WEAK) do fire, so
  Appendix B's sentence is true, but the mutant does not isolate its target.
- Not exercised by any mutant: the seam's *co-relabelling* in Q8's transport
  (only SYN-ST-BROKEN touches it, and it is the sole source of that gate's
  2,772); Q1's and Q3's quantity functions have no through-the-instrument anchor
  at all (m3), although §4's rationale — "so that a tampered quantity cannot pass
  by agreeing with itself" — applies to them as much as to Q4–Q8, and they are
  precisely the quantities whose equivariance test cannot fail.

### 5.5 D2 (MODERATE) — "745 admissible patches" is arithmetically impossible

`identity_free_admissible()` returns (patch, law, …) tuples. I recomputed: **745
entries, comprising exactly 4 distinct patches across 428 distinct identity-free
laws.** At three configurations there are only 5 partitions in total, so "745
admissible patches" (§5.3, §6) cannot be a patch count, and the receipt key
`"admissible_patches": 745` carries the error into the machine record. The
witness's *force* survives — all 4 proper coarse charts occur and the fine chart
never does, which is exactly the point being made — but the number is
mislabelled at three sites. **Repair F6.**

### 5.6 The §2 six-row record table — **verbatim-faithful. No defect.**

I checked every verdict name against `v13/LOG.md` and every commit against the
successor pins' declared immutable bases (Deviation 8's stated method):

| # | ledger | verdict names | commit | successor pin's declared base |
|---|---|---|---|---|
| 1 | #123 | `RQ0-L0-BLOCKED-AT-DE-SMUGGLING` ✓ | `0bc943c` | L1 pin: `0bc943c` ✓ |
| 2 | #134 | `RQ0-L1-COMPOSITE-BOUNDARY` / `ENTANGLEMENT-WITNESS` (classifier-total form) / `ALIGNMENT-SELECTOR-AT-DECLARED-ALGEBRA` ✓ | `efa7224` | L2 pin: `efa7224` ✓ |
| 3 | #145 | `RQ0-L2-GENERATIVE-ATLAS-AXIOM` + `RQ0-L2-BLOCKED-AT-CARRIER` ✓ | `267cb2a` | L3 pin: `267cb2a` ✓ |
| 4 | #156 | `RQ0-L3-EPSILON-BLIND` (every-state) + `MIXED-LAW-CLOSED`/`PLURALISM-PRICED` + `OCCUPANCY-STATISTIC` (quadruple-bound) + `BLOCKED-AT-PROVENANCE` ✓ | `a5cb096` | L4 pin: `a5cb096` ✓ |
| 5 | #166 | `RQ0-L4-CLASS-IMPOSSIBILITY` (fused) + `FINGERPRINT-AMNESTY` + `BLOCKED-AT-THE-REFINEMENT-ORDER`, fingerprint withdrawn ✓ | `483311c` | L5 pin: `483311c` ✓ |
| 6 | #177 | `RQ0-L5-BLOCKED-AT-THE-DECLARATION` ✓ | `77b015e` | synth pin: `77b015e` ✓ |

Row-level numbers also check: "descends fourteen times of fifteen" = ledger
#134's "14-of-15"; row 5's "(resolution profile, marked-block excess)"
factorization is ledger #166's Theorem 7.3 verbatim; row 6's constant ζ₈⁴ = −1
is ledger #177's headline. **All six rows are faithful.** K5's last item passes
cleanly.

---

## 6. Findings, ranked

| id | sev | finding | repair |
|---|---|---|---|
| M1 | major | Q1/Q2/Q3's equivariance tests are `x == x` on one memoized object; Q7's is `0 == 0`. 12,876 of the self-test's 19,314 instances carry no information, and the discrimination statistic reported to expose this measures a coordinate three of them do not read. | F1 |
| M2 | major | `SYN-ST-RELABEL` survives `transport-lax` by self-scoping onto the tautological quantities; Q8 silently flips to ARTIFACT and the unit still reports CENSUS-COMPLETE. Demonstrated by running the frozen script. | F2 |
| M3 | major | Both Q8 degeneracy routes return False when fed Q8's own constructed neutral; `ARENA-INERT-Q8` is unreachable. Route 2 is not independent, it is identically False. The ω lesson fails at the headline quantity. | F3 |
| M4 | major | Q4 and Q5 have identical measured law-dependence; the READS/ACTS declaration alone decides INVARIANT vs ARTIFACT, and §9.2 licenses physical significance off that undetermined choice. | F4 |
| M5 | major | The asymmetry compares a law-consuming quantity with a law-blind one; the seam is the coarser member of a frozen 3-chain; 123 is naming-inflated (true per-declaration figure: 5) while 75's inflation is disclosed. | F5 |
| D1 | mod | Q-OPT's instrument can emit only 2 of the pin's 4 names; all three conjuncts of its verdict are theorems; `[SAMP] 576` is a subgroup, not a sample; `INERT + BLOCKED-AT-⟨object⟩` is an undeclared fifth outcome shape. | F11 |
| D2 | mod | "745 admissible patches" — truly 745 (law, patch) instances, 4 distinct proper charts, 428 laws. Impossible as a patch count at 3 configurations. Also in the receipt key. | F6 |
| D3 | mod | Q8's nondegeneracy witness is a tautology (`meet(p, one-atom) == one-atom` for all 52 partitions) **and** absent from `SYN-NONDEGENERACY`'s pass condition. | F3 |
| D4 | mod | The broken-action control fails on Q8 only (2,772/3,024); Q1 and Q4 are 0/3,024, and the described bug is a no-op under an admitted relabelling. | F7 |
| D5 | mod | §7.2 claims the switching sweep covers every lift; it is `[SAMP]` 32/512, disclosed only at §10 and the receipt. I ran the exhaustive 262,144 — 0 moved. | F8 |
| D6 | mod | The fibration suppresses three ε values (flat 17 → fibered 14); undisclosed. | F9 |
| m1 | minor | The thesis string in `verdict()` is typed, not derived; contradicts the tags under a mutant. | F10 |
| m2 | minor | `action-weaken` kills nine gates/anchors including two unrelated to the action's strength; it does not isolate. | — |
| m3 | minor | Q1 and Q3 have no through-the-instrument anchor, though §4's rationale covers them. | — |
| m4 | minor | 7 of 8 quantities are never evaluated at any switching but the base, so \|𝒜\| = 1,648,128 is the declared family size while the census's evaluation set is the 3,219-element quotient plus Q2's sweep. Argued and legitimate; "the family is enumerated" reads stronger than what happens. | — |

**Required fixes.** F1 report per-quantity discrimination on every equivariance
and self-test row, and mark Q1/Q2/Q3 structurally fixed. F2 scope
`SYN-ST-RELABEL` over the *declared* quantity list so the transport mutant cannot
self-heal it, and record its expected kill. F3 compare Q8 against the constructed
neutral structurally, add a positive control that feeds each neutral through the
predicate and asserts True, and put Q8's witness into `SYN-NONDEGENERACY`'s pass
condition. F4 derive the READS split from a stated criterion and re-derive Q4/Q5,
or publish a second declaration-free verdict alongside and amend §9.2. F5 give
Q5's naming-quotiented count (5 per declared patch, 15 over three) wherever 123
appears including the abstract; state that Q8 is law-blind and state-blind by
definition and that the three declarations form a chain. F6 correct "745
admissible patches" at all three sites. F7 correct §7.3 to "one quantity, Q8,
fails, at 2,772 of 3,024" and describe the perturbation actually applied. F8 put
the `[SAMP]` tag at §7.2's claim or adopt the exhaustive 262,144 sweep. F9
disclose the flat-vs-fibered ε range. F10 derive the thesis string from the
computed verdicts. F11 declare `ARENA-INERT + BLOCKED-AT-⟨object⟩` as a
vocabulary deviation and record that Q-OPT's instrument can emit only two of the
pin's four names.

**What survives untouched.** |𝒜| = 1,648,128 and the whole fibration; all eight
census rows; every self-test and witness count; §5.2's certificate numbers and
its clause claim; A19 against v12 paper 1; the §2 record table; the
`ACTION-TOO-WEAK` machinery, which is correctly designed and correctly did not
fire. **Zero arithmetic errors found in the delivered artifacts.**

---

## 7. Independent recomputation count: **142**

4 SHA verifications (paper, code, output, receipt) + 1 receipt/source hash
self-match. **Family (21):** 13 named states; all 13 ε-triples against L3's
committed receipt; 5 laws and their 5 sizes; my from-scratch stabilizer predicate
against `L4.stabilizer` on all 65 fibers; 65 fibers; Σ|G| = 1,073; the 5
histogram entries; identity ∈ every fiber; 3 free loop vertices; 512 switchings;
|𝒜| = 1,648,128; the 120-element union. **Census (41):** 8 distinct-value counts;
8 patch maxima; 8 law maxima; 8 state maxima; 8 equivariance rows; the 2,144
discriminating count. **Probes (23):** 8 per-quantity discrimination figures; the
identity-slice profile as 8 further rows (§1); the 3-way self-test decomposition;
1,075 σ-fixed instances; 3 broken-action per-quantity figures + total. **Controls
(4):** 728/3,219; 2,772/9,072; 9,072 = 3·3·1,008; 19,314 = 6·3,219 and 12,864 =
6·2,144. **Section 5 (16):** 5 preserving-family sizes; the 5 per-law clause-bit
vectors; the ii_b/REV identification; Q5's 5 per-law orbit counts (30/30/30/30/3);
Q5 = 123 = |realized (patch, law)|; Q5's 21/41/61 and 15-at-identity; Q6's 14
values, max 8, and the flat 17. **Witnesses (8):** 201/775; 745; 745 proper; 4
distinct patches; 428 laws; 8 ambient holonomy values; the one-atom seam over all
52 partitions; 4,845. **Q-OPT (6):** Δᴮ(H,H) vs v12 line 339; `perms[:24]` = the
point stabilizer of 0; 0/576; 0/14,400; 0/200 phased monomial pairs; 384/512.
**Gauge (2):** base-gauge holonomy over all 512 lifts; the exhaustive 512×512 =
262,144 sweep. **Degeneracy (3):** `_is_neutral` and route 2 on the constructed
Q8 neutral; Q8 = 3 values at identity and 75 over the family. **Ledger (14):** 6
verdict names; 6 base commits; "14 of 15"; Thm 7.3's phrasing; ζ₈⁴ = −1.
**Receipt (3):** 19/19 anchors; 20/20 gates; the fiber histogram against mine.
**Mutant (2):** `transport-lax`'s SYN-ST-RELABEL pass at 12,876 over {Q1,Q2,Q3,Q7};
its three flipped verdicts with CENSUS-COMPLETE still emitted.

Largest single recomputations: the 262,144-instance exhaustive gauge sweep; the
14,400-pair exhaustive Δᴮ sweep; two full independent passes of the 3,219 ×
8-quantity census.

---

## 8. GRADE

# ACCEPT-WITH-FIXES

The unit's arithmetic is clean and its family is sound. |𝒜| = 1,648,128 is
correct, the fibration is the right structure and does not smuggle
arena-dependence — the identity relabelling in every fiber makes the σ = identity
slice the flat product, and I reproduced the entire dependence profile on it. All
123, 14, 40, 75, 5, 1, 1, 1 reproduce; so do 19,314, 2,772, 728, 384, 201, 745,
8, 4,845 and Δᴮ(H,H). I found **no false number anywhere in the delivered
artifacts**, and I strengthened one claim (the gauge sweep) from `[SAMP]` to
exhaustive on the unit's behalf.

`REJECT` would be wrong: nothing stated is false, and the thesis's measured
content — the same declared patch receives a different certificate under a
different committed law — is real and correctly gated.

`ACCEPT` would be wrong: §9.2 turns `ARENA-INVARIANT` into a licence for claims
of physical significance, and for the two quantities that licence most matters
to — Q4 and Q8 — the label rests on an undetermined declaration (M4), a
degeneracy predicate that cannot return the verdict it exists to return (M3), an
ungated tautological witness (D3) and a self-test that survives its own transport
mutant (M2), 12,876 of whose 19,314 instances cannot fail (M1). The seam is being
handed to the successor rung as "the finding worth carrying forward"; it must not
be handed on with those four holes under it.

The eleven fixes F1–F11 are repairs to the evidentiary layer, not to the
measurements. None requires a new fixture, a new arena or a re-run of the tower.
With F1–F5 discharged I would grade this ACCEPT.
