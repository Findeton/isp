# The renewal-grain transport

**v14 R6b′ — paper-09.**  Does a motivated identification carry the
deep corpus's renewal-grain positional structure to the spatial
record-interval arena, and does the derived kernel collapse the R6a
split fiber?

**Status:** `TERMINAL` — panel #59/#60/#62 (3× ACCEPT-WITH-FIXES),
adjudicated #62; repair R-R6BP-1…R-R6BP-9 delivered #68 and
adjudicator-verified (plain-run byte-identical; selftest 76/76 mutants
dead by named gates); v14 ledger #70, 2026-08-09.  Pin:
`v14/note-r6bprime-transport-pin.md`, sha256-12 `17111fd19022`.**Pin:** `v14/note-r6bprime-transport-pin.md` (frozen, v14 ledger #43).
**Instrument:** `v14/code/r6bp_transport_exact.py` with
`_output.txt` and `_receipt.json`; exact `int`/`Fraction` arithmetic
under an AST float guard; two plain runs byte-identical.
**Provenance:** every source is read at a commit sha declared in the
instrument's own frozen text — the corpus at `d042ef1ae74e`, R6a's
TERMINAL receipt at `d5fb2a5956f7`, R6a's delivered receipt at
`b0087a9d262b` for the stability comparison alone.  No mutable
repository state is read.
**Discipline:** RUNBOOK §13/§14/§15 with every addendum, all ten
2026-08-09 v14 engravings gated at birth, each compliance claim
verified against the measured mutant death table.

---

## 1. The question, and why it is a transport question

R6a proved that the pinned record grammar admits no motivated
interval-subdivision move, and located the mechanism: the datum a
split needs — where inside an interval the division events sit — is
exactly the datum the record does not carry.  CR-B then asked whether
a motivated split *distribution* exists and returned
`CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW`, naming the missing object
in its own receipt: the interval positional law, the transition
kernel between an interval's endpoints whose renewal count is n, and
observing that R0 carries the record layer and no transition layer.

The deep corpus does carry a transition layer, at renewal grain.  So
the question is not whether the stratum exists.  It is whether the
stratum **transports**: whether a motivated identification carries
the renewal-grain positional structure of v10/v11 to I7's spatial
interval arena, and if so whether the induced law collapses R6a's
split fiber to a forced value or a forced distribution.

The answer is composite, and every part of it is first-class.

---

## 2. What is assumed

Six deep rows plus one added by adjudication, all hash-pinned at a
declared commit sha and each carried with its pedigree; plus I7, the
baseline arena row of the founding pin.

| row | supplies | pedigree carried |
|---|---|---|
| S1 the transition matrix | the exact 6×6 transfer, λ = 2, the completed chain q′, the named renewal state, root = renewal | TERMINAL (v10 #349) |
| S2 the positional census | the exhaustive intervening-pattern census inside inter-renewal intervals at lengths 3 and 4, with exact leaf counts | TERMINAL (v11 #20–#21); interval lengths are ENSEMBLE DATA; the two length-4 cells are E2's leg 1 and E3's leg 2 |
| S3 the type declaration | division event ≡ renewal; the bridges = the interval; Γ(cut′←cut) declared to be constructed | founding paper; v11 frozen |
| S4 the renewal theorem | every pair arbitration is a renewal to the root; the elementary-click refinement | TERMINAL (v10 #326, ten hostile rounds; its header's paper-level-review-open note carried) |
| S5 the declared positional law | the continuous positional layer, with its own verbatim disclaimer that the waiting law and rates are chosen, not derived | D34b TERMINAL delta |
| S6 the extremal standard | the frozen bar any extremal selector must clear | audit (completed pre-hostile-review — carried) + finite nonselection theorem |
| S7 the escape | the measured cause of the transport-scope seam, and nothing else | TERMINAL (v10 #392); consumed for one statement only |
| I7 | the record layer: sites, links, and n_ℓ(x) — the number of division events in the record interval between x and x+ℓ | v14 R0 founding pin |

R6a's split-fiber values and CR-B's simplex dimensions are anchored as
(path, value) pairs at their receipts.  R6a is TERMINAL, and this unit
consumes its TERMINAL receipt at the declared sha; the same path-values
are read at R6a's earlier delivered receipt and compared, and none has
moved.  Three of the values this unit consumes exist only in the
terminal receipt.

**Named exclusions, binding and honoured.**  `u1c` is NOT CITABLE and
appears only as a registered lead with its status printed;
THE-THEORY-SO-FAR is index-only; v12's Γ objects are arena-free and
are not a source; `d70` is excluded — and the exclusion's stated
reason is corrected here, since its round-1-repaired header was stale
and `d70` is terminal at one hostile round.  It is excluded because it
supplies horizon kernels rather than an interval-positional law.  The
instrument gates that no named-excluded artifact is cited.

---

## 3. What a renewal is

The convention is not this unit's to choose.  Three pinned rows fix
it, and they agree.

S1's own code defines the renewal set as

> *"REN = [h for h in FAM if len(h) <= 4 and CLS[tuple(h)] == 0 and any(e[0] == 'r' for e in h)]"*

and its gate reads

> *"ALL clean-slate renewal points at len <= 4 (class 0 carrying an arb; each with a UNIQUE shared non-superseded base) have root-identical one-step menus under their own base substitution -- the 144-point census."*

Class 0 is necessary and not sufficient: an arbitration is required.
S4 names the same event rather than the state —

> *"every pair arbitration is a renewal to the root state [THEOREM at two-actor delivery-free scope]"*

— and every leg S2 censuses terminates in the same `r` tag that S1's
code tests for.

Measured on the completed chain, the arbitration edge set is the
single transition 3 → 0.  The root's self-loop q′(0→0) = `3/4` is an
*idle at the root*: it lands in class 0 and carries no arbitration, so
it is not a renewal.  The alternative reading — renewal = any visit to
state 0 — is measured below and printed as a disclosure, never adopted.

The chain itself is read from two distinct pinned artifacts in two
formats: paper 31's fenced prose block and `d43b`'s `T_REF`/`f` source
objects.  They agree entry by entry.  Both are authored literals, so
what this establishes is transcription fidelity across two artifacts,
not two derivations; the genuine second derivation exists and this
unit does not run it — `d43b`'s own `rows` object, built by the
bisimulation and gated against `T_REF` over the `215` length-≤3
histories in `d43b`'s own terminal run.  The completed transfer
q′(i→j) = T_ij f_j / (2 f_i) normalises exactly on all six rows and
reproduces S1's own printed conflict row.

---

## 4. The derived kernel

The completed chain has exactly one closed communicating class,
`{2, 4, 5}`; S1 states it —

> *"The dominant class {2, 4, 5} (Tarjan decomposition; {0, 1, 3} is transient and carries the renewal loop 3 -> 0)"*

and

> *"the conflict row is {0: 1/7, 3: 3/4, 5: 3/28}.  This is the root-free completion, exhibited on the intrinsic chain."*

— and this unit rebuilds it by a Tarjan decomposition of its own.

An inter-renewal leg runs from one arbitration to the next.  Because
the only route back to the root is 0 → 1 → 3 → 0, a leg of length n
carries exactly two advancing steps among its n−1 interior steps and
therefore exactly n−3 self-loop fillers, distributed over the three
states in C(n−1,2) equiprobable ways.  Hence

> **g(1) = g(2) = 0;  g(n) = C(n−1,2)(3/4)^(n−3)/256 for n ≥ 3.**

So g(3) = `1/256`, g(4) = `9/1024` and g(5) = `27/2048`.  The law is
computed three ways that agree: the closed form; an exact integer
taboo iteration of q′ over the common denominator `448` to `400`
terms, with the residual mass beyond the cap bounded below 1e-40; and
exhaustive path enumeration at n = 3 … 12.

Summing it, the return probability is `1/4` and the defect `3/4` — the
mass absorbed into the closed class.  The number of renewals after any
renewal is therefore geometric and almost surely finite: **the
delivery-free renewal process terminates almost surely.**  The
expected total number of renewals after any renewal is `4/3`, and the
mean inter-renewal length conditional on a further renewal is `12`.

**The support holes.**  There is no inter-renewal leg of length one or
two, exactly.  Pushed onto the arena, that means the derived
kernel assigns probability zero to `79` censused intervals — the
count-1 and count-2 ones — a refutation of the count-matching
identification on better than a third of the arena, and a stronger
statement than any count of free items.

**The disclosed alternative.**  Read "renewal" as any visit to state 0
and the idle self-loop becomes a completed leg of length one.  Then
f(1) = 3/4, f(2) = 0 and f(n) = (n−2)(3/4)^(n−3)/256, with
a return probability of `13/16`, defect 3/16, expected visits 16/3 and
a single support hole at 2.  That reading has two length-4 legs rather
than three, and its induced positional law is (0, 1/2, 1/2) — not
uniform, and it reproduces nothing.  It is recorded because the choice
is real and must be visible; it is not this unit's law, because the
source settles it.

Every statement in this section carries S1's and S4's own
delivery-free scope tag.  S1 declares what changes at transport scope:

> *"At transport scope the picture will change and is declared: deliveries reopen the absorbing sector (diverged holdings can reconverge), the class structure of §3.2 is not stable under the transport grammar, and the Martin-boundary machinery that this section did not need is expected to become load-bearing exactly there (§7, successor 2)."*

---

## 5. The positional law, at every count, from S1 alone

The configuration census above is a positional statement, not only a
length statement.  A leg of length n has n−3 fillers among n−1
interior slots, uniformly placed, so the position marginal is
**exactly uniform on the n−1 positions at every n ≥ 4** — verified
exactly at n = 4 … 12.  At n = 4 it is (1/3, 1/3, 1/3).

At n = 3 there is exactly one configuration and it carries no filler,
so the pattern class distinguishes no interior position at all.  That
is a law of the pinned chain, not a census cap, and S2 measured the
same fact independently by an unpruned scan: `256` leaves, one pattern,
with (p,p,r) forced.

> *"A renewal three events after a renewal forces (p,p,r) and nothing else.  A renewal four events after a renewal admits exactly five intervening patterns -- (d,p,p,r), (n,p,p,r), (p,n,p,r), (p,p,d,r), (p,p,n,r) -- each with exactly two proposals plus one delivery or one idle."*

**The one residual freedom, measured.**  At n ≥ 5 a leg carries two or
more fillers, so reducing a filler *set* to a *position* is a choice,
and the choices differ: at n = 5 the marginal gives
(1/4, 1/4, 1/4, 1/4) while a first-filler reading gives
(1/2, 1/3, 1/6, 0).  At n = 4 the two coincide, which is precisely why
a count-4-only result looks convention-free and is not.  The freedom
is registered in the inventory as `I-FILLER-REDUCTION`.

**The weld.**  Deleting the delivery-bearing patterns from S2's
length-4 census and renormalising gives (1/3, 1/3, 1/3) at both
censused cells — the same law the chain derives from S1 alone — and
the three chain configurations biject with the three retained S2
patterns slot for slot: the chain's self-loop filler *is* S2's idle.
The corrected convention is what makes this true.  The bare-state-0
reading gives (0, 1/2, 1/2) and reproduces nothing.

---

## 6. The transport census, and the mechanism

S2's two length-4 profiles carry the leaf counts
`1024`/`512`/`512`/`1024`/`512` at leg one (total `3584`) and
`24576`/`8192`/`8192`/`24576`/`8192` at leg two (total `73728`).  Read
as a law on the interior slot:

| scope | leg one | leg two |
|---|---|---|
| transport | (3/7, 1/7, 3/7) | (4/9, 1/9, 4/9) |
| no-delivery conditional | (1/3, 1/3, 1/3) | (1/3, 1/3, 1/3) |

with total variation `2/63` between the two cells at transport scope,
while for the conditional the total variation between the cells is `0`.

**The mechanism is exact and it is one exclusion.**  Of the six
combinatorial possibilities — three interior slots by
{delivery, idle} — S2 realises five.  The missing one is (p,d,p,r):
**a delivery cannot occupy the middle interior slot.**  Slots one and
three admit a delivery or an idle; slot two admits only an idle.  That
single asymmetry is the whole of the transport-scope positional
structure, and deleting the delivery-bearing patterns restores exactly
one pattern per slot.

**And its parameter.**  The delivery multiplicity per slot is `2` at
leg one and `3` at leg two — one more deliverable message in flight.
With the middle slot excluded the law is forced to
((1+m), 1, (1+m))/(2m+3), which reproduces both measured cells exactly
and runs toward (1/2, 0, 1/2) as m grows.  The other side of the same
Boolean partition — retain the deliveries, delete the idles — is
already at that limit, (1/2, 0, 1/2), at measured distance 1/3 from
the conditional.  So the delivery multiplicity per interior slot is a
concrete candidate for the first coordinate of a frozen-stage validity
domain, measured here at two values.

**Two disclosures the numbers require.**  First, the conditional is
what its name says: the transport census conditioned on no delivery,
carrying transport branching weights.  The conditioning is not
innocuous — it retains `3/7` of the leg-one mass and `1/3` of the
leg-two mass, so the two conditional laws coincide as laws conditioned
on *different* events.  What carries the uniformity is that the three
retained patterns have equal weight within each cell.  Second, the two
cells are not two chain positions of one ensemble: leg one is E2's
first leg (renewals at 3, 7, 10; depths 3→7) and leg two is E3's
second (renewals at 3, 6, 10; depths 6→10).  Ordinal position,
absolute depth and ensemble identity move together across the only two
data points, so "chain-position dependent" is one of three readings the
data cannot separate.  Every segment carrying these cells is stamped
with that restriction.

S2's leg lengths are ensemble data — renewal positions declared by the
ensembles, not sampled from any kernel — and its scope is its own:

> *"Transport scope (d42b1) only; the two-actor pool only"*

---

## 7. The seam, at both of its referents

As an obstruction to *this unit's* question the scope seam is
**avoidable**.  A single-scope delivery-free row set already exists
inside the pin — S1 + S4 + I7 — and supplies both layers, the
leg-length law and the positional law.  S2 is a declared cross-check
that agrees exactly at count four, not the only source of the
positional layer.

As a *measurement* the seam is real, and its cause is not row
provenance.  There is no transport-scope analogue of S1's 6×6 chain to
pin, because the transport-scope window chain escapes:

> *"the window chain ESCAPES: 68 transitions from shallow parents land in 5 classes first realized at length 3.  Escape is not non-stabilization: the partition behaves; the state space outruns every window."*

> *"menu-shape factorization fails at transport scope (gated exhibit), so the delivery-free machinery cannot be silently reused (a gated negative control: zero of the 3,969 transport menus match any delivery-free menu shape)."*

That is the whole of what S7 is consumed for.  Its 36-state quotient
claim is not pinned and is not read.

So the seam blocks a transport-scope *chain*, permanently and for a
measured reason; it never blocked the delivery-free positional
construction this unit performs.  The 2/63 measurement is a
transport-scope finding to be carried, not a blocker.

---

## 8. The fiber collapse

The arena carries `201` censused record intervals over nine admissible
records — seven homogeneous at all nine sites, two inhomogeneous at
the two sites the R6a receipt prints, a declared cap.  Classify each
interval by what the derived kernel can say about it.

| class | intervals |
|---|---|
| kernel hole (counts 1 and 2) | 79 |
| stratum empty by law (count 3) | 20 |
| **collapsed in distribution (count ≥ 4)** | **102** |

> **The derived kernel collapses the R6a split fiber on every interval
> of count four or more, and the collapse is IN DISTRIBUTION, never to
> a value.**

Of the 201 censused intervals 122 carry a non-trivial fiber, and the
derived kernel speaks on `102` of them.

**And on the honest denominator.**  Three admissible records —
G-ANISO, G-CURVED, G-FLAT — have R6a split fiber zero: they admit no
subdivision at all, in CR-B's own words.  They carry `60` of the
censused intervals, ten of them at count four.  On those there is no
R6a split fiber to collapse.  Restricting to the six records that
admit the move leaves `141` censused intervals, of which `103` carry a
non-trivial fiber; the kernel speaks on `83` of those.  For the
narrower count-four-only reading the same two denominators give:
count four alone gives `37`, and `27` on the honest denominator.

At delivery-free scope the induced split law is uniform, with three
maximisers, so no functional of it names a split.  At transport scope
it is (3/7, 1/7, 3/7): the maximum ties on the two ends, but the
*minimum* names the middle slot uniquely — the claim that no
functional names a split is a claim about maximising functionals, and
at transport scope the minimum-probability split is named.

Stated in CR-B's own coordinates, at one interval: at count four CR-B
measured a fiber of 3 and an invariant-measure simplex of dimension
`2` under the pinned symmetry.  The derived kernel selects one point
of it, so the dimension goes 2 → 0.  That is a statement about a
per-interval simplex, not about a record's fiber.

**One record is completely covered — and the caveat is measured.**
Exactly one record, G-DIAG2, has every splittable interval at count
four and every other at fiber one, so on it the derived kernel
supplies a complete law on R6a's entire split fiber: the uniform law
on 19683 elements.  That is the law CR-B classed REFUTED-AS-FORCING
for want of a declared support.  But G-DIAG2 is also the only
splittable record where the raw and admissible-at-images fibers
coincide — exactly the record where CR-B's support-dependence
objection was already vacuous.  And the derived kernel is
per-interval and factorises while admissibility couples the three
links at a site: rebuilding the admissible fiber independently
reproduces R6a's per-site counts (221 at G-ANISO2, 23 at G-OFFNEG) and
the derived marginal equals the admissible-uniform marginal at G-DIAG2
only — G-ANISO2 gives (59/221, 76/221, 86/221) and G-OFFNEG
(7/23, 8/23, 8/23).  CR-B's non-factorisation recurs one level down.
That is not a defect of the measurement; it is the scope of it.

**The two positional layers disagree.**  S5's continuous layer places
interior positions as uniform order statistics, giving the binomial
split law (2/7, 3/7, 2/7) at count four, separated from the derived
law by total variation `2/21` — a number that reproduces CR-B's own
anchored uniform-versus-binomial total variation at count four,
computed by a different unit on a different route.  One layer is
derived and one is chosen, and S5's disclaimer is carried wherever the
continuous layer is touched:

> *"the coefficients 1/4 are chosen, not derived"*

> *"For the chosen static-adjacency D34b birth/idle/interaction exemplar"*

---

## 9. The identification census

`5` identification candidates are expressible from the pinned rows.
Each carries a choice inventory whose items are classed forced /
stabilizer-fixed / genuinely free with exact fibers, and every item's
class is re-derived from its own recorded evidence and gated against
the declared one.  The motivation qualifier is computed: motivated iff
zero free items.

| candidate | forced | stabilizer | free | qualifier |
|---|---|---|---|---|
| C1 count-match-length (the pin's literal reading) | 4 | 1 | 6 | UNMOTIVATED |
| C2 count-match-legs (the type-honest reading) | 2 | 0 | 5 | UNMOTIVATED |
| C3 the bridges reading (S3's verbatim declaration) | 2 | 0 | 1 | UNMOTIVATED |
| C4 the elementary-click refinement | 1 | 0 | 4 | UNMOTIVATED |
| C5 the continuous comparator (S5, labelled) | 0 | 1 | 1 | UNMOTIVATED |

**Motivated identifications: `0`** of the five.  The most-shared free
items are `I-BASIS` and `I-SCOPE`, each free in three of the five.

Four findings inside the inventory are worth naming.

**The type census.**  S3 posits

> *"[POSIT] v11's division events are the renewal events."*

n_ℓ counts division events; every censused leg carries exactly one
arbitration tag.  C1 — the pin's literal "n_ℓ events ↔ a length-n_ℓ
leg" — therefore equates a division-event count with a grammar-event
count.  C2 is the type-honest repair, and it pays for the repair with
extra free items, because the record fixes only the number of legs and
neither their lengths nor the halving rule.

**The bridges reading lands where there is nothing to split.**  S3
declares

> *"The bridges are the conflict windows between renewals."*

A bridge's interior carries no division event, so the reading is
admissible exactly at count one — and 29 of the 201 censused intervals
carry count one, every one inside a record whose split fiber is zero.

**The observable is a choice, and it is registered.**  The map from a
pattern class to an interior position is this unit's construction; it
is in no pinned row, and the type census proves a leg has no interior
division event for a split to sit at.  It enters C1 and C4 as
`I-READOUT`, classed free.

**Orientation splits per observable.**  The induced *position law* is
reversal-invariant at both scopes and both censused cells, so
orientation is fixed by a stabilizer of that observable.  It is not
fixed for the *front rule*, which §10 measures to be
orientation-dependent everywhere.  One item cannot be stabilizer-fixed
and consequential at once, so it is split: `I-ORIENT-POSITION-LAW`
stabilizer-fixed, `I-ORIENT-FRONT-RULE` free.  S4's own click
refinement and its declared open question enter C4 the same way:

> *"K1 refines into a chain of selection clicks"*

> *"Which basis nature seals — the fine order-sealed record or the coarse winner-sealed record — is an empirical question."*

---

## 10. The R6a audit, re-run at the enriched type

| freedom | R6a | at the enriched type |
|---|---|---|
| THE-SPLIT | class (iii), fiber 19683 … 1257565061957837936381 | class (ii) **in distribution**, at every count ≥ 4, at delivery-free scope |
| FREE-TRANSVERSE-LINKS | class (iii), fiber infinite, 54 of 108 | **unchanged**: the kernel is count-indexed and these links carry no count |
| NEW-FRONT-VALUES | class (iii), fiber infinite | **forced relative to the split *and an orientation*, fiber 2**, the two members separated on every cycle |
| THE-LIFT-PAIR | class (iii), fiber 2 | **unchanged, and the freedom grows**: a third admissible rule |

The forced part is re-verified unchanged, and against an independent
comparator: count additivity holds on 647 split constraints of this
unit's own enumeration with zero violations, and the readout rebuilt
from (q₁₁, q₂₂, q₁₂) recovers the *anchored* record-family counts at
67 of 67 (record, site) cells.  Feeding that rebuild garbage counts
fails the gate, which is what a re-verification has to be able to do.
R6a's own figures (972 additivity checks with zero violations; 324 of
324 restriction checks) are anchored separately as path-values; the
two enumerations are different objects and no ratio is formed.

**The front values are the interesting entry, and they are not forced
to a value.**  The enriched type does supply a front rule at a new
site: front(new) = front(x) + n₁, the count of division events on the
left half.  But the right-anchored rule front(new) = front(x+ℓ) − n₂
is expressible from exactly the same objects — the interval's other
endpoint is a coarse site with a declared front, and n₂ is the same
split datum — and the two agree at a new site if and only if
front(x+ℓ) − front(x) = n_ℓ(x), the coboundary condition R6a's own
gated theorem says no record's counts satisfy.  Measured on (ℤ₃)²:
over the `63` cycles — seven homogeneous admissible records by three
link directions by three cycles — the front telescopes to zero around
any 3-cycle while the count sum is a sum of three strictly positive
integers, and the count sum is nonzero at `63` of them, minimum 3,
nine distinct values.  So on every cycle of every record at least one
new site carries a left/right disagreement.  The fiber is 2 and its
two members are provably separated.

R6a's dynamics-forced count-weighted lift is non-integral at 30 of its
81 cells, but that grid is a (front, site, link) grid at one record
and one split rule — a different object, and no ratio is formed
against this unit's.

**The lift pair grows.**  Reading R6a's anchored fiber of 2: the
transported front rules are neither of R6a's two declared lifts, which
interpolate between the endpoint front values; they coincide with them
only under the coboundary condition that fails.  So the enriched type
adds a third admissible rule rather than selecting inside a pair.

**The transverse links** are untouched for a structural reason: an
enrichment indexed by interval counts has no index at all for a link
that lies on no interval.

**The tally, which is the honest headline.**  Of R6a's four
genuinely-free entries the enrichment forces a unique value at zero,
and supplies more than one admissible rule at two.  Importing a deeper
layer added freedom where it was expected to shrink it.

Also independently rebuilt here from the count data alone, not routed
through R6a's own fiber code: R6a's raw split fibers on the eight
records the printed-site data determines, and its equivariant fibers
on the five homogeneous splittable records.  All agree.  One
inhomogeneous record's fiber is not determined by the printed-site
data and is declared unrebuilt.

---

## 11. The extremal lead against the S6 bar

R6a's reopening lead (ii) pre-registered the criterion: max-det is
motivated iff a deeper row declares a variational principle.  That
condition is measured here rather than typed.  Every pinned row's
committed bytes are scanned paragraph by paragraph for declared
variational markers and, where one is found, for declared refutation
markers in the same paragraph.  Exactly one row carries any marker —
S6, the row that refutes the class — and the number of paragraphs
asserting a variational principle unrefuted is zero.  **The lead is
discharged by its own pre-registered condition.**

The constructive corollary is a countermodel.  S6's bar reads

> *"A proposed selector Q derives a unique law only if the frozen SHARD premises plus Q have exactly one physical equivalence class of models."*

and it is not enough that Q be a

> *"least-committal law relative to a supplied base measure and supplied constraints"*

Max-det does select uniquely — at 54 of 54 sites by R6a's own terminal
receipt, and uniquely on this arena's count-four fixture.  So do three
other record-intrinsic functionals, and they do not agree: max-det and
max-balance pick the middle split, max-left-count picks the last, and
max-|q₁₂| ties on the two ends.  Four functionals, three distinct
selections — twins the selector cannot separate, separated instead by
the choice of selector.  This is D12's second clause, generalised from
families of models to families of selectors, and the generalisation is
this unit's rather than D12's.

The determinant leg is narrower than it looks and is stated narrowly.
det q *is* computed from the record alone — q₁₁ = n₁, q₂₂ = n₂,
q₁₂ = (n₃−n₁−n₂)/2 — and the arena's admissibility predicate is
q₁₁ > 0 and det q > 0, so the record reads sign(det q) at every site.
At the declared density weight w = 0 the readout I = q⁻¹ is inversely
det-weighted, not det-blind.  What is true: det enters the declared
readout only through the admissibility predicate's sign, never through
the density weight, and a functional the arena reads only by sign is
not thereby a selector of magnitude.  S6's companion prohibitions
stand beside it:

> *"the corpus has no record-intrinsic, field-redefinition-invariant complexity measure that selects one generator."*

> *"a fixed causal action does not select the boundary state, orbit measure, extension kernel or complete next-record law."*

And the derived law does not rescue the selector: it assigns max-det's
selection probability 1/3, not 1.

**Outcome: DIES-AT-THE-BAR.**

---

## 12. The cover lead, dissolved

R6a's universal-cover route is motivated iff a deeper row de-periodizes
the declared arena or pins cover objects.  Measured, not typed: every
pinned row's committed bytes are scanned for declared cover markers and
zero of six rows carry any.  The deep arenas are rooted generated
objects, not periodic lattices —

> *"Truncated completions are therefore depth-non-stationary: rooted"*

> *"its state count grows with depth (17, 23, 29 at depths 4, 5, 6) while representing no new structure"*

— and a rooted, depth-non-stationary arena carries no deck group, so it
supplies no cover object for a torus it never mentions.  Recorded
DISSOLVED; no hunt is run.

---

## 13. Controls

Three negative controls, all failing the audit by distinct measured
modes.  The R1 copying move re-posed as an identification forces no
constraint and leaves six intervals unrepresented.  An identification
reaching a named-excluded artifact is refused at source, and the
anchor set is scanned to confirm that no excluded artifact appears in
it.  And the census's own control — identify an interval of count n
with a leg of length n+1 — fails on a cardinality mismatch measured at
every one of the 201 censused intervals: the leg offers n interior
positions against n−1 admissible splits.

An audit that could not fail a move would not be an instrument.

---

## 14. What Γ-main inherits

This unit does not construct Γ(cut′←cut).  S3 declares it

> *"the sparse indivisible family Γ(cut′ ← cut), conditioned only at division events | to be constructed"*

and building it is a future unit.  What this one hands over is
registered here as data rather than narrated.

**The head structure.**  Four heads, each answering about one object
with its referent named in the head: the construction (first-class
both ways); the requirements, computed against pre-registered lists,
each status computed in-gate; the motivation inventory applied to Γ's
own construction, carrying an `I-READOUT`-class item; and the scope —
grain, cap, completion, and the escape's status.

**The kernel is Γ's delivery-free shadow, not a first approximation
to it.**  Γ does not extend this kernel: it replaces one half and
inherits the other whole.  The S1 half — the leg-length law, the
closed class, the defect — is delivery-free, and the pinned corpus
declares and measures that transport *removes* its central feature by
reopening the absorbing sector.  So the corrected return probability
is a **control to contrast against, never a target**; recovering it
would be evidence the construction had lost the deliveries.  The S2
half is already at transport scope, which is Γ-main's own scope, and
it transfers whole.

**The pre-registered agreement test.**  A correct Γ must reproduce
(3/7, 1/7, 3/7) at leg one and (4/9, 1/9, 4/9) at leg two, together
with the mechanism that produces them: no delivery in the middle
interior slot, multiplicity two then three.

**The holonomy requirement.**  If Γ is constructed on D74's committed
quotient, its holonomy must be measured and compared to T5's curvature
group ⟨2,3⟩ as a pre-registered gate.  Agreement is the claim that the
geometry-update slot's measured occupant and the constructed law are
the same object; disagreement is a first-class negative and must be
statable before the construction runs.

**Two structural lessons, as pin text rather than habit.**  Do not
weld an identification-free result to an identification-relative one
under one head.  And a verdict segment must carry the restriction that
makes it true.

**The don't-inherit list.**  The count-four-only coverage figure as a
coverage claim; a delivery-free stamp on the S2 conditional; the
det-blindness argument; a fiber-1 front forcing; and the bare-state-0
kernel numbers.

---

## 15. The verdict

```
R6BP-KERNEL-DERIVED<IDENT=C1-COUNT-MATCH-LENGTH-UNMOTIVATED|CONVENTION=RENEWAL-IS-CLASS-0-CARRYING-AN-ARB-SOURCE-FORCED|LAW=FIRST-RETURN-g1-0-g2-0-gn-C(n-1,2)(3/4)^(n-3)/256|POSITION-LAW=UNIFORM-ON-n-1-AT-EVERY-n>=4-FROM-S1-ALONE|COLLAPSE=DISTRIBUTION-NEVER-VALUE|COVERAGE=102-OF-201-ALL-INTERVALS|COVERAGE-HONEST=83-OF-141-CENSUSED-83-OF-103-WITH-A-NON-TRIVIAL-FIBER|UNREFINABLE-RECORDS=G-ANISO+G-CURVED+G-FLAT-60-INTERVALS-EXCLUDED|CRB-SIMPLEX-DIM-2-TO-0-AT-ONE-COUNT-4-INTERVAL|S2-INTERVAL-LENGTHS-ARE-ENSEMBLE-DATA|INHOMOGENEOUS-RECORDS-AT-2-OF-9-SITES|SCOPE=DELIVERY-FREE>
R6BP-TRANSPORT-UNMOTIVATED<CANDIDATES=5|MOTIVATED=0|FREE-ITEMS=C1-COUNT-MATCH-LENGTH:6+C2-COUNT-MATCH-LEGS:5+C3-THE-BRIDGES-READING:1+C4-ELEMENTARY-CLICK-REFINEMENT:4+C5-CONTINUOUS-PLACEMENT-COMPARATOR:1|DECISIVE=I-BASIS+I-SCOPE-EACH-FREE-IN-3-OF-5|TV-BETWEEN-CELLS-TRANSPORT=2/63|TV-NO-DELIVERY-CONDITIONAL=0-CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2|BRIDGES-READING-REACHES-ONLY-COUNT-1-29-OF-201-WITH-FIBER-0>
R6BP-KERNEL-DEFECTIVE<RETURN=1/4|DEFECT=3/4|CLOSED-CLASS={2,4,5}|TERMINATES-A-S=TRUE|RENEWALS=4/3|SUPPORT-HOLES={1,2}-COST-79-OF-201-INTERVALS|BARE-STATE-0-READING-DISCLOSED-RETURN=13/16|SCOPE=DELIVERY-FREE>
R6BP-SEAM-AVOIDABLE-AT-DELIVERY-FREE-SCOPE<SINGLE-SCOPE-ROW-SET=S1+S4+I7|POSITIONAL-LAYER-DERIVABLE-FROM-S1-ALONE|S2-AGREES-AT-COUNT-4-WELD-EXACT|CAUSE-AT-TRANSPORT-SCOPE=THE-ESCAPE-NOT-ROW-PROVENANCE|MIDDLE-SLOT-ADMITS-NO-DELIVERY|DELIVERY-MULTIPLICITY-2-THEN-3|TRANSPORT-LAWS=3/7-1/7-3/7-AND-4/9-1/9-4/9|CONDITIONING-MASSES=3/7-AND-1/3|CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2>
EXTREMAL-BAR=DIES-AT-THE-BAR<VARIATIONAL-ROWS-0-OF-6|FUNCTIONALS=4|DISTINCT-SELECTIONS=3|MAX-DET-UNIQUE=TRUE|READOUT-CARRIES-NO-EXPLICIT-DET-WEIGHT-AT-W-0|DET-IS-RECORD-INTRINSIC|D12-SECOND-CLAUSE-EXTENDED-FROM-MODELS-TO-SELECTORS|DERIVED-LAW-RATIFIES-AT-1/3>
COVER=DISSOLVED<ROWS-PINNING-COVER-OBJECTS-0-OF-6|ROWS-DE-PERIODIZING-0-OF-6|DEEP-ARENAS-ROOTED-AND-DEPTH-NON-STATIONARY|NO-HUNT>
R6A-RECLASSIFICATION=<THE-SPLIT:ii-IN-DISTRIBUTION|FREE-TRANSVERSE-LINKS:UNCHANGED-0-OF-54|NEW-FRONT-VALUES:FORCED-RELATIVE-TO-THE-SPLIT-AND-AN-ORIENTATION-FIBER-2-SEPARATED-AT-63-OF-63-CYCLES|THE-LIFT-PAIR:UNCHANGED-AND-GROWN-2-TO-3|FORCES-A-VALUE-AT-0-OF-4|SUPPLIES-MORE-THAN-ONE-RULE-AT-2-OF-4>
S1-PROVENANCE=TWO-TRANSCRIPTIONS-NOT-TWO-DERIVATIONS<ROUTE-P=PAPER-31-FENCED-LITERAL|ROUTE-C=d43b-T_REF-LITERAL|THE-DERIVATION-NOT-RUN=d43b-rows-OVER-215-HISTORIES|#219-DISCLOSED>
PROVENANCE=BY-COMMITTED-SHA<CORPUS=d042ef1ae74e|R6A-TERMINAL=d5fb2a5956f7|R6A-DELIVERED=b0087a9d262b|PATH-VALUES-STABLE-29-OF-29|RECORD-FAMILY-AND-SPLIT-FIBERS-BYTE-IDENTICAL|WORKTREE-READS-0>
CONTROLS=R1-COPY-UNMOTIVATED|EXTERNAL-REFUSED-AT-SOURCE|COUNT-MISMATCH-FAILS-THE-CENSUS-201-OF-201|EXCLUDED-CITED-0>
```

Read plainly: **the stratum exists and is derivable without any
identification, at every count, from one row.  Its transport requires
an identification, and none is motivated.  The kernel is defective and
terminates; where it speaks it forces a distribution and never a
value; and the seam that looked like the blocker was never
load-bearing for the construction — what is genuinely blocked at
transport scope is a chain, and the corpus has measured why.**

---

## 16. Scope, caps, and what this unit does not do

Scope qualifiers are mandatory and are carried at every claim.  S1's
chain and S4's renewal theorem are two-actor delivery-free; S2's
census is transport scope, its interval lengths are ensemble data, and
its two length-4 cells are E2's leg one and E3's leg two; S5's
continuous layer is chosen, not derived, and is used only as a
labelled comparator.

Declared caps.  The two inhomogeneous records are censused at the two
sites the R6a receipt prints; the remaining seven sites of each are
uncensused, and one record's fiber is consequently not rebuilt.  The
first-return law is iterated to 400 terms with the residual tail
bounded exactly, and cross-checked by exhaustive enumeration only to
length 12.  S2's transport-scope census reaches two cells only, so
every transport-scope statement is measured at two cells, not proved.

Not done.  This unit does not construct Γ(cut′←cut).  It runs no
scaling census.  It does not touch the transport-scope renewal arm.
It claims nothing about the continuum beyond what the fiber-collapse
measurement earns.

**Registered lead, status printed:** `v11/note-u1c-depth15-two-sided.md`
is GREEN-UNREVIEWED and NOT CITABLE per its own status line.  No value
in this paper reads from it.  It is registered because S2 names depth
fifteen as the first depth at which its own question is askable, and a
terminal row there would extend the transport-scope census past two
cells.  It would not relieve any count-≥5 gap, because there is none:
the all-n law closes that from S1 alone.

---

## 17. The instrument

`83` anchors in three stages that genuinely short-circuit — `23`
quotation anchors binding every quotation this paper prints against
its source's committed bytes, then 18 file-bytes anchors on committed
objects at declared shas, then 42 path-value anchors.  A failure in a
stage stops the run before any later stage or any gate is evaluated,
and that is proved by measurement rather than by list order: under the
quotation-drift injection the run's evaluated stages are the first
alone.  Every quotation-shaped span in this paper must be a declared
row, and every declared row names a consumer gate that must exist,
have a non-literal predicate, and be observed to fail under a declared
mutant.  A separate sentinel scans the neighbourhood of each anchored
quotation for declared withdrawal and supersession markers and
compares the measured hits against a frozen declaration — three hits,
all of them D33's own §9 corrections beside S5's disclaimer,
adjudicated in the receipt.  A context window binds quote fidelity; it
cannot bind that a faithful quotation is in force, and this unit does
not claim otherwise.

`71` must-pass gates, zero failures, and none of them has a literal
predicate — an AST pass over the instrument's own syntax tree proves
it, and a second AST pass proves no gate predicate references the
injection channel.  `76` declared mutants, every one dying by its
named gate or anchor.  `20` compliance rows — the ten 2026-08-09 v14
engravings and their v13 companions — each naming the gate that
discharges it and the mutants *measured* to kill that gate.

The never-falsified census covers all 71 gates and is computed from
measured deaths: the whole mutant set is run in process, each gate's
failure set collected, and FALSIFIER-REACHES-IT entered only where a
mutant is observed to make the gate fail.  Zero unwaived; and each
gate's own declared falsifier is separately checked against those
measured deaths, so a declaration that names a mutant which does not
in fact kill the gate fails a gate of its own.

Every load-bearing number in this paper is rendered from a receipt
path and bound positionally — the value must appear inside its own
declared sentence context, exactly once — so exchanging two paper
numbers that are both receipt values dies.  The verdict string is
compared for complete equality against a comparator rebuilt segment by
segment from the receipt's own values; this paper's verdict block is
compared against the emitted one segment by segment, 10 of 10; the
four head names are selected by measurement and the counterfactual is
exhibited; and every restriction the unit measured is present as a
segment.
