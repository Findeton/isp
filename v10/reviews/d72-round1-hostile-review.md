# D72 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-27.
**Unit under review:** D72 "the weld" — `note-d72-weld-pin.md` (STRICT, frozen
and committed before any code was written, `#487`), `note-d72-weld-result.md`
(GREEN-UNREVIEWED), `code/d72_weld_exact.py` + `data/d72_weld_exact.out`
(50 PASS / 0 FAIL, exit 0, 343 s), LOG `#488`.
Context read: `note-d71b-holonomy-phase-identity.md` (Clauses 2/3),
`note-d71-phase-archaeology.md`, `note-d42b4-quantum-lift.md`,
`code/d42b3_placement_exact.py`, `code/d42b1_transport_exact.py`,
`v7/code/p30_complex_amplitude_campaign.py`, `code/v6_p4n_exchange_cocycle_law.py`,
`note-d65-descent-conditions-result.md`.
**Reviewer:** independent worker, no prior context, no loyalty to the unit,
recompute-never-trust. Every number below was produced by code I wrote for this
review (`rev1.py`, `d72rev_b.py`, `d72rev_c.py`, `d72rev_d.py`, `d72rev_e.py`,
`d72rev_f.py`, `g2abc.py` under the session scratchpad): my own family builder,
my own exchange-square census, my own comparability predicate, my own mass
functional, my own normalised-kernel census, my own spanning-forest holonomy,
my own linear-extension and order-type machinery, my own `k`-type census.
Nothing was lifted from the unit's receipt and nothing was read out of its
`.out`. The only objects I share with the unit are the committed layers under
test (`d42b3` and `d42b1`'s `candidates_for` / `admissible` / `event_poset` /
`View` / `canon` / `mu_of` / `regs_of`), which must not be re-implemented.
**Calibration:** `reviews/d68-round1-hostile-review.md` (operationalisation
fidelity), `reviews/d70-round1-hostile-review.md` (the unasked computation),
`reviews/d65-round1-hostile-review.md` (the raw-vs-normalised dichotomy).

---

**VERDICT: REVISE. 5 MAJOR / 5 MODERATE / 6 MINOR.**

**Every arithmetic claim in the unit reproduces.** I rebuilt the generated line
independently and got 6,471 histories with the identical per-depth profile
`{0:1, 1:6, 2:32, 3:176, 4:976, 5:5280}`, 1,565 record classes, the exchange
census `{closed: 2227, both-blocked: 610}` with the ratio multiset
`{1: 2227}`, `AB-only = BA-only = 0`, the linear-extension bijection on all
6,464 histories, `28` of the `32` two-event histories with an admissible
reverse, `2,214` non-empty-base squares of which `0` agree and `578` have an
admissible `*_seq` image, the dual census `294 / 1,264`, `μ` constant on all
1,565 classes, the deletion graph `V=1565, E=2322, C=1, rank=758`, `0`
multi-valued edges, `0` non-trivial holonomies, and — to all 32 published
digits — `2·exp(−3/32) = 1.8210207227600682556870097725525` with `E = 3` the
argmax (I checked `E ∈ 0..3999`, not the receipt's `0..399`). The receipt
reruns byte-identically apart from timings. **I broke nothing in the
arithmetic of grammar 1. I broke the scope, the instrument, and the second
grammar.**

The three headline breaks:

1. **The flatness verdict is false in the second grammar, inside the note's
   own licensed window.** On `d42b1` at `(A,B)` depth ≤ 4, `88` of `1,546`
   closed exchange squares have `dP_AB/dP_BA ≠ 1` (spectrum
   `{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}`) and a further `40` squares are
   **half-open** (`A_D = ±∞`); on `(A,B,C)` depth ≤ 3, `12` of `1,554`.
   Licensed claim 1 asserts the opposite as `[MEASURED]` on exactly those
   windows, and it was never measured there.
2. **The instrument used in the second grammar is blind to the defect by
   construction.** `0` of those `88` squares close at record level, so the
   record-deletion-graph holonomy census — the only test the receipt ran on
   `d42b1` — cannot see any of them. The negative control cannot detect this
   class of blindness.
3. **On the normalised kernel the line is not flat, and the defect is
   `R+`-valued — falsifier F4's shape, which the note records as "not reached,
   vacuously".** The normalised square ratio takes `{4/5: 220, 1: 1687,
   5/4: 320}`; the normalised connection descends to records and has
   non-trivial holonomy on `175` of the `758` independent cycles, with value
   set `{64/125, 16/25, 4/5, 1, 5/4, 25/16, 125/64}`. This is D65's committed,
   round-1-hardened result restated; D72 cites D65 nowhere.

**The depth-free argument: half-closed and re-sited.** The note's stated
argument (step weight = function of the past-local view; incomparable events
absent from each other's views) is **correct and I proved it** — but it covers
only `1,355` of the `2,227` squares. The other `872` are register-overlapping
(causally comparable) pairs to which its hypothesis does not apply. I close
the remaining half (Lemmas L4–L6, §APPENDIX) and the result re-sites the
finding: the missing half is **not locality**, it is a budget/menu coincidence
(`q(n_a|h) ≡ 3/4`, verified on 68,750 / 19,767 / 6,868 pairs at 2 / 3 / 4
actors) — and that coincidence is **exactly what fails in `d42b1`**, where
`q(n_a|h) ∈ {1/2, 3/4}`. The mechanism analysis and the counterexample are the
same fact seen from two sides.

**Free window left on the table.** Exchange squares at bases `|h| = 4, 5`
reach depth **6 and 7** and require no new enumeration; they cost 62 s and add
`61,744` more closed squares, all exactly `1`. The raw grammar-1 flatness is
true on a window **~30× larger** than the one licensed.

---

## MAJOR 1 — `A_D` IS NOT ZERO IN THE SECOND GRAMMAR, AND THE FALSE STATEMENT IS INSIDE LICENSED CLAIM 1'S OWN WINDOW

**Where.** Note §5 licensed claim 1 (lines 218–220): "*On the d42b3 placement
grammar with actors (A,B) at depth ≤ 5, **and on the d42b1 transport grammar
at (A,B) depth ≤ 4 and (A,B,C) depth ≤ 3, every closed exchange square has
`dP_AB/dP_BA` exactly 1***… `[MEASURED]` on those windows"; §0 line 44 "Two
grammars, three arms, same answer"; §1 row T2.5; §2 F2 row; abstract line 1;
LOG #488's headline.

**Defect.** The receipt never computes an exchange square in `d42b1`. Its
grammar-2 arms (`SEC 4`, lines 896–909) run **only** `deletion_graph_holonomy`
— up-edge single-valuedness and cycle holonomy. The square statement is
asserted for those windows and labelled `[MEASURED]`. It is false.

**Recomputation (mine).** Same layer, same actor pools, same depths as the
receipt's own T2.5 arms — my enumeration reproduces the receipt's own history
and class counts exactly (`3,969` histories / `2,477` classes at `(A,B)` d≤4;
`3,424` histories at `(A,B,C)` d≤3), so it is the same object:

```
  d42b1 (A,B) depth<=4     closed squares 1546   half-open 40   both-blocked 142
      raw dP_AB/dP_BA  =  {1/2: 70, 2/3: 2, 1: 1458, 3/2: 6, 2: 10}
      half-open split  =  AB-only 28,  BA-only 12        (A_D = +/- infinity)
  d42b1 (A,B,C) depth<=3   closed squares 1554   both-blocked 42
      raw dP_AB/dP_BA  =  {1/2: 12, 1: 1542}
```

The defect already exists at depth 3, i.e. two events above the empty history.
A witness, in full, cross-checked by the independent `μ` route (products of
whole-history weights, the receipt's own D1 second route):

```
  h  = [('p','A',V0,0)]
  eA = ('r','A', {(A,V0,0)}, {(A,V0,0)})          # arbitrate own proposal
  eB = ('d','A','B', V0)                          # deliver V0 to B
  q(eA|h) = 1/4 ,  q(eB|h.eA) = 1/8   ->  dP_AB = 1/32
  q(eB|h) = 1/4 ,  q(eA|h.eB) = 1/4   ->  dP_BA = 1/16
  dP_AB/dP_BA = 1/2 ,   A_D = -log 2
  mu(h.eA.eB) = 1/256   vs   mu(h.eB.eA) = 1/128        (route 2 agrees)
```

The mechanism is a menu denominator: arbitrating first creates a second held
value, which doubles `A`'s delivery menu (`1/4 / len(opts)`), while delivering
first does not change the arbitration menu. **Every one of the 88 non-unit
squares and all 40 half-open squares involve a delivery event** — kinds
`(r,d) 68, (d,r) 8, (d,n) 6, (d,d) 4, (n,d) 2` and `(r,d) 12, (d,r) 4,
(p,d) 16, (d,p) 8`.

**Why this is MAJOR and not MODERATE.** (a) It falsifies a `[MEASURED]`
licensed claim on its own stated window. (b) It removes the unit's only
answer to its own question "is the flatness a grammar artifact?" — the answer
is **yes**. (c) LOG #488 names "TRANSPORT-SCOPE FLATNESS (does `A_D` stay 0
when deliveries and multi-proposer arbs enter?)" as the era's **next pin**,
while this unit's licensed claim already asserts it and the unit already had
the family in memory; the deciding computation is 6 s of the same run.
(d) T1.2's "no half-open square … a support-level, non-`U(1)` and non-`R+`
defect" is a grammar-1 row, but §0's "two grammars, three arms, same answer"
and licensed claim 1's second grammar carry it across; in `d42b1` there are
**40** half-open squares, i.e. genuine `±∞` support defects of exactly the
kind T1.2 rules out.
(e) The non-unit value set `{1/2, 2/3, 3/2, 2}` is **`R+`-valued with no
`U(1)` part**, which is precisely falsifier **F4**, recorded in the note's own
board (§2, line 111) as "not reached, vacuously".

**Required repair.** Delete the `d42b1` clause from licensed claim 1; restate
the flatness claim as `d42b3`-only; add the `d42b1` square census as a
first-class result with its own falsifier reading (F4 fires on the transport
grammar); correct §0's "two grammars, three arms, same answer" and the
abstract; correct LOG #488's "the closed scope is flat" to name the grammar;
and note that the era's second-wave pin is already answered negatively.

---

## MAJOR 2 — THE FLATNESS IS RAW-WEIGHT-SPECIFIC: ON THE NORMALISED KERNEL THE HOLONOMY GROUP IS NOT TRIVIAL, IT IS ⟨5/4⟩ ⊂ R+ — AND THIS IS D65's COMMITTED RESULT, UNCITED

**Where.** §0 ("its holonomy is **exactly 1** on every one of the 758
independent cycles"); §1 rows T2.2 / T2.4 ("the holonomy group … is the
**trivial group**"); §2 F2 / F4; §4(b) ("no other section of the phase bundle
is reachable by transport"); §5 claim 6 ("it is v10's substrate that is flat");
receipt `build_edges` (line 755) and `T2.4` (line 888).

**Defect.** The receipt transports the **raw** step weight `q(e|h)`. The v10
step weights are not conditional probabilities: the menu mass
`M(h) = Σ_e q(e|h)` is **not** constant — it takes `2` and `5/2` at two
actors, and `3, 7/2, 19/4` at three. `A_D = log dP_AB/dP_BA` is quoted from
v6 p4 §34, where `P` is a *stochastic* transport (v6's `stochastic_transport`
builds row-stochastic kernels), and the receipt's own fidelity control T1.0
uses **row-stochastic** matrices `_KA`, `_KB` (rows `[1/4,3/4]`, `[2/3,1/3]`;
`[1/2,1/2]`, `[1/5,4/5]`). So the one property that differs between v6's
object and v10's — normalisation — is the one property the fidelity gate
cannot see. The choice of raw over normalised is never stated, never
justified, and never run both ways, in a unit whose §5 makes a point of
running the contestable T3 reading both ways.

**Recomputation (mine).** With `p̃(e|h) = q(e|h)/M(h)`, the exchange-square
ratio is exactly `M(h·e_B)/M(h·e_A)` (the raw ratio being 1), so:

```
  grammar 1 (A,B):   M(h) spectrum over 6,471 histories  {2: 5963, 5/2: 508}
                     M is CLASS-CONSTANT (1565/1565)  -> the normalised
                     connection descends to records exactly as the raw one does

  normalised square ratios, receipt's window (bases |h| <= 3):
        {4/5: 220,  1: 1687,  5/4: 320}      540 of 2,227 squares non-unit
  base |h| = 4:  {4/5: 672,  1: 8144,  5/4: 1056}
  base |h| = 5:  {4/5: 3072, 1: 44384, 5/4: 4416}

  normalised holonomy census on the SAME 758 independent cycles:
        175 non-trivial;  value set
        {64/125, 16/25, 4/5, 1, 5/4, 25/16, 125/64}   = <5/4> subset of R+

  grammar 1 (A,B,C) depth<=4:  M spectrum {3: 5209, 7/2: 912, 19/4: 468};
        normalised square ratios {12/19, 14/19, 6/7, 1, 7/6, 19/14, 19/12}
        (912 of 2,439 non-unit)
```

**This is D65.** `note-d65-descent-conditions-result.md` — ROUND-1 REVIEWED
AND REPAIRED — is titled "*The generated law's **normalised** kernel does not
descend to a record measure; its **unnormalised** weight is order-independent*"
and its defect spectrum is `{1, 4/5, 5/4}`, the **same numbers**, identified
there as a pure mass-ratio coboundary. D72 rediscovers the raw half of an
already-decided dichotomy, states it without the qualifier that makes it true,
and never cites D65. The sentence "the holonomy group of `√q`-transport on the
generated line's record deletion graph is the **trivial group**" is true of the
raw connection and false of the process's conditional kernel.

**What survives.** `[sqrtq]`'s own quote is "the amplitude `∏√q` (the #152
budget amplitudes)", so **for the D42b4 lift specifically the raw weight is
the right object** and finding (b)'s phase-slot corollary survives — but only
as: *the `+1` is forced for the `∏√q` lift as D42b4 defines it*, not as "the
generated line is flat" and not as "no other section of the phase bundle is
reachable by transport". The pin's own P1 says both of its objects are
"functions of the process's own probabilities"; on the process's own
probabilities the answer is the opposite one.

**Required repair.** State the weight choice in §0, §1, §2 and every licensed
claim; run and report both connections; cite D65; downgrade "the trivial
group" to "the trivial group *for the un-normalised budget weight*"; record
that **F4 fires on the normalised connection** (an `R+`-valued holonomy with
no argument — the pin's own words for the founding slogan refuted in its
interesting direction).

---

## MAJOR 3 — T2 IS A COROLLARY OF T1.8, NOT AN INDEPENDENT MEASUREMENT: `μ` IS AN EXACT POTENTIAL, SO THE 758 CYCLES, THE THREE ARMS AND THE NEGATIVE CONTROL ARE ALGEBRAICALLY FORCED

**Where.** §0 ("The closure test then **generalises that** from squares to the
whole loop space"); §1 rows T2.1, T2.2, T2.3, T2.NC, T2.5; §6 residue 2 ("a
graph whose edge weights are single-valued can still have non-trivial
holonomy, so T2.2 is **not implied by** T2.1"); receipt lines 755–910.

**Defect.** Residue 2 is right that T2.2 is not implied by T2.1 — and misses
that T2.2 *is* implied by **T1.8**, which the receipt proves 200 lines earlier.
`μ(h·e) = μ(h)·q(e|h)` by definition (`mu_of`, `d42b3:251`). If `μ` is constant
on record classes (T1.8), then `φ(C) := μ(C)` is a well-defined node potential
and **every** up-edge weight is `φ(C₂)/φ(C₁)`. That single identity gives, with
no census:

* T2.1 (single-valuedness): two parallel up-edges `C₁→C₂` both equal
  `φ(C₂)/φ(C₁)`;
* T2.2 (holonomy `≡ 1`): a product of `φ`-ratios telescopes around any cycle;
* T2.3, T2.5, and the grammar-2 arms: same argument, and I verified `μ` is
  class-constant in `d42b1` too (0 failures on 2,477 and 2,128 classes);
* T2.NC (the negative control): multiplying one edge of an exact gradient by
  `3/2` **must** produce a defect. The control cannot fail, so "the detector is
  not blind" is not evidence that it is sensitive.

**Recomputation (mine).** On all 2,322 up-edges of grammar 1, `w = φ(C₂)/φ(C₁)`
with `φ = μ`: **2,322/2,322, exactly**. Cycle rank recomputed independently
(`E − V + C = 2322 − 1565 + 1 = 758`) — identical.

**Consequence.** "Two grammars, three arms, 1,827 independent cycles" (§4(b))
is one fact — class-constancy of `μ` — counted six times, and class-constancy
of `μ` is not new here: it is the gauge anchor the F-PAIR fixture already
carries (A3's "one `μ` per class"), and D65's review re-verified it globally at
depth ≤ 6. **And it is the reason the T2 instrument is blind in MAJOR 1**: a
gradient-flat record graph is compatible with a non-zero `A_D` on any square
whose two orders land in different record classes — which is where all 88
`d42b1` defects live (0/88 close at record level), and where all 872 of
grammar 1's comparable squares live too.

**Required repair.** Present T2.1–T2.5 as corollaries of T1.8 with the two-line
proof; drop the "758 / 1,827 independent cycles" as an independent evidential
count; replace the negative control with one that can fail (a substrate with a
genuine defect — `d42b1` now supplies one); and state the instrument's blind
spot explicitly.

---

## MAJOR 4 — THE DEPTH-FREE ARGUMENT COVERS 61 % OF ITS OWN SQUARES; THE OTHER 39 % ARE HELD BY A BUDGET COINCIDENCE, NOT BY LOCALITY

**Where.** §6 residue 1 ("the step weight `q(e|h)` is a function of the *view*
at `h` …, and for an incomparable pair neither event is in the other's view, so
the two step weights cannot depend on the order. If that argument closes it
turns F2 from `[MEASURED]` into `[THEOREM]`"); §4(b); LOG #488's bracketed
"`[MEASURED] not THEOREM — a candidate depth-free argument … is stated, not
closed: the round's primary target]`".

**Defect.** The argument's hypothesis is *incomparability*, and in this grammar
**39 % of the closed squares are comparable**. Two events appended at a common
base are causally comparable exactly when their register sets meet
(`regs_of`, `d42b3:32`); `regs_of` of a `p`/`n` event is `{actor}` and of an
`r` event is `{proposers} ∪ {new value}`. So the pair `(idle_A, any A-move)` is
comparable, closes in both orders, and is **outside the stated argument**:

```
  grammar 1 (A,B), receipt's window: 2,227 closed squares
        register-disjoint (the argument's domain)     1,355
        register-overlapping (comparable)               872   <- not covered
  bases |h| = 4 and 5:  3,712 and 18,880 more comparable closed squares
        (23,464 comparable closed squares in all, bases 0-5)
  three actors d<=4:  516 of 2,439 comparable;  four actors d<=3: 96 of 726
```

The comparable squares are not incidental: they are exactly the squares whose
two orders land in **different record classes**, i.e. the ones T2 cannot see
(MAJOR 3). So the note's two arguments for flatness — the locality sketch and
the holonomy census — have **complementary blind spots covering the same 872
squares**, and only the raw square census (T1.1) actually decides them.

**What I did about it.** I closed the argument; the completed proof is in the
APPENDIX. The load-bearing content is not locality:

* **L1–L3 (locality) are true and I proved them**, and they give exactly the
  1,355 disjoint squares. Verified independently: `q(e|h)` is a function of
  `(e, canon(down-set of e))` — 2,708 keys, **0 clashes** at depth ≤ 6; and
  `q(e_B|h) = q(e_B|h·e_A)` on 2,710 ordered disjoint pairs at bases ≤ 3 and
  on **43,051** disjoint closed squares across all arms (both weights checked
  in each), 0 violations.
* **L4 and L6 carry the other 872**, and they are *menu* facts.
  L6 is `q(n_a|h) ≡ 3/4` — because in a's past-local view exactly one of
  `has_p`, `has_r` holds. Verified: **68,750 / 19,767 / 6,868** `(history,
  actor)` pairs at 2 / 3 / 4 actors, spectrum `{3/4}` in every case;
  `(has_p, has_r)` census `{(T,F): 6458, (F,T): 6484}`, never `(T,T)` or
  `(F,F)`; available-base count ∈ `{0,1}`, never `≥ 2`.

**Why the re-siting matters.** `q(n) ≡ 3/4` holds because the propose-budget
`1/4` and the arbitrate-budget `1/4` are **equal** and the two options are
mutually exclusive in a's own view. Change either constant and the 872
comparable squares stop being flat while the 1,355 disjoint ones stay flat.
This is a *tuning*, not a structural theorem, and it is precisely what fails
one grammar over: in `d42b1` the idle budget is a three-way split
`1 − 1/4[has_p] − 1/4[has_am] − 1/4[has_d]`, the exclusivity is gone
(`q(n_a|h) ∈ {1/2, 3/4}`: `{1/2: 7738, 3/4: 200}`), L4 fails outright
(`(r,d)` pairs by the same actor are comparable closed squares with **no**
idle member), and `A_D ≠ 0` (MAJOR 1).

**Required repair.** Residue 1's argument must be restated with its hypothesis
(register-disjoint / incomparable) and its coverage (1,355 of 2,227); the
completed theorem, if adopted, must carry L4 and L6 as separate, *grammar-1
specific, budget-dependent* lemmas — and must state that it does not extend to
`d42b1`, where its conclusion is false.

---

## MAJOR 5 — THE `k = 5` CELL IS AVAILABLE, COSTS 2 SECONDS, AND REVERSES T3.B1 — AND IT IS THE ONLY CELL THAT MATCHES v7's OWN CONSTRUCTION

**Where.** Receipt line 928 ("*v10 records have at most DEPTH events, so
`k = 5` does not exist here*"); §1 T3 header ("*v10's records carry at most
`DEPTH` events, so `k = 5` does not exist here*"); §6 residue 4 ("`k = 5`
exists on exactly the deepest layer and was not run … `[OPEN]`").

**Defect.** The receipt's own census reports **1,138 record classes of depth
exactly 5**. `k = 5` does not merely "exist on the deepest layer" — it is
available on 1,138 records, and it is the **only** `k` that reproduces v7's
"five-record type" (`QUOTES['star']`), which is what the whole T3 port claims
fidelity to. `k ∈ {2,3,4}` are analogues; `k = 5` is the thing itself. The two
sentences in the receipt and in §1 flatly assert it does not exist.

**Recomputation (mine).** `flags_5` over the 1,138 depth-5 records:
**2 seconds**.

```
  k = 5 :  8 order types realised, 8 dual orbits, 4 non-self-dual
           odd orbits with a member ABSENT from the family:  4 / 4
           O spectrum (odd-orbit reading): {-1: 384, 0: 754}
           E spectrum (odd-orbit reading): { 0: 754, 1: 384}
           O sign-definite: max 0, min -1
```

**It reverses the T3.B1 finding.** §4(e) and §1 T3.B1 record, as one of the
unit's two self-caught corrections, that "the type-level one-sidedness is a
**window artifact**" — the fork type appears at depth 5, so the family is not
type-level one-sided. That is a `k = 3` statement. At `k = 5`, the faithful
port, **all 4 of 4** non-self-dual orbits have their dual member absent: the
type-level one-sidedness is **total**. The correction the unit is proudest of
is itself `k`-specific, and at v7's own `k` the original reading was closer to
right. (T3.B2's sign-definiteness does survive at `k = 5`.)

**Required repair.** Delete both "`k = 5` does not exist here" sentences; run
the cell; restate T3.B1 as a `k`-dependent statement with the `k = 3 / 4 / 5`
absent-orbit counts `0/1`, `1/2`, `4/4` side by side; move residue 4 from
`[OPEN]` to a measured row.

---

## MODERATE 1 — T3 IS ENTIRELY FLOAT, AND THE "EXACT CLOSED FORM" IT IS GATED AGAINST IS A FLOAT64 EVALUATION

**Where.** §1 row `T3.·.A/.B` ("the float port agrees with the **exact closed
form** `2·e^{−κE}·|sin(θE)|` at `|float − exact| = 0.000e+00`"); receipt lines
1090–1126 (`L()` uses `math.exp/cos/sin`; `worst_exact` uses
`math.exp`/`math.sin`); banner "exact Fractions on every v10 weight".

**Defect.** Both sides of that gate are `float64`. The comparison is
float-against-float, so `0.000e+00` says the two expression trees round
identically — not that anything is exact. The derivation *is* exact and
correct (I re-derived it); the **evaluation** is not, and §1's table sells the
agreement as an exactness result. `KAPPA_F = Fr(1,32)` is built as a Fraction
and then immediately floated (`float(KAPPA_F)`), which reads as exactness
theatre.

**Recomputation.** The identity
`L_naive(R*) − conj L_naive(R) = e^{−κE} ρ^{−O}(ρ^{−E} − ρ^{E})`, hence modulus
`2 e^{−κE}|sin θE|`, is exact and holds symbolically. Nothing in T3 requires
floats: `κ = 1/32`, `θ = π/6`, `E` integer, so `|sin(πE/6)| ∈ {0, 1/2,
√3/2, 1}` and the whole T3 table is closed-form. Relabel, or compute in
`mpmath`/`Decimal` and quote a real digit count.

## MODERATE 2 — THE `*`-CLOSURE STATISTIC IS A *LABELLED* ONE, AND THE UNLABELLED ANSWER IS `k`-DEPENDENT AND PARTLY OPPOSITE

**Where.** §1 T1.9; §4(d) "**The order-dual is not an operation on v10's
records.** 1,264 of 1,558 record classes have no in-family labelled
order-dual"; §2 F1 row; the licensed reading "`*` is a partial map on v10's
objects".

**Defect.** `dual_realised` (receipt line 677) asks whether the *same multiset
of events*, re-ordered, is an admissible history realising the dual order —
a labelled question. The order-type question gives a different and partly
opposite answer, and the receipt itself prints it: at `k = 3`, `0/1` odd
orbits have an absent dual member (the family **is** type-level dual-closed);
at `k = 4`, `1/2`; at `k = 5` (MAJOR 5), `4/4`. §4(d)'s prose sentence drops
the qualifier its own row carries.

**Repair.** Carry "labelled" in every statement of finding (d), and put the
type-level counts beside it.

## MODERATE 3 — THE MEASURED WINDOW WAS LEFT ~30× SMALLER THAN FREE

**Where.** §5 claim 1; §6 residue 1 ("The measurement is exhaustive on its
window"); receipt line 528 (`if len(h) + 2 > DEPTH: continue`).

**Defect.** Squares are censused only at bases `|h| ≤ 3` because the loop
guards on `DEPTH`. But `AD_ratio` only calls `admissible`, which needs no
enumeration: squares at bases `|h| = 4, 5` are computable from the *same*
depth-5 family and reach depth 6 and 7. The unit's own residue says the
window is where the argument stops, and the window was three lines and 62 s
from being 30× wider.

**Recomputation (mine).**

```
  base |h| = 4  ->  depth 6 :  9,872 closed, raw ratios {1: 9872}   ( 9 s)
  base |h| = 5  ->  depth 7 : 51,872 closed, raw ratios {1: 51872}  (53 s)
  total raw-flat squares, grammar 1 (A,B):  63,971  (vs 2,227 licensed)
  three actors  d<=4: 2,439 closed, all 1;  four actors d<=3: 726, all 1
```

This lands in the unit's favour and should be taken: licensed claim 1 can be
widened to depth ≤ 7 and to 3- and 4-actor pools at no cost.

## MODERATE 4 — FOUR OF THE FIFTY PASSES CARRY NO INDEPENDENT INFORMATION

**Where.** Receipt T1.3 (line 577), T1.7 (650), T2.4 (888), T2.NC (877).

**Defect.** T1.7's predicate is `set(ratios) == {Fr(1)}`, a strict
sub-predicate of T1.1's; T2.4's is `len(d1) == 0`, a sub-predicate of T2.2's.
T1.3 gates a statement true of **every** finite poset (`rev` is a bijection
`LinExt(P) → LinExt(P*)` because `σ` is a linear extension of `P` iff `σ`
reversed is one of `P*`) — a one-line theorem presented as a 6,464-history
measurement. T2.NC cannot fail (MAJOR 3). The "50 PASS / 0 FAIL" headline and
LOG #488's citation of it should not count these four as evidence.

## MODERATE 5 — THE FALSIFIER BOARD'S F3 AND F4 VERDICTS ARE HARDCODED BOOLEANS

**Where.** Receipt lines 1274–1275: `F3_fired = False  # measured below…` and
`F4_fired = False  # no defect exists…`.

**Defect.** In a receipt whose stated house rule is "no bare-constant
predicates", two of the four pre-registered falsifier verdicts are literal
constants assigned by hand, with the justification in a comment. `F1_fired`
and `F2_fired` are computed from gate variables; F3 and F4 are not. Given
MAJOR 2 (F4 fires on the normalised connection) and MAJOR 1 (F4's shape fires
on `d42b1`), a hand-set `F4_fired = False` is exactly the kind of constant the
rule exists to prevent.

---

## MINOR

1. **Bare-constant thresholds** contrary to the receipt's own banner: `1e-14`
   (T1.0), `1e-12` (T3 gates, twice per cell), `1e-15` and the range `0..399`
   (A2c). The A2c argmax holds on `0..3999` (I checked); the range is still a
   chosen constant.
2. **The determinism claim is note-only.** §0 asserts byte-identical output at
   `PYTHONHASHSEED ∈ {1,3,7,99,12345}`; only the default-seed run is committed
   (`data/d72_weld_exact.out`, whose D3 line prints `PYTHONHASHSEED =
   default`). I reran at `PYTHONHASHSEED=7`: exit 0, 50 PASS / 0 FAIL, and the
   output differs from the committed one on exactly two things — the timings
   and the echoed seed on the D3 line. The claim is true; no seeded artefact is
   committed to support it.
3. **"1,069 more of a second [grammar]"** (abstract) sums two different arms
   (different actor pool, different depth) into one number.
4. **T2.3's factor of two** (`2·log Hol_√q = A_D`) is asserted, never gated;
   the receipt computes the `q`-holonomy and calls it the `√q`-holonomy
   squared throughout without a line establishing the square-root branch.
5. **The 610 both-blocked pairs are counted and never analysed.** They are
   where the pin's question is *undefined*, and 2 of the 3 comparable-pair
   families (p/p and p/r, same actor) live entirely there — the structure that
   makes grammar 1 flat is visible in that bucket and is not reported.
6. **§4(a)'s downgrade of D71b Clause 2 is right and understated.** The
   closed form shows the `0` is an identity; it also shows the `1.82` carries
   exactly one bit about the `N=9` universe ("some record has `E=3`"). I
   confirmed the argmax is `E = 3` over `0..3999` and that `2e^{−3/32}`
   matches all 32 published digits. Worth stating that A2 (296 s of the 343 s
   budget) is therefore an anchor that A2c reproduces in microseconds — the
   run is a fidelity check on the *port*, not evidence for the constant.

---

## APPENDIX — THE DEPTH-FREE ARGUMENT, CLOSED (for `d42b3` only)

**Theorem.** Let `h` be any history of the `d42b3` placement grammar over any
finite actor pool, and let `e_A ≠ e_B` both be admissible at `h` with both
orders admissible. Then `q(e_A|h) q(e_B|h·e_A) = q(e_B|h) q(e_A|h·e_B)`, i.e.
`A_D ≡ 0`, **at every depth**.

*L1 (past-locality). PROVED.* `admissible(acts, e)` (`d42b3:160`) computes
`pred = event_poset(acts+[e])` and `view = View(acts2, pred, pred[j])` with
`j = |acts|`. Every field the weight reads — `props`, `arbs`, `resolved`,
`superseded`, `live`, `holdings`, `incomparable`, `edges`, `components` — is a
function of `{acts2[i] : i ∈ pred[j]}` and of `pred` restricted to that set,
which is downward closed. Hence `q(e|h) = Q(e, D(e))` where `D(e)` is the
labelled induced sub-poset on `e`'s down-set. *[Verified: 2,708 distinct
`(e, canon(D(e)))` keys at depth ≤ 6, 0 clashes.]*

*L2 (comparability = register overlap). PROVED.* `event_poset` (`d42b3:38`)
links `j` to `last[r]` for each `r ∈ regs_of(acts[j])`. Appending `e_A` at
index `|h|` sets `last[r] = |h|` exactly for `r ∈ regs(e_A)`, and no strictly
earlier event's past can contain `|h|`. Hence
`e_A ∈ pred[e_B] ⟺ regs(e_A) ∩ regs(e_B) ≠ ∅`.

*L3 (disjoint ⇒ commuting). PROVED from L1+L2.* If the register sets are
disjoint, `D(e_B)` in `h·e_A·e_B` is the same index set with the same labels
and the same induced order as in `h·e_B`; so `q(e_B|h·e_A) = q(e_B|h)`, and
symmetrically. Ratio `= 1`. *[Verified: 43,051 disjoint closed squares across
all arms plus 2,710 ordered disjoint pairs at bases ≤ 3 — 0 violations.]*

*L4 (an overlapping closed square always contains an idle).* `regs` of a `p`
or `n` event by `a` is `{a}`; `regs` of an `r` event is
`{proposers} ∪ {new value}` and admissibility forces the initiator into the
proposers. So an overlap between two non-idle events means they share an actor
`a`, and: **(p,p)** ⇒ same actor, and after `a` proposes on its unique
available base that base carries a live proposal of `a`, so
`prop_options_in_view` empties (L6a) and the second `p` is blocked;
**(p,r)** ⇒ `a`'s proposal is in the arbitrated component, so after the `p`
the component's `ckey` no longer matches and after the `r` the base is
superseded — blocked either way; **(r,r)** ⇒ two arbs sharing a proposer, and
the first supersedes the base and resolves the proposals, so the second's
`ckey`/component no longer matches. Hence one member has kind `n`.
*[Verified: 23,464 comparable closed squares at 2 actors (bases 0–5), 516 at
3 actors, 96 at 4 actors — **0** without an idle member.]*

*L5 (idle inertness). PROVED.* `View.props` filters on kind `'p'` and
`View.arbs` on kind `'r'`; a kind-`'n'` act contributes to no field. So adding
`('n',a)` to a down-set changes no weight: `q(e|h·n_a) = q(e|h)`.
*[Verified: 0 violations on every arm — e.g. 19,764 and 6,864 evaluations at
3 and 4 actors.]*

*L6 (the idle weight is the constant 3/4).* `q(n_a|h) = 1 − ¼[has_p] −
¼[has_r]` evaluated in `a`'s own past-local view. **L6a (single available
base):** `holdings(a) = {V0} ∪ {value created by each arb in the view in which
a is a proposer}`; each such arb supersedes its own base; `a`'s own chain
contains all of `a`'s own events, so `a` holds at most one live proposal at a
time and can arbitrate a given base at most once. Hence `a`'s holdings form a
chain whose members are all superseded except the newest. **L6b:** therefore
exactly one of two states holds — `S0` (no live proposal of `a`: the unique
non-superseded base is free ⇒ `has_p = T`, `has_r = F`) or `S1` (a live
proposal of `a` on that base ⇒ `has_p = F`, `has_r = T`) — and the transitions
`S0 →(a proposes)→ S1 →(any arb resolving a's proposal)→ S0` preserve the
dichotomy. Either way `q(n_a) = 3/4`. *[Verified: 68,750 / 19,767 / 6,868
`(history, actor)` pairs at 2 / 3 / 4 actors; spectrum `{3/4}` in every case;
`(has_p,has_r)` never `(T,T)` or `(F,F)`; available bases ∈ `{0,1}`.]*

*Proof of the theorem.* If `regs(e_A) ∩ regs(e_B) = ∅`, apply L3. Otherwise
by L4 one member is `n_a`; by L5 `q(e|h·n_a) = q(e|h)`; by L6
`q(n_a|h) = q(n_a|h·e) = 3/4`. Both products equal
`3/4 · q(e|h)`. ∎

**Status I would give it.** L1, L2, L3, L5 are proofs from the committed
source and can be labelled `[THEOREM]` today. L4 and L6 are case analyses over
the layer's admission rules; I have written them out and verified their
statements exhaustively on every arm I could reach (depth ≤ 7 squares, depth
≤ 6 idle weights, 2/3/4 actors), but they are not machine-gated, and L6a's
induction deserves a receipt. **So: `[THEOREM]` for the 61 % locality half;
`[PROVED, ungated]` for the rest; and — the point of MAJOR 4 — the rest is a
budget coincidence of `d42b3`, false in `d42b1`, so the depth-free result must
never be stated for "the generated line" without naming the grammar.**

---

## CHECKED AND CLEAN

* The receipt reruns at `PYTHONHASHSEED=7`, **exit 0**, 50 PASS / 0 FAIL,
  445 s, output identical to `data/d72_weld_exact.out` apart from timings and
  the echoed seed. Substantive-negative exit protocol honoured (exit 0 with F2
  fired; `sys.exit(1)` reserved for anchor failure and correctly gated).
* The pin is genuinely STRICT and was committed alone in `#487` (85 lines,
  no code) one commit before the receipt and result landed in `#488`; the four
  falsifiers are pre-registered, and F2's "publishable
  negative / no null outcome" clause is honoured — this unit does deliver a
  negative and does not dress it as a positive.
* The text-slice loader with fidelity markers and gated exit-freedom is sound;
  I re-executed all four slices independently and got identical namespaces.
  Neutralising `sys.exit`/`os._exit` inside the slice is the right call and is
  correctly restored in a `finally`.
* Anchors: A1 antisymmetry gap `2.220e-16` and eventless-loop rms `0.0e+00`;
  A2 `131,526` records at `N = 9`, naive `1.8210207227600682556870097725525`,
  `L_dual = 0`; A2b involution on all 1,956 `N = 7` records; A2c
  `2·exp(−3/32)` to all 32 published digits and `E = 3` the argmax (I extended
  to `E ∈ 0..3999`); A3 32 sequences / 23 classes / `Z_seq = 4` / `Z_class = 3`.
* T1.0's fidelity control is correctly reasoned *within its own scope* — the
  uniform-start factor does cancel in the ratio, and my exact Fractions agree
  with v6's float `A_D` at `2.2e-16` on all four atoms. (Its scope defect is
  MAJOR 2.)
* T1.1, T1.2, T1.3, T1.4, T1.5, T1.6, T1.8, T1.9 all reproduce exactly:
  `2227 / 610 / 0 / 0`, `{1: 2227}`, 6,464 histories, `32` and `28`, `2214`,
  `0`, `578`, 1,565 one-`μ` classes, `294 / 1264`.
* T2.1/T2.2's graph numbers reproduce exactly (`1565 / 2322 / 0 / 758 / 0`),
  as do the grammar-2 arms' `2477 / 2900 / 424` and `2128 / 2772 / 645` and
  their history counts `3,969` and `3,424`. (Their *reading* is MAJOR 3.)
* T3's `k = 2,3,4` order-type censuses, orbit counts, `O`/`E` spectra and the
  depth-stratified fork/merge table `{3:…, 4:…, 5:{6:216, 36:1592}}` reproduce
  exactly; T3.B2's sign-definiteness holds at every `k` I ran including `k = 5`.
* T3.CTRL is a real and well-designed control, and its conclusion — the `0` is
  an identity of the ansatz — is correct; I re-derived the identity
  symbolically. §4(a) is the unit's best finding and is right.
* The frozenset-`repr` determinism trap and its `stable_key` repair (§4(e))
  are correctly diagnosed and correctly fixed; D2/D3/D4 are genuine
  order-independence probes and pass under my own reimplementation.
* §7 is accurate: no committed file was edited by the unit.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-27)

All findings applied; receipt rerun 77 PASS / 0 FAIL (468 s), every
referee number reproduced exactly (the one divergence — 175 vs
148/118 non-trivial basis cycles — is spanning-forest-dependent; the
basis-independent image group <5/4>, exponents -3..3, is identical
and is what the gate reads; both builds printed).  The round's
theorem (L1-L6) is adopted as §4 of the note with authorship
credited; grammar-1 raw flatness is [THEOREM at closed scope], its
L4-L6 half gated as the equal-budget coincidence with the d42b1
counter-census (idle spectrum {1/2, 3/4}; 533/1,073 comparable
squares idle-free) carried as the scope clause.  THE TRANSPORT
CENSUS IS GATED (T6): 88 non-unit closed squares {1/2:70, 2/3:2,
3/2:6, 2:10} + 40 half-open at (A,B) d<=4; 12 more at three actors;
ALL delivery-bearing; shallowest at depth 3; 0/88 close at record
level — and the NEW structural facts: mu is class-constant in
grammar 2 too (its record graph is an exact gradient — that IS the
instrument's blindness), and record-level closure <=> register
disjointness (T2.3b).  Normalized holonomy gated: image <5/4>, R+,
no U(1); anchored to D65's committed masses.  k=5: T3.B1 REVERSED
as the referee found (4/4 dual-absent at v7's own k; the
one-sidedness is total there); T3.B2 survives.  F3/F4 computed
predicates — F4 FIRES on both objects.  9 of 77 passes flagged
no-independent-information with the dependency map printed.
**THE D74 HANDOFF, sharpened by the repair: the transport defect
values 2/3 and 3/2 sit OUTSIDE <5/4> — the transport holonomy is
NOT the D65 coboundary family alone.  D74 = characterisation:
the record-level carrier (register-overlapping squares), the
group generated, whether it is a coboundary at all, and the
odd-sector U(1) search.**  TERMINAL for round 1.
