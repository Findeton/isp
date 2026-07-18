# D41 round-one hostile review — record-closure of the identified benchmark

**Frozen target:** commit `a33bff4dbb60b97f9b7428f7674aa05ce7ca050b` (HEAD).
**Pin:** `note-d41-record-closure-of-the-identified-benchmark.md` at `01b22e1`
(the receipt's docstring pin claim verified against git history).
**Reviewed source:** `v10/code/d41_benchmark_record_closure_exact.py`, SHA-256
`5bec02cd1b994245b3717fc4cf271b2aaf16ad593e6e7daecc3ee53ff122c9cc`.
**Reviewed stdout:** `v10/data/d41_benchmark_record_closure_exact.out`, SHA-256
`77819688db59d7189512d0f6580a687a0c835fa48cd950a16b95506477a86ab9`.
**Date:** 2026-07-18.
**Verdict:** `3 BLOCKERS / 5 MAJOR / 5 MINOR / 4 NIT`.
**Promotion:** withheld.  The paper-30 decision must wait for a d41d repair
delta.  Blocker grading uses the d39-round-1 standard: a gate that does not
exercise the mathematical object named by its output is a blocker when an
item verdict leans on it.

Every printed number reproduces and every recomputed number is correct —
this is not a false-result rejection.  The rejection is that the round's
central headline (item 4) and two further item verdicts lean on checks that
cannot fail, and the scorecard's counting drifts from the pin's own verdict
alphabet.  The repairs are small, verified available, and in two cases
provably *strengthen* the receipt.

## 1. Reproduction and fixture fidelity

The frozen source exits 0 and reproduces the committed stdout byte-for-byte
under `PYTHONHASHSEED=7` and `83` (complete-output SHA-256
`77819688...86ab9` both runs).  The receipt contains no randomness, so
"seed-independent" is trivially true.

Fixture-convention fidelity to the paper-15 validator was checked item by
item and is clean:

- `tri_diagonal([0.6, 0.0, 2.2], [(0,1),(1,2)], 1.0)` is exactly
  `theorem3_check()`'s reference Hamiltonian (energy_x=0.6, energy_y=0,
  energy_z=2.2, t=1);
- the extracted entry `[2][0]` is Theorem 3's `(Z,X)` entry under the
  validator's basis ordering X=0, Y=1, Z=2;
- the fit deltas `[0.010, 0.012, 0.014, 0.016]` and powers `[4,6,8,10]` are
  the validator's own;
- the point-b prediction `p6b = (13/6) - (0.3^2 + 1.1^2)/12 = 2.058333...`
  is Theorem 3's formula with gaps `delta_{n+3/2}(X)=0.3`,
  `delta_{n+1/2}(Y)=1.1` (middle energy 0), faithful to Definition 6.

The B2 step change is disclosed honestly.  I reproduce both numbers in the
LOG's first-run lesson: at the fit-scale step 0.01 the bare-history
interference mass is `0.00079985` (the LOG's "0.0008 < 1/1000"); at the
declared functional step 0.3 it is `0.60857405` (the printed 0.6086).  The
redeclaration is marked DECLARED in the source and recorded in LOG #264
[D41 block].  For an existence exhibit this tuning direction is benign.

RF4 is discharged (the failing clause K is printed).  RF5 is discharged in
both directions: B6 cites `d41c RF5`; `note-d41c` §1 cites "D41 item 6"
by name.

## 2. BLOCKER-1 (gate B4) — "D26's 4/5 DERIVED in-benchmark" is not what the
computation does, and the NSE gate cannot fail

The two halves of the blocker:

**(a) The claim's width.**  The printed claim — "the birth-decoherence
bridge derived in-benchmark, not imported", echoed by the scorecard
("D26's 4/5 derived in-benchmark"), LOG #264 [D41 block] in bold, and the
commit headline — is wider than the computation.  What B4 computes is:
`phi = (|site0> + |site1>)/sqrt(2)`, `out = V1*phi`, reduced coherence
`rho01: 1/2 -> CTH/2`, ratio `CTH = sqrt(1-g) = 4/5`.  That is the D24
controlled-rotation overlap algebra — the same one-line trace identity D26's
E4 gate already proved terminally ("each birth contracts the parent's
coherence by exactly sqrt(1-g)", `d26_interface_equivalence_exact.py`).  No
benchmark datum enters the derivation: not the couplings, not the reduced
Hamiltonian, not the parity string, not the dynamics `U`.  The benchmark's
matter sector serves as a passive 3-dimensional substrate supplying one
orthogonal two-outcome distinction; any qubit would give the same 4/5.  The
only line where `U` touches the instrument (`v_rec[r] = Pr*(V1*(U*psi))`)
feeds the vacuous gate of part (b).  "Derived" is defensible (the number is
recomputed, not pasted); "in-benchmark ... not imported" is not: the
derivation is imported algebra executed on benchmark-labelled axes.

I verified the repair the pin actually asked for, and it exists, is exact,
and is stronger.  Inserting the click between the two `U` steps of B2's own
functional (class operators `(P_{i2} U (x) I) V1 (P_{i1} U P_{i0} psi)`,
ancilla traced) gives, at dps 80:

```text
max |D_click(h,h') - (4/5)*D_bare(h,h')|  over pairs with [i1=1] != [i1'=1]  =  9.3e-83
max |D_click(h,h') -       D_bare(h,h')|  over all other pairs               =  1.3e-82
```

i.e. the D26 factor holds at the *decoherence-functional* level of the
interacting fixture, exactly, on precisely the site-1-distinguishing
history pairs.  That is the genuine "two halves touch" statement.  Note
what the verified repair also proves: the 4/5 factorizes off the ancilla
tensor leg, so the benchmark's dynamics cancels from the FACTOR
identically.  The benchmark's contribution is to select WHICH pairs are
suppressed (the record basis / the queried algebra), never the value.  Any
repaired claim must carry that width.

**(b) The `nse_ok` gate cannot fail.**  `v_rec[0]` and `v_rec[1]` are
supported on disjoint coordinate sets (even vs odd indices of the 6-dim
space), so `cross` is identically zero for every `U`, `psi`, `V`.  I reran
the gate with a garbage non-unitary 3x3 matrix in place of `U`: cross =
`0.0` exactly.  "Record-sector overlap < 1e-60" is a structural triviality
of orthogonal coordinate projectors, printed as if it were a contingent
check.  Moreover the pin's item-4(c) NSE gate — "the value/content split
checked on the Z2 observables" — is not discharged by it: the value half
(populations preserved through the click) is exactly available and ungated
(I verified: max population error `0.0` at dps 80), and the content half is
the coherence dispersal of part (a).  Clause (b) of the pin (Busch class,
distinguishability-isometry) is prose ("trivially", "by dilation") attached
to the one real computation in the gate, `V1^dag V1 = I` (which I confirm
is exact at dps 80, since `CTH^2 + STH^2 = (16+9)/25` exactly).

The verdict "GENERATED-CONTENT" leans on (a)+(b); under the pin's own
honest fork ("if only a SUPPLIED instrument closes, the item is
IRREDUCIBLE with the failing clause printed") the item verdict is
IRREDUCIBLE-at-scope with generated content *typing* — see MAJOR-1.  The
half of B4 that survives attack is real and listed in §9.

## 3. BLOCKER-2 (gate B6) — the clock-invariance gate is an arithmetic
identity, and the pinned record-native clock is never constructed

`ok6c`'s first clause compares `(c6a/c4a)/(c6b/c4b)` with
`((s^6 c6a)/(s^4 c4a))/((s^6 c6b)/(s^4 c4b))`.  The `s` powers cancel by
construction; the equality holds for any four nonzero floats, to rounding.
The source comment itself concedes "verified symbolically".  The second
clause `|s^4 c4a - c4a| > 1` verifies `81 != 1`.  Neither clause can fail.
This is the D33-G5-class disease: a tautology dressed as a gate, and the
item verdict "RATIOS GENERATED" cites it ("cross-point ratio ... EXACTLY
invariant").

Second, deeper infidelity: the pin's item 6 defines record-native time as
"a repeatable click pattern in the generated instrument whose count serves
as duration" and asks for the coefficient re-expressed in that time.  The
receipt substitutes Trotter *layer count* — simulation bookkeeping, not a
record-born clock — and performs no re-expression at all.  Since B4's
schedule is supplied, an honest click-count clock is supplied-schedule
dependent; that dependence is exactly the "bridge-dependent absolute
scale" residue and should be stated as such, not silently bypassed.

The contentful version of the rescaling gate exists and passes; I ran it.
Refitting the *same* defect samples against the rescaled variable
`s*delta` (s=3) with the validator's own fit machinery:

```text
c4a' = 1.234567901235e-02   vs c4a/s^4 = 1.234567901235e-02
c6a' = 2.377686328095e-03   vs c6a/s^6 = 2.377686328319e-03
cross-point ratio from independent rescaled refits = 0.842105262926313
native cross-point ratio                           = 0.842105262946155
|difference| = 1.98e-11
```

So the physics claim behind B6 is true and demonstrable by an independent
computation — the receipt just did not gate it.  (Bonus: the exact
cross-point ratio is rational, `(26/15)/(247/120) = 208/247 = 16/19 =
0.84210526315...`; the fits sit 2e-11 off it.  A repaired gate can pin the
exact value.)

## 4. BLOCKER-3 (gate B3) — the "complete parameter census of every
constructed object" is neither complete nor a census, and the gate cannot fail

`ok3 = all(k not in params for k in ("cutoff","Lambda_UV","renorm_scale"))`
checks that three keys the author did not write are absent from a dict the
author wrote.  It cannot fail.  Worse, the dict misdescribes the receipt's
own constructed objects:

- B1's actual call is `occupation_hamiltonian(..., 1.0, 0.5, 0.3, lam)` —
  hopping 1.0, **mass 0.5, electric 0.3**; the census says mass 1.0,
  electric 0.5;
- the census lists `trotter_delta = 0.01` but the functional is built at
  `delta_D = 0.3` (the receipt's own headline declared step) — absent;
- also absent: `lam2 = 0.3` (B5), `g = 9/25` (B4), the theorem-3 energies
  `(0.6, 2.2)` and the point-b couplings `(0.3, 1.1)` (B6).

The pinned gate is "the absence [of renormalization data] is PROVED (no
cutoff parameter appears in any constructed object)".  That proof was not
executed.  The verdict COLLAPSED-AT-SCOPE is *true* (finite-dimensional
fixture; no `bench` constructor signature carries a cutoff-class argument
— checkable mechanically), so this is a receipt-integrity blocker, not a
physics error; but as printed, the one item the pin called "why the
benchmark is the right first fixture" is certified by a vacuous check over
a false census.

## 5. MAJOR findings

**MAJOR-1 — verdict-alphabet drift and count inflation.**  The pin is
explicit: "Every one of paper 29's supplied items must end in exactly one
of three verdicts, per item".  The receipt issues hybrids for items 2
(GENERATED-AS-OBJECT / descent conditional), 4 (GENERATED-CONTENT /
SUPPLIED-SCHEDULE) and 6 (RATIOS GENERATED / SCALE SUPPLIED).  Item 4 is
the sharp case: the pin's own fork assigns IRREDUCIBLE when only a supplied
instrument closes — which is what happened (the schedule, i.e. the
instrument as an executing law, is supplied; one content isometry was
built by hand per the D24 recipe, not generated by a D34-class law as
pinned).  The NET line "3 generated" counts item 4 as generated; at the
pinned alphabet the honest count is 2 generated (items 2 and 5, each with
a disclosed qualification), 4 irreducible, 1 collapsed.  "7/7 verdict
gates" also counts B7, which is `ok7 = True` — a declaration, permitted by
the pin, but not a gate.

**MAJOR-2 — "ZERO OBSTRUCTED" and "closer to record-closed" are wider than
the receipt.**  OBSTRUCTED per the pin requires a produced finite witness.
The receipt sought none: items 1 and 7 had no generation attempt at all,
and item 4's schedule was declared supplied without an attempted-and-failed
construction.  "Zero obstructed" is therefore "zero obstruction witnesses
sought", and the scorecard headline reads as a positive structural result
it cannot license.  The true movements against paper 29's raw list (item 3
collapses by finiteness; the functional exists as an object; the string
term compiles to arity <= 2; the D26 bridge instantiates exactly) do
support "closer than the raw list read" — but only with corrected counts
and a rescoped obstruction sentence.  The scorecard's "confirmed AT the
identified law's smallest fixture" language also carries no d41b bin
labels; per RF3 every one of these results is Bin T (toy-relative) until a
second grammar instantiates it, and the receipt-level scorecard should say
so once.

**MAJOR-3 — the preferred-durable-algebra residue is unnamed; "every
residue lands on K, the boundary, or the clock bridge" is false at the
parent audit's own census.**  Paper 29 §9.2 lists *eight* slots, including
"preferred durable algebra ... determines the queried record basis"
(supplied/selected by an open physical mechanism) and the action-to-
finite-operator map.  The pin's seven items silently drop the former (the
latter is discharged by fiat in choosing the fixture).  In the receipt the
choice re-enters invisibly: B4 reads the *occupation* basis because the
pin pre-selected "matter occupation; parity string" as the record
observables.  Nothing generates that basis choice, and it lands on none of
the three named organs.  The scorecard's closing sentence must name it as
the fourth residue (it is exactly the "preferred durable algebra" slot,
and — per BLOCKER-1's tensor-leg cancellation — it is the *only* place the
benchmark enters the D26 bridge).

**MAJOR-4 — B1's pinned "attempt generation of the sector CHOICE" was not
attempted, and its census gate cannot fail.**  The gate counts
`len(H) == 8` over the 8 sign blocks; `occupation_hamiltonian` returns an
`len(basis)`-square matrix for *any* lambdas (I verified `len = 8` for
lambdas `[17, -3.2, 0]`), so only a crash could fail it.  No record-law
generation of the block choice was attempted; the IRREDUCIBLE declaration
matches the pin's expectation, so the verdict stands, but the pinned
attempt clause is undischarged (a one-paragraph structural argument — the
in-scope record laws output click patterns, not sector labels — would
discharge it honestly).

**MAJOR-5 — B5's pinned gate ("a bijective-at-scope typed map") was
reinterpreted, and the linear-cost claim is asserted, not gated.**  The
ladder identity itself is exact and survives independent rebuild (integer
bit algebra and float, 3-site error `0.0`), and I verified the 4-site
extension (3 CNOTs, error `0.0`), so "cost linear in prefix" is true — but
the receipt gates only the single 3-site instance and asserts the rest.
More important: one benchmark elementary process (the parity-string term)
maps to a *composite* of five record events, so the map is not bijective
per process; the pin's alternative branch for that situation was the
obstruction witness.  The receipt discloses the composite honestly
("DISCLOSED COMPOSITE COST") but the scorecard still counts item 5
GENERATED simpliciter, and whether ladder CNOTs are admitted *typed record
events* (with D24 birth content) rather than compilation gadgets is
asserted, not typed.  Each CNOT does touch exactly 2 wires, so the
"arity <= 2" count itself is honest.

## 6. MINOR findings

**m1 — B6 tolerances are ~9 orders looser than achieved.**  Recomputed
residuals: `|c4a - 1| = 2.0e-15`, `|c6a - 26/15| = 1.1e-11`,
`|c4b - 1| = 2.1e-14`, `|c6b - 247/120| = 5.3e-10`, against gate
tolerances 5e-3 and 5e-1.  A c6 wrong by 24% would pass the printed gate.
Tighten to achieved order (e.g. 1e-8).

**m2 — precision-discipline deviation in B6 and in the coupling embedding,
disclosed but pin-nonconforming.**  The pin's capacity clause: "exact
rationals wherever the couplings admit them; declared-precision mpmath
(dps >= 80) where not".  B6 runs the validator's float64 machinery
(declared in the docstring as a deliberate no-reconstruction choice), and
the quantum gates embed the exactly-rational couplings 0.6 = 3/5,
2.2 = 11/5 as *binary floats* via `mpc(float)` (off the true rationals by
~2e-17; I measured the induced U difference at 5.2e-17 against a true-
rational rebuild).  Harmless at every gated tolerance; still a letter
violation.  One mpmath cross-extraction at a single B6 point, and
`mpf(3)/5`-style couplings, close it.

**m3 — Taylor-U unitarity is nowhere gated.**  The mass-1 gate is a
one-orbit surrogate (`sum D = ||U^2 psi||^2` identically).  It happens to
be safe: spectral radius of H is 2.65989, so `||H*delta_D|| = 0.798`,
59-term truncation bound `1.6e-88`, and I measured
`max|U^dag U - I| = 8.4e-81` (dps-80 rounding floor).  No conspiracy is
possible — but the receipt should print the defect or the bound instead of
implying unitarity.

**m4 — LEDGER numbering collision.**  The D41 LOG entries carry LEDGER
#261-#264 while the same file's D40/paper-29 block already uses #261-#273
(both dated 2026-07-15), and D41's "findings -> #265" collides with "D40b
closes the typed probability-space repair (LEDGER #265)".  The D41 block
also chronologically postdates paper 29's #273 (its own pin cites paper 29
as parent).  The D41 entries should be renumbered #274-#277 and the LOG's
top-block/bottom-block ordering unified; cross-references (including this
review's commission) are currently ambiguous.

**m5 — the printed "coherence factor = 0.8" is honest but its baseline is
implicit.**  The print multiplies `coh_after` by 2, i.e. divides by the
before-click coherence 1/2, which the receipt never computes.  The
arithmetic is right (I recomputed: before 0.5, after 0.4, ratio exactly
4/5); print before/after explicitly so the factor is self-auditing.

## 7. NITs

**n1** — unused imports: `asin`, `norm` (mpmath) and `math` are imported
and never used.
**n2** — stale comments: `delta = mpf(1)/100` is annotated "B6's fit scale
(the validator's)" but B6 hardcodes its own delta list (0.01 actually
feeds B5's phase and the census); the B6 comment "scales c4 by s^0"
contradicts the s^4/s^6 usage four lines later.
**n3** — the exact cross-point ratio 16/19 is available and worth printing
(see BLOCKER-2).
**n4** — LOG #264's "seed-independent 0/7" describes a receipt with no
randomness; say "deterministic, no RNG" instead.

## 8. SURVIVES ATTACK

- Byte-identical reproduction, exit 0, hash-seed independent, RNG-free.
- Fixture-convention import fidelity to the paper-15 validator: energies,
  entry convention, fit deltas/powers, and the Theorem-3 c6 prediction
  formula at both parameter points (§1) — no reconstruction drift found.
- B2's functional as an object: 27 class operators; total mass 1 at dps 80
  (independently rebuilt via eigendecomposition; `|sum D - 1| = 0.0` at
  dps 80); bare-history interference 0.60857405 reproduced; the
  0.01 -> 0.3 step redeclaration disclosed accurately (I reproduce the
  first-run 0.0008).
- B4's numbers: `V1^dag V1 = I` exact; coherence 0.5 -> 0.4, ratio exactly
  4/5; populations exactly preserved.  The *instantiation* of the D26
  bridge on the fixture's matter sector is real.
- The functional-level D26 statement (the repair) is verified true and
  exact: suppression by 4/5 on exactly the site-1-distinguishing history
  pairs, deviations < 1.4e-82 (§2) — the repaired receipt will be stronger
  than the current one.
- B5's ladder identity: exact at dps 80 and under two independent rebuilds;
  the 4-site extension holds (linear cost confirmed at s=3).
- B6's two-point coefficient recomputation is genuine: c4 = t^4 to 2e-15 /
  2e-14; c6 matches Theorem 3 to 1.1e-11 / 5.3e-10; the contentful
  rescaled-refit invariance holds at 2e-11 with exact value 16/19.
- Verdicts B1-IRREDUCIBLE, B3-COLLAPSED, B7-IRREDUCIBLE are true
  conclusions at scope (the findings above concern their gates and
  arithmetic of the scorecard, not the conclusions).
- RF4 and RF5 discharged; RF1/RF2 correctly silent at the finite fixture.

## 9. Gates re-verified

```text
gate  printed check                          recomputation                    status
B1    8/8 blocks define H                    len=8 for ANY lambdas            cannot fail; verdict true
B2    |sum D-1|<1e-60; offdiag 0.6086        0.0; 0.60857405 (indep. rebuild) REAL (mass-1 = one-orbit unitarity surrogate)
B3    census keys lack cutoff names          dict mismatches actual objects   cannot fail; census false; verdict true
B4    V iso; coh factor 4/5; cross<1e-60     exact; exact; cross==0 for       iso+factor REAL; cross cannot fail;
                                             garbage U                        claim wider than computation
B5    |string-ladder| = 0                    0 (two indep. rebuilds; 4-site)  REAL at the single gated instance
B6    c4/c6 two points; ratio invariance     residuals 2e-15..5.3e-10;        two-point part REAL (loose tol);
                                             identity passes for any floats   invariance clause cannot fail
B7    (none)                                 —                                declaration, not a gate
```

## 10. Pin fidelity, item by item

```text
item  pinned gate                                receipt                              fidelity
1     census + ATTEMPT generation of choice      census-print (vacuous); no attempt   PARTIAL (M4)
2     functional constructed; strong positivity  27 ops at dps 80; PSD by Gram        GOOD (positivity is
      + ladder hypotheses at scope               (admitted); interference exhibit     by-construction, honest;
                                                 -> descent withheld                  rational-coupling letter dev.)
3     absence PROVED over constructed objects    vacuous key check, false census      FAILED as gate (BLOCKER-3);
                                                                                      conclusion true
4     (a) D24 typed content at declared g        isometry at g=9/25 exact; birth      PARTIAL (BLOCKER-1);
      (b) Busch + distinguishability-isometry    content implicit (sin^2 = 9/25);     fork verdict should be
      (c) NSE value/content on Z2 observables    (b) prose; (c) vacuous cross;        IRREDUCIBLE per pin
      (d) honest fork w/ failing clause          (d) clause K printed, verdict drift
5     bijective-at-scope typed map or witness    composite w/ disclosed cost          REINTERPRETED (M5)
6     record-counted (click-count) time;         Trotter layers, no re-expression;    FAILED as pinned gate
      value-invariance gate                      identity check                       (BLOCKER-2); claim true
7     record as supplied; name D42               done                                 MATCHES pin
```

## 11. False-result count

**False numerical results: 0.**  Every gated and printed number was
recomputed and is correct (mass 1; 0.6086; 4/5; ladder 0; c4/c6 at both
points; 81; the disclosed first-run 0.0008).  **False printed artifacts:
1** — B3's "complete parameter census of every constructed object" line
(the census is incomplete and its underlying values disagree with the
receipt's own calls; §4).  The claim-width findings (BLOCKER-1, MAJOR-2,
MAJOR-3) are scope inflations, not numerical falsities.

## 12. Owed repairs (ordered)

1. **B4 (BLOCKER-1):** add the functional-level click insertion and gate
   `D_click = (4/5) * D_bare` on site-1-distinguishing pairs, `= D_bare`
   otherwise (both < 1e-60 at dps 80; verified available).  Rewrite the
   claim at instantiation width: the D26 bridge *exactly instantiated on
   the identified fixture's decoherence functional*; the factor's value is
   fixture-independent D24 algebra (tensor-leg cancellation), the fixture
   selects which pairs are suppressed (the record basis).  Delete "derived
   in-benchmark, not imported" from the label and scorecard; record the
   width correction in the round ledger.
2. **B4 NSE (BLOCKER-1b):** gate the value/content split per pin 4(c):
   populations preserved exactly (value), coherence dispersed into the
   ancilla by exactly 4/5 (content); demote the disjoint-support cross to
   a structural remark.
3. **B6 (BLOCKER-2):** replace the identity clause with the independent
   rescaled refit (fit the same samples against `s*delta`; gate
   `c4' = c4/s^4`, `c6' = c6/s^6`, and refit-ratio vs native ratio at
   <= 1e-8; optionally pin the exact 16/19).  State explicitly that the
   layer-count clock is a *stand-in* for the pinned click-count clock and
   that a click-count clock is supplied-schedule dependent until K exists.
4. **B3 (BLOCKER-3):** build the census from the actual constructor calls
   (collect every parameter passed to `bench` plus the receipt's own
   scales: delta_D, lam2, g, both B6 points; fix mass/electric to B1's
   real values) and prove absence mechanically (no cutoff-class argument
   in any used `bench` signature).
5. **Scorecard (MAJOR-1/2/3):** restate in the pinned three-verdict
   alphabet with splits as sub-annotations (item 4 IRREDUCIBLE per the
   pin's fork, generated content typing noted; honest NET 2 generated /
   4 irreducible / 1 collapsed / 0 obstructed); rescope "zero obstructed"
   to "no obstruction witness found; none systematically sought"; name the
   preferred-durable-algebra choice as the fourth residue; add the d41b
   Bin-T label once.
6. **B1 (MAJOR-4):** discharge the attempt clause with the structural
   argument (in-scope record laws output click patterns, not sector
   labels), or re-pin.
7. **B5 (MAJOR-5):** gate the 4-site ladder (linear cost becomes a checked
   claim at two lengths) and either type the ladder CNOTs as admitted
   record events or label the dictionary homomorphic-with-composites
   rather than GENERATED simpliciter.
8. Minors: tighten B6 tolerances (m1); one mpmath cross-extraction +
   rational couplings (m2); print the unitarity defect (m3); renumber the
   D41 LEDGER entries #274-#277 (m4); print before/after coherence (m5);
   sweep the nits.

## 13. The commissioned question (round 1)

**Does B4's in-benchmark D26 claim survive at its printed width?  No.**
"The birth-decoherence bridge derived in-benchmark, not imported" is, as
computed, D24/D26's own controlled-rotation overlap algebra re-executed on
a passive 3-dimensional substrate; the benchmark's couplings, interaction
and dynamics provably cancel from the factor, and the one gate that ties
the instrument to the benchmark's evolution cannot fail.  The claim
survives at the narrower width "the D26 bridge exactly instantiated at the
identified fixture, with the reading observable a benchmark gauge
invariant" — and the verified functional-level repair (suppression of
exactly the site-1-distinguishing history pairs of the interacting
fixture's own functional by exactly 4/5) upgrades it to a true
in-benchmark statement whose benchmark content is the *record-basis
selection*, never the number.  That, not the current headline, is the
honest shape of the program's first contact between its two halves — and
it is one inserted isometry away from being receipt-true.

---

## 14. Delta verification of the d41d repair receipt — DELTA-CLEAN

**Delta target:** commit `183e78e9e63e18fde041146e6e361313c6e368f1` (HEAD).
**Repair source:** `v10/code/d41d_benchmark_record_closure_repair.py`, SHA-256
`ab1aa8d70c1b7961a403a7eec4030afe5533d85e17c5f2e31952099c0e7ca8e4`.
**Repair stdout:** `v10/data/d41d_benchmark_record_closure_repair.out`, SHA-256
`0f8eefe89799835a02391a3b6c249c2525cd4852775a63f4c5f26ce1a2c8fabc`.
**Date:** 2026-07-18.
**Delta verdict:** `0 BLOCKERS / 0 MAJOR / 0 MINOR / 3 NIT` + 2 carried
obligations.  **DELTA-CLEAN.**  All three blockers and all five majors are
repaired, in every case by the strengthening this review pre-verified.  The
round-one report above is retained unmodified as history (this section is
append-only).  Reproduction: exit 0, byte-identical to the committed stdout
under `PYTHONHASHSEED=7` and `101`; the receipt is RNG-free, so
seed-independence is structural.  The original `d41_...exact.py/.out` and
this report were untouched by the repair commit (verified by diff).

### 14.1 R2 — the functional-level D26 gate: verified; deviation reconciled

The construction is the one this review pre-verified in §2 (click between
the functional's own U-steps; all 729 pairs; suppression by exactly 4/5 on
exactly the site-1-membership-distinguishing pairs).  The printed pair
census 12/15 is correct both combinatorially (h0 = 1 forced by psi; final
slots must match; 4 of 9 ordered middle pairs distinguish, times 3 finals =
12 suppressed; 15 = 27 − 12 nonzero unchanged) and numerically.

**Deviation reconciliation (1.05e-81 vs the round's < 1.4e-82): VARIANT,
not a finding.**  With the receipt's own Taylor U (couplings embedded from
binary floats 0.6/2.2), *both* the receipt's kron pipeline and this
review's per-ancilla-block pipeline give worst deviation `1.0542e-81` —
identical, and matching the printed 1.05e-81.  The round-one 1.3178e-82
came from this review's independent U built by *eigendecomposition* over
decimal-rational couplings — a different dps-80 rounding path, not a
different mathematics.  Both figures are rounding-floor artifacts sitting
more than 20 orders below the 1e-60 gate.  The honest-width sentence is
inline and faithful to §2's prescription verbatim (the 4/5 VALUE is D24's
algebra; the benchmark contributes WHICH pairs — the record basis, the
eighth residue).

### 14.2 R3 — a real NSE gate: verified; the negative-control fix graded correct

All 10 = C(5,2) pairwise distances on the probed family are preserved with
worst deviation `0.0` at dps 80.  The negative control is genuine: analytic
violation `|sqrt(1/2) − sqrt(1/5)| = 0.25989319` matches the printed
0.2599, and the gate threshold 1/100 can fail.  The first-run lesson is
empirically confirmed: I reran the *orthogonal* basis pair under the same
diagonal control — violation exactly `0.0`, so the original control was
indeed incapable of rejecting, and the fix (a non-orthogonal pair, overlap
1/sqrt(2)) is both correct and necessary.  Grade: correct fix, honestly
recorded.  The value/content split is now computed on rho: Z-marginals
preserved exactly (worst err 0.0), X-coherence exactly `0.4 = CTH/2`.  The
round-one vacuous cross gate is gone entirely.  Pin item 4(c) is
discharged.

### 14.3 R4 — the click-count clock and refit gate: now a computation

Yes — a computation, no longer an identity.  The refit against click-native
abscissae is an independent Vandermonde solve whose s-scaling *emerges*
numerically; recomputed margins: c4 relative deviation `3.3e-15` / `1.9e-15`
(gate 1e-8), c6 `3.8e-11` / `1.8e-11` (gate 1e-6), ratio agreement
`1.7e-11` (gate 2e-9), `|native − 16/19| = 2.1e-10` (gate 5e-7) — every
gate can fail and sits 3-4 orders above the achieved error.  The Fraction
derivation of the exact ratio re-verified: `(26/15)/(247/120) = 208/247 =
16/19`.  The exact-rational anchor also substantially discharges round-one
m2 (the float pipeline is now checked against an exact prediction).  The
clock is a *declared* dictionary (one click per layer; bridge supplied) and
item 6 is scored IRREDUCIBLE accordingly — consistent with the pin's fork;
no generation claim is made.

### 14.4 R6 — the census: it can fail (demonstrated), value-complete, one coverage nit

Failability demonstrated by mutation: (A) removing the `rec()` wrapper on
"g" -> R6 `[FAIL]`, exit 1; (B) introducing an undeclared key -> R6
`[FAIL]`, exit 1.  The 13 declared keys are value-complete for every model
parameter in the file.  Coverage nit (N3 below): four use sites carry
unwrapped literals that coincide with censused values — point-a's
`(0.6, 2.2)` at the R4 loop and `defect_samples`' hard-coded hopping
`1.0`/middle `0.0`.  Demonstrated: mutating the unwrapped `0.6 -> 0.7`
*evades* R6 (still passes) but is caught by R4's exact-16/19 gate (exit 1)
— defense-in-depth holds for every such site (hopping drift likewise
breaks the exact ratio), so the exposure is theoretical.  Precision knobs
(dps, Taylor order, TOL) and probe/control artifacts are legitimately
outside the census's declared scope (cutoff-class data).

### 14.5 R5, R1 — verified

R5: the 4-site string equals the 7-event ladder exactly (`0.00e+00` at dps
80); independently re-confirmed by bit-exact parity algebra; cost
`2(n−1)+1` now instantiated at two sizes, as owed.  R1: gated unitarity
defect `8.43e-81` equals this review's round-one measurement (8.4338e-81)
exactly; gate < 1e-75 can fail; consistent with the truncation bound
1.6e-88 at `rho(H)*delta_D = 0.798`.

### 14.6 R7 — the corrected scorecard satisfies the verdict-alphabet and scope majors

Yes.  Eight items (paper 29 §9.2's census restored); strict trichotomy with
qualifications as annotations only; item 4 IRREDUCIBLE per the pin's own
fork; item 6 IRREDUCIBLE (scale supplied); NET `2 GENERATED / 5 IRREDUCIBLE
/ 1 COLLAPSED` — exactly the honest count §5/§12 prescribed.  The eighth
residue is declared with the correct width tie-in (the record basis is what
the benchmark contributes to D26's suppression map).  The obstruction
sentence is exactly the prescribed rescope ("zero obstructions FOUND AT
THESE GATES; no obstruction witnesses were sought — absence is not
proven").  The inflating "closer to record-closed" headline is gone.  R7's
`check(True)` is an unconditional print, but it is now labeled as a
scorecard print and the ALL-CHECKS line discloses "R1-R6 substantive, R7
scorecard" — acceptable.

### 14.7 The #278 numbering forward-correction — adequate

The LOG re-keys by declaration (append-only): the D41-turn entries are
henceforth #274 (pin), #275 (consolidations), #276 (d41c+D42), #277 (D41
green), #278 (this report), #279 (d41d), with the map stated in the #278
entry and repeated in both commit messages.  Adequate; more honest than
rewriting an append-only log.  Residue accepted as-is: the old block
headers still literally read #261-#264, stale by design — any future
citation must use the forward map.

### 14.8 Delta nits and carried obligations

- **N1** — R2's `ok2` does not assert `npairs_s > 0`; an all-zero
  functional would pass vacuously.  The printed 12/15 evidences
  non-vacuity and U's unitarity is gated by R1, so the exposure is
  theoretical.  Add `ok2 &= npairs_s > 0`.
- **N2** — R3's comment "an orthogonal pair keeps distance 1 under any
  linear map" is over-broad: true when the pair are singular vectors of
  the control (as here — verified violation 0.0), false for general M
  (`<a|M^dag M|b>` need not vanish).  Scope the comment to the diagonal
  control.
- **N3** — the four unwrapped census use sites of §14.4; wrap them (or
  assert-same-value) for closure.
- **Carried obligation 1** — the d41b Bin-T / second-grammar label (RF3):
  the sweeping sentence that triggered it is deleted, so per d41b's own
  protocol the obligation now binds at *paper-30 abstract* time — every
  fixture-level result here is Bin T until a second grammar instantiates
  it.
- **Carried obligation 2** — the superseded original receipt
  (`d41_benchmark_record_closure_exact.py/.out`) remains in-tree with its
  round-one headline, as history.  Correct under LOG #278/#279, but paper
  30 must cite d41d's gates and scorecard, never the original's B4/B6/B3
  labels.

### 14.9 Delta conclusion

Every blocker repaired by the pre-verified stronger computation; every
major repaired at the prescribed width; all repairs independently
recomputed and reconciled; the corrected scorecard is the honest one.
False numerical results in d41d: **0**.  **DELTA-CLEAN.**  D41 may go
terminal at the corrected scorecard (2 GENERATED / 5 IRREDUCIBLE / 1
COLLAPSED over paper 29's eight items, zero obstruction witnesses sought),
and the paper-30 decision opens, carrying obligations 1 and 2.
