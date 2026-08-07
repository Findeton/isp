# R1 — OPERATOR-LENS HOSTILE REVIEW

## RQ0-L5 Branch A, *The Provenance Quintuple* — K1 (the delta-zero theorem) and K2 (the REGRESS reduction) primary

**Reviewer:** R1, operator lens.
**Protocol:** `v13/note-rq0-provenance-hostile-protocol.md` (frozen, `0e1ff17`).
**Object:** `v13/paper-rq0-provenance-quintuple.md` + `v13/code/rq0_l5_provenance_*`
(commit `6ee172c`); pin `ce18eac` + amendment v2 `a05e3d5`.
**Method:** own exact code, `/opt/homebrew/bin/python3.13`, in a scratch directory;
**nothing imported from the unit**. Amplitudes were re-implemented in the
cyclotomic ring $\mathbb Q[\zeta_8]$ as 4-tuples of `Fraction`s over
$\{1,\zeta,\zeta^2,\zeta^3\}$ with $\zeta^4=-1$ and
$2^{-1/2}=(\zeta-\zeta^3)/2$ — deliberately *not* the unit's $(c,s,e)$ triple, so
the arithmetic is independent. No float anywhere. **30 independent
recomputations** (protocol minimum: 10).

---

## VERDICT

> ## `ACCEPT-WITH-FIXES`

**The registered outcome stands.** Both kills fire, on both variants;
`RQ0-L5-BLOCKED-AT-THE-DECLARATION` is the right instantiation; branch B is the
proven residue. I could not reverse a single verdict line, and my constructed
escape attempt against the quadruple bound **failed and confirmed the unit's own
diagnosis**.

**But one substantive defect is found and it is not cosmetic.** The unit's
`cycle_basis_holonomies` computes a **gauge-variant** quantity — precisely the
thing the paper declares illegal to carry. Measured: under 512 random vertex
switchings the unit's quantity changes in **379 of 512** trials; the true
invariant changes in **0 of 512**. Consequently:

* **Proposition 5.4 is false as stated.** The carried gauge-invariant holonomy
  over the complete 512-lift family takes **one** value ($\zeta_8^4$, all 512
  lifts), not "$4$ values with $128$ lifts realizing each". This is a *theorem*,
  not a fixture fact: any $2\times2$ unitary with all entries of equal modulus
  satisfies $U_{00}U_{11}=-U_{01}U_{10}$ (verified, 0 violations / 512), so the
  single loop invariant is identically $-1$.
* **Gate `L5-AMP-FREE` fails under correction** (its predicate is
  `len(hol) >= 2 and all(v > 1)`; corrected, `len(hol) == 1`). The receipt's
  "$0$ must-pass failures" and the paper's "$29$ gates, all passing" do not
  survive the repair as written. A kill-class gate is involved.
* **Theorem 6.3's exhibited witness numbers are corrupted.** "Per-step
  holonomies $\zeta_8^4$ and $\zeta_8^6$" is *impossible*: over the whole 512-lift
  family the achievable set of per-step holonomies is $\{4\}$. The reported
  cross-checkpoint triple $(0,4,6)$ is likewise unachievable.

The reason this is `ACCEPT-WITH-FIXES` and not `REJECT`: **every conclusion
survives the repair, and two of them get stronger.** The corrected facts support
REGRESS-at-amplitude-scope and LOSSY-against-V-AMP *better* than the printed ones
do, and I supply the replacement constructions and numbers below. No kill is
reversed; no anchor moved; the delta-zero theorem — K1's core, and the paper's
headline — is **correct, and I confirmed it far beyond the unit's own sweep**.

---

## FINDINGS, RANKED

### F1 — MAJOR. The carried "gauge-invariant holonomy" is gauge-variant

`rq0_l5_provenance_exact.py:441–476`. `tree_path` stores each tree leg as
`out.append((e, -s))` — already reversed — and `cycle_basis_holonomies` then
reverses again:

```python
legs = [(e, +1)] + [(ee, -ss) for ee, ss in reversed(p)]
```

The double negation means the tree legs are traversed in the **same** direction
as the extra edge. The "loop" is never closed: the quantity computed is the
product of the extra edge and the tree path *both* running $a\to b$. Its gauge
factor at the $H_{01}$-support step is $\varphi(1,1)^2\varphi(0,1)^{-2}\neq1$.

**Measured decisively.** Applying random vertex switchings (phases $\zeta_8^k$ at
each vertex) to the layered diagram:

| convention | changed under switching | verdict |
|---|---|---|
| alternating product (extra edge forward, tree path **reversed**) | **0 / 512** | GAUGE-INVARIANT |
| the unit's sign pattern | **379 / 512** | **GAUGE-VARIANT** |

This is exactly the smuggling the paper forbids in §2.3 and §3.1: *"a raw
per-edge phase is an artifact of the lift and carrying it would smuggle."* The
unit carries a quantity that is not a loop product.

**Blast radius — audited claim by claim.**

*Unaffected (the two conventions agree):* the entire §3.3 generator table. I
reproduced every row on both conventions and they coincide, because the relevant
tree legs of `ID`, `SW01`, $H_{01}$, $H_{23}$ and $F_4$ carry weight $1$ or $\pm1$.
Cycle **ranks** are combinatorial and untouched. Theorem 3.2, `L5-ACYC-M` and
`L5-ACYC-P` are untouched — rank $0$ means *no cycles*, so no sign convention can
matter.

*Broken:* `L5-AMP-FREE` / Prop 5.4 / abstract line "the carried holonomy takes
$4$ values with $128$ lifts realizing each" / §7.3 "Gain 1 is eaten … $128$
admitted unitary lifts realize each of the $4$ holonomy classes" / §8 "$128$
lifts per class" / `L5-LOSSY-AMP-A`'s printed witness.

**The repair, supplied.** Prop 5.4's *role* is rescued by a stronger fact:

> Over the complete family of $512$ admitted unitary lifts of one declared
> support step the carried gauge-invariant holonomy is **constant** —
> $\zeta_8^4$, all $512$ — so it carries *no information whatever* about which
> lift was declared, while the endpoint record of the two-step word $(U,U)$
> varies over that same family: **128 of the 512 write $\delta$ (the amplitude
> composite cancels) and 384 write the forged $2{+}1{+}1$**; over $64\times64$
> mixed pairs $(U,V)$ the split is $1024$ / $3072$. The forger chooses the lift;
> the carried invariant cannot police the choice, because it does not vary with
> it.

That is a *better* REGRESS than the printed one: the amplitude datum is not
merely a free declaration among four options, it is **blind**.

### F2 — MAJOR. No mutant in the falsification suite could have caught F1

`MUTANTS` includes `hol-lax`, which sets `acc = AONE` — it replaces the
accumulated holonomy *wholesale*. A sign-convention error survives it untouched,
because `hol-lax` only tests that *some* holonomy is computed, never that the
**right** one is. There is no gauge-covariance mutant and no gauge-invariance
gate anywhere in the unit. Given that gauge-invariance is the paper's own
stated admissibility criterion for carried content (§2.3, §3.1, Non-claim 5),
its absence from both the gate set and the mutant set is the process failure
that let F1 through. **A `L5-GAUGE` self-test — switch the diagram, recompute,
require equality — belongs in the repair, with a permanent negative control
(the unit's current convention) that the gate must catch.**

### F3 — SUBSTANTIVE. Theorem 6.3's witness is real; its exhibited numbers are not

The rank accounting is exactly right and lift-independent: global two-step rank
$\mathbf 3$, checkpoint-local ranks $1+1=\mathbf 2$, residue $\mathbf 1$
(reproduced). And a witness **does** exist under the corrected convention — in
fact a stronger one, since the checkpoint-local shadow is *constant* across the
whole lift family:

| | unit (printed) | R1, corrected |
|---|---|---|
| local per-step holonomies | $[[4],[6]]$ | $((4),(4))$ — **and $(4)$ is the only achievable value** |
| global A | $(0,4,6)$ — **unachievable** | $(0,4,4)$ |
| global B | $(1,4,5)$ | $(1,4,5)$ |

The achievable global triples are exactly $(h,4,h{+}4)$ for $h\in\{0,1,2,3\}$.
So Theorem 6.3's conclusion holds *a fortiori*: a checkpoint-local verification
reads a constant and therefore reads nothing, while the cross-checkpoint part
takes four values.

**And this sharpens §6.4's scissors rather than dissolving it.** I measured that
the four cross-checkpoint holonomy classes each determine a *unique* amplitude
composite record (0 classes contain more than one record over $64\times64$
pairs; exactly one class carries the cancelling record, $1024$ of $4096$). So
under reading A (a classical computation on declared numerals) the verification
genuinely does read the datum that decides the endpoint — and under reading B it
genuinely reads a constant. The scissors is *better founded* after repair than
before. This is the one place where the correction actively helps the paper, and
it should be said in the paper's own voice.

### F4 — SUBSTANTIVE. The 120→1 collision and LOSSY-CL are definitional, not measured

`certificate_CL(C, law, prep, n)` computes `part = written_of(C)` and derives
every remaining component from `part` alone. **The carried certificate reads the
checkpoint only through the record it writes.** Therefore any two one-step
histories writing the same record are indistinguishable — always, at every
boundary, under every law. Measured: the same $120\to1$ collapse occurs at *all
four* committed boundaries ($120,120,60,20$ histories $\to$ one certificate
each), and over all $3125$ DET one-step histories the number of distinct carried
certificates equals the number of distinct records written, $52 = 52$.

Theorem 6.1 and `L5-LOSSY-CL` are therefore **true but carry no fixture
content**. They are presented as "an exhibited witness at the committed fixture";
they are a restatement of Definition 2.1. Deviation 3 already notes the kill is
"stronger than the pin's form" — the *reason* is this, and it is not stated.
The honest and much stronger sentence is available: *the pin's carried object is
record-valued, so provenance beyond the written record is not carried at all,
and LOSSY is immediate from the definition of what is carried.*

### F5 — SUBSTANTIVE. Theorem 3.2's stated conclusion exceeds its proof

The theorem concludes "**V-AMP's certificate reduces to V-CL's identically**".
The Euler argument establishes only that the *loop-holonomy* content is empty.
`certificate_AMP` returns four extra fields: the amplitude record, the rank, the
holonomies **and the moduli profile**. Rank-$0$ covers two of them. The moduli
profile is **not** covered — and moduli are gauge-invariant, so they are not
trivialised by switching on a forest.

At the committed scope this is closed only by a *declared choice*: the unit uses
`canonical_lift`, the all-ones matrix. Its docstring says it is "used only where
the acyclicity theorem says the lift is immaterial" — but the acyclicity theorem
says the *phases* are immaterial, not the moduli. Demonstrated on a committed,
single-valued, non-injective step (the block-minimum idempotent of the forged
$2{+}1{+}1$):

| declared lift | rank | holonomy | moduli profile |
|---|---|---|---|
| all-ones (`canonical_lift`) | 0 | empty | $(1,1,1,1,1)$ |
| modulus $\tfrac12$ on one column | 0 | empty | $(1,1,1,1,\tfrac12)$ |
| global phase $\zeta_8^3$ | 0 | empty | $(1,1,1,1,1)$ |

A single-valued **non-injective** step has *no* unitary lift, so nothing in (P1)
or (P2) pins its amplitude description — exactly the freedom Prop 5.4
celebrates one section later. §7.1's *"They were carried in full, exactly"* is
therefore not earned as an unqualified sentence: the committed-scope amplitude
lift is **chosen**, not ranged over. The verdict is unaffected (a varying
modulus profile would be one more free declaration, which REGRESS eats), but the
theorem needs the hypothesis and §7.1 needs the qualifier.

### F6 — MODERATE. "2,880 carried paths" is 2,880 *tests* over 1,680 distinct paths

`run_acyclicity` iterates `for a in pool: for b in pool[:6]: for w in ([a],[a,b])`,
so each one-step path is re-tested six times. Reproduced exactly: **2,880 tests,
1,680 distinct carried paths** (240 one-step, 1,440 two-step); 1,200 tests are
duplicates. The receipt's own key is honest (`"paths_tested": 2880`); the paper's
prose at lines 99 and 325 converts tests into "carried paths". (Line 425's
$6\times4\times120=2{,}880$ name-blindness figure is correctly described as
*tests* and I reproduce it.)

**Scope-tag error rides along.** Theorem 3.2 is tagged `[EXH-1]` — "exhaustive
over all one-step histories at the committed law". The sweep takes
`list(law)[:60]`: 60 of DET's 3,125 and 60 of the funnel closure's **3,006**. It
is an arbitrary prefix sample, not exhaustive. Since the theorem is *proved*, the
measurement is confirmatory and nothing substantive turns on it — but the tag is
wrong and the protocol asks for tag discipline.

I closed the gap on the unit's behalf: **zero violations over *all* 120 members
of REV, *all* 3,006 members of the funnel closure (36,072 tests, 21,042 distinct
paths) and a 120-member DET slice** — $E=mn$, $C=n$, rank $0$, empty holonomy
family, every case.

### F7 — MODERATE. Two scope quantifiers missing on kill sentences

1. "the **complete** family of $512$ admitted unitary lifts" (abstract line 110,
   §8 line 703). Complete only within the declared equal-modulus $\zeta_8$
   family. §5.4 displays the matrix form so the scope is visible *there*; the
   abstract and §8 assert completeness unqualified. I verified the enumeration is
   genuinely complete *within that family*: brute force over all $8^4=4096$
   exponent tuples yields exactly **512** unitaries, and they are exactly the set
   the unit's parametrisation produces.
2. `L5-AMP-EXACT`'s claim sentence says "all sums formed are between
   commensurable terms, so no float and no MIXED residue arises", but its
   predicate inspects **only the declared generators' moduli strings**. No sum
   formed inside `matmul`, `asum` or `is_unitary` is ever checked for a MIXED
   token. The claim is true (I formed every one of those sums in an independent
   exact representation with no incommensurable residue) but it is **not what the
   gate measures**. Gate-claim/gate-predicate mismatch.

### F8 — MINOR. Theorem 5.3's proof invokes structure it does not use

See K2 below. The reduction never uses (P1)'s factorisation, and saying "By (P1)…"
invites a reader to hunt for an escape through a cleverer (P1) — which cannot
exist. The stronger statement is available for free.

---

## K1 — THE DELTA-ZERO THEOREM: `SOUND`

**Re-proved independently, and by a shorter route than the paper's.** The paper's
Euler argument ($E=mn$, $V=(m+1)n$, $C\le n$, $\operatorname{rank}=C-n\le0$) is
correct as written and I verified each step. But it is stronger than it needs to
be, and the stronger form matters for the edge-probe:

> **The forest lemma.** In a layered diagram whose edges join adjacent layers
> only and in which every vertex has **at most one** upward edge, take any
> undirected cycle and consider the lowest layer it meets. A vertex there carries
> two cycle-edges, both going upward — contradicting "at most one". So the
> diagram is a forest and the cycle rank is $0$. $\square$

This needs neither totality nor the component count, so it survives **partial**
steps (a vertex with no image), which the paper's $E=mn$ does not. The paper's
proof is correct for the total single-valued case it states; the lemma shows the
theorem's edge is wider than claimed.

**Edge-probes, as the protocol requires.**

* *Multivalued steps.* The hypothesis is sharp and the failure is immediate: one
  multivalued step at a 2-block support gives rank $1$ (reproduced: $E=7$,
  $V=10$, $C=4$, rank $1$). The theorem does not over-reach.
* *The declared amplitude family's closure — is the 7-op gate right?* Reproduced
  independently: the support-level composition closure of
  $\{{\rm ID},{\rm SW}_{01},H_{01},H_{23},F_4\}$ has exactly **7** members
  ($I$, the transposition, the two blocks, their union, the transposition-times-
  block, and the 4-block). The gate is right, and Deviation 4 correctly discloses
  that the *amplitude*-level monoid is a different object — necessarily so, since
  $H_{01}\!\cdot\!H_{01}={\rm ID}$ at amplitude level while the support composite
  is the 2-block. That disclosure is honest and load-bearing.
* *"Vertex switching trivializes every edge phase on a forest."* True — root each
  tree, set phases inductively — and the declared gauge group ($\zeta_8$ powers)
  is rich enough, since every declared amplitude's phase is an 8th root. No gap.
* *The 2,880 rank-0 measurement and the empty holonomy family.* Confirmed, and
  extended to exhaustive coverage of two whole laws (F6). Zero violations
  anywhere.

**The one real gap is F5:** the theorem's *conclusion* ("V-AMP's certificate
reduces to V-CL's identically") is not what the argument proves. The argument
proves the holonomy family is empty. Restrict the conclusion, or add the
hypothesis that the declared lift is monomial with unit moduli.

**And §3.1's characterisation is false as written**: *"a cycle basis therefore
carries all of it and nothing else does."* The moduli are gauge-invariant and are
not loop products — which the unit's own `certificate_AMP` concedes by carrying
`mods` as a separate field. (I tested the sharper conjecture that the amplitude
composite's record escapes the holonomy family too: it does **not** — the record
is gauge-invariant, 0/128 trials changed it, but on this family the cycle basis
*does* determine it. The claim fails on moduli, not on cancellation.)

---

## K2 — THE REGRESS REDUCTION: `SOUND, AND STRONGER THAN STATED`

**The decoupling (120 vs 0).** Reproduced from scratch: the admitted one-step
paths writing each committed boundary are $120,120,60,20$ and the B″ obstruction
sizes are $120,360,1260,3120$. The forged $2{+}1{+}1$ costs $120$ deletions to
make *admissible* and $0$ to *generate* — $120$ admitted operations already write
it. Sound, and the arithmetic behind it is transparent: the maps writing a
partition with blocks $b_1..b_k$ are the injections of the $k$ blocks into the
carrier, $5\cdot4\cdots(5-k+1)$, giving $120,120,60,20$ for block counts
$5,4,3,2$. Theorem 5.1 is correct.

**The declarable-history set as a quadruple function — audit of the proof.**
The proof is valid. Two notes:

1. The paper writes $\mathcal H(B,X_0,L)$; (P1) as implemented ignores the
   preparation entirely, so it is really $\mathcal H(B,L)$. Harmless (a function
   of fewer arguments is a function of more), and the gate `L5-D2-FUNCTION` states
   the tighter version. Cosmetic inconsistency only.
2. **The reduction never uses (P1).** Its engine is: *the admissible values of the
   new component are decided by a predicate whose arguments are all already
   declared.* Nothing about (P1)'s particular shape enters. The general statement
   subsumes it:

> **Declaration-closure bound (R1).** Let $D$ be a declared datum and extend it by
> a component $H$ whose admissibility is decided by *any* predicate $A(D,H)$. For
> any statistic $S(D,H)$ the achievable range $\{S(D,H):A(D,H)\}$ is a function of
> $D$. Hence two contexts presenting the same $D$ have identical achievable
> ranges, and no $S$ separates them under adversarial declaration of $H$.

Theorem 5.3 is the case $A=$ (P1). Stating it this way is strictly better: it
closes the escape route *in advance* instead of inviting the reader to look for
a cleverer (P1). It also makes §8's sentence — *"Adding a sixth declaration to
five cannot bind the five"* — a corollary rather than a summary, which is what it
deserves to be.

**The 120→1 certificate collision.** Reproduced ($120\to1$ in V-CL and in
V-AMP). See F4: it is definitional, and the unit should own that, because owning
it makes the kill stronger. I confirmed the V-AMP arm is nonetheless *robust*
under my F5 concern: at $\delta$ the histories are permutations, whose unitary
lifts are forced monomial with unit moduli, so the moduli profile cannot vary
there and the collision holds for *every* admitted lift, not just the all-ones
one. That is worth stating — it is the one place where the lift-freedom does not
bite, and it is the place the argument most needs it not to.

**The 512/4/128 structure at amplitude scope.** **Falsified** — see F1. Replaced
by: 512 lifts, **one** holonomy class, endpoint record varying 128/384.

### THE ESCAPE QUESTION — attempted, and it failed

*Task: construct a provenance-reading that escapes the quadruple bound by reading
the carried path's internal structure in a way (P1) does not factor.*

I built five candidate readings that each read internal structure (P1) is blind
to, and measured the admissible-history set each induces at the collision patch:

| candidate reading | reads what (P1) cannot | $|\mathcal H|$ at $\delta$ | escapes? |
|---|---|---|---|
| (P1) as pinned | — | 120 | no |
| (P2)-strong | every checkpoint's admissibility | 120 | no |
| monotone-refinement | the order relation between successive records | 120 | no |
| state-reading | the checkpoints' concordance defect against $\rho$ | 120 | no |
| generated-law | the law the carried steps generate | 120 | no |
| fan-in-minimal | the cardinality of $\mathcal H$ itself | 0 | no |

**All six fail, and they fail for one reason.** Each is a predicate of
$(w,\text{law},\text{part},\text{prep},\rho)$; the two contexts at the collision
agree on all five arguments; so each induces the *same* admissible set for both.
The bound is **not about the quadruple** and **not about (P1)'s factorisation** —
it is about the arguments being **declared**. Reading deeper into the carried
path cannot help, because the carried path is itself supplied by the party under
test.

The only door I found is the one the paper already names. A predicate taking an
argument the declarer does *not* supply separates immediately: I instantiated an
oracle reading that consults the true history, and $|\mathcal H|$ collapses from
$120$ to $1$. But its argument is not in the quintuple, so it is not a
provenance-reading at all — it is the thing provenance was supposed to replace.

**Conclusion: no escape exists at this scope, and the impossibility is wider
than the paper claims for it.** §8's *"a condition whose arguments the adversary
does not supply"* is independently confirmed as the unique residue, and
`RQ0-L5-BLOCKED-AT-THE-DECLARATION` is the correct object — the block is at
declaredness, not at the quadruple, not at the carrier and not at the law.

---

## NUMBERS TABLE — 30 INDEPENDENT RECOMPUTATIONS

| # | quantity | paper / receipt | R1 | |
|---|---|---|---|---|
| N1 | record-lattice sizes, 1..5 | 1,2,5,15,52 | 1,2,5,15,52 | ✓ |
| N2 | \|DET\|, \|REV\| | 3125, 120 | 3125, 120 | ✓ |
| N3 | declarable one-step histories ($\delta$,2+1+1,2+2,tomo) | 120,120,60,20 | 120,120,60,20 | ✓ |
| N4 | $\operatorname{Pres}$ under DET | 120,240,420,1280 | 120,240,420,1280 | ✓ |
| N5 | obstruction / cost tower | 120,360,1260,3120 | 120,360,1260,3120 | ✓ |
| N6 | admissible records, DET & REV | 1, 1 | 1, 1 | ✓ |
| N7 | single-valuedness, committed laws | all true | all true | ✓ |
| N8 | acyclicity violations, **all** REV + **all** funnel closure + DET slice | (0 over sample) | **0 over 38,952 tests** | ✓+ |
| N9 | acyclicity sweep: tests vs **distinct paths** | 2,880 "carried paths" | 2,880 tests / **1,680 paths** | **✗** |
| N10 | support closure of the declared amplitude family | 7 | 7 | ✓ |
| N11 | cycle ranks (ID,SW01,H01,(H01,H23),F4,(H01,H01)) | 0,0,1,2,9,3 | 0,0,1,2,9,3 | ✓ |
| N12 | holonomy phases, §3.3 table | (4),(4,4),(0,2,2,4,4,4,4,6,6),(0,4,4) | identical | ✓ |
| N13 | $(H_{01},H_{01})$ support vs amplitude record | 2+1+1 vs $\delta$ | 2+1+1 vs $\delta$ | ✓ |
| N14 | $\varepsilon$ at the coarse triple | 1/16, 1/8, 3/16 | 1/16, 1/8, 3/16 | ✓ |
| N15 | admitted isomorphisms / orbits of the 52 | 24, 12 | 24, 12 | ✓ |
| N16 | declared state grid at denominator 16 | 4845 | 4845 | ✓ |
| N17 | histories at $\delta$ → carried certificates | 120 → 1 | 120 → 1 | ✓ |
| N18 | same collapse at **every** boundary | (presented as fixture) | **holds at all four — definitional** | **✗** |
| N19 | over all 3125 DET steps: records vs certificates | — | 52 = 52 | (F4) |
| N20 | amplitude-composite record under switching | — | invariant, 0/128 | ✓ |
| N21 | (P1),(P2)-weak at every committed patch | pass | pass | ✓ |
| N22 | legit tomo min ≡ forged clause vector | identical | (F,T,F,T) both | ✓ |
| N23 | (P2)-strong certifies only $\delta$ | yes | yes | ✓ |
| N24 | name-blindness violations, six statistics | 0 / 2,880 | 0 / 2,880 | ✓ |
| N25 | negative control caught | caught | caught, 120 violations | ✓ |
| N26 | amnesty sweep | 0 / 4845 / 0 | 0 / 4845 / 0 | ✓ |
| N27 | unitary lifts among all $8^4$ exponent tuples | 512 "complete" | **512, complete in-family** | ✓ (F7) |
| N28 | **holonomy classes over the 512 lifts** | **4 × 128** | **1 × 512 ($\zeta_8^4$)** | **✗** |
| N29 | gauge test: unit's convention vs alternating | (untested) | **379/512 vs 0/512** | **✗** |
| N30 | two-step rank / local rank / residue | 3 / 2 / 1 | 3 / 2 / 1 | ✓ |

Plus: $U_{00}U_{11}=-U_{01}U_{10}$ over all 512 lifts, **0 violations**;
per-step holonomy achievable set $=\{4\}$ (so $\zeta_8^6$ is impossible);
achievable global triples $=(h,4,h{+}4)$, $h\in\{0,1,2,3\}$ (so $(0,4,6)$ is
impossible); endpoint record over the 512 lifts of $(U,U)$: **128 $\delta$ / 384
forged**; funnel closure size **3,006**.

**No anchor moved.** All twelve anchor quantities reproduce exactly by
independent routes, including three the unit reaches through inherited modules
that I rebuilt from their published definitions ($\varepsilon$ as
$\sum_b(\sum_{i\in b}\rho_i-\max_{i\in b}\rho_i)$; the stabiliser as the
$\rho$-preserving permutations; the grid as compositions of 16 into 5 parts).

---

## PER-RUNG CONFIRMATIONS

**(a) REGRESS, both variants — `CONFIRMED, one arm needs repair.`** Theorems 5.1,
5.2 and 5.3 are sound and reproduce; the reduction is stronger than stated (K2).
Proposition 5.4, the V-AMP arm's stated *mechanism*, is falsified by F1 and must
be replaced by the constancy construction. REGRESS still fires on both variants.

**(b) LOSSY, both variants, incl. the V-AMP rank-residue construction —
`CONFIRMED, numbers must be replaced.`** The rank residue ($3$ vs $2$) is exactly
right and lift-independent. The V-CL arm is sound but definitional (F4). The
V-AMP witness exists under correction — in a stronger form, since the
checkpoint-local shadow is constant — but the printed per-step and
cross-checkpoint values are unachievable (F3).

**(c) The delta-zero theorem — `CONFIRMED.`** Re-proved independently by a
shorter argument that widens its edge; every measurement reproduced and extended
to exhaustive coverage of two laws. One conclusion-vs-proof gap (F5) and one
count/tag overstatement (F6). **This is the paper's strongest result and it
holds.**

**(d) `BLOCKED-AT-THE-DECLARATION` as the correct census instantiation —
`CONFIRMED, independently.`** My escape attempt, run without reference to §8,
terminated on exactly this object: not the quadruple, not the carrier, not the
law, but declaredness. The instantiation is right and the paper's justification
for preferring it is right.

**(e) The scissors disclosure honest — `CONFIRMED, and improved by the repair.`**
Both readings are genuinely run and neither is chosen by fiat. After correction
the scissors is *better* founded: I measured that the cross-checkpoint holonomy
classes each determine the amplitude composite's record uniquely, so reading A
really does read the decisive datum and reading B really does read a constant.
§6.4 should be re-derived on the corrected numbers; its conclusion is unchanged.

**(f) Process deviations (mutant repairs; budget) — `PARTIAL, deferred to R3
with one finding added.`** Not my rung; I record F2, which is process-critical:
the declared mutant `hol-lax` is structurally incapable of catching F1, and
there is no gauge-covariance gate anywhere in the unit despite gauge-invariance
being the paper's own admissibility criterion for carried content. The two
mutants the paper discloses as repaired mid-unit (§10) are a good-faith
disclosure; the gap F2 names is a different and larger one.

---

## SENTENCES TO REWRITE

1. **§5.4 / abstract line 110 / §7.3 / §8** — *"the carried gauge-invariant
   holonomy takes exactly **4** values … with **128 lifts realizing each**"*.
   **False.** Replace with: *over the complete family of 512 admitted unitary
   lifts the carried gauge-invariant holonomy is **constant** at $\zeta_8^4$ — a
   theorem, since an equal-modulus $2\times2$ unitary satisfies
   $U_{00}U_{11}=-U_{01}U_{10}$ — so it carries no information about which lift
   was declared, while the endpoint record of $(U,U)$ varies 128 / 384 across
   that family. The amplitude datum is not merely free; it is blind.*

2. **§6.3** — *"per-step holonomies $\zeta_8^4$ and $\zeta_8^6$ in both — and
   different cross-checkpoint holonomy, $(0,4,6)$ against $(1,4,5)$"*. Both
   $\zeta_8^6$ and $(0,4,6)$ are **unachievable**. Replace with the corrected
   witness: *identical checkpoint-local shadows $\zeta_8^4$ and $\zeta_8^4$ — the
   only value the family admits — and cross-checkpoint holonomies $(0,4,4)$
   against $(1,4,5)$.*

3. **§3.1** — *"a cycle basis therefore carries all of it and nothing else does"*.
   **False**: moduli are gauge-invariant and are not loop products, as the unit's
   own `certificate_AMP` concedes by carrying `mods` separately. Replace with
   *"carries all of its **phase** content"*.

4. **Theorem 3.2 statement** — *"V-AMP's certificate reduces to V-CL's
   identically"*. Not proved by the argument given. Either restrict to *"the
   carried gauge-invariant loop content is empty"*, or add the hypothesis that the
   declared lift is monomial with unit moduli, and say that at the committed scope
   this is a **declared choice** (the all-ones lift) rather than a forced one.

5. **§7.1** — *"It is not that the amplitudes were withheld … They were carried in
   full, exactly."* Add the qualifier: *for the declared all-ones lift*. A
   single-valued non-injective step has no unitary lift, so (P1)/(P2) do not pin
   its amplitude description (F5).

6. **§3.2 / abstract line 99** — *"Measured over $2{,}880$ carried paths"* →
   *"$2{,}880$ tests over $1{,}680$ distinct carried paths, sampling 60 operations
   per law"*. And **drop the `[EXH-1]` tag from Theorem 3.2**; the sweep is a
   prefix sample, not exhaustive. (Optionally cite R1's exhaustive coverage of
   REV and the funnel closure.)

7. **§6.1 / Deviation 3** — say why the kill is stronger than the pin's form:
   *the carried certificate is a function of the record the checkpoint writes, so
   any two one-step histories writing the same record are indistinguishable by
   construction — at every boundary, under every law. LOSSY against V-CL is
   immediate from what the pin specifies is carried.*

8. **Theorem 5.3** — replace *"By (P1), the set of declarable histories…"* with the
   declaration-closure form (K2 above). The reduction does not use (P1) and saying
   it does understates the result and invites a hunt for an escape that cannot
   exist.

9. **§8, third bullet** — the abstract's "complete family of $512$" should carry
   the in-family quantifier that §5.4 already displays.

10. **§10 / `L5-AMP-EXACT`** — the gate's claim sentence promises more than its
    predicate measures (F7.2). Either check for MIXED tokens on the sums actually
    formed, or narrow the claim to the declared generators.

---

## COMMON GATES

| gate | disposition |
|---|---|
| paper-vs-receipt sweep | **Clean.** Every number I checked in the paper appears in the receipt with the same value; the receipt's own key `"paths_tested"` is more honest than the paper's prose (F6). No number is invented in the paper. |
| scope tags | **Two defects.** `[EXH-1]` misapplied to Theorem 3.2 (F6); "complete" unqualified in the abstract and §8 (F7.1). Elsewhere the variant- and reading-quantifiers are present and correct — §6.4, §8 bullet 2 and Deviation 6 are exemplary. |
| name-blindness | **Maintained.** 0 violations over $6\times4\times120$, reproduced; the negative control is caught (120 violations). The gate is genuinely self-testing. |
| forbidden vocabulary | **Clean.** The only hits in the whole paper are inside the two disclaimer sentences. No spatial, temporal, causal or gravitational reading is made anywhere. |
| deviations complete | **Complete as to what the unit knew.** Ten deviations, all real, all load-bearing; Deviation 4 (support-closure vs amplitude monoid) and Deviation 6 (reading-relativity) are exactly the two a hostile reader would demand. F1 is not a deviation but an error, so its absence is not a completeness failure. |
| mutants / determinism / floats | **Floats: clean** — I found no float in any substantive path and re-derived everything in an independent exact ring. **Determinism: clean** — no wall-clock value in the artifacts. **Mutants: gap** — see F2; the suite cannot catch a sign-convention error in the holonomy. |
| single-threaded | **Clean.** The paper reports its findings as findings; the two mid-unit mutant repairs are disclosed in §10 as a correction rather than smoothed over, which is the honest form. No catalogue of internal review rounds. |

---

## WHAT I COULD NOT BREAK

Recorded so the fixes above are read in proportion. The forest lemma and the
delta-zero theorem are correct and I strengthened rather than dented them. The
cost-vs-generation decoupling is correct and its arithmetic is transparent. The
reduction is correct and is *more* general than claimed. The discriminator table
is exactly right, including the finding that (P1) and (P2) pass at every
committed patch and that the legitimate coarse chart dies by the identical clause
vector — I reproduced the clause vector $(\text{F},\text{T},\text{F},\text{T})$ at
both. The backwards fan-in ($120$ forged against $20$ legitimate) is real. The
amnesty sweep really does have nothing to amnesty. The name-blindness gate is
sound and self-testing. **And the escape question has a negative answer that is
firmer than the paper claims.** The unit's verdict is the right verdict; it is
supported in one place by a number that is not.

---

## REPRODUCTION

R1's code lives outside the repo, at
`…/scratchpad/r1pv/{r1_core,run_a,run_b,run_c,run_d}.py`, imports nothing from
the unit, and is exact throughout. The decisive test is `run_b.py`: build the 512
lifts, compute the loop quantity under both sign conventions, apply random vertex
switchings, and compare. It is four lines of logic and it settles F1 on its own.

**FREEZE-ON-DELIVERY observed.** No repo file other than this one was written; no
git operation was performed.
