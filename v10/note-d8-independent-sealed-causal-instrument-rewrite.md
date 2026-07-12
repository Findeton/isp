# D8 independent construction ledger — Sealed Causal Instrument Rewrite rulebook

**Frozen:** 2026-07-11, after the D8 gate freeze and internal V1–V10 audit,
before the new external literature search.  No originality claim is made.

## 1. Reduction achieved inside the corpus

The earlier corpus contains three positive results that were never assembled
into a complete birth law:

1. V6's primitive binary modular-defect campaign selects a nonzero normalized
   contrast by stored-work/screen-response balance in the count-dual
   one-channel case.
2. V6's retained-holonomy representation fixes Born squared-modulus weights
   once coherent alternatives and admissible screen isometries are supplied.
3. V8–V9 fix the renewal law in integrated evidence/hazard time: a local
   opportunity carries an exponential unit threshold, so survival after
   exposure `I` is `exp(-I)`.

These results do **not** create an opportunity.  D8 therefore takes the
irreducible remaining physical datum to be the analog of a particle/vertex
content table: a finite typed local rewrite grammar with local pre-seal
couplings.  The candidate below makes that primitive explicit and derives the
rest of the path law.

## 2. Primitive finite data

Call the candidate **SCIR**, the Sealed Causal Instrument Rewrite rulebook.
Its primitive specification is:

$$
\mathfrak R=(\mathcal T,\{\mathcal H_t\},R_0,\mathcal G,
\{U_r,P_{r,o}\}_{r\in\mathcal G}).
$$

### 2.1 Port types

`T` is a finite set of oriented port/channel types with a compatibility or
dual operation.  Each type has a finite-dimensional Hilbert space `H_t` and a
finite record-capacity declaration.

### 2.2 Root

`R_0` is one typed root package, its finite initial state `rho_0`, and its
finite exposed ports.  The empty history admits exactly this root extension;
after it commits, the physical universe is one connected record component.
This is an initial condition, not a claimed derivation of why there is a
universe.

### 2.3 Local rewrite grammar

`G` is a finite set of rewrite types.  A rule `r` specifies:

```text
a finite typed connected incoming collar I_r;
ports/factors consumed exactly once;
a finite output record packet and exposed ports O_r;
conservation/compatibility conditions;
a finite pointer/outcome set;
a fresh opportunity-token construction rule.
```

An enabled match is not found by scanning arbitrary record tuples.  It is
created locally when a committed rewrite emits an opportunity token naming
its finite licensed collar.  Every open port participates in at most `M`
active tokens for a fixed finite grammar constant `M`.

Multileg rules join causal branches only when a committed token or connected
boundary factor already carries all legs.  Branches with no recorded common
collar cannot suddenly interact.  Because the root is connected, this does
not require a law for merging independent universes.

### 2.4 Pre-seal dynamics and pointer

For rule `r`, `U_r` is a finite-dimensional unitary (or a specified local
unitary semigroup) acting on the incoming collar and a fresh finite ancilla.
`{P_{r,o}}` is a complete orthogonal pointer family.  Equivalently, the local
Kraus operators are

$$
M_{r,o}
=
P_{r,o}U_r(\,\cdot\otimes|0_r\rangle),
\qquad
\sum_o M_{r,o}^\dagger M_{r,o}=\mathbf1.
$$

The matrices/couplings in `U_r` are primitive measurable physics.  They are
not described as derived from covariance.  This is the finite analog of
declaring an interaction Hamiltonian.

## 3. Derived local click law

### 3.1 Opportunity creation

The grammar, not a global proposal oracle, creates a finite opportunity token
`nu=(r,m)` when a local output collar matches `I_r`.  The token owns its
candidate scope and all provenance needed to apply the rule once.

### 3.2 Hazard/evidence threshold

At token creation draw an independent unit exponential threshold

$$
X_\nu\sim\operatorname{Exp}(1).
$$

The token accumulates only its record-local integrated exposure

$$
I_\nu=\int \lambda_\nu,ds_\nu,
$$

where `s_nu` is an intrinsic collar/evidence parameter and `lambda_nu` is
computed from the supplied local instrument/state.  The token fires when
`I_nu >= X_nu`.  Consequently

$$
P(\hbox{no fire through }I)=e^{-I}.
$$

The exponential variable may equivalently be integrated out and represented
by this survival law.  It is not a universe clock.

The V6/V8 single-channel modular result fixes the binary fire/not-yet
normalization when the opportunity is a primitive count-dual defect.  It does
not fix `U_r`; that is why the local coupling table remains declared.

### 3.3 Outcome and seal

Conditional on a fire at local collar state `rho`, outcome `o` has

$$
p(o|r,m,\rho)
=
\operatorname{tr}(M_{r,o}\rho M_{r,o}^\dagger).
$$

The post-seal state is the normalized corresponding branch.  The committed
extension stores `r`, the collar/token IDs, `o`, its RN/holonomy factor, and
exactly-once ownership.  Pre-seal amplitudes may interfere; post-seal pointer
records are exclusive.  This is precisely where the classical marked-history
shadow begins.

### 3.4 Null law

For any finite family of disjoint active tokens with exposure increments
`Delta I_nu`, the joint no-fire weight is

$$
\exp\left[-\sum_\nu\Delta I_\nu\right].
$$

Overlapping tokens share at least one consumed port.  Their competition is
ordered on that port's local causal history; firing one consumes the token or
port and disables incompatible alternatives.  Continuous thresholds give
zero probability of an exact tie.  Disjoint firings form one concurrent
package when no physical order relates them.

## 4. No global scheduler

SCIR is fundamentally a law on a causal event structure, not on one total
enumeration.  A computer may choose a linear extension to sample it.

For disjoint enabled tokens:

```text
their threshold variables are independent;
their Kraus operators act on disjoint tensor factors;
their rewrite matches consume disjoint IDs;
their operators commute;
their final marked history is the same under either sampled order.
```

Hence auxiliary order is gauge.  For overlapping tokens the shared port makes
the order a physical recorded relation.

## 5. Projective history law

For a finite sealed history with a chosen linear extension, multiply the local
survival factors and ordered Kraus operators, then apply the Born trace.  Two
linear extensions related by swaps of disjoint events give the same value.
Therefore the value descends to the canonical partial-order history.

Summing over all next pointer outcomes uses

$$
\sum_oM_{r,o}^\dagger M_{r,o}=\mathbf1,
$$

so deleting an unobserved terminal extension recovers the parent-cylinder
weight.  Repetition gives a projectively consistent committed-history measure.

This is a direct construction of the `mu` that D7 said could otherwise be
posited.

## 6. Local finiteness and non-explosion

Let a finite history have `n` exposed ports.  Suppose:

```text
each port participates in at most M active opportunity tokens;
each token has local hazard at most lambda_max;
each firing creates at most B new exposed ports.
```

Then the total hazard is at most `M lambda_max n`, and after `k` births the
port count is at most `n_0+B k`.  The expected holding-time lower comparison
has harmonic sum

$$
\sum_{k\ge0}\frac1{M\lambda_{\max}(n_0+Bk)}=\infty.
$$

Thus the comparison linear birth process is nonexplosive.  This is why SCIR
forbids all-to-all tuple scanning and requires locally emitted opportunity
tokens.

## 7. Relativistic and quantum causality

SCIR's primitive locality is record incidence, not distance.  On disjoint
collars, local trace-preserving instruments commute.  Applying an unobserved
instrument on one collar cannot change the reduced state of a disjoint collar;
conditioning on its recorded outcome may reveal correlations.  This gives
operational no-signalling without Bell-local hidden-variable factorization.

A finite propagation speed, metric, and proper-time conversion must be
measured from the generated record graph.  They are not inputs to `G` or
`U_r`.

## 8. What SCIR fixes and what it declares

| rulebook field | status in SCIR |
|---|---|
| root | one declared finite root package/state |
| candidate scopes | generated by finite local grammar and tokens |
| bridges | finite multileg rules with recorded connected collars |
| null mass | exponential local survival |
| timing | unit exponential in intrinsic integrated exposure |
| outcome probability | Born trace of local instrument |
| pre-seal interference | local unitary/Kraus amplitude composition |
| seal | pointer record committed by firing token |
| ownership | token and consumed-port IDs, exactly once |
| construction order | quotient of commuting disjoint firings |
| projectivity | instrument completeness |
| local finiteness | bounded tokens per port and bounded output |
| port types/grammar | primitive finite physics |
| local unitaries/couplings | primitive finite physics |
| initial root state | primitive boundary condition |

The declared primitive packet is finite.  It does not contain one number for
every history.  SCIR therefore reaches `COMPLETE-COMPRESSED` if the
mathematical gates above survive exact tests.

## 9. Rejected stronger claims

1. Covariance cannot select the grammar or `U_r`; V6's orbit-simplex and
   convex-mixture no-go applies.
2. The modular fixed point selects a primitive binary contrast, not every
   multichannel interaction matrix.
3. Born's rule selects probabilities from supplied amplitudes, not the local
   unitary that creates those amplitudes.
4. Exponential renewal selects survival in supplied exposure, not which token
   exists or its exposure generator.
5. A root boundary is not derived from an empty history.
6. Geometry cannot be used to set the grammar/couplings before downstream
   tests.

## 10. Falsifiers

SCIR fails if any of the following occurs:

```text
linear-extension dependence for disjoint rewrites;
failure of cylinder normalization/projectivity;
signalling under an unobserved disjoint instrument;
unbounded opportunity creation per finite collar;
finite-exposure explosion;
an interaction between collars with no recorded token/path;
inability to represent the V6 retained-holonomy Born screens;
systematic failure of the V9 cone/dimension/scale diagnostics for every
physically plausible finite grammar/coupling packet.
```

The post-freeze literature search must now determine whether SCIR is already
known as a quantum stochastic graph rewrite/event-structure/causal-history
construction, and whether stronger existence or uniqueness theorems close or
invalidate any field.

