# D11 hostile mathematics review — round 1

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**

The extinction theorem is sound, the frozen numerical outcome reproduces, and
the declared packet is substantially more complete than its predecessors. The
major grade comes from one preregistered exact gate that was not actually
tested—projectivity—and one numerical influence gate whose implemented proxy
does not match the frozen definition. Neither defect rescues the universe: the
extinction result and the failed numerical interaction threshold remain.

## 1. Reproduction

All six frozen artifact hashes match `v10/data/d11-pre-review-receipt.md`.
Ordinary and optimized exact execution agree and reproduce:

```text
checks=65
cutoff3_histories=117
depth12_orbit=113
depth12_support=0.914143429015
stdout_sha256=be58dff995e1103e08236d735370bf996e9cbd81de071d0d8e3bbd2e31b807be
```

The numerical campaign reproduces all frozen summaries and
`receipt_sha256=f073ed07f712c0d578dcd360ccf312be49129428beac20cf9c6bab8e142888e0`.
It again gives zero cone violations and false join, support, and rank gates,
with `numerical_verdict=INTERACTION-INERT`.

## 2. Blockers

### B1 — normalization was mislabeled as projectivity

**Severity: MAJOR**

Frozen G3 requires:

> Deleting terminal continuations gives the parent cylinder law.

The exact engine never defines a truncation/deletion map and never pushes a
depth-`n+1` measure through one. At lines 695–707 it only iterates the kernel
and checks

```python
sum(mass for _, mass in rows) == 1
```

at each depth. The check label `full-history mass projective` is therefore
incorrect: normalization of each level is not projective consistency between
levels. This matters especially because terminal histories are padded by an
absorbing clone, disjoint schedules are later quotiented canonically, and raw
rows are not coalesced. Those conventions need an explicit bonding map before
their cylinder pushforward can be audited.

A normalized next-state kernel can indeed generate a consistent path measure,
and the present grammar is likely repairable. But Paper 12's claim of
“projective mass through exhaustive cutoff three,” the literature note's
projectivity PASS, and exact G3 are not established by the frozen receipt.

**Required repair:** represent or retain each committed-event path, define the
one-event truncation including terminal padding and construction-order
quotienting, aggregate equal parent cylinders exactly, and check
`pi_* mu_{n+1}=mu_n` through the registered cutoff. Also state the general
kernel-to-path-measure argument separately from the finite test.

### B2 — numerical JOIN influence is not the registered influence observable

**Severity: MAJOR**

The protocol defines interventional influence by a changed **later seal
distribution**. The numerical campaign increments `join_transfers` immediately
after a JOIN whenever either its output density matrix **or its coordinate**
differs between paired worlds:

```python
if (left_changed or right_changed) and (differs(rho, rhoi) or differs(y, yi)):
    join_transfers += 1
```

A coordinate difference is not a seal-law difference. Even a density-matrix
difference need not change the fixed `P0/P1` seal probabilities; phase-only
differences are a direct counterexample. The code does not require a later
seal, compare its Born distribution, or attribute that changed seal to a JOIN
ancestor. Thus the reported `3/24, 9/24, 5/24` are state/position-transfer
counts, not the frozen “JOIN-transmitted influence” statistic.

The exact engine separately contains a valid witness where JOIN changes a
later `P0` probability. That proves the mechanism can transmit influence, but
not its per-history numerical prevalence.

The frozen numerical verdict is nevertheless stable: the current proxy already
fails `20/24`, and a stricter genuine seal-influence count can only be no larger
for these same histories. Therefore `INTERACTION-INERT` remains the registered
precedence outcome, but its printed gate statistic and the paper's prevalence
sentence require repair.

**Required repair:** count a JOIN only when a downstream seal Born distribution
changes and the causal provenance includes that JOIN; retain state transfer as
a separately named diagnostic.

## 3. Moderate opening

### M1 — theorem-critical algebraic signs are decided by Decimal without the promised margin

**Severity: MODERATE**

The exact engine stores numbers in `Q(sqrt(2),i)`, but `Q2.__lt__` and
`Q2.__le__` convert `a+b sqrt(2)` to 120-digit `Decimal`. These comparisons
feed `is_psd2`, including ancestry positivity, the boosted common-future test,
the naive-join negative control, and the branch-disjoint positivity witness.
The module docstring says every such sign is separated from zero by a
**disclosed margin**, but no minimum margin or exact sign certificate is
printed.

The audited controls are not numerically close—the naive-join determinant, for
example, is safely negative—and the construction identities strongly support
the conclusions. Still, a high-precision sign is not exact merely because its
input is algebraic.

**Required repair:** compare `a+b sqrt(2)` exactly by rational sign and squared-
magnitude cases, or print a rigorous rational error bound and the minimum
separation used by every load-bearing Decimal comparison. Keep the Fibonacci
support explicitly in the float diagnostic class, where it already belongs.

## 4. Extinction theorem audit

The population theorem passes hostile reconstruction.

With `p` open ports, there are `p` SPLIT and `p` SEAL tokens. Enabled sibling
JOINs are port-disjoint: splitting or consuming either endpoint invalidates its
old JOIN, and each fresh pair receives only one JOIN. Hence

```text
0 <= j <= floor(p/2).
```

Equal activities give

```text
Pr(Delta P=+1 | H_n) = p/(2p+j),
Pr(Delta P=-1 | H_n) = (p+j)/(2p+j),
E[Delta P | H_n]     = -j/(2p+j) <= 0.
```

Thus the stopped open-port population is a bounded nonnegative
supermartingale. From `P_0=1`, optional stopping (equivalently Ville's
inequality) gives probability at most `1/M` of reaching `M` before zero.
Inside `1<=p<M`, total SEAL probability satisfies

```text
p/(2p+j) >= 2/5.
```

Whatever the current population, at most `M-1` successive SEALs reach zero,
so every block of `M` steps has conditional absorption probability at least
`(2/5)^M`. Survival forever while remaining below `M` therefore has probability
zero. Letting `M` tend to infinity proves almost-sure extinction. The root's
immediate-extinction probability is exactly `1/2`.

This also validates the proposed COMMIT drift arithmetic:
`(p-j)/(2p+j)>0` follows from `j<=p/2`, though COMMIT remains an untested next
packet.

## 5. Numerical gates, M4, and precedence

- The code implements the frozen verdict precedence exactly: causal violation
  first, then join gate, then support/rank. Since the join gate fails, the
  registered label is `INTERACTION-INERT` even though support and rank also
  fail.
- That label is semantically coarse—the exact witness shows interaction is
  possible—and the notes correctly replace it physically with
  “interaction-capable but population-extinct.”
- The inherited generated-cloud `F` statistic mostly refuses for insufficient
  projections. No generated roundness PASS is asserted.
- The M4 control passes only the registered `m4` time-axis pipeline and refuses
  the diagonal/`dom` convention on `24/24` controls. Because the protocol
  forbids an `F` claim unless both inherited conventions are valid, refusal is
  the correct mathematical outcome; the reported M4 means are controls, not a
  generated-packet shape result.
- The float64 campaign is properly secondary to the exact construction, but
  B2 must be corrected before its interaction prevalence is interpretable.

## 6. Primary-verdict audit

The packet specifies root, token emission, activities, ownership, instruments,
invalidation, positions, and outcomes, and its exact causal-containment theorem
survives. The numerical conjunction fails without any cone counterexample, so
`REFUTED-CAUSAL-WIRING` is not warranted. `COMPLETE-KINEMATICS/INFLUENCE-
ENVELOPE-OPEN` is the natural intended branch.

However, the frozen protocol makes exact G0–G6 primary, and G3 projectivity was
not actually demonstrated. The submitted primary verdict is therefore **not
yet certified by its own frozen gates**. This is a proof/receipt failure, not
evidence that a rule field is absent; after an actual truncation-pushforward
test, the same primary verdict may stand.

## 7. Verdict

**MAJOR REVISION.** Preserve the extinction theorem, the zero cone-violation
result, exact local JOIN influence witness, M4 refusal, and intended primary
branch. Repair the projectivity gate and the numerical JOIN-influence
observable, and replace Decimal sign decisions with exact or rigorously bounded
algebraic comparisons before issuing a final D11 receipt.
