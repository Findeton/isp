# D21 investigation — two finite universes and the first identifying question

**Status:** final at the fixed-carrier finite-generator boundary, 2026-07-12.

## Executive result

Two inequivalent finite rulebooks now answer exactly the same sealed-record
questions:

```text
Q  coherent source + local instruments + durable outcome registers
C  objective hard-seal source selection + the same instruments/registers.
```

Both are complete on the declared three-region carrier.  Both are normalized,
positive, no-signalling and independent of the arbitrary order used to
evaluate spacelike instruments.  They agree on all 37 Pauli observables with
proper support, every one- and two-record marginal, the full `ZZZ` record law
and every positive `Z`-basis next-record conditional.

They disagree on the preregistered complete-history question:

```math
<XXX>_Q=1,       <XXX>_C=0,
<M>_Q=4,         <M>_C=0,
M=XXX-XYY-YXY-YYX.
```

The exact executable passes `40/40` checks in normal and optimized Python.

## The two generators

Candidate Q starts from `|000>`, applies a Hadamard at the source and then two
finite carrier interactions `CNOT(A->B)` and `CNOT(A->C)`.  This supplies the
pure regional boundary state

```math
rho_Q={1\over2}(|000>+|111>)(<000|+<111|).
```

Candidate C applies the explicit objective hard-seal channel

```math
Delta_Z(rho)=sum_{s=+,-} P_s^{Z,A} rho P_s^{Z,A},
```

which gives

```math
rho_C={1\over2}(|000><000|+|111><111|).
```

Its objective source variable is explicit: `s=-` and `s=+` each have
probability `1/2`, conditional states `|000><000|` and `|111><111|`, and their
weighted mixture is exactly `rho_C`.

The source circuit contains genuine carrier interactions.  The three later
output records are spacelike correlated descendants; they do not dynamically
act on one another.  Thus this closes a finite interacting-source packet, not
the open law for arbitrary record-record birth and joining.

`rho_Q` has purity `1` and rank `1`; `rho_C` has purity `1/2` and rank `2`.
No unitary basis change, carrier relabeling or construction-order gauge can
identify them.

For local setting triple `(x,y,z)` and outcomes `(a,b,c)`, both answer through

```math
P(a,b,c|x,y,z)=Tr[rho Pi_a^x tensor Pi_b^y tensor Pi_c^z].
```

Every positive past is then conditionalized in the ordinary way.  There is no
second click lottery.

## Exact marginal-blindness theorem

For

```math
rho_eta={1\over2}(|0^N><0^N|+|1^N><1^N|
 +eta|0^N><1^N|+eta|1^N><0^N|),
```

tracing out any one factor kills the off-diagonal terms because `<0|1>=0`.
Thus every proper reduced state is independent of `eta`.  Complete-support
coherence remains:

```math
<X tensor ... tensor X>=eta.
```

At `N=3`, the chosen Mermin convention gives `<M>=4 eta`.  This analytically
explains all exact D21 lower-shadow agreements and shows why no collection of
one- and two-record measurements can estimate `eta`.

The `XXX` outcome law is

```math
P_eta(a,b,c|XXX)={1+eta abc\over8}.
```

For Q, conditionalizing on any two X outcomes fixes the remaining outcome.
For C it remains uniformly random.  Since the three output regions are
spacelike, this is a conditional correlation, not a claim that the first two
physically cause a later click.

## What nature has already answered

Microscopic multipartite experiments observe nonzero GHZ/Mermin coherence,
including spacelike separated tests.  They therefore reject Candidate C's
parameter-free claim that record formation immediately and completely
dephases microscopic alternatives.  Candidate Q survives this finite test.

This does not select the final universe law.  A viable objective-collapse
model predicts a scale-dependent residual

```math
eta_phys=exp[-Gamma(model; mass distribution, separation, time, ...)];
```

ordinary environmental decoherence produces its own suppression.  D21 does
not derive `Gamma`, its coefficients or a unique separation of these effects.

## The physical question that remains open

The most direct cross-rulebook question is:

> After ordinary environment, control and readout losses are independently
> calibrated, is there an additional irreversible decrease of complete-
> support record coherence with increasing mass, branch separation, dwell
> time or number of record factors?

A lawful experiment must:

1. choose one concrete collapse generator and one unitary environmental model;
2. fix all nuisance and collapse coefficients on separate training data;
3. use process-tensor or equivalent multi-time controls to expose residual
   environmental memory rather than assuming Markov noise;
4. freeze several `(mass,separation,time,N)` holdout points;
5. measure the normalized complete-support parity/Mermin visibility there;
6. compare the full preprinted likelihoods, not a post-hoc best curve.

Unitary Q predicts no residual fundamental loss after the calibrated open-
system channel.  A fixed collapse model predicts its independently calibrated
nonzero `Gamma`.  If both predictions overlap over the accessible scale, the
experiment returns a bound, not a selection.

## Why cone geometry stays closed

Both D21 packets use a supplied source and three supplied spacelike output
regions.  Neither generates carrier birth, a growing causal web, a metric,
metres/seconds, `G`, or an effective dimension.  Therefore neither predicts a
V9 cone score `F`, dimension estimate or scale ladder.  Feeding their outcome
tables into a tuned graph builder would reintroduce the unselected generative
law.

Geometry becomes admissible only after Q and a surviving scale-dependent C
are lifted to variable causal-carrier generators with independently frozen
state, measure, record map and units.

## Verdict

```text
FINITE-COMPLETE-RULEBOOK-DISCRIMINATOR       PROVED
MICROSCOPIC-HARD-SEAL ENDPOINT               DISFAVORED BY EXISTING GHZ EVIDENCE
UNIQUE PHYSICAL HISTORY LAW                  NOT SELECTED
ROUND-CONE / 3+1 / G CONSEQUENCES            NOT LICENSED
```

The investigation has found the right **kind** of question—irreducible
complete-history coherence beyond all proper record shadows—and a concrete
laboratory version.  It has not manufactured the missing cosmological
generator or an untouched result.
