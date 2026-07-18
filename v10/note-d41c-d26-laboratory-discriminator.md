# The D26 laboratory discriminator — turning √(1−g) into an instrument bound

**Status:** EXPERIMENT-FACING NOTE, 2026-07-15 (the paper-29 hand-off
executed; no new data claimed; every platform number below is
[LITERATURE, order-of-magnitude, to be verified against current primary
sources before any proposal-grade use]). **The law (D26, terminal):** each
represented same-line BORN carrier contracts the monitored parent line's
probed coherence by √(1−g); N identified births give V_N/V_0 = (1−g)^{N/2}
((4/5)^N at the pinned g = 9/25). TOKEN activation is coherence-neutral —
the BORN/TOKEN discriminator (paper 25 review M1; paper 27 §7) is what
makes record birth a laboratory observable at all.

## 1. The bound, in instrument variables

For a system identified (by the O-V bridge) with one monitored record
line, over a dwell time T with interferometric visibility measured to
relative precision δ ≡ δV/V₀, a NULL result bounds the number of same-line
births in the window:

```text
N · [−ln√(1−g)] ≤ −ln(1−δ) ≈ δ        (small δ)
⇒ N ≤ δ / κ(g),   κ(g) = ½ ln(1/(1−g));   κ(9/25) = ½ ln(25/16) ≈ 0.2231.
```

At unknown g the bounded object is the PRODUCT N·κ(g) ≤ δ — the same
ratios-only structure as paper 28 Theorem 5: absolute birth RATE requires
the clock bridge (T in whose time?), so all rates below are per laboratory
dwell time with the conversion declared open (this note and D41 item 6
cite each other's scope guard — D41 RF5).

## 2. Candidate platforms (representative orders; verify before use)

```text
platform                    T_dwell        δ (vis. prec.)   N·κ bound → N at g=9/25
trapped-ion hyperfine qubit ~10³–5×10³ s   ~10⁻²–10⁻³      N ≲ 5×10⁻³–5×10⁻² per dwell
                            (DD-extended)                   ⇒ rate ≲ 10⁻⁵–10⁻⁶ /s
atom interferometer         ~1–10 s        ~10⁻³            N ≲ 5×10⁻³ ⇒ ≲ 10⁻³ /s
macromolecule (OTIMA-class) ~10⁻³–10⁻² s   ~10⁻²            N ≲ 5×10⁻² ⇒ ≲ 10 /s
levitated nanoparticle      ~10⁻³–1 s      ~10⁻²            intermediate; mass-scaling axis
```

The trapped-ion column is the strongest raw bound; the macromolecule and
levitated columns matter because the O-V bridge plausibly scales the
record count N_records with system size — the MASS/COMPLEXITY SCALING of
the bound is the discriminating axis against ordinary decoherence (which
scales with environmental coupling, not record count; this is the same
separation axis as the corpus's D21 calibrated ladder).

## 3. The confound budget (what a proposal must subtract)

(a) Ordinary environmental decoherence: bounded independently per platform
(T₂ characterization); the D26 channel must be reported as EXCESS
visibility loss after that subtraction. (b) TOKEN-mode dynamics: factor
one by D26; a nonzero TOKEN-side effect would itself be new physics and
must be declared as a separate hypothesis (paper 27 §7). (c) The
value/content split (D25): Z-value survival vs X-content dispersal — the
probe basis must be the COHERENCE basis of the monitored line, pinned in
the protocol. (d) The bridge items (paper 29 §7 / paper 28 §7.1): system ↔
record line identification; which events are births; the parent line's
identity; background g-variation. Every reported bound is conditional on
the declared bridge — the note's honesty clause.

## 4. The falsifier statement

If a platform's excess visibility loss FLOOR (after (a)) is measured at
Δ over dwell T reproducibly, the record hypothesis with the declared
bridge asserts N·κ(g) = Δ births occurred on the monitored line — a
POSITIVE detection channel with a parameter-free cross-check: the same N
must appear in any second coherence observable on the same line
(the functional form (1−g)^{N/2}, not the value, is the signature —
paper 19's second functional-form prediction, now instrument-mounted).
A null at improving δ monotonically tightens N·κ(g) → the record-birth
rate on monitored lines is driven toward zero, which CONSTRAINS every
D34-class generated law whose q_birth would touch laboratory systems —
the first experimental back-pressure on the architecture arc.

## 5. Next actions (proposal-grade path)

(1) Verify the platform table against current primary literature
[deep-research pass; not done here]. (2) Pick the two-platform pair
(best raw bound + best mass-scaling axis). (3) Write the bridge
declaration for each (the O-V dictionary as a pinned, criticizable
object). (4) Pre-register the excess-loss analysis with the confound
budget. (5) Only then: contact/collaboration. This note is the artifact
for step (0): the law, the bound, the axes, and the honesty clauses in
one citable place.

## 6. Step (1) EXECUTED + step (2) pair adopted (forward corrections,
## 2026-07-18; full sourced pass: reviews/d41c-step1-platform-verification.md)

The deep-research verification (primary sources, July 2026; every
number tagged MEASURED/FIT/PROJECTED) returns SEVEN corrections to §2:

1. **Levitated row WRONG as a measured claim (biggest):** measured
   coherence ≈ 4×10⁻⁵ s (Rossi 2025, PRL 135, 083601) and NO
   interference-visibility observable demonstrated on any levitated
   nanoparticle — the 10⁻³–1 s band is proposal-stage (Neumeier 2024).
   Row re-labeled [PROJECTED] wholesale; it cannot host the bound today.
2. Mass record superseded IN OUR FAVOR: 143–197 kDa quantum-certified
   (Pedalino et al., Nature, Jan 2026; V = 0.10 ± 0.01, μ = 15.5),
   ≈ 7× the note's 25 kDa; the mass axis strengthens.
3. Atom-interferometer dwell outdated: 70 s lattice-hold measured
   (Panda 2024, Nat. Phys. 20, 1234) vs the note's 1–10 s; projected
   rate improves to 6.4×10⁻⁵ /s (1.5 orders better than credited).
4. Ion caveats: 5500 s is a FITTED constant (probed to 960 s); the
   (5×10³ s, 10⁻³) joint cell is undemonstrated — measured-anchored
   band 1.4×10⁻⁴–8×10⁻⁶ /s, the 10⁻⁶ endpoint a projected corner.
5. Frontier-mass δ is 10⁻¹, not 10⁻² (10⁻² holds for established
   species only).
6. Two platforms MISSED: ¹⁵¹Eu³⁺:Y₂SiO₅ six-hour nuclear ensemble
   (best raw product 2×10⁻⁶ /s; bridge-hostile: ensemble in solid) and
   ⁸⁷Sr lattice-clock lines (118 s optical-line coherence; the
   cleanest raw upgrade path; erasure-conversion bookkeeping is
   natively an excess-loss analysis).
7. Attribution: the minute-scale holds are Müller-group (Berkeley).

**Step (2) ADOPTED on the pass's recommendation:** the pair =
**¹⁷¹Yb⁺ single-ion hyperfine (raw bound; the only long-T platform
where the monitored object IS one line — minimal O-V bridge, native
T₂ subtraction)** + **Arndt-class Talbot–Lau beams (mass axis; the
only platform with a MEASURED visibility ladder 10²–2×10⁵ amu in one
instrument family)**. Successors named: ⁸⁷Sr clock (raw), levitated
(mass, [PROJECTED]). Next: step (3), the two bridge declarations.
