# K1 OPERATOR-LENS REVIEW — paper-20, the coupling unit

**Seat:** K1 OPERATOR (panel protocol frozen at v14 ledger #180).
**Object at 9b1860e, all five sha256-12 verified at open and at close:**
`v14/paper-20-coupling.md` **b328a8278fac** · `v14/code/coupling_exact.py`
**9e71cf511ab3** · `coupling_output.txt` **3e3d04222782** ·
`coupling_receipt.json` **3ca0308b6c19** · pin `v14/note-coupling-pin.md`
**7c6e9e44fc2c**. (HEAD is 2c00e29; its diff against 9b1860e touches
`v14/LOG.md` only, and the five objects are byte-identical at both.)

**Method.** Everything below was rebuilt from the pin's and the paper's
mathematical description in a scratch tree that never imports, execs or calls
`coupling_exact.py`. My own Z[w]/(w²+w+1) arithmetic (self-checked for norm
multiplicativity on a 6 561-product grid), my own arena, coin, shift, menu,
kernel, emission and update, my own exhaustive tree walk. The delivered code
was read for **declared semantics only**, never used as an oracle. Two
exceptions, both stated: the R = 3 grammar drive (48 events / 9 divisions /
the 30-event R = 2 anchor) is the committed layer's own and I re-ran it in an
independent off-tree git-less process rather than re-implementing an
admissibility rule the paper explicitly refuses to re-implement; and the two
named mutants were exercised through the delivered CLI in that same mirror.

---

## VERDICT

**GRADE: AWF — ACCEPT WITH FIXES.**

The headline reproduces exactly. **Zero false numbers.** Every number in all
three verdict segments, in §5–§9's tables and in the gate transcript came out
of my independent rebuild bit for bit. The negative is not fragile: it
survives dropping either of the two refusal declarations on its own, and it
survives replacing the coin with any of the five *other* admissible
S₃-covariant unitary coins on this arena.

What fails is not the measurement. It is **four load-bearing attributions and
one gate's coverage**: one head sentence is true only under an undeclared
restriction (M-1), one §4 sentence credits a definitional identity to a
mechanism that measurably does not carry it (M-2), the numeral-coverage gate
does not scan the paper's own contrast and ladder tables and I passed a
corrupted paper through all 44 paper gates to prove it (M-3), and one choice
row's "MEASURED" is a comparison of a run with itself (M-4).

---

## 1. WHAT REPRODUCED (72 delivered results, 0 mismatches)

**Arena** — q = [[1, −1/2], [−1/2, 1]] and det = 3/4 at 9 of 9 sites; posdef
9 of 9 by Sylvester; n = 1 at 27 of 27 cells; split fiber 0 at 27 of 27 and
product fiber 0; realised co-division relation = the target's Cayley incidence
at 27 of 27 pairs, meeting the undeclared ANT direction in **0** (and I
confirm the stronger structural fact: the realised relation is exactly the
complement of the 9 pairs inside the 3 ANT lines, so 27 = 36 − 9); 1296 =
3!·(3!)³. In the independent off-tree process: 48 events, 9 division events,
maxhits 1, refusal None, the R = 2 anchor identical at 30 events, 1296 cited
with 19 occurrences in the weld's receipt. **Sections 1–6 of the off-tree
`--numbers` transcript are byte-identical to the committed output** (110
lines diffed clean).

**Walk** — 6 nonzero differences, multiplicities [1,1,1,1,1,1]; axis stencil
[3,3]; 343 maps, 18 unitary, 0 non-monomial; 4 coin solutions on the delivered
grid, 2 non-trivial, all Grover; 3G·3Gᵀ = 9I exactly; the Z₃ phase alphabet
closes; **6 of 9** momentum sectors with trace outside Z[w].

**Law transport** — G(x,1) = M(x) at **406 413** site-steps, 0 violations;
arbitrary exact re-pricing 406 413 of 406 413; k₁ = q/M at **1 215 681**
entries, 0 violations; menu-mass-is-density **187 155**, 0 violations;
terminal-condition falsifier kills the identity at **10**.

**Ensemble** — A-COUPLED 3, 27, 486, 10527, **284078**; A-FROZEN 3, 27, 486,
9234, **212382**; B-COUPLED and B-FROZEN 3, 27, 486, 11664, **314928**; branch
mass exactly 1 at all 20 levels.

**Gate 1** — composition census **948 297 / 0**, and every class separately:
norm 45 157, site 406 413, column 406 413, emission_total 45 157, total
45 157.

**Gate 2** — 18 of 18 rows differ, at both readings. Every fraction in §7's
table, character for character:

| row | coupled | frozen |
|---|---|---|
| inverse participation | 35971074413334039128803/239299329230617529590083 | 2306155/14348907 |
| exit probability | 927415552/847288609443 | 0 |
| posdef distribution | {8: 927415552/847288609443, 9: 846361193891/847288609443} | {9: 1} |
| determinants | 0, 1, 2, 3, 3/4, 7/4 | 3/4 |
| max cell | 4 | 1 |
| constant curvature | 7598838656/22876792454961 | 1 |

**The horizon-5 exit** — threshold exactly 5 on **both** readings; exit
probability **0** at horizons 1, 2, 3, 4 (proved by my own ladder, not read
off theirs); 927415552/847288609443 at the Born menu and 37440224/5811307335
at the record menu; frozen exit identically 0 at every horizon of both arms;
det < 0 **never** reached; max-cell column 2, 2, 3, 3, 4. **I also verified
the mechanism §9 asserts:** the only inadmissible site-count multiset reached
at horizon 5 is (1, 1, 4), whose determinant is exactly 0, and the reachable
multisets are {(1,1,1), (1,1,2), (1,1,3), (1,1,4), (1,2,2), (1,2,3), (2,2,2)}
— the singular boundary is reached and the indefinite region is not merely
unobserved, it is arithmetically out of range at this horizon.

**Gate 3** — all 10 battery rows at both readings, 0 polarity mismatches;
0 witnesses; reverse {K6, K7, K8}; restated {K9, K10}; K5 repeat_states 0 on
all four arms; total emitted 5 coupled / 0 frozen. Staleness: **2 455**
checks, every ψ-internal closure clean, the stale field admissible and not the
welded record.

**Fibers** — order G·D moves 7 of 9, D·G moves 5; orientation ipr equal;
init-coin 0 and 1 equal, 2 different.

**Paper binding** — 68 distinct paper numerals, every one located in the
receipt bytes; the 3 fenced segments verbatim in the output and matched to the
receipt's `verdict.arena / .gates / .walk_law`.

**Mutants, off-tree, git-less, hostile PATH** — `MUT-COIN-FREE` → died at
G-COIN-FORCED, exit 1; `MUT-BRANCH-MASS` → died at G-BRANCH-MASS, exit 1. No
artifact written by either.

---

## 2. WHERE THE NEGATIVE IS STRONGER THAN THE PAPER CLAIMS

Two results the paper is entitled to and does not take.

**S-1. The refusal is doubly grounded, not singly.** My brief flagged the
selector's UPDATE-RULE-RESTATED refusals of K9/K10 as load-bearing: if a
refusal is wrong, NO-WITNESS flips. It does not. I flip-tested both
declarations independently:

| perturbation | witnesses |
|---|---|
| drop the UPDATE-RULE-RESTATED stamp on K9 and K10 | **0** (class filter still excludes them) |
| reclassify K9 and K10 as PSI-INTERNAL, keep the stamp | **0** (stamp still excludes them) |
| both together | K9, K10 |

NO-WITNESS therefore survives the failure of *either* refusal declaration
alone. And the stamp is not merely defensible, it is **provably correct**:
K9's coupled leg is Σ_l w(x,l) = p(x)·Σ_l k(l|x) = p(x), an identity that
holds for any coin, any reading and any record whenever the kernel is
column-stochastic. I verified this on 7 200 randomised checks with foreign
Born data and foreign count fields at both readings — 0 failures. The head's
"BOTH STAMPED UPDATE-RULE-RESTATED AND REFUSED BY THE SELECTOR" understates
its own instrument.

**S-2. Staleness blindness is not a horizon-3 result.** §8.3's 2 455 checks
are taken at the reduced horizon 3, which the paper does not say. I re-ran the
stale frozen arm at the unit's own declared horizon 5: **1 040 065 checks,
every ψ-internal closure still clean** (only the RECORD-COUPLED sourcing row
registers violations, as it must on a frozen arm). The theorem is stronger
than delivered.

---

## 3. FINDINGS

### MAJOR M-1 — the coin-forcing theorem is not a theorem at the arena's own ring; a head sentence carries an undeclared restriction

**Claim under test.** §3.2 and the head: "4 SOLUTIONS OF THE S_3-COVARIANT
UNITARITY CONDITIONS, 2 NON-TRIVIAL, EVERY ONE OF THEM +/-GROVER"; §11 row 4
prices F4-COIN as **DERIVED, fiber 1**.

**Measured.** The stated conditions are |a|² = 1 and a·b̄ + ā·b + 3|b|² = 0.
The delivered scan solves them over a ∈ {1, −1} and b ∈ **Q** — a reality
restriction that appears in the code's docstring ("with a real") and **nowhere
in the paper**, and that is precisely what produces the answer 4. Solved
instead over **(1/3)Z[w]** — the ring the walk's own phases w^n and the Grover
coin's own entries both live in, and the ring §3.3 derives from the arena's
own field F₃ — the conditions have **36 solutions, 30 non-trivial, of which
only 6 are ±Grover times a unit**; up to a global phase there are **6 distinct
coins**, of which exactly one is ±Grover:

    c = b/a  ∈  { 0,  −2/3 (Grover),  w/3,  (−1+w)/3,  (−1−w)/3,  (−2−w)/3 }

Explicit witness, verified unitary by full C·C* = I in exact Q(w) arithmetic
and verified to commute with all six permutation matrices:

    a = 1, b = w/3;   3C = [[3+w, w, w], [w, 3+w, w], [w, w, 3+w]]

This is S₃-covariant, exactly unitary, entries in the arena's own (1/3)Z[w],
and it is not ±Grover. The theorem as stated is false; the theorem with
"and b/a real" is true.

**Does it move the verdict?** I ran the walk to the full horizon 5 on all four
hidden non-Grover coins, coupled and frozen. It does not:

| coin | leaves (coupled) | consistency violations | obs rows differing | exit threshold | exit probability at 5 | det < 0 |
|---|---|---|---|---|---|---|
| Grover c = −2/3 | 284078 | 0 | 9 of 9 | **5** | 927415552/847288609443 | no |
| c = w/3 | 314627 | 0 | 9 of 9 | **5** | 145274395/94143178827 | no |
| c = (−1+w)/3 | 214772 | 0 | 9 of 9 | **5** | 646/177147 | no |
| c = (−1−w)/3 | 313842 | 0 | 9 of 9 | **5** | 833849422/282429536481 | no |
| c = (−2−w)/3 | 192258 | 0 | 9 of 9 | **5** | 2087/531441 | no |

On every member: exact composition, not inert, K5 holds on both stages, K7
frozen-true/coupled-false, K8 frozen exit zero, threshold exactly 5, singular
boundary only. **The verdict shape is invariant across the whole hidden
family; the numbers are coin-specific** (Grover happens to give the *smallest*
exit probability of the five).

**Repair.** (a) §3.2 and §11 row 4: F4-COIN becomes **DECLARED**, fiber 6 (up
to global phase), with the reality restriction stated as the selector, or
**DERIVED-UNDER-A-DECLARED-REALITY-CONDITION** with the condition printed.
(b) The head's `COIN-FORCED-BY-THEOREM` segment must say what it scanned —
e.g. "4 SOLUTIONS OVER REAL a AND b; 6 UP TO PHASE OVER THE ARENA'S OWN
(1/3)Z[w], OF WHICH ONE IS +/-GROVER". Because this is a head segment bound by
G-PAPER-HEAD-VERBATIM and G-VERDICT-RECONSTRUCTED, **this repair requires a
re-delivery, not a prose edit.** (c) The five-coin table above is a free
strengthening: it converts a broken forcing claim into a measured invariance
claim, which is the better result.

### MAJOR M-2 — "the row that could have failed" cannot fail, and the mechanism it names measurably does not carry it

**Claim under test.** §4 and G-LAW-TRANSPORT: "under reading A the law's local
menu mass M(x) is exactly the walk's own local Born mass p(x), at 187 155 of
187 155 site-steps — **because the coin is site-block-diagonal**, which is a
property of the walk and not a stipulation about the law."

**Measured.** Under reading A the menu is *defined* as q(l|x) = |(Cψ)(x,l)|²,
so M(x) = Σ_l q(l|x) is the post-coin site mass by construction; the check
`M != post[s]/den` is an identity in the definition, not a consequence of the
coin's block structure. I tested the mechanism directly, as my brief required:
I built a coin that is **exactly unitary but not site-block-diagonal** (Grover
on the link register composed with a cyclic permutation of the nine sites) and
re-took both rows over three steps —

| row | checks | violations |
|---|---|---|
| menu-mass-is-density (the row §4 calls "could have failed") | 27 | **0** |
| site-block-diagonality | 27 | **15** |

The row passes at 27 of 27 with a coin that violates the very property it is
credited to. The property site-block-diagonality actually buys is
p_post(x) = p_pre(x), which is the **`site` class, 406 413 checks, 0
violations** — and §3 already names that one correctly as "the law
transport's own precondition".

**No number is wrong.** 187 155 and 0 are right. The causal sentence and the
"could have failed" framing are wrong.

**Repair.** In §4 and in G-LAW-TRANSPORT's statement, move "the transport's
content is the row that could have failed" from the 187 155 mass-is-density
row to the **406 413 site row**, and relabel the 187 155 row as what it is —
the reading-A menu's definitional consistency, retained as a type check.
Alternatively, give the row content by defining reading A's menu from the
**pre-coin** site mass, in which case site-block-diagonality genuinely becomes
its premise. Same fix applies to G-CONSISTENCY's "site-block-diagonality gives
Σ_l k₁(l|x) = 1" — Σ_l k₁ = 1 follows from k := q/M alone.

### MAJOR M-3 — the numeral-coverage gate does not scan the paper's own tables; a corrupted paper passes all 44 paper gates

**Claim under test.** §14: "The paper under test is checked in the same run
for claim rendering, numeral coverage **including the fenced verdict blocks**
…"; G-PAPER-NUMERAL-COVERAGE reports "341 numerals … unregistered numerals:
none".

**Measured.** `paper_coverage` strips inline code spans
(`INLINE_RE.sub(" ", …)`) before scanning the prose. Every value in §7's
contrast table and every cell in §9's ladder table is inside backticks, so
**none of them is scanned**. I made this a measurement rather than a reading:
I corrupted two load-bearing values inside those spans —

    `2306155/14348907`          ->  `2306156/14348907`        (§7, frozen ipr)
    `7598838656/22876792454961` ->  `7598838657/22876792454961` (§7, curvature)

— and ran `--verify-paper` on the corrupted file in the provisioned mirror.
Result: **exit 0, "44 gates, all passed", G-PAPER-NUMERAL-COVERAGE PASS,
"unregistered numerals: none".** The head's fenced blocks *are* protected by
the fenced addendum, and the nine G-PAPER-CLAIMS sentences are protected; the
body tables a reader will quote are not.

**Repair, verified liftable.** Route inline code spans through the fenced rule
as well (i.e. collect `INLINE_RE.findall` on the fence-stripped text and scan
each span with `NUM_FENCED_RE`, instead of substituting them away). I
simulated the repair against the delivered receipt: the **clean** paper has 42
numerals inside 81 inline spans and **0 unregistered** under the repair, while
the **injected** paper yields exactly the two corrupted tokens. The repair
catches the injection and costs the clean paper nothing.

### MAJOR M-4 — F9-INIT-SITE's "MEASURED" compares a run with itself

**Claim under test.** §11 row 9: "`F9-INIT-SITE` | **MEASURED** | 1 | the
start site, measured invariant by the arena's own translation covariance";
G-FIBERS evidence "start-site fiber measured invariant True", and that boolean
is part of G-FIBERS' pass condition.

**Measured.** `run_arm` has **no start-site parameter** — the start is
hard-coded to `cell(SITE_INDEX[(0,0)], init_coin)`. The measurement is

    base    = run_arm(FIBER_T, True, "A", light=True)[...]["p_site"]
    shifted = run_arm(FIBER_T, True, "A", n0=WELDED, light=True)[...]["p_site"]

and `n0=WELDED` **is the default** (`n0=None → WELDED`). The two calls are the
same call. The comparison is vacuously True and never varies the start site.

**The underlying claim is true; I measured it properly.** Adding a start
parameter and running from (1,0): the site distribution is the exact
translate of the base distribution (list equality is **False**, translate
equality is **True**), and translation-invariant functionals agree exactly —
ipr = 33596579/129140163 from (0,0), (1,0) and (1,1) alike.

**Repair.** Give `run_arm` a `start` argument, run at least two start sites,
and compare **the translated distributions** (naive list equality fails by
construction and would have red-flagged the vacuity immediately). Report the
ipr triple above as the measurement.

### MINOR m-1 — K6-BLOCH is measured with K7's observable

`measure_battery` sets K6's frozen leg to a hard-coded `True` and its coupled
leg to `Fraction(C["final"]["curvature_constant_probability"]) == 1` — which
is *identical* to K7's coupled leg. The two SYMMETRY rows of the "two-way"
battery are therefore the same measurement. The correct observable exists and
is computed but unused: `translation_invariant_probability`. I measured K6
with its own stated observable — frozen 1, coupled 0 — so **the polarity is
unchanged (True, False) and the verdict does not move**, but §8.2's "3 rows
pass frozen and fail coupled" currently rests on 2 independent rows and one
duplicate. *Repair:* set `mf`/`mc` from `translation_invariant_probability`
(frozen 1, coupled 0 at horizon 5).

### MINOR m-2 — the scalar theorem's "exhaustive check" has zero discriminating power

§3.1: "checked exhaustively as well as proved — over a declared alphabet of 7
values, 343 maps scanned, 18 unitary, 0 of them non-monomial — and the
contrast is exact". The alphabet is {0} ∪ units of Z[w], i.e. exactly the
norm-≤-1 elements of Z[w]; over it Σ|c_v|² = 1 forces one nonzero coefficient
by integrality alone, with no reference to the offset set. I ran the identical
scan on **R4b's own axis stencil**, where the paper says interference
survives: **343 maps, 18 unitary, 0 non-monomial — the same three numbers.**
The scan cannot tell the two stencils apart. (The multiplicity contrast
[1×6] vs [3,3] *is* the real content and is correct; the theorem is true.)
*Repair, with numbers:* scan the alphabet (1/3)Z[w] with |c| ≤ 1 (37 values,
50 653 maps), which discriminates properly — **LINKS: 18 unitary, 0
non-monomial; AXIS: 216 unitary, 198 non-monomial**, one example being
c = (−3−2w, −1−w, 1)/3. That is an exhaustive check that corroborates
something.

### MINOR m-3 — "the orientation fiber … measured inert" is inert on the ipr only

§11: "The orientation fiber and the start-site fiber are measured inert." The
instrument records only the ipr for that fiber. On the full declared
observable set at the reduced horizon, PLUS vs MINUS differ in **2 of 9**
rows — `p_site` and `emission_field` — as the arena's own reflection (the
distributions are exact reversals of each other). *Repair:* "measured inert on
the inverse participation; p_site and emission_field are its reflection."

### MINOR m-4 — 406 413 of the 948 297 composition checks are definitional

Of the five classes, `norm` (45 157), `total` (45 157) and `site` (406 413)
are contentful; `column` (406 413) is Σ_l q/M = 1, an identity in the
definition of k₁ that cannot fail for any coin, menu or record (same 7 200
randomised checks as S-1); `emission_total` (45 157) reduces to `total`. The
gate's own framing — "unitarity × column-stochasticity **compose**" — is
honest, since composing an identity with a theorem is the claim. But §6's
"Nothing here is an aggregate: every site of every branch of every step is
compared against its own value" invites the reading that all 948 297 could
have failed. *Repair:* one clause in §6 marking the `column` class as the
kernel's definitional leg.

### MINOR m-5 — two undisclosed / vacuous instrument details

(a) §8.3's 2 455 staleness checks are taken at horizon **3**, not the unit's
declared 5; disclose it (and see S-2, which upgrades it for free).
(b) G-FIBERS' `measured_members` is `len({...}) >= 1` on three sets, which is
true for any non-empty set; it binds execution only via KeyError. Change to
the intended cardinality test or say what it binds.

---

## 4. THINGS I PRESSED THAT HELD

- **The horizon-5 exit is not an artifact of the update semantics.** Threshold
  5 with 0 below is reproduced independently at both readings, on my own
  ladder, and the frozen control's exit is identically zero at every horizon
  of both arms.
- **"No indefinite form is reached" is not a lucky sample.** Only (1,1,4) is
  inadmissible at horizon 5 and its det is exactly 0; det < 0 would need
  (1,1,5), which is out of range at max cell 4.
- **The 18-row contrast is not carried by a single volatile observable.** All
  18 rows differ, at both readings, and the six §7 fractions reproduce exactly.
- **The battery's polarity pre-registration is honest.** 0 mismatches on my
  own measurement of all 20 row-readings.
- **The `COUPLING-INERT` and `COUPLING-BLOCKED` branches were live.** The
  transport falsifier genuinely kills at 10; the leaf-count and observable
  differences are real, not stipulated.
- **Off-tree correctness.** The `--numbers` transcript from a git-less mirror
  with a hostile PATH is byte-identical to the committed output over
  sections 1–6, and both mutants die at their named gates without writing.

---

## 5. RECOMPUTATION COUNT, HONESTLY

**72 delivered results re-derived from scratch with my own machinery, 0
mismatches** (15 arena, 12 walk, 6 law, 7 ensemble, 24 gate/observable/ladder,
5 fiber, 3 paper-binding). Plus **8 new measurements the delivered run does
not take**: the six-member S₃-covariant coin family and its horizon-5
behaviour on all five non-Grover members; the non-block-diagonal-coin
mechanism test; the K9 identity test (7 200 randomised checks); the proper F9
translation test; the paper-gate injection test; the discriminating scalar
scan; the staleness theorem at horizon 5 (1 040 065 checks); the exit-mechanism
enumeration. Two mutants and one `--numbers` run exercised off-tree.

---

## 6. WHAT WOULD CLEAR THE GRADE

M-1 (head segment — needs re-delivery), M-2, M-3 (with the verified repair),
M-4, and the five minors. None of them touches a computed number; all five
majors are attribution, coverage or fiber-pricing repairs. **The verdict word
`COUPLING-CONSISTENT-NOT-REQUIRED`, the three gate readings, the
threshold-exactly-5 exit and the staleness-blindness theorem all stand as
measured**, and M-1's repair strengthens the unit rather than weakening it:
what looked like a forced coin is instead a measured invariance of the verdict
shape across a six-member family.

*K1 OPERATOR, panel of three. Between delivery and adjudication every headline
reading is a candidate reading.*
