# D52 — the dichotomy at TRANSPORT scope (PIN + first probe)

**Status:** PIN, STRICT, 2026-07-25.  Parents: D49/D50 (the dichotomy
settled and then narrowed at d42a scope), D51 (the four
menu-relevant projections), paper 32 §2.3 (the state space escapes
every computed window at transport scope).

## 1. Why this is the real frontier

Everything settled about the completion dichotomy is at **d42a,
delivery-free, two actors**.  The theory that matters — the one D47
and D48 probe for spacetime structure — has **delivery and merge**.
D49's own pin says plainly that nothing transfers.

At d42a the whole settlement rested on one fact: `sigma` closes at
**36 states**, so the transfer is a finite matrix and Perron theory
applies.  **If no bounded abstraction exists at transport scope, the
dichotomy cannot even be posed the same way there** — there is no
finite chain to carry an eigenvector.

So the first question is not "which horn?" but:

> **Does a bounded local-state abstraction exist at transport
> scope?**

## 2. First probe, run 2026-07-25, and its LIMITATION

Applying D51's four menu-relevant projections to the committed
`d42b1_transport_exact.py` layer, two actors, to depth 5:

| depth | histories | distinct projection-states | cumulative |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | 8 | 5 | 5 |
| 2 | 60 | 13 | 13 |
| 3 | 452 | 39 | 39 |
| 4 | 3,448 | 107 | 107 |
| 5 | 26,760 | 275 | 275 |

Two observations, and the second disqualifies the first as evidence:

1. Growth is roughly ×2.6 per depth with **no closure in sight**,
   and the cumulative count equals the per-depth count — **no state
   ever recurs across depths.**
2. **BUT THIS PROBE LACKS THE BASE-RENAMING QUOTIENT**, and that
   quotient is exactly what makes `sigma` finite at d42a.  Every
   arbitration mints a fresh version name; without identifying names
   up to renaming, *even d42a would not close*.  The non-recurrence
   in the table is therefore substantially an artifact of the missing
   quotient, not a finding about transport.

> **`[MEASURED, upper bound only]` The table above bounds the true
> state count from ABOVE and DOES NOT decide the question.  It must
> not be cited as evidence that transport fails to close.**

## 3. What the campaign must do

- **T1 — port the renaming quotient.**  Rebuild `sigma` for the
  transport layer with base renaming, genesis/renewal identification,
  and the superseded-pattern restriction, as d44a does for d42a.
  Delivery adds holdings monotonically, so the *right* abstraction
  must also quotient by which actor holds what, not merely record it.
- **T2 — closure or blow-up, decided.**  BFS on the quotiented state
  space with a frontier-exhaustion test, exactly as d44a's CG3a did.
  Both outcomes are results; a measured blow-up rate with the
  quotient in place is worth as much as a closure.
- **T3 — only if T2 closes:** the Perron package, then D49's `Zhat`
  construction, then the dichotomy itself.
- **T4 — if T2 does not close:** state precisely what replaces the
  finite-chain argument, or record that the dichotomy is
  **undecidable by these means** at transport scope, which is itself
  the deliverable.

## 4. Pre-registered expectation

**Unknown, deliberately.**  Paper 32 §2.3's "escapes every computed
window" was measured without the quotient this pin requires, so the
corpus does not currently have grounds for an expectation either way.
Recording *no* expectation is the honest state; inventing one would be
the error D49 was corrected for.

## 5. Scope and inheritance

Whatever T2 returns, the d42a results stand exactly as scoped, and
**(H1) remains undischarged there** (D51), so anything built at
transport scope inherits that too unless it re-establishes its own
foundations.
