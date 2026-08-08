# HA — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens.
**Protocol:** `v13/note-ha-hostile-protocol.md` (FROZEN, v13 #240), kill-shots
K1–K5 binding.  Primary weight K3 and K4 per dispatch; K1/K2/K5 at lower depth.
**Object reviewed (SHA-256, first 12, verified at open AND at close of review):**

| artifact | pinned | measured |
|---|---|---|
| `v13/paper-ha-successor.md` | `4e7589da58fe` | `4e7589da58fe` ✓ |
| `v13/code/ha_successor_exact.py` | `19dad19b01ee` | `19dad19b01ee` ✓ |
| `v13/code/ha_successor_output.txt` | `fda287ee86c3` | `fda287ee86c3` ✓ |
| `v13/code/ha_successor_receipt.json` | `7d74bea76760` | `7d74bea76760` ✓ |

**Independent recomputations: 32.**  All performed with my own from-scratch
code in the scratchpad (`r2_defs.py`, `r2_recompute.py`, `r2_bridge.py`,
`r2_final.py`), importing nothing from the instrument, exact `Fraction`
arithmetic, and — where the instrument fixes a coordinate — deliberately
different choices (a different base front, four different reduction primes, an
enlarged antisymmetry sweep).  Six of the 32 are measurements the unit does not
report.

**Grade: at the end, per protocol.**

---

## 0. Summary of the verdict I reached

Sections 3–9 of the paper are, so far as I can refute them, **correct**.  I
reproduced every headline number of the primary result from scratch — including
the full 11 × 9 × 132 closure table by literal five-map composition (13,068
residual evaluations) — and found **zero** numerical discrepancies.  The
construction is real, the inversion is closed-form, the transport is genuine and
load-bearing, and the disclosures (X02, X04) and §13 non-claims are unusually
honest.  `HA-RUNNABLE` is earned.

**§10, the declared secondary, does not hold up.**  Four independent defects,
each of which I measured:

1. the decisive order-spectrum criterion is evaluated against the **wrong one of
   two spectra**, and the right one — which this very instrument computes at
   anchor A14 — **contains 5**;
2. the "order 5, exponent 5" structure group is an artifact of the **declared
   reduction prime** (I measure order 7 at p = 7, 11 at p = 11, 13 at p = 13);
3. the posability predicate is **unreachable** — no achievable measurement at
   this arena could return POSABLE, so the gate is not falsifiable on the
   measurement;
4. the supporting "17 of 24" is **17/17 vacuous** — every one of the 17 is a
   cell where `R_HH` is the identity.

The bridge *conclusion* is probably still right.  Its *stated grounds* are
largely artifact.  Under this programme's own engraved discipline that is a
repair, not a dismissal, because the primary verdict survives intact.

---

## 1. K3 — THE READOUT DEVIATION (primary weight)

The dispatch asks two questions.  I answer them separately.

### 1.1 Was the rejection of `v6_task2b` correct by GW1's own text?  **YES —
and the paper understates its own case.**

I read `code/v6_task2b_metric_extraction.py` in full (119 lines).  GW1 §2's
grading cites `:48`, `:60-65` and `:57-58`.  The reach outside order+count data
is **broader than GW1 recorded**:

| line | what enters | order+count? |
|---|---|---|
| `:40` | `central = np.all(np.abs(P) < sub)` — the sample region | **embedding coordinates** |
| `:48` | `dx = P[b] - P[a]` | **embedding separations** |
| `:49–51` | `tt = dx[0]**2 - Σdx[1:]**2`; `if tt <= 0 or tt > tau_cap**2: continue` | **the true interval filters the sample** |
| `:57–58` | `K = Σ(card·τ²_true^{d/2}) / Σ(τ²_true^d)` | **scale calibrated against the true interval** |
| `:63–65` | the design matrix `A` built from `dX` | **embedding separations** |
| `:52` | `c = C[a,b]` | the *only* order+count ingredient |

Against GW1 §1.1 condition 5 — "`q^{ij}_order` on the same hypersurface, **from
order and count data on the same substrate**" — and §1.2's ban on "held-out
embedding coordinates", `v6_task2b` cannot supply the readout.  **The worker's
rejection is correct.**  Executing the directive's letter would have inserted
held-out embedding data into `β`, i.e. into the residual under test, and the
unit would have been dead on arrival.

Two further reasons the directive's letter is unexecutable, **neither of which
the paper gives**, and both of which strengthen the deviation:

- **Type mismatch.**  `v6_task2b` returns a single constant `d × d` float matrix
  least-squares-fitted over a whole sprinkling.  `β_a^i = I_a(g)^{ij}(x)·ω_j(x)`
  needs an **exact, site-dependent rational field** on a `3^d` lattice.  There is
  no route from the former to the latter; the directive names an object of the
  wrong type.
- **Flat-only, no error control.**  The script's own closing note lists
  "(i) curved test — repeat on a curved sprinkling" as REMAINING, and GW1 §9
  records that none of the nine re-run scripts prints a standard error: every
  quoted value is a single-seed point estimate.

**One citation slip.**  §1 and §12.1 say using `v6_task2b` "would fail GW1 §1.2
at the first line".  §1.2's first line is the *permission* list ("may use the
causal order, event counts, record adjacency, and eventwise lapse values").  The
operative provisions are §1.2's **second** bullet and §1.1 **condition 5**.  The
claim is right; the pin-cite is loose.  [MINOR, repair below.]

### 1.2 Does the substitute smuggle?  **Not by GW1 §1.2's enumerated bans — but
its provenance claim is unsupported, and its mitigation is under-powered.**

I ran the same no-smuggling audit K1 runs on the drag, on the readout.
Ingredients of `q_ij e_ℓ^i e_ℓ^j = n_ℓ(x)`, `I = q^{-1}(det q)^w`:

- **(a) the counts `n_ℓ(x)`.**  GW1 §1.2 permits "event counts" explicitly.
  **CLEAN.**
- **(b) the link vectors `e_ℓ`** — the declared basis of `(Z_L)^d`, including the
  relation `e_diag = e_1 + e_2`.  This is a **frame**, and GW1 §1.2's ban list
  contains "planted frames".  Deviation 3 declares it and cites GW1 §2's
  unsolved direction-labelling problem, so it is **disclosed** — but it is not
  identified as touching the §1.2 ban list, and the mitigation offered is weak
  (see below).
- **No metric estimator `G_a`, no held-out embedding coordinate, no background
  unit normal** is called anywhere in the readout.  I checked the construction
  end to end.  **On GW1 §1.2's enumerated bans, the substitute PASSES.**

So K3 half 2 comes out in the paper's favour on the letter of the predicate.
Three structural qualifications, all measured:

**(i) The readout is an invertible re-encoding, not a reconstruction.**  I
measured that counts → `q` is **linear and invertible** at the declared arena:
`q_11 = n_{e1}`, `q_22 = n_{e2}`, `q_12 = (n_diag − n_{e1} − n_{e2})/2` (three
links ↔ three components at `d = 2`; six ↔ six at `d = 3`).  The "geometry
record" and "the metric" are therefore **the same datum in two coordinate
systems**.  §13's non-claim ("No metric is recovered … read from the geometry
record by a declared readout") is honest about this.  §3.2 is not.

**(ii) "the corpus's own order+count relation" is unsupported.**  I checked the
two candidate sources:
  - **v4 p7 Definition 1.4** (`:175-193`, read in source) says only: "let
    `I_a(g_a)^{ij}` be its **metric candidate**."  It is an undetermined
    placeholder.  HA's readout is a legitimate *instantiation* of it — but Def
    1.4 supplies no relation.
  - **v6_task2b** — the only committed text implementing cardinality → metric —
    uses `τ̂² = (card/K)^{2/d}`, i.e. the Myrheim–Meyer exponent, **not**
    cardinality-linear.  HA's linear relation coincides with it only at
    *spacetime* `d = 2`, while HA applies it at *spatial* `d = 2` **and `d = 3`**
    (§9).
  The honest description is: **a declared readout, chosen because it inverts
  exactly.**  Calling it "the corpus's own" is a provenance overclaim.

**(iii) The chart-equivariance mitigation is under-powered.**  Deviation 3
offers §7.4's equivariance (4,860 comparisons, 0 violations — I did not
re-derive this one) as the mitigation for the planted frame.  But the declared
chart group is the `|X|` translations plus the `d!` direction relabellings —
a subgroup of the **automorphisms of the very structure being questioned**.  A
self-test conducted under a group derived from the planted frame cannot certify
the frame.  This is the RUNBOOK §14 lesson in its own idiom (a self-test routed
through the audited component tests the component, not the quantity).  I checked
what the split actually rests on: `q_12 = 0 ⟺ n_diag = n_{e1} + n_{e2}` — a
statement about counts **and** about which link is called the diagonal.  The
sector split is therefore a property of (counts, declared link set), and the
declared link set is not record-derived.

**K3 verdict: the rejection is correct and should be argued harder; the
substitute is clean on §1.2's bans; two statements about the substitute
(provenance, mitigation) need to be brought down to what was measured.**

---

## 2. K4 — THE BRIDGE NEGATIVE (primary weight)

The dispatch asks: obstruction **theorem**, or **search** that found none, and
does the paper say which?

**Answer: neither, and the paper says so in one place only.**  §13 states "The
negative in §10.4 is scoped to the committed coordinates enumerated there; no
nonexistence theorem about bridges is claimed."  That is the correct disclosure
and it earns real credit.  But there is also **no search**: no receipted census
of candidate carrier morphisms exists anywhere in the unit.  What §10 actually
exhibits is a **coordinate mismatch at one declared loop**.  Below, the four
defects I measured in that exhibit.

### 2.1 [MAJOR] The spectrum criterion reads the wrong spectrum — and the right
one, computed by this instrument, contains 5

The instrument's decisive predicate is

```
in_spectrum = ha_order in (1, 4, 6, 8, 10, 12, 14, 30)     # line 2021
```

That is GEN's **holonomy** order spectrum (`2n`, the dihedral orders).  But the
compared object is GEN's **defect**:

- §10.3's coordinate table pairs *"defect construction: `D = P_W U⁻¹ P_W U`"*
  with *"`R_HH = C(H[N],H[M]) D[−β]`"* — R_HH ↔ **D**;
- §10.2 tests **the defect's** relation `ΣDΣ = D⁻¹` on `R_HH`, with **GEN's own
  defect** as the positive control.

And this instrument **computes GEN's defect order spectrum itself**, at anchor
A14 (read from the delivered receipt):

```
A14  GEN: the order spectrum of the defect over the whole family
     {1:96, 2:1440, 3:4224, 4:4608, 5:4608, 6:6912, 7:9216, 15:9216}
```

**Order 5 occurs at 4,608 of GEN's 40,320 members.**  So the like-for-like
comparison — HA's `R_HH` against GEN's `D` — **succeeds**; it is only by
checking HA against the *holonomy* spectrum while checking GEN against the
*defect* spectrum that the criterion fails.  §10.2's table makes the mismatch
visible in a single row: GEN's defect (order 2) is marked "yes" and HA (order 5)
"no", against a cell that lists **both** spectra.

Two RUNBOOK provisions bite:
- **§15 addendum** — "a class-vs-class verdict whose classes are read at
  different coordinates is a coordinate effect in disguise";
- **failure catalogue #24** — "counts computed, never typed".  The spectrum is a
  **typed tuple literal**, while the correct quantity is anchored and computed
  in the same run.

### 2.2 [MAJOR] The holonomy group's order is the declared prime, not a property
of `R_HH`

`R_HH` acts on the reduced carrier as a **translation of the address register**
by `ρ(x*) mod p`.  For prime `p` and `ρ ≢ 0` the generated group is cyclic of
order exactly `p`.  I measured this by rebuilding the reduced carrier at four
primes:

| p | carrier | group order | abelian | element orders | `ΣRΣ = R⁻¹` | `ρ(0,0)` (exact) |
|---|---|---|---|---|---|---|
| 5 | 625 | **5** | True | [1, 5] | False | (1/6, 1/6) |
| 7 | 2401 | **7** | True | [1, 7] | False | (1/6, 1/6) |
| 11 | 14641 | **11** | True | [1, 11] | False | (1/6, 1/6) |
| 13 | 28561 | **13** | True | [1, 13] | False | (1/6, 1/6) |

The exact rational residual is **identical at every prime**; only the group order
moves, and it moves *as the prime*.  The coordinate table hedges correctly
("order 5 **here**"), but §10.4's obstruction prose does not, and the
`in_spectrum` predicate consumes the artifact as if it were data.  Note the
sting: **at p = 7 the order is 7, which is in GEN's defect spectrum with 9,216
members** — so under a different declared prime the criterion flips under either
reading.

### 2.3 [MAJOR] The posability predicate is unreachable — G22 cannot fail on the
measurement

```
posable = bridge_posable(carrier_match, in_spectrum, bool(ha_dih))   # = AND
carrier_match := RC.size in (36, 81)
```

`RC.size = p^k · p^d = p^(k+d)`.  I enumerated: for `p ∈ {5,7,13}` and `d = 2`
the reachable sizes are 125, 625, 3125, 343, 2401, 16807, 2197, 28561, 371293 …
**36 is not a prime power at all**, and **81 = 3⁴ requires p = 3**, which is not
in the declared prime set.  So `carrier_match` is **False a priori**.
Independently, `in_spectrum` is False for every odd prime by parity (the
spectrum is `{1}` ∪ evens; `ha_order = p` is an odd prime).

Two of three conjuncts are therefore false **before any measurement is taken**,
and `G22 = gen_dih and (not posable)` collapses to the positive control alone.
The only thing that kills G22 is the `bridge-lax` mutant, which mutates **the
predicate**, not the measurement — so the mutant does not demonstrate that the
verdict *could* have come out the other way.

This contradicts the pin's own instruction for the secondary — "**A yes or no BY
MEASUREMENT, not analogy**" — and RUNBOOK #36 ("every gate falsifiable;
positive+negative controls") and the §13 addendum ("a verdict-flip mutant must
prove that derivation can fail").

### 2.4 [MAJOR] "holds at 17 of 24" is 17/17 vacuous, and is measured by a
different route from the verdict it supports

Paper §10.2: *"The dihedral relation is measured over 24 further declared lapse
pairs and holds at **17** of them — so it is a coordinate coincidence at this
arena, not a structural property of `R_HH`."*

I reproduced the 17, then decomposed it:

```
predicate rho_1 + rho_2 == 0 holds at 17/24
  of which residual IDENTICALLY ZERO (relation vacuous): 17
  of which residual nonzero (genuine):                    0
```

**Every one of the 17 is a cell where `R_HH` is the identity**, where
`Σ·id·Σ = id = id⁻¹` holds trivially.  And at **all 7** cells where `ρ ≠ 0`, the
relation **fails**.  The paper's reading is wrong twice: the 17 are not
coincidences, they are the identity cells; and the true statement is far
stronger and cleaner than the one printed — *the relation fails at every tested
cell where `R_HH` is nontrivial, 7 of 7*.  **The repair strengthens the paper's
own conclusion.**

Two further problems in the same sentence:
- **Route mismatch.**  The 17/24 is computed by a **surrogate** predicate
  (`rho[0] + rho[1] == 0` on the exact rational field, code `:1994`), while the
  declared-loop verdict is computed as an actual **permutation** relation
  (`ΣRΣ` vs `R⁻¹`, code `:1989`).  Two routes, reported as one measurement.
- **"declared" is not true.**  The pairs are `pairs[:24]` — the first 24 of an
  internal enumeration (all with `a ∈ {δ(0,0), δ(0,1), δ(0,2)}`), not a declared
  set.  RUNBOOK §14 addendum: "a symmetry gate's tested set is fixed by
  declaration, never selected by …" — here it is selected by list order.

### 2.5 [MAJOR→MODERATE] What "NO COMMITTED CARRIER MORPHISM" is entitled to
mean, and whether the pin's vocabulary is used honestly

**Honest at the pin's bar.**  The pin's outcome vocabulary is
`HA-BRIDGE-⟨POSABLE|NOT-POSABLE⟩` — "…or not (**the obstruction named**)".  It
asks for a *named* obstruction, not a theorem.  §10.4 names one, and §13 refuses
the nonexistence reading explicitly.  On the pin's own terms the vocabulary is
used correctly, and I do not find the HA-BRIDGE vocabulary abused.

**Not entitled to the "measured consequences" dressing.**  With §2.1–§2.3
removed, what survives of §10.4 is:
- (a) the carriers have different sizes and factorisations — an **observation**,
  not an obstruction, and asserted from inspection rather than from any search;
- (b) `ΣDΣ = D⁻¹` fails for `R_HH` wherever `R_HH` is nontrivial, while holding
  for GEN's own defect — **this is real, and §2.4 makes it stronger**.

So the negative is: *one genuine structural relation fails, at one declared
loop, on carriers that are visibly different objects*.  That is a defensible
`NOT-POSABLE` at the pin's bar.  It is **not** an obstruction theorem, **not** a
search, and the phrase "The measured consequences:" in §10.4 currently attaches
the verdict to two facts that are instrument artifacts.

---

## 3. CLOSURE-IS-INSERTION — is the right-sized conclusion drawn?

### 3.1 What I verified

I re-derived the residual by hand and confirmed it by computation.  For
architecture A with the geometry sector frozen, `w[N,n] = N·Λ·∂n` is linear in
the front, so the group commutator's register displacement telescopes to

```
Δm = w[N, n−N] − w[N, n−M−N] + w[M, n−M−N] − w[M, n−M]
   = Λ^{ij}(N ∂_j M − M ∂_j N) = Λ^{ij} ω_j
```

and hence `ρ^i = (Λ^{ij} − I^{ij}) ω_j`.  Measured: **756 literal-vs-closed
comparisons, 0 disagreements**; and the frozen-front variant gives literal
`= −β` at **108/108**.  I also measured something the unit does not report:
**the residual is completely independent of the base front** — 792 cells × 4
distinct base fronts (including two randomised), **0** cells moved.  The front's
only role is to make the maps nontrivial.

### 3.2 Where the paper is right

- **X02 is disclosed and correct.**  Given full rank, `ρ = (Λ−I)ω` vanishing on
  a spanning family ⟺ `Λ = I`.  The paper records this as a disclosure and not
  as a discovery, and states plainly what the measured content is.
- **§13's non-claims are excellent** and preempt most of the overreach available
  here: "**No metric is recovered**", "No claim that the closure that holds on
  the diagonal sector is a derivation of geometry", "§6.3 measures the opposite".
- **§6.5's mechanism is correct and is the unit's best idea.**  I verified it:
  `I^{jj} = adj(q)^{jj}/det q`, `det q` is a joint function of all link counts,
  and the two-record witness is exact (G-CURVOFF and G-DIAG2 share
  `n_{e1}(0,0) = 2` while demanding `I^{11} = 2/3` and `1/2`).

### 3.3 [MODERATE] Where it is one register too hot

**(a) The A-axis closure sector is itself immediate arithmetic, and §6.1's
headline does not say so.**  I measured: for `q` diagonal, `n_{e_j} = q_jj`, so
`Λ_axis = diag(1/q_jj) = q^{-1} = I` **identically** — verified on all nine
records (diagonal ⟺ Λ==I ⟺ closes, with no exceptions).  §6.5 explains this
("coincides with the metric by arithmetic rather than by design"), so it *is*
disclosed in substance — but §6.1's blockquote presents diagonal-sector closure
as a finding and the reader must reach §6.5 to learn it is an identity.  The
pointer belongs at the blockquote.

**(b) The kill's disjunct is misattributed.**  GW1's kill condition has two
disjuncts: *the metric must already be inserted into `J[N]`*, **or** *the same
record law permits inequivalent recovered tensors*.  Under GW1's own STEP 4
reading, the commutator **alone** has displacement `Λ^{ij}ω_j`, so the extracted
tensor is `q̃ = Λ` — whatever was built into the drag.  The declared family
supplies **11 rules on one record, hence 11 different `q̃`**.  That is the
**second** disjunct, and it fires cleanly and is the sharper statement.  The
Scope box says only "The kill fires"; §6.3's framing attributes it to the first.

**(c) "Insertion" is doing rhetorical work.**  Nothing external is inserted.
What closure forces is that the drag weight be a specific **non-link-local
function of the record** — the count-matrix inverse.  GW1's kill was written for
substrates where the metric arrived from **outside** (a background normal at
`v6_p2c:32-36`, a frame at `v2 p10:655-671`).  The boundary HA actually locates
— *emergent vs inserted at weight-rule locality* — is a boundary between
**link-local and joint functions of the record**, which is a genuinely
interesting and genuinely weaker thing.  §6.5 says this correctly; the §6.3
heading "closure IS insertion" and the §15 verdict line "on this construction,
closure is insertion" do not.

**Sizing.**  This is not an overclaim in the sense of a false statement — §13
holds the line — but the headline and the mechanism are at different
temperatures, and a reader who stops at §6.3 will carry away a stronger kill
than was measured.

---

## 4. Deviations 2 and 3 — legitimate declines or dodges?

### 4.1 Deviation 2 (`K_i` and `ε` eliminated) — **LEGITIMATE DECLINE**

GW1 §5 items 2 and 4 are requirements of GW1's **divided** reading,
`(Ω − I)/ε² = K_i[q̃^{ij}ω_j]`.  v4 p7 Definition 2.3 — which the pin ordered, and
which I verified in source reads exactly as HA poses it — is **multiplicative**:
`R_HH := C(H[N],H[M]) D[−β]`, with the tangential correction **composed rather
than fitted**.  It needs no division by `ε²` and no decoder inverse.  The paper
says the right thing in both places: "they are not open here; they are not needed
by this formulation, which is itself a declared narrowing of GW1's original
STEP 4" (§1) and "it does not discharge them, it declines to need them" (§12.2).
That is a decline, correctly labelled, not a dodge.

**One consequence left unstated.**  Eliminating `K_i` also eliminates GW1's
`q_comp`/`q_order` **comparison**: with no decoder there is no independently
extracted tensor to compare against the record readout, which is exactly why §1
can say "there is only one metric object here".  That is *why* the unit cannot
fire the kill's first disjunct by GW1's original route — and it is the same
observation as §3.3(b).  It should be said out loud, because it is the honest
price of the narrowing.

### 4.2 Deviation 3 (declared direction-labelled adjacency) — **DECLARED, BUT
UNDER-PRICED**

Covered at §1.2 above.  Summary: the arena's frame is planted; GW1 §1.2 bans
"planted frames" in constructions; the paper declares the planting and cites
GW1 §2's own open problem, which is the honest move — but (i) it does not
identify the declaration as touching §1.2's ban list, and (ii) the mitigation
(chart-equivariance under translations + `d!` relabellings) is a symmetry test
under a subgroup of the automorphisms of the planted structure, so it cannot
certify the structure.  RUNBOOK §15 asks for scope tags **at the claim**; the
sector-split headline in §6.1 carries none.

### 4.3 Deviation 4 (tangential sector abelian) — **HONEST PER THE PIN**

The additive address-register realisation makes the tangential maps commute, so
`[v,w]_a = 0`, `R_DD` is vacuous, `H_a[N]` and `D_a[B]` commute identically, and
the corrected switch degenerates.  I confirmed `C(H,D)` trivial at **108/108**.
The pin asks for `H_a[N]` and `R_HH`; it does not ask for the diffeomorphism
sector.  §12.4 and §13 declare the consequences and refuse
`V4P7-FIN-ALG-CLOSE` and `R_DD`/`R_DH`.  Critically, the alternative realisation
**is** measured rather than waved away: D-TOT admits a site-permutation
realisation at only **8 of 1188** cells with `β ≠ 0` (§7.6).  That measurement is
the real content and it is properly carried.  **Not a dodge.**  I would ask only
for one sentence making explicit that the abelian tangential sector is a
*realisation choice* whose only tested alternative is almost nowhere defined, so
GW1's diffeomorphism content is untouched by this unit.

---

## 5. K1, K2, K5 at lower depth (as dispatched)

Everything in this section reproduced **exactly**; no discrepancy found.

**K1 — the construction.**  `H_a[N](n,m) = (n+N, m+w[N,n])` is a skew product
over the front; the closed-form inverse is correct (I re-derived it, and
literal-vs-closed agrees at 756/756).  The transported second step is not
cosmetic: I verified that freezing the front makes all four drag terms cancel,
leaving `ρ = −β` exactly (108/108) — which is precisely §6.4's mechanism.  The
drag uses only the front tilt `n(x+e) − n(x)` (a difference of committed
division-event counts) and the eventwise lapse `N(x)`, both on GW1 §1.2's
permitted list.  **No smuggling found in the drag.**

**K2 — the two-sided closure.**  Recomputed independently, by **literal five-map
composition**, with a base front of my own choosing:

- the full 11 × 9 × 132 closure table — **every cell matches**, including the
  non-obvious ones (`A-chart` 70 on G-ANISO and 84 on G-CURVED; `B-all` 78/114;
  `A-insert-x` failing on exactly the four cross-term records);
- the sector-law grid — **0 mismatches over the 63 transported cells**, including
  the `A-chart | G-CURVED` 1/1 cell;
- **G08B** — `A-notransport` is 9/0 on all nine records;
- **G09** — the two-record witness verified exactly;
- the `Λ − I` and `max|ρ|` table — all five exact values reproduce
  (2, 40/33, 20/33, 2/3, 0);
- **d = 3** — `A-chart` 30/CLOSES/30, `A-axis` CLOSES/CLOSES/18,
  `A-linkframe` 30/30/30, `A-insert` all CLOSES;
- **antisymmetry** — 1,080 pair-swaps (vs the unit's 360), **0** violations;
- **density-weight flip** — 4 cells move, G-CURVED = 92 at `w = 1`.

On "is G09 a theorem?": as stated it is an **exhibited counterexample** for the
declared record family, not a theorem over all link-local weights, and §13's
"No claim about … general weights" scopes it correctly.

**K5 — instrument.**  The multi-prime control has real teeth, and I verified its
witness cell exactly: `A-linkframe | G-OFFDIAG2` has
`(Λ−I)(0,0) = [−5/132, 35/132; 35/132, 7/660]`, residual `(35/132, 7/660)`,
**undefined mod 5**, exactly **(0,0) mod 7**, and **(11,2) mod 13**.  Only
`p = 13` sees it.  G16 and G19 are correctly demoted to *recorded* (X04): I
confirm both are analytically forced (front advance additive → 594/594 trivial;
register passive under the front).  Two small notes:

- **[MINOR]** `residual_field_closed` **hard-codes** the `A-notransport` branch
  as `−β` (`:757-761`) rather than deriving it from the uniform formula.  It is
  still genuinely independent of the literal composition — I verified literal
  `= −β` at 108/108 — so G05 remains a real check and this is **not** the
  #38→#40 disease.  But §3.7's description of a single "closed form, built from
  the drag rule and the record readout" is inaccurate for that row.
- **[MINOR]** §13-addendum verdict-gate compliance: the unit predates the
  addendum.  The bridge verdict **is** gate-derived (G22), which is the right
  shape — but per §2.3 that derivation cannot fail on measurement, so the
  addendum's substance is not met for §10.  Flag for repair, not fault.

---

## 6. Findings, ranked

| # | severity | finding | repair |
|---|---|---|---|
| 1 | **MAJOR** | §10 spectrum criterion evaluates HA against GEN's *holonomy* spectrum while evaluating GEN against its *defect* spectrum; order 5 **is** in the defect spectrum (4,608/40,320), which the instrument itself computes at A14.  The tuple is **typed**, not read from the anchor (failure-catalogue #24). | Replace the literal with the A14-computed defect spectrum; report that 5 **is** in it; remove the spectrum criterion from the posability predicate. |
| 2 | **MAJOR** | `ha_order` = the declared reduction prime (measured 5, 7, 11, 13 at p = 5, 7, 11, 13), not a property of `R_HH`; the exact residual `(1/6,1/6)` is prime-independent.  §10.4's "order 5, exponent 5" is an instrument artifact. | State the p-dependence; replace the structure-group row with a p-invariant object (the exact rational `ρ`, or the group over `Q`). |
| 3 | **MAJOR** | The posability predicate is **unreachable**: `carrier_match` requires `p^(k+d) ∈ {36,81}` (impossible for `p ∈ {5,7,13}`) and `in_spectrum` is false for every odd prime by parity.  G22 cannot fail on measurement, contradicting the pin's "yes or no BY MEASUREMENT". | Either reframe the negative as **structural** and drop the "measured consequences" framing, or add a positive control — a synthetic HA-like object on an 81-element carrier with an exchange involution — that the predicate returns POSABLE for. |
| 4 | **MAJOR** | "the relation holds at 17 of 24" is **17/17 vacuous** — all 17 are identity cells; the relation **fails at 7 of 7** nontrivial cells.  Also: computed by a surrogate predicate, not the permutation route used for the verdict; and the 24 are `pairs[:24]`, not a declared set. | Restate as "fails at every tested pair where `R_HH ≠ id` (7/7); holds vacuously at the 17 where `R_HH = id`" — a **stronger** claim.  Declare the tested set; use one route. |
| 5 | **MAJOR→MOD** | "NO COMMITTED CARRIER MORPHISM" is **neither** an obstruction theorem **nor** a search — no morphism census is receipted.  §13 disclaims the theorem reading (good); §10.4's "measured consequences" dressing attaches the verdict to artifacts. | Say plainly: a coordinate mismatch at one declared loop plus the failure of GEN's defining relation wherever `R_HH` is nontrivial; no search run, no theorem proved. |
| 6 | MODERATE | K3 half 1: the rejection of `v6_task2b` is **correct and understated** — four further embedding-coordinate insertions (`:40`, `:50`, plus the cited ones), a **type mismatch** (constant float matrix vs exact site-dependent rational field), and flat-only validation with no error control.  §1.2 pin-cite is loose ("first line"). | Cite §1.1 cond. 5 + §1.2 bullet 2; add the four insertion sites, the type mismatch, and the flat-only argument. |
| 7 | MODERATE | K3 half 2: substitute is **clean on §1.2's bans**, but (a) "the corpus's own order+count relation" is unsupported (v4 p7 Def 1.4 says only "metric candidate"; `v6_task2b` uses exponent `2/d`); (b) counts → `q` is an **invertible re-encoding**, disclosed only at §13; (c) the chart-group mitigation is a subgroup of the planted frame's own automorphisms. | Call it a declared instantiation of Def 1.4; move the re-encoding observation into §3.2; price the mitigation honestly. |
| 8 | MODERATE | CLOSURE-IS-INSERTION: correct and well-disclosed at §6.5/X02/§13, but §6.1's headline omits that `Λ_axis = I ⟺ q` diagonal is immediate arithmetic; the kill's **second** disjunct (inequivalent recovered tensors — 11 rules, 11 `q̃`, one record) is the one that actually fires and is not named; "insertion" reads as external when what is forced is a **joint** function of the record. | Name the disjunct; carry the §6.5 pointer into §6.1; retitle §6.3 toward "closure forces the count-matrix inverse — a joint, not link-local, function of the record". |
| 9 | MODERATE | §8 compares a **corrected** pair object to an **uncorrected** triple.  I isolated the mechanism (new, 108/108, 0 failures): with `C(H,D) = I`, `SW_HHH = H[A]H[B]H[C]` with `A+B+C = 0` and register displacement exactly `Λ^{ij}(B ∂_j C + A ∂_j B + A ∂_j C)`.  Non-vanishing is expected: no triple-level correction is defined. | Print the closed form; state that v4 p7 defines no triple-level correction; retitle away from "Pair closure does not buy HHH closure". |
| 10 | MINOR-MOD | Deviation 2 is a legitimate decline, but the consequence — eliminating `K_i` eliminates the `q_comp`/`q_order` comparison itself — is unstated. | One sentence in §12.2. |
| 11 | MINOR-MOD | Deviation 4 honest per the pin; add that the abelian tangential sector is a realisation choice whose only tested alternative is almost nowhere defined. | One sentence in §12.4. |
| 12 | MINOR | `residual_field_closed` hard-codes the `A-notransport` branch as `−β`; §3.7's description of a uniform closed form is inaccurate for that row (the check itself is sound).  §13-addendum substance unmet for §10 (see #3). | Describe the branch; fold the §10 repair into #3. |

**Nothing I tested produced a false numerical result in §§3–9.**  Every headline
number of the primary result reproduced exactly, from independent code, at a
different base front.

---

## 7. Recomputation count and inventory

**32 independent recomputations.**  Enumerated:

1 readout table (11 records: counts, `q`, `det q`, `I`, admissibility) · 2
admissibility split 9/2 with both failure modes · 3 lapse family 12 / 132 pairs ·
4 identifiability rank 2 at all 9 sites · 5 **full closure table by literal
five-map composition (11 × 9 × 132 = 13,068 evaluations)** · 6 sector-law grid,
0 mismatches over 63 cells · 7 G08B 9/0 on all records · 8 `Λ−I` and `max|ρ|`
table · 9 antisymmetry, 1,080 swaps · 10 density-weight flip, 4 cells move ·
11 d = 3 table · 12 `C(H,D)` trivial 108/108 · 13 Jacobi lapse sum 0/108 ·
14 `SW_HHH ≠ id` 81/108, 27/36 per rule · 15 **[new]** `SW_HHH` register
displacement `= Λ(B∂C + A∂B + A∂C)`, 108/108 · 16 bridge holonomy at p = 5 ·
17 **[new]** the same at p = 7, 11, 13 → order = p · 18 **[new]** `ρ(0,0)`
prime-independent · 19 the 17/24 reproduced **and decomposed 17 vacuous / 0
genuine** · 20 **[new]** base-front independence, 792 cells × 4 fronts ·
21 literal-vs-closed 756/0 · 22 `A-notransport` literal `= −β` 108/108 ·
23 A-axis closes ⟺ `q` diagonal ⟺ `Λ = I`, all 9 records · 24 G09 witness ·
25 the `prime-single` cell mod 5/7/13 · 26 matter-free front commutator 594/594 ·
27 **[new]** `carrier_match` unreachable (`p^(k+d) ∉ {36,81}`) · 28 **[new]**
`in_spectrum` unreachable by parity · 29 GEN A14 defect order spectrum from the
receipt (contains 5 at 4,608) · 30 GEN per-setting holonomy orders {1,1,1,1,4,4}
· 31 `v6_task2b` source audit (five insertion sites) · 32 hand derivation of
`Δm = Λ^{ij}ω_j` for the commutator.

---

## 8. What I could not refute

- The construction itself.  `H_a[N]` is a genuine bijection of total records
  with a closed-form inverse, built from front tilts and eventwise lapses only.
  I looked hard for a metric-shaped ingredient in the drag and found none.
- The transport result (§6.4).  It is the sharpest thing in the unit and it is
  exactly right: the frozen-front variant is fully metric-inserted and closes
  **nowhere**, because `ρ = −β` uncancelled.  Insertion without transport buys
  nothing.
- §6.5's wall, and its identification with v2 p10 Prop 10.4's `h^{12}` blindness.
- The honesty architecture: X02, X04, §12's eleven deviations and §13's
  seventeen non-claims are the reason most of my attacks landed on *framing*
  rather than on *claims*.  Several overclaims I went looking for were already
  disclaimed before I got there.

---

## 9. Grade

The primary verdict `HA-RUNNABLE` is **earned and survives hostile
recomputation intact** — 13,068 independently recomputed residuals, zero
discrepancies, at a base front the instrument never used.  GW1's kernel/
deformation block is genuinely lifted: a record-native, lapse-profiled,
invertible, transported comparison family now exists and the residual runs.

The secondary verdict `HA-BRIDGE-NOT-POSABLE` is probably **true** but is
**not established by what §10 says establishes it**.  Two of its three
posability conjuncts are unreachable a priori, its spectrum criterion reads the
wrong spectrum (while the instrument computes the right one), its structure
group is an artifact of the declared prime, and its supporting 17/24 is
vacuous and misdescribed.  Four defects in one section, on a pre-registered
outcome.  None of them is a false physics claim, and the repair for #4 makes the
paper's own conclusion **stronger** — which is why this is a repair and not a
kill.

Findings 1–5 are **mandatory** fixes; §10 must either be reframed as a
structural finding or re-run with a reachable predicate, and the
"measured consequences" sentence must go or be rewritten to the two facts that
survive.  Findings 6–9 are framing repairs that bring headlines down to
mechanisms.  Findings 10–12 are one-sentence additions.

> ## **ACCEPT-WITH-FIXES**

Conditional on: (i) Findings 1–5 discharged in full, with §10.4's obstruction
restated at the strength its surviving evidence supports; (ii) Findings 6–9
discharged as framing repairs, in particular naming which disjunct of GW1's kill
condition fires; (iii) Findings 10–12 carried as declared sentences.  The
`HA-RUNNABLE` half needs no repair and I would accept it as it stands.
