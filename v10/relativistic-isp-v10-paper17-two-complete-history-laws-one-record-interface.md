# Relativistic ISP / SHARD V10 Paper 17

# Two Complete History Laws at One Sealed-Record Interface

**Status:** final at the fixed-carrier finite-generator boundary after D21
hostile audit and repair, 2026-07-12.

## Abstract

V10 Paper 16 proved that an action and finite lower-order evidence need not
select a complete history law.  This paper performs the next constructive
step.  On one source region with three spacelike sealed-record outputs, it
builds two inequivalent but complete finite instrument generators.  Candidate
Q retains the coherent GHZ regional boundary state.  Candidate C applies an
objective hard-seal selection channel before the same local record
instruments.  Both candidates supply every joint probability and every
positive next-record conditional without a global commit order.

An exact Gaussian-rational receipt verifies positivity, normalization,
spacelike commutation, construction-order gauge, no-signalling, decoherent
outcome records and complete conditionalization.  The candidates agree on all
37 proper-support Pauli observables, every one- and two-record marginal and
the full computational-record law.  They nevertheless differ on the
preregistered complete-support observables: `XXX` is `1` versus `0`, and the
Mermin combination is `4` versus `0`.  The interpolation `rho_eta` proves
`<M>=4 eta` while every proper reduced state is `eta`-independent.

Existing multipartite experiments already exclude the parameter-free claim
of complete microscopic hard-seal dephasing.  They do not select a unique
unitary or scale-dependent objective-collapse cosmology.  The surviving
physical discriminator is an independently calibrated mass–separation–time–
factor ladder of residual complete-history coherence.  Because both packets
use a fixed carrier and supplied source, neither licenses a round-cone, 3+1,
gravity or `G` prediction.

## 1. The promoted question

D19 exhibited abstract history laws with identical one/two-record statistics
and different triple statistics.  It did not produce physical instrument
generators.  D20 therefore required at least two complete candidates at one
observable interface.

Here “complete” is explicitly domain-relative.  A D21 packet is complete for
the declared finite carrier and intervention alphabet if it specifies:

```text
source state/process;
all allowed local instruments;
all joint outcome probabilities;
all positive-past conditionals;
the durable record sector;
the causal quotient of arbitrary evaluation order.
```

This is not cosmological completeness.  Carrier birth, a continuum or
profinite extension, matter content, gravity, physical units and a universal
record map are outside the frozen domain.

## 2. Common causal record interface

A source `S` precedes three pairwise spacelike regions `A,B,C`.  Each region
chooses `X`, `Y` or `Z` and seals a binary outcome.  Local effects are

```math
Pi_a^x={I+a sigma_x\over2}.
```

For state `rho`, the complete finite law is

```math
P_rho(a,b,c|x,y,z)=
Tr[rho(Pi_a^x tensor Pi_b^y tensor Pi_c^z)].
```

The effects on different factors commute.  Thus all six serializations of
the three spacelike instruments represent the same joint event.  Given any
positive already-recorded event `R`, the next-record law is

```math
P(next|R)={P(R and next)\over P(R)}.
```

No universe-wide clock or second dynamical lottery is introduced.

## 3. Candidate Q: coherent regional history

Candidate Q begins from `|000>`, applies a Hadamard in the source region and
then the two carrier interactions `CNOT(A->B)` and `CNOT(A->C)`.  The exact
receipt reconstructs the resulting state

```math
rho_Q={1\over2}(|000>+|111>)(<000|+<111|).
```

It has rank one and purity one.  The source alternatives remain coherent
until the declared local instruments correlate them with orthogonal outcome
registers.  The resulting complete outcome histories form a positive
decoherent record sector.

Q is an exact finite unitary/decoherent-history packet.  Its source interaction
circuit is supplied rather than derived from sealed records.  The later
spacelike records share that interacting source but do not dynamically act on
one another.

## 4. Candidate C: objective hard seal

Candidate C applies

```math
Delta_Z(rho)=sum_s P_s^{Z,A} rho P_s^{Z,A}
```

to the Q source, yielding

```math
rho_C={1\over2}(|000><000|+|111><111|).
```

The source selection variable is objective and stochastic, with the two
branches weighted equally.  The executable prints both `1/2` branch weights,
the conditional states `|000><000|` and `|111><111|`, and their exact
reconstruction of `rho_C`.  C has rank two and purity one half, so it cannot
be related to Q by a unitary basis change, relabeling or construction gauge.
The downstream instrument interface is otherwise identical.

C is intentionally the parameter-free hard-seal endpoint.  It is not
promoted to GRW, CSL, Diósi-Penrose or a relativistic flash law.

## 5. Exact common gates

The standard-library executable uses Gaussian rational matrices and passes
`40/40` checks under normal and optimized Python.  It establishes:

- exact Hermiticity, unit trace and nonnegative spectra;
- exact PVM idempotence, orthogonality and completion;
- normalization and nonnegative probabilities for all 27 setting triples;
- exhaustive spacelike local commutation and a six-order rebuild;
- one- and two-site operational no-signalling;
- normalized conditionals for every positive past and every site order;
- diagonal nonnegative decoherence matrices for sealed outcomes.

These are finite operational locality and consistency results.  They do not
provide a relativistic collapse ontology or derive the common source carrier.

## 6. Why every lower shadow agrees

Embed both candidates in

```math
rho_eta={1\over2}(|0^N><0^N|+|1^N><1^N|
 +eta|0^N><1^N|+eta|1^N><0^N|).
```

If any factor is traced out, each off-diagonal term contains `<0|1>=0` and
vanishes.  Every proper reduced state is therefore independent of `eta`.
For three factors this means all 37 Pauli words containing at least one
identity have identical expectations.  D21 verifies the corresponding one-
and two-record probability tables for every local setting.

The full `ZZZ` history law also agrees:

```text
P(---)=1/2, P(+++)=1/2, all other outcomes=0.
```

Consequently every positive next-record conditional asked solely in that
record basis agrees.  Looking harder at the same lower shadows cannot reveal
the missing coherence.

## 7. The preregistered identifying question

Complete-support coherence survives as

```math
<X tensor ... tensor X>=eta.
```

At three records,

```math
P_eta(a,b,c|XXX)={1+eta abc\over8}.
```

Q has only positive-parity outcomes; C is uniform.  Conditionalizing on two
positive X records, Q assigns probability one to a positive remaining record,
whereas C assigns one half.  The regions are spacelike, so this is a joint-law
conditional and not a causal influence or physical time ordering.

The frozen Mermin operator

```math
M=XXX-XYY-YXY-YYX
```

gives

```math
<M>_eta=4 eta,
```

and hence `4` for Q and `0` for C.  This is a multipartite complete-support
correlator, not Sorkin third-order interference and not yet a literal SHARD
Wilson-loop holonomy.

## 8. Empirical disposition

Three-photon GHZ experiments observe nonzero multipartite coherence and
Mermin violations.  A strict-locality experiment reported `2.77 +/- 0.08`
against the local bound `2`, fair-sampling assumed
([Erven et al.](https://www.nature.com/articles/nphoton.2014.50)).  The
parameter-free microscopic C endpoint, which predicts zero for this ideal
complete-support combination, is therefore not a viable universal record law
at the photon/qubit scale.

This does not prove Q is the universe's final law.  Physical collapse models
are normally weak and scale dependent.  A general operational interpolation
has

```math
eta_phys=exp[-Gamma(model; M,Delta x,T,...)],
```

while ordinary environmental and control noise also suppress visibility.
`Gamma` and its coefficients must come from a named generator and must be fit
outside the holdout.  Current collapse experiments constrain parameter
regions; they do not identify a unique alternative law.

## 9. The admissible future experiment

The cross-rulebook question is now precise:

> Does independently calibrated conventional open-system dynamics exhaust
> the loss of complete-history coherence, or is there residual irreversible
> suppression with a separately predicted mass, branch-separation, dwell-time
> and factor-number dependence?

The experiment must first freeze a concrete unitary environment packet and a
concrete collapse packet.  Multi-time/process-tensor controls should diagnose
environmental memory.  Parameters must be calibrated on separate data.  Only
then may blind scale points be queried with complete-support parity or Mermin
observables.  Overlapping predictions give bounds; separated predictions can
select between the two printed packets.

## 10. Geometry and fundamental-law boundary

Neither candidate grows its causal carrier.  Neither specifies a metric,
matter sector, scale dictionary, `G`, or continuum/profinite extension.
Therefore neither prints `F`, effective dimension, a cone scale ladder or a
gravity prediction.  Unit conversion cannot supply these missing dynamics,
and using the V9 builder would import an independently unselected law.

The D20 full objective remains open.  D21 supplies the first generator-level
finite discriminator and eliminates one deliberately sharp endpoint; it does
not supply two complete cosmological generators or untouched evidence.

## 11. Conclusion

Two complete finite universes can share every proper record shadow and every
ordinary computational-basis click while disagreeing on a complete-history
phase question.  Nature has already answered the sharp microscopic version:
coherence survives enough to reject immediate total hard-seal dephasing.

The remaining useful question is a scale question, not another selector
slogan.  A viable rival law must specify how residual complete-history
coherence varies with physical mass, separation, duration and factor number,
after conventional memory and noise are independently fixed.  Until such a
packet and untouched comparison exist, the honest verdict is

```text
FINITE-COMPLETE-RULEBOOK-DISCRIMINATOR — PROVED;
UNIQUE PHYSICAL RULEBOOK — NOT SELECTED.
```
