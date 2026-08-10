# Γ-MAIN — The geometry-update law

**Status:** `GREEN-UNREVIEWED` — delivered under
`v14/note-gmain-pin.md`, sha256-12 `8529ddc4a319` (v14 ledger #64).
Not citable until an external hostile round confers terminal.

**Artifacts:** `v14/code/gmain_exact.py`,
`v14/code/gmain_output.txt`, `v14/code/gmain_receipt.json`. Every
number below renders from the receipt.

---

## Abstract

This unit constructs $\Gamma(\mathrm{cut}' \leftarrow \mathrm{cut})$ —
the geometry-update law the corpus has been naming for two units and
had not built — and then tries to break it with a nine-test battery
that was registered before it ran.

The construction lands. On D74's committed MENU quotient, at the
$(A,B)$ depth-4 cap, $\Gamma$ is an exact rational column-stochastic
family between the five declared depth cuts, of dimensions
[1, 5, 13, 45, 113] over 3969 histories and 113 classes, built from
the pinned relative-horizon kernels, with every one of its 20
transfers verified column-stochastic in exact arithmetic. The record
quotient, 2477 classes, is carried beside it as the negative control
at every step.

The battery then splits the result in two, and the split is the
finding. **The pre-registered position-law targets are hit exactly —
(3/7, 1/7, 3/7) at leg 1 and (4/9, 1/9, 4/9) at leg 2 — but only at
one of the two readouts the construction admits, and the other readout
is the process's own law.** The occupancy readout returns
(3/8, 1/4, 3/8) at *both* legs, and the exact cause is measured: the
delivery budget is a quarter per actor divided by the holder's
holdings, so the delivery sector's total mass is $1/2$ at every
renewal base while its *count* moves from 4 to 6. The quarter law
makes the process's own readout multiplicity-blind. F8's mechanism —
no delivery in the middle interior slot — is not imported but derived:
after a delivery the two live proposals are order-comparable at
512 of 512 instances, and a pair-arbitration needs two incomparable
ones.

**The holonomy gate deviates, and the deviation is exact.** D74's
group reproduces on the carrier, primes {2, 3}, rank 2, obstruction 44,
1402 squares closing. The horizon normalization — the step that makes
the construction possible at all — enlarges it to primes
[2, 3, 5, 13] by adding exactly eight self-loops at $64/65$ and
$65/64$, and the constructed family itself carries primes
[2, 3, 5, 13, 19, 97, 389]. Both enlargements contain $\langle 2,3
\rangle$; neither equals it. The negative control is flat at all
three readings, and the record chain is exactly lumpable where the
carrier is not: the class chain fails Chapman-Kolmogorov at 4 of the
10 depth-cut triples, and at every one of those four eq. 22's unique
algebraic candidate carries negative entries, so no interpolant of
that form exists there at all.

The motivation inventory is non-empty and honest: ten choices, five
of them forced or stabilizer-fixed, five genuinely free with exact
fibers — and the free one that matters is the readout, whose fiber of
two is what the targets select.

So the settlement condition is evaluated and reported PARTIAL, with
the failed link named: the holonomy is not consistent with
$\langle 2,3 \rangle$, it strictly contains it.

---

## 1. What this unit is for, and what it is not

CR-A named the missing object — CRA-BLOCKED-AT-STATIC-GEOMETRY-<MISSING=A-GEOMETRY-UPDATE-LAW — and CR-B named the
other one:

THE-INTERVAL-POSITIONAL-LAW-=-THE-TRANSITION-KERNEL-BETWEEN-AN-INTERVALS-ENDPOINTS-WHOSE-RENEWAL-COUNT-IS-N

This unit builds a law and measures what it does to both. It does not
re-pose the transport-scope chain, whose attempt is terminal-negative
(the escape); it does not claim a continuum limit; it makes no
curvature ⟹ quantum claim, and §8 says why it may not.

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
| readout | OCCUPANCY primary, COUNT alternative — both measured, the fiber is 2 |
| provenance | declared commit shas; 23 hash-pinned artifacts |

## 3. Provenance, and the discipline it is read under

Every cross-unit read in this unit goes through `git show
<sha>:<path>` at a sha declared in the frozen text; worktree bytes and
`git show HEAD:` are mutable state and are read for no source. Thirteen
verbatim-text anchors bind quote fidelity — the quotations in this
paper against the sources' committed bytes — and are evaluated first,
with a genuine short-circuit: a failing quotation exits the run before
a single byte anchor is evaluated. Each is bound to a named consumer
gate that exists, is non-literal, and dies to a declared mutant.

The named exclusions are printed in-unit and honoured: u1c (not
citable), d56 (reachable only through d57's pin, not reached), the two
index documents, `v14/LOG.md` and `/STATUS.md` as forbidden runtime
inputs, and the R6b′ delivery artifacts, which are mid-repair — the
adjudication register at its own declared sha is the frozen carrier of
what this unit inherits. The v14 LOG #4 erratum is carried as a frozen
declaration rather than read: this unit reads neither paper the erratum
touches and no verdict segment descends from those rows.

## 4. The construction

$\Gamma$ is the transport process read on the carrier. The
relative-horizon kernel is

$$k_r(e \mid h) \;=\; \frac{q(e \mid h)\, G(h+e,\, r-1)}{G(h, r)},$$

with $G$ the finite-horizon potential of the committed layer; the root
potentials reproduce Γ-prep's committed values exactly. The chain's
own law at depth $d$ is $w(h) = \mu(h)\, G(h, 4-d) / G(\text{root}, 4)$,
which has cut mass 1 at every cut, and the identity
$w(h)\, k_r(e \mid h) = w(h+e)$ makes the class-level law the exact
conditional

$$\Gamma(d' \leftarrow d)[s', s] \;=\; \frac{\sum_{h \in s,\, |h| = d}\;
\sum_{h' \in s',\, h' \succ h} w(h')}{\sum_{h \in s,\, |h| = d} w(h)},$$

column-stochastic by construction and verified so, exactly, on all 20
transfers of the two quotients.

**Why a readout has to be declared.** The horizon potential is *not*
class-constant on the carrier: $G(\cdot, 2)$ takes more than one value
on 4 of the 13 classes the depth-2 cut carries. So the horizon kernel
does not descend, a lift is needed, and naming one silently would be
an arena artefact. Two are declared: OCCUPANCY, the process's own law
above; and COUNT, the same construction with the uniform measure on
the admissible objects. On the record quotient the potential *does*
descend, at every horizon, which is why the control behaves.

**The block decomposition.** Γ-prep's B2 atoms — the holdings-profile
blocks of R-SIG — are read, not chosen: 5161 R-SIG points, 1365 of
them menu-exact, in blocks {(1,1): 1365, (2,2): 3788, (2,3): 4,
(3,2): 4}, reproducing the committed census exactly, and every carrier
class that meets R-SIG meets exactly one block. Γ-prep's blocking fact
is inherited with it:

The holdings profile decreases at
**zero** transitions of the family: it is a monotone non-decreasing

## 5. The battery

### 5.1 The position-law targets

The R6b′ register pre-registered them: reproduce (3/7,1/7,3/7) at leg 1 and
(4/9,1/9,4/9) at leg 2.

Leg 1 is scanned **unpruned** — 152672 raw continuations generated
from the 16 renewal-1 bases and only then filtered, returning 3584
legs in exactly five patterns. Leg 2 is scanned over all 256
renewal-2 bases with a pattern prune that is gated rather than
assumed: on a declared subsample the unpruned scan returns the pruned
leg set leg for leg and weight for weight.

| | leg 1 | leg 2 |
|---|---|---|
| COUNT readout | (3/7, 1/7, 3/7) | (4/9, 1/9, 4/9) |
| OCCUPANCY readout | (3/8, 1/4, 3/8) | (3/8, 1/4, 3/8) |
| delivery multiplicity | 2 | 3 |
| delivery sector mass | $1/2$ | $1/2$ |

**The targets are hit at the COUNT readout and missed at the
OCCUPANCY readout, and the head says so.** The cause is measured, not
argued: the delivery budget is a quarter per actor divided by
$\lvert \mathrm{hold}(a) \rvert$, so adding a version splits the same
mass into more entries. The sector masses are identical at the two
legs while the delivery count moves from 4 to 6 — the quarter law
makes the process's own readout multiplicity-blind, and
$(m+1)/(2m+3)$ is $3/7$ at $m = 2$ and $4/9$ at $m = 3$ only for the
readout that can see $m$.

**F8, derived rather than imported.** The register records the
mechanism as (p,d,p,r) does not
occur: no delivery in the middle interior slot**; delivery
multiplicity 2→3 drives 3/7→4/9. Here it is a measurement of
this unit's own scan: deliveries occur in slots 1 and 3 at 1024 legs
each and in slot 2 at 0, and the cause is exhibited — after
$(p, d, p)$ the two live proposals are order-comparable at 512 of 512
instances, because the delivery joins the two actors' registers, while
after $(p, n, p)$ they are comparable at 0; a pair-arbitration needs
two incomparable live proposals, so the pattern cannot close.

### 5.2 The holonomy gate

The pin's requirement: the holonomy of the
   constructed family compared against d74's measured **⟨2,3⟩** — agreement or the measured
deviation, exactly; REC flat.

D74's committed claim is the comparator:

the multiplicative
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

**The deviation is an enlargement with a located cause.** The
horizon-normalized connection differs from $q$ by the factor
$G(h e_A e_B,\, r-2) / G(h e_B e_A,\, r-2)$, which is 1 exactly when
the potential agrees on the two endpoints — and the potential is the
quantity measured above *not* to descend. Eight squares pick up the
values $64/65$ and $65/64$, and those two rationals are what add the
primes 5 and 13. The constructed family adds more still, because its
entries aggregate every event that carries one class into another;
its holonomy is the curvature of the *coarse* law, not of the
descended connection.

**The negative control fires at all three readings.** On the record
quotient the obstruction is 0, the non-unit self-loops are 0, and
$\Gamma$ assigns holonomy exactly 1 to every one of the 473 squares
that close. D74's own verdict is the comparator here too:
removable at `[SEQ,
REC]`, NOT removable at `[MULT, STATE, PORT, MENU]`

**A methodological note this unit owes its own gate.** At the $q$
reading the *group* is not a discriminating statistic: every closed
square's ratio lies in the measured value set, so the $q$-holonomy
group of any quotient of this family is a subgroup of
$\langle 2,3 \rangle$. What discriminates a scrambled carrier is
descent and the ladder row, and the scramble control is scored on
those. The group *does* discriminate at the $k$ and $\Gamma$ readings,
which leave $\langle 2,3 \rangle$ on the true carrier.

### 5.3 The screen

U3's criterion is the input contract: `[B3]`'s criterion is `Γ_ij = |U_ij|²` for one unitary `U` **of the same
size** The screen is
reimplemented from the pinned code's declared decision order, with one
omission declared where it is made: U3's general polygon obstruction
needs U3's exact surd sign oracle and is not rebuilt here. It is a
necessary condition only, and the census's single pass carries a
constructed certificate, so the omission cannot move a verdict.

The census is the result. The raw transfers are not square and return
N/A-SHAPE. The identity-padded transfers are square and fail double
stochasticity with exact deficits and an exact $L_1$ price. The
mis-normalized control fails it too, which is what makes the pass
meaningful. The one S-PASS is the renewal-cut transfer, which is
exactly $J/8$ — U3's own committed `ARMC2-8x8`, with U3's own
Sylvester $H_8/\sqrt{8}$ certificate, verified here in exact integer
arithmetic. U3's qualifier is carried and not softened: $J/n$ is
column-constant, is doubly stochastic only because its column is
uniform, and is unistochastic at every $n$ — the pass carries no
quantum content whatever.

The $n = 3$ discriminant cell is EMPTY-BY-SHAPE: the family's shapes
are [1, 5, 13, 45, 113] and their padded completions, and no $3 \times
3$ object arises from the construction.

### 5.4 The interpolant test

U1's caveat is carried verbatim, because it is the reason the test
needs a convention at all:

Barandes' eq. 22 needs a square `Gamma`, i.e. his kinematical axiom: one
fixed configuration space for all cuts.  This carrier has none away from
renewals

The identity padding is a CONVENTION — an unrealised configuration is
held fixed by the law — and every count below is relative to it.

The process's own intermediate conditional is the canonical
interpolant candidate, and it is tested triple by triple. On the
carrier it interpolates exactly at every triple whose first cut is the
root (where the first transfer has one column and the question is
degenerate) and **fails at all 4 triples with a non-degenerate first
cut**, at 34, 112, 12 and 12 cells. On the record quotient it
interpolates everywhere: the record chain is exactly lumpable, the
carrier chain is not Markov.

**And the algebraic reading is not silent here, as U1b's was.** Under
the padding convention the first transfer is invertible at all four
triples — the padded matrix is the identity outside the realised
columns, so its inverse costs the cube of the realised count and not
of the label count — so eq. 22's candidate is *unique*, and it is
computed exactly. It carries negative entries at all four. A unique
candidate that fails positivity refutes existence outright, with no
Farkas vector needed: **at every depth-cut triple with a non-degenerate
first cut, no interpolant of eq. 22's form exists.** The verdict is
relative to the padding convention and is quoted with it, and it is
not a divisibility claim about the process at renewal grain, where the
next paragraph's wall stands.

The renewal cuts are the positive control, and U1b's wall is stated,
not evaded:

The second transfer is column-constant for all 176
admissible maps of all four ensembles** — 0 exceptions.  By (D-2) this
forces DIVISIBLE on every admissible map before any test is run

Measured here: the renewal transfer has exactly one distinct column,
every entry $1/8$, and the count and occupancy readouts agree on it.
DIVISIBLE is forced by structure at renewal grain, and **this unit
makes no indivisibility claim there, at any scope.**

### 5.5 CR-B's kernel question

CR-B's simplex is the anchored comparator: at renewal count $n = 4$
the pinned symmetry gives 3 orbits, simplex dimension 2 and
transitivity False — no unique invariant law, so the object was
missing.

**Γ supplies a point, and which point depends on the readout — so the
answer to CR-B is readout-relative and both halves are printed.** At
the occupancy readout Γ induces one point, (3/8, 1/4, 3/8), at both
legs: that *is* an $n$-indexed interval-positional kernel, exactly the
object CR-B named missing, and it is neither pre-registered target. At
the count readout Γ induces two points, (3/7, 1/7, 3/7) and
(4/9, 1/9, 4/9), at the same $n = 4$: those *are* the targets, and
they refute an $n$-indexed law. The missing object exists at one
readout and cannot exist at the other, and the targets select the
readout at which it cannot.

### 5.6 CR-A's mover question

Γ advances on its own carrier — the one-step columns move the class,
and the self-transitions are censused. But CR-A's 8192-candidate
census lives on I7's record lattice and this unit's carrier is the
MENU quotient of the transport grammar; **no pinned source declares a
map between them.** The commutation status with $H_a[N]$ is therefore
BLOCKED-AT-REFERENT, the four-gate rule's first gate, and CR-A's
anchored `CENSUS=8192|ADVANCING=2976|ADMISSIBLE=1232` and
`FORCED=2|FORCED-ADVANCING=0` stand untouched by this unit.

### 5.7 The W-CROSS constraint

U2 measured that the three loci do not coincide at cut grain:
No single grammar quantity predicts all three statuses — so a curvature measurement does not license a quantum
verdict. This unit therefore makes zero curvature ⟹ quantum claims,
and the count is gated rather than promised. The record-grain form of
the crossing remains the open one.

### 5.8 The motivation inventory

At the RSQ standard, every construction choice classed with an exact
fiber.

| item | choice | class | fiber |
|---|---|---|---|
| I-CARRIER | the quotient Γ is read on | FORCED | 1 |
| I-CAP | the depth cap of the carrier | FORCED | 1 |
| I-GRAIN | the menu grain | GENUINELY-FREE | 2 |
| I-HORIZON | the horizon convention | GENUINELY-FREE | 2 |
| I-CUTS | the cut family | GENUINELY-FREE | 2 |
| I-READOUT | the class-level readout | GENUINELY-FREE | 2 |
| I-PADDING | the identity padding for eq. 22 | GENUINELY-FREE | 2 |
| I-PRUNE | the leg-2 enumeration prune | STABILIZER-FIXED | 1 |
| I-RENEWAL | the renewal predicate | FORCED | 1 |
| I-BLOCKS | the block decomposition | FORCED | 1 |

Four forced, one stabilizer-fixed, five genuinely free. The inventory
is not empty on the motivated side, and the free item that carries the
unit is I-READOUT: its fiber of two is exactly the fiber the targets
select, and the two readings disagree on the pre-registered values.

### 5.9 The 44 squares

D74's dichotomy reproduces: 44 curvature-type and 44
descent-obstruction-type, with U1's committed base-depth census {1: 4,
2: 40} on the second half. Under the constructed family the curvature
half closes in the carrier and Γ assigns it a non-trivial holonomy;
the descent-obstruction half does not close in the carrier at all, so
Γ has no loop there and assigns it nothing. Γ's holonomy on the 44 that close is non-unit at
every one of them, with the spectrum {1/4: 2, 1/3: 8, 8/13: 2,
13/8: 6, 3: 24, 4: 2}. **The constructed law is silent on exactly the
half D74 named as having no formalism at transport scope.**

## 6. The verdict

Composed, every segment computed in-gate, the complete emitted string
compared for equality against a segment-by-segment rebuild from the
measured values, with five verdict falsifiers — value swap, appended
text, truncation, dropped segment, retyped segment — each proving the
derivation can fail.

> **GMAIN-CONSTRUCTED-<CARRIER=D74-MENU-113-CLASSES-AT-(A,B)-D<=4|CUTS=5|DIMS=1x5x13x45x113|PAIRS=10|COLUMN-STOCHASTIC-EXACT|PROVENANCE=23-SHA-PINNED-ARTIFACTS -- REQUIREMENTS-TARGETS=TARGETS-HIT-AT-THE-COUNT-READOUT-MISSED-AT-THE-OCCUPANCY-READOUT|HOLONOMY=DEVIATE-AT-BOTH:D74-{2,3}-RANK-2-REPRODUCED,K-PRIMES-{2,3,5,13}-RANK-3,GAMMA-PRIMES-{2,3,5,13,19,97,389}-RANK-7,REC-FLAT-AT-ALL-THREE-READINGS|SCREEN=N/A-SHAPE:5-S-FAIL-DS:4-S-PASS:1|KERNEL=INDUCED;N-INDEXED-AT-OCCUPANCY;LEG-INDEXED-AT-COUNT|MOVER=BLOCKED-AT-REFERENT-NO-SHARED-CARRIER-WITH-H_a[N]|INTERPOLANT=NON-MARKOV-AT-4-OF-10-DEPTH-TRIPLES-REC-EXACTLY-LUMPABLE|44+44=44-CLOSE-44-NOT-A-LOOP -- MOTIVATION-FORCED-4|STABILIZER-FIXED-1|GENUINELY-FREE-5|I-READOUT=GENUINELY-FREE-FIBER-2-AND-TARGET-SELECTING|NON-EMPTY-True -- SCOPE-CAP=(A,B)-D<=4-CARRIER-AND-D<=5-ANCHOR|GRAIN=113-CLASS-EVENTxWEIGHT|HORIZON=H4|READOUT=OCCUPANCY-PRIMARY-COUNT-DECLARED|PADDING=U1-IDENTITY-CONVENTION|LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-3..10|DELIVERY-FREE-SHADOW=CONTROL-NEVER-TARGET|NO-CURVATURE=>QUANTUM-CLAIM|NO-INDIVISIBILITY-CLAIM-AT-RENEWAL-GRAIN -- SETTLEMENT=PARTIAL-FAILED-LINK-HOLONOMY-CONSISTENT>**

**The settlement condition, the pin's own words:**

QFT-needs-gravity stake is settled ONLY by: constructed ∧ targets
hit ∧ holonomy consistent ∧ motivation non-empty — anything less is
partial and says which link failed.

Evaluated link by link:

| link | measured |
|---|---|
| constructed | True |
| targets hit | True — TARGETS-HIT-AT-THE-COUNT-READOUT-MISSED-AT-THE-OCCUPANCY-READOUT |
| holonomy consistent | False — DEVIATE-AT-BOTH |
| motivation non-empty | True |

**PARTIAL. The failed link(s): holonomy_consistent.**

## 7. Controls and falsifiers

| control | direction | measured |
|---|---|---|
| REC quotient | negative | flat at all three readings; obstruction 0, non-unit self-loops 0, Γ-holonomy 1 on 473 of 473; and exactly lumpable at every cut triple |
| renewal cuts | positive | one distinct column, every entry $1/8$; DIVISIBLE forced by U1b's (D-2) |
| mis-normalized Γ | negative | dividing by $G(h, r-1)$ where $G(h,r)$ belongs breaks column-stochasticity, and the padded re-weighted transfer fails the screen's DS test with an exact deficit |
| scrambled quotient | negative | a size-matched congruential shuffle loses descent and moves D74's ladder row; the group is not the discriminating statistic and the unit says so |
| unpruned leg-2 agreement | positive | the prune reproduces the unpruned leg set on a declared subsample, leg for leg and weight for weight |
| grain, horizon, readout | declared | each an inventory item with its fiber |

## 8. Scope, and what this unit does not decide

- **No curvature ⟹ quantum claim.** U2's W-CROSS forbids it at cut
  grain and the count of such claims here is gated at zero.
- **No indivisibility claim at renewal grain**, at any scope: U1b's
  column-constancy forces DIVISIBLE before a test can run.
- **No continuum, infinite-volume, asymptotic or limit claim.**
- **No CP-divisibility, Bell, locality or covariance statement.**
- The carrier is the $(A,B)$ $d \le 4$ arena the pin declares; the
  $d \le 6$ and $d \le 7$ arenas are EXCLUDED-BY-CAP, Γ-prep having
  declared depth 7 infeasible.
- The three- and four-actor pools of D74 are not built here.
- The MATCHED horizon convention and the 13-class primary grain are
  named in the inventory and not run.
- The eq.-22 inversion on the record quotient is EXCLUDED-BY-CAP.
- The exact feasibility LP is not run: the decision order stops at the
  process's own conditional and the unique algebraic candidate,
  exactly as U1 and U1b declare theirs.

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
| R-SIG points | 5161 |
| leg-1 legs | 3584 |
| leg-2 legs | 73728 |
| leg 1, COUNT | 3/7, 1/7, 3/7 |
| leg 2, COUNT | 4/9, 1/9, 4/9 |
| leg 1, OCCUPANCY | 3/8, 1/4, 3/8 |
| cut triples failing CK | 4 |
| $k$-connection primes | [2, 3, 5, 13] |
| Γ-family primes | [2, 3, 5, 13, 19, 97, 389] |

| | |
|---|---|
| sources, by declared commit sha | 23 |
| verbatim-text anchors | 13 |
| byte anchors | 23 |
| path-value anchors | 9 |
| gates | 88 (33 must-pass, 0 failures) |
| mutants | 36 declared, 36 killed |
| never-falsified | 2, unwaived non-anchor 0 |
| engravings swept | 10 of the ten, each with a computed status |
| arithmetic | exact `int` and `fractions.Fraction`; the file's own syntax tree carries 0 float literals |
