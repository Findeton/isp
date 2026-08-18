# OVG hostile review protocol

Status: **FROZEN BEFORE REVIEWER ASSIGNMENT**.

This protocol binds the replay-verified green-unreviewed OVG candidate. It
does not authorize reviewer dispatch, adjudication, repair, or terminal
promotion.

## Immutable target

| object | binding |
|---|---|
| candidate commit | `bb0f13aedadc354068ea2bcc08478bcd8c43ded1` |
| verification commit | `22da1143cfdea19cea4a29f2b942677a02c0c110` |
| pin | `286e681a05b7346226f4f3f381036b2b6bc07d809c93c2ac352d9f71a0f44c40` |
| generic core | `7b17a138dc45f564a5180fca81bdb4620aaa570514d090d8a5c45f0f22d985bf` |
| physical fixture | `7b7658492a49c77f6c9ee3e0a2031d5121c627aad5ae6630e21940a68c92b133` |
| repaired scorer | `75cc0e7279ee93a60bfa520eecb4ea37fcde49b3d9e9f7298d98031396628844` |
| freeze/refusal/repair record | `d44fd66678fe16ce85c2c9780142583a111776108b87788b734833419c9a3b34` |
| transcript | `48cf0fdecc43b1d148c97bac936a879cbbcf14daddfccd6e597014017155fe7f` |
| receipt | `4ba954430acd0772da62c8df16b2c6b08bca9e76fd7b25d3b5b72fcc43ce2852` |
| Paper 5 | `89a6ad8b10b97351d71a499ebbb36b2cf5a89f32d5ec9d005f9b4a68dab16b31` |
| candidate verification | `12774e1a2d9d72d147a67e066679bc6e376e29f4acecc453f3d164ce19ba37e5` |

Frozen machine findings, in order:

```text
OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED
SINGLE-PORT-PHASE-CONSTRAINED
MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED
LOCAL-FLAG-KINEMATICALLY-PERMITTED-BUT-IMPLEMENTATION-UNSELECTED
COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY
CAUSAL-NONSEPARABILITY-UNTESTED
OVERLAP-LAW-UNSELECTED
```

The candidate is not terminal and none of these words may be strengthened by
a reviewer. The disclosed #55 no-artifact refusal and #56 whitespace-only
repair are part of the review target.

## Independence contract

Three seats are mandatory. Each reviewer must:

1. receive this protocol, the immutable target paths, the v16 runbook, and the
   relevant antecedents;
2. work read-only and make no repository mutation;
3. not read, request, summarize, or infer either other review before freezing
   their own report;
4. rebuild load-bearing claims independently rather than treating passing
   receipt gates as proof;
5. state exact disagreements, counterexamples, and scope corrections;
6. grade `ACCEPT`, `ACCEPT-WITH-FIXES`, or `REJECT`; and
7. end with a numbered repair/kill list and a SHA-256 of the report.

Reports are frozen separately as:

```text
v16/review-ovg-operator.md
v16/review-ovg-rewrite.md
v16/review-ovg-physics.md
```

No seat may edit candidate bytes or turn an unconstructed object into a
philosophical assumption. A proof, exact counterexample, or independently
typed physical objection outranks a preference.

## Seat O — operator algebra, instruments, and representation

This seat must independently rebuild the complete exact operator result. It
must not import the scorer as its only computation.

### Mandatory recomputations

1. Reconstruct both three-qubit CNOT orders and verify or refute
   `A^dagger B=CNOT(A->C)`.
2. Compute `K^dagger K` directly for `a=3/5,b=4/5` and
   `a=3/5,b=4i/5`; determine whether the former fails and the latter equals
   identity for every input.
3. Prove or refute, for common-boundary isometries,
   `K_+=(A+B)/2,K_-=(A-B)/2` and
   `K_+^dagger K_+ + K_-^dagger K_-=I`.
4. Re-derive the general two-history multiport equation
   `S I+C Omega+conjugate(C)Omega^dagger=I`.
5. Audit the single-unitary-port theorem. In particular test:
   - whether three distinct eigenphases always force `(Re z,Im z,c)=0`;
   - whether exactly two phases always leave a nonzero `z` direction;
   - the sign and modulo convention in
     `arg z=-(phi_1+phi_2)/2 mod pi`;
   - whether a formal `(z,c)` direction always lifts to actual nonzero
     coefficients `a,b`; and
   - scalar/projectively proportional edge cases and degeneracies.
6. Independently certify all five phase/multiplicity rows. Determine whether
   annihilator plus trace moments is an adequate finite certificate here.
7. Rebuild the nonnormal `C^2 -> C^4` overlap and solve its full real-linear
   operator equation. Attack any use of eigenvalues outside the unitary case.
8. Rebuild the three-history family and its screens. Decide whether an exact
   implicit polynomial equation plus a positive-dimensional embedded family
   licenses the headline “variety constructed,” or only “a subvariety and
   witnesses constructed.” This wording question is load-bearing.
9. Verify that the real and imaginary port decompositions have the same
   unconditioned channel but different calibrated branch maps. Distinguish
   Kraus rotations, physical instruments, and record-individuated histories.
10. Audit complete positivity, trace preservation, affinity, ancilla stability,
    and the fixed-spectator no-signalling inference. Look for any one-state
    normalization hidden in an all-input claim.
11. Rebuild seals, claim occurrence counts, 30 mutation bindings, transcript
    equality, and true off-tree reproducibility.

### Mandatory attacks

- Is the phase census merely a bounded `Q(i)` witness while the paper states a
  theorem over all complex coefficients? If so, is the prose proof complete?
- Does “coherent” exclude `z=0` consistently in machine and paper?
- Are scalar relative operators one history up to phase as operators but still
  configuration-distinct events? What additional calibration decides?
- Does the canonical flag dilation prove only mathematical existence, or does
  any claim silently promote it into physical output records?
- Can a different number of ports or non-isometric histories evade or enlarge
  the stated strata?
- Does the paper distinguish an implicit solution variety from a solved
  irreducible-component/moduli classification?

## Seat R — relational rewriting, concurrency, and primitive arity

This seat attacks whether the operator histories are lawfully typed relational
histories and whether any arity statement is licensed.

### Mandatory recomputations

1. Rebuild all four rewrite critical pairs from the data, including both
   orders and final token sets.
2. Check that `AB` and `BC` are overlapping actor supports but both CNOT order
   composites really share independently typed source and final carriers.
3. Decide whether the operator common boundary is joined to a relational
   common future or merely declared by equal matrix dimension. Reuse Papers 3
   and 4's pullback/bundle distinctions exactly.
4. Verify all length-at-most-four binary factorization words for both order
   maps. Explain identity-padding/relation effects and whether the existence,
   not the count `5`, is the physical point.
5. Rebuild the Toffoli nonlinearity witness and prove or refute impossibility
   under arbitrary-length CNOT-only circuits. Audit the stated ancilla-zero /
   ancilla-return policy rather than accepting its mere presence in JSON.
6. Test relabeling covariance and an idle spectator at the rewrite and operator
   levels. Note any pin requirement not actually implemented.
7. Separate four cases exactly: lower-arity composite, named fusion, primitive
   generator irreducible in the frozen grammar, and ontology-level indivisible
   event. Decide which the candidate earns.
8. Attack the local flag claim. Assigning a factor to actor `B` may be catalogue
   metadata, not relational locality. State the minimum event-grammar or
   reachability theorem needed for local implementation and durable recording.
9. Determine whether delete/use is correctly called a dependency and whether
   divergent endpoints are merely untyped at that cut. Neither may be called a
   record without a permanence census.
10. Attempt the first genuine extension: three overlapping binary generators
    or two overlaps sharing different actors. Identify exactly why the current
    fixture is not an arbitrary-`n` theorem.

### Mandatory attacks

- Can the coherent CNOT sum be phrased as two configuration-individuated ISP
  histories, or only as two circuit decompositions on a fixed carrier?
- Does event-order composition add a hidden micro-time or fixed background that
  conflicts with the intended indivisible back-reacting successor ontology?
- Is the graph grammar operationally used by the matrices, or does the scorer
  run an operator fixture and a token-rewrite fixture alongside each other?
- Does “primitive arity not forced” survive allowed catalogue enlargement and
  ancillas? Does any positive primitive-arity control say anything about ISP's
  selected law?
- Which additional overlap/gluing/associativity/cocycle gates are necessary
  before a two-to-`n` closure can be stated?

## Seat P — quantum causality, EPR, gravity/QFT, and ontology

This seat audits physical meaning, literature, and every refused promotion.

### Mandatory recomputations and literature checks

1. Rebuild the spectator density matrix, complete channel, partial trace, and
   amplifier contrast. State its exact scope: fixed tensor factor,
   unconditioned operation, one entangled preparation versus the general
   all-input theorem.
2. Determine what remains of the EPR/steering problem. In particular, does the
   candidate construct remote steering, conditional records, a changing Bob
   algebra, or only an idle fixed spectator?
3. Consult primary literature on process matrices, quantum switches, and
   causal-nonseparability witnesses. Verify that the candidate correctly
   refuses those claims and that its cited references support the distinction.
4. Decide whether a class-operator sum of two definite circuit orders has any
   operational preparation/implementation in the frozen relational grammar.
   Mathematical completeness alone may not make it a physical process.
5. Audit the ontology: one actual relational history, coherent alternatives,
   port records, the separate actualization postulate, and the absence of
   record permanence for the new flag. Identify any contradiction with the
   Paper 3 event-algebra doctrine.
6. Search for genuine backreaction. Does any relation rewrite alter a later
   probe through the output geometry with nonfactorizing matter/geometry
   response, or are the quantum and token-rewrite controls still neighboring
   fixtures?
7. Audit all claims concerning fields, Fock structure, particles, species,
   exchange statistics, Hamiltonian reconstruction, Lorentz symmetry,
   continuum gravity, and QFT/GR deviations. Every promotion requires its own
   constructed object and calibrated discriminator.
8. Check whether the phase constraint could be mistaken for exchange
   statistics, spin-statistics, a coupling constant, curvature, or a
   Hamiltonian phase. Require explicit refusal where needed.
9. Compare the result with Barandes-style indivisible stochastic processes
   without assuming fixed spacetime. State whether the history-level operator
   law is ontology or still only representation in this extension.
10. Audit the paper for source accuracy, terminology, arithmetic readability,
    and any statement stronger than the sealed machine object.

### Mandatory attacks

- Does the fixed-carrier CNOT fixture answer the user's back-reacting local
  spacetime question, or only one quantum-overlap algebra question?
- Does the local flag simply reintroduce a measurement apparatus/catalogue by
  declaration?
- Is “overlap law unselected” the real primary physical result, with the
  mathematical classifier subordinate?
- What empirical observable, if any, differs from ordinary quantum circuits?
  If none is fixed across the surviving law family, every QFT/GR deviation
  claim must remain refused.
- Are the paper's causal-order citations primary, correctly scoped, and
  accurately dated/titled?

## Required report structure

Every report must contain, in order:

1. immutable-target/hash audit;
2. independent method and tools;
3. exact recomputation table with candidate value, reviewer value, and status;
4. theorem/proof audit;
5. representation and ontology audit;
6. counterexamples and unrun controls;
7. consequence/scope reclassification;
8. grade;
9. numbered repairs or kill conditions; and
10. report SHA-256.

“The script passes” is never an adequate recomputation. A seat may reuse exact
fixture data but must rebuild the inference.

## Adjudicator decision order

After all three reports are frozen, the adjudicator must answer in order:

1. Are the candidate hashes and exact numbers reproduced?
2. Is the non-scalar CNOT complex-weight counterexample valid?
3. Is the single-port spectral theorem valid over the stated complex/unitary
   scope, including phase sign and coefficient lifting?
4. Does the headline mean the full implicit Gram/instrument variety exists,
   or overclaim a solved/global variety?
5. Are the operator order histories physically typed relational alternatives,
   or only fixed-carrier circuit decompositions?
6. Do parity ports establish mathematical existence only, or a licensed local
   record mechanism?
7. Is the binary-composite/minimum-arity refusal valid? What does the Toffoli
   sensitivity control add and not add?
8. Are dependency, divergent boundary, record, permanence, and actualization
   kept separate?
9. Is fixed-spectator no-signalling stated at its exact scope, with steering
   and changing subsystems open?
10. Are causal nonseparability, all-`n`, backreaction, Hamiltonian, fields,
    particles, QFT, GR, and deviations correctly refused?
11. Which machine words survive unchanged, which require qualifiers, and which
    are killed?
12. What bounded repairs, new falsifiers, and terminal wording are ordered?

## Kill hierarchy

The following are immediate major findings if established:

- an exact counterexample to the single-port spectral theorem;
- a failure of all-input completeness for the advertised CNOT or parity maps;
- a nonnormal row classified using the unitary shortcut;
- the same physical fixture represented twice while being called two
  configuration-individuated histories without a relational calibration;
- “variety constructed” requiring a decomposition/classification the candidate
  never computes;
- a binary product called primitive or a CNOT-only control promoted to ISP's
  actual minimum arity;
- a formal flag called local implementation or durable record;
- order interference promoted to a quantum switch/causal nonseparability;
- fixed-spectator no-signalling promoted to conditional steering or changing-
  carrier locality;
- any backreaction, field, particle, Hamiltonian, QFT, GR, or empirical
  deviation claim without its missing object; or
- any candidate byte, review, or scope wall moved before adjudication.

The strongest possible review outcome remains finite and conditional. Even a
fully accepted OVG candidate selects neither the elementary successor law nor
its port weights and does not complete the unified quantum-gravity theory.
