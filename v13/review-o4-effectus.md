# HOSTILE REVIEW R2 — EFFECTUS / CATEGORICAL LENS

## The O4 Discriminator (v13), against the frozen protocol

**Reviewer:** R2, structural/conceptual lens (effectus-order, categorical).
**Date:** 2026-08-07.
**Protocol:** `v13/note-o4-hostile-protocol.md` (FROZEN, v13 #192), kill-shots
K1–K5, primary weight on **K3** and on the conceptual soundness of the
discrimination.
**Object:** commit `9fcea62` as-is #191; pin `2568bc528796` @ `e1e8dcd`.
**Interpreter:** `/opt/homebrew/bin/python3.13`. No git. No child agents.

---

## 0. SHA verification (done first, as ordered)

| artifact | required sha256-12 | measured | verdict |
|---|---|---|---|
| `v13/paper-o4-discriminator.md` | `e45c090f226f` | `e45c090f226f` | **MATCH** |
| `v13/code/o4_discriminator_exact.py` | `240a6e05dce7` | `240a6e05dce7` | **MATCH** |
| `v13/code/o4_discriminator_output.txt` | `fd1cb9273951` | `fd1cb9273951` | **MATCH** |
| `v13/code/o4_discriminator_receipt.json` | `b791ec7e2d30` | `b791ec7e2d30` | **MATCH** |

All four match. The review proceeds.

**Recomputation count: 532 independently recomputed quantities**, across six
scratchpad scripts built directly on `model_composite` / `w6_coreference_exact`
(not on the O4 instrument, except where the instrument's *own* predicate was
deliberately re-run at a coordinate the unit does not visit), plus two full
delivery-mode reruns of the frozen script.

---

## 1. What reproduces

Recorded first, because the negative findings below are findings about
*meaning*, not about arithmetic. I found **no false computed number** anywhere
in this unit.

1. **Byte-identical delivery.** A full `--falsification-selftest` rerun
   regenerates `o4_discriminator_output.txt` and `o4_discriminator_receipt.json`
   byte for byte (`fd1cb9273951`, `b791ec7e2d30`). 27 anchors pass, 21 gates,
   0 must-pass failures. Determinism claim (§12) upheld.
2. **§6's obstruction table.** Recomputed from the model's own legs and
   `p(0)=δ_{j_0}` without touching the instrument: all twelve occupied sets,
   all six intersections (0) and unions (10,10,16,16,4,16) reproduce exactly.
3. **§7's LTP residual.** `‖r‖₀ = (0,0,16,16,0,16)` in **both** frames,
   recomputed as the `j_0` column of `Γ(3←0) − Γ(3←2)Γ(2←0)` in the exact
   field. Value censuses reproduce: SP-C four distinct values, **zero**
   rational of sixteen; SP-F six distinct, **eight** rational. Rationality by
   the field's own test.
4. **D1's 288.** The full matrix residual is `(0,0,288,288,0,288)` in both
   frames, `= 16 × 18`, independently recomputed.
5. **§5's gate table and transport counts.** 135 gate cells and 90 count cells
   transcribed from the paper and checked against the receipt: **0 mismatches**.
6. **§8's arena rows.** QA1 moves under {setting, frame, relabelling}, 4
   distinct values, orbit 2 per chart; QA2 moves under {setting}, 2 distinct,
   orbit 1. Reproduced by an independent 192-point sweep.
7. **§2's arena arithmetic.** 72-element scope, `j_0` filter admitting 2;
   96-element extension admitting 8; 2³ = 8 switchings; 6×2×2×8 = 192.
8. **The level census.** `exact` is measured non-covariant with **24**
   switching failures; `sign` and `born` are covariant with 0. §8's claim holds.
9. **Instrument hygiene.** The freeze counter is real (`_FEVALS == 0` and
   `len(GATES) == 0` at the freeze). The fresh-evaluation self-test genuinely
   bypasses the memo (`memo-lax` → `O4-ST-FRESH`). The mutant census is
   17-of-17 with `never falsified []`, and D6's eighteenth gate is killed by
   `verdict-lax` → `O4-VOCABULARY`, as claimed.
10. **The verdict derivation is honest about coordinates.** I read
    `derive_candidate_verdict` line by line looking for the classic leak — an
    SP-A-only gate (TRI/GLUE) contaminating per-coordinate verdicts at other
    settings. It does not leak: `passes(row, sp)` applies TRI/GLUE **only** at
    `sp == "SP-A"`. Credit where due.
11. **No dead verdicts in the outcome selector.** I constructed green rows by
    hand and confirmed `derive_candidate_verdict` emits both `O4-RULE-EXISTS`
    (with LTP-LAWFUL) and `O4-RULE-EXISTS-LTP-BARE` (with LTP-BARE). The
    outcome space is reachable.
12. **A K1 result stronger than the paper's.** The paper measures disjointness
    on the six *committed* pairs. I swept all 66 unordered pairs of the twelve
    charts: **all 36 cross-frame pairs are disjoint at the intermediate time;
    all 30 same-frame pairs share**. Disjointness tracks the frame coordinate
    exactly and is not an artifact of which pair was committed. This is a
    genuine strengthening of §6 and should be adopted.

---

## 2. Findings

### MAJOR-1 — The discrimination is a TIME effect, not a CLASS effect. The unit never runs the cell that would show this, and its own anchors already carry it.

**Severity: MAJOR.** This is the finding that governs my grade.

The unit's headline is that *record facts transport and unrecorded
configuration facts do not*. But the two classes are read at **different
times**: `datum_rec` reads the chart at the final time ("read at the time every
token has been written"); `datum_cfg` reads `c.dist(2)`, the intermediate time.
The positive control is therefore evaluated at the one coordinate where the
base itself proves the two frames' laws agree, and the object at the one
coordinate where the base itself proves they differ.

I ran the missing cell: **the unit's own `transports_rec`, with the unit's own
candidate declarations, the unit's own permutation scopes and the unit's own
matching levels, applied to the record class at the intermediate time.**

| candidate | F-REC @ final | **F-REC @ intermediate** | F-CFG @ intermediate |
|---|---|---|---|
| **C2** | `[1,1,1,1,1,1]` | **`[0,0,0,0,0,0]`** | `[0,0,0,0,0,0]` |
| **C3** | `[1,1,1,1,1,1]` | **`[0,0,0,0,0,0]`** | `[0,0,0,0,0,0]` |
| **C4** | `[0,0,0,0,1,1]` | **`[0,0,0,0,1,1]`** | `[0,0,0,0,1,1]` |

**Identical, candidate by candidate, setting by setting.** And the certificate
behaves the same way:

| setting | F-REC CERT @ intermediate | disagreeing configs | F-REC CERT @ final |
|---|---|---|---|
| SP-A | `DISAGREEMENT` | 10 | `True` (0) |
| SP-B | `DISAGREEMENT` | 10 | `True` (0) |
| SP-C | `DISAGREEMENT` | 16 | `True` (0) |
| SP-D | `DISAGREEMENT` | 16 | `True` (0) |
| SP-E | `DISAGREEMENT` | 4 | `True` (0) |
| SP-F | `DISAGREEMENT` | 16 | `True` (0) |

Those disagreeing-configuration counts are exactly §6's union sizes. The record
class, read where the object is read, is refused by the same certificate, with
the same numbers.

This is not news to the base, and it is **anchored in this very unit**:

- **A13** — `|Φ_A|` and `|Φ_B|` at the intermediate slice = `((1,1,1,1,1,1),
  (0,0,0,0,0,0))`. The instrument's own F-REC transport is a Φ_B object
  (`transports_rec` calls `W6.phi_set(..., items=LIST_B, ...)`), and Φ_B is
  **zero at every setting** there.
- **A14** — shared record subalgebra at the intermediate time = `(0,0,0,0,0,0)`.
- W6's M4 row, quoted in the base note: *"FORCED but NOT CERTIFIED — ROUTE-EXT
  at t = 2 refuses it at every setting"*, `|Φ_B| = 0`, `NO-INSTRUMENT`.

§6 half-concedes it — *"Where the base measured that the records do not overlap
there, this unit measures that the configurations do not either"* — and then
proceeds to report the class contrast as the result.

**What this costs.** Two things:

1. **There is no positive control at the object's coordinate.** §3/§5 rest the
   whole instrument on the claim *"If the instrument could not reproduce the
   base's own positive result, nothing it says about the object would mean
   anything."* But the control is green only at a coordinate the object never
   occupies. A control that cannot be green where the negative is reported is
   the mirror image of a gate that cannot fail — the pathology RUNBOOK §14 was
   written about.
2. **The verdict name over-claims.** `O4-DISCRIMINATED-RECORD-ACTUALISM`
   asserts a class discrimination. What is measured is: *at a declared division
   event, facts descend; at the intermediate time, nothing descends under this
   instrument — records included.*

**Not fatal, and the repair is cheap and makes the paper stronger.** There *is*
a genuine class-level difference at fixed time, and the unit already anchors
it: at t = 2, W6 measures `|Φ_A| = 1` for records (forced, uncertified) against
`0` transports for configurations. That is a real asymmetry at one coordinate
and one matching level, and it is the claim the unit can actually carry.

**Repair.**
(a) Add the F-REC@intermediate row to §5 as a fourth row, with the numbers
above — the instrument already builds the `@t2` charts inside `run_anchors`.
(b) Either restate the result as time-indexed (*"facts descend at division
events and not between them; the record class is no exception"* — which is a
better result, and welds directly to §7's finding that the intermediate time is
not a division event), or, if the class reading is wanted, isolate it at fixed
time via the Φ_A/Φ_B contrast and scope it to that level.
(c) Re-scope the abstract's *"The record class reproduces the base's terminal
descent results under this instrument (positive control)"* with the time tag.

---

### MAJOR-2 — The named obstruction is asserted, not measured, as a cause; and the paper's own C4 row falsifies it as stated.

**Severity: MAJOR.**

`O4-OBSTRUCTION-NAMED`'s **predicate** is only
`all(v == 0 for v in inter.values())` — it measures that the intersections are
zero. Its **claim string** then asserts causal responsibility: *"That is the
object on which every F-CFG transport count below is measured to die."* §6
repeats it. Nothing computes the attribution.

I decomposed the F-CFG transport predicate into its four successive clauses
(`j_0` filter → `legs_compatible` → actual-set → law) for all five candidates
at all six settings. The result:

| candidate | perms in scope | pass `j_0` | pass **legs** | pass actual-set | pass law |
|---|---|---|---|---|---|
| C1 | 72 | 2 | **0** | 0 | 0 |
| C2 | 72 | 2 | **1 (the identity)** | 0 | 0 |
| C2X | 72 | 2 | **1 (the identity)** | 0 | 0 |
| C3 | 96 | 8 | **1 (the identity)** | 0 | 0 |
| C4 | 72 | 2 | 0 (SP-A..D) / **1 (the wing swap)** (SP-E,F) | 1 | 1 |

Two things follow.

**(i) The disjointness is not what excludes the map that would have worked.**
Under C2/C2X/C3, the sole legs-compatible admitted permutation is the
**identity**, and the identity fails the support clause because the supports are
disjoint — so far, so consistent with §6. But the **wing exchange**, which *does*
carry F2's occupied set onto F1's at SP-C, SP-D, SP-E and SP-F, and which at
SP-E and SP-F *additionally preserves the exact intermediate law*, is excluded
one clause earlier, at `legs_compatible` on the full declared legs. The object
that kills the candidate transport is the leg-matching clause, not the
disjointness. Measured, per candidate, per setting:

| candidate | wing swap: legs? | actual-set? | law? |
|---|---|---|---|
| C2 / C2X / C3 @ SP-E, SP-F | **False** | True | **True** |
| C2 / C2X / C3 @ SP-C, SP-D | **False** | True | False |
| C4 @ SP-E, SP-F | **True** | True | True |

**(ii) "Every F-CFG transport count is measured to die" is contradicted by the
paper's own §5 table.** C4's F-CFG row is `1` at SP-E and SP-F, on exactly the
same disjoint supports. The paper reports this itself, three pages earlier
(§5 reading 3), and never reconciles it with §6.

**What survives.** The disjointness *is* sufficient for the CERT failure —
`route_ext_pair` returns `DISAGREEMENT` whenever `dis ≠ 0`, and disjoint
non-empty supports force `dis ≥ |S₁| + |S₂| > 0`. So the honest statement is:
*the disjointness is what the certificate refuses, at every setting and for
every candidate, because the certificate is candidate-independent.* That is
true and I verified it. It is a much narrower statement than the one made.

**Repair.** Replace the universal causal sentence in §6 and in
`O4-OBSTRUCTION-NAMED` with the per-clause decomposition above; state that the
disjointness is decisive **through CERT**; delete "every F-CFG transport count"
or restrict it to C1/C2/C2X/C3.

---

### MAJOR-3 — At four of six settings the two occupied sets lie in one orbit of the base's own admitted group, and this is nowhere disclosed.

**Severity: MAJOR.**

§6 exhibits the twelve supports and says they are *"not merely unequal, but
sharing no configuration at all."* True. What it does not say:

| setting | F1 support | F2 support | carried onto each other by the **admitted wing exchange**? | by any of the admitted-extension 8? |
|---|---|---|---|---|
| SP-A | `{12,24}` | `{1,2,10,11,19,20,28,29}` | **no** (sizes 2 vs 8) | no |
| SP-B | `{12,24}` | `{1,2,10,11,19,20,28,29}` | **no** (sizes 2 vs 8) | no |
| SP-C | 8 elts | 8 elts | **YES** | 4 of 8 |
| SP-D | 8 elts | 8 elts | **YES** | 4 of 8 |
| **SP-E** | `{12,24}` | `{11,19}` | **YES, and it preserves the exact Born law** | 2 of 8 |
| **SP-F** | 8 elts | 8 elts | **YES, and it preserves the exact Born law** | 4 of 8 |

At SP-E both supports carry Born weight `(1/2, 1/2)` and the wing exchange
maps one onto the other exactly. At SP-A and SP-B the disjointness is
gauge-robust — but for a trivial reason: the sets have different cardinalities,
so *no* bijection whatever relates them, admitted or otherwise.

This matters for three reasons.

1. The base's **deepest finding** is about that very group element (W6: *"at
   SP-E and SP-F exactly one token map survives ... the wing swap, which is the
   opposite of the identity the full declared legs force"*). Reporting a
   disjointness whose two sides are exchanged by the wing swap, in a unit built
   on that base, without saying so, withholds the datum the reader needs.
2. It is the mechanism behind C4. I identified the map: **C4's F-CFG transport
   at SP-E and SP-F *is* the wing exchange** (not the identity), and C4's F-REC
   transport there is the corresponding token swap `((0,1),(1,0))`. The paper
   reports C4's counts and never names the map.
3. It sets up MODERATE-1: at SP-E and SP-F, both classes transport uniquely by
   *the same group element*, and the only gate separating them is a
   candidate-independent, name-bound certificate.

**Repair.** Add an orbit column to §6's table. State plainly that at SP-C/D/E/F
the two supports are one orbit of the declared admitted group, that at SP-E/SP-F
the wing exchange preserves the exact intermediate law, and that at SP-A/SP-B
the disjointness is cardinality-forced. Name C4's transport.

---

### MAJOR-4 — The arena test compares a name-indexed quantity with a name-free one. The "relabelling" leg of `O4-ARENA-RELATIVE` is the negative control's own failure mode.

**Severity: MAJOR.**

- **QA1** = `tuple(1 if i in d["actual"] else 0 for i in range(NC))` — a 36-bit
  vector **indexed by configuration name**.
- **QA2** = `tuple(sorted(canon(k) for k in c.law))` — a set of record
  **values**, carrying no configuration name at all.

Under a relabelling `g`, QA1's entries permute by construction; QA2's cannot
move. The measured difference "F-CFG moves under relabelling, F-REC does not"
is therefore fixed before any physics is consulted — and reading a label the
declared gauge is free to change is precisely how the paper *defines* its
negative control F-CTRL (§3.1).

I built the like-for-like counterpart. **QA1′** is the same intermediate datum
with the names quotiented out: the sorted multiset of the exact probabilities
on the occupied support — the same construction that makes QA2 name-free.

| quantity | moves under | distinct values over the family | orbit per chart |
|---|---|---|---|
| QA1 (as delivered, name-indexed) | setting, frame, **relabelling** | 4 | **2** |
| QA2 (as delivered, name-free) | setting | 2 | 1 |
| **QA1′ (name-free F-CFG)** | setting, frame | **3** | **1** |

So §8's central measured sentence — *"The unrecorded-configuration class's
truth-values move under both: orbit size **2** at every one of the twelve
charts, four distinct truth-value vectors over the whole arena"* — and the
abstract's *"in orbits of measured size 2, with four distinct truth-value
vectors over an arena of size 192"* are **carried entirely by name-reading**.
Quotient the names and the orbit is 1 at every chart and the count is 3.

The `O4-LIKE-FOR-LIKE` gate does not cover this. Read it: it checks that every
fact-class row carries every declared gate key and that the three transport
functions share one signature. It never touches `ARENA_QUANTITIES`. The arena
test — which supplies half the unit verdict — has no like-for-like gate at all.

**What survives.** The **frame** leg survives the name-free reading, and the
`arena_relative` predicate in `run_verdict` (`cfg["moved_under"]` non-empty and
different from `rec["moved_under"]`) would still fire with QA1′. So the verdict
*term* survives; §8's measured content does not, and it must be restated.

**And it survives only at four of six settings.** Name-free, the two frames'
intermediate data are **equal** at SP-E and SP-F:

| setting | QA1′(F1) | QA1′(F2) | equal? |
|---|---|---|---|
| SP-A / SP-B | `(1/2, 1/2)` | eight-element multiset | no |
| SP-C / SP-D | `(1/8)×8` | eight-element multiset | no |
| **SP-E** | `(1/2, 1/2)` | `(1/2, 1/2)` | **YES** |
| **SP-F** | eight-element multiset | same multiset | **YES** |

Which is exactly why C4 finds a transport at SP-E and SP-F and nowhere else.
The paper's framing ("the unrecorded class's truth-values move with the frame")
is name-free-true at SP-A–SP-D and name-free-**false** at SP-E–SP-F.

**Repair.** Declare QA1′ (or any name-free F-CFG datum) as the arena quantity
and report both; restate §8's orbit sentence; withdraw "relabelling" from the
name-free moved-under set; scope the frame claim to `[SP-A, SP-B, SP-C, SP-D]`.

---

### MAJOR-5 — The dual verdict double-counts one measurement.

**Severity: MAJOR.** (My brief asks this directly; the answer is yes.)

Strip MAJOR-4's naming artifact and what is left of `O4-ARENA-RELATIVE` is:
*QA1 moves under the frame coordinate.* That statement is, term for term:

- **=** "the two frames' occupied supports at the intermediate time differ"
- **=** §6's obstruction
- **=** the `dis ≠ 0` that makes CERT return `DISAGREEMENT`
- **=** the reason the identity fails the support clause in `transports_cfg`

One measurement, four presentations. `O4-DISCRIMINATED-RECORD-ACTUALISM` and
`O4-ARENA-RELATIVE` are therefore not two independent earnings; the second is
the first restated in truth-value language, plus a name artifact. The abstract
presents them as co-equal (*"The arena test decides the shape of the result"*),
and §9.2 says *"Both parts are pre-registered outcomes of the pin and both are
earned by measurement"* — which is true of the vocabulary and misleading about
the evidence.

**Repair.** Either report `O4-ARENA-RELATIVE` explicitly as a restatement of
the §6 obstruction in the arena's language, scoped `[SP-A..SP-D]` under the
name-free reading, or drop it from the headline and keep it as a §8 remark.
Do not present it as a second earned outcome.

---

### MAJOR-6 — Strengthening-in-paraphrase of the charter, with a load-bearing consequence.

**Severity: MAJOR.**

§1 says *"Paper 0 v2.4 §5 states the fork and its prices"* and then sets a
**blockquote**. The blockquote is not paper 0's text. Diff against
`v12/relativistic-isp-v12-paper0-the-weld.md` §O4:

**Dropped from O4-A:**
1. the attribution *"BC2 shows"*;
2. the scope parenthetical **"(scoped to that formal apparatus, not to
   relativity in nature)"**;
3. **"a preferred structure is one possible completion, *not yet a forced
   conclusion*"**;
4. the fulcrum's mechanism *"[B3]'s own axioms deny composite division events
   exactly where the process is indivisible"*.

**Dropped from O4-B:**
5. **"unrecorded configurations are variables of the nomological
   representation"**;
6. *"the result departs from Barandes configuration realism"*.

Items 3 and 5 are load-bearing.

**Item 3.** The dropped clause is the charter's own hedge *against* reading the
missing co-reference rule as forcing a preferred structure. §10 then asserts,
without that hedge on the page, *"The illegitimate route is not merely
illegitimate; on this base it is empty."* That is a claim strictly stronger
than the sentence it silently removes. (It is also independently wrong as
stated — see MAJOR-7.)

**Item 5.** §10 says the unit adds *"one further clause, **which is not in the
charter's statement of either branch**"*, namely that unrecorded configuration
truth-values are arena-relative. But paper 0's O4-B **already says** unrecorded
configurations are *variables of the nomological representation* — that the
values of a representational variable depend on the representation is not an
addition. §10's own next sentence concedes it: *"A branch that keeps unrecorded
configurations as variables of the nomological representation is consistent
with that."* The novelty claim survives only against the truncated quotation
the paper itself supplies.

**Repair.** Quote paper 0 verbatim, or mark the passage explicitly as a
paraphrase and carry clauses 2, 3 and 5 in the surrounding text. Restate §10's
novelty as *"the charter's own O4-B clause, here measured with an orbit"* —
which is a real and defensible contribution.

---

### MAJOR-7 — "Leaving the corridor is empty" is carried by the leg-order convention, not by the global-now reading; and the NOSLICE gate tests only one of the corridor's two stipulations.

**Severity: MAJOR.** (My brief: *does the no-slice corridor bite for the RIGHT
reason, or merely because the committed frames differ by leg order?* Measured
answer: **the emptiness is the leg order; the gate bites on something else
again.**)

C1 changes **three** declarations at once relative to C2X: `level`,
`order_free=False`, `drop_identity=False`. I separated them.

| probe | level | order_free | drop_identity | F-REC counts | F-CFG counts | NOSLICE |
|---|---|---|---|---|---|---|
| **C1 as declared** | exact | False | False | `[0,0,0,0,0,0]` | `[0,0,0,0,0,0]` | **fail (12/12 charts)** |
| **C1a** order-free only | exact | **True** | False | **`[1,1,1,1,1,1]`** | `[0,0,0,0,0,0]` | **fail (12/12 charts)** |
| **C1b** identity-blind only | exact | False | **True** | `[0,0,0,0,0,0]` | `[0,0,0,0,0,0]` | PASS |
| C2X | exact | True | True | `[1,1,1,1,1,1]` | `[0,0,0,0,0,0]` | PASS |
| C2 | born | True | True | `[1,1,1,1,1,1]` | `[0,0,0,0,0,0]` | PASS |

And the gate's sensitivity, swept over all eight `(level, order_free,
drop_identity)` combinations:

> **NOSLICE PASS ⟺ `drop_identity = True`.** It is measured **insensitive** to
> `order_free` and to `level`, 8 probes out of 8.

Three consequences.

1. **C1's emptiness is the leg-order convention.** Flip `order_free` alone and
   the *same* slice-reading, identity-leg-counting rule — still failing NOSLICE
   at all twelve charts, still outside the corridor by the unit's own gate —
   transports the record class at **every** setting. §10's *"measured on this
   base, the slice rule admits zero transports at every setting for every
   fact-class, because the two frames of one experiment differ exactly by the
   order of two commuting legs and an index-bound rule cannot match them"*
   correctly names the mechanism, and then draws from it a conclusion about
   *reading a time index* that the mechanism does not support.
2. **The corridor's second stipulation is ungated.** §3.3 defines a
   corridor-bound rule as one that *both* drops identity legs *and* matches
   order-free. NOSLICE tests the first. Nothing tests the second — and the
   second is what empties C1.
3. **The declared outside-corridor control kills the positive control.**
   C1's F-REC row is `0` at all six settings. A candidate that cannot transport
   the facts W6 *proves* descend is not a serious preferred-structure
   completion; it is a mis-built rule. Its zeros measure its own convention.

**What survives, and it is worth saying.** With `order_free` restored (C1a),
the slice-reading rule still gets `F-CFG = 0` at every setting. So the honest
form of §10's second bullet is: *a preferred slice does not help here, because
the supports at the shared index are disjoint* — not *the slice rule cannot
even match the legs*. The first is a result; the second is a convention.

**Repair.** Add C1a (or equivalent) as the slice-reading candidate that
survives the leg convention, and re-derive §10's bullet from it. Either gate
the order-free stipulation or declare it as an untested corridor axiom in §11.

---

### MODERATE-1 — CERT, the gate that carries the negative at SP-E/SP-F, is candidate-independent and, for F-CFG, a name-bound identity test — the criterion the corridor forbids.

**Severity: MODERATE**, rising to MAJOR if the paper keeps CERT as the
decisive gate without taking a position.

`certify(fid, fn)` takes no candidate argument; D4 discloses this. Its verdict
comes from `route_ext_pair(K, joint, dis)`, which returns `DISAGREEMENT`
whenever `dis ≠ 0`, where

```
dis = #{ i : p_F1(i) ≠ p_F2(i) }
```

— a **pointwise comparison in the configuration name, with no transport
interposed**. For F-CFG, the certificate is satisfied only if the *identity* is
the co-reference map. That is the naive-slice reading (C1) that the corridor's
own no-slice and name-blindness clauses reject. A rule *inside* the corridor is
being refused its certificate by a criterion only the *forbidden* rule could
meet.

At SP-E and SP-F this is decisive and nothing else is. There, under C4, both
classes transport **uniquely, by the same group element** (the base's own wing
exchange), with the exact intermediate law preserved. `cfg_ok` in
`derive_candidate_verdict` is `counts == 1 and cert_per_setting`; the counts are
equal; the certificate is the sole separator. So the unit's `DISCRIMINATED`
verdict at those two coordinates rests entirely on a candidate-independent,
name-bound test.

A second asymmetry inside the same gate: `dis` is read on `ca.dist()` (final
time) for F-REC and on `ca.dist(2)` (intermediate) for F-CFG. So the pair guard
compares frame-invariant data for one class and frame-variant data for the
other — see MAJOR-1.

**There is a real defence and the paper should make it.** The two frames live on
**one** configuration space with **one** labelling; configuration 12 is
configuration 12 in both. On that reading the identity *is* the canonical
cross-frame co-reference, the disjointness is substantive, and CERT is right.
But then the paper owes an explanation of why name-blindness is a corridor
requirement at all (answer: the declared gauge acts on charts, not across
frames) — and it must say that C4's admitted transport is the **wing exchange**,
i.e. a rule that does not co-refer configurations but permutes them.

The paper currently uses both criteria in one table without choosing.

**Repair.** State the position explicitly in §3.2: on one shared configuration
space the identity is the cross-frame co-reference, name-blindness is a
within-chart gauge condition, and a transport by a non-identity admitted
permutation is a re-identification rather than a co-reference. Then C4's SP-E/F
row can be read correctly by a reader. Alternatively, replace CERT's F-CFG
branch with a transport-relative certificate and report what changes.

---

### MODERATE-2 — `LTP-LAWFUL` is never demonstrated reachable, and the LTP verdict is not gated at all. (K3's explicit Q-OPT test.)

**Severity: MODERATE.** The claim is **true** — I proved it myself — but the
receipt does not carry it, and the protocol demands a mutant.

§7 states: *"`LTP-LAWFUL` is reachable by the gate — it fires whenever a shared
record law conditions on the datum — and is measured never to obtain on this
base. That is a measured negative, not a stipulation."*

Measured facts:

- `shared_record_at_intermediate(sp) = 0` at all six settings, **by
  construction**: at t = 2 the F1 chart has written only `R_A` and the F2 chart
  only `R_B`, and `PARTA ≠ PARTB`. So the `LTP-LAWFUL` branch is unreachable on
  this base for structural reasons.
- **No gate predicate anywhere reads the LTP verdict.** I enumerated all 21
  gates; none does. `run_verdict` consumes `ltp["per_setting"][sp]` but the LTP
  outcome itself is never gated.
- `ltp-lax` dies on **anchors A25/A27** — it also empties the residual vector at
  line 883. It does *not* falsify the selector. A mutant that flipped only the
  LTP branch would survive.

**I discharged the reachability test independently.** Injecting one shared
record partition at SP-E (and changing nothing else) makes the per-setting
verdict read `LTP-LAWFUL (a shared record law conditions on the datum)`. And
`derive_candidate_verdict`, given green F-CFG rows, emits `O4-RULE-EXISTS` under
LTP-LAWFUL and `O4-RULE-EXISTS-LTP-BARE` under LTP-BARE. **The branch is live
and the outcome space is reachable.** The paper's sentence is correct; it is
simply unwitnessed by the artifact.

**The rest of K3 is genuinely satisfied — this is the unit's strongest section.**
LTP-BARE is *computed*, not asserted:

1. the intermediate actuality is exhibited (I reproduced all twelve supports
   from the model);
2. the residual reproduces exactly — `(0,0,16,16,0,16)` in both frames — with
   both value censuses (SP-C: 4 distinct, 0 rational; SP-F: 6 distinct, 8
   rational), rationality decided by the field's own test;
3. the absence of a conditioning law is **derivable by hand** and I derived it:
   the frames' leg orders guarantee that only `R_A` (F1) and only `R_B` (F2)
   have been written by t = 2, and those are different partitions, so the shared
   subalgebra is empty at all six settings;
4. the gate correctly distinguishes `LTP-BARE` (SP-F, residual fires) from
   `LTP-BARE-UNWITNESSED` (SP-E, residual vanishes, subalgebra empty) rather
   than reporting the second as the first.

**Repair.** Add an `ltp-lawful-unreachable` mutant that forces the shared-record
count positive and gates the emitted per-setting verdict set; that converts the
sentence from a structural assertion into a receipt line. One gate, one mutant.

---

### MODERATE-3 — `O4-ARENA-RELATIVE` is not distinct from O4-B.

**Severity: MODERATE.** (My brief asks this directly.)

The pin registers `O4-ARENA-RELATIVE` as *"a sharpened form of O4-B, distinct
from both charter branches."* Measured against paper 0's actual text:

- O4-B already holds that *"unrecorded configurations are variables of the
  nomological representation."*
- A representational variable's values are representation-relative. "Arena" is
  this unit's operational word for the representation's declared coordinates
  (§11.8 says so).
- §10 itself concedes: *"A branch that keeps unrecorded configurations as
  variables of the nomological representation is consistent with that."*

So the outcome is **entailed by O4-B**, not distinct from it. Against O4-A it is
a genuine price statement: *if you keep unrecorded configurations actual, you
must say which arena's actuality you mean.* That is the real content, and the
paper's §10 second bullet gets it right in its final sentence. What is not
earned is co-equal verdict status in the abstract and §9.2, or the pin's
"distinct from both branches."

**Repair.** Report it as a price for O4-A and a measurement of O4-B's own
clause. Withdraw "distinct from both charter branches" (and note the pin's
wording as a deviation, which is the honest route).

---

### MODERATE-4 — The candidate space is slice-bound by construction, so the corridor's central prohibition is not tested by any candidate.

**Severity: MODERATE.**

Every one of the five candidates matches **F1's index-2 datum against F2's
index-2 datum**: `datum_cfg` reads `c.dist(2)` for all of them, and the only
re-indexing anywhere is NOSLICE's, which is *compensated* in the datum itself
(`upto = 3 if extra_identity else 2`). No candidate ever proposes to co-refer
F1's index-2 configuration with F2's index-1 or index-3 configuration.

But in F1 the legs are `(prep, U_A, U_B)` and in F2 `(prep, U_B, U_A)`, so
index 2 names **different events** in the two frames — after A in one, after B
in the other. The candidate generator therefore supplies only rules that
identify moments the model says are not the same moment, while the corridor
forbids exactly that identification. The search space contains no rule that
could succeed, and the reported negative measures the generator as much as the
base.

This is not fatal — the correct diagnosis is *available and is a better
result*: **the committed frame pair has no shared intermediate event**, which
is the relativity-of-simultaneity content the unit is reaching for, and which
also explains MAJOR-1 (nothing descends between division events, records
included) and §7 (the intermediate time is not a division event of the declared
model). But the paper argues from disjointness instead, and never states the
mechanism.

**Repair.** State the mechanism in §6 and §10. Either declare event-aligned
candidates (F1@2 ↔ F2@k for k ≠ 2) and report their measured emptiness, or
record their absence as an explicit scope clause in §11.

---

### MODERATE-5 — D1's *cause* is inferred, not measured. (I confirm the inference; the wording overstates the receipt.)

**Severity: MODERATE**, downgraded because I independently confirmed the
mechanism.

`O4-COMPLETION-DISCLOSURE` says *"The cause is measured and disclosed: W5
rebuilt the model from the singlet dictionary and chose a different orthogonal
completion of `U_prep` off the `j₀` column."* Nothing in the receipt constructs
W5's completion. What is measured is the divergence (288 vs 576) and the
`j₀`-column agreement (A25). The cause is a hypothesis.

**I tested it structurally and it holds.** `U_prep`'s 4×4 `V`-block has columns
`(0,r₂,−r₂,0)`, `(0,r₂,r₂,0)`, `e₀`, `e₃` — two superpositions and two basis
vectors. The residual's differing columns are exactly

> the 18 configurations with `(q_A,q_B) ∈ {(0,0),(0,1)}` — i.e. **the two
> superposition columns of `V` × the 9 pointer combinations** — and the 18 that
> do **not** differ are precisely `V`'s two basis-vector columns × 9.

A completion in which all four `V`-columns are superpositions would give
`16 × 36 = 576`. So D1's diagnosis is mechanistically right, and `288 = 16 × 18`
reproduces exactly on this base.

**But the alternative K5 asks for is live and undiscussed.** W5's own **G4**
reads *"`16 × 36 = 576`: the vector count and the committed matrix count are the
same fact, seen once per column"* — the shape of a **typed product**, not of a
count. That is the failure mode the RUNBOOK appendix records at #24 ("hard-coded
6561 (true 729)"). If W5's 576 was multiplied rather than counted, the
completion story is the wrong explanation of a right observation. The unit does
not weigh this.

**Repair.** Reword to "the cause is diagnosed, and the diagnosis is confirmed
structurally"; add the `V`-column check (it is four lines); name W5's G4 wording
as the untested alternative and route it.

---

### MINOR-1 — The receipt's own header prints a false pairing.

`render()` emits

```
  admitted isomorphisms       2 (of the declared 96, after the base's own j0 filter)
```

pairing `f["admitted_isomorphisms"]` (2 — the `j₀` filter of the **72**-element
base scope) with `SCOPE["n_ext_total"]` (**96** — the extension). The unit's own
anchors say A05: 2 of 72; A06: 8 of 96. The paper's §2 table is correct
(*"2 of the declared 72-element permutation scope (96 with its declared
extension)"*); the receipt is not. A printed number claim that is false, in the
artifact of record.

**Repair.** Print `SCOPE["n_base"]`, or print both filters.

### MINOR-2 — §5 reading 2 understates the negative control.

*"where it admits a transport at all, it fails NAMEBLIND."* Measured: F-CTRL
fails NAMEBLIND under **all five** rules, including C1 and C4 where it admits
none (`name_blindness_of_the_negative_control` is `false` for every candidate).
Not a strengthening — an unnecessary weakening. Tighten it.

### MINOR-3 — TRI/GLUE are SP-A-only but are presented as candidate-level rows.

`triple_descent` fixes `sp = "SP-A"`. The verdict derivation handles this
correctly (verified). §5's table does not tag the columns, inviting the reading
that the triple descends at all six settings. Tag them `[SP-A]`.

---

## 3. Kill-shot coverage

**K1 — THE OBSTRUCTION (lower depth, as assigned).** Occupied sets recomputed
independently from the model; §6 reproduces exactly. I swept **all 66 unordered
pairs** of the twelve charts: 36/36 cross-frame pairs disjoint, 30/30 same-frame
pairs sharing. So disjointness is **not** choice-relative and does not collapse
to `BLOCKED-AT-FRAME-CHOICE` — it tracks the frame coordinate exactly, and my
sweep strengthens the paper's claim beyond the six committed pairs. Two caveats
that the paper must carry: it is **orbit-level** at four of six settings
(MAJOR-3), and it is **not the operative killer** of the transport counts
(MAJOR-2). What it does collapse toward is `BLOCKED-AT-TIME-CHOICE` (MAJOR-1).

**K2 — LIKE-FOR-LIKE (lower depth).** Gate keys and transport signatures are
genuinely identical across the three classes (gate verified, code read). F-REC's
positive control reproduces `|Φ| = 1 × 6` at all six settings against the
paper-2 anchors; 27 anchors trace exit-1 and all pass on rerun. F-CTRL's
failures are teeth, not tautology (it admits transports under C2/C2X/C3 and
still fails NAMEBLIND and CERT). C2X's `BLOCKED-AT-COVAR` is verified — the
level census measures **24** switching failures at the exact level against 0 at
sign and Born. **But like-for-like fails in *content* on two axes the code-path
gate cannot see:** evaluation **time** (MAJOR-1) and name-indexing in the arena
quantities (MAJOR-4). D5's carve-out is legitimate and correctly implemented.

**K3 — THE LTP GATE (primary).** LTP-BARE is **computed, not asserted**, and I
verified every link myself: the intermediate actuality is exhibited (12 supports
recomputed), the residual reproduces exactly `(0,0,16,16,0,16)` in both frames
with both value censuses, and the absence of a conditioning law is derivable by
hand from the frames' leg orders. The SP-E/SP-F distinction (`BARE` vs
`BARE-UNWITNESSED`) is drawn correctly and not conflated. **`LTP-LAWFUL` is
genuinely reachable — I proved it by injection — but no delivered mutant or gate
witnesses it, and no gate reads the LTP verdict at all** (MODERATE-2). The
Q-OPT test is therefore *passed on the merits and failed on the receipt*. The
outcome selector is clean: I emitted both `O4-RULE-EXISTS` and
`O4-RULE-EXISTS-LTP-BARE` from constructed rows.

**K4 — THE ARENA TEST + D3 (lower depth).** `|arena| = 192` recomputed
(6×2×2×8). QA1 orbit 2 / QA2 orbit 1 both reproduce. D3's shrinkage to the
admitted 2 does **not** hollow the orbit claims arithmetically — the acting
group is contained in every candidate's search scope, and a name-free quantity
has orbit 1 under *any* relabelling group, so widening to the 8 could not
rescue QA1′ either. What hollows the orbit claim is the **quantity**, not the
group (MAJOR-4). "Moves under FRAME, not switching" is verified per coordinate:
neither quantity moves under any of the 8 switchings. §15's per-coordinate
discipline is respected in the verdict derivation (verified in code) but
violated in §8's "at every one of the twelve charts" once names are quotiented.

**K5 — INSTRUMENT + D1 (lower depth).** §14 fresh-eval is real (`memo-lax` →
`O4-ST-FRESH`; hits gated 0, misses gated positive). 23 mutants audited via the
kill map: each dies at a gate or anchor that names what it broke; the
never-falsified set is genuinely empty at denominator 17; D6's census exception
is legitimate (`verdict-lax` → `O4-VOCABULARY`, recorded). All reused
W6/W5/paper-2 values pass on rerun. **D1 decided: the 288 is right** — I
recomputed it independently and confirmed the mechanism structurally (the 18
differing columns are exactly `U_prep`'s two superposition `V`-columns × 9
pointers). It is a finding about W5's model build, not a false number here. But
the *cause* is inferred rather than measured, and W5's own G4 wording
(`16 × 36 = 576`) is a live alternative the unit never weighs (MODERATE-5).

---

## 4. On the question the unit was built to answer

Does *"record facts transport, configuration facts do not"* price the charter's
fork as the paper claims?

**Partly, and less than claimed.** What is solidly established, at the committed
finite scope and per coordinate:

- No rule in the declared corridor delivers a certified, unique, covariant
  transport for unrecorded configuration facts at the intermediate time.
- Where a rule admits one at all (C4 at SP-E/SP-F, carried by the base's own
  wing exchange), the actuality it would carry has no committed law attaching —
  forced by W5's lemma at SP-F, unwitnessed-but-equally-bare at SP-E. **This is
  the unit's strongest result and it is fully earned.**
- The two frames' intermediate supports never coincide, at any cross-frame pair
  of the twelve charts.

What is **not** established:

- That the failure is a *class* fact about records versus configurations. Read
  at the same time, the record class fails identically, and the unit's own
  A13/A14 anchors say so (MAJOR-1).
- That the disjointness is the obstruction (MAJOR-2), or that it is
  gauge-robust (MAJOR-3).
- That unrecorded actuality is arena-relative in any sense beyond the frame
  dependence already reported as the obstruction (MAJOR-4, MAJOR-5).
- That leaving the corridor is empty (MAJOR-7).
- That the arena clause is new to the charter (MAJOR-6).

The good news for the programme: **every repair above strengthens the result.**
The time-indexed reading (facts descend at division events and not between
them, records included) is cleaner than the class reading, welds directly to
the LTP finding, and is already anchored. The wing-exchange disclosure makes
SP-E the interesting case rather than an anomaly. The name-free arena quantity
gives a defensible `ARENA-RELATIVE` scoped to four settings. None of this needs
a new fixture.

---

## 5. Grade

Zero false computed numbers; 225 of 225 gate/count cells reproduce; byte-identical
delivery; the LTP section — the pin's fulcrum and this review's primary
assignment — is computed rather than asserted and survives independent
reconstruction end to end. Against that: seven MAJOR findings, all of
interpretation, control design, disclosure and charter fidelity rather than
arithmetic, and all repairable within the existing fixtures and receipts. The
unit verdict's first term survives on a reading the paper does not currently
state; its second term survives only in weakened and rescoped form.

That is not a REJECT — nothing here is unsalvageable and no theorem is false.
It is well short of ACCEPT — the headline as written attributes to a class
distinction a difference the instrument measures as a time distinction, and
half the dual verdict is a naming artifact plus a restatement.

> ## **ACCEPT-WITH-FIXES**

**Fixes required before terminal status,** in priority order:

1. **MAJOR-1** — add the F-REC@intermediate row; restate the discrimination as
   time-indexed, or isolate the class claim at fixed time via Φ_A/Φ_B.
2. **MAJOR-2** — replace §6's and `O4-OBSTRUCTION-NAMED`'s causal claim with the
   per-clause decomposition; state that the disjointness bites *through CERT*.
3. **MAJOR-3** — disclose the wing-exchange orbit at SP-C/D/E/F; name C4's
   transport.
4. **MAJOR-4** — add the name-free arena quantity; restate §8's orbit sentence.
5. **MAJOR-5** — report `O4-ARENA-RELATIVE` as a restatement of the obstruction,
   or drop it from the headline.
6. **MAJOR-6** — quote paper 0 verbatim (or mark the paraphrase); restate §10's
   novelty claim.
7. **MAJOR-7** — add the order-free-only slice candidate; re-derive §10's second
   bullet; declare or gate the order-free stipulation.
8. **MODERATE-1** — take a stated position on identity-bound vs
   up-to-isomorphism co-reference.
9. **MODERATE-2** — add the `LTP-LAWFUL` reachability mutant and gate.
10. **MODERATE-3/4/5, MINOR-1/2/3** — as described above.
