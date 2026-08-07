# R2 — EFFECTUS / ORDER-LENS HOSTILE REVIEW

## RQ0-L5 branch A, *The Provenance Quintuple* — K3 primary (the LOSSY constructions and the scissors) + the reduction's order-theoretic side

**Lens:** R2 (effectus).  **Protocol:** `v13/note-rq0-provenance-hostile-protocol.md`
(commit `0e1ff17`), frozen before dispatch.  **Object:**
`v13/paper-rq0-provenance-quintuple.md` + `v13/code/rq0_l5_provenance_exact.py`
+ `_output.txt` + `_receipt.json` at commit `6ee172c`.  **Pin:** `ce18eac` +
amendment v2 (`a05e3d5`).  **Antecedent checked against:** v12 W7 / paper 1's
recorded-but-phased limit.

**Discipline observed.** All arithmetic exact (`Fraction` + integer phase
exponents in **Z**/8); no float anywhere; `/opt/homebrew/bin/python3.13`;
nothing imported from the unit — every object rebuilt from the definitions
quoted in the paper and in the predecessor sources; no child agents; no git
mutations; repo read-only apart from this one file.  **50 independent
recomputations** are recorded below (protocol minimum: 10).  Freeze-on-delivery
observed: this file is final on delivery.

---

## 1. VERDICT

> ### `REJECT` — of the delivered artifact, **not** of its headline.
>
> The registered outcome box survives and is re-derivable on repaired grounds.
> The classical layer (Sections 1, 2, 4, 5.1–5.3, 6.1, 6.2, 7.1) reproduces
> **exactly**: 23 of the 24 paper quantities I recomputed blind came out
> identical, and several come out *stronger* than stated.
>
> The amplitude layer does not survive.  **The object the unit calls "the
> gauge-invariant loop holonomy" is gauge-VARIANT** — it moves under 384 of the
> 512 vertex switchings of the unit's own committed one-step diagram, by the
> unit's own Definition 3.1 criterion.  Consequently **Proposition 5.4 is
> false** ("exactly 4 values, 128 lifts each"; the truth is **one** value,
> ζ₈⁴, on all 512, and it is *forced by unitarity*), and **Theorem 6.3's
> exhibited witness is invalid on its own terms** (its two "indistinguishable"
> words are separated by checkpoint-local data the shadow function omits — one
> writes the address chart, the other the forged 2+1+1).
>
> A false numerical proposition about a constructed object is the one thing
> this campaign's ledger has never carried.  It must not be recorded as
> terminal in this state.  The repair is fully computed here (§6): the kills
> still fire, by better mechanisms, and Theorem 6.3 has a valid corrected
> witness which I exhibit.

The verdict is `REJECT` rather than `ACCEPT-WITH-FIXES` because the required
changes are not editorial: one proposition inverts, one theorem's witness is
replaced, one central constructed object must be recomputed, and the code must
be re-run — §§3.3(partly), 5.4, 6.3, 6.4, 7.2–7.4, the delta table, the abstract
and the §8 REGRESS bullet all move.

---

## 2. FINDINGS, RANKED

### F1 — DECISIVE. The carried "gauge-invariant content" is gauge-variant. `[AMP]`

`cycle_basis_holonomies` builds each fundamental cycle as

```
legs = [(e, +1)] + [(ee, -ss) for ee, ss in reversed(tree_path(e[0], e[1]))]
```

and `tree_path` has already stored each step as `(e, -s)`.  The two negations
cancel.  The return leg of every fundamental cycle is therefore traversed with
the **outbound** direction instead of the reversed one, so the accumulated
product is

  w(e) · hol(tree path)   in place of   w(e) · hol(tree path)⁻¹,

i.e. a product along a walk that **does not close**.  My own implementation
asserts closure at every leg (`assert v == e[0], "cycle does not close"`); the
unit's construction fails that assertion by design.

*Measured.* Applying the paper's own gauge — vertex switching, Definition 3.1 —
to the committed one-step diagram over all 512 switchings of the three free
vertex phases: **the unit's quantity moves in 384 cases; a correctly closed
loop moves in 0** (`N18` / `N18b`).  Non-claim 5 of the paper says "Carrying
gauge-variant per-edge phases would smuggle; only closed-loop holonomies are
carried."  The measurement says the carried object *is* the smuggled one.

*Closed form.* For one block 2^(−1/2)[[ζᵃ,ζᵇ],[ζᶜ,ζᵈ]] the unit computes
`d + b − a + c`; unitarity forces `d = c − a + b + 4`, so the unit's value is
`2(b + c − a) + 4`, which sweeps {0,2,4,6} with multiplicity 128 each — exactly
the receipt's `L5-AMP-FREE` value, reproduced to the last count.  The correctly
closed loop is `a − b + d − c = 4`, identically.

*The sharpest form.* Vertex switching by a phase at each vertex is exactly
conjugation by diagonal phase matrices, D₂ U D₁†, so it preserves unitarity and
keeps a switched lift inside the declared family.  Measured on the gauge orbit
of the committed Hadamard lift: **all 4,096 switchings land back inside the
admitted 512-element family**, and on that **single orbit** the unit's quantity
takes all four values (0),(2),(4),(6) while the closed-loop holonomy takes the
one value (4).  In other words, **Proposition 5.4's "4 classes with 128 lifts
each" is the gauge orbit itself, relabelled as invariant content** — 512 lifts
= 128 gauge classes × 4 orbit-internal phase labels, and the unit is reading
the labels.

*Blast radius.* The defect is confined to this unit's file: the pattern
`for ee, ss in reversed(p)` occurs nowhere else in `v13/code/` or `v12/`, and
v12's `paper1_code/sec6_signature.py` uses an unrelated vertex-list
construction that closes its loop explicitly (`cycle_vector(path + [u], …)`).
No contagion into v12 paper 1 is indicated.  (I did not audit v12 paper 1;
out of scope.)

### F2 — Proposition 5.4 is false, and inverts. `[AMP]`

Paper: "the carried gauge-invariant holonomy takes exactly **4** values …
with **128 lifts realizing each**", whence "the amplitude datum is one further
**free declaration**."

Recomputed: over the same complete 512-element admitted unitary lift family the
closed-loop holonomy takes **exactly one value, ζ₈⁴, with all 512 realizing
it** (`N22`).  And this is not an artifact of the declared ζ₈ family: for **any**
2×2 unitary [[α,β],[γ,δ]] with all entries non-zero, row orthogonality gives
αγ̄ = −βδ̄, hence αδ/(βγ) = −|α/β|², a negative real.  **The one-step loop
holonomy of a full-support unitary block is rigidly −1.**

The inversion matters for the argument, not for the verdict.  The paper's
mechanism is "the datum is free, so the adversary matches it."  The truth is
"the datum is a **constant forced by unitarity**, so it discriminates nothing."
Both defeat Gain 2; they are opposite mechanisms, and only one of them is true.

*The repair is stronger than what it replaces.*  REGRESS at the amplitude scope
does not need the lift count at all.  Deviation 4 already concedes that the
amplitude scope's **law is the support-level composition closure** — a
support-level object that places **no constraint whatever** on carried
amplitudes.  Every gauge-invariant amplitude datum not already forced by
unitarity is therefore free by construction, with no counting required.  That
is the sentence §5.4 should have.

### F3 — Theorem 6.3's exhibited witness is invalid on its own terms. `[AMP]`

The unit's witness (recomputed exactly, `N25`–`N26`: lifts (0,0,0,4),(0,0,1,5)
against (0,0,0,4),(0,1,0,5); global "holonomies" (0,4,6) vs (1,4,5); per-step
(4) and (6)) fails twice over:

1. **Its per-step shadow is unattainable.**  A per-step holonomy of ζ₈⁶ cannot
   occur: F2 shows every admitted unitary lift has per-step holonomy ζ₈⁴.  The
   reported `[[4],[6]]` is an artifact of F1.  Under a closed loop the same two
   lifts give `[[4],[4]]` (`N27`).
2. **Its two words are separated by checkpoint-local data the shadow omits.**
   `local_holonomy_shadow` carries only per-step holonomies and the moduli
   multiset.  But Definition 2.3 puts **the record the amplitude composite
   writes** inside V-AMP's certificate, and that record is checkpoint-local data
   par excellence.  Recomputed: word A's amplitude composite writes
   `0|1|2|3|4` (the address chart) and word B's writes `01|2|3|4` (the forged
   2+1+1) (`N34`, `N35`).  The two words the unit exhibits as agreeing on
   "everything any admitted verification can read" differ in the endpoint
   record — and differ **precisely in the paper's own Gain 1**, the visible
   cancellation of Proposition 3.4.  The lossy witness is separated by the
   capability the delta section celebrates one page later.

*The conclusion is nonetheless repairable, and I exhibit the repair.*  Under a
correctly closed loop the checkpoint-local shadow over the 120×120 word pool
takes **exactly 1 value** while the global family takes **4** (`N29`): the
local shadow reads *nothing at all*, so the theorem's conclusion is far
stronger than claimed.  The cross-checkpoint invariant in closed form is
X = (arg u₀₀ − arg u₁₀) + (arg v₀₀ − arg v₀₁), sweeping all 8 values (`N30`),
and the endpoint record is the function of X that is δ exactly on X ∈ {0,4}
(`N33`).  **A valid witness** — agreeing on every checkpoint-local datum
including both amplitude records, differing in cross-checkpoint holonomy:

  A = ((0,0,0,4), (0,1,0,5)),  B = ((0,0,0,4), (0,2,0,6)),
  both writing `01|2|3|4` at checkpoints 1 and 2, both with per-step
  holonomies (4),(4), global families (1,4,5) vs (2,4,6), X = 7 vs 6 (`N36`).

### F4 — THE SCISSORS DO NOT STAND. The numerals reading binds. `[AMP]`

Full adjudication in §3 below.  In one line: the "record-producing,
checkpoint-local" blade is cut by the unit's own Definition 2.3, by the
cumulative definition of a checkpoint, and by the incompatibility between the
construal that licenses *carrying* the amplitudes and the construal that
forbids *reading* them.  §6.4 presents as a free choice something the unit has
already decided against itself.

### F5 — "Checkpoint-local" ⟹ "step-local" is a non sequitur, and the unit's own certificate refutes it. `[AMP]`

Definition 2.1: the checkpoints are the **cumulative composites**
C_t = g_t∘⋯∘g_1.  Definition 2.3: V-AMP's certificate is Definition 2.1's plus
"the gauge-invariant loop holonomies of **the carried diagram**."  At the final
checkpoint the carried diagram *is* the whole two-step diagram, so its
certificate contains the cross-checkpoint holonomy, and (P2) — which compares
carried against recomputed certificates — **reads it**.  `certificate_AMP`
implements exactly that: it calls `cycle_basis_holonomies(word_mats, word_sups,
n)` over the **whole** word, and `adjudicate_quintuple` uses it for every
committed patch.  Only the lossy adversary switches to a per-step object.  The
unit therefore uses two incompatible notions of what V-AMP's certificate
contains, and the lossy arm is the one that contradicts the definition.

### F6 — The (P2)-weak clause is vacuous, and the paper does not say so.

`passing_histories_1`'s own docstring records it — "(P2) is vacuous for an
honestly-carried certificate — the certificate is RECOMPUTED, so an honest
declarer always verifies" — and it is right: (P2)-weak can fail only if a
declarer carries a certificate he did not compute, which no adversary would do.
The paper reports "(P1) and (P2) pass at every committed patch" as a
*measurement* (§4.1, gate `L5-D1-P1`).  Half of it is a tautology.  Saying so
strengthens `BLOCKED-AT-THE-DECLARATION` materially: the axiom's second clause
is not a constraint on the declarer at all.

### F7 — The carried certificate is a function of the written record alone, which makes LOSSY-vs-V-CL far stronger than stated.

`certificate_CL(C, law, prep, n)` returns `(written_of(C), pres_size, clauses,
reach)`, and every component after the first is computed from `adj_c(part, law,
prep, n)` — a function of the *record* `part`, never of the operation `C`.
Measured: over all 3,125 DET operations, operations writing the same record
carry the **same** certificate in every case, and the whole of DET carries
exactly **52** distinct certificates — one per record (`N10`, `N10b`).

So Theorem 6.1's "120 histories, one class" is not a fixture accident and not a
measurement of the 120: **a chain of carried B″-certificates carries exactly
the sequence of written records and nothing else**.  The word *fine-grained*
(Definition 2.1, §1.1) is misleading: the certificate is not fine-grained about
the operation at all.  The honest form of Theorem 6.1 is the general one, and
it makes the kill unconditional rather than exhibited.

### F8 — Theorem 5.3's quantifier is wrong as written.

Paper, §5.3: "The range {S(B,𝔉,X₀,L,ρ,H) : H ∈ 𝓗(B,X₀,L)} is therefore a
function of the quadruple."  It is not: ρ is an argument of S and is not in the
quadruple.  The range is a function of **(quadruple, ρ)**.  The conclusion
survives — the stage-5 collision presents the same patch *at the same committed
state* — but the sentence as printed asserts more than the proof gives, and
branch C's own verdict (every covariant statistic is resolution-reading **or
state-reading**) makes the state argument the live one.  Order-theoretic
restatement in §4 below.  Two further slips in the same theorem: 𝓗 does not
depend on X₀ at all (it is a function of (B, L)), and "bounded by a quadruple
statistic" is the wrong relation — the correct one is *equality of achievable
sets*, not a bound.

### F9 — The amendment's "one legitimate one forged" clause is unmet at the amplitude scope, and unmeetable by this construction.

Amendment v2 §3 (binding): "two histories agreeing on everything any admitted
VERIFICATION can read, differing in the carried amplitude data, **one
legitimate one forged**."  Theorem 6.1's V-CL witness meets this (identity vs
deleted rotation, with the base's own labels).  Theorem 6.3's does not: it is
two lifts of one declared support word, and the base supplies **no provenance
labels anywhere in the declared amplitude family**.  Nor can the gap be closed
by giving the two words different endpoints — the endpoint record is
checkpoint-local data (F3), so any pair differing there is separated.  What
Theorem 6.3 actually establishes, at best, is *information loss*, not
*provenance loss*.  Deviation 3 records the V-CL arm coming out stronger than
pinned; the V-AMP arm coming out weaker than pinned is not recorded anywhere.

### F10 — Scope-tag and count defects.

- **Theorem 3.2 is tagged `[EXH-1]`** ("exhaustive over all one-step histories
  at the committed law").  The corroborating sweep uses `list(law)[:60]` — 60
  of DET's 3,125 operations (`N43`).  The tag is unearned.  (The theorem itself
  is proved; I re-proved it independently and it is correct.)
- **"Measured over 2,880 … carried paths"** (§3.2, §7.1, and the abstract).
  2,880 is the number of **tests**: the sweep is 4 laws × 60 × 6 × 2, over 240
  distinct one-step paths (each tested six times) and 1,440 distinct two-step
  paths — **1,680 distinct carried paths** (`N42`).
- **Theorem 6.2 is measured at one lift per history.**  `L5-LOSSY-AMP-C` uses
  `canonical_lift` (all-ones) only, while the paper's Theorem 6.2 speaks of the
  120 histories as such.  The gap closes on the general argument — a monomial
  diagram has rank 0, and unitarity forces unit moduli on a monomial matrix —
  so Theorem 6.2 is **true and reading-independent**, but the paper should carry
  the argument rather than the single-lift measurement.
- **The carried invariant is represented lossily.**  The holonomy family is
  reported as a *sorted multiset*, which forgets which basis element carries
  which phase; measured, it identifies X with X+4 (4 classes over 8 values,
  `N31`/`N32`) — and X = 0 against X = 4 is exactly the pair of cancelling
  configurations.  A sorted multiset of fundamental-cycle phases is not a
  complete invariant of the gauge class.

---

## 3. THE K3 ADJUDICATION — THE SCISSORS

**The question put to me:** is the "declared numerals" reading of verification
legitimately admissible; does one reading bind; or is the both-readings
disclosure the honest terminal form?

**Verdict: the numerals reading BINDS.  The both-readings disclosure is not the
honest terminal form** — it presents as an open choice a question the unit's own
definitions have already closed.  Under the binding reading,
`RQ0-L5-PROVENANCE-LOSSY` **does not fire against V-AMP at the amplitude
scope**.  Three independent grounds, in increasing order of force:

**(i) The unit's own Definition 2.3 puts the disputed datum inside the
certificate.**  V-AMP's certificate is defined to include "the gauge-invariant
loop holonomies of the carried diagram", and (P2) is defined as the comparison
of carried against recomputed certificates.  `certificate_AMP` computes those
holonomies over the whole word and is what every committed patch is adjudicated
with.  A verification that compares certificates containing the cross-checkpoint
holonomy reads the cross-checkpoint holonomy.  The step-local restriction
appears exactly once in the unit — inside the lossy adversary — and nowhere in
its definitions (F5).

**(ii) "Checkpoint-local" does not mean "step-local".**  Checkpoints are the
cumulative composites C_t (Definition 2.1).  Locality at the final checkpoint is
locality to the whole carried path.  §6.3's inference — "(P2) is
checkpoint-local by its own definition … so an admitted checkpoint verification
reads step-local invariants only" — replaces one word with another and carries
the conclusion on the substitution.

**(iii) The antecedent does not transport, and the two construals are
incompatible.**  I checked the scissors against v12's recorded-but-phased limit
as instructed.  v12 states it (paper 0, T3′ gloss; W7/paper-1 O2): *"The
theorem's content is block structure (cross-sector coherence dies), not phase
triviality: within an unresolved record sector, phase structure may survive."*
Two mismatches:

- **The localities are different.**  v12's "block" is a **record sector at one
  time**, and its surviving phase is *intra-sector*.  The unit's residue is
  *cross-checkpoint* — a loop spanning two steps.  §6.3's "block-local data is
  not phase-triviality of the composite" equivocates between sector-local and
  step-local.  Nothing in W7 says a check spanning two operations must fail to
  read a loop spanning them; W7's limit says a record that fails to resolve a
  sector leaves phase inside it.  To transport it the unit would have to build
  the check as a record-producing process, exhibit its block-diagonalization,
  and show the cross-checkpoint loop lies in an *unresolved* sector.  None of
  the three is done.  The transport is asserted.
- **The unit cannot have both construals.**  §2.3 licenses *carrying* the
  amplitudes on the ground that they are **declared numerals about known
  admitted operations** — "no-cloning constrains copying an unknown state; it
  says nothing against writing down the declared amplitudes of known admitted
  operations."  §6.3 forbids *reading* them on the ground that verifications are
  **record-producing physical processes**.  If checks are physical processes on
  unknown states, carrying is illegal by the same no-cloning argument §2.3
  disposes of.  If the amplitudes are declared numerals, computing a loop
  product of declared numerals is arithmetic, and the amendment's own gating
  question — "can checkpoint verification consume the carried amplitude data or
  does it necessarily collapse to its classical shadow?" — is answered **it can
  consume it**, by the unit's own `certificate_AMP`.

The scissors as drawn are therefore not symmetric.  One blade is the unit's
definitions; the other is an asserted analogy that its own §2.3 forecloses.

**What this costs the paper, and what it does not.**  It costs §6.3, §6.4, the
LOSSY-V-AMP-at-amplitude-scope arm, the §7.3 "Gain 2 is eaten by LOSSY" bullet,
and the abstract's italicised epigram (*"readable only under the reading that
leaves them unanchored…"*), which is the scissors restated and falls with it.
It does **not** cost the registered box.  `RQ0-L5-PROVENANCE-LOSSY` still fires
against V-AMP — at the **committed scope**, by Theorem 6.2, which is
reading-independent (the content is genuinely empty there: cycle rank 0, proved
and reproduced).  And `RQ0-L5-PROVENANCE-REGRESS` still fires against V-AMP,
for the reason in F2's repair: the amplitude scope's law is a support-level
object and constrains no amplitude at all.

**The honest terminal form**, in my judgement: *the amplitude datum that
verification can read is anchored by nothing (the law is support-level), and the
amplitude datum unitarity anchors (the per-step holonomy, ζ₈⁴) is constant and
therefore reads on nothing.*  That is a true scissors, it is measured, and it
does not depend on a contested reading of "verification."

---

## 4. THE REDUCTION'S ORDER-THEORETIC SIDE

Theorem 5.3 is not really a bound; it is a **fibre** statement, and saying so
makes it both correct and sharper.

Fix the law L.  (P1) defines
  𝓗(B) = { H : every step in L, comp(C_m) = A(B) },
which at one-step scope is precisely the **fibre of `comp` over B**.  Measured:
the fibres of `comp` partition all 3,125 DET operations into 52 classes, one per
record (`N40`); the fibre over the collision boundary has 120 members carrying
one certificate (`N41`).  Three consequences, in order-theoretic form:

1. **𝓗 is a function of (B, L)** — not of (B, X₀, L); X₀ does not occur in
   (P1).  The declarable-history map is a section of the partition of L into
   `comp`-fibres.
2. For any statistic S the **achievable set**
   A_S(B,𝔉,X₀,L,ρ) = { S(B,𝔉,X₀,L,ρ,H) : H ∈ 𝓗(B) } is a function of the
   quadruple **and of ρ** (F8).  The right relation is *equality of achievable
   sets*, not "bounded by": at a quadruple-and-state collision the two
   declarations have **identical** achievable sets, so no admission rule of the
   form "admit iff S ∈ A" — for any A whatever, up-set, down-set or neither —
   can admit one and reject the other, provided the adversary declares
   optimally.
3. Hence the corpus's "admitted iff small" orientation is **not needed**.  The
   paper's §4.2 orientation remark and the "adversary realizes any element"
   phrasing both suggest an infimum argument over an ordered range.  The fibre
   statement is stronger and order-free: the adversary does not need to
   *minimise* anything, he need only **declare the history the legitimate party
   declares**, which is available to him because the fibres coincide.  At that
   point the two quintuples are *identical*, and no statistic of any kind
   separates identical objects.

That is the whole of REGRESS, and it survives every finding above untouched.  I
attempted the protocol's escape question — is there any provenance-reading that
escapes the fibre bound by reading the carried path's internal structure? — and
found none: any such reading is a function of H, hence of a member of a fibre
both parties share.  The escape would require an argument the adversary does not
supply, which is exactly what §8's "next obstruction, named" already says.

**(P2)-strong's collapse, re-derived.**  Recomputed independently (`N38`):
(P2)-strong certifies δ and rejects the forged 2+1+1, the forged 2+2 **and the
legitimate tomographic minimum** — [True, False, False, False].  The collapse
onto B″ rigidity is exact, and the collateral rejection of the legitimate coarse
chart carries the **identical clause vector** as the forgeries,
(i-a) F, (i-b) T, (ii-a) F, (ii-b) T (`N39`, `N39b`).  §4.1's Discriminator-3
finding is correct as printed.  The order content is worth stating: (P2)-strong
demands admissibility at *every* checkpoint, and admissibility is the singleton
{δ} at any identity-containing law, so (P2)-strong forces the whole carried
chain into the top of the refinement order — it is rigidity applied m times, not
a new condition.

---

## 5. NUMBERS TABLE — 50 INDEPENDENT RECOMPUTATIONS

Exact arithmetic; own code; nothing imported from the unit.
"paper" = value as printed in the object or its receipt.

| # | quantity | recomputed | paper | verdict |
|---|---|---|---|---|
| N1 | record-lattice sizes, 1..5 configurations | 1,2,5,15,52 | same | ✓ |
| N2 | \|DET\|, \|REV\| | 3125, 120 | same | ✓ |
| N3 | \|Pres_DET\| at δ, 2+1+1, 2+2, tomo | 120,240,420,1280 | same | ✓ |
| N4 | ε at the coarse triple | 1/16, 1/8, 3/16 | same | ✓ |
| N5 | declarable one-step histories, four boundaries | 120,120,60,20 | same | ✓ |
| N5b | same as falling factorials 5₍ₖ₎, k = #blocks | 120,120,60,20 | — | new |
| N6 | admissible records under DET / REV | 1, 1 | same | ✓ |
| N6b | the singleton is δ | True, True | same | ✓ |
| N7 | declared states at denominator 16 | 4845 | same | ✓ |
| N8 | admitted isomorphisms; orbits of the 52 | 24, 12 | same | ✓ |
| N9 | 120 histories at δ → distinct V-CL certificates | 1 | 1 | ✓ |
| N9b | identity and (1,2,3,0,4) both in the class | True,True | same | ✓ |
| N10 | max distinct certificates among same-record ops (all 3125) | 1 | — | **F7** |
| N10b | distinct V-CL certificates over all of DET | 52 | — | **F7** |
| N11 | five declared generators exactly unitary | all True | same | ✓ |
| N12 | cycle ranks (H01),(H01,H23),(F4),(H01,H01) | 1,2,9,3 | same | ✓ |
| N13 | holonomy phases at the same words | [4],[4,4],[0,2,2,4,4,4,4,6,6],[0,4,4] | same | ✓ |
| N14 | Prop 3.4: support record vs amplitude record | 01\|2\|3\|4 vs 0\|1\|2\|3\|4 | same | ✓ |
| N15 | admitted unitary lifts of the declared step | 512 | 512 | ✓ |
| N16 | R2 one-step closed-loop holonomy classes | **1** | 4 | **F2** |
| N16b | unit-algorithm classes and multiplicities | 128×4 | same | reproduced |
| N17 | closed-loop phase a−b+d−c over all 512 | {4} | — | **F2** |
| N18 | vertex switchings moving R2's holonomy (of 512) | 0 | — | control |
| N18b | vertex switchings moving the UNIT's holonomy | **384** | 0 implied | **F1** |
| N19 | unit's per-step value = d+b−a+c = 2(b+c−a)+4 | verified all 512 | — | **F1** |
| N20 | R2's per-step value = a−b+d−c | verified all 512 | — | **F1** |
| N21 | unit's classes over the 512 family | {0:128,2:128,4:128,6:128} | same | reproduced |
| N22 | **corrected** classes over the 512 family | **{4: 512}** | 4 classes | **F2** |
| N23 | two-step diagram E, V, C, rank | 14, 15, 4, 3 | rank 3 | ✓ |
| N24 | checkpoint-local rank summed; unread residue | 2; 1 | 2; 1 | ✓ |
| N25 | unit's exhibited global holonomies A vs B | (0,4,6),(1,4,5) | same | reproduced |
| N26 | unit's exhibited per-step holonomies | [4],[6] | [4],[6] | reproduced |
| N27 | the same, correctly closed | [4],[4] | — | **F3** |
| N28/34 | amplitude records of the witness words | δ vs 01\|2\|3\|4 | — | **F3** |
| N35 | witness words separated by checkpoint-local data | True | — | **F3** |
| N29 | correct local shadows / global families over 120×120 | 1 / 4 | — | **F3** |
| N30 | values of the cross-checkpoint invariant X | all 8 | — | new |
| N31 | each X gives one global family | 1 | — | new |
| N32 | distinct global families over the 8 X-values | 4 (X ≡ X+4) | — | **F10** |
| N33 | endpoint record = δ exactly on X ∈ {0,4} | {0,4} | — | new |
| N36 | valid corrected witness exists | True | — | **F3 repair** |
| N37 | (P1),(P2)-weak at all four committed patches | all True | same | ✓ |
| N38 | (P2)-strong at the four patches | T,F,F,F | same | ✓ |
| N39 | tomo's clause vector = forged 2+1+1's | True | same | ✓ |
| N39b | that vector | F,T,F,T | same | ✓ |
| N40 | comp-fibres over DET: total, count | 3125, 52 | — | §4 |
| N41 | fibre over δ; its certificate image | 120, 1 | 120, 1 | ✓ |
| N42 | acyclicity sweep: tests vs distinct paths | 2880 / 1680 | "2,880 paths" | **F10** |
| N43 | DET operations covered by the sweep | 60 of 3125 | `[EXH-1]` | **F10** |

**Score:** 23 of 24 blind reproductions exact; the 24th (`N18b`) is F1.
Every classical number in the paper that I recomputed is correct.  Every
amplitude number that depends on the holonomy of a **non-Hadamard** lift is
wrong; the §3.3 table survives only because at the Hadamard the erroneous and
correct expressions coincide (a=b=c=0, d=4 gives 4 either way).

---

## 6. PER-RUNG CONFIRMATIONS (protocol §Verdict vocabulary)

| rung | claim | R2 disposition |
|---|---|---|
| (a) | REGRESS fires, both variants | **CONFIRMED**, and the proof is sound — but the V-AMP arm's stated mechanism (Prop 5.4) is false and must be replaced by the support-level-law argument (F2).  The reduction itself survives every finding; its quantifier needs repair (F8). |
| (b) | LOSSY fires, both variants, incl. the V-AMP rank-residue construction | **SPLIT.**  V-CL: **CONFIRMED and strengthened** (F7 — it is a theorem about the certificate, not a fact about 120 permutations).  V-AMP at the committed scope (Thm 6.2): **CONFIRMED**, reading-independent, though measured at one lift (F10).  V-AMP at the amplitude scope (Thm 6.3): **NOT CONFIRMED as delivered** — the witness is invalid (F3) and the reading it needs does not bind (F4).  The **rank accounting alone survives**: 3 against 2, residue 1, exactly reproduced (`N23`,`N24`), because cycle rank is combinatorial and untouched by F1.  A valid witness exists and is exhibited (`N36`). |
| (c) | the delta-zero theorem | **CONFIRMED.**  I re-proved Theorem 3.2 independently (E = mn, V = (m+1)n, every component meets the top layer so C ≤ n, rank = C − n ≤ 0, non-negativity forces 0) and reproduced rank 0 with an empty holonomy family on every single-valued path I built.  Untouched by F1: at rank 0 there are no cycles to mis-close.  §7.1 is the soundest section of the paper.  Caveats are cosmetic (F10: the `[EXH-1]` tag and the 2,880 count). |
| (d) | BLOCKED-AT-THE-DECLARATION as the census instantiation | **CONFIRMED**, and F6 strengthens it: (P2)-weak is not merely passed, it is vacuous.  "Adding a sixth declaration to five cannot bind the five" is the correct location and survives every finding. |
| (e) | the scissors disclosure honest | **NOT CONFIRMED.**  See §3.  The disclosure is not dishonest in intent — both readings were genuinely run and reported, which is more than most units do — but it is not *adjudicated*, and the adjudication goes against the reading the paper's kill depends on. |
| (f) | process deviations correctly recorded | Deviations 1–10 are individually accurate and Deviation 3 is exemplary (it records the pin's expectation being *beaten*).  **Two gaps:** the V-AMP lossy arm coming out *weaker* than the amendment specifies is nowhere recorded (F9), and the "declared numerals" reading is filed as Deviation 6 (a reading choice) when it is in fact the reading the unit's own Definition 2.3 imposes (F4/F5).  R3 holds K4; I flag these two as within my K3 scope only. |

---

## 7. SENTENCES TO REWRITE

1. **Abstract, "the carried holonomy takes 4 values with 128 lifts realizing
   each, so the amplitude datum is one further free declaration"** → the carried
   closed-loop holonomy of a full-support unitary step is **rigidly ζ₈⁴** on all
   512 admitted lifts; the amplitude datum is free not because it varies but
   because **the amplitude scope's law is support-level and constrains no
   amplitude at all**.
2. **Proposition 5.4, whole** → replace as above; delete "exactly 4 values …
   128 lifts realizing each"; keep the conclusion.
3. **§3.1, "a cycle basis therefore carries all of it and nothing else does"** →
   true of a cycle basis, false of what the code computes; and a *sorted
   multiset* of fundamental-cycle phases is not a complete invariant of the
   gauge class (F10).
4. **§6.3, "(P2) is checkpoint-local by its own definition … so an admitted
   checkpoint verification reads step-local invariants only"** → the inference
   does not hold: checkpoints are cumulative composites, and V-AMP's own
   certificate (Def 2.3) contains the whole carried diagram's holonomies.  If
   the step-local restriction is wanted it must be **postulated and labelled a
   postulate**, not derived.
5. **§6.3, the exhibited witness (per-step ζ₈⁴/ζ₈⁶; global (0,4,6) vs (1,4,5))**
   → per-step ζ₈⁶ is unattainable; both witness words are separated by their
   endpoint records.  Replace with the valid pair at `N36`, and state the far
   stronger true fact: **the checkpoint-local shadow is constant over the whole
   pool** while the cross-checkpoint invariant sweeps all eight values.
6. **§6.3, "This is the v12 recorded-but-phased limit applied to the checks"** →
   v12's limit is about **record sectors at one time** and its surviving phase
   is **intra-sector**; the residue here is **cross-checkpoint**.  Either build
   the check as a record-producing process and show the residue lies in an
   unresolved sector, or drop the citation and own the step-local reading as a
   declared modelling choice.
7. **§6.4 table and the italicised epigram** → the scissors do not stand as
   drawn (§3).  Replace with the true scissors: *anchored ⟹ constant (unitarity
   forces ζ₈⁴); free ⟹ unanchored (the law is support-level)*.
8. **§7.3, "Gain 1 is eaten by REGRESS … 128 admitted unitary lifts realize each
   of the 4 holonomy classes"** → the count is wrong; the mechanism is the
   support-level law.  And **§7.3, "Gain 2 is eaten by LOSSY"** → not under the
   binding reading; Gain 2 is eaten by REGRESS as well, for the same reason.
9. **Definition 2.1, "the carried certificate … the fine-grained B″-certificate"**
   → the certificate is a function of the **written record alone** (F7).  Say so:
   it makes Theorem 6.1 a theorem instead of an exhibit.
10. **§4.1 / gate `L5-D1-P1`, "(P1) and (P2) pass at every committed patch"** →
    note that **(P2)-weak cannot fail for an honest declarer** (F6).
11. **Theorem 5.3, "is therefore a function of the quadruple"** → of the
    quadruple **and the state**; 𝓗 is a function of **(B, L)**, X₀ does not
    occur; and the relation is **equality of achievable sets**, not "bounded by"
    (F8, §4).
12. **§3.2 / §7.1 / abstract, "over 2,880 … carried paths"** → 2,880 **tests**
    over **1,680 distinct paths**; and drop `[EXH-1]` from Theorem 3.2 (F10).
13. **Theorem 6.2** → carry the general argument (monomial ⟹ rank 0; unitarity
    ⟹ unit moduli on a monomial matrix), since the measurement fixes one lift
    per history.
14. **Deviations** → add: the V-AMP lossy arm does not meet the amendment's
    "one legitimate one forged" clause and cannot (F9).

---

## 8. COMMON GATES

- **Paper-vs-receipt sweep.**  Clean on counts and values: 12 anchors, 29 gates,
  0 must-pass failures, as printed; `L5-AMP-FREE`, `L5-LOSSY-AMP-A`,
  `L5-LOSSY-AMP-DIM`, `L5-LOSSY-CL`, `L5-LOSSY-AMP-C`, `L5-ACYC-M`,
  `L5-AMP-CONTENT`, `L5-D2-COLLISION` all carry exactly the values the paper
  quotes.  **The paper faithfully reports what the code computed.**  The defect
  is upstream of the reporting, in what the code computes.
- **Scope tags.**  One unearned (`[EXH-1]` on Theorem 3.2, F10).  Otherwise the
  variant- and reading-quantifiers are present on the kill sentences —
  §6.3/§6.4/§8 all carry the reading-relativity, and the §8 scope paragraph is
  candid.  This is why the finding is a *wrong adjudication*, not a hidden one.
- **Name-blindness.**  Not my rung (R3's), but I note the six statistics'
  relabelling sweep is unaffected by F1: `s_carried_cycle_rank` reads the
  **rank**, which is combinatorial and correct.  The separation table's
  "carried cycle rank: 0,0,0,0" is right.
- **Forbidden vocabulary.**  Clean.  I searched for spatial/temporal/causal
  smuggling around "path", "history", "step", "checkpoint": every use is
  operational, the non-claims section is explicit, and §9's first bullet is
  exactly the right disclaimer.  No region, locality, manifold, causal order or
  gravity object appears.
- **Deviations complete.**  Two gaps, both in §6 (F9, F4) — see rung (f).
- **Mutants / determinism / floats.**  No float in any path I read or rebuilt;
  the amplitude representation (c, s, e) is exact.  **A mutant-coverage gap
  falls in my rung:** `hol-lax` sets `acc = AONE`, i.e. it kills the holonomy
  wholesale.  No mutant perturbs the **sign convention** — which is precisely
  the defect that survived.  A mutant that reverses one leg's direction, or a
  gauge-invariance self-test (switch the vertices, assert the invariants are
  fixed), would have caught F1 immediately.  I recommend the self-test as a
  permanent gate: it is four lines and it is the definitional criterion the
  paper already states.
- **Single-threaded.**  The paper reads as authorship throughout; no correction
  rounds are catalogued.  Compliant.

---

## 9. WHAT I DID NOT CHECK

K1 (the delta-zero theorem's edge cases beyond my re-proof) and K2 (the full
reduction audit) are R1's primary; K4, the deviations census, the freeze and the
mutant-repair audit are R3's.  I did not re-derive the B″ cost tower
(120/360/1260/3120), the obstruction-set construction, ω's three zeros, or B″
Theorem 6.1's comparable-pair count — anchors A07, A08, A12 are unverified by
me.  I did not audit v12 paper 1's own holonomy code beyond confirming it does
not share the defect.  I did not run the object's code; every number above is
from my own implementation, and where I needed to know what the unit's algorithm
does I transcribed it into my scratchpad rather than importing it.

**Frozen on delivery.**
