# D49 — the completion dichotomy, settled: does paper 30 §5.7's
# stationary completion exist on HISTORIES?

**Status:** CAMPAIGN PIN, 2026-07-25.  **§0 ORDERING DECLARATION
(round-1 m2):** this pin was written CONCURRENTLY with the receipt, not
strictly before it.  The gates and failure modes below were fixed before
the runs that decided them, and §6 records four first-run deviations, but
the strict pin-then-receipt ordering the corpus requires was NOT
observed and the unit does not claim it.  Parents: paper 30 §5.3 / §5.5 / §5.6 / §5.7 (the
decided trilemma, the telescoping theorem, the rootedness exhibit, the
one-way reduction to the infinite-volume core); d43b TERMINAL (#339 /
#345: MG3–MG5, `lambda = 2`, `f = (4,4,3,7,3,3)/3`, MG4's "root-free
certificate YES" on the computed window); d44a TERMINAL (#348 ff.: the
depth-free 36-state closure, the six-class quotient, the (H0)–(H2)
conditional theorem); `THE-COMPLETION-DICHOTOMY.md` (#416, audited
#417).  Receipt: `v10/code/d49_dichotomy_settlement_exact.py`.

## 1. Why this front exists

Paper 30 §5.7 **defines** a stationary (root-free) completion as a
positive-eigenvector solution

```
Zhat(h) = f(state(h)) . lambda^(-depth(h))
```

of the local transfer on the bisimulation quotient, and then declares:
*"No existence claim is made in either direction at this scope
[OPEN, declared]."*

d43b subsequently **computed the eigenproblem** (`lambda = 2`, `f`
positive and unique up to scale, MG4 gating both per-state
normalization and root-class = renewal-class) and d44a **closed the
state space** (36 sigma-states, six quotient classes, all-depth
conditional on (H0)–(H2)).

**But no unit has ever built `Zhat` on HISTORIES and tested it against
the completion demands of paper 30 §5.2.**  Every gate in the chain
above lives on the quotient; the object the dichotomy is about lives on
the cut complex.  The gap is not a hard one — it is simply unperformed
work — and until it is performed the corpus is entitled to say only
"residue 1 is decided", never *which way*.  That is exactly what
`THE-COMPLETION-DICHOTOMY.md` §XI says, and why it closes with "nobody
yet knows which".

**This front performs it.**  Pre-registered, before execution: the
answer is expected to be YES, and the pin is written so that a NO is a
delivered result of equal standing (§4).

## 2. The target

**[TARGET] At d42a scope, `Zhat(h) := lambda^(-|h|) . f(class(sigma(h)))`
with `lambda = 2` and `f = (4,4,3,7,3,3)/3` is a COMPLETION in the
sense of paper 30 §5.2 — per-cut normalized, foliation-invariant,
strictly positive, support-preserving — and it is DEPTH-STATIONARY:
it prices the root and the post-arbitration renewal point identically,
which is precisely the defect §5.6 used to convict every truncated
completion of being ROOTED.  Therefore horn (II) of the dichotomy
HOLDS and the record law is FORWARD-COMPLETE: it does not import a
boundary condition.**

The claim inherits d44a's conditionality EXACTLY and no more:
unconditional at every verified depth, conditional on (H0)–(H2) at all
depths, d42a (delivery-free) scope only.

## 3. Gates (pre-registered; exact Fractions; exit 1 on any failure)

**A — anchors.**  A1 census `[1,7,39,215,1191,6471,34375]`, 427 / 5,548
canonical classes, the depth-4 complex split 114 interior + 313
terminal.  A2 the frontier-exhausted sigma closure (36 states, 176
edges) re-derived.  A3 the six-class quotient (trajectory 4-5-6-6) and
`T == T_REF` with row sums `(2,2,2,5/2,2,2)`.

**C — the Perron package, re-derived not imported.**  C1 `{2,4,5}`
closed and irreducible; `charpoly(dominant) = (x-2)(x-3/2)(x-1)`;
`charpoly(transient) = (x-3/2)^3 - 1/32`, i.e. transient radius
`3/2 + 2^(-5/3) < 2`.  C2 `T f = 2 f` exactly with `f > 0`.

**D — the settlement object, on histories.**  D1 `Zhat` strictly
positive and per-cut normalized at every history of depth <= 5, zero
exceptions.  D2 class-constancy on all 5,548 canonical classes.  D3
foliation invariance directly: the completed chain product equal across
ALL linear extensions of every canonical class at depth <= 4.  D4 the
flatness ladder's third rung: 0/202 diamonds for `Zhat` against 36/202
for the naive normalizer in the same run.  D5 support preservation —
join arbitrations survive (the d42b3-D3 zero class did not).  D6 the
completed MENU is a function of `sigma(h)` alone (the kernel is a law,
not a table).  D7 the completed weights of all depth-`D` histories sum
to exactly 1 for `D = 1..6` (it is a measure).

**E — the rootedness defect.**  E1 paper 30 §5.6 reproduced exactly on
both canonical boundaries (`1037/64`, `133/2074` vs `1/16`; `325/64`,
`21/325` vs `1/16`).  E2 `Zhat` prices the matched pair EQUAL, and the
entire 215-node matched subtree carries identical completed menus.
E3 depth-stationarity: the completed state-to-state transfer is a
function of the state alone, with d43b's conflict row `{1/7, 3/4, 3/28}`
recovered from histories.

**F — uniqueness.**  F1 `lambda = 1` is impossible (row sums in
`[2, 5/2]`; the eigenvalue 1 exists but its generator has mixed signs)
— the depth grading is forced, not chosen.  F2 `lambda = 2` is the only
eigenvalue admitting a positive eigenvector, and the transient
extension is forced by the nonnegative resolvent.  F3 the stationary
completion is realizable inside the boundary freedom as exactly one
ray.  F4 washout within sigma-measurable boundaries.  F5 **the
uniqueness re-run at the FINE 36-state level** — the settlement must
not be an artifact of quotienting.

**G — negative controls.**  G1 unconstrained boundaries do NOT wash
out (pre-registered as a gate whichever way it lands).  G2 what the
settlement does not buy: demand (c) is not restored.  G3 mutants: a
class-constant non-harmonic probe passes the diamond test and fails
normalization (the separating content is harmonicity); a perturbed `f`
fails.  G4 out-of-sample normalization at all depth-6 histories, whose
menus reach the uncached depth-7 level.

## 4. Failure modes (pre-registered; each a delivered outcome)

- **D1 fails** — `Zhat` is not normalized at some history: then the
  Perron package does NOT lift from the quotient to the cut complex,
  paper 30 §5.7's reduction is broken as stated, and **the failing
  history is the result**.  Horn (I) would then be forced and the
  corpus would owe a correction to d43b MG4's "root-free certificate
  YES", which would stand convicted of being a quotient-level claim
  mis-read as a history-level one.
- **E2 fails** — the matched pair prices unequally: `Zhat` is rooted
  too, the reduction is vacuous, and residue 1 answers NO.
- **F5 fails** — a positive eigenvector exists at the fine level with
  a different `lambda`, or the fine chain has several closed classes
  with different Perron roots: uniqueness is a quotient artifact, the
  settlement degrades to "a stationary completion exists but is not
  canonical", and horn (II) survives only in a weakened form that must
  be stated as such.
- **G1 lands EITHER WAY and is reported either way.**  If unconstrained
  boundaries DO wash out, the settlement is stronger than claimed
  (the boundary is asymptotically irrelevant, full stop).  If they do
  NOT, the settlement rests entirely on the sigma-measurability demand
  and the note must say so in its headline.

## 5. Scope, declared before execution

d42a (two actors, `p`/`r`/`n`, the committed admission layer) —
**delivery-free scope ONLY**.  At d42b1 transport scope the state space
escapes every computed window (paper 32 §2.3) and nothing here
transfers.  Exact Fractions throughout; stdlib only; the admission
layer exec'd `__file__`-anchored from the committed d42b3 receipt;
`sigma` ported from the committed d44a SECTION A; determinism gated by
byte-identical runs across `PYTHONHASHSEED`.

## 6. First-run amendments (2026-07-25, pre-round; four deviations,
## all gated, nothing silently weakened)

**A1 (F1's certificate was hand-computed and WRONG).**  The pinned
`lambda = 1` eigenvector `(0,0,1,0,1,-1)` satisfies the dominant block
but not row 1 of the full transfer.  Repaired mechanically: the receipt
now computes `ker(T - I)` by exact elimination, finds it
one-dimensional with generator `(-4/5, 4/5, -1, -1/5, -1, 1)`, and
gates the sign-mixing.  The gate's content is unchanged; its evidence
is now machine-derived rather than asserted.

**A2 (F3's pinned rank was wrong, and the true value is a RESULT).**
The pin expected the boundary -> interior-completion map to have rank
114 (all interior cut classes independently controllable).  The true
rank is **84 = the number of depth-3 cut classes** (layer census
`1/6/23/84/313`), so **229 of paper 30 §5.3's 313 boundary dimensions
act TRIVIALLY on the completion**: the map is onto the deepest interior
layer and every shallower layer is then forced.  This SHARPENS §5.3 —
the completion freedom at depth-4 truncation is 84-dimensional, not
313-dimensional — and the gate is re-anchored to 84 with the layer
census gated alongside it.

**A3 (F4's iteration budget was too small).**  `n = 120` left the most
skewed boundary at `2e-2`.  The gate is repaired at the level of its
certificate rather than its budget: the left Perron vector
`pi = (1,1,2)/4` is now gated (`pi T = 2 pi`, strictly positive on the
dominant class, zero on the transient one), which with C1's spectral
gap IS the convergence theorem; the iteration battery is extended to
`n = 400` and retained as its exhibit.

**A4 (a determinism defect in this receipt, caught by seed variation
and repaired).**  E2's matched-subtree comparison serialized `'r'`
events through a raw `frozenset` repr, so under `PYTHONHASHSEED=7` it
reported 7 spurious mismatches and the receipt exited 1 — exactly the
failure mode the d44a banner warns about.  Repaired with a recursive
deterministic key (`dkey`: frozensets become tuples sorted by their own
deterministic keys), applied at every ordering and comparison site in
this receipt.  **Recorded rather than quietly fixed** because it is a
live demonstration that the corpus's determinism discipline earns its
keep.

**A2 IS ITSELF WITHDRAWN BY ROUND 1 (BLOCKER B1).**  The rank is 84 and
that is right; the *reading* — "229 boundary dimensions act trivially on
the completion", and the paper-30 erratum it queued — is FALSE.  The
depth-3 transfers read the boundary directly.  See the result note §3.4
and gate F3.

Post-first-run: 25 PASS / 0 FAIL.  **Post-round-1 repair: 31 PASS / 0
FAIL, exit 0**, ~100 s single-threaded, byte-identical across
`PYTHONHASHSEED` 0 / 7 / 61 / 999.  Round frozen at
`v10/reviews/d49-round1-hostile-review.md`; TERMINAL at #419.
