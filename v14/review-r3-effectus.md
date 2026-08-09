# R3 — HOSTILE REVIEW: EFFECTUS / STRUCTURAL LENS (reviewer R2)

**Object:** the frozen R3 delivery — paper `00850cc796d0`, code `bbcc9a1aa7de`,
output `d54142292980`, receipt `1c8beb16c8a2`.  **Protocol:**
`v14/note-r3-hostile-protocol.md` (`c575340216fc`).  **Pin:**
`v14/note-r3-relativity-pin.md` (`a2ac89687a65`).  **Standards:**
`v14/note-r6a-adjudication.md`, `v14/note-r2-adjudication.md`, RUNBOOK §13/§14/§15
with every addendum including both #34 engravings.

**Hash verification.** All four delivery hashes re-verified before work and again
after (§9).  All match.  Scratch-only; no imports from the unit; one repo write
(this file); no git writes.

**Recomputations: ≈159,900** exact-arithmetic cell/bracket/field recomputations in
an independent reimplementation that shares no code with the unit, plus a
≈10⁶-value exact residual sweep behind the eight `max|ρ|` entries, plus a
paper↔output↔receipt number sweep.

**Grade: ACCEPT-WITH-FIXES.**

**Zero false numbers.**  Every number I recomputed matched the delivery exactly —
the full 476-cell closure and coefficient census, all six class counts, all eight
L-sweep rows including all eight `max|ρ|` values (9, 9, 16, 16, 8, 27, 128/9, 48),
the {D,H} tally (10506 / 120 / 10386) reproduced from scratch, the {D,D} 644, the
defect probe counts 3096 / 2280, the control counts 120969 / 58572 / 6144 / 128,
the chart-group orders 32/50/384/750, the L-gate 36-of-36-on-9-sites, and every
derived denominator (476, 21012, 21126, 21420, 198, 62).  This is the campaign's
second clean prose surface.

The fixes are not about arithmetic.  They are about **what the numbers mean**.

---

## 1. Findings, ranked

| # | sev | finding |
|---|---|---|
| F1 | MAJOR | The whole 476-cell closure-and-coefficient census is ANALYTIC — `ρ = (Λ−I)ω`, `c = Λ` — reproduced 476/476 without computing one commutator.  Per #208 the census clauses reclassify as forced. |
| F2 | MAJOR | "Closes" is defined as *equals the metric-inserted generator*.  Hence `closes ⟺ metric-reading` as **sets**, 476/476 — the L-sweep's two columns are one column printed twice, and the paper uses "closes" in two incompatible senses (476/476 in §9.1, 26/99 in §8). |
| F3 | MAJOR | The pin's **RIGID branch is unreachable by construction**: closure ∩ CONSTANT-NON-METRIC = ∅ necessarily.  A three-outcome verdict design whose instrument can return only two. |
| F4 | MAJOR | The register defect is **realization-relative**.  A third realization D-FULL (transport the register too) puts OUTSIDE at **0 of 2926** homogeneous-record brackets (d=2,L=4) and **0 of 360** (d=3,L=4).  §6's "no vanishing sector … a statement about transport, not about curvature" **reverses** there. |
| F5 | MAJOR | **THE COVARIANCE THEOREM (2064/2064, exact):** `D_full[v] ∘ H_g[N] ∘ D_full[v]⁻¹ = H_{S_v g}[S_v N]`; it fails at D-TOT.  The surviving obstruction is exactly `H_{S_v g} ≠ H_g` — **the record does not transport**.  The unit's own symmetry self-test transports the record and finds exact covariance (6144/6144): the control's success and the bracket's failure are one fact seen twice. |
| F6 | MAJOR | The three relations are **not simultaneously realizable on one tangential family**.  Over the full declared lapse family: of 15,228 nonzero {H,H} generators at d=2,L=4, **15,120 (99.29%) do not exist at D-TOT** (non-integral or non-bijective site map); at d=3,L=4, **18,114 of 18,160 (99.75%)**.  **0** are lattice translations, at either arena.  {H,H} closes only at D-REG, where D is central and carries no diffeomorphism content. |
| F7 | MAJOR | The HDA's defining discriminator — the coefficient is a **canonical variable**, which is what makes the algebra open — is **negative here and unlabelled**: `Λ(x)` is read from a fixed background record and the commutator field is configuration-independent (measured). |
| F8 | MAJOR | Relation 3's discriminating content is **absent, not merely forced**: the declared tangential family contains only constant fields, where `[v,w] ≡ 0`.  192 of the 644 brackets involve two distinct nonzero generators and all commute by abelianness. |
| F9 | MODERATE | The measured object in the first bracket is a **central extension** (Heisenberg-type), measured: `H[N]H[M] = T_{w[N,M]}∘H[N+M]`; the "structure coefficient" is the 2-cocycle's antisymmetrization. |
| F10 | MODERATE | L-stability and lapse-scope-inertness are **theorems**, not measurements (the per-cell class is a function of (rule, record) alone). |
| F11 | MODERATE | Denominator inflation ×3, plus exact duplicate rules: A-axis≡B-axis and A-chart≡B-chart everywhere (census rows identical 36/36 each); A-insert≡A-notransport in the {D,H} and defect sectors (18/18, 36/36) — an R6a recurrence. |
| F12 | MODERATE | Three of the five worker flags never reached the paper: the w=1 density-weight flip, the d=3 dense-route gap, the non-constant-tangential exclusion and its reason. |
| F13 | MINOR | The CONTROLS segment's 120969-of-120969 is forced by modular arithmetic and carries no FORCED label; the residual-covariance control's non-vacuity is 128 of 3072 cells (4.2%). |
| F14 | MINOR | d=3, L=3 is excluded from the census although the receipt's own `l_gate` row records `meets_r2_criterion: true` there; a free d=3 L-sweep point was left on the table. |
| F15 | MINOR | Segment scoping gaps (§7). |

---

## 2. K3 — THE HDA CORRESPONDENCE (my primary)

### 2.1 What the Dirac/ADM hypersurface-deformation algebra IS

Three relations on the constraint functions of the ADM phase space
`(q_ij, π^ij)`:

```
{H[N], H[M]} = D[ q^{ij}(N ∂_j M − M ∂_j N) ]        (I)
{D[v], H[N]} = H[ L_v N ]                             (II)
{D[v], D[w]} = D[ [v,w] ]                             (III)
```

Four load-bearing properties, none of them decorative:

1. **(I)'s coefficient `q^{ij}` is a canonical variable.**  The bracket's
   "structure coefficient" is a *function on phase space*, so the HDA is **not a
   Lie algebra** — it is an open/soft algebra (a Lie algebroid over the space of
   metrics).  This is the whole reason the algebra is called *relativity-shaped*:
   the algebra of deformations knows the geometry it deforms, and the geometry is
   dynamical.  Site-dependence alone is not this property; **state-dependence is.**
2. **(III) is nonabelian.**  `[v,w]` is the Lie bracket of vector fields;
   relation (III) says the tangential generators represent `vect(Σ)`.
3. **(II) says `H` is a scalar density of weight one** — that is exactly what
   makes `L_v N` the right right-hand side, and what ties the weight to the
   relation.
4. **The three relations are one structure.**  Their Jacobi identities are not
   independent: `{H,{H,H}}` forces (II)'s Lie-derivative form, and (I)'s sign
   `ε = ±1` is the **signature** (Lorentzian vs Euclidean).  The HDA's physical
   force is the Hojman–Kuchař–Teitelboim representation theorem: the algebra plus
   canonical embedding variables ⟹ Einstein's equations up to two constants.

### 2.2 The correspondence map, object by object

| HDA object | R3's object | verdict |
|---|---|---|
| Poisson bracket on phase-space functionals | **group commutator** `H[N]H[M]H[N]⁻¹H[M]⁻¹` of bijections of a configuration set | **ABSENT** — no symplectic form, no phase space |
| constraint (`H ≈ 0`, first class, generates gauge on a surface) | an invertible map `H_a[N](n,m) = (n+N, m+w[N,n])`; nothing vanishes, no surface | **ABSENT** — "constraint family" is a name, not a constraint |
| `N ∂_j M − M ∂_j N` | `ω_j(x) = N(x)M(x+e_j) − M(x)N(x+e_j) = N Δ_j M − M Δ_j N` | **EXACT** — the exact finite transcription |
| `q^{ij}` as coefficient | `Λ^{ij}(x)`, matched against `I_a(g)=q⁻¹` re-encoded independently | **EXACT IN VALUE** where the rule declares it (X03 owns this) |
| `q^{ij}` as a **structure function** (canonical variable) | `Λ^{ij}(x)` read from a **fixed background record**; the commutator field is **configuration-independent** (measured, and stated in §4) | **ABSENT** — see F7 |
| relation (I) landing | `D_a[Λ^{ij}ω_j]`, empty normal channel, 476/476 | **EXACT IN FORM, FORCED** (X01) |
| relation (II) front sector | `S_vN − N` vs `L_vN`; matches at exactly 1 of 4 conventions, constant `v` only | **EXACT AT CONSTANT v** |
| relation (II) register sector | the defect | **DEFECTS at D-TOT; absorbed on the homogeneous sector at D-FULL** (F4) |
| relation (III) `[v,w]` | only constant fields, where `[v,w] ≡ 0` | **ABSENT in discriminating content** (F8) |
| `q` transported by `D[v]` | no declared generator moves the record | **ABSENT** (F5) |
| signature `ε` | not measured | **ABSENT** |
| density weight of `H` | `w=0` only; the declared `w=1` flip anchored, never swept | **ABSENT** |
| HKT representation leg | not attempted | **ABSENT** (correctly — the paper does not claim it) |

**Verdict per relation.**

- **(I) — EXACT IN FORM, ANALOGICAL IN STATUS.**  The finite bracket covector is
  the exact lattice transcription and the coefficient equals `q⁻¹` where declared;
  but the bracket is a group commutator, the coefficient is a background field,
  and the algebra realized is a **central extension**, not an open algebra.
- **(II) — PARTIAL.**  Front sector EXACT at one convention and at constant `v`;
  register sector defective at D-TOT and inside the basis at D-FULL on the
  homogeneous sector; entirely ABSENT at D-REG.
- **(III) — ABSENT.**  Only the abelian constant-field subfamily is testable, by
  the bijection requirement; the nonabelian core is untested by construction.

### 2.3 What would DISTINGUISH "the discrete HDA" from "a deformation algebra with metric coefficients"

Seven discriminators.  I state each, then whether the unit ran it.

| # | discriminator | ran? | outcome |
|---|---|---|---|
| D1 | **State-dependence of the coefficient.** Vary the dynamical configuration at fixed declarations; the HDA's coefficient must move. | **RUN** | **NEGATIVE.** The commutator field is configuration-independent (the unit's own §4 sentence, verified here: 20/20 pairs, three configurations, identical). The property that makes the HDA an open algebra is measured absent — and read as a convenience rather than as the discriminator. |
| D2 | **Nonabelian (III).** `{D[v],D[w]} = D[[v,w]]` with `[v,w] ≠ 0`. | NOT RUN | Excluded by the bijection requirement. 0 of 644 brackets have `[v,w] ≠ 0`. |
| D3 | **Joint Jacobi.** The three relations' Jacobi identities, which force (II)'s Lie-derivative form from (I). | NOT RUN | The three brackets are censused independently and never tested for mutual consistency. F6 shows they cannot be: the generator (I) produces does not exist in the realization (II) needs — measured over the full declared lapse family, **99.29%** of nonzero generators at d=2,L=4 and **99.75%** at d=3,L=4 admit no D-TOT realization, and **none at all** is a lattice translation. |
| D4 | **Signature `ε`.** The sign of `q⁻¹` in (I). | NOT RUN | The record layer's signature is not measured anywhere in the unit. |
| D5 | **Density weight.** (II) holds because `H` is weight-one. | NOT RUN | `density_weight_flip = 1` is anchored (`P-I7-WEIGHTFLIP`, and it sits in the never-falsified 29) and never swept; the entire census is at `w=0`. |
| D6 | **Coefficient uniqueness/rigidity.** Do other coefficients reproduce the commutators? | **RUN** | **POSITIVE.** The realized bracket covectors span at rank `d` at every site of every cell (my analytic reconstruction matched 476/476, which requires the span to hold everywhere). This is the unit's one genuine HDA-relevant positive measurement. |
| D7 | **Same `q` in both places.** In GR the `q` in (I) is the same `q` whose momentum `H` generates. | NOT RUN | Installed by declaration at the positive control (X03 says so). |

**So: of seven discriminators, one was run and came out positive (D6), one was run
and came out negative but unlabelled (D1), and five were not run.**  The unit's
positive finding rests on D6 plus the coefficient's *value* — and the value is
disclosed as forced.

### 2.4 The closing 26/99 sector — HDA-analog sector or subalgebra artifact?

**Neither.  Membership is characterized exactly and analytically, and it is a
statement about which rules were written down.**

The residual is `ρ = (W − B)·Ω` with `B = I_a(g)` the metric-inserted matrix.
So a cell closes **iff its declared drag weight coincides with the record's
inverse metric at every site**: `Λ_rule(x) ≡ I_record(x)`.  Recomputed
analytically, 476/476, zero exceptions.  The sector enumerates as:

| rule | closes on | why | count (per d=2 arena-scope) |
|---|---|---|---|
| A-insert | all 9 records | `Λ := I` **by declaration** (X03) | 9 |
| A-axis | the 5 diagonal-readout records | `Λ = diag(1/n_{e_j})` and `q_jj = n_{e_j}` ⟹ `Λ = q⁻¹` iff `q` is diagonal | 5 |
| A-insert-x | the same 5 | sign-flipping the cross term is a no-op on a diagonal record ⟹ **identical to A-insert there** | 5 |
| B-axis | the same 5 | **identical weight matrix to A-axis at every site** (verified) | 5 |
| A-chart | G-FLAT | `Λ = δ` equals `q⁻¹` iff `q = δ` | 1 |
| B-chart | G-FLAT | **identical weight matrix to A-chart** | 1 |
|  |  | **total** | **26** |

At d=3: 5 + 3 + 1 = **9**.  I verified independently that A-axis's closure set is
*exactly* the diagonal-readout record set, at both dimensions.

Three consequences.

1. **The sector is a rule-declaration census, not a record-layer measurement.**
   Of its six rows, one is metric-reading by declaration and two are exact
   duplicates of other rows.  The number of *distinct weight matrices* in the
   sector is **3** at each dimension (`q⁻¹`; `diag(1/n_{e_j})`; `δ`).
2. **`closes ⟺ metric-reading` is an identity, not a discovery** (F2).  I verified
   set-equality at 476/476.  The L-sweep table prints it as two columns whose
   eight rows are pairwise identical, without remark.
3. **The death certificate for the naming:** `A-notransport`'s commutator is
   **identically zero** — the most closed an algebra can be — and it is recorded
   as NOT CLOSING at 36 cells (class ZERO, `closes: false`).  A closure column
   that fails the zero algebra is not measuring closure.

### 2.5 The rigid cells

The pin offered three first-class outcomes: metric-reading closure (HDA), constant
closure (**rigid** — "a different, weaker geometry"), or a defect.

**The rigid branch cannot be returned.**  Because closure is *defined* as agreement
with the metric-inserted generator, `closes ∩ CONSTANT-NON-METRIC = ∅` necessarily
— verified: the 140 closing cells are exactly the 140 metric-reading cells, and
all 216 CONSTANT-NON-METRIC cells have nonzero residual.  The only cells that
could be read as "rigid" are the 108 METRIC-READING-CONSTANT ones, and the paper
correctly says those are indistinguishable from metric readings.  So:

> **The discriminating rigid outcome — "closes with a constant coefficient that is
> demonstrably not a metric" — is unreachable by this instrument.**  The pin's
> three-way design is degenerate at two.

This is the single most important structural repair: **the residual must be
defined against the declared generator basis, not against the answer being tested
for.**  A closure test that presupposes its own coefficient cannot distinguish
"the algebra closes with metric coefficients" from "this rule was written with
metric coefficients."

### 2.6 The structure actually measured

What the first bracket exhibits, measured here and not named in the paper:

```
H[N] H[M]  =  T_{w[N,M]} ∘ H[N+M]              (verified 36/36)
[H[N],H[M]] = T_{w[N,M] − w[M,N]}, config-free  (verified 20/20)
register shifts are central at D-REG            (verified)
```

`⟨H[N], D-REG[v]⟩` is a **two-step nilpotent (Heisenberg-type) group**: a central
extension of the abelian group of lapse profiles by the abelian group of register
fields, with 2-cocycle `w[N,M]`.  The "structure coefficient" the unit extracts is
the antisymmetrization of that cocycle.  That is the honest name for the object,
and it is a genuinely interesting one — but a central extension with an
`x`-dependent cocycle is not a hypersurface-deformation algebra, and calling the
coefficient a *structure function* imports a property (state-dependence) that D1
measures absent.

### 2.7 THE FORWARD REQUIREMENTS — what a successor must measure to earn "GR's algebra at scale"

These are written to be pinnable verbatim.  R4-relevant.

- **FR1 — A BRACKET, NOT A GROUP COMMUTATOR.**  Declare a phase space (or a Lie
  algebroid with a named anchor) and compute the relations as brackets on it.
  Gate antisymmetry and the **Jacobi identity**, measured, with a mutant that
  breaks it.  Until then the object is a group, and group commutators of
  bijections are not the HDA.
- **FR2 — THE COEFFICIENT MUST MOVE WITH THE STATE.**  Gate: vary the dynamical
  configuration at fixed declarations and measure that the {H,H} coefficient
  changes.  R3's configuration-independence is the null result this requirement is
  written against.  Operationally this requires the **record counts to enter the
  configuration space**.
- **FR3 — THE RECORD MUST TRANSPORT.**  A tangential generator must act on *all*
  declared fields — front, register **and record**.  R3's covariance theorem
  (`D_full H_g[N] D_full⁻¹ = H_{S_v g}[S_v N]`, 2064/2064) shows the algebra is
  exactly covariant the moment it does; the successor either makes the record
  dynamical or states that its arena carries a **fixed background metric**, in
  which case the HDA is the wrong target and must not be named.
- **FR4 — NONABELIAN TANGENTIAL GENERATORS.**  Declare a tangential family closed
  under a nonvanishing bracket — e.g. lattice vector fields realized by partial
  bijections / a groupoid action rather than by `x ↦ x+v(x)` — and measure
  `{D[v],D[w]} = D[[v,w]]` with `[v,w] ≠ 0` at a stated fraction of the census.
  Report that fraction; if it is 0, relation (III) is not tested.
- **FR5 — ONE ALGEBRA, ONE REALIZATION.**  Gate that the generator produced by (I)
  **is an element of the family used in (II) and (III)**.  R3 fails this at
  99.29% (d=2,L=4) and 99.75% (d=3,L=4) of its own nonzero generators, and the
  failure is invisible in the delivery.  A three-relation claim requires a single
  realization in which all three brackets are defined.
- **FR6 — THE SAME `q` IN BOTH PLACES.**  Gate that the metric read off the {H,H}
  coefficient is the *same datum* as the metric appearing in `H`'s own definition,
  as a measured identity rather than a declaration (X03 currently installs it).
- **FR7 — SIGNATURE.**  Measure `ε` in `{H,H} = ε D[q⁻¹(N dM − M dN)]` and its
  stability across records.  A relativity-shaped claim that does not know its own
  signature is incomplete.
- **FR8 — DENSITY WEIGHT SWEPT, NOT ANCHORED.**  Sweep `w ∈ {0,1}` (both are
  declared) and gate the weight at which (II)'s front sector holds.
- **FR9 — A RIGID OUTCOME THAT CAN WIN.**  Define the residual against the
  **declared generator basis**, so that "closes with a constant non-metric
  coefficient" is a reachable verdict.  Ship the injection that returns it.
- **FR10 — SCALE, OR SILENCE ABOUT SCALE.**  "At scale" requires the relations to
  survive a refinement direction.  R1's terminal closes that door; until it
  reopens, the requirement is to carry the finite-extent scope **at the claim**,
  not only in a scope box.
- **FR11 — THE REPRESENTATION LEG, NAMED.**  The HDA's force is HKT: algebra +
  canonical embedding variables ⟹ Einstein up to two constants, and the corpus's
  own paper 57 already proves `G` un-fixable here (`κ·σ_A = G·Λ² = const`).  A
  successor must state which leg it attempts and which it concedes.

---

## 3. K1 (structural side) — what the unit's real contribution is

**The derivability theorem lands.**  I reconstructed the entire census from the
declarations alone:

- The residual is `ρ(x) = (W_rule(x) − I_record(x))·Ω(x)`.  Closure ⟺ `W ≡ I`.
- The extraction solves `Δ^i = Σ_j c^{ij} ω_j` with `Δ = W·Ω`; on architecture A
  the axis block of `W` **is** `Λ`, so `c = Λ` whenever the covectors span.
- Therefore the coefficient class is the function
  `class = f(Λ, I) ∈ {ZERO, METRIC-READING-{CONSTANT, SITE-VARYING},
  {CONSTANT, SITE-VARYING}-NON-METRIC}`, plus NOT-EXTRACTABLE whenever the rule
  populates a diagonal-link column (architecture B with `λ_diag ≠ 0`, i.e. B-all).

Recomputed with no commutator anywhere: **476/476 closure statuses, 476/476
coefficient classes, all six class totals (216/108/32/36/48/36), all eight L-sweep
rows.**

**Per #208 the following clauses reclassify as FORCED:** the closure census, the
coefficient-class census, the six class counts, the 26/9 closing counts, the
"32 of 120", the "56 of 56", the LSWEEP segment's constancy claims, and the
LAPSE segment's "coefficient class moves at 0 cells".  X03 already concedes the
positive control's *value*; the correct scope of that concession is **the whole
census**, not one rule.

**What remains genuinely measured (this is the unit's real contribution):**

1. **Identifiability** — the realized bracket covectors span at rank `d` at every
   site of every cell.  This is D6, the one HDA-relevant positive, and it is what
   makes `c = Λ` a *determination* rather than a *reading*.  It should be the
   COEFFICIENT segment's headline.
2. **The arch-B non-extractability**, with the arch-A control (X05 owns the
   forcing; the control is real).
3. **The residual magnitudes** `max|ρ|` — the only quantity in the census that
   actually moves along `L` and along the lapse coordinate (9→16 at d=2;
   8→27→128/9→48 at d=3), and the 62 magnitude-moving cells.
4. **The {D,H} sector in full** — closed forms verified against literal
   composition, the convention decision, the defect's closed form.
5. **The arena and controls** — the L-gate reproduction, the chart-group orders by
   explicit closure, the scrambled negative control.
6. **The machinery recovery** (99/99, 72/72, two-route record-IS-metric).

**The site-variation question's meaning.**  "Is the coefficient site-varying?" is,
after the theorem, the question "**does the declared rule read an inhomogeneous
record?**"  It is answered by `Λ`'s dependence on `x`, which is a property of the
rule's declaration composed with the record's inhomogeneity — not a property of
the algebra.  So the protocol's K1(d) is answered: **yes, SITE-VARYING is
trivially inherited from record inhomogeneity for any record-reading rule.**  Any
inhomogeneous record forces it at A-insert, A-axis, A-insert-x, B-axis,
A-linkframe, A-linkhalf, A-insert-2x — every rule except the two count-blind ones.
The 32-of-120 count is therefore **the count of (rule, inhomogeneous-record) pairs
at which the declared weight happens to equal `q⁻¹`** — realized at exactly four
rules, three of which reduce to two distinct matrices.  The COEFFICIENT segment
must carry that rule scope.

---

## 4. K2 (structural side) — the defect's ontological status

### 4.1 The realization census (the hunt the protocol ordered)

The pin declares the tangential family "at the two declared realisations D-REG and
D-TOT", inherited verbatim from I7:

> **D-REG** — "`D_a[v]` shifts the **matter record's address register** by `v`; the
> **geometry front** is not transported (primary)"
> **D-TOT** — "shifts the register **AND** drags the front along `x → x+v(x)`"

Read these carefully.  **D-TOT pulls the geometry front back and shifts the matter
register by a constant.**  It transports one field and increments the other.  That
asymmetry is D-TOT's definition — and the defect the unit measures sits *exactly*
in the untransported sector.  "Matter does not follow geometry's deformations" is
therefore not a discovery; **it is a restatement of the realization's declaration.**

I enumerated the realization space.  There is a third realization built from the
identical declared ingredients — the site map and the register shift — namely the
one in which the register transports too:

```
D-FULL[v] : (n, m) ↦ (S_v n, S_v m + v)
```

Measured, at the unit's own membership criterion, its own three declared
configurations, its own lapse probe and its own translation generators:

| arena | realization | IDENTITY | IN-EXTENDED | OUTSIDE | **OUTSIDE on homogeneous records** |
|---|---|---|---|---|---|
| d=2, L=4 | D-REG | 3762 | 0 | 0 | 0 |
| d=2, L=4 | D-TOT | 0 | 0 | 3762 | **2926** |
| d=2, L=4 | **D-FULL** | 324 | 2754 | 684 | **0 of 2926** |
| d=3, L=4 | D-REG | 600 | 0 | 0 | 0 |
| d=3, L=4 | D-TOT | 60 | 0 | 540 | **324** |
| d=3, L=4 | **D-FULL** | 135 | 315 | 150 | **0 of 360** |

(My D-REG and D-TOT figures reproduce the delivered tally exactly: summed over the
four arenas they give 10506 / 120 / 10386.)

**At D-FULL every OUTSIDE cell is on an inhomogeneous record.**  The IN-EXTENDED
cells decompose exactly:

- deviation from `H[P]` is **configuration-independent** at every homogeneous cell
  (verified 418/418) and equals **`−w[S_vN − N, N]`** exactly — a fixed tangential
  field, hence `H[P]∘D[u]`, which is *inside* the unit's own declared basis;
- the IDENTITY count decomposes exactly: 7 homogeneous records × 11 rules × 2
  directions × 2 translation-invariant lapses = **308**, plus the two count-blind
  rules on the two inhomogeneous records = **16**, total **324** — reproduced;
- the IN-EXTENDED count on inhomogeneous records is exactly the count-blind rules:
  2 records × 2 rules × 19 lapses × 2 directions − 16 = **136** — reproduced.

### 4.2 The mechanism (F5), proved

```
D_full[v] ∘ H_g[N] ∘ D_full[v]⁻¹  =  H_{S_v g}[S_v N]      exactly
```

verified at **2064 of 2064** (rule × record × lapse × direction × configuration)
comparisons, and **failing** at D-TOT.  Because `W_{S_v g}(x) = W_g(x−v)`, the
conjugated constraint is the constraint *of the transported record*.  Hence:

- record homogeneous, or rule count-blind ⟹ `S_v g = g` ⟹ the bracket is
  `H[S_vN − N] ∘ D[u]` with `u` fixed ⟹ **inside the basis**;
- record inhomogeneous with a record-reading rule ⟹ the bracket compares **two
  different constraint families** ⟹ OUTSIDE.

**So the realization-robust residue of the defect is: `H_{S_v g} ≠ H_g` — the
record does not transport.**  The metric datum is not in the configuration space
and no declared generator moves it.  In ADM, `D[v]` moves `q_ij`; here nothing
does.

The unit's own instrument already knows this.  `translation_covariance_of_the_
residual` transports the record (`recu.counts = rec.counts[x−u]`) and finds
**exact covariance at 6144 of 6144 cells**.  The symmetry self-test's success and
the {D,H} bracket's failure are the same fact seen from two sides — and the unit
reports them 30 lines apart without connecting them.

### 4.3 At what strength the reading may be carried

**Not a candidate deviation-from-GR object.  Not (quite) a realization artifact
either.  A GRAMMAR FACT, carried at a stated scope.**

The honest carriable statement:

> At finite extent, at `w = 0`, at the declared realization D-TOT, the
> normal-tangential bracket's register sector lies outside the declared generator
> basis at every probe, with the exact closed form
> `w[N,(S_{-v}−1)(n−N)] − w[S_vN−N, n]`.  The obstruction is realization-relative:
> at the realization that transports the register as well as the front it vanishes
> from the basis-membership test on the entire homogeneous sector, and what
> survives is exactly the failure of the geometry record to transport —
> `D H_g D⁻¹ = H_{S_v g}`, exactly.  The declared arena carries a **fixed
> background metric**, and this bracket is the instrument that detects it.

That is a real and useful result.  It is not "matter does not follow geometry's
deformations"; it is "**this arena has a background, and here is the exact
functional that measures it.**"

**The v12 defect precedent does NOT transfer.**  Δᴮ earned its status because it
survived a realization/relabelling hunt (the W-batch's six-for-six, paper 1's
369/369 bundle, the wing-exchange orbit analysis), and because it was a defect of a
composition both sides of the arena agreed on.  The register defect is a defect of
an **asymmetric transport whose alternatives the unit did not enumerate** — the
pin named two realizations and the unit censused exactly those two, one of which
is vacuous.  Under RUNBOOK §15 ("claims of physical significance are entered only
for quantities gated as invariant across the unit's admissible arenas;
arena-artifacts may serve as instruments but never as conclusions"), the defect is
an **instrument**, and an excellent one.  It is not yet a conclusion.

Four of the paper's headline properties must be re-scoped or corrected:

| §6 claim | status |
|---|---|
| "It never vanishes" | TRUE, D-TOT-scoped, one-configuration/six-lapse probe |
| "It is not a boundary term" | TRUE, same scope; the degenerate-probe death certificate is good practice |
| "**It has no vanishing sector** … The defect is a statement about **transport, not about curvature**" | **REVERSES at D-FULL**: there it vanishes from the basis test on the whole homogeneous sector and is *precisely* about curvature (record inhomogeneity).  Must be re-scoped and the reversal reported. |
| "It is L- and d-independent" | TRUE, and now explained: the mechanism is a per-site weight comparison, which is extent-free |

---

## 5. K4 — scope

**The five flags, by materiality.**

1. **`w = 1` anchored, not swept — MATERIAL, and absent from the paper.**  The
   density weight is the property that makes relation (II) hold (D5/FR8).  The
   entire census is at `w = 0`; `P-I7-WEIGHTFLIP` sits in the never-falsified 29 as
   an anchor for a test that is never run.  The paper never states the weight
   scope.  The ARENA segment must carry `WEIGHT=0`.
2. **The d=3 dense-route sparsity — MATERIAL, and absent from the paper.**  The
   dense cross-route runs at `DENSE_ARENAS = ((2,4),(2,5))` and BASE only: **0 of
   the 40 d=3 census cells** have a second route.  The paper says "the dense route
   cross-checks 198 cells" with no scope; the receipt carries `dense_arenas` but
   the paper does not.  198 = 2 × 99, verified.  Repair: state the coverage
   fraction at the claim, or run d=3.
3. **The {D,H} d=3 lapse scope (X07) — DISCLOSED, and correctly.**  Immaterial to
   the verdict: the defect is present at every probe and the mechanism is per-site.
4. **The non-constant tangential exclusion — MATERIAL, and absent from the
   paper.**  This is the load-bearing one.  It is not merely a restriction on the
   defect claim; it is what makes **relation (III) contentless** (F8) and what
   makes the first bracket's own generator unrealizable (F6) — measured over the
   full declared lapse family at 15,120 of 15,228 nonzero generators (d=2,L=4)
   and 18,114 of 18,160 (d=3,L=4), with **zero** lattice-translation generators at
   either arena.  The word "bijection" does not occur in the paper.  Repair: a
   disclosure X08 stating the exclusion, its reason, and its two costs.
5. **The TRANSLATES enlargement — DISCLOSED, well handled**, printed as arena data
   and carried as a named verdict coordinate.  Correct §15 practice.

**Is L-stability a theorem?  YES — and so is lapse-scope inertness.**  The
per-cell closure condition `Λ(x) = I(x)` and the coefficient class are functions of
`(rule, record)` alone.  Neither `L` nor the lapse family appears.  Hence
"closing-cell count and coefficient census constant in `L`" and
"COEFFICIENT-CLASS-MOVES-AT-0-CELLS" are **forced**, and the epistemic label of the
L-sweep's *structural* columns must change from measured to forced (#208).

What survives as measurement in the L-sweep: **`max|ρ|` alone** — and it does move
(9, 16 at d=2; 8, 27, 128/9, 48 at d=3), all eight reproduced.  The sweep's honest
headline is therefore: *the structure is extent-free by construction; the anomaly's
size is not.*  That is still worth reporting — it is just a different claim.

**Denominator inflation (F11).**  Three instances, all recomputed:

- **Convention sweep.**  Reported `21126`; the front sector provably depends on
  neither the record nor the rule (the unit gates exactly that), so the distinct
  front-sector computations number **685** — a **30.8×** record×rule multiplicity.
  The "1 of 4" conclusion is sound; the denominators are copies.
- **{D,H}.**  `10506` of the `21012` brackets are the D-REG branch, which is a
  hard-coded `return "IDENTITY", None` — the count is computed, the value is
  typed.  X02 owns the forcing; the *presentation* as a measured tally does not.
- **{D,D}.**  Of `644`, only **192** involve two distinct nonzero generators, and
  all commute by abelianness; **452** involve a zero or repeated generator.

**Exact duplicate rules.**  A-axis ≡ B-axis and A-chart ≡ B-chart as weight
matrices at every site of every record (census rows identical at 36/36 each);
A-insert ≡ A-notransport in the drag used by `H`'s register action, hence identical
{D,H} rows (36/36) and identical defect rows (18/18).  This is a **recurrence of
the R6a finding** (`A-notransport` implemented identically to `A-insert`) and under
the #313 engraving a recurrence is a MAJOR by default; here it is MODERATE because
the two rules *are* distinct in the {H,H} sector (frozen front ⟹ `W = 0`), so the
duplication is sector-local.  Effective distinct rules: 9 of 11 in {H,H}, 8 of 11
in {D,H} and the defect.

---

## 6. K5 — do the 14 segments carry every measured restriction?

**Mostly yes on forcing; no on scope.**  The unit is unusually good at forced
labels (X01–X05 are in the segments) and at the realization dichotomy.  The gaps:

| segment | missing restriction |
|---|---|
| ARENA | the density weight (`w=0` only); which records are the declared d=3 extension (X06 carries it, the segment does not) |
| L-GATE | that d=3,L=3 is also excluded from the census though the receipt's own row records `meets_r2_criterion: true` |
| COEFFICIENT | **rule scope** — the 32/120 is realized at exactly four rules (A-insert, A-axis, A-insert-x, B-axis), three of which reduce to two distinct matrices; and the analytic identity `closes ⟺ metric-reading` |
| HH-RESIDUAL | that the "residual" is measured against the metric-inserted generator, not against the declared basis |
| DEFECT | **realization scope (D-TOT)** on all four properties; the probe scope (one configuration, six lapses, `d` directions); the D-FULL reversal |
| DD-BRACKET | that only constant fields are in the family, and that `[v,w] ≡ 0` there — so the relation's content is absent, not merely forced |
| CONVENTION | that the front sector is record- and rule-independent, so 21126 is 685 × 30.8 |
| LSWEEP | that the structural constancy is forced, not measured |
| CONTROLS | that 120969-of-120969 is forced by modular arithmetic; the residual-covariance non-vacuity (128 of 3072) |

The five verdict-injection classes, the comparator's independence, and the
never-falsified census are the instrument reviewer's; I note only that
`P-I7-WEIGHTFLIP` and `G-CONVENTION-RULE-INDEPENDENT` appear in the
never-falsified 29 and both bear on findings above.

---

## 7. THE R4 QUESTION — is the register defect the right seed?

**Recommendation: NO.  Seed R4 from Δᴮ (v12's composition defect).  Carry the
register defect into R4 as a second-layer instrument — specifically as a
realization gate — not as the seed.**

Five measured reasons.

1. **It fails the realization census.**  A realization built from the same declared
   ingredients absorbs it on the entire homogeneous sector (0 of 2926 and 0 of 360
   OUTSIDE).  A seed for an interaction law must be invariant across the arena's
   admissible realizations; this one is not (§15).
2. **Its signature property inverts.**  "No vanishing sector — a statement about
   transport, not curvature" becomes "vanishes on the whole homogeneous sector — a
   statement about curvature" one realization over.  A defect whose defining
   property flips cannot carry a dynamical law.
3. **What survives is a background, not an interaction.**  The realization-robust
   residue is `D H_g D⁻¹ = H_{S_v g}` — the record does not transport.  The
   correct response is FR2/FR3 (make the record dynamical), not to build
   interactions on the obstruction.  Seeding interactions from it would encode a
   fixed background into the interaction law.
4. **Δᴮ has already fought this fight.**  v12's composition defect survived a
   realization/relabelling hunt, is a defect of a *composition* (which is what an
   interaction is), and is terminal-publishable at paper-1 scope.  It is a defect
   of the law, not of the bookkeeping.
5. **The register defect's real value is diagnostic, and it is high.**  It has an
   exact closed form, it is cheap, it is `L`- and `d`-independent, and it detects
   with precision **which declared fields a declared generator transports**.  That
   is exactly the gate R4 needs before any of its own defects are read as physics.

**Concrete R4 shape I recommend the adjudicator pin:**

- **Seed:** Δᴮ, the composition defect, at its v12 scope, with the composition
  declared as arena data.
- **Second layer (this unit's product):** the **realization census gate** — every
  R4 interaction generator is run through a D-REG / D-TOT / D-FULL-style
  enumeration of *which declared fields it transports*, and its defect is reported
  per realization with the invariant residue named.  No defect enters an R4 verdict
  head without that census.  R3's own numbers ship as the gate's positive and
  negative controls (D-TOT: 10386 OUTSIDE; D-FULL: 0 OUTSIDE on the homogeneous
  sector; the covariance theorem 2064/2064 as the closed form the gate checks
  against).
- **Third layer:** the register defect as a **background detector** — if an R4
  arena is meant to have no background, this functional must vanish; if it does
  not, the arena has one and the unit says where.

---

## 8. Binding repairs (structural side)

1. **Rename and redefine the residual.**  The census's `ρ = (W − I)·Ω` measures
   *deviation from the metric-inserted generator*, not failure to close.  Rename
   the column (HDA-AGREEMENT / METRIC-MATCH), and **add** a genuine
   basis-membership residual measured against the declared generator basis, so the
   pin's RIGID branch becomes reachable (FR9).  Ship the injection that returns it.
2. **Carry the census at its forced label** (#208): closure statuses, all six class
   counts, the 26/9, the 56/56, the 32/120, LSWEEP's constancy, LAPSE's "0 moved".
   Promote **identifiability (rank `d` at every site)** to the COEFFICIENT
   segment's headline — it is the measured content.
3. **Fix the two senses of "closes."**  §9.1's "closes … at every census cell" and
   §8's "26 of 99" cannot share a word.  Add the `A-notransport` death certificate
   (a zero commutator recorded as non-closing) as the demonstration.
4. **Ship the realization census.**  Add D-FULL as a measured third realization
   with the table of §4.1, the covariance theorem as a gated in-unit result, and
   the four §6 properties re-scoped to D-TOT with the reversal reported.  Correct
   "a statement about transport, not about curvature."
5. **Name the mechanism.**  Replace §6's front-difference story with: *the declared
   realizations transport a proper subset of the declared fields; the record — the
   metric datum — is transported by none of them; the bracket measures exactly
   that.*  Cite the unit's own covariance control (6144/6144) as the other side of
   the same fact.
6. **Add disclosure X08** (the non-constant tangential exclusion, its bijection
   reason, and its two costs: relation (III) contentless; the first bracket's own
   generator unrealizable at D-TOT at 99.29% / 99.75%) and **X09** (weight `w=0` only;
   `w=1` declared and not swept).  Print the d=3 dense-route coverage at the claim.
7. **Honest denominators**: the convention sweep's 685 distinct computations
   printed beside 21126; the D-REG 10506 marked as a forced branch rather than a
   tally; the {D,D} 192-of-644 informative count printed; the three duplicate rule
   pairs named with the effective distinct-rule counts (9 / 8 of 11).
8. **Label the forced control.**  `120969 of 120969` is `(x+u)+l = (x+l)+u`; it is
   as forced as X04 and should say so.  Print the residual-covariance non-vacuity
   (128 of 3072) at the claim.
9. **Segment scope tags** per §6's table — above all `REALISATION=D-TOT` inside the
   DEFECT segment and the rule scope inside COEFFICIENT.
10. **Paper rewrite, single-threaded** (RUNBOOK §9): the finding is *(a)* the
    defect head, correctly scoped and correctly mechanized as the record's
    non-transport, with the covariance theorem as its exact converse; *(b)* the
    census as a theorem with identifiability as its measured residue; *(c)* the
    HDA correspondence map of §2.2 with its ABSENT entries stated; *(d)* the
    forward requirements FR1–FR11 as the successor's inputs.  No correction
    narrative.

---

## 9. Recomputation ledger, and re-verification

| block | what | count |
|---|---|---|
| A | closure + coefficient class, analytic, per cell | 952 |
| A | class totals, set-equality, positive control, inhomogeneity, trajectory | 51 |
| B | closure sets by rule; diagonal-readout sets; duplicate-rule sweeps | 9 |
| C | eight `max|ρ|` values (exact max over every realized bracket-covector pair) | 8 verdicts over ≈10⁶ exact residual values |
| D | central-extension identity; commutator = antisymmetrized cocycle; centrality | 57 |
| E | realization census D-REG / D-TOT / D-FULL, two arenas | 13,086 |
| F | covariance theorem (2064) + defect fields at two realizations (3096) + 6 | 5,166 |
| G | convention/DD/defect/census duplicate denominators; L-gate; chart group | 566 |
| H | D-TOT realizability of the {H,H} generator (15,048 sampled + 124,978 full-family) | 140,026 |
| — | paper↔output↔receipt number sweep and derived denominators | ≈65 |
| | **total** | **≈159,900** |

**Hashes re-verified after all work** (`shasum -a 256`):

```
00850cc796d0…  v14/paper-03-relativity-rung.md
bbcc9a1aa7de…  v14/code/r3_relativity_exact.py
d54142292980…  v14/code/r3_relativity_output.txt
1c8beb16c8a2…  v14/code/r3_relativity_receipt.json
c575340216fc…  v14/note-r3-hostile-protocol.md
a2ac89687a65…  v14/note-r3-relativity-pin.md
```

All unchanged.  One repo write: this file.

---

## 10. Grade

**ACCEPT-WITH-FIXES.**

The verdict head is right: the defect head is the honest head, and the unit chose
it over the positive.  The arithmetic is clean — every number I recomputed matched,
and an independent reimplementation reproduced the {D,H} tally, the eight `max|ρ|`
values and the whole 476-cell census exactly.  The disclosures X01–X07 are the best
forced-clause practice in v14 to date.  The arena, the controls, the closed forms
and the convention decision all survive.

What does not survive is the **anatomy**: the census's positive finding is analytic
and mislabelled as measured; "closure" is defined as agreement with the answer,
which makes the pin's rigid branch unreachable and makes `closes ⟺ metric-reading`
a tautology; the defect's headline property reverses under a realization the unit
did not enumerate; and the three brackets are not simultaneously realizable, so
"two of the three reproduced" sums two incompatible realizations.

That is the R6a pattern — verdict holds, mechanism rewritten — and it is
ACCEPT-WITH-FIXES, not REJECT.  The repairs are definite and are listed in §8.  The
forward requirements in §2.7 and the R4 recommendation in §7 are the parts I most
want carried into the adjudicator's next pin.
