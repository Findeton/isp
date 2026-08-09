# RSQ — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, INSTRUMENT lens.  **Protocol:** `v13/note-rsq-hostile-protocol.md`
(FROZEN, K1–K5 binding).  **Object:** the frozen RSQ delivery.  **Method:**
independent recomputation from the paper's prose; scratch-only; no repo file
modified; no git.  **Interpreter:** `/opt/homebrew/bin/python3.13` (3.13.2).

**Recomputation count: 212** — 15 hash verifications; 86 distinct quantities
recomputed from scratch in four independent scripts that import none of the
unit's code; 111 instrument executions (1 full delivery reproduction, 27
anchor-corruption runs, 57 declared-mutant re-runs, 19 reviewer-built mutants
and probes, 7 carrier builds).

## 0. Integrity and reproduction — all clean

| check | result |
|---|---|
| sha256-12 of paper / code / output / receipt | `f208ff12974b` / `18eb651d1ab1` / `810f923392d8` / `4db809f7b618` — **all four verify** |
| the 11 pinned external artifacts | **all 11 verify** against the code's `PINS` table |
| full delivery re-run in an isolated tree | `_output.txt` **byte-identical**; `_receipt.json` identical modulo `source_sha256`/`python` |
| `source_sha256` in the receipt vs the file | **matches** (`18eb651d1ab1053d…`) |
| determinism | confirmed — my run is a second independent full execution |

The repo was never written to; the reproduction ran against copies in scratch.

## 1. Findings

### MAJOR

**F1 — "Three sources that share no deciding variable" is false: sources 1 and
2 are the same function.**  G35's claim, and paper §12's table, present three
independent sources.  Source 1 is `src1 = live_full`
(`rsq_reposed_square_exact.py:3418`), and

```
2731:  "injective_possible": order_criterion(E, p, pord(SIGMA[pi]))
2735:  live_full = sum(1 for r in census_rows if r["injective_possible"])
```

so source 1 is `order_criterion` evaluated on the 9 declared census cells — a
strict sub-index-set of source 2's 20,160 rows (same 7 primes, same wing orders
{2,3}), computed by the identical function.  **Demonstrated:** a one-line edit to
`order_criterion`'s return moves src1 0→315 **and** src2 0→20160 simultaneously,
while the census's own two-route enumeration is untouched at 25 of 315
(`PROBE src1=315 src2=20160 src3=0 live_s1ab=25`).  Source 3 is unaffected (0) —
it is genuinely independent.  So there are **two** independent sources, not three.

This also makes paper §7.4's row "rows admitting an injective candidate
(S1a+S1b+S3) — 0 of 315" a misdescription: it is not a census output.  The census
routes *cannot* decide injectivity — every candidate they enumerate has image
inside a single cyclic subgroup of order p, so |image| ≤ p < p⁶ and injectivity
fails on cardinality for every row by construction.

Directly the rule in RUNBOOK §13 addendum (v13 #234): "a pair related by an
algebraic identity is one route."  Here the relation is not even algebraic — it
is literal identity of the deciding function.

*Repair:* relabel source 1 as "the order criterion restricted to the declared
census cells" (a coverage check on the census, not a source); report
`live_s1ab` = 25/315 as what routes A/B actually measure; state the verdict as
resting on two independent sources.

**F2 — No cell-completeness gate protects any of the three verdict-carrying
tables.**  RUNBOOK §13 addendum (#234): "a cell-completeness gate must catch a
dropped cell."  Four reviewer probes, each dropping rows from a table the
verdict rests on, **survive with exit 0 and zero gate failures**:

| probe | effect | result |
|---|---|---|
| drop 1 row from the 20,160-row criterion sweep | src2 denominator → 20,159 | **exit 0**, G36 PASS `20159/20159 covered arena-free`, qualifier still `UNIVERSAL-FOR-THIS-FAMILY` |
| drop a whole prime from the criterion sweep (2,880 rows) | denominator → 17,280 | **exit 0**, G36 PASS `17280/17280`, still `UNIVERSAL` |
| drop 1 row from the 315-row census | src1 table short | **exit 0**, nothing fails |
| drop 1 row from the 210-row module table | src3 table short | **exit 0**, nothing fails |

Only two tables are protected: the 1,440-cell family (G14, via
`ncells == ncells_forced` — my own `cell-drop` variant, dropping the *first*
slot order rather than the last, correctly dies at G13/G14/G15/G30) and the
precheck tally (G17's `completeness` clause — my dropped-precheck-cell probe
dies there).  The `completeness()` helper is never applied to a forced product
for the three tables above.

*Repair:* gate `crit_total_cells == ncells * len(sweep_primes()) * 2`,
`len(census_rows) == len(census_cells) * len(sweep_primes()) * 5`, and
`len(mod_rows) == 6 * len(sweep_primes()) * 5`, each against the computed
product.

**F3 — `UNIVERSAL-FOR-THIS-FAMILY` is an alias for "zero criterion hits", not a
coverage measurement.**  `covered = crit_total_cells - crit_total_hits`
(3422), then G36 asserts `covered == crit_total_cells` — identically true iff
`crit_total_hits == 0`.  The denominator is whatever the sweep happened to
count and is never compared to a forced total.  The **declared** mutant
`prime-single` collapses that denominator sevenfold and the qualifier still
reads `UNIVERSAL`; it is caught only by the unrelated G08 (holonomy-order
list).  Paper §12's "The qualifier is earned from measured coverage: **20 160
of 20 160** … rows are covered" is therefore stronger than what is measured.

*In mitigation, the numerator side is genuinely falsifiable*: `criterion-lax`
drives it to `PARTIAL-11320-OF-20160` and G36 fails; my G19 probe drove it to
`PARTIAL-20148-OF-20160` and G36 failed.  The defect is confined to the
denominator.

*Repair:* count `covered` directly as rows measured not to satisfy the
criterion, and gate the denominator against the forced product (with F2).

**F4 — G20's route-independence clause is a self-report, defeated by a silent
alias.**  `ROUTE_CALLS["taint"]` is incremented only inside the declared
`route-alias` mutant's own branch (1408–1411).  A silent alias — route B
returning route A's answer *without* bumping the counter — **survives: exit 0,
G20 PASS `0 disagreements; taint 0`**.  The only measured content of G20 is
that the two routes agree, which an alias satisfies trivially.

*In mitigation:* I checked route A against my own from-scratch full-covector
enumeration (no projective quotient, no shared code): **0 disagreements at every
row with p-torsion**, and the calibration cell returns **745 = 745**.  The
numbers are sound; the instrument's evidence for independence is not.

*Repair:* make the detection structural (evaluate route B with
`route_a_count` unbound in its namespace) or drop the counter and rest the
claim on X02's prose, which is accurate.

### MODERATE

**F5 — G19 measures a cardinality inequality, not the containment it claims.**
The predicate reduces to `crit_cells_set < pre_surv_cells` — two integers.
**Probe:** force the criterion to fire *only* on cells the precheck kills (12
hits, every one stillborn) → **`G19 PASS   criterion 12 <= precheck 4420`**
while the claimed containment is exactly inverted.  The two counts also have
different index sets: 12 is out of 20,160 (cell, prime, order) rows; 4,420 is
out of 10,080 (cell, prime) pairs.  Paper §7.3 calls the first "cells".  The
mathematical subsumption is a correct theorem — the *gate* does not measure it.

*Repair:* measure containment as a set predicate (every criterion-satisfying
(cell, prime) has `dim ker(E−I) = 0`) and report each count against its own
denominator.

**F6 — the precheck's negative control is the object under audit.**  G16 and
paper §6.1 describe "a synthetic MISMATCHED pair".  In the code
`synth_bad_Efr = encoding_matrix(tuple(range(NV)), "q->counts")` (2502) — that
is C1, the pin's own minimum candidate, not a synthetic.  The two-way
*reachability* of `precheck` is real (both arms run through the same function;
my independently reconstructed `precheck-lax` dies at G16/G17/G37 and
`precheck-blind` at G16/G17/G19/G35, matching the declared kills exactly), but
the negative arm is not independent of the measurement.  *Repair:* relabel, or
supply a genuinely synthetic mismatched matrix.

### MINOR

**F7** — Route C's "four declared instances" is four *rows* from **two**
instances (one at p=5, one at p=7), each with an admitted and a rejected
covector.  Paper §7.4's "Two instances at p = 5 … and two at p = 7" doubles the
count; the table beneath it is correct.

**F8** — Five declared mutants (`complete-lax`, `qualifier-typo`, `s2-lax`,
`stillborn-lax`, `universal-lax`) are killed **only** by the G37 synthetic
probe: the helpers they blind return the same answer in the honest run whether
blinded or not.  This is the correct use of a probe as negative control, not a
defect — but those five clauses carry no gate weight in the delivered run and
that is not disclosed.  (`completeness` *is* load-bearing at G17.)

**F9** — 13 of 57 mutants never reach the totals block, and two (`arena3-lax`,
`prime-single`) exit 1 partly via **uncaught exceptions** (`TypeError:
'NoneType' object is not subscriptable`; `KeyError: 7`).  Both still raise a
genuine gate FAIL first (G04/G05; G08), so the kills are legitimate — but the
receipt does not disclose that some mutants terminate on an exception rather
than at a gate.

**F10** — the build cap is honest but conservative, **and the excluded primes
confirm the claim**.  I built the reduced carrier at all four excluded primes:
p=13 (2.2 s), 17 (8.6 s), 19 (15.6 s), 23 (42.4 s), k=2 at every one, with
|⟨R_HH⟩| = p and translation-by-ρ **True at 7 of 7**.  X04 and deviation 4 are
accurate ("a declared computational cap, not a measured boundary"); the real
cost is the 58-run harness, not the unit.  The paper's printed carrier sizes
for the unbuilt primes (which assume k=2) are correct.  *Recommend* extending
the table — the result is favourable — or naming the harness cost in X04.

**F11** — source 3's universality is analytic, measured at 6 of 1,440
identifications (`mod_rows` covers only module+lex cells).  §8's box claims "at
any prime, any identification, any direction, any dimension".  I checked the
mechanism family-wide: **E kills the all-ones vector at 0 of 10,080 (cell,
prime) pairs**, so the claim holds — but the instrument does not measure it
there.  Scope the table's reach or extend it.

**F12** — G15 gates the computed census-cell count only as `>= 8` while the
paper reports "9 (computed)".  The rule itself has teeth: my probe substituting
nine stillborn duplicates dies at G15.

## 2. What survived every attack

Every load-bearing number I recomputed matched **exactly**.  No false numerical
result was found.

- **K1 (0 / 20,160).**  Reproduced exhaustively by my own route — not sampled —
  by both the matrix-power and the polynomial form, **0 hits, 0 disagreements**,
  per prime all zero.  I checked the derivation line by line (image abelian and
  Σ-stable; δ|_A = I − ρ; ρ = α(I−E)α⁻¹; ρ^ord = I ⟹ (I−E)^ord = I; the
  polynomial forms E = 2I and E² − 3E + 3I = 0 with roots 1−ω) — **it is
  correct**, and the ord-1 case is soundly handled separately (δ_e ≡ e forces a
  constant map).  Precheck survivors {5:580, 7:580, 11–23:652}, stillborn
  {860, 860, 788×5}, module/lex mismatches 343:1, 7:1, 49:1 at p=7 and 125:1,
  5:1, 25:1 at p=5 — all reproduced.
- **K2 (held-out).**  FIT = e₁ is excluded from HELD; HELD = p⁶ − 1 = 117,648;
  H1 = H2 = H3 = 117,648; fixed-label values {1,8,15,22,29,36,43}; BREAK-HOM 0
  square violations of 117,649 and **1,536** homomorphism violations — all
  exact.  The H1/H2 sets provably never enter the fit **because nothing is
  fitted**: the candidate is built from the declared constants c = (2,2,2,4,4,4).
  Worth noting in the paper — "predictive" is weaker than it sounds.
- **K5(a).**  **26 of 26 anchors corrupt-and-fire**: exit 1, self-named on
  stderr, baseline exit 0 with no gate failure.  All **15 external** committed
  values trace to their pinned artifacts — LCB G36 d=3 rows (`dim_fix` 3 and 1,
  `column_sums` ["3","3","3","2","2","2"]), LCB G35 (1 fixed point of 40,320),
  HA G28 (`readout_determinant` "2"), TB3 `defect_subgroup_order` {1,12,168,
  360,2520}, TB3-A1-ORDCENSUS, `element_orders` [1,2,2,2,3,3], `form_hits`
  F1=36 over 9 members (⇒ 4), LCB §12.3 "16 at p = 5, 22 at p = 7".
- **K5(b).**  57 declared mutants; **0 exit ≠ 1, 0 without a named kill**; all
  **38 of 38** must-pass gates falsified by at least one mutant, so
  `never_falsified = []` is honest at an honest denominator.  Five mutants
  reconstructed from prose (both precheck mutants, a differently-placed cell
  drop, a verdict flip on the *other* input to `derive_verdict`, and an asserted
  qualifier) — all die, and at the same gates as declared.
- **K5(g).**  The "exactly 1 analytically-forced exemption" verified: the single
  exempt HELD cell is precisely the zero record (0,0,0,0,0,0), where α returns
  the identity.  The predicate is `alpha_perm == ident` — blind, algebraic,
  referencing no mutant identity — and the count is **gated** to exactly one.
  Fully compliant with RUNBOOK §14 addendum (#208); `teeth-off` dies at G25.
- **K5(i) / K4.**  Exact Sylvester verified: G3-FLAT (1,1,1), G3-ANISO (1,4,36),
  G3-OFF (2,3,6) admissible; G3-SINGULAR (1,**0**,0) and G3-INDEF (1,**−3**,−3)
  rejected — genuine singular and indefinite controls.  det 8 in both
  conventions, spectrum {1,1,1,2,2,2} (the matrix is lower-triangular, so the
  diagonal *is* the spectrum), 81/81 re-encoding, det = 2^{d(d−1)/2} at
  d = 2,3,4,5, ρ(x*) = (1/6, 1/6, 0).  The X01 pin-reading is internally
  consistent: the record datum space is F_p³ at d=2 and F_p⁶ at d=3, so the
  pin's "V: F_p³ → F_p⁶" reads naturally as the d=2 → d=3 move, and det 8 with
  spectrum {1,1,1,2,2,2} are the d=3 readout's, which I recomputed.
- **Transport side.**  |G_C| = 5040, wing orders [1,2,2,2,3,3] non-abelian,
  fixed labels {0,7}, 4 involutions, fix(δ) = 1 at 6 of 6 (the fixed point is
  the identity), 9-label arena 1 of 40,320, ladder {1,12,168,360,2520}, F1=F3 at
  20 of 30 and at all 20 involution cells, cocycle 0 of 150.
- **Census and controls.**  9 declared census cells reproduced by my own
  implementation of the stated rule; 315 rows, 25 live; route C 0 violations of
  117,649 with the rejected control at **100,842**, and 0 of 15,625 with the
  rejected control at **12,500**; grown arena m=6/43 labels, square 117,649 of
  117,649, injective, (I−Ẽ)³ = I; thresholds 26/31, 43/43, …, 139/139 and the
  d=2 analogue 16/22; the spectral meeting at p=7 alone.
- **Cache discipline** (§14 addenda #185/#219) correctly implemented: 2,000
  fresh bypasses, 0 self-test hits, cache exercised first (9,501 hits of 39,741
  lookups); both `cache-lax` and `cache-unused` die at G32.
- **G03's AST guard** genuinely enforces #208 — no gate-registering function
  references mutant identity — and is itself validated by a sample it must flag.
- **G01** honestly discloses in its own claim text that it records ordering
  *within one execution* only.

## 3. Assessment

The scientific result is not damaged by anything I found.
`RSQ-SQUARE-FOUND-BRIDGE-EMPTY` rests on source 2 (0 of 20,160, which I
reproduced exhaustively by an independent route, from a derivation I checked and
found correct) and source 3 (0 of 210, whose mechanism I confirmed holds at
0 of 10,080 family-wide).  Both survive.  The precheck genuinely has survivors,
so the premise of the FOUND branch is genuinely reached; FOUND and EMPTY are
both genuinely reachable; the held-out control is exact and its single exemption
is honest.

What is damaged is the **instrument's account of itself**.  Four claims the
gates make are not the claims the gates measure — the three-source independence
(F1), the coverage qualifier's denominator (F3), the route-independence taint
counter (F4), and the subsumption containment (F5) — and the verdict-carrying
tables have no dropped-cell protection at all (F2).  Three of these I
demonstrated with probes that **survive at exit 0**, which is the standard this
programme applies to itself.  F1, F2 and F3 are violations of engraved RUNBOOK
§13 addendum (#234) specifically.

Every one of these is repairable by changing gate predicates and paper wording.
**Not one requires a computed number to move** — I recomputed all of them and
they are right.  That is the difference between this and a REJECT.

---

# GRADE: ACCEPT-WITH-FIXES

Required fixes, in order: **F1** (relabel the verdict's sources; there are two,
not three), **F2** (cell-completeness gates on the criterion, census and module
tables against forced products), **F3** (compute `covered` independently and
gate its denominator), **F4** (make route independence structural or rest it on
X02's prose), **F5** (measure the subsumption as a set containment, and report
the two counts against their own denominators).  Recommended: **F6** (relabel
the precheck's negative control), **F7**, **F9**, **F11** (scope the module
table's reach), **F12**.  **F10** is a favourable finding — the excluded primes
confirm G29 at 7 of 7 and the table can simply be extended.
