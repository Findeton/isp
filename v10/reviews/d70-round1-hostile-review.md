# D70 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-27.
**Unit under review:** D70 "the horizon limit", the measure campaign's
opening unit — `note-d70-horizon-limit-pin.md` (STRICT, frozen from the D69
scoping draft before any code was written), `note-d69-measure-campaign-scoping.md`
(the campaign map), `note-d70-horizon-limit-result.md` (GREEN-UNREVIEWED),
`code/d70_horizon_limit_exact.py` + `data/d70_horizon_limit_exact.out`
(41 PASS / 1 FAIL, exit 0, 534.8 s), LOG #482 / #484.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`ref_core.py`, `two_actor.py`, `four_actor3.py`,
`four_actor4.py`, `horn_sym.py`, `sym_proof.py`, `renewal.py`, `renewal2.py`,
`hz5.py`, scratch under the session scratchpad): my own family builder, my own
backward recursion `G(h, r)`, my own `k_r`, my own sector mass, my own
sector-normalized conditional, my own five norms, my own depth-stratified and
family-uniform drift tables, my own terminal conventions, my own renewal
predicates, my own hitting-probability chains, my own lumpability refinement.
Nothing was AST-lifted from D46b and nothing was read out of the unit's
`.out`. The only object I share with the unit is the committed layer under
test (`d42b1`'s `candidates_for` / `admissible` / `event_poset` / `View` /
`vname` / `V0`), which the pin correctly forbids re-implementing.
Calibration: `reviews/d68-round1-hostile-review.md`,
`reviews/d65-round1-hostile-review.md`, D46b's committed receipt
(`code/d46b_martin_transport_exact.py`), `code/d42b1_transport_exact.py`,
`code/d57_sector_exact_refinement.py`, `note-d62-h2-update-table.md` row R4.

**VERDICT: REVISE. 5 MAJOR / 4 MODERATE / 5 MINOR.**

**The arithmetic is flawless. Every single number I checked reproduced
exactly** — the census, all seven potentials, properness at every `r`, the
complete five-norm depth-stratified drift table, both window columns, the
`×1.92` understatement, the root ratio sequence `0.7382 / 0.3985 / 0.0864 /
7.5091` identical in all three absolute norms, the 3-actor and 4-actor matched
cells, both horn tables entrywise, the renewal counts `5,161 / 1,365 / 3,796`,
the `0.7705`, the ladder cylinders, and both HZ5 refinement tables including
the S4 controls. **I broke nothing in the arithmetic. I broke the readings.**

Four of the five MAJORs are inference defects of exactly the kind D65 and D68
were convicted of: the operationalization is not faithful to what the unit
says it is testing. The fifth is the one the unit named itself and declined to
run — **I ran it, and it re-grades the headline.**

---

## MAJOR 1 — I RAN THE FOUR-ACTOR DEPTH-4 ARM. THE HZ-I ROW'S RISE IS A ONE-STEP BLIP THAT REVERSES AT THE VERY NEXT HORIZON.

**Where.** Result §0, §4.4, §9 claim 3, §10 residue 1; receipt `HZ2-c`; LOG
#484 part (2) and its headline.

**Defect.** The delivered outcome rests on a two-term row at the shallowest
declared cap, and the unit itself names the deciding computation, prices it at
"318,704 more histories; ~5–10 minutes of build at this receipt's rates", calls
it "**the cheapest thing in the campaign and the one that would re-grade the
headline**" — and then delivers the outcome without running it, inside a
receipt whose total budget was 534.8 s. That is not a scoping decision; it is
delivering a headline the unit knew one cheap computation could overturn.

**Recomputation.** I built the four-actor family to cap 4 (318,704 depth-4
histories confirmed exactly; 332,696 menu evaluations total; **176 s wall on 7
processes**, ≈ 20 min single-core — i.e. affordable, and trivially parallel).
My cap-3 pipeline reproduces the unit's first two terms exactly in all five
norms, so the third term below is produced by the identical instrument:

| norm, 4 actors, `L = 1` | `r=1→2` | `r=2→3` | **`r=3→4` (NEW)** | `t2/t1` | **`t3/t2`** | `t3/t1` |
|---|---|---|---|---|---|---|
| `L∞` abs | 29/8288 | 23117/6594399 | **33367649/10728807102** | +0.19% | **−11.28%** | **−11.12%** |
| `L1` abs | 87/4144 | 1160/53613 | **897664/43613037** | +3.06% | **−4.87%** | **−1.96%** |
| sector-`L∞` | 39/4144 | 580/53613 | **448832/43613037** | +14.95% | **−4.87%** | +9.35% |
| `L∞` **cond** | 1/102 | 691/89913 | **902551/161966810** | −21.61% | −27.49% | −43.16% |
| `L1` **cond** | 1/17 | 744465/15495007 | **39986658899218/1059396641001655** | −18.32% | −21.44% | −35.83% |

The drift resumes falling in **every** norm at the next horizon, and in `L∞`
and `L1` the third term is **below the first**. The sup is attained at the
same single history — `(('p','A',v0,0),)` — in every cell of every norm, so
the whole HZ-I firing is one depth-1 proposal's absolute kernel at two
horizons.

**The unit's own data already contained the counter-example.** At **three**
actors the ROOT row does exactly the same thing: `0, 1/1734, 3496/4043977,
1014199/1191210097` — a **×1.50 rise** at step 2 followed by a fall at step 3.
Had that row been truncated at two terms it would have read as "stopped
contracting" too. A two-term rise was already known, inside this receipt, to be
non-diagnostic in this family.

**What survives.** The receipt's own predicate (`contracts_from_first_nonzero`,
strict decrease from the first nonzero term) would still return `False` at cap
4 because `t2 > t1`. So **HZ-I still fires by the letter of the pin** — but the
*reading* is refuted. These must be corrected:

* §0 "**It does not contract at four actors**" → "at four actors the depth-1
  absolute row is non-monotone: it rises by 0.19–14.95% at `r = 2→3` and falls
  by 4.9–11.3% at `r = 3→4`".
* §4.4 "a drift that is **small in magnitude and has stopped falling** — and in
  the sector-norm, has turned up appreciably" → **withdrawn**; it resumes
  falling.
* §4.4 "Whether that is saturation or non-contraction **cannot be decided at
  depth 3, and this unit does not decide it**" → it can be decided at depth 4,
  it now is, and the answer is *neither*: a single-step blip.
* LOG #484's "the FOUR-ACTOR depth-1 absolute row RISES between its only two
  reachable horizons" needs "…and falls again at the third, which this unit did
  not compute".
* §10 residue 1 is **discharged**, not open.

**Severity.** MAJOR, not BLOCKER: the outcome label survives, the numbers are
right, and the note's §11 already declines the strong consequence. What fails
is the discipline the pin itself imposes at HZ2 — *no reading past the computed
table* — applied asymmetrically. The pin forbids "converges" from a finite
table; the same discipline forbids "has stopped falling" from a two-term one,
and the pin set **no minimum-evidence bar on clause (c)** — a gap the pin
should be recorded as having.

---

## MAJOR 2 — THE UNIT APPLIES ITS OWN PINNED-OBJECT DOCTRINE IN OPPOSITE DIRECTIONS IN THE SAME RECEIPT, AND THE HEADLINE OUTCOME DEPENDS ON WHICH WAY IT IS APPLIED.

**Where.** Receipt `HZ3-b` vs `HZ2-c`; result §4.3 vs §4.4; pin §2 and §6.

**Defect.** The pin binds, twice and in terms: *"the pinned object is the
SECTOR-NORMALIZED CONDITIONAL; absolute completed weights are horizon-bound
(D44f) and are context"* (§6), and *"the absolute weights are carried as
context"* (§2). The receipt enforces this at HZ3, in capitals:

> **THE HORN VERDICT IS TAKEN ON THE PINNED OBJECT AND ON NOTHING ELSE,
> because the pin's §6 says so in terms … The absolute rows are printed in full
> beside it and are NOT folded into the verdict.**

§4.3 uses the same doctrine to *decline* to count the root reversal as HZ-I:
"the object that reverses is the **horizon-bound absolute kernel** … and the
object the pin names is untouched."

**Then HZ2-c folds exactly those absolute rows into the delivered verdict.**
`POOLROWBAD_OFF` is computed over all five norms and the FAIL predicate is
`all(not POOLROWBAD_OFF[nm])`, so a failure in any *absolute* norm flips the
boolean that fires HZ-I.

**Recomputation.** At four actors the **pinned** object contracts strictly at
every computable row, at cap 3 and again at cap 4 (rows above): `L∞` cond
`1/102 → 691/89913 → 902551/161966810`; `L1` cond `1/17 → 744465/15495007 →
3.7745e-2`. The root conditional row is identically 0. **On the pin's own
object, HZ-I clause (c) does not fire at any pool, at any cap this unit or I
computed.**

The receipt *has* this datum — its printed 4-actor bad-row list is
`[('L-inf (abs kernel)', 0), ('L-inf (abs kernel)', 1), ('L1 (abs kernel)', 0),
('L1 (abs kernel)', 1), ('sector-L-inf', 0), ('sector-L-inf', 1)]`, containing
**no conditional row** — and neither the receipt nor the note ever says so.
Worse, the cross-pool tables are printed for norm index 0 only
(`POOLCELLS[nm][(r,L)][0]`), so **the pinned object is never tabulated across
actor pools anywhere in this unit**, which is precisely what the pin's
falsifier 4 asks about.

**Required.** Either (a) state the doctrine once and apply it to HZ2-c as it is
applied to HZ3-b and §4.3 — in which case HZ-I does **not** fire and the
delivered outcome changes — or (b) withdraw the HZ3-b/§4.3 doctrine and count
the root reversal as HZ-I clause (b) as well. As it stands the receipt selects
the object per gate in the direction that maximises the delivered negative at
HZ2 and minimises it at HZ3. Whichever way it is resolved, the note must print
the 4-actor conditional rows beside the absolute ones.

---

## MAJOR 3 — THE HORN'S ROOT LEG IS A SYMMETRY IDENTITY, NOT A MEASUREMENT. "THE HORN IS OBJECT-DEPENDENT" MUST BE DEMOTED TO ITS OFF-ROOT CONTENT.

**Where.** Result §5.2(ii), §9 claim 6, the `HZ3-HORN` outcome block, LOG #484
part (3); and, by the same argument, anchor `HZ0-7` / D46b **MB3-c** and result
§4.3's consolation.

**Defect.** "The pinned object separates **nowhere at the root** (exactly 0 at
every horizon)" is presented as the measured half of an object-dependence
finding — something that could have come out otherwise. It could not.

**Recomputation.** `A ↔ B` is an **exact automorphism of the committed layer**:
over all 521 histories of depth ≤ 3, relabelling a history and relabelling its
menu give byte-identical `(event, weight)` multisets — **0 violations** — and
`G(h, r) = G(σh, r)` with 0 violations. Combined with the `0 ↔ 1` value swap,
**each event kind in the root menu is a single orbit**: `{p(A,v0,0), p(A,v0,1),
p(B,v0,0), p(B,v0,1)}`, `{d(A,B,v0), d(B,A,v0)}`, `{n(A), n(B)}`. Therefore for
**any terminal convention invariant under those relabellings**, the root
sector-normalized conditional is the uniform-within-kind distribution at every
horizon:

```
  root conditional, EVERY r, under C1, C2, C3 and my C5:
     p: 1/4, 1/4, 1/4, 1/4      d: 1/2, 1/2      n: 1/2, 1/2
```

So `HZ0-7` ("root drift exactly 0 at `r = 1..6`", D46b MB3-c) and `HZ3-b`
("convention separation exactly 0 at the root at every horizon") are **the same
identity**, and neither carries any information about horizon stability or
convention independence.

**The falsification test the pin's HZ3 asks for, run.** I built two further
terminals, both legitimate functions of the terminal history's own state, both
strictly positive:

* **C5 — sector-weighted, equivariant** (`G(h,0) = 1 + |{kinds in menu(h)}|`):
  this is **exactly the note's own §10 residue 4** ("a third that refines
  differently, e.g. a sector-weighted terminal"). Root conditional separation
  from C1: **`0, 0, 0, 0`** at `r = 1..4`. Absolute separation: `1/68, 1/140,
  50/14649, 2707/2122785`. **Residue 4 as written cannot sharpen the finding** —
  it reproduces the same tautology.
* **C4 — actor-asymmetric** (`G(h,0) = 2` if the last event's actor is `A`,
  else `1`): root conditional separation **`1/6` at `r = 1`**. The invariance
  breaks the moment equivariance is dropped.

**Required.** The exact-0 at the root must be labelled `[THEOREM of the
construction: root-menu symmetry × equivariant terminal]`, not `[MEASURED]`.
The horn's real content is the **off-root** table — conditional separation
`1/8, 1/12, 487/7790, 40337/800358, 109092211/2569013838` (≈ `1/(4r+4)`, five
terms, a fixed 8-history window) against absolute rows that do not shrink at 2
of 6 depths. That is a genuine finding and it is much weaker than "the horn is
object-dependent". §4.3's "the **pinned** object … stays exactly 0 throughout,
so **nothing physical moves**" is likewise not a consolation: the 0 is forced,
so it would have stayed 0 whatever the absolute kernel did.

---

## MAJOR 4 — "D69 ROUTE R5 IS CLOSED" IS AN OVER-CLAIM ABOUT A ROUTE FAMILY. THE UNIT'S OWN COARSER PORT IS RE-ENTERED, WAS NEVER TESTED, AND HAS A STRICTLY POSITIVE HITTING PROBABILITY WHERE I COULD COMPUTE IT.

**Where.** Result §6.2, §6.5, §9 claim 7; receipt `HZ4-ii(a)` / `HZ4-iv`; LOG
#484 part (4) ("**route R5 CLOSED**", "N-step return probability EXACTLY 0").

**Defect, three layers.**

**(a) The monotonicity fact is definitional and applies only to R-MENU.**
`View.holdings(a)` is literally a union over the arbs/deliveries/merges in the
view; extending a history adds events; therefore it grows. The receipt says so
in its own preamble and then gates it exhaustively (30,728 transitions, 0
shrinking). Confirmed — and it is a one-line theorem, not a census. Crucially,
the layer *does* have a shrinking set: `superseded` grows, so **non-superseded
holdings shrink**, which is why `prop_options_in_view` skips superseded. The
absorbing-complement argument therefore covers `R-MENU` and nothing else.

**(b) `R-SIG` — the literal D62 row-R4 port, which is what D69's R5 actually
names — is NOT absorbing-complement.** My recomputation, over the same window:

| | count | menu = root's under renaming | **points with a non-R-SIG prefix (RE-ENTRY)** |
|---|---|---|---|
| R-SIG | **5,161** | 1,365 yes / 3,796 no | **3,796** |
| R-MENU | **1,365** | 1,365 / 0 | **0** |

All three unit counts reproduce. But **R-SIG is re-entered 3,796 times** — e.g.
`[p(B,v0,0), p(A,v0,1), r(A,…), n(A), n(A)]`, a history with a created version
where both actors' non-superseded holdings are again a common singleton. The
unit's stated reason for the closure — *"the renewal class is left exactly once
and never re-entered"*, *"the return weight is **exactly zero** for almost every
history"* — is **false for R-SIG**.

**(c) The minorization test was run on `R-MENU` only** (`RMSET`, line 1471).
I ran it on `R-SIG`:

| N | tested | hitting prob exactly 0 | infimum |
|---|---|---|---|
| 1 | 3,969 | 2,520 | 0 |
| 2 | 521 | 84 | 0 |
| 3 | 69 | **4** | 0 |
| **4** | **9** | **0** | **118/1455 ≈ 0.0811** |
| **5** | **1** | **0** | **308834/403761 ≈ 0.7649** |

(R-MENU, for contrast: 3628/3969, 436/521, 48/69 — reproduced exactly.) The
R-SIG zero-set **collapses** with `N` and vanishes at `N = 4`, which is the
shape of a Doeblin condition, not of a closed route. And the class is not
obviously useless: over the whole window R-SIG carries only **three** distinct
menu shapes, with **3,788 of the 3,796** non-root-menu points sharing one
(`4×d@1/8, 2×n@1/2, 4×p@1/8`).

**Stated against myself:** my `N = 4` and `N = 5` windows are 9 and 1 histories
— this is **not** a bound and I claim none. It is a demonstration that the
route was not tested. Separately, classical Doeblin minorization needs no atom
at all (`P^N(x, ·) ≥ δ ν(·)`); §6.5 states the *atom* version as if it were the
general one, and no operator-level minorization (Birkhoff/Hilbert-metric
contraction of the positive backward recursion — the natural instrument for
`G`) was attempted anywhere.

**Required.** "D69 route R5 is CLOSED" → "**the menu-exact atom route is
closed**: the class of histories whose menu is the root's under renaming is
absorbing-complement and unreachable. The σ-level class (R-SIG, the literal
D62-R4 port) is re-entered, was not tested for minorization, and its N-step
hitting probability is not zero at `N = 4` on the window where it is
computable. Operator-level minorization is untried." §9 claim 7 and LOG #484
part (4) need the same narrowing.

---

## MAJOR 5 — HZ5's TWO "ROUTES" ARE ONE COMPUTATION AT EVERY DEPTH THE DECIDER USES. R1 AND R2 DID NOT CLOSE INDEPENDENTLY.

**Where.** Result §7, §9 claim 8; receipt `HZ5-0` / `HZ5-3`; LOG #484 part (5)
("**BOTH AGGREGATION ROUTES CLOSED**", "routes R1 AND R2 close").

**Defect.** `sec_budget` differs from `sec_type` only by merging `r` and `m`.
My census over the full depth-6 family:

```
menu entries of kind 'm', by parent depth:  {5: 72, 6: 2672}
histories CONTAINING an m event:            72   (of 243,769)
```

**No `m` event appears in any menu at parent depth ≤ 4.** On every menu entry
below parent depth 5, `sec_budget` is therefore a *bijective relabelling* of
`sec_type` — the same function up to names — so the two sector maps induce the
**identical** initial signature and the **identical** fixpoint partition there.

D57's decider, carried verbatim by this unit, is *"for every depth carrying at
least three cap values, do the last two cap values agree?"* — which uses
**depths 0–4 only** (depth 5 has two cap values, depth 6 has one). At those
depths the two maps are provably the same map. The one number that differs
(depth 6: 10 vs 9) is in the cap layer and **never enters the decider**.

**Recomputation** (my own refinement, both maps, both boundary treatments):

| depth | type-only cap 3/4/5/6 | budget-only cap 3/4/5/6 |
|---|---|---|
| 0–2 | 1,1,1,1 / 2,2,2,2 / 6,6,6,6 | identical |
| 3 | 5, 10, 10, **11** | 5, 10, 10, **11** |
| 4 | —, 6, 14, **16** | —, 6, 14, **16** |
| 5 | —, —, 7, **19** | —, —, 7, **19** |
| 6 | —, —, —, **10** | —, —, —, **9** |

Every number matches the unit's. S4 trivial-boundary control transfers at
`C = 3, 4, 5` for both maps — confirmed. The blow-up is real and the
lower-bound reading is right.

The note *discloses* the coincidence ("a datum worth carrying: identical
per-depth counts at every depth except the cap layer") and *explains* the
mechanism (HZ5-0, merge-sector vacuity) — but then still reports **two** route
closures. It is not a datum; it is an identity, and the honest statement is
that **one** test was run and it closes R1, with R2 following only insofar as
R2 is not a distinct map at these caps.

**Required.** §7, §9 claim 8 and LOG #484 part (5): "routes R1 and R2 close"
→ "route R1 closes; **route R2 is not a distinct test at these caps** — the
budget map coincides with the type map on every menu entry below parent
depth 5, so the decider's input is bit-identical, and R2's closure is inherited,
not measured." Extending R2 to a cap where merges have support is the honest
residue.

---

## MODERATE 6 — HZ1-c ("cut-additivity"), the disposal of pre-registered outcome HZ-IV, is an identity of the construction, not a measurement.

**Where.** Result §3 ("**The substantive half**"), §9 claim 1; receipt `HZ1-c`;
LOG #484 part (1) ("the chained kernel cut-additive at every cut — **HZ-IV
dead**").

**Defect.** The note correctly labels `Σ_e k_r(e|h) = 1` an identity and calls
HZ1-a a tripwire. But then it presents cut-additivity as the substantive half.
Given the identity, the chained mass at cut `n` is 1 **by induction**: it is a
product of probability kernels. The contrast drawn against the raw weight
(cut masses `1, 2, 4, 257/32, …`) is just the observation that the raw weight
is unnormalized. HZ-IV was therefore disposed of by construction before the
receipt ran, and no measurement is involved.

**Recomputation.** True for `R = 1..7`, as it must be; raw cut masses reproduce
the root potentials exactly. The one non-vacuous half is `HZ1-b` (strict
positivity of every `G`, so no zero denominator) — that is the real tripwire and
it should carry the weight §3 gives to cut-additivity. The substantive version
of the question — Kolmogorov consistency **across** `R` — is not cut-additivity
at all; it is precisely what HZ2's drift table measures.

---

## MODERATE 7 — theorem-passes among the 41, four of them undisclosed.

At least **seven** of the 41 PASSes cannot fail:

| gate | why it cannot fail | disclosed? |
|---|---|---|
| HZ1-a properness | identity of `G`'s definition | **yes** |
| HZ1-c cut-additivity | follows from HZ1-a by induction | **no** (MODERATE 6) |
| HZ3-a C3-leg | `G^{C3}(·,r) = G^{C1}(·,r+1)` by definition | yes ("gated to be") |
| HZ4-ii(a) holdings monotone | `View.holdings` is a union over view events | yes (preamble) |
| HZ5-1 alphabet | see MODERATE 8 | **no** |
| HZ0-7 root conditional drift = 0 | symmetry (MAJOR 3) | **no** |
| HZ3-b root leg | symmetry (MAJOR 3) | **no** |

"0 of 42 flagged" by the AST anti-vacuity scan is therefore compatible with
~17% of the passes being unfailable — which is exactly the defect the receipt
names for its own scanner ("bounds the *shape* of a predicate, not its
content"). The receipt names the defect honestly; it should also carry a
**theorem-pass count** in the summary line so `41 PASS` is not read as 41
tests.

---

## MODERATE 8 — HZ5-1's gate predicate is structurally incapable of failing.

**Where.** Receipt `HZ5-1` (the finite-alphabet prerequisite, "gated FIRST and
SEPARATELY").

**Defect.** The predicate is `all(len(v) == len(HZ5_CAPS) …) and all(v[i] >=
v[i-1] …)` — it passes iff the per-cap alphabet sizes are non-decreasing. The
cap-`c` family is a **subset** of the cap-`(c+1)` family, so the collected
sector-total alphabets are nested and their sizes are non-decreasing **by
construction**. The gate cannot return False for any input.

The *verdict* it carries — `[OPEN]` in both directions — is exactly right and
is the pin's and D69 §6's requirement. The **gate** is vacuous. Label it as a
reporting gate, not a test.

---

## MODERATE 9 — two "contracts / shrinks to 0" readings are window artifacts of the symmetry identity.

**Where.** Result §4.2 ("**All five contract**", `L∞` cond and `L1` cond rows
ending in `0`); §5.2's family-wide conditional column ending in `0`; LOG #484
part (3) "off-root separation **shrinking to 0 at r = 6**".

**Defect.** At `r = 6` the family-uniform window contains **only the root**,
where the conditional is exactly 0 by MAJOR 3's symmetry. The final `0` in both
conditional sequences is therefore neither contraction nor shrinkage — it is
the window emptying of off-root histories. The LOG phrase "**off-root**
separation shrinking to 0 at `r = 6`" is doubly wrong: the `r = 6` row contains
no off-root history at all.

The note flags window dependence in general (HZ2-b, and again in §5.2's
preamble) and prints the depth-stratified tables first, which is the right
discipline — but it then quotes the artifact zeros in a summary sentence and in
the LOG. Strike the terminal `0`s from any "contracts"/"shrinks" claim, or
mark them `[root only]`.

---

## MINOR

1. **Anchor count disagrees three ways.** The receipt prints "HZ0: all **15**
   anchors reproduce" (which counts the four HZ0-a provenance gates as
   anchors); result §1's table says "**HZ0 (14 anchors)**"; result §2 says "all
   **fourteen**" over a list of **ten** bullets. Pick one and make the receipt
   the source.
2. **HZ8-b scanned 40 of 42 labels** ("forbidden root present in the 40 gate
   labels = False") — the last two checks are delivered after the scan runs. Say
   so, or move the scan.
3. **HZ6-i NC2 is a perturbed grammar, not a perturbed weight law.** "deliveries
   FORBIDDEN at even depth, proposals FORBIDDEN at odd depth" removes menu
   entries, so NC2's drift is taken over a different family. The pin asks for "a
   deliberately perturbed **weight law**"; NC1 and NC3 are that, NC2 is not.
   NC2 is one of the two controls that break contraction, so the count "2 of 3"
   should read "1 of 3 weight-law perturbations and 1 of 1 grammar
   perturbations".
4. **The determinism digest covers cap 3 only** (disclosed in the label, which
   is the right practice). It therefore excludes the 3- and 4-actor pools, all
   of HZ4, all of HZ5, and the horn beyond depth 3 — i.e. every arm this review
   found a defect in. Not a breach; worth naming in the note, which currently
   says only "determinism 3 seeds".
5. **§10 residue 4 is not a route** (MAJOR 3): I ran the sector-weighted
   terminal it proposes and it returns exactly 0 at the root. Replace it with
   "a **non-equivariant** terminal", which is what actually probes the root
   invariance.

---

## Checked and CLEAN

Everything below I recomputed from my own instrument and it reproduced
**exactly**. Where the unit's claim is correct I say so without qualification.

* **Census.** Per level `[1, 8, 60, 452, 3448, 26760, 213040]`, cumulative
  `[1, 9, 69, 521, 3969, 30729, 243769]`. 3 actors `[1, 16, 235, 3424, 50617]`;
  4 actors `[1, 25, 593, 13993]`, and depth-4 level count **318,704** exactly as
  the note estimates.
* **Potentials.** `G_1..G_6 = 2, 4, 257/32, 1035/64, 4173/128, 134587/2048` and
  the new **`G_7 = 2168717/16384`**; transport ratio at `D = 7` =
  `2168717/1076696 ≈ 2.014233`.
* **Properness.** `Σ_e k_r = 1` exactly at `r = 1..7` over `243769, 30729, 3969,
  521, 69, 9, 1` histories, **0 violations**, matching the unit's table row for
  row. Chained masses exactly 1 at every cut for `R = 1..7`; raw cut masses
  exactly the root potentials.
* **The whole two-actor drift table**, all five norms, all depth rows, exact —
  including `L=0: 0, 1/1028, 191/265995, 412/1439685, 4629/187210517,
  54193948/291881114879`; `L=1: 3/208, 1/156, 1/356, 2333/1838829,
  12494788/19065729755`; the conditional rows `1/18, 4/171, 8/741, 176/32877,
  302623/103087098`; and every family-uniform row.
* **The window fact.** D46b's window (`len(h)+r ≤ 5`) gives `3/110, 3/253,
  373/69230, 2333/1838829`; the deeper family gives `…, 89364/36687385`. The
  **×1.92** understatement is real and correctly reported as a lower bound.
* **THE D46b REVERSAL IS GENUINE, AND IT IS NOT A WINDOW ARTIFACT.** Root
  absolute drift `0, 1/1028, 191/265995, 412/1439685, 4629/187210517,
  54193948/291881114879`; ratios **0.7381642512, 0.3985380964, 0.0864026777,
  7.5090994424**, and the `L∞`, `L1` and sector-`L∞` ratio sequences are
  **exactly equal, rational for rational**. This is a fixed-history (root)
  sequence, not a sup over a window, so no window or family semantics changed
  between D46b's `r ≤ 6` points and this unit's `r = 7` point — the only new
  ingredient is the depth-6 menu layer, computed by the same recursion on the
  same committed layer. **D46b MB3-e must be corrected to:** *"the root's
  absolute drift contracts monotonically from `r = 2` through `r = 6`, and
  **rises by a factor ≈ 7.509 at `r = 6 → 7`**; the monotonicity claim was true
  of every step D46b could compute and is false at the next one. The
  sector-normalized conditional at the root is exactly 0 at every horizon —
  for the symmetry reason of MAJOR 3, not as evidence of stability."*
* **Both horn tables entrywise.** Absolute `L=0: 1/124, 3/980, 1044/1007183,
  1849/13060665, 1710615/4253203669`; `L=3: 7/200, 559/16776, 29255/822216`
  (the non-monotone row); conditional `L=1: 1/8, 1/12, 487/7790, 40337/800358,
  109092211/2569013838`. C3's declared status verified: it is exactly a horizon
  shift of C1.
* **Renewal counts.** R-SIG 5,161 (1,365 menu-exact / 3,796 not), R-MENU 1,365
  `= Σ_{n≤5} 4^n`, R-MENU absorbing-complement with **0** re-entries, R-MENU
  hitting-probability zero-counts `3628/3969, 436/521, 48/69` — all exact.
* **The 0.7705.** Verified numerically *and* closed-form: renewal mass at
  depth 5 `= (3/2)^5 · G_2 / G_7 = 243·2048/2168717 = 497664/2168717`, so the
  never-regenerating mass is `1671053/2168717 = 0.770526…`. Correct.
* **The ladder.** Cylinder weight `1/32` per rung, `|holdings(A)| = k+1`, every
  rung admissible.
* **HZ5.** Both refinement tables, all four caps, both boundary treatments, and
  the S4 lower-bound control at `C = 3, 4, 5` for both maps. The blow-up is real
  and the conservative reading is the right one.
* **Matched-cell pool comparison.** All five cells, all three pools; the drift
  magnitude does fall with actor pool in every one — the pin's falsifier 4 does
  not fire in the direction it feared.
* **Exit protocol.** `sys.exit(1)` is reachable only from the HZ0 anchor block
  (`ANCHOR_FAIL`), `sys.exit(0)` at the end. Exactly the pin's §7. The single
  FAIL is the pre-registered clause and is accounted for correctly.
* **Doctrine.** No infinite-volume claim anywhere in the note or receipt. Every
  numeric claim in §9 is horizon-scoped and pool-scoped. The three unregistered
  outcomes are labelled unregistered in §1, §4.3, §5.2 and flagged again in §10
  residue 8. No sampled arm exists, so D46d's exact/sampled separation is
  vacuous here and the receipt says so. HZ7's mandated label is printed
  verbatim by the gate. The pin's lexical prohibition on "converges" holds: the
  word appears in no gate label.
* **Pin/receipt correspondence.** Every gate the pin declares ran; HZ5 was not
  dropped; every cap, pool, window and seed is printed by the receipt itself;
  the pin was frozen before the code and names the receipt path.

---

## What a round 2 must deliver

1. Fold the 4-actor cap-4 row (MAJOR 1) into §4.4, §0, §9 claim 3, §10 and the
   LOG; discharge residue 1.
2. Resolve the pinned-object doctrine one way (MAJOR 2) and print the 4-actor
   conditional rows.
3. Demote the horn's root leg to `[THEOREM]` and re-state HZ3-HORN on its
   off-root content (MAJOR 3); replace residue 4 with a non-equivariant
   terminal.
4. Narrow "R5 closed" to "the menu-exact atom route is closed", and either run
   the R-SIG minorization at usable `N` or record it as the open residue
   (MAJOR 4).
5. Re-state HZ5 as one test with an inherited second closure (MAJOR 5).
6. Re-grade HZ1-c, HZ5-1, HZ0-7 and HZ3-b's root leg as theorem-passes and
   print a theorem-pass count beside `41 PASS` (MODERATE 6–8).
7. Strike the window-artifact zeros from every "contracts"/"shrinks" claim
   (MODERATE 9).

None of this touches the unit's arithmetic, which is exact and reproduces
without a single discrepancy.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-27)

All findings verified and applied; receipt rerun by the adjudicator,
byte-identical modulo timings (51 PASS / 0 FAIL, 1,086 s — the
campaign's longest).  MAJOR 1: the four-actor depth-4 arm is IN THE
RECEIPT (318,704 depth-4 histories, serial build printed) and matches
the referee cell-for-cell — the rise reverses, below the first term
in L-inf/L1; HZ-I's substance dissolved; residue 1 discharged.
MAJOR 2: the pinned-object doctrine applied in one direction — the
doctrine-consistent outcome is **HZ-III's shape WITHOUT its licence
(contraction everywhere; no bound yet)**, tagged
"HZ-III (bound clause NOT satisfied) + HZ5-b", with the absolute
letter-reading printed as context.  MAJOR 3: the root exact-0
relabelled a SYMMETRY THEOREM (A<->B, 0<->1 gated automorphisms; an
asymmetric terminal breaks it at 1/6) — the horn's content is the
off-root table.  MAJOR 4: "R5 closed" narrowed to the menu-exact
atom; **R-SIG gated OPEN** (re-entered 3,796/5,161; zero-set collapse
2520/3969 -> 84/521 -> 4/69 -> 0/9; N=4 infimum ~0.081 under both
window conventions; zero-sets horizon-independent) — operator-level
(Birkhoff/Hilbert-metric) minorization is the campaign's surviving
proof-engine candidate.  MAJOR 5: the two aggregation maps gated
identical at every decider depth — ONE closed route.  All MODERATEs/
MINORs applied (identity labels, theorem-passes disclosed 7/51,
window-artifact readings requalified, 42/42 scans, determinism
widened — with the worker's own by-product find: equal frozensets
can carry different reprs in one process; repr-sorts converted to
set comparisons).  **The D46b MB3-e forward correction is stated
verbatim in the note.**  TERMINAL for round 1.
