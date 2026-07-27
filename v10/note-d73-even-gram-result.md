# D73 — result: **the even Gram is genuinely rank-2 and genuinely useless.** F1 does not fire at `N = 9` — `G^even` is an anisotropic positive-definite form with three distinct eigenvalues — but F1's *consequent* holds anyway: `E_total` is exactly as predictive as the full even vector, and no `N` can beat it because the trace already sits at the family's floor. **The pin's F1 is a biconditional and the two halves come apart.** Three further findings the pin did not pre-register: at `N = 5`, the bottom of the pin's own window, the Gram **is** exactly diagonal and F1 literally holds; the "reflection" in §25.4's *reflected* Gram acts as the **identity** on the even channel, so paper 30's even reflection positivity is a Gram-matrix tautology; and the per-record object is **rank 1** — rank 3 exists only in the ensemble.

**Status: GREEN-UNREVIEWED, 2026-07-27.** First delivery. No independent
hostile round has been run against this unit. Nothing here is
review-hardened and nothing here may be cited as such.

Pin `v10/note-d73-even-gram-pin.md` (STRICT, FROZEN, committed **before**
any code was written; it names claim P2, tests 1–3 and falsifiers F1–F4).
Receipt `v10/code/d73_even_gram_exact.py`, output
`v10/data/d73_even_gram_exact.out` — run from the repository root under
`python3.13` (the committed v7 campaign uses `int.bit_count`, so it needs
`>= 3.10`; the repo's default `python3` is 3.8 and cannot run it),
**29 PASS / 0 FAIL, exit 0, wall clock 457.5 s**.
Parents: D71c (`note-d71c-spin2-archaeology.md`), v2 paper 10 Prop 10.6,
v6 paper 4 `:1064` (`FAILS-FULL-GR`), v6 paper 54, D63/D67.

Every number below is quoted from the receipt's own stdout. **Where the
receipt and this note disagree, the receipt is authoritative.**

---

## 0. The one-paragraph answer

`v7/code/p30_reflection_positive_campaign.py:394-406` was lifted by AST
extraction, driven on a reconstructed `N = 1..9` record universe
(1, 2, 5, 16, 63, 315, 1956, 14794, **131526** canonical classes), and
its seven committed principal minors reproduced **character for
character** against the seven lines text-sliced out of paper 30 at
`:2991-2997`, together with the odd diagonal, the `i`-twisted minors and
the whole `§25.3` aggregate table. Then the matrix itself was printed —
**the corpus printed the minors and never printed the matrix.** It is
**not** a multiple of the identity and **not** diagonal at `N = 9`: three
distinct nonzero off-diagonals, three distinct diagonal entries,
eigenvalues `108.0449, 45.9226, 20.8323`, cubic discriminant exactly
positive, condition number `5.1864`. So **F1 does not fire, and P2's
rank-2 half is confirmed as a matter of fact.** But the promotion
`K(E) = k·E_total → K(E) = EᵀNE` was then run through paper 30's own four
gates on eleven choices of `N` — the identity, the Gram itself, its
adjugate, its covariance, two diagonals, two off-diagonal forms, a linear
control and the componentwise ceiling — and **every one of them lands on
the committed `TV_9 = 1.67603622405300634803560e-5` exactly**, with
identical recurrence error, zero dual-conjugation error and zero
coarsening violations. That is not eleven coincidences: paper 30's own
committed identity `TV_9(full) = TV_9(even_abs) = TV_9(agg_l2)` means the
**trace already achieves the ceiling of the entire family**, so no `N`
can improve it, ever, at this window. The even channel is
**structurally anisotropic and predictively trace-only**, and the pin's
F1 — which asserts that a non-identity Gram implies `E_total` is lossy in
the sense that matters — is **false as a biconditional**.

---

## 1. Gate-by-gate

| gate | verdict | what it settles |
|---|---|---|
| **G0-a/b/c** (3 anchors) | **PASS / PASS / PASS** | the campaign, the primitives and the *committed numbers* are each a single source. The Gram is gated character-for-character (`value += Fraction(count, total) * f(key) * g(target)`); the anchor targets are text-sliced out of the paper, not retyped. |
| **G1-a** | **PASS** [ANCHOR] | record census `[1,2,5,16,63,315,1956,14794,131526]`, 362880 permutations at `N = 9`. |
| **G1-b** | **PASS** [ANCHOR] | **the seven committed even principal minors reproduce string-for-string.** |
| **G1-c** | **PASS** [ANCHOR] | the odd diagonal `−26.0510…, −16.5258…, −29.7804…` and the seven `i`-twisted minors reproduce too. |
| **G1-d** | **PASS** [ANCHOR] | paper 30 `§25.3`'s `L1 / L2 / Linf` rows reproduce, atoms **and** 24-digit `TV_9`: `66039 / 66057 / 66036`. |
| **G1-e** | **PASS** [ANCHOR] | the two ceiling identities: `TV_9(even_abs) = TV_9(full)` and `TV_9(agg_l2) = TV_9(even_abs)`; `known` is `299.7×` worse, so the identity is not vacuous. |
| **G2-a** | PASS | the Gram is symmetric, and *for a reason*: `P(R*) = P(R)` on all 131526 classes. |
| **G2-b** | PASS | **F1 DECIDED — DOES NOT FIRE at `N = 9`.** |
| **G2-c** | PASS | **the reflection is the identity on the even channel and a sign on the odd one** — 0 violations in 394578 tests. |
| **G2-d** | PASS | three distinct positive eigenvalues, discriminant exactly `> 0`; char-poly coefficients *are* the committed minors. |
| **G2-e** | PASS | anisotropy nonzero; traceless share `0.2836` — a **minority**, reported as measured. |
| **G2-f** | PASS | the anisotropy survives removal of the rank-1 mean `μμᵀ`. |
| **G2-g** | PASS | it survives reweighting: raw class-uniform Gram is anisotropic too. |
| **G2-h** | PASS | **the `N = 5` Gram is exactly diagonal** (disjoint channel supports, gated); off-diagonals switch on at `N = 6/7`. |
| **G3-a** | PASS | **operationalization fidelity gated first**: `colors_for_K(·, sum)` reproduces p30's `agg_l2` colour dictionary key-for-key at every `N` in the window. |
| **G3-b** | PASS | **F2 does not fire** — the quadratic matches the committed `TV_9`. |
| **G3-c** | PASS | **and no `N` can improve it**: the componentwise ceiling equals the committed value. |
| **G3-d** | PASS | dual conjugation, atom identity and non-lookup hold for all 11 candidates. |
| **G3-e** | PASS | the trace is **lossy as a colouring** (atoms `66057 → 66059`, refines, 2 splits) and **lossless as a predictor**. |
| **G4-a** | PASS | **the per-record object is rank 1** — census `{rank 0: 3862, rank 1: 127664}`. |
| **G4-b** | PASS | `S_3` stabiliser of `G^even` = order **1**; the order-dual acts trivially; no sign freedom. |
| **G4-c** | PASS | the `FAILS-FULL-GR` answer, in p4's own units: deficit `789150`. |
| **G4-d** | PASS | the Prop-10.6 relation, stated as a *distinction*, with the one shared datum located. |
| **G5** | PASS [SAMPLED] | transfer probe on D63's winner `DOUBLE-RING(8,10,8)`. |
| **G6-a** | PASS | 30 gate predicates parsed, none flagged; the hoisting defect named. |
| **G6-b** | PASS | determinism under `PYTHONHASHSEED 0/7/999`, byte-identical digest. |
| **G6-c** | PASS | **negative control**: on a synthetic `7I` the same code reports traceless `= 0`, discriminant `= 0`, stabiliser order `6`. The F1 instrument fires when F1 is true. |

Exit 1 was reachable only at G0/G1 and was not reached.

---

## 2. The matrix the corpus never printed

`G^even_{jk} = Σ_R P(R) E_j(R) E_k(R*)` at `N = 9`, exact:

```text
  17902637/181440        411581/30240       1623817/90720
     411581/30240         203491/5040            6331/378
    1623817/90720             6331/378          57923/1620
```

```text
  98.6697365520282187   13.6104828042328042   17.8992173721340388
  13.6104828042328042   40.3751984126984127   16.7486772486772487
  17.8992173721340388   16.7486772486772487   35.7549382716049383
```

Characteristic polynomial, exact, with the committed minors as its
coefficients (`c₂` = the three `1×1`s, `c₁` = the three `2×2`s, `c₀` = the
`3×3`):

```text
  lam^3 - 174.79987323633156966 lam^2 + 8169.2078429803634417 lam - 103363.83796002682333
```

| quantity | value |
|---|---|
| eigenvalues (float port of certified rational brackets) | `108.044928115558159`, `45.922634116580272`, `20.832311004193138` |
| cubic discriminant (exact) | `1.84785e10 > 0` — three distinct real roots |
| condition number `λ_max/λ_min` | `5.18641105607` |
| `‖G − (tr/3)I‖²_F` / `‖G‖²_F` | `0.283583072514` |
| anisotropy ratio `‖traceless‖²_F / (tr²/3)` | `0.395835248491` |
| channel means `μ` | `(63/10, 21/5, 21/5)` — **channels 2 and 3 coincide** |
| channel variances | `58.9797, 22.7352, 18.1149` |
| `Cov = G − μμᵀ` off-diagonals | `−12.8495, −8.5608, −0.8913` — **all negative** |
| `Cov` eigenvalues | `64.4236, 21.2269, 14.1794`; anisotropy `0.4455` |
| raw (class-uniform) off-diagonals | `14.1265, 15.6007, 20.5577`; anisotropy `0.2814` |

The anisotropy is therefore not an artefact of the measure (G2-g), not an
artefact of the rank-1 mean (G2-f), and not a rounding residue (exact
rationals throughout). **P2's factual claim — that the corpus computed a
rank-2 object and threw it away — is confirmed.**

---

## 3. F1, decided — and the qualification the pin could not have written

F1 reads: *`G^even` is diagonal, or is a multiple of the identity.* At
`N = 9` neither holds. But the receipt swept the pin's **own declared
window** `N = 5..9`:

| `N` | trace | nonzero off-diagonals | anisotropy ratio | discriminant |
|---:|---|---:|---|---|
| 5 | `7/60` | **0 / 3** | `0.040816327` | `0` (repeated root) |
| 6 | `1.30833` | 2 / 3 | `0.088198304` | `1.52e-5` |
| 7 | `8.70794` | 3 / 3 | `0.173236730` | `20.99` |
| 8 | `43.2983` | 3 / 3 | `0.281181510` | `1.57e6` |
| 9 | `174.800` | 3 / 3 | `0.395835249` | `1.85e10` |

At `N = 5` the Gram is **exactly `diag(1/20, 1/30, 1/30)`** — diagonal,
with a repeated eigenvalue and a nontrivial `S_3` stabiliser. And the
reason is structural, gated not observed: the three even channels count
**5-element** induced subposets, so at `N = 5` every record has exactly
one 5-subset, the three channel indicators have **disjoint support** (0
of 63 records carry two channels at once), and `E_a E_b ≡ 0` for `a ≠ b`.

> **The off-diagonal is generated by record depth exceeding the flag
> size. It is not a property of the channels.** F1's literal condition is
> TRUE at `N = 5`, half-true at `N = 6`, and false from `N = 7` up.

This is the sharpest thing the unit found about F1, and it is not in the
pin. Anyone citing "the even Gram is anisotropic" must cite the window.

---

## 4. What the "reflected Gram" actually is — the deflation

Each of the three `DUAL_PAIRS` is gated to be a genuine order-dual pair
of 5-element record types (`dual_key(left, 5) == right`). It follows —
and the receipt verifies it exhaustively, **0 violations in 394578
tests** — that

```text
  E_j(R*) = +E_j(R)      O_j(R*) = -O_j(R)
```

identically. Therefore, as exact Fraction identities:

* the **reflected** even Gram **equals** the ordinary second-moment
  matrix `E[E_j E_k]`;
* the **reflected** odd Gram **equals** `−E[O_j O_k]`.

So paper 30 `§25.4`'s two results are algebra, not measurement. "The even
sector's reflected Gram is positive semidefinite" is the statement that a
second-moment matrix of three real observables is PSD — true of every
such matrix. "The real odd sector has negative reflected norm, repaired
by the `i`-twist" is the same tautology carrying the `Z/2` sign. **The
`i`-twist is not a discovery about the odd channel; it is the sign the
grading puts there by construction.** `[MEASURED]`, and this note claims
nothing about whether paper 30 believed otherwise.

What survives as content: the odd channel's means are **exactly zero** in
all three channels (a consequence of the same grading), and its
off-diagonals are mixed-sign (`−0.01220, −5.64990, +0.39107`) — so the
odd sector's off-diagonal structure, which paper 30 never scanned (it
swept 253 *diagonal* `M` and chose `diag(5,5,3)`), is nontrivial and
remains unexplored. That is residue 3.

---

## 5. The quadratic promotion: F2 dies, and so does the positive branch

`K(E) = k·E_total` was replaced by `K(E) = EᵀNE` in **exactly one slot**
of p30's own `colors_for_mode(..., 'agg_l2')` branch — a fidelity gate
(G3-a) requires the promoted colouring to reproduce p30's `agg_l2` colour
dictionary key-for-key at every `N` in the window before anything is
measured. All downstream machinery (`atom_weights`, `atom_metrics`,
`forward_tv`, `recurrence_errors`, `coarsening_identity`) is p30's,
unmodified.

| `N` | atoms₉ | `TV_9` | rec₉ | dual err |
|---|---:|---|---|---:|
| `k·E_total` **[committed]** | 66057 | `1.67603622405300634803560e-5` | `1.71467764060356653e-5` | 0 |
| `I` (the pin's `diag(k,k,k)`) | 66059 | *same* | *same* | 0 |
| `G^even` itself | 66059 | *same* | *same* | 0 |
| `adj(G^even) ~ G⁻¹` | 66059 | *same* | *same* | 0 |
| `Cov = G − μμᵀ` | 66059 | *same* | *same* | 0 |
| `diag(5,5,3)` | 66059 | *same* | *same* | 0 |
| `diag(1,2,3)` | 66059 | *same* | *same* | 0 |
| `I + offdiag(1)` | 66057 | *same* | *same* | 0 |
| `3I − offdiag(1)` | 66059 | *same* | *same* | 0 |
| linear contraction `k_j = Σ_k G_jk` | 66059 | *same* | *same* | 0 |
| **componentwise `(E₁,E₂,E₃)`** | 66059 | *same* | *same* | 0 |

**F2 does not fire**: the quadratic is fully consistent with the
receipted law — it is admissible on all four committed gates (dual
conjugation error 0 at 11/11, coarsening-identity violations 0 at 11/11,
max h-difference 0 at 11/11, 0 lookup colourings).

**And the pin's positive branch is structurally closed, not merely
unfired.** Any `K` whatsoever is a function of the 3-vector `E`, so its
colouring is a coarsening of the componentwise colouring, which is a
coarsening of p30's `full`. Hence `TV_9(any N) ≥ TV_9(componentwise) ≥
TV_9(full)`. G1-e measures `TV_9(full) = TV_9(agg_l2)` = the committed
value. **The trace already sits at the family's floor.** No search was
needed and none would have helped.

Two small consistency facts worth recording. `N = I + offdiag(1)` is the
all-ones matrix, giving `EᵀNE = (ΣE_j)²`, a bijection of `ΣE_j` on
nonnegative integers — and it reproduces the trace's atom count exactly
(`66057`, `+0` splits), as it must. And the pin's own phrase
"`N = diag(k,k,k)`" is loose: `EᵀIE = Σ_j E_j²`, **not** `k·Σ_j E_j`. The
receipt tests the literal quadratic and reports that it lands on the same
number anyway.

**The central measurement (G3-e).** The trace is *lossy as a colouring*
and *lossless as a predictor*: the componentwise even colouring strictly
refines the trace's partition at `N = 9` (every componentwise atom sits
inside one trace atom; atoms rise `66057 → 66059`; exactly 2 trace atoms
are split), so `E_total` genuinely discards information — but everything
it discards is predictively inert for the deletion-graph law at this
window. **The two halves of F1's consequent come apart.**

---

## 6. The `FAILS-FULL-GR` answer

v6 paper 4 `:1064` rejected the scalar→tensor shortcut on a component
count: *"a scalar potential equation has one response component per
screen atom; a two-dimensional symmetric tensor equation has three
components per atom, with differential constraints"* —
`missing_components = 8193`, verdict `FAILS-FULL-GR`.

**Half-cleared, still failing, and for a sharper reason.**

1. **Cleared, globally.** `G^even` supplies **6** independent components
   where `K(E) = k·E_total` supplied **1**. The count objection, at the
   global level, is answered.
2. **Failed, at the level p4 actually stated it.** Those 6 components are
   **one global form** for the entire `N = 9` window. p4's row counts
   components *per atom*. In p4's own units the deficit is
   `6 × 131526 − 6 = 789150`.
3. **Failed again, at a level p4 never needed.** The per-record summand
   of the Gram is `E_j(R)E_k(R*) = E_j(R)E_k(R)` — an outer product,
   **rank exactly 1** at every record with `E(R) ≠ 0` (census
   `{0: 3862, 1: 127664}`). Rank 3 appears *only after averaging*. A
   metric is a form at a point; this form exists only in the ensemble.
4. **Failed a third time, on equivariance — the decisive one.** A metric
   response must transform, `N → A N Aᵀ`, under whatever acts on the
   index it carries. Three candidates, all empty:
   * the substrate's one involution, paper 30's order-dual `*` (the same
     `Z/2` as Prop 10.6's and `χ^NN`'s), acts **trivially** on the even
     index and as a **sign** on the odd one;
   * relabelling the three dual pairs: the `S_3` stabiliser of `G^even`
     is the **identity alone**. Reported against the unit's own interest:
     channels 2 and 3 have *equal means* (`21/5` each) — a near-symmetry
     — and the second moment breaks it anyway, `G₂₂ ≠ G₃₃`;
   * sign freedom: every `E_j` is a nonnegative count (`min/max` over
     records `(0,54), (0,36), (0,29)`), so the basis is **canonically
     oriented** and no analogue of Prop 10.6's frame flip exists.

> **A scalar did not become a metric by interpretation. It became a
> covariance matrix, which is a different thing.** A Gram-derived `N` is
> a metric-shaped **ensemble summary statistic** with no atom index, no
> local rank, and no group acting on the index it does have.

The pin's epigraph — *"it has to become a form"* — is satisfied in the
weakest possible sense (it *is* a symmetric bilinear form) and fails in
every sense that would matter.

---

## 7. The Prop-10.6 relation, stated carefully

**This is the unit's biggest risk of being misquoted, so the statement is
made twice and gated once (G4-d).**

v2 paper 10 Prop 10.6 is an all-order no-go: the **signed** off-diagonal
`h^{12}` of a *frame* metric cannot be recovered from `Γ`-level
(endpoint-probability) data, because the staggered conjugation `S_2`
flips `h^{12}` while leaving every Born-squared kernel invariant. The
missing information is *representational phase data*, not a relabelling
convention.

> **`G^even₁₂ ≠ 0` is NOT a counterexample to Prop 10.6 and must never be
> cited as one.**

Reason, and it is the same reason both ways: `G^even` is built **from**
the endpoint measure `P(R)`, so by Prop 10.6's own argument it is
invariant under any representational sign flip. Its off-diagonal is
nonzero **not** because the shadow recovered an orientation, but because
the channel basis is *canonically oriented by counting* — precisely the
freedom Prop 10.6's frames have and these observables do not. The two
objects live on different index sets (a frame index versus a named list
of three 5-element record types) and have different symmetry groups
(a frame `Z/2` versus nothing at all).

What they **do** share, located exactly: **the orientation datum sits in
the odd sector in both.** Here the even Gram is blind to the order-dual
and the odd Gram changes sign under it (G2-c). So paper 30's even/odd
channel split reproduces Prop 10.6's diagonal/off-diagonal split *one
level down*, with the **sign carried by the odd channel** and the
**anisotropy by the even one** — which is D71c `§3.2`'s imported table
recovered on the generated line's own objects, and is the one place where
this unit's result and D72's P1 touch. It is a structural correspondence,
not a numerical one, and no numerical relation is claimed.

---

## 8. The transfer probe `[SAMPLED]`

Context grade, one blueprint, one depth, no sweep. Nothing in `§2–§7`
depends on it.

D63's own winner **`DOUBLE-RING(8, 10, 8)`** — 177 events, the only
configuration D63 found carrying 4-direction charts at `d = 2` — was
rebuilt from D63's own function object through the committed
`d42b1 → d47a → d55c → d58 → d60` chain (event counts 177 and 65 gated
against D63's and D60's published rows). Each wide chart's direction set
was given the same bilinear treatment: a co-occurrence Gram over the
chart's own SKY-B shadow rows.

* **59** charts with `|D| ≥ 4` at `d = 2`; **59** anisotropic, **0**
  identity-proportional. So the v7 fixture is **not special** in carrying
  a rank-2 object — the machinery transfers in shape.
* **And the hint runs the other way on the test that mattered.** G4-b's
  equivariance census, transferred verbatim, does *not* come back empty
  on the v10 side. The census is uniform: **all 59 charts have `|D| = 4`,
  a constant diagonal, and a relabelling stabiliser of order 8 in `S₄`**
  — i.e. the dihedral group of the square. Every one of them is a `4×4`
  circulant; the example at event 24 is `3/8` on the diagonal with
  off-diagonals `1/8` and `1/4`:

  ```text
    3/8   1/8   1/4   1/8
    1/8   3/8   1/8   1/4
    1/4   1/8   3/8   1/8
    1/8   1/4   1/8   3/8
  ```

  Where v7's three named dual pairs give a Gram with `S₃` stabiliser of
  order **1**, the v10 direction Grams give order **8 of 24**, at
  **59/59** charts.

> **The hint: if a rank-2 object on this programme is ever going to be a
> form rather than a table, the index it lives on should be the
> generated line's DIRECTION index, not v7's channel index.** The v7
> channel index is a list of three names; the v10 direction index is
> something a group can act on.

This licenses nothing beyond this blueprint at this depth, and in
particular **no** claim that any stabiliser found is a *substrate*
symmetry rather than an arithmetic coincidence of one small circuit.
`[SAMPLED]`.

---

## 9. Licensed claims, fixture-scoped

Every claim below is a statement about **one fixture**: the `N = 5..9`
record window of v7 paper 30's rooted boundary law, three named dual
pairs, one measure. No gravity claim, no continuum claim, and no claim
that any object here is a metric.

1. `[MEASURED, N = 9]` `G^even` is a positive-definite symmetric form
   with three distinct nonzero off-diagonals and three distinct
   eigenvalues `108.0449 / 45.9226 / 20.8323`. **F1 does not fire at
   `N = 9`.**
2. `[THEOREM at the fixture, gated]` `E_j(R*) = E_j(R)` and
   `O_j(R*) = −O_j(R)` identically; hence the reflected even Gram **is**
   `E[E_jE_k]` and the reflected odd Gram **is** `−E[O_jO_k]`. Paper 30
   `§25.4`'s positivity results are algebraic consequences of the
   grading.
3. `[MEASURED, window]` The `N = 5` Gram is exactly `diag(1/20,1/30,1/30)`
   because the three channel indicators have disjoint support at `N = 5`.
   **F1's literal condition holds at `N = 5` and fails from `N = 7`.**
4. `[THEOREM at the fixture]` No `N` — positive-definite or not, diagonal
   or not — can improve `TV_9` at this window, because the componentwise
   colouring, the ceiling of the whole family, already equals
   `TV_9(agg_l2)`. **F2 does not fire and its positive branch is
   structurally closed.**
5. `[MEASURED]` The trace is lossy as a colouring (`66057 → 66059`,
   2 atoms split) and lossless as a predictor.
6. `[MEASURED]` The per-record even Gram summand has rank ≤ 1
   (`{0: 3862, 1: 127664}`); the `S_3` stabiliser of `G^even` is trivial;
   the order-dual acts trivially on the even index. **A Gram-derived `N`
   is an ensemble summary statistic, not a metric response.**
7. `[STATED, not computed]` The relation to Prop 10.6 is a *distinction*
   (`§7`). The shared content is that the orientation datum lives in the
   odd sector.
8. `[SAMPLED]` One v10 wide-crystal blueprint (`DOUBLE-RING(8,10,8)`)
   carries anisotropic direction Grams at all 59 of its wide charts,
   every one a `4×4` circulant with constant diagonal and a relabelling
   stabiliser of order **8** in `S₄` — against v7's stabiliser order 1.

**Not licensed, and explicitly disclaimed:** that `G^even₁₂ ≠ 0` evades
Prop 10.6; that anything here is a metric, a response, a field, or a
graviton; that the `N = 9` anisotropy survives to any other window,
substrate or measure; that the v10 charts' stabilisers are substrate
symmetries.

---

## 10. What this does to P2, and to D71c `§7`

P2 asserted three things. **Fact one — the corpus computed a rank-2
object on the even channel and discarded it in favour of its trace — is
CONFIRMED, exactly and at the named line.** **Fact two — that `K` should
be `EᵀNE` — is ADMISSIBLE but EMPTY**: the promotion passes every gate the
committed law imposes and buys nothing, and cannot buy anything at this
window. **Fact three — that the orientation is the datum that decides
geometry versus bookkeeping — SURVIVES AND SHARPENS**: the orientation is
exactly what the even channel lacks (its basis is canonically oriented,
so there is no orientation to have) and exactly what the odd channel
carries (the `Z/2` sign). D71c `§4.3`'s parallel — that the corpus prices
the trace of a rank-2 object and discards the traceless part — is
confirmed at the mechanical level and **deflated at the significance
level**: the discarded traceless part is a covariance, and it was inert.

**F1 must be restated before it is cited.** As written it is a
biconditional: *Gram ∝ I ⟺ `E_total` lossless ⟺ the even channel cannot
host a metric.* The receipt separates all three. The corpus does gain a
no-go, but it is not the one F1 drafted; it is:

> **D73 no-go (fixture-scoped).** *At the `N = 5..9` window of the rooted
> boundary law, the dual-even channel's second-moment form is
> anisotropic and positive-definite, and is nonetheless predictively
> equivalent to its trace for the deletion-graph law — no quadratic
> promotion can do better, because the componentwise colouring already
> attains the floor. The form carries no atom index, has rank 1 locally,
> and admits no group action on its channel index. On this substrate the
> even channel hosts a covariance, not a metric response.*

---

## 11. Residues

1. **The `N`-dependence is unexplained.** The anisotropy ratio rises
   monotonically `0.0408 → 0.0882 → 0.1732 → 0.2812 → 0.3958` across
   `N = 5..9` and shows no sign of saturating. Whether it converges,
   diverges or is a finite-`N` artefact of `9!` is **open** and is a
   `N = 10` question the receipt did not attempt (the universe build
   already dominates its runtime at `N = 9`).
2. **The pin's test 3 (the orientation test / cross-link to D71b's P1) is
   not run here.** This unit gates the even/odd grading exactly
   (`§4`) and locates the sign in the odd channel, but does not form
   `A_D` or ask whether it is odd under `*`. **That is D72's object and
   F4 remains undecided by this unit.**
3. **The odd sector's off-diagonal is still unexplored.** Paper 30 swept
   253 *diagonal* `M` for `Q_M(O) = OᵀMO` and never scanned the
   off-diagonal sector. This receipt measures the odd Gram's
   off-diagonals as `−0.01220, −5.64990, +0.39107` — mixed sign,
   one of them large — but does **not** promote `Q_odd`. The obvious
   successor unit is the *odd*-sector promotion, and by the ceiling
   argument of `§5` it is subject to exactly the same floor.
4. **The transfer probe is one blueprint at one depth.** Whether the
   v10 direction-Gram stabilisers are substrate symmetries is
   **open**, and it is the only lead this unit produces for a form that
   could be equivariant.
5. **The `known` baseline is `299.7×` worse than the even/odd
   colourings.** So the even/odd *data* are strongly load-bearing; it is
   only the *decomposition beyond the trace* that is inert. Anyone
   reading `§5` as "the even channel does not matter" has misread it.
6. **An environment fact worth committing.** The committed v7 campaign
   `p30_reflection_positive_campaign.py` calls `int.bit_count()`
   (`:165`), which requires Python **≥ 3.10**. The repository's default
   `python3` in this environment is 3.8 and the committed receipt
   **crashes** under it (`AttributeError: 'int' object has no attribute
   'bit_count'`). It reproduces cleanly under 3.13 (13/13 PASS, 5 min
   17 s), and this receipt was run the same way. No v7 number is in
   doubt; the reproduction instruction is.
7. **`missing_components = 8193` was not recomputed.** v6 paper 4's own
   receipt (`code/v6_p4e_screen_tensor_gravity_gate.py`) is not present
   in the tree; the row is quoted from the paper and the deficit
   computed here (`789150`) is stated *in p4's units*, not verified
   against p4's code. `[STATED]`.
