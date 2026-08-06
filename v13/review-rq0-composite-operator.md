# R1 — OPERATOR-LENS HOSTILE REVIEW (Cycle B′)

**Reviewer:** R1, operator lens, H1 primary (kill-shots K1 and K2).
**Protocol:** `v13/note-rq0-composite-hostile-protocol.md` (frozen, 612b149).
Judged against that protocol only. No cross-reading of R2 or R3.
**Object, hashes re-verified at review time (all four match the freeze):**

| file | sha256 prefix | pinned | match |
|---|---|---|---|
| `v13/paper-rq0-composite-boundaries.md` | `fc94524d6ef2` | `fc94524d6ef2` | yes |
| `v13/code/rq0_l1_composite_exact.py` | `52809c240345` | `52809c240345` | yes |
| `v13/code/rq0_l1_composite_output.txt` | `cb520b01c1df` | `cb520b01c1df` | yes |
| `v13/code/rq0_l1_composite_receipt.json` | `73dbdc4a1d5f` | `73dbdc4a1d5f` | yes |

**Method.** Own exact code in a private scratchpad, `fractions.Fraction`
throughout, nothing imported from the unit and nothing imported from the
Cycle B module. Every fixture, every declared task, the manufactured Givens
construction, the admitted-split computation and the local-split computation
were rebuilt from their stated definitions. The admitted-split partition was
computed by a deliberately different route from the unit's (annihilator of the
effect system, then nullspace of its action on the atom coordinates, where the
unit reduces atom indicators modulo an effect-system basis), so agreement is
evidence and not a shared bug.

---

## VERDICT

```
ACCEPT-WITH-FIXES
```

Every H1 number in the paper reproduced exactly under an independent
implementation: 30/30 lemma pairs, 65/65 sweep pairs with gap zero, 10/10
hostile-wing composites, all eight rows of the Theorem 4.2 table including
every Schmidt-rank multiset and every product-projection flag, and every
anchor I could reach. **I found no false computed number anywhere in H1.**
The three registered rungs survive at their declared scopes.

The fixes are four, and one of them is MAJOR. It does not overturn
`RQ0-L1-ENTANGLEMENT-WITNESS` at its declared `[DECL-8]` scope — I verified
with an exact separability decision that the unit's classification is *correct
on all eight declared tasks* — but the witness is presented in language that
reads as a general instrument, and as a general instrument it returns a false
negative on a task the paper's own recipe can build at the paper's own
committed dimension. That must be scoped explicitly, and the decisive row's
key word must be either measured or withdrawn.

---

## Per-rung confirmations required by the protocol

**(a) The factorization/support-space lemma and its carrier-≤20 +
lemma-carried scope — CONFIRMED, and strengthened.**
Lemma 3.1 is true as stated and I re-proved it independently (below). It holds
by exact subspace intersection on all 30 fixture pairs of composite carrier
dimension ≤ 9. The conclusion holds on all 65 ordered pairs of carrier ≤ 20
with the gap zero and no exception. **I additionally tested the excluded
pairs directly at carrier 25** — the protocol asked for at least one; I ran
six, including both manufactured×manufactured cases and the largest pair C5×C5 — and every one
distributes exactly. The lemma-carried scope is sound. See K1 below; the proof
as written, however, has a stated gap.

**(b) The corrected witness (gap = joint readability; gap + exact atom
classification = entanglement), including the parity refutation of the naive
form — CONFIRMED AT `[DECL-8]`, WITH A MAJOR SCOPE FIX.**
The parity refutation is real and I confirm it independently: PARITY opens the
gap (core 2 vs product core 1) and its rank-two atoms are genuinely separable
— which I *measured* by exact partial transpose (PPT ⟺ separable in 2⊗2) and
by exhibiting `P = |00⟩⟨00| + |11⟩⟨11|` as a sum of two orthogonal product
projections. The naive pre-registered form is correctly refuted. But see K2:
the classification's negative verdict is a default, not a measurement, and the
paper's decisive word "separable" is nowhere computed by the unit.

**(c) The discriminator both ways at the declared arena — CONFIRMED against
the receipt (not re-derived; H2 is R2/R3's primary).**
All H2 counts the paper states reproduce from the receipt exactly: records
15/5/52, one certified record per manufactured context, 51/52 for the eraser,
the six carrying isomorphisms with the cyclic shift among them, the atom map
(4,0,1,2,3) with four of five address projections moved, the carrier of size
one with the candidate absent, 160 families, 120 sector maps with exactly one
reversible and 52 records fixed, and the 51→1 withdrawal under the coarser
context. No drift between prose and receipt on any of them.

**(d) The top-of-lattice guard escape — CONFIRMED at the receipt level.**
`top_certified: False` on all three constructed manufactured contexts;
`candidate_present: False` with `carrier_size: 1`. The argument in Theorem 6.2
is valid as written (extensivity gives ⊤ in every closure's fixed-point set;
the certified set omits it; hence distinct). Not my primary lens.

**(e) The measured limits honestly framed — CONFIRMED, with one wording
defect.** Both limits are in the verdict and both narrow the rung. But §6.4's
boldface sentence and §7.6's control are in tension; see finding M3.

**(f) The verdict rungs as the correct pre-registered instantiations —
CONFIRMED.** The deviations appendix is present and complete (ten items, each
substantive). Deviations 1, 2, 3 and 9 are exactly the ones a hostile reader
would demand, and they are declared rather than buried. The paper is
single-threaded: it records a pre-registration-versus-measurement deviation,
which the #121 rule requires, and catalogues no correction rounds.

---

## K1 — THE LEMMA'S REACH (primary)

### K1.1 The lemma is true; I re-proved it independently

For subspaces V, X ⊆ A and W, Y ⊆ B of finite-dimensional spaces,
(V⊗W) ∩ (X⊗Y) = (V∩X) ⊗ (W∩Y).

The paper's proof via minimal-length representations is correct. My
independent route: identify A⊗B with matrices; for t ∈ A⊗B, t ∈ U⊗U′ iff the
column space of t lies in U and the row space lies in U′. Membership in the
left side then reads (col ⊆ V and row ⊆ W) and (col ⊆ X and row ⊆ Y), i.e.
col ⊆ V∩X and row ⊆ W∩Y, which is membership in the right side. **The lemma
carries no gap.** Confirmed numerically on all 30 pairs at carrier ≤ 9 and on
five pairs at carrier 25 (the sixth, C5×C5, had its distribution verified but
its 625-dimensional lemma intersection was still running at freeze).

### K1.2 The passage from the lemma to Theorem 3.2 has a real gap

Theorem 3.2's proof concludes: *"so every admitted composite split is a
combination of products of admitted local splits, and the projections among
them are exactly the unions of products of local core blocks."* Two defects.

**(i) Only one containment is argued.** The lemma gives ⊆. The reverse — that
every local split still cuts the composite, so that Core(A⊗B) *refines*
Core(A)⊗Core(B) — needs P⊗1 ∈ E_A⊗E_B, i.e. **1_B ∈ E_B and 1_A ∈ E_A**.
Unitality of the effect systems is used and never stated. All nine fixtures
are unital, so nothing computed is affected, but the proof as printed does not
close.

**(ii) The word "exactly" is false without a hypothesis the paper never
states.** Let A be the diagonal algebra on four atoms and let
E = span{(1,1,1,1), (1,1,0,0), (1,0,1,0)} — self-adjoint, unital, dimension 3.
Its projections are exactly {0, (1,1,0,0), (1,0,1,0), (0,0,1,1), (0,1,0,1),
(1,1,1,1)}, and they generate the **discrete** partition; yet the atom
(1,0,0,0) is not in E. So "the projections among them are exactly the unions
of products of local core blocks" fails: the core blocks are the singletons
and their indicators are not admitted splits at all. The missing hypothesis is
precisely the one the **unit checks and the paper omits** — that each core
block indicator lies in E (the `ok`/`cok` flag inside
`admitted_split_partition`, folded into gate H1-03 via `fact_ok`). Under that
hypothesis both containments close and the sentence becomes true. I confirmed
the hypothesis holds on all 9 fixtures, all 65 swept pairs and all six
excluded pairs I ran, so **no computed number is affected**; this is a
statement-of-theorem repair, not a numerical one.

### K1.3 The direct excluded-pair test (protocol requirement) — PASSES

The 16 excluded ordered pairs are exactly the pairs among the four
carrier-5 fixtures {C5, M4+C, MAN211, MAN22}, all at composite carrier 25.
I tested six directly, at full exactness, including the lemma itself in
dimension 625 on the first five (C5×C5 distributes; its 625-dimensional lemma
intersection was still running at freeze and is not claimed):

| excluded pair | carrier | core A | core B | core A⊗B | product core | distributes | lemma |
|---|---|---|---|---|---|---|---|
| MAN22 × MAN22 | 25 | 3 | 3 | 9 | 9 | yes | holds |
| MAN211 × MAN22 | 25 | 4 | 3 | 12 | 12 | yes | holds |
| C5 × M4+C | 25 | 5 | 2 | 10 | 10 | yes | holds |
| MAN211 × MAN211 | 25 | 4 | 4 | 16 | 16 | yes | holds |
| M4+C × MAN22 | 25 | 2 | 3 | 6 | 6 | yes | holds |
| C5 × C5 | 25 | 5 | 5 | 25 | 25 | yes | — |

Block indicators verified admitted in every case. **The lemma-carried scope is
not merely licensed, it is now partly discharged by measurement.** Deviation 9
is honest, and the cap at 20 is more conservative than it needs to be — the
carrier-25 pairs are reachable; the authors may wish to raise the cap and
retire the deviation, but nothing forces it.

### K1.4 The generation claim — the proof uses a reading the prose does not fix

The protocol asks whether "the joint class GENERATED by the locals" is what
the proof actually uses. **It is not, on the natural reading.** Definition 2.1
says *"The admitted joint operations are those generated by the local ones;
the composite effect system is the algebraic span E_A⊗E_B"*, and gate H1-03's
own claim text repeats "the joint class GENERATED by them". The unit computes
the **linear span of simple tensors** (`span = [mkron(a,b) for a in bA.span
for b in bB.span]`). Lemma 3.1 applies to that and only to that. The natural
reading of "generated" — closure under composition, i.e. the ∗-algebra
generated — gives a strictly larger object and a different core:

| composite | dim(linear span) | core | dim(algebra generated) | core |
|---|---|---|---|---|
| HOSTILE ⊗ C2 | 6 | 2 | 16 | 4 |
| HOSTILE ⊗ M2 | 12 | 1 | 32 | 2 |
| HOSTILE alone | 3 | 1 | 8 | 2 |

The distribution law happens to survive both readings when applied
consistently to factors and composite, so no result is wrong. But the hostile
wing's *trivial core* — the object §3.1's control exists to protect — is
itself an artifact of the linear-span reading, and the word "generated" is the
only word in the declaration that decides it. One sentence fixes this.

**K1 adjudication: the lemma survives; the theorem's proof needs two stated
hypotheses (unitality, block-indicator admissibility) and the declaration needs
"generated" disambiguated. No number moves.**

---

## K2 — THE CORRECTED WITNESS'S OWN SOUNDNESS (primary)

### K2.1 The declared family reproduces exactly, and the classification is
### correct on it

I rebuilt all eight declared tasks and recomputed every column. All 8 rows
match the receipt exactly — atom ranks, core, both local cores, product core,
gap, Schmidt-rank multisets, product-projection flags, `has_entangled_atom`.
I then added the decision the unit never makes: **exact separability by
partial transpose with a PSD test over all principal minors**, which in 2⊗2 is
complete (PPT ⟺ separable). On the declared eight, the unit's verdict and the
true verdict agree in every case. The rung stands at `[DECL-8]`.

### K2.2 The decisive row's decisive word is not measured

Theorem 4.3 turns on: *"the classically correlated parity task has **separable**
rank-two atoms and opens the gap."* The unit never computes separability. What
it computes is

```
srs = [schmidt_rank_of_rank_one(p,2,2) if mrank(p)==1 else None for p in projs]
entangled_atom = any(s is not None and s > 1 for s in srs)
```

so for PARITY, whose atoms are rank two, `srs = [None, None]` and
`has_entangled_atom = False` **by default** — it would be False for any task
with no rank-one atom whatsoever. Worse, the one higher-rank classification
the unit does run reports PARITY's atoms as **not** product projections
(`atoms_are_product_projections: [False, False]`, which I reproduce). So the
unit's own output does not support the word "separable"; that word is supplied
by the author. It is *true* — I verified it two ways — but it is asserted, and
it is the load-bearing step of the theorem that corrects the pre-registered
outcome.

### K2.3 THE KILL: a false negative at the committed dimension

Take the admitted joint task with measure {P, I−P} where

- P = |00⟩⟨00| + |Ψ⁺⟩⟨Ψ⁺|, Ψ⁺ = (|01⟩+|10⟩)/√2
- I−P = |11⟩⟨11| + |Ψ⁻⟩⟨Ψ⁻|

This is a rational PVM on the paper's own two-factor carrier of dimension
four, and its boundary is built by the paper's own recipe (the range of the
matched dephasing). Exact results from my code:

| quantity | value |
|---|---|
| atom ranks | (2, 2) |
| product directions in each atom's range | **1** (exactly one, by the exact discriminant of the binary det form) |
| det(partial transpose) of each atom | **−1/16** |
| partial transpose PSD | **False** — both atoms are **entangled** |
| Core(A⊗B) | 2 |
| local A / local B / product core | 1 / 1 / 1 |
| gap opens | **yes** |
| unit's `has_entangled_atom` | **False** |

So the corrected witness — "the gap together with the exact atom
classification" — reports *joint-readable but not entangled* on a task whose
composite-core atoms are both entangled. **A false negative, inside the
declared dimension, inside the declared construction.**

Non-claim 8 ("no claim that the atom classification decides entanglement
beyond rank-one atoms") blunts this but does not cover it, because Theorem 4.3
and the §8 verdict state the witness without any hypothesis on the *task*'s
rank profile — only on the classification. The witness as a rule needs the
antecedent "on tasks all of whose composite-core atoms are rank one", or it
needs the two-line separability test.

### K2.4 The defect is exactly localizable — and I bound it

I ran the rank-profile census at the committed dimension. The false negative
requires a task with no rank-one entangled atom but some entangled atom.

- **(1,1,1,1)** — every atom rank one, classification exact. Impossible.
- **(1,1,2) with both rank-one atoms product** — impossible. Proof: if
  |a⟩|b⟩ ⊥ |c⟩|d⟩ in C²⊗C² then ⟨a|c⟩=0 or ⟨b|d⟩=0. If ⟨a|c⟩=0 the orthogonal
  complement is span{|a⟩|b^⊥⟩, |c⟩|d^⊥⟩}; if ⟨b|d⟩=0 it is
  span{|a^⊥⟩|b⟩, |c^⊥⟩|d⟩}. Either way it is spanned by two orthogonal product
  vectors, hence separable. Confirmed on 114 orthogonal product pairs, zero
  entangled remainders.
- **(1,3)** — impossible. For rank-one |φ⟩ in 2⊗2 the partial transpose of
  |φ⟩⟨φ| has spectrum {cos²θ, sin²θ, ±cosθ sinθ} ⊆ [−1/2, 1], so
  PT(I−|φ⟩⟨φ|) ⪰ 0 and the rank-three atom is always separable. Confirmed on
  four representatives including Φ⁺ and Ψ⁻ (this is why SYMANTI's rank-three
  atom is correctly unflagged).
- **(2,2)** — **the only profile that admits it**, and it does.

So the gap in the instrument is one rank profile wide, and the declared family
contains exactly two (2,2) tasks (PARITY, LOCALZ) — both of which happen to be
separable. The paper got the right answer on its family by the draw, not by
measurement. **The repair is small:** run the exact PPT test on every atom of
rank ≥ 2 (I did; it is ~15 lines of exact rational arithmetic and completes
instantly), and the classification becomes exact on all of 2⊗2 rather than on
rank-one atoms only.

### K2.5 A second adversarial task, favourable to the paper

To be fair to the corrected reading, I also built a task where **every atom is
a rank-one product projection and the gap still opens**:
{|1⟩⟨1|⊗|0⟩⟨0|, |1⟩⟨1|⊗|1⟩⟨1|, |0⟩⟨0|⊗|+⟩⟨+|, |0⟩⟨0|⊗|−⟩⟨−|}. Core 4, local A
2, local B 1, product core 2, gap **opens**, zero entanglement anywhere. This
independently corroborates Theorem 4.3's corrected reading and is a stronger
witness for it than PARITY, because in the declared family every gap-opening
task has at least one non-product atom, so a reader can wrongly infer that
non-product atoms track the gap. My task refutes that too. I recommend the
authors adopt it (or one like it) as a second row.

**K2 adjudication: the corrected witness is sound on the declared family and I
certify that independently; as a general instrument it is unsound in exactly
one rank profile, demonstrated by explicit construction. The rung survives at
`[DECL-8]`; the framing must be scoped and the decisive word measured.**

---

## Findings, ranked

**MAJOR-1 — the corrected witness returns a false negative on rank-(2,2)
tasks, and the decisive row's "separable" is never measured.**
K2.2–K2.4. `has_entangled_atom` is a default-False for any task without
rank-one atoms; Theorem 4.3's claim that PARITY's atoms are separable is true
but supplied by the author, and the unit's only higher-rank classifier reports
those same atoms as non-product. An explicit admitted PVM at the committed
dimension (K2.3) makes the default fire wrongly. Does **not** overturn the
rung at `[DECL-8]` — I certified the eight declared rows independently — but
the witness must not be stated without a rank hypothesis, and the PARITY row
should carry a measurement. Fix: add the exact PPT test for atoms of rank ≥ 2,
or add the antecedent "all composite-core atoms of rank one" to Theorem 4.3
and §8.

**MODERATE-2 — Theorem 3.2's proof is one-sided and its "exactly" clause needs
an unstated hypothesis.** K1.2. Unitality of the effect systems is used
silently for the refinement direction; the "exactly" clause is false without
the block-indicator-admissibility condition, which the unit checks (`cok`) and
the paper never states. Explicit counterexample supplied. No number moves.

**MODERATE-3 — "the joint class GENERATED by the local ones" names a closure
the unit does not compute.** K1.4. The unit uses the linear span of simple
tensors, which is what Lemma 3.1 requires; the ∗-algebra reading gives
dim 6 → 16 on HOSTILE⊗C2 and a core of 4 rather than 2. The hostile wing's
trivial core exists only under the span reading. Appears in Definition 2.1 and
in gate H1-03's own claim text.

**MODERATE-4 — §6.4's headline sentence is contradicted by §7.6's own
control.** §6.4 asserts "The manufactured record fails for exactly the feature
that manufactured it," then glosses that feature as the rotated basis. §7.6
then reports that the same manufacturing construction with the rotation
deleted **descends**, and concludes that descent "does not certify 'not chosen
to match a measure'". Both cannot stand: if aligned manufacture descends, the
feature the record fails for (rotation) is precisely *not* the feature that
manufactured it (choosing a measure to match). §7.6 is the honest one; §6.4
must be rewritten to name rotation rather than manufacture.

**LOW-5 — the abstract reverts to count language for the flagship gap.**
"the gap is four against one" sits against Definition 2.2's insistence that
the gap "is their inequality, not a difference of two counts", which
Deviation 2 emphasises further. Harmless but self-undercutting.

**LOW-6 — "independent routes" oversells the lemma verification.** §3's
"computed on both sides by independent routes" means one construction per side
of the identity, both finishing in row reduction. Accurate on a charitable
reading, loose on a hostile one.

**LOW-7 — vocabulary hygiene.** The forbidden-vocabulary sweep is clean: all
hits (lines 111–112, 204, 686–692) are negations in the scope box, the
no-smuggling gate row, or the non-claims, which the protocol permits. The word
"local" appears eight times in the non-forbidden factor-index sense ("local
admitted operations", "local unitaries", "local cores"); it is always glossed
nearby as "readable on one factor alone", so it passes, but it is the one word
in the paper a hostile outside reader will misread first.

**No finding of an arena-independent selector claim.** I looked. §8 disclaims
it explicitly, §6 carries `[ARENA]` throughout, and the "next obstruction"
paragraph names the residual relativity honestly.

---

## Numbers table — claimed vs. mine

All recomputed independently in exact rational arithmetic unless marked
"(receipt)".

| # | quantity | paper / receipt | R1 | agree |
|---|---|---|---|---|
| 1 | lemma pairs, carrier ≤ 9 | 30, lemma holds | 30, holds | yes |
| 2 | product-law sweep pairs, carrier ≤ 20 | 65 | 65 | yes |
| 3 | sweep pairs with nonzero gap | 0 | 0 | yes |
| 4 | ordered pairs excluded by the cap | 16 of 81 | 16 of 81 | yes |
| 5 | excluded pairs tested directly at carrier 25 | 0 (carried) | **6 of 16, all distribute exactly** | — (new) |
| 6 | hostile-wing composites | 10, none promoted | 10, none promoted | yes |
| 7 | dim(E ∩ Z) for the hostile system | 1 | 1 | yes |
| 8 | hostile core / HOSTILE⊗C2 core | 1 / 2 | 1 / 2 | yes |
| 9 | rank J(identity channel) | 1 | 1 | yes |
| 10 | ⟨ψ⁻\|J(P)\|ψ⁻⟩ | −1/2 | −1/2 | yes |
| 11 | Bell four: orthogonal projections summing to I | yes | yes | yes |
| 12 | Bell Schmidt ranks / marginals | 2,2,2,2 / max mixed | 2,2,2,2 / max mixed | yes |
| 13 | BELL row: core, locA, locB, product | 4, 1, 1, 1 | 4, 1, 1, 1 | yes |
| 14 | PROD row: core, locA, locB, product | 4, 2, 2, 4 | 4, 2, 2, 4 | yes |
| 15 | PRODROT row (rotated control) | 4, 2, 2, 4, gap no | 4, 2, 2, 4, gap no | yes |
| 16 | PARITY row | ranks (2,2), core 2, product 1, gap yes | same | yes |
| 17 | SYMANTI row | ranks (3,1), SR (—,2), gap yes | same | yes |
| 18 | LOCALZ row | ranks (2,2), core 2, locA 2, product 2, gap no | same | yes |
| 19 | all eight SR multisets | see Thm 4.2 | identical, 8/8 | yes |
| 20 | all eight product-projection flags | see receipt | identical, 8/8 | yes |
| 21 | MAN211 / MAN22 centre dims | 4 / 3 | 4 / 3 | yes |
| 22 | MAN211 / MAN22 rank multisets | (2,1,1) / (2,2) | (2,1,1) / (2,2) | yes |
| 23 | gates / anchors / mutants | 25 / 31 / 9 | 25 / 31 / 9 (receipt) | yes |
| 24 | float literals in the unit | none (AST sweep) | **0**, own AST scan; no math/numpy/random import | yes |
| 25 | manufactured records: 15 / 5 / 52, one certified each | as stated | matches receipt | yes |
| 26 | eraser certified / total; coarser withdrawal | 51/52; 51→1 | matches receipt | yes |
| 27 | carrying isomorphisms; atom map; overlap moved | 6; (4,0,1,2,3); 4 of 5 | matches receipt | yes |
| 28 | PARITY atoms separable | asserted in prose | **True** (exact PPT; also = sum of two orthogonal product projections) | claim true, unmeasured by unit |
| 29 | ADV-ENT2 atoms separable | not run | **False**, det(PT) = −1/16 | new — the K2 kill |

**No claimed number was found wrong.** Item 28 is a true claim the unit does
not compute; item 29 is outside the paper's family and is the finding.

---

## Sentences to rewrite

1. **§3, Theorem 3.2, proof.** Replace *"so every admitted composite split is
   a combination of products of admitted local splits, and the projections
   among them are exactly the unions of products of local core blocks"* with a
   two-directional statement carrying its hypotheses, e.g.: *"…so every
   admitted composite split is a combination of products of admitted local
   splits. Conversely, since each effect system contains the unit, P⊗1 and
   1⊗Q are admitted whenever P and Q are, so the composite cut refines the
   product cut. Under the standing condition — verified on every pair — that
   each core block indicator is itself an admitted split, the two cuts
   coincide and the projections among them are exactly the unions of products
   of local core blocks."*

2. **§2, Definition 2.1, product law.** Replace *"The admitted joint
   operations are those generated by the local ones; the composite effect
   system is the algebraic span E_A⊗E_B"* with *"…the composite effect system
   is the linear span of the simple tensors E_A⊗E_B (not the ∗-algebra they
   generate, which is a different and strictly larger declaration)."* Mirror
   the change in gate H1-03's claim text.

3. **§4, Theorem 4.3.** Replace *"the classically correlated parity task has
   separable rank-two atoms and opens the gap"* with either a measured form —
   *"…has rank-two atoms that are separable, each being the sum of two
   orthogonal product projections (verified exactly), and opens the gap"* — or
   the PPT form once the test is added.

4. **§4, Theorem 4.3 and §8, the witness rung.** Add the missing antecedent:
   the entanglement witness is the gap together with the atom classification
   **on tasks whose composite-core atoms are rank one** — or, better, add the
   rank-≥2 separability test and state the witness without restriction. As
   printed, the rule admits a false negative at rank profile (2,2).

5. **§9, non-claims.** Non-claim 8 should say what the default actually is:
   *"…and 'no entangled atom' records the absence of a rank-one entangled
   atom, not a measurement of separability; a task with no rank-one atom is
   reported unentangled by construction."*

6. **§6.4.** Replace *"The manufactured record fails for exactly the feature
   that manufactured it"* with a claim §7.6 supports, e.g. *"The manufactured
   record fails for the rotation, not for the manufacture: §7.6 shows the same
   construction with the rotation deleted descends."*

7. **Abstract.** *"the gap is four against one"* → a partition-level phrasing,
   for consistency with Definition 2.2 and Deviation 2.

8. **§3 (optional).** *"computed on both sides by independent routes"* →
   *"each side computed by its own construction and compared by dimension and
   containment"*.

---

## Scope of this review

I re-derived H1 in full and treated H2 as a numbers-and-prose cross-check
against the receipt, since the arena, the guard and the independence gate are
R2's and R3's primaries. Within H1 I attempted all four kill-shots; K3 and K4
findings that fall to me are recorded as MODERATE-4 and in the vocabulary
sweep. I ran no child agents, mutated no git state, imported nothing from the
unit, and wrote exactly this one file in the repository.

**FROZEN ON DELIVERY.**
