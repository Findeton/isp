# Γ-ITERATION — The law on the ruled carrier

**Status:** `GREEN-UNREVIEWED`, 2026-08-10 — delivered under
`v14/note-giter-pin.md` (v14 ledger #109), whose parents are Γ-main
(paper-12) and Γ-prep (paper-11), both terminal, and whose governing
authorities are the two joint adjudications. Not citable until an
external hostile round confers terminal. Between delivery and
adjudication every headline below is a **candidate reading**.

**Artifacts:** `v14/code/giter_exact.py`, `v14/code/giter_output.txt`,
`v14/code/giter_receipt.json`. Every number below renders from the
receipt, and the paper is swept inside the delivery run for the ones
that do not.

---

## Abstract

Γ-main built the geometry-update law on the weighted-menu quotient and
its adjudication ruled that the law belongs somewhere else: on
CONG-185, the coarsest weighted congruence of the same arena. This unit
builds it there.

**The carrier is re-derived and gated before it is used.** Partition
refinement of the menu partition reaches its fixed point at 185 classes
after 5 rounds, and all six ruling properties hold on the result, each
measured on its own object: the horizon potential descends at every
horizon (0 multi-valued classes at r = 0, 1, 2, 3 and 4, against 4 of 13
at horizon 2 on the predecessor carrier); there are 0 multi-valued
labelled edges, in the weight and in the target; all 44 curvature
squares survive, and they are the same 44 *as sets*, symmetric
difference 0; both holonomy readings return prime support {2, 3} at rank
2, so the horizon normalisation's enlargement to {2, 3, 5, 13} at rank 3
disappears; and the class chain is exactly lumpable, Chapman–Kolmogorov
holding at all 10 depth-cut triples where the predecessor carrier fails
at 4.

**The law is exact and the targets are hit.** Γ is an exact rational
column-stochastic family between the five depth cuts, of dimensions
[1, 5, 17, 49, 113] over 3969 histories and 185 classes, all 102 of its
columns verified column-stochastic in exact arithmetic, with the
disintegration identity exact at 3968 of 3968 transitions and false at
352 of the 596 tests at any other admissible horizon. The step-normalised
readout is re-proved on *this* carrier to be exactly the pinned kernel
k₁ — 0 violations of 30728 kernel entries, against 1340 of 3968 for the
horizon-2 kernel — and at that readout the positional law is
(15/38, 5/19, 13/38) at both legs. Those were the pre-registered
targets, and they were pre-registered **from the law**. The two
leaf-count triples are reproduced exactly, at the counting measure that
defined them, as a declared external control that touches no object of
the constructed family.

**The holonomy agrees.** On the ruled carrier r_k = r_q at 1362 of 1362
closing squares with 0 deviations, and the deviation identity
r_k = r_q·G(h e_A e_B, r−2)/G(h e_B e_A, r−2) still holds at 1546 of
1546 closed squares as a killable must-pass. The 8 non-unit correction
factors that produced the predecessor's enlargement all sit on squares
that close in the predecessor carrier and in none of the ruled one.

**The quantum character is carrier-relative, and the relativity has a
mechanism.** At MENU-113 the chain is non-Markov at 4 of 10 depth
triples and eq. 22's unique algebraic candidate carries 36, 104, 108 and
164 negative entries under the 2 of 4 completions that speak; at
CONG-185 the chain is Markov, exactly lumpable, and all 4 completions
are silent. The whole signature is carried by the 4 multi-target
labelled edges of the coarser quotient, which sit on the 4 menu classes
that recur across depth cuts.

**And the [B3] obstruction is the column-sum coupling, not the rows.**
Convention-free, the row-decomposed feasibility problem is feasible at
every one of its 772 rows, at both carriers and at all four triples,
every verdict certified. Coupled, the same problem is feasible at 4 of 4
triples at CONG-185 with an exhibited witness, and infeasible at 3 of 4
at MENU-113 with a Farkas certificate at each. The predecessor's
padding-based "no interpolant exists at 4 of 4" is a convention effect
at one triple.

**The anchor is sedimentary.** At the ruled carrier no class is ever
revisited — 0 of 185 classes occur at more than one depth cut — the one
surviving small set is entered at 0 transitions, and its δ\* falls from
1 to 0 under the refinement. The renewal-root candidate fails at the
class grain for a measured reason, so the long-run structure is argued
from accumulation, not return, and the grading that forbids return is
itself measured to be cap-driven.

---

## 1. What this unit is for, and what it is not

Γ-main's §10 register named the successor: rebuild the battery on the
ruled carrier, pre-register targets that are values of the law, carry
the holonomy conjunct in its well-posed form, run the [B3] feasibility
LP, and stamp every quantum-shape claim with the carrier it is read at.
This unit does those five things and answers the adjudicated open they
were named around.

It does not re-pose the transport-scope chain, whose attempt is
terminal-negative. It claims no continuum and no limit. It makes no
curvature ⟹ quantum claim. It asserts no recurrence anywhere.

## 2. The declared arena

Declared as data, before anything is computed, and matched at every use.

| coordinate | declaration |
|---|---|
| boundary | the empty history; genesis is the committed layer's declared boundary |
| family | actor pool (A, B), exhaustive menus; depth ≤ 4 for the carrier, depth ≤ 5 for the anchor scope |
| law | the committed transport weight law, exec'd from its pinned bytes; nothing about admission or pricing re-implemented |
| state | the history itself; every coarser object is a declared abstraction, named at each use |
| carrier | CONG-185, the coarsest weighted congruence at (A, B) d ≤ 4, re-derived in unit and gated on six properties before use |
| contrast carrier | MENU-113, the weighted-menu partition — the carrier the predecessor built |
| negative control | the record quotient, 2477 classes, measured flat |
| cuts | depth cuts 0 … 4; the renewal-leg ensembles at the declared deeper conditioned scope |
| horizon | H4 — a history at depth d steps under k₄₋d, terminal G(h, 0) = 1; MATCHED is also run where a predecessor row is stated at it, and is named at each use |
| readout | primary: the step-normalised law q/M, re-proved here to be exactly k₁. Also measured: the raw price product, and the counting measure |
| targets | pre-registered **from the law**: (15/38, 5/19, 13/38) at both legs |
| census shadow | the two leaf-count triples are a declared external control, never a target |
| provenance | 13 sha-pinned sources plus this unit's own paper, byte-anchored; 1 declared and not read |

## 3. Provenance, and the discipline it is read under

Every source is read from a path resolved from the delivery file's own
location and gated against a sha256-12 declared in the frozen pin. No
subprocess is spawned, no version-control command is invoked, and no
moving reference is read: a drifted source dies at its byte anchor
before a single measurement runs. That is what a pinned-sha read buys
without a version-control system present, and it is why the plain run
byte-reproduces off-tree and with git absent.

19 verbatim-context windows bind quote fidelity — each at least 40
characters, each located exactly once in its source, each bound to a
*registered* consumer gate, and each perturbed at a content-bearing
token and re-located, so that a row counts as covered only when its own
predicate flips; 19 of 19 do. 11 path-value probes resolve into the two
pinned receipts and match declared values; an unresolvable probe aborts
the delivery rather than being swallowed.

**One source is declared and not read.** The pin cites the weld-2
re-derivation of the same carrier as a cross-check, "cited, not
imported". Its pinned sha is not the sha at the tip and its working copy
is being rewritten by a concurrent unit, so its bytes move. A file whose
bytes move cannot be a runtime input of a byte-reproducible run. The
citation is carried as a frozen declaration and this unit re-derives the
carrier itself instead.

The delivery ships an argv-parsed command line: unknown flags exit 2
rather than being ignored; `--selftest` corrupts exactly one declared
anchor, confirms the delivery is refused, and writes nothing;
`--mutant NAME` evaluates one declared falsifier and leaves every
artifact untouched; `--list-gates` and `--list-mutants` print the
registries the run delivers. Every failure path writes nothing, and the
one success path re-reads what it wrote and compares it against a digest
accumulated inside the emitter at emission time.

## 4. The carrier, re-derived and gated

The recipe is the predecessor's own, quoted from its receipt and re-run
here rather than imported: refine the menu partition by
successor-closure — a history's signature is its current class together
with the multiset of (event label, successor class) over the successors
that lie inside the window — and iterate to a fixed point.

From the pinned layer, the family carries [1, 8, 60, 452, 3448, 26760]
histories per level and [1, 9, 69, 521, 3969, 30729] cumulatively; the
carrier arena is the 3969 histories of depth ≤ 4. The menu partition has
113 classes and the record quotient 2477. The refinement reaches
185 classes after 5 rounds, its per-round class counts running
162, 179, 184, 185, 185, and the number of classes still spanning more
than one depth cut falling 17, 5, 1, 0, 0.

**The six ruling properties, one object at a time.**

| # | property | @CONG-185 | @MENU-113 |
|---|---|---|---|
| 1 | descent at every horizon | 0 multi-valued classes at r = 0, 1, 2, 3, 4 | 4 of 13 at r = 2 |
| 2 | multi-valued labelled edges | 0 weight and 0 target of 572 | 0 weight and 4 target of 368 |
| 3 | curvature squares intact | 44 of 88, symmetric difference 0 | 44 of 88 |
| 4 | q-holonomy | primes [2, 3], rank 2, obstruction 44 | primes [2, 3], rank 2 |
| 5 | k-holonomy | primes [2, 3], rank 2 | primes [2, 3, 5, 13], rank 3 |
| 6 | exact lumpability | 0 of 10 triples fail | 4 of 10 fail |

All six hold; the contrast carrier scores 2 of 6. The square census
reproduces the committed row exactly — 1546 closed, 28 AB-only,
12 BA-only, 142 both-blocked, non-unit spectrum {1/2: 70, 2/3: 2,
3/2: 6, 2: 10}, 88 defective — and the ruled carrier closes 1362 of the
1546 against the predecessor's 1402, while the record quotient closes
473 and none of the 88.

Property 3 is gated as a **set identity** and not as a count: the 44 the
ruled carrier closes are the same 44 the predecessor carrier closes,
symmetric difference 0. Property 2 carries the clause a congruence buys
and a menu partition does not — single-valuedness of the *target*, not
only of the weight — and that clause is what makes the class process a
probabilistic bisimulation and what §7 identifies as the mechanism
behind the whole carrier-relativity.

**The carrier is not a label.** A size-matched shuffle — the same number
of classes and the same multiset of class sizes, cut out of a fixed
ordering of the histories instead of read off the menus — loses descent
and single-valuedness at once, so the six properties are properties of
the partition and not of its cardinality.

## 5. The law and its targets

Γ is the transport process read on the carrier. The relative-horizon
kernel is k_r(e|h) = q(e|h) G(h+e, r−1) / G(h, r), the chain's own law
at depth d is w(h) = μ(h) G(h, 4−d) / G(root, 4), which has cut mass 1
at every one of the 5 cuts, and the disintegration identity

  w(h) · k₄₋|h|(e|h) = w(h+e)

makes the class-level law the exact conditional. It holds at 3968 of
3968 transitions with 0 violations. **The horizon in it is not free:**
at every other admissible horizon the identity fails at 352 of 596
tests, so written with r free it is false. Γ then has dimensions
[1, 5, 17, 49, 113] across the 10 cut pairs, 102 columns, every one of
them summing to 1 in exact rational arithmetic with 0 negative entries.

**The readout is re-proved on this carrier, not assumed.** The local
menu mass M(h) takes the value 2 at 3757 carrier histories and 5/2 at
212, so it is not constant on histories and a raw product of weights
along a path is not a probability; it *is* class-constant on both
quotients, which is descent at horizon 1. Normalising each step gives
q/M, and q/M is exactly k₁ because G(h, 1) = M(h): 0 violations over
30728 kernel entries, where the same identification against the
horizon-2 kernel fails at 1340 of 3968. The primary readout is therefore
the r = 1 member of the very kernel family Γ is built from.

**The targets, pre-registered from the law, are hit.**

| readout | leg 1 | leg 2 | leg-independent |
|---|---|---|---|
| primary, step-normalised q/M = k₁ | (15/38, 5/19, 13/38) | (15/38, 5/19, 13/38) | yes |
| raw price product | (3/8, 1/4, 3/8) | (3/8, 1/4, 3/8) | yes |
| counting measure (the shadow's own) | (3/7, 1/7, 3/7) | (4/9, 1/9, 4/9) | no |

Leg 1 is scanned unpruned — 152672 raw continuations generated from the
16 renewal-1 bases and only then filtered, returning 3584 legs. Leg 2 is
scanned over all 256 renewal-2 bases, 796672 expansions, 73728 legs,
with a pattern prune that is gated rather than assumed: on 3 of the 256
bases the unpruned scan generates 60492 continuations and returns 864
legs, identical to the pruned set leg for leg and weight for weight, at
both weights.

The law value is leg-independent and left–right asymmetric, 15/38
against 13/38, which no other reading here is. **The census shadow is
reproduced exactly and labelled as what it is:** an external control of
the enumeration, at the counting measure that defined it, leg-*dependent*
where the law value is not. That the measurement reproducing it touches
no object of the constructed family is measured rather than asserted —
a token scan of the delivery's own source over the region between two
markers returns 0 occurrences of the constructed family, of either
quotient, or of the class indices.

This is the #82 lesson executed rather than restated. The predecessor
was asked to hit two leaf-count statistics and could not, because they
were never values of any law; the successor pre-registers the law's own
value and hits it at both legs.

## 6. Holonomy at the well-posed gate

The gate is REPRODUCED-AND-LOCATED, in four conjuncts, each measured and
each killable.

The deviation is derived, not observed: the horizon-normalized
connection differs from q by the exact factor
G(h e_A e_B, r−2)/G(h e_B e_A, r−2), and the identity
r_k = r_q · that factor holds at 1546 of 1546 closed squares with 0
violations, correction-factor spectrum {1: 1538, 64/65: 6, 65/64: 2}.
The 8 non-unit factors all sit at base depth 0.

**On the ruled carrier the deviation vanishes.** Of the 1362 squares
that close there, 0 carry a non-unit correction factor and r_k = r_q at
1362 of 1362. On the predecessor carrier 8 of the 1402 closing squares
carry one and the reading deviates at 8. So the adjudicated expectation
holds: descent forces r_k = r_q on every closing square, the enlargement
disappears, and the located deviation becomes a vanishing one.

The mechanism is exact and is worth stating, because it is the reason
the ruled carrier is the right one rather than merely a finer one: all
8 squares carrying a non-unit factor close in MENU-113 and in none of
CONG-185. The refinement does not repair those squares — it declines to
close them, and the 40 squares it declines to close include every one
that carried the enlargement and none of the 88 defective ones.

The negative control fires at both readings: on the record quotient the
obstruction is 0 and the non-unit self-loops are 0 at the q and the k
reading alike, over the 473 squares that close there.

A synthetic deviation planted on a square that closes in the ruled
carrier turns the head's own vanishing conjunct false, and the same
four-conjunct predicate evaluated at the contrast carrier turns false
there too. AGREES is a verdict that can fail.

## 7. The quantum character, carrier-stamped

The adjudication left this open as first class: the chain is exactly
lumpable at CONG-185 while the indivisibility signature lives at MENU —
is Γ's quantum character carrier-relative? It is, and the measurement
says why.

| claim | @MENU-113 | @CONG-185 |
|---|---|---|
| non-Markov triple census | 4 of 10 depth-cut triples fail, at 34, 112, 12 and 12 cells | 0 of 10 |
| Chapman–Kolmogorov | fails | holds |
| exact lumpability | no | yes |
| eq. 22, completions that speak | 2 of 4 | 0 of 4 |
| eq. 22, negative entries | 36, 104, 108, 164 | the algebraic reading is silent |

At MENU-113 the identity and cyclic completions leave the padded first
transfer invertible, so eq. 22's candidate is unique and computed
exactly; both return the *same* negative-entry census, with minima
−1/97, −5/97, −1/18 and −1/128 and column sums exactly 1. A unique
candidate that fails positivity refutes existence outright. The uniform
and marginal completions are exactly singular by a duplicate-column
certificate and say nothing.

At CONG-185 **all four completions are silent**, and the cause is
exhibited rather than guessed. The ruled carrier's classes are
depth-pure — 0 of 185 occur at more than one depth cut — so the labels
of two cuts are disjoint and the padded configuration space is a
disjoint union rather than an overlap: across the four triples the cuts
share 0, 0, 0 and 0 labels, where the predecessor carrier shares 13, 13,
45 and 45. The realised columns then lie in the span of the padding
block and the first transfer is singular under every completion. The
algebraic route is therefore not available at the ruled carrier, and the
existence question it was posed to answer is settled instead by the
direct construction: Chapman–Kolmogorov holds at all 10 triples, so an
interpolant exists and is the process's own conditional.

**The mechanism of the relativity is the multi-target edges.** MENU-113
carries 4 labelled edges whose target is not single-valued; CONG-185
carries 0. A quotient with a single-valued labelled target is a
probabilistic bisimulation and its class process is Markov by
construction; a quotient without one need not be, and is not. The 4 bad
edges sit on 4 distinct source classes, and those classes are among the
45 of 113 menu classes that recur across depth cuts — the same
recurrence that makes the eq.-22 padding speak at that carrier and be
silent at this one. One structural fact accounts for both halves of the
carrier-relativity.

**No quantum sentence in this unit is unstamped.** The four claims above
are each measured at both carriers and each carries the carrier it is
read at, in the paper, in the output and in the verdict string.

## 8. [B3], and the anchor question

### 8.1 The feasibility LP, convention-free

The register named the route: the exact rational feasibility LP, row
decomposable, at the first triple 45 independent 13-variable
non-negative feasibility problems plus one column-sum coupling. Both
halves are run here, in exact arithmetic, with **both** verdicts
certified — a feasible verdict returns a primal point verified against
the constraints, an infeasible verdict returns a Farkas vector verified
to satisfy y·A ≤ 0 and y·b > 0.

The support reduction the problems use is exact and not a relaxation: if
Γ(dd←d)[i][s] is 0 and Γ(md←d)[j][s] is positive then Ḡ[i][j] must be 0,
because every term of the sum is non-negative.

**The rows carry no obstruction.** Over the 772 row problems of the 8
(carrier, triple) cells, 0 are infeasible, at both carriers and at all
four triples with a non-degenerate first cut. Nor does the support
pattern carry one: 0 orphan columns and 0 empty rows anywhere.

**The coupling carries all of it, and it separates the two carriers.**

| carrier | coupled feasibility by triple | witness |
|---|---|---|
| CONG-185 | feasible at 4 of 4 | exhibited: the process's own two-cut conditional, non-negative, column-stochastic, reproducing the target exactly |
| MENU-113 | infeasible at 3 of 4, Farkas-certified; feasible at the fourth | none |

This is a correction to the predecessor's reading, and it is located.
Γ-main concluded that at every depth-cut triple with a non-degenerate
first cut no interpolant of eq. 22's form exists. Convention-free, that
holds at 3 of the 4 triples, not at 4: one triple admits a genuine
column-stochastic interpolant that the identity and cyclic paddings
declared impossible. The refutation survives, with its scope narrowed by
one cell, and what the padding was doing is now visible — it was
answering a question about an enlarged configuration space, not about
the family.

### 8.2 The atom, at (1,1)-block scope only, with the unreachability stamp

The coarsening lemma is quoted verbatim and applied where it bites: δ\*
is monotone under coarsening, CONG-185 refines MENU-113, and four of the
predecessor's six delivered atom rows therefore vanish at the ruled
carrier. The live content is the (1,1) block, which is exactly the
menu-exact renewal port, and it carries the unreachability stamp.

Re-measured in unit at this unit's own window: over the 30728
transitions out of every history of depth < 5, the number entering the
(1,1) block from outside it is **0**, while the other blocks are entered
at 1700, 4 and 4. The pinned wider measurement is 0 of 243768.
Recurrence-based readings of the atom are barred, and none is taken.

The predecessor left an open question — whether refinement rounds 2 … 5
split the block — and it is answered here. The depth-≤ 4 part of the
block is 341 points; they lie inside **one** MENU-113 class, which is
exactly the block and nothing else, and inside **five** CONG-185 classes
of sizes 256, 64, 16, 4 and 1 — one per depth stratum, every one of them
block-pure.

That answers the atom question too.

| row | @MENU-113 | @CONG-185 |
|---|---|---|
| δ\*((1,1) ∩ d ≤ 3, N = 1), matched horizon | 1 | 0 |
| δ\*((1,1) ∩ d ≤ 3, N = 1), H4 | 1373/1380 | 0 |
| δ\*((1,1) ∩ d ≤ 2, N = 2), matched horizon | 1 | 0 |
| δ\*((1,1) ∩ d ≤ 2, N = 2), H4 | 5629529/5674560 | 0 |

The last surviving atom dies at the ruled carrier. Meanwhile **every**
class of the ruled carrier is an exact atom — all 72 classes the cap can
test have δ\* = 1 at N = 1 — which is what a congruence makes trivially
true and is therefore no instrument at all. Each of the four depth
strata of the block has δ\* = 1 for the same trivial reason. The atom
language, at this carrier, is empty on the block and vacuous on the
classes.

### 8.3 The anchor: renewal root, or sedimentary?

The pin declared two honest paths and made the choice a measurement.

**Path (a), the renewal-root candidate, is measured and it fails at the
class grain.** The ruled carrier's classes are depth-pure: 0 of 185
occur at more than one depth cut, so the class chain is graded by depth
and no class is ever revisited. The count of histories whose class
equals the class of one of their own prefixes is 0 at CONG-185 and 1900
at MENU-113. The root's own class occurs at depth 0 alone at the ruled
carrier and at all of 0, 1, 2, 3, 4 at the predecessor carrier — so
recurrence of the renewal root is a property of the *coarser* carrier,
and exactly there the chain is not Markov. The one small set that
survives the coarsening is entered at 0 transitions and has δ\* = 0.
And the first-return law the pin offers as the candidate,
g(1) = g(2) = 0 and g(n) = C(n−1,2)(3/4)^(n−3)/256 for n ≥ 3, is stated
at **delivery-free** scope by its own source, which declares in terms
that transport scope changes the picture.

Projecting the holdings ladder out does not lift the obstruction,
because the carrier's own class label *determines* the depth: a second
monotone coordinate that the projection cannot remove.

**And the reason is scoped honestly.** The grading is cap-driven, and
this unit says so rather than promoting it to a substrate fact. The
terminal stratum has an empty successor signature, so it separates
first, and the separation propagates inward one depth per round: depth
purity is reached at refinement round 4 of the 5, the count of classes
still spanning more than one depth falling 17, 5, 1, 0, 0. A carrier
built at a different cap, or at a fixed point taken without one, need
not be graded — and this unit does not build one.

**Path (b) is therefore adopted, and stamped: THE SEDIMENTARY FRAME.**
The law's long-run structure on this carrier is argued from
accumulation, not from return. No recurrence is assumed anywhere in this
unit, and the outcome segment says which path the measurements support.

## 9. Supply

Five cross-unit rows are disposed of, each either re-derived here or
excluded with its reason printed.

| row | status |
|---|---|
| the d ≤ 5 arm: menu quotient 265, coarsest congruence 462, 6 refinement rounds | **pinned and re-derived** — reproduced from this unit's own family and its own refinement |
| the coarsening lemma, δ\* monotone under coarsening | pinned and applied, with its consequence measured on both carriers |
| the fifth holdings-profile block (3, 3), 424 points all at depth 6 | pinned citation, EXCLUDED-BY-CAP, and the exclusion machine-checked: 0 of its points lie inside this arena |
| Γ-prep's own d ≤ 6 arena | excluded — 243769 histories; every statement taken from it is a pinned receipt citation, stamped, never re-measured here |
| the weld-2 six-of-six re-derivation of the carrier | excluded — the bytes move (§3) |

The R-SIG census reproduces at the anchor scope: 5161 points, of which
1365 are menu-exact, in holdings-profile blocks (1, 1): 1365,
(2, 2): 3788, (2, 3): 4 and (3, 2): 4, and the (1, 1) block is exactly
the menu-exact port.

## 10. The verdict

Every segment is computed in gate. The complete emitted string is then
audited by a reconstruction that shares no code, no input and no typed
literal with the builder: it re-parses a serialised record, reads the
frozen pin itself for the outcome vocabulary and refuses any head not
found there, locates the head and the segments by search, *characterises*
the connective tissue instead of quoting it, requires the body to be
closed by a delimiter, proves the spans cover the emitted string
exactly, and checks every declared measured value against the segment
that carries it **by occurrence count**, so that retyping one of two
occurrences is caught. Six falsifiers attack it — appended text, a
swapped head, truncation, a dropped segment, a retyped value, and a
record desynchronised from the string — and each flips its predicate.

The complete emitted string, byte for byte:

```
GITER-LAW-CONFIRMED-<CARRIER=CONG-185-RE-DERIVED-IN-UNIT-185-CLASSES-AFTER-5-REFINEMENT-ROUNDS-AT-(A,B)-D<=4|DIMS=1x5x17x49x113|SIX-RULING-PROPERTIES=6-OF-6:DESCENT-AT-EVERY-HORIZON-0-MULTIVALUED-CLASSES-AT-r=0..4;MULTIVALUED-EDGES-0-WEIGHT-AND-0-TARGET-OF-572;44-CURVATURE-SQUARES-INTACT-SET-IDENTICAL-TO-MENU-113-SYMDIFF-0;Q-HOLONOMY-PRIMES-[2, 3]-RANK-2-OBSTRUCTION-44;K-HOLONOMY-PRIMES-[2, 3]-RANK-2-THE-ENLARGEMENT-DISAPPEARS;EXACTLY-LUMPABLE-CK-0-OF-10|CONTRAST-CARRIER-MENU-113-SCORES-2-OF-6 -- LAW=COLUMN-STOCHASTIC-EXACT-102-OF-102-COLUMNS-OVER-10-CUT-PAIRS-0-NEGATIVE-ENTRIES|FLOW-IDENTITY-w(h)k_{4-|h|}(e|h)=w(h+e)-3968-OF-3968-AND-352-OF-596-FAIL-AT-EVERY-OTHER-ADMISSIBLE-HORIZON|CUT-MASS-1-AT-ALL-5-CUTS -- TARGETS=HIT-AT-THE-LAW-VALUES-(15/38, 5/19, 13/38)-AT-BOTH-LEGS-LEG-INDEPENDENT-AND-LEFT-RIGHT-ASYMMETRIC|STEP-NORMALISER-RE-PROVED-ON-THIS-CARRIER-0-OF-30728-VIOLATIONS-k_2-FAILS-1340-OF-3968|RAW-PRODUCT-READOUT=(3/8, 1/4, 3/8)|CENSUS-SHADOW=(3/7, 1/7, 3/7)-AND-(4/9, 1/9, 4/9)-REPRODUCED-AT-THE-COUNTING-MEASURE-THAT-DEFINED-IT-DECLARED-EXTERNAL-CONTROL-NEVER-A-TARGET-TOKEN-SCAN-0-HITS -- HOLONOMY=AGREES-AT-REPRODUCED-AND-LOCATED:r_k=r_q-AT-1362-OF-1362-CLOSING-SQUARES-0-DEVIATIONS|DEVIATION-IDENTITY-1546-OF-1546-KILLABLE-MUST-PASS|THE-8-NON-UNIT-CORRECTION-FACTORS-CLOSE-AT-MENU-113-AND-AT-0-OF-CONG-185|REC-FLAT-OBSTRUCTION-0-AT-BOTH-READINGS -- QUANTUM=CARRIER-RELATIVE-CONFIRMED-BY-MEASUREMENT|@MENU-113:NON-MARKOV-AT-4-OF-10-DEPTH-TRIPLES;EQ22-NEGATIVES-36/104/108/164-AT-2-OF-4-COMPLETIONS-THAT-SPEAK;NOT-LUMPABLE;MULTI-TARGET-EDGES-4|@CONG-185:MARKOV-CK-0-OF-10;EXACTLY-LUMPABLE;EQ22-SILENT-AT-4-OF-4-COMPLETIONS;MULTI-TARGET-EDGES-0|MECHANISM=THE-SIGNATURE-IS-CARRIED-BY-THE-MULTI-TARGET-EDGES-AND-THE-45-OF-113-MENU-CLASSES-THAT-RECUR-ACROSS-CUTS -- B3=ROW-DECOMPOSED-FEASIBLE-0-INFEASIBLE-ROWS-OF-772-AT-4-OF-4-TRIPLES-ON-BOTH-CARRIERS-ALL-CERTIFIED|COUPLED=@CONG-185-FEASIBLE-4-OF-4-WITNESS-EXHIBITED;@MENU-113-INFEASIBLE-3-OF-4-FARKAS-CERTIFIED|THE-COLUMN-SUM-COUPLING-IS-THE-WHOLE-CONTENT-ORPHAN-COLUMNS-0|ATOM-AT-(1,1)-BLOCK-SCOPE-ONLY:delta*=0-AT-CONG-185-AGAINST-1-AT-MENU-113-THE-BLOCK-SPLITS-INTO-5-CLASSES-ONE-PER-DEPTH -- ANCHOR=SEDIMENTARY<CLASS-CHAIN-DEPTH-GRADED-0-OF-185-CLASSES-AT-MORE-THAN-ONE-DEPTH;PREFIX-CLASS-RETURNS-0-AT-CONG-185-AGAINST-1900-AT-MENU-113;(1,1)-BLOCK-ENTERED-AT-0-OF-30728-TRANSITIONS;RENEWAL-ROOT-LAW-IS-DELIVERY-FREE-SCOPED-BY-ITS-OWN-SOURCE;THE-GRADING-IS-CAP-DRIVEN-PURITY-AT-REFINEMENT-ROUND-4-OF-5>|LONG-RUN-STRUCTURE-FROM-ACCUMULATION-NOT-RETURN-NO-RECURRENCE-ASSUMED -- SCOPE=(A,B)-D<=4-CARRIER-AND-D<=5-ANCHOR|GRAIN=CONG-185-EVENTxWEIGHT-CONGRUENCE|HORIZON=H4-PRIMARY-MATCHED-NAMED-AT-USE|READOUT=STEP-NORMALISED-PRIMARY-RAW-PRODUCT-AND-COUNT-MEASURED|LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-3..10-OUTSIDE-THE-CARRIER-CAP|SUPPLY=5-CROSS-UNIT-ROWS-DISPOSED|SOURCES=13-SHA-PINNED-1-DECLARED-AND-NOT-READ|NO-CURVATURE=>QUANTUM-CLAIM|NO-INDIVISIBILITY-CLAIM-AT-RENEWAL-GRAIN|NO-CONTINUUM-OR-LIMIT-CLAIM|DEPTH-6-AND-THE-FIFTH-BLOCK-EXCLUDED-BY-CAP>
```

## 11. Controls and falsifiers

| control | direction | measured |
|---|---|---|
| the record quotient | negative | flat at both readings; obstruction 0, non-unit self-loops 0, 473 squares closing, exactly lumpable |
| the contrast carrier MENU-113 | discriminating | scores 2 of the 6 ruling properties; carries the deviation, the non-Markov signature and the eq.-22 refutation the ruled carrier does not |
| the size-matched scramble | negative | same class count and same class-size multiset, and it loses descent and single-valuedness at once |
| the off-by-one horizon | negative | breaks the flow identity, so the joint stops agreeing with the marginal and the columns stop summing to 1 |
| a synthetic deviation | negative | a non-unit factor planted on a carrier-closing square turns the holonomy head's vanishing conjunct false |
| the unpruned leg agreement | positive | the prune reproduces the unpruned leg set on 3 of the 256 bases, leg for leg and weight for weight, at both weights |
| a constructed infeasible system | negative | the LP solver returns infeasible with a verified Farkas certificate, so a solver that always answers feasible is caught |
| the re-priced law | forcing | re-pricing every priced event by an arbitrary exact rational leaves the properness identity at 0 violations; zeroing one price leaves non-positive kernel entries |
| the reversed traversal | determinism | the refinement's partition is invariant under reversing the traversal order, compared as a set of blocks; the class *indices* are not, which is why the delivered labelling is pinned to a sorted traversal rather than to a set's iteration order |

Coverage is measured by **reach**: a gate counts as covered only when a
declared falsifier turns that gate's own predicate from true to false,
and the reach is computed from the observed pair rather than asserted.
Every MUST gate carries at least one such falsifier. The only gates
without one are the two theorem-passes and the one disclosure, each of
which carries a waiver whose forcing is itself machine-checked.

## 12. Scope, and what this unit does not decide

- The arena is (A, B) at depth ≤ 4 for the carrier and depth ≤ 5 for the
  anchor scope. Depth 6 and the fifth holdings-profile block are
  EXCLUDED-BY-CAP, and the exclusion is machine-checked.
- **The depth-grading of the ruled carrier is cap-driven** and is
  stamped as such. Every consequence drawn from it — the eq.-22
  silence, the absence of class returns, the sedimentary frame — is a
  statement about this carrier at this cap, not about the transport
  process.
- The coupled [B3] verdict at MENU-113 is a statement about the four
  depth-cut triples with a non-degenerate first cut, at this carrier and
  this cap.
- **No curvature ⟹ quantum claim**, at any grain.
- **No indivisibility claim at renewal grain**, at any scope.
- No continuum, infinite-volume, asymptotic or limit claim.
- No CP-divisibility, Bell, locality or covariance statement.
- The three- and four-actor pools are not built here.
- The eq.-22 algebraic route at the ruled carrier is silent, not
  negative; nothing is concluded from its silence except that the
  question must be asked another way, and it is.

## 13. The receipt

`v14/code/giter_receipt.json`, written by the plain delivery run, then
re-read from disk and verified against the gated object before the
process exits; the output file is compared against a digest accumulated
inside the emitter at emission time, which a later mutation of the line
buffer cannot reach. Plain runs produce byte-identical artifacts — in
the repository, outside it, with git absent, and under three different
interpreter hash seeds — and every wall-clock number goes to stderr and
reaches neither file. The hash-seed leg is not decoration: it is what
catches an index handed out by iterating a set, and one such index was
found and pinned to a sorted traversal.

| | |
|---|---|
| carrier histories | 3969 |
| CONG-185 classes / refinement rounds | 185 / 5 |
| MENU-113 classes, record classes | 113, 2477 |
| dimensions per cut | [1, 5, 17, 49, 113] |
| columns, ruled carrier | 102 |
| flow-identity transitions | 3968 |
| off-horizon failures | 352 of 596 |
| closed squares / defective | 1546 / 88 |
| squares closing at the carrier | 1362 |
| deviation identity | 1546 of 1546 |
| non-unit correction factors | 8 |
| leg 1, leg 2 | 3584, 73728 |
| law value, both legs | 15/38, 5/19, 13/38 |
| census shadow | 3/7, 1/7, 3/7 and 4/9, 1/9, 4/9 |
| Chapman–Kolmogorov failures | 0 at CONG-185, 4 at MENU-113 |
| eq. 22 negatives @MENU-113 | 36, 104, 108, 164 |
| [B3] row problems / infeasible | 772 / 0 |
| [B3] coupled infeasible @MENU-113 | 3 of 4 |
| δ\* of the (1,1) block, matched | 0 at CONG-185, 1 at MENU-113 |
| block entries from outside | 0 of 30728 |
| prefix-class returns | 0 at CONG-185, 1900 at MENU-113 |
| d ≤ 5 supply row | 265 menu, 462 congruence, 6 rounds |
| sources by pinned sha / declared and not read | 13 / 1 |
| verbatim windows, each with a drift falsifier | 19 |
| path-value probes | 11 |
| arithmetic | exact `int` and `fractions.Fraction`; the file's own syntax tree carries 0 float literals |

## 14. The next-iteration register

**The cap is now the object.** Every negative result in §8.3 rests on
the depth-grading of the ruled carrier, and the grading is measured to
be cap-driven. The successor's first question is what the coarsest
weighted congruence looks like when the terminal stratum is not a
terminal stratum — at d ≤ 5, where this unit has already re-derived the
265 / 462 row, or at a fixed point taken with a boundary convention that
does not separate the last depth. Only there can the renewal-root
candidate be posed as a question about the process rather than about the
window.

**The [B3] cell that speaks.** One of the four triples at MENU-113
admits a column-stochastic interpolant while three do not. What
distinguishes it is not measured here and should be: the predecessor's
padding-based reading could not see the distinction at all.

**The eq.-22 question at a carrier with a shared configuration space.**
The algebraic route is silent at CONG-185 because the cuts share no
labels. A carrier whose classes are *not* depth-pure but which is still
a congruence would let both routes speak at once, and would separate
"the padding was doing the work" from "the carrier was".

**The atom language is spent at this carrier** — empty on the block,
vacuous on the classes — and the successor should stop carrying it.
What replaces it, if anything, is the accumulation reading the anchor
segment now stamps, and that reading has no instrument yet.

**Two rows to pin.** The d ≤ 6 arena, which this unit excluded by cost
and which every full-family statement still leans on; and the weld-2
re-derivation of this carrier, once its bytes stop moving.
