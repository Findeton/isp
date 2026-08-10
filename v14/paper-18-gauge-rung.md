# R5 — the gauge rung: link-indexed unitaries and their holonomy

**Status:** `DELIVERED-PENDING-ADJUDICATION` — built against the frozen pin
`v14/note-r5-gauge-pin.md`, whose design authority is the frozen R4-effectus
review's R5 recommendation. Verified to run: two plain runs byte-identical,
every gate passed, every declared mutant dead at its declared target, the
falsification self-test fatal and writing nothing. Between delivery and
adjudication every headline below is a candidate reading.

## The Holonomy Is the Full Alternating Group on Its Own Support, and the Gate That Would Have Found It Admits Nothing

**Unit:** R5 (the gauge rung), v14, paper #18, pinned at v14 ledger #129 (its own).
**Instrument:** `v14/code/r5_gauge_exact.py`.
**Artifacts:** `v14/code/r5_gauge_output.txt`,
`v14/code/r5_gauge_receipt.json`.
**Inheritance, hash-verified at run time and by no other route:** the stage,
the coefficient alphabet, the brickwork controls and the abelian stratum come
from R4, `v14/paper-10-defect-on-the-stage.md` (`1063401c7bb5`) with its
receipt (`3dc1393b0df8`), terminal at commit 583cae7; the seal discipline and
the two carried handoffs come from R4b, `v14/paper-15-momentum.md`
(`89c636906061`) with its receipt (`562e2a3d4d85`), terminal at commit
6d32993; the design is the frozen R5 recommendation of
`v14/review-r4-effectus.md` (`f54fa11dfd07`); the pin is
`v14/note-r5-gauge-pin.md` (`b53adba0eee0`); the group-family prior is CR-D's
tower, `v14/paper-08-tower-four-wings.md` (`602c9ac2ccc4`). Every object below
is **reimplemented** from those definitions; nothing is imported from any
other unit's program.
**Anchors are (path, value) pairs and (context, consumer) pairs, not only file
bytes:** 9 file-bytes anchors, 17 path-value anchors and 14 verbatim-text
anchors, 40 anchors in all — each verbatim window pinned by the digest of its
exact bytes and by a declared length floor, and each bound to the gate that
consumes it.
**Runtime inputs (engraving #46):** exactly the nine hash-pinned sources
above, plus exactly one file read as the *object under test* — this paper,
which the delivery run reads and gates its own numeric claims against, and
which cannot be pinned against itself. Both lists are enumerated and gated. No
ledger, no status board, no other unit's working file, and no subprocess: the
import list and the attribute-call list are read off the instrument's own
syntax tree, so the run is correct off-tree and in a directory with no version
control at all (#91).
**Exact arithmetic only:** the field is $\mathbb{Q}(\zeta_8)$ carried as
integer 5-tuples $(a_0,a_1,a_2,a_3,\mathrm{den})$ over the basis
$(1,z,z^2,z^3)$ reduced modulo $\Phi_8(x)=x^4+1$, in lowest terms; the
representation is canonical, so tuple equality is field equality. Group orders
come from a deterministic Schreier–Sims over the integers. An AST scan of the
instrument's own source and a recursive type scan of the emitted receipt are
gates.
**The seal (#119), native from birth:** every published object is digested at
the moment its gate passes, the payload may be sealed only if every earlier
seal still verifies, and the artifacts are written from the sealed payload
through temporaries moved into place only after the bytes on disk match the
gate-time digests.

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field, and the complete string —
head included — is compared for equality against an *independent
reconstruction* that derives the head by its own copy of the head law, reads
only the serialized receipt, and shares no helper, no input and no typed value
with the builder:

```
R5-NON-ABELIAN-<CLASS=ALTERNATING-ON-ITS-OWN-SUPPORT(S1-ONE=A3<S2-EDGE=A5<S2-CORNER=A3 x A3<S2-APART=A3 x A3<S3-ROW=A7<S4-BLOCK=A8);RANK=8-OF-16-DECLARED-PLAQUETTE-GENERATORS-ARENA-RELATIVE;COMMUTATOR-SUBGROUP=NONTRIVIAL-AT-576-OF-640-UNIFORM-COINS|GATE=INHERITED-PER-GENERATOR-FULL-ADMITS-0-OF-52(R5-BLOCKED-AT-THE-GATE-AT-THAT-READING);MAXIMAL-PER-GENERATOR-LEVEL=NONE;DECLARED-GATE=FAMILY-COVARIANCE-512-OF-512-CHECKS|CURVATURE-DEFECT=CURVATURE-DEFECT-INDEPENDENT(LINK-GRAIN=MUTUALLY-EXCLUSIVE-BY-THEOREM-0-OF-1920-BOTH;PLAQUETTE-GRAIN=ALL-FOUR-CELLS-384-BOTH;TWO-EXCITATION=EXCLUSIVITY-SURVIVES-0-OF-9-BOTH;PARENT-BASELINE=588-DEFECTS-AT-ZERO-CURVATURE)|CONTROL=FULL-STRATUM-FLAT-0-OF-3364-TRIVIAL-GROUP|REFINEMENT=LOCAL-STABLE-GLOBAL-EXTENSIVE(LOCAL-STABLE-6-OF-6;GLOBAL-A16-TO-A64)|SCRAMBLE=SEPARATES-LOCAL-12-OF-12;FAILS-GLOBAL-0-OF-2|INTERFERING-SECTOR=INFINITE-ORDER-512-OF-512-BY-TRACE-NON-INTEGRALITY|SCOPE=D=2;L=4;REFINED-TO-8;FIELD=Q(ZETA-8);ALPHABET=25;COINS=640;LINKS=32;PLAQUETTES=16;CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));STENCIL=2-SITE-DOMINO-PER-LINK;SECTOR=SINGLE-OCCUPATION;SWEPT-RANGE=UNIFORM-CONFIGURATIONS-EXHAUSTIVE-OVER-THE-COIN-ALPHABET;NON-UNIFORM-CONFIGURATIONS=NOT-SWEPT;INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-CONFINEMENT-CLAIM>
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and the datum it had to start from

Does the declaration-connection on the record stage carry a non-abelian
holonomy group, does it survive one refinement step, and does its curvature
couple to the composition defect $\Delta^{B}$?

The pin required this unit to state one inherited fact before anything else,
and the reason is that the fact decides where a gauge rung may honestly be
built. R4's verdict-bearing stratum is **abelian**: of its ordered pairs of
translation-covariant circulants, `0 of 3364` fail to commute. Every plaquette
holonomy and every Wilson loop assembled from that stratum is the identity by
a theorem — circulant convolution on an abelian group commutes — and the only
non-commuting generators on R4's stage are the four brickwork generators,
which are exactly the ones R4's mandatory realization gate excludes. A gauge
rung built on R4's verdict stratum would have returned a trivial answer at
exit 0 and could not have been falsified.

So R5 builds on the **excluded** sub-maximal stratum, promoted to a first-class
family, and keeps R4's stratum as the provably flat negative control. Both
halves of that sentence are measured here rather than quoted: this unit
rebuilds the circulant family from its own definitions, recovers `58
circulants`, recomputes the whole ordered-pair census and finds `0 of 3364`,
and confirms that the direction-indexed connection assembled from them has the
trivial holonomy group. Without a negative control that is *provably* flat, a
non-abelian result elsewhere in the unit would be uninterpretable.

**What would have answered the other way.** Four outcomes were pre-registered
in the pin and all four are reachable by the one head law, demonstrated on
synthetic censuses inside a gate: `R5-BLOCKED-AT-THE-GATE` if no declared gate
admits a family, `R5-BLOCKED-AT-THE-COMMUTATOR-SUBGROUP` if the holonomies all
commute, `R5-BLOCKED-AT-THE-SCRAMBLE-CONTROL` if the group fails to separate
the physical case from a scramble, and `R5-NO-STABLE-GROUP` if no class
survives refinement. The head is computed from the measured counts and cannot
be typed: a mutant that retypes it after every verdict gate has been built dies
at the string-equality gate, and a mutant that makes the head law constant dies
because, run on a census whose declared gate admits nothing, the head it
produces fails to move.

## 2. The arena, declared as data

**The stage.** The lattice is $X=(\mathbb{Z}_L)^2$ with $L$ taken from R4's
receipt at a named path, not typed here: `L = 4`, at the anchored dimension
`d = 2`. That gives 16 sites, and the single-occupation sector makes the
carrier $\mathbb{C}^{16}$. The link set and the plaquette set are derived from
the lattice rather than declared: two links per site and one unit square per
site, so `32 links` and `16 plaquettes`. The neighbourhood connective is
inherited verbatim from the parent as a forced choice —
`CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))` — and this arena does not
get to choose it either.

**The strata.** R4's brickwork generator is a two-site coin applied on a parity
class of dominoes. Generalising it so the coin may vary link to link gives
`four parity strata` — the $x$-links at even and at odd $x$, the $y$-links at
even and at odd $y$ — and each is measured to be a **perfect matching** of the
site set: eight disjoint dominoes covering all 16 sites. That is what makes a
stratum operator a product of pairwise commuting link operators, and it is
gated rather than assumed.

**The coin alphabet is derived, not chosen.** R4 declares a coefficient
alphabet of `25 elements`: zero together with $\zeta_8^{t}$ at each of the
three declared moduli. A *coin* here is a two-by-two unitary
all four of whose entries lie in that alphabet, and the enumeration is
exhaustive over the alphabet's fourth power. It returns `640 coins`, and the
support pattern splits them into three sectors with nothing left over:
`64 diagonal, 64 antidiagonal and 512 balanced`. Nothing about the size is
typed; unitarity is confirmed by a second route, $U^{\dagger}U=I$ written out,
on every one of them. The row analysis behind the split is worth one line
because it is what makes the family finite: a row of squared moduli drawn from
$\{0,\tfrac14,\tfrac12,1\}$ can sum to 1 only as $(1,0)$, $(0,1)$ or
$(\tfrac12,\tfrac12)$, and orthogonality then forbids a mixed pair of rows.

**The link-indexed unitary.** For a link $\ell$ and a coin $U$, the operator
$L(\ell,U)$ acts as $U$ on the two-dimensional span of the link's own domino
and as the identity on every other site. This is precisely the single-link
factor of R4's brickwork generator; the stratum operator is the product of the
eight that make up a parity class. A configuration assigns a coin to every
link.

**The plaquette holonomy.** For the plaquette based at $x$ with corners
$x,\;x+e_1,\;x+e_1+e_2,\;x+e_2$, the holonomy is the ordered product of the
four link operators around the boundary, each inverted where the boundary runs
against the link's own direction:
$$
W_p \;=\; L(\ell_4)^{-1}\,L(\ell_3)^{-1}\,L(\ell_2)\,L(\ell_1).
$$
Each factor is the identity off the plaquette's four corners, so $W_p$ is too:
the whole holonomy lives in a four-by-four block, which is why a census over
the entire coin alphabet is finite work rather than a sample. Unitarity of
$W_p$ is gated on every swept configuration.

**What is swept and what is not.** The uniform configurations — one coin
repeated on every link — are swept **exhaustively** over the coin alphabet:
`640 coins`, all of them. The full configuration space is $640^{32}$ and is
**not** swept. That restriction is declared here, carried in the verdict's
`SWEPT-RANGE` segment as `NON-UNIFORM-CONFIGURATIONS=NOT-SWEPT`, and named
again in section 8 among the things this unit does not decide. It is a
disclosed window with the corpus's own precedent, never a silence.

**The two groups.** The anchored chart group — the lattice translations
together with the direction relabelling — has `order 32`; this unit's declared
extension by the square point group has `order 128`. Both are censused, as R4
censuses them.

**The choice inventory.** 15 construction choices are inventoried, each classed
with an exact fibre: the dimension, the lattice size, the connective, the
coefficient alphabet, the coin alphabet, the link set, the plaquette set and
the parity strata are all FORCED with fibre 1, either by an anchor or by an
exhaustive derivation; the loop base point and orientation and the global phase
are STABILIZER-FIXED with fibres 4 and 8; the division-event times, the leg at
the cut, the six declared plaquette stencils, the three gauge handles and the
two-excitation extension are GENUINELY-FREE, the last with fibre 2 because the
symmetric square is the other unitary option at fixed dimension.

## 3. The holonomy group

### The curvature census

For each of the 640 uniform configurations the instrument builds the holonomy
at a base plaquette and at its edge-neighbour and asks two questions: is the
holonomy the identity, and do the two holonomies commute. Of the 640,
`632 of 640 are non-flat`, and the commutator subgroup is non-trivial at
`576 of 640 uniform configurations` — every antidiagonal and every balanced
coin, and no diagonal one.

| sector | coins | non-flat | non-commuting |
|---|---|---|---|
| DIAGONAL | 64 | 56 | 0 |
| ANTIDIAGONAL | 64 | 64 | 64 |
| BALANCED | 512 | 512 | 512 |

The diagonal row is the arena's own abelian arm and is carried rather than
dropped: simultaneously diagonal link operators commute, so `0 of the 64
diagonal coins` produce a non-commuting pair, while 56 of them still produce a
non-trivial holonomy. Curvature and non-commutativity are separated already in
this first table, in the precise sense that $W_p \neq I$ on 56 coins whose
every commutator vanishes.

**G1 is decisive and it passes.** The commutator subgroup of the
plaquette-holonomy group is non-trivial, on an arena whose provably flat
control returns the trivial group.

### The group, as an isomorphism class

The group is reported as an isomorphism class with its rank, and never as
matrices. On the two monomial sectors every plaquette holonomy is a monomial
matrix over the eighth roots of unity, so the group acts faithfully on the
$16\times 8$ pairs (site, phase) and is a **permutation group**: its order is
an exact integer from a deterministic Schreier–Sims, and its position part —
the image in the symmetric group on the 16 sites — is the object the class is
read from.

The certificate is set equality and nothing weaker. Every generator preserves
each orbit of the group and restricts to an even permutation of it, so the
group is contained in the direct product of the alternating groups on its
orbits; the measured order equals that product's order; containment together
with equal cardinality is equality. No fingerprint of element orders, no
heuristic, and no matrix enters the receipt.

Measured at the six declared plaquette stencils and at the global one, on
every one of the 64 antidiagonal coins:

| stencil | plaquettes | support | order | class |
|---|---|---|---|---|
| S1-ONE | 1 | 3 | 3 | $A_3$ |
| S2-EDGE | 2 | 5 | 60 | $A_5$ |
| S2-CORNER | 2 | 6 | 9 | $A_3 \times A_3$ |
| S2-APART | 2 | 6 | 9 | $A_3 \times A_3$ |
| S3-ROW | 3 | 7 | 2520 | $A_7$ |
| S4-BLOCK | 4 | 8 | 20160 | $A_8$ |
| S-ALL | 16 | 16 | 10461394944000 | $A_{16}$ |

*Scope: exhaustive over the antidiagonal sector of the derived coin alphabet
at every listed stencil; the class is identical at all 64 of them. On the
diagonal sector the position group is trivial at every stencil — the holonomy
there is pure phase — and that sector is reported separately below.*

**The measured law is one sentence.** The holonomy group is
**the FULL alternating group on its own support** — and at a stencil whose
plaquettes do not share a link, the direct product of the full alternating
groups on the components. The ladder the declared stencils trace is
`S1-ONE = A3 < S2-EDGE = A5 < S2-CORNER = A3 x A3 < S2-APART = A3 x A3 < S3-ROW = A7 < S4-BLOCK = A8`,
and the mechanism is visible in the smallest case: with the swap coin the
holonomy of a single plaquette is a **three-cycle** on three of that
plaquette's four corners, and three-cycles whose supports overlap generate the
alternating group on the union.

The **rank** is measured and is arena-relative, which the verdict says in as
many words: it is the least number of the *declared plaquette holonomies* that
generate the whole group, not the abstract minimal generator number of the
abstract group. At the global stencil it is `rank 8 of the 16 declared
plaquette generators`, found by exhaustive search over subsets pruned by the
necessary covering condition; at the six local stencils it is 1, 2, 2, 2, 3 and
4 respectively, so every declared local generator is needed and none is
redundant.

The phase part is measured too and is not folded into the class. At every
local stencil the phase kernel — the part of the monomial group lying in the
diagonal — is trivial, so the position group *is* the group. At the global
stencil it is trivial for 32 of the antidiagonal coins and of order 32768 for
the other 32, split by the parity of the coin's upper-right phase. On the
diagonal sector the position group is trivial outright and the whole holonomy
group is phase, of order 1, 4096, 16777216 or 68719476736 according to the
coin. Both are measured stratifications of the arena, not corrections to the
class.

### The interfering sector has no finite class, and that is a theorem

On the 512 balanced coins the holonomy is not monomial, and the group is
**infinite**. The certificate is not a search cap: a matrix of finite order has
root-of-unity eigenvalues, so its trace is a sum of roots of unity and hence an
algebraic integer. Every one of these traces has a denominator — `512 of 512`
of them — so no power of the holonomy is the identity, and there is no finite
isomorphism class there to report. The projective periods agree and are
reported on R4's own template, since the raw order is not gauge invariant while
the least exponent at which the holonomy becomes a scalar is: the diagonal
sector reaches $\{1,2,4,8\}$, the antidiagonal sector reaches $\{3\}$ uniformly,
and the balanced sector reaches no such exponent within the declared cap of 32.

This is the sharpest single structural fact the unit measures, and it is worth
stating without decoration. **The sector that carries the composition defect is
exactly the sector whose holonomy group is infinite, and the sector whose
holonomy group is a finite alternating group carries no defect at all.** The
next section makes that quantitative.

### The flat control

R4's FULL-transport stratum is rebuilt here from its own definitions —
coefficient maps on the three-term axis stencil, unitary by the delta
autocorrelation criterion, quotiented by the declared global-phase gauge, every
gauge orbit of full size 8 — and returns `58 circulants` over 9 axes. Its whole
ordered-pair commutator census is recomputed by the coefficient convolution and
independently on explicit matrices for a declared sample, with 0 disagreements
between the two routes, and gives `0 of 3364`. The direction-indexed connection
assembled from that stratum has the trivial holonomy group, of order 1. The
control is provably flat, and it is the reason the alternating result above is
a measurement rather than an artifact of the instrument.

## 4. The gate-inheritance audit

The pin forbids inheriting R4's realization gate unmodified, and requires this
unit to state at construction whether *maximal declared transport* is compatible
with non-abelian holonomy on this arena. The answer is measured, and it is the
unit's second headline.

R4's ladder is reimplemented here: a generator is at NONE when its translation
stabiliser is trivial, at OCC when the stabiliser is a non-trivial proper
subgroup, at OCC+AXIS when it is the whole translation group, and at FULL when
in addition its image under every chart element is again a family member up to
the declared gauge, with the transported label. Applied per generator to the
objects this arena actually has:

| kind | objects | measured level |
|---|---|---|
| link operator | 32 | NONE, all of them |
| plaquette holonomy | 16 | NONE, all of them |
| stratum operator | 4 | OCC, all of them |

The reason is not subtle and is exactly why it matters: conjugating a link
operator by a translation moves the *link*, so $T_v L(\ell,U) T_v^{-1} =
L(\ell+v,U)$, and the stabiliser is trivial for every non-identity coin. The
maximal declared level is attained by `0 of the 52` objects censused. **Under
the inherited gate read per generator, this unit's verdict is
`R5-BLOCKED-AT-THE-GATE`**, and the verdict string carries that reading as its
own segment. The gate motivated by one unit's transport question does not merely
project onto the abelian sector at the next arena, as the review anticipated —
on this arena it empties the family outright.

The unit does not stop there, because the pin's own gate requires the criterion
to be re-derived rather than obeyed, and the re-derivation locates the trouble.
A gauge family's link variables are *never* individually translation-invariant;
that is what makes them link variables. What is covariant is the **family**: the
image of any link operator under any chart element is again a link operator, on
the transported link, with the transported coin — the swap conjugate where the
point part reverses the direction. That is R4's own FULL criterion read at the
level at which a link-indexed family has it, and it is measured here, over the
extension of order 128 acting on the link set, at `4096 of the 4096 checks`, with
the link set itself gated closed under all 5120 chart actions of both groups.

So the answer to the pin's question is two-sided and both sides are in the
verdict. Read per generator, maximal declared transport is **incompatible** with
non-abelian holonomy on this arena, because at that level the arena is empty.
Read at the family level — the level at which the criterion was meant to bite —
it is **compatible**, and the holonomy measured under it is non-abelian. The
per-generator stabiliser is simply the wrong instrument for a gauge family, and
that is a real result about the programme's own gate rather than about this
arena.

## 5. Curvature against the defect, at matched coordinates

The composition defect is reimplemented from the seed's definition,
$$
\Delta^{B}(U_2,U_1)\;=\;B(U_2U_1)\;-\;B(U_2)B(U_1),\qquad B(U)=\lvert U\rvert^{\circ 2},
$$
with the division events declared at $t=0$ and $t=2$, the cut at $t=1$ declared
not to be one, and the leg across it declared to be $B(U_2)$. The
reimplementation is checked against the seed's own named two-by-two witness: on
the Hadamard against itself it returns the half-and-minus-half matrix exactly,
and a sign flip of that witness dies at the gate.

The matched table is the primary object. Four coordinates are held equal in
every row — the coin value, the division-event times, the leg at the cut, and
the gauge fixing — and exactly one coordinate varies per table.

**At link grain.** Rows are ordered pairs of link operators; the varying
coordinate is the geometric relation between the two links, and the coin is
swept exhaustively over the alphabet at each relation.

| relation | neither | defect only | curvature only | both |
|---|---|---|---|---|
| SAME-LINK | 256 | 384 | 0 | 0 |
| SHARE-ONE-SITE | 64 | 0 | 576 | 0 |
| DISJOINT | 640 | 0 | 0 | 0 |

`0 of the 1920 rows carry both`. `576 rows carry curvature and no defect`, and
`384 carry a defect and no curvature`. The two are **mutually exclusive** at
this grain, and the exclusion is a theorem rather than a tally.

> **Theorem (single path).** *Let $\ell_1$ and $\ell_2$ be links sharing at most
> one site, and let $U_1,U_2$ be the corresponding link operators for any coins
> whatever. Then $\Delta^{B}(U_2,U_1)=0$.*
>
> *Proof.* Write the shared site $b$, so $U_1$ is supported on $\{a,b\}$ and
> $U_2$ on $\{b,c\}$ with $a\neq c$ (the disjoint case is the same argument with
> the supports separated). An entry of the composite is
> $(U_2U_1)_{ij}=\sum_k (U_2)_{ik}(U_1)_{kj}$, and $(U_2)_{ik}$ is non-zero only
> for $(i,k)$ inside $\{b,c\}^2$ or on the diagonal outside it, and likewise
> $(U_1)_{kj}$ only inside $\{a,b\}^2$ or on the diagonal. Enumerating the five
> admissible $(i,j)$ shapes gives exactly one surviving $k$ in each. A sum with
> one term has nothing to interfere with, so $B(U_2U_1)=B(U_2)B(U_1)$
> entrywise. $\square$

Two link operators fail to commute only when their links share exactly one
site. Curvature therefore *implies* the single-path condition, which *implies*
zero defect: the cell that would carry both is empty by the theorem, over every
coin alphabet and not only this one. The defect-only cell is populated exactly
by the same-link rows, where the composite is $U^2$ and genuinely interferes.

**At plaquette grain.** Rows are ordered pairs of plaquette holonomies, and the
same contrast is taken with the same coordinates held equal.

| relation | neither | defect only | curvature only | both |
|---|---|---|---|---|
| SAME-PLAQUETTE | 128 | 512 | 0 | 0 |
| SHARE-AN-EDGE | 64 | 0 | 192 | 384 |
| SHARE-A-CORNER | 128 | 0 | 512 | 0 |
| DISJOINT | 640 | 0 | 0 | 0 |

Here `384 rows carry both`, and all four cells are populated. The row that
carries both is the edge-sharing one, where the two holonomies overlap on two
sites rather than one — precisely the support at which the single-path count
fails. So the exclusivity is a statement about the **generators** and not about
the connection they build, and the grain is a declared coordinate of the result
rather than an incidental choice. Taken together with R4's measured baseline —
`588 defects at identically zero curvature` — the pre-registered outcome is
`CURVATURE-DEFECT-INDEPENDENT`: neither predicate implies the other, and each
direction has a witness in numbers.

**The must-not, gated rather than promised.** Curvature does not imply quantum
character on this stage. The instrument gates that there exist non-commuting
pairs with identically zero defect, in numbers, at both grains; R4 supplies the
converse witness. The implication is settled negative in both directions and
nothing in this unit asserts it.

**The one declared two-excitation extension, pre-registered and run.** R4 named
exactly three routes out of its frozen-stage arena, and the cheapest is a
two-excitation sector. This unit declares one and runs it: the hard-core
antisymmetric sector $\Lambda^2$, on `120 two-excitation states`, the forced
choice at fixed dimension up to the symmetric square, which the choice inventory
carries with fibre 2. The extension returns a **negative**: `0 of 18` rows carry
both, so at link grain the exclusivity **survives** one dimension up. The reason
is the same counting argument — the exterior square of an operator supported on
two sites still admits at most one intermediate two-particle state between any
given pair of endpoints — and the pre-registered route out of the arena does not,
at this grain, get out.

## 6. The gauge self-test, in both directions

The declared gauge action is site-diagonal: $g=\mathrm{diag}(\zeta_8^{\theta_x})$
acting on link operators by conjugation. Three handles are declared — CONSTANT,
LINEAR-X and CHECKER — and the first is the null handle, the global phase, which
is central and therefore *must* move nothing.

The positive direction is reported with its forcing named, because it is forced:
the Wilson trace is invariant under any conjugation whatever, by cyclicity, so
its invariance at every checked loop is a disclosure and not a measurement. What
is measured is the negative direction, and it fires everywhere it can. Under
each declared non-constant handle the **untraced** holonomy moves at every one
of the 16 checked loops, on both non-abelian arms, `64` loop-moves over the 4
live rows; under the null handle it moves at none of them.

The third row of that table is a measurement about the arena and is kept: on the
abelian arm the untraced holonomy moves at **no** loop at all, because a
diagonal holonomy commutes with every site-diagonal gauge. The abelian arm's
holonomy is already gauge invariant, which is the structural reason it can be
reported without a conjugacy-class caveat while the others cannot.

Finally the action is gated to map the family to itself: every site-diagonal
conjugate of a link operator is again a link operator on the same link with a
coin from the same derived alphabet, checked on every named coin, every handle
and every link. So the holonomy enters every claim in this paper only as a
conjugacy class, and R4's projective-period self-test is the template this
section follows — the raw order moves under the gauge, the projective period
does not.

## 7. Refinement, and the scramble caveat

**Refinement.** The pin's charter question is whether the class survives one
refinement step. The declared doubling takes the lattice to `L = 8`: 64 sites,
128 links, 64 plaquettes. The step is decided in the symmetric group and never
touches the field, so it is cheap and exact.

| stencil | class at L = 4 | class at L = 8 |
|---|---|---|
| S1-ONE | $A_3$ | $A_3$ |
| S2-EDGE | $A_5$ | $A_5$ |
| S2-CORNER | $A_3 \times A_3$ | $A_3 \times A_3$ |
| S2-APART | $A_3 \times A_3$ | $A_3 \times A_3$ |
| S3-ROW | $A_7$ | $A_7$ |
| S4-BLOCK | $A_8$ | $A_8$ |
| S-ALL | $A_{16}$ | $A_{64}$ |

The isomorphism class is the invariant and the plaquette count is the extensive
control, and the two come apart exactly where the table says they do. At `6 of 6
declared local stencils` the class is **identical** at the two sizes; at the
global stencil it is `A16 at L = 4 and A64 at L = 8`, of order
`10461394944000` at the smaller size. The refinement verdict is therefore
`LOCAL-STABLE-GLOBAL-EXTENSIVE`, and `NO-STABLE-GROUP` is refuted for the local
readings and confirmed for the global one. Success at `6 of 6 declared local
stencils` is a stable non-abelian isomorphism class under refinement; the global
group is an extensive object that grows with the lattice and is not an invariant
of any refinement limit.

**Against CR-D's ladder.** G6 requires the class to be reported against the
programme's existing group-family prior, and the comparison is closer than a
family resemblance. CR-D's tower reported, at every realised rung, exactly
`the FULL alternating group on its own support` — $A_5$ on a five-point support,
$A_{11}$ on eleven, $A_{15}$ on fifteen. This arena returns the same **form** by
an independent route, with CR-D's own $A_5$ reappearing at the five-point
stencil and $A_7$, which CR-D's ladder tops out at, appearing here at the
three-plaquette row. Two units, two arenas, one form: where these constructions
produce a finite group at all, they produce the whole alternating group on
whatever support they touch. The alternating-family prior is confirmed on the gauge rung.

**The scramble caveat, and it bites.** Γ-main's standing warning is that a group
reading is not automatically a discriminating statistic, and the pin makes the
separation a precondition on any group claim. Two scrambles are declared — a
transposition of link labels and a direction flip — and applied to the boundary
assembly, so the four operators multiplied are no longer the four edges of a
loop.

| stencil | physical | scramble 1 | scramble 2 |
|---|---|---|---|
| S1-ONE | 3 on 3 points | 4 on 6 points | 5 on 5 points |
| S2-EDGE | 60 on 5 points | 720 on 8 points | 20160 on 8 points |
| S2-CORNER | 9 on 6 points | 5040 on 9 points | 25 on 10 points |
| S2-APART | 9 on 6 points | 12 on 9 points | 20160 on 8 points |
| S3-ROW | 2520 on 7 points | 40320 on 10 points | 1814400 on 10 points |
| S4-BLOCK | 20160 on 8 points | 1814400 on 10 points | 239500800 on 12 points |
| S-ALL | $A_{16}$ | $A_{16}$ | $A_{16}$ |

The local profile separates the physical connection from both scrambles at
`12 of 12` stencil-and-scramble pairs. The global class separates at neither:
`neither scramble separates the global class` — a product of four
transpositions is even however the links are chosen, and both scrambles are
measured to reach the whole of $A_{16}$ from there. So the group
claim is entered where it separates — at the local stencils — and the global
class is entered as measured-but-not-discriminating. That is the caveat doing
exactly the work it was pinned to do, and it is the reason the verdict's CLASS
segment carries the local ladder rather than $A_{16}$.

## 8. What this decides, and what it does not

**Decided, at the declared scope.**

- The declaration-connection on this stage carries a non-abelian holonomy
  group. The commutator subgroup is non-trivial at `576 of 640 uniform
  configurations`, on an arena whose provably flat control returns the trivial
  group at `0 of 3364`.
- Where the group is finite, its isomorphism class is
  `the FULL alternating group on its own support`, certified by set equality
  and reported with its rank; at a disconnected stencil it is the direct
  product over the components.
- The class survives one refinement step at every declared local stencil and
  does not at the global one: the holonomy has stable local content and
  extensive global content.
- On the interfering sector the group is infinite, certified by a theorem about
  traces rather than by a search cap.
- Curvature and the composition defect are independent predicates. At the grain
  of the generators they are `mutually exclusive` by theorem, in the
  single-excitation sector and in the declared two-excitation extension alike;
  at the grain of the holonomies all four cells are populated.
- R4's realization gate, inherited unmodified and read per generator, admits
  nothing on this arena; read at the family level it admits the whole family.
  Both readings are in the verdict.

**Not decided, and named.**

- **The non-uniform configurations.** Only the uniform configurations are swept.
  A coin that varies link to link is the general object this arena was built for,
  and the group census over it is open. Nothing here shows the alternating law
  survives it; nothing here shows it fails.
- **The balanced sector's group.** It is infinite, and that is all this unit
  says about it. Its structure — whether it is dense in a compact group, whether
  it has a finite image worth naming — is untouched.
- **Confinement.** No confinement-analog claim is entered anywhere, in the
  verdict or in the prose, and the scope segment says so. G1 passing is a
  precondition for that language, and it is a precondition and not a licence:
  the objects that would carry such a claim — an area law, a static potential,
  a large-$N$ limit — are absent from this arena entirely.
- **Any quantum reading of curvature.** Settled negative in both directions,
  above.
- **The phase kernel's meaning.** Its order is measured and its discriminant is
  measured. What the 32768 counts is not interpreted here.
- **The refinement limit.** One step is not a limit. `L = 8` is the declared
  doubling; the sequence beyond it is untouched, and the global class is already
  known to move.

**The two carried handoffs, and their limits.** R4b's NOT-BLOCH-DIAGONAL is a
theorem about the brickwork classes and is cited, not re-derived. No transport
number is inherited from R4b at all — its scope is the single-occupation uniform
average — and the anchor list is gated to take no value from that receipt, which
is how the restriction is enforced rather than promised.

## 9. The instrument

The instrument is `v14/code/r5_gauge_exact.py`, and its contract is the era's
minimum (#82): a delivery run that is the only writer, a `--no-write` twin, a
falsification self-test that corrupts one anchor in memory and must die writing
nothing, a per-mutant runner, an anchor breaker, and a `--verify-paper` mode
that rebuilds the whole derivation with a named file as the object under test.
Every documented behaviour is exercised inside a gate; no flag is a no-op and no
flag is mutant-only.

61 gates, 60 of them evaluated inside the receipt.
58 carrying their own injection falsifier and 3 their registered forcing —
the three exceptions are the mutant-sweep adjudicator, the artifact-integrity
gate and the final paper-coverage gate, each of which is evaluated outside the
in-process mutant runner and each of which registers the mechanism that
falsifies it instead (#34). 24 declared mutants, all dead, each at the gate it
was declared to falsify. 40 anchors: 9 file-bytes anchors, 17 path-value
anchors and 14 verbatim-text anchors, the windows evaluated before the byte
anchors, each pinned by its own digest and by a length floor of 20 characters
(#62), and each bound to the gate that consumes it (#87).

The text gates match text as written (#125): needle and haystack are both
whitespace-normalised, so a claim broken across two lines is still the same
characters in the same order, and nothing else is forgiven. The paper gates run
in three legs — claim rendering, numeral coverage, and claim **polarity**, the
last closing the direction-blindness of the first two by requiring each
polarity-bearing claim to occur exactly the expected number of times and to sit
outside a 64-character window carrying a declared negator.

21 sealed objects carry the gate-to-disk seal (#119), and the manifest — each
object, the receipt path it was taken at, the gate whose passing took it, and
the digest — is published in the receipt, so the seal is auditable from the
artifact alone. Each is digested at the moment its gate passes; the payload is sealed only if every earlier digest still
verifies; the artifacts are written to temporaries, re-read, matched against the
gate-time seal — never against a re-derivation, which would confirm a corruption
rather than catch it — and only then moved into place. A deliberately corrupted
payload is written to a probe path and required to be detected first. A failure
anywhere in that path exits 1 and leaves the previous artifacts untouched.

The head is derived twice by disjoint routes. The builder computes it from the
measured counts; the reconstruction reads only the serialized receipt, carries
its own copy of the head law, and shares no helper, no input and no typed value
with the builder. The two complete strings are compared for equality.

## 10. The successor register

- **The non-uniform configuration census.** The obvious successor and the one
  the arena was built for: does the alternating law survive coins that vary
  link to link, and does the rank move? A declared window over configurations
  with two coins, or over the four stratum-uniform coins, is the cheap first
  step.
- **The balanced sector's group.** Infinite is a floor, not a description. The
  natural question is whether its closure is a compact group and whether the
  alternating law is the finite shadow of something there.
- **The exclusivity's reach.** The single-path theorem is about generators
  supported on two sites. What is the largest support at which it still holds,
  and is the plaquette-grain co-occurrence simply the first support at which it
  fails?
- **The gate, at the programme level.** This unit found the per-generator
  realization criterion empty on a gauge arena and the family-level criterion
  full. Whether the earlier units' transport numbers are sensitive to the same
  distinction is a question about the corpus and not about this rung.
- **The area law.** With a non-abelian holonomy measured and a scramble control
  that separates locally, the objects a confinement analog would need can now be
  posed. They are not posed here.

## 11. Deviations, and the register of scope

The pin's arena, gates and must-nots are followed as written. Three points are
recorded as scope rather than deviation.

First, the pin names a coin alphabet and requires either exact enumerability or
a declared window with pinned precedent, disclosed. The alphabet is exactly
enumerable — `640 coins`, derived — but the *configuration* space over it is
not, and the uniform-configuration restriction is the declared window. It is
carried in the verdict, in section 2, and in section 8.

Second, G1 asks for the group as an isomorphism class with rank. On the
interfering sector no finite class exists, and the unit reports the proof of
that rather than a class. The class and rank in the verdict are therefore the
monomial sectors', and the verdict's CLASS segment is the local ladder rather
than the global group, because G7's separation requirement is what licenses a
group claim and the global reading does not meet it.

Third, the two-excitation extension is run at link grain only. At plaquette
grain the sector's dimension makes the sweep expensive, and the unit declares
the restriction rather than spending the budget; the link-grain result is a
negative, so the restriction does not shelter a positive claim.

*Every headline above is a candidate reading until adjudication.*
