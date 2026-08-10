# CR-D — the symmetry-tower limit: four wings

**Status:** GREEN-UNREVIEWED (v14, CR-D; pin `v14/note-cr-batch-pins.md`,
CR-D box, frozen at v14 ledger #30).
**Instrument:** `v14/code/crd_tower_exact.py` — `86 gates, all passed`,
exact arithmetic throughout, artifacts `crd_tower_output.txt` and
`crd_tower_receipt.json`.

---

## The tower, and what a fourth wing does to it

The corpus owns one measured growth that is not a copy of something
smaller: the group tower carried by the wing bases. At two wings the
transport geometry is a group of order 6; at three wings it is a ladder of
named groups topped by an order-15,120 holonomy whose defect subgroup is
$A_7$. This unit takes the tower's first step past three wings. It builds
the four-wing base by the three-wing construction rule read as data,
computes the groups at the rule's own declared completions, and asks the
four questions the pin poses: does the three-wing ladder embed, is there a
four-wing ceiling and is it attained, what is the growth law, and do the
new groups stay in the alternating or linear families.

The answers are, in one line:

```
CRD-TOWER-EXTENDS-<EMBEDS-IN-THE-TOP-RUNG-5-of-5-rungs-0-elements-outside, ATTAINED-AT-15692092416000, ALTERNATING-3-of-4-LINEAR-0-of-4, 3-MODES-COMPLETION-RULE-EMPTY+SPLIT-STRUCTURE-FAILS-AT-1-of-4-RUNGS+LINEAR-RUNG-NOT-REALISED, EXHAUSTIVE-CENSUS-1307674368000-COMPLETIONS-AT-675675-ORBITS>  ||  CRD-TOWER-BREAKS-<3-MODES-COMPLETION-RULE-EMPTY+SPLIT-STRUCTURE-FAILS-AT-1-of-4-RUNGS+LINEAR-RUNG-NOT-REALISED>
```

The three questions the pin asks all answer *extends*. What breaks is not
any of them: it is the rule that selects the reference completion, which
has no solution at four wings at all.

---

## 1. The three-wing recovery, first

Nothing four-wing counts until the three-wing base is re-derived from the
pinned declarations and matches. Every object below is reimplemented — the
carrier and its index, the wing symmetry $P_\pi = \Sigma_\pi\otimes
\Sigma_\pi$, the three declared rotations, the local legs, the setting
family, the frames, the completion-selection rule, the four-clause gluing
predicate and the based holonomy — and nothing is imported from the
committed instrument.

The reimplemented completion rule returns, at three wings, exactly the
completion the pinned receipt declares. The exhaustive completion census
over all $7! = 5{,}040$ label permutations fixing label 0 reproduces the
committed distribution cell for cell. And the transport groups match:
`the four declared-target holonomy orders [1, 1008, 72, 15120], the reference order 2160 and the top defect subgroup 2520`.

| instance | $\lvert\mathrm{Hol}\rvert$ | $\lvert K\rvert$ | the type of $K$ |
|---|---|---|---|
| reference (GHZ) | 2,160 | 360 | $A_6$ on its own 6-point support |
| ord 1 | 1 | 1 | trivial |
| ord 2 | 1,008 | 168 | $\mathrm{GL}(3,2)$, $\mathbb F_2$-linear on the seven non-zero labels |
| ord 3 | 72 | 12 | $A_4$ on its own 4-point support |
| ord 6 | 15,120 | 2,520 | $A_7$ on its own 7-point support |

Rendered from the receipt, as `|Hol|/|K|` in the receipt's own instance
order: `1/1; 1008/168; 72/12; 15120/2520; 2160/360`, over an exhaustive
census of `5040` completions whose defect-order distribution is
`{1: 48, 2: 384, 3: 1728, 4: 1152, 5: 1152, 6: 576}`.

Each name is earned by set equality against a group brute-forced in the
same run, never read off an order.

**One clarification the recovery supplies.** The ladder's `<` orders its
rungs by size; it is not a chain of subgroup containments. Measured as
sets, every rung lies inside the top rung $A_7$, and the intermediate
containments do not hold — $A_4 \not\subset \mathrm{GL}(3,2)$,
$\mathrm{GL}(3,2)\not\subset A_6$. That is exactly the structure the
four-wing test then generalizes.

---

## 2. The four-wing base

The construction rule is generic in the wing count, and at four wings it
forces almost everything: a carrier of $2^4\times 2^4 = 256$
configurations, the wing group $S_4$ acting as $\Sigma_\pi\otimes
\Sigma_\pi$, $3^4 = 81$ settings, $4! = 24$ frames, five legs per frame,
six checkpoints, 144 nodes per setting, and the same four-clause gluing
predicate with a link drawn only where the predicate admits uniquely.
Every local leg is exactly orthogonal and the conjugation law
$P_\pi U_w P_\pi^{-1} = U_{\pi(w)}$ holds at every declared cell.

The choice inventory on the extension is `18 coordinates, 14 forced, 2 free, 1 empty`
(one further coordinate — the wing count — is declared by the pin). The
two free coordinates are the reference preparation's reading and the rest
of the nine-member preparation family; the latter is genuinely
undetermined, because the family's classifier is Cayley's
$2\times2\times2$ hyperdeterminant and its $W$-class weight triples,
neither of which has a unique four-wing analogue. No quantity in this unit
reads any preparation but the reference, exactly as the three-wing ladder
does, so that freedom binds nothing.

### 2.1 The completion rule is empty at four wings

The one *empty* coordinate is the reference completion, and it is the
paper's first result. The pinned rule asks for the lexicographically first
transposition $(i,j)$ of the system labels, $1\le i<j<2^n$, whose
completion $V = H(\psi)\,Q$ has a Born shadow invariant under no
non-identity wing symmetry. At four wings the rule admits
`0 of 105 label pairs`. At three wings the same census admits `6 of 21`.

The mechanism is measured, in both directions and at every cell. When the
preparation's Born shadow is wing-symmetric — the class the declared GHZ
type specifies, whose support labels are pointwise fixed by every wing
symmetry — the shadow of $V$ is invariant under $\sigma_\pi$ exactly when
$\sigma_\pi$ commutes with $Q$, because the shadow's columns are pairwise
distinct. So the rule reduces to pure wing-group combinatorics: it asks
for a label pair whose **setwise stabiliser in the wing group is
trivial**. The stabiliser census over the four-wing pairs is
`{2: 72, 4: 18, 6: 12, 8: 3}` — no pair has a trivial stabiliser, and the
smallest is 2. At three wings six pairs do.

This is a determinate negative, not a licence to choose: the ladder's
reference row has no four-wing analogue by the pinned rule, and none is
invented here. Its scope is stated exactly. The emptiness holds for every
member of the declared GHZ family, all of whose shadows are invariant
under the whole wing group. The alternative, literal-label reading of the
same declaration leaves that class at four wings — its shadow is invariant
under only a proper subgroup of the wing symmetries, the equivalence above
fails there at measured cells, and the rule does return a completion:
`reading A 24 of 24 wing symmetries, equivalence 2415 of 2415 cells; reading B 6 of 24, equivalence 2289 of 2415`.
The reading is therefore reported as binding this negative rather than
hidden.

### 2.2 The census that four wings makes impossible, and the one that replaces it

The three-wing census enumerates $7!$ completions. The four-wing census
would enumerate $15! = 1{,}307{,}674{,}368{,}000$ — and a direct
lexicographic scan is not merely slow: it reaches rank 1,000,000 without
finding a single completion at the maximum defect order.

It is nevertheless exhaustive here, by an orbit count. (The scan's own
scope: `reached rank 1000000 of 1307674368000`.) The defect at $P^*$
depends on the completion $q$ only through $\tau = q^{-1}\sigma q$; as $q$
runs over the permutations fixing label 0, $\tau$ runs over **every**
involution of $\sigma$'s cycle type on the non-zero labels, with equal
fibres. So the exhaustive distribution is obtained by enumerating the
$\tau$ and weighting each by the common fibre:
`1307674368000 completions at 675675 orbits of common fibre 1935360`,
with the product gated against a derived factorial. The same route,
validated against direct enumeration at three wings where both are
affordable, also returns the lexicographically first completion at each
order, so the rule-selected targets are exact and not approximate.

`the maximum defect order at P* is 30` — against 6 at three wings.

---

## 3. The four-wing ladder

At the rule's four declared targets $\{1, 2, 3, 30\}$, at the lex-first
fully symmetric setting and the GHZ reference:

`A1 target ord = 1: |Hol| = 1, |K| = 1, trivial; A1 target ord = 2: |Hol| = 479001600, |K| = 19958400, A_11, the FULL alternating group on its own 11-point support; A1 target ord = 3: |Hol| = 60, |K| = 60, A_5, the FULL alternating group on its own 5-point support; A1 target ord = 30: |Hol| = 15692092416000, |K| = 653837184000, A_15, the FULL alternating group on its own 15-point support`

| target | $\lvert\mathrm{Hol}\rvert$ | $\lvert K\rvert$ | support | the type of $K$ | pointer image | wings inside $\mathrm{Hol}$ |
|---|---|---|---|---|---|---|
| ord 1 | 1 | 1 | — | trivial | 1 | 1 |
| ord 2 | 479,001,600 | 19,958,400 | 11 labels | $A_{11}$ | 24 | 24 |
| ord 3 | 60 | 60 | 5 labels | $A_5$ | 1 | 1 |
| ord 30 | 15,692,092,416,000 | 653,837,184,000 | 15 labels | $A_{15}$ | 24 | 24 |

Rendered from the receipt, as `|Hol|/|K|/support size` in target order:
`1/1/0; 479001600/19958400/11; 60/60/5; 15692092416000/653837184000/15`;
and as `pointer image/wing symmetries inside Hol`: `1/1; 24/24; 1/1; 24/24`.

The supports are not arbitrary. Each non-trivial rung's support is
measured to be exactly a Hamming weight class of the system labels —
`0:None; 11:2; 5:3; 15:1` as `support size:weight threshold` — so the
ord-2 target's eleven points are exactly the labels of weight at least 2,
the ord-3 target's five are the labels of weight at least 3, and the
top rung's fifteen are all the non-zero labels.

**Two identification methods, labelled per group.** $A_5$ and the
three-wing rungs are identified by literal set equality against a
brute-forced alternating group. $A_{11}$ and $A_{15}$ cannot be: a group
of order 653,837,184,000 admits no element-by-element comparison. They are
identified by *containment plus order*, which is a proof of the same set
equality: every generator is measured even, measured to fix label 0 and
measured to fix the complement of the support, so the group lies inside
the alternating group on that support; the order is gated equal to the
derived $\lvert\mathrm{Alt}(\text{support})\rvert$; equality of sets
follows. The cap above which enumeration is refused is printed and gated.

Group orders are computed by two genuinely independent routes wherever
both are affordable — a brute-force closure that builds every element and
a Schreier–Sims chain that builds none — and gated equal at every such
cell. Above the cap only the chain runs, and the receipt says so.

**The split structure does not survive intact.** At three wings every
non-trivial instance satisfied $\mathrm{Hol} = K\rtimes S_3$ with all six
wing symmetries inside. At four wings that holds at the ord-2 and ord-30
targets and **fails at the ord-3 target**, where the geometry equals its
own defect subgroup, only the identity wing symmetry lies inside, and
$\langle K,\text{wings}\rangle$ is properly larger than $\mathrm{Hol}$.

---

## 4. The ladder-extension test

The three wings $A,B,C$ sit inside the four wings $A,B,C,D$ with wing $D$
in the zero state, so the system label $a$ becomes $2a$ and every odd
four-wing label is fixed. The embedding is *constructed*: every element of
every three-wing rung is lifted through that map and sifted through each
four-wing rung's base-and-strong-generating set.

The result: `5 of 5 rungs, 0 elements outside` — the whole three-wing
ladder, $1 < A_4 < \mathrm{GL}(3,2) < A_6 < A_7$, lies inside the
four-wing **top** rung $A_{15}$.

| three-wing rung | order | outside ord 1 | outside ord 2 | outside ord 3 | outside ord 30 |
|---|---|---|---|---|---|
| trivial | 1 | 0 | 0 | 0 | 0 |
| $\mathrm{GL}(3,2)$ | 168 | 167 | 167 | 167 | **0** |
| $A_4$ | 12 | 11 | **0** | 11 | **0** |
| $A_7$ | 2,520 | 2,519 | 2,508 | 2,519 | **0** |
| $A_6$ | 360 | 359 | 357 | 359 | **0** |

Rendered from the receipt, as `rung order:elements outside each of the
four targets in receipt order`:
`1:0/0/0/0; 168:167/167/167/0; 12:11/0/11/0; 2520:2519/2508/2519/0; 360:359/357/359/0`.

The table says precisely what extends and what does not. The ladder
embeds *as a whole, into the top rung* — the same relation the three-wing
ladder has to its own top. It does **not** extend rung by rung: the
three-wing $\mathrm{GL}(3,2)$ has no home in the four-wing ord-2 target,
and $A_6$ and $A_7$ have none below the top. The one exception is
measured too, and its cause is derived here at its own site: the
three-wing $A_4$ also lies inside the four-wing ord-2 rung $A_{11}$,
because $A_4$'s three-wing support $\{3,5,6,7\}$ lifts under $a\mapsto 2a$
to $\{6,10,12,14\}$, every member of which has Hamming weight at least 2
and so lies in that rung's weight-class support. The containment is measured
one-way — the four-wing top rung does not lie inside the lifted
three-wing one — so what is reported is an embedding, not an equality read
in whichever direction happens to pass.

---

## 5. The ceiling

The three-wing ceiling argument has three ingredients, and all three are
re-measured at four wings rather than inherited. Every defect is a
commutator of label permutations fixing label 0, hence an even permutation
of the $2^n-1$ non-zero system labels. Every wing symmetry is measured
even on the labels and measured to fix label 0 — 24 of 24 on both counts.
Every holonomy element is measured to act in product form (system label
permutation) $\times$ (pointer label permutation). Hence

$$\lvert\mathrm{Hol}\rvert \;\le\; \lvert\mathrm{Alt}(2^n-1)\rvert\times
(\text{the measured pointer image}).$$

At four wings that is `|Alt(15)| x 24 = 15692092416000, attained` — the
ord-30 target reaches it exactly.

**The parity hypothesis is a lemma with a boundary.** A wing transposition
moves $2^{n-1}$ labels in $2^{n-2}$ transpositions, so it is *odd* exactly
at $n = 2$ and even for every $n\ge 3$; since transpositions generate, all
wing symmetries are even for $n\ge 3$. The lemma is proved by that count
and measured at $n = 2, 3, 4$. So the ceiling argument holds for every
$n\ge 3$, and at two wings it does not — the two-wing agreement between
the measured maximum and the alternating form is numerical, not an
instance of the theorem, and is reported as such.

Because the ceiling is attained, the maximum over the *declared targets*
is upgraded to the maximum over **all** completions: no completion
whatever can exceed a bound that one of them already reaches.

---

## 6. The growth law, and the families

Three points, all measured by one instrument. Each reaches the value the
ceiling formula gives, but the ceiling *argument* is licensed only at
$n\ge3$:

| wings | system labels | max $\lvert\mathrm{Hol}\rvert$ | $(2^n-1)!/2\times n!$ | ceiling attained | parity hypothesis |
|---|---|---|---|---|---|
| 2 | 4 | 6 | 6 | yes | **fails** |
| 3 | 8 | 15,120 | 15,120 | yes | holds |
| 4 | 16 | 15,692,092,416,000 | 15,692,092,416,000 | yes | holds |

Rendered from the receipt as `wings:maximum`:
`2:6; 3:15120; 4:15692092416000`. The sequence is
`6 -> 15120 -> 15692092416000`, and the closed form
$(2^n-1)!/2\times n!$ matches at all three wing counts — as a *theorem's
instance* at $n = 3, 4$ and as a numerical coincidence at $n = 2$. As an
upper bound the closed form is proved for every $n\ge3$ by the argument of
§5. The ratio from three to four wings is `1037836800`.

**The families.** At four wings the named rungs are `3 alternating, 0 linear`
— $A_5$, $A_{11}$, $A_{15}$, plus the trivial group. This is the
Lie-direction's first datum, and it points away from the linear family:
at three wings the ord-2 target realised the substrate's *own* linear
group $\mathrm{GL}(3,2)$ as a rung, and at four wings no declared
completion realises $\mathrm{GL}(4,2)$. The linear group has not
disappeared — `|GL(4,2)| = 20160, 0 outside the top rung`, every element
of it sifting into $A_{15}$ — but it is a subgroup of the top rung rather
than a rung of its own.

---

## 7. What breaks

Three modes, each computed from a measured table and each naming the gate
that measured it.

1. **COMPLETION-RULE-EMPTY.** The pinned completion-selection rule admits
   nothing at four wings (§2.1). The wing group grows faster than the
   label-pair space can separate it: no pair of the 15 non-zero labels has
   a trivial setwise stabiliser in $S_4$.
2. **SPLIT-STRUCTURE-FAILS-AT-1-of-4-RUNGS.** The three-wing law
   $\mathrm{Hol} = K\rtimes S_n$ with every wing symmetry inside fails at
   the ord-3 target (§3).
3. **LINEAR-RUNG-NOT-REALISED.** $\mathrm{GL}(3,2)$ was a realised rung;
   $\mathrm{GL}(4,2)$ is not (§6).

None of the three is one of the pin's three questions, and the two
verdicts are emitted side by side for that reason: the tower *extends* in
embedding, ceiling and families, and the *construction rule* around it
breaks.

---

## 8. Scope, and what this does not decide

Everything above is a statement about one declared finite model at its
declared scope, with nothing claimed about nature.

- The four-wing groups are computed at **one** setting (the lex-first
  fully symmetric one) and **one** preparation (the GHZ reference), which
  is the three-wing ladder's own scope. The four-wing setting sweep is not
  run.
- The completion census is exhaustive at $P^*$, the lex-first
  non-identity wing symmetry. The full profile over all 24 wing symmetries
  is not censused.
- The maximum holonomy order is exact over all completions **because** the
  ceiling is attained; without attainment it would be a maximum over the
  declared targets only.
- The ladder-extension result is about the declared wing-$D$ embedding.
  Other embeddings of three wings into four are conjugate under the wing
  group but are not separately censused.
- Nothing here bears on the physical interpretation of the tower. It is a
  measured growth law for a group-valued invariant of a finite transport
  construction, and the growth is faster than any Lie-type family: the
  rungs are alternating groups on $2^n-1$ points.
- GEN's $\psi$-independent defect form and PSI's one law
  $D = [P_\pi^{-1}, u]$ are re-evaluated at four wings and hold at every
  cell — but they are **analytically forced** by the declared construction
  and are reported as disclosures, not as must-pass results. What is
  contingent beside them, and is gated, is that every defect is readable
  as a carrier permutation at all and that its pointer part is the
  identity.

---

## 9. The instrument

`86 gates, all passed`, with `90 declared mutants; 5 of 86 gates never falsified`
and anchors in three kinds — `6 verbatim-text, 7 file-byte, 24 path-value`.
Exact arithmetic throughout, enforced by an AST
scan of the source: no float literal, no true-division operator, no banned
import. Anchors arrive in three kinds and in this order — verbatim-text
context windows quoted from the three-wing paper, this unit's pin and the
runbook, each bound to a named consumer gate; file-byte anchors on the
pinned receipts and the two construction-recipe artifacts; and path-value
anchors, which bind the (path, value) pair rather than the file alone.

Controls: the two-wing point recovered by the same generic machinery and
gated against the committed two-wing values; the three-wing ladder
recovered before any four-wing number counts; a symmetry self-test
evaluated fresh outside the memo; base-node and relabelling invariance of
the holonomy order; a connective-witness gate whose death certificate is
the measured delta of the alternative link-drawing connective; and
negative controls in which the equivariant completion collapses the
geometry.

The verdict string is derived inside a gate from the measured counts and
compared for complete string equality against an independent
reconstruction built from the receipt object alone, by a function sharing
no code and no input with the builder. Every segment is shown flippable at
its own measurement, and both pre-registered heads are reachable from the
same derivation.
