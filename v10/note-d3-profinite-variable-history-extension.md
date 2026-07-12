# D3 — profinite variable-history extension dynamics

**Status:** complete at the finite unmarked common-future/prefix-tower claim
ceiling, 2026-07-11. Preregistered before the D3 executable was written or
run; revised after hostile-review round 1; independently passed in round 2.
All production code and generated receipts remain under `v10/`. Exact
integer/rational arithmetic is mandatory wherever available; any exponential
or cancellation-sensitive diagnostic uses `Decimal` with precision at least
120.

## 1. Question

Investigation 2 proved a no-bootstrap theorem for deterministic closure on a
fixed support vertex set. D3 asks whether that arena was too restrictive:

> Can a variable-history growth law preserve every old recorded relationship
> while creating a new joint record whose precursor meets previously
> disconnected components, and do construction-order gauge, Barandes-style
> full-history conditioning, sealed-diamond composition, or the v9 profinite
> spaces select the probability of that extension?

The candidate transition has the form

$$
H_n\longrightarrow H_{n+1}=H_n\cup\{e_n\},
$$

not a closure `F(H_n)` on the same event set. In the unmarked causal-order
shadow, the ancestry of the new maximal event is a down-set `D` of `H_n`; its
direct parents are the maximal elements of `D`.

## 2. Frozen distinctions

The investigation must not conflate:

1. preservation of all old relations with prohibition of new incidence to a
   newly born event;
2. a labeled finite-prefix tower with the covariant stem/covtree tower;
3. existence of a compatible history measure with selection of that measure;
4. dependence on the full history with a formula assigning probabilities;
5. a common-future joint event with a directed influence edge between its old
   ancestors;
6. pre-geometric ancestry locality with locality in an emergent metric;
7. a finite unmarked causet shadow with a completed marked sealed diamond.

## 3. Frozen finite arena

The exact receipt will use naturally labeled finite partial orders on
`{0,...,n-1}`. A legal one-record extension adds the maximal label `n` above
an ancestor-closed subset `D` and nowhere else. End-deletion removes `n`.

The undirected comparability graph supplies a deliberately weak component
diagnostic. A **bridge extension** is one whose precursor meets at least two
old components. This says only that the new event has ancestry in both; it
does not declare the old components spatially near, causally comparable, or
able to signal to one another.

The finite arena is an incidence/order shadow. Marks, screens, collars,
likelihood blocks, transport, holonomy, and outcome instruments are not
silently reconstructed from it.

## 4. Preregistered theorem and receipt gates

### A. Variable-history mechanics

- **A1 — tower census:** enumerate every naturally labeled order through the
  registered finite cutoff independently by growth and by transitively closed
  upper-triangular relations.
- **A2 — end-deletion:** every generated child deletes to exactly its parent;
  every finite parent has at least one child.
- **A3 — past immutability:** a legal maximal extension changes no order
  relation between old elements.
- **A4 — bridge existence:** every parent with at least two comparability
  components has at least one bridge extension.
- **A5 — direct-parent typing:** the maximal elements of the precursor are
  exactly the covers into the new event.
- **A6 — fixed-vertex separation:** the child has cardinality `n+1`; therefore
  D2's closure census on a fixed `n`-vertex support system does not apply
  without an additional descent theorem.

### B. Measure and kernel equivalence

- **B1 — normalized exact kernels:** construct at least two positive rational,
  relabeling-covariant kernels on legal down-set extensions.
- **B2 — cylinder consistency:** recursively generated finite measures obey
  `mu_n(H)=sum_{child -> H} mu_{n+1}(child)` exactly.
- **B3 — kernel recovery:** at every positive-mass parent, recover the original
  transition kernel as `mu_{n+1}(child)/mu_n(parent)`.
- **B4 — nonselection witness:** two kernels on the same extension arena obey
  the same tower, preservation, covariance, and consistency gates but assign
  different bridge probabilities somewhere.
- **B5 — click/placement factorization:** hold the v7 conditional waiting law
  `exp(-Delta I)` fixed while changing the conditional child kernel; print the
  common survival at at least 120-digit working precision and the unequal
  extension probabilities.

### C. Gauge and profinite scope

- **C1 — isomorphism covariance:** isomorphic parent/precursor pairs receive
  equal probabilities under each registered kernel.
- **C2 — quotient discipline:** distinguish equality of a physical pushforward
  from equality of raw scheduler-path weights; D3 will not reimpose the
  superseded strong gauge convention.
- **C3 — two inverse limits:** verify by an exact finite witness that one
  covtree node can contain multiple nonisomorphic exact-rank stems. Therefore
  a covtree refinement step is not a one-event prefix transition.
- **C4 — arena-not-selector:** the labeled history inverse limit and the stem
  spectrum can host compatible measures, but topology alone supplies no
  numerical kernel.
- **C5 — marked-completion boundary:** no profinite theorem for real/rational
  marks is claimed without finite observable alphabets or an explicit compact
  marked topology.

### D. Diamond interpretation

- **D1 — joint-record reading:** if the precursor meets two old components,
  the new event is a common-future record with both in its ancestry.
- **D2 — no retroactive old edge:** no relation between two old incomparable
  records is inserted.
- **D3 — locality refusal:** the construction does not explain why those
  components were eligible to participate. A bridge kernel is a root/bridge
  law, not a derivation of metric locality.
- **D4 — downstream composition:** once the new marked joint event and its
  interfaces are supplied, D2 pushout and D1 no-silent tests may apply; neither
  supplies its birth probability upstream.

## 5. Registered law family

For a parent order `C` and legal down-set `D`, define exact positive weights

$$
w_{a,b}(D\mid C)=a^{|D|}b^{\beta_C(D)},
$$

where `a,b` are positive rationals and

$$
\beta_C(D)=\max(0,\#\{\text{old comparability components met by }D\}-1).
$$

Normalize over all down-sets of `C`. This family is registered as a
nonuniqueness witness, not as proposed physics. At least two parameter pairs
must be tested. Any bug or covariance failure kills the witness rather than
being tuned away after inspection.

## 6. Verdict gates

- `SELECTED`: the frozen foundational conditions leave exactly one extension
  law in the audited arena.
- `CONSISTENT-FAMILY`: variable-history birth is consistent and evades the
  fixed-vertex no-go, but at least two inequivalent measures survive.
- `NO-BRIDGE`: preservation/projectivity forbids even a new-event bridge.
- `ILL-TYPED`: the prefix/profinite/diamond maps cannot be made mutually
  coherent at the claimed scope.

No cone, dimension, continuum, quantum, or absolute-scale conclusion is
licensed by any D3 verdict. Those are mandatory downstream tests only after a
marked interacting law is actually selected or explicitly posited.

## 7. Hostile-review protocol

After the notes, executable, and Paper 4 are complete, independent hostile
reviews will audit:

1. mathematics and measure/projective claims;
2. independent reconstruction and executable reproducibility;
3. ontology, Barandes/SHARD scope, diamonds, locality, and the two profinite
   towers.

Every concrete opening must be investigated and dispositioned before the
next review round. Final acceptance requires all streams to reproduce the
receipt and accept the scoped conclusion.

## 8. Initial exact results

The preregistered executable was then written and run:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d3_profinite_extension_exact.py
```

Initial result: **23/23 checks passed**. Hostile round 1 confirmed the core
finite result but rejected four overgraded controls. After executing every
opening, the repaired result is **27/27 checks passed**. Consecutive repaired
runs are byte-identical.

### 8.1 Variable history evades the fixed-vertex no-go

Independent enumerations agree on the naturally labeled order counts

```text
n = 0,1,2,3,4,5:  1, 1, 2, 7, 40, 357.
```

Every legal new-maximal-event extension end-deletes to exactly its parent and
changes no old-old relation. Across the 203 disconnected audited parents
through `n=5`, every one admits a down-set precursor meeting multiple old
components. The new event joins those components in the undirected incidence
shadow while leaving them mutually incomparable in the old past.

The extension's ancestry is the chosen down-set `D`; its direct parents are
the maximal elements of `D`. Thus the primitive incidence is more accurately
written into the new record than inserted retroactively between old records.

### 8.2 A path measure and positive conditional kernels are equivalent

Both registered positive rational kernel families normalize exactly. Their
recursively generated finite cylinder measures obey

$$
\mu_n(C)=\sum_{e_n(C')=C}\mu_{n+1}(C')
$$

at every audited parent, and the actual next-level cylinder ratios recover
the original kernel exactly. This is the finite shadow of the standard
projective-limit statement: compatible finite probability measures define a
probability measure on the compact labeled history inverse limit.

This equivalence clarifies the primitive-law fork. A primitive positive path
measure supplies its supported extensions and their conditional weights. It
does not derive itself from record principles.

### 8.3 Covariance and profinite consistency do not select the law

On the three-record antichain, the registered `b=1` and `b=2` laws assign
total bridge probabilities

$$
P_{1}(\text{bridge})=\frac12,
\qquad
P_{2}(\text{bridge})=\frac57.
$$

Both are positive on the same extension set, exactly normalized, exactly
isomorphism-covariant over 17,648 audited mapped precursor cases, and generate
end-deletion-consistent measures on the same finite tower. Individual pair
precursors receive `1/8` and `1/7`. The family is a nonselection witness, not
a candidate physical law; its component-count weight is intentionally allowed
to use global finite-history information.

The v7 evidence clock is orthogonal to this choice. At `Delta I=1.1`, both
placement laws retain

```text
exp(-1.1) =
0.33287108369807955328884690643131552161247952156921249179333138675074708541284431161261707270054785196654212528402885007445958
```

at 140-digit working precision. Hence the click clock fixes whether/when a
seal occurs in evidence coordinates, not which precursor or joint support the
seal uses.

### 8.4 The two profinite towers have different physical readings

The labeled history tower

$$
\widetilde\Omega_0\leftarrow\widetilde\Omega_1
\leftarrow\widetilde\Omega_2\leftarrow\cdots
$$

uses end-deletion and is a sequential-prefix arena. The stem spectrum/covtree
tower instead refines which finite stem questions a completed history
answers. An exact three-event witness—one two-chain plus one isolated
event—has both the two-chain and two-antichain as exact-rank-two stems. Its
rank-two covtree datum is therefore a **set of two nonisomorphic stem types**,
not one two-event prefix. A covtree step is not automatically a seal click.

Covtree can carry a manifestly covariant stem-observable/spectrum measure. A
full-history measure requires a generally nonunique lift through the
completed-history evaluation map. Turning either object into SHARD's
next-record law still requires a physical filtration or a marked extension
kernel relating observable refinement to committed record birth.

### 8.5 Initial verdict

```text
CONSISTENT-FAMILY
```

Variable-history growth consistently reconciles exact preservation of the
old past with new common-future incidence. The labeled-prefix profinite
structure hosts multiple laws but does not select one. This is not yet an
interaction theorem. The remaining physics is the common-future eligibility
and weighting law, the marked sealed-diamond content of the event, and the
boundary memory needed for record restriction.

## 9. Openings pinned before hostile round 1

The initial paper must be attacked on at least these points:

1. whether “bridge” overstates what a common-future event proves;
2. whether cylinder consistency was tested from actual next-level masses;
3. whether the infinite projective-limit theorem needs hypotheses not present
   in the finite receipt;
4. whether a covtree random walk can itself count as dynamics even though its
   level is not a click count;
5. whether primitive full-history conditioning has been confused with Markov
   factorization;
6. whether the unmarked causet shadow can legitimately say anything about a
   sealed holonomy diamond;
7. whether the witness law's global component statistic silently reintroduces
   a universe ledger;
8. whether an arbitrary new-event precursor has any defensible locality
   interpretation;
9. whether real/rational marks preserve profiniteness;
10. whether any D3 result changes the v9 cone or dimension claims before the
    selected law is implemented.

## 10. Hostile round 1 and opening dispositions

All three independent streams returned **MAJOR REVISION** while independently
confirming the extension/down-set theorem, counts, 203-parent common-future
census, exact rational probabilities, labeled-prefix inverse-limit theorem,
and the prefix/covtree distinction.

### O1 — overstrong physical nouns: repaired

The theorem object is now a **common-future extension** or **bridge shadow**.
The unmarked order proves ancestry incidence only. `Interaction`, `joint
record`, `carrier birth`, and `bridge event` are reserved for a marked law
with typed ports and a load-bearing joint proposition/outcome.

### O2 — temporal consistency versus record restriction: investigated, failure promoted

The deterministic arena restricts exactly:

$$
C[D]|_{K\cup\{e\}}=(C|_K)[D\cap K].
$$

The repaired receipt verifies 6,064 arbitrary old-subset incidence squares.
The probabilities fail the analogous autonomy equation. For the chain
`0<1`, retained stem `{0}`,

$$
P_{\rm push}=(1/3,2/3),
\qquad
P_{\rm recompute}=(1/2,1/2).
$$

Across the audited ancestor-closed squares, the `b=1` law fails 212 and the
`b=2` law fails 296. Therefore D3 claims only end-deletion prefix consistency.

Interpretation: the global measure is consistent, but a retained unmarked
subsystem is not autonomous. The pushed-forward prediction exists; it differs
from pretending discarded history never existed. A SHARD no-silent
restriction would need boundary/environment marks sufficient to close that
gap. Whether a marked kernel can do so is open.

### O3 — placeholder gauge arithmetic: replaced by actual quotient

The arbitrary `1/4+3/4` illustration was removed. At every audited level, the
repaired receipt canonicalizes each naturally labeled order, sums its actual
fiber mass, and verifies exact normalization. Raw natural-label masses can be
unequal inside one orbit. The two finite physical pushforwards remain
inequivalent: the three-antichain has mass `1/8` for `b=1` and `1/10` for
`b=2`.

This is a finite quotient theorem only. There is no canonical “delete the
last event” map on an unlabeled causet, so an infinite unlabeled-prefix measure
has not been constructed. Covtree consistency is separate.

### O4 — coupled kernel recovery and state typing: repaired

The receipt now traverses actual next-level child states, independently
recovers each parent by end-deletion and each precursor from the new event's
ancestry, checks one-to-one fibers, recomputes the closed-form kernel, and then
forms the cylinder sums. Finite level `n` remains part of state identity, so
empty relations at different cardinalities cannot collide.

### O5 — eligibility versus weighting: separated

The two preregistered positive laws share support and prove weighting
nonselection. A post-review controlled-zero covariant kernel forbids all
`beta>0` precursors while remaining normalized and end-deletion consistent.
It has bridge-shadow probability zero versus `1/2` for the positive uniform
law. This proves eligibility nonselection only under the weaker global-prefix
gates; no restriction/locality promotion is made.

### O6 — covtree lift: repaired

A covtree random walk defines a stem-observable/spectrum measure. It is not
automatically a unique full-history measure because the completed-history
evaluation map has rogue fibers. A full-history law needs a lift through those
fibers; a SHARD click law additionally needs a marked committed-history
filtration. The finite chain-plus-isolate certificate is extended through nine
events without changing its rank-two stem theory; the general infinite
statement is explicitly imported from v9 Paper 7.

### O7 — downstream diamond scope: repaired

D2 composes only supplied typed marked-support incidence. It does not glue
probability laws, screens, collars, sources, transport, or holonomy. D1 tests
finite boundary logic. Full sealed-diamond gluing and birth remain open.

### O8 — universe ledger and Barandes: repaired

The `(a,b)` family is now explicitly a global-prefix/universe-ledger control:
it enumerates every down-set, sees the entire component decomposition, and
normalizes one next event. It proves nonselection, not locality.

Barandes indivisibility, full-history dependence, disintegration of a supplied
measure, and derivation of that measure remain separate. The primitive-measure
route must include its filtration and extension domain. No correspondence
principle selects them.

### O9 — geometry: unchanged refusal

No cone, dimension, stationarity, scale, continuum, or quantum inference was
made. The refusal survives unchanged.

## 11. Round-2 claim submitted for review

```text
IMMUTABLE-PAST COMMON-FUTURE EXTENSION
+ LABELED-PREFIX CONSISTENT-FAMILY
+ FINITE UNMARKED-QUOTIENT NONSELECTION
+ UNMARKED RESTRICTION-NATURALITY FAILURE
+ PREFIX-LEVEL ELIGIBILITY NONSELECTION
```

This is not the final interacting click law. The next selector must be a
record-readable marked finite-boundary rule, or the theory must explicitly
posit a global/nonlocal history measure, connected boundary seed, or eternal
spectrum law plus history lift.

## 12. Hostile round-2 closure

All three streams passed the repaired claim ceiling:

- mathematics/measure/profinite: **PASS**;
- independent reconstruction/reproducibility: **PASS**;
- ontology/locality/Barandes/diamonds: **PASS** after one stale covtree
  sentence was corrected and rechecked.

No D3 blocker or undispositioned opening remains. Final receipt: 27/27; two
stdout runs byte-identical; self-containment: 4/4.
