# D70 — THE HORIZON LIMIT: is there a measure at transport scope that needs no bounded abstraction?

**Status:** PIN, STRICT (frozen from the D69 scoping draft, unchanged except this status line), 2026-07-27.  **Parents:** B1/D56 probe
(LOG #432 — no bounded menu-exact abstraction at transport scope, for
any design; the two load-bearing claims independently verified);
D57 (LOG #436 — sector-exact closed at `(actor, type)` on ground (2)
alone, counts as lower bounds; residues: type-only, budget-only,
untested); **D46b TERMINAL** (LOG #384 → #398 → #400 — relative-horizon
potentials and kernels, three round-1 reversals, delta CLEAN);
**D44f** (LOG #370 — the horizon-stable forced object is the SECTOR
CONDITIONAL; absolute weights are horizon-bound); **D50** (LOG
#421/#422 — record-level observables are the AGGREGATED ones; the form
is a CHOICE); D44b (LOG #374 — the transport chain escapes its windows;
no menu-shape transfer); D62 (LOG #460 — row R4: every pair-arb is a
renewal to the root state); D65 (LOG #468 — `Zhat`'s descent and the
573 ⊃ 205 ⊃ 28 ⊃ 1 hierarchy); D46d (LOG #398/#400 — BLOCKER B2:
*"the theory's own law" is not established*).  **Campaign opened at LOG
#481.**

## 1. The question

Every settled measure result in the corpus was bought with a **finite
menu-exact quotient plus Perron**, and B1 proves that method cannot
transfer.  But a measure is not a quotient.  This unit asks whether the
object D46b already computes — the relative-horizon kernel

```
    k_r(e | h)  =  q(e | h) · G(h + e, r − 1) / G(h, r)
```

— has a **limit** as the remaining horizon `r → ∞`, uniformly over a
declared family; whether that limit is **independent of the truncation
convention** (the transport analogue of root-freeness); and whether it
is **proper** (a probability at every history).  A uniform,
convention-independent, proper limit is a consistent family of
conditionals and hence a measure on transport-scope histories — **built
without any bounded abstraction, and therefore untouched by every wall
the corpus owns.**

A secondary arm, cheap and independent, settles the two remaining
aggregation residues in the same receipt (§3, gate HZ5).

## 2. The objects

- **The layer:** the committed `v10/code/d42b1_transport_exact.py`,
  exec'd path-anchored, AST/text-slice verified.  Admission and pricing
  are **never** re-implemented.
- **The families:** ARM-1T (2 actors) exhaustively to its committed
  caps; and declared 3-actor and 4-actor pools to printed depths.  Every
  cap printed by the receipt.  Sampled arms, if any, labelled
  `[SAMPLED]` and never conflated with exact rows (D46d's method gate).
- **The kernels:** `G(h, r)` by exact backward recursion; `k_r(e|h)` in
  exact `Fraction`s; and the **sector-normalized conditional** of
  D44f/D46b as the *pinned* object (the absolute weights are carried as
  context, per the D44f lesson).
- **The drift norms:** L∞, L1 and sector-L∞ — the three D46b used, which
  gave exactly equal sequences at the root; reported separately, never
  merged.
- **The truncation conventions:** at least two declared terminal
  treatments of the cap layer (the committed one, plus a second — e.g.
  the D57 **S4** pattern of a maximally coarse terminal), each carried
  through the whole computation independently.

## 3. Gates

- **HZ0 — ANCHORS.**  Committed layer by AST/text-slice.  Reproduce, in
  this receipt's own process: the ARM-1T cumulative census
  `[1, 9, 69, 521, 3969, 30729]` and **243,769** to depth 6 (the D56
  probe's M1 anchors); the ladder `{2: 3757, 5/2: 212}` (D46b MB1);
  the transport potentials `G_3 = 257/32`, `G_4 = 1035/64`,
  `G_5 = 4173/128`, `G_6 = 134587/2048` and **both** ratio columns
  (delivery-free and transport) exactly; the root sector-normalized
  drift **exactly zero at `r = 1..6`**; the off-root sup sequence
  `1/18, 4/171, 8/741, 176/32877`; and the family-uniform sup
  `3/110, 3/253, 373/69230, 2333/1838829`.  **Exit 1 only here.**
- **HZ1 — PROPERNESS, EXTENDED.**  `Σ_e k_r(e|h) = 1` exactly, for every
  `h` in each declared family, at `r = 1..R` with `R` printed.  D46b has
  this family-wide only at `r = 1, 2`.  A failure is a **first-class
  finding** (outcome HZ-IV), not an error.
- **HZ2 — THE CAUCHY TABLE (the unit's core).**  The family-uniform sup
  of `‖k_{r+1} − k_r‖` in the three norms, over each declared family,
  extended in `r` **and in actor pool**, as exact rationals.  **No fitted
  rate, no extrapolation, no invented threshold.**  The word "converges"
  may not appear in any label unless HZ4 supplies a bound; otherwise the
  deliverable is the table and the word is "contracts over the computed
  horizons".  *(This clause exists because D46d's BLOCKER B1 convicted
  exactly this inference and D57's S2 label had to be corrected for a
  threshold "justified nowhere".)*
- **HZ3 — TRUNCATION-CONVENTION INDEPENDENCE (the horn gate).**  The
  same kernels under at least two declared terminal conventions,
  compared **at matched relative horizon**, entrywise in exact
  `Fraction`s, at the root **and** family-wide at the reachable `r`.
  Equal, and staying equal as `r` grows = evidence of root-freeness at
  transport.  Different, and **not** shrinking in `r` = **the imported
  completion horn (I)**, and the difference is the deliverable.
- **HZ4 — THE LEMMA SLOT (proof-shaped; may return empty, and saying so
  is a result).**  Attempt a **contraction / minorization bound** rather
  than a measurement, on the corpus's own named candidate: D62's row R4
  (every pair-arb is a renewal to the root state, derived), plus D46b's
  **MB5** (root = renewal transfers at matched horizon,
  necessary-not-sufficient with the non-sufficiency censused
  8,196/30,728, 1,060/3,968, 104/520).  Gate: (i) the transport renewal
  predicate defined from R4's serialisation and verified at every
  occurrence against the layer; (ii) the exact return-weight census from
  renewal to renewal by cycle length; (iii) whether the **B1 ladder's**
  cylinders (which never regenerate) carry vanishing total weight;
  (iv) a printed minorization constant **or** an explicit "no bound
  exhibited".  **No outcome here may upgrade HZ2's labels unless a bound
  is printed.**
- **HZ5 — THE AGGREGATION ARM (secondary, cheap, independent).**  D57's
  coarsest-lumpable fixpoint recomputed at two strictly coarser sector
  maps — **TYPE-ONLY** (`s = event-type`) and **BUDGET-ONLY** (`s = the
  weight budget`) — at caps 3/4/5/6, with D57's **S4** trivial-boundary
  control so the counts are lower bounds, and D57's **S3** split witness
  at each cap.  Its finite-alphabet prerequisite gated first and
  separately.  **Declared droppable** if the runtime budget binds — with
  the drop printed, never silent.
- **HZ6 — CONTROLS AND ANTI-VACUITY.**  (i) **Negative control:** a
  deliberately perturbed weight law must break contraction — an
  instrument that cannot fail is not evidence (D68 **F5**; the probe's
  `full0` row).  (ii) **Positive control:** the delivery-free d42a
  family through the same pipeline must reproduce `Zhat`'s known objects
  — `f = (4,4,3,7,3,3)/3`, values `{1, 4/3, 7/3}` at multiplicities
  `{29, 5, 2}`, and `λ = 2` as an **asymptotic** eigenvalue (never
  compared to a finite-horizon ratio — D46b's own relabelling).
  (iii) **AST anti-vacuity scan** over every `check()` predicate (D57
  **S5**), with the hoisting defect D46b carried named in the label so
  the scan is not sold as more than it is.  (iv) **Determinism** under
  `PYTHONHASHSEED` 0/7/999, byte-identical stdout (D63 **W6b**).
- **HZ7 — THE WALL CONTROL (diagnostic; changes nothing).**  Re-derive
  the B1 ladder with `deliver_options_in_view` restricted to
  non-superseded holdings, **as a diagnostic only**, and report whether
  unboundedness survives.  The gate label must print: *the committed
  layer is unchanged; no other number in this receipt uses the
  restricted enumerator; adopting it would be a different theory and is
  not proposed.*
- **HZ8 — DOCTRINE.**  No infinite-volume claim from finite horizons
  (D46b **MB6**, binding).  Every statement horizon-scoped and
  pool-scoped.  Every normalization named at every use (D46d **B2**).
  Sampled never conflated with exact (D46d **TY3/TY5**).  No dimension
  claim and no typicality claim of any kind in this unit.  Scale
  doctrine, LOG #440.  No claim about the identified law: the missing
  map is untouched.  Caps and runtime printed by the receipt itself.

## 4. Pre-registered outcomes (any is the result)

- **HZ-I — NOT CAUCHY.**  The family-uniform drift stops contracting at
  reachable `r`, or contracts at the root while failing family-wide, or
  fails at wider pools.  Then the horizon-limit route is **closed by
  measurement**: the finite-horizon measures are horizon artifacts,
  D46d's typicality numbers stay horizon-scoped permanently, and the
  campaign's weight moves to R1/R2 (HZ5's arm) and R8.  A first-class
  negative and the cheapest one to reach.
- **HZ-II — CONVERGENT BUT CONVENTION-DEPENDENT (horn I at transport).**
  HZ2 contracts and HZ3 separates.  Then a measure at transport scope
  exists but is an **imported completion**, and D50's *"the form is a
  CHOICE"* becomes a program-wide statement rather than a d42a one.
  **This is the most informative outcome for the four frontiers**, since
  every frontier question becomes "under which completion?" — a
  well-posed question with a priced answer.
- **HZ-III — CONVERGENT AND CONVENTION-INDEPENDENT.**  A root-free
  measure at transport scope, obtained without any bounded abstraction —
  the walls confirmed to bite the **reduction** and not the **object**.
  Then dimension typicality, grid typicality and the transport-scope
  functional slot become posable immediately.  **This outcome may be
  claimed only with HZ4's bound printed**; without it the label is
  "root-free over the computed horizons", explicitly not a boundary
  theorem.
- **HZ-IV — CONVERGENT BUT NOT PROPER / NOT A MEASURE.**  HZ1 fails
  family-wide, or the limit is a kernel that is not additive along cuts
  — the transport analogue of §B2.10's cut-mass non-additivity
  (`1, 2, 4, 257/32, 1037/64, 2101/64, 68313/1024` at d42a).  Then the
  defect is named exactly and the completion problem is re-posed with
  its transport shape known.
- **HZ5-a / HZ5-b:** a coarser sector granularity **closes** (Perron
  reopens in aggregated form; the D57 wall is granularity-specific) /
  **blows up** (the aggregation wall extends to the two named residues
  and routes R1/R2 close).

**LEAN — stated exactly, and narrowly.**  *(The campaign's record: D57
pre-registered two expectations and both were refuted, one of the
refutations then withdrawn; D46d's lean produced a blocker; D68 declined
to bet and was right to.)*

- **HZ1 (properness at `r ≥ 3` family-wide): weak lean POSITIVE**, on
  the ground that it is proved by construction at the root for
  `r = 1..6` and gated family-wide at `r = 1, 2`.  Gated **first**, as
  the prerequisite; its failure is outcome HZ-IV.
- **HZ2 at the two-actor arm: weak lean CONTRACTING**, on the ground of
  D46b's gated four-term family-uniform sequence
  `3/110, 3/253, 373/69230, 2333/1838829` — **and the pin records that
  this is four terms at small caps at two actors, that the sequence is
  explicitly "not a rate" in its own source, and that a contracting
  finite sequence is not a limit.**
- **HZ3 (the horn), HZ2 at wider pools, HZ4 (the bound), HZ5: NO LEAN.**
  These are the questions the unit exists to answer and the pin declines
  to bet on any of them.

## 5. Falsifiers, named

1. **The instrument cannot fail** — if the perturbed-law control
   (HZ6-i) still shows contraction, every HZ2 number is void.
2. **The root is not the family** — if drift is zero at the root and
   non-contracting family-wide, "horizon-stable" was a root artifact
   (this is precisely the reversal D46b's round-1 already performed once
   in the other direction, and the reason MB5-c exists).
3. **The convention gate collapses** — if the two terminal conventions
   differ by an amount that does **not** shrink in `r`, HZ-III is
   excluded no matter how good the Cauchy table looks.
4. **Pool dependence** — if the drift's contraction rate degrades
   systematically with actor pool, the two-actor arm was measuring the
   ARM-1T family and not transport.
5. **Ladder mass** — if the B1 ladder's non-regenerating cylinders carry
   non-vanishing weight under the limit candidate, no regenerative
   argument (HZ4) can ever supply the bound, and HZ-III is
   permanently out of reach by this route.
6. **Anchor breakage** — any committed D46b number failing to reproduce
   invalidates the unit (exit 1).

## 6. Scope, binding at every citation

Transport scope, the **declared families and caps only**; exact
`Fraction`s throughout.  **No infinite-volume claim under any outcome.**
The pinned object is the **sector-normalized conditional**; absolute
completed weights are horizon-bound (D44f) and are context.  No claim
that any limit is *the* click law's measure — the identified law is
reached only through the missing map (D59/D65), untouched here.  No
dimension, typicality or quantum-layer claim of any kind; those are the
**consequences** this unit would unblock, not its content.  Scale
doctrine (LOG #440): this unit certifies a **mechanism** — the existence
or non-existence of a horizon-limit measure — never an object.  (H1)/(H2)
and the 36-state closure remain **two-actor delivery-free d42a**; nothing
here extends them, and the own-view dichotomy's **proposer test** is
known to break at three actors.

## 7. Exit protocol

Exit **0** for every substantive negative, including HZ-I, HZ-IV and
HZ5-b — these are results.  Exit **1** only on **HZ0** anchor breakage,
i.e. if the committed layer or a committed D46b/D57 number fails to
reproduce in-process.  Every cap, seed, pool, runtime and dropped arm
printed by the receipt itself.  Pin frozen and committed **before** any
code is written; the note names the receipt path before it exists.

---

## §6. WHAT THIS NOTE DOES NOT DO

- It **proposes no new numbers** and closes no question.
- It does **not** adjudicate the ambiguity it found in the corpus: D57's
  ground (1) is withdrawn, so **whether the sector-total alphabet at
  transport scope is finite is `[OPEN]`**, and both the pin's HZ5 arm
  and any future citation must treat it as open rather than as either
  settled direction.
- It does **not** rank the **TRIPLE-GRID** construction (book §D4 item 2,
  `[NOT BUILT]`) against the measure campaign; that is a construction
  front, not a measure front, and the two are independent.
- It takes no position on the **Lean-grade mechanization** residue, on
  the two empty bridges (§C5, §C6.11), or on the demand's-uniqueness
  computation (book §D4 item 1a) — the last of which is *cheaper* than
  anything in §5 and belongs to the missing-map front rather than to
  this campaign.
