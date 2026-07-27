# D70 — result: **the horizon-limit route is NOT closed, and it is not open either — it fails the pin's own wider-pool clause, on one two-term row, while everything else it was built to test comes back positive.** Outcome **HZ-I** by the letter of the pin, with three findings the pin did not pre-register: the root's committed contraction **reverses** at the one horizon D46b could not compute; the truncation-convention horn is **object-dependent**; and the regenerative proof engine (D69 route R5) is **structurally closed**, not merely unfired. The aggregation arm returns **HZ5-b**: type-only and budget-only both blow up, so D69's routes R1 and R2 close at D57's grade.

**Status: GREEN-UNREVIEWED, 2026-07-27.**  First delivery.  No
independent hostile round has been run against this unit.  Nothing here
is review-hardened and nothing here may be cited as such.

Pin `note-d70-horizon-limit-pin.md` (STRICT, frozen and committed
**before** any code was written; it named this note and the receipt
before either existed).  Receipt
`v10/code/d70_horizon_limit_exact.py`, output
`v10/data/d70_horizon_limit_exact.out` — run from the repository root,
**exit 0**, wall clock printed by the receipt itself.  Campaign: THE
MEASURE CAMPAIGN, opened at LOG #481, scoped by
`note-d69-measure-campaign-scoping.md` (route **R4**, with R5 as its
intended proof engine and R1+R2 as the HZ5 arm).

Every number below is quoted from the receipt's own stdout.  **Where the
receipt and this note disagree, the receipt is authoritative** (LOG
#477's standing rule).

---

## 0. The one-paragraph answer

D46b's relative-horizon kernels `k_r(e|h) = q(e|h)·G(h+e, r−1)/G(h, r)`
were extended from a 30,729-history family at relative horizons `r = 1,
2` to a **243,769-history** family at `r = 1..7`, at **three actor
pools**, under **two declared terminal conventions**, with a renewal
analysis, an aggregation arm, four controls and a wall diagnostic.  The
kernels are **proper everywhere they are computable** and the chained
measure is **cut-additive at every cut** — so outcome HZ-IV does not
fire and the finite-horizon objects are honest measures.  The drift
**contracts over the computed horizons at every off-root depth, in all
five norms, at two and three actors**.  It does **not** contract at four
actors: the depth-1 row rises between the only two horizons that pool's
cap can reach — by 0.19% in `L∞`, 3.06% in `L1` and **14.95% in
sector-`L∞`**.  That is the pin's HZ-I clause (c), stated in advance,
and the receipt does not re-adjudicate it after the fact — so **HZ-I is
the delivered outcome**.  Underneath it, three things the pin
did not anticipate: D46b's committed statement that the **root** drift
contracts monotonically out to `r = 6` is **false at `r = 7`**; the
truncation-convention horn separates on the **horizon-bound** absolute
kernel and not on the **pinned** conditional, so the horn is
object-dependent and reporting one object alone would have decided it by
choice of statistic; and the regenerative route is closed by a
structural fact — **holdings never shrink**, so the menu-exact renewal
class is left exactly once and never re-entered.

---

## 1. Gate-by-gate

| gate | verdict | what it settles |
|---|---|---|
| **HZ0** (14 anchors) | **all PASS** | every committed D46b / D56 / D57 / D65 number this unit stands on reproduces in-process.  Exit 1 was reachable only here and was not reached. |
| **HZ1-a/b/c** | PASS / PASS / PASS | properness extended from `r = 1, 2` family-wide to `r = 1..7`; strict positivity and non-negativity; **cut-additivity of the chained measure**, against a raw weight that is *not* additive. |
| **HZ2-a** | PASS | drift contracts at every **off-root** depth, all five norms, two-actor arm. |
| **HZ2-b** | PASS | the family-uniform sup is **window-dependent**; both windows printed. |
| **HZ2-c** | **FAIL — the pre-registered negative** | one off-root row at the **four-actor** pool does not contract.  This is HZ-I clause (c). |
| **HZ2-d** | PASS | D46b's five root steps reproduce and are norm-free; the **sixth reverses**, delivered as its own outcome. |
| **HZ3-a** | PASS | the three declared conventions are what they are declared to be; C3 is gated to be a pure horizon shift. |
| **HZ3-b** | PASS | conventions differ at **every** history; the **pinned** object is convention-free at the root at every horizon and shrinks off it. |
| **HZ4-i/ii(a)/ii(b)/iii/iv/v** | all PASS | renewal predicate verified against the layer; holdings monotone; departure census; ladder cylinders; **no bound exhibited**; positive control finds d42a's renewal. |
| **HZ5-0/1/2/3** | all PASS | both coarser sector maps blow up, with the S4 lower-bound control and the S3 split witness; the finite-alphabet prerequisite left `[OPEN]` in both directions. |
| **HZ6-i/ii/iii/iv** | all PASS | the instrument can fail; the pipeline reproduces `Ẑ`; anti-vacuity scan clean with its defect named; hash-seed determinism. |
| **HZ7** | PASS | the B1 ladder does **not** survive the restricted enumerator — diagnostic only. |
| **HZ8-a/b/c** | all PASS | no infinite-volume claim (scanned); the pin's lexical prohibition enforced on the gate labels; every normalization named. |

**41 PASS / 1 FAIL, 4 delivered outcomes, exit 0, wall clock 534.8 s**
(the two-actor depth-6 build alone is 206.1 s).  The single FAIL is the
outcome, not a breakage: the pin's §7 requires exit 0 for every
substantive negative and exit 1 only on HZ0 anchor breakage.  **Nothing
was cut** — every arm the pin declares ran, including HZ5, which the pin
explicitly allowed to be dropped if the runtime budget bound.  The four
delivered outcomes are **HZ-I**, **HZ5-b**, and the two the pin did not
pre-register: **HZ2-ROOT-REVERSAL** (§4.3) and **HZ3-HORN** (§5.2).

---

## 2. HZ0 — the anchors, all fourteen

Reproduced in this receipt's own process, from the committed layers:

* **ARM-1T census** `[1, 9, 69, 521, 3969, 30729]` and **243,769** to
  depth 6.  D46b held menus to depth 5 and D56 obtained its depth-6
  count by summing menu sizes at depth 5; **this receipt holds the
  menus themselves to depth 6**, so 243,769 is an enumerated family
  here and not a count.  Per level: `1, 8, 60, 452, 3448, 26760,
  213040`.
* **the quarter-quantized ladder** `{2: 3757, 5/2: 212}` at depth ≤ 4
  and `{2: 29605, 5/2: 1124}` at depth ≤ 5 (both committed); the value
  set is unchanged at depth ≤ 6 — `{2: 237269, 5/2: 6500}` — which is
  this unit's own one-level extension.
* **the delivery-free partner** rebuilt from the committed d42b3 layer:
  `[1, 7, 39, 215, 1191, 6471]` to depth 5 and **34,375** to depth 6;
  census `{2: 5963, 5/2: 508}`.
* **the transport potentials** `G_1..G_6 = 2, 4, 257/32, 1035/64,
  4173/128, 134587/2048`; **the delivery-free potentials** `2, 4,
  257/32, 1037/64, 2101/64, 68313/1024`, identical through `D = 3` and
  first separating at `D = 4`.
* **both ratio columns** exactly, with the sign and the turnover:
  delivery-free ≥ transport at every horizon, transport peaking at
  `D = 5` and turning down at `D = 6`.
* **the root sector-normalized conditional**, drift exactly zero at
  `r = 1..6`.
* **the root absolute drift** in all three norms (D46b MB3-b).
* **the off-root conditional sup** `1/18, 4/171, 8/741, 176/32877` over
  `3969, 521, 69, 9` histories with `700, 140, 36, 4` drifting — taken
  **in D46b's own window** `len(h) + r ≤ 5`, because a sup over a wider
  family is a different number.
* **the family-uniform sup** `3/110, 3/253, 373/69230, 2333/1838829`,
  same window.
* **MB5**: the `1/256` reconvergence witness, matched-horizon equality
  at `r = 1, 2, 3`, and the non-sufficiency census `8196/30728`,
  `1060/3968`, `104/520`.

**New, and anchored to nothing** (the extension the deeper family
buys): `G_7 = 2168717/16384` at transport and `139065/1024`
delivery-free; transport ratio at `D = 7` = `2168717/1076696`
(~2.014233), continuing down from the `D = 5` peak.

---

## 3. HZ1 — properness, extended

`Σ_e k_r(e|h) = 1` is an **identity of the construction** — `G(h, r)`
is *defined* as `Σ_e q(e|h)G(h+e, r−1)` and `k_r` divides by it — and
the receipt says so before printing it.  Verifying it is a regression
tripwire on the AST extraction and the menu bookkeeping.  What is new
is the **extent**: D46b had it family-wide at `r = 1` (30,729) and
`r = 2` (3,969); here it holds at **every history of the depth-6 family
with a computable `k_r`**:

| `r` | histories | `Σ_e k_r = 1` |
|---|---|---|
| 1 | 243,769 | exactly |
| 2 | 30,729 | exactly |
| 3 | 3,969 | exactly |
| 4 | 521 | exactly |
| 5 | 69 | exactly |
| 6 | 9 | exactly |
| 7 | 1 | exactly |

The pin's weak POSITIVE lean on HZ1 at `r ≥ 3` family-wide is
**confirmed at these caps**.  Outcome HZ-IV is not entered by this
route.

**The substantive half.**  Every potential is strictly positive (the
committed layer always emits the idle option at weight ≥ `1/4`), every
kernel entry is `≥ 0`, and — the transport analogue of §B2.10's
cut-mass defect — the **raw** path weight is *not* a measure at
transport either: its cut masses are exactly the root potentials
`1, 2, 4, 257/32, 1035/64, 4173/128, 134587/2048`.  What the horizon
normalization buys is precisely this: chaining `k_R, k_{R−1}, …, k_1`
from the root gives total mass **exactly 1 at every intermediate cut**,
for every `R = 1..7`, with **0 violations**.  So the finite-horizon
objects are honest measures — at the price of the horizon dependence
HZ2 and HZ3 then measure.

---

## 4. HZ2 — the Cauchy table

### 4.1 The window-controlled table (the one that matters)

A family-uniform sup at horizon `r` is taken over histories of depth
`≤ 6 − r`, so **the window shrinks as `r` grows** and a family-uniform
sequence falling in `r` proves nothing on its own.  The rows below fix
the history depth `L` and vary `r`.  Two-actor arm, `L∞` on the
absolute kernel, exact:

| `L` | `r=1→2` | `r=2→3` | `r=3→4` | `r=4→5` | `r=5→6` | `r=6→7` |
|---|---|---|---|---|---|---|
| 0 | 0 | 1/1028 | 191/265995 | 412/1439685 | 4629/187210517 | **54193948/291881114879** |
| 1 | 3/208 | 1/156 | 1/356 | 2333/1838829 | 12494788/19065729755 | — |
| 2 | 3/110 | 3/253 | 373/69230 | 89364/36687385 | — | — |
| 3 | 3/110 | 3/253 | 373/69230 | — | — | — |
| 4 | 3/110 | 3/253 | — | — | — | — |
| 5 | 3/110 | — | — | — | — | — |

and the **pinned object**, `L∞` on the sector-normalized conditional:

| `L` | `r=1→2` | `r=2→3` | `r=3→4` | `r=4→5` | `r=5→6` | `r=6→7` |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1/18 | 4/171 | 8/741 | 176/32877 | 302623/103087098 | — |
| 2 | 1/18 | 4/171 | 8/741 | 176/32877 | — | — |
| 3 | 1/18 | 4/171 | 8/741 | — | — | — |
| 4 | 1/18 | 4/171 | — | — | — | — |
| 5 | 1/18 | — | — | — | — | — |

**Every off-root row contracts, in all five norms** (`L∞`, `L1` and
sector-`L∞` on the absolute kernel; `L∞` and `L1` on the conditional).
The **root** row of the three *absolute* norms does not — see §4.3.
The root row of the pinned object is identically zero at every horizon.

The word "converges" appears nowhere in any gate label, and the
receipt enforces that lexically (HZ8-b) conditional on HZ4's actual
outcome.  The standing wording is **"contracts over the computed
horizons"**.

### 4.2 The family-uniform row and its window dependence

| norm | `r=1→2` | `r=2→3` | `r=3→4` | `r=4→5` | `r=5→6` | `r=6→7` |
|---|---|---|---|---|---|---|
| `L∞` abs | 3/110 | 3/253 | 373/69230 | 89364/36687385 | 12494788/19065729755 | 54193948/291881114879 |
| `L1` abs | 6/55 | 12/253 | 746/34615 | 357456/36687385 | 74555672/19065729755 | 325163688/291881114879 |
| sector-`L∞` | 3/55 | 6/253 | 373/34615 | 178728/36687385 | 24989576/19065729755 | 162581844/291881114879 |
| `L∞` cond | 1/18 | 4/171 | 8/741 | 176/32877 | 302623/103087098 | 0 |
| `L1` cond | 1/9 | 8/171 | 16/741 | 352/32877 | 302623/51543549 | 0 |

**All five contract.**  But the fourth term is **not** D46b's:

| `r` | D46b window (`len(h)+r ≤ 5`) | this receipt (`len(h)+r ≤ 6`) | larger? |
|---|---|---|---|
| 1 | 3/110 | 3/110 | no |
| 2 | 3/253 | 3/253 | no |
| 3 | 373/69230 | 373/69230 | no |
| 4 | **2333/1838829** (~1.269e-3) | **89364/36687385** (~2.436e-3) | **yes, ×1.92** |

**D46b's committed four-term sequence is a LOWER BOUND on the sup over
the deeper family**, and its last term understates it by a factor of
about 1.92.  Quoting it as if it were window-free would be the
horizon-mismatch error D46b's own round 1 convicted in the other
direction.  Both columns are printed side by side in the receipt.

### 4.3 The root reversal — outcome `HZ2-ROOT-REVERSAL`

D46b MB3-e gated that the root's absolute drift *"contracts
monotonically at the root from `r = 2` on, out to `r = 6`"*, which was
true of every step it could compute.  This receipt computes one more:

```
root L-inf drift, r = 1..7:
  0,  1/1028,  191/265995,  412/1439685,  4629/187210517,
  54193948/291881114879
ratio sequence:  0.7382,  0.3985,  0.0864,  7.5091
```

**It falls through D46b's five steps and then rises by a factor
`≈ 7.51` at the sixth.**  The reversal is exact, is **identical in all
three norms** (the `L∞`, `L1` and sector-`L∞` ratio sequences are
exactly equal, rational for rational, over all four ratios), and is the
same shape as the reversal D46b's own round 1 found in the growth
column — a finite-horizon quantity read as a trend over five points
that turns at the sixth.

**What it does not touch.**  The **pinned** object.  The
sector-normalized conditional at the root is exactly zero at every one
of the six steps including `r = 6 → 7`, and every off-root stratum
contracts in all five norms.  So the object that reverses is the
**horizon-bound absolute kernel** — precisely the quantity D44f says is
horizon-bound — and the object the pin names is untouched.  This is the
**mirror image** of the pin's falsifier 2 ("drift zero at the root and
non-contracting family-wide"): here the family contracts and the root
does not.  The pin did not pre-register this direction, so it is
delivered as its own outcome and is **not** counted as HZ-I.

### 4.4 Actor pools — and the clause that fires

Pools are exact and exhaustive at the printed depths; **no sampled arm
is run anywhere in this receipt**.

```
2 actors (A,B)      depth 6, cumulative [1, 9, 69, 521, 3969, 30729, 243769]
3 actors (A,B,C)    depth 4, cumulative [1, 16, 235, 3424, 50617]
4 actors (A,B,C,D)  depth 3, cumulative [1, 25, 593, 13993]
```

Matched-cell comparison (same `r`, same `L`, `L∞` absolute, exact):

| `(r, L)` | 2 actors | 3 actors | 4 actors |
|---|---|---|---|
| (1, 0) | 0 | 0 | 0 |
| (1, 1) | 3/208 | 11/1752 | 29/8288 |
| (1, 2) | 3/110 | 161/7080 | 105/8416 |
| (2, 0) | 1/1028 | 1/1734 | 3/8216 |
| (2, 1) | 1/156 | 2763/523994 | 23117/6594399 |

**The drift MAGNITUDE falls with actor pool in every matched cell** —
the two-actor arm is the worst case, not an unrepresentative one, which
is the opposite of what falsifier 4 feared.  But:

> **THE FAILING ROWS, in full.**  At **four actors**, depth `L = 1`,
> two terms (the only two horizons that pool's cap can reach), in all
> three absolute norms:
>
> | norm | `r = 1→2` | `r = 2→3` | rise |
> |---|---|---|---|
> | `L∞` | 29/8288 (~3.499035e-03) | 23117/6594399 (~3.505551e-03) | **1375/738369 ≈ +0.19%** |
> | `L1` | 87/4144 (~2.099421e-02) | 1160/53613 (~2.163654e-02) | **19/621 ≈ +3.06%** |
> | sector-`L∞` | 39/4144 (~9.411197e-03) | 580/53613 (~1.081827e-02) | **1207/8073 ≈ +14.95%** |

That is the pin's **HZ-I clause (c)**, *"or fails at wider pools"*,
and its **falsifier 4**.  It was pre-registered before the run and the
receipt does not re-adjudicate it afterwards.  **The rise is an order
of magnitude larger in sector-`L∞` than in `L∞`, so quoting one norm
would have understated it** — which is exactly why the pin requires
the three norms reported separately and never merged.

Reported at its exact grade, and both ways: it is **one depth row**,
**two terms**, at the **shallowest declared cap** (depth 3), and it is
the **only** off-root row that fails at any pool.  At two and three
actors the only failing rows are the root rows of §4.3.  What four
actors shows is not a drift that is growing fast but a drift that is
**small in magnitude and has stopped falling** — and in the
sector-norm, has turned up appreciably.

**Whether that is saturation or non-contraction cannot be decided at
depth 3, and this unit does not decide it.**  The pin's clause is
binary and it fired; the honest reading of *why* it fired needs a
four-actor family at depth 4, which is the first named residue (§10).

---

## 5. HZ3 — the horn gate

### 5.1 A correction to the pin's own suggested pattern, made in place

The pin proposes *"the committed one, plus a second — e.g. the D57 S4
pattern of a maximally coarse terminal"*.  But **the committed terminal
IS already the maximally coarse one**: `G(h, 0) = 1` is
state-independent and there is nothing coarser.  The S4 pattern
therefore **inverts** here — a second convention must **refine** the
terminal.  Three are declared:

* **C1** (committed, D46b): `G(h, 0) = 1`.  Maximally coarse.
* **C2** (branch-count terminal): `G(h, 0) = |menu(h)|` — counting
  measure at the cap layer instead of uniform measure.
* **C3** (menu-mass terminal): `G(h, 0) = Σ_e q(e|h)` — **declared and
  gated to be exactly a horizon shift of C1** (`G^{C3}(·, r) =
  G^{C1}(·, r+1)` at every horizon, and `k^{C3}_r = k^{C1}_{r+1}`
  entrywise over the family).  It is carried precisely so that C2's
  separation cannot be mistaken for a reparametrization.

### 5.2 The result — outcome `HZ3-HORN`

**(i) The conventions are genuinely different completions.**  Over the
whole comparison (`len(h) + r ≤ 6`), the number of histories with
`k^{C1}_r = k^{C2}_r` is **zero**.  Not one.

**(ii) On the PINNED object the choice is invisible at the root and
shrinks off it.**  The sector-normalized conditional's C1-vs-C2
difference at the root is **exactly 0 at every computed horizon**
(`r = 1..6`), while the absolute kernel's is never 0.  Off the root it
shrinks in `r` at **every** fixed depth:

| `L` | `r=1` | `r=2` | `r=3` | `r=4` | `r=5` |
|---|---|---|---|---|---|
| 1 | 1/8 | 1/12 | 487/7790 | 40337/800358 | 109092211/2569013838 |
| 2 | 1/8 | 1/12 | 487/7790 | 7443521/132068175 | — |
| 3 | 1/8 | 1/12 | 487/7790 | — | — |

**(iii) On the ABSOLUTE kernel it does not.**  Two of the six depth
rows are non-monotone — the root row (rising at `r = 5` and `r = 6`)
and `L = 3` (`7/200 → 559/16776 → 29255/822216`, up at `r = 3`).

> **SO THE HORN IS OBJECT-DEPENDENT.**  On the pin's own object
> (§6 of the pin: *"the pinned object is the SECTOR-NORMALIZED
> CONDITIONAL; absolute completed weights are horizon-bound (D44f) and
> are context"*) the **imported completion horn (I) does NOT fire over
> the computed horizons**.  On the horizon-bound object it does.
> Reporting one without the other would have decided the horn by choice
> of statistic; the receipt gates the verdict on the pinned object and
> prints the absolute rows in full beside it.

**And the size is not small.**  `1/8` at `r = 1` is the conditional's
separation over 30,729 histories, decaying to `~0.0425` by `r = 5` over
9 histories.  **The conventions are far apart where the family is large
and close only where the window is small.**  Nothing is extrapolated
past the computed horizons.

---

## 6. HZ4 — the lemma slot: NO BOUND, and none available by this route

### 6.1 The renewal predicate, and the two ports coming apart

D62 row R4's serialisation (`hold = {A: v, B: v}`, `live = ()`,
`comps = ()`, `refs = {v}`, `flag(v) = False`) is ported to transport
**two** ways, because the port is not unique and reporting one would
decide the question by fiat:

* **R-SIG** — every actor's **non-superseded** holdings is the same
  singleton `{v}`; no live proposals, no components, no merge pairs.
  (The literal R4 port: d42a's `sigma` sees the non-superseded token
  only, because `prop_options_in_view` **skips** superseded.)
* **R-MENU** — R-SIG **and** `holdings(a) = {v}` exactly for every `a`.
  (The menu-exact port: at transport `deliver_options_in_view`
  enumerates over the **whole** holdings set.)

Verified against the committed layer at every occurrence, over the
declared window (depth ≤ 5, where full views are affordable):

| | count | menu = root's menu under renaming |
|---|---|---|
| **R-SIG** | **5,161** | **1,365 yes / 3,796 NO** |
| **R-MENU** | **1,365** | **1,365 yes / 0 no** |

**The literal D62 port is NOT sufficient for a menu renewal at
transport scope**, and the gap is exhibited: at the first failing point
the delivery options are four at `1/8` where the renamed root menu has
two at `1/4` — because the actor still holds a superseded `v0` and the
delivery enumerator reads it.  **This is the B1 wall showing up inside
the renewal question**, and it is the same one line of the committed
layer that HZ7 probes.  The R-MENU points are exactly `4^n` at depth
`n` (1, 4, 16, 64, 256, 1024 = 1,365) — the histories built only from
idles and re-deliveries of the genesis version.

**Positive control (HZ4-v):** at delivery-free d42a scope the same
predicate machinery finds renewals, and at **every** one of them the
menu is the root's under renaming, weight for weight — **including at
every history ending in a pair-arb**, which is D62 row R4's derived
statement re-derived here through this receipt's own predicate.  So the
transport negative is a fact about transport, not about the instrument.

### 6.2 The structural fact that decides the census

> **HZ4-ii(a): holdings are monotone along every transition** —
> exhaustively verified over the declared window, **0 shrinking
> transitions**.  `View.holdings` in the committed layer is a union
> over the arbs, deliveries and merges in the view, so extending a
> history can only add to it.

Together with R-MENU (which requires `holdings(a) = {v}` exactly), this
makes the menu-exact renewal set **absorbing-complement**: *once any
actor holds a second version, no continuation of that history is ever a
menu renewal again.*

### 6.3 The return-weight census is a departure census

Normalizations named at every use: `q` is the **raw** committed weight
product; `k^{C1}` is the **horizon-7 completed conditional** chained
from the root under convention C1.

| cycle length `n` | renewal histories | raw-`q` mass | `k^{C1}` mass at a renewal | `k^{C1}` mass NOT at a renewal |
|---|---|---|---|---|
| 1 | 4 | 3/2 | 1615044/2168717 (~0.7447) | ~0.2553 |
| 2 | 16 | 9/4 | 1201824/2168717 (~0.5542) | ~0.4458 |
| 3 | 64 | 27/8 | 894240/2168717 (~0.4123) | ~0.5877 |
| 4 | 256 | 81/16 | 666144/2168717 (~0.3072) | ~0.6928 |
| 5 | 1024 | 243/32 | 497664/2168717 (~0.2295) | **~0.7705** |

There are no cycles, only a survival curve.  The raw-`q` renewal mass
is exactly `(3/2)^n` and the renewal count exactly `4^n`.

### 6.4 The B1 ladder's weight census, and why it does not help

| rung `k` | admissible | `q`(propose) | `q`(self-arb) | `|holdings(A)|` | cylinder weight `∏q` |
|---|---|---|---|---|---|
| 1 | yes | 1/8 | 1/4 | 2 | 1/32 |
| 2 | yes | 1/8 | 1/4 | 3 | 1/1024 |
| 3 | yes | 1/8 | 1/4 | 4 | 1/32768 |
| 4 | yes | 1/8 | 1/4 | 5 | 1/1048576 |
| 5 | yes | 1/8 | 1/4 | 6 | 1/33554432 |
| 6 | yes | 1/8 | 1/4 | 7 | 1/1073741824 |
| 7 | yes | 1/8 | 1/4 | 8 | 1/34359738368 |
| 8 | yes | 1/8 | 1/4 | 9 | 1/1099511627776 |

The single ladder cylinder's weight **does** vanish, rung by rung, at
exactly `1/32` per rung.  So **the pin's falsifier 5, read narrowly
("the ladder's cylinders carry non-vanishing weight"), does NOT
fire.**  It does not help: by §6.2 the ladder is not the object that
matters — the **never-regenerating set is everything past the first
creation event**, and it carries **~0.77** of the horizon-completed
mass at depth 5, rising with depth.

### 6.5 The minorization attempt — **NO BOUND EXHIBITED**

A Doeblin/regenerative bound needs `δ > 0` with: from **every** history,
the probability of hitting a renewal within `N` steps is `≥ δ`.
Computed directly under the horizon-completed conditional:

| `N` | histories tested | hitting probability exactly 0 | infimum |
|---|---|---|---|
| 1 | 3,969 | 3,628 | **0** |
| 2 | 521 | 436 | **0** |
| 3 | 69 | 48 | **0** |

**There is no minorization constant to print.**  And it is zero for a
**structural** reason, not for want of depth: by §6.2 every history in
which some actor already holds two versions has hitting probability
exactly 0 for **every** `N`, not merely for the `N` computed.

> **D69's route R5 — the regenerative / atom route, "the route the
> corpus implies and has never named" — is therefore CLOSED as a proof
> engine for this unit's bound, not merely unfired.**  D69 §3 R5(c)
> guessed the failure mode as *"the return weight is not bounded below
> uniformly"*; the actual failure is harder than that — **the return
> weight is exactly zero** for almost every history, because the
> renewal class is left once and never re-entered.

Per the pin: **nothing in HZ4 upgrades any HZ2 label**, HZ2's rows stay
a table over the computed horizons, and outcome HZ-III's bound clause
is not satisfied.

---

## 7. HZ5 — the aggregation arm: both residues close (**HZ5-b**)

D57's coarsest-lumpable fixpoint, recomputed at the two strictly
coarser sector maps D57's own residue list named as untested.  **Not
dropped** — the runtime budget did not bind, and the receipt says so.

**The maps, and one structural fact found on the way (HZ5-0).**
`(actor, type)` (10 sectors on the full family) refines **TYPE-ONLY**
(5 sectors) refines **BUDGET-ONLY** (4 sectors: propose /
arb-and-merge / deliver / idle).  But budget-only merges `r` and `m`,
so **it is strictly coarser than type-only only once merge events
appear in the family** — which first happens at cumulative depth 5.
Below that the two maps coincide at 4 sectors each.  That is d42b1's
own declared MERGE-SECTOR VACUITY showing up as a sector-map fact.

**The finite-alphabet prerequisite, gated FIRST and SEPARATELY.**
Distinct sector totals by cap — type-only `4, 4, 5, 6`; budget-only
`4, 4, 5, 5`.  **Left `[OPEN]` in both directions**, as D69 §6 requires:
not extrapolated to finiteness and not extrapolated to blow-up.  D57's
precedent is the reason for the caution — it pre-registered this
prerequisite, published a refutation, and the refutation was withdrawn
in round.

**The decider, stated as implemented** (D57 round-1 MINOR 6, carried
verbatim): *for every depth carrying at least three cap values, do the
LAST TWO cap values agree?*  No other threshold is used and none is
invented.

| depth | type-only cap3/4/5/6 | budget-only cap3/4/5/6 |
|---|---|---|
| 0 | 1, 1, 1, 1 | 1, 1, 1, 1 |
| 1 | 2, 2, 2, 2 | 2, 2, 2, 2 |
| 2 | 6, 6, 6, 6 | 6, 6, 6, 6 |
| 3 | 5, 10, 10, **11** | 5, 10, 10, **11** |
| 4 | —, 6, 14, **16** | —, 6, 14, **16** |
| 5 | —, —, 7, **19** | —, —, 7, **19** |
| 6 | —, —, —, 10 | —, —, —, 9 |

`(depth, stable-at-last-two-caps) = [(0, True), (1, True), (2, True),
(3, False), (4, False)]` at **both** maps.

* **S4 trivial-boundary control transfers to both maps**:
  `cap-C-with-signature == cap-(C+1)-with-trivial` on every shared
  depth for `C = 3, 4, 5`.  So both truncations **under-refine**, the
  printed counts are **LOWER BOUNDS**, and the blow-up reading is the
  **conservative** one — exactly as at D57's own granularity.
* **S3 split witness** at every cap, plus the headline creep exhibited:
  at both maps a depth-3 class of **84** histories splits **64 / 20**
  between cap 5 and cap 6.  Not a marginal one-off.

> **Answer to the two aggregation residues, both of them: NEITHER
> CLOSES.**  `[MEASURED, caps 3–6, two actors, counts are LOWER
> BOUNDS]` — the same grade as D57's verdict and no stronger.  The
> aggregation wall extends from D57's `(actor, type)` granularity to
> the **two coarsest maps the corpus had named**, and **D69's routes R1
> and R2 close**.  Outcome **HZ5-b**.

A datum worth carrying: type-only and budget-only give **identical**
per-depth counts at every depth except the cap layer itself (10 vs 9 at
depth 6).  Merging `r` with `m` buys essentially nothing at these caps
— consistent with d42b1's merge-sector vacuity.

---

## 8. Controls, and the wall diagnostic

**HZ6-i — the instrument can fail.**  Three declared perturbed weight
laws through the identical pipeline, same window (depth ≤ 5), all
reported including the one the statistic survives:

| control | family-uniform `L∞` drift, `r = 1→2 … 5→6` | contracts? |
|---|---|---|
| **true law** | 3/110, 3/253, 373/69230, 2333/1838829, 4629/187210517 | yes |
| **NC1** propose ×3/×⅓ by depth parity | 4.31e-2, 2.32e-2, 7.85e-3, 7.09e-3, 1.86e-3 | **yes** (survives) |
| **NC2** no deliveries at even depth, no proposals at odd | 5.30e-2, 2.25e-2, 1.44e-2, 5.08e-3, **7.16e-3** | **no** |
| **NC3** idle ×100 at even depth only | 2.38e-2, **2.69e-2**, 4.94e-3, **6.24e-3**, 2.77e-5 | **no** |

Two of three break contraction, so **the pin's falsifier 1 does not
fire and the HZ2 numbers are not void**.  NC1's survival is reported as
a measured robustness fact, not discarded.  Every perturbed kernel is
still proper.  Noted in the receipt: a purely depth-dependent rescaling
of *all* weights is **invisible** to `k_r` by construction — it cancels
in the ratio — which is why every control is type-selective as well.

**HZ6-ii — the positive control.**  The delivery-free d42a family
through the same pipeline: `ker(T − 2I)` is **one-dimensional with a
strictly positive generator** taking values `{1, 4/3, 7/3}` at
multiplicities `{29, 5, 2}` = D49's `f = (4,4,3,7,3,3)/3`;
`ker(T − I)` is one-dimensional and **mixed-sign**; `ker(T − 5/2 I)`
and `ker(T − 9/4 I)` are **empty**; `T f = 2 f` exactly.  And this
receipt's **own** potential `G(h, r)` — the object HZ0–HZ3 measure — is
a function of `sigma(h)` alone on that family with **0 violations**
(distinct `(sigma, G)` values `36, 32, 28` at `r = 1, 2, 3`), with
`T^r 1` reproducing `G(root, r)` at every horizon.  `λ = 2` is used
**only** as an asymptotic eigenvalue and is never compared with a
finite-horizon ratio (D46b's own relabelling, carried).

**HZ6-iii — anti-vacuity.**  All 42 `check()` predicates parsed; 0
flagged.  **The carried defect is named in the gate label**: the scan is
defeated by **hoisting** — a predicate reading a boolean computed on an
earlier line looks substantive whatever that line did.  The scan bounds
the *shape* of a predicate, not its content.

**HZ6-iv — determinism.**  Byte-identical pipeline digest under
`PYTHONHASHSEED` 0 / 7 / 999.  **Scope stated in the label**: the digest
(layer, census, potentials, kernels under both terminal conventions,
conditional, renewal predicate, a type-only refinement at cap 3), **not
this receipt's whole stdout** — three full runs would triple a runtime
the receipt prints in its own output.  The wider claim is not made.

**HZ7 — the wall control, diagnostic only.**  With
`deliver_options_in_view` restricted to non-superseded holdings inside a
**separate namespace**, the B1 ladder is still admissible at every rung
and `|holdings(A)|` still grows without bound, but the delivery menu
collapses to **1 option at `1/4`** and the **whole menu is constant at 8
options from rung 2 on**, for all ten rungs.

> **The B1 ladder does NOT survive the restricted enumerator.**  So the
> obstruction, *as constructed*, rests on that one line of the committed
> layer, and it does **not** harden from "a fact about one line" to "a
> fact about transport" on this evidence.  **What this does not show:**
> that any bounded abstraction exists under the restricted enumerator —
> only that *this ladder* stops being a witness.
>
> **MANDATED LABEL, printed by the gate itself: the committed layer is
> unchanged; no other number in this receipt uses the restricted
> enumerator; adopting it would be a different theory and is not
> proposed.**

---

## 9. What is licensed, horizon-scoped and pool-scoped (HZ8)

Every claim below is scoped to **transport scope, the declared families
and caps only**, in exact `Fraction`s.  **No infinite-volume claim under
any outcome** (D46b MB6, binding, and scanned rather than asserted).

1. `[MEASURED, ARM-1T, depth ≤ 6, r ≤ 7]` The relative-horizon kernels
   are **proper at every computable `(h, r)`**, and the measure chained
   from them is **cut-additive at every cut** while the raw weight is
   not.  D46b's `r = 1, 2` becomes `r = 1..7`.
2. `[MEASURED, two-actor depth ≤ 6; three-actor depth ≤ 4]` The
   family-uniform and depth-stratified drift of both the absolute
   kernel and the pinned conditional **contracts over the computed
   horizons at every off-root depth, in all five norms**.  *This is a
   table.*  It is **not** a rate, **not** a limit, and no fit,
   extrapolation or threshold is applied to it anywhere.
3. `[MEASURED, four-actor depth ≤ 3]` At four actors the `L = 1` row
   **does not contract** in any of the three absolute norms — `L∞`
   `29/8288 → 23117/6594399` (+0.19%), `L1` `87/4144 → 1160/53613`
   (+3.06%), sector-`L∞` `39/4144 → 580/53613` (**1207/8073 ≈ +14.95%**).  Two
   terms at the shallowest cap.  **This is the pin's HZ-I clause (c)
   and it fired.**
4. `[MEASURED]` The family-uniform sup is **window-dependent**; D46b's
   committed four-term sequence is a **lower bound** on the deeper
   family's sup and its fourth term understates it by ×1.92.
5. `[MEASURED, r ≤ 7]` **D46b MB3-e's root monotonicity is FALSE at the
   next horizon** — the root absolute drift rises by ×7.51 at
   `r = 6 → 7`, identically in all three norms.  The **pinned** object
   at the root stays exactly 0.
6. `[MEASURED, len(h)+r ≤ 6]` The two declared terminal conventions are
   **different completions at every single history**.  On the **pinned**
   object the difference is **exactly 0 at the root** at every horizon
   and shrinks at every fixed off-root depth; on the **horizon-bound**
   absolute kernel it does not shrink at two of six depth rows.  **The
   horn is object-dependent.**
7. `[EXACT, from the committed layer]` **Holdings never shrink.**  The
   menu-exact transport renewal class is **absorbing-complement**;
   `R-SIG` (the literal D62 R4 port) is **necessary and not sufficient**
   at transport (1,365 of 5,161); **no minorization constant exists by
   this argument**; **D69 route R5 is closed** as this unit's proof
   engine.
8. `[MEASURED, caps 3–6, two actors, LOWER BOUNDS]` **Type-only and
   budget-only aggregation both blow up.**  D69 routes **R1 and R2
   close** at D57's grade.  The finite-alphabet prerequisite stays
   `[OPEN]`.
9. `[DIAGNOSTIC ONLY]` The B1 ladder does not survive a restricted
   delivery enumerator.  Nothing in the corpus changes.

**What is NOT licensed.**  No claim that any of this is *the* click
law's measure — the identified law is reached only through the missing
map (D59/D65), untouched here.  No dimension claim, no typicality claim
of any kind, no quantum-layer claim; those are the **consequences** this
unit would have unblocked, not its content.  (H1)/(H2) and the 36-state
closure remain **two-actor delivery-free d42a**.  Scale doctrine (LOG
#440): this unit certifies a **mechanism**, never an object.

---

## 10. Residues, named

1. **The four-actor pool at depth 4.**  The clause that fired did so on
   a two-term row at depth 3.  Whether that is saturation or genuine
   non-contraction is **undecided**, and the deciding computation is a
   four-actor family at depth 4 (318,704 more histories; ~5–10 minutes
   of build at this receipt's rates).  **This is the cheapest thing in
   the campaign and it is the one that would re-grade the headline.**
2. **The three-actor pool at depth 5** — 713,967 more histories; not
   affordable in this unit's budget and declared so rather than cut
   silently.
3. **The root reversal's mechanism.**  `r = 6 → 7` is the deepest
   horizon this cap can reach, so the reversal is a single step.
   Whether it is the onset of oscillation or one turn needs `G_8`, i.e.
   a depth-7 family (~1.9M histories).
4. **A third terminal convention.**  Two refining conventions were
   declared; the horn's object-dependence would be sharper with a third
   that refines differently (e.g. a sector-weighted terminal).
5. **The renewal window.**  R-SIG / R-MENU were evaluated at depth ≤ 5
   because the predicate needs full views.  The monotonicity argument is
   depth-free from the layer's own `holdings` clause, but the census is
   window-bound.
6. **D57's own residues remain**: depth 7, and the actor-swap quotient
   (`≤ 2×`, cannot rescue the trend alone).  This unit did not touch
   them.
7. **The join-view lattice completeness** (D56 caveat C3, `[MEASURED to
   depth 5]`, 0 exceptions over 243,768 candidate views) is **not**
   re-verified here and this unit does not rely on it — but any successor
   that builds a `sigma` on top of these kernels must.
8. **Not review-hardened.**  No hostile round has been run.  Given the
   campaign's record — D57 pre-registered two expectations and both were
   refuted, one refutation then withdrawn; D46b reversed two of four
   first-pass headlines; D46d's lean produced a blocker — **the three
   unregistered findings in §4.3, §5.2 and §6.5 are exactly the kind a
   round tends to move**, and they should be read as green-unreviewed
   until one converts.

---

## 11. What this note does not do

* It does **not** claim the horizon-limit route is dead.  HZ-I fired on
  one clause, on one row, at one pool, at that pool's shallowest cap.
  The pin's consequence — *"the finite-horizon measures are horizon
  artifacts and D46d's typicality numbers stay horizon-scoped
  permanently"* — is **not** asserted here on that evidence, and §10
  residue 1 is the reason.
* It does **not** claim the route is alive either.  Every positive
  reading in §4 is a table over computed horizons; HZ4 exhibited no
  bound and showed that the corpus's own named proof engine cannot
  supply one; and HZ-III's licence is therefore unavailable under the
  pin's own terms.
* It does **not** propose adopting the restricted delivery enumerator,
  and it does not re-grade W-A.  HZ7 is a diagnostic and its label says
  so.
* It takes **no** position on the missing map, on the TRIPLE-GRID
  construction, or on any of the four frontiers.
