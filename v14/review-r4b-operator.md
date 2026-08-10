# R4b (paper-15, momentum) — OPERATOR-LENS HOSTILE REVIEW

**Grade: AWF (accept with fixes).**

**Object, hashes verified at read time and again at write time:**
paper `v14/paper-15-momentum.md` `5f8ec142319c`, code
`v14/code/r4b_momentum_exact.py` `53a10e87ec19`, output `d33412225949`,
receipt `00e7f6ea0f90`, all at commit `10c8d17`; pin
`v14/note-r4b-momentum-pin.md` `bcd12bbe6fd8`; protocol
`v14/note-r4b-hostile-protocol.md` `b9cd2133d961`. Parent at `583cae7`:
paper `1063401c7bb5`, code `2959c5a6a84b`, output `ffd069ff3eb4`, receipt
`3dc1393b0df8`. Frozen panel files: `review-r4-effectus.md` `f54fa11dfd07`,
`review-r4-operator.md` `3828376b49a6`, `note-r4-adjudication.md`
`3b00a9481b28`. All eight of the unit's declared runtime sources hash-match
their declarations exactly.

**Recomputations: 92**, all exact-arithmetic, all against a from-scratch
rebuild that imports nothing from the unit. **Zero false numbers found.**
Every delivered number in the paper, the output and the receipt reproduces
exactly. All findings below are scope, claim-vs-predicate, or
reading-relativity findings; **not one of them moves a computed value.**

**Disclosure.** Concurrent workers are active in this repo. HEAD moved from
`0d73569` to `a0992ef` during this review (u4 delivery + protocol + orchestrator
rows, and the sibling R4b effectus review). The working tree carries the w2
worker's uncommitted `v14/code/w2_census_{exact.py,output.txt,receipt.json}`
and `v14/paper-13-weld2-carrier-census.md` — none of them mine, none of them
read. Every file I read was read through `git show` at its pinned commit; I
read no uncommitted state. I have **not** read `review-r4b-effectus.md` or
`review-r4b-instrument.md`; everything below is from my own rebuild. My only
repository write is this file.

---

## 1. What I rebuilt differently

The protocol asks this lens for a from-scratch rebuild importing nothing, with
different primitives and different routes. What I built:

**A different field representation.** The unit carries Q(ζ₈) as four-tuples of
rationals in the basis (1, ζ₈, ζ₈², ζ₈³). I carry it as
Q(i)(√2) — four-tuples in the basis **(1, i, √2, i√2)**, with multiplication
factored as (u + v√2)(u′ + v′√2) = (uu′ + 2vv′) + (uv′ + vu′)√2 over Q(i).
Different structure constants, different code path, different canonical forms.
The unit's rows are converted into my basis only at the matching step, by
(p₀,p₁,p₂,p₃) ↦ (p₀, p₂, (p₁−p₃)/2, (p₁+p₃)/2).

**Two sweep routes for the family, not one.** Route A treats the stencil as a
**set** {0, a, −a} (2 distinct offsets at an order-2 axis, 3 at order 4) and
sweeps alphabet-valued maps on it. Route B reproduces the unit's own route —
`product(alphabet, repeat=3)` with the two ± entries **added** when a = −a,
which at the three order-2 axes admits coefficients from the *sumset* of the
alphabet, a strictly larger value set than the declared 25. I ran both.
**They yield the identical 58 generators** (`routes_identical: true`); the
sumset admits no extra unitary. The unit's route is therefore harmless, but it
is not the declared alphabet at three of nine axes, and only a computation
shows that this does not matter. Worth an in-code sentence.

**Three diagonalisation routes, two of which never touch the symbol.**
- *Route 1 — M⁸ = I.* For each of the 58 generators I formed the 16×16 matrix
  exactly and computed M⁸ by repeated multiplication. **58 of 58 give exactly
  the identity**, which proves every eigenvalue lies in μ₈ without computing a
  single symbol and without any Kronecker argument.
- *Route 2 — trace inversion.* From the exact traces tr(M^j), j = 0…7, I
  recovered the eigenphase multiplicities by m_t = (1/8)·Σ_j tr(M^j)·ζ₈^{−jt},
  checking that each came out a non-negative rational integer (it did, every
  time). **The multiset from the traces equals the multiset from the symbol for
  all 58 families** — a second symbol-free confirmation, this one of the
  dispersion's *content*, not just its home.
- *Route 3 — full conjugation.* Rather than checking Mχ_k = λ(k)χ_k column by
  column as the unit does, I formed Λ = (1/16)·F†MF as a complete 16×16 matrix
  product (having first verified F†F = 16·I exactly). **All off-diagonal entries
  vanish for all 58 families**, and the diagonal equals the symbol at all
  **928** cells. The same construction applied to the six controls gives
  **non-zero off-diagonal entries for all six** — 16 each for the four
  brickwork, 60 and 24 for the two scrambled — so the not-Bloch-diagonal claim
  is measured by a route that would have exhibited the diagonalisation had one
  existed, not merely by a failed test.

**Independent identification.** My families are matched to the unit's C-names
purely by *content*: coefficient map modulo the global phase, in both
directions. The match is a bijection, 58 for 58, unmatched 0; and for every
matched pair the axis, axis order, support, radius, monomiality, the full
16-vector eigenphase and the full 16-vector reduced dispersion agree —
`invariant_or_dispersion_mismatch: []`.

**Off-tree, git-less reproduction.** I built a bare directory containing only
the ten files the unit reads, with no `.git` anywhere, and ran the committed
instrument there. Both artifacts came out **byte-identical to the committed
ones** (`d33412225949`, `00e7f6ea0f90`). A second plain run with
`PYTHONHASHSEED=12345` reproduced the same two hashes, so the determinism
survives set-iteration reordering. The `--selftest` died at `G-BYTE-ANCHORS`
and wrote nothing; five targeted mutants (`MUT-IDENTITY`, `MUT-DRIFT-TABLE`,
`MUT-ALIAS`, `MUT-MU8`, `MUT-NOTBLOCH`) each died at their declared gate; and
the artifacts were unchanged after all diagnostic runs.

**The thirteen verbatim windows, checked against bytes.** I extracted the
declared `VERBATIM_ANCHORS` literal and searched each window in its pinned
source. **All 13 occur exactly once**, none zero times and none ambiguously.
The `VB-DRIFT-TABLE` window is the frozen effectus table character for
character.

---

## 2. K1 — the census

Everything in K1 reproduces. Measured independently:

| object | delivered | my rebuild |
|---|---|---|
| axes (offset, order, radius) | 9 rows | identical 9 rows |
| pool | 58 circulants | 58, by two sweep routes, identical sets |
| gauge orbits | free | every orbit size 8 |
| monomial / interfering | 16 / 42 | 16 / 42 |
| support histogram | 16 / 18 / 24 | 16 / 18 / 24 |
| census cells | 928 | 928 |
| eigen-equation verified | 928 | 928 (full conjugation) |
| eigenvalues in μ₈ | 928 | 928, plus M⁸ = I at 58 of 58 |
| exact unit modulus | 928 | 928 |
| parity a family invariant | 58 of 58 | 58 of 58 |
| non-constant dispersions | 57 of 58 | 57, the exception C004 |
| distinct reduced profiles | 58 | 58 (and 58 distinct raw profiles) |
| controls not Bloch diagonal | 6 of 6, 3 classes | 6 of 6, none circulant |
| translation stabilisers | 16 circulant, 8 brickwork | 16 (exact) / 8 (exact and gauge) |

Two things I add that the unit does not report. The scrambled controls'
translation stabilisers are **1 and 2**, not merely "< 16" — the gate's
`all(x < len(sites))` is satisfied with room to spare, and printing the two
values would make §5's "fixes no control" a sharper sentence. And at the
delivered gauge every one of the 928 eigenphases is **even** — the exponents
occurring are exactly {0, 2, 4, 6}, so the census populates four of the eight
values of Z/8 and every eigenvalue is in fact a *fourth* root of unity. This is
not an error: the eigenphase is gauge-covariant, multiplying a generator by ζ₈
moves the exponents off the even sublattice, so **μ₈ is the correct
gauge-invariant statement** and μ₄ is not gauge-stable. It is the same fact as
the parity invariant, seen from the other side, and one sentence in §3 would
tie them together.

The Kronecker paragraph has a gap — MINOR-3 below.

---

## 3. K2 — the motion census (decisive)

**Everything reproduces, including both halves of the convention-selection
claim.**

- **C004 is the identity.** Its matrix is exactly ζ₈⁴·I = −I; support 1,
  radius 0, reduced dispersion identically zero. Two-way: it is the unique
  constant family and the unique zero-speed family.
- **MOVING 57 of 58**, by both routes (non-constant reduced dispersion; some
  non-zero cell speed), and the two routes agree on **every** one of the 58.
- **Per-class v_max.** My 22 class rows reproduce the paper's table exactly —
  sizes, supports, radii, v_max, aliased counts (32, 32, 64, 64, 96, 32) and
  the `profiles` column (4, 4, 2, 1 …). v_max and the head are constant on
  every class, measured class by class. 18 circulant classes MOVE, 1 STATIC,
  3 NOT-BLOCH-DIAGONAL.
- **Aliasing.** 320 of 1856 cells, in exactly 19 of 58 families; the 19 are
  exactly the v_max = 2 families, and 32+32+64+64+96+32 = 320.
- **The fiber table.** All nine entries reproduce: 1856 / 1088 / 832 / 1536 /
  768 / 1536 / 768 / 704 / 704. (My CENTRAL uses the ½-step normalisation
  v = −lift(Δ)/4; the unnormalised variant would give 1088 / 832 / 832, so the
  unit's central difference is the normalised one, correctly.)
- **The tie is the whole ambiguity**: at the declared stencil the other two
  lifts agree with the declared one at exactly the non-aliased cells and
  disagree at exactly the aliased ones, cell by cell.
- **THE CONVENTION-SELECTION CLAIM, half (i).** My 3×3 agreement matrix is
  **identical** to the delivered one: 58 / 39 / 39 / 33 / 25 / 32 / 33 / 32 /
  25. Exactly one lift pair reaches 58 of 58; the best other is 39 of 58.
- **THE CONVENTION-SELECTION CLAIM, half (ii).** Under the tie-averaged
  reading my support-classified drift table is **16 | 12, 18 | 0, 24 | 0** —
  character for character the table frozen in `review-r4-effectus.md`
  `f54fa11dfd07`, which I read at its pinned hash. Under the positive reading
  it is **16 | 15, 18 | 10, 24 | 8**, exactly as §7 says. I also computed the
  negative reading, which the unit does not: **16 | 15, 18 | 10, 24 | 8** as
  well, so §7's "and only under it" is *true* across all three readings — and
  ungated (MINOR-4).

Two decompositions the unit does not print, both of which bear on how much the
identity is worth:

*Where the 58 lives.* Splitting the agreement matrix by monomiality, the
declared pair scores 16 (monomial) + 42 (interfering). The 42 agree because
both sides are **zero**. So the identity's evidential weight is 42 zero-versus-
zero coincidences plus 16 genuine monomial matches; under `TIE|POSITIVE` it
falls to 9 + 30. The claim survives — the gap 58 vs 39 is real — but the
sentence "the convention is selected by an identity" would be more honest with
the decomposition beside it.

*The identity does not see the stencil.* This is MAJOR-1.

### MAJOR-1 — the identity selects the lift and is blind to the stencil; a gate claim says otherwise

**Measured.** The winding — the mean group velocity over the dual torus — is
**identical, family by family, all 58, under the FORWARD and the BACKWARD
difference stencils**. Consequently the entire 3×3 agreement matrix is
identical under BACKWARD, including **58 of 58 at tie-averaged | tie-averaged
and best-other 39**. Under CENTRAL it is not (the diagonal falls to 46). So of
the **nine readings printed in §4** (3 lifts × 3 stencils), **two** reach the
identity:

```
FORWARD  | TIE-AVERAGED | TIE-AVERAGED  -> 58 of 58
BACKWARD | TIE-AVERAGED | TIE-AVERAGED  -> 58 of 58
```

These are not the same velocity field. §4's own fiber table records that
tie-averaged BACKWARD agrees with tie-averaged FORWARD at only 1088 of 1856
cells — they differ at **768 cells** — yet they produce the same winding, the
same identity, and the same 58.

**What breaks.** §12's choice inventory reads "the velocity definition
(fiber 9, printed in full in section 4, with the declared member selected by
the identity of section 7)". That is false as written: §7's identity ranges
over drift-lift × winding-lift, a *different* nine, and it cannot and does not
discriminate the stencil. The declared member FORWARD is not selected against
BACKWARD by anything in this unit. Worse, the gate carries the over-claim:
`G-DRIFT-WINDING-IDENTITY`'s claim sentence ends "**The velocity convention is
therefore SELECTED by an identity, not chosen**", while its predicate is
`matched_agree == ncirc and full == [(LIFT_DECLARED, LIFT_DECLARED)] and
best_other < ncirc` — evaluated over lift pairs only, with the stencil frozen.
Under the era's discipline that a gate's claim is what its predicate evaluates,
this is a claim/predicate mismatch on the unit's own headline result.

§1 and §7 are, to their credit, narrower: "the antipodal tie … has to be
resolved twice … and there are 9 ways to do it" is the lift × lift nine, and
is correct. It is §12 and the gate that widen "the tie" into "the velocity
convention".

**Exact repair.**
1. §12: "the velocity definition (fiber 9 = 3 lifts × 3 stencils, printed in
   §4). The identity of §7 selects the **lift** — tie-averaged — and is blind
   to the **stencil**: the backward difference gives the identical winding
   family by family and therefore the identical 58-of-58 agreement, although
   it is a different velocity field at 768 of 1856 cells. Residual fiber 2,
   DECLARED."
2. §1 / §7: "the velocity convention is not free" → "the antipodal **tie** is
   not free"; "A convention that was expected to be declared turns out to be
   selected by an identity" → "A **tie reading** that was expected to be
   declared turns out to be selected by an identity; the difference stencil
   remains declared."
3. Gate: either widen the predicate to the 27 (lift × stencil) × lift readings
   and record that **two** reach 58, or narrow the claim sentence to "the tie
   reading is selected by an identity".
4. Verdict: `DEFINITION=FORWARD-DIFFERENCE-WITH-TIE-AVERAGED(FIBER=9)` →
   `…(FIBER=9;TIE=SELECTED-BY-IDENTITY;STENCIL=DECLARED,RESIDUAL-FIBER=2)`.

**On the protocol's question — is "selected-not-declared" honest, and what must
SCOPE carry?** "Selected" is honest for the tie and only for the tie. §15's
declared-arena discipline wants every declared coordinate matched: the SCOPE
segment currently carries the momentum lattice but neither the velocity
definition (it sits in the VELOCITY segment, which is acceptable) nor **the
character convention**, which §12 registers with fiber 2 and which appears
nowhere in the verdict string. Since the unit measures that the character
convention is inert only when the sign of the velocity formula travels with it
— and the drift, computed in position space, does *not* flip with it — the
joint declaration is load-bearing for the 58-of-58 identity and should be in
SCOPE, not only in the prose: add
`CHARACTER-CONVENTION=DECLARED-JOINTLY-WITH-VELOCITY-SIGN(FIBER=2)`.
(I verified the sign is not idle: with the velocity sign flipped, the diagonal
of the agreement matrix falls from 58 to 46.)

---

## 4. K3 — the bound

All of it reproduces: VMAX = 2; max-norm diameter 2; radius classes [0, 1, 2];
interior radii [1]; the one-step cone covers 16 of 16 sites; the per-family
reach partition **8 over / 14 under / 36 equal**; the inherited ceilings
(separations 16 of 16, max defect radius 2 of 2) read from the parent's receipt
at its pinned hash. I also confirmed the two structural sentences §6 attaches:
every one of the 8 overshooters has radius 1, v_max 2 and non-zero aliasing;
every one of the 14 undershooters has radius 2, v_max 1 and **zero** aliasing.
The verdict's `REACH-BOUND-FALSE-AT=14-OF-58` has the direction right — the
bound fails where the reach exceeds the speed.

### MINOR-1 — the cone leg is forced, not measured

Under the declared definition the speed of a cell is the circle distance of
Δ_j s to 0, halved. Δ_j s lives in Z/8, so the circle distance is at most 4 and
**the speed is at most 2 for every conceivable generator on this arena** — no
census could have returned anything else. The max-norm diameter of (Z₄)² is
also 2. So "VMAX = 2 = the max-norm diameter" is a ceiling coincidence fixed by
the field and the lattice size before any family is built, and the cone clause
of §6 is vacuous whatever the dispersions had turned out to be. What is
measured is only that the ceiling is **attained** (some cell has Δ = 4). §6's
"both come back empty" and §9's "empty in both senses available at this scale"
therefore count one forced clause and one measurement as two measurements.

*Repair.* §6, in the **Cone** paragraph: "the speed ceiling is 2 by
construction here — phase differences lie in Z/8, so the halved circle distance
cannot exceed 2 — and the diameter is 2, so the cone clause is vacuous for any
family whatever at this scale; what the census adds is that the ceiling is
attained." Verdict: `VMAX=2=DIAMETER=2` →
`VMAX=2=DIAMETER=2(CEILING-FORCED;ATTAINMENT-MEASURED)`. The **reach** leg is
untouched by this and remains the unit's real negative result.

### MINOR-2 — "the top of the speed spectrum is the resolution limit itself" is definitional

§5 presents, in bold and with "the reason is worth seeing", the statement that
the classes with maximal speed 2 are precisely the classes with aliased cells.
I verified it over all 1856 cells — and it is an identity of the two
definitions: speed = circdist(Δ)/2 equals 2 **iff** circdist(Δ) = 4 **iff**
Δ = 4 **iff** the cell is aliased. Nothing was discovered; the two names denote
the same predicate.

*Repair.* Mark it FORCED-BY-DEFINITION in §5 and drop the discovery framing;
the interesting neighbouring fact — that the *overshooters* are exactly the
radius-1 aliased families — is genuinely measured and survives.

### On "measured relation or renamed register row"

The protocol asks this directly. §6's **resolution relation** has two legs and
they are of different kinds. The position-side leg — three max-norm radius
classes, diameter 2, exactly one interior radius — is **arithmetic about
(Z₄)²** and involves no property of the family, no generator and no census; it
would read the same if the pool were empty. The momentum-side leg — 320 of
1856 cells in 19 of 58 families — is a real measurement. No equation relates
the two. So "the observation is now a measured relation, not a remark" is half
earned: it is one lattice identity printed beside one census count. I would not
call it a renamed register row (the 320/1856 is new and is the unit's), but the
word *relation* is unearned.

*Repair.* §6: label the position-side bullet "a property of the admitted
lattice, not of the family" and keep the momentum-side bullet as the
measurement; or supply the equation that binds them, if one exists.

---

## 5. K4 — the cancellation claim

The arithmetic is right, all of it, and one leg is stronger than the paper
claims.

- **42 interfering families**, every one with non-constant dispersion and
  non-zero group velocity at individual momenta: **42 of 42 MOVE**.
- **Zero net transport at the declared reading**: all 42 have zero drift and
  zero winding.
- **12 families with non-zero winding, every one monomial**, out of 16
  monomial families. The four monomials with zero net transport are exactly
  the offsets (0,0), (0,2), (2,0), (2,2) — the identity and the three
  self-antipodal shifts, each verified self-negative.
- **The Markov binding.** 64² − 48² = 1792 = the parent's `markov_pairs`; the
  parent's `markov_nonzero` is 0; and my 16 monomial names are set-equal to the
  parent's `markov_control/monomial_generators`.
- **A leg the paper asserts and I verified.** §8 says the generators on which
  the defect vanishes identically "are precisely this unit's 16 monomial
  families". The set identity on *pairs* is arithmetic, but the word
  *precisely* needs the converse — that no non-monomial has an identically
  vanishing defect. I checked it against the parent's full 4096-row defect
  census: the generators with zero non-zero cells across every pair they appear
  in are **exactly** the 16 monomials. The claim holds and is stronger than
  gated.

### MAJOR-2 — "cancellation, not absence" is measured only at the selected reading, and the paper does not say which part survives

**Measured.** Of the 42 interfering families:

| | zero under **all three** readings | zero **only** under tie-averaged |
|---|---|---|
| drift (position space) | **24** of 42 | **18** of 42 |
| winding (dual torus) | **30** of 42 | **12** of 42 |

The 12 are exactly the 12 interfering families that carry aliased cells. So
"All 42 have exactly zero net transport, in both spaces" — §1 and §8, both
unqualified, and `INTERFERING=42-ZERO-NET-TRANSPORT-AND-42-MOVING` in the
verdict, also unqualified — is **true at the declared reading and false at the
other two**, and the subsets that break differ between the two spaces (18 vs
12). For those families the zero is not a cancellation between distinct
offsets; it is the antipodal average — the displacement that is its own
negative, given the value 0 by convention. That is precisely §8's **reading 3
(Resolution)**, not §8's **reading 2 (Cancellation)**.

So §8's adjudication — "The measurements support 2 outright, support 1 as a
structural fact, and measure the size of 3" — over-reads. The measurements
support 2 outright on the reading-independent part (24 of 42 in position space,
30 of 42 on the dual torus) and, on the remainder, *are* the size of 3.

This is the sharpest thing I found, because the headline sentence of §8 and of
the abstract is the one that the successor (R4c-multi) will inherit. The
honest sentence hands the successor a smaller but real object: **24 families
whose position-space transport cancels for reasons no convention can undo**.

*Exact repair.*
1. §1: "The 42 interfering families all have exactly zero net transport, in
   both spaces" → "…zero net transport in both spaces at the selected reading;
   for 24 of them in position space and 30 of them on the dual torus the zero
   is independent of every tie reading."
2. §8, bullet 2: add the table above verbatim.
3. §8, closing: "The measurements support 2 outright **on the
   reading-independent part** — 24 of 42 in position space, 30 of 42 on the
   dual torus — support 1 as a structural fact, and on the remaining 18 and 12
   they measure 3."
4. Verdict: `INTERFERING=42-ZERO-NET-TRANSPORT-AND-42-MOVING` →
   `INTERFERING=42-MOVING;ZERO-NET-TRANSPORT-AT-SELECTED-READING=42;READING-INDEPENDENT-ZERO=DRIFT-24-OF-42;WINDING-30-OF-42`.
5. Add a per-object gate binding each of the 42 to its own three-reading drift
   and winding vectors.

**Over-readings to kill.** "Cancellation" does *not* import an interference
ontology this arena measures. The unit computes ⟨Δx⟩ = Σ|c_o|²·o — a Born
expectation over a **classical** distribution on offsets — and a mean group
velocity. Neither is a coherence functional; nothing here shows two amplitudes
cancelling. The only interference object in the vicinity is the parent's
composition defect Δᴮ, which this unit does not recompute (correctly declared
in NOT EXECUTED). "Interfering" in this paper means *non-monomial*, a support
predicate, and the licensed sentence at citable scope is:

> On the 58-family circulant stratum at L = 4 over the declared 25-element
> alphabet, every non-monomial generator has non-constant dispersion and
> non-zero group velocity at individual momenta, while its Born drift and its
> mean group velocity both vanish — for 24 (resp. 30) of the 42 independently
> of how the antipodal tie is read. Momentum is not absent from these
> generators; it is present momentum-by-momentum and sums to zero.

Anything beyond that — that the vanishing is *caused* by interference, that it
is a quantum cancellation, that it says anything about states — is unlicensed.

### MAJOR-3 — the 58-vs-14 separation compares a per-family quantity with a per-class one

**Measured.** The reduced dispersion is constant on only **4 of the 19
circulant classes** — exactly the four singletons (C004, C055, C056, C057). On
the fifteen classes of size ≥ 2 it takes as many distinct values as the class
has members; §5's own `profiles` column says so (4, 4, 4, 2, …). **The reduced
dispersion is therefore not a class invariant at all.** It cannot "supply the
grading the labels lack" (§8, reading 1), and "The label the class table lacks
was available in the symbol the whole time" (§3) is not what was measured. What
the symbol separates is **families**, 58 of 58 — and so does the parent's
coefficient map, 58 of 58, trivially, which the paper itself concedes is forced
by the invertibility of the character transform.

The comparison in §1, §3, §8 and in the verdict row
`DISTINCT-REDUCED-PROFILES=58-VS-14-INVARIANT-LABELS` puts 58 *families*
against 14 labels over 22 *classes* — different objects, different
denominators.

**The like-for-like statement exists and is a positive result the unit missed.**
I computed the **multiset of member reduced dispersions** per extended class:
it is a class invariant by construction, and it separates **19 of 19 circulant
classes**. That is the statement the parent's label deficit actually calls for,
and it closes the gap: 19 of 19 where the parent's invariant labels give 14 for
22, with the one label shared by four classes (C000, C001, C020, C021 — which I
verified in the parent's receipt) split apart.

*Exact repair.* Replace the 58-vs-14 juxtaposition with: "the multiset of
member reduced dispersions is a class invariant and separates 19 of 19
circulant classes, where the parent's conjugacy invariants give 14 distinct
labels for 22 classes, one of them shared by four." Keep the family-level row
but mark it FORCED (the character transform is invertible) and
NOT-A-CLASS-LABEL. Verdict:
`DISTINCT-REDUCED-PROFILES=58-OF-58-FAMILIES(FORCED);CLASS-SEPARATION=19-OF-19-CIRCULANT-BY-DISPERSION-MULTISET-VS-14-LABELS-FOR-22`.
The computation is four lines and needs nothing the unit does not already have.

---

## 6. Remaining findings

### MINOR-3 — the μ₈ paragraph omits the load-bearing step

§3 argues: "Every coefficient has a 2-power denominator, so a symbol of unit
modulus is a unit of Z[ζ₈] all of whose conjugates have modulus one — … By
Kronecker's theorem such a number is a root of unity". The inference from
λ ∈ (1/2^k)·Z[ζ₈] with |σ(λ)| = 1 for every σ to **λ ∈ Z[ζ₈]** is exactly what
Kronecker needs and exactly what is not stated. It is not free: (3+4i)/5 has all
conjugates of modulus one and is not a root of unity. The step requires that 2
is totally ramified in Q(ζ₈) — 2 = unit·(1−ζ₈)⁴ — together with the fact that
complex conjugation lies in the Galois group, so λ·τ(λ) = 1 forces v_𝔭(λ) = 0
at every prime and λ is an algebraic integer. The two gated "finite legs" (odd
part of every denominator is 1; the field has exactly eight roots of unity) do
not cover it.

I verified the missing step computationally: for all **928** symbols the
characteristic polynomial of multiplication-by-λ on the Q-basis has integer
coefficients — **0 exceptions** — so every symbol is an algebraic integer and
the conclusion stands. The result is safe; the printed argument does not reach
it. (And the census's independent M⁸ = I route makes the whole paragraph
optional as evidence.)

*Repair.* Insert the ramification sentence in §3, and add the integrality check
as a third leg of `G-MU8-THEOREM-LEGS`.

### MINOR-4 — `G-EFFECTUS-DRIFT-TABLE`'s "and only under it" is asserted, not evaluated

The gate's claim ends "Under that reading, **and only under it**, the table's
three rows come out as the review printed them", but the predicate tests only
that the tie-averaged table equals the three rows. The positive-reading table
is computed and stored but never compared; the negative-reading table is not
computed at all. I verified the claim is **true** — positive and negative both
give 16 | 15, 18 | 10, 24 | 8 — so this is a coverage gap, not a false number.

*Repair.* Extend the predicate to `supp_table_alt != review_rows`, add the
negative table, and store all three.

### MINOR-5 — the artifact says 67 gates passed while carrying 66 gate rows

`totals.gates_passed` is computed as `sum(1 for g in LD.rows if g["passed"]) + 2`
at a point where `LD.rows` has **65** entries; the receipt written to disk holds
**66** gate rows; the 67th, `G-ARTIFACT-INTEGRITY`, is evaluated **only in the
writing path, after the payload has already been written**, and its result
appears on stdout alone. So the artifact's "67/67 passed" — and the output
file's `ALL GATES PASSED (67/67)` — anticipate two evaluations, and a failing
integrity gate would leave artifacts on disk asserting 67/67. The waiver ledger
does disclose the gate and its forcing (67 rows, 3 WAIVED), and §10 discloses
the two-way construction; what is undisclosed is that the count is
anticipatory. This is the one place where the pin's "failing runs write
nothing" is structurally unavailable, which the unit knows; the honest fix is
to say so in the number.

*Repair.* Report `gates_evaluated_in_receipt: 66` beside `gates_declared: 67`,
and either re-serialise after the integrity gate or record
`integrity_gate: REPORTED-ON-STDOUT-ONLY`.

### MINOR-6 — "a law with all three reachable" is exercised for two of the three

§1: "the head is derived from the census by a law with all three reachable:
with the census's motion count zeroed, the head law returns `R4B-NO-MOTION`,
and a gate proves it." `derive_head` does carry three BLOCKED branches, and
`G-HEAD-LAW-RESPONSIVE` drives the NO-MOTION branch. **No probe drives any
BLOCKED branch.** The counterfactual in the very next sentence — "would have
returned `R4B-BLOCKED-AT` if the eigenvalues had not been roots of unity" — is
the ungated branch, and `MUT-MU8` cannot reach it: it dies earlier, at
`G-EIGENPHASE-IN-MU8`, which I confirmed by running it. So "all three
reachable" is a reading of the source, not a measurement.

*Repair.* Add a probe feeding `derive_head` a counts dict with
`in_mu8 < cells` and requiring `R4B-BLOCKED-AT-EIGENPHASE-OUTSIDE-MU-8`
(three lines, no new computation); or soften §1 to "two of the law's three
outcomes are exercised".

### NITs

- The code comment above `FORCINGS` reads "the only **two** gates with no
  declared mutant"; `FORCINGS` has three entries and the paper correctly says
  three. Stale comment.
- `DERIVED_IN_TEXT` justifies the numeral "5" as "the section numbers" only.
  The paper also uses 5 as the programme's false-claim register count — which I
  verified against `note-r4-adjudication.md` `3b00a9481b28` ("the programme
  count rises to 5 … all prose; zero in computed artifacts"), so the number is
  right, but the residue entry should name that use or the coverage gate is
  waving a substantive number through on a wrong description.
- §3's "one label shared by four classes" is **correct** — I checked the
  parent's `class_labels`: six shared groups, five pairs and one quadruple
  (C000, C001, C020, C021), plus eight singletons, giving 14 labels for 22
  classes. Recorded because it is the kind of number that is usually wrong.
- The unit's sweep adds the two ± coefficients at the three order-2 axes, so it
  samples the alphabet's sumset there rather than the declared alphabet. It
  changes nothing (I checked both routes give the identical 58), but the code
  should say why.

---

## 7. Prose numbers audited against the receipt

I checked every substantive numeral in the paper against the receipt and
against my rebuild. All agree. The sample dispersion table in §3 (six rows,
including the σ strings `0022002200220022`, `0660066006600660`,
`0220022002200220`, `0066006600660066`, `0642064206420642`) matches the
receipt's `dispersion_census` rows exactly and matches my independently
computed reduced dispersions. The 22-row class table of §5 matches. The
instrument totals close: 41 = 8 + 20 + 13 anchors; 67 = 64 + 3 gates; 66
mutants declared, killed and on target; 56 verdict values; 928, 1856, 320, 19,
58, 42, 16, 12, 1792, 8/14/36, 16/18/24 all reproduce. `paper_coverage` reports
44 claims, 78 distinct numerals over 413 occurrences, nothing missing and
nothing uncovered, and I found no numeral it should have caught — subject to
the "5" residue nit above.

**Candidate-readings rule.** Audited against my rebuild, the delivered headline

> `R4B-DISPERSION-READ<MOVING=57-OF-58 … VMAX=2 … BOUND=NO-CONTENT>`

is **sustained**: the census, the motion head, the velocity spectrum and the
emptiness of the bound all reproduce exactly. The two headline *sentences* that
do not survive unmodified are the convention-selection sentence (MAJOR-1: the
identity selects the tie, not the velocity definition; two of the nine §4
readings reach 58) and the cancellation sentence (MAJOR-2: zero net transport
holds at the selected reading, and is reading-independent for 24 of 42 in
position space and 30 of 42 on the dual torus). Both repairs *strengthen* what
the unit hands its successor, because both replace an unqualified claim with a
measured subset.

---

## 8. Verdict

**AWF.** The computational core is the strongest I have audited in this era.
A from-scratch rebuild in a different basis, with two sweep routes and three
diagonalisation routes — two of which never compute a symbol — reproduces
every one of the delivered numbers, including all 928 eigenphases and all 928
reduced-dispersion entries, the full 9-cell agreement matrix, the full 9-cell
velocity fiber, the 22-row class table and both drift tables. The unit's
byte-identity is robust off-tree, git-less and under a permuted hash seed; its
thirteen verbatim quotations are all present exactly once in their pinned
sources; its selftest and its mutants bite where they say they do.

What holds it back from A is that three delivered sentences — one of them a
gate claim, two of them verdict rows — assert more than the unit evaluated:
the identity is credited with selecting a velocity *definition* it cannot see
half of; "zero net transport in both spaces" is stated without the reading it
depends on, in a section that names reading-relativity as a rival hypothesis
and then dismisses it; and a per-family separation is compared with a per-class
label count. All three repairs are cheap, all three are exact, and all three
leave the computed artifacts untouched. Two of them (MAJOR-2, MAJOR-3) hand the
R4c-multi successor a sharper object than it currently has: 24 reading-independent
zero-transport families, and a dispersion-multiset class invariant that
separates 19 of 19 where the parent's labels separate 14 of 22.

**Recomputations: 92. False numbers found: 0.**
