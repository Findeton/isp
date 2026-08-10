# Γ-MAIN — The geometry-update law

**Status:** `GREEN-REPAIRED`, 2026-08-10 — delivered under
`v14/note-gmain-pin.md` (v14 ledger #64) and its governing register
`v14/note-gmain-adjudication.md` (v14 ledger #82), with the
supplementary orders of v14 ledger #88. Not citable until an external
hostile round confers terminal.

**Artifacts:** `v14/code/gmain_exact.py`,
`v14/code/gmain_output.txt`, `v14/code/gmain_receipt.json`. Every
number below renders from the receipt, and the paper is swept for the
ones that do not.

---

## Abstract

This unit constructs $\Gamma(\mathrm{cut}' \leftarrow \mathrm{cut})$ —
the geometry-update law the corpus has been naming for two units and
had not built — and then tries to break it with a battery registered
before it ran.

**The construction lands.** On D74's committed MENU quotient, at the
$(A,B)$ depth-4 cap, $\Gamma$ is an exact rational column-stochastic
family between the five declared depth cuts, of dimensions
[1, 5, 13, 45, 113] over 3969 histories and 113 classes, built from
the pinned relative-horizon kernels, with all 544 of its columns
verified column-stochastic in exact arithmetic and the disintegration
identity $w(h)\,k_{4-|h|}(e \mid h) = w(h+e)$ exact at 3968 of 3968
transitions. The record quotient, 2477 classes, is carried beside it
as the negative control at every step.

**The pre-registered position-law values are not values of the law.**
They are leaf-count statistics of the external transport census, and
this unit enters them as a declared census shadow — a control, never a
target. It reproduces them exactly at the counting measure that
defined them, 3/7, 1/7, 3/7 at leg 1 and 4/9, 1/9, 4/9 at leg 2. At
the declared primary readout — the step-normalised weight
$q(e \mid h)/M(h)$, which is *exactly* the pinned kernel $k_1$ — the
positional law is 15/38, 5/19, 13/38 at both legs: leg-independent,
left–right asymmetric, and equal to neither shadow value. Three
convergent measurements say why the shadow cannot be a target: it is a
count statistic in its own frozen source; the measurement that
reproduces it touches no object of the constructed family, which a
token scan of the source over the measuring region proves; and
adopting the readout that hits it destroys the pin's own mandatory
negative control, giving the record quotient a rank-4 holonomy,
failing Chapman–Kolmogorov at 10 of 10 triples where the primary
construction fails at 0, and leaving 0 of 544 columns stochastic
before an undeclared repair.

**The holonomy is reproduced and its deviation is located.** D74's
group reproduces on the carrier digit for digit — primes [2, 3],
rank 2, obstruction 44, 1402 squares closing, cycle rank 134. The
horizon normalisation, the step that makes the construction possible
at all, enlarges it to primes [2, 3, 5, 13]; and the enlargement is
not a census but an identity,
$r_k = r_q \cdot G(h e_A e_B, r-2)/G(h e_B e_A, r-2)$, verified at
1546 of 1546 closed squares, with every non-unit correction factor
sitting on a class where the horizon potential is measured not to
descend. The negative control is flat at all three readings, and the
record chain is exactly lumpable where the carrier is not: the class
chain fails Chapman–Kolmogorov at 4 of 10 depth-cut triples, and at
every one of those four the unique algebraic candidate of eq. 22
carries negative entries under both completions that admit the
question at all.

**The motivation inventory is non-empty, and the readout fiber is
three.** Ten choices, five of them forced or stabilizer-fixed, five
genuinely free with fibers that are machine-computed rather than
declared; the free item that carries the unit is the readout, and its
fiber is three measured laws with a fourth excluded by the cap.

So the settlement condition is evaluated at one arena and reported
PARTIAL, with the failed link named: the census numbers the unit was
asked to hit were never values of any law.

---

## 1. What this unit is for, and what it is not

CR-A named the missing object —
CRA-BLOCKED-AT-STATIC-GEOMETRY-<MISSING=A-GEOMETRY-UPDATE-LAW> — and
CR-B named the other one:

> THE-INTERVAL-POSITIONAL-LAW-=-THE-TRANSITION-KERNEL-BETWEEN-AN-INTERVALS-ENDPOINTS-WHOSE-RENEWAL-COUNT-IS-N

This unit builds a law and measures what it does to both. It does not
re-pose the transport-scope chain, whose attempt is terminal-negative
(the escape); it does not claim a continuum limit; it makes no
curvature ⟹ quantum claim, and the count of such claims is measured
rather than declared.

## 2. The declared arena

Declared as data, before anything is computed (RUNBOOK §15).

| coordinate | declaration |
|---|---|
| boundary | the empty history; genesis $v_0$ is the committed layer's declared boundary |
| family | ARM-1T, actor pool $(A,B)$, exhaustive menus; depth $\le 5$ for the anchor scope, depth $\le 4$ for THE CARRIER |
| law | the committed d42b1 weight law, exec'd from its committed bytes; nothing about admission or pricing re-implemented |
| state | the history itself; every coarser object is a declared abstraction, named at each use |
| carrier | D74's committed MENU quotient (the weighted-menu partition), 113 classes at $(A,B)$ $d \le 4$ |
| negative control | D74's committed REC quotient, 2477 classes, measured FLAT |
| positive control | the renewal cuts (the D62-R4 pair-arb events), U1b's column-constancy wall |
| cuts | depth cuts $0 \ldots 4$; renewal cuts; the renewal-leg ensembles at the declared deeper conditioned scope |
| horizon | H4 — the horizon-4 chain from the root, a history at depth $d$ stepping under $k_{4-d}$; terminal $G(h,0) = 1$ |
| readout | the fiber is 3, all three measured. PRIMARY: the step-normalised law $q/M$, which is exactly the pinned kernel $k_1$. Also measured: the raw price product, and the counting measure. A fourth — the H4 chain itself — is EXCLUDED-BY-CAP on the legs |
| census shadow | the pre-registered rational triples are leaf-count statistics of the external transport census: a declared CONTROL, never a target |
| provenance | declared commit shas; 24 hash-pinned sources plus this unit's own paper, byte-anchored |

## 3. Provenance, and the discipline it is read under

Every cross-unit read in this unit goes through `git show
<sha>:<path>` at a sha declared in the frozen text; worktree bytes and
`git show HEAD:` are mutable state and are read for no source. The one
exception is this unit's own paper, which is the fourth deliverable
and is therefore not committed when the delivery run reads it: its
bytes are frozen before the run and **hash-pinned as a byte anchor**,
so the run refuses to proceed against any other bytes. Twenty-one
verbatim-text anchors bind quote fidelity — the quotations in this
paper against the sources' committed bytes — and are evaluated first,
with a genuine short-circuit: a failing quotation exits the run before
a single byte anchor is evaluated. Each is bound to a named consumer
gate that exists, reads a measured quantity, and dies to a declared
falsifier whose reach is measured; and each carries its own per-row
drift falsifier, so a row is covered only when its own predicate
flips.

The unit ships an argv-parsed command line, as the programme requires:

> every unit ships an argv-parsed CLI that rejects
unknown flags (exit 2), a `--selftest` that corrupts one
anchor, confirms exit 1, and writes nothing, and a
`--mutant NAME` harness

Unknown flags exit 2 rather than being ignored; `--selftest` corrupts
one declared anchor, confirms the run exits 1, and writes nothing;
`--mutant NAME` evaluates one declared falsifier in isolation and
exits 0 only if it reaches its gate and kills it; `--list-mutants`
prints the declared registry, which is gated equal to the set the run
evaluates. The default output directory is the source file's own
directory and nowhere else, so a reviewer's scratch copy writes beside
itself.

The named exclusions are printed in-unit and honoured: u1c (not
citable), d56 (reachable only through d57's pin, not reached), the two
index documents, `v14/LOG.md` and `/STATUS.md` as forbidden runtime
inputs, the R6b′ delivery artifacts, which are mid-repair — the
adjudication register at its own declared sha is the frozen carrier of
what this unit inherits — and the three frozen review files, which are
not read at run time. The v14 LOG #4 erratum is carried as a frozen
declaration rather than read.

## 4. The construction

$\Gamma$ is the transport process read on the carrier. The
relative-horizon kernel is

$$k_r(e \mid h) \;=\; \frac{q(e \mid h)\, G(h+e,\, r-1)}{G(h, r)},$$

with $G$ the finite-horizon potential of the committed layer; the root
potentials reproduce Γ-prep's committed values exactly. The chain's
own law at depth $d$ is $w(h) = \mu(h)\, G(h, 4-d) / G(\text{root}, 4)$,
which has cut mass 1 at every cut, and the identity

$$w(h)\, k_{4-|h|}(e \mid h) \;=\; w(h+e)$$

makes the class-level law the exact conditional

$$\Gamma(d' \leftarrow d)[s', s] \;=\; \frac{\sum_{h \in s,\, |h| = d}\;
\sum_{h' \in s',\, h' \succ h} w(h')}{\sum_{h \in s,\, |h| = d} w(h)},$$

column-stochastic by construction and verified so, exactly, on all 544
columns of the two quotients. **The horizon in that identity is not
free.** At $r = 4-|h|$ it holds at 3968 of 3968 transitions with zero
violations; at every other admissible $r$ it fails at 352 of 596
tests. Written with $r$ free the identity is false, and the unit
writes $k_{4-|h|}$.

**Why a readout has to be declared, and why the primary one is
pinned.** The horizon potential is *not* class-constant on the
carrier: $G(\cdot, 2)$ takes more than one value on 4 of the 13
classes the depth-2 cut carries. So the horizon kernel does not
descend and a lift is needed. The local menu mass
$M(h) = \sum_e q(e \mid h)$ is not constant either — it is 2 at 3757
carrier histories and 5/2 at 212 — so a raw product of weights along a
path is not a probability. Normalising each step gives $q/M$, and
$q/M$ **is** $k_1$, because $G(h,1) = M(h)$ by definition: the
step-normalised readout is the $r = 1$ member of the very kernel
family $\Gamma$ is built from, not a third ad-hoc choice. On the
record quotient the potential *does* descend, at every horizon, which
is why the control behaves.

**The block decomposition, and the scope of what is imported.** From
Γ-prep this unit imports a *census* and not a claim. The census: 5161
R-SIG points at the depth $\le 5$ anchor scope, 1365 of them
menu-exact, in blocks {(1,1): 1365, (2,2): 3788, (2,3): 4, (3,2): 4},
reproduced here from the committed layer. On **the carrier** the
decomposition is a statement about nine classes: 689 carrier R-SIG
points in blocks {(1, 1): 341, (2, 2): 348}, meeting 9 of 113 MENU
classes, every one of them block-pure. What is *not* imported is the
unqualified atom claim: Γ-prep's minorization result holds at its own
declared

> scope = 2 actors, transport depth <= 6, MATCHED horizon, primary grain

and this unit runs neither of those two alternatives — the MATCHED
horizon convention and the 13-class primary grain are inventory items
here, declared and not run. The exclusion has teeth at the ruled
carrier: the minorization constant is monotone under coarsening, so at
CONG-185, which refines MENU-113, four of the six delivered block rows
have a vanishing constant and the claim collapses to the (1,1) block.
This unit therefore inherits the census, and inherits the atom
language only for that one block, pending the Γ-prep adjudication.

**The blocking fact, with its denominator.** Γ-prep's monotone-ladder
result is scoped in its own §7:

> Over all
$30{,}728$ transitions out of every history of depth $< 5$,
holdings-shrinking transitions: $0$.

The censused window is transitions out of histories of depth below 5.
This unit reproduces the censused count independently from its own
per-level census, at 30728, and reads the family's own per-level table
from Γ-prep's committed receipt: the family has 243768 transitions in
all, so the fact is measured on 30728 of 243768 of them — 12.60 per
cent. No unscoped reading of it is used here.

## 5. The battery

### 5.1 The census shadow, and the law value

The R6b′ register pre-registered two rational triples:

> reproduce (3/7,1/7,3/7) at leg 1 and
(4/9,1/9,4/9) at leg 2.

They are **census statistics in their own frozen source**, which
derives the positional law from

> (C(n−1,2) equiprobable
configurations; position marginal uniform on n−1)

— the uniform measure on configurations, i.e. a leaf count. This unit
therefore enters them as a **declared census shadow**: an external
control of the enumeration, never a target of the constructed law.

Leg 1 is scanned **unpruned** — 152672 raw continuations generated
from the 16 renewal-1 bases and only then filtered, returning 3584
legs in exactly five patterns. Leg 2 is scanned over all 256
renewal-2 bases, 796672 expansions, with a pattern prune that is
gated rather than assumed: on 3 of the 256 bases the unpruned scan generates 60492
continuations and returns 864 legs, identical to the pruned set leg
for leg and weight for weight, at both weights.

| readout | leg 1 | leg 2 | leg-independent |
|---|---|---|---|
| PRIMARY, step-normalised $q/M = k_1$ | (15/38, 5/19, 13/38) | (15/38, 5/19, 13/38) | yes |
| raw price product | (3/8, 1/4, 3/8) | (3/8, 1/4, 3/8) | yes |
| counting measure (the shadow's own) | (3/7, 1/7, 3/7) | (4/9, 1/9, 4/9) | no |
| delivery multiplicity | 2 | 3 | — |
| delivery sector mass | $1/2$ | $1/2$ | — |

**The census shadow is reproduced exactly, and the law value is
neither of its two values.** At the declared primary readout the
positional law is leg-independent and left–right asymmetric —
15/38 against 13/38 — which no other reading here is. The cause of
the split is measured, not argued: the delivery budget is a quarter
per actor divided by $\lvert \mathrm{hold}(a) \rvert$, so adding a
version splits the same mass into more entries. The sector masses are
identical at the two legs while the delivery count moves from 4 to 6 —
the quarter law makes both mass readouts multiplicity-blind, and
$(m+1)/(2m+3)$ is $3/7$ at $m = 2$ and $4/9$ at $m = 3$ only for the
readout that can *see* $m$. The shadow is a function of a count, which
is exactly why only a counting readout reproduces it.

**The measurement that reproduces the shadow never touches $\Gamma$,
and this is measured rather than asserted.** A token scan of the
unit's own source over the region between two markers returns zero
occurrences of the constructed family, of either quotient, of the
class indices, of the occupancy or of the kernels; and the leg
ensembles live at depths 3 to 10, outside the declared carrier cap.
Reproducing a leaf census by re-running the leaf census tests the
enumeration, not the law.

**The third convergent measurement: adopting the shadow's readout
costs the negative control.** The counting readout is built here at
the class level, twice. Taken literally — the same construction with
the uniform measure on the admissible objects in place of $w$ — it is
not a law at all: 0 of 544 columns sum to 1, because they sum to the
branching factors. Repaired by an undeclared second choice —
renormalise each column by its own total — it becomes
column-stochastic, and it destroys the pin's own mandatory negative
control: on the record quotient the repaired count family is non-unit
at 296 of 473 closing squares with group primes [2, 3, 5, 7] and
rank 4, and it fails Chapman–Kolmogorov at 10 of 10 triples where the
primary construction fails at 0. The readout at which the shadow is
hit is the readout at which the pin's own control fails.

**F8, derived rather than imported.** The register records the
mechanism as

> (p,d,p,r) does not
occur: no delivery in the middle interior slot**; delivery
multiplicity

2→3 driving the shadow. Here it is a measurement of this unit's own
scan: deliveries occur in slots 1 and 3 at 1024 legs each and in
slot 2 at 0, and the cause is exhibited — after $(p, d, p)$ the two
live proposals are order-comparable at 512 of 512 instances, because
the delivery joins the two actors' registers, while after $(p, n, p)$
they are comparable at 0 of 256; a pair-arbitration needs two
incomparable live proposals, so the pattern cannot close.

**The readout-invariant residue, with its exact scope.** Conditioned
on the filler being a delivery, the positional law is (1/2, 0, 1/2) at
both legs and at **all three** readouts: that conditional is the F8
exclusion itself and it is readout-free. Conditioned on the filler
being idle, the law is (1/3, 1/3, 1/3) at the two count-like readouts
and (5/14, 5/14, 2/7) at the step-normalised one. The residue is
therefore partial, and the partiality is printed rather than rounded
away.

### 5.2 The holonomy gate

The pin's requirement:

> the holonomy of the
   constructed family compared against d74's measured **⟨2,3⟩**

read as *agreement or the measured deviation, exactly*. Read instead
as equality of groups it is

> an agreement demand that is unsatisfiable by an
  identity (r_k = r_q·G/G at 1,546/1,546, deviation forced exactly at
  non-descent)

so the gate is posed here in the form it can be met or failed in:
REPRODUCED-AND-LOCATED, three conjuncts, each measured and each
killable.

D74's committed claim is the comparator for the first:

> the multiplicative
   group generated is **`⟨2,3⟩`, free abelian of rank 2, the full group of
   3-smooth positive rationals**

Three readings of the same squares, all on the carrier:

| reading | squares closing | non-unit self-loops | obstruction | primes | rank | contains ⟨2,3⟩ |
|---|---|---|---|---|---|---|
| $q$ — D74's connection | 1402 | 44 | 44 | [2, 3] | 2 | — |
| $k$ — horizon-normalized | 1402 | 52 | 44 | [2, 3, 5, 13] | 3 | yes |
| $\Gamma$ — the constructed family | 1402 | 416 non-unit of 1402 | — | [2, 3, 5, 13, 19, 97, 389] | 7 | yes |

The $q$ row reproduces D74's ladder rung digit for digit — 1402
closing, 44 obstruction, 44 self-loops, cycle rank 134 — and the
census that feeds it reproduces too: 1546 closed squares, spectrum
{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}, 88 defective.

**The deviation is derived, not observed.** The horizon-normalized
connection differs from $q$ by the exact factor

$$\frac{G(h e_A e_B,\, r-2)}{G(h e_B e_A,\, r-2)},$$

verified as an identity at 1546 of 1546 closed squares, with
correction-factor spectrum {1: 1538, 64/65: 6, 65/64: 2}. **And every
deviation is located.** Of the squares that close in the carrier,
exactly those carrying a non-unit factor sit on a class where
$G(\cdot, r-2)$ is measured to take more than one value; the factor is
1 exactly when the potential agrees at the two endpoints, and the
endpoints of a closing square lie in one class. The eight deviating
squares all sit at base depth 0, and the two rationals 64/65 and 65/64
are what add the primes 5 and 13. The converse does not hold and is
reported rather than claimed: a class can be multi-valued and still
carry a unit factor. The constructed family adds more still, because
its entries aggregate every event that carries one class into another;
its holonomy is the curvature of the *coarse* law read at the
occupancy construction, not of the descended connection, and the
segment carries that stamp.

**The negative control fires at all three readings.** On the record
quotient the obstruction is 0, the non-unit self-loops are 0, and
$\Gamma$ assigns holonomy exactly 1 to every one of the 473 squares
that close; the rung reproduces with cycle rank 145. D74's own verdict
is the comparator here too:

> removable at `[SEQ,
REC]`, NOT removable at `[MULT, STATE, PORT, MENU]`

**A methodological note this unit owes its own gate.** At the $q$
reading the *group* is not a discriminating statistic: every closed
square's ratio lies in the measured value set, so the $q$-holonomy
group of any quotient of this family is a subgroup of
$\langle 2,3 \rangle$. What discriminates a scrambled carrier is
descent and the ladder row, and the scramble control is scored on
those. The $k$ reading discriminates too, but as a *descent detector*
rather than a carrier fingerprint: it takes rank 2 wherever the
horizon potential descends and rank 3 wherever it does not.

### 5.3 The screen

U3's criterion is the input contract:

> `[B3]`'s criterion is `Γ_ij = |U_ij|²` for one unitary `U` **of the same
size**

The screen is reimplemented from the pinned code's declared decision
order, with one omission declared where it is made: U3's general
polygon obstruction needs U3's exact surd sign oracle and is not
rebuilt here. It is a necessary condition only, and the census's
single pass carries a constructed certificate, so the omission cannot
move a verdict.

The census composition is the result and is gated exactly: five
N/A-SHAPE, four S-FAIL-DS, one S-PASS. The raw transfers are not
square. The identity-padded transfers are square and fail double
stochasticity with exact deficits and an exact $L_1$ price — 70/33,
31083/4279 and 209/10 — and that failure is *forced by shape* for a
column-stochastic matrix under the padding, so the exact price is the
datum, not the failure. The mis-normalized control fails it too, which
is what makes the pass meaningful. The one S-PASS is the renewal-cut
transfer, which is exactly $J/8$ — U3's own committed `ARMC2-8x8`,
with U3's own Sylvester $H_8/\sqrt{8}$ certificate, verified here in
exact integer arithmetic. Its degeneracy is measured, not footnoted:
its columns are all equal, so it is doubly stochastic only because its
column is uniform and it is unistochastic at every $n$. **The pass
carries no quantum content whatever, and the verdict segment says so
in the segment.** The positive half of the Barandes correspondence is
empty at every object this unit builds.

The $n = 3$ discriminant cell is EMPTY-BY-SHAPE: the family's shapes
are [1, 5, 13, 45, 113] and their padded completions, and no $3 \times
3$ object arises from the construction.

### 5.4 The interpolant test

U1's caveat is carried verbatim, because it is the reason the test
needs a convention at all:

> Barandes' eq. 22 needs a square `Gamma`, i.e. his kinematical axiom: one
fixed configuration space for all cuts.  This carrier has none away from
renewals

The process's own intermediate conditional is the canonical
interpolant candidate, and it is tested triple by triple. On the
carrier it interpolates exactly at every triple whose first cut is the
root — where the first transfer has one column and the question is
degenerate — and **fails at all 4 of 10 triples with a non-degenerate
first cut**, at 34, 112, 12 and 12 cells. On the record quotient it
interpolates everywhere: the record chain is exactly lumpable, the
carrier chain is not Markov. Both statements are read at the declared
readout, and the count control of §5.1 shows the record quotient loses
its exact lumpability under the other one.

**The completion is a convention, and the fiber that matters is
measured.** Four completions are run, not one. Under the identity
padding — hold an unrealised configuration fixed — and under a cyclic
permutation padding, the first transfer is invertible at all four
triples, so eq. 22's candidate is *unique* and is computed exactly;
under a uniform padding and a marginal padding it is exactly singular,
by the certificate that two unrealised columns coincide, and the
algebraic reading says nothing at all. So the fiber that carries the
*result* is 2 of 4: two completions speak, two are silent, and the two
that speak return **identical** negative-entry counts, 36/104/108/164,
with minima $-1/97$, $-5/97$, $-1/18$ and $-1/128$. A unique candidate
that fails positivity refutes existence outright, with no Farkas
vector needed: **at every depth-cut triple with a non-degenerate first
cut, no interpolant of eq. 22's form exists**, and the refutation does
not turn on the choice between the completions that admit the
question. It is not a divisibility claim about the process at renewal
grain, where the next paragraph's wall stands.

The renewal cuts are the positive control, and U1b's wall is stated,
not evaded:

> The second transfer is column-constant for all 176
admissible maps of all four ensembles** — 0 exceptions.  By (D-2) this
forces DIVISIBLE on every admissible map before any test is run

Measured here: the renewal transfer has exactly one distinct column,
every entry $1/8$, and the counting and mass readouts agree on it.
DIVISIBLE is forced by structure at renewal grain, and **this unit
makes no indivisibility claim there, at any scope.**

### 5.5 CR-B's kernel question

CR-B's simplex is the anchored comparator: at renewal count $n = 4$
the pinned symmetry gives 3 orbits, simplex dimension 2 and
transitivity False — no unique invariant law, so the object was
missing.

**Γ's process supplies a point, and the scope of that supply is
gated.** At the declared primary readout it induces one point,
(15/38, 5/19, 13/38), at both censused cells — a point of the very
simplex CR-B's symmetry could not select. But **both cells sit at
$n = 4$**: constancy across two cells at one value of $n$ is not
$n$-indexing, and the three coordinates the R6b′ inheritance orders
carried — ordinal position, absolute depth and ensemble identity —
move together across them. The honest stamp, and the one the verdict
segment carries, is CONSTANT-ACROSS-THE-TWO-CENSUSED-CELLS-AT-n=4,
ORDINAL/DEPTH/ENSEMBLE-CONFOUNDED.

### 5.6 CR-A's mover question

Γ advances on its own carrier — the one-step columns move the class,
and the self-transitions are censused. But CR-A's census lives on
I7's record lattice and this unit's carrier is the MENU quotient of
the transport grammar, and **the number of declared maps between the
two is measured, not assumed**: every pinned source body is scanned
for a line declaring a map, a functor, a bijection, an identification,
an isomorphism or an embedding between them, and the count is zero.
The commutation status with $H_a[N]$ is therefore
BLOCKED-AT-REFERENT, the four-gate rule's first gate, and CR-A's
anchored CENSUS=8192|ADVANCING=2976|ADMISSIBLE=1232 and
FORCED=2|FORCED-ADVANCING=0 stand untouched by this unit.

### 5.7 The W-CROSS constraint

U2 measured that the three loci do not coincide at cut grain:

> No single grammar quantity predicts all three statuses

so a curvature measurement does not license a quantum verdict. This
unit makes zero curvature ⟹ quantum claims, and **the count is
measured**: every sentence of the unit's own emitted text and of this
paper is scanned for one carrying a curvature term, a quantum term and
an inference term together without a negation, and the count of such
sentences is zero. The record-grain form of the crossing remains the
open one.

### 5.8 The motivation inventory

At the RSQ standard, every construction choice classed with an exact
fiber — and the classification column is *gated* against a
machine-computed fiber wherever one exists, so a relabelled row fails
the gate.

| item | choice | class | fiber | computed from |
|---|---|---|---|---|
| I-CARRIER | the quotient Γ is read on | FORCED | 1 | the rungs rebuilt here that both descend and are non-flat |
| I-CAP | the depth cap of the carrier | FORCED | 1 | the arenas built |
| I-GRAIN | the menu grain | GENUINELY-FREE | 2 | Γ-prep's own committed grain counts |
| I-HORIZON | the horizon convention | GENUINELY-FREE | 2 | DECLARED — not computable here, and stamped as such |
| I-CUTS | the cut family | GENUINELY-FREE | 2 | the cut families built here |
| I-READOUT | the readout | GENUINELY-FREE | 3 | the distinct measured positional laws |
| I-PADDING | the completion convention for eq. 22 | GENUINELY-FREE | 2 | the completions that let the reading speak |
| I-PRUNE | the leg-2 enumeration prune | STABILIZER-FIXED | 1 | the unpruned agreement |
| I-RENEWAL | the renewal predicate | FORCED | 1 | U1's committed predicate, ported |
| I-BLOCKS | the block decomposition | FORCED | 1 | Γ-prep's committed census |

Four forced, one stabilizer-fixed, five genuinely free. The governing
register puts the load-bearing item exactly where the measurement puts
it:

> I-READOUT's fiber
  is ≥3 (the third, step-normalised law measured: 15/38, 5/19,
  13/38)

Two scopes are stamped on the rows themselves. I-CARRIER is forced
*among D74's six committed rungs* and free *in the quotient lattice* —
the ruled carrier is a strictly better one by this unit's own stated
criterion, and it is not built here. I-PADDING's fiber counts
**completions that support a reading**, not completions imaginable;
that semantics is declared rather than left to the reader.

And motivation is reported **per verdict segment**, which is what the
standard actually asks, and the answer is harsher than the inventory
census: of the seven segments the map covers, exactly 1 of 7 descends
from motivated choices alone. Every other segment — the carrier
included, through the grain — rides on at least one genuinely free
choice, and the map naming them is printed rather than summarised.

### 5.9 The 44 squares

D74's dichotomy reproduces: 44 curvature-type and 44
descent-obstruction-type, with U1's committed base-depth census
{1: 4, 2: 40} on the second half. Under the constructed family the
curvature half closes in the carrier and Γ assigns it a non-trivial
holonomy at every one of the 44, with the spectrum {1/4: 2, 1/3: 8,
8/13: 2, 13/8: 6, 3: 24, 4: 2}; the descent-obstruction half does not
close in the carrier at all, so Γ has no loop there and assigns it
nothing. **The constructed law is silent on exactly the half D74 named
as having no formalism at transport scope.** The spectrum is
readout-relative; the qualitative half — non-unit at all 44 — is not.

## 6. The verdict

Every segment is computed in-gate. The complete emitted string is then
audited by a comparator built to the strengthened standard:

> a verdict comparator shares
NOTHING with its builder — neither code, nor inputs, nor
typed literals

It takes as its only inputs the emitted string and a serialised
receipt record, which it re-parses itself; it concatenates nothing,
being a parser rather than a builder; it types no delimiter, no
segment name and no measured value, locating the head and the five
segments by search, *characterising* the connective tissue (equal
between segments, non-empty, alphanumeric-free) instead of quoting it,
proving the spans cover the string exactly, and checking every
declared measured value against the segment that carries it. Six
falsifiers attack it — appended text, a swapped head, truncation, a
dropped segment, a retyped value, and a receipt desynchronised from
the string — and each flips its predicate.

> **GMAIN-CONSTRUCTED-<CARRIER=D74-MENU-113-CLASSES-AT-(A,B)-D<=4|CUTS=5|DIMS=1x5x13x45x113|PAIRS=10|COLUMN-STOCHASTIC-EXACT-544-OF-544-COLUMNS|FLOW-IDENTITY-w(h)k_{4-|h|}=w(h+e)-3968-OF-3968|B2-BLOCKS-PURE-ON-9-OF-113-CARRIER-CLASSES|PROVENANCE=24-SHA-PINNED-SOURCES-PLUS-THE-SELF-PAPER-BYTE-ANCHORED -- REQUIREMENTS-CENSUS-SHADOW=REPRODUCED-AT-THE-COUNTING-MEASURE-THAT-DEFINED-IT-(3/7, 1/7, 3/7)-AND-(4/9, 1/9, 4/9)-EXTERNAL-CONTROL-NEVER-A-TARGET|LAW-VALUE-AT-THE-STEP-NORMALISED-PRIMARY-READOUT=(15/38, 5/19, 13/38)-AT-BOTH-LEGS-LEG-INDEPENDENT-AND-LEFT-RIGHT-ASYMMETRIC|RAW-PRODUCT-READOUT=(3/8, 1/4, 3/8)-AT-BOTH-LEGS|READOUT-FIBER>=3-H4-CHAIN-READING-EXCLUDED-BY-CAP|HOLONOMY=REPRODUCED-AND-LOCATED:D74-{2,3}-RANK-2-REPRODUCED-DIGIT-FOR-DIGIT-1402-CLOSES-44-OBSTRUCTION-44-SELFLOOPS-134-CYCLE-RANK,DEVIATION-IDENTITY-1546-OF-1546,UNLOCATED-DEVIATIONS-0,K-PRIMES-{2,3,5,13}-RANK-3-ON-A-NON-DESCENDING-CARRIER,GAMMA-PRIMES-{2,3,5,13,19,97,389}-RANK-7-AT-THE-OCCUPANCY-CONSTRUCTION,REC-FLAT-AT-3-OF-3-READINGS-AT-THE-DECLARED-READOUT|SCREEN=N/A-SHAPE:5-S-FAIL-DS:4-S-PASS:1-THE-ONE-PASS-DEGENERATE-J/8-COLUMN-CONSTANT|KERNEL=INDUCED;CONSTANT-ACROSS-THE-2-CENSUSED-CELLS-AT-n=4;ORDINAL/BASE_DEPTH/ENSEMBLE-CONFOUNDED|MOVER=BLOCKED-AT-REFERENT-0-DECLARED-MAPS-MEASURED-OVER-24-PINNED-SOURCES|INTERPOLANT=NON-MARKOV-AT-4-OF-10-DEPTH-TRIPLES-AT-THE-DECLARED-READOUT-REC-EXACTLY-LUMPABLE|EQ22=NO-FORM-INTERPOLANT-AT-4-OF-4-INVERTIBLE-TRIPLES-NEGATIVES-36/104/108/164-AT-2-OF-4-COMPLETIONS-THAT-SPEAK|44+44=44-CLOSE-44-NOT-A-LOOP -- MOTIVATION-FORCED-4|STABILIZER-FIXED-1|GENUINELY-FREE-5|I-READOUT=GENUINELY-FREE-FIBER-3-MEASURED-THE-THIRD-LAW-(15/38, 5/19, 13/38)|I-CARRIER=FORCED-AMONG-D74-RUNGS-FREE-IN-THE-LATTICE|I-PADDING=FIBER-2-COMPLETIONS-THAT-SPEAK-OF-4-TESTED|PER-SEGMENT-MOTIVATED-1-OF-7|NON-EMPTY-True -- SCOPE-CAP=(A,B)-D<=4-CARRIER-AND-D<=5-ANCHOR|GRAIN=113-CLASS-EVENTxWEIGHT|HORIZON=H4|READOUT=STEP-NORMALISED-PRIMARY-RAW-PRODUCT-AND-COUNT-MEASURED|PADDING=2-SPEAKING-OF-4-DECLARED|LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-3..10|CENSUS-SHADOW=EXTERNAL-CONTROL-NEVER-TARGET|B2-IMPORT=CENSUS-ONLY-ATOM-CLAIM-NOT-IMPORTED-3-EXCLUSIONS-NAMED|MONOTONICITY=30728-OF-243768-TRANSITIONS-CENSUSED|NO-CURVATURE=>QUANTUM-CLAIM-0-MEASURED|NO-INDIVISIBILITY-CLAIM-AT-RENEWAL-GRAIN -- SETTLEMENT=PARTIAL-FAILED-LINK-TARGETS|CONSTRUCTED=TRUE-<544-OF-544-COLUMNS-EXACT;FLOW-IDENTITY-3968-OF-3968;REBUILT-ON-BOTH-QUOTIENTS>|TARGETS=FALSE-<CENSUS-STATISTICS-AT-BIRTH-TRUE;THE-TARGET-TEST-IS-GAMMA-FREE-AND-OFF-CARRIER-TRUE-TOKEN-SCAN-0-HITS-AT-DEPTHS-3..10;THE-COUNT-READOUT-BREAKS-THE-MANDATORY-NEGATIVE-CONTROL-TRUE-REC-HOLONOMY-RANK-4-CK-10-OF-10-FAILS-0-OF-544-COLUMNS-STOCHASTIC>|HOLONOMY=TRUE-UNDER-REPRODUCED-AND-LOCATED-<D74-RUNG-DIGIT-FOR-DIGIT;DEVIATION-IDENTITY-1546-OF-1546;UNLOCATED-0;REC-FLAT>|MOTIVATION=TRUE-<READOUT-FIBER-3;THE-THIRD-STEP-NORMALISED-LAW-(15/38, 5/19, 13/38);PER-SEGMENT-MAP-1-OF-7-MOTIVATED>>**

**The settlement condition, the pin's own words:**

> QFT-needs-gravity stake is settled ONLY by: constructed ∧ targets
hit ∧ holonomy consistent ∧ motivation non-empty — anything less is
partial and says which link failed.

Evaluated at **one arena** — the declared primary readout — link by
link:

| link | measured |
|---|---|
| constructed | TRUE — exact, column-stochastic on all 544 columns, the disintegration identity exact at 3968 of 3968 transitions, built on both quotients |
| targets | FALSE — the law value at the declared primary readout is (15/38, 5/19, 13/38) at both legs; the pre-registered values are (3/7, 1/7, 3/7) and (4/9, 1/9, 4/9) |
| holonomy | TRUE under REPRODUCED-AND-LOCATED — D74's rung digit for digit, the deviation derived by an identity at 1546 of 1546 squares and located at every one of them, the control flat at all three readings |
| motivation | TRUE — readout fiber 3 with the third law measured, five of ten choices motivated, the per-segment map printed |

The failed link is the second, and the governing register states the
three convergent reasons this unit measures:

> the targets were census
  statistics at birth (their frozen source defines them by leaf
  counts); the target test is Γ-free and off-carrier (token-scan
  proof); the count readout breaks the mandatory negative control
  (REC gains holonomy; CK fails; 0/544 columns stochastic — not a
  law).

**PARTIAL. The failed link: targets.** The honest statement: the law
is constructed, its geometry is reproduced and its deviation located,
its motivation is non-empty — and the census numbers it was asked to
hit were never values of any law.

## 7. Controls and falsifiers

| control | direction | measured |
|---|---|---|
| REC quotient | negative | flat at all three readings; obstruction 0, non-unit self-loops 0, Γ-holonomy 1 on 473 of 473; exactly lumpable at every cut triple |
| the counting readout, built | negative | not a law as described (0 of 544 columns); after the undeclared repair it gives the record quotient rank 4 and destroys its lumpability at 10 of 10 triples |
| renewal cuts | positive | one distinct column, every entry $1/8$; DIVISIBLE forced by U1b's (D-2) |
| mis-normalized Γ | negative | the off-by-one horizon breaks the flow identity, so the joint stops agreeing with the marginal and the columns stop summing to 1 |
| scrambled quotient | negative | a size-matched congruential shuffle loses descent and moves D74's ladder row; the group is not the discriminating statistic and the unit says so |
| unpruned leg-2 agreement | positive | the prune reproduces the unpruned leg set on 3 of the 256 bases, leg for leg and weight for weight, at both weights |
| the re-priced law | forcing | both theorem-pass waivers are machine-checked: re-pricing every event by an arbitrary exact rational leaves properness and cut-additivity at zero violations |
| a synthetic deviation | negative | a non-unit factor planted on a carrier-closing square whose class descends fails the location gate — which is what makes the holonomy head falsifiable |
| an all-true synthetic settlement | positive | the instrument emits SETTLED on it with the falsifier sheet clean, and every one of the four links moves the emitted segment in both directions |

Coverage is measured by **reach**, not by naming: a gate counts as
covered only when a declared falsifier's injection turns that gate's
own predicate from true to false, and the reach is computed from the
observed pair rather than asserted. Every anchor row and every
verbatim row carries its own per-row drift falsifier. Both
theorem-pass waivers carry a machine-checked forcing.

## 8. Scope, and what this unit does not decide

- **No curvature ⟹ quantum claim.** U2's W-CROSS forbids it at cut
  grain and the count of such claims here is measured at zero by a
  sentence scan of the unit's own text.
- **No indivisibility claim at renewal grain**, at any scope: U1b's
  column-constancy forces DIVISIBLE before a test can run.
- **No continuum, infinite-volume, asymptotic or limit claim.**
- **No CP-divisibility, Bell, locality or covariance statement.**
- The carrier is the $(A,B)$ $d \le 4$ arena the pin declares, with a
  $d \le 5$ anchor scope. The $d \le 6$ arena is **Γ-prep's own
  delivered arena**, not an excluded one, and is not rebuilt here;
  depth 7 is what Γ-prep declares infeasible.
- **CONG-185, the ruled carrier, is not built here.** The pin names
  MENU-113 and this unit builds what the pin names. Everything this
  unit measures about non-Markovianity, about the eq.-22 candidate and
  about the k-enlargement is stamped MENU-113 in consequence.
- The three- and four-actor pools of D74 are not built here.
- The MATCHED horizon convention and the 13-class primary grain are
  named in the inventory, stamped at the import site, and not run.
- The eq.-22 inversion on the record quotient is EXCLUDED-BY-CAP.
- The exact feasibility LP is not run: the decision order stops at the
  process's own conditional and at the unique algebraic candidate
  under four declared completions.

## 9. The receipt

`v14/code/gmain_receipt.json`, written by the plain delivery run. Two
plain runs produce byte-identical `gmain_output.txt` and
`gmain_receipt.json`; every wall-clock number goes to stderr and
reaches neither file.

**The receipt-rendered values this paper's prose uses**, so that every
numeric claim above has one source of truth:

| key | value |
|---|---|
| carrier histories | 3969 |
| MENU classes | 113 |
| REC classes | 2477 |
| MENU dims per cut | [1, 5, 13, 45, 113] |
| columns, both quotients | 544 |
| flow-identity transitions | 3968 |
| R-SIG points, anchor scope | 5161 |
| carrier blocks | 9 of 113 |
| monotonicity scope | 30728 of 243768 |
| leg-1 legs | 3584 |
| leg-2 legs | 73728 |
| leg 1, PRIMARY | 15/38, 5/19, 13/38 |
| leg 1, census shadow | 3/7, 1/7, 3/7 |
| leg 2, census shadow | 4/9, 1/9, 4/9 |
| leg 1, raw product | 3/8, 1/4, 3/8 |
| cut triples failing CK | 4 of 10 |
| deviation identity | 1546 of 1546 |
| eq. 22 negatives | 36/104/108/164 |
| completions that speak | 2 of 4 |
| $k$-connection primes | [2, 3, 5, 13] |
| Γ-family primes | [2, 3, 5, 13, 19, 97, 389] |
| CR-B simplex | 3 orbits |
| count readout, literal | 0 of 544 |
| count readout, record quotient | rank 4 |
| motivation | 4 forced |
| readout | fiber is 3 |

| | |
|---|---|
| sources, by declared commit sha | 24 |
| verbatim-text anchors | 21, each with its own drift falsifier |
| byte anchors | 24, plus this paper's own |
| path-value anchors | 17, every declared probe resolved |
| declared falsifiers | 60, all killed and all *reaching* |
| coverage | every ledger entry covered by reach, none by naming |
| never-falsified without a verified waiver | 0 |
| theorem-pass waivers | 2, both with a machine-checked forcing |
| engravings swept | 12, each with a computed status |
| prose numerals | 0 unexplained |
| must-pass failures | 0 |
| arithmetic | exact `int` and `fractions.Fraction`; the file's own syntax tree carries 0 float literals |

## 10. The next-iteration register

**CONG-185, the ruled carrier.** The governing register's carrier
ruling:

> **CONG-185 supersedes MENU+G**: d74's own coarsest weighted
congruence has descent at every horizon, zero multi-valued edges,
all 44 curvature squares intact, q-holonomy ⟨2,3⟩, **k-holonomy
collapsing back to ⟨2,3⟩** (the enlargement disappears)

The recipe is one line: partition refinement of the menu partition to
a fixed point, reproducing d74's own committed row for that arena;
then re-run this battery on it. The successor is cheap.

**The disintegration criterion, properly normalised.** The readout
must be fixed by a criterion declared before the battery and
independent of any target. The criterion this unit declares, and that
the successor should pin: *the readout under which Γ is a
disintegration of one measure across cuts* — the flow identity. Every
other reading runs as a control whose declared job is to show the
battery can move, and it does.

**Law-value targets, pre-registered from the law.** A target must be a
value of the law under the declared readout, not a leaf count. The
demotion is done here; the pre-registration is the successor's. If the
corpus wants the counting values back as targets it must first pin a
typicality postulate — a separate, nameable decision that should be
taken in the open.

**The holonomy conjunct.** REPRODUCED-AND-LOCATED is the well-posed
form and it is carried forward; on the ruled carrier the k-reading is
expected to collapse onto the q-reading, which turns the located
deviation into a vanishing one.

**The [B3] feasibility LP.** The algebraic route speaks at exactly two
of the four completions tested here. The convention-free route is the
exact rational feasibility LP, and it is row-decomposable — at the
first triple it is 45 independent 13-variable non-negative feasibility
problems plus one column-sum coupling — so the scope-out is not forced
by cost. **And it must carry the block scope**: the minorization
constant is monotone under coarsening, so at the ruled carrier four of
the six delivered block rows vanish and the claim collapses to the
(1,1) block; the successor inherits only that block as live, pending
the Γ-prep adjudication. Three of the four blocks are not even
statable on the $d \le 4$ window, so the carrier must first be
extended — d74 commits the wider arm at $d \le 5$, 265 menu classes
and coarsest congruence 462.

**The lumpability / indivisibility carrier stamp — a first-class
open.** On the ruled carrier the chain is exactly lumpable, Markov at
that level, while the indivisibility signature lives at MENU. **The
quantum character of Γ is carrier-relative.** The next iteration must
measure the signature at both levels and stamp every quantum-shape
claim with the carrier it is read at. This unit's non-Markov and
eq.-22 results are stamped MENU-113 accordingly.

**The cross-unit rows this unit leans on and does not pin.** Γ-prep's
$d \le 6$ arena and d74's $d \le 5$ arm are both rows the successor
needs and the supply lists do not carry. Pin both explicitly.
