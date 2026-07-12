# D13 hostile ontology/locality/physics review — round 1

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION / `INCOMPLETE-INVESTIGATION`**

## Executive finding

D13 has a valid action-**nonuniqueness** witness, but not yet a maximal action
theorem or a sealed-diamond action implementation.

The quarter-/half-iSWAP pair correctly shows that unitarity, exchange
symmetry, excitation conservation, entangling capacity, one composition
identity, one disjoint commutator, and one endpoint probability covariance
test do not select the interaction angle. The EFT and causal-set literature
also support the broader conclusion that covariance and consistency leave
physical coefficients and often whole families.

What does not survive hostile inspection is the stronger architecture claim.
The exact code contains two supplied unitary matrices and a supplied pointer
isometry. It contains no diamond, collar, screen, link, opportunity, output
birth, record identity, future record persistence, boundary state type, or
canonical construction fiber. The symmetric-monoidal boundary-amplitude
functor is proposed in prose rather than derived or implemented. Record
formation is imported as `W`, and “durability” is inferred from orthogonal
pointer projectors at one instant. Non-Markov whole-history compatibility is
not executed at all.

The strongest defensible result is therefore:

```text
ONE LOCAL UNITARY ACTION FAMILY = EXACT
ACTION UNIQUENESS UNDER THE TESTED FINITE CONSTRAINTS = REFUTED
GENERAL-BOUNDARY AMPLITUDES = PLAUSIBLE CANDIDATE ARCHITECTURE
SEALED-DIAMOND ACTION/RECORD PROCESS = NOT IMPLEMENTED
FIELDS, GRAMMAR, COUPLINGS, STATE, RECORD RULE, AND SCALE = PRIMITIVE
PROTOCOL VERDICT = INCOMPLETE-INVESTIGATION
```

## Artifacts and reproduction

Reviewed:

- `note-d13-action-selection-protocol.md`;
- `note-d13-v1-v10-action-ledger.md`;
- `note-d13-literature-audit-action-selection.md`;
- `note-d13-maximal-action-theorem.md`;
- both `code/d13_*.py` programs and both generated JSON outputs;
- the D12 whole-history endpoint relevant to the action claim.

The frozen exact JSON reports 12/12 true cells and the expected predictions:

```text
P(10|10, theta=pi/4) = 1/2
P(10|10, theta=pi/2) = 0
concurrence witnesses = 1, 1
verdict = LOCAL-COVARIANT-ACTION-UNIQUENESS-REFUTED
```

The same interaction-family core independently reproduces in D12's
standard-library exact engine at 18/18 with semantic receipt:

```text
7da912f8deb705aaa1467d3428aacf7cc626b249bf16c324c5c365f376b89db9
```

The D13 executable itself does **not** run in the current workspace:

```text
ModuleNotFoundError: No module named 'sympy'
```

`code/requirements.txt` does not list SymPy and no D13 lock/manifest supplies
it. Thus the simple algebra is independently credible, but D13's own exact
receipt is not clean-room reproducible under the checked repository
environment.

The corpus inventory is intentionally live until hostile reviews finish. Its
current generated output scans 528 Markdown files and labels 505 relevant;
the interpretive ledger still says 525/502. A final rerun and synchronized
manifest are therefore pending rather than passed.

## Blockers

### B1 — `Diam -> Hilb/CP` is an undefined proposal, not the selected mathematical type

**Severity:** critical

The theorem note declares a symmetric monoidal category `Diam` of sealed
screens/collars modulo construction presentation and a functor

```text
Z : Diam -> Hilb/CP.
```

Neither category is defined. In particular:

- objects and morphisms of `Diam` are not constructed;
- the construction-presentation quotient is assumed before it is proved;
- collar matching, orientations, dual boundaries, zero/null histories,
  refinement maps, and automorphisms are absent;
- `Hilb/CP` is not identified as linear Hilbert-space amplitudes, completely
  positive maps, a quotient category, or some combination;
- possible projective/anomaly factors and gluing normalization are omitted;
  and
- no theorem maps the D12 typed history category into this object.

Oeckl's general-boundary formulation is indeed a relevant established
architecture: it associates state spaces to general boundaries and amplitude
maps to regions, with explicit axioms and a probability interpretation
([foundations](https://arxiv.org/abs/hep-th/0509122)). It does not prove that
SHARD's record axioms uniquely entail D13's particular category or functor.

**Required repair:** define the source and target categories completely,
including the amplitude-versus-channel distinction, gluing maps, anomaly or
normalization factors, boundary orientations, and the exact construction
quotient. Call the result a candidate representation until derivation or an
equivalence theorem is supplied.

### B2 — The exact witness does not implement a sealed diamond

**Severity:** critical

`d13_local_action_family_exact.py` contains no runtime type corresponding to
the D13 packet

```text
(T,G,K,S/Amp,rho_boundary,R,Q,U).
```

It supplies a four-dimensional Hilbert space, `U_theta`, an input vector, an
effect, endpoint basis matrices, and a pointer isometry. There are no typed
lower/upper screens, owned collars, frame links, local order units,
opportunities, durable records, output collars, provenance, or physical
scales. “Diamond gluing” is the single matrix identity

```text
U_(pi/4) U_(pi/4) = U_(pi/2).
```

This is exact sequential composition, not a sealed-screen gluing theorem.
There is no contraction over a typed shared boundary, coherent alternative
sum, eventless repair, boundary term, or refinement comparison.

**Required repair:** insert both action members into the already repaired D12
typed multidiamond runtime. Every branch must consume an owned input collar,
create the declared record and output collar, store transported links and
frames, emit opportunities, and generate projective cylinder amplitudes.

### B3 — Record formation is imported, and permanence is not tested

**Severity:** critical

The code declares an isometry `W` that correlates each computational basis
state with an orthogonal pointer. Orthogonal pointer projectors then make
off-diagonal entries vanish. This correctly demonstrates a supplied ideal
measurement channel. It does not derive record formation from `U_theta` or an
action.

There is no record identifier, finite evidence content, parent diamond,
output inscription, repeat-read operation, future interaction, or test that
the record remains decoherent under history extension. Gell-Mann and Hartle's
strong-decoherence condition is stronger precisely because it requires
permanence of generalized records as histories extend
([Strong Decoherence](https://arxiv.org/abs/gr-qc/9509054)). One-time pointer
orthogonality does not establish that condition.

The notes partly admit that `R` remains primitive, but phrases such as “exact
durable records” and gate A5's positive construction overstate the code. The
verdict `PRIMITIVE-COEFFICIENTS` also understates the missing primitive: the
record instrument and coarse graining are entire physical maps, not numerical
coefficients of the action.

**Required repair:** either grade this as `SUPPLIED ORTHOGONAL POINTER
INSTRUMENT`, or derive `W/R` from an enlarged action and environment. In both
cases, generate typed immutable records and test permanence through later
allowed diamonds and observational coarse grainings.

### B4 — Construction-order gauge and locality regress to one commutator

**Severity:** major

The exact construction-order test is

```text
(U_q tensor I)(I tensor U_h) = (I tensor U_h)(U_q tensor I).
```

No auxiliary schedules are enumerated, no marked histories are
canonicalized, no amplitudes are coherently grouped into fibers, and no
record/collar births are compared. The overlap control only shows that
`U_q` and a local `Z` do not commute. D12 already achieved a stronger bounded
fiber test; D13 does not inherit it merely by citing the endpoint.

The statement “no universe-wide commit clock” is true of a fully supplied
general-boundary functor by construction. Here it is an architectural
assumption, not an emergent consequence of the exact model. Moreover,
`disjoint`, `overlapping`, and `shared screen` are primitive relations in
`Diam`; they already contain the locality structure whose origin is at issue.

**Required repair:** execute full amplitude/record histories in both orders,
push them to canonical typed fibers, compare complex amplitudes or the correct
decoherence weights without double counting, and retain the overlapping
negative control. State that causal ownership/disjointness is supplied by
`T,G` unless separately derived.

### B5 — The finite frame test is not the claimed general covariance gate

**Severity:** major

The code changes one whole two-qubit input basis and one whole output basis
and verifies one probability. It has no independently framed multidiamond
vertices, screens, links, order units, records, anchors, or history
amplitudes. It also tests unitary basis changes, not the nonunitary
`SL(2,C)`/Lorentz endpoint structure discussed in V10.

The gate table's wording “exact finite frame covariance” is defensible only
for this one endpoint cell. A6 as frozen in the protocol is not passed.

**Required repair:** use the D12 independent-vertex construction with both
action members, transport every typed boundary object, and explicitly retain
full Lorentz/nonunitary integration as open if it is not executed.

### B6 — Non-Markov compatibility is asserted, not demonstrated

**Severity:** major

A local amplitude law *can* yield a non-Markov visible-record process after
unobserved degrees of freedom are retained and later re-interact. That is a
possibility theorem, not a consequence of functorial gluing alone. The exact
D13 witness has one interaction and one pointer readout; it contains no
multi-time memory, environment return, process tensor, or two histories with
the same current record and different future conditionals.

D12 also established an important literature boundary that D13 omits:
Barandes proposes a stochastic-quantum correspondence, while Egri et al.
distinguish probability dynamics from probability on trajectories and show
generic nonuniqueness of stochastic implementations
([Egri et al.](https://arxiv.org/abs/2602.23491)). A boundary amplitude does
not automatically select a unique classical path measure or Barandes-style
implementation.

**Required repair:** say the architecture is *compatible with* non-Markov
record laws. To claim implementation, construct a memory-bearing multidiamond
history and show a future durable probability depends on an earlier record
beyond the current visible boundary. Carry forward D12's contested-Barandes
qualification.

### B7 — “Maximal” and “universal” are not established

**Severity:** major

The protocol requires every surviving architecture class A–H to be
implemented or excluded. D13 supplies prose comparisons and one member of
class B. It does not prove that primitive path measures, process tensors,
information actions, causal-set actions, bootstrap amplitudes, and empirically
identified EFTs all reduce faithfully to one `Diam -> Hilb/CP` functor with
the same record ontology.

The polar identity

```text
K = sqrt(nu) exp(-I/2 + i Phi)
```

is a lossless coordinate representation of a supplied nonzero amplitude. It
does not select amplitudes and does not establish the maximality of the
boundary-amplitude category.

**Required repair:** rename the theorem `boundary-amplitude candidate and
action nonuniqueness theorem`, or prove representation/equivalence results
for every surviving class. Under the frozen verdict rules, unexecuted classes
and gates require `INCOMPLETE-INVESTIGATION`.

### B8 — Primitive data are much broader than coefficients

**Severity:** major claim repair

The notes are admirably clear that field content, grammar, kernels, boundary
state, record instrument, quotient, units, masses, couplings, vacuum, and
metric scale remain supplied. The verdict

```text
UNIVERSAL-ACTION-ARCHITECTURE/PRIMITIVE-COEFFICIENTS
```

then narrows that admission incorrectly. `T`, `G`, `rho_boundary`, `R`, and
even the functorial representation are structural choices, not coefficients.

**Required repair:** use `BOUNDARY-AMPLITUDE-ARCHITECTURE CANDIDATE /
PRIMITIVE PHYSICAL PACKET REMAINS`, unless stronger gates select the missing
objects.

### B9 — The corpus census is auditable but does not close A0

**Severity:** major

The machine inventory is a broad keyword census. It hashes files and records
counts, headings, and at most 24 scope-guard lines per relevant file. It does
not extract or adjudicate every action claim. With 505 of 528 Markdown files
flagged, “relevance” is intentionally high-recall and very low-specificity.
The version ledger is a useful expert summary, not a clause-complete proof
that no older action was omitted.

The live inventory and prose are currently unsynchronized: JSON says 528/505
while the ledger says 525/502. This is expected during review but means A0 and
the final manifest remain pending.

**Required repair:** rerun after all D13 reviews, synchronize the ledger and
hash manifest, and add a human adjudication table mapping each actual
candidate action—not merely each version—to its hypotheses, equivalences,
free data, and final status.

### B10 — The exact artifact is not self-contained or frozen for hostile reconstruction

**Severity:** major

The D13 code introduces SymPy without adding it to the repository dependency
manifest or recording a version. The default and alternate system Python
runtimes cannot import it. The generated JSON shows the intended result, and
D12 independently confirms the core unitary family, but A12 asks for
independent clean-room reproduction of the reviewed bytes.

**Required repair:** declare and lock SymPy, record the interpreter and
version, run normal/optimized or another independent exact path, freeze
source/stdout/semantic hashes, and provide a dependency-free reconstruction
or second algebra system for the 12 cells.

## Physics and literature findings

### Field content, couplings, and scales

**Correctly characterized.** D13 does not claim to derive Standard Model
fields, masses, mixings, Wilson coefficients, the boundary state, `hbar`,
Newton's constant, or the evidence-to-SI bridge. The `U_theta` pair and the
`lambda phi^4` family correctly exhibit coefficient freedom within supplied
sectors. The continuum argument should remain explicitly conditional on the
field content, dimension, vacuum, and scattering assumptions.

### Causal sets and gravity

**Correctly cautious, not a recovery result.** Benincasa–Dowker construct a
one-parameter nonlocal causal-set operator whose continuum approximation is
stated for causal sets approximating four-dimensional spacetime and depends
on a nonlocality scale
([paper](https://arxiv.org/abs/1001.2725)). Rideout–Sorkin derive a general
family of sequential-growth dynamics, not one law
([paper](https://arxiv.org/abs/gr-qc/9904062)).

These sources support D13's refusal: causal order, dimension, sprinkling or
sum measure, contour, couplings, boundary state, and record rule still have to
be supplied. Likewise, the EFT metric action presupposes a metric and a
four-dimensional low-energy sector; it does not derive causal structure from
records. D13 has not recovered gravity, and the notes mostly say so.

### Consistency and bootstrap claims

**Acceptable with their stated hypotheses.** Deser-style self-coupling and
Lovelock results constrain a chosen massless-spin/metric/derivative sector;
they do not select the sector or its scales. The S-matrix bootstrap explicitly
maps an infinite-dimensional allowed space and only sometimes identifies
special boundary points
([survey](https://arxiv.org/abs/2203.02421)). These are conditional selectors,
not missing universal action generators.

## What physical principle could still select the action?

No principle actually supplied in D13 distinguishes every primitive in

```text
(T,G,K,S/Amp,rho_boundary,R,Q,U).
```

A successful new principle must at minimum:

1. choose the field/record spectrum and admissible local collars;
2. distinguish the exact `theta=pi/4` and `theta=pi/2` survivors without
   naming the desired answer;
3. fix the boundary state and record/decoherence instrument, not only the
   unitary bulk kernel;
4. determine dimensionful ratios and the gravity/clock/rod bridge;
5. be invariant under the D13 equivalence moves; and
6. make predictions on data not used to formulate it.

Plausible research routes remain, but none is presently a selector:

- a unique anomaly-free field/representation theorem would still need
  couplings, state, and scale;
- a unique RG fixed point plus a uniquely fixed relevant trajectory and
  boundary condition could select more, but D13 supplies none of those
  objects;
- an amplitude bootstrap could work in a sharply declared sector if it
  isolated one point and scale, which is not shown generally;
- an intrinsic record/decoherence extremum would need a noncircular,
  representation-invariant functional and would have to reject the exact
  action pair; and
- empirical scattering, process tomography, cosmology, and gravity data can
  identify an effective packet, but that is empirical action selection rather
  than derivation from records.

The missing ingredient is therefore not “least action” by itself. It is new
physical information or a genuinely stronger axiom that selects the action,
record channel, state, and scale simultaneously.

## V9 holdout adjudication

**The refusal is correct.** No action has been uniquely derived or selected
on independent data. Running V9 cone, dimension, or gravity diagnostics on a
chosen Lorentz-covariant continuum action would import the desired geometry;
running the old diffusion-churn builder would test a different guessed growth
law. Either would violate the frozen A10–A11 sequence.

This refusal should not be described as evidence that the boundary-amplitude
architecture is physically successful. It is simply correct experimental
discipline while the selector is absent.

## Gate adjudication

| Gate | Hostile result |
|---|---|
| A0 corpus recovery | **OPEN.** Live high-recall census and stale prose counts; no clause-complete candidate adjudication. |
| A1 complete typed ontology | **FAIL.** Packet fields are listed in prose, absent from the executable. |
| A2 locality/no global clock | **PARTIAL.** Boundary formalism can avoid a preferred clock, but locality/disjointness is imported and only one commutator is checked. |
| A3 amplitude/action gluing | **FAIL at registered scope.** One sequential product identity, no typed shared-boundary or coherent-sum/refinement law. |
| A4 quantum consistency | **PARTIAL.** Exact unitary normalization, entangling capacity, and pointer probabilities; no general instruments, open systems, or operational no-signalling process. |
| A5 record formation | **FAIL as derivation/durability.** Supplied pointer isometry and one-time orthogonality only. |
| A6 covariance/gauge | **PARTIAL.** One input/output unitary basis cell, not generated independent-vertex or Lorentz covariance. |
| A7 uniqueness | **REFUTED at tested finite scope.** This is the strongest exact D13 result. |
| A8 fields/couplings | **OPEN and honestly primitive.** |
| A9 units/gravity | **OPEN and honestly primitive.** |
| A10 empirical selection | **NOT FIRED.** Correctly no universe-action claim. |
| A11 spacetime holdouts | **CORRECTLY REFUSED.** |
| A12 hostile closure | **OPEN.** This review finds blockers and the SymPy artifact is not clean-room reproducible. |

## Accepted results

Hostile review accepts:

- exact physical inequivalence of the quarter-/half-iSWAP kernels;
- failure of the tested locality/symmetry/unitarity conditions to select
  `theta`;
- the polar evidence/phase formula as a representation of a supplied
  nonzero amplitude, not a generator;
- general-boundary amplitudes as a serious candidate architecture that avoids
  preferred global time once region/boundary structure is supplied;
- strong decoherence, process tensors, EFT, causal-set actions, and bootstrap
  methods as conditional frameworks rather than unique law selectors;
- the conclusion that field content, couplings, boundary state, record rule,
  physical units, and gravity remain unselected; and
- refusal to open the V9 geometry holdouts.

## Verdict

**MAJOR REVISION / `INCOMPLETE-INVESTIGATION`.** D13 successfully moves the
question one level upward and proves a useful finite action nonuniqueness
lemma. It has not shown that boundary amplitudes are the maximal object
entailed by sealed records, nor implemented the typed diamond/action/record
process required by its own protocol.

The defensible headline is:

```text
TESTED FINITE ACTION UNIQUENESS = REFUTED
GENERAL-BOUNDARY AMPLITUDE = CANDIDATE ARCHITECTURE
RECORD FORMATION, PHYSICAL ACTION, STATE, AND SCALE = PRIMITIVE
GEOMETRY HOLDOUTS = CORRECTLY CLOSED
= INCOMPLETE-INVESTIGATION
```

Do not discard the `U_theta` theorem. Narrow its title and claims, make the
artifact reproducible, and build or explicitly decline the missing
sealed-diamond/action/record implementation before another closure round.
