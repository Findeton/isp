# LCB — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, instrument lens. **Protocol:** `v13/note-lcb-hostile-protocol.md`
(FROZEN, v13 #283), primary weight K5, secondary K1 and K3 at lower depth.
**Object reviewed, SHA-256 verified on disk before reading:**

| file | sha256-12 | verified |
|---|---|---|
| `v13/paper-lcb-livecell.md` | `9b081a1e72af` | ✔ |
| `v13/code/lcb_livecell_exact.py` | `57d3072b1031` | ✔ |
| `v13/code/lcb_livecell_output.txt` | `50dad82e0637` | ✔ |
| `v13/code/lcb_livecell_receipt.json` | `2ffe123e16cf` | ✔ |

All seven of the unit's own hash pins also verify byte-exact against disk
(`note-lcb-livecell-pin.md`, `paper-brg-bridge.md`, and the BRG/HA/GEN/XBA/PSI
receipts). Repository read-only throughout; all work in the session scratchpad;
no repository file was modified (re-verified after every probe). No git.

**Recomputation count: 134 independent checks** — 97 numerical recomputations in
a from-scratch rebuild (`indep.py`, importing nothing from the unit, own
permutation conventions), 18 source-patch instrument probes against a scratch
copy, 7 corrupt-and-fire pin tests, 11 SHA verifications, and 1 full independent
rerun of the unit plus its 55-mutant harness (56 process runs). **Numerical
disagreements: 0.**

**Grade: at the end.**

---

## 0. What held up

I record this first because it is the larger part of the finding, and because
the defects below are all about how results are *gated*, not about what they
*are*.

- **Every load-bearing number reproduces.** 97 recomputations, zero
  disagreements. Including: the 40,320-member family and both spectra; the
  4,608-member ord-5 class; `Q0 = [0,1,2,3,4,5,7,8,6]` moving exactly 3 labels
  and the class minimum of 3; `D`, ord 5, fix₈₁ 36; `|⟨W,D⟩| = 10` with orders
  `[1,2,2,2,2,2,5,5,5,5]` and the dihedral relations; C_HA(5)'s 625/(1,1)/5/125;
  the determinant-2 readout; all four encoding cells' matrices mod 5, their
  determinants and their exact rational spectra; 1,344 order-5 elements, 48
  Σ-anti-invariant, **0** Σ-invariant; the census 0/48/0/48 by both routes and
  the kernel dimensions 0/1/0/1; 100-of-125 S1c violations; S1d (5, 36);
  |image| 5, kernel 25, strata {36,81}; p-part exponents 1 (nine labels) and 3
  (sixteen); the 224-cell grid and 32/4/0; the anti-invariant counts
  {5:48, 7:96, 0 above}; BRG's three live cells and their 4/4/6; 6,336 / 6,144 /
  192 / 48 distinct maps / 124-of-124 / 124-of-124 / 99 / 99; SYNTH-EMPTY 0;
  BREAK-HOM 0 and 6,000 of 15,625 with its accepted counterpart 0 and 0; the
  relabelled-arena 40,320 and 48; and the Open-1 sets.
- **Two of those I also derived in closed form**, independently of any
  enumeration: the 100-of-125 S1c violation count (λ = (1,1,1) forces
  α(τr) = α(r) while Σα(r)Σ = α(r)⁻¹, so the clause holds exactly on the 25
  cells with r₁+r₂+r₃ ≡ 0), and BREAK-HOM's 6,000 (2,000 from each of the three
  violating composition regimes). Both match to the unit.
- **41,665 verified by three separate constructions**, as K5(b) requires:
  the subgroup-counting formula 1 + (1344/4)·124; an explicit enumeration of the
  336 distinct order-5 subgroups; and a direct count of pairwise-commuting
  triples of elements of order dividing 5 by a different algorithm. All give
  41,665. The unit's own "independent count" (G11) is legitimate.
- **Route independence is real, and survives stresses the unit did not declare.**
  Corrupting the *shared* input `ANTI` by one element makes the routes diverge
  (47 vs 48) and G10 fires; swapping route B's square orientation makes them
  diverge in opposite directions (route A 0/48 vs route B 48/0) and G10, G30,
  G31 all fire. X09's honest framing ("two computations over shared data") is
  if anything an understatement.
- **Dropped-cell probes fire at positions other than the declared mutants'.**
  Dropping the *first* encoding cell (the declared mutant drops the last) →
  G09, G11, G30. Dropping a *middle* grid cell → G16, G30. Dropping a *middle*
  basis image → G11, G30. Deleting one P-candidate from the Open-1 table (not a
  declared mutant at all) → G29. Cell-completeness has teeth in all four places
  K5(h) names.
- **All 7 hash pins corrupt-and-fire.** I appended one byte to each pinned file
  in a scratch repo tree and ran: every one exits 1 with its own named
  `ANCHOR FAILURE A00-…`, and the originals restore byte-exact. Exit 0 is
  reached only with nothing broken.
- **The 124 HELD cells genuinely never enter the fit.** `fit_admitted` iterates
  `for r in FIT` alone (FIT = [(1,0,0)], size computed); HELD is the complement,
  size computed; the HELD square is a strictly later loop. K5(c) is satisfied at
  the mechanical level — see F3 for what is *not* satisfied.
- **The BRIDGE verdict is genuinely two-source gated.** Single-point corruption
  of the clause-table source (`s1_pass`) is caught by the S4-grid recount;
  single-point corruption of the S4-grid recount (`live_full`) is caught by the
  clause table. Both probes exit 1 at G30.
- **The no-sampling / no-randomness / no-floats claims verify.** No `random`,
  `secrets`, `time` or `datetime` import; no seeded stream; the only `sample`
  identifiers are the *declared* 5-member completion subset and the two
  synthetic scanner samples. My own AST scan for float/complex literals and
  `float()`/`complex()`/`round()` calls is clean; the only three true-division
  sites (lines 616, 630 ×2) operate on `Fraction`s. My own run-mode scan,
  *widened* beyond the unit's (`gate` **or** `anchor` **or** `report`), also
  returns zero offenders.
- **55 mutants, all exit 1, `never_falsified` empty at an honest denominator.**
  The paper's §14 breakdown (12/3/6/7/8/3/5/5/2/4) matches the source dict
  exactly; all 34 must-pass gates appear in some mutant's named kills.
- **Determinism and freeze.** My rerun is byte-identical to the delivered
  `lcb_livecell_output.txt`; cache arithmetic is internally consistent
  (690,493 = 650,173 + 40,320); the delivered artifacts were untouched by every
  run I performed.
- **Anchors trace to their cited sources.** A08/A10 verify against BRG §14
  open 1's own sentence ("**4,608** … the smallest of them moves just **3**
  labels"); A22/A23 against BRG receipt G34's live-cell table
  `[[5,ord=15,4],[5,ord=5,4],[7,ord=7,6]]`; A05/A06/A11 against GEN; A13/A18
  against HA; A04 against XBA; A12 against PSI.
- **K1 (lower depth): the spectral obstruction reproduces.** I re-derived the
  squaring-forcing myself — the p-part of 8! is 5¹ so every image is cyclic of
  order 1 or 5; the square forces ΣgΣ = g^c with c² ≡ 1; the c = +1 branch is
  measured empty (0 Σ-invariant order-5 elements, against 48 anti-invariant);
  hence δ(α(r)) = α(r)² and the square reads λ∘E = 2λ. spec(E) = {1, 1, ½} in
  the registered direction, {1, ½, −1} in the index one. Sweeping every prime
  below 60: 2 enters the spectrum at **p = 3 only**, and E is undefined at
  p = 2. All confirmed. I further verified the squaring identity at **all 240**
  cells, not merely the declared 40.
- **K3 (lower depth): six P-candidates spot-verified**, not the three required —
  P3, P4, P5, P8, P10, P12. No candidate is misclassified in the direction that
  would matter: P1 and P3 do carry declarations (P1 is a function of the
  declared p; P3 contains this unit's own ord(D) = 5 selection rule), and the
  {5,7} narrowing and the p = 3 singleton both reproduce. See F8 for the one
  looseness.

---

## 1. Findings

### F1 — MAJOR. The `obstruction` qualifier is not gated. A fabricated obstruction string reaches the receipt at exit 0.

**Evidence.** G30 builds `quals["obstruction"]` from
`qualifier_value("obstruction", obstruction)` where
`obstruction = obstruction_name(spectral, parity)` (line 2523), and builds its
"recomputation" as `qcheck["obstruction"] = obstruction_name(spectral, parity)`
(line 2571) — *the same function, called with the same two arguments*. It
cannot disagree. I replaced the helper's return string with a fabrication and
ran the unit:

```
=== PROBE wrong-but-plausible-obstruction -> exit=0  gate-fails: NONE
   G30 PASS  ... ; 15 qualifiers recomputed, 0 disagreements
   G31 PASS  obstruction measured coextensive with the clause failures
   obstruction   S9 -- FABRICATED: the carriers have incompatible torsion ...
```

All 34 gates green, exit 0, and the fabrication is printed as the unit's named
obstruction. The only defences are two hard-coded substring tests inside G30
(`obstruction != "UNDETERMINED"` and `"cardinality" not in obstruction`), and
the declared `obstruction-misname` mutant exercises only the second. G31 does
not reference the string at all — it gates `spectral`, `parity` and the
direction pattern, never the words that reach the reader.

This is exactly the disease RUNBOOK §14 addendum (v13 #219) names — "a gate
clause that compares an object against a copy of itself routed through the very
component under test verifies nothing" — landing on the single qualifier that
carries the unit's headline physics claim.

**Repair.** (i) In G30, assemble the expected obstruction tokens from the
measured booleans without calling `obstruction_name`, and gate that the returned
string contains "SPECTRAL", "CHART-PARITY" and both direction names, matched
against the per-direction clause counts already in `s1_rows`. (ii) Add a
declared mutant returning a plausible, non-cardinality, *wrong* obstruction.
(iii) Amend §13. Replacement sentence, verbatim:

> Every **numeric** qualifier below is recomputed inside that gate from its own
> source (14 of them, 0 disagreements), so a typed number cannot reach the
> receipt. The fifteenth, the obstruction string, is not recomputed but
> **token-gated**: G31 measures its SPECTRAL and CHART-PARITY tags coextensive
> with the per-direction clause failures, and G30 rejects a cardinality claim.

### F2 — MAJOR. The Open-1 verdict's two sources collapse to one variable; a one-line corruption flips `LCB-PRIME-DECLARED` to `LCB-PRIME-DERIVED` at exit 0 with all 34 gates green.

**Evidence.** The verdict is derived as
`prime_verdict = derive_prime_verdict(unique_forced)` and recomputed as
`prime_recomputed = ("LCB-PRIME-DERIVED" if len(inter) == 1 else …)` — presented
as two sources. But `unique_forced` (line 2458) ranges over `open1`, and by then
`open1` contains **P12, whose `primes_it_admits` is `sorted(inter)`** (line
2453). Both "sources" are therefore functions of the single variable `inter`.
Setting `inter = {5}` at its assignment:

```
=== PROBE open1-inter -> singleton {5} -> exit=0  gate-fails: NONE
   G30 PASS  ... / LCB-PRIME-DERIVED; 15 qualifiers recomputed, 0 disagreements
   OPEN-1 VERDICT: LCB-PRIME-DERIVED
   open1_declaration_free_intersection   [5]
```

A verdict flip, at exit 0, with every gate passing. Corruptions of other
cardinalities print silently too, because
`qcheck["open1_declaration_free_intersection"]` is `sorted(inter)` — *the same
variable* as the qualifier it audits: `inter = {11}` prints `[]` and
`inter = {5,7,11}` prints `[5,7]`, both at exit 0, no gate failure.

The delivered value is **correct** — I recomputed the intersection independently
and got {5,7}, and the delivered Open-1 verdict is right. The finding is that
the instrument the paper credits with protecting it does not. RUNBOOK §13
addendum (v13 #234): "the printed verdict string must be derived inside a gate
from the measured counts, and a verdict-flip mutant must prove that derivation
can fail." The declared `verdict-flip` mutant proves only that the *hand-typed
string* path fails; it never touches the derivation's inputs.

**Repair.** (i) Compute `unique_forced` over `open1` **excluding P12** — P12 is
the intersection, not an independent candidate, and including it makes the
uniqueness test read its own output. (ii) Recompute the intersection inside G30
from the per-candidate `admissible_part` fields rather than reading `inter`.
(iii) Add a declared mutant perturbing `inter` to a singleton. (iv) Amend §15
deviation 6 to say the Open-1 verdict, unlike the bridge verdict, currently has
one source.

### F3 — MAJOR. S5's held-out verification is run against the SYNTHETIC chart map, and this is disclosed nowhere.

**Evidence.** `Esy = synth_compatible_matrix(P)` at line 1951; every S5
computation — `fit_admitted` (1967–68), the HELD square (1975–76), H2/H3 and
both teeth (2016–2030) — applies `Esy`. HA's readout `E` never enters §8. The
transport side is the pairing's real one; **the deformation side is not.**

Nothing says so. Not §8. Not §2.6's held-out table. Not the frozen
`DECL["strengthened_standard"]["S5"]` or `DECL["held_out"]`. Not G18's receipt
detail (keys: FIT, HELD_cells, fit_admitted, rejected_out_of_sample,
survived_held_out, total_held_out_violations) nor G19's. I searched the whole
receipt: only G22, G23, G32 and G33 mention anything synthetic. A reader of §8
has no way to learn that 6,336 / 6,144 / 192 / 124-of-124 / 99 / 99 — the
unit's most quantitatively impressive block — are measured against a chart map
invented as a control.

BRG's own registry reads "**S5 HELD-OUT AT A LIVE CELL** WITH A TRANSPORTED
QUANTITY", and BRG itself carried a dedicated non-must-pass disclosure gate
(its G41) recording precisely this asymmetry for its own FOUND
("FOUND_is_demonstrated_at": "one declared synthetic pair (p = 3) …"). The
precedent exists in the immediate parent; LCB does not follow it here.

That the in-arena census is empty makes this *unavoidable*, not *undisclosable*.

**Repair.** Add disclosure X11 and open §8 with, verbatim:

> Because the in-arena census is empty at S1, there is no in-arena candidate to
> hold anything out from. The held-out protocol is therefore exercised on the
> declared SYNTHETIC compatible pair of §2.7: the pairing's own transport side —
> the real completion group with the real defect map — against the synthetic
> chart map whose 2-eigencovector is chart-antisymmetric. The transport side is
> the pairing's; the deformation side is not. Every number in this section is at
> that scope, and BRG's S5 "at a live cell" is met on the transport half only.

Mirror the sentence in §2.6 and in G18's gate claim, and record the synthetic
matrix in G18's receipt detail as G22 already does.

### F4 — MAJOR. F0-IDENT, the declared positive control, is a tautology: all four of its clauses are `x == x` at the delivery configuration.

**Evidence.** With `idc = identity`, G21 evaluates
`compare_square(δ(e·q), e·δ(q))` — i.e. `compare_square(δ(q), δ(q))`; S1c is
`e·σ(q) == σ(e·q)`; S1d is `ord(δ(e·Q0)) == ord(D)`; injectivity is
`|{e·q}| == |COMPL|`. Each is an identity for *any* δ and *any* comparison
predicate. Pairing an object with itself and mapping it by the identity always
commutes.

Empirically, I gutted `compare_square` to `return True` — destroying the census
predicate outright and failing nine gates (G10, G13, G14, G18, G19, G23, G27,
G30, G31) — and G21 still reported `identity self-morphism: 0 square violations
at 40320 cells; injective True`. The delivered mutant table corroborates:
`matrix-lax`, `square-lax`, `hom-lax` and `s1c-lax` each kill other gates and
**none of them names G21**. The advertised "40,320 cells" is 40,320 evaluations
of an identity.

RUNBOOK §4 requires a positive control that "fires when it should"; RUNBOOK §14
addendum (#208) rules that "analytically-forced clauses (true by algebra for
every input) are disclosures, not must-pass gates". F0-IDENT is the latter
presented as the former, in §2.7, in §10's control table, and in §1's
requirements table ("positive control (identity self-morphism) … gates G21,
G24").

**The substance is nonetheless discharged** — by G22. SYNTH-COMPATIBLE is a
genuine, non-trivial FOUND control: I reproduced its 192 pairs, 48 distinct
maps, S1c and S1d passage, and independently re-verified the exhibited witness
`g = [0,1,4,3,6,2,7,5,8]`, `λ = (1,4,0)`. So this is a labelling defect, not a
missing control.

**Repair.** Either (a) demote F0-IDENT to a disclosure, naming G22 as the
positive control in §1, §2.7 and §10; or (b) re-pose it so the identity is run
through route B's own `keep` predicate with E = the identity matrix, which is a
real pass of the census machinery. Replacement row for §10:

> | **F0-IDENT** (analytically forced; disclosure, not a control) | the identity
> self-morphism commutes with any encoding by construction; its 0 violations at
> 40,320 cells record that `identity_candidate` returns the identity, and
> nothing about the square. **The positive control is SYNTH-COMPATIBLE (G22).** |

### F5 — MINOR. The "three sources" of the emptiness decision are two.

`empty` is `census_is_empty(sum(r["s1_pass"] for r in s1_rows))`;
`empty_from_tables` sums over `tables["s1_clause_census"]`, which is bound to
**the same list object** at line 1737. Trivially equivalent (a sum of
non-negative integers is 0 iff no entry is positive). The genuinely independent
source is the S4 grid's `live_full`, and my two flip probes confirm the
two-source protection is real. But §13 ("derived a **third** time") and §15
deviation 6 ("has three sources") claim three.

**Repair.** §15 deviation 6: "The emptiness decision has **two** sources: the
clause table, and the S4 grid's Gaussian-elimination decision, which never
touches the enumeration. A third reading re-sums the same clause table and is
reported as a consistency check, not as a source."

### F6 — MINOR. S1d's "48 pass" is base-record-dependent, and the state coordinate is never swept.

S1d passes iff λ·r₀ ≢ 0 (mod 5) with λ = (1,1,1). Sweeping HA's nine admissible
records myself:

| record | counts | λ·r₀ | S1d |
|---|---|---|---|
| G-FLAT, G-DIAG2, G-ANISO2, G-CURVED, G-OFFNEG | — | 4, 3, 1, 4, 2 | **48/48** |
| G-ANISO, G-OFFDIAG, G-OFFDIAG2, G-CURVOFF | — | 0, 0, 0, 0 | **0/48** |

Five of nine pass; four give zero. The declared r₀ = G-FLAT is one of the
passing ones. §2.1's arena-action list sweeps identification, direction,
relabelling, basis, prime and completion — but not the **state**, which RUNBOOK
§15 requires declared *and* which §14 requires self-tested where an instrument
enforces it. The `s1d-lax` mutant substitutes G-ANISO but is caught by G13's
`r0 == tuple(RECORDS["G-FLAT"])` name-check, not by any downstream measurement.

Scope note in the unit's favour: the S4-grid narrowing 3 → 2 is **not**
affected, because the grid's S1d criterion is the structural `n == p`, not the
base record. The finding is confined to §5's S1d column and to the sentence
"The base-point clause is satisfiable; the chart clause is not" (which is true
as an existential, but sits beside a table whose 48 is state-relative).

**Repair.** Add a base-record sweep over HA's nine admissible records, or state
at the claim: "S1d passes at all 48 for the declared base record G-FLAT, and at
five of HA's nine admissible records; the state coordinate is a declaration and
is not swept."

### F7 — MINOR. The 224-cell grid is 28 independent measurements replicated eight times.

`spec2_by_p` and `spec2c_by_p` are computed once per (encoding cell, prime) at
lines 1847–1855 and reused across all eight defect orders; S1a/S1b liveness is
constant along the ord-D axis, which enters only through `n == p`. "224 cells,
each visited exactly once" is honest bookkeeping and the dropped-cell probe
works, but it overstates the census's independent content, and 224 appears as a
scope qualifier in §13's verdict table.

**Repair.** §7: "…= **224** cells, each visited exactly once. The
kernel computation is per (encoding cell, prime) — 28 distinct linear-algebra
decisions — and the defect-order axis enters the S1 clause list only through the
base-point condition ord(D) = p."

### F8 — MINOR. The "declaration-free" column means free of the declared *prime*, not free of declaration.

P4, P5, P10 and P11 all read the **nine-label** completion arena, which is a
declared choice (inherited from GEN/BRG, but declared). Only P6–P9 are
arena-independent. The helper's own docstring says "no declared prime and no
declared choice of this unit among its inputs" — the nine-label arena is not
this unit's choice, so the code is self-consistent, but the paper's column
header is not. This makes the {5,7} narrowing *weaker*, never stronger, so it
cannot threaten `LCB-PRIME-DECLARED`; §12's prose is already correctly scoped
("nothing in the committed structure of **this pairing**").

**Repair.** Rename the column "declaration-free (of the prime)" and add: "every
candidate but P6–P9 reads the declared nine-label arena; freedom here is freedom
from the declared prime, not from declaration."

### F9 — MINOR. The frozen declaration's H2 disagrees with the paper's H2 and with the code.

`DECL["held_out"]["H2"]` (frozen, and reproduced verbatim in the receipt) reads
"ord(delta(alpha(r))) at every HELD cell". The paper §2.6 and the code (line
2020, `transported_quantity(pd, img) == gpow(gw, 2*k)`) both use the **defect
permutation itself, entry by entry** — strictly stronger. The direction is safe,
but RUNBOOK §13's "freeze estimators before fixture truth" protects the frozen
declaration, and the delivered instrument is not the declared one.

**Repair.** Correct `DECL["held_out"]["H2"]` to match, or disclose the
strengthening explicitly.

### F10 — NOTE. Two prose numbers are not receipt-backed.

A full sweep of every integer in the paper against the receipt and output leaves
exactly two unmatched: **97** (§8, "97% of the FIT-admitted candidates die") and
**240** (§14, "40 declared cells of 240"). 6,144/6,336 = **32/33** exactly; "97%"
is a rounded, float-valued statistic in a unit whose §14 states that no float
appears anywhere. 240 = 48 × 5 is a trivial product, and I verified the squaring
identity at all 240 cells.

**Repair.** §8: "here **32 of every 33** FIT-admitted candidates (6,144 of
6,336) die on cells the fit never saw".

### F11 — NOTE. Gate claim strings do not carry the sub-total scopes the note carries.

G17's claim does not say "5 of the 4,608-member class"; G12's does not say "40
of 240". Both are recoverable from the gate details (`class_size: 4608` with 5
rows; `squaring_identity_cells_verified: 40`), and the note states both at every
claim, so RUNBOOK §4 is met in the note — but the receipt's claim strings, read
alone, do not disclose sub-totality.

### F12 — NOTE. Anchor coverage, stated honestly.

30 anchors, all reproduced. Seven (the hash pins) I corrupt-and-fire tested
individually; four content anchors (A01, A05, A14, A18) plus the exit-1 policy
are covered by declared mutants. The remaining eighteen are not individually
corrupted. Since `anchor()` is a single code path whose exit-1 behaviour I
verified seven times, this is structurally adequate — but "**30**, all
reproduced" should not be read as "30, each corrupt-tested", and the mutant
table's "twelve anchor mutants" against thirty anchors is the honest ratio.

---

## 2. K5 checklist, item by item

| K5 item | verdict |
|---|---|
| (a) 30 anchors traced; every hash pin corrupt-and-fire tested; exit-1 only by deliberate breakage | **PASS** — 7/7 pins fire with named anchors; clean run exits 0; see F12 for coverage scope |
| (b) 41,665 verified by independent formula/construction; route independence; dropped-cell probe | **PASS, strongly** — three constructions agree; two shared-input/orientation stresses make the routes diverge; mid-list basis drop fires G11 |
| (c) S5's 124 HELD cells genuinely held out (6,336 / 6,144 / 124-of-124) | **PASS mechanically, FAIL on disclosure** — the fit consults FIT alone and all numbers reproduce, but the whole protocol runs on the synthetic chart map (**F3**) |
| (d) synthetic FOUND (192 pairs, witness re-verified in-gate) and synthetic EMPTY reachability, both reconstructed | **PASS** — 192 pairs, 48 maps, witness re-verified independently; SYNTH-EMPTY 0, both reproduced from my own rebuild |
| (e) BREAK-HOM rejected by S1b alone (6,000/15,625) | **PASS** — reproduced numerically *and* derived in closed form; S1a exactly 0, accepted counterpart 0/0 |
| (f) 55 mutants audited (≥3 reconstructed); `never_falsified` empty at honest denominators | **PASS** — 55 declared, 55 exit 1, breakdown matches; I reconstructed `enum-drop`, `encoding-drop`, `grid-drop`, `route-alias`, `count-flip`, `qualifier-typo` and `verdict-flip` at different corruption points; all 34 must-pass gates covered |
| (g) verdict-in-gate with computed qualifiers; typed-value and branch-flip probes impossible at exit 0; **both** verdicts probed | **FAIL** — bridge verdict is genuinely two-source gated and both flip probes are caught, but the Open-1 verdict flips at exit 0 (**F2**) and the obstruction qualifier accepts a fabrication at exit 0 (**F1**) |
| (h) cell-completeness: 224-cell grid, 4 encoding cells, P1–P12 — dropped-cell probes | **PASS** — all four fire, at drop positions other than the declared mutants'; see F7 on what the 224 counts |
| (i) no-sampling / no-randomness (AST + read); no-floats | **PASS** — no randomness imports, no seeded stream, no `[SAMP]`; my own float/complex/round scan clean, all three true-division sites on `Fraction`s; my widened run-mode AST scan returns zero offenders |
| (j) four-encoding-cell sweep complete (2 identifications × 2 directions); natural-identification-carries-the-involution measurement | **PASS** — all four cells built, invertible, distinct; I independently recomputed the induced slot permutations (natural → (1,0,2) = τ; index → (2,1,0) ≠ τ) and confirm exactly one identification carries the involution, and that the two τ-equivariant cells are exactly the natural ones |
| K1 (lower depth) spec(E) + p-sweep | **PASS** — squaring-forcing re-derived; spectra and the p = 3 singleton reproduced over every prime below 60 |
| K3 (lower depth) three P-candidates | **PASS** — six spot-verified; no misclassification found; see F8 on the column header |

---

## 3. What I could not break

For the record, these attacks failed to produce a defect:

- Corrupting the shared input to both census routes (routes diverge; caught).
- Swapping route B's square orientation (routes diverge; caught).
- Flipping the emptiness decision at the clause table (caught by the S4 grid).
- Flipping it at the S4 grid (caught by the clause table).
- Typing a qualifier other than the one the declared mutant targets — I tried
  `homomorphisms_enumerated` and `open1_declaration_free_intersection`; both
  caught at G30 (the latter only because `qualifier_value` is the injection
  point; the *source* corruption of the same quantity is not caught — F2).
- Dropping cells at four different positions in four different censuses.
- Gutting `defect_of` to the identity (dies at anchor A01).
- Finding a float, a random draw, an undeclared sample, a hidden timestamp, a
  gate function reading mutant identity, or a mutant surviving.

---

## 4. Grade

**ACCEPT-WITH-FIXES.**

Not REJECT: I could not move a single number. 97 independent recomputations
disagree with the unit nowhere; two of the load-bearing counts I re-derived in
closed form and they match exactly; both delivered verdicts —
`LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD` and `LCB-PRIME-DECLARED` — are, on
my own reconstruction, correct. The census is exhaustive as claimed, the two
routes are genuinely two, the 41,665 stands under three constructions, the pins
all fire, the mutant harness is complete at an honest denominator, and the
arithmetic discipline is clean under a scanner stricter than the unit's own.

Not ACCEPT: four MAJOR instrument defects, none of which changes a result and
all of which are local, but three of which defeat claims the paper makes in its
own voice about its own instrument. §13's "so a typed qualifier cannot reach the
receipt" is **false as delivered** — I put a fabricated obstruction into the
receipt at exit 0 with all 34 gates green (F1). The Open-1 verdict's advertised
double derivation is a single variable, and a one-line corruption flips it to
`LCB-PRIME-DERIVED` with nothing failing (F2) — the precise failure RUNBOOK §13
addendum #234 was written to prevent. The flagship held-out block is measured on
a synthetic deformation side and says so nowhere, in a unit whose own parent
carried a dedicated disclosure gate for exactly that asymmetry (F3). And the
declared positive control is an identity that survives the total destruction of
the predicate it claims to exercise (F4).

Required before terminal: **F1, F2, F3, F4** repaired as specified, with F2's
repair including a new declared mutant that perturbs `inter` to a singleton and
F1's including a mutant returning a plausible wrong obstruction. **F5–F9**
adopted as sentence-level corrections (replacement text supplied verbatim
above). **F10–F12** at the adjudicator's discretion. No number may move: none of
these findings proves a computed value wrong, and I verified 97 of them.
