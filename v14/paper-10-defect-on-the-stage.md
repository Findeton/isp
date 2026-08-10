# R4 — the QFT rung: the defect on the stage

**Status:** `REPAIRED-PENDING-VERIFICATION` — delivered against the frozen
pin, attacked by a three-lens hostile panel (3 x ACCEPT-WITH-FIXES), adjudicated,
and repaired against the binding orders R-R4-1 through R-R4-12. Verified to run:
two plain runs byte-identical, every gate passed, every declared mutant dead at
its declared target, the falsification self-test fatal and writing nothing.
Awaiting adjudicator verification. Pin: `v14/note-r4-qft-pin.md`.

## One Lattice Size Admits a Local Declared-Indivisible Family, and On It the Defect Is Present

**Unit:** R4 (the QFT rung), v14.
**Instrument:** `v14/code/r4_defect_stage_exact.py`.
**Artifacts:** `v14/code/r4_defect_stage_output.txt`,
`v14/code/r4_defect_stage_receipt.json`.
**Inheritance, hash-verified at run time and by no other route:** the seed is
the composition defect $\Delta^{B}$ of `v12/paper1-composition-defect.md`
(`81bdab5673fb`) with the exact-field recipes of `v12/paper1_code/exact.py`
(`8e90f6435922`); the stage is the record layer's declared site lattice,
`v13/code/ha_successor_receipt.json` (`542b8735daf0`), which supplies the
spatial dimension, the link set and the chart group as anchored values; the
locality criterion is ported from the terminal manifold receipt
`v14/code/r2_manifold_receipt.json` (`08b2140f46ae`); the pin is
`v14/note-r4-qft-pin.md` (`1582cea5df51`). Every object below is
**reimplemented** from those definitions; nothing is imported from any other
unit.
**Anchors are (path, value) pairs and (context, consumer) pairs, not only file
bytes:** 5 file-bytes anchors, 10 path-value anchors and 9 verbatim-text
anchors — the verbatim windows evaluated before the byte anchors, each bound to
the named gate that consumes it, each a context window rather than a fragment.
**Runtime inputs:** the five hash-pinned sources above, plus exactly one file
read as the *object under test* — this paper, which the delivery run reads and
gates its own numeric claims against, and which cannot be pinned against itself.
Both lists are enumerated and gated. No ledger, no status board, no other
unit's working file.
**Exact arithmetic only:** the field is $\mathbb{Q}(\zeta_8)$ carried as integer
coefficient 4-tuples over a positive integer denominator, reduced modulo
$\Phi_8(x)=x^4+1$; the representation is canonical, so tuple equality is field
equality. An AST scan of the instrument's own source and a recursive type scan
of the emitted receipt are gates.

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field, and the complete string —
head included — is compared for equality against an *independent
reconstruction* that derives the head by its own copy of the head law, reads
only the serialized receipt, and shares no helper, no input and no typed value
with the builder:

```
R4-DEFECT-PRESENT<DEFECT=588-OF-3364-PAIRS-AT-MAXIMAL-TRANSPORT-FULL;VALUES=8-DISTINCT;ALL-RATIONAL-ROWS=588|TWO-POINT=SEPARATIONS=16-OF-16-CEILING;MAX-DEFECT-RADIUS=2-OF-2-CEILING;LIGHTCONE=BOUND-HAS-CONTENT-ONLY-AT-RADIUS-0;RADIUS-PROFILES=6;HALF-WIDTH-ATTAINED=33-OF-58;PERIODS=1+2+4;EQUAL-TIME=15/256|CLASSES=EXTENDED=22;ANCHORED=38;SIZES=1+2+4;DISTINCT-INVARIANT-LABELS=14|LOCALITY=LOCAL=216-OF-576;NONLOCAL=372-OF-1188;DEFECT-INDIFFERENT-AT-MATCHED-VALUE-MULTISET=616-OF-1024-WEIGHTED-FROM-25-DISTINCT|MARKOV=0-OF-1792-NONZERO|COMMUTATOR=0-OF-3364-NONZERO-IN-THE-VERDICT-STRATUM|REALIZATION=LEVELS=NONE+OCC+FULL;MAXIMAL=FULL;EXCLUDED-NONZERO=150;PRINCIPLED-BITE=36|STATE=BACKGROUND-COEFFICIENT-BY-CONSTRUCTION(LINEAR-LAW;SINGLE-OCCUPATION);OBSERVABLE-MOVES-AT-18-DISTINCT-RESPONSES-OVER-8-PROBE-PAIRS|SCALE=L=4-UNIQUE(LOCALITY-IFF-L>=4;NON-MONOMIAL-LOCAL-AXIS-ONLY-IF-L<=4;PRESENT-AT-L-IN-{2,4});CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))|SCOPE=D=2;L=4;FIELD=Q(ZETA-8);ALPHABET=25;GENERATORS=64;STENCIL=3-TERM-AXIS;SECTOR=SINGLE-OCCUPATION;SWEPT-RANGE=L-IN-2..9;INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-INTERACTING-THEORY-CLAIM-BEYOND-THE-COMPOSED-SEGMENT-DEFECT>
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and what would have answered it the other way

Does a spatially structured declared-indivisible family on the record stage
exhibit a nonzero composition defect, and does the defect carry excitation
structure?

*Spatially structured* means the transition matrices act on lattice
configurations, moves respect adjacency, and the family is translation
covariant. *Excitation structure* means measured two-point content and
transformation-type classes. It does not mean a field theory. The word "field"
is used below in exactly three senses: the algebraic field of coefficients; the
declared fields a generator transports in the realization census; and, for the
physics, only in "free-field analog". The paper says **transformation-type**
and, where the object is a conjugacy class of laws, **conjugacy type** — never
"particle".

*Declared-indivisible* means what it says. Indivisibility here is a
**declaration** — the division-event times are declared, not measured — and the
seed's own engraving forbids the inference from a nonzero defect to stochastic
indivisibility. The verdict carries the word as a scope segment, not as a
finding.

Three outcomes are pre-registered and all three are reachable by the same
derivation, demonstrated on synthetic censuses inside a gate:
`R4-DEFECT-PRESENT`, `R4-DEFECT-ABSENT` (the Markovian collapse), and
`R4-BLOCKED-AT-<named fact>` — the latter in two forms, an empty
maximal-transport class and a stage with no locality-bearing scale. The
pre-registered names are parsed from the pin's own bytes rather than typed in
the instrument. The head is computed from the measured counts and cannot be
typed: a mutant that types it dies, a mutant that makes the derivation constant
dies, a mutant that retypes it *after* every verdict gate has been built dies at
the string-equality gate, and a mutant that lets the scale precheck name it dies
because, run on a zeroed census, the head it produces fails to move.

## 2. The stage, the connective it forces, and the size it forces

The dimension is not this unit's to choose: it is read from the anchored stage
at `declarations/d`, with value $2$, and the link set at
`declarations/links_d2`, with value $\{(1,0),(0,1),(1,1)\}$. A path drift or a
value drift dies at the anchor.

The lattice is $X=(\mathbb{Z}_L)^2$ with periodic boundaries; sites carry a
single occupation label, so the configuration space is $C=X$ with $|C|=L^2$.

**The neighbourhood connective is forced, and this is the paper's first
finding.** Two Boolean connectives are declared, each with its own radius-one
ball: the max-norm ball and the sum-norm ball. The anchored link set decides
between them. The anchored diagonal link $(1,1)$ has max-norm $1$ and sum-norm
$2$: it lies inside the max-norm ball and outside the sum-norm one. So exactly
one declared connective can carry the stage's own declared links, and the
neighbourhood relation is not this unit's to choose either. The excluded
connective is swept anyway, to measure what excluding it costs:

| connective | $d$ | locality threshold | admits the anchored links |
|---|---|---|---|
| MAX-NORM | 1 | 4 | yes |
| MAX-NORM | 2 | 4 | yes |
| MAX-NORM | 3 | 4 | yes |
| SUM-NORM | 1 | 4 | no |
| SUM-NORM | 2 | 2 | no |
| SUM-NORM | 3 | 2 | no |

Under the excluded connective at $d=2$ the completeness measurement is:
threshold 2 against the max-norm's 4, a measured delta of -2. Had the excluded
connective been admitted, the admissible set would be {2, 4} rather than a
single size. The exclusion therefore has teeth, and the segment
`CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))` carries it. A mutant that
routes the sum-norm rows into the admissibility loop dies at the gate that
names the anchored-link forcing.

The locality criterion is ported verbatim from the terminal manifold receipt:
*locality exists iff some connected component of the overlap graph is not
complete*. Applied to the lattice adjacency graph under the forced connective
and swept over $L\in\{2,\dots,9\}$ at $d\in\{1,2,3\}$, it returns the same
threshold at every dimension:

| $L$ | nonzero offsets | neighbours | complete | locality |
|---|---|---|---|---|
| 2 | 3 | 3 | yes | no |
| 3 | 8 | 8 | yes | no |
| 4 | 15 | 8 | no | yes |
| 5 | 24 | 8 | no | yes |
| 6 | 35 | 8 | no | yes |
| 7 | 48 | 8 | no | yes |
| 8 | 63 | 8 | no | yes |
| 9 | 80 | 8 | no | yes |

*Scope: exhaustive over $L\in\{2,\dots,9\}$ and $d\in\{1,2,3\}$, under the
forced connective; the excluded connective's thresholds are in the table above.*

**Locality on this stage requires $L\ge 4$ under the anchored adjacency.**
Section 3 shows that a local non-monomial generator requires $L\le 4$, and the
two requirements meet at exactly one point.

## 3. The family, and the collapse that isolates one scale

### The construction

A generator is a coefficient map $c$ on lattice offsets; its matrix is
$M_{x+v,\,x}=c_v$, so it moves an occupied site by $v$ with amplitude $c_v$.
Write $S$ for the declared **stencil**: the three offsets $\{0,a,-a\}$ along a
declared **axis** $a$, which is a nonzero offset taken modulo sign. On the
working lattice there are 9 axes, 4 of them local and 5 not: the local axes are
$(0,1)$, $(1,0)$, $(1,1)$ and $(1,3)$, and the non-local ones are $(0,2)$,
$(2,0)$, $(1,2)$, $(2,1)$ and $(2,2)$. All nine are used — the axis set is
exhaustive, not sampled.

Unitarity has a closed criterion. Writing the periodic autocorrelation
$$
A(m)\;=\;\sum_{v} c_v\,\overline{c_{v+m}},
$$
the matrix is unitary if and only if $A(m)=\delta_{m,0}$: the coefficient
sequence must have delta autocorrelation. The instrument uses this criterion and
confirms every generator by two further routes — the adjoint product
$U^{\dagger}U=I$ and unit modulus of the character transform — with zero
disagreements. The three routes are one identity in three bases, so they are
carried as implementation cross-checks, not as independent measurements.

The coefficient alphabet is declared: $0$ together with $\zeta_8^{t}$ times a
modulus in $\{1, 1/2, 1/\sqrt2\}$, 25 elements in all. The sweep runs over
15,625 coefficient triples at every swept axis order and is exhaustive there.

### The collapse theorem, and its extension to the whole ball

**Theorem (order collapse).** *Let $a$ have order $n\ge 5$ in the lattice group.
Then every unitary generator on the stencil $\{0,a,-a\}$ is monomial — exactly
one coefficient is nonzero.*

*Proof.* For $n\ge5$ the five offsets $0,\pm a,\pm 2a$ are distinct. Taking
$m=2a$, the only surviving term of $A(2a)$ is $c_{-a}\overline{c_{a}}$, so
$c_{a}c_{-a}=0$. Taking $m=a$, the surviving terms are
$c_0\overline{c_a}+c_{-a}\overline{c_0}$, so $c_0\overline{c_a}+c_{-a}\overline{c_0}=0$.
If $c_{-a}=0$ this forces $c_0\overline{c_a}=0$, hence $c_0=0$ or $c_a=0$; if
instead $c_a=0$ it forces $c_{-a}\overline{c_0}=0$ with the same conclusion. In
either case at most one coefficient survives. $\square$

The argument uses no property of the coefficients beyond the field operations,
so it is independent of the declared alphabet. Its machine confirmation is
alphabet-relative and agrees, at every swept order:

| ord | distinct unitary generators | monomial | non-monomial |
|---|---|---|---|
| 1 | 8 | 8 | 0 |
| 2 | 32 | 16 | 16 |
| 3 | 24 | 24 | 0 |
| 4 | 72 | 24 | 48 |
| 5 | 24 | 24 | 0 |
| 6 | 24 | 24 | 0 |
| 7 | 24 | 24 | 0 |
| 8 | 24 | 24 | 0 |
| 9 | 24 | 24 | 0 |

*Scope: exhaustive over the declared alphabet cubed at each order; the $\ge5$
rows are a theorem, the order-3 emptiness is alphabet-relative and is declared
as such.*

The theorem extends past the axis stencil to the whole radius-one ball.

**Theorem (Moore-ball collapse).** *Let $L\ge 5$ and let $U$ be a unitary
generator on $(\mathbb{Z}_L)^2$ whose coefficient map is supported inside the
radius-one Chebyshev ball $\{-1,0,1\}^2$. Then $U$ is monomial. Over any field
closed under conjugation.*

*Proof.* Write the ball's three columns $X=(c_{-1,j})$, $Y=(c_{0,j})$,
$Z=(c_{1,j})$ for $j\in\{-1,0,1\}$. For $L\ge5$ there is no wraparound inside
the ball, so the lag $(2,t)$ receives contributions only from column $-1$
paired with column $+1$:
$A(2,t)=\sum_j c_{-1,j}\,\overline{c_{1,j+t}}=0$ for every
$t\in\{-2,\dots,2\}$. That is the vanishing of the entire aperiodic
cross-correlation of the length-three sequences $X$ and $Z$, i.e.
$X(x)\cdot\tilde{Z}(x)\equiv 0$ in the Laurent polynomial ring over the field.
The ring is an integral domain because the field is, so $X\equiv0$ or
$Z\equiv0$. Say $Z\equiv0$; then the lag $(1,t)$ receives contributions only
from column $-1$ against column $0$, giving likewise $X\equiv0$ or $Y\equiv0$.
Either way the support lies in a single column, and the vertical lags $(0,t)$
are then the aperiodic autocorrelation of a length-three sequence, which by the
two-lag argument above forces support at most one. The case $X\equiv0$ is
symmetric. $\square$

Both legs of that proof that are finite are gated. The lag structure is
measured by exhaustive enumeration of the ball's pair sets at
L in {5, 6, 7, 8, 9}: the extreme lag receives exactly the cross-column pairs,
the single-column lag receives exactly one pair, and no ball difference wraps.
The domain property is measured on
576 ordered pairs of nonzero alphabet elements, 0 zero divisors.
The single-column reduction is the order census's own rows at order five and
above.

**Consequence.** No local stencil whatever — three-term, five-point, nine-point,
or any subset of the radius-one ball — admits a non-monomial unitary at any
$L\ge5$, over any field. That closes the scope hole the nine-point stencil left
open at every size above the admitted one.

The declared five-point extension is swept directly as a control, at four sizes
and in both declared offset orderings:

| $L$ | complete assignments | non-monomial |
|---|---|---|
| 4 | 1561 | 160 |
| 5 | 121 | 0 |
| 6 | 121 | 0 |
| 7 | 121 | 0 |

*Scope: exhaustive with autocorrelation pruning over the declared alphabet. The
node count is an artifact of the search order and is not reported as a property.
At $L=5$ the sweep visits
34,925 and 452,525 nodes under the two declared orderings, and at $L=4$ it
visits 150,125 and 722,525 nodes, reaching the same leaves and the same
solutions in each case.*

The $L=4$ row is a disclosure and not a promotion. At the admitted size the
five-point stencil carries a wider local family than the three-term axis
stencil this unit censuses, and that family is not examined here.

### The unique scale, and its alphabet independence

A local axis on $(\mathbb{Z}_L)^d$ has order exactly $L$; this is measured, not
assumed. Combining with section 2:
locality requires L >= 4; a non-monomial local-axis generator requires L <= 4, and is present at L in {2, 4}.
The second half is an **only-if** bound with a measured presence set — the presence
set is not the whole interval below the bound, because order three carries no
non-monomial generator over the declared alphabet.

Therefore **the admissible set is {4}**, and one lattice size in the swept range
carries both. The instrument computes the set and gates that it has exactly one
member, with the value anchored separately; the lattice the census then runs on
is taken *from* that set rather than typed beside it, and a mutant that censuses
a different size dies at the binding gate. A mutant that admits a second size
dies. At $L=4$ the family is not empty: the order-four axes carry
72 distinct unitary generators, 48 of them non-monomial, in 9 gauge classes.

The uniqueness survives every alphabet enlargement, and this is a theorem rather
than a sweep:
the sizes bearing locality are {4, 5, 6, 7, 8, 9} and the sizes below the collapse threshold are {2, 3, 4}.
The first set is a property of the
stage and the second is a consequence of a field-independent theorem, so the
only size an enlarged alphabet could add lies in their intersection, which is
the admitted size itself. The order-three alphabet-relativity is therefore true
of the table row and irrelevant to the verdict.

This whole section is a precheck: it selects which lattice is censused. It does
not name the verdict, and a gate proves it cannot — with the defect census
zeroed, the head produced by the head law in force moves, and a head law that
reads the precheck instead of the census dies there.

### The choice inventory

15 construction choices are inventoried, each classed with an exact fibre.

| choice | class | fibre |
|---|---|---|
| the spatial dimension | FORCED (anchored) | 1 |
| the link set | FORCED (anchored) | 1 |
| the neighbourhood connective | FORCED (anchored) | 1 |
| the lattice size | FORCED (measured) | 1 |
| the coefficient alphabet | GENUINELY-FREE | 25 |
| the stencil | GENUINELY-FREE | 2 |
| the axis set | FORCED (exhaustive) | 9 |
| the global phase | STABILIZER-FIXED | 8 |
| the gauge representative | STABILIZER-FIXED | 8 |
| the division-event times | GENUINELY-FREE | 1 |
| the leg at the cut | GENUINELY-FREE | 1 |
| the brickwork coin | GENUINELY-FREE | 1 |
| the scramble permutations | GENUINELY-FREE | 2 |
| the symmetry group | GENUINELY-FREE | 2 |
| the prepared-state set | GENUINELY-FREE | 18 |

The connective row is FORCED with fibre one for the reason section 2 gives, and
the reason is printed in the receipt beside the row. The declared global phase
is stabilizer-fixed rather than free because the anchored gauge row makes the
defect invariant under it; that invariance is measured, with its own two-sided
self-test. The stencil row stays free because at the admitted size — and only
there — a wider local stencil exists.

## 4. The defect, and its census

### The object

The composition defect is reimplemented from the anchored definition:
$$
\Delta^{B}(U_2,U_1)\;=\;B(U_2U_1)\;-\;B(U_2)B(U_1),\qquad
B(U)=\lvert U\rvert^{\circ 2},
$$
the failure of the Born shadow of the coherent composite to equal the shadow
obtained by forgetting phases and restarting at the intermediate cut. The
division-event times are declared: $t=0$ and $t=2$ are division events, the cut
at $t=1$ is not, and the leg across the cut is declared to be $B(U_2)$. With
$t=1$ a division event there would be no cut to test, and a mutant that declares
it one dies.

The reimplementation is checked against the anchored source's own named
two-by-two witness, exactly: on the Hadamard against the unbiased $V$ the defect
vanishes, and on the Hadamard against itself it returns
$\begin{pmatrix}1/2&-1/2\\-1/2&1/2\end{pmatrix}$. A sign flip of that witness
dies at the gate.

Three routes compute it: the definitional route on sparse matrices, the
separation-indexed coefficient convolution
$$
\Delta(s)\;=\;\Bigl\lvert\sum_t v_t\,u_{s-t}\Bigr\rvert^2-\sum_t \lvert v_t\rvert^2\lvert u_{s-t}\rvert^2 ,
$$
and the character-basis product transformed back. They agree everywhere they are
compared. All three are the same identity written in different bases, as is the
closed cross-term form of the anchored source; each is therefore registered as
an implementation cross-check rather than as an independent measurement. What
the second code path *does* carry is the binding of the census: the whole value
multiset is recomputed through it.

### The census

The pool is
64 generators: 58 translation-covariant circulants, 4 brickwork generators and 2 scrambled generators
— the last six are the controls. The
census is 4096 ordered pairs, one row per ordered pair, the count derived from
the pool.

**588 of 3364 pairs at maximal transport carry a nonzero defect.** Their values
form eight distinct exact numbers, and the whole multiset is gated against a
recomputation by a second code path, together with its exact zero-sum identity:

| value | cells |
|---|---|
| $+5/8$ | 24 |
| $+1/2$ | 108 |
| $+1/4$ | 336 |
| $+1/8$ | 144 |
| $-1/8$ | 192 |
| $-1/4$ | 336 |
| $-1/2$ | 108 |
| $-3/8$ | 24 |

Every nonzero row at maximal transport is rational — 588 of 588 — although the
field carries irrational elements and the Born projection is never coerced out
of it. Each defect column sums to zero, as it must, both composites being
stochastic; that identity is forced, and the check is taken over every census
row rather than a sample so that the evidence matches the claim.

### The Markovian control, gated in both directions and bound to the object

The Markovian sub-family is classified by measured support size: a generator is
monomial when its coefficient map has at most one nonzero offset, which makes
its transition matrix a deterministic shift and its process divisible across the
cut. 16 of the pool's generators are monomial.

**0 of 1792 Markovian pairs** carry a nonzero defect. This is the anchored
annihilator theorem — the row-monomial unitaries annihilate the defect against
everything — measured here rather than assumed: the pairwise sum through the cut
is literally empty, and the gate reads the defect dictionaries themselves rather
than a count of their entries, so a nonzero object written into a Markovian row
dies even with the count left intact.

The zero is a measurement because the same instrument returns nonzero on the
complementary set: 738 of 2304 free pairs are nonzero. And it is gated in both
directions. A mutant that mislabels a two-support generator as monomial dies at
the classifier. A mutant that injects a nonzero into a Markovian pair dies at the
Markovian gate. A mutant that zeroes every defect dies at the positive control.
A mutant that zeroes only the twelve named value-census rows dies at the value
census — and a mutant that zeroes rows *outside* those twelve dies too, at the
full-multiset gate, because the binding is the whole census and not a sample of
it.

### Locality dependence, at matched coordinates

Locality and transport are different axes. Non-local circulants transport
everything a local one does; they differ only in the radius of their stencil.
That is what makes a matched comparison possible: the order-four local and
non-local axes carry the same coefficient values, so the contrast can be read
with the coefficient class and the axis order held equal, varying only the
radius.

Matching each order-four local generator to a non-local generator of the same
coefficient value multiset yields
1024 ordered comparisons drawn from 25 distinct non-local pairs; 616 of the 1024 agree
on the defect value multiset. The matching is by value multiset, not by
gauge class, and the count is weighted accordingly, with
multiplicities 9 at 64, 12 at 32, 4 at 16.

Because the value multiset does not hold the gauge fixing equal, a second
matching is taken on the full axis-relative gauge class — which offset carries
which value, read in axis coordinates. It gives
1024 ordered comparisons from 64 distinct pairs, of which 648 agree.

Over the whole maximal-transport census,
216 of 576 local pairs and 372 of 1188 non-local pairs are nonzero, with the
same maximal defect radius on both sides. The defect is therefore largely, but
not entirely, indifferent to the locality of the generators that produce it: the
matched tables are the primary objects and the contrast is read off them.

## 5. Two-point structure — the free-field analog

The phrase is used in one sense only: the objects below are the lattice
propagator and its correlators, the analog of a free field's two-point
functions. No field operator, no multi-excitation sector and no interaction term
is constructed.

### The tables

*Equal time.* The connected correlator of the occupation observable on the
declared uniform state is $C_0(x,y)=\delta_{xy}p(x)-p(x)p(y)$,
exactly 15/256 at zero separation and -1/256 at every nonzero separation. That
is $p(1-p)$ on a sixteen-site lattice: a function of the lattice size and the
declared state alone, identical for every family on this stage. It is state
arithmetic, carried as a disclosure, and it says nothing about the dynamics.

*Composed time.* The two-time correlator across the cut splits exactly:
$$
\underbrace{B(U_2U_1)}_{\text{coherent}}\;=\;\underbrace{B(U_2)B(U_1)}_{\text{restarted at the cut}}\;+\;\Delta^{B}(U_2,U_1).
$$
The split is the definition of $\Delta^{B}$ rearranged and is therefore forced;
it is carried as an implementation check. **The composition defect is the
interference part of the two-time correlation function**: the two-point
structure and the defect census are the same table, read two ways, and what is
measured is the size of the interference part.

*Translation covariance, gated.* Every circulant's transition table is a
function of the lattice separation alone — not merely foldable without conflict,
but with every separation class wholly present and constant — and its defect
table folds without conflict on every pair: all 58 pass.

*The negative control.* Scrambling the lattice by a declared site transposition
breaks it measurably: both scrambled generators lose the full translation
stabiliser, neither transition table remains a separation table, and
32 of their 48 defect tables against the probe set fail to be one, and 16 are identically zero.

### Decay, periodicity, and how much the cone bound says

The defect spreads over
16 separations, every separation the torus has, with maximum defect radius 2, the Chebyshev diameter.
Both numbers are arena
**ceilings**, attained rather than profiled: at the admitted size there are no
further separations to reach and no larger radius to have. The verdict carries
them as ceilings for that reason.

The composed propagator's support starts at the generator's own radius and
never grows faster than one neighbourhood per step. How much that says is
measured rather than assumed. Sweeping every conceivable radius profile at this
lattice size gives
81 conceivable profiles, and the bound can fail only at single-step radius 0
— so for every generator of radius one or more the clause
is forced, and the verdict says so rather than reporting it as a physical
finding.

The measurement that does have content takes its place:
6 radius profiles occur across the first four powers, distributed as
0000 at 1, 1010 at 8, 1110 at 16, 1210 at 8, 2020 at 7, 2220 at 18, and
33 of 58 attain the half-width. The bound is not saturated by all of them,
because the torus wraps and because most of the family satisfies a quadratic
minimal polynomial.

Periodicity is reported projectively. The raw order of $U$ — the least $k$ with
$U^k=I$ — is *not* gauge invariant, since a global phase rescales every power;
the least $k$ with $U^k$ a scalar is. Measured:
the projective periods present are {1, 2, 4}; the raw orders are {2, 4}. The
gauge self-test confirms the split:
the projective period is invariant at 42 of 42 and the raw order moves at 29.

### The defect algebra, self-tested

Reimplemented and measured on this family: the defect vanishes against the
identity on both sides; it is equivariant under conjugation of the pair by a
site permutation; transposing it reverses the pair; and the coherence law holds
on the declared 48 triples with 0 violations. All four are identities of the
Born map under composition, conjugation and transposition, and each is
registered as a disclosure with its forcing named.

The symmetry self-test required by the discipline is present in both directions
and on both factors, and evaluates fresh, with the product cache cleared and a
cache-free recomputation alongside: multiplying **either** factor by a global
phase leaves the defect fixed at every one of the checked pairs, while the one
handle — an inner diagonal inserted at the cut — moves it at every one of them.
An invariance gate whose negative direction never fires would be vacuous; this
one's negative direction fires everywhere.

## 6. Conjugacy-type classes

The Wigner move at finite scale, taken at the strength it actually has: classify
the family by orbits of the symmetry group and label the orbits by invariants.
What the census produces is a **conjugacy census of dynamical laws**, not a
classification of states, and the labels are constant on orbits but do not
separate them. Both facts are measured below, and the analogy is not drawn past
them.

Two groups are censused. The **anchored** group is the stage's own chart group —
the lattice translations together with the direction relabellings —
of order 32. This unit's declared **extension** adds the remaining square point
symmetries, order 128. Both act on generators by relabelling sites, and
generators are identified up to the declared global phase, since that phase is
gauge.

There are
22 transformation-type classes under the extended group and 38 under the anchored chart group,
with sizes 1, 2 and 4. The orbits partition the pool; the orbit-stabiliser
identity holds on every class from the measured action; and the declared class
invariants — support, radius, transport level and projective period — are
constant on every orbit.

| class | size | kind | support | radius | ord(axis) | transport | period |
|---|---|---|---|---|---|---|---|
| C000 | 4 | circulant | 3 | 1 | 4 | FULL | 4 |
| C001 | 4 | circulant | 3 | 1 | 4 | FULL | 4 |
| C004 | 1 | circulant | 1 | 0 | 4 | FULL | 1 |
| C005 | 4 | circulant | 2 | 1 | 4 | FULL | 2 |
| C007 | 4 | circulant | 1 | 1 | 4 | FULL | 4 |
| C009 | 2 | circulant | 2 | 2 | 2 | FULL | 4 |
| C010 | 2 | circulant | 2 | 2 | 2 | FULL | 4 |
| C011 | 2 | circulant | 1 | 2 | 2 | FULL | 2 |
| C020 | 4 | circulant | 3 | 1 | 4 | FULL | 4 |
| C021 | 4 | circulant | 3 | 1 | 4 | FULL | 4 |
| C024 | 4 | circulant | 2 | 1 | 4 | FULL | 2 |
| C026 | 4 | circulant | 1 | 1 | 4 | FULL | 4 |
| C028 | 4 | circulant | 3 | 2 | 4 | FULL | 4 |
| C029 | 4 | circulant | 3 | 2 | 4 | FULL | 4 |
| C032 | 4 | circulant | 2 | 2 | 4 | FULL | 2 |
| C034 | 4 | circulant | 1 | 2 | 4 | FULL | 4 |
| C055 | 1 | circulant | 2 | 2 | 2 | FULL | 4 |
| C056 | 1 | circulant | 2 | 2 | 2 | FULL | 4 |
| C057 | 1 | circulant | 1 | 2 | 2 | FULL | 2 |
| B058 | 4 | brickwork | — | 1 | 4 | OCC | — |
| S062 | 1 | scrambled | — | 2 | — | NONE | — |
| S063 | 1 | scrambled | — | 2 | — | OCC | — |

*Scope: the declared pool at $d=2$ and the admitted size, both declared groups,
generators identified up to the declared global phase.*

**The labels do not label.**
22 classes carry only 14 distinct invariant tuples; adding a direction label raises it to 17.
One tuple is shared by four classes at once. Wigner's labels separate; these do
not, and the two invariants that would complete them are a direction label and a
chirality label — which is to say, exactly the momentum-like and parity-like
quantum numbers this census does not have.

One reading deserves its own line, at the strength it has. **The translation
group acts trivially on the whole circulant family** — every circulant is its own
translate, and all 58 translation orbits are singletons. That is forced: a
coefficient-map matrix commutes with every lattice translation by construction.
The measurement in that paragraph is its converse, and it is what makes the
covariance census non-vacuous: the *controls* do move under the translation
action. The consequence is a real reading and survives: the classification is
carried entirely by the point symmetries, and the census produces charge-like
invariants and no momentum-like invariant whatever.

## 7. The realization census, its bite, and the abelian stratum

Every generator declares which fields it transports, and the declaration is
measured, not typed:

- **OCC** — the occupation field is transported along a nontrivial subgroup of
  the translations (measured by the translation stabiliser being nontrivial);
- **OCC+AXIS** — the stabiliser is the full translation group, so the site and
  axis structure is transported everywhere;
- **FULL** — in addition the coefficient register transports equivariantly: for
  every element of the anchored chart group extended by the point symmetries,
  the image is again a family member up to the declared gauge, and its axis
  label is the transported label.

The measured census is:
1 generator at NONE, 5 at OCC, 0 at OCC+AXIS, 58 at FULL. The maximal declared
transport attained is **FULL**, and the verdict's defect segment is rebuilt from
that subset alone. Every individual classification is verified against its own
computed invariant by a second route that shares no helper with the classifier —
the stabiliser from explicit permutation-matrix products, the covariance from
the matrix action's gauge-canonical membership in the pool — and a single
promotion or a single demotion dies there.

The gate bites, and the size of its bite is reported honestly.
150 nonzero defects are excluded from the verdict because their pairs do not
reach maximal transport — genuine nonzero measurements, printed in the census
rows, kept out of the verdict segment. But
114 of them involve the scrambled control, so the gate's principled bite is 36:
the scrambled generators are a deliberately broken negative control and were
never candidates for the verdict. The segment rebuilt from the maximal-transport
subset differs from the segment rebuilt from all pairs, and a mutant that admits
the sub-maximal defects dies; so does a mutant that promotes every generator to
maximal transport, and so does one that claims nothing was excluded.

The brickwork controls are the substance of the principled part of that
exclusion. They are ordinary local unitaries — a two-site coin applied on a
parity class of dominoes, unitary by construction and radius one — and they carry
nonzero defects. What they do not carry is full covariance: their stabiliser is
the index-two subgroup that preserves the parity, so they transport occupation
but not the axis structure, and their defects stay out of the verdict. Their
exclusion is not the removal of an artifact; it is a restriction to a covariant
sub-family, and the excluded stratum is a different family rather than a
degraded realization of this one.

**And the gate selects the commuting sector.** The commutator census, over every
ordered pair of the pool:

| stratum | non-commuting | ordered pairs |
|---|---|---|
| BRICK-BRICK | 4 | 16 |
| CIRC-BRICK | 256 | 464 |
| CIRC-CIRC-THE-VERDICT-STRATUM | 0 | 3364 |
| WITH-SCRAMBLE | 222 | 252 |

0 of 3364 ordered pairs of the verdict-bearing stratum fail to commute. That
zero is forced — circulant convolution on an abelian group commutes — and its
consequence is not: **every plaquette holonomy and every Wilson loop assembled
from R4's verdict stratum is the identity by a theorem, and the only
non-commuting generators on this stage are the ones the mandatory realization
gate excludes.** A gate motivated by a transport question acts, on this arena,
as a projector onto the abelian sector. That is the single most consequential
structural fact the unit measures, and it is the fact the gauge rung inherits.

## 8. The state-motion check

The prepared states are declared: sixteen point masses, the uniform state, and
one wedge — 18 declared prepared states over 8 probe pairs. For a probe pair the
observable defect is $\delta(p)=\Delta^{B}p$, the difference between the
coherent and the restarted prediction on that state.

Two facts, and they are not of the same kind. First, the matrix reconstructed
from the sixteen point-mass responses equals the coefficient matrix $\Delta^{B}$
exactly, at every probe pair: one and the same coefficient serves every prepared
state. **That is forced, not measured.** $\delta(p)=\Delta^{B}p$ is linear, so
the point-mass responses *are* the columns of $\Delta^{B}$ and reassemble it for
every matrix whatever. Second, the observable does move: there are
18 distinct responses across the eighteen declared states, at every probe pair,
so the instrument that reported the background could have reported motion and
did not.

The honest statement is therefore stronger and narrower than a finding about
this family. On a linear law over a single-occupation sector **no** coefficient
can move with the state; the frozen-stage stratification is not confirmed at the
quantum layer here, it is enforced by the arena. Testing it requires leaving the
arena, and there are exactly three routes out, in increasing cost: a
two-excitation sector, in which one excitation's effective coefficient becomes a
functional of another's occupation; state-dependent division-event times, so the
cut moves with the state; or a self-consistent mean-field generator, which
breaks linearity outright. Any of those makes the background reading falsifiable
for the first time. None of them is taken here.

## 9. What this decides, and what it does not

**Decided, at the declared scope.**

- On a $d=2$ periodic lattice of the admitted size, with occupation
  configurations and declared local moves, a spatially structured
  declared-indivisible family exists and its composed segments carry a nonzero
  composition defect: 588 of 3364 pairs at maximal transport carry a nonzero
  defect, over eight distinct exact rational values.
- One lattice size in the swept range admits the **local-move** construction at
  all, the connective that makes it unique is anchored rather than chosen, and
  the uniqueness survives every alphabet enlargement.
- The Markovian sub-family returns exactly zero, gated in both directions and
  bound to the defect object and to the whole value census.
- The defect is the interference part of the two-time correlator.
- The family carries 22 transformation-type classes under the extended group and
  38 under the anchored chart group, with the declared invariants constant on
  each — and not separating.
- The verdict-bearing stratum is abelian, and the generators the mandatory gate
  excludes are the entire source of non-commutativity on the stage.
- The observable moves with the prepared state.

**Not decided, and not attempted.**

- Indivisibility is *declared*, by the declared division-event times, and is
  never measured. The seed engraves that a nonzero defect does not imply
  stochastic indivisibility, and no existential divisor search is run here. The
  verdict carries `INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES` for that
  reason.
- Quantum structure is *not* unique to the admitted size. What is unique to it
  is quantum structure among **local** moves; non-local non-monomial unitaries
  exist at every swept size and carry a defect. The bolded claim is about the
  locality of the moves, never about the existence of superposition.
- No continuum or infinite-volume limit is taken. Nothing here is a statement
  about a field theory; in the physics, "field" is used only as the free-field
  analog.
- No multi-excitation sector, no interaction term, no field operator. The only
  interaction-shaped object is the composed-segment defect itself. The sector is
  single occupation throughout, and it is carried in the verdict's scope.
- Coefficients outside the declared alphabet are not swept. The
  order-five-and-above collapse and the Moore-ball collapse are theorems and
  alphabet-independent; the order-three emptiness is alphabet-relative and is
  declared so, and it is irrelevant to the verdict.
- The nine-point stencil is not swept at the admitted size. The Moore-ball
  collapse settles every size above it; at the admitted size itself the
  five-point stencil already carries a wider local family that is disclosed and
  not censused.
- $d=3$ is swept for the locality threshold only, not for the family.
- The excluded nonzero defects are real measurements at sub-maximal transport.
  They are printed, not promoted.
- The two-point observables sit at their arena ceilings. At the admitted size
  the lattice diameter is 2 and there are only three Chebyshev separation
  classes, so no decay profile and no dispersion curve can be resolved: **the
  local family lives exactly where the propagator cannot be resolved.** That
  tension is a consequence of the uniqueness theorem, not an artifact of the
  measurement.

## 10. The instrument

101 gates, all passed; 24 anchors; 116 declared mutants, all dead — and every
mutant killed by the gate it was declared to falsify. The anchors are
5 file-bytes anchors, 10 path-value anchors and 9 verbatim-text anchors.

Gates that discharge a per-object obligation bind objects, not cardinalities:
the realization census verifies every individual generator classification
against its own computed invariant; the Markovian zero reads the defect
dictionaries rather than their sizes; the value census binds the whole
multiset of the verdict-bearing census against a second code path, together with
its exact zero-sum identity.

The verdict carries 50 measured values, and each one has its own flip probe:
the value renders from a declared receipt key, and perturbing that key must move
the complete reconstruction. The reconstruction derives the head by its own copy
of the head law and re-asserts it against the pin's pre-registered names, so a
head retyped after the verdict object exists is caught by the string-equality
gate rather than copied past it.

Gates whose clause is analytically forced are registered as disclosures with
their forcing named and with the gate that carries the measured content in their
place: the cone bound against the radius-profile census, the background
coefficient against the moving observable, the trivial translation action
against the moving controls, the composed-time split and the coherence law
against the defect census, the column sums and the stochasticity against
unitarity, the equal-time correlator against the declared state.

The CLI is argv-parsed against a whitelist and exercised inside the run: an
unknown flag, an unknown mutant name, an unknown anchor name and a missing flag
argument are all rejected with exit 2; a self-test corrupts one anchor in
memory, confirms that the run dies at the anchor gate, writes nothing and exits
1; and the plain run with no flags is the only invocation that writes.

The compliance sweep enumerates 22 engraved rules, and every status is a
computed predicate: a row is APPLIED only when every gate it names is in the
frozen registry, was evaluated on this run, and carries an injection-falsifier
or a registered forcing. The paper's own numeric claims are gated inside the
delivery run: every claim is rendered from the receipt and checked against this
file's bytes, and this file carries no numeral outside that rendering except a
declared residue, each entry of which names the site that derives it and must
occur here.

Controls run in both directions throughout: the Markovian zero against the free
nonzero; the gauge invariance against the handle that moves it; the covariant
circulants against the scrambled control; the maximal transport against the
excluded sub-maximal defects; the background coefficient against the moving
observable; the trivial translation action against the moving controls.

Determinism: two plain runs, byte-identical in both artifacts.

## 11. The successor register

**R4b — momentum.** Two objects this unit computes and does not read are the
character-basis dispersions of the circulant family and the per-generator radius
profiles beyond the first four powers. The census is taken on *generators* by
conjugation, and translations act trivially there by construction; momentum
lives on the symbol, not on the orbit, and a census taken on (state, generator)
pairs in the character basis would recover a grading the present labels lack —
which is exactly the direction label the class table is missing. The
propagator observation is the constraint: the uniqueness theorem confines the
local family to the one lattice where the two-point observables are
ceiling-saturated, so any dispersion measurement must either widen the modulus
set, leave the local class, or leave the admitted size. The connective is forced
by the anchored link set, and that forcing travels with the arena.

**R5 — gauge.** Its pin opens with this unit's datum, verbatim:

> **R4's verdict-bearing stratum is abelian: 0 of 3364 commutators are nonzero.
> Every plaquette holonomy and every Wilson loop built from it is the identity by
> a theorem. The only non-commuting generators on the stage are the brickwork
> generators — exactly the ones R4's mandatory realization gate excludes.**

A gauge rung built on R4's FULL stratum is pre-committed to flat abelian
holonomy: it would return a trivial answer at exit 0 and could not be falsified.
R5 must therefore build on the **excluded non-abelian stratum** — the
sub-maximal-transport family promoted to first class, link-indexed unitaries on
the admitted torus with a coin per link, in declared parity strata. The stratum
this unit excludes is not a degraded realization; it is where the
non-commutativity is.

Seven gates are pre-registered for it. Non-abelian non-vacuity is decisive: the
plaquette-holonomy group is measured, its commutator subgroup gated nontrivial,
the group reported as an isomorphism class and never as matrices, with R4's FULL
stratum as the mandatory negative control — a flat control that is flat by
theorem. Gate inheritance is binding: the realization-census gate may not be
inherited unmodified, R5 must state at pin time whether maximal declared
transport is compatible with non-abelian holonomy on its arena, and if the
maximal level again selects a commuting sub-family the verdict is
`R5-BLOCKED-AT-THE-GATE`, first class. Curvature against defect is read at
matched coordinates, with coin values, division-event times, leg declaration and
gauge fixing held equal, and three outcomes pre-registered; R4 supplies the
measured baseline for one of them, since its defects sit at identically zero
curvature. The gauge self-test runs in both directions, with this unit's
projective-period self-test as the template. The verdict must carry the
connective, the link set, the sector, the swept range and the indivisibility
status as explicit declaration segments — this unit's scale segment is the
cautionary case, and the connective-forced fact travels into R5 unchanged.
Refinement is the charter's actual question: the holonomy group at the admitted
size against its declared doubling, with the isomorphism class as the invariant
and the plaquette count as the extensive control. And the scramble caveat is
inherited: R5 must show its holonomy group separates the physical case from a
scrambled control before any group-theoretic claim is entered.

No confinement-analog language before non-vacuity passes. No silent inheritance
of the maximal-transport gate. No matrix-valued holonomy reported as physics.
And no claim that curvature implies quantum character: this unit measures
588 nonzero defects at identically zero curvature, which settles that
implication in the negative on this stage.

Note the resonance with the weld-2 census of `paper-13`: this is the second
result in the programme resting on the declared lattice rather than on the
substrate, and the two carry the same weight.

## 12. Deviations, and the register of scope

**The false-claim register.** The programme's count of false paper claims
stands at five, all of the prose species and none in a computed artifact. This
unit supplies the fifth, and it is this: the uniqueness of the admitted size is
connective-relative, and the connective is forced by the anchored link set
rather than free. The register entry is the scope statement section 2 makes and
the verdict's scale segment carries, and the choice inventory classes the
connective FORCED with fibre one. Its content is a strengthening rather than a
retreat: **the unique scale is a theorem about the declared link set of the
record stage, not a law of the substrate.**

**What the verdict's segments are entitled to assert.** The defect census, the
value multiset, the class census, the commutator census outside the verdict
stratum, the principled bite, the radius profiles, the distinct-label count and
the observable's motion are measurements. The Markovian zero, the column sums,
the stochasticity, the composed-time split, the coherence law, the defect
algebra's normalization, equivariance and reversal, the equal-time correlator,
the cone bound above radius zero, the trivial translation action on circulants,
the background coefficient, and the zero commutator on the verdict stratum are
forced, and each is carried as a disclosure naming its forcing. The separation
count and the maximum defect radius are arena ceilings. Indivisibility is
declared.

**A naming drift, disclosed.** The pin names the delivered artifacts with an
`_exact_output` and `_exact_receipt` infix; the delivery ships
`r4_defect_stage_output.txt` and `r4_defect_stage_receipt.json`. The pin is
frozen and hash-anchored, so the drift is recorded here rather than repaired
there. The hashes match the shipped names, so this is a naming drift and not a
substitution.

**The transport gate's reach.** FULL transport is forced for every circulant,
because the point group maps the exhaustive axis set into itself; the
realization census therefore discriminates only among the six declared controls,
and no member of the family under study was excluded by the gate that is said to
bite. The exclusion's principled part is the brickwork stratum, and its size is
36 rather than 150.
