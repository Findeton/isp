# D34d round 2 — locality/clock final delta

**Target:** commit `44a54d4`, audited only against the two minors and two nits
remaining in `d34d-round1-locality-clock-hostile-delta.md`.

**Exact verdict:** **DELTA-CLEAN — 0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

## Reproduction

Fresh-salt executions are byte-identical to the committed data:

- D34d classical, `PYTHONHASHSEED=13579,24680`:
  `912394a45eb76e3cf3d36ed51310f44f7f51f0e2c0d9162b97d42015feb6b16b`,
  13/13;
- D34d quantum, the same salts:
  `e1990fe3a4dfbc44c83b4b49216df44ad9462dcb410c9c24c19dc4144c3884d1`,
  10/10;
- D34b exact parent:
  `47993cbcaf3d3a719ef868fd6a4d122b9b2d46e23555133d886185f79358740c`,
  7/7;
- D34b actor parent:
  `59d28bc5db03cca5e30a81eaed09c1c42d7e51541f6ea7c3d078c9d59a75c2a3`,
  8/8.

## m1 — sealed initiator/target eligibility: CLOSED

The reconstructed generator now forms each actor's eligible target set by
filtering out sealed neighbors. It separately skips sealed initiators, and the
event step rejects a forced interaction with a sealed target.

The explicit `R--A--B` control carries the actual actor-architecture case:

```text
R initiator rows: absent,
R target rows:    absent,
A -> B rate:      1/4.
```

Thus the sealed root does not dilute A's interaction mass and cannot receive
an event. The prior active-only/prose mismatch is gone.

## m2 — full rate–horizon source coupling: CLOSED

The note now carries the correct pathwise proof, not merely a no-ring
cylinder: under common scale `c`, divide every preassigned exponential wait by
`c`, retain every mark and Ulam address, and induct across each birth. The
deterministic Harris map therefore produces the same typed path through `T` in
the scaled law as through `cT` in the base law.

P11 instantiates a nontrivial exact tape:

```text
base c=1, horizon 2: A birth at 1; B passive reception into A at 2,
scaled c=2, horizon 1: the same birth/reception DAG at 1/2 and 1.
```

The complete state key and typed-DAG key agree, the event kinds are exactly
`("b","i")`, both private ring counts advance once, and every scaled time is
the base time divided by two. This is the requested birth-plus-reception gate.
The surrounding transformation table still correctly distinguishes fixed-T
law change, compensated-horizon equality, embedded-order invariance and
nonlinear-hazard change.

## n1 — construction-time stopping wording: CLOSED

Both pin and executable now say:

> stopping times of the complete construction-time filtration.

No “physical stopping time” phrase remains in the repaired theorem. Causal
order, construction time and emergent proper time remain separate, and proper
time is explicitly open.

## n2 — independent renewal race derivation: CLOSED

The duplicate function call is removed. The algorithmic residual-race formula
is compared with the independent direct integral for residual supports
`L_A=2,L_B=1`:

```text
integral_0^1 (1/L_A)(1-r/L_B) dr = 1/4.
```

Both yield `(P(A first),P(B first))=(1/4,3/4)`. The reset/no-reset, newborn-age
and joint-survival gates remain unchanged and exact.

## Claim-ceiling audit

The final classical scorecard still claims only:

> the chosen D34b law is strong Markov on its **complete global** Harris
> configuration and has support-local actor generator terms.

It explicitly leaves open a bounded local predictive collar, uniform
per-record predictive memory, physical proper time, the timed D34b–D34c
operator-valued law, and derivation of physical rates/operations. The capacity
ledger still records unbounded actor degree, Ulam identifier length, boundary
width, age-vector width and posterior complexity. Nothing in this cleanup
silently upgrades global Markov closure to a bounded local-state theorem.

## Final stamp

The locality/clock stream accepts the repaired statement without reservation:

> **D34d GLOBAL-MARKOV / LOCAL-GENERATOR / OBSERVABLE-MEMORY
> CHARACTERIZATION:** the chosen static-adjacency D34b law is strong Markov on
> its complete global configuration and has support-local generator terms;
> visible record memory is governed by the explicitly scoped predictive-state
> and lumpability tests; a bounded all-future local collar remains open.

**DELTA-CLEAN — 0B / 0M / 0m / 0n.**
