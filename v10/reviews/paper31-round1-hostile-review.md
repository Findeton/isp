# Paper 31 round 1 — hostile review (full number sweep + claim audit)

**Object:** `v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md`
at HEAD 3da9a63 (LOG #346).
**Read against:** the four terminal receipts + committed outputs
(`d43a` 7/7, `d43b` 18/18, `d43c` 11/11, `d43d` 6/6, under `v10/code/` +
`v10/data/`); the campaign pins with their §5–§7 amendments
(`note-d43a/b/c/d`, `note-d43-corpus-audit`, `note-d43e`); the frozen
review records (`d43a-round1`, `d43bc-round1`, `d43d-round1`, each with
its delta); paper 30 (abstract, §1.2, §5.4–5.7, §6.1–6.3, §7.2,
§8.1–8.3, §9, §9.1, §9.2); LOG #327–#346; and the cited corpus files
`v1/paper1`, `v1/paper8`, `v2/paper1`, `v8/paper12`, `v8/paper13`
(all present in the repo and checked at the cited content).
**Method:** every quantitative claim in the paper traced to its
committed source; the load-bearing reductions recomputed independently
in exact `Fraction` arithmetic (scratchpad `paper31_referee_probe.py`,
43 checks, all green — inventory in the appendix); all four receipts
rerun fresh (exit 0, byte-identical to the committed `.out`s); the
receipt sources inspected where the paper's provenance tags depend on
what is actually gated. Nothing in the repo modified except this file.

## VERDICT: REVISE — 2 BLOCKER / 3 MAJOR / 8 minor / 4 nit

**The physics survives the sweep intact.** Approximately 270
quantitative items were checked individually (every fraction, count,
matrix entry, table row, threshold, PASS count, and census number —
inventory in §V). **Zero false physics numbers.** Every kappa, orbit
ratio, tau entry, transfer entry, spectral certificate, menu weight,
D\* value, width, and threshold in the paper is exactly what the
receipts and the frozen record deliver, and the four decision
statements are scoped exactly as their terminal endorsements require
(operator-ray-only for d43a with lattice rule-relativity kept real;
window-scoped for d43b with both closure ingredients receipt-gated;
existence-face-only for d43c with foliation/measure open and separate;
width-axis for d43d with the multi-author-arb corner named). The two
BLOCKERs are a false mathematical gloss in the residue ledger (the
`kappa(m)` zero crossing described as the rules' agreement point — it
is the opposite) and one unsupported numerical claim in the methods
note (the resurrected fit-era "27 digits of margin" figure). The
MAJORs are provenance/characterization defects: one sentence that
asserts the open closure theorem's conclusion as fact, one false
`[EXACT, gated]` tag, and a misdescription of d43a's as-run
arithmetic. All fixes are one to three lines; none touches a delivered
number or a decision scope.

---

## I. BLOCKER findings

### B1 — §7 item 7 (lines 710–712): the zero-crossing gloss is false —
### `kappa = 0` is where the rules maximally DISAGREE in the constant,
### not where they agree

Paper: "compute `kappa(m)` as an exact function and locate its zero
crossing — **the mass at which the two admission rules agree to this
order *including* the constant**, a distinguished point of the
fixture."

The receipts and the paper's own §2.4 fix the two constants: EXC
collapses to exactly `1 · (I − sigma_x)` at **both** masses; LT
collapses to `kappa(m) · (I − sigma_x)` with `kappa(1/2) = +13/2304`,
`kappa(1) = −1/72`. At the zero crossing `kappa(m0) = 0` the LT rule's
identified transport operator **vanishes** at this order while EXC's
is `1 · (I − sigma_x)` — the constants disagree maximally there
(one is zero, the other is one). Agreement *including the constant*
would be `kappa(m) = 1`, a different point whose existence is not
established by anything in the record. No authoritative source carries
the agreement gloss: the frozen d43a review (R4/B4), LOG #340, and the
synthesis note all say only "kappa(m) as an exact function (locate the
zero crossing)" — the crossing implied by the sign flip. The paper
invented the characterization, and it mis-aims the named successor.

**Fix (one clause):** "… and locate its zero crossing — the mass at
which the LT rule's identified transport operator vanishes at this
order (the sign flip's guaranteed crossing), a distinguished point of
the fixture." (Optionally note `kappa = 1`, agreement with EXC, as a
separate question if it occurs.)

### B2 — §8 (lines 733–735): "`>= 27` digits of margin at every gate"
### is the retired fit-era figure; unsupported — and false under every
### as-run reading this referee can construct

Paper: "floating amplitudes only where isometry defects are measured,
at `mpmath dps 50` against thresholds `1e-30`/`1e-40` with `>= 27`
digits of margin at every gate."

The 27-digit figure descends from pin d43a §5's **fit-era** spec
("thresholds 1e-40 (Δ⁸ coefficients at these Δ are ≥ 1e-13 — 27
digits of margin)") — a spec the campaign itself superseded (pin §7
B5: "§5's precision is corrected to the as-run dps 50 / 1e-30 /
exact-series"; the fits no longer exist). No receipt computes or
prints a margin. As-run readings: (i) d43a's gate comparisons are
mpmath dps-50 values against `TOL = 1e-30`; the dps-50 rounding floor
is ~`1e-49`, giving ~19 digits of margin; (ii) the smallest genuine
nonzero d43a quantity (`1/36864 ≈ 2.7e-5`) against `1e-30` gives
~25.4 digits; (iii) the d43c isometry gates print defect `0.0`
(margin unbounded) — but the claim is "at every gate", and the d43a
gates cannot reach 27 under any reading. Recomputed in the probe
script: both candidate readings land below 27.

**Fix:** delete the margin figure, or replace with the true as-run
statement: "thresholds `1e-30` (d43a) / `1e-40` (d43c); measured
defects are zero at working precision (dps 50), and the exact-series /
exact-`Fraction` layers behind the gates carry no tolerance at all."
If a margin figure is wanted, compute one and cite where it is
printed.

---

## II. MAJOR findings

### M1 — §3.5 (lines 422–424): the closure theorem's conclusion is
### asserted as fact one sentence before it is declared open

Paper: "Between them: **every deep history is, up to idle padding and
base renaming, a concatenation of copies of the finite window already
decided.** What remains is to assemble the two gated identities into
the induction — a theorem statement, not a computation, and it is left
open here."

The first sentence is precisely the renewal-pumping closure theorem's
content, and it is exactly what is NOT yet proved. The gated
ingredients are window-bounded: the pad-shift identity is verified on
the 12,942 pad extensions of the depth-≤6 family (NC3); the subtree
isomorphism reaches depth 3 below `H3` (215 nodes, MG6); the 144-point
census gates **one-step** menus at `len <= 4`. Nothing gated extends
these to "every deep history". The authoritative scope language (note
d43b §5 A3, the d43bc delta endorsement, synthesis S2) is uniformly
conditional: "the all-depth statement awaits the renewal-pumping
closure theorem, whose two ingredients are exhibited". The paper's
flat assertion widens that — and if it were true as written, the
induction would not be open.

**Fix (one line):** "Between them, the intended induction is exactly
this: that every deep history is, up to idle padding and base
renaming, a concatenation of copies of the finite window already
decided. Assembling the two gated identities into that induction is a
theorem statement, not a computation, and it is left open here."

### M2 — §5.4 (lines 606–611): "[EXACT, gated]" is a false provenance
### tag — no receipt gates the version-name-recurrence vacuousness

Paper: "The candidate alternative corner (version-name recurrence) is
mechanically vacuous — exact-repeat arbitrations and same-base
re-proposals are inadmissible under the grammar — so 'multi-author
arbitration events' is exactly the residual scope **[EXACT, gated]**."

The committed `d43d_dstar_generated_exact.py` carries exactly six
gates — NG1, NG2, NG3, NG3b, NG3c, NG4 — verified by source
inspection; none touches exact-repeat arbitrations, same-base
re-proposals, or vname recurrence (the only `vname` references build
the W6/W4 events). The vacuousness fact is TRUE and verified — but by
the d43d **delta review** (round-2 item 7: "checked mechanically" by
the referee) and recorded at LOG #342 ("BONUS CLOSURE") — i.e., it is
committed-campaign-record content, exactly the class the paper's own
Status line requires to be tagged in-line as such. "Gated" claims a
receipt gate that does not exist.

**Fix:** retag "[EXACT, cited to the committed campaign record]" (or
add the ~5-line gate to a future receipt touch and only then restore
"gated").

### M3 — §2.1 (lines 171–173) + §8 (lines 730–734): d43a's as-run
### arithmetic is misdescribed — the receipt's series ladder is
### dps-50 floating, not exact-rational

Paper §2.1: "All expansions below are truncated power series in
`Delta` to order 12 **with exact rational coefficients** — there is no
fitting anywhere in the receipt [EXACT]." Paper §8: "**exact truncated
power-series arithmetic (order 12, rational coefficients)** for the
defect ladders of §2 — no fitting anywhere; **floating amplitudes only
where isometry defects are measured**…"

Source-inspected: `d43a_lie_trotter_exact.py` computes the entire
series ladder in `mpmath` complex at `dps 50` (`s_mul`/`m_mul` over
`mpc`), compares against `Fraction` references converted to `mpf` at
`TOL = 1e-30`, and even hard-drops sub-`1e-45` entries inside `comm()`.
The committed `.out` shows the rounding (e.g. `…444455` tails on
`1/9216`). The coefficients are exact rationals *as mathematical
objects*, and their exactness was established by the frozen round's
independent Gaussian-rational rebuild ("my Fraction rebuild confirms
every receipt quantity exactly") — i.e., the exact-rational status is
**record-carried**, not receipt-computed. And "floating … only where
isometry defects are measured" is false: the whole §2 ladder is
floating at `1e-30` gates (the `1e-30` threshold belongs to d43a's
anchors, not to isometry defects; d43c's isometries are the `1e-40`
gates). The no-fitting clause is correct. The commissioning discipline
for this paper explicitly required as-run precision stated honestly;
these two sentences fail it.

**Fix:** §2.1: "truncated power series in `Delta` to order 12 — series
arithmetic at `mpmath dps 50` against `1e-30`, with the coefficients'
exact rational values confirmed by the frozen round's independent
exact-rational rebuild; there is no fitting anywhere in the receipt."
§8: "series arithmetic at dps 50 / `1e-30` for the defect ladders of
§2 (exact-rational values record-confirmed); exact `Fraction`
arithmetic wherever grammar weights, transfers, spectra, and menus
appear; `mpmath dps 50` at `1e-40` for the d43c isometry layer."

---

## III. minor findings

**m1 — §2.2 (lines 200–202).** "Strip-channel moments (the p7/p8
basis) are likewise non-proportional (six distinct channel ratios;
twelve LT residual entries outside the basis)" — the 6/12 figures are
the **d = 3** p8-faithful computation (frozen review F3(iii); pin B3
inherits the same unscoped wording). At d = 2 the corresponding
figures differ. Fix: "…non-proportional (at `d = 3`: six distinct
channel ratios; twelve LT residual entries outside the basis)".

**m2 — §2.3 (lines 219–225).** The d = 2 rows print single kappas
(`+79/2304`, `+13/576`) with no qualifier, but these are max-orbit
*representatives* — the max-magnitude orbit at d = 2 carries THREE
exact ratios per cell (the paper's own §2.2 table; frozen review F2;
pin B2 replaced per-cell kappa reporting for exactly this reason). The
d = 1 and d = 3 kappas are single-ratio orbits and fine as printed.
Fix: one clause, e.g. "kappa = the deterministic max-orbit
representative; the full d = 2 orbits are the §2.2 table's."

**m3 — §2.4 (lines 254–257).** "with one per-mass constant for the LT
rule **across both derivative layers**" — the second layer (`chi0`,
the `½ d_x beta` layer) is not gated in the receipt (the `.out` says
"chi0 cited to the report, delta to confirm"); it is carried by the
frozen d43a review's delta (bidirectionally re-verified, same kappa
both layers, LOG #340). Under the Status line's own rule this needs
the in-line campaign-record tag; §8's catch-all ("the frozen review
files for the independently re-derived certificates") is too vague to
bind this specific clause. Same note applies, more mildly, to §2.3's
`E^LT[Delta^8] = [A^LT_R, A^LT_S]` [THEOREM] (referee-proved in the
frozen round; in-receipt only as a label). Fix: append "(the second
layer per the frozen review record)" or equivalent.

**m4 — §1.3 (lines 129–144) vs §6 (lines 657–660).** §1.3 lists THREE
supersessions; §6 says "None of the four decisions weakens a committed
claim; **two of them** (§3, §5) supersede committed scaffolding … and
the supersessions are stated in §1.3". The third §1.3 item (the
pincer's scope) is itself a narrowing of paper 30 §6.2's literal claim
(which posed the horns for "a lifted arbitration step operator"
unrestricted); §6's sentence silently drops it. Fix: "…two of them
supersede committed scaffolding …; the third supersession (§1.3) is a
scope sharpening of the pincer, under which the horns stand."

**m5 — §1.3, supersession completeness.** Two further paper-30
sentences are now stale and should be named (the sweep found no
others): (i) paper 30 §8.3 — "until the step operator exists at the
discrete arbitration layer, there is nothing to take a limit of" — the
existence face is now discharged at fixture scale, so the continuum
gate transfers to the foliation/commutation face and the measure side
(the conclusion stands; the stated premise is superseded); (ii) paper
30 §7.2 — "the full probe needs depth beyond enumeration" — names the
wrong axis: §5 shows the capability axis is actor width (six events
suffice at width ≥ 4; depth alone never suffices at width ≤ 2). Item
(ii) is half-covered by §1.3's "and of width" clause; naming the
sentence would complete it. Checked and NOT stale: paper 30 abstract /
§5.6 / §5.7 / §9 residues 3–6 / §9.2 (all either superseded by the
listed items or untouched).

**m6 — §5.3 (line 579), §6 (line 652), abstract (line 61).** `S3` is
called "the minimal order of dimension 3" / "the first order that
breaks two-dimensionality". Minimal in SIZE, yes (no 3D poset on ≤ 5
elements — receipt-gated); but not unique at six elements: the
chevron is a classical 6-element 3-irreducible order, and the paper's
own `W4` poset is a second 6-element order failing `dim <= 2`
(explicitly "a non-S3 3-irreducible" in the frozen round). Fix: "the
standard minimal example of dimension 3" (matching the Dushnik–Miller
reference note) or "a minimum-size order of dimension 3".

**m7 — References item 3 (lines 788–790).** "v8 Paper 12, *the
canonical star-discrepancy instrument*; v8 Paper 13, *two-clock
universality*…" — the italicized phrases read as titles and are not:
the actual titles are "The 2D sufficiency theorem: a canonical
realizer, the rank embedding, and an intrinsic quantitative
characterization of volume-faithful record orders" and "Do records
measure positive? The two-clock frame, the natural-supply sweep, and
the Gibbs reconnaissance". The cited *content* is correct in both
(canonical D\*/rank embedding; Theorem 2.1 two-clock universality with
the `b`/`chi` ranks). Fix: real titles, or unitalicized descriptive
glosses in the style of reference 2.

**m8 — Abstract (lines 34–36).** "both collapse onto the *same*
tangential operator ray …, **with one per-mass constant each**:
`kappa(1/2) = 13/2304`, `kappa(1) = -1/72`" — "each" distributes over
both rules, but EXC's constant is exactly `1` at both masses
(mass-INdependent); the listed kappas are LT-only, unlabeled here.
§2.4 is precise. Fix: "…with the EXC constant exactly 1 at both masses
and one per-mass LT constant: …".

---

## IV. nits

**n1 — §8 (lines 726–728).** "the two chain receipts additionally
verified byte-identical across hash seeds" — d43c is the pincer
receipt, not a chain receipt; say "the d43b/d43c pair (seeds
0/7/11/61, LOG #344)".

**n2 — Coda (lines 774–777).** "The program's open surface is now
three theorems and a census" — undercounts the paper's own §7:
missing the arbitration-alone dimension question (residue 5's new
entry condition), transport-scope invariance (item 8), and the
standing empirical residues 3/4/6. "Nearest open surface" or an
explicit enumeration fixes it.

**n3 — §3.4 (lines 371–373).** "`u = lambda - 3/2` satisfies
`u^2 = 1/4` — the spectrum is rational" — the dominant class also has
the eigenvalue `3/2` (`u = 0`); the full spectrum is `{1, 3/2, 2}`
(recomputed exactly). The receipt uses the same shorthand; "the
nonzero shifted eigenvalues satisfy `u^2 = 1/4`" would be exact.

**n4 — §5.2 (lines 561–564).** "deliver two-clock certificates with
exact canonical values (`SIG_KR: 23/64`; …)" — the listed values are
canonical D\*, not the `(b, chi)` rank certificates; and the receipt's
rows assert "ranks delivered" without printing the ranks (a frozen-
round residual, F5, unrepaired in the committed `.out`). Reword:
"pass, with canonical `D*` values (…) and the `(b, chi)` certificate
computed in-receipt".

---

## Record observations (not paper defects; for the next natural touch)

1. **LOG #342 vs the committed artifact:** #342 records "The D1.3
   cosmetic (the malformed median print -> 512/1037 ~ 0.4937) … applied",
   but the committed d43d receipt still prints the malformed
   `= 8/1037/64` (code line 299; `.out` line 8). The *legacy
   chain-scale print* half of that sentence WAS applied. The paper is
   unaffected (its `512/1037 ~ 49.4%` is the exact decode, performed
   verbatim in the frozen delta review), but the LOG row overstates —
   a correction row is owed by this program's own record-integrity
   standard (the F4 class it convicted one round earlier).
2. d43d NG4 remains `check(True)` (disclosure gate; round-1-disclosed,
   corpus-tolerated) and the NG3 parity conjunct remains the
   star-symmetry identity — both inflate "6/6" slightly; known and
   documented in the frozen round.

---

## V. Number-sweep inventory

Method: every quantitative token in the paper was located in a
committed source (receipt `.out`, receipt source, pin amendment,
frozen review, LOG, or paper 30) and, where a reduction intervenes,
recomputed exactly. Counting matrix/table entries individually,
**~270 items checked; 269 verified; 1 failed** (the §8 margin figure,
B2 — the only quantitative claim in the paper with no committed
source). The scope/wording defects above are catalogued separately;
none involves a wrong number.

| paper section | items (approx.) | outcome |
|---|---|---|
| §1.1 inherited state (36/202, 21/114, six residues, two heads) | 5 | all match paper 30 |
| §2.1 fixture + anchors (L=12, masses, order 12, AN1 entries, `c_lam`, ±1/8, onset exponent, 1e-30) | 14 | all match `.out`/v1 p1/v2 p1 |
| §2.2 orbits {−137/2304, −5/256, +79/2304}, {−7/288, −3/128, +13/576}, {−13/48}, {−11/24}; strip devs 10/13 ~0.77, 5/11 ~0.45; 6 ratios/12 residuals | 16 | all match (decimals verified to 28–50 digits); 6/12 scope flagged (m1) |
| §2.3 kappas −5/384, +79/2304, +19/384, +13/576; SUPPORT-MISMATCH ×2; onset orders; Δ⁸ identity | 9 | all match; d=2 representativeness flagged (m2) |
| §2.4 tau tables (8 channels, both masses), delta-oddness, EXC support, D collapses (EXC 1; +13/2304; −1/72), sign flip | 17 | all match; **kappa(1/2)=13/2304 and kappa(1)=−1/72 independently rederived from the printed tau tables by exact summation** |
| §3.1–3.2 census [1,7,39,215,1191,6471,34375]; 12,942/0; 17/23/29; 14 pure + 3 mixed (3/3/3/3 + 1/1), onto; P_t tables [4,4,5,5,5]/[4,5,6,6]/[4,5,6]; t=2,3,4; six reps; depth-7 179,783 | 42 | all match `.out`/frozen record |
| §3.3 T (36 entries), row sums (2,2,2,5/2,2,2), 215, 5/4-per-actor | 44 | all match; row sums recomputed |
| §3.4 λ=2; u²=1/4; classes {2,4,5}/{0,1,3}; loop 3→0; det 3/32; resolvent rows (8/3,8/3,2/3),(2/3,8/3,2/3),(8/3,8/3,8/3); radius 3/2+(1/32)^{1/3}~1.815; f=(4,4,3,7,3,3)/3; forced (4/3,4/3,7/3); q′ rows=1; conflict {1/7,3/4,3/28}; root=renewal; π=(1,1,2)/4; stationarity | 38 | all match; **charpolys, (2I−M_t)R=I, Tf=2f, forced extension, completed rows, πT=2π, and π·f-stationarity all independently recomputed in Fractions** |
| §3.5 ingredients (12,942/0; 215==215; 144; len≤4) | 5 | all match MG6/NC3 |
| §4 menus 1/3 events, sums 1 vs 5/4; shapes 2×1/4×1; √(1/2); defects 0.0 @1e-40; Born ½–½; reconstruction ¼ and ¼+⅛+⅛; index sets; sizes {1,2}; Born sums 1; control 0.25989318568658958511900962835859379219671226576617 | 17 | all match; menu arithmetic and the control (=1/√2−1/√5) recomputed to 45 digits |
| §5.1 S3 reject; 219; 4,231; [1/4,7/20]; 120; [19/64,25/64]; 4735/14016 ~0.3378; 23595/66368 ~0.3555; 512/1037 ~49.4%; zero pairs/not run | 13 | all match; **512/1037 rederived from the receipt's `below=8`/`wsum=1037/64`** |
| §5.2 D\* 23/64, 1/4, 79/256, 83/400, 1/4, 145/576 (+decimals); widths (2,2,2,3,2,2); 5-of-6 | 14 | all match `.out` |
| §5.3 1/20 (=¼÷5, rederived); W6 preds = S3 (pattern verified); W4 weights (1/12,1/12,1/8,1/8,1/12,1/12) and preds; thresholds 2/3-through-10/4-at-6/6 | 24 | all match `.out`/frozen record |
| §5.4 vacuousness facts | 2 | facts match the frozen delta + #342; provenance tag false (M2) |
| §7 ledger (1/6-vs-0; restated items) | 3 | match paper 30 + terminals; item-7 gloss false (B1) |
| §8 PASS 7/18/11/6; dps 50; 1e-30/1e-40; order 12; seeds; **≥27-digit margin** | 9 | 8 match; **margin figure FAILED** (B2) |

Record-cited claims verified present in the record: the depth-7
confirmation (179,783; still six) — `.out` MG2a label + note-d43b §5
A2 + frozen d43bc review; the 3-actor-through-10-events threshold —
`.out` NG3b label + LOG #337 + frozen d43d review §3.6; the χ0
two-layer collapse — frozen d43a delta + LOG #340; the E-A
distributional strengthening — note-d43c §5 C4 + frozen review; the
vname-vacuousness — frozen d43d delta item 7 + LOG #342.

External references: FLP JACM 32 (1985) 374–382 ✓; Ben-Or PODC 1983,
27–30 ✓; Oreshkov–Costa–Brukner Nat. Commun. 3 (2012) 1092 ✓;
Chiribella–D'Ariano–Perinotti PRA 80 (2009) 022339 ✓; Doob 1984 ✓;
Aldous–Lyons EJP 12 (2007) 1454–1508 ✓; Larsen–Skou Inf. Comput. 94
(1991) 1–28 ✓; Dushnik–Miller Amer. J. Math. 63 (1941) 600–610 ✓;
Hegerfeldt PRD 10 (1974) 3320–3321 ✓. All correctly attributed and
used at the right joints. Internal: v1 p1 line 706 orphan quote
verbatim ✓; v1 p1's ±1/8 worked case (lines 532/1257) ✓; v1 p8's
onset-class contrast sentence verbatim ✓; v2 p1 §5 (the
coefficient-level/continuum identification) and §11 burden 4 ✓;
v8 p12/p13 content ✓ (titles mis-styled — m7).

Voice/style: grep-clean — no correction-round narrative, no
referee/round vocabulary outside the Status line, the §8 generic
"adversarially reviewed" (paper 30 §9.1 precedent), and the
references; negative controls presented as gates (§3.1, §8) exactly
per the discipline. The single-threaded presentation of Q2/Q4 (the
corrected formulations presented as the questions) is the series'
documented convention, not a finding. Provenance-label misuse:
exactly the two items M2 (false "gated") and m3 (missing
record-citation tags); all other [THEOREM]/[EXACT]/[MEASURED]/
[POSITED]/[LITERATURE] tags check out against their sources.

---

## VI. What survives (verified positive content)

- All four decision statements at their terminal scopes, verbatim-
  compatible with the frozen endorsements (#340/#342/#344/#345).
- The §1.3 supersessions: each accurate about what paper 30 says
  (abstract/§5.7/§9 "17 states"; §7.2 null; §6.2 pincer), each
  justified by a gated artifact (NC4 stratification map; NG3b
  witnesses; PG2/PG3 + the horns' channel scoping).
- The §3 chain package end-to-end, independently recomputed: SCCs,
  the full dominant spectrum {1, 3/2, 2}, the M-matrix certificate,
  uniqueness, the completed transfer, root=renewal, mass transport.
- The §2.4 collapse: both kappas rederived from the paper's own tau
  tables by exact summation; the sign-flip no-go's logic (a shared
  `c^2 > 0` generator forces a fixed-sign ratio) checks against v1
  p1 Theorem 3's stated form.
- The §5 threshold structure, including the W6 weight (1/4 over 5
  receivers) and the S3 predecessor pattern, verified structurally.
- §8's determinism claim: all four receipts rerun by this referee,
  exit 0, byte-identical to the committed `.out`s.

## VII. Reproduction appendix

1. **Receipt reruns (this session):** `python3 v10/code/d43a…py`,
   `d43b…py`, `d43c…py`, `d43d…py` from the repo root → all exit 0,
   outputs byte-identical (`diff -q`) to the committed
   `v10/data/*.out`. (PASS counts 7/18/11/6 as the paper states.)
2. **Independent recomputation battery:** scratchpad
   `paper31_referee_probe.py` (exact `Fraction` arithmetic; mpmath
   only to check the `.out` decimal strings) — 43 checks, all green:
   tau→kappa collapses for both masses; 19 decimal↔rational
   identifications at 28–50 digits (orbits, kappas, strip devs 10/13
   and 5/11, tau entries); the full §3 battery (row sums, SCCs,
   charpoly zeros at 1/3/2/2, `(x−3/2)³−1/32` transient charpoly,
   det 3/32, `(2I−M_t)R = I` for the paper's resolvent rows, radius
   <2, `Tf = 2f`, forced extension, completed-row normalization,
   conflict row, `πT = 2π`, exact π·f stationarity); `8/(1037/64) =
   512/1037 ≈ 0.4937`; landscape/family means to 4 decimals; the six
   chain D\* decimals; stratification arithmetic (17 = 14+3; +6 per
   level); W6/W4 weight derivations; the S3 predecessor pattern; the
   d43c menu arithmetic (¼·½ = ⅛; sector ½; full 5/4) and the lossy
   control `1/√2 − 1/√5` to 45 digits; the two candidate margin
   readings (19 and 25.4 digits, both < 27 — the B2 exhibit).
3. **Source inspections:** `d43d…py` full gate census (six gates; no
   vacuousness gate; median print `{below}/{wsum}` at line 299);
   `d43a…py` arithmetic layer (mpc dps-50 series, `TOL = 1e-30`,
   `comm()`'s 1e-45 drop, T5's Fraction-reference-to-mpf gate);
   `d43c…py` `share()`/`BORN`/`reconstruct()` (the §4.3 formula is
   the receipt's own, and the arithmetic closes).
4. **Corpus verification:** v1 p1 (line 706; lines 532/1257), v1 p8
   (lines 28/42–44/284–290), v2 p1 (headings; §5; §11 burden 4),
   v8 p12/p13 (titles, canonical-D\*/rank-embedding content, Theorem
   2.1 two-clock universality), paper 30 (all sections named in §III
   m5 plus the audited abstract/§5.7/§6.2/§7.2/§9/§9.1), LOG
   #327–#346 read in full.

**Disposition.** Not terminal-fit as committed — but close. The two
BLOCKERs and three MAJORs are text-layer defects with one-to-three-
line fixes, none touching a delivered number, a decision, or a scope
sentence; the minor/nit list is likewise wording-local. On those
repairs and a fresh read of §7/§8, this referee expects round 2 to be
a delta, not a re-review. The zero-false-physics-numbers streak
holds; the paper's discipline failure is confined to two glosses and
the methods note's precision sentence — the exact places where prose
outran the receipts.

---

# Delta verification (round 2) — repairs at HEAD 32330f0 (LOG #348)

**Object:** the repaired
`v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md`
(129-line delta over 3da9a63, reviewed hunk-by-hunk from
`git diff 3da9a63 32330f0`); LOG #347/#348. Round-1 body above
untouched. **Method:** every one of the 17 applications located in
the diff and read in final context; leftover-phrase greps over the
repaired paper (zero hits for the convicted wordings); the three
coupling points re-verified (recount arithmetic; the §2.2/§2.3 orbit
cross-pointer against the frozen d43a review's F2 spectra; the §8
precision sentence clause-by-clause against the receipt sources and
`.out`s); the v8 titles compared verbatim against the v8 files' own
header lines; `git diff 3da9a63 32330f0 -- v10/code v10/data`
confirmed EMPTY (no receipt or output touched — round 1's four
byte-identical reruns remain current and no re-execution is needed);
every number inside a changed hunk re-checked against round 1's
verified values.

## VERDICT: DELTA-CLEAN — 17/17 discharged, recount verified,
## 0 new findings above nit (1 nit + 1 zero-action reading note)

## Item-by-item

- **B1 — DISCHARGED.** §7 item 7 now reads "the mass at which the LT
  rule's identified transport operator vanishes at this order (the
  sign flip's guaranteed crossing)", with `kappa(m) = 1` (agreement
  with EXC) explicitly separated as "not established either way by
  the record". Mathematically correct on both halves; matches the
  prescription.
- **B2 — DISCHARGED.** The "≥ 27 digits" figure is gone (grep-clean).
  The replacement §8 sentence is verified clause-by-clause: dps 50 /
  `TOL = 1e-30` / `ORD = 12` (d43a source, lines 26–28); the
  exact-rational values record-confirmed (frozen d43a review: "my
  Fraction rebuild confirms every receipt quantity exactly"); dps 50
  / `1e-40` for d43c with defects `0.0` at working precision (`.out`
  PG3-E1/E2/R4); "the exact-`Fraction` layers behind the gates carry
  no tolerance at all" — true of d43b (all-Fraction), d43c's
  menu/kernel layer, and d43d's exact D\*. (The d43c lossy CONTROL is
  a designed non-zero, outside the "measured defects" clause's scope
  as worded — no conflict.)
- **M1 — DISCHARGED.** §3.5: "the intended induction is exactly
  this: that every deep history is … Assembling the two gated
  identities into that induction is a theorem statement … left open
  here." The conclusion is now conditional content of the named open
  theorem; matches the prescription nearly verbatim.
- **M2 — DISCHARGED.** §5.4 retagged "[EXACT, cited to the committed
  campaign record]" — now provenance-true (frozen d43d delta item 7
  + LOG #342).
- **M3 — DISCHARGED.** §2.1 and §8 both describe the ladder as
  dps-50 series arithmetic at `1e-30` gates with the exact rational
  values confirmed by the frozen round's independent exact-rational
  rebuild; the "[EXACT, values record-confirmed]" qualified tag is
  house style (round-1 §2.1 already carried qualified [EXACT] tags);
  "floating amplitudes only where isometry defects are measured" is
  gone (grep-clean).
- **m1 — DISCHARGED.** "(at `d = 3`: six distinct channel ratios;
  twelve LT residual entries outside the basis)" — correctly scoped
  to the frozen review F3(iii) computation.
- **m2 — DISCHARGED.** The §2.3 parenthetical labels the d = 2
  kappas "deterministic max-orbit representatives" and points to
  "the §2.2 table's" orbits — the §2.2 table does carry exactly the
  two full d = 2 max-orbit spectra. See the reading note below on
  the d = 1 clause (verified correct; zero action).
- **m3 — DISCHARGED.** "(the second layer per the frozen review
  record)" on the two-derivative-layers clause; "[THEOREM at fixture
  scale, per the frozen review record]" on the `E^LT[Delta^8]`
  identity. Both provenance-true (frozen d43a review F1 + delta χ0
  section; LOG #340).
- **m4 + m5 — DISCHARGED, RECOUNT VERIFIED.** §1.3's intro says
  "five statements" and the list has exactly five items (counted):
  (1) §5.7/§9 17-states; (2) §7.2 pilot null; (3) §6.2 pincer scope;
  (4) §8.3 premise — with "the conclusion (no continuum claim)
  stands with its premise updated", accurate against paper 30 §8.3's
  actual text; (5) §7.2 depth axis — accurate (width ≥ 4 at six
  events; width ≤ 2 never). §6 reconciles: two scaffolding
  supersessions (§3, §5) + three scope sharpenings named
  individually, "All five are stated in §1.3 and gated in the
  receipts" — the gate mapping checks: NC4 (item 1), NG3b (item 2),
  PG2 + PG3 (item 3), PG3-E1..E5 (item 4), NG3 widths + NG3b
  (item 5). The deviation from round-1's m4 one-liner is exactly the
  m5 interaction and is the better resolution.
- **m6 — DISCHARGED at all three sites.** Abstract: "a minimum-size
  order of dimension 3"; §5.3: "the standard minimal example of
  dimension 3 (minimum size; not unique at six elements — `W4` below
  is a second)"; §6: "the standard minimal example of dimension 3".
  All correct (and the W4-as-second-witness clause is
  receipt-consistent). One trailing residual: D-n1 below.
- **m7 — DISCHARGED.** Both v8 titles now verbatim — compared
  character-for-character against the v8 files' own header lines
  ("The 2D sufficiency theorem: a canonical realizer, the rank
  embedding, and an intrinsic quantitative characterization of
  volume-faithful record orders"; "Do records measure positive? The
  two-clock frame, the natural-supply sweep, and the Gibbs
  reconnaissance"), with the Theorem-2.1 gloss accurate.
- **m8 — DISCHARGED.** Abstract: "with the EXC constant exactly 1 at
  both masses and one per-mass LT constant: …" — correct.
- **n1 — DISCHARGED.** "the d43b/d43c pair additionally verified
  byte-identical across hash seeds 0/7/11/61" — matches LOG #344.
- **n2 — DISCHARGED.** The coda now reads "nearest open surface" and
  enumerates the arbitration-alone dimension question,
  transport-scope invariance, and the standing empirical/breadth
  items — consistent with the paper's own §7 ledger.
- **n3 — DISCHARGED.** "the nonzero shifted eigenvalues … satisfy
  `u^2 = 1/4` (the full dominant-class spectrum is `{1, 3/2, 2}`)" —
  the spectrum was verified exactly in round 1's probe (charpoly
  zeros at 1, 3/2, 2).
- **n4 — DISCHARGED.** §5.2: "with the `(b, chi)` two-clock
  certificate computed in-receipt and exact canonical `D*` values
  (…)" — "computed in-receipt" is exactly right (the ranks are
  computed; the `.out` does not print them — the known frozen-round
  residual on the terminal receipt, not the paper's to repair).

## Coupling spot-checks (commissioned)

All three clean; no adjacent number or cross-reference broken.
Numbers inside changed hunks re-verified against round-1 values:
the abstract kappas, `1/20`, the §2.3 table (untouched), the §5.2
D\* list (untouched), the W6/W4 data (untouched), seeds 0/7/11/61,
`{1, 3/2, 2}`, the five-count, and the §8 PASS table (untouched).
Leftover-phrase grep over the repaired paper: zero hits for "27
digits", "the two chain receipts", "[EXACT, gated]", "agree to this
order", "three statements", "first order that breaks", "floating
amplitudes only", "the minimal order of dimension", "exact rational
coefficients".

## Record observations — disposition ENDORSED

LOG #348's forward-correction of #342 states the facts exactly (only
the chain-scale half of D1.3 was applied; the committed print stands
and decodes as `below = 8 / wsum = 1037/64 = 512/1037`), assigns the
cosmetic print repair to D44c's natural touch of the d43d machinery,
and notes NG4's `check(True)` status. **This referee agrees with
leaving the terminal d43d receipt untouched**: the defect is
cosmetic, its decode is unambiguous and now on the record, and
re-opening a frozen terminal receipt for a print string would trade
a real discipline (the freeze) for a nil one — the round-1
classification ("for the next natural touch") is honored precisely.

## Residuals (non-blocking)

- **D-n1 — nit (the only new finding):** §5.3's W6 bullet still ends
  "realizes the first non-two-dimensional order" — the "first"
  phrasing class of m6, at a site round 1 did not list. It is now
  disambiguated by the new "(minimum size; not unique at six
  elements — `W4` below is a second)" parenthetical one line above,
  so it reads as first-by-size; optional one-word polish ("a
  minimum-size non-two-dimensional order") at the next natural
  touch. Not blocking.
- **D-note — zero action (reading verified):** §2.3's "the `d = 1`
  orbits are single-ratio" is correct in the passage's own sense —
  "orbit" throughout §2.2–2.3 is the maximal-magnitude entry orbit
  (the §2.2 table's column header defines it), and the d = 1 max
  orbits are single-ratio (frozen review F2). The FULL d = 1 ratio
  spectra have 5 classes — a different object, not the one named.
  Recorded so no future reader mistakes the clause for a
  full-spectrum claim.

## Terminal endorsement

**DELTA-CLEAN.** All 17 round-1 findings are correctly discharged;
the supersession recount (5 = 2 scaffolding + 3 sharpenings) is
verified against both §1.3 and §6; the applications introduced
nothing above nit; no receipt, output, or delivered number changed.
Per the stamped terminal condition, **paper 31 converts to terminal**
as: "EXACT-RECEIPT PAPER at the declared finite scope; independent
paper-level review: round 1 + delta, frozen at
`reviews/paper31-round1-hostile-review.md`." The
zero-false-physics-numbers record now extends through the paper and
its repair.
