# v12 W2 — THE MULTIPLIER LADDER: THE DEFECT ALGEBRA, THE PROJECTIVE
# DESCENT NO-GO, AND THE VACUOUS SELECTION

**Status:** GREEN-UNREVIEWED, STRICT, 2026-07-28.
**Pin:** `note-w2-multiplier-ladder-pin.md` (frozen before any code).
**Binding:** paper 0 v2.1 §1 (T2′, Δᴮ and the three-defect
distinction), §4 W2′ (the three-way split, verbatim), §5 (non-claims);
LOG #1–#8.
**Receipt:** `v12/code/w2_multiplier_ladder_exact.py` →
`v12/code/w2_output.txt`.  **32 anchors, 152 gates, 152 pass, 0 fail**
(of which 8 carry no independent information and are named in-receipt:
**144 independent-evidence gates**); runtime 283.9 s; re-run at
`PYTHONHASHSEED=7` identical apart from timings.
**Verdicts:** **W2a-STRUCTURE-DELIVERED / W2b-NO-ACTION /
W2c-VACUOUS.**

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

At n = 2 the family is **one-dimensional**: Δᴮ is a multiple of
[[1,−1],[−1,1]] whose parameter is 2Re(A₀B₀) with A_i = (U₂)_{i0}
conj((U₂)_{i1}) and B_j = (U₁)_{0j}conj((U₁)_{1j}) — W1′'s
phase-alignment obstruction — and **its exact range is [−½, ½]**, both
ends attained by the Hadamard pair (H,H).  The bound follows from the
AM-GM certificate (x+y)² − 4xy = (x−y)²; the range is read off all
9216 census pairs with the exact ℚ(√2) sign oracle.

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
map whatsoever.  Made concrete: the same identity is gated with B
replaced by five declared non-Born maps — the identity map, entrywise
Re, the entrywise square without modulus, the transpose, and
M ↦ M + 2Mᵀ + 3I — on 432 ordered triples each.  It holds for all
five.  **A law that survives replacing its subject constrains the
subject not at all**: the coherence law is an identity of
associativity.  (The identity-map instance is degenerate, both sides
being identically zero; it is named as such in-receipt.)

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

    Δᴮ = 0  ⟺  |DFT(ε)(s)| = √N for every s
            ⟺  ε has zero periodic autocorrelation at every nonzero lag
               (a CAZAC / perfect sequence).

**Δᴮ = 0 is phase alignment, and the alignment condition is flatness of
a Fourier spectrum.**  Gated with ε₀ = 1 fixed: N = 2 over μ₈ in
ℚ(ζ₈) (8 diagonals, 2 flat), N = 3 over μ₆ in ℚ(ζ₁₂) (36, 6), N = 4
over μ₈ in ℚ(ζ₈) (512, 16), N = 5 over μ₅ in ℚ(ζ₅) (625, 20); 0
mismatches against either characterization, and the Wiener–Khinchin
equivalence between them gated exactly.

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
word of the Weyl group at N = 2..6 against every scalar of the carrier
field.

### 14. Four classes, one Born shadow

Take U = X_N (shift), V = Z_N^k (clock power), k = 0..N−1.  The
commutator is ζ_N^{−k}·I, so the class has order N/gcd(N,k) — every
class realizable on ℂ^N, the trivial one included.  But B(Z_N^k) = I
for every k, so β_B(a,b) = B(X^a Z^{kb}) = P^a with P the shift
permutation, **independent of k**.

At N = 6 the classes have orders **1, 2, 3 and 6** — four distinct
elements of H²(ℤ², U(1)) — carried by realizations with literally
identical Born data and an identically zero Δᴮ-family.  Gated at
N = 2..6 (all N² words per class; all N⁴ ordered word pairs for
N ≤ 4, the 9×9 sub-block for N = 5, 6).  **No functional of the
Δᴮ-family can separate them.**

### 15. The canonical realization is flat, and breaking it hands control to the basis

The Weyl pair is monomial, and §6 makes the monomial group the exact
annihilator, so [W]'s own object — the only irreducible realization at
a primitive multiplier, by [SvN] — carries no defect at all.
Conjugating it by an exact rational rotation preserves θ = 1/2 and
creates a defect: R(3/5,4/5) gives Δᴮ₀₀ = −56448/390625, R(5/13,12/13)
gives Δᴮ₀₀ = −407836800/815730721.  **One θ, two bases, two different
families**: the basis controls the defect.

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

### 17. The parity obstruction

(v) is the family's reversal law: under R : (U₂,U₁) ↦ (U₁ᵀ, U₂ᵀ) —
reverse the order, transpose each step — Δᴮ goes to its transpose.
Hence **every scalar functional of Δᴮ that is transpose-invariant** —
the trace, the entry sums, the Frobenius norm, every symmetric function
of the spectrum — **is reversal-EVEN**.  Gated on all 13,185 census
pairs, for the law and for the trace separately.

A U(1) holonomy is reversal-ODD by definition:
Hol(γ⁻¹) = conj(Hol(γ)).  That is [D71b] Clause 2's finding — the
corpus's only phase-shaped amplitude is placed on the reversal-odd
channel, at dual-conjugation error exactly 0, and no other placement
transforms like a holonomy.  A quantity that is both reversal-even and
unimodular satisfies z = conj(z) and |z| = 1, hence z = ±1; and −1 is
realized nowhere in the committed values ([D74] D2).  **The multiplier
and the defect sit on opposite parity channels.**

### 18. The missing-piece census

| candidate | status | what is missing |
|---|---|---|
| **CAND-1** D74's transport holonomy r, group ⟨2,3⟩ | a group of VALUES in (ℝ⁺,×); no committed action on any space; ℝ⁺ ∩ U(1) = {1} | the action ρ : ℤ² → PU(H), and a U(1)-valued cocycle |
| **CAND-2** the i-twist L′ = e^{i log r} ([D74] D4.1) | committed and committed-dead — the law it restores is D1's own identity; log r is a holonomy, an H¹ object, and e^{i log r} is a character-valued H¹ object | the antisymmetric BILINEAR pairing that an H² class *is* (§12) |
| **CAND-3** v7 paper 30's e^{−kE}e^{iΦ(O)} ([D71b] §3.2) | a phase built from a LINEAR functional Φ of the reversal-odd channel O = F − F*: a character, not a multiplier | the pairing; the closure; and the parity is wrong (§17) |
| **CAND-4** D42b4's ∏√q amplitude ([D71b] §4.2) | the right carrier — it is the square root of the process's own weights — but assigned per complete history, with no loop/cycle/closure/holonomy anywhere in its note and its phase slot filled with +1 without an argument | the closure device, hence any commutator at all |
| **CAND-5** W1′'s U(1)-Gram edge phases g_ab = z_a conj(w_b) | committed and gated: the 4-cycle holonomy is identically 1 on 8192 quadruples — every factorized edge phase is a coboundary | non-factorizability; the class is zero by construction |
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
- **(3) the CONTROL.**  This is what fails, and it fails as a theorem
  (§13) and twice over as a measurement (§14, §16).

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
multiplier lives.  §13 says even all three together do not suffice: the
multiplier still cancels from the family, so a fourth thing is needed —
an invariant of the **lift** rather than of the projective
representation, which the Born projection cannot see by construction.

---

## 21. Antecedents

Every theorem used carries its citation in the receipt at the gate
where it is used.

- **[B1]** Barandes, arXiv 2302.10778 — the identification of the
  Born-projection cross terms with interference.  §1's closed form is
  his sum, rewritten; the identification is not originated here.
- **[W]** Weyl relations / noncommutative torus: projective multipliers
  on ℤ², realized by the clock/shift pair (e.g. arXiv 1606.01829).
  W1′ named it and used it at no gate; this is the unit where it is
  used, and where it fails.
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
  (the loop is not written), §4.2 (∏√q has no closure).

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
   about all unitaries.
5. **§16's table is a census of two committed families**, not of U(n).
   The projective pairs found there generate projective ℤ²-actions
   through finite quotients; that is what a scalar commutator gives.
6. **W2b-NO-ACTION is scoped by §19.**  Requirements (1) and (2) are
   met by committed objects; only (3) fails.  The failure of (3) is a
   theorem (§13) with two independent measured confirmations.
7. **Nothing here is a claim about W3′ or W4′.**  §9 is
   reporting-only; the general record theorem is W3′'s, and whether the
   Δᴮ-structure is the same obstruction the contextual and BC
   invariants measure is W4′'s open question.
8. Paper 0 v2.1 §5's non-claims stand unmodified.  The H¹ formulation
   remains dead.

---

## 23. What this unit hands over

- **W2a delivers** the closed form (§1), the invariance group (§2), the
  doubly-centred structure with sharp bounds and the exact n = 2 range
  (§3), the tree coherence law at every n (§4), the content-free
  demonstration (§5), the exact two-sided annihilator (§6), the failure
  of local determination (§7), the flat-spectrum form of the alignment
  condition (§8), and the three killing conditionings (§9).
- **W2b delivers** the no-go: the multiplier cancels from the family
  identically (§13), four classes share one Born shadow (§14), and the
  committed carriers exhibit the double dissociation in both
  directions (§16), with the parity obstruction (§17) and the
  missing-piece census (§18).
- **W2c is vacuous**, with θ's dimension quantization θ ∈ (1/N)ℤ gated
  anyway, so that a future bridge knows what it must supply.
- **W3′ receives** §9's three killing conditionings, and §6's
  annihilator as the algebraic boundary of "the defect dies here".
- **W4′ receives** §17's parity statement: the Δᴮ-family is
  reversal-even, which any proposed identification with a
  holonomy-shaped obstruction must clear.
- **The [W] line closes here** for the Δᴮ-family: the object exists,
  the class exists, and the Born projection cannot see either.
