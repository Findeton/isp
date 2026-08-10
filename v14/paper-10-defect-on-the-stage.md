# R4 — the QFT rung: the defect on the stage

**Status:** `GREEN-UNREVIEWED` — delivered against the frozen pin, verified to
run (two plain runs byte-identical; 77 gates passed; 82 declared mutants, all
dead, all killed by their declared target), not yet attacked. Pin:
`v14/note-r4-qft-pin.md`, sha256-12 `1582cea5df51` (v14 ledger #47).

## One Lattice Size Admits an Indivisible Family At All, and On It the Defect Is Present

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
`v14/code/r2_manifold_receipt.json` (`08b2140f46ae`). Every object below is
**reimplemented** from those definitions; nothing is imported from any other
unit.
**Anchors are (path, value) pairs and (context, consumer) pairs, not only file
bytes:** five file-bytes anchors, ten path-value anchors each naming the exact
JSON path it reads and the exact value it expects, and nine verbatim-text
anchors — evaluated before the byte anchors, each bound to the named gate that
consumes it, each a context window rather than a fragment.
**No unanchored runtime inputs:** exactly five files are read at run time, all
hash-pinned; no ledger, no status board, no other unit's working file.
**Exact arithmetic only:** the field is $\mathbb{Q}(\zeta_8)$ carried as integer
coefficient 4-tuples over a positive integer denominator, reduced modulo
$\Phi_8(x)=x^4+1$; the representation is canonical, so tuple equality is field
equality. An AST scan of the instrument's own source and a recursive type scan
of the emitted receipt are gates.

**The verdict, quoted exactly as the instrument emits it.** Every segment is
derived inside a gate from measured counts, and the complete string is compared
for equality against an *independent reconstruction* built from the serialized
receipt alone, by a function that shares no helper with the builder:

```
R4-DEFECT-PRESENT<DEFECT=588-OF-3364-PAIRS-AT-MAXIMAL-TRANSPORT-FULL;VALUES=8-DISTINCT;ALL-RATIONAL-ROWS=588|TWO-POINT=SEPARATIONS=16;MAX-DEFECT-RADIUS=2;LIGHTCONE=ONE-NEIGHBOURHOOD-PER-STEP;PERIODS=1+2+4;EQUAL-TIME=15/256|CLASSES=EXTENDED=22;ANCHORED=38;SIZES=1+2+4|LOCALITY=LOCAL=216-OF-576;NONLOCAL=372-OF-1188;DEFECT-INDIFFERENT-AT-MATCHED-COORDINATES=616-OF-1024|MARKOV=0-OF-1792-NONZERO|REALIZATION=LEVELS=NONE+OCC+FULL;MAXIMAL=FULL;EXCLUDED-NONZERO=150|STATE=BACKGROUND-COEFFICIENT;OBSERVABLE-MOVES-AT-18-DISTINCT-RESPONSES|SCALE=L=4-UNIQUE(LOCALITY-IFF-L>=4;NON-MONOMIAL-LOCAL-AXIS-IFF-L<=4)|SCOPE=D=2;L=4;FIELD=Q(ZETA-8);ALPHABET=25;GENERATORS=64;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-INTERACTING-THEORY-CLAIM-BEYOND-THE-COMPOSED-SEGMENT-DEFECT>
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and what would have answered it the other way

Does a spatially structured indivisible family on the record stage exhibit a
nonzero composition defect, and does the defect carry excitation structure?

*Spatially structured* means the transition matrices act on lattice
configurations, moves respect adjacency, and the family is translation
covariant. *Excitation structure* means measured two-point content and
transformation-type classes. It does not mean a field theory. The word "field"
is used below in exactly three senses: the algebraic field of coefficients; the
declared fields a generator transports in the realization census; and, for the
physics, only in "free-field analog". The paper says **transformation-type**,
never "particle".

Three outcomes were pre-registered and all three are reachable by the same
derivation, demonstrated on synthetic censuses inside a gate:
`R4-DEFECT-PRESENT`, `R4-DEFECT-ABSENT` (the Markovian collapse), and
`R4-BLOCKED-AT-<named fact>` — the latter in two forms, an empty
maximal-transport class and a stage with no locality-bearing scale. The head is
computed from the measured counts and cannot be typed; a mutant that types it
dies, and a mutant that makes the derivation constant dies.

## 2. The stage, and the size it forces

The dimension is not this unit's to choose: it is read from the anchored stage
at `declarations/d`, with value $2$, and the link set at
`declarations/links_d2`, with value $\{(1,0),(0,1),(1,1)\}$. A path drift or a
value drift dies at the anchor.

The lattice is $X=(\mathbb{Z}_L)^2$ with periodic boundaries; sites carry a
single occupation label, so the configuration space is $C=X$ with $|C|=L^2$.
Adjacency is the radius-one ball in the maximum norm on the torus — the closure
of the anchored link set under sign and coordinate combination, gated to contain
every anchored link. The alternative Boolean connective (the sum-norm, or von
Neumann, neighbourhood) is swept alongside as the parity witness; its
completeness threshold is $2$ against the maximum norm's $4$, a measured delta
of $-2$.

The locality criterion is ported verbatim from the terminal manifold receipt:
*locality exists iff some connected component of the overlap graph is not
complete*. Applied to the lattice adjacency graph and swept over
$L\in\{2,\dots,9\}$ at $d\in\{1,2,3\}$, it returns the same threshold at every
dimension:

| $L$ | nonzero offsets | neighbours | complete | locality |
|---|---|---|---|---|
| 2 | 3 | 3 | yes | no |
| 3 | 8 | 8 | yes | no |
| 4 | 15 | 8 | no | **yes** |
| 5 | 24 | 8 | no | yes |
| 9 | 80 | 8 | no | yes |

*Scope: exhaustive over $L\in\{2,\dots,9\}$ and $d\in\{1,2,3\}$, both declared
connectives.*

**Locality on this stage requires $L\ge 4$.** Section 3 shows that the family
requires $L\le 4$, and the two requirements meet at exactly one point.

## 3. The family, and the collapse that isolates one scale

### 3.1 The construction

A generator is a coefficient map $c$ on lattice offsets; its matrix is
$M_{x+v,\,x}=c_v$, so it moves an occupied site by $v$ with amplitude $c_v$.
Write $S$ for the declared **stencil**: the three offsets $\{0,a,-a\}$ along a
declared **axis** $a$, which is a nonzero offset taken modulo sign. There are
nine axes on the working lattice, four of them local (radius one) and five not,
and all nine are used — the axis set is exhaustive, not sampled.

Unitarity has a closed criterion. Writing the periodic autocorrelation
$$
A(m)\;=\;\sum_{v} c_v\,\overline{c_{v+m}},
$$
the matrix is unitary if and only if $A(m)=\delta_{m,0}$: the coefficient
sequence must have delta autocorrelation. The instrument uses this criterion and
independently confirms every generator by two further routes — the adjoint
product $U^{\dagger}U=I$ and unit modulus of the character transform — with zero
disagreements.

The coefficient alphabet is declared: $0$ together with $\zeta_8^{t}$ times a
modulus in $\{1,\tfrac12,\tfrac1{\sqrt2}\}$, twenty-five elements in all. The
sweep over the alphabet cubed is exhaustive at every swept axis order.

### 3.2 The collapse theorem

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
**at axis order five and above the only unitary generators on this stencil are the monomial ones**.

| $\operatorname{ord}(a)$ | distinct unitary generators | monomial | non-monomial |
|---|---|---|---|
| 1 | 8 | 8 | 0 |
| 2 | 32 | 16 | 16 |
| 3 | 24 | 24 | 0 |
| **4** | **72** | 24 | **48** |
| 5 | 24 | 24 | 0 |
| 6 | 24 | 24 | 0 |
| 7 | 24 | 24 | 0 |
| 8 | 24 | 24 | 0 |
| 9 | 24 | 24 | 0 |

*Scope: exhaustive over the declared 25-element alphabet cubed at each order;
the $\ge5$ row is a theorem, the order-3 emptiness is alphabet-relative and is
declared as such.*

The declared extension agrees: sweeping the five-point (von Neumann) stencil at
$L=5$ with autocorrelation pruning — 34,925 nodes visited, 121 complete
assignments surviving — returns no non-monomial unitary generator.

### 3.3 The unique scale

A local axis on $(\mathbb{Z}_L)^d$ has order exactly $L$; this is measured, not
assumed. Combining with section 2:

- locality on the stage requires $L\ge 4$ (measured, both connectives, three
  dimensions);
- a non-monomial local-axis generator requires $L\le 4$ (theorem above, plus the
  exhaustive alphabet sweep).

Therefore:
**L = 4 is the only lattice size in the swept range that carries both**.
The instrument computes the admissible set and gates it; a mutant that admits a
second size dies. At $L=4$ the family is not empty: the order-four axes carry
**72 distinct unitary generators, 48 of them non-monomial, in 9 gauge classes**.

This is a precheck: it selects which lattice is censused. It does not name the
verdict, and a gate proves it cannot — with the defect census zeroed, the head
moves while the scale datum does not.

### 3.4 The choice inventory

Fifteen construction choices are inventoried, each classed with an exact fibre.

| choice | class | fibre |
|---|---|---|
| the spatial dimension | FORCED (anchored) | 1 |
| the link set | FORCED (anchored) | 1 |
| the neighbourhood connective | GENUINELY-FREE | 2, both swept |
| the lattice size | FORCED (measured) | 1 of 8 swept |
| the coefficient alphabet | GENUINELY-FREE | 25 elements, swept exhaustively |
| the stencil | GENUINELY-FREE | 2 swept, a third declared not-swept |
| the axis set | FORCED (exhaustive) | 9 of 9 |
| the global phase | STABILIZER-FIXED | 8, free orbit, self-tested |
| the gauge representative | STABILIZER-FIXED | 8 |
| the division-event times | GENUINELY-FREE | declared |
| the leg at the cut | GENUINELY-FREE | declared |
| the brickwork coin | GENUINELY-FREE | 1 |
| the scramble permutations | GENUINELY-FREE | 2 |
| the symmetry group | GENUINELY-FREE | 2, both censused |
| the prepared-state set | GENUINELY-FREE | 18 |

The declared global phase is stabilizer-fixed rather than free because the
anchored gauge row makes the defect invariant under it; that invariance is
measured, with its own two-sided self-test (section 5.3).

## 4. The defect, and its census

### 4.1 The object

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

Three routes compute it, and they are genuinely different computations: the
definitional route on sparse matrices; the separation-indexed coefficient
convolution
$$
\Delta(s)\;=\;\Bigl\lvert\sum_t v_t\,u_{s-t}\Bigr\rvert^2-\sum_t \lvert v_t\rvert^2\lvert u_{s-t}\rvert^2 ;
$$
and the character-basis product transformed back. They agree everywhere they are
compared. The closed cross-term form of the anchored source is also computed and
agrees, but it is registered as FORCED — it is algebraically the same identity,
so it checks the implementation and measures nothing.

### 4.2 The census

The pool is **64 generators**: 58 translation-covariant circulants (the declared
family), 4 brickwork generators and 2 scrambled generators (the controls). The
census is **4096 ordered pairs**, one row per ordered pair, the count derived
from the pool.

**588 of 3364 pairs at maximal transport carry a nonzero defect.** Their values
form eight distinct exact numbers:

| value | cells | value | cells |
|---|---|---|---|
| $+5/8$ | 24 | $-3/8$ | 24 |
| $+1/2$ | 108 | $-1/2$ | 108 |
| $+1/4$ | 336 | $-1/4$ | 336 |
| $+1/8$ | 144 | $-1/8$ | 192 |

Every nonzero row at maximal transport is rational — 588 of 588 — although the
field carries irrational elements and the Born projection is never coerced out
of it. Each defect column sums to zero, as it must, both composites being
stochastic.

### 4.3 The Markovian control, gated in both directions

The Markovian sub-family is classified by measured support size: a generator is
monomial when its coefficient map has at most one nonzero offset, which makes
its transition matrix a deterministic shift and its process divisible across the
cut. Sixteen of the pool's generators are monomial.

**0 of 1792 Markovian pairs** carry a nonzero defect. This is the anchored
annihilator theorem — the row-monomial unitaries annihilate the defect against
everything — measured here rather than assumed: the pairwise sum through the cut
is literally empty.

The zero is a measurement because the same instrument returns nonzero on the
complementary set: 738 of 2304 free pairs are nonzero. And it is gated in both
directions. A mutant that mislabels a two-support generator as monomial dies at
the classifier. A mutant that injects a nonzero into a Markovian pair dies at the
Markovian gate. A mutant that zeroes every defect dies at the positive control.
And — the lesson the pin names — a mutant that zeroes only the *censused* defect
cells, leaving every count intact, dies at the value census, because the defect
gates are bound to the exact values and not merely to a count.

### 4.4 Locality dependence, at matched coordinates

Locality and transport are different axes. Non-local circulants transport
everything a local one does; they differ only in the radius of their stencil.
That is what makes the comparison possible at matched coordinates: the
order-four local and non-local axes carry the same nine gauge classes with the
same coefficient values, so the contrast can be read with the coefficient class,
the axis order and the gauge fixing all held equal, varying only the radius.

Of 1024 matched pairs, **616 have identical defect value multisets** on the
local and the non-local side. Over the whole maximal-transport census, 216 of
576 local pairs and 372 of 1188 non-local pairs are nonzero, with the same
maximal defect radius of 2 on both sides. The defect is therefore largely, but
not entirely, indifferent to the locality of the generators that produce it: the
matched table is the primary object and the contrast is read off it.

## 5. Two-point structure — the free-field analog

The phrase is used in one sense only: the objects below are the lattice
propagator and its correlators, the analog of a free field's two-point
functions. No field operator, no multi-excitation sector and no interaction term
is constructed.

### 5.1 The tables

*Equal time.* The connected correlator of the occupation observable on the
declared uniform state is
$C_0(x,y)=\delta_{xy}p(x)-p(x)p(y)$, exactly $15/256$ at zero separation and
$-1/256$ at every nonzero separation — the hard-core constraint of the
single-occupation sector, and translation invariant.

*Composed time.* The two-time correlator across the cut splits exactly:
$$
\underbrace{B(U_2U_1)}_{\text{coherent}}\;=\;\underbrace{B(U_2)B(U_1)}_{\text{restarted at the cut}}\;+\;\Delta^{B}(U_2,U_1).
$$
This is verified as an exact matrix identity on the probe pairs. **The
composition defect is the interference part of the two-time correlation
function**: the two-point structure and the defect census are the same table,
read two ways.

*Translation covariance, gated.* Every circulant's transition table is a
function of the lattice separation alone — not merely foldable without conflict,
but with every separation class wholly present and constant — and its defect
table folds without conflict on every pair. All 58 pass.

*The negative control.* Scrambling the lattice by a declared site transposition
breaks it measurably: both scrambled generators lose the full translation
stabiliser, neither transition table remains a separation table, and every one
of their 32 nonzero defect tables against the probe set fails to be one (16
further probes return an identically zero defect and are reported as such).

### 5.2 Decay and periodicity

The defect spreads over **16 separations** across the census, with maximum
defect radius 2 — the lattice half-width. The composed propagator's support
starts at the generator's own radius and never grows faster than one
neighbourhood per step; the bound holds at every generator and is not saturated
by all of them, because the torus wraps and because most of the family satisfies
a quadratic minimal polynomial. Six radius profiles occur across the first four
powers, among them $(1,1,1,0)$ at 16 generators, $(1,2,1,0)$ at 8, and
$(2,2,2,0)$ at 18; 33 of 58 attain the half-width.

Periodicity is reported projectively. The raw order of $U$ — the least $k$ with
$U^k=I$ — is *not* gauge invariant, since a global phase rescales every power;
the least $k$ with $U^k$ a scalar is. The projective periods present are
$\{1,2,4\}$; the raw orders are $\{2,4\}$. The gauge self-test confirms the
split: over 42 phase-and-generator combinations the projective period is
invariant at all of them and the raw order moves.

### 5.3 The defect algebra, self-tested

Reimplemented and measured on this family: the defect vanishes against the
identity on both sides; it is equivariant under conjugation of the pair by a
site permutation; transposing it reverses the pair; and the coherence law holds
on the declared 48 triples with zero violations — registered FORCED, because it
is an identity of associativity and constrains the family not at all.

The symmetry self-test required by the discipline is present in both directions
and evaluates fresh, with the product cache cleared and a cache-free
recomputation alongside: multiplying either factor by a global phase leaves the
defect fixed at every one of the checked pairs, while the one handle — an inner
diagonal inserted at the cut — moves it at every one of them. An invariance gate
whose negative direction never fires would be vacuous; this one's negative
direction fires everywhere.

## 6. Transformation-type classes

The Wigner move at finite scale: classify the family by orbits of the symmetry
group, and label the orbits by invariants.

Two groups are censused. The **anchored** group is the stage's own chart group —
the lattice translations together with the direction relabellings — of order 32.
This unit's declared **extension** adds the remaining square point symmetries,
order 128. Both act on generators by relabelling sites, and generators are
identified up to the declared global phase, since that phase is gauge.

There are
**22 transformation-type classes under the extended group and 38 under the anchored chart group**,
with sizes 1, 2 and 4. The orbits partition the pool;
the orbit-stabiliser identity holds on every class from the measured action; and
the declared class invariants — support, radius, transport level and projective
period — are constant on every orbit.

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

*Scope: the declared 64-generator pool at $d=2$, $L=4$, both declared groups,
generators identified up to the declared global phase.*

One reading deserves its own line. **The translation group acts trivially on the
whole circulant family** — every circulant is its own translate, all 58 orbits
under translations alone are singletons — while it acts non-trivially on the
controls. The classification is therefore carried entirely by the point
symmetries. That is measured, not assumed: a mutant that misreports the
translation action dies.

## 7. The realization census — the mandatory gate

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

The measured census is: 1 generator at NONE, 5 at OCC, 0 at OCC+AXIS, 58 at
FULL. The maximal declared transport attained is **FULL**, and the verdict's
defect segment is rebuilt from that subset alone.

The gate bites. **150 nonzero defects are excluded from the verdict** because
their pairs do not reach maximal transport — genuine nonzero measurements,
printed in the census rows, kept out of the verdict segment. The segment rebuilt
from the maximal-transport subset differs from the segment rebuilt from all
pairs, and a mutant that admits the sub-maximal defects dies; so does a mutant
that promotes every generator to maximal transport, and so does one that claims
nothing was excluded.

The brickwork controls are the substance of that exclusion. They are ordinary
local unitaries — a two-site coin applied on a parity class of dominoes, unitary
by construction and radius one — and they carry nonzero defects. What they do not
carry is full covariance: their stabiliser is the index-two subgroup that
preserves the parity, so they transport occupation but not the axis structure,
and their defects stay out of the verdict.

## 8. The state-motion check

The prepared states are declared: sixteen point masses, the uniform state, and
one wedge, eighteen in all. For a probe pair the observable defect is
$\delta(p)=\Delta^{B}p$, the difference between the coherent and the restarted
prediction on that state.

Two facts, measured together. First, the matrix reconstructed from the sixteen
point-mass responses equals the coefficient matrix $\Delta^{B}$ exactly: one and
the same coefficient serves every prepared state. The defect coefficient is
**background**. Second, the observable does move: there are
**18 distinct responses** across the eighteen declared states, so the instrument
that reported the background could have reported motion and did not.

This is the honest answer to the successor requirement that coefficients move
with the state. On this family they do not: the law is linear, the coefficient
sits behind every state, and only the observable moves. A mutant that makes the
reconstruction state-dependent dies; a mutant that freezes the observable dies.

## 9. What this decides, and what it does not

**Decided, at the declared scope.**

- On a $d=2$ periodic lattice of size 4 with occupation configurations and
  declared local moves, a spatially structured indivisible family exists and its
  composed segments carry a nonzero composition defect: 588 of 3364 pairs at
  maximal declared transport, eight distinct exact rational values, spread over
  16 separations with maximal defect radius 2.
- The Markovian sub-family returns exactly zero, gated in both directions and
  bound to the value census.
- The defect is the interference part of the two-time correlator; the
  equal-time correlator is the hard-core constraint of the sector.
- The family carries 22 transformation-type classes under the extended group and
  38 under the anchored chart group, with support, radius, transport level and
  projective period constant on each.
- The defect coefficient is background; only the observable moves with the
  prepared state.
- One lattice size in the swept range admits the construction at all.

**Not decided, and not attempted.**

- No continuum or infinite-volume limit is taken. Nothing here is a statement
  about a field theory; in the physics, "field" is used only as the free-field
  analog.
- No multi-excitation sector, no interaction term, no field operator. The only
  interaction-shaped object is the composed-segment defect itself.
- The 9-point stencil is not swept. Only the 3-term axis stencil (exhaustively,
  at every swept order) and the 5-point stencil (at one size above the collapse
  threshold) are.
- Coefficients outside the declared 25-element alphabet are not swept. The
  order-5-and-above collapse is a theorem and alphabet-independent; the
  order-3 emptiness is alphabet-relative and is declared so.
- $d=3$ is swept for the locality threshold only, not for the family.
- The excluded 150 nonzero defects are real measurements at sub-maximal
  transport. They are printed, not promoted; whether a weaker transport
  declaration should admit them is a question for a successor, not a finding
  here.

## 10. The instrument

**77 gates, all passed; 24 anchors; 82 declared mutants, all dead** — and every
mutant killed by the gate it was declared to falsify. Seventy-five gates carry a
declared falsifier. Two carry a registered forcing instead: the gate that
records the shape of the defect definition, which is analytically true by
construction and is a disclosure rather than a measurement (its content is
measured against the anchored two-by-two witness), and the waiver-verification
gate itself, which runs after the mutant harness and therefore carries its own
in-gate injection falsifier — a synthetic waiver with no registered forcing,
which the same predicate must detect.

Controls run in both directions throughout: the Markovian zero against the free
nonzero; the gauge invariance against the handle that moves it; the covariant
circulants against the scrambled control; the maximal transport against the
excluded sub-maximal defects; the background coefficient against the moving
observable.

Determinism: two plain runs, byte-identical in both artifacts. Falsification
self-test: breaking any pinned anchor's expected digest exits 1 visibly at the
anchor gate.

The compliance sweep enumerates each engraved rule with a computed status,
including all eight of the standing 2026-08-09 engravings — complete-string
verdict equality against an independent reconstruction; rendering from the gated
object; prose rendering from the receipt; compliance claims shipping with
injection-falsifiers; path-value anchoring; verified waiver claims;
verbatim-text anchors evaluated first and bound to named consumers; and no
unanchored runtime inputs.
