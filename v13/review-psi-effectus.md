# PSI — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens.  **Protocol:**
`v13/note-psi-hostile-protocol.md` (FROZEN, v13 #251), kill-shots
K1–K5 binding.  **Object:** commit 759b12e as-is #241, pin
c12749532eae @ 095c6f7.  **Date:** 2026-08-08.  **No git; no child
agents; this is the only file I wrote.**

## 0. Hash verification of the frozen object

All four verified **before** reading, and re-verified after every
run (no frozen artifact was written to; the delivery-mode writer is
behind `--falsification-selftest`, which I did not invoke in the
repository):

| artifact | sha256-12 | expected | |
|---|---|---|---|
| `v13/paper-psi-curvature.md` | `e79d0ff48933` | `e79d0ff48933` | ✓ |
| `v13/code/psi_curvature_exact.py` | `49b3c980e7d8` | `49b3c980e7d8` | ✓ |
| `v13/code/psi_curvature_output.txt` | `8ea66d096ec8` | `8ea66d096ec8` | ✓ |
| `v13/code/psi_curvature_receipt.json` | `443cf2460dba` | `443cf2460dba` | ✓ |

## 1. Method and recomputation count

Seven scripts of my own in the scratchpad, importing **nothing** from
`psi_curvature_exact.py` except in the one place where I probed the
delivered verdict function directly.  Base G, the Euler–Rodrigues
rotations, the measurement legs, the 162-element scope, the
four-clause admission predicate, the graph, the path enumeration and
the holonomy readings were all **rebuilt from the paper's §2–§5
declarations**, in exact rationals, with my own data structures.

**≈ 1,240 independent recomputations**, plus **8,500** randomised
algebraic trials (cocycle identity and the E=I iff, off-family),
plus a **byte-identical reproduction** of the frozen instrument's
entire non-mutant output (387 lines, 20 gates, 146 anchors — the
only diff is the mutant-table gate, which needs the flag).

*What I did not re-run:* the full 34-mutant table (each mutant is a
~4-minute subprocess; the switching self-test dominates).  I audited
the mutant declarations and the delivered per-gate falsifier table as
data, and probed the verdict gate directly, which is stronger
evidence for F-K5 than any mutant run would be.

**Computed-number errors found in the delivery: ZERO.**  Every
headline number reproduced on my independent route:
18/8 and 18/0 admission cells · links (9,9,9,9,13,13) and
(9,9,9,9,9,9) · 34,024 / 5,864 / 760 and 2,532 / 336 / 48 ·
364 common loops · **206** born-differing and **206**
permutation-differing at psi-N1 · **196** at psi-N2 · **2**
flat→non-flat · the 8 moving cells named (REAL at GP-E/GP-F, all
four checkpoints) · the Klein four-group with fixed-configuration
counts {9,9,45,81} · the 48-member census **26/22/0** · the ψ-law
entry-by-entry at 9×9 and against the direct 81×81 at all 11
members · the E=I ⟺ exchange-invariant coincidence both ways ·
Q-negA order 6 non-abelian, Q-negB order 1 with links refused
(11 links, 52 based loops, 2 permutations admitted at the symmetric
settings).  The §5.3 witness loops came out **character for
character** as printed.

The arithmetic of this unit is clean.  Every finding below is at
the meaning layer, the gate layer, or the cross-unit layer.

---

## 2. K2 — THE CROSS-UNIT TEST: the unification is real, and the
## paper leaves it on the table

This is the protocol's primary weight and it is where the unit's
largest result is sitting unclaimed.

### 2.1 The derivation (mine, then verified)

XBA's adjudicated law (v13 #249) is `D = P·u⁻¹·P·u = [P, u]`.
PSI's §6.1 writes its own defect as
`D(ψ) = P_W·U_prep⁻¹·P_W·U_prep` — **that is already the XBA
commutator, at u = u(ψ) = (H(ψ)·Q) ⊗ I₉.**  The identification
needs one premise, `P_W² = I` (XBA's *unnamed fifth premise*,
involutivity), which holds here because `P_W = Σ ⊗ Σ`.  So the
answer to K2's question is **yes: PSI's law is the commutator law
with ψ restored.  It is one law.**

But the structure is sharper than that, and it is what makes the
split into `D_GEN` and `E(ψ)` exist at all.  Write
`δ(X) := [Σ, X] = Σ X⁻¹ Σ X`.  Then:

- `D_GEN = δ(Q) = [Σ, Q]` — **verified**, entry by entry;
- `E(ψ) = δ(H(ψ)) = [Σ, H(ψ)]` — **verified** at all 11 members;
- `D(ψ) = δ(V) = [Σ, V]`, `V = H(ψ)Q` — **verified** at all 11.

and δ is a **1-cocycle** for the right-conjugation action:

> `δ(XY) = δ(Y) · Y⁻¹ δ(X) Y`

**Verified as a general identity on 300 random orthogonal triples
(0 deviations).**  Instantiating at `(X,Y) = (H(ψ), Q)` gives
**exactly** the paper's ψ-law:

> `δ(H(ψ)Q) = δ(Q) · Q⁻¹ δ(H(ψ)) Q  =  D_GEN · QᵀE(ψ)Q`

So `E(ψ)` is *precisely* the ψ-dependence of the commutator, and
the paper's "theorem" is the standard commutator expansion applied
to the declared factorisation of the completion.  It needs no new
proof; it needs a citation and a name.

**Cross-check with the operator lens: AGREEMENT, from two
independent routes.**  I derived and ran the above before any other
reviewer's result reached me.  R1 (operator lens) independently
reports `D = [P_W, U_prep]` with `E(ψ) = [Σ, H(ψ)]` via the same
commutator expansion written in its mirror form
`[a,xy] = [a,y]·y⁻¹[a,x]y`, at 11/11 members.  That is the identical
identity under a renaming (`[a,bc] = [a,c]·c⁻¹[a,b]c`), reached from
a different instrument and a different starting point, and the two
derivations agree at every member.  I add two things R1's route does
not need to reach: the general-identity check (300 random orthogonal
triples, 0 deviations; the mirror-*ordered* variant false on 200/200,
so the order is forced) and the cocycle/centralizer reading of §2.2,
which is what makes the unification cover COC and GEN as well as XBA.
**No disagreement to report on the ONE-LAW question.**

### 2.2 The unification runs through all four units

Each factor of the cocycle vanishes exactly on a **centralizer** —
which is COC's adjudicated criterion (v13 #234: *closure ⟺ the
chart-generating group centralises the level-1 holonomy*) in the
same variable.  Measured, 0 mismatches:

| condition | ⟺ | unit it belongs to |
|---|---|---|
| `E(ψ) = I` | `H(ψ) ∈ C(Σ)` | **PSI** (this unit's iff) |
| `D_GEN = I` | `Q ∈ C(Σ)` | **GEN** (the equivariant locus = Q-negB) |
| `D(ψ) = I` | `V ∈ C(Σ)` | the joint condition |
| `ord(D)` | dihedral order 2n | **GEN**'s completion-selection |
| `D = [P,u]` | — | **XBA** |

Verified member by member: `E=I ⟺ ΣH=HΣ` at 11/11; and
`D_GEN=I ⟺ ΣQ=QΣ` at the pinned Q and both controls, with Q-negB
the unique centralising one.

**This is the arc's synthesis, and it is derivable in four lines
from objects this unit already computes.**  The paper mentions XBA
nowhere, COC nowhere, and never uses the word "commutator" —
although it writes the commutator twice.

### 2.3 The residual, characterised (K2 asks for it)

The identity does **not** fail.  What fails is *canonicity*, and
this is the honest scope of "E(ψ) is the ψ-dependence":

**The state/declaration split is relative to the declared
factorisation of the completion, not to the completion.**  `D(ψ)`
depends only on `V`.  Refactoring the same `V` as `Q·H′` with
`H′ = QᵀHQ` gives an equally valid cocycle expansion
`δ(QH′) = δ(H′)·H′⁻¹δ(Q)H′` whose state factor is
`E′(ψ) = [Σ,H′]`, and **`E′(ψ) ≠ E(ψ)` at psi-N1** (measured;
they coincide at psi-N2, which is why one example would not have
caught it).  So "the curvature's ψ-part is `E(ψ)`" is a statement
*given the declared completion form* `V = H(ψ)·Q`, exactly as
§10.2 scopes the unit — but §6.1 states the law as if `E(ψ)` were
canonical.

Second residual: **the order in the law is load-bearing and is not
gated as such.**  The mirror-ordered expansion
`δ(XY) = δ(X)·X⁻¹δ(Y)X` is false on **200/200** random triples,
and `D_GEN` fails to commute with `QᵀE(ψ)Q` at psi-N1, psi-N3 and
psi-N4 (measured).  The `defect-order` mutant permutes the four
factors of `D`; it does not test the order of the *law's* two
factors.

**F-K2 (MAJOR, positive — a result withheld, not an error).**
*Repair:* state `D(ψ) = [P_W, u(ψ)]` as the unit's central
identity, cite XBA #249 and COC #234, gate the cocycle identity
`δ(XY) = δ(Y)Y⁻¹δ(X)Y` and the three centralizer equivalences, and
own both residuals (factorisation-relativity; the forced order,
with a mutant that swaps the law's two factors).

---

## 3. K1 — the Born-scoping audit

### 3.1 The census gate asserts something false, and does not
### measure it

`PSI-SIGNFLIP-CENSUS`'s must-pass claim text says:

> "The **BORN SHADOW** is unchanged by a sign pattern, **so no
> Born-level declaration can see the flip.**"

The inference is a non-sequitur and **its conclusion is false**.
The *node law* — `p_i = θ[i,j₀]²` at the node's declared read time
— is Born-level data and is a declared object of the arena (§2.4,
row "law").  I rebuilt all 48 census members and compared each
one's law layer at all 48 nodes **against its own unflipped
member**:

| invariant | law layer unchanged | holonomy agrees | patterns |
|---|---|---|---|
| no | no | no | 16 |
| no | **yes** | no | **10** |
| yes | **no** | yes | **5** |
| yes | yes | yes | 17 |

> **21 of the 48 census sign patterns move the declared node-law
> layer.**  Per member: psi-I1 7/8, psi-I3 2/4, psi-I4 12/16; never
> at psi-G, psi-I2, psi-S1, psi-S2.

The census's own code measures `born_same` and `same_space` and
**never measures the law layer at all** — so the gate carries a
claim its predicate cannot fail on.  (RUNBOOK §13's failure
catalogue, "#36: 22 circular/vacuous gates carried a table".)

This is not cosmetic, because the paper uses "fixed Born shadow" at
**two different strengths**.  §6.2 means "|ψ| fixed" (true of all
48).  §9 justifies the verdict's qualifier by the strong reading —
"at a fixed Born shadow the arena, the admission table, the loop
space **and the law layer** are all measured identical".  **The
census establishes only the weak reading.**  The strong reading is
established for psi-N1 (and psi-N2 against psi-I4) by §8's
flip-test, and nowhere else.  The equivocation is what lets the
48-member census read as if it generalised the witness; it does
not.

**F-K1a (MAJOR).** *Repair:* delete the inference from the gate
claim; replace it with what is measured — the Born shadow of ψ is
unchanged, **hence the admission table and the loop space are
unchanged**, which is all the census needs.  Add a law-layer clause
to the census gate and **print the 21/48**; it is a genuine and
interesting measured fact.  Rescope §6.2's dependence law to the
weak reading and say so; keep the strong reading where it is
earned.

### 3.2 The witness's invisibility has a mechanism, and it is a
### property of the inherited reference

Why *can* ψ_G and ψ_N1 have identical laws at all 48 nodes?  I
measured the **interference width** of the declared leg sequence —
the number of nonzero paths j₀ → i through the first t legs:

| members | max width | consequence |
|---|---|---|
| psi-G, psi-I2, psi-S1, psi-S2, psi-N1, psi-N3 | **1** | every declared amplitude is a **single product**; the declared law is a function of \|ψ\| alone and **cannot** see any sign |
| psi-I1, psi-I3, psi-I4, psi-N2, psi-N4 | 2 | interference; a Born-shadow-preserving flip is generically visible |

and the prediction is exact: the law layer moves under a sign flip
at precisely the width-2 members (psi-I1, psi-I3, psi-I4) and never
at the width-1 ones.  (Width 2 is necessary, not sufficient:
psi-N2's flip is a global sign on the one interfering block, which
is why psi-I4 → psi-N2 stays invisible.)

So: **the fixed-Born-shadow witness exists because ψ_G's support
makes this model interference-free at ψ_G.**  There is no steering
here — ψ_G is *inherited* from GEN, not chosen — but the scope is
much narrower than the prose suggests, and stating the mechanism
costs one paragraph and strengthens the result rather than
weakening it (it says exactly *where* such witnesses live).

**F-K1b (MODERATE).** *Repair:* state the mechanism and the width
table; rewrite "the sign structure carries the curvature" (abstract)
as a statement about the witness's locus, not about sign structure
generally.

### 3.3 Overclaim toward "unobservable structure does physical work"

The paper is *mostly* well scoped: every "invisible" is qualified
by "the model contains" / "Born-level declaration", §10.1 and §10.9
disclaim nature and vocabulary, and §5.2's Born-level identity is
measured rather than argued.  Two places lean past it:

- the receipt's `findings.thesis` opens **"THE PHYSICAL STATE
  CONTRIBUTES GEOMETRY."** as a bare sentence (the scope clause
  arrives 2,000 characters later), and the paper's subtitle asks the
  same unqualified question;
- nowhere does the paper say the obvious defusing fact: **ψ_G and
  ψ_N1 are physically distinct states** (⟨ψ_G|ψ_N1⟩ = 1/9) and are
  perfectly distinguishable by measurements *outside the declared
  six settings*.  The invisibility is relative to the declared
  measurement family and its declared read times, not to quantum
  mechanics.  Without that sentence a reader can take the result as
  "unobservable structure does physical work", which is not what was
  measured.

**F-K1c (MODERATE).** *Repair:* one sentence in §9 and one in §10;
qualify the thesis sentence at its first clause.

---

## 4. K5 — THE VERDICT: #234 noncompliance, decided

The protocol orders me to decide this.  **Decision: NONCOMPLIANT.
Required repair.**

`run_verdict` (lines 2593–2634) derives the *branch* from measured
counts, then:

```python
qual = "-AT-FIXED-BORN-SHADOW"          # a string literal
full = v + qual
inv  = v in PREREGISTERED               # the gate's whole predicate
```

The gate's predicate never looks at `full`, never looks at the
qualifier, and never looks at
`TABLES["flip_tests"]["members_where_the_two_layers_part_company"]`
— the measured set `(psi-N1)` that is the *only* evidence for the
qualifier.  I drove the delivered function directly:

| scenario | printed verdict | gate |
|---|---|---|
| as delivered | `PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW` | PASS |
| **no witness at all** | `PSI-PATH-SPACE-DEPENDENCE-AT-FIXED-BORN-SHADOW` | **PASS** |
| **no movers, no witnesses** | `PSI-DECLARATION-ONLY-AT-FIXED-BORN-SHADOW` | **PASS** |
| **witness only at psi-N2** (not at a fixed Born shadow) | `PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW` | **PASS** |

Rows 2 and 3 are self-contradictory strings in the pin's own
vocabulary and the gate accepts them.  Row 4 is the case that
matters scientifically: the qualifier survives the removal of the
only witness that earns it.

Against the addendum, clause by clause:

- *"derived inside a gate from the measured counts"* — the branch
  is; **the qualifier, which carries the entire scientific strength
  of the result, is a literal.**  This is the **#24 disease at the
  central object**, one unit after the XBA adjudication named it
  ("the hard-coded 'derivation'").
- *"a verdict-flip mutant must prove that derivation can fail"* —
  `verdict-lax` substitutes an out-of-vocabulary token; it does not
  flip the derivation.  The receipt's own per-gate table confirms
  **PSI-VERDICT is falsified by no computation mutant at all**, and
  my probe shows why: no in-vocabulary miscomputation can be caught.
- The paper's §11 excuse — *"a verdict vocabulary can only be
  violated by emitting a bad string"* — restates the defect as its
  justification.

**F-K5 (MAJOR, required repair).** *Repair:* derive `qual` inside
the gate from the measured members-where-the-layers-part-company set
(non-empty **and** intersecting `curv`), gate the full string, and
add a **computation** mutant that empties that set and dies there.
Then PSI-VERDICT leaves the waiver-only list on its own merits.

Related, smaller: `PSI-WITNESS` reports `witness_pairs: 2`, one at
psi-N1 and one at psi-N2 — but psi-N2's Born shadow, completion
shadow, leg keys and **law layer all differ from the reference**
(measured).  Only psi-N1 is a fixed-Born-shadow witness.  §10.3's
"needs one witness and has two" reads as two of the strong kind;
§5.3's two are both at psi-N1, so the paper is defensible, but the
receipt's count and the verdict's qualifier disagree with each
other.  **F-K5b (MINOR).** *Repair:* report the two counts
separately — witnesses (2) and fixed-Born-shadow witnesses (1
member, 206 loops, 2 of them flat→non-flat).

### K5, remaining instrument items (probed at lower depth)

Verified from the frozen artifacts and my byte-identical re-run:
146/146 anchors; 21 gates, 0 disclosures; 34 mutants declared with
kinds; `never_falsified: []`; the cache-refusal mechanism
(8 primed, 8 served on the second visit, 65,544 fresh requests
against 0 hits) is structurally real — the priming makes the
zero-hit gate non-vacuous, which satisfies the #185 and #219
addenda; the AST exemption sweep finds one `MUTANT not in` outside
every call site with the `!=` count gated at zero; the switching
self-test's 66,560 comparisons are complete against a *measured*
link count.  I found no silent drop in the readable/unreadable
handling: the unreadable loops are carried, counted, and compared
by the always-defined Born shadow.

---

## 5. K3 — the family, the comparator, and D7

**Steering.**  Low, and honestly bounded.  ψ_G is inherited, not
chosen.  psi-N1 is a one-sign perturbation of it — the minimal
possible construction.  psi-S1/psi-S2 are genuine in-family
negative controls and they do their job (§5.2's table comes out
both ways).  The 48-member census is the real anti-steering device.
The `[SAMP]` tag is carried at §2.3 and §10.3 and no quantifier
escapes it.

One overclaim: the abstract says the family "is declared as data in
§2 before any transport quantity is evaluated, **and the receipt's
own gate order is gated as the proof**".  Gate order proves
ordering *within one execution*; it cannot prove the family was
fixed before the worker saw any fixture truth.  **F-K3a (MINOR).**
*Repair:* "records it", not "proves it".

**D7 — the comparator choice.**  The choice is correct and I would
have made it: the permutation part is genuinely undefined where the
witness lives, and filtering those loops away would have hidden the
finding.  But the reporting of it is imprecise at a headline number.
I measured, at psi-N1 vs psi-G on the 364 common loops:

- 206 loops differ in the Born shadow;
- **206 of 206 are readability flips** — a signed permutation at
  ψ_G, **not** a signed permutation at ψ_N1;
- **0 loops have two defined permutations that differ.**

So §5.2's column header "**permutation part differs**" describes
nothing that happens: no permutation part differs; 206 of them
cease to exist.  The receipt has the right name for it
(`common_loops_where_readability_flips`), so the instrument knows;
the paper's table does not.  §6.1 and §10.5 own the underlying fact,
which is why this is a labelling defect rather than a
misrepresentation.

And the split *is* gated — the switching self-test measures
0 loops whose readability moves under a switching, so the
readable/unreadable partition is gauge-invariant.  What is missing
is the positive statement it supports, which is stronger and
cleaner than "206 loops differ":

> At ψ_N1 the **readable** holonomy collapses from ψ_G's Klein
> four-group (4 values, fixed-configuration counts {9,9,45,81}) to a
> **group of order 2** — measured closed, values {identity, the wing
> exchange}, counts {81,9} — with **206** of 364 loops leaving the
> readable class entirely.  The same at psi-N2 (2 readable values,
> 196 unreadable).

That is precisely K3's "readable group order 2 with 206 unreadable
loops", it is measured, and it says what ψ does: **it does not
permute the group's elements, it removes the defect from the class
in which GEN's invariant is defined.**  §6.1 says this about the
*defect*; nobody says it about the *holonomy group*.

**F-K3b (MODERATE).** *Repair:* rename the column
("readability flips"), and state the order-4 → order-2 collapse as
a measured result with its own gate.

---

## 6. K4 — the two-phenomena split (D10)

**D10's reading is honest and I endorse it.**  The pre-registered
`PSI-PATH-SPACE-DEPENDENCE` is a *conjunction* — the loop space
moves **and** every common loop's holonomy is ψ-invariant — and the
family refutes the second conjunct at psi-N1.  So it cannot be the
verdict, the first outcome is, and reporting the phenomenon beside
it is the only non-lossy option.  The co-finding carries its own
must-pass gate with both halves in its predicate and its own printed
cell list, so "beside, not folded" is backed rather than asserted.
The real situation is that the pin's outcome vocabulary was written
for a homogeneous family and the delivered family is heterogeneous
(curvature at psi-N1/N2, path-space movement at psi-N3/N4); D10
says as much without quite naming it.

Two precision points:

- The instance is **degenerate**.  At psi-N3/psi-N4 the loop space
  does not get *reshaped*; it **collapses to the flat baseline** the
  four asymmetric settings already have (13 → 9 links, 364 → 8 based
  loops at GP-E, and the 8 moving cells are the entire realized rule
  at GP-E and GP-F).  The pin's gloss — "the state shapes the
  arena's connectivity but not its twists" — suggests a reshaping.
  The honest form is: *the state's Born asymmetry destroys the
  geometry-bearing identifications outright.*  **F-K4a (MINOR).**
- The gate name `PSI-PATH-SPACE-DEPENDENCE` is also a pre-registered
  **verdict token**.  A reader scanning `[PASS]
  PSI-PATH-SPACE-DEPENDENCE` in the receipt can read it as the
  verdict.  **F-K4b (MINOR).** *Repair:* rename the gate
  (`PSI-ARENA-MOVES`).

---

## 7. Further findings

**F-7a (MODERATE) — the negative control is a second reproduction,
not a prediction.**  §7.2 says the pin requires "that the amount be
**predicted rather than observed**", then says "GEN's census
supplies the prediction" — which concedes it was observed.  It was:
GEN §8.4 rebuilt **all 28** single-transposition completions "each a
full rebuild at GP-E and GP-A", delivering 4 flat / 12 Klein / 12
non-abelian-of-order-6.  Both control Q's are transpositions fixing
label 0, hence members of that 28.  The control is still excellent —
it has real teeth, it moves the instrument, and I reproduced all of
it independently (order 6 non-abelian; order 1 with 11 links,
52 based loops and two permutations admitted at the symmetric
settings, exactly D3) — but it is a **reproduction of an inherited
measured value at a moved declaration**, not a prediction risked on
unseen data.  K2 asks me to verify the out-of-sample claim: **it is
not out-of-sample.**  *Repair:* say so; the control loses nothing.

**F-7b (MODERATE) — the central equation is dimensionally
inconsistent.**  §6.1 defines `D_GEN = (ΣQᵀΣQ) ⊗ I₉` (81×81) and
then writes `D(ψ) = D_GEN · QᵀE(ψ)Q` with `QᵀE(ψ)Q` at 9×9.  The
abstract repeats it and so does the receipt's thesis.  The code is
right (`D_gen9` is 9×9 and the tensor is applied to the product), so
this is a paper-notation defect at the unit's headline law — but it
is the headline law, and it appears four times.  *Repair:* carry
`D_GEN` at 9×9 and tensor once, or write
`D(ψ) = (D_GEN⁹ · QᵀE(ψ)Q) ⊗ I₉`.

**F-7c (MINOR) — the census's independence.**  §6.2's 26/22/0 is
heavily determined by §6.1's ψ-law (invariant ⟹ `D = D_GEN`), and I
confirmed the 22/26 split is exactly the invariant/non-invariant
split predicted by counting sign patterns constant on Σ-pairs
(4+4+2+2+4+4+2 = 22).  It is **not** vacuous — the loop holonomies
involve `U_prep` directly, not only `D`, and the six invariant
members with *different* completions all agreeing is a real
measurement — but the paper presents it as settling something the
law did not, and #234's "two independent routes must be independent
computations" is the relevant discipline.  *Repair:* state the
forced part and what remains genuinely measured.

---

## 8. Findings, ranked

| # | sev | finding | repair |
|---|---|---|---|
| F-K5 | **MAJOR** | `-AT-FIXED-BORN-SHADOW` is a hard-coded literal; the gate cannot fail on any in-vocabulary miscomputation; no computation mutant reaches PSI-VERDICT. **#234 noncompliant — decided.** Demonstrated: the qualifier survives removing every witness. | derive the qualifier in-gate from the measured layers-part-company set; add a computation verdict-flip mutant |
| F-K1a | **MAJOR** | `PSI-SIGNFLIP-CENSUS`'s claim "no Born-level declaration can see the flip" is an unmeasured non-sequitur and is **false at 21 of 48** census patterns; the paper equivocates between the weak and strong readings of "fixed Born shadow" | delete the inference, measure and print 21/48, rescope §6.2 |
| F-K2 | **MAJOR (positive)** | the XBA/COC/GEN unification is derivable in four lines from objects already computed and is entirely absent; `D(ψ)=[P_W,u(ψ)]`, `δ=[Σ,·]` a 1-cocycle, all three vanishing conditions centralizer conditions. Residuals: the split is factorisation-relative (`E′≠E` at psi-N1); the order is forced and ungated | state and gate the identity; cite #249 and #234; own both residuals |
| F-K1b | MOD | the witness's Born-invisibility is carried by ψ_G's **interference width 1**, unstated; "the sign structure carries the curvature" over-generalises a width-1 fact | state the mechanism + the width table |
| F-K3b | MOD | §5.2's "permutation part differs" (206) is a readability-flip count — 0 loops have two defined differing permutations; the real result (readable group order 4 → order 2) is unstated | rename the column; state and gate the collapse |
| F-K1c | MOD | no sentence says ψ_G and ψ_N1 are physically distinct and distinguishable outside the declared settings; the receipt thesis opens unqualified | one sentence each in §9/§10; qualify the thesis |
| F-7a | MOD | "predicted rather than observed" — both control Q's lie in GEN §8.4's exhaustively rebuilt 28 | call it a second reproduction |
| F-7b | MOD | the central equation mixes 81×81 and 9×9 (abstract, §6.1 ×2, thesis) | fix the notation |
| F-7c | MIN | the census's outcome is largely forced by the ψ-law | state the forced part |
| F-K5b | MIN | `witness_pairs: 2` includes psi-N2, which is not at a fixed Born shadow | report the two counts separately |
| F-K3a | MIN | gate order "gated as the proof" of the freeze proves in-run ordering only | "records", not "proves" |
| F-K4a | MIN | the path-space instance is a **collapse to the flat baseline**, not a reshaping | say so |
| F-K4b | MIN | the gate name duplicates a pre-registered verdict token | rename |

Nothing in this list touches a computed number.  I attempted to
refute the 206, the 196, the 2, the 26/22/0, the 48-cell tables, the
loop counts, the Klein four-group, the ψ-law and both controls on a
fully independent rebuild, and **every one of them survived**.

---

## 9. Grade

The measurement is sound and the finding is real: at psi-N1 every
Born-level object this model builds — the Born shadow of ψ, the
Born shadow of the completion entry by entry, the Born-level key of
every declared and realized leg, the law at all 48 nodes, the
48-cell admission table, the whole loop space — is **measured**
identical to the reference, and 206 of 364 common loops carry
different holonomy, 2 of them flat at one preparation and not at the
other.  I reproduced all of it independently and found no
computed-number error anywhere in the unit.

But the unit has to be sent back for three things.  Its **verdict
string is half typed** — the qualifier that carries the entire
scientific claim is a literal that survives the removal of every
witness, in a unit delivered *after* the #234 addendum was written
to forbid exactly this.  Its **census gate asserts a falsehood** —
21 of its 48 members move a declared Born-level datum, and the gate
neither measures it nor could fail on it, which is what lets the
weak and strong readings of "fixed Born shadow" pass for one
another.  And it **misses its own biggest result**: the law it
presents as a generalisation of GEN is XBA's commutator law with ψ
restored, its two factors are values of a single 1-cocycle, and all
three units' vanishing conditions are the same centralizer
condition — one law, four readings, four lines away.

`ACCEPT-WITH-FIXES` — the arithmetic is clean and the witness
stands; F-K5, F-K1a and F-K2 are mandatory before terminal.

**Grade: ACCEPT-WITH-FIXES.**
