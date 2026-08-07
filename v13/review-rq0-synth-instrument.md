# RQ0-SYNTH — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, instrument lens. **Date:** 2026-08-07.
**Protocol:** `v13/note-rq0-synth-hostile-protocol.md` (FROZEN, #181).
**Object:** commit `b36ea87`, pin `f74a8511b204` @ `a14bda0`, base `77b015e`.

## 0. SHA verification (before reading)

| file | sha256-12 recorded | sha256-12 measured | |
|---|---|---|---|
| `v13/paper-rq0-arena-synthesis.md` | `3a03467dd43e` | `3a03467dd43e` | ok |
| `v13/code/rq0_synth_census_exact.py` | `5a3d5b0b1704` | `5a3d5b0b1704` | ok |
| `v13/code/rq0_synth_census_output.txt` | `ee94cc4c6612` | `ee94cc4c6612` | ok |
| `v13/code/rq0_synth_census_receipt.json` | `0dc2c182b66b` | `0dc2c182b66b` | ok |

All four match; the frozen object was read as delivered. No repo file was
modified by this review. All work was done on copies in a scratch tree;
`NO git` observed.

**Independent recomputations performed: 106.** They are enumerated in §7.

---

## 1. What holds

Stated first and plainly, because it is most of the object.

1. **Byte-identical reproduction.** A full delivery-mode run
   (`--falsification-selftest`) from a *different working directory*, on a
   fresh interpreter, reproduces **both** delivered artifacts byte for byte
   (`diff` clean on `rq0_synth_census_output.txt` and
   `rq0_synth_census_receipt.json`). 19 anchors, 20 gates, 20 mutants, 0
   must-pass failures. This is a third byte-identical run beyond the
   worker's two.
2. **Every number I recomputed reproduces.** I reimplemented the family, the
   admitted-isomorphism groups, all eight quantities, their transports, the
   dependence profile and all four self-test counters from the terminal
   fixtures, without calling the census module — and using **native tuple
   equality instead of the census's `canon()` string**. Every count agrees:
   orbits `5, 1, 1, 40, 123, 14, 1, 75`; per-coordinate maxima; equivariance
   `0/3219` with `2144` discriminating for all eight; self-test
   `19314/19314/12864`; switching `0 moved / 384 unclosed`; broken action
   `2772/9072`; name-reader `728/3219`; ω ambient `201/775`; identity-free
   `745/745`; ambient holonomy `8`. The agreement of the native-equality
   route with the canon route is itself the check that `canon` is injective
   on the census's values — no collision, no over-separation.
3. **|𝒜| is right and the fibration is faithful.** My own stabilizer gives
   65 fibers, Σ|G| = **1073**, |𝒜| = 3 × 1073 × 512 = **1,648,128**.
4. **All 20 mutant kills reproduce exactly.** I re-ran every mutant with a
   full gate/anchor state dump: for all 20, exit code, failed-anchor list and
   failed-gate list are **identical** to the delivered `TABLES["mutants"]`.
   20/20 MATCH.
5. **Four mutants reconstructed from the receipt's prose description alone**
   (`name-reader`, `action-weaken`, `seam-orient`, `transport-lax`), in my own
   framework, reproduce their recorded kills: `name-reader` → 728/3219
   equivariance failures → `SYN-Q4-NAME-BLIND` fails; `action-weaken` → Q5
   stops moving under law and Q6 under state → `SYN-NEGATIVE-CONTROL` fails
   and `ACTION-TOO-WEAK` fires; `seam-orient` (join for meet) → the A14 atom
   counts become 3,4 / 4,4 → A14 fails; `transport-lax` → 536/3219 → gate
   fails.
6. **Exit-1-only confirmed by deliberate breakage.** Corrupting anchor A07's
   committed value (12 → 13) in a scratch copy yields exit 1, exactly one
   failed anchor (`A07`), **zero** failed gates, and an otherwise unchanged
   verdict table.
7. **The 19 anchors are genuinely anchored.** Every reused tower value traces
   to a terminal unit's own committed record, not to a retyped number:
   A01/A02 ← L4 A01–A02 and L5 A01–A02; A03 ← L5 A03; A04 ← L4 A03 / L5 A04;
   A05 ← L4 A04 / L5 A05; A06 ← L5 A06; A07 ← L5 A09; A08 ← L5 A08; A09 ←
   L5's gate `L5-AMP-CONSTANCY` (`distinct_holonomy_classes: 1`,
   `classes: {"(4,)": 512}`) and `L5-AMP-CONTENT` (`"(H01)": [1,[4]]`);
   A10 ← L5 A10 / L4 A08; A11 ← the L3 receipt's `the_state_map` rows;
   A12 ← `L5-HOL-GAUGE` (`switchings_swept: 512`); Q3's 745 witness ← L4 A10
   (`[745, 0]`); A19 ← `v12/paper1-composition-defect.md` line 339, verbatim.
   Anchors A14–A18 do run through the census's own quantity functions, so a
   tampered quantity cannot pass by agreeing with itself — verified by
   `omega-lax`, which is caught by A16 and by nothing else.
8. **§2's six-row record table is verbatim-faithful.** The six commits are
   the six successor pins' declared immutable bases (`0bc943c` ← L1's pin,
   `efa7224` ← L2's, `267cb2a` ← L3's, `a5cb096` ← L4's, `483311c` ← L5's,
   `77b015e` ← this unit's pin). The six ledger numbers and every verdict
   name appear verbatim in `v13/LOG.md`: #123 `RQ0-L0-BLOCKED-AT-DE-SMUGGLING`;
   #134 `RQ0-L1-COMPOSITE-BOUNDARY / ENTANGLEMENT-WITNESS (classifier-total
   form) / ALIGNMENT-SELECTOR-AT-DECLARED-ALGEBRA` and "the forged ⊤ record
   DESCENDS (14 of 15 certified)"; #145 `GENERATIVE-ATLAS-AXIOM +
   BLOCKED-AT-CARRIER`; #156 `RQ0-L3-EPSILON-BLIND (every-state form) +
   MIXED-LAW-CLOSED / PLURALISM-PRICED + OCCUPANCY-STATISTIC
   (quadruple-bound) + BLOCKED-AT-PROVENANCE`; #166 `RQ0-L4-CLASS-IMPOSSIBILITY
   (fused form) + FINGERPRINT-AMNESTY + BLOCKED-AT-THE-REFINEMENT-ORDER`,
   fingerprint withdrawn; #177 `RQ0-L5-BLOCKED-AT-THE-DECLARATION`,
   `PROVENANCE-CERTIFIES does not occur`. No misquotation found.
9. **§5.2's certificate numbers reproduce**: preserving family at the
   legitimate declaration = 1280 (DET), 13 (FUNNEL), 120 (REV), 1161
   (FUNNEL-CLOSURE), 60 (counter-law); the REV certificate differs in the
   **fourth** clause bit, which is `(ii-b)`, the reachable subprocess — the
   paper's "the reachability clause fails under REV" is exact; and 0 of 15
   (declaration × law) instances are admissible.
10. **`ACTION-TOO-WEAK` is a real pre-registered kill.** It does not fire on
    the delivery, and it *does* fire on my independent reconstruction of a
    weakened action. It is not decoration.
11. **Gate order proves within-run freeze ordering.** `SYN-FREEZE` is gate
    index 0 with `census_evaluations_so_far: 0`, `SYN-SWITCH-SCOPE` index 1;
    the first census gate is index 2. The `_FROZEN` guard in `evaluate()`
    would raise on any earlier evaluation.

---

## 2. K5 — instrument integrity (primary weight)

### K5(a) The §14 self-test and whether its controls have teeth

**Verified numbers.** All four counters reproduce independently:
`19,314 / 19,314` fixed with `12,864` discriminating; unclosed control
`384 / 512`; broken action `2,772 / 9,072`; name-reader `728 / 3,219`. I
reconstructed the unclosed control from scratch (my own switching
enumeration, my own base comparison) and obtained 384; I reconstructed the
name-reader and obtained 728. Both controls fire.

But three findings sit under those numbers.

---

**F1 — `SYN-ST-RELABEL`, the §14 headline gate, is structurally incapable of
failing. [MAJOR]**

Three independent lines of evidence.

*(i) No mutant falsifies it.* Running all 20 mutants with a full gate dump,
six of the nineteen delivered non-mutant gates are never falsified by
anything in the suite:

```
SYN-FREEZE   SYN-CENSUS-COMPLETE   SYN-ST-RELABEL
SYN-ST-SWITCH   SYN-QOPT-T2   SYN-QOPT-SCOPE
```

*(ii) It self-selects.* `inv` (line 1023) is computed **from the census
verdicts**, so any quantity a broken transport or a broken stabilizer makes
move is deleted from the test rather than failing it. Measured:

| run | quantities tested | gate value |
|---|---|---|
| baseline | Q1 Q2 Q3 Q4 Q7 Q8 | 19,314 / 19,314 fixed — PASS |
| `transport-lax` | Q1 Q2 Q3 Q7 | 12,876 / 12,876 fixed — **PASS** |
| `stab-lax` | Q2 Q3 Q7 Q8 | 93,600 / 93,600 fixed — **PASS** |
| `name-reader` | Q1 Q2 Q3 Q7 Q8 | 16,095 / 16,095 fixed — **PASS** |

A deliberately wrong value transport leaves the §14 gate passing.

*(iii) It recomputes nothing.* I instrumented `evaluate()` to count memo hits
and misses per phase:

```
census    hits=  1560   misses= 25752
selftest  hits= 20484   misses=     0      <-- the section-14 relabel test
broken    hits= 17052   misses=  1092
```

The self-test performs **zero** fresh evaluations. It replays the census's
`_EVAL` cache through the same memoized `transport()`, recounting the census's
own `equi_fail == 0` under a different name. §7.1 of the paper presents it as
a separate measurement; it is a recount.

*Repair that would satisfy me:* (a) run the self-test over **all** declared
quantities, not the invariant subset, reporting per-quantity pass/fail — a
quantity that fails should appear as a failure, not as an absence; (b) bypass
`_EVAL`/`_TRANS` inside the self-test so it is an independent measurement;
(c) add a mutant whose named kill is `SYN-ST-RELABEL`.

---

**F2 — `SYN-ST-RELABEL`'s anti-vacuity counter is reported but not gated,
and it passes vacuously under an existing mutant. [MAJOR]**

The predicate (line 1051) is

```python
fixed == tested and tested > 0
```

`disc` — `instances_where_the_configuration_actually_moved` — is placed in the
gate's value and never tested. Contrast `SYN-Q4-NAME-BLIND` (lines 802–803),
which *does* carry the conjunct:

```python
dep["relabelling"]["equivariance_failures"] == 0
and dep["relabelling"]["configurations_actually_moved"] > 0
```

Measured consequence: under the delivered `action-weaken` mutant,
`SYN-ST-RELABEL` **passes** with

```
{"instances": 24, "fixed": 24,
 "instances_where_the_configuration_actually_moved": 0}
```

— a wholly vacuous pass, which is precisely the failure mode the gate's own
claim text says it prevents ("the count … is reported beside it, so a vacuous
pass would be visible"). Visible is not gated. This is the standing rule from
the RUNBOOK failure catalogue (#36: "every gate falsifiable; positive+negative
controls").

*Repair:* add `and disc > 0` to the predicate. One line.

---

**F3 — The §7.3 "mis-conventioned action" control has teeth on exactly one of
its three quantities. [MAJOR]**

I measured the broken-action failures per quantity rather than in aggregate:

| quantity | failures / instances |
|---|---|
| Q1 | **0** / 3,024 |
| Q4 | **0** / 3,024 |
| Q8 | 2,772 / 3,024 |
| total | 2,772 / 9,072 |

The headline `2,772 of 9,072` is `2,772 of Q8's 3,024`. Two thirds of the
control's instances are structurally incapable of failing.

The mechanism. For every admitted σ the stabilizer fixes the law setwise and
the state pointwise — I verified this exhaustively: over all 1,073
relabellings in all 65 fibers, `σ·ρ ≠ ρ` occurs **0** times and `σ·L ≠ L`
occurs **0** times. So the census's own action (line 747) already passes the
law and the state through unchanged. `_broken_action` therefore differs from
the census's action in exactly one respect — the `sigma` argument threaded to
the quantity — and Q8 is the only quantity whose body reads `sigma`. The
paper's description of the control ("the patch is relabelled while the law and
the state are left alone, which is the classic transport bug") describes what
the **census itself** does, not a deviation from it.

*Repair:* (a) report the per-quantity split (0 / 0 / 2,772) in §7.3 and in the
gate value; (b) construct a control that bites on the nomological quantities
too — e.g. relabel the patch while conjugating the law by σ⁻¹ instead of σ,
which is a genuine mis-convention Q1 and Q4 can feel.

*Consequential note for §3.2/§7.1.* "An arena change acts on the **whole
configuration**, never on one argument alone" is true but weaker than it
reads: two of the three components are fixed by construction, so the admitted
relabelling moves only the naming of the patch (and, for Q8, of the other
declared patches). The paper's own §3.2 says this; §7.1's "applied to the
WHOLE declared configuration — patch, law, state" should carry the same
qualifier.

---

### K5(b) The mutant table — is each kill the RIGHT gate?

Audited all twenty, with independently reproduced kill lists.

| mutant | perturbs | recorded = reproduced kills | right gate? |
|---|---|---|---|
| `anchor-A04` | nothing computed | A04 | plumbing only — see F4 |
| `anchor-A05` | nothing computed | A05 | plumbing only |
| `anchor-A09` | nothing computed | A09 | plumbing only |
| `anchor-A11` | nothing computed | A11 | plumbing only |
| `anchor-A12` | nothing computed | A12 | plumbing only |
| `anchor-A19` | nothing computed | A19 | plumbing only |
| `states-drop` | state list → 5 | A11 | **right** (the state-count anchor) |
| `stab-lax` | stabilizer → all 120 | A07, `SYN-Q4-NAME-BLIND`, `SYN-POSITIVE-CONTROLS` | **right**, and the strongest mutant in the suite: Q1 and Q4 genuinely flip to ARTIFACT |
| `action-weaken` | 1 law, 1 state, trivial group | A11, A13, `SYN-FAMILY`, `SYN-Q4-NAME-BLIND`, `SYN-NEGATIVE-CONTROL`, `SYN-ACTION-NOT-TOO-WEAK`, `SYN-NONDEGENERACY`, `SYN-ST-BROKEN`, `SYN-ST-NAME-READER` | the two intended gates are present — but **over-broad**, see F5 |
| `transport-lax` | transport → identity | `SYN-Q4-NAME-BLIND` | right, but **not** `SYN-ST-RELABEL` (F1) |
| `name-reader` | Q4 + label bit | `SYN-Q4-NAME-BLIND` | **right** |
| `seam-orient` | meet ↔ join | A14 | **right** (the seam anchor); the Q8 *verdict* is untested |
| `hol-sign` | closed → unclosed | A09 | right for the value; leaves `SYN-ST-SWITCH` passing (F6) |
| `hol-orient` | closed → reversed | A09 | same |
| `degeneracy-lax` | `_is_neutral` → False | `SYN-DEGENERACY` | right, but a predicate stub |
| `born-lax` | `born(A) = A` | A19, `SYN-QOPT-T1`, `SYN-QOPT-VALUE` | **right**, and Q-OPT correctly becomes `BLOCKED-AT-IMPORT` |
| `srcscan-lax` | scan output → {} | `SYN-SWITCH-SCOPE` | right, but a gate-input stub |
| `float-lax` | float list → [1] | `SYN-EXACT` | right, but a gate-input stub |
| `eps-lax` | `L3.state_map` → 0 | A11 | right for what it breaks — but see F7 |
| `omega-lax` | `q7_omega` → 1 | A16 | **right**; nothing else notices — see F8 |

---

**F4 — Six of twenty mutants perturb no computation. [MODERATE]**

The `anchor-*` mutants are applied at lines 1631–1634, **after** every value
has been computed, by overwriting `x["computed"] = "MUTATED"`. They test that
a failed anchor propagates to exit 1; they do not test that the anchor's
computation is load-bearing. Adding `float-lax` (stubs the float list),
`srcscan-lax` (stubs the scan output) and `degeneracy-lax` (stubs the
predicate), **9 of 20 mutants stub a gate's own input rather than perturb an
instrument.** The effective instrument-perturbing count is 11.

*Repair:* say so in Appendix B, and make the anchor mutants perturb the
computation each anchors (`hol-sign` already shows how — it earns A09 by
breaking the holonomy convention, not by overwriting the field).

**F5 — `action-weaken` is over-broad and cannot isolate. [MINOR]**

Because the mutation is applied *after* `build_family()`, the mutant also
breaks A11 (13 → 1 state), A13 (5 → 1 law) and `SYN-FAMILY` (65 fibers vs
1 × 1). The paper says it "is killed by the negative control and by
`ACTION-TOO-WEAK` exactly as designed" — literally true, both are in the kill
list — but the mutant fails seven other things first. *Repair:* apply the
restriction before `build_family()` so the family gates stay consistent and
the kill is clean.

**F6 — The §14-mandated sign/orientation mutants never reach the §14 gates.
[MODERATE]** `hol-sign` and `hol-orient` die to anchor A09 only. Under both,
`SYN-ST-SWITCH` still reports `carried_invariant_moved: 0` and
`unclosed_control_moved: 384` and passes, and `SYN-ST-RELABEL` still reports
19,314/19,314. RUNBOOK §14 requires the direction-convention mutants; they are
present and they do pin the right *value*, but neither exercises the symmetry
self-test they were added for.

**F7 — No mutant perturbs ε as the census uses it. [MODERATE]** `eps-lax` sets
`L3.MUTANT = "statemap-lax"`, which stubs `L3.state_map` (returning
`Fr(0), Fr(0), Fr(0)`). Q6 calls `L3.bayes_error`, which `statemap-lax` does
not touch — confirmed by reading `rq0_l3_epsilon_exact.py` line 250 and by the
fact that A15 (Q6 *through the instrument*) survives `eps-lax`. The kill is
A11, the state-map cross-check. So the ARTIFACT verdict for Q6 and its orbit
count 14 have no mutant coverage. Likewise nothing covers the orbit counts
123, 40, 75, nor `SYN-CENSUS-COMPLETE`, `SYN-QOPT-T2`, `SYN-ST-RELABEL`,
`SYN-ST-SWITCH`.

**F8 — The INERT/INVARIANT decision is thinly covered. [MODERATE]**
`omega-lax` flips Q7 from `ARENA-INERT` to `ARENA-INVARIANT` and **no gate
notices** — `SYN-DEGENERACY`'s consistency condition still holds, because
both routes agree that the (mutated) value is not the neutral. Only anchor
A16 catches it. The paper's §9(4) — "Inert is not invariant … ω is the type
specimen and the reason the distinction is first-class" — is therefore
protected by one value anchor plus one predicate stub (`degeneracy-lax`).

**F9 — Mutant runs still emit `RQ0-SYNTH-CENSUS-COMPLETE`. [MINOR]** Fifteen
of the twenty mutants (e.g. `transport-lax`, `name-reader`, `born-lax`,
`seam-orient`) exit 1 with a broken gate or anchor and still carry the
completion tag, because `verdict()` conditions `complete` on four gates only,
not on `must_pass_failures == 0`. Exit 1 protects the delivery; the tag list
should be suppressed on any must-pass failure.

---

### K5(c) Anchors, tower provenance, exit-1-only

Provenance verified — see §1(7). Exit-1-only verified by deliberate breakage —
see §1(6): corrupting A07's committed 12 → 13 gives `rc=1`,
`failed_anchors=["A07"]`, `failed_gates=[]`, all nineteen gates still
`true`, and the verdict tags unchanged. That is the declared behaviour.

---

### K5(d) READS-vs-ACTS (Deviation 3): the alternative declaration

**F10 — The declaration flips 3 of 8 verdicts, including a declared positive
control, and un-earns the completion tag. [MAJOR]**

I implemented two alternative declarations in scratch, changing **only** the
`acts` field — no measured number was touched:

- **A**: every arena coordinate acts on every quantity (the reader who
  rejects the split outright);
- **B**: the declared ACTS ∪ the quantity's own READS that are themselves
  arena coordinates (the mildest alternative).

Both collapse to the same acting set and give the same result:

| | delivered | alternative |
|---|---|---|
| Q1 | `ARENA-INVARIANT` (**positive control**) | **`ARENA-ARTIFACT`** |
| Q2 | `ARENA-INVARIANT` | `ARENA-INVARIANT` |
| Q3 | `ARENA-INVARIANT` | `ARENA-INVARIANT` |
| Q4 | `ARENA-INVARIANT` | **`ARENA-ARTIFACT`** |
| Q5 | `ARENA-ARTIFACT` | `ARENA-ARTIFACT` |
| Q6 | `ARENA-ARTIFACT` | `ARENA-ARTIFACT` |
| Q7 | `ARENA-INERT` | `ARENA-INERT` |
| Q8 | `ARENA-INVARIANT` (**the carried finding**) | **`ARENA-ARTIFACT`** |

`SYN-POSITIVE-CONTROLS` fails, `census_complete` becomes `false`, and the run
does **not** emit `RQ0-SYNTH-CENSUS-COMPLETE`.

Two things must be said, in both directions.

*Against the paper.* Deviation 3 states that the pin does not fix READS vs
ACTS. `SYN-FREEZE`'s `census_evaluations_so_far == 0` is a **within-run**
ordering witness only: `QUANTITIES` is a module-level literal, and a
declaration authored after seeing results would still leave the counter at
zero. So the one declaration that determines three of eight verdict labels has
**no external pre-registration at all** — the pin (`a14bda0`) does not carry
it. Under a defensible alternative, three labels move and the census's own
completion tag is not earned. The abstract's "Six do not move" is therefore
declaration-relative in a way the abstract does not say.

*For the paper.* The mitigation is real and it works: the full dependence
profile of every quantity over every coordinate is measured and printed, and
the columns are honestly annotated ("5 (its argument)", "3 (its argument)").
A reader who disputes the split can read the flip off the delivered table —
I did exactly that, and the run confirmed it. And critically for K4:
**Q5 and Q8 face the identical action** — same READS (`patch`), same ACTS
(`law, state, relabelling, switching`), same fibration, same 3,219-instance
sweep. The comparison at the heart of the paper is apples-to-apples.

*Repair that would satisfy me:* (a) restate the abstract and §5.3 headline in
the form the census actually earns — *at a fixed patch declaration, the
legitimacy certificate moves with the law while the seam does not* — rather
than the unqualified "six do not move"; (b) put the flip table above into
Deviation 3, naming which verdicts are declaration-robust (Q2, Q3, Q5, Q6, Q7)
and which are not (Q1, Q4, Q8).

---

### K5(e) Fixture-truth freeze, source scan, AST extraction

**Gate order.** Confirmed from the receipt: `SYN-FREEZE` (index 0,
`census_evaluations_so_far: 0`, 8 quantities, declaration sha256 recorded),
`SYN-SWITCH-SCOPE` (index 1), then `SYN-FAMILY` (2), `SYN-Q4-NAME-BLIND` (3),
`SYN-DEGENERACY` (4), `SYN-CENSUS-COMPLETE` (5) … The declarations do precede
every result, and name-blindness is gated before the degeneracy and
completeness gates, as the pin's order requires. The `_FROZEN` guard is real.

**F11 — The source scan is one level deep, and its "negative control" is a
stub of its own output. [MINOR]** `SYN-SWITCH-SCOPE` scans only
`inspect.getsource(fn)` of the quantity function itself. Demonstrated: a
quantity whose body calls a helper that calls
`L5.cycle_basis_holonomies` returns **`[]`** amplitude tokens under the gate's
scan while its value demonstrably depends on amplitude data (I built one and
it returned `(2, (4,))`). Such a quantity would be declared "switching-blind
by construction" and never swept. `srcscan-lax` blanks the scan's *output*;
it is not a control on the scan's *reach*. *Repair:* scan the transitive
closure of a quantity's callees within the census module, or — cheaper and
stronger — drop the structural shortcut and sweep all eight quantities over
the 512 switchings by measurement (seven extra sweeps of memoized values).

**F12 — A11 anchors the thirteen AST-extracted states only up to permutation
within ε-degenerate rows. [MINOR]** A11 zips the extracted `(label, ρ)` pairs
against the L3 receipt rows and compares the ε **triple** only; the state
**vectors** are not in the receipt and so are not pinned. Measured: swapping
"sink mass moved to address 0" ↔ "address 1" leaves A11 at `[13, True]`;
swapping "address 2" ↔ "address 3" likewise. The count *is* gated —
truncation gives `[5, True]` and `states-drop` dies at A11 — so the negative
control exists and works for the failure mode it covers. *Repair:* one clause
in §4 or Deviation 2 stating the anchoring is up to permutation of the four
ε-degenerate rows, or add a per-state vector hash.

---

## 3. K1 — the family (lower depth)

|𝒜| recomputed independently: **1,648,128** = 3 × 1073 × 512. 65 fibers,
Σ|G| = **1073**. Fiber-size histogram: `{1: 17, 6: 24, 12: 4, 24: 16, 120: 4}`;
17 fibers carry the trivial group. A flat product would be 11,980,800.

**Does the fibering smuggle arena-dependence into the action?** I looked for
the specific failure the protocol names — a quantity invariant only because
the fiber group is small exactly where it would move. It is not present: the
2,144 discriminating instances per quantity are supplied by the large fibers
(the four |G| = 120 fibers and the sixteen |G| = 24 fibers), and every quantity
gated invariant is fixed across **those** fibers as well as the trivial ones.
The 17 trivial fibers contribute zero discriminating instances and therefore
cannot manufacture an invariance verdict. The fibration is the defensible
choice — a flat product would count relabellings that no arena admits — and
Deviation 1 declares the departure from the pin's product sign correctly.

The one substantive qualification is F3's mechanism: because every admitted σ
fixes the law setwise and the state pointwise (0 violations in 1,073
relabellings), the relabelling coordinate is *only* a patch-renaming
coordinate. That is a fact about the declared data, not a defect, but it makes
"acts on the whole configuration" a weaker statement than its wording.

---

## 4. K2 — verdict soundness (lower depth)

All orbit counts and sweeps recomputed with native equality — Q5 = **123**
under law, Q6 = **14** under state with **8** at one patch, Q1 = 5, Q4 = 40,
Q8 = 75, Q2 = Q3 = Q7 = 1; Q1/Q3/Q4/Q5/Q6/Q7/Q8 all `0/3219` equivariance
failures with `2144` discriminating; Q2 `0/512` under switching.

**Are the nondegeneracy (content) gates real or vacuous?** Mixed.

- **Real and gated:** Q1 (`distinct_transition_data == len(laws)` is in the
  predicate — the five laws are separated), Q2 (`len(amb) > 1`: 8 ambient
  holonomy values against 1 admitted — I recomputed 8), Q3 (`len(idf) > 0 and
  proper > 0`: 745 admissible, all 745 proper — recomputed, block counts are
  1 or 2, never 3), Q7 (`nz > 0`: 201 non-zero of 775 — recomputed).
- **F13 — Q8's nondegeneracy witness is reported but NOT gated. [MODERATE]**
  `SYN-NONDEGENERACY`'s predicate (lines 999–1000) is
  `nz > 0 and len(idf) > 0 and proper > 0 and len(amb) > 1 and
  wit["Q1"]["distinct_transition_data"] == len(fam["laws"])`. `wit["Q8"]`
  appears nowhere in it, and its recorded value `one_atom_seams: 1` would pass
  at any value whatsoever. Q8 is the finding the paper carries forward.
  *Repair:* add the Q8 conjunct (the ambient one-atom seam must equal the
  declared neutral, and the family's seams must not).
- **F14 — Q8's independent degeneracy route is dead code and, if reached,
  wrong. [MODERATE]** Both `_is_neutral`'s Q8 branch (line 905) and
  `SYN-DEGENERACY`'s `route2["Q8"]` (lines 838–839) test
  `x.endswith(",1)")` on the canon string. I constructed the declared Q8
  neutral and canonised it:

  ```
  ((0123|4,((0,1,2,3,4)),1),(01|23|4,((0,1,2,3,4)),1),(01|2|3|4,((0,1,2,3,4)),1))
  ```

  Both predicates return **False on the true neutral value**. `route2["Q8"]`
  can therefore never be `True`, at any input. It is unreachable today only
  because Q8 has 75 values, so `len(allv) == 1` short-circuits. The "ROUTE 2,
  independent of the degeneracy predicate" comment is accurate for Q1–Q7 (I
  built all seven neutrals and confirmed the comparison is meaningful there)
  and false for Q8. *Repair:* compare against
  `canon(neutral_value("Q8", lifts))` like every other quantity.

**Is any `[SAMP]` hiding inside a claimed exhaustive sweep?** No hidden ones.
Two declared ones, both correctly disclosed in §10, in the gate `scope`
fields, and in the receipt: the gauge sweep is `[EXH]` 512 switchings ×
`[SAMP]` 32 of 512 lifts (whole family at base gauge via A09); the Δᴮ
reversible sweep is `[SAMP]` 576 of 14,400. **F15 [MINOR]:** the *abstract*
drops the qualifier — "constant at ζ₈⁴ = −1 over the whole admitted lift
family **and** under all 512 switchings" reads as the cross product, which is
not swept. One clause fixes it.

---

## 5. K3 — Q-OPT (lower depth)

**The arithmetic transports, genuinely.** A19 reproduces
`v12/paper1-composition-defect.md` line 339 verbatim, in exact ℚ(ζ₈);
`born-lax` kills A19 + `SYN-QOPT-T1` + `SYN-QOPT-VALUE` and correctly turns
the verdict into `BLOCKED-AT-IMPORT` — reproduced.

**F16 — The receipt contradicts the paper on the second transport.
[MODERATE]** The delivered receipt records
`findings.Q_OPT.transport_object: false` and
`SYN-QOPT-T2.value.the_object_transports: false`, while §8 says "**The object
transports**, and is then empty" and Deviation 4 says "the transport succeeded
in both senses". The code's `t2 = any(admits.values())` computes a *different*
proposition — "some committed law admits the lifted step" — and `t2` is then
ignored by the verdict (`t1 and nz == 0 and ctrl_nonzero`). No number is
wrong; two frozen artifacts state opposite things in the words a reader checks
first. *Repair:* rename the field to
`some_committed_law_admits_the_lifted_step`, or restate §8 / Deviation 4.

**F17 — The 576-pair reversible census is vacuous, and its "sample" is a
subgroup. [MODERATE]** Two measurements:

1. `perms[:24]` is exactly the point stabiliser of configuration 0 — I checked
   that all 24 fix 0 and that the set is closed under composition. So the
   "576 pairs" are H × H for a subgroup H, not a sample of the 120.
2. Δᴮ vanishes on **all** 14,400 admitted permutation pairs — I ran the
   exhaustive sweep. It is forced: a permutation matrix over {0, 1} satisfies
   `born(P) = P` entrywise, so `B(PQ) = PQ = B(P)B(Q)` identically.

So the zero is a one-line theorem, not a measurement, and the `[SAMP]` is both
unnecessary and structurally degenerate. `SYN-QOPT-VALUE`'s claim text ("Over
**every** composable pair of admitted reversible operations") also disagrees
with `SYN-QOPT-SCOPE`'s `[SAMP]` inside the same receipt. *Repair:* run all
14,400 (it costs seconds), delete the `[SAMP]`, and state the monomial
argument so the zero reads as the theorem it is. The real content — the
positive control at 384/512 on the non-monomial family, and the obstruction
that no committed law admits such an operation — is unaffected and is
correctly gated by `SYN-QOPT-T2`'s two-route consistency (liftable counts
120/1/120/1/1 by both routes, reproduced).

**Verdict vocabulary.** `ARENA-INERT-Q-OPT` with
`BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION` as a *named obstruction*
rather than as the verdict is pin-compliant: the pin's `ARENA-INERT` is
"fixed but degenerate", which is exactly identically-zero, and Deviation 4
declares that `BLOCKED-AT-IMPORT` was available and unused. I do not challenge
this.

---

## 6. K4 — the asymmetry (lower depth)

**Do Q5 and Q8 face the same action?** Yes — verified from the frozen
declaration table: identical READS (`patch`), identical ACTS
(`law, state, relabelling, switching`), the same 65-fiber fibration, the same
3,219-instance relabelling sweep with the same 2,144 discriminating. The
comparison is apples-to-apples. This is the strongest thing in the paper and
it survives.

**Is Q8's invariance contentful?** Its 75 values are never the declared
neutral — I recomputed the atom counts and they are exactly {2, 3}, never 1 —
so the *fact* is right. But the *gate* is not: F13 (the witness is ungated)
and F14 (the independent route cannot fire for Q8). The paper's carried
finding is therefore measured but under-gated.

**Does the chain trivialise the seam?** Partly, and the paper should say so.
The three declarations form a chain (δ ⊏ 2+1+1 ⊏ 2+2 ⊏ tomographic minimum),
so every seam is simply the coarser member — the seam datum is a function of
the refinement order alone, which is exactly why nothing but the patch
coordinate can move it. Q8's arena-invariance is, as measured, a fact about a
three-element chain rather than about seams in general.
**F18 [MODERATE]:** §5.3 and §10 should carry that scope limit explicitly
before this rung is handed to a successor; the successor will otherwise
inherit "the seam is arena-invariant" as if it had been tested on
incomparable patches, which it has not.

**Decomposition, recomputed:** 75 = 30 (legitimate) + 15 (forged 2+1+1) + 30
(forged 2+2), which is the paper's "the three declared patches carried
through the admitted relabellings" — confirmed.

---

## 7. Independent recomputations (106)

Family and fixtures (18): Bell 1–5; DET 3125; FUNNEL 21; REV 120;
FUNNEL-CLOSURE 3006; counter-law 120 + 1 reversible; law-set identity vs
`L2.committed_laws`; 13 states typed from source with ε triples vs the L3
receipt; 65 fibers; Σ|G| = 1073; |𝒜| = 1,648,128; fiber histogram; 17 trivial
fibers; flat product 11,980,800; σ·ρ = ρ (0 violations); σ·L = L (0
violations); lift family 512; free vertices 3 / 512 switchings.

Census (24): eight orbit counts by native equality; eight per-quantity
dependence profiles (patch/law/state maxima); eight per-quantity equivariance
sweeps (0/3219, 2144 discriminating).

Seam and self-test (11): Q8 at PTOMO, PI1, P22; self-test (a)
19,314/19,314/12,864; 512 switchings enumerated; self-test (b) 0 / 384;
self-test (c) total and per-quantity split; self-test (d) 728/3,219; memo-hit
instrumentation for the census, self-test and broken-action phases.

Witnesses (3): ω 201/775; identity-free 745/745 with block-count spectrum;
ambient holonomy 8.

Mutants (24): 20 mutant kill lists + exit codes reproduced; 4 mutants
reconstructed from the receipt's prose description alone.

Delivery and gating (5): output.txt byte-identical; receipt.json
byte-identical; deliberate A07 break → exit-1-only; alternative declaration A;
alternative declaration B.

Q-OPT and §5.2 (8): certificate sizes 1280/13/120/1161/60; clause bits and the
REV reachability difference; 0/15 admissible; `perms[:24]` is the point
stabiliser of 0; it is a subgroup; Δᴮ over all 14,400 pairs; `admits` all
false / t2 false; Q8 = 30 + 15 + 30 with atom counts {2,3}.

Instrument probes (6): canon of the Q8 neutral vs both degeneracy predicates;
neutrals constructed for Q1–Q7; one-level source-scan hole; A11 under two
ε-degenerate label swaps; A11 under truncation; `SYN-FREEZE` value.

Provenance (7): anchors A01–A10/A13 vs the L4/L5 terminal receipt anchors;
A09 vs `L5-AMP-CONSTANCY`/`L5-AMP-CONTENT`; A12 and the 384 control vs
`L5-HOL-GAUGE`; A19 vs `v12/paper1-composition-defect.md` line 339; Q3's 745
vs L4 A10; §2's six commits vs the six successor pins; §2's six ledger
entries and verdict names vs `v13/LOG.md`.

---

## 8. Findings, ranked

| # | severity | finding |
|---|---|---|
| F1 | MAJOR | `SYN-ST-RELABEL` cannot fail: no mutant falsifies it, it self-selects on the census's own verdicts, and it makes 0 fresh evaluations (20,484 memo hits) |
| F2 | MAJOR | `SYN-ST-RELABEL` reports but does not gate its anti-vacuity counter; it passes vacuously under `action-weaken` at 24 instances / 0 moved |
| F3 | MAJOR | the §7.3 mis-conventioned control fails only Q8 (0 / 0 / 2,772 of 3,024 each); it differs from the census's own action solely in the `sigma` argument |
| F10 | MAJOR | the READS/ACTS declaration — which the pin does not fix — flips Q1, Q4 and Q8, fails `SYN-POSITIVE-CONTROLS`, and un-earns `RQ0-SYNTH-CENSUS-COMPLETE` |
| F4 | MODERATE | 6 of 20 mutants perturb no computation (9 of 20 stub a gate's own input); effective mutant count 11 |
| F6 | MODERATE | the §14-mandated sign/orientation mutants die to an anchor and leave both §14 gates passing |
| F7 | MODERATE | no mutant perturbs ε as Q6 uses it; orbit counts 123/40/14/75 have no mutant coverage |
| F8 | MODERATE | `omega-lax` flips Q7 INERT→INVARIANT and no *gate* notices — only anchor A16 |
| F13 | MODERATE | Q8's nondegeneracy witness is reported but absent from `SYN-NONDEGENERACY`'s predicate |
| F14 | MODERATE | Q8's independent degeneracy route returns False on the true Q8 neutral — dead and wrong |
| F16 | MODERATE | the receipt's `transport_object: false` contradicts §8 / Deviation 4's "the transport succeeded in both senses" |
| F17 | MODERATE | the 576-pair Δᴮ census is vacuous (`born(P)=P` for permutations) and its sample is the point stabiliser of 0, a subgroup; exhaustive 14,400 gives 0 |
| F18 | MODERATE | Q8's arena-invariance is a fact about a three-element chain; the scope limit should be stated before the rung is handed on |
| F5 | MINOR | `action-weaken` is over-broad (kills 7 unrelated gates/anchors) because it is applied after `build_family()` |
| F9 | MINOR | mutant runs with broken gates still emit `RQ0-SYNTH-CENSUS-COMPLETE` |
| F11 | MINOR | the switching source scan is one level deep; `srcscan-lax` stubs its output, not its reach |
| F12 | MINOR | A11 anchors the 13 states only up to permutation within the four ε-degenerate rows |
| F15 | MINOR | the abstract drops the `[SAMP]` qualifier on the switching × lift cross product |

**No false theorem found. No false number found.** Every delivered numeral I
recomputed is correct; the delivery is byte-identically reproducible; the
anchors are real anchors; the mutant kills all reproduce; §2 is
verbatim-faithful. The defects are gate-design defects — controls that are
reported rather than gated, a self-test that recounts what it should
independently measure, a control with teeth on one quantity in three, and one
declaration carrying more weight than its pre-registration supports — plus one
receipt/paper wording contradiction and two broken routes sitting under the
finding the paper carries forward.

---

## 9. Grade

**ACCEPT-WITH-FIXES.**

Required before terminal, in order: **F2** (one-line predicate fix), **F1**
(self-test over all quantities, unmemoized, with a mutant that kills it),
**F3** (per-quantity split reported, plus a control that bites the nomological
quantities), **F10** (restate the abstract/§5.3 headline in the
fixed-patch-declaration form the census earns, and put the flip table in
Deviation 3), **F14** and **F13** (Q8's degeneracy route repaired and its
witness gated — these sit directly under the carried finding), **F16** (make
the receipt and the paper say the same thing about Q-OPT's second transport),
**F17** (run all 14,400 pairs and state the monomial argument), **F18** (state
the chain scope limit). The remaining MINOR items are disclosure edits.
