# NT — HOSTILE REVIEW R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator-system / algebraic lens.
**Date:** 2026-08-07.
**Object under review (SHA-256, first 12, all VERIFIED before reading):**

| artifact | claimed | measured | |
|---|---|---|---|
| `v13/paper-nt-nomological-transport.md` | `730679a896de` | `730679a896de` | ok |
| `v13/code/nt_transport_exact.py` | `76fb081b124f` | `76fb081b124f` | ok |
| `v13/code/nt_transport_output.txt` | `e0dca9e00d34` | `e0dca9e00d34` | ok |
| `v13/code/nt_transport_receipt.json` | `b0f6482be448` | `b0f6482be448` | ok |

**Method.** I built my own instrument in
`/private/tmp/.../scratchpad/r1_{base,holo,gauge2,t1t3,paths,vs,scope,mut,k4,k2,fin}.py`.
It imports **only** the committed base (`v12/paper1_code/model_composite.py`,
`v12/code/w6_coreference_exact.py`). Every NT-specific object — the
admissibility predicate, the prefix profile, the graph, the path enumerator,
the three transport actions, the pair table, the loop probes, the switching
sweep, the holonomy group — is written from scratch here. The delivered
script was never executed to obtain any number in this review; it was read,
and its receipt was read, only to identify the claims to attack.

**Recomputation count.** **254 distinct claimed quantities** independently
recomputed, resting on **4,972,096** path-pair classifications rebuilt from my
own enumeration and **101,120** exact matrix comparisons in the sweeps
(81,920 in a complete 8192-element switching sweep the delivery did not run;
19,200 in the mutant-conjunct isolation).

---

## 0. What reproduces exactly

Stated first, because most of it does, and the findings below must be read
against it. Every one of these is my number, computed independently, agreeing
with the delivered number to the unit:

- **Arena.** Declared scope 72 / extension 96 / admitted 2 / admitted
  extension 8; NLEGS = 3; checkpoints {0,1,2,3}; 8 nodes; `L_max` = 8. The
  admitted group is exactly {identity, wing exchange} — a two-element decision
  at every admissibility call.
- **The 26 identification links**, row for row: FULL admits uniquely at
  t ∈ {0,1,3} at all six settings and **nothing** at t = 2; REAL admits
  uniquely at all four checkpoints at SP-E and SP-F and **nothing** at
  SP-A–SP-D. Multiplicities are exactly 1 wherever a link is drawn.
- **PREFIX-DECIDES.** Prefix profile 18/18 agreement with transport, residual
  profile 12/18, six equal-residual / opposite-transport witnesses — all
  reproduced, and all matching the committed O4 receipt's
  `read_time_structure` verbatim.
- **Path space.** 9 / 13 links, 3 / 7 identification links, cycle rank 2 / 6,
  **34,024** reduced paths, **4,972,096** pairs sharing both endpoints. Closed
  counts 56 / 2,820 reconcile with my 64 / 2,828 exactly: the delivered count
  excludes the 8 length-0 paths (`and p["len"]`). No discrepancy.
- **All 12 cells of the matched pair table**, to the unit (681,660 / 1,025,340
  / 1,276,120 / 1,988,976 / 1,478,644 / 228,356 / 2,769,932 / 495,164 /
  434,744 / 1,272,256 / 917,412 / 2,347,684), and **0 obstructed sides** for
  all three objects.
- **Distinct transported values: T1 = 223, T2 = 5, T3 = 186.**
- **Generated holonomy group order 4** at SP-E/SP-F, 1 elsewhere.
- **Controls.** Canonical loop = the identity at all six settings, and equal on
  the nose to Θ_F2(3←0)⁻¹ Θ_F1(3←0); legs commute 9/9 (A14). Negative control
  not even a signed permutation at SP-A–SP-D, a further permutation with sign
  orbit {−1,+1} at SP-E/SP-F.
- **Direction flip-test: 8/8** on the eight headline witnesses (reverse
  traversal returns the inverse permutation).
- **Posability weld 48/48**; defect weights 0 / 288 with j₀-column 16.
- **Census.** 21 mutants, all exit 1; kind split **17 computation / 4 waiver**
  counted from the declaration; must-pass denominator **13** (the 14th is
  `NT-FALSIFICATION` itself, correctly excluded and correctly disclosed);
  `never_falsified` **EMPTY**. Fresh-eval instance count **6,400** — my
  independent replay of the declared sweep produces exactly 6,400 instances
  (10 swept loops × (512 + 128)).

---

## K1 — THE REFUTATION WITNESSES

### K1.1 All eight witnesses reproduce, and the bigons are genuinely closed

I rebuilt each bigon as an edge list and *walked the node sequence*, asserting
at every step that the traversal's tail equals the current node:

```
SP-E/SP-F, t ∈ {0,1,3}:  F1@t -> F2@t -> F1@t      closed = True
```

Both ends are certified in the declared (FORCED) sense and I verified the
certification rather than accepting it: at each of the six coordinates the
FULL rule admits **exactly one** element of the admitted scope (the identity)
and the REAL rule admits **exactly one** (the wing exchange). Holonomy =
the wing exchange at all six; it equals `P_REAL · P_FULL⁻¹` on the nose; it
squares to the identity. **Six witnesses confirmed.**

The two flat crossings likewise: `F1@1 -> F1@2 -> F2@2 -> F2@1 -> F1@1`,
closed, holonomy exactly the identity at SP-E and SP-F. **Eight for eight.**

### K1.2 Is the wing-exchange holonomy gauge content or a gauge orbit? — content, but the sweep that says so cannot fail

It is content: the permutation part is invariant. But the sweep the pin made
mandatory establishes that *vacuously*. See **K3.3 (M2)** — the finding is
algebraic and belongs there.

One consequence worth stating here: the bigon is a **two-link** loop of
signed-permutation link variables. Under the declared switching group its
matrix is ε_a ε_b · P_W. There is no switching that could have moved its
permutation part. The L5 sweep, applied to the six headline witnesses, is
therefore incapable of returning anything but "invariant".

### K1.3 Is the flat crossing forced by construction? — yes, and the paper's presentation of it overreaches (M5)

Forced, and I verified the forcing directly: at SP-E and SP-F the two
settings' angles coincide, and I measure `P_W · L₂^{F2} · P_W == L₂^{F1}`
exactly. The declared probe is `P_W (L₂^{F2})⁻¹ P_W L₂^{F1}`, which is
therefore the identity by that one identity. The paper says so in §6, and
that is honest.

What the paper does not say is that **the crossing checkpoint is not flat**.
I built every minimal loop through the same prefix-divergent t = 2 link that
the same instrument can build:

| loop through the t=2 crossing | SP-E | SP-F |
|---|---|---|
| t1↔t2 closed by **REAL** at t=1 (*the declared probe*) | the identity | the identity |
| t1↔t2 closed by **FULL** at t=1 | **the wing exchange** | **the wing exchange** |
| t2↔t3 closed by **REAL** at t=3 | the identity | the identity |
| t2↔t3 closed by **FULL** at t=3 | **a further permutation** | **not a signed permutation** |

The existential refutation survives untouched — a flat crossing exists. But
§5 reading 3 ("*the* loop through the divergent checkpoint t = 2 is measured
flat") and the §5 table row read as a statement about the crossing, and they
are false as such. The paper's own pair table already contains 1,988,976
disagreeing crossing pairs for T1 and 2,347,684 for T3; the counter-loops
above are the named witnesses of that column, and they are not reported.

### K1.4 The two refutations are one mechanism

Both witness classes exist only at SP-E and SP-F, and both rest on the *same*
algebraic fact: at equal angles the wing exchange intertwines the two frames'
second legs. That is what lets the REAL rule admit W (creating the twisted
corridor) and what makes `P_W L₂^{F2} P_W = L₂^{F1}` (making the declared
crossing flat). "Refuted twice" (abstract, §6) is one mechanism read at two
coordinates, not two independent falsifiers. Not an error — the pre-registered
hypothesis is dead either way — but the rhetorical doubling should go.

---

## K3 — THE HOLONOMY COMPUTATIONS

### K3.1 T1: 223 values reproduce; the claimed cause is verified by construction; the *characterization* is measured false (M6)

**223 confirmed.** The claimed cause — "the transposed Born step fails to
invert the forward one" — I verified by construction rather than by
inference. For each of the 36 (setting, frame, leg) triples I computed
`B(L)ᵀB(L)`:

- **28 of 36 legs fail to invert.** `B(L)ᵀB(L) = I` iff `B(L)` is a
  permutation matrix; U_prep's Born shadow carries ½ entries, so it never is.
- All 36 Born shadows are exactly doubly stochastic, which is why neither
  direction ever obstructs (consistent with the measured 0 obstructed sides).

The cause claim stands. **The characterization built on it does not.** §8.1
states: "the law's restriction transports flatly along the law's own forward
steps and is path-dependent as soon as a reverse step is taken". I measure the
forward one-step Born push against the node's own law at all 36 cells:

```
forward push == the node's own law at every cell?  FALSE
failing cells: (SP-C,F1,3) (SP-C,F2,3) (SP-D,F1,3) (SP-D,F2,3) (SP-F,F1,3) (SP-F,F2,3)
```

Six of thirty-six — exactly the three settings whose composition defect is
nonzero. At SP-C, SP-D and SP-F the forward step is *already* not the law's
own evolution, so the sentence is false there and the causal story ("that is
why the canonical loop does not return T1: the Born-level step is
irreversible") is incomplete at half the settings. The **verdict**
`NT-HOLONOMY-⟨T1⟩` is untouched and if anything strengthened.

### K3.2 T3: the value set is 4, not 3 — a wrong number in a headline table, with a false mechanism attached (M1, MAJOR)

§8.2 states, for SP-E and SP-F: "**3** — the identity, **the wing exchange**,
and *one* further permutation | **order 4**, computed by closure", and §8.2 /
D5 explain the 3-vs-4 gap as non-closure of the value set at the length bound.

I enumerate every closed path based at F1@t0 in the committed path space and
extract the permutation part:

| | delivered | measured (R1) |
|---|---|---|
| SP-E value set | 3 | **4** |
| SP-F value set | 3 | **4** |
| generated group order | 4 | 4 |
| value set already closed under composition | (implied no) | **yes** |
| holonomies dropped as non-signed-permutations | (unreported) | 0 |

The four elements, with their multiplicities over the 365 closed paths at
F1@t0 (identical at both settings):

| element | count | sign orbit |
|---|---|---|
| pointer-only swap (pa↔pb) | 106 | {−1,+1} |
| qubit-only swap (qa↔qb) | 90 | {−1,+1} |
| the wing exchange | 86 | {+1} |
| the identity | 83 | {+1} |

W = (pointer swap)∘(qubit swap); the group is the Klein four-group.

**Root cause, and it is not arithmetic.** `run_verdicts` builds the value set
as a set of **name strings**:
`els.add(PERM_NAME.get(canon(...), "another permutation"))`, and `PERM_NAME`
has exactly two entries. Every unnamed permutation collapses onto the single
label `"another permutation"`. `value_set_size = len(els)` is therefore a
count of *labels*, not of *values*, while `gen = {tuple(p) …}` (used for the
group) correctly counts values. **The receipt convicts itself**: for SP-E and
SP-F it prints `group_elements` with **four** entries of which **two** are
literally `"another permutation"`, alongside `value_set_size: 3`.

This matters beyond the digit. The paper *explains* the 3 ≠ 4 gap with a real
mathematical mechanism (a value set not closed at the length bound) that does
not obtain here — the set is closed, and 4 = 4. A bug is being narrated as
structure. This is the failure class the RUNBOOK appendix exists for ("counts
computed, never typed" — here the count is computed, but of the wrong object).

**Also unreported:** two of the four group elements — the pointer-only swap
and the qubit-only swap — are **not in the declared 72-element permutation
scope, nor in its 96-element extension** (I checked membership directly; both
fix j₀). The holonomy group *leaves the base's admitted isomorphism group*.
That is the most interesting structural fact I found in this unit and the
paper does not state it. §8.3's summary — "a two-element wing-exchange
holonomy at the two symmetric settings" — understates §8.2's own order-4
result.

**Is the group that of gauge-fixed content or of raw values?** Gauge-fixed:
signs are stripped before the closure. That part of the protocol question is
answered in the paper's favour.

### K3.3 The §14 sweep cannot fail on the clause it advertises (M2, MAJOR)

The declared switching group assigns one sign per link, and
`link_variable_switched` implements it as `W6.sp_neg(K, A)` — **scalar**
multiplication of the link variable. Therefore, for any closed loop,

> H_switched = ( ∏_{traversed edges} ε_li ) · H — a global scalar.

The permutation part of a signed-permutation holonomy is invariant under
multiplication by ±1. **So the declared invariant is invariant identically**,
for every loop, every setting, every switching, whether or not anything about
the model is right.

I verified this rather than merely arguing it, and in doing so answered the
**D2 [SAMP] attack** at full strength. The delivery swept a 512-stride sample
of the 8,192 at SP-E/SP-F. **I swept the complete 8,192**, for all five
declared loops at both settings — including the bigons at t = 1 and t = 3,
which the delivered sweep never touches at all:

```
SP-E/SP-F, each of {bigon@t0, bigon@t1, bigon@t3, crossing t1<->t2, canonical}
  swept ALL 8192 : distinct permutation parts = 1
                   distinct sign orbits       = 2
                   deviations from (prod eps)*H0 = 0     (81,920 exact comparisons)
```

**D2 is answered: there is no hidden switching-variance in the unswept
7,680 elements, and there cannot be.** But the same fact guts the gate.

I then isolated which conjunct of `NT-GAUGE-COVARIANCE` each killer mutant
actually breaks, by re-implementing the mutations in my own instrument
(the gate is a five-way conjunction and a kill does not say which conjunct
fell; `inv_fail` conflates "the permutation part moved" with "the holonomy is
not a signed permutation at all"):

| mode | instances | not a signed perm | **perm part MOVED** | checkpoint-sign clause failures |
|---|---|---|---|---|
| baseline | 6,400 | 0 | **0** | 0 |
| `gauge-sign` | 6,400 | 0 | **0** | 10 |
| `orient-flip` | 6,400 | 4,480 | 7 (artifact of the 4,480) | 7 |

`gauge-sign` — the sign/orientation perturbation §14 specifically demands —
moves the permutation part at **0 of 10** swept loops; its kill comes entirely
from the checkpoint-subgroup sign clause. `orient-flip`'s apparent movement is
an artifact: 4,480 of 6,400 holonomies stop being signed permutations, so the
surviving `perms` set is sampled, not moved.

**No mutant, and no group element, tests the invariance claim.** §7's
"the sweep is built so that a wrong invariant would show" is not supported.

The second clause is forced too: the checkpoint switching is
`sw[li] = sn[a]·sn[b]`, and a **closed** walk visits each node an even number
of times, so ∏sw ≡ +1 identically. And `NT-GAUGE-CONTROL-MOVES` ("the raw
sign moves") is satisfied by any single-link sign flip. All three clauses of
the §14 apparatus are theorems of the construction.

This is precisely the RUNBOOK §14 lesson, restated: *a mutant that replaces
the quantity wholesale does not test that the RIGHT invariant is computed.*
The gate does retain one piece of genuine content — that each declared loop's
holonomy **is** a signed permutation at all, which for the 8-link canonical
loop of non-permutation matrices is a real fact — but that is not what it
claims to measure.

### K3.4 The gauge split discards invariant content (M3)

Under s → εs, the *relative* signs of a signed permutation are invariant;
only the overall factor is gauge. The paper reports
`sorted(set(sgn.values()))`, which is not a clean invariant — for a
uniform-sign loop it flips between [1] and [−1] — and which discards the
relative structure entirely. Concretely, **two of the four measured holonomy
elements carry mixed signs** (orbit {−1,+1}): that mixture is gauge-invariant
content, and it is neither reported nor gated. §7's "The declared invariant is
the closed loop's permutation part; its overall sign is the gauge orbit" is
incomplete on its own data.

### K3.5 T2: the weld is a tautology, and it is not new (m7)

I confirm Δᴮ = Γ(N←0) − Γ(N←t)Γ(t←0) at **48/48** nodes. But this is implied
by the gate's own clause 2. Both are `msub(X, born(U₂)·born(U₁))`; the
subtrahend is literally the same expression, and the minuends are
`born(U₂·U₁)` and `born(Θ(N←0))`, which clause 2 *already gates equal*. Same
subtrahend, gated-equal minuend ⇒ identity. It cannot fail while clause 2
passes.

Nor is it a new cross-corpus fact. W5's committed M4 says it in as many
words: *"This is what makes the declared residual D_210 EQUAL to the
Born-shadow defect Delta^B(Theta(3<-2), Theta(2<-0)) of [p0]'s T2' on this
model — the two objects are distinct in general and coincide here."* §4.1
clause 3 presents "Paper 1's composition defect and W5's divisibility residual
are **one object** on this base, not two" as a discovery of this unit, with no
citation of W5 M4.

---

## K2 — THE MECHANISM (verified against the full table, not the 8 witnesses)

The claim: "holonomy appears exactly where the base admits two certified
identifications at one coordinate". Multiplicity ≥ 2 occurs at exactly
SP-E/SP-F × t ∈ {0,1,3} (FULL identity + REAL wing exchange) — I confirm, and
I confirm it occurs nowhere else.

Aligned-corridor **disagreeing** pairs, per setting, from my own enumeration:

| setting | T1 | T2 | T3 |
|---|---|---|---|
| SP-A | **460** | 0 | 0 |
| SP-B | **460** | 0 | 0 |
| SP-C | **672** | 0 | 0 |
| SP-D | **672** | 0 | 0 |
| SP-E | 449,700 | 0 | 636,128 |
| SP-F | 573,376 | 228,356 | 636,128 |

**"There and only there" holds for T3 and for T2 — and fails for T1.** T1
disagrees inside aligned corridors at all four settings where *no* second
identification exists; that disagreement is Born-level irreversibility, not
identification multiplicity. §8.1 knows this ("at every setting including the
four where the frames' geometry is trivial"); §6's mechanism paragraph states
it unrestrictedly and is contradicted by the unit's own T1 column (M4). The
fix is one clause: scope the mechanism to the geometric layer.

T2's cell is confirmed sharp: the defect moves under wing conjugation at
SP-C/SP-D/SP-F (t = 1,2), but the wing exchange is an admitted identification
only at SP-E/SP-F, and at SP-E the defect is identically zero — so SP-F alone
survives both conditions. Exactly as §5 reading 5 states.

**D3.** The demotion from CERT to FORCED does not undermine "certified
identifications": at every drawn link I measure the admitted set to be a
singleton, which is what FORCED means, and the alternative reading's
consequence (links only at t = 3, loop space empty) is disclosed with its
measured effect in §8.4 and D3. I find the disclosure honest and complete.

---

## K4 — PREFIX-DECIDES RE-DERIVATION (lower depth)

The reproduction is exact: 18/18, 12/18, six witnesses, all three profiles
cell by cell against the committed O4 receipt.

The **independence** claim is weaker than stated (m8). `W6.leg_match(K,X,Y,"born")`
reduces to `sp_born(X) == sp_born(Y)` — an *equivalence relation*. O4 asks
"does some permutation match the two leg lists under that equivalence"; NT
asks "are the two multisets of equivalence keys equal". Those are the **same
predicate**, provably, and I confirm they agree at 18/18 cells and continue to
agree at 18/18 under a deliberate one-leg perturbation. So the prefix leg is a
different *algorithm* for one predicate — it would catch a bug in the
permutation search, not a defect in the predicate. The transport-profile leg
(NT's own four-clause admissibility predicate versus O4's matched-table
machinery) is genuinely independent, and it carries the 18/18. §2's wording
describes what was done accurately; the abstract's "re-derived here
independently" is what over-reads it.

---

## K5 — INSTRUMENT (lower depth)

- **D1.** Scoping the positive control to the amplitude layer is legitimate
  and the contrast is stated as a contrast, not reconciled away. I verify the
  canonical loop equals Θ_F2(3←0)⁻¹Θ_F1(3←0) exactly at all six settings and
  that the legs commute 9/9. T1's non-return is a genuine finding and is
  reported as one. I note only that the positive control is nearly as forced
  as the negative control has teeth — given A14 it could not have come out
  otherwise — so its discriminating power is small; the negative control is
  carrying the instrument.
- **D8.** The waiver-direction fix is sound. All four waivers exit 1 and each
  falsifies its own named gate; the paper's disclaimer (a waiver measures that
  the predicate carries the exit code, not that the gate catches a
  computational defect) is exactly right and is the honest reading.
- **Census.** `never_falsified` EMPTY at denominator 13 confirmed; the exempt
  gate is `NT-FALSIFICATION` itself, correctly excluded and disclosed. 17/4
  split confirmed from the declarations. Caveat: gate coverage counts
  conjunctions, and §K3.3 shows one gate's advertised conjunct has coverage
  zero — the census cannot see this, and that is a limitation of the census,
  not a violation of it.
- **Path-space counts** 9/13, rank 2/6, 34,024, 4,972,096 — all confirmed.
- **Fresh-eval** 6,400 misses / 0 hits — the instance count reproduces exactly
  in my independent replay of the declared sweep. Coverage caveat (m9): the
  sweep takes **one loop per role**, so four of the six headline bigons are
  never swept. Harmless in fact — I swept all four under the complete 8,192
  with no variance — but it should be stated.
- **Anchors.** 22, exit-1-only; I independently reproduced A01–A07 against the
  committed O4 receipt, A14 (9/9), A17 (72,2,96,8), A18 (3), A19/A20
  (0,0,16,16,0,16) and A21 (0,0,288,288,0,288).
- **m10.** The based-holonomy enumeration silently drops closed paths whose
  holonomy is not a signed permutation (`if p is None: continue`). On this base
  it fires **0 times** at every setting — I checked — so nothing is lost, but
  it is an undisclosed selection that would bite elsewhere; the count should be
  printed.
- **m11.** D2's [SAMP] is harmless and I have discharged it exhaustively. It
  can simply be retired: either run the complete 8,192 (~8 minutes) or cite
  the scalar-action argument that makes any sample sufficient.

---

## Findings, ranked

| # | sev | finding | repair that would satisfy me |
|---|---|---|---|
| **M1** | **major** | §8.2 value set is **4, not 3** at SP-E/SP-F (two further permutations, not one); the value set **is** closed at the bound, so D5's non-closure explanation of the 3-vs-4 gap is a **false mechanism**. Cause: `value_set_size` counts *label* strings from a 2-entry `PERM_NAME`; the receipt's own `group_elements` prints four entries with two duplicated names. | Count distinct permutation tuples. Restate §8.2: value set 4, already the whole group. Delete/rewrite D5's non-closure story. Name the two elements. |
| **M2** | **major** | The mandatory §14 sweep **cannot fail** on its advertised clause: switching acts by a global scalar, so the permutation part is invariant identically (0 deviations from (∏ε)·H₀ over the complete 8,192 × 5 loops × 2 settings). Mutant isolation: `gauge-sign` moves the permutation part at **0/10** loops. §7's "a wrong invariant would show" is unsupported. | Either declare a switching group that acts non-scalarly (e.g. per-node conjugation by admitted permutations), or restate the gate as what it measures — "the holonomy is a signed permutation; its overall sign is pure gauge" — and drop the claim that the invariance is a measurement. |
| **M3** | **major** | The gauge split discards invariant content: relative signs are invariant under s→εs and are neither reported nor gated; two of the four measured holonomy elements carry mixed signs. `sorted(set(sgn))` is not itself a clean invariant. | Report the relative-sign class (e.g. s_j·s_0) as invariant content alongside the permutation part; correct §7's sentence. |
| **M4** | moderate | §6's mechanism ("holonomy exactly where two certified identifications meet") is contradicted by the unit's own T1 column: 460/460/672/672 aligned-corridor disagreements at SP-A–SP-D, where no second identification exists. Holds for T3 and T2 only. | Scope the mechanism claim to the geometric layer; cite §8.1's own layer contrast at the point of statement. |
| **M5** | moderate | The flat crossing is presented with an unearned definite article. Same t=2 crossing closed by FULL at t=1 gives **the wing exchange**; closed at t=3 gives a further permutation (SP-E) / not a signed permutation (SP-F). | State the flat crossing existentially and publish the counter-loops; the refutation is unaffected. |
| **M6** | moderate | §8.1's "transports flatly along the law's own forward steps" is **false at 6 of 36 cells** (SP-C/SP-D/SP-F, leg 3, both frames): the forward Born push does not reproduce the node's own law. The causal story is incomplete at three of six settings. | Correct the sentence; report the 6 cells; note the verdict is unaffected. |
| m7 | minor | The §4.1 weld is implied by clause 2 (same subtrahend, gated-equal minuend), and W5's committed M4 already states the identity. | Cite W5 M4; state it as an implication, not a discovery. |
| m8 | minor | K4 independence is algorithmic only: `leg_match(·,·,"born")` is an equivalence, so permutation-search ≡ multiset-key equality as predicates. | Say "a different algorithm for the same predicate, plus a genuinely independent transport predicate". |
| m9 | minor | §14 sweeps one loop per role; four of six headline bigons never swept. | State the coverage; or sweep all declared loops (I did — no variance). |
| m10 | minor | Non-signed-permutation closed-path holonomies silently dropped from the value set (fires 0× here). | Print the dropped count. |
| m11 | minor | D2 [SAMP] is discharged: complete 8,192 sweep shows no hidden variance. | Retire the deviation or cite the scalar-action argument. |
| m12 | minor | Two of the four holonomy-group elements lie **outside** the declared 72-element scope and its 96-element extension — unreported, and arguably the unit's most interesting structural fact. §8.3's "two-element wing-exchange holonomy" understates §8.2's order-4 group. | State it. |

**Not found.** No fatal defect. No verdict overturned: the eight refutation
witnesses are real, `NT-PREFIX-FLATNESS-REFUTED` stands on both witness
classes, and `NT-HOLONOMY-⟨T1⟩ / ⟨T2⟩ / ⟨T3⟩` all stand on pair tables I
reproduced to the unit. No fabricated count: every headline number except the
value set reproduces exactly. No float, no tolerance, no coordinate
conflation — the read-time coordinate is genuinely carried in the datum and I
could not construct a comparison across checkpoints. The declared-arena
discipline (§15) is met.

---

## Grade

The unit's science survives my attack. Eight of eight refutation witnesses are
genuine, closed, and certified at both ends; 34,024 paths, 4,972,096 pairs,
all twelve pair-table cells, 223 / 5 / 186, the group order 4, the census, the
controls and the flip-tests all reproduce independently and exactly. The D2
sampling worry is not merely unfounded — I discharged it exhaustively.

But one headline table carries a wrong computed number (M1), and worse, the
paper narrates that error as a mathematical mechanism that does not obtain.
And the pin's mandatory §14 clause — the one the L5 disease made compulsory —
is satisfied by a gate that no switching and no mutant could ever fail (M2),
while the split it declares throws away invariant content (M3). Those are
repairable at the level of text plus a two-line change to how the value set is
counted; none of them moves a verdict. Three further claims (M4, M5, M6)
overstate what was measured and are contradicted by the unit's own data.

**ACCEPT-WITH-FIXES.**

Binding for acceptance: M1 (recount the value set and delete the false
non-closure explanation), M2 (restate or re-arm the §14 gate — it must not
continue to claim that its invariance is measured), M3 (report the relative
signs or scope the split honestly), and the three scoping corrections M4, M5,
M6. The minors should ship in the same pass; m12 in particular deserves
promotion into the text rather than a footnote.
