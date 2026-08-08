# TB3 — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens.
**Object reviewed (SHA-256 verified before reading, all four exact):**

| artifact | declared | computed |
|---|---|---|
| `v13/paper-tb3-third-base.md` | `0a9c5dff0e92` | `0a9c5dff0e92` ✓ |
| `v13/code/tb3_third_base_exact.py` | `0fe72a05970b` | `0fe72a05970b` ✓ |
| `v13/code/tb3_third_base_output.txt` | `a14684073857` | `a14684073857` ✓ |
| `v13/code/tb3_third_base_receipt.json` | `3cd7981d173e` | `3cd7981d173e` ✓ |

**Method.** Independent rebuild of the three-wing base from the paper's
declarations, in my own scratchpad, in my own data structures (matrices as
`{(i,j): Fraction}` dictionaries rather than the delivery's column-dict class);
nothing of `tb3_third_base_exact.py` imported. Background read: PSI, COC, XBA,
BRG terminal papers; RUNBOOK §13–§15 with all addenda; the pin and the frozen
protocol.

**Recomputations performed: 129.** **Numerical discrepancies found: 0.** Every
table, count, order and census in the paper reproduces exactly, including
1,226,304 / 62,784 / 5,040 / 15,120 / 2,160 / 343,296 / 216,720 / 600 and the
two-wing control's 8/13/7/6/364/6. The findings below are therefore *not*
arithmetic findings. They are findings about what the numbers mean, what the
verdict strings say they mean, and what the unit did not notice.

---

## MAJOR

### M1 (K2). A2's headline counts are analytically forced by the comparator's own definition, and the pre-registered trichotomy has exactly one reachable branch.

`World.defect_measured(pi)` returns `conj.T() @ self.u` with
`conj = P u P⁻¹`. Every object in this base is measured exactly orthogonal, so
`conj.T() = conj⁻¹`, and therefore

$$D_\pi \;\equiv\; (P u P^{-1})^{-1} u \;=\; P\,u^{-1}P^{-1}u \;\equiv\; F_3 .$$

Not at this base — **for every invertible orthogonal `u` and every `P`.** I
verified it on 200 random pairs (`P` a random permutation matrix of arbitrary
order, `u` a random rational orthogonal matrix built from a signed permutation
and a Givens rotation, dimension 6, nothing to do with TB3): **0 deviations.**
"F₃ reproduces the measured defect at 54 of 54" is an identity, not a
measurement.

The rest follows by arithmetic. $F_1 = F_3 \iff P u^{-1}Pu = P u^{-1}P^{-1}u
\iff P = P^{-1}$; $|\{\pi \in S_3 : \pi^2 = 1\}| = 4$; $4 \times 9 = 36$. The
paper's "**36**, precisely the involution cells" is $4\times 9$, computed in
advance. I confirmed both implications cell by cell.

Consequently:

- **`HOLDS-VERBATIM` is algebraically unreachable at $S_3$** — it requires
  $F_1 = D$ at every cell, i.e. every element of $S_3$ to be an involution.
- **`FAILS` is algebraically unreachable** — it requires no form to reproduce
  $D$ at some cell, but $F_3 \equiv D$ always.
- **`GENERALIZES` was fixed before the base was built.**

This is precisely what RUNBOOK §14's #208 addendum forbids: *"Analytically-forced
clauses (true by algebra for every input) are disclosures, not must-pass
gates."* Gate `TB3-A2` is a must-pass derivation gate whose branch is forced.
The unit applies the correct standard one section later — §4.3 enters the
cocycle as a disclosure "because it is forced by algebra in one line" — and does
not apply it to the identity that carries the axis's headline.

What *is* free in A2, and what should carry the axis: $F_2 = F_3 \iff P^2$
centralises $u$. I verified this equivalence at all 54 cells; the measured 36 is
a genuine measurement about which $P^2$ commute with the preparation leg. And
§4.4's generation result (below) is free. Neither is where the verdict weight
sits.

**Repair.** (a) State in §4.1 that $D_\sigma = [\sigma^{-1},u]$ follows in one
line from the defining equation $\sigma.u\,\sigma^{-1} = u\,D_\sigma^{-1}$, and
re-enter the 54/36/36 table as a **disclosure**. (b) Record that
`HOLDS-VERBATIM` and `FAILS` were unreachable at $S_3$ — a pre-registration
whose alternatives are impossible is not a pre-registration. (c) Move A2's
must-pass weight onto $F_2$-vs-$F_3$ and §4.4.

### M2 (K2, the naming adjudication). `GENERALIZES` over-reports; the honest verdict is that the law holds verbatim as a commutator law and only its *index* moves.

Three things decide this, and the paper has all three in hand.

1. **The set of defects is unchanged.** $\pi \mapsto \pi^{-1}$ is a bijection of
   $S_3$, so $\{[\pi,u] : \pi\in S_3\} = \{[\pi^{-1},u] : \pi\in S_3\}$. The
   correction moves *which symmetry is paired with which defect*, not which
   defects exist. Every downstream object in this paper — the
   defect-generated subgroup, the holonomy group, the ord profile — is built
   from the *set*, and is therefore identical under either reading. The
   "correction" is invisible to everything the unit measures except the
   cell table.
2. **The index is a convention, not a measurement.** $D_\sigma$ is fixed by
   *where $D$ is placed* in $\sigma.u\,\sigma^{-1} = u\,D_\sigma^{-1}$; the
   opposite placement ($= D_\sigma u$) yields $[u^{-1},\sigma^{-1}]$ instead.
   Appendix deviation 6 says "the convention is fixed by the *measurement*" —
   this inverts the dependency. The convention is inherited (it is the placement
   that reproduces PSI's committed form at involutions, which is the right
   consistency check and should be stated as such), and the index at $\pi^{-1}$
   is its consequence.
3. **PSI never claimed the four-factor form beyond involutions.** PSI §6.1:
   *"$P_W$ is measured to be an involution … **Therefore** the four-factor
   product that GEN and this unit both call the non-equivariance defect **is**
   the group commutator."* The committed claim was already conditional on
   $P^2=1$. TB3 refutes a universalisation the committed paper did not assert.

The paper's own §10 states the honest position exactly — *"the law survives as a
law about commutators and centralisers and dies as a law about numbers"* — and
the verdict string contradicts it by naming the law's *form* as the thing that
changed. The four-factor writing was an involution artifact: true, and the
paper says it well. But "an artifact of the writing was corrected" is not
"the law generalizes".

**Repair.** Either rename to
`TB3-ONE-LAW-HOLDS-VERBATIM-AT-⟨the commutator reading; the index at P⁻¹ forced
by the inherited chart-action convention; the four-factor writing an involution
artifact⟩`, or keep `GENERALIZES` with a qualifier that names *what* generalises
— the index, not the law — and states that the committed writing was never a
claim at non-involutions.

### M3 (K3). The "computed refinement" is not discriminated from a rival criterion by any instance this base offers, and §10 states it as settled.

At the five declared instances the **normaliser verdict is analytically forced
at three of five**:

| instance | \|Hol\| | cent | norm | forced? | why |
|---|---|---|---|---|---|
| declared base, fully symmetric | 2160 | 1/6 | 6/6 | **forced** | $\langle\text{wings}\rangle \subseteq \mathrm{Hol}$ — a group is normalised by its own subgroups |
| equivariant control | 1 | 6/6 | 6/6 | **forced** | trivial group |
| partially symmetric | 6 | 1/6 | 2/6 | free | — |
| asymmetric | 1 | 6/6 | 6/6 | **forced** | trivial group |
| W-class prep | 6 | 1/6 | 2/6 | free | — |

(All recomputed. $\langle\text{wings}\rangle\subseteq\mathrm{Hol}$ at the
declared base verified directly.)

Now the rival. **"The cocycle closes iff the chart-generating group *contains*
or *centralises* the level-1 holonomy"** agrees with the measured closure at
**5 of 5** on identical data. So does "$|\mathrm{Hol}|=1$ or
$\langle\text{wings}\rangle\subseteq\mathrm{Hol}$". The five instances cannot
tell these apart from "normalises".

K3 asks for a normalising-but-escaping probe. I hunted for the prior object —
an instance where $\langle\text{wings}\rangle$ **normalises** $\mathrm{Hol}$
**without containing it and without centralising it**, the only kind of instance
that could separate the criteria. **Swept 51 instances** (psi-G1 at all 27
declared settings, plus the other 8 preparations at three settings each, at the
declared $Q$): **zero hits.** The complete observed profile space is

```
(cent, norm, contains, |Hol|)   count
(6, 6, False, 1)                 21     trivial: normalises forced
(1, 6, True,  2160)               5     containment: normalises forced
(1, 2, False, 6)                 16     non-normalising
(2, 2, False, 4)                  7     non-normalising
(1, 1, False, 2)                  1     non-normalising
unreadable holonomy               1
```

**On this base, "normalises" is extensionally "contains-or-centralises".** It is
never non-trivially satisfied anywhere I could reach. The refinement is not
refuted — it is *unidentified*.

**On whether COC is superseded, and whether "measured FALSE" overclaims.**
It does not overclaim. COC §5 is explicit that only sufficiency is forced and
that *"the necessity direction is **not** forced … Whether an admissible
triangle realises it is a measurement"*, and COC §13.2/§13.7 scope both censuses
to its two declared atlases. TB3 §5.2 quotes this fairly and §11.5 scopes its
own refinement to five instances. **There is no contradiction between the two
units**, and TB3's phrasing is accurate. What *is* superseded is narrower and
should be routed as such: COC's **displayed biconditional** — stated unscoped in
its abstract and again at §5 — can no longer stand as displayed, because a third
atlas closes without centralisation. That is an errata-class corpus action
(retro-scope COC's display to "at the two declared atlases"), and TB3 identifies
the need without routing it.

The overclaim is elsewhere and it is §10: *"COC's criterion needed one word
changed: **normalises**, not **centralises**."* Stated in the verdict section as
a settled correction, on evidence that is three-fifths forced and that does not
identify the replacement.

**Repair.** (i) Split the normaliser column into forced/free. (ii) State the
rival criterion and that the base does not separate them. (iii) Scope §10 to
match §11.5, or restate the refinement as *"normalisation is the weakest
condition the telescoping argument supports; at every instance measured it is
satisfied only by containment or triviality, so the biconditional's necessity
direction remains open."*

### M4 (K2, cross-unit coherence). TB3 reopens BRG's live cells at the bridge primes 5 and 7, natively, and does not notice.

Recomputed factorisations of the measured holonomy orders:

$$1008 = 2^4\cdot3^2\cdot\mathbf{7},\qquad
15120 = 2^4\cdot3^3\cdot\mathbf{5}\cdot\mathbf{7},\qquad
2160 = 2^4\cdot3^3\cdot\mathbf{5},\qquad 72 = 2^3\cdot 3^2 .$$

BRG §9.1's theorem is prime-general and carries **no dihedral hypothesis**:
$\mathrm{hom}(\mathbb Z/q, G)$ is trivial $\iff q\nmid |G|$ (Lagrange one way,
Cauchy the other, swept over a deliberately non-dihedral zoo, 189 cells, 0
failures). Applied to TB3's groups it yields, immediately: **non-trivial
$\mathbb Z/5\to\mathrm{Hol}$ and $\mathbb Z/7\to\mathrm{Hol}$ at the ord-6
target; non-trivial $\mathbb Z/7\to\mathrm{Hol}$ at the ord-2 target; non-trivial
$\mathbb Z/5\to\mathrm{Hol}$ at the declared reference.**

BRG §9.5 states its EMPTY verdict at exactly this strength and says outright
that *"it is false one scope out"*: at GEN's twelve rebuilt classes the primes
are $\{2,3,5,7\}$, of which **5 and 7 are admissible on the deformation side** —
which is where BRG's §8.3 FOUNDs and its three live cells sit. TB3 puts those
two primes into a transport holonomy group **at the programme's own new base**,
by construction rather than by scope extension. That is a live-cell event and it
is the single most consequential downstream fact this unit produces.

The paper mentions BRG **nowhere**; the strings `BRG`, `prime`, `coprime`,
`bridge` do not occur in it, and no holonomy order is factored.

Second, symmetrically: BRG §9.2 derives $|\langle W,D\rangle| = 2\,\mathrm{ord}(D)$
from *two* hypotheses — $W^2=1$ and $G=\langle W,D\rangle$ generated by **one**
involution and **one** defect — and concludes it is *"a theorem about the
commutator law's entire group family … covering every base the corpus builds
under that law, including ones not yet prepared."* At three wings both
hypotheses fail (the symmetry group is $S_3$; the geometry is generated by six
defects and six symmetries). **BRG's theorem is not contradicted — its stated
reach is now bounded, and TB3 is the instance that bounds it.** A1's "0 of 4"
is exactly the measurement that shows BRG §9.2's universal quantifier was over
two-wing bases. Neither implication is drawn.

**Repair.** A cross-unit subsection: factor the four holonomy orders, name the
groups (M5), and state (a) BRG's coprimality theorem applies unchanged and
delivers live forward cells at $q\in\{5,7\}$ at this base; (b) BRG §9.2's family
theorem is scoped to involutive-exchange (two-wing) bases, with TB3 as the
witness that the scope is not vacuous.

### M5 (K1, structurally load-bearing for K2). The groups are unnamed, and the one name the paper does use makes a §10 sentence false.

Identified by element-order profile plus faithful transitive constituent, all
recomputed:

| target | $K=\langle D_P : P\in S_3\rangle$ | identification | $\mathrm{Hol}$ |
|---|---|---|---|
| ord 2 | 168, profile $\{1{:}1,2{:}21,3{:}56,4{:}42,7{:}48\}$, faithful on 7 points, simple | $\mathrm{PSL}(2,7)\cong\mathrm{GL}(3,2)$ | $1008 = \mathrm{PSL}(2,7)\rtimes S_3$ |
| ord 3 | 12, profile $\{1{:}1,2{:}3,3{:}8\}$, faithful on 4 points | $A_4$ | $72 = A_4\rtimes S_3$ |
| ord 6 | 2520, profile $\{1{:}1,2{:}105,3{:}350,4{:}630,5{:}504,6{:}210,7{:}720\}$, faithful on 7 points, perfect | $A_7$ | $15120 = A_7\rtimes S_3$ |
| reference $Q$ | 360, profile $\{1{:}1,2{:}45,3{:}80,4{:}90,5{:}144\}$, faithful on 6 points, perfect | $A_6$ | $2160 = A_6\rtimes S_3$ |

**All four are split**, measured: $K \trianglelefteq \mathrm{Hol}$,
$K\cap\langle\text{wings}\rangle = 1$, $|K|\cdot 6 = |\mathrm{Hol}|$. The paper
measures normality and the order factorisation but never measures or states the
*complement*, which is exactly what promotes "$2160 = 6\times360$" from an
extension to a **semidirect product**. The unit's claim is weaker than its data.

And the misnomer. **$K$ is not the commutator subgroup of $\mathrm{Hol}$.**
Recomputed derived subgroups:

$$|[\mathrm{Hol},\mathrm{Hol}]| = 36,\ 504,\ 1080,\ 7560
\quad\text{against}\quad |K| = 12,\ 168,\ 360,\ 2520 .$$

$[\mathrm{Hol},\mathrm{Hol}] = 3|K|$ in every case — index 2 in $\mathrm{Hol}$,
forced by $\mathrm{Hol}/K \cong S_3$ having abelianisation $C_2$. (That
regularity is itself a result the paper is leaving on the table.) The paper
calls $K$ "the commutator subgroup" in the A1 table header, in §4.4's table, and
in §10's summary sentence. §4.4 defines the notation inline, so §4.4 is
defensible; the A1 column header is bare; and **§10's sentence — "the geometry
is generated by the commutator subgroup together with the symmetry group, of
which it is the normal part" — is false on the standard reading**, the derived
subgroup having index 2 and not index 6.

**Repair.** Rename throughout to "the defect-generated subgroup
$K=\langle D_P : P\in S_3\rangle$"; add the four isomorphism types, the measured
splitting, and the measured $[\mathrm{Hol},\mathrm{Hol}] = 3|K|$.

---

## MODERATE

### m6 (K2/K4). §4.4 and §5.2 are the same measured fact, and joining them answers the question the pin asks.

"$|\mathrm{Hol}| = 6\times|K|$" (§4.4) and "the level-1 holonomy group
**contains all six wing symmetries** … the escape route is shut not by
centralisation but by **containment**" (§5.2) are one fact reported twice, in
two axes, with no cross-reference. $\langle\text{wings}\rangle\subseteq
\mathrm{Hol}$ is what produces both the index-6 factorisation and A3's closure.

Joined, it answers *"what does the wing group's entry as a factor MEAN"*
plainly, and the paper never says it: **this holonomy group is not a curvature
group.** It contains the atlas's own relabelling group, because the
identification links transport *by* those relabellings — a loop that crosses a
chart boundary carries $P_\pi$ itself. So $\mathrm{Hol}$ is a **gauge-inclusive
holonomy**: $K$ is the curvature part, and the $S_3$ quotient is the relabelling
group, present in the geometry because the loop space traverses identification
edges. That is why "$4 = 2\times2$" was invisible at two wings (§4.4 sees this),
and it is why the dihedral law had to fail rather than merely happening to.
Stated at measured strength this is the unit's cleanest structural result and it
is currently split across two sections as two separate observations.

### m7 (K2/K1). The generation claim is scoped in §3.2 and unscoped in §4.4 and §10.

$\langle K, \text{wings}\rangle = \mathrm{Hol}$ holds at **3 of 4** A1 targets.
At the ord-1 target $|\mathrm{Hol}| = 1$ while $\langle K,\text{wings}\rangle =
6$ — recomputed; the receipt's own row records
`the_geometry_equals_commutators_and_wings: false`. §3.2 says "at three of the
four targets" and is correct. §4.4's table row ("generated by the commutators
**and** the wing symmetries — **yes**") and §10's summary carry no scope tag.
RUNBOOK failure catalogue, #40 F1/F2: *scope tags at the claim, not just the
receipt.*

### m8 (K1/K5). §3.2's "different cotree" claim is measured false at 1 of 4 targets by the unit's own receipt.

§3.2: the second route is "a depth-first tree in the reversed link order —
**measured to have a different cotree**, hence different generators and different
loops". The receipt's A1 row at the ord-1 target records
`different_cotrees: false`; I recomputed identical tree-edge sets. At that
target the two "routes" are one computation up to the side of multiplication.
The conclusion is unaffected (the group is trivial), but the claim is stated
unscoped and the row is not disclosed — deviation 7 discusses the route redesign
without it.

### m9 (K1/K5). §11.8's "two independent routes … on every census" does not hold for the completion census, and the two objects are related by an algebraic identity.

The 5,040-completion census is computed by the **label route only**; the matrix
route runs at the **6 lex-first representatives** (0.12%). §3.1's body text is
honest ("agree at every *sampled* order"); §11.8's non-claims sentence is not.

Worse for RUNBOOK §13's #234 addendum: the label route computes
$A = \sigma^{-1}q^{-1}\sigma q$, while the matrix route yields
$B = \sigma q^{-1}\sigma^{-1}q = \sigma A^{-1}\sigma^{-1}$, so
$\mathrm{ord}(B) = \mathrm{ord}(A)$ is **forced**. Only orders are compared, so
the agreement is an identity — *"a pair related by an algebraic identity is one
route."* What the matrix route *does* independently confirm is real and worth
saying: that the $64\times64$ defect is a permutation at all, and that $H(\psi)$
cancels because psi-G1 is $S_3$-invariant. That is not a second route to the
census.

### m10 (K5). The receipt carries a field asserting the opposite of the unit's own headline, unlabelled.

`tables.a1_ord_sweep.the_order_is_a_function_of_ord_at_P_star_alone: **true**`,
while the same receipt's `thesis` says *"the order is not a function of
ord([P,u]) at one symmetry"* and §3.3/§7 say the same. The field is computed
across the four targets, whose defect orders are **distinct by construction**, so
it is `true` vacuously — §7 says a lazy test of S7 "would have passed
vacuously", and the receipt contains exactly that lazy test with no marker. Not
gated, so no gate is false; but a successor unit reading the receipt would take
it as a positive result for the statement this unit refutes.

### m11 (K4). The GHZ/W contrast is confounded with the wing stabiliser, and the control that decides it is in the paper's own table, unused.

Recomputed, at identical declarations:

| member | class | wing stab. | Born-shadow stab. | $\lvert\mathrm{Hol}\rvert$ |
|---|---|---|---|---|
| psi-G1/G2/G3 | GHZ | 6 | 6 | 2160 |
| psi-W1 | W | 2 | 2 | 6 |
| **psi-B** | **BISEP** | **2** | **2** | **6** |
| psi-W2 | W | 2 | 2 | 4 |
| psi-P | PRODUCT | 2 | 2 | 2 |
| psi-W3 | W | 1 | 1 | 1 |

Among the four members with Born-shadow stabiliser 2, the holonomy orders are
$6, 6, 4, 2$ — not a function of the entanglement class **and not a function of
the stabiliser either**. The only clean separation the table supports is
stabiliser 6 (all three GHZ, 2160) against stabiliser $\le 2$ (everything else,
$\le 6$) — and §2.5 discloses that no rational W state can have stabiliser 6, so
the design confounds class with stabiliser by construction.

**psi-B, biseparable, stabiliser 2, $|\mathrm{Hol}| = 6$ — identical to psi-W1's
— is the control that settles this**, and it sits in §6.2's own table without
being read. §11.6 concedes "the comparison is not at matched stabiliser", but
the abstract, §6.2's headline claim ("the sharpest form in which the GHZ/W
distinction has appeared in this programme") and the receipt's `thesis` all state
the contrast as GHZ-versus-W.

**Repair.** Restate §6.2 as a **stabiliser** contrast with the entanglement class
as a disclosed confound, using psi-B as the separating control; keep §6.3's
witness pair as the matched-coordinate claim — it *is* at matched coordinates
and it survives intact.

### m12 (K4). §6.2's mechanism sentence is refuted one subsection later by the unit's own witness.

*"The entanglement class enters the geometry through the symmetry of the Born
shadow, and through nothing else the predicate can see."* The clause "the
predicate can see" makes it literally defensible, but the natural reading is
refuted by §6.3: psi-W1 and psi-W4 have the identical Born shadow and the
identical admission table (recomputed, cell for cell) and different holonomy.
The sentence should say what it means: the predicate reads Born data only, so
**the drawn graph** is a function of the Born shadow; **the holonomy** is not,
and the witness pair is the proof.

### m13 (K4). The "not a permutation group" phenomenon is one class further out than PSI's, and is mischaracterised as a reproduction of it.

§6.3: *"This reproduces PSI's mechanism at $S_3$ from a native construction."*
PSI's readability failure is out of the **signed-permutation** class (PSI §6.4:
GEN's invariant is "undefined where the product is not a signed permutation").

I measured psi-W4's 14 unreadable cycle-basis generators. **None is a signed
permutation. None is even monomial.** Each has 32 columns of support 4, with
entries in $\{\pm 1/81, \pm 4/81, \pm 4/27, 16/27, -7/9\}$. So this is not a
sign/gauge-adjacent collapse; it is a genuine **delocalisation** of the loop
transport — a strictly stronger departure than PSI's, at a class the paper never
names. Additional measured structure the paper does not report: all 14 are
exactly orthogonal and **all 14 have order exactly 2**.

Whether the generated matrix group is finite is undetermined — my closure
exceeded $2\times10^5$ elements without terminating — so §11.7's "not computed"
is defensible. "Reproduces PSI's mechanism" is not, and the class actually left
is a one-line measurement.

Related, presentational: the abstract's list *"the W-class members 6, 4, 1 and a
group that is not a permutation group at all"* puts three group orders and one
**absence** in a single enumeration, read as a four-point contrast. §11.7
discloses the absence; the abstract and the receipt `thesis`
(`(6,4,1,None)`) do not carry it.

### m14 (K3). The two escaping instances are one phenomenon counted twice.

§5.2 and §8.2 present "two instances escape, at 62,784 triangles each" as A3's
negative control with teeth. Recomputed, the partially-symmetric setting and the
W-class preparation agree on: charts (36), seeds (6), links (90),
triangles (343,296), escapes (62,784), $|\mathrm{Hol}|$ (6), centralising (1/6),
normalising (2/6) — **and on the full defect multiset** (identical counter over
all 343,296 triangle defects). Their holonomy groups differ as sets of
permutations, so they are not literally one instance; but **every quantity the
control reports is identical.** §5.2 diagnoses the shared mechanism ("both of
which have exactly two of the six symmetries available") without drawing the
consequence: the control has one independent tooth, not two.

### m15 (K5). Clause 1 is analytically vacuous, not "measured inert".

§2.8 reports all four clauses' drop-effects and concludes the three non-leg-key
clauses are "measured inert, **their content already implied by it**". For
clause 1 (the $j_0$ filter) that diagnosis is wrong: $P_\pi[0] = 0$ for **every**
$\pi\in S_3$ by construction — the wing permutations fix the all-zeros
configuration — so clause 1 can never reject a candidate at **any** base of this
construction. Recomputed. Its inertness is not implied by clause 2; it is
forced. §2.8's framing ("That is a fact about this base") understates a
structural vacuity as a contingency. Deviation 9's re-targeting of the
clause-dropping mutant is correct and unaffected.

---

## MINOR / SCOPE

- **m16 (K5).** §8.2's control map assigns the two-wing run as A1's positive
  control. The control anchors defect orders **1 and 3**; A1's claims are at
  orders **1, 2, 3 and 6**, including the $|\mathrm{Hol}| = 1008$ claim at
  order 2. Deviation 3 says "no order-2 claim is made", which is true of the
  *control* and false of *A1*. I confirmed the two-wing species realises only
  orders $\{1,3\}$, so the limitation is real and correctly diagnosed; the
  control map should say which A1 rows it does and does not reach.
- The paper's disclosure discipline is, elsewhere, unusually good: §2's freeze
  gate explicitly disclaims what an in-run ordering measurement can establish;
  §4.3 enters the cocycle as a disclosure; §11.2–§11.8 are accurate; §2.5's
  "there is no fully $S_3$-invariant rational W state" is exactly the kind of
  self-incriminating disclosure that makes a paper trustworthy. M1 and M11 are
  failures to apply the paper's *own* standard, not the absence of one.

## CONFIRMATIONS (independently recomputed, 0 discrepancies)

Base: carrier 64; wing group order 6, non-abelian, orders $\{1,2,3\}$; settings
$3/18/6$ by stabiliser; $P_\pi U_w P_\pi^{-1} = U_{\pi(w)}$ at 54/54;
distinct-wing legs commute 54/54; rotations and legs exactly orthogonal;
$Q = (0,3,2,1,4,5,6,7)$ from the declared rule; $V$ orthogonal with $Ve_0=\psi$.
**A1:** census 5,040; distribution 48/384/1728/1152/1152/576; max 6 at $P^*$ and
7 over all of $S_3$; the six lex-first $Q$; $|\mathrm{Hol}| = 1, 1008, 72,
15120$; links/rank 99/70, 150/121, 111/82, 111/82; routes equal as sets at all
four; dihedral 0 of 4. **A2:** 54 cells; $F_1/F_2/F_3$ at 36/36/54; pointer
splits 36/54/54; involution cells 36/36/36; $E_P=\mathbf 1 \iff \psi$
$P$-invariant, 0 deviations; cocycle 0 deviations; reconstruction 0 deviations;
$K = 360$, normal, $|\mathrm{Hol}| = 2160 = 6\times360$. **A3:** all five
instances — charts 36/6/36/36/36, seeds 6, $|\mathrm{Hol}|$ 2160/1/6/1/6,
triangles 1,226,304 / 600 / 343,296 / 216,720 / 343,296, escapes
0/0/62,784/0/62,784, centralising 1/6/1/6/1, normalising 6/6/2/6/2; criteria
4/5 and 5/5. **A4:** all nine members' links/rank/$|\mathrm{Hol}|$ including
psi-W4's 47/61 readable generators; the exhaustive 36-pair census with exactly
two Born-shadow-sharing pairs and the single witness (psi-W1, psi-W4).
**A5:** $(30,150,121)$; S3 at 27/27. **Controls:** §8.3's 150/121/2160,
99/70/1, 111/82/18 (at $Q=(0,2,1,3,4,5,6,7)$), 75/46/1; the two-wing control at
8/11/5/4/52/1 and 8/13/7/6/364/6, and the order-2 unreachability.

---

## GRADE

# ACCEPT-WITH-FIXES

**Why not REJECT.** 129 independent recomputations, **zero** numerical
discrepancies. No false theorem, no false number, no gate carrying a positive
claim it cannot support, no census that fails to reproduce. The unit's central
scientific results — the dihedral law's failure at three wings, the
gauge-inclusive semidirect structure of the holonomy, the fixed-Born-shadow
witness, COC's necessity direction refuted — are all real, all reproduced, and
all correctly bounded in §11. Nothing here requires the instrument to be re-run.

**Why not ACCEPT.** Five findings change what a reader takes away.
**M1**: A2's headline is an algebraic identity presented as a blind three-way
measurement, with two of three pre-registered branches unreachable — a §14/#208
violation the paper avoids two pages earlier. **M2**: the verdict string
`GENERALIZES` names the law's form as the thing corrected when the whole content
is an inherited index convention, and the paper's own §10 says so better.
**M3**: the "computed refinement" is forced at three of five instances and
extensionally indistinguishable from a rival across 51 further instances I swept,
yet §10 states it as a settled correction. **M4**: the unit's most consequential
downstream fact — bridge primes 5 and 7 dividing a natively constructed holonomy
order, reopening BRG's live cells — is neither computed nor mentioned.
**M5**: "the commutator subgroup" is not the commutator subgroup, which makes a
§10 sentence false on the standard reading, while the true structure (four named
groups, four measured splittings, $[\mathrm{Hol},\mathrm{Hol}] = 3|K|$) is
stronger than what is claimed.

All five are repairable in the paper, plus one added disclosure gate (M1), one
added forced/free split and rival-criterion statement (M3), one added cross-unit
subsection (M4), and one renaming with the splitting and derived-subgroup orders
recorded (M5). The measurements stand.
