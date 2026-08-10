# R5 — the gauge rung: link-indexed unitaries and their holonomy

**Status:** `DELIVERED` — built against the frozen pin `v14/note-r5-gauge-pin.md`,
whose design authority is the frozen R4-effectus review's R5 recommendation.
Verified to run: two plain runs byte-identical, every gate passed, every declared
mutant dead at its declared target, the falsification self-test fatal and writing
nothing.

## The Holonomy Is the Full Alternating Group on Each of Its Orbits, and This Arena Has No Realization Gate That Selects

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
exact bytes, by its own frozen character count and by a declared length floor,
and each bound to the gate that consumes it.
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
**The seal (#119), native from birth and total:** every published object is
digested at the moment its gate passes; every top-level key of the receipt is
either sealed that way or named in the declaration with the reason it cannot
be, and a published table that is neither dies at a gate; the payload may be
sealed only if every earlier seal still verifies; and the artifacts are written
from the sealed payload through temporaries moved into place only after the
bytes on disk match the gate-time digests.

**The verdict, quoted exactly as the instrument emits it.** Every value is
derived inside a gate from a measured receipt field; the complete string —
head included — is compared for equality against an *independent
reconstruction* that derives the head by its own copy of the head law and
re-renders **every segment** from the primitive measured tables, reading
neither the builder's segments nor the builder's counts; and the block below is
compared, character for character under whitespace normalisation, against the
string this run emits, so a paper quoting an earlier run's verdict cannot be
delivered:

```
R5-NON-ABELIAN-<CLASS=ALTERNATING-ON-EACH-OF-ITS-ORBITS(S1-ONE=A3;S2-EDGE=A5;S2-CORNER=A3 x A3;S2-APART=A3 x A3;S3-ROW=A7;S4-BLOCK=A8);RANK=8-OF-16-DECLARED-PLAQUETTE-GENERATORS-ARENA-RELATIVE;COMMUTATOR-SUBGROUP=NONTRIVIAL-AT-576-OF-640-UNIFORM-COINS|REALIZATION-GATE=NONE-EFFECTIVE(INHERITED-PER-GENERATOR-FULL-ADMITS-0-OF-52(R5-BLOCKED-AT-THE-GATE-AT-THAT-READING);DECLARED-FAMILY-COVARIANCE-IS-A-FORCED-IDENTITY-128-OF-128-OFF-CHART-OFF-ALPHABET-PROBES-AGREE-SELECTS-NOTHING);MAXIMAL-PER-GENERATOR-LEVEL=NONE;DECLARED-GATE=LINK-SET-CLOSED-5120-OF-5120-CHART-ACTIONS|CURVATURE-DEFECT=CURVATURE-DEFECT-INDEPENDENT(SUPPORT-OVERLAP-LAW=NO-DEFECT-AT-OVERLAP-LE-1-BY-THEOREM-4-OF-7-RELATIONS;LINK-GRAIN=0-OF-1920-BOTH(BY-THEOREM-AT-SHARE-ONE-SITE-AND-DISJOINT;BY-THE-UNIFORM-RESTRICTION-AT-SAME-LINK-WHERE-189952-OF-409600-DIFFERING-COIN-PAIRS-CARRY-BOTH);PLAQUETTE-GRAIN=ALL-FOUR-CELLS-384-BOTH;TWO-EXCITATION=EXCLUSIVITY-SURVIVES-0-OF-18-BOTH-AT-6-NAMED-COINS-X-3-RELATIONS(SAME-LINK-DIFFERING-COINS-0-OF-36-BOTH);PARENT-BASELINE=588-DEFECTS-AT-ZERO-CURVATURE)|CONTROL=FULL-STRATUM-FLAT-0-OF-3364-TRIVIAL-GROUP|REFINEMENT=LOCAL-STABLE-BY-NON-WRAPPING-GLOBAL-SUPPORT-IS-THE-VOLUME(LOCAL-STABLE-BY-NON-WRAPPING-6-OF-6-WITH-0-WRAPPING-STENCILS;GLOBAL-SUPPORT-IS-THE-VOLUME-16-AT-L-4-AND-64-AT-L-8(A16-TO-A64-NOT-SCRAMBLE-SEPARATED))|SCRAMBLE=SEPARATES-LOCAL-BY-THE-ORDER-SUPPORT-PROFILE-12-OF-12;THE-FORM-ALONE-IS-NOT-THE-SEPARATOR-SCRAMBLES-REACH-IT-AT-5-OF-12-LOCAL-AND-2-OF-2-GLOBAL-CELLS;FAILS-GLOBAL-0-OF-2|INTERFERING-SECTOR=INFINITE-ORDER-512-OF-512-BY-TRACE-NON-INTEGRALITY;DEFECT-STRICTLY-CONTAINED-384-OF-512-ONE-WAY-ONLY|SCOPE=D=2;L=4;REFINED-TO-8;FIELD=Q(ZETA-8);ALPHABET=25;COINS=640;LINKS=32;PLAQUETTES=16;CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));STENCIL=2-SITE-DOMINO-PER-LINK;SECTOR=SINGLE-OCCUPATION;SWEPT-RANGE=UNIFORM-CONFIGURATIONS-EXHAUSTIVE-OVER-THE-COIN-ALPHABET;NON-UNIFORM-CONFIGURATIONS=NOT-SWEPT;INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;THIS-IS-A-CONNECTION-NOT-A-GAUGE-FIELD;NO-CONFIGURATION-MEASURE;NO-ACTION;NO-COUPLING;NO-DYNAMICS;NOT-QCD;NO-CONFINEMENT-CLAIM>
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, the datum it had to start from, and what could not have answered the other way

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

**What could have answered the other way, and what could not.** Four blocking
outcomes were pre-registered in the pin, and all four are reachable *by the one
head law*, demonstrated on synthetic censuses inside a gate:
`R5-BLOCKED-AT-THE-GATE` if no declared gate admits a family,
`R5-BLOCKED-AT-THE-COMMUTATOR-SUBGROUP` if the holonomies all commute,
`R5-BLOCKED-AT-THE-SCRAMBLE-CONTROL` if the group fails to separate the
physical case from a scramble, and `R5-NO-STABLE-GROUP` if no class survives
refinement. Reachability *by the law* is not reachability *on this arena*, and
the difference is measured rather than left for a reader to notice. **Two of
the four were forced shut here by the declaration and not by the physics**, and
the instrument says which and why:

| pre-registered outcome | on this arena | why |
|---|---|---|
| `R5-BLOCKED-AT-THE-GATE` | **forced shut** | the declared gate's covariance half is an identity (section 4) and its closure half holds for any link set built from a lattice |
| `R5-NO-STABLE-GROUP` | **forced shut** | no declared local stencil wraps at the smaller size, so every local class agrees by relabelling (section 7) |
| `R5-BLOCKED-AT-THE-COMMUTATOR-SUBGROUP` | genuinely reachable | a diagonal-only alphabet would have returned zero, and the measured value is far from it (section 3) |
| `R5-BLOCKED-AT-THE-SCRAMBLE-CONTROL` | genuinely reachable | the global grain measures exactly this failure, and the local grain did not have to separate either |

This unit's falsifiability therefore lives in the commutator census and in the
scramble control. Both could have gone the other way, and both are measured to
have gone this way. The head itself is computed from the counts and cannot be
typed: a mutant that retypes it after every verdict gate has been built dies at
the string-equality gate, and a mutant that makes the head law constant dies
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

That same analysis has a consequence worth recording, because it strengthens
the forcing rather than weakening it: the value $\tfrac14$ never appears in an
admissible row, so **no coin uses any element of modulus $\tfrac12$**. The 640
coins are built from 17 of the declared 25 elements, and the other eight are
inert. The derivation is still forced with fibre 1 — the enumeration is
exhaustive over the whole alphabet and simply returns nothing at those eight —
but the family is insensitive to a third of its declared input, and a reader
should know that before reading the alphabet size as a measure of richness.

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
disclosed window with the corpus's own precedent, never a silence. Section 5
measures what one part of that window was worth.

**The two groups.** The anchored chart group — the lattice translations
together with the direction relabelling — has `order 32`; this unit's declared
extension by the square point group has `order 128`. Both are censused, as R4
censuses them.

**The choice inventory.** `20 construction choices` are inventoried, and each
carries **two** numbers rather than one, because one column cannot carry both
of the quantities a reader needs. The **fibre** is the
cardinality of the admissible alternatives, `UNBOUNDED` where there is no
finite set of them; the **declared instances** is how many this unit ran. The
dimension, the lattice size, the connective, the coefficient alphabet, the coin
alphabet, the link set, the plaquette set and the parity strata are FORCED with
fibre 1; the loop base point and orientation and the global phase are
STABILIZER-FIXED with fibres 4 and 8; the plaquette stencils, the gauge
handles, the scramble controls, the named coins, the refined lattice size, the
projective-period cap and the division-event times are GENUINELY-FREE with
unbounded fibre and 6, 3, 2, 6, 1, 1 and 1 declared instances respectively;
the leg at the cut and the two-excitation extension are GENUINELY-FREE with
fibre 2. A genuinely free choice with fibre 1 is a contradiction in terms and
none is reported.

The inventory's first row in importance is the one an inventory of this kind
most easily leaves out. **Which realization gate is declared is the choice this
unit's head law branches on**, it has at least two admissible values — the inherited
per-generator criterion and the family-level replacement — and declaring the
other one would have produced `R5-BLOCKED-AT-THE-GATE` as the head rather than
as a segment. It is inventoried as GENUINELY-FREE with fibre 2, one declared
instance, and flagged **verdict-determining**; a gate requires exactly one row
to carry that flag and requires it to be that row.

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
with equal cardinality is equality. A proper subgroup cannot pass, because it
has strictly smaller order and the comparison is an identity of finite
cardinalities rather than an inference from an invariant. No fingerprint of
element orders, no heuristic, and no holonomy matrix enters the receipt — the
six named coins do, as declared two-by-two inputs, which is what they are.

Measured at the six declared plaquette stencils and at the global one, on
every one of the 64 antidiagonal coins:

| stencil | plaquettes | support | orbits | order | class |
|---|---|---|---|---|---|
| S1-ONE | 1 | 3 | 3 | 3 | $A_3$ |
| S2-EDGE | 2 | 5 | 5 | 60 | $A_5$ |
| S2-CORNER | 2 | 6 | 3 + 3 | 9 | $A_3 \times A_3$ |
| S2-APART | 2 | 6 | 3 + 3 | 9 | $A_3 \times A_3$ |
| S3-ROW | 3 | 7 | 7 | 2520 | $A_7$ |
| S4-BLOCK | 4 | 8 | 8 | 20160 | $A_8$ |
| S-ALL | 16 | 16 | 16 | 10461394944000 | $A_{16}$ |

*Scope: exhaustive over the antidiagonal sector of the derived coin alphabet
at every listed stencil; the class is identical at all 64 of them. On the
diagonal sector the position group is trivial at every stencil — the holonomy
there is pure phase — and that sector is reported separately below.*

**The measured law is one sentence, and the sentence names orbits.** The
holonomy group is **the FULL alternating group on each of its orbits** — the
direct product of the alternating groups on the orbits, which at a
single-orbit stencil is the full alternating group on the support and at a
multi-orbit stencil is not. `2 of the six declared stencils have two orbits`,
and there the group is $A_3\times A_3$, a proper subgroup of $\mathrm{Alt}(6)$, so
"the full alternating group on its own support" would be false exactly there.
The orbit form is what the certificate proves and it is what every row is
certified against.

The stencil profile the declarations trace is
`S1-ONE = A3; S2-EDGE = A5; S2-CORNER = A3 x A3; S2-APART = A3 x A3; S3-ROW = A7; S4-BLOCK = A8`,
and it is a *profile* and not a ladder: the six classes have orders 3, 60, 9,
9, 2520 and 20160, so they are not an ascending chain, and a "<" between them
would assert containments that are false in two places at once. The separator
in the verdict is ";" for that reason. The mechanism behind the profile is
visible in the smallest case: with the swap coin the holonomy of a single
plaquette is a **three-cycle** on three of that plaquette's four corners, and
three-cycles whose supports overlap generate the alternating group on the
union. That is a classical theorem, and it is why the form recurs — a point
section 7 returns to, because it decides how much the form is worth.

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
algebraic integer, and $\mathbb{Z}[\zeta_8]$ is the full ring of integers of
$\mathbb{Q}(\zeta_8)$, so "has a denominator" is the right test. Every one of
these traces has one — `512 of 512` of them — so no power of the holonomy is
the identity, and there is no finite isomorphism class there to report. The
projective periods agree and are reported on R4's own template, since the raw
order is not gauge invariant while the least exponent at which the holonomy
becomes a scalar is: the diagonal sector reaches $\{1,2,4,8\}$, the
antidiagonal sector reaches $\{3\}$ uniformly, and the balanced sector reaches
no such exponent within the declared cap of 32.

The relation between that sector and the composition defect is the sharpest
structural fact the unit measures, and it runs **one way only**. Every coin
that carries a defect lies in the interfering sector — but the sector is
strictly larger than the set that carries the defect: `384 of the 512 balanced
coins` carry one, and the other 128 do not. So *defect implies infinite-order
holonomy*, and *a finite alternating class implies no defect*; the converse is
false, and "exactly the sector" would be a biconditional the measurement
refuses. The next section makes the containment quantitative.

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

## 4. The gate-inheritance audit, and the gate honesty

The pin forbids inheriting R4's realization gate unmodified, and requires this
unit to state at construction whether *maximal declared transport* is compatible
with non-abelian holonomy on this arena. The answer is measured, and it is the
unit's second headline — but it is not the headline the natural reading
supplies, so both halves are stated in the same place.

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
on this arena it empties the family outright. And the mechanism generalises
past this arena: a link-indexed family has no translation-invariant generators
ever, because conjugating a link operator by a translation moves the link, so
the per-generator criterion is empty on *any* family whose generators carry a
location. Where it has bitten before, it bit on objects that were already
location-free.

The unit does not stop there, because the pin's own gate requires the criterion
to be re-derived rather than obeyed. A gauge family's link variables are *never*
individually translation-invariant; that is what makes them link variables. What
is covariant is the **family**: the image of any link operator under any chart
element is again a link operator, on the transported link, with the transported
coin — the swap conjugate where the point part reverses the direction. That
holds here over the extension of order 128 acting on the link set, at
`4096 of the 4096 checks`.

**And that check is forced, which is measured here rather than argued.**
Conjugating an operator supported on two sites by any site permutation returns
the same operator on the image sites; the identity has nothing to do with the
chart, with unitarity or with the derived alphabet. The instrument probes it
with permutations of the 16 sites that are **not** chart elements and with a
matrix that is neither unitary nor a member of the derived alphabet, and the
identity holds at `128 of 128 off-chart` probes. A check that cannot fail on any
arena of link-indexed operators is a **disclosure and not a measurement**, and
it selects nothing. Section 6 applies exactly the same standard to the Wilson
trace, and this section owes the reader the same honesty.

What is left is the arena-dependent half, and it is the half the verdict's
declared-gate segment carries: the link set is closed under `5120 of 5120 chart
actions` of both groups. That is a real, if easy, property of this arena — a
family whose image left the family would fail it — and it is what the head law
branches on.

So the answer to the pin's question is two-sided, and the second side is
sharper than the first. Read per generator, maximal declared transport is
**incompatible** with non-abelian holonomy on this arena, because at that level
the arena is empty. Read at the family level, the criterion is **an identity**,
so it is compatible with everything and licenses nothing. **This arena has no
effective realization gate at all**: one criterion is empty, the other is
vacuous, and neither selects. `R5-NON-ABELIAN` is therefore not a gate-selected
verdict; it is the unselected arena's census, and the verdict says
`REALIZATION-GATE=NONE-EFFECTIVE` in as many words. That is a real result about
the programme's own gate rather than about this arena, and it is the most
transferable thing this rung produced.

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
the gauge fixing — and exactly one coordinate varies per table. The
division-event times and the leg at the cut are *not* varied at all, so every
row of every table below is at the declared times and the declared leg.

**At link grain.** Rows are ordered pairs of link operators; the varying
coordinate is the geometric relation between the two links, and the coin is
swept exhaustively over the alphabet at each relation.

| relation | sites shared | neither | defect only | curvature only | both |
|---|---|---|---|---|---|
| SAME-LINK | 2 | 256 | 384 | 0 | 0 |
| SHARE-ONE-SITE | 1 | 64 | 0 | 576 | 0 |
| DISJOINT | 0 | 640 | 0 | 0 | 0 |

`0 of the 1920 rows carry both`. `576 rows carry curvature and no defect`, and
`384 carry a defect and no curvature`. The two are **mutually exclusive** at
this grain — and the reason the cell is empty is different in the last row from
the first two, which is the whole content of this section.

### The support-overlap law

> **Theorem (single path).** *Let $\ell_1$ and $\ell_2$ be links sharing at most
> one site, and let $U_1,U_2$ be the corresponding link operators for any coins
> whatever. Then $\Delta^{B}(U_2,U_1)=0$.*
>
> *Proof.* Write the shared site $b$, so $U_1$ is supported on $\{a,b\}$ and
> $U_2$ on $\{b,c\}$ with $a\neq c$ (the disjoint case is the same argument with
> the supports separated). An entry of the composite is
> $(U_2U_1)_{ij}=\sum_k (U_2)_{ik}(U_1)_{kj}$, and $(U_2)_{ik}$ is non-zero only
> for $(i,k)$ inside $\{b,c\}^2$ or on the diagonal outside it, and likewise
> $(U_1)_{kj}$ only inside $\{a,b\}^2$ or on the diagonal. Every admissible
> $(i,j)$ shape then leaves exactly one surviving $k$. A sum with
> one term has nothing to interfere with, so $B(U_2U_1)=B(U_2)B(U_1)$
> entrywise. $\square$

The proof's mechanism is **support overlap**, and stating it that way explains
both grains at once and locates the theorem's exact boundary. The maximum
number of intermediate paths $i \to k \to j$ between a pair of endpoints is a
function of how many sites the two operators' supports share, and the
instrument measures that maximum at the densest coin, at every declared
relation of both grains:

| overlap | max intermediate paths | consequence |
|---|---|---|
| 0 sites | 1 | no defect; the operators commute |
| 1 site | 1 | no defect; **the only overlap at which two link operators fail to commute** |
| 2 sites | 2 | defect possible **and** non-commutation possible |
| 4 sites | 4 | defect possible; a holonomy commutes with itself, so no curvature |

`4 of the 7 declared relations` — SHARE-ONE-SITE and DISJOINT at link grain,
SHARE-A-CORNER and DISJOINT at plaquette grain — have overlap at most one and
are covered by the theorem, which says their `both` cells are empty for every
coin alphabet whatever and not only this one. **The other three are not
covered**, and SAME-LINK is one of them: two links that coincide share *two*
sites.

So the SAME-LINK row's empty `both` cell is not the theorem. It is the
**declared uniform configuration**, which puts the *same* coin on both legs, so
the two operators are the same operator and commute for free. Lifting that
restriction is cheap, and the instrument does it exhaustively: over all ordered
pairs of the 640 coins on one link,

| SAME-LINK, coins allowed to differ | pairs | neither | defect only | curvature only | both |
|---|---|---|---|---|---|
| exhaustive | 409600 | 15872 | 6656 | 197120 | 189952 |

`189952 of 409600 ordered coin pairs` carry both. So the exclusivity is a
theorem on two of the three link relations and an artifact of the declared
window on the third, and the verdict segments it that way rather than claiming
the stronger thing. The licensed sentence is this one:

> A non-zero composition defect needs two composition paths between one pair of
> endpoints; a non-zero commutator of link operators needs their supports to meet
> in exactly one site; and one shared site admits exactly one path. So wherever
> two two-site generators overlap in at most one site the two cannot occur
> together — for every coin alphabet, not only this one. The exclusion is a
> theorem about **support overlap**, and it stops as soon as two objects overlap
> in two sites. It is a statement about two-site generators, and it carries no
> claim about quantum character and geometry in general.

**At plaquette grain.** Rows are ordered pairs of plaquette holonomies, and the
same contrast is taken with the same coordinates held equal.

| relation | sites shared | neither | defect only | curvature only | both |
|---|---|---|---|---|---|
| SAME-PLAQUETTE | 4 | 128 | 512 | 0 | 0 |
| SHARE-AN-EDGE | 2 | 64 | 0 | 192 | 384 |
| SHARE-A-CORNER | 1 | 128 | 0 | 512 | 0 |
| DISJOINT | 0 | 640 | 0 | 0 | 0 |

Here `384 rows carry both`, and all four cells are populated. Every cell of
both tables follows from the overlap column: the edge-sharing row is the one
where two holonomies meet in two sites, which is precisely where the single-path
count fails. So the exclusivity is a statement about **generator support** and
not about the connection those generators build, and the grain is a declared
coordinate of the result rather than an incidental choice. Taken together with
R4's measured baseline — `588 defects at identically zero curvature` — the
pre-registered outcome is `CURVATURE-DEFECT-INDEPENDENT`: neither predicate
implies the other, and each direction has a witness in numbers.

**The must-not, gated against this paper and not only against the verdict.**
Curvature does not imply quantum character on this stage. The instrument gates
that there exist non-commuting pairs with identically zero defect, in numbers,
at both grains; R4 supplies the converse witness. The implication is settled
negative in both directions and nothing in this unit asserts it. The gate that
enforces the wording now sweeps this paper's own text rather than the
instrument's rendered claims, so a paragraph inverting the must-not dies on the
delivery run.

**The one declared two-excitation extension, pre-registered and run.** R4 named
exactly three routes out of its frozen-stage arena, and the cheapest is a
two-excitation sector. This unit declares one and runs it: the hard-core
antisymmetric sector $\Lambda^2$, on `120 two-excitation states`, the forced
choice at fixed dimension up to the symmetric square, which the choice inventory
carries with fibre 2. The extension returns a **negative**: `0 of 18` rows carry
both. That count is `6 named coins against 3 relations` — a declared sample, not
the exhaustive sweep the 1920-row table is, and it is reported as such.

The extension is then taken to the same boundary the single-excitation census
was. At SAME-LINK with the coins allowed to differ, exhaustively over the named
coins, `0 of 36` ordered pairs carry both — two carry a defect alone. And on a
declared stride sample of the whole alphabet, 6400 ordered pairs, the
two-excitation cell agrees with the single-excitation cell every time, with zero
disagreements. The reason is structural: the exterior square of an operator
supported on one domino acts as the determinant on the domino's own two-particle
state and as the coin itself on every state that meets it, so one dimension up
does not move the census at all. The symmetric square admits no more
intermediate two-particle states than the exterior square does, so the fibre-2
choice is not load-bearing either. The pre-registered route out of the arena
does not, at this grain, get out.

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
live rows; under the null handle it moves at none of them. The rows are taken at
the six named coins.

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

## 7. Refinement, and what the scramble control decides

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

At `6 of 6 declared local stencils` the class is **identical** at the two sizes;
at the global stencil it is `A16 at L = 4 and A64 at L = 8`, of order
`10461394944000` at the smaller size.

**The local half of that is forced, and the unit measures the forcing rather
than leaving it to be noticed.** `0 of the 6 declared local stencils wrap` at
$L=4$: the widest of them spans four sites in one direction and the torus is
four wide, so every declared patch sits inside the smaller lattice without
meeting itself. The plaquette holonomy with the swap coin is the three-cycle on
the plaquette's own corners, so for a patch that does not wrap the generators at
$L=4$ and at $L=8$ are literally the same maps on the same relative coordinates,
and the two groups are equal by relabelling. Local stability could not have come
out otherwise at any size at least as large as the widest declared stencil. What
the refinement step measures is the **global** stencil alone, and the verdict
segment says `LOCAL-STABLE-BY-NON-WRAPPING`.

At the global stencil the sharper statement is available and is the one entered.
"Extensive" is licensed for the *support* and the plaquette count and for nothing
else — $\log\lvert A_n\rvert \approx n\log n - n$ is superextensive by a
logarithmic factor, and "extensive object" is not a predicate of a group at all.
What is measured is that the global class is the full alternating group on the
**entire site set at both sizes**: support `16 at L = 4 and 64 at L = 8`, which
is exactly the volume $L^2$. So the *law* — full alternating on the orbits —
holds at both grains and both sizes, and what refines is the support. The
verdict says `GLOBAL-SUPPORT-IS-THE-VOLUME`, and it carries the global class
with the disclosure that it is not scramble-separated, in the same segment,
because a reader who quotes that segment alone must not be able to quote a
non-discriminating measurement as a finding.

**The scramble control, and what it decides about the form.** Γ-main's standing
warning is that a group reading is not automatically a discriminating statistic,
and the pin makes the separation a precondition on any group claim. Two scrambles
are declared — a transposition of link labels and a direction flip — and applied
to the boundary assembly, so the four operators multiplied are no longer the four
edges of a loop. All rows are taken at the named coin ANTI-X, at which the
physical class is uniform across the whole antidiagonal sector.

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
`neither scramble separates the global class` — a product of four transpositions
is even however the links are chosen, and both scrambles are measured to reach
the whole of $A_{16}$ from there.

**And the control decides which statistic is doing the separating.** The
scrambles are assemblies built to be wrong, and they reach the full alternating
group on their own orbits anyway, at `5 of 12 local cells and 2 of 2 global
cells` — $A_8$, $A_8$, $A_{10}$, $A_{10}$, $A_{12}$ locally and $A_{16}$ at both
global cells. So **the form is not the discriminating statistic on this arena**.
What separates at every local cell is the pair **(order, support)**, and that
pair is what the verdict enters as the separator. The group claim goes in where
that pair separates — at the local stencils — and the global class goes in as
measured-but-not-discriminating, which is why the verdict's CLASS segment carries
the stencil profile rather than $A_{16}$.

**Against CR-D's tower, at the standard CR-D itself set.** G6 requires the class
to be reported against the programme's existing group-family prior. CR-D reported
`the FULL alternating group on its own support` — $A_5$ on five labels, $A_{11}$
on eleven, $A_{15}$ on fifteen — and this arena returns the same *form*, which
here reads `the FULL alternating group on each of its orbits` because two of
its stencils have two orbits. The form
match is real and is stated verbatim in both units. It is not evidence that the
theory prefers the alternating family, and this unit does not enter it as such,
for three measured reasons. First, in **both** constructions the generators are
even permutations of small overlapping support, and by a classical theorem that
forces the alternating group; the convergence is therefore evidence about the
**generator type the two constructions share**, and each arena's specific groups
follow from its support cardinalities alone once the shared form is granted.
Second, the two constructions have no shared support law and no shared ceiling:
CR-D's supports are Hamming-weight classes of system labels and its tower tops at
$A_{15}$, while this arena's are lattice-geometric. Third, and decisively, the
scramble control above reaches the same form. A statistic that a deliberately
scrambled connection satisfies just as well is not evidence of a structural
preference at that grain. CR-D's own paper sets the discipline by refusing to
call a form agreement an instance of its theorem, and this unit meets that
standard: the agreement is a **form coincidence with a shared generator
mechanism and no shared law**, and the physical content on this rung is the
(order, support) profile.

## 8. What this decides, and what it does not

**Decided, at the declared scope.**

- The declaration-connection on this stage carries a non-abelian holonomy
  group. The commutator subgroup is non-trivial at `576 of 640 uniform
  configurations`, on an arena whose provably flat control returns the trivial
  group at `0 of 3364`.
- Where the group is finite, its isomorphism class is
  `the FULL alternating group on each of its orbits`, certified by set equality
  and reported with its rank; at a two-orbit stencil that is the direct product
  and not the alternating group on the support.
- The class survives one refinement step at `6 of 6 declared local stencils` —
  by non-wrapping, which is forced — and does not at the global one, where the
  support is the volume at both sizes.
- On the interfering sector the group is infinite, certified by a theorem about
  traces rather than by a search cap; and the coins that carry a defect are a
  strict subset of it, so the link runs one way only (section 3).
- Curvature and the composition defect are independent predicates. Where two
  two-site generators overlap in at most one site they are `mutually exclusive`
  by theorem; where they overlap in more, both occur, and the exhaustive
  SAME-LINK census says so in numbers.
- R4's realization gate, inherited unmodified and read per generator, admits
  nothing on this arena; the declared family-level replacement is an identity
  and admits everything. **Neither selects.** Both readings are in the verdict.

**Not decided, and named.**

- **The non-uniform configurations.** Only the uniform configurations are swept.
  A coin that varies link to link is the general object this arena was built for,
  and the group census over it is open. Nothing here shows the alternating law
  survives it; nothing here shows it fails. What section 5 does show is that
  lifting the restriction on one link changes an exclusivity cell from empty to
  nearly half full, so the window is not innocuous.
- **The balanced sector's group.** It is infinite, and that is all this unit
  says about it. Its structure — whether it is dense in a compact group, whether
  it has a finite image worth naming — is untouched.
- **A gauge field.** What this arena has is a **connection** in the holonomy
  sense: an assignment of unitaries to links and an ordered product around a
  loop. It has no configuration measure, no action functional, no coupling and
  no dynamics for the link variables, and its group is a finite alternating
  permutation group on lattice sites rather than a compact Lie group with a
  colour space. So: a non-abelian holonomy on a finite record lattice. Not a
  gauge field, not QCD, and no confinement-analog object, because the objects
  such a claim would need are absent from this arena entirely. The verdict's
  scope segment says all of that in as many words, and everything on the far
  side of the word *field* — coupling, running, area laws, continuum limits,
  spectra — is untouched.
- **Any quantum reading of curvature.** Settled negative in both directions,
  above.
- **The phase kernel's meaning.** Its order is measured and its discriminant is
  measured. What the 32768 counts is not interpreted here.
- **The refinement limit.** One step is not a limit, and the local half of that
  one step is forced. `L = 8` is the declared doubling; the sequence beyond it
  is untouched, and the global class is already known to move.

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

75 gates, 74 of them evaluated inside the receipt. The #34 ledger is published
at an honest denominator, in four classes rather than two: 41 carry a declared
mutant that reaches them and 2 an anchor break that does, and 3 carry a
registered forcing and 29 carry no falsifier that reaches them at all. That last
class is disclosed by name rather than folded into the first, and the reason it
has to be is measured: an anchor break kills the run at the anchor gate itself,
so a gate downstream of the anchors is never arrived at and is not exercised by
it. The anchor breaker is correspondingly gate-specific — it accepts any of the
three anchor classes and dies at that anchor's own gate, and those are the two
gates the class covers. 45 declared mutants, all dead, each at the gate it was
declared to falsify. 40 anchors: 9 file-bytes
anchors, 17 path-value anchors and 14 verbatim-text anchors, the windows
evaluated before the byte anchors, each pinned by its own digest, by its own
frozen character count and by a length floor of 50 characters (#62), and each
bound to the gate that consumes it (#87). The floor is set at the shortest
window this unit declares, so no window can be shrunk at all without falling
through it, and pinning the character count as well as the digest means a
shrink has to move two frozen declarations rather than one.

The text gates match text as written (#125): needle and haystack are both
whitespace-normalised, so a claim broken across two lines is still the same
characters in the same order, and nothing else is forgiven. The paper gates run
in four legs. Claim rendering and numeral coverage are the first two. Claim
**polarity** is the third, closing the direction-blindness of the first two by
requiring each polarity-bearing claim to occur exactly the expected number of
times and to sit outside a 64-character window carrying a declared negator; the
guarded set covers the claims whose direction is verdict-bearing: the rank, the
gate census, the covariance, the global class, the plaquette cells, the strict
containment and the closure count. The fourth leg is the one that binds this
paper to this run. The complete emitted verdict string must occur here
verbatim, and the must-not vocabulary is swept over this paper's own text with
the declaring sentences removed first. Nothing weaker can carry either
requirement: the claim gate asks only for fragments, and the numeral gate is
structurally blind to every numeral inside a hyphenated segment, so only string
equality reaches a retyped verdict block and only a text sweep reaches a
must-not that carries no numeral at all.

33 sealed objects carry the gate-to-disk seal (#119), and the manifest is
**total**: every top-level key of the receipt is either sealed at the gate that
produced it or named in the declaration with the reason it cannot be, and a
published table that is neither dies at a gate. The gate table is sealed **row by row at gate
time** — each row digested at the moment it closes — rather than in one late
take at the end of the run, and the totals are a re-derived identity rather than
an assignment. The manifest — each object, the receipt path it was taken at, the
gate whose passing took it, and the digest — is published in the receipt, so the
seal is auditable from the artifact alone. The payload is sealed only if every
earlier digest still verifies; the artifacts are written to temporaries, re-read,
matched against the gate-time seal — never against a re-derivation, which would
confirm a corruption rather than catch it — and only then moved into place. A
deliberately corrupted payload is written to a probe path and required to be
detected first. At that boundary the instrument also re-derives, **from the bytes
on disk**, the verdict, every gate row against its gate-time digest, the
post-sweep totals, the published seal manifest against the live seal, and every
rendered transcript line against the receipt it claims to render. A failure
anywhere in that path exits 1, rewrites the sealed payload over whatever is on
disk, and leaves no corrupt bytes behind.

The head is derived twice by disjoint routes, and the second route now
re-derives the **whole** string. The builder computes it from the measured
counts; the reconstruction reads only the serialized receipt, carries its own
copy of the head law, and re-renders every segment from the primitive measured
tables — the censuses, the group rows, the audits, the controls — sharing no
format string, no helper and no typed value with the builder, and reading
neither the builder's segments nor the builder's counts. The two complete
strings are compared for equality. A literal drifted inside the builder dies
there, and it is worth saying why that requires re-rendering rather than
re-reading: a comparator that reads the builder's own segments back compares
them with themselves, and the number never leaves the builder to be checked.

## 10. The successor register

- **A measure on configurations.** This is the missing object behind everything
  else on this list, and it is named first because the register's order is an
  obligation and not a preference. There is nothing on this arena to take an
  expectation over: 640 uniform configurations out of $640^{32}$, no action, no
  coupling. Any expectation-valued successor requires it first.
- **The non-uniform configuration census.** The gating successor, and the one
  the arena was built for: does the alternating law survive coins that vary link
  to link, and does the rank move? A declared window over configurations with
  two coins, or over the four stratum-uniform coins, is the cheap first step.
  Section 5's exhaustive SAME-LINK census is the first evidence that the window
  is doing real work.
- **A third realization criterion.** This unit found the per-generator criterion
  empty on any location-carrying family and the family-level criterion an
  identity that selects nothing. Neither can serve. Deriving a criterion that
  actually selects, and re-reading the earlier units' transport numbers through
  it, is the highest-value item here and is a question about the corpus rather
  than about this rung.
- **The balanced sector's group.** Infinite is a floor, not a description. The
  natural question is whether its closure is a compact group and whether the
  alternating law is the finite shadow of something there.
- **The exclusivity's reach, re-posed.** The single-path theorem is answered by
  its own proof: it holds exactly when the two supports meet in at most one
  site, and the plaquette grain is the first overlap at which it fails. What
  remains open is the non-uniform census one grain down — the SAME-LINK
  exhaustive table is a first slice of it — and whether an overlap-graded law
  organises defect and curvature on families of larger support.
- **The refinement question, re-posed on stencils that wrap.** Local stability
  here is forced by non-wrapping. The question G6 meant to ask is what happens
  to a declared stencil whose extent exceeds the lattice, where the two sizes
  give genuinely different generators. That is the refinement test this unit did
  not run and the successor should declare.
- **The area law, and what stands between.** A confinement analog would need
  three objects this arena does not have: a measure on configurations, a family
  of loops whose size can grow, and a coupling to vary. Naming them is not
  posing them, and none is posed here. The second of them is worth its own
  sentence: the global grain is exactly where the scramble control does *not*
  separate, `0 of 2`, so the scale at which such an object would live is the
  scale at which this instrument is measured to be non-discriminating. Any pin
  that opens such a follow-on has the configuration measure as its **first**
  obligation, before a loop family and before a coupling, and a pin that opens
  anywhere else is opening in the wrong place.

**What a coupling unit inherits from this rung, and what it does not.**
Inheritable as measured: the existence of a non-abelian plaquette **connection**
on the declared arena, against a provably flat control; the exclusion **as a
support-overlap law**, which is coin-alphabet-independent, proved, and unmoved
by the declared two-excitation sector; the one-way link from the defect to the
infinite-order sector, with its strictness; the finite classes as isomorphism
classes with arena-relative rank, at the local stencils only; and the
gate-lineage result of section 4, which is the most transferable thing this rung
produced. Inheritable only with its scope attached: every group statement here
carries `SWEPT-RANGE=UNIFORM-CONFIGURATIONS`, and a successor that drops that
segment changes the claim. Not inheritable at all: the family-covariance
criterion as a *gate*, since it selects nothing; any refinement-*limit*
statement, since one step is not a limit and its local half is forced; the
global class as a *discriminating* fact; the alternating form as a theory-level
preference, the discipline being that the (order, support) profile is what
separates; the rank as anything but arena-relative; and the word *field*, with
everything on its far side. The gap a coupling unit inherits above all is the
one this rung could not close: **there is no measure on configurations here**,
so there is nothing yet to take an expectation over.

## 11. Deviations, and the register of scope

The pin's arena, gates and must-nots are followed as written. Four points are
recorded as scope rather than deviation.

First, the pin names a coin alphabet and requires either exact enumerability or
a declared window with pinned precedent, disclosed. The alphabet is exactly
enumerable — `640 coins`, derived — but the *configuration* space over it is
not, and the uniform-configuration restriction is the declared window. It is
carried in the verdict, in section 2, in section 5 and in section 8.

Second, G1 asks for the group as an isomorphism class with rank. On the
interfering sector no finite class exists, and the unit reports the proof of
that rather than a class. The class and rank in the verdict are therefore the
monomial sectors', and the verdict's CLASS segment is the stencil profile rather
than the global group, because G7's separation requirement is what licenses a
group claim and the global reading does not meet it.

Third, the two-excitation extension is run at link grain only, and its 18-row
table is `6 named coins against 3 relations` rather than an exhaustive sweep. At
plaquette grain the sector's dimension makes the sweep expensive, and the unit
declares the restriction rather than spending the budget; the link-grain result
is a negative, so the restriction does not shelter a positive claim.

Fourth, two of the declared free axes are not varied at all: the division-event
times and the leg at the cut, each run at one value. Every row of section 5 is
therefore at the declared times and the declared leg, and the tables are entered
that way rather than as statements about the defect in general.
