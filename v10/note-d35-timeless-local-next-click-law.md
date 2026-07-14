# D35 — timeless local next-click law

**Status:** PIN before corpus receipt, derivation, simulation or result.
**Date:** 2026-07-14.

**Parent:** terminal D34f / Paper 23 at commit `de51b4e`.

## 1. Question

Can SHARD define the probability law of A's next record update without a
global time, a numerical proper time on each record, or a supplied Poisson
clock, while retaining:

- a strong local causal principle for which evidence may enter A's next
  record;
- the already constructed D24 birth-content kernel and D25/D27 reception
  constraints;
- construction-order gauge for incomparable events;
- projectively consistent finite-stem probabilities;
- genuine record birth and variable actor support; and
- an executable actor-local sampler whose physical law is independent of its
  machine serialization?

The target is not another D34b clock model.  It is a time-free marked-history
law or a proof that the inherited structures do not select one.

## 2. Corpus boundary

Before derivation, a deterministic census must cover every primary paper and
note in V1--V10 existing before D35.  Reviews are routed through their parent
artifacts and may be read where they changed a terminal claim.  The census
must hash each file and classify at least:

```text
causal order and locality;
next-click and record-wire semantics;
birth/support/opportunity kernels;
diamonds, collars and holonomy;
whole-history/path measures and actions;
construction-order gauge/projectivity/profinite stems;
proper/local/global clock claims;
Markov and non-Markov predictive-state claims;
simulation/generative algorithms;
scope guards and retractions.
```

The accepted D13 522-file action census is inherited as an independent
antecedent control, not substituted for the fresh D35 causal/birth/time audit.

## 3. Primitive time-free object

A finite marked record stem is

```text
H = (events, directed ancestry, record wires, active tips,
     typed marks, parentage, sealed evidence references).
```

There is no numerical event time.  The ancestry relation is acyclic and
locally finite.  Every record wire is linearly ordered by its own successive
updates; unrelated events may remain incomparable.

A completed history is a compatible infinite or terminal extension of finite
stems.  A candidate primitive law is a normalized measure `mu` on completed
marked histories, specified by consistent finite cylinder probabilities.
Sequential growth is a sampling representation only.  Its integer step and
linear extension are construction gauge.

## 4. Strong causal acquisition principle

Let A1 be a current A-wire event and let A2(H) be the next A-wire successor in
a completed history H.  Define

```text
NewPast_A(A1,A2) = Anc(A2) minus Anc(A1).
```

The structural principle under test is:

> **CAP.** Evidence record e is newly acquired by A at A2 if and only if e is
> in `NewPast_A(A1,A2)`, connected to A2 by a finite chain of locally licensed
> record transfers.  Construction order, nominal adjacency and correlation
> through a common older cause do not by themselves constitute acquisition.

The realized relation is binary.  The pre-click probability is the cylinder
ratio

```text
P(e reaches A2 | H0)
 = mu({completed H extending H0: e in NewPast_A(A1,A2(H))})
   / mu({completed H extending H0}).
```

No elapsed time occurs.  “Before the next A click” is the local stopping
condition that A2 is A1's first wire successor.

An operational influence strengthening must be typed separately: when an
intervention family exists, changing e's locally allowed content must change
the A2 law.  CAP ancestry alone may carry correlation and is not silently
promoted to interventionist causation.

## 5. Existing birth result and missing layer

D24 is not reopened as absent.  Its one-parent tree birth family supplies:

```text
fresh child initialized in |0>;
controlled-Ry parent/child coupling g_e;
isometric/distinguishability-preserving closure;
collar locality and exact ledger balance;
construction-order gauge on rooted trees;
click-identifiability of tree and interior couplings.
```

Its own scope guard leaves free which collar attaches next and `g_e`.  D1
shows that no-silent centers do not select support or firing probability; D2
shows that diamond amalgamation composes a supplied interface but does not
create the first carrier; D28 names the opportunity kernel.

Accordingly distinguish:

```text
q(o | H)          opportunity/extension selection on a finite stem;
B_o(dr | H)       D24-type conditional newborn record-content kernel.
```

The time-free law must combine them without pretending that B already selects
q.  Paper 19's completeness remains at its declared experimental interface,
not a unique cosmological history measure.

## 6. Mathematical obligations

Any positive result must establish:

### O1 — legal grammar and local finiteness

Continuation, one-parent birth, interaction and any admitted join have typed
parents and finite local ancestry.  Every finite causal interval is finite.
The root/seed rule is explicit.

### O2 — cylinder normalization and projectivity

Finite stem probabilities are nonnegative, normalized and compatible under
restriction.  If amplitudes rather than probabilities are used, strong
positivity and the probability extraction are separately proved.

### O3 — construction-order gauge

For independent extensions x,y,

```text
p(x | H) p(y | Hx) = p(y | H) p(x | Hy),
```

or the equivalent cylinder identity.  Two linear extensions of one marked
causal history have one physical weight.

### O4 — strong locality

An event's extension weight and content kernel consult only its declared
causal collar plus inherited sufficient marks.  Any normalization depending
on an entire spacelike antichain is disclosed as global and cannot earn the
local row.

### O5 — CAP next-A law

The next A-wire successor and its complete ancestry are well typed on the
completed-history cylinders.  CAP acquisition probabilities are exactly
recoverable and unaffected by disjoint components.

### O6 — D24/D25/D27 compatibility

Birth uses the admitted D24 isometric family at the frozen tree scope;
reception obeys the distinguishability-isometry/NSE ceiling.  Any selector of
opportunity or `g_e` is proved, clearly posited, or returned as a family.

### O7 — real simulation

One self-contained implementation under `v10/code/` must provide:

1. an exact finite-stem enumerator;
2. at least two incompatible machine schedulers/linear-extension policies;
3. an actor/tip-local message implementation rather than only a global-state
   transition table;
4. exact agreement of gauge-quotiented history and next-A distributions;
5. live birth, interaction, ancestry transfer and A stopping;
6. deterministic replay and independent hash-seed equality; and
7. explicit rejection of malformed nonlocal or ancestry-forging messages.

A central priority queue may be an implementation aid only if changing it
does not change the physical measure.  No computer step is called time.

### O8 — infinite ceiling

The finite law must identify what is proved about completed histories.  A
finite discrete inverse system is not identified with the v9 stem spectrum
without the construction-order quotient and bonding maps.  Existence,
uniqueness and continuity are separately scored.

## 7. Exact receipt requirements

Discrete probabilities and amplitudes use exact rational/algebraic arithmetic
where available.  Decimal evaluations use at least 100-digit working
precision.  The receipt must print:

```text
corpus file count and stream hash;
primary-artifact category counts;
finite-stem normalization/projectivity checks;
independent-extension covariance checks;
disconnected-component invariance;
birth/reception compatibility checks;
next-A outcome and ancestry distributions;
scheduler and actor-message equivalence counts;
malformed-message rejection counts;
finite/infinite/profinite ceiling;
source, stdout and internal hashes.
```

Finite enumeration is a regression/counterexample search.  Any all-size claim
requires a separate proof.

## 8. Decision rows

Apply the first supported row.

1. **TIMELESS LOCAL NEXT-CLICK LAW / SELECTED:** O1--O8 hold and inherited
   principles uniquely select the extension/opportunity and D24 parameter
   data at the declared scope.
2. **TIMELESS LOCAL NEXT-CLICK FAMILY / EXECUTABLE:** a covariant projective
   actor-local family exists and is executable, but opportunity weights,
   couplings or root data remain extra physics.
3. **TIMELESS MEASURE / NONLOCAL NORMALIZATION:** a projective history measure
   exists but exact next-click probabilities require spacelike-global state.
4. **FINITE TRACE LAW ONLY:** finite scheduler-covariant stems exist, but no
   completed-history measure or consistent projective family is proved.
5. **NO TIME-FREE LIFT:** D24/reception/locality constraints are inconsistent
   with every registered time-free extension family.
6. **REFUSAL/UNDEFINED:** a required grammar, opportunity law, root, instrument
   or completed-history object remains absent.

No row may claim physical proper time, Lorentzian distance, cone roundness,
dimension, G, the actual universe law or a v9 posterior factorization.

## 9. Review protocol

After the corpus audit and frozen candidate are executable, three independent
hostile streams must attack:

1. probability/projectivity/profinite completion;
2. causal locality/construction gauge/actor simulation; and
3. D24 birth/reception/quantum and ontology scope.

Every major opening is frozen before repair.  A synthesis paper is written
only after the D35 theorem ceiling survives exact deltas.
