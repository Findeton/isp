# v12 W2 — THE MULTIPLIER LADDER: THE DEFECT ALGEBRA, THE PROJECTIVE
# DESCENT NO-GO, AND THE VACUOUS SELECTION

**Status:** GREEN-UNREVIEWED-REPAIRED, STRICT, 2026-07-28.
**Pin:** `note-w2-multiplier-ladder-pin.md` (frozen before any code).
**Binding:** paper 0 v2.1 §1 (T2′, Δᴮ and the three-defect
distinction), §4 W2′ (the three-way split, verbatim), §5 (non-claims);
LOG #1–#8.
**Receipt:** `v12/code/w2_multiplier_ladder_exact.py` →
`v12/code/w2_output.txt`.  **32 anchors, 161 gates, 161 pass, 0 fail**
(of which **17** carry no independent information and are named in
full in-receipt: **144 independent-evidence gates**); runtime 278.2 s;
re-run at `PYTHONHASHSEED=7` identical apart from timings.
**Verdicts:** **W2a-STRUCTURE-DELIVERED / W2b-NO-ACTION /
W2c-VACUOUS** — all three unchanged by the repair; the no-go is real
and its evidence reproduced entirely.

**READ THE GATE COUNT CAREFULLY — the numeral is a trap.**  The
pre-repair printing claimed *152 gates, 8 disclosed, 144 independent*.
The round found nine further gates that carry no independent
information, so **on that same gate set the honest count is 135, not
144**.  This repaired receipt drops one vacuous gate, adds nine
genuine ones, and discloses seventeen: *161 − 17 = 144* again.  **The
coincidence is arithmetic and nothing else.**  What changed is the
disclosed list, not the total.

**Round 1 (hostile, external) returned ACCEPT-WITH-FIXES**: the no-go
real and airtight, every number reproduced, six major fixes, five
minor, two nits.  All are applied here.  The four that changed what
this unit *says*, as opposed to how it says it:

1. **The closure is re-attributed.**  §13 alone does *not* close
   requirement (3); §13 **plus** §14 does.  See §19.
2. **The handover to a successor was cohomologically backwards** and
   is rewritten.  See §20.
3. **"The Δᴮ-family is reversal-even" was false unqualified.**  §17 is
   rewritten around the *covariance* law and the odd channel, and the
   [D74]-D2 step is **withdrawn**.
4. **A8's second equivalence is a classical theorem**, not this
   unit's: it is the discrete Wiener–Khinchin theorem and the
   definition of a CAZAC sequence.  Attribution added; the claim is
   scoped to the identification.

Two further corrections run *upward*: §14's exhibit is stronger than
it was stated to be (six classes, not four), and §3's range is now
carried by two genuine attainment witnesses instead of one vacuous
pair.

Arithmetic: `fractions.Fraction` for every rational; the cyclotomic
fields ℚ(ζ_N), N = 2, 3, 4, 5, 6, 8, 12 (canonical representation
modulo Φ_N, so tuple equality *is* field equality) for every complex
algebraic quantity; a multivariate polynomial ring over ℚ for every
symbolic identity; ℚ(√2) with an exact sign oracle for the one order
comparison the unit makes.  √5 enters through the quadratic Gauss sum
in ℚ(ζ₅), gated by squaring.  No float in any substantive path; no
tolerance anywhere.  Substantive negatives exit 0; exit 1 is
anchor-only.

**Instruments are read, not copied.**  W1′'s arithmetic layer, matrix
layer and two census families, and D74's group instrument, are
extracted from the committed source files by AST slice (36 and 3
top-level definitions) and executed here.  The 32 anchors are the
parents' own committed numbers: Δᴮ(H,H) = [[½,−½],[−½,½]], the two
census tables 5120/0/1024/3072 and 3888/0/54/27, both closed forms,
C+1's −4032/15625 and K = S(−175/527), the record example, and D74's
⟨2,3⟩ with prime support [2,3], rank 2, index 1 and lattice basis
[[−1,0],[0,1]].  A drift in either parent exits 1.

**The standing wall, engraved in the pin:** B(ωU) = B(U).  §2 makes it
a special case of a much larger annihilation, and §5 promotes it from
a pointwise remark to a statement about the entire Δᴮ-family.

---

## W2a — THE DEFECT ALGEBRA

### 1. The universal closed form

With m = row i of U₂ and n = column j of U₁, put w_k := m_k n_k =
(U₂)_{ik}(U₁)_{kj} — the amplitude of the path through intermediate
value k.  Then

    Δᴮ_ij  =  |Σ_k w_k|²  −  Σ_k |w_k|²  =  2 Σ_{k<ℓ} Re(w_k conj(w_ℓ)).

**The defect entry is the total pairwise interference of the path
amplitudes through the cut, and nothing else.**  This is [B1]'s
cross-term sum in closed form.  Gated as a real polynomial identity
(w_k = x_k + i y_k) at d = 2, 3, 4, 5, 6, and against the definition on
all 13,185 W1′ census pairs.  Every structural result below is read
off this one line.

### 2. Normalized forms and the exact invariance group

With D, D′ diagonal unitary and P a permutation:

| | law | |
|---|---|---|
| (i) | Δᴮ(I,U) = Δᴮ(U,I) = 0 | NORMALIZED |
| (ii) | Δᴮ(D U₂, U₁ D′) = Δᴮ(U₂,U₁) | OUTER TORI |
| (iii) | Δᴮ(U₂ D, D⁻¹U₁) = Δᴮ(U₂,U₁) | CUT GAUGE |
| (iv) | Δᴮ(P U₂, U₁ P) = P Δᴮ(U₂,U₁) P | EQUIVARIANCE |
| (v) | Δᴮ(U₂,U₁)ᵀ = Δᴮ(U₁ᵀ, U₂ᵀ) | REVERSAL |
| (vi) | Δᴮ(U₂ D, U₁) ≠ Δᴮ(U₂,U₁) in general | the only handle |

(ii) contains the wall — a scalar ω is a diagonal unitary — and is
strictly stronger: **what dies at each outer slot is not only the
scalars but the whole maximal torus 𝕋ⁿ**, and by (iii) the compensated
torus at the cut dies too.  (vi) is the only surviving handle and it is
an uncompensated insertion, not a group action on the pair; it moves
192 of 576 pairs at 2×2 and 25 of 576 at 3×3.  Gated on a declared
deterministic stride of 24 matrices from each family.

Two of these lines are weaker than the list makes them look, and both
are tagged at their gates.  (i) is **near-tautological**: B(I) = I, so
the two terms of the definition coincide term by term.  (v) is a
**covariance, not an evenness**, and the A2 instance is **subsumed by
§17**, which re-gates it on the full census and reads off the odd
channel it leaves open — the reading that survives is stated there,
not here.

### 3. The doubly-centred structure and the sharp bounds

B(U) is doubly stochastic for unitary U, so B(U₂U₁) and B(U₂)B(U₁)
both are and **Δᴮ has all row sums and all column sums zero**: the
family lands in the (n−1)²-dimensional space of doubly-centred
matrices, the tangent space of the Birkhoff polytope.  With
s_ij := (B(U₂)B(U₁))_ij = Σ_k |w_k|²,

    Δᴮ_ij + s_ij = B(U₂U₁)_ij ≥ 0,
    n·s_ij − (Δᴮ_ij + s_ij) = Σ_{k<ℓ} |w_k − w_ℓ|² ≥ 0,

i.e. **−s_ij ≤ Δᴮ_ij ≤ (n−1) s_ij**, both by exact certificates — the
first definitional (a modulus square), the second the Lagrange
sum-of-squares identity, gated at d = 2..6 — and neither by any order
comparison.

The first certificate needs one thing the earlier receipt asserted and
did not gate, and the round was right to ask for it: **s_ij must be a
non-negative real number before Δᴮ_ij + s_ij ≥ 0 bounds anything.**
That is now the gate — every s_ij over both censuses is checked to be
a **non-negative rational** (36,864 + 35,721 entries, 0 violations).
The identity Δᴮ + B(U₂)B(U₁) = B(U₂U₁) itself is retained but
**disclosed as a tautology**: Δᴮ was *built* as that difference, so
the gate tests (a−b)+b = a.

At n = 2 the family is **one-dimensional**: Δᴮ is a multiple of
[[1,−1],[−1,1]] whose parameter is 2Re(A₀B₀) with A_i = (U₂)_{i0}
conj((U₂)_{i1}) and B_j = (U₁)_{0j}conj((U₁)_{1j}) — W1′'s
phase-alignment obstruction — and **its exact range is [−½, ½]**, read
off all 9216 census pairs with the exact ℚ(√2) sign oracle.  The bound
follows from the AM-GM certificate (x+y)² − 4xy = (x−y)².

**Which pairs attain the ends (round-1 repair M3).**  Not both (H,H):
that reading was **false**.  (H,H) gives Δᴮ = [[½,−½],[−½,½]], hence
**+½ only**; the old gate paired Δ₀₀ = +½ with Δ₀₁ = −½, which is
**vacuous**, since one-dimensionality makes Δ₀₁ = −Δ₀₀ identically.
Two genuine witnesses replace it:

    Δᴮ(H, H)₀₀              =  +1/2,
    Δᴮ(H, diag(1,−1)·H)₀₀   =  −1/2,

both exact in ℚ(ζ₈), with diag(1,−1)·H gated unitary.  The lower end
is attained **elsewhere**, and elsewhere is exhibited.

### 4. The n-fold telescoping is a tree identity

Write Δ_n(L₁..L_n) := B(L₁···L_n) − B(L₁)···B(L_n).  For a binary
bracketing T define Φ(leaf) = 0 and

    Φ(T) = Δᴮ(U(T_L), U(T_R)) + Φ(T_L)·B(U(T_R)) + (∏_L B)·Φ(T_R).

**Theorem: Φ(T) = Δ_n for every bracketing T.**  The distinct
telescopings at n steps number the Catalan number C_{n−1}; the two at
n = 3 are exactly W1′'s C+2 coherence law, and the receipt gates that
reduction verbatim.

The gate uses independent polynomial variables for B of every
contiguous sub-product, so **no property of B is assumed** — not
unitarity, not positivity, not even that B acts entrywise.  Gated at
d = 2 for n = 2..6 (1, 2, 5, 14, 42 bracketings; 12 to 84 formal
variables) and d = 3 for n = 2..5 (27 to 135 variables).  Corroborated
on exact committed matrices — a declared deterministic stride of 4
family members, every ordered tuple, every bracketing: 1360 tuples
(2×2, n = 2..5) and 336 (3×3, n = 2..4), 0 failures.

### 5. The law is content-free about the Born projection

Because §4's gate assumes nothing about B, the law holds for **any**
map whatsoever.  Made concrete **and falsifiable-looking**: the same
identity is gated with B replaced by six declared non-Born maps — the
identity map, entrywise Re, the entrywise square without modulus, the
transpose, M ↦ M + 2Mᵀ + 3I, and a **declared-nonsense constant map
that ignores its argument entirely** — on 432 ordered triples each.
It holds for all six.  **A law that survives replacing its subject
constrains the subject not at all**: the coherence law is an identity
of associativity.

And this section's thesis applies to its own gates, which is the
round's point (M6) and is now stated at the gates themselves: **none
of these six can fail.**  The telescope

    (f(ABC) − f(AB)f(C)) + (f(AB) − f(A)f(B))f(C)
      = (f(ABC) − f(A)f(BC)) + f(A)(f(BC) − f(B)f(C))

has both sides equal to f(ABC) − f(A)f(B)f(C) for *every* f.  All six
are therefore **declarative** and all six are named in the receipt's
disclosure block; the sixth was added precisely to make that
undeniable rather than arguable.

### 6. The two-sided annihilator is exactly the monomial group

W1′ gated sufficiency and showed it is not necessary pairwise.  Under a
universal quantifier it becomes an equivalence:

    K_L := {U₂ : Δᴮ(U₂,V) = 0 for every unitary V} = the ROW-monomial
                                                     unitaries, exactly;
    K_R := {U₁ : Δᴮ(V,U₁) = 0 for every unitary V} = the COLUMN-monomial
                                                     unitaries, exactly.

Sufficiency is §1's closed form: at most one w_k is nonzero, so the
pairwise sum is empty.  Necessity: if row i of U₂ has nonzero entries
a, b at columns k ≠ ℓ, the probe V = D_m^{(k)}·R_{kℓ}, with R_{kℓ} the
exact rational rotation [[3/5,−4/5],[4/5,3/5]] in the (k,ℓ) plane and
D_m^{(k)} carrying i^m at position k, gives

    Δᴮ(U₂,V)_{ik} = (24/25)·Re( i^m · a · conj(b) ),

and Re(z) = Re(iz) = 0 forces z = 0, so m ∈ {0,1} separates every
non-monomial row.  K_R follows from K_L by (v).

**This is a hand proof with gated ingredients**: the closed form, the
probes' unitarity (entries in ℚ(i) only, no √2 needed), the two-phase
separation and the exhaustive family corroboration are gated; the
quantifier over all unitaries is carried by the argument, not by the
sweep.  Corroboration: 64 non-row-monomial members at 2×2 and 9 at
3×3, 0 unseparated in either slot, with 2 and 6 probes respectively.
(The **sufficiency** half of the gate pair is a *re-assertion* of
§0.2's census anchor `cond_nonzero = 0`, recomputed from the same
table; it is disclosed in-receipt as carrying no independent
information.  The necessity half is where the content is.)

**Corollary — the wall's structural form.**  B restricted to the
monomial group Mon(n) = 𝕋ⁿ ⋊ S_n *is* a group homomorphism onto S_n,
with the whole torus 𝕋ⁿ in its kernel.  Gated on the 32 and 54
monomial members of the two families.

### 7. Pairwise flatness does not imply n-fold flatness

The coherence law gives Δ₃ = Δᴮ(U₃, U₂U₁) + B(U₃)Δᴮ(U₂,U₁); with both
consecutive defects zero the first term survives.  Exhibited: family
indices (28, 0, 29) at 2×2 and (36, 0, 36) at 3×3, both cuts flat and
Δ₃ ≠ 0.  **The defect is not locally determined** — flatness at every
cut of a chain does not make the chain flat.

### 8. The phase-alignment condition in closed form, for all N

On the DFT-sandwich family U₂ = D_a F_N D_b, U₁ = D_c F_N D_e one has
B(U₂) = B(U₁) = J/N, so Δᴮ = 0 ⟺ B(F_N E F_N) = J/N with E = D_b D_c
the **interleaving** diagonal.  Since (F_N E F_N)_{jk} =
(1/N)Σ_m ε_m ω^{m(j+k)}, the entries are the DFT of the unimodular
sequence ε read at j+k, so

    Δᴮ = 0  ⟺  |DFT(ε)(s)| = √N for every s          [the IDENTIFICATION]
            ⟺  ε has zero periodic autocorrelation at every nonzero lag
               (a CAZAC / perfect sequence).          [ CLASSICAL, cited ]

**Δᴮ = 0 is phase alignment, and the alignment condition is flatness of
a Fourier spectrum.**  Gated with ε₀ = 1 fixed: N = 2 over μ₈ in
ℚ(ζ₈) (8 diagonals, 2 flat), N = 3 over μ₆ in ℚ(ζ₁₂) (36, 6), N = 4
over μ₈ in ℚ(ζ₈) (512, 16), N = 5 over μ₅ in ℚ(ζ₅) (625, 20); 0
mismatches against either characterization.

**Attribution, and it is load-bearing (round-1 repair M5).**  The
*second* equivalence is **not this unit's, and not new**.  "Flat |DFT|"
⟺ "zero periodic autocorrelation at every nonzero lag" is the
**discrete Wiener–Khinchin theorem** — the autocorrelation and the
squared modulus of the DFT are a transform pair — and it is the
**definition** of the CAZAC / perfect sequences, a classical family
with explicit constructions at every N (Björck; Chu and Zadoff–Chu;
Frank; Turyn; Golomb–Gong).  See **[WK/CAZAC]** in §21.  **What §8
claims is the first line only: the identification of Δᴮ = 0 on the
DFT-sandwich family with that known condition on the interleaving
diagonal.**  Both gates now carry the `[WK/CAZAC]` tag, and the second
is re-gated here as a check on this receipt's arithmetic, not as a
theorem of this unit.

W1′'s two committed closed forms are the N = 2 and N = 3 cases, and the
receipt re-derives them from flatness: at N = 2 flat ⟺ ε₁ = ±i ⟺
t + u ≡ ±2 (mod 8); at N = 3 with ε = (1, ω^m, 1), flat ⟺ m ≢ 0
(mod 3) ⟺ b₂ + a₁ ≢ 0 (mod 3).

### 9. What kills the family

Exactly three shapes appear, and §1 says why: **support** (at most one
w_k nonzero — sufficient only), **algebraic** (a monomial slot —
exact under a universal quantifier, §6), and **conditioning at the
cut** (the dephasing channel D, which replaces Σ_k w_k by an
incoherent sum).  Interleaving D at every cut kills Δ_n identically:
gated at n = 2, 3, 4 on H∘H and F₃∘F₃, where the D-interleaved shadow
*is* the product of the Born shadows.  Reporting-only; the general
record theorem is W3′'s.

---

## W2b — PROJECTIVE DESCENT

### 10. The target, made precise before anything is run

W2b asks for three things at once:

1. a committed object supplying a homomorphism ρ : ℤ² → PU(H) — the
   generated group **acting**;
2. a lift ρ̃ : ℤ² → U(H) whose multiplier ω(g,h) = ρ̃(g)ρ̃(h)ρ̃(g+h)⁻¹
   has [ω] ≠ 0 in H²_grp(ℤ², U(1)) — the Weyl relation
   UV = e^{2πiθ}VU;
3. a functional F of the Δᴮ-family that the multiplier **controls**:
   constant on fixed-θ data, and separating different θ.

### 11. The generated ℤ² is a group of values, not of transformations

D74's ⟨2,3⟩ is the image of the loops of the menu quotient under the
transport-holonomy map, computed as an integer exponent lattice: prime
support [2,3], rank 2, index 1 in ℤ², the full group of 3-smooth
positive rationals.  Its values are positive rationals, so it sits in
(ℝ⁺, ×), and **ℝ⁺ ∩ U(1) = {1}**: the only possible U(1) content of a
positive-rational holonomy is the sign −1, realized nowhere — D74's D2,
in one line.  D74 exhibits no action of ⟨2,3⟩ on anything; the holonomy
map runs *from* loops *to* this group.  **Requirement (1) is not in the
committed record for the generated group.**

(The lattice basis is presentation-order dependent — D74's own
instrument returns [[−1,0],[0,1]] from a set and [[−1,0],[0,−1]] from a
sorted list.  What is licensed and what is used here is the lattice:
prime support, rank, index, all three basis-independent.)

### 12. What [ω] is: an alternating bicharacter, and it is a scalar

For ℤ² with trivial action, [ω] ∈ H²_grp(ℤ², U(1)) is determined by the
antisymmetrization β(g,h) := ω(g,h)/ω(h,g), an alternating bicharacter
invariant under coboundaries; and for **any** lift,

    ρ̃(g) ρ̃(h) ρ̃(g)⁻¹ ρ̃(h)⁻¹  =  β(g,h) · I,   a SCALAR matrix.

So the complete invariant of the class is exactly a scalar — and B
annihilates scalars.  Gated on the finite models ℤ_m × ℤ_m, m = 2..6:
the Weyl cocycles ω_k((a,b),(c,d)) = ζ_m^{k·b·c} are normalized
2-cocycles (all |G|³ associativity checks each); β(e₁,e₂) separates all
m classes; there are exactly m alternating bicharacters on ℤ_m²
(H²(ℤ_m², U(1)) = ℤ_m, realized by the Weyl cocycles); and β is
coboundary-invariant across **all** normalized 1-cochains at m = 2 and
m = 3 (8 and 6561 of them).

### 13. THE MULTIPLIER CANCELS FROM THE ENTIRE FAMILY

**Theorem.**  Let ρ̃ : G → U(N) be any projective representation with
multiplier ω, and put β_B := B ∘ ρ̃.  Then β_B is independent of the
lift, and

    Δᴮ(ρ̃(g), ρ̃(h))  =  B(ω(g,h) ρ̃(gh)) − B(ρ̃(g))B(ρ̃(h))
                      =  β_B(gh) − β_B(g)β_B(h).

**The multiplier does not appear.**  The whole Δᴮ-family of a
projective representation is the deviation of β_B from being a
homomorphism, and β_B is a function of the PU(N)-valued map alone.
This promotes the wall B(ωU) = B(U) from a pointwise remark to a
statement about the entire family.  Lift-independence gated on every
word of the Weyl group at N = 2..6 against **every root of unity of
the carrier field** — μ_n for the field ℚ(ζ_n) actually in use, not
every scalar of it, which is what the sweep runs and what the gate now
says (round-1 repair m3).

**What this section does and does not settle.**  It removes ω from the
*formula*.  It does **not**, by itself, show that no functional of the
family determines the class: [ω] is a **lift-independent** invariant
of the projective map ρ, so "absent from the formula" and "invisible
to every functional" are different statements.  The counterfactual is
the cleanest way to see it — *were B injective on PU(N), requirement
(3) would be met and this theorem would hold verbatim.*  §14 is what
closes the road.

### 14. THE COLLAPSE: six classes, one Born shadow — and this is what closes requirement (3)

Take U = X_N (shift), V = Z_N^k (clock power), k = 0..N−1.  The
commutator is ζ_N^{−k}·I, so the class has order N/gcd(N,k) — every
class realizable on ℂ^N, the trivial one included.  But B(Z_N^k) = I
for every k, so β_B(a,b) = B(X^a Z^{kb}) = P^a with P the shift
permutation, **independent of k**.

At N = 6 the six values k = 0..5 give β = ζ₆^{−k}: **six distinct
elements** of H²(ℤ², U(1)), of **four distinct orders** 1, 2, 3, 6,
the trivial class among them — carried by realizations with literally
identical Born data and an identically zero Δᴮ-family.  (The earlier
reading, "four distinct elements", under-sold the exhibit: the classes
number six and it is their *orders* that number four — round-1 repair
m2, a correction upward.)

Gated at N = 2..6: all N² words per class, all N⁴ ordered word pairs
for N ≤ 4, the 9×9 sub-block for N = 5, 6 — **and at N = 6, which is
the case the no-go leans on, the cap is now removed entirely**
(round-1 repair M1).  The receipt's **B4x** runs all 36 words U^aV^b,
a,b < 6, and all 36 × 36 = 1296 ordered word pairs, for **all six k**:
**7776 exact Δᴮ computations in ℚ(ζ₆), all zero**, with the six β
values gated distinct.

**This is the argument that closes requirement (3), and §13 is only
its first half.**  Because B(Z^k) = I, β_B is independent of k, so
every finite-dimension-realizable class — and by W2c's own determinant
argument that is exactly θ ∈ (1/N)ℤ — **collapses onto one and the
same Δᴮ-family**.  A functional cannot separate arguments it is not
given: **any functional whatsoever, of any shape, takes the same value
on all six.**  §13 removes ω from the formula; §14 shows the family
cannot separate the classes.  Neither alone suffices.

### 15. The canonical realization is flat, and breaking it splits one θ into two families

The Weyl pair is monomial, and §6 makes the monomial group the exact
annihilator, so [W]'s own object — the only irreducible realization at
a primitive multiplier, by [SvN], and the gate now carries that tag —
carries no defect at all.  Conjugating it by an exact rational
rotation preserves θ = 1/2 and creates a defect: R(3/5,4/5) gives
Δᴮ₀₀ = −56448/390625, R(5/13,12/13) gives Δᴮ₀₀ = −407836800/815730721.
**One θ, two bases, two different families.**

**What that shows, and what it does not (round-1 repair m5).**  It
shows the **SPLIT** — θ does *not* determine the Δᴮ-family — which is
§16's first direction, exhibited here on two matrices.  It does **not**
show that the basis *determines* the family: no map from bases to
families is exhibited anywhere in this unit, and two conjugators is
not a determination.  The earlier phrasing "the basis controls the
defect" over-read a two-point exhibit and is **withdrawn**.

### 16. The double dissociation, on the committed carriers themselves

Every ordered pair of W1′'s two committed families is classified by
whether its group commutator UVU⁻¹V⁻¹ is a scalar — in which case the
pair generates a projective ℤ²-action whose β(e₁,e₂) is that scalar —
and by the full fingerprint of its Δᴮ-family over the nine words
U^aV^b, a,b < 3 (all 81 ordered word pairs).  No sampling: all
9216 + 3969 pairs.

| family | θ | pairs | distinct Δᴮ-families | zero family present | monomial × monomial |
|---|---|---|---|---|---|
| 2×2 | 0 | 1144 | 22 | yes | 448 |
| 2×2 | **1/2** | 264 | **4** | yes | 192 |
| 3×3 | 0 | 435 | 14 | yes | 396 |
| 3×3 | **1/3** | 78 | **3** | yes | 72 |
| 3×3 | **2/3** | 78 | **3** | yes | 72 |

All 640 + 540 monomial × monomial projective pairs are Δᴮ-flat, at
every θ — §6's prediction.  The non-monomial ones are not: **committed
projective pairs with θ ≠ 0 carry nonzero Δᴮ-families** (3 distinct
nonzero families at 2×2, 4 at 3×3).  And then:

- **SPLIT — θ does not determine the family.**  At one fixed θ = 1/2
  the committed carriers realize 4 distinct Δᴮ-families; at θ = 1/3
  and at θ = 2/3, 3 each.
- **COLLISION — the family does not determine θ.**  One and the same
  family (the identically zero one) is realized at θ = 0 and θ = 1/2
  in the 2×2 family, and at θ = 0, 1/3 and 2/3 in the 3×3 family.

Both directions fail at once, on committed objects, in exact
arithmetic.

### 17. The covariance law, the odd channel, and what the parity argument actually delivers

*Rewritten at round 1.  The earlier version of this section was wrong
at three separate joints, and each is corrected below rather than
patched.*

**(a) The law is a COVARIANCE, and the carrier-independent obstruction
needs no parity at all.**  Under R : (U₂,U₁) ↦ (U₁ᵀ, U₂ᵀ) — reverse
the order, transpose each step — Δᴮ goes to its **transpose**:

    Δᴮ  ⟼  (Δᴮ)ᵀ.

Gated on all 13,185 census pairs.  It follows that every scalar
functional of Δᴮ that is **transpose-invariant** — the trace, the
entry sums, the Frobenius norm, every symmetric function of the
spectrum — is reversal-**even**; gated for the trace separately.  It
does **not** follow that "the Δᴮ-family is reversal-even", and that
statement is **false** as it stands.  See (b).

The obstruction that actually carries weight is one line and needs
neither parity nor any committed value set: **Δᴮ has real entries** —
immediately from §1, |Σw|² − Σ|w|² — gated as conj(x) = x on all
72,585 census entries.  So every real-polynomial functional of Δᴮ is
**real**, and a real number of modulus 1 is **±1**.  That is
carrier-independent and it is the load-bearing step.

**(b) The family has an ODD channel, and it is not empty.**  Split

    Δᴮ = S + A,   S = (Δᴮ + (Δᴮ)ᵀ)/2,   A = (Δᴮ − (Δᴮ)ᵀ)/2;

under R, S is even and **A is reversal-ODD**.  A is a genuine channel
of the family:

- **Off the committed families A ≠ 0.**  Declared witness set at 3×3,
  exact rational arithmetic: W = {R₀₁, R₁₂, R₀₁F₃, R₁₂F₃} with R_{kl}
  the rational rotation [[3/5,−4/5],[4/5,3/5]] in the (k,l) plane
  (§6's own probe) and F₃ the committed 3-point DFT.  All four are
  unitary; **none lies in W1′'s committed 3×3 family**; and A ≠ 0 on
  **12 of the 16 ordered pairs**, with A ↦ −A under R on all 16.
  First witness (R₀₁, R₀₁F₃): A has entries ±14/625 off the diagonal.
- **On the committed families A ≡ 0** — 0 of 9216 at 2×2 and 0 of 3969
  at 3×3.  At 2×2 this is *forced* (a multiple of [[1,−1],[−1,1]] is
  symmetric); at 3×3 it is a **contingent property of that family**,
  and it is labelled as such.  It is not a property of Δᴮ.

So the accurate statement, and the one any successor must carry, is:
**Δᴮ is reversal-covariant; transpose-invariant functionals of it are
reversal-even; its antisymmetric part is reversal-odd and is generally
nonzero.**

**(c) What parity still adds, and under what condition.**  Parity's
residual content is confined to **complex-valued** functionals, where
realness does not decide — and it is **conditional on identifying this
R with loop reversal**, which is exactly what [D71b] Clause 3 says is
not written:

> v6's reversal reverses **transport order** (`T_A T_B` vs `T_B T_A`);
> v7's reversal reverses a **record's own order relations**… **The
> bridge is one identification and one closure, and neither is
> written.**
> — `v10/note-d71b-holonomy-phase-identity.md:623-631`

And Clause 2's *naming* of the transformation law as a holonomy law is
itself flagged `[MY READING]` in its own note (`:769-775`): what is
measured is the law (dual-conjugation error exactly 0), not the name.
Both disclosures are made here because the parity leg rests on them.

**(d) What is withdrawn.**  The old chain ended "…hence z = ±1; and −1
is realized nowhere in the committed values ([D74] D2)".  **That step
is deleted.**  D74's D2 is about D74's *own* value set — positive
rationals — and says nothing about the values of Δᴮ.  For Δᴮ's own
values the **±1 escape is wide open**, and both branches are occupied
on committed pairs:

    tr Δᴮ = +1  at 2×2 family pair (28, 29),
    tr Δᴮ = −1  at 2×2 family pair (28, 34),

each occurring **512 times** over the 9216-pair 2×2 census (and
neither occurring in the 3×3 one).  Both are gated.
The conclusion that survives is the weaker and true one: **a
transpose-invariant functional of Δᴮ is reversal-even and real, so it
cannot be a generic unimodular phase — but it can be ±1, and is.**

### 18. The missing-piece census

| candidate | status | what is missing |
|---|---|---|
| **CAND-1** D74's transport holonomy r, group ⟨2,3⟩ | a group of VALUES in (ℝ⁺,×); no committed action on any space; ℝ⁺ ∩ U(1) = {1} | the action ρ : ℤ² → PU(H), and a U(1)-valued cocycle |
| **CAND-2** the i-twist L′ = e^{i log r} ([D74] D4.1) | committed and committed-dead — the law it restores is D1's own identity; log r is a holonomy, an H¹ object, and e^{i log r} is a character-valued H¹ object | the antisymmetric BILINEAR pairing that an H² class *is* (§12) |
| **CAND-3** v7 paper 30's e^{−kE}e^{iΦ(O)} ([D71b] §3.2) | a phase built from a LINEAR functional Φ of the reversal-odd channel O = F − F*: a character, not a multiplier.  §17 as rewritten scopes the parity leg: what sits opposite Φ's channel is not "the Δᴮ-family" but its **transpose-invariant functionals**, Δᴮ's own antisymmetric part being odd and generally nonzero | the pairing and the closure — outright.  The parity mismatch is real for transpose-invariant functionals but **conditional** on an identification [D71b] Clause 3 says is unwritten, so it supports and does not stand alone |
| **CAND-4** D42b4's ∏√q amplitude ([D71b] §4.2) | the right carrier — it is the square root of the process's own weights — but assigned per complete history, with no loop/cycle/closure/holonomy anywhere in its note and its phase slot filled with +1 without an argument | the closure device, hence any commutator at all |
| **CAND-5** W1′'s U(1)-Gram edge phases g_ab = z_a conj(w_b) | committed and gated: the 4-cycle holonomy is identically 1 in W1′'s **two separate gates** — 4096 quadruples of the π/4 family (exhaustive) and 4096 of the π/8 family (a₀ = 0 fixed, the holonomy being invariant under z_a ↦ λz_a and w_b ↦ μw_b independently).  They are different sweeps over different families and are cited separately, not as one sweep of 8192 (round-1 repair m4).  Every factorized edge phase is a coboundary | non-factorizability; the class is zero by construction |
| **CAND-6** the canonical Weyl / NC-torus pair ([W]) | the action EXISTS and [ω] ≠ 0 for every θ ∈ (1/N)ℤ — but it is monomial, so its Δᴮ-family is identically zero, and all N classes share one Born shadow | NOT MISSING, REFUTING: the action exists and controls nothing |
| **CAND-7** W1′'s committed families as carriers | exhaustive over 13,185 ordered pairs: 1999 generate a projective ℤ²-action, and the non-monomial ones DO carry a nonzero Δᴮ-family — but the same θ carries several families and the same family occurs at several θ | NOT MISSING, REFUTING: the carriers realize the action and the correspondence fails in both directions at once |

### 19. The verdict, split by requirement

- **(1) the ACTION.**  D74's ⟨2,3⟩ never acts.  But other committed
  objects do carry projective ℤ²-actions: 1999 of W1′'s 13,185 ordered
  pairs.  Requirement (1) is met, by carriers unrelated to the
  generated group.
- **(2) the CLASS.**  Those carriers realize θ = 1/2 (2×2) and
  θ = 1/3, 2/3 (3×3) — genuinely nontrivial classes.  Requirement (2)
  is met.
- **(3) the CONTROL.**  This is what fails, **and the attribution
  matters (round-1 repair M1).  The failure of (3) is a theorem — §13
  PLUS §14.**  §13 removes ω from the formula; §14 shows the family
  cannot separate the classes.  §13 alone does not suffice, because
  [ω] is itself a lift-independent invariant of ρ, so "ω absent from
  the formula" does not imply "no functional of the family determines
  [ω]" — were B injective on PU(N), (3) would be met and §13 would
  hold verbatim.  §14 supplies what is missing: B(Z^k) = I forces
  β_B = P^a independent of k, so every finite-dimension-realizable
  class (θ ∈ (1/N)ℤ, by W2c's own determinant argument) collapses onto
  one identical family, and any functional whatsoever takes the same
  value on all of them.  §16 then measures the same failure again,
  independently, on committed carriers.

**W2b-NO-ACTION** therefore names the failure precisely: not that no
projective action can be built from committed objects, but that the
multiplier of any such action is invisible to the Δᴮ-family — and that
the generated ℤ² in particular is not the group that acts.

---

## W2c — SELECTION

**W2c-VACUOUS.**  No class survives W2b, so there is no θ to select.
Two facts are gated anyway, because they are what any future bridge
would face.

**θ is quantized by dimension.**  From UV = ωVU on ℂ^N,
det(UV) = det(U)det(V) while det(ωVU) = ω^N det(V)det(U), so
**ω^N = 1**: on ℂ^N only θ ∈ (1/N)ℤ is realizable, and the continuum
H²(ℤ², U(1)) ≅ U(1) is reached only in a limit.  Gated: det(AB) =
det(A)det(B) as a polynomial identity at d = 2, 3; ω^N = 1 on the
realized Weyl pairs at N = 2..6.

**No committed principle selects θ.**  The corpus supplies a value
group in (ℝ⁺,×) with no unimodular part ([D74] D2), a phase form on a
reversal-odd channel with no bilinear pairing ([D71b] Clauses 2 and 3),
and an amplitude carrier with no closure ([D71b] §4.2).  None of the
three fixes a dimension N, a residue k, or a pairing.  Paper 0 v2.1's
own reading of θ as ħ-like is explicitly conditional on the generators
carrying physical dimensions and the exponent being a symplectic
pairing; no committed object supplies either.

---

## 20. What would reopen W2b

A committed object that (a) represents the generated group by
**operators on a common space** rather than by values, (b) supplies an
**antisymmetric bilinear pairing** on it, and (c) breaks monomiality in
the configuration basis so that the defect is nonzero where the
multiplier lives.  §13 and §14 together say even all three do not
suffice, and a fourth thing is needed.

**What the fourth thing is — and it is not what this note previously
said (round-1 repair M2).**  It is **not** "an invariant of the *lift*
rather than of the projective representation".  That was
cohomologically **backwards**, and it is the most consequential
sentence the round corrected.  [ω] **is** an invariant of the
projective map ρ — it is precisely *lift-independent*, which is what
makes it a cohomology class at all — while lift-**dependent**
quantities are gauge artifacts of a choice and can never detect it.
Chasing the lift is chasing the gauge.

What a successor needs is a **phase-retaining invariant of the
projective map ρ that is finer than its Born shadow B∘ρ**: a
functional that sees the **relative phases of matrix entries**, which
B annihilates entrywise.  **B is the whole obstruction; the lift never
was.**

---

## 21. Antecedents

Every theorem used carries its citation in the receipt **at the gate
where it is used**, and the round was right that three did not: they do
now.  **[SvN]** tags §15's base-Weyl-pair gate, **[WK/CAZAC]** tags
both of §8's equivalence gates, and **[D71b]** tags §17's ±1-escape
gate (round-1 repair M5).

- **[B1]** Barandes, arXiv 2302.10778 — the identification of the
  Born-projection cross terms with interference.  §1's closed form is
  his sum, rewritten; the identification is not originated here.
- **[W]** Weyl relations / noncommutative torus: projective multipliers
  on ℤ², realized by the clock/shift pair (e.g. arXiv 1606.01829).
  W1′ named it and used it at no gate; this is the unit where it is
  used, and where it fails.
- **[WK/CAZAC]** The **discrete Wiener–Khinchin theorem** (the
  periodic autocorrelation of a sequence and the squared modulus of
  its DFT are a transform pair) and the classical theory of **CAZAC /
  perfect sequences**, for which "flat |DFT|" *is* the defining
  property, with explicit constructions at every N: Björck; Chu and
  Zadoff–Chu; Frank; Turyn; Golomb and Gong, *Signal Design for Good
  Correlation*.  **§8 originates neither.**  What §8 claims is the
  identification — Δᴮ = 0 on the DFT-sandwich family ⟺ that known
  condition on the interleaving diagonal.  The equivalence between the
  two characterizations is re-gated for the four N in scope as an
  arithmetic check, not proven here.
- **[SvN]** Stone–von Neumann, finite form: on ℂ^N the irreducible
  projective representations of ℤ² with a primitive q-th root
  multiplier have dimension exactly q and are the Weyl pair up to
  unitary equivalence and scalars.  **Cited**, not proven here; used
  only to say the Weyl realization is not an exotic corner.
- **[REV2]** the second external hostile review, LOG #4 — the
  three-defect distinction, the coherence law (W2a's seed), and the
  B(ωU) = B(U) observation that forced the W2a/W2b/W2c staging.
- **[W1′]** `note-w1p-three-class.md` + `code/w1p_three_class_exact.py`,
  TERMINAL at LOG #7 — sliced and reused; its committed gate values are
  this unit's anchors.
- **[D74]** `v10/note-d74-transport-holonomy-result.md` + its receipt,
  TERMINAL, round-1 reviewed — the generated group, the value set, D2,
  D4.1, D9.1.
- **[D71b]** `v10/note-d71b-holonomy-phase-identity.md` — Clause 2 (the
  reversal-odd placement, dual-conjugation error exactly 0), Clause 3
  (the loop is not written), §4.2 (∏√q has no closure).  **Two
  disclosures the round required, because §17's parity leg rests on
  them.**  Clause 3 is `[SILENT]` and says so of itself: *"The bridge
  is one identification and one closure, and neither is written"*
  (`:623-631`) — so identifying §17's R with loop reversal is
  **not** written anywhere in the corpus.  And Clause 2's *naming* of
  the transformation law as a holonomy law is flagged `[MY READING]`
  in that note's own reading-claims paragraph (`:769-775`); what is
  `[MEASURED]` is the law, at dual-conjugation error exactly 0, not
  the name.

---

## 22. Scope

1. **No claim about nature.**  Every result is a statement about a
   declared matrix-valued defect and declared finite families.
2. **W2a's results are about Δᴮ, not about quantum mechanics.**  §4's
   tree law is an identity of associativity and §5 measures exactly
   that: it constrains the family and selects nothing.
3. **§6 is a hand proof with gated ingredients.**  The quantifier over
   all unitaries is carried by the probe argument; the sweeps
   corroborate on two finite families.
4. **§8's closed form is stated for the DFT-sandwich family** at
   N = 2, 3, 4, 5 with the declared phase groups.  It is not a claim
   about all unitaries.  **And §8's claim is the IDENTIFICATION only**:
   the equivalence of flat |DFT| with zero periodic autocorrelation is
   the discrete Wiener–Khinchin theorem and the definition of a CAZAC
   sequence, cited as [WK/CAZAC] and not originated here.
5. **§16's table is a census of two committed families**, not of U(n).
   The projective pairs found there generate projective ℤ²-actions
   through finite quotients; that is what a scalar commutator gives.
6. **W2b-NO-ACTION is scoped by §19.**  Requirements (1) and (2) are
   met by committed objects; only (3) fails.  **The failure of (3) is
   a theorem — §13 PLUS §14** (round-1 repair M1): §13 removes ω from
   the formula, §14 shows the family cannot separate the classes.
   §13 alone is *not* the no-go, since [ω] is a lift-independent
   invariant of ρ.  §16 is an independent measured confirmation on
   committed carriers.
7. **§17 delivers less than its old title claimed.**  What is gated is
   a *covariance* law, the reality of Δᴮ's entries, a nonzero odd
   channel off the committed families, and both ±1 witnesses.  What is
   *not* gated, and is now explicitly conditional on an identification
   [D71b] Clause 3 calls unwritten, is any statement that the
   multiplier and the defect sit on opposite parity channels.
8. **Nothing here is a claim about W3′ or W4′.**  §9 is
   reporting-only; the general record theorem is W3′'s, and whether the
   Δᴮ-structure is the same obstruction the contextual and BC
   invariants measure is W4′'s open question.
9. Paper 0 v2.1 §5's non-claims stand unmodified.  The H¹ formulation
   remains dead.

---

## 23. What this unit hands over

- **W2a delivers** the closed form (§1), the invariance group (§2), the
  doubly-centred structure with sharp bounds, a gated non-negative
  s_ij, and the exact n = 2 range with both ends witnessed (§3), the
  tree coherence law at every n (§4), the content-free demonstration
  with all six of its gates disclosed (§5), the exact two-sided
  annihilator (§6), the failure of local determination (§7), the
  identification of the alignment condition with the CAZAC condition
  (§8), and the three killing conditionings (§9).
- **W2b delivers** the no-go, and its two halves are named separately:
  the multiplier cancels from the *formula* (§13), and **six classes
  collapse onto one Born shadow** — gated uncapped at N = 6 over all
  7776 word pairs — so that no functional can separate them (§14).
  Those two *together* are the theorem.  The committed carriers then
  exhibit the double dissociation in both directions (§16),
  independently, with the covariance law and its odd channel (§17) and
  the missing-piece census (§18).
- **W2c is vacuous**, with θ's dimension quantization θ ∈ (1/N)ℤ gated
  anyway, so that a future bridge knows what it must supply.
- **W3′ receives** §9's three killing conditionings, and §6's
  annihilator as the algebraic boundary of "the defect dies here".
- **W4′ receives §17 in its corrected form, and the correction is the
  point** (round-1 repair M4).  The handover is **not** "the Δᴮ-family
  is reversal-even" — that is **false unqualified** and would have
  poisoned anything built on it.  What W4′ receives is:
  1. the **covariance law** Δᴮ ↦ Δᴮᵀ under order-reversal-with-
     transpose;
  2. hence: **transpose-invariant** functionals of Δᴮ — and only
     those — are reversal-even;
  3. the family's **antisymmetric part A is reversal-ODD** and is
     **not** identically zero (12 of 16 pairs of a declared exact
     witness set at 3×3); A ≡ 0 on all 3,969 committed 3×3 pairs and
     all 9,216 committed 2×2 pairs is a property **of those families**,
     not of Δᴮ;
  4. the carrier-independent obstruction that needs none of the above:
     **Δᴮ has real entries**, so real-polynomial functionals are real
     and a real unimodular value is ±1;
  5. and the standing warning that **±1 is not excluded** — both
     values occur on committed pairs — so any argument routed through
     [D74] D2 at this joint is invalid.
- **The [W] line closes here** for the Δᴮ-family: the object exists,
  the class exists, and the Born projection cannot see either.  What
  would reopen it is a **phase-retaining invariant of ρ finer than
  B∘ρ**, not an invariant of the lift (§20).
