# D49 — THE COMPLETION DICHOTOMY IS SETTLED: HORN (II)

**Result note, 2026-07-25.**  Pin:
`note-d49-completion-dichotomy-settlement-pin.md` (strict).  Receipt:
`v10/code/d49_dichotomy_settlement_exact.py` — **31 PASS / 0 FAIL**,
exit 0, ~100 s single-threaded, byte-identical across
`PYTHONHASHSEED` 0 / 7 / 61 / 999.  Ledger #418; **round 1 frozen at
`v10/reviews/d49-round1-hostile-review.md` (REVISE, 2 BLOCKER / 4 MAJOR
/ 3 MINOR / 1 NIT), repaired and delta'd at #419 — TERMINAL.**  Every
round-1 finding is carried in §7 below and in the gate text itself; two
headline claims of the first delivery are WITHDRAWN there.

---

## 1. The verdict

> **`[THEOREM at d42a scope, conditional on (H0)–(H2); `[EXACT]`
> unconditionally at every verified depth]`**
>
> **A root-free completion of the record law EXISTS — which is exactly
> what paper 30 §5.7 declared `[OPEN, declared]` — and it is**
>
> ```
> Zhat(h)  =  2^(-|h|) . f(class(sigma(h))),
>       f  =  (4, 4, 3, 7, 3, 3)/3,     lambda = 2.
> ```
>
> It is strictly positive, per-cut normalized, foliation-invariant,
> support-preserving, flat on all 202 canonical diamonds, and it
> prices the root and the post-arbitration renewal point **identically
> at `1/16`** — the defect that convicted every truncated completion
> of being ROOTED.
>
> It is **unique up to scale within paper 30 §5.7's stationary form**
> (`Z` a depth-graded state function on the closed chain).
>
> **Horn (II) holds.**
>
> **On "forward-complete" (round-1 B2, binding).**  The phrase is true
> of *the law plus that form*, and must never be quoted without it.
> The form is a **postulate about the shape of `Z`**, not an invariance
> principle: measured at depth-4 truncation, renewal-pair agreement
> leaves **308 of 313** boundary directions free and
> bisimulation-invariance leaves **119** (§4b). The *existence* result
> — the dichotomy's actual question — is untouched by this.

The question `THE-COMPLETION-DICHOTOMY.md` §XI closes with — *"is the
record law forward-complete, or does the world carry a boundary
condition?"* — is answered: **forward-complete**, at d42a scope.

## 2. What was actually missing, and it was not a hard problem

Paper 30 §5.7 **defines** the stationary completion in exactly the form
above and declares its existence `[OPEN, declared]`.  d43b then
computed the eigenproblem and gated MG4 — *"root-free certificate:
YES"* — and d44a closed the state space.  **Every one of those gates
lives on the quotient.**  The object the dichotomy is about lives on
the cut complex, and no unit had ever built `Zhat` on histories and
run it against the §5.2 demands.

So the corpus has been carrying a decided question as an open one for
the span #339 to #417.  The distance was one receipt, not one theorem.
That is the finding, and it is worth stating plainly rather than
dressing up: **the settlement was already implied by committed work;
what was missing was the lift and the test.**

## 3. The certificates

### 3.1 `Zhat` is a completion (SECTION D)

| gate | result |
|---|---|
| positivity + per-cut normalization, depth <= 5 | **0 violations / 6,471 histories** |
| class-constancy (gauge invariance) | **0 violations / 5,548 canonical classes** |
| foliation invariance, DIRECT | completed chain products equal across **all 1,191 linear extensions of all 427 classes** at depth <= 4, **0 violating classes** |
| diamond flatness | **0 / 202** — against the naive normalizer's **36 / 202** in the same run |
| support preservation | **2,032** join arbitrations retain strictly positive weight at depth <= 5 |
| the kernel is a LAW | the completed menu, up to base renaming, is a function of `sigma(h)` alone: **1,163 same-sigma comparisons over 28 sigma-classes, 0 mismatches** |
| it is a MEASURE | completed weights of all depth-`D` histories sum to **exactly 1** for `D = 1..6` |
| out-of-sample | normalization holds at all **27,904 depth-6 histories**, whose menus reach the uncached depth-7 level (145,408 children): **0 violations** |

The foliation-invariance gate is worth singling out.  Paper 30 §5.5
established that diamond flatness certifies *class-constancy*, not
harmonicity — so passing 0/202 proves less than it looks.  D3 does not
rely on it: it compares the completed chain product across **every**
linear extension of **every** canonical class, which is the definition
rather than a proxy for it.  D4 is retained only because its control
arm reproduces the 36-diamond census that forced the dichotomy.

### 3.2 The rootedness defect is healed (SECTION E)

Paper 30 §5.6 reproduced exactly, then removed:

| completion | `Z(empty)` | root | renewal `H3` |
|---|---|---|---|
| unit boundary | `1037/64` | `133/2074` | `1/16` |
| class-`1/k` boundary | `325/64` | `21/325` | `1/16` |
| **`Zhat`** | — | **`1/16`** | **`1/16`** |

`Zhat` reaches exactly the number the truncated completions could not.
And not only at the exhibited pair: **the entire 215-node matched
subtree** — the root tree against `H3`'s subtree under the `v0 -> v1`
substitution — carries **identical completed menus event-by-event, 0
mismatches**.  The completion no longer distinguishes two record points
the law identifies.

Depth-stationarity is gated directly: the completed state-to-state
transfer is identical at every one of the 6,471 histories of depth <= 5
carrying that state, with d43b's conflict row `{0: 1/7, 3: 3/4,
5: 3/28}` recovered from histories rather than from the quotient.

### 3.3 Uniqueness — the completion is not a choice (SECTION F)

- **`lambda = 1` is IMPOSSIBLE.**  Every menu of the closed 36-state
  chain has weight sum in `[2, 5/2]`, so for any `f > 0` the minimising
  state forces `lambda >= 2`.  The value 1 *is* an eigenvalue of `T`,
  its eigenspace is one-dimensional, and its generator
  `(-4/5, 4/5, -1, -1/5, -1, 1)` has **mixed signs**.  So a
  depth-UNGRADED positive completion — `Z` a function of the state
  alone — does not exist, and paper 30 §5.7's `lambda^(-depth)` factor
  is a **necessity, not a convention**.
- **`lambda = 2` is the only eigenvalue admitting a positive
  eigenvector.**  `{2,4,5}` is closed and irreducible, so `f` restricted
  to it must be its Perron vector and `lambda = rho(dominant) = 2`
  (`charpoly(dominant) = (x-2)(x-3/2)(x-1)`).  The transient extension
  is forced by the entrywise-nonnegative resolvent `(2I - M_t)^(-1)`
  (`det = 3/32`), returning exactly `(4/3, 4/3, 7/3)`.
- **It is not an artifact of quotienting.**  Re-run at the FINE
  36-state level: exactly **one** closed communicating class (9 states,
  every row summing to 2, Perron root 2), 27 transient states with
  `det(2I - M_t) = 2187/2^41` and a nonnegative resolvent, and
  `dim ker(2I - M36) = 1`.  The fine chain's positive eigenvector
  exists only at `lambda = 2`, is unique up to scale, and is exactly
  `f` pulled back along the quotient.

### 3.4 The rank-84 result, correctly stated (round-1 BLOCKER B1)

**WITHDRAWN, in full:** the first delivery claimed "the boundary freedom
is 84-dimensional, not 313" and that "229 of the 313 boundary dimensions
act trivially on the completion", and queued an erratum against paper 30
§5.3.  **All of that is wrong and the erratum is withdrawn.**  A
completion is the transfer at *every* interior cut, and the transfer at a
depth-3 cut is `q . Z(h+e)/Z(h)` with `|h+e| = 4` — **it reads the
boundary directly.**  Gated counter-witness (F3): two strictly positive
boundaries differing by a kernel direction give **identical interior
potentials** and **different completed transfers at depth-3 cuts**.
**Paper 30 §5.3's 313-dimensional boundary freedom is CORRECT.**

What survives is narrower and is an *addendum*, not a correction. The
boundary → interior-**potential** map has rank exactly **84 = the number
of depth-3 cut classes** (layer census `1/6/23/84/313`); the `<=` is
forced, since shallower layers are determined by the depth-3 layer, so
the content is surjectivity onto it.  Corollary, gated: **the completed
transfer at cuts of depth `<= 2` sees the boundary only through that
84-dimensional image**, while the depth-3 layer sees all 313.  And the
stationary boundary `b*(t) = 2^(-4) f(class(t))` is strictly positive
and reproduces `Zhat` at all 215 interior histories exactly.

### 3.5 The deformation is exactly the Perron tilt

For every pair of alternatives at every cut,

```
q'(e1) / q'(e2)  =  [ q(e1)/q(e2) ] . [ f(class(h+e1)) / f(class(h+e2)) ]
```

— which is `[THEOREM-PASS]`: it is the definition of `q'` rearranged,
and its 77,541 pairs are a restatement, not a sweep (round-1 M1).  As a
*characterisation* it is still the useful statement: the completion preserves the weight-system
ratio *exactly* between options leading to the same state, and tilts it
*only* by the ratio of the successors' Perron weights.  In words: **each
option is re-weighted in proportion to how much record-growth capacity
it leads to, and by nothing else.**  That, and nothing else, is what
horn (II) costs.

## 4. What the settlement does NOT buy — stated before anyone asks

**(a) Demand (c) is not restored, and the §5.2 no-go is untouched.**
`Zhat` deforms within-cut ratios at **50 of the 114 interior cut
classes** — *more* than the unit boundary's 21.  Ratio-preserving
completions remain refuted by the 36-diamond certificate; that theorem
is unconditional and this work does not touch it.

**But the ROOT is not among the 50.**  At the root `Zhat` is exactly
ratio-preserving: `q' = q/2`, every proposal `1/16`, every idle `3/8`.
Paper 30 §5.3's sharp point — that the deformation reaches the theory's
beginning — **is removed**.  (It is a fact of the chain, not a design
choice: `f(0) = f(1) = 4/3`.)

**(b) The settlement rests on the sigma-measurability demand, NOT on
asymptotic forgetting.**  Pre-registered as a gate that would be
reported whichever way it landed, and it landed negative: **unconstrained
boundaries do NOT wash out.**  The achievable root-transfer set is a
projective image of the boundary cone, hence the convex hull of its
vertices, and its diameter is **1 at every truncation depth tested**
(6 / 23 / 84 / 313 terminal classes).  A boundary free to distinguish
anything can drive the root anywhere.

What *does* wash out is every boundary that respects the law's own
identifications: the left Perron vector `pi = (1,1,2)/4` satisfies
`pi T = 2 pi` and is strictly positive on the dominant class, so
`pi . b > 0` for every strictly positive sigma-measurable `b`; with the
spectral gap (every other modulus `<= 3/2 + 2^(-5/3) ~ 1.81498 < 2`)
this gives `T^n b / 2^n -> (pi.b / pi.f) f` at geometric rate
`~ 0.9075^n` — gated to `< 1e-9` by `n = 400` on a battery of extreme
positive boundaries.

**So horn (I) is refuted by uniqueness under the law's own
identifications, not by any limit.**  The honest form of the
settlement is:

> Among completions that do not distinguish record points the law
> identifies, there is exactly one, and it needs no boundary.
> Importing a boundary condition is possible only by choosing to
> violate the renewal identification.

**(c) The evidence is stratified, and the gate count is not a score
(round-1 M1).**  Of the 31 gates: **15 SUBSTANTIVE, 5 ANCHOR, 6 DERIVED,
5 THEOREM-PASS** — anchored in-receipt at H6 by an AST scan of the gate
labels.  D1 is arithmetic given d44a CG1+CG2 and d43b MG3; **E2 is a
theorem-pass given d44a SG3 plus `sigma`-measurability, so the
most-quoted number in this note — `1/16` = `1/16` — is a property of
the DEMAND, not evidence for the Perron vector**; D4 is paper 30 §5.5's
telescoping theorem; D5, D7 and G5 are the definition of `q'`
rearranged.  Large pass counts now carry their vacuous members: of the
5,548 canonical classes in D2, **813 are singletons** where
class-constancy cannot fail (effective 4,735); of D3's 427 classes, 137
have a single linear extension (effective 290).

**(d) Scope.**  d42a, delivery-free, two actors.  Unconditional at
every verified depth (exhaustive through depth 7 across this receipt
and d44a's); conditional on (H0)–(H2) at all depths, exactly as d44a's
conditional theorem is and no more.  **Transport scope (d42b1) is OPEN**
and must be said so at every citation: paper 32 §2.3 shows the state
space escapes every computed window there.

## 5. Forward corrections owed

1. **Paper 30 §5.7's `[OPEN, declared]` is DISCHARGED**, in the
   affirmative, at d42a scope, *for existence*.  The form it states is
   the thing that also delivers uniqueness, and that is a postulate
   (§4b).  Its residue item 1 ("the infinite-volume
   positive-harmonic core") is answered: the positive harmonic function
   exists on the cut complex, it is `Zhat`, and the one-way reduction
   §5.7 constructed is the route that delivers it.
2. **NO ERRATUM IS OWED TO PAPER 30 §5.3** — the first delivery queued
   one and round-1 B1 refuted it.  313 is correct.  The rank-84
   computation is an **addendum** (§3.4): the boundary → interior-
   *potential* map has rank 84, so cuts of depth `<= 2` see the boundary
   only through an 84-dimensional image.
3. **Paper 30 §5.6's "truncated completions are rooted" STANDS** — and
   is now the load-bearing premise of the settlement rather than a
   defect report, since it is exactly what singles `Zhat` out.
4. **`THE-COMPLETION-DICHOTOMY.md` requires a Part XII and a rewritten
   §XI** (both applied, #418): its Part VI, Part VIII item 1, and §XI
   present residue 1 as undetermined, which it was not at the time of
   writing and certainly is not now.
5. **The dichotomy's two horns are NOT mutually exclusive as stated**
   in the brief §3.2, and this is a real defect in the framing, not a
   quibble.  Horn (I) is "the completion deforms within-cut ratios";
   horn (II) is "a root-free completion exists".  `Zhat` does both.
   The genuine fork is **imported boundary vs law-determined boundary**,
   and the brief must say so.

## 6. What this opens

- **(H1) becomes the whole of it.**  The settlement's conditionality is
  now identical to d44a's, so the depth-free menu-factorization lemma
  is no longer "the last gap before residue 1 can be decided" but "the
  last gap before the dichotomy is settled unconditionally at d42a
  scope".  Its leverage went up, not down.
- **Transport scope is now a question with a known shape.**  At d42b1
  one asks the same three things: does the state space close, is there a
  single closed communicating class, and is its Perron root the one the
  menus force?  D46b already has the Martin/`h`-transform structure and
  a contraction sequence there.
- **A physical reading is now available and should be audited, not
  assumed.**  `Zhat` is the Doob `h`-transform of the weight system by
  its Perron function — the canonical "condition on continued growth"
  object.  Its tilt weights each option by the record-growth capacity of
  the state it leads to.  Whether that is *the* physical selection
  principle or merely the unique mathematically canonical one is a
  question this receipt does not touch.
- **The second grammar.**  Two-of-two breadth discipline applies: d42b7's
  ternary-payload grammar has a state chain that has never been built.
  Until it is, `lambda = 2` and `f = (4,4,3,7,3,3)/3` are
  **toy-relative values**; the FORM (a unique Perron completion) is what
  is claimed to generalize, not the numbers.


## 7. Round-1 amendments (2026-07-25; review frozen at
## `v10/reviews/d49-round1-hostile-review.md` — REVISE, 2 BLOCKER /
## 4 MAJOR / 3 MINOR / 1 NIT; every finding applied)

**B1 — the rank-84 interpretation WITHDRAWN, the paper-30 erratum
withdrawn with it.**  §3.4 rewritten; F3 now gates the counter-witness
in-receipt (two strictly positive boundaries differing by a kernel
direction: identical interior potentials, different depth-3 transfers,
identical depth-`<=`-2 transfers).

**B2 — the uniqueness claim WITHDRAWN and restated.**  §4b rewritten;
new gate H1 measures 308/313 and 119/313 free directions.  The
existence result is untouched.

**M1 — evidence stratified.**  Every gate carries `[SUBSTANTIVE]` /
`[ANCHOR]` / `[DERIVED]` / `[THEOREM-PASS]`; H6 anchors the counts by
AST scan; the verdict reports them.

**M2 — the deformation comparison un-cherry-picked.**  New gate H2; the
three-way table is in §4a.

**M3 — the root-exclusion labelled toy-relative.**  New gate H3;
"removed" downgraded to "does not occur in this grammar".

**M4 — the citation-discipline breach recorded.**  The brief's banner
now carries scope and review status; the breach itself is logged at
#419 rather than repaired away.

**m1 — attribution corrected.**  The form `Z(h) = f(state) .
lambda^(-depth)` was pinned in **d42b56 A3** (#319/#321), before paper 30
§5.7.  The archaeology claim itself was checked by the referee and
**stands**: d42b56's receipt builds `Z` only from three boundaries and
constructs no eigenvector; d43b and d44a build `f` on states only.

**m2 — pin ordering declared.**  The pin was written concurrently with
the receipt, not strictly before it.  Declared in the pin's §0.

**m3 — anti-vacuity and witness branches.**  New gate H5 (AST scan,
labelled to exactly what it enforces: no literal conditions, every
condition references a computed name — it does NOT certify
falsifiability); the singular-matrix branch in F2/F5 is now exercised
every run by a deliberately singular probe.

**n1 — vacuous members split out.**  New gate H4.

Post-repair: **31 PASS / 0 FAIL**, exit 0, byte-identical across
`PYTHONHASHSEED` 0 / 7 / 61 / 999.  **TERMINAL.**
