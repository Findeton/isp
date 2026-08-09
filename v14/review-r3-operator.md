# R3 — HOSTILE REVIEW, REVIEWER R1 (OPERATOR LENS)

**Object:** the frozen R3 delivery — paper `00850cc796d0`, code `bbcc9a1aa7de`,
output `d54142292980`, receipt `1c8beb16c8a2`.  All four verified at the start
of the run and again at the end; unchanged.
**Protocol:** `v14/note-r3-hostile-protocol.md` (`c575340216fc`), K1–K5 binding.
**Pin:** `v14/note-r3-relativity-pin.md` (`a2ac89687a65`).
**Pinned sources verified:** `v13/code/ha_successor_receipt.json` `542b8735daf0`,
`v13/paper-ha-successor.md` `f286ba10d2d9`, `v13/code/ha_successor_exact.py`
`d44cb72f8ee9`, `v14/code/r2_manifold_receipt.json` `08b2140f46ae`.
**Method:** a from-scratch reconstruction of the whole unit with different
primitives throughout — sites as integer indices in mixed radix (the unit uses
coordinate tuples keying dicts); fields as flat lists; exact arithmetic carried
as (integer matrix, common denominator) pairs and, in the bracket layer, as
integers in units of `1/Dg` (the unit uses per-site `Fraction` fields); the
record readout solved by my own Gaussian elimination AND by the closed form,
with the inverse taken by **adjugate/determinant** rather than Gauss–Jordan;
the coefficient system solved **collect-rank-solve-then-verify-every-equation**
rather than by the unit's streaming incremental row reduction; the bracket
literal composition rebuilt from the map definitions.  Nothing was imported
from the unit and the unit was never executed.

**GRADE: ACCEPT-WITH-FIXES.**

**Recomputations: 37,312** delivered or derived quantities independently
recomputed and compared, resting on ~1.03 M exact-rational evaluations, plus
five censuses the delivery does not contain (460 spanning ranks; a 27-member
realisation census over 73,872 bracket classifications; 2,616 non-constant
tangential brackets; a third L point, 40 cells; 238 other-order defect rows).

---

## 0. What reproduced

Byte-for-byte against the receipt, from the independent rebuild:

| object | cells | result |
|---|---|---|
| closure census rows (8 fields each) | 476 | **0 mismatches** |
| coefficient rows (class, constant, metric_reading, statuses, ranks, value, distinct) | 476 | **0 mismatches** (one cosmetic: I omit `distinct_values` on NOT-EXTRACTABLE) |
| coefficient class census | — | `{CONSTANT-NON-METRIC 216, METRIC-READING-CONSTANT 108, METRIC-READING-SITE-VARYING 32, NOT-EXTRACTABLE 36, SITE-VARYING-NON-METRIC 48, ZERO 36}` |
| `{D,H}` bracket rows / classifications | 476 / 21 012 | **0 mismatches**; `D-REG/IDENTITY 10506, D-TOT/IDENTITY 120, D-TOT/OUTSIDE 10386`, IN-CONSTRAINT 0 |
| `{D,D}` rows / brackets | 56 / 644 | **644 of 644 close** |
| defect rows (probes, vanishing, lattice-sum-zero, max_abs) | 238 / 3 096 | **0 mismatches**; 0 vanishing, 0 lattice-sum-zero, 0 of 2 280 homogeneous |
| defect closed form vs my own literal 4-map composition | 3 096 | **0 disagreements** |
| convention sweep rows | 16 | **0 mismatches**; 1 of 4 exact |
| I7 recovery: pinned closure table | 99 | **0 mismatches** |
| I7 recovery: pinned sector law | 72 | **0 mismatches** |
| I7 recovery: rank, readout (det 2, 81 sites), general-d, count lattice (361/5100/781), diagonal sector (5 records) | — | all match the pin |
| L-gate overlap fractions | 6 rows | 36/36, 64/120, 100/300, 324/351, 768/2016, 1500/7750 |
| chart-group orders | 4 | 32, 50, 384, 750 = \|X\|·d! |
| equivariance / scrambled | 8 rows | 120 969 of 120 969; scrambled violates 58 572 |
| L-sweep trajectory (7 fields × 8 rows) | 56 | **0 mismatches** |
| lapse-enlargement magnitude moves | — | 62 (all strictly upward, 0 downward), class moves 0, closure moves 0 |

**Every headline number in the paper reproduces exactly.**  I found no false
numerical result anywhere in the unit.  The findings below are about what the
numbers are claimed to *mean*, about two gates, and about one control that does
not exist.

---

## 1. THE DERIVABILITY THEOREM (K1c), stated and checked

**Setting.** Fix an arena `(d,L)` and a lapse scope.  At each site `x` write

* `W(x) ∈ Q^{d×|L|}` — the rule's declared drag matrix: `W^{ij} = Λ^{ij}` on the
  `d` axis columns and `0` on the `C(d,2)` diagonal columns for architecture A;
  `W ≡ 0` for `A-notransport` (the frozen front makes the normal steps commute);
  `W^{iℓ} = λ_ℓ e_ℓ^i` for architecture B;
* `B(x)` — the record's metric matrix: `B^{ij} = (q(x)^{-1})^{ij}` on the axis
  columns, `0` on the diagonal columns;
* `Ω_ℓ(x) = N(x)M(x+ℓ) − M(x)N(x+ℓ)` — the declared bracket covector.

**MEASURED HYPOTHESIS (S).**  At every site of every censused arena and both
lapse scopes, the realised `Ω(x)` **span the full `|L|`-dimensional link space**
(3 at d=2, 6 at d=3), and a fortiori their axis parts span `Q^d`.
*Measured here: 460 of 460 sites over all 8 arena–scopes, minimum rank = |L| in
every one.*  **The delivery does not measure this** — it records only the axis
rank (2 or 3) per coefficient row.

**Theorem.** Under (S), for every census cell:

1. the commutator's normal channel is empty and its register displacement is
   `Δ(x) = W(x)Ω(x)`  *(this is X01: linearity of `w[N,·]` in the front)*;
2. the census residual is `ρ = Δ − β = (W−B)Ω` — **HA's own closed form
   `ρ = (Λ−I)ω` extended from the axis covectors to the full link space** — and
   `CLOSES ⟺ W ≡ B`;
3. the coefficient system `Δ^i = Σ_j c^{ij} ω_j` is **consistent ⟺ W's
   diagonal-link columns vanish**; when consistent, the solution is unique and
   equals the axis block of `W`;
4. hence the coefficient class is the pure function

   ```
   NOT-EXTRACTABLE              ⟸ W has a nonzero diagonal-link column
   ZERO                         ⟸ W = 0
   METRIC-READING-{C,SV}        ⟸ axis(W) ≡ q^{-1} at every site
   {CONSTANT,SITE-VARYING}-NON-METRIC   otherwise
   ```
   with `CONSTANT ⟺ axis(W)` the same matrix at every site — **a function of
   (the rule's weight field, the record's readout) alone, containing no
   commutator, no lapse and no bracket**;
5. `CLOSES ⟺ class ∈ {METRIC-READING-CONSTANT, METRIC-READING-SITE-VARYING}`.

**CHECK (mine).**  I evaluated the right-hand sides of (2) and (4) with no
commutator anywhere and compared against my rebuilt census at all 476 cells:
**0 class mispredictions, 0 closure mispredictions.**  Independently,
`closes ⟺ metric_reading` at **476 of 476** cells, and `closing_cells = 140 =
metric_reading_cells` in the delivery's own summary.

**WHAT REMAINS MEASURED after the theorem:**

* **(a)** hypothesis (S) itself — the full-link-space spanning at 460 sites.
  This is the load-bearing measurement of the whole `{H,H}` half, and it is the
  one thing not in the receipt.
* **(b)** the sector arithmetic "at which sites does *this* weight equal *this*
  record's `q^{-1}`" — I7's own sector law, re-run at `L ∈ {4,5}`, `d ∈ {2,3}`
  (and reproduced against the pin at 99+72 cells with 0 mismatches).
* **(c)** the residual **magnitudes** `max|ρ|` (9, 16, 8, 27, 128/9, 48) and the
  62 lapse-enlargement magnitude moves — genuinely `L`- and scope-dependent.
* **(d)** the entire `{D,H}` bracket and the defect — untouched by the theorem.
* **(e)** the literal four-map composition agreeing with the closed form
  (21 420 + 3 096 cells; I independently reproduced the defect leg at 3 096/3 096
  with 0 disagreements).

Everything else in the `{H,H}` half — the 476-of-476 landing, the 140 closing
cells, the six class counts, 56/56, 32/120, the 36 NOT-EXTRACTABLE, the
`L`-constancy and the scope-inertness — is a **corollary** of (S) plus the
declared weights and records.  This is the R2/R6a pattern, and the unit should
carry it as such.

---

## MAJOR

### M1 — `G-CONVENTION-RULE-INDEPENDENT` is vacuous by construction, and is cited as compliance evidence (recurrence of the #219 / #20 vacuity class)

**Evidence.**  `r3_relativity_exact.py:2954–2960`.  The gate's condition is

```
all(c["brackets"] % (len(rules_at(c["d"], decl))) == 0 for c in res["conventions"])
```

and `c["brackets"]` is constructed thirty lines earlier (line 1938) as
`len(base) * len(tgens) * len(adm) * len(rules)`.  Divisibility by `len(rules)`
is therefore an **identity**: the comparator cannot disagree with the object
under test.  No per-rule row exists to be compared, because the sweep is
computed once, at `rec0 = recs[adm[0]]` (line 1924), and then multiplied.  The
`convention-sweep-truncate` mutant perturbs `front_matches`, not `brackets`, so
no declared falsifier can reach this gate.

**Two aggravations.**
1. The gate is in the never-falsified list with the waiver *"FORCED (#208): the
   bracket's front sector contains no drag weight, so the per-rule rows cannot
   differ"*.  The waiver names only the **rule** factor.  The code also
   multiplies by `len(adm)` — the **record** factor, ×9 at d=2 and ×5 at d=3 —
   and record-independence is neither stated in the gate nor machine-checked
   anywhere.  Under the #34 engraving (waiver claims are gate claims; a named
   forcing must be machine-checked) the waiver is incomplete.
2. The compliance sweep row
   `{"rule": "208 forced clauses are disclosures, not findings", "evidence":
   "G-FORCED-CLAUSES-DISCLOSED,G-CONVENTION-RULE-INDEPENDENT"}` cites the
   vacuous gate as its evidence — the #20 engraving's own disease at the gate
   that is supposed to certify #208.

**Measured consequence.**  The four convention rows report `21126` as the
denominator.  The number of **distinct front-sector evaluations actually
performed** per (order, convention) is **685** — I measured it: 26 hits for each
of the three failing combinations, 685 for the winner.  The delivered
denominator is inflated **30.8×** by a pure multiplication.  Paper §5 renders it
as *"at every bracket in the census"*; note also `21126 ≠ 21012`, so "the
census" in that sentence is a third denominator.

**The substance is correct.**  My reconstruction builds the front sector from
`(N, v, L)` alone — no record, no rule anywhere in the computation — and
reproduces `1152 / 1152 / 21126 / 1152` exactly, confirming 1-of-4.

**Repair (exact).**  (i) Replace the divisibility check with a real comparison:
evaluate `front` and `L_vN` at ≥2 rules × ≥2 records per arena and require
equality (16 extra evaluations total), and ship an injection-falsifier that
perturbs one side.  (ii) Restate the waiver to name **both** forcings.
(iii) Either report `685` as the measured denominator with the multiplicity
disclosed, or keep `21126` and label it `DERIVED-BY-MULTIPLICATION` in the
receipt row, the verdict segment and §5.

### M2 — The defect's *outside-the-basis* status is REALISATION-RELATIVE, and the absorbing realisation is expressible from the pinned declarations (K2)

The unit censuses two tangential realisations.  I censused **all 27** built from
the *same two declared atoms* — the declared site map `x ↦ x+v(x)` and the
declared address register — as `(a,b,c) ∈ {−1,0,1}³`:
`a` = front drag, `b` = register shift, `c` = register transport **along the same
declared site map**.  `D-REG = (0,1,0)`, `D-TOT = (1,1,0)`.  Transporting the
register along the very site map that already transports the front introduces no
new ingredient; if anything it is the *less* arbitrary of the two, since D-TOT
moves the front but leaves the register's site-labelling behind.

**Measured (all three arenas run: d2L4, d2L5, d3L4; 73 872 classifications):**

| realisation | d2L4 tally | d3L4 tally | defect field nonzero |
|---|---|---|---|
| `(0,1,0)` **D-REG** | IDENTITY 1188 | IDENTITY 360 | 0 / 1188 |
| `(1,1,0)` **D-TOT** | OUTSIDE 1188 | OUTSIDE 360 | 1188 / 1188 |
| `(1,1,1)` register transported | **IN-EXTENDED 972**, OUTSIDE 216 | **IN-EXTENDED 270**, OUTSIDE 90 | 1188 / 1188 |
| `(1,0,1)`, `(1,−1,1)`, `(−1,b,−1)` | IN-EXTENDED 972, OUTSIDE 216 | IN-EXTENDED 270, OUTSIDE 90 | 1188 / 1188 |
| the other 20 | IDENTITY or OUTSIDE only | — | 0 or 1188 |

`IN-EXTENDED` is **the unit's own class** (`dh_membership`, line 1439): *the
bracket equals `H[P]·D[u]` for a configuration-independent tangential field `u`*
— i.e. **inside the declared generator basis extended by a fixed `D-REG`
factor**.  The unit reports it at 0 cells because it only ever asks two
realisations.  At `(1,1,1)` it fires at **81.8 %** of the same brackets, with
the **front sector unchanged** (the front action is identical for `a=1`
regardless of `c`), so the absorbing realisation keeps all of the good news.

**Which cells resist, measured.**  At d=2 L=4 the 216 OUTSIDE cells are exactly
the 18 inhomogeneous `(rule, record)` pairs whose weight is count-sensitive:
every `G-CURVED`/`G-CURVOFF` pair except the two count-blind rules `A-chart`
and `B-chart`.  **Every homogeneous record, at every declared rule, is
IN-EXTENDED.**  At d=3 L=4 the 90 OUTSIDE cells sit entirely on
`G3-CURVED`/`G3-CURVOFF`.

**Consequences for the delivered text.**
* Paper §6 — *"The defect therefore lies **outside the declared generator
  basis**, which is the precise sense in which the algebra does not close"* — is
  true at D-TOT and **false at `(1,1,1)` on the entire homogeneous sector**.
* Paper §6 — *"It has no vanishing sector… The defect is a statement about
  **transport**, not about curvature"* — survives at the **field** level (the
  defect field is nonzero at 100 % of probes for all 18 of the 27 realisations
  that drag the front) but **inverts at the membership level**: the sector that
  resists absorption is exactly the curved sector.
* Paper §11's *"The tangential realisation is a named verdict coordinate…
  Neither is a bookkeeping choice, and the unit reports both"* — the coordinate
  has ≥3 declared-expressible values, and the third one changes the verdict
  segment.

**What survives the census — and it is the strongest object in the unit.**
`IN-CONSTRAINT` is reached at **0 of 73 872** classifications across all 27
realisations and 3 arenas.  `{D[v],H[N]} = H[L_vN]` is realised by **no**
declared-expressible tangential realisation.  The DEFECT head is
realisation-**independent**; only the *outside-the-basis* characterisation is
realisation-relative.

**Repair (exact).**  Run the `(a,b,c)` enumeration as the R6a-style
realisation census (it costs seconds); publish the `(1,1,1)` row; rewrite §6,
§9(3) and the `DEFECT=` / `REALISATION=` verdict segments to:

> outside the declared generator basis at D-TOT; at the register-transporting
> realisation the bracket lies in the **extended** basis on every homogeneous
> record and outside it exactly on the inhomogeneous ones; `IN-CONSTRAINT` is
> realised at no declared-expressible realisation (0 of 73 872).

---

## MODERATE

### D1 — The `arch-B` characterisation of the 36 NOT-EXTRACTABLE cells is FALSE

It appears in paper §4, in disclosure **X05**, in the emitted verdict
(`NOT-EXTRACTABLE-AT-36-CELLS(ARCH-B:OUTSIDE-THE-AXIS-COVECTOR-FORM,FORCED)`)
and in `G-COEFFICIENT-EXTRACTION`'s statement.

**Measured (independently, by my own solve).**  NOT-EXTRACTABLE is exactly the
rule `B-all` — 36 cells = 1 rule × 9 records × 4 arena-scopes.  The other two
architecture-B rules are extractable at **all 72** of their cells:

* `B-axis`: METRIC-READING-CONSTANT 16, METRIC-READING-SITE-VARYING 4,
  SITE-VARYING-NON-METRIC 4, CONSTANT-NON-METRIC 12;
* `B-chart`: CONSTANT-NON-METRIC 32, METRIC-READING-CONSTANT 4.

**Why.**  `B-axis` (`λ_ℓ = 1/n_ℓ` on the axis links **only**) and `B-chart`
(`λ_ℓ = 1` on the axis links **only**) put zero weight on the diagonal links, so
`W`'s diagonal columns vanish and the displacement is exactly of the axis-covector
form.  Only `B-all` (`λ_ℓ = 1/n_ℓ` on **every** link) carries diagonal-link
brackets.  This is Theorem (3) above, and it is also what HA already records
("`B-axis` reproduces `A-axis` and `B-chart` reproduces `A-chart`").
The count 36 is right; the "exactly" and the causal clause are wrong.

The gate does not catch it because it never tests the clause it states: its
condition is `not_extractable_cells > 0 and positive_control_metric_reading ==
positive_control_cells` — a threshold plus the X03 tautology.

**Repair.**  Replace "the architecture-B rules" with "the rule `B-all` — the
only declared rule carrying weight on the diagonal links" in §4, X05, the verdict
segment and the gate statement; and change the gate condition to test the iff
(`extractable ⟺ the drag matrix's diagonal-link columns vanish`) over all 476
cells, with a mutant that flips a diagonal column.

### D2 — X03 overstates what is measured: the site-variation class at the positive control is forced too (K1d)

By Theorem (4), for `A-insert` the extracted coefficient is `Λ = q^{-1}` by
declaration, so `metric_reading` is an identity, and CONSTANT vs SITE-VARYING is
the question *"is `q^{-1}` the same at every site"* — i.e. *"is the record's count
field constant"*.  That is a property of the **arena**, with no bracket, no
solve and no algebra in it.

**Demonstrated, not argued.**  I built three inhomogeneous records that appear
in no declaration anywhere in the corpus (`SYN-A`: `n_ℓ = Σ_{j∈ℓ}(3+2x_j)`;
`SYN-B`: `Σ(5 + x_j² mod 4)`; `SYN-C`: `Σ(7+x_0+2x_1)`) and ran the full
extraction and typing at d=2, L=4.  All three: `A-insert` →
**METRIC-READING-SITE-VARYING**, **closes**.  Any inhomogeneous admissible
record forces it.

**The 32/120 decomposed (measured).**

| contribution | cells | status |
|---|---|---|
| `A-insert` (the metric-inserted positive control) | 16 | value forced (X03) **and class forced** (record inhomogeneity) |
| `A-axis` (8), `A-insert-x` (4), `B-axis` (4) — **all on `G-CURVED`/`G3-CURVED` only** | 16 | I7's diagonal-sector theorem: on a diagonal record `diag(1/n_{e_j}) ≡ q^{-1}` |

On the genuinely **off-diagonal** inhomogeneous record (`G-CURVOFF` /
`G3-CURVOFF`) the only rule with a site-varying metric coefficient is the one
that has the metric inserted by declaration.  **There is no cell in the census
where a rule that does not already contain the metric produces a site-varying
metric coefficient on an off-diagonal record.**  That is the honest scope of
"the programme's first relativity-shaped statement about the record layer".

**Robustness (in the unit's favour):** 32/120 is identical at all four arenas
and both lapse scopes, and I reproduced the same class census at a fifth arena
(d=3, L=3) the unit excludes.

**Repair.**  X03 → "*forced:* `metric_reading` **and** the site-variation class
at the positive control; *measured:* the uniqueness of the solve (the full-rank
spanning, hypothesis (S)) and the class census at the rules that do **not**
insert the metric."  §4 / §9(1) / §11 should carry the 16 + 16 split and the
diagonal-sector caveat.

### D3 — The boundary test's "degenerate probe" does not exist; the receipt field is a typed literal

`r3_relativity_exact.py:2991` emits `"degenerate_probe_sums_to_zero": True` as a
hard-coded constant.  The gate's condition (2987–2988) is
`S["defect_lattice_sum_zero"] < S["defect_probes"] and S["defect_probes"] > 0`
and evaluates **no degenerate probe at all**.  `grep -n "degenerate"` over the
instrument returns exactly those two lines.  No zero-field probe is in the
defect probe set (the first six declared lapses × the `d` translation
generators), and `vanishing_probes = 0` confirms none arises.

Paper §6 renders it as a measured fact — *"The degenerate probe — the zero
field, which does sum to zero — is carried alongside as the test's own death
certificate, so the boundary test is not vacuous"* — and §12 asserts *"Every
count is computed, never typed."*  Both fail on this row.  This is the class the
#20 and #34 engravings cover: a claimed control that has no computation behind
it.

**The substance is salvageable.**  The gate has a real declared falsifier —
`boundary-lax` (line 2061) subtracts the lattice total from one site, driving
`lattice_sum_zero` to 3 096 and killing the gate — so non-vacuity *is*
established, by a mutant rather than by a probe.

**Repair (exact).**  Either (i) add a genuine degenerate probe and count it: the
**constant lapse `N ≡ 1`** gives `front = S_vN − N ≡ 0` and `shifted ≡ 0`, hence
a defect field identically zero with lattice sum zero — computed, counted and
reported as its own row (I confirmed the constant profile is *not* in the d=2
defect probe set, so this is a real addition); or (ii) delete the sentence and
the receipt field and cite `boundary-lax` as the death certificate.

### D4 — `62 of 476` uses a pair-count numerator against a cell-count denominator

The lapse-enlargement comparison is between the BASE and TRANSLATES versions of
the *same* (arena, rule, record) cell; there are **238** such comparisons.
`receipt.summary.lapse_coordinate_moves` holds exactly 62 entries, each a
`(d, L, rule, record)` 4-tuple.  My recomputation: **62 of 238** comparisons move
the residual magnitude, **all 62 strictly upward** (0 decreases), 0 move the
closure status, 0 move the coefficient class.

**Repair.**  §8 → "moves the residual **magnitude** at 62 of the 238 (arena,
rule, record) cells compared across the two lapse scopes — always upward".

### D5 — The lapse-scope inertness is FORCED by a quantity the unit needs but never measures

Hypothesis (S) — the full-link-space spanning of the realised bracket covectors —
holds at **460 of 460 sites** across all 8 arena–scopes (measured here; minimum
rank `|L|` everywhere).  The unit records only the axis rank.

Given full spanning **already at BASE**, enlarging the lapse family cannot change
the closure verdict (equivalent to `W ≡ B` by Theorem (2)) nor the coefficient
(already uniquely determined by Theorem (3)).  So *"moves no cell's closure
status and no cell's coefficient class (0 moved)"* is a **theorem**, not an
independent measurement; only the 62 magnitude moves are measured content.  §8
presents the two side by side as symmetric measurements ("measured on both
counts, which is why it is carried as a named verdict coordinate rather than a
convention").

**Repair.**  Compute and report the full-link span (8 small rank computations),
state the corollary, and mark the `0 moved` clause `FORCED` in the `LAPSE=`
verdict segment.

---

## MINOR

**m1 — The L-sweep table's `closing` and `metric-reading` columns are the same
column.**  Measured: `closes ⟺ metric_reading` at **476 of 476** cells, 0
exceptions; the summary's `closing_cells = 140 = metric_reading_cells`.  §8
prints 26 / 26 and 9 / 9 as two census outcomes.  *Repair:* state the
equivalence — it is the cleanest sentence available in the unit ("on this
substrate, closure **is** the metric-reading condition") — and drop or derive
one column.

**m2 — The excluded d=3, L=3 arena passes the inherited criterion, and it is
free evidence.**  The receipt's own `l_gate` row reads `complete=False,
meets_r2_criterion=True, censused=False`, yet §2 justifies the exclusion with a
d=2-only fact.  I ran the excluded arena: **closing 9 of 20 at both lapse
scopes**, class census `{CONSTANT-NON-METRIC 8, METRIC-READING-CONSTANT 6,
METRIC-READING-SITE-VARYING 3, SITE-VARYING-NON-METRIC 3}`, axis rank 3
everywhere — **0 differences from d=3, L=4**.  A third point on the refinement
direction, obtained in under a second, which the unit's own L-stability claim
would be strengthened by.  *Repair:* one sentence in §2 noting that d=3, L=3
passes and is excluded only because R2's handoff gates `L ≥ 4` uniformly;
optionally add the row.

**m3 — #219 residual at the coefficient-typing comparator.**
`type_coefficient` types against `inv_exact(q_from_counts_closed(...))` while the
audited object (`A-insert`'s `Λ`) is `inv_exact(q_from_counts(...))`: the readout
*is* independently re-encoded, but the **inversion primitive is shared**, and at
the positive control the comparison degenerates to "do the two readout routes
agree" — which `G-RECORD-IS-METRIC-TWO-ROUTES` already forbids from
disagreeing, at exactly the 56 cells the headline leans on.  I re-ran the entire
typing with an **adjugate/determinant** inverse (a different algorithm) and got
all 476 classes identical, so nothing is hiding there.  *Repair:* type against a
second inversion algorithm, or add a per-site `Λ·q = I` residual check.

**m4 — `G-LSWEEP-STABILITY` does not test what it states.**  Its statement says
"the coefficient-class census [is] constant in L"; its condition tests only the
tuple `(d, closing, cells, metric_reading)`.  `site_varying_metric` and
`not_extractable` are in the trajectory rows and in §8's table but not in the
tested tuple.  (They are in fact constant — I checked.)  *Repair:* put the whole
class census in the tuple.

**m5 — The residual-covariance non-vacuity count is a 16× multiple.**
`translation_covariance_of_the_residual` recomputes `r0`, which does not depend
on the translation `u`, inside the `u` loop and increments `nonzero` each pass;
so "non-vacuity: 128 nonzero base cells" is **8 distinct** nonzero base cells
counted once per translation.  Harmless as a `>0` witness; the number does not
mean what it reads as.

---

## NOTES

**n1 (in R3's favour, new).**  The defect also never vanishes at the **other
bracket order** — `H-D-Hinv-Dinv`, the order whose front sector *does* reproduce
`L_vN` under the declared backward convention: **0 of 3 096** probes vanish.
The unit measures the defect only at `D-H-Dinv-Hinv`; the order is not
load-bearing, and saying so would close an obvious line of attack.

**n2 (in R3's favour, new).**  The restriction to constant tangential fields is
**not** load-bearing for the defect (K4's bijection-constraint flag).  I ran two
non-constant bijective `v` fields — a shear `v(x) = (x_1,0,…)` and a parity kick
`v(x) = (x_1 mod 2, 0,…)` — through the literal composition: the bracket is
OUTSIDE and the defect nonzero at **594/594** (d2L4), **495/594** (d2L5),
**120/120** (d3L4).  The defect is not an artefact of translations.

**n3.**  The three failing convention combinations all score exactly 1152
because their conditions coincide on this lapse family: `f = 0` (constant along
`e_j`), zero second difference, and 2-periodicity all select the same 4
`(N, tgen)` pairs at d=2 and 9 at d=3 for `L ∈ {4,5} > 2`.  The identical triple
is structural, not coincidental, and could be stated in one clause.

**n4.**  The `{D,D}` control is forced not only at the two declared realisations
(X04) but at all 27 in my census; it discriminates nothing except the
`commutator-machinery` mutant, exactly as X04 says.  Correctly handled.

**n5.**  The 21 012 `{D,H}` denominator is dominated by d=2 (18 612 of 21 012);
the d=3 evidence for that verdict is 2 400 brackets under X07's probe
convention.  Honest and printed; worth a clause in §5 so the reader does not
read "21 012" as balanced across dimension.

---

## K1–K5 ADJUDICATIONS

**K1 (DECISIVE).**
* **(a) Well-posedness / over-determination.** The solve is well-posed and unique
  wherever (S) holds; my collect-rank-solve-then-verify algorithm (structurally
  different from the unit's streaming elimination) reproduces all 476 statuses,
  ranks and values.  But by Theorem (3) the over-determination is a real
  existence test **only against `B-all`**: architecture A cannot fail it.
  Existence is therefore a genuine but analytically predictable test.
* **(b) Comparator independence (#219).** PARTIAL — see **m3**.  The readout is
  independently re-encoded; the inversion primitive is shared; at the positive
  control the comparison collapses onto a route agreement another gate already
  forces.  Re-typed with a different inverse: no error found.
* **(c) Are the coefficient classes themselves forced?**  **YES — derivable.**
  The theorem is stated and checked at all 476 cells above (0 mispredictions).
  What remains measured is (a)–(e) of §1, of which the load-bearing item —
  hypothesis (S), the full-link-space spanning — **is not in the delivery**.
* **(d) Is SITE-VARYING a real algebra property?**  **NO at the positive control
  — trivially inherited from record inhomogeneity** (demonstrated on three
  never-declared records), and elsewhere inherited from I7's diagonal sector.
  32/120 is robust across arenas, lapse scopes and a fifth arena, but it is not
  an algebra discovery.  See **D2** for the 16 + 16 decomposition and the
  off-diagonal null result.

**K2.**  **The defect survives as a FIELD; it does not survive as a
basis-membership claim.**  A 27-member census of declared-expressible
realisations (M2) shows: the defect field is nonzero at 100 % of probes for all
18 realisations that drag the front; but the OUTSIDE classification is
realisation-relative, and `(1,1,1)` — D-TOT with the register transported along
the same declared site map — moves 81.8 % of the brackets into the unit's own
`IN-EXTENDED` class, resisting exactly on the inhomogeneous records.  All other
K2 sub-checks confirmed independently: the closed form verified against my own
literal composition at 3 096/3 096 (0 disagreements); the lattice sum nonzero at
3 096/3 096 (but the degenerate probe does not exist — **D3**); 0 of 2 280
homogeneous probes vanish at field level; `L`/`d`-independence confirmed at four
arenas plus a fifth I added; the 1-of-4 convention exactness confirmed
independently (with the **M1** denominator caveat).  **The honest verdict
segment changes** — repair given in M2.

**K3 (adjudicated from my data).**  The distinguishing test *is* available and
*is* run: "the discrete HDA" requires `{D,H}` to close into the constraint
family, and it does so at **0 of 21 012** brackets and at **0 of 73 872**
classifications over the full realisation census.  What the unit possesses is
one bracket with metric coefficients, and by Theorem (4) those coefficients are
**the rule's own declared weight field** — so "a deformation algebra with metric
coefficients" is precisely what has been measured, with the metric *inserted*
rather than *recovered* (HA's own second-disjunct finding).  The closing 26/99
sector is, by Theorem (5), exactly the `Λ ≡ q^{-1}` locus — a subalgebra
selected by the coefficient condition, not an independent HDA-analogue sector.
The rigid (constant-coefficient) cells are the homogeneous records, where by
Theorem (4) constant and metric-reading are indistinguishable.  A successor
earning "GR's algebra at scale" needs: (i) a realisation at which
`{D,H} = H[L_vN]` — my census says none of the 27 does; (ii) a coefficient
*recovered* rather than inserted on an **off-diagonal** record — currently 0
cells; (iii) a refinement direction, which R1's terminal blocks.

**K4.**
* **Is L-stability a theorem?**  **Not from the linearity that forces closure** —
  linearity forces only the landing (T1).  It *is* forced, by a different route:
  by Theorem (4) closure and class are **pointwise** functions of the count
  vector at each site; the declared records' counts are functions of the raw
  coordinates `x_j` with **no mod-`L` wrap**, so the realised count vectors at
  `L=4` are a **subset** of those at `L=5`.  Hence closure/constancy at `L=5`
  ⟹ at `L=4` (one implication is a theorem); the converse is a finite check over
  the count vectors present at `L=5` and absent at `L=4` — that is the measured
  content.  Verified at a **third** L (d=3, L=3): 0 differences (**m2**).
* **Scope-stability** (BASE vs TRANSLATES) is a **full theorem** given the
  measured full-rank spanning at BASE (**D5**).
* **The five worker flags.**  `w = 1` anchored-not-swept — accepted (the pin's
  `density_weight` is 0; the flip value is anchored, not used).  d=3 dense-route
  sparsity — the unit's dense route runs at (2,4),(2,5) only, but my
  reconstruction ran a genuinely different route (support-free per-site, integer
  scaled) at **all four** arenas and agrees at 476/476, so the gap is closed from
  outside.  X07's d=3 probe convention — honest and printed; see **n5**.  The
  non-constant tangential exclusion — **not load-bearing** (**n2**, measured).
  The TRANSLATES enlargement — inert by theorem (**D5**).

**K5 (at the operator depth).**  I rebuilt the verdict's measured content from
my own censuses.  Every counted quantity in the emitted string reproduces
byte-for-byte: `ARENA` (16/25/64/125, links 3/6, records 14, rules 11),
`L-GATE` (36-OF-36, 3 recomputed fractions), `RECOVERY` (99/99, 72/72, det 2,
5 records), `HH-BRACKET` (476/476, 56/56), `COEFFICIENT` (all six class counts,
56/56, 32/120), `HH-RESIDUAL` (336/476, the ten-rule list, 36, MAX=48),
`DH-BRACKET` (10506/120/10386, 0 of 21012), `DEFECT` (3096/3096, 0, 0),
`CONVENTION` (1152/1152/21126/1152 of 21126), `DD-BRACKET` (644/644),
`LAPSE` (62), `LSWEEP` (all eight rows, class-constant TRUE),
`CONTROLS` (4/4, 120969, 58572, 128).  **No divergence in any number.**  The
divergences are the three characterisations (D1, D3, M2) and the two
denominators (M1, D4).  I also confirm the verdict comparator
(`reconstruct_verdict_from_receipt`) rebuilds from the **raw rows**, not from
`summary` — #219-compliant at that gate.

---

## Grade and rationale

**ACCEPT-WITH-FIXES.**

Zero false physics numbers.  A from-scratch rebuild with different primitives
reproduced 476/476 census cells, 476/476 coefficient rows, 21 012 `{D,H}`
classifications, 644 `{D,D}` brackets, 3 096 defect probes (twice, by two
routes), all 171 pinned I7 recovery cells, all controls and all eight L-sweep
rows, with zero mismatches.  The DEFECT head survives the hardest attack I could
mount: **no** declared-expressible tangential realisation, in a 27-member
census over 73 872 classifications, ever closes `{D,H}` into the constraint
family.  Two new measurements strengthen the unit (the defect survives the other
bracket order and non-constant tangential fields).

Against that: two structural claims must move — the defect's
*outside-the-basis* status is realisation-relative on the homogeneous sector
(**M2**), and the `arch-B` characterisation of the 36 inconsistent cells is
false (**D1**).  One gate is vacuous by construction and is cited as compliance
evidence for the very rule it fails (**M1**).  One paper sentence and one
receipt field describe a control that does not exist (**D3**).  And the `{H,H}`
half of the unit is a corollary of a theorem the unit does not state, whose own
hypothesis it does not measure (**§1**, **D5**).  Every one of these has a
definite, cheap repair.

---

*Reviewer R1 (operator lens).  Recomputations: 37,312 delivered/derived
quantities, ~1.03 M exact-rational evaluations, five new censuses.  Frozen
hashes re-verified after all work: paper `00850cc796d0`, code `bbcc9a1aa7de`,
output `d54142292980`, receipt `1c8beb16c8a2` — unchanged.  Single repo file
written: this one.*
