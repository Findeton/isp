# Relativistic ISP v10 Paper 9: A Complete Sealed Causal Instrument Rewrite Rulebook

## Finite primitive interaction data, local opportunity birth, quantum sealing, construction-order gauge, projective full-history measure, non-explosion, and the diffusion shadow of the V9 geometry builder

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** D8 complete-compressed rulebook, 2026-07-11.  The D8 gates and
independent construction were frozen before the D8 literature search.  This
paper claims a complete finite generative specification, not a parameter-free
derivation or empirical identification of nature's coupling packet.

**Exact receipts:**

- `v10/code/d8_scir_exact.py` — 101/101 exact/high-precision checks;
- `v10/code/d8_scir_diffusion_shadow_exact.py` — 19/19 exact/high-precision
  checks;
- `v10/code/d8_scir_v9_shape_replication.py` — fresh 24-seed strict V9 shape
  replication against a SHA-256-pinned V9 source.

## Abstract

V10 Paper 8 proved that SHARD's existing consistency principles do not select
a unique interacting extension law.  This paper answers the stronger
constructive demand: give a complete rulebook anyway, while exposing rather
than disguising the new physics it requires.

The rulebook is the **Sealed Causal Instrument Rewrite** system, SCIR.  Its
primitive data are finite: oriented record-port types and finite state spaces;
one root package/state; a finite local rewrite grammar; and one finite local
unitary/instrument packet per rewrite type.  The grammar creates candidate
opportunity tokens locally.  Each token carries an independent unit
exponential threshold in integrated local evidence/hazard.  When the token
fires, its local Kraus instrument supplies Born outcome weights, consumes its
owned ports exactly once, commits a pointer/seal record, and emits the next
finite opportunity tokens.  Disjoint tokens are genuinely concurrent;
overlapping tokens share a port and acquire physical order.

This supplies every field missing in Paper 8: root, candidate scope,
continuation, multileg bridges, null survival, numerical outcomes, pre-seal
interference, commitment, provenance, and off-support grammar.  It contains no
observable universe clock.  Products of commuting disjoint operators descend
from arbitrary sampler order to one marked causal history.  Instrument
completeness gives finite-cylinder projectivity.  Bounded opportunity tokens
per port, bounded local hazard, and bounded output imply non-explosion by a
harmonic comparison.  Local trace-preserving instruments give operational
no-signalling while conditioned seals retain Bell-type correlations.

The previously free V9 objects acquire precise status.  Shared-evidence
allocation `c` is not an additional scalar once the local quantum instrument
is supplied; its outcome allocation is the instrument's Born shadow.  The
transfer `g` is a genuine coupling in the local instrument, analogous to an
interaction angle or rate, and must be declared or measured.  A conservative
partial-transfer instrument has exactly the continuous fractional-leak shadow
that made V9 cones substantially less anisotropic.  At `g=9/50`, the exact
shadow preserves every channel, contracts a pair difference by `16/25`,
propagates influence through locally recorded transfers, and obeys a
memoryless leak semigroup.

A fresh 24-seed rerun of the frozen V9 `g=0.18` builder gives
`F_dom=1.20636 +/- 0.01486` (`t=-1.994`, failing the strict `-2.33` bar) and
`F_m4=1.17254 +/- 0.00999` (`t=-3.950`, passing strongly), with dimension-2
refusals and `S_4` witnesses on 24/24 seeds.  The pinned dimension proxy reads
4.486 but remains instrument-suspect and is excluded from grading.  Thus the
SCIR diffusion shadow remains geometrically promising, not validated.

The primary literature contains close predecessors for every mathematical
component—quantum causal histories, quantum Petri nets, stochastic rewriting,
relativistic flash processes, and quantum causal graph dynamics.  SCIR is a
SHARD-specific assembly.  Its result is nevertheless substantive: SHARD now
has a complete executable rulebook schema whose irreducible primitive content
is no longer an arbitrary law on all histories, but a finite local interaction
packet, exactly the normal status of a Hamiltonian/Lagrangian and its measured
couplings.

## 1. What has been found

The rulebook is not a single universal number.  It is the finite specification

$$
\mathfrak R=
(\mathcal T,\{\mathcal H_t\},R_0,\mathcal G,
\{U_r,P_{r,o},\lambda_r\}_{r\in\mathcal G}).
$$

Given this packet, the probability of every finite committed record history
and the conditional law of every next licensed extension are determined.

This is `COMPLETE-COMPRESSED` in Paper 8's success ladder:

```text
complete:
  every generative case has a rule;

compressed:
  the primitive data are a finite type/rule/coupling table, not one number
  for each possible history;

not parameter-free:
  the local interaction types and couplings are physical input;

not empirically identified:
  the exact packet used by nature remains to be measured/reconstructed.
```

Physical theories ordinarily do not derive their particle content and all
couplings from covariance.  SCIR puts SHARD in the same honest position.

## 2. Primitive data

### 2.1 Typed finite ports

`T` is a finite set of oriented channel/port types.  It includes a declared
compatibility or dual operation.  Every `t` has a finite-dimensional state
space `H_t` and a finite record-capacity declaration.

Ports are not spatial directions in a prior manifold.  They are incidence
and interaction interfaces.  A derived geometry may later interpret stable
families of them as direction, matter, charge, or gauge channels.

### 2.2 Root package

`R_0` contains one finite root record, initial state `rho_0`, and its finite
exposed ports.  The empty history has exactly one allowed non-null extension:
commit `R_0`.  Afterward, the physical universe is one connected record
component.

The root is a boundary condition.  SCIR does not claim that “nothing” causes
itself.  This closes the empty-history bootstrap without a hidden immigration
oracle.

### 2.3 Finite local rewrite grammar

`G` is a finite collection of rule types.  Each `r` declares:

```text
a finite connected incoming collar I_r;
typed ports and factors consumed exactly once;
a finite output record packet O_r;
new exposed ports and opportunity tokens;
conservation/compatibility predicates;
a finite pointer/outcome set.
```

The grammar is generative: when one committed extension produces a matching
local collar, it creates a token naming that candidate.  The theory never
searches every tuple of old records for a possible interaction.

### 2.4 Local quantum packet

For each rule, a finite local unitary or unitary semigroup `U_r` acts on the
incoming collar plus a fresh finite ancilla.  A complete pointer family
`{P_{r,o}}` gives local Kraus operators

$$
M_{r,o}=P_{r,o}U_r(\,\cdot\otimes|0_r\rangle),
\qquad
\sum_oM_{r,o}^\dagger M_{r,o}=\mathbf1.
$$

The entries/couplings in `U_r` are primitive measurable physics.  Covariance
constrains their typed form but does not determine their values; the V6 and D7
no-go theorems forbid saying otherwise.

### 2.5 Local hazard/exposure

Each token has a nonnegative locally computed hazard `lambda_r` along an
intrinsic collar parameter.  Equivalently, it accumulates integrated exposure

$$
I_\nu=\int\lambda_\nu ds_\nu.
$$

This parameter is evidence/hazard, not seconds and not a global present.

## 3. The complete generative algorithm

### Rule 0 — root

At the empty history, commit `R_0` with probability one.  Create the finite
opportunity tokens declared by its output grammar.

### Rule 1 — local survival

At token creation, associate

$$
X_\nu\sim\operatorname{Exp}(1).
$$

Before exposure `I`, the token's null/no-fire probability is

$$
S_\nu(I)=e^{-I}.
$$

This is the V8/V9 renewal law in its proper role: it acts only after the
grammar creates an opportunity.

### Rule 2 — local competition

Disjoint tokens accumulate independent local exposure and need no physical
relative order.  Tokens sharing a consumed port are causally comparable on
that port.  The first local threshold crossing consumes the port and disables
incompatible alternatives.  Continuous thresholds make exact ties null.

### Rule 3 — quantum outcome

When token `(r,m)` fires at collar state `rho`, outcome `o` occurs with

$$
p(o|r,m,\rho)=
\operatorname{tr}(M_{r,o}\rho M_{r,o}^\dagger).
$$

The normalized corresponding state is retained on the output collar.

### Rule 4 — seal and birth

Commit one typed extension package containing:

```text
rule and token identity;
all incoming collar IDs;
the physical causal orientation;
pointer outcome o;
the retained RN/holonomy factor;
consumed-port ownership;
new output ports/tokens and provenance.
```

The pointer outcome is durable.  Alternatives may interfere before this
record, while committed outcomes are exclusive afterward.

### Rule 5 — concurrency quotient

If multiple disjoint tokens fire without a causal relation, commit the set as
one concurrent package or any auxiliary linearization thereof.  The physical
history stores no relation between those events.

These five rules plus the root define the complete history law.

## 4. How records actually create the web

Every new record consumes an explicitly named incoming collar and emits a
finite output collar.  Therefore records cross into a spacetime web in three
ways:

1. **Continuation:** one incoming lineage produces a later record.
2. **Branching:** one collar produces multiple outgoing opportunity tokens.
3. **Interaction:** a multileg token whose collar was already jointly recorded
   consumes two or more branch ports and produces a common future record.

No record searches the universe for a distant partner.  Branches interact
only when a chain of prior records has brought their compatible ports into one
licensed boundary token.  “Spatial meeting” is eventually a stable pattern of
this record routing; it is not a primitive coordinate test.

The root-connectivity choice resolves the earlier disconnected-component
question.  Independent mathematical universes do not later join.  Apparently
separated physical branches inside one universe retain common-root ancestry
and may exchange explicit carrier tokens.

## 5. Construction-order theorem

Consider two enabled extensions `a,b` with disjoint consumed ports, disjoint
token IDs, and local Kraus operators acting on tensor factors `A,B`.  Then

$$
(M_a\otimes\mathbf1_B)
(\mathbf1_A\otimes M_b)
=
(\mathbf1_A\otimes M_b)
(M_a\otimes\mathbf1_B).
$$

Their independent survival factors also multiply commutatively.  Hence both
linear extensions have the same branch operator, probability, output state,
and canonical record history.

When tokens overlap, their operators need not commute and consuming one token
changes the other's domain.  Their order is then physical and is stored.

The 101-check receipt verifies both sides exactly: disjoint two-qubit
operations commute and produce identical states; two qutrit operations sharing
one collar do not commute and produce different normalized states.

## 6. Projective full-history measure

For a finite causal history choose any linear extension.  Multiply its local
survival factors and causal-order Kraus operators, then apply the Born trace to
the root state.  Section 5 makes the result independent of swaps of concurrent
events, so it descends to the partial-order history.

Summing terminal pointer alternatives uses

$$
\sum_oM_{r,o}^\dagger M_{r,o}=\mathbf1
$$

and exactly recovers the parent cylinder.  Iterated terminal deletion gives a
consistent family of finite-cylinder laws.  The non-explosion theorem below
prevents infinitely many births in finite intrinsic exposure.  Standard
extension of the consistent cylinders therefore supplies a full-history
measure `mu_R`.

Thus SCIR constructs rather than merely posits the D7 path measure.

## 7. Non-explosion theorem

Assume:

```text
at most M active tokens contain any exposed port;
every token hazard is at most lambda_max;
each committed extension emits at most B ports.
```

With `n` exposed ports, total hazard is at most

$$
M\lambda_{\max}n.
$$

After `k` births the port count is at most `n_0+Bk`.  The comparison holding
times have divergent sum

$$
\sum_{k\ge0}
\frac{1}{M\lambda_{\max}(n_0+Bk)}=\infty.
$$

Therefore the bounded local grammar is nonexplosive.  The exact receipt
certifies twelve dyadic blocks with common positive lower bound `1/4` after
removing the fixed prefactor.

This theorem is load-bearing.  If every `k`-tuple of old records were scanned
for bridges, the total hazard could grow superlinearly and permit explosion.

## 8. Quantum correlations without signalling

The exact Bell-state witness applies a complete pointer instrument on record
`B`.  Each recorded outcome occurs with probability `1/2` and perfectly
predicts the corresponding `A` pointer.  If the `B` result is unobserved, the
reduced `A` state remains exactly `I/2`.

Therefore SCIR distinguishes:

```text
conditioned correlation:
  permitted and retained by the joint sealed history;

unconditioned influence across a disjoint collar:
  absent by trace preservation;

Bell-local hidden variables:
  not assumed for the pre-seal quantum state.
```

This is the correct relativistic target at the pregeometric level.

## 9. What happened to c, g, K, and b?

### 9.1 Shared allocation `c`

There is no independent universal scalar `c`.  Once the multileg local
instrument is supplied, shared outcome allocation is

$$
p(o)=\operatorname{tr}(M_o\rho M_o^\dagger).
$$

Different interactions can have different allocation structures because they
have different physical instruments.  A single global `c` was a convenient
V9 builder compression, not fundamental ontology.

### 9.2 Transfer `g`

`g` is genuine local coupling data.  In a partial-transfer realization it is
an emission probability or a function such as `sin^2(theta)` of a unitary
interaction angle.  Memorylessness gives the continuous semigroup form

$$
g(s)=1-e^{-\gamma s}.
$$

The shape is fixed; the rate/coupling `gamma` is measurable physics.  SHARD's
structural axioms do not determine it.

### 9.3 `K`

No universal face-size constant `K` is fundamental.  Finite record capacity
and the grammar bound local ports and rule arity.  The number of effective
facets/directional clocks at a macroscopic scale is generated by the spectrum
and state of active port channels.

### 9.4 Global build order `b`

`b` is a sampler gauge for concurrent records.  Each lineage has its own
causal record order and exposure.  A global linear extension can be used in
code but is absent from the physical history.

## 10. Exact diffusion shadow and V9 geometry

For a victim content vector `v`, receiver `r`, and transfer `g`, the classical
diagonal shadow of a conservative emitted packet is

$$
v'=(1-g)v,
\qquad
r'=r+gv.
$$

It preserves each channel exactly.  A symmetric partial swap gives

$$
v'=(1-g)v+gr,
\qquad
r'=gv+(1-g)r,
$$

and contracts their difference by `1-2g`.

At the V9 protocol value `g=9/50`, the exact contraction is

$$
1-2g=\frac{16}{25}.
$$

This supplies a physical reason for the V9 jump/leak result.  A destructive
reset creates a macroscopic discontinuity.  Repeated weak local transfer
instruments generate continuous diffusion while conserving total content and
propagating disturbances between records.

The 19-check receipt proves exact channel, monopole, and dipole conservation;
the semigroup identity to 110-digit precision; commutation of disjoint
transfers; physical order of overlapping transfers; and expansion of a marked
influence from one to eight slots through recorded local tokens.

### 10.1 Fresh 24-seed result

The new wrapper verifies the frozen V9 source hash

```text
aff9525110f6fd209332badccf1a5353c011be9eb8461a4db50063bf0670d81a
```

and changes only the ten-seed range to 24 fresh seeds.  Against the stricter
`t <= -2.33` threshold in both conventions:

| measurement | mean | SE | standardized value | strict result |
|---|---:|---:|---:|---|
| `F_dom` | 1.206359972 | 0.014863056 | -1.994208 | fail |
| `F_m4` | 1.172542400 | 0.009990490 | -3.949516 | pass |

Every seed refuses dimension two and contains a verified `S_4` witness.  The
pinned dimension proxy reads 4.486459, but D7's nonstationarity diagnosis
still applies; it is printed and excluded from the verdict.

This result does not refute SCIR.  It says one phenomenological SCIR shadow at
one coupling does not yet pass the strict two-convention geometry protocol.
The `m4` leg is highly significant, while the `dom` leg remains suggestive.

## 11. Literature comparison

SCIR assembles known structures:

1. [Quantum Petri Nets](https://arxiv.org/abs/2508.14531) already combine
   quantum valuation, local transitions, true concurrency, unfolding, and
   composition.
2. [Quantum causal histories](https://arxiv.org/abs/hep-th/0302111) assign
   finite event algebras and completely positive maps to a locally finite
   causal pre-spacetime.
3. [Relativistic interacting GRW flashes](https://arxiv.org/abs/2002.00482)
   construct a normalized joint flash POVM and prove admissible-order
   independence from commuting spacelike operators.
4. [Stochastic rewriting](https://arxiv.org/abs/2003.09395) supplies finite
   structural rewrite rules with CTMC semantics.
5. [Quantum causal graph dynamics](https://arxiv.org/abs/1607.06700) proves
   localization of unitary causal dynamics on time-varying quantum graphs.
6. Causal-set cosmic renormalization reaches a line, not one point, of
   transitive-percolation fixed laws:
   [Martin–O'Connor–Rideout–Sorkin](https://arxiv.org/abs/gr-qc/0009063).

No component-level originality is claimed.  SCIR's contribution is the exact
SHARD closure assignment: which established object fills each previously
missing rulebook field, and which remaining numbers must be admitted as local
physical couplings.

## 12. Why this is not “just posit mu”

A primitive arbitrary history measure assigns an independent functional over
an enormous history space.  SCIR instead supplies:

```text
finite types;
finite local rewrite rules;
finite local matrices/couplings;
one root state;
bounded local hazard.
```

Every long-history probability is computed by repeated local composition.
The compression is physical: changing one local coupling changes an infinite
family of histories coherently.  Construction-order gauge, projectivity, and
no-signalling can fail for an arbitrary `mu` but are theorems of the SCIR
packet when its gates hold.

## 13. Claim boundary

### Established here

```text
one complete root-to-history generative algorithm;
finite primitive description rather than full-history lookup;
explicit local creation of candidate scope;
explicit connected multileg interaction;
null survival and local timing;
quantum outcome and durable seal;
construction-order gauge for disjoint events;
projective cylinder laws;
operational no-signalling;
bounded-grammar non-explosion;
exact conservative diffusion shadow;
fresh downstream geometry replication.
```

### Not established

```text
that the particular finite grammar/couplings used by nature are known;
that covariance derives those couplings;
that the V9 g=0.18 shadow passes the strict two-convention shape standard;
that the current dimension instrument is stationary;
that Standard Model and gravitational sectors have been reconstructed as one
explicit SCIR packet;
that SCIR is mathematically original.
```

## 14. Final verdict

```text
COMPLETE-COMPRESSED-RULEBOOK-FOUND
+ ROOT-AND-LOCAL-OPPORTUNITY-CLOSED
+ QUANTUM-INSTRUMENT-SEAL
+ EXPONENTIAL-EVIDENCE-TIME
+ CONSTRUCTION-ORDER-GAUGE
+ PROJECTIVE-FULL-HISTORY-MEASURE
+ LOCAL-BOUNDED-NONEXPLOSIVE
+ C-ABSORBED-IN-INSTRUMENT
+ G-IDENTIFIED-AS-PHYSICAL-COUPLING
+ DIFFUSION-SHADOW-GEOMETRICALLY-PROMISING-NOT-YET-VALIDATED
+ NOT-UNIQUE-OR-PARAMETER-FREE
```

The missing rulebook is no longer an unnamed probability measure.  It is a
finite causal quantum rewrite/flash theory.  Its irreducible input is exactly
where physical input belongs: the root boundary, interaction grammar, and
local coupling matrices.  Everything else—candidate ownership, survival,
Born allocation, seal, history probability, concurrency quotient,
projectivity, and no-signalling—is generated from that packet.

