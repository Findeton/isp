# v12 W7 — THE PHASE-RETAINING LOOP SIGNATURE: THE GAUGE REDUCTION,
# THE PAIR-ORBIT THEOREM, AND THE COMPLETENESS NO-GO

**Status:** GREEN-UNREVIEWED, STRICT, 2026-07-29.
**Pin:** `note-w7-loop-signature-pin.md` (frozen at commit e5d1d44, before
any code).
**Binding:** paper 0 v2.2 §1 (T2′, T3′), §4 (W2′, W3′, the W7 entry), §5
(O2 and the four-gate rule); LOG #16, #18, #19.
**Receipt:** `v12/code/w7_loop_signature_exact.py` →
`v12/code/w7_output.txt`. **41 anchors, 78 gates, 78 pass, 0 fail**;
runtime 189.0 s; re-run at `PYTHONHASHSEED=7` byte-identical apart from
timings. Lean: NONE.

**Verdicts.** **G-REDUCED** at W7-0 — the reduction of the full
Schur–Hadamard gauge to the boundary gauge is *derived*, by two
independent routes, not chosen. **W7-SIGNATURE-INCOMPLETE-SEAM-DATUM-NAMED**
at W7-3 — the pinned triple (cycle holonomies + relation loops + the
cut-coherence tensor 𝒞) is **not** complete for two-step composition;
the no-go is exhibited in exact unitary arithmetic at n = 4, and the
missing seam datum is named and gated.

Arithmetic: `fractions.Fraction` for every rational; the cyclotomic
fields ℚ(ζ_n), n = 2, 3, 4, 5, 6, 8, 12, 16 (canonical representation
modulo Φ_n, so tuple equality *is* field equality) for every complex
algebraic quantity; integer linear algebra with Smith normal form over ℤ
for every lattice statement. No float in any substantive path; no
tolerance anywhere. Substantive negatives exit 0; exit 1 is anchor-only.

**Instruments are read, not copied.** W1′'s arithmetic layer, matrix
layer and two census families, and W3′'s record model, hypotheses and
decision procedure, are extracted from the committed source files by AST
slice (30 and 7 top-level definitions) and executed here. The 41 anchors
are the parents' own committed numbers — among them Δᴮ(H,H) =
[[½,−½],[−½,½]], the two census tables 5120/0/1024/3072 and
3888/0/54/27, T2′'s exact rotation counterexample (Δᴮ₀₀ = −4032/15625
with the stochastic divisor K = S(−175/527)), W2's cap-free B4x collapse
(7,776 ordered word pairs, 0 nonzero, six distinct β = ζ₆^{−k}), the B5
conjugation defects −56448/390625 and −407836800/815730721, the B7
odd-channel witness with its ±14/625 entries, and W3′'s dim-4 eraser
with its 0, ±½ residual. A drift in any parent exits 1.

**Scope engraving.** W7 is one-chart / common-carrier mathematics. It
does not solve cross-chart co-reference; W6 owns that bridge.

---

## W7-0 — THE GAUGE CENSUS

### 1. The declared gauges

| | transformation | status |
|---|---|---|
| (a) | full Schur–Hadamard: U_ij ↦ e^{iθ_ij}U_ij, θ independent per **ordered pair** | [B3] p.12 eqs. 29–30; W5 I-13 |
| (b) | projective scalar: U ↦ ωU | |
| (c) | configuration-basis rephasing: U ↦ D U D⁻¹ | same space |
| (d) | source/target boundary: U ↦ D_out U D_in | bipartite; in and out distinct |
| (e) | compensated cut: (U₂,U₁) ↦ (U₂D, D⁻¹U₁) | [W2] A2(iii) |
| (f) | everything else | physical |

Call a Schur matrix Θ of **boundary form** iff Θ_ij = d_i conj(e_j) for
unimodular d, e. The whole census turns on which Schur matrices are of
boundary form.

### 2. The two facts the pin demanded first

**The full-Schur orbit is exactly the modulus class.** For any U the
orbit is { V : |V_ij| = |U_ij| ∀ i,j }: one inclusion is immediate, and
for the other, given V with matching moduli put Θ_ij = V_ij/U_ij on the
support (unimodular, since the moduli agree) and 1 off it. Hence **every
full-Schur invariant is a function of B(U) alone — moduli and support,
no phase.** Gated constructively on 1,152 ordered pairs of W1′'s 2×2
family, the connecting Θ built and gated unimodular in every reachable
case (G0.1); and 3 of the 2×2 Born-shadow classes contain more than one
matrix, all of whose members differ in phase (G0.2).

**Triangular products are not invariants of the committed gauge.** The
founding sketch proposed u_ij u_jk u_ki. That object is a **ray/Gram**
invariant [MSS] — invariant under the *one-index* gauge
g_ij ↦ conj(λ_i) λ_j g_ij on a single space, where the phases telescope
around **any** cycle, odd ones included. It is not an invariant of the
committed matrix gauge, for two separate reasons, both gated on all 9
full-support members of W1′'s committed 3×3 family: it is moved by a
declared unimodular Θ (G0.3), and it is moved by the declared boundary
gauge D_out = diag(1,1,ζ₃), because the row phases contribute
d₀d₁d₂ ≠ 1 — **odd cycles do not close in a bipartite support graph,
where rows and columns carry independent phases** (G0.4). The same gate
confirms the correct typing: under the ray/Gram gauge the triple product
*is* invariant, 9 of 9. That is [MSS]'s setting, and it is a different
gauge from the committed one.

The even 4-cycle survives. The Haagerup-type invariant

    H_{ii′;jj′}  =  U_ij U_i′j′ conj(U_ij′) conj(U_i′j)

has gauge factors (d_i e_j)(d_i′e_j′)(d_i e_j′)⁻¹(d_i′e_j)⁻¹ = 1,
gated over 9 matrices × 6 gauges × 9 index quadruples (G0.5).

### 3. THE COMPOSITION-COMPATIBILITY THEOREM

Objects are configuration spaces; an arrow U : V_a → V_b is a matrix.
A Schur gauge family {Θ^{(b,a)}} is **composition-compatible** iff for
every composable pair

    (Θ^{(2,1)} ∘ U₂)(Θ^{(1,0)} ∘ U₁)  =  Θ^{(2,0)} ∘ (U₂U₁),

i.e. the transformed factors compose to the transformed composite: the
gauge is an endofunctor fixing objects.

**Theorem.** Over unitary arrows in dimension ≥ 2, a Schur gauge family
is composition-compatible **iff**

    Θ^{(b,a)}_{ij}  =  d^{(b)}_i · conj(d^{(a)}_j)

for object-indexed unimodular functions d^{(a)}. Hence the
composition-compatible subgroup of the full Schur–Hadamard gauge is
**exactly the boundary gauge**.

*Proof.* (⇐) Θ^{(b,a)}∘U = D_b U D_a⁻¹, and
(D₂U₂D₁⁻¹)(D₁U₁D₀⁻¹) = D₂U₂U₁D₀⁻¹.

(⇒) Entrywise the requirement reads, for each (i,j),

    Σ_k Θ^{(2,1)}_{ik} Θ^{(1,0)}_{kj} w_k
        = Θ^{(2,0)}_{ij} Σ_k w_k,      w_k = (U₂)_{ik}(U₁)_{kj}.

Take U₂ = V D_c and U₁ = D_c′ V′ with V, V′ the DFT-sandwich carriers of
[W2] §8 (all entries nonzero) and c, c′ free unimodular diagonals. Then
w_k = r_k u_k with r_k ≠ 0 fixed and u an arbitrary unimodular vector.
Subtracting the requirement at u and at u with slot k negated gives
2(Θ^{(2,1)}_{ik}Θ^{(1,0)}_{kj} − Θ^{(2,0)}_{ij}) r_k = 0, hence the
pointwise functional equation

    (★)   Θ^{(2,1)}_{ik} Θ^{(1,0)}_{kj}  =  Θ^{(2,0)}_{ij}
          for all i, j, k.

Fix k₀ and set a_i := Θ^{(2,1)}_{ik₀}, b_j := Θ^{(1,0)}_{k₀j}. Then
Θ^{(2,0)}_{ij} = a_i b_j, and (★) forces Θ^{(1,0)}_{kj}/b_j to be
independent of j, say c_k; so Θ^{(1,0)}_{kj} = c_k b_j and
Θ^{(2,1)}_{ik} = a_i conj(c_k). Taking d^{(2)} = a, d^{(1)} = c,
d^{(0)} = conj(b) gives the boundary form. ∎

**Both halves of the equivalence are gated, exhaustively over declared
finite phase groups** (G0.6). At n = 2 over μ₄: of 65,536 ordered
Θ-pairs, **1,024 satisfy (★), and exactly the same 1,024 admit an
object-indexed family** d^{(0)}, d^{(1)}, d^{(2)}. At n = 3 over μ₂: 256
of 262,144, again exactly matching. The gate also measures the gap that
makes the theorem's *coupling* visible: 4,096 pairs at n = 2 have both
factors of boundary form **separately**, and the surplus 3,072 is
precisely the set whose middle phase functions disagree — an
**uncompensated cut**. Separate boundary form is necessary and not
sufficient; the compensated cut is exactly the coupling condition.

A second gate closes the quantifier honestly: the sweep over W1′'s
committed unitary families is *already* enough to force (★) — 0
disagreements between "compatible on the declared family" and (★) over
65,536 and 262,144 ordered Θ-pairs respectively.

### 4. THE UNITARITY-PRESERVATION THEOREM

**Theorem.** Θ ∘ U is unitary for **every** unitary U iff every Haagerup
invariant of Θ equals 1 iff Θ is of boundary form.

*Proof.* (⇐) Θ∘U = D U E† is unitary. (⇒) For i ≠ j, orthogonality of
rows i, j of Θ∘U reads Σ_k λ_k v_k = 0 whenever Σ_k v_k = 0, with
λ_k = Θ_ik conj(Θ_jk) and v_k = U_ik conj(U_jk). Real rotations in the
(k,l) plane realize v = t(e_k − e_l) for every k ≠ l with t ≠ 0, forcing
λ_k = λ_l, i.e. H_{ij;kl}(Θ) = 1. Trivial Haagerup on every 4-cycle of
the complete bipartite graph is precisely the boundary form (the
switching reconstruction of W7-1 §6). ∎

Gated (G0.7): at n = 2 over μ₈, 512 of 4,096 Θ preserve unitarity on the
committed family and exactly 512 are Haagerup-trivial; at n = 3 over μ₂,
32 of 512, again exactly matching, with 0 disagreements against the
boundary decomposition.

**This is the precise content of [B3]'s "partial fixing of the gauge
freedom."** Fixing a unitary representative does not exhaust the Schur
freedom; the residual stabilizer is *exactly* the boundary group. W5's
I-14 records the phrase; this theorem says what it leaves.

### 5. The verdict, and its scope

Two further gates corroborate. The full Schur gauge **moves the
composite's Born shadow**: with Θ = [[1,1],[1,−1]] on (H,H),
B((Θ∘H)(Θ∘H)) ≠ B(H·H), and B(U₂U₁) is the committed two-step
transition law, so a transformation that moves it is not a gauge of a
composable system; the same Θ destroys unitarity, which is [B3]'s own
observation (G0.8). And the boundary group is gated to contain the three
named sub-gauges — projective scalar, compensated cut, same-space
rephasing — while an **uncompensated** cut insertion is gated *not* to
be a gauge: it moves Δᴮ on **192 of 576** stride pairs, independently
reproducing [W2] A2(vi)'s committed count (G0.9).

> **THE FIRST VERDICT: G-REDUCED.** The reduction of the full
> Schur–Hadamard gauge to the boundary gauge is **derived**, by two
> independent routes — composition-compatibility (§3) and unitarity
> preservation (§4) — and corroborated by the composite's Born shadow
> (§5). Neither route is a new postulate: T2′ makes the composable pair
> the subject, and W2 §3's doubly-stochastic structure requires unitary
> arrows.

**Scope, engraved.** What is reduced is the gauge of a *composable,
unitary* system. For a single arrow considered in isolation, with
neither composition nor unitarity asked of it, §2 stands and no phase
invariant exists at all. The two facts are consistent, and both are
stated: the pin's **G-ANNIHILATED** branch is exactly the
isolated-arrow reading, and it is what the committed structure excludes.

**The unit-wide kill is therefore: any candidate that changes under
boundary + compensated cut + scalar.** Every candidate below is gated
against it.

---

## W7-1 — THE SINGLE-ARROW ORBIT THEOREM

### 6. The structure, and what is antecedent

For a matrix U let G(U) be the **bipartite support graph**: vertices
Rows ⊔ Cols, an edge (i,j) carrying U_ij for each nonzero entry. The
boundary gauge acts as **vertex switching** on G(U). Traversing an edge
rows→cols contributes U_ij and cols→rows contributes conj(U_ij); around
any cycle each vertex is entered once and left once, so its phase
cancels and the **cycle holonomy is switching-invariant**. All cycles of
a bipartite graph are even, and the elementary 4-cycles are exactly the
Haagerup invariants.

**[ANTECEDENT, not W7's theorem]:** the gain-graph / switching
classification — phases on a cycle basis classify edge-phase assignments
up to vertex switching, componentwise, with cycle rank |E| − |V| + c
[GG]; and the ray/Gram Bargmann treatment [MSS]. W7's own contribution
is the exact adaptation to the committed matrix families, to support
changes, and (in W7-3) to the composable-pair graph.

Gated: the cycle rank identity μ = |E| − |V| + c on all 96 + 63
committed matrices, with μ ∈ [0,1] at 2×2 and μ ∈ [0,4] at 3×3 (G1.1);
and holonomy invariance under 24 × 256 gauges at 2×2 and 21 × 6561 at
3×3, exhaustive over the declared phase groups (G1.2).

### 7. Completeness, constructively

**Theorem.** Two matrices with the same support and the same moduli are
boundary-gauge equivalent **iff** their cycle-basis holonomies agree.

*Proof (the construction).* Fix a spanning forest of the support graph,
set the switching to 1 at each component root and propagate it along
tree edges — forced, one choice per vertex, since V_ij = d_i conj(d_j)U_ij
determines the far endpoint from the near one. Every non-tree edge then
agrees iff its fundamental-cycle holonomy agrees. ∎

Gated by *building* the switching in every positive case and verifying
it entrywise: **4,608 of 9,216** ordered 2×2 pairs and **567 of 3,969**
ordered 3×3 pairs are equivalent, with **0 disagreements** against the
holonomy test (G1.3). At full support the Haagerup 4-cycles generate the
whole lattice, so H is a complete phase invariant there (G1.4).

### 8. Support changes, and undefined phases

The moduli determine the support, and the boundary gauge can neither
create nor destroy an entry, so **support strata never mix**: 0 of
9,216 + 3,969 ordered pairs are gauge-equivalent across different
supports (G1.5). The orbit classification is therefore stratified by
support, and the invariants are not continuous across strata.

On a monomial support the cycle set is **empty** — μ = 0 for all 32 + 54
monomial members of the committed families (G1.6). **A vanished
amplitude does not have a trivial phase; it has no phase.** The
invariant is not 1, it does not exist. This bookkeeping is carried
through W7-3 and W7-4, where it becomes load-bearing.

---

## W7-2 — DEGENERATE AND MONOMIAL SUPPORTS; THE RELATION-LOOP PHASE

### 9. The single-arrow sector is empty exactly where the class lives

A monomial matrix's support is a perfect matching: n edges on 2n
vertices in n components, so μ = n − 2n + n = **0**. Gated on every Weyl
word U^aV^b, for every k, at N = 2..6 (G2.1). The single-arrow cycle
sector is empty precisely on the family whose projective class is
nontrivial — so a single-arrow signature cannot be the whole answer.

### 10. The relation-loop commutator scalar

For a projective family ρ with lifts ρ̃, the relation loop retains

    ρ̃(g) ρ̃(h) ρ̃(g)⁻¹ ρ̃(h)⁻¹  =  β(g,h) · I,

the antisymmetrization of the multiplier and the complete invariant of
[ω] ∈ H²(ℤ², U(1)) ([W2] §12).

**The mandatory anchors are cleared.** β is a scalar and separates all N
classes at every N = 2..6, with β = ζ_N^{−k}, k = 0..N−1 (G2.2); at
N = 6 these are exactly the six values W2's cap-free 36×36 B4x collapse
gate carries (G2.3).

**β is an invariant of ρ, not of a choice.** It is lift-independent —
scalars cancel in a group commutator — gated against every pair of roots
of unity of the carrier field at N = 2..6 (G2.4); and it is invariant
under configuration-basis rephasing, since the commutator conjugates and
a scalar is central (G2.5).

### 11. W2's successor target, met at family level

W2's corrected handover (LOG #16, §20) asks for **a phase-retaining
invariant of ρ finer than its Born shadow B∘ρ**. β is one:

> B∘ρ is **identical** across all N classes at every N = 2..6 — this is
> W2's collapse, B(Z^k) = I — while β takes **N distinct values**.
> (G2.6)

β also carries a structural consequence the Born shadow cannot state:
ord β = N/gcd(N,k) at every N = 2..6 (G2.6), and by [SvN] an irreducible
realization at a primitive q-th root multiplier has dimension exactly q.
Cited, not proven here.

Consistency with W7-0 is gated: β is **not** a full-Schur invariant —
the full Schur gauge does not even map a group element to a group
element — so β's invariance is a statement about the *reduced* gauge,
which is what W7-0 licensed (G2.7).

---

## W7-3 — COMPOSITIONAL CLOSURE

### 12. The no-descent fact

The gauge orbits of U₂ and U₁ *separately* do not determine the orbit of
U₂U₁. U₂ ↦ U₂D is a boundary gauge on U₂ alone and leaves its isolated
orbit data unchanged, but moves the composite. Gated by building the
switching between U₂ and U₂D and then measuring the composite: **192 of
576** stride pairs have U₂, U₂D in the same boundary orbit while
B(U₂DU₁) ≠ B(U₂U₁) (G3.0) — the same count [W2] A2(vi) reports for the
uncompensated insertion, reached independently.

**A shared-boundary phase frame is therefore required.**

### 13. The cut-coherence tensor and its seven gates

    w_k^{ij}        =  (U₂)_{ik} (U₁)_{kj}
    𝒞^{ij}_{kℓ}     =  w_k^{ij} · conj(w_ℓ^{ij})

| gate | statement | receipt |
|---|---|---|
| G3.1 | compensated-cut invariance | w itself is invariant; 256 stride pairs × 4 cut diagonals |
| G3.2 | outer boundary rephasings cancel | w_k ↦ d_i e_j w_k, so 𝒞 ↦ \|d_i e_j\|²𝒞 |
| G3.3 | projective scalars of both factors cancel | moduli 1 |
| G3.4 | diagonal = classical path weights | 𝒞^{ij}_{kk} = B(U₂)_{ik}B(U₁)_{kj} |
| G3.5 | rank-one PSD, 𝒞^{ij} = w(w)† | hermiticity entrywise **and every 2×2 minor identically zero**, with a non-negative diagonal by G3.4 — no order comparison used |
| G3.6 | **readout** Δᴮ_ij = 2Σ_{k<ℓ} Re 𝒞^{ij}_{kℓ} | 256 stride pairs, against the committed definition [B1] |
| G3.7 | 𝒞 does **not** detect monomial Weyl multipliers | exactly one live path per endpoint pair, every X_N, Z_N^k, N = 2..6 |

G3.6 is a **gate, not the theorem** — it is [B1]'s cross-term sum
rewritten. G3.7 is the fact that forces W7-2's relation loops to be part
of the signature at all.

### 14. THE PAIR-ORBIT THEOREM

**Theorem.** The declared gauge on a composable pair — outer boundary,
compensated cut, scalar — acts **exactly as vertex switching on the
tripartite path graph**

    Γ(U₂,U₁):  vertices R ⊔ K ⊔ C,
       an edge (i,k) valued (U₂)_{ik} for each nonzero entry of U₂,
       an edge (k,j) valued (U₁)_{kj} for each nonzero entry of U₁.

Γ is bipartite with parts K and R ⊔ C — every edge has exactly one
endpoint in K — so all its cycles are even. The switching at an
R-vertex is the outer output rephasing, at a C-vertex the outer input
rephasing, and **at a K-vertex it is exactly the compensated cut**:
conj(d_k) on U₂ and d_k on U₁. Hence, at fixed moduli, a complete set of
invariants of the pair is a cycle basis of Γ, of size

    μ(Γ)  =  |E| − |V| + c.

Gated over 2,304 switchings: the Γ-holonomies are invariant, and the
composite transforms by the outer boundary alone, the K-switching
cancelling in U₂U₁ (G3.8).

**The seam torsor is the K-vertex switching.** That is the pin's
shared-boundary phase frame, identified.

### 15. What 𝒞 sees, exactly

arg 𝒞^{ij}_{kℓ} = arg w_k^{ij} − arg w_ℓ^{ij} is the holonomy of the
**seam 4-cycle** i–k–j–ℓ–i in Γ. Matched entry by entry on 144 seam
4-cycles (G3.9). So the pinned signature decomposes cleanly:

- W7-1's factor cycle holonomies = the **pure-U₂ and pure-U₁ 4-cycles**;
- 𝒞 = the **seam 4-cycles**;

and **the pinned signature spans exactly the 4-cycle sublattice L₄ of
the cycle lattice Z(Γ).** Everything now turns on whether L₄ = Z(Γ).

### 16. Completeness at full support

**Theorem.** If every path amplitude w_k^{ij} is nonzero, 𝒞 is a
**complete** invariant of the pair up to the declared gauge, and a
fortiori determines the composite's boundary orbit.

*Proof.* 𝒞^{ij} = w^{ij}(w^{ij})† determines w^{ij} up to one phase
φ_ij. Suppose 𝒞(U₂′,U₁′) = 𝒞(U₂,U₁). The diagonal forces |w′| = |w|
entrywise; the off-diagonal forces w′_k/w_k independent of k, = φ_ij.
Writing a_ik = (U₂′)_{ik}/(U₂)_{ik} and b_kj = (U₁′)_{kj}/(U₁)_{kj} we
get a_ik b_kj = φ_ij for all k — **the same functional equation as
W7-0 §3** — hence a_ik = α_i/c_k and b_kj = c_k β_j. So
(U₂′,U₁′) = (D_α U₂ D_c⁻¹, D_c U₁ D_β): outer boundary plus compensated
cut, exactly the declared gauge. ∎

The lattice reading is the same statement: at full support Γ contains
the complete bipartite structure and L₄ = Z(Γ). Gated on **4,096**
full-support ordered pairs of the committed 2×2 family, the 4-cycle
sublattice having full cycle rank with all elementary divisors 1
(G3.10).

### 17. The exhaustive support-class sweep

A support pattern carries a unitary only if any two rows — and any two
columns — have supports that are **disjoint or overlap in at least two
places**; an overlap of exactly one would make the inner product a
single nonzero term. That necessary condition is the declared scope, and
it is a *superset* of the realizable patterns, so a clean sweep on it is
a clean sweep on them. At n = 3 it returns exactly **25** patterns,
independently matching W3′'s committed count of unitary-realizable
supports. Relabelling R and C are graph isomorphisms of Γ, so S₂ is
reduced modulo row-and-column permutations and S₁ modulo column
permutations; that reduction is exhaustive.

| n | admissible patterns | Γ classes | max μ | 4-cycle failures |
|---|---|---|---|---|
| 2 | 3 | 2 × 2 = 4 | 3 | **0** |
| 3 | 25 | 4 × 8 = 32 | 10 | **0** |
| 4 | 783 | 16 × 79 = 1,264 | 21 | **7** |

(G3.11.) At n = 2 and n = 3 the 4-cycles generate and the pinned
signature is complete. **At n = 4 seven Γ-classes have a 4-cycle
sublattice of rank μ − 1**: a genuine long-cycle invariant that neither
the factor holonomies nor 𝒞 can see.

### 18. THE NO-GO, WITNESSED IN EXACT UNITARY ARITHMETIC

The gap is realized by block-structured 4×4 unitaries. Write

    U₂ = [ 0 A ; B 0 ]   (rows 01 → cols 23, rows 23 → cols 01),
    U₁ :  rows 02 → cols 23,  rows 13 → cols 01,

with A, B, C, D drawn from the declared 2×2 set
{H·diag(1, ζ₈^t) : t = 0..7} ∪ {I, X}. The witness triple is
U₂ = embed(H,H), U₂′ = embed(H, H·diag(1,ζ₈)), U₁ = embed(H,H).

- all three are unitary, and **neither factor is monomial** (G3.12);
- **every endpoint pair has exactly one live path** — the live-path
  table is all 1s. This is *total path degeneracy without monomial
  factors*, so [W2] A6's annihilator theorem does not cover it (G3.12);
- U₂ and U₂′ are in the **same** boundary orbit (the switching is built
  and verified entrywise);
- the two pairs have the **same** cut-coherence tensor 𝒞, block by
  block, entry by entry — 𝒞 is blind because there is one live path per
  endpoint pair;
- the relation-loop sector is **empty** here, so β contributes nothing;
- the composites have the **same moduli**: B(U₂U₁) = B(U₂′U₁), so the
  Born shadow cannot see it either;
- **and both pairs are Δᴮ-flat**: one live path per endpoint pair kills
  every cross term, so the entire Δᴮ-family is silent;
- **but the composites are in different gauge orbits.**
  H_{02;02}(U₂U₁) = 1/16 while H_{02;02}(U₂′U₁) = −ζ₈³/16; the ratio is
  **ζ₈⁷**, a primitive 8th root, and no switching exists between them.

> **The pinned signature (cycle holonomies + relation loops + 𝒞) is
> INCOMPLETE.** A composable pair of unitaries can carry a
> boundary-gauge phase invariant in its composite that the entire
> signature — and the entire Δᴮ-family — does not see.

### 19. The missing seam datum, named

𝒞 is the **(i,j)-block-diagonal restriction** of the full
**path-amplitude Gram form**

    𝒢_{(ijk),(i′j′k′)}  =  w_k^{ij} · conj(w_{k′}^{i′j′}),

a rank-one PSD form on the set of live paths. What 𝒞 discards is exactly
𝒢's **cross-block** entries — the coherences between different endpoint
pairs. Those are not individually gauge-invariant (they carry
d_i e_j conj(d_i′) conj(e_j′)), and their minimal invariant combination
is the quadruple

    𝒦^{(ii′;jj′)}_{kℓ;k′ℓ′}
      =  w_k^{ij} conj(w_ℓ^{i′j}) w_{k′}^{i′j′} conj(w_{ℓ′}^{ij′}),

whose gauge factors telescope around the 8-cycle
i–k–j–ℓ–i′–k′–j′–ℓ′–i of Γ. Summing 𝒦 over k, ℓ, k′, ℓ′ returns the
composite's own Haagerup invariant H_{ii′;jj′}.

- 𝒦 is boundary- and compensated-cut invariant: 256 checks, 64 declared
  switchings of Γ moving all three vertex classes simultaneously × 4
  index tuples (G3.13);
- 𝒦 **separates the witness that 𝒞 could not**, first at
  (i,i′,j,j′,k,ℓ,k′,ℓ′) = (0,2,0,2,3,1,0,2) (G3.13);
- and adjoining 𝒦's 8-cycles closes **all seven** n = 4 gaps:
  L₄ + 𝒦 = Z(Γ) on every Γ-class at n = 2, 3 and 4 — 4, 32 and 1,264
  classes, 0 remaining gaps (G3.13).

> **THE MAIN THEOREM — the no-go, with the missing seam datum named.**
> (cycle holonomies + relation loops + 𝒞) is complete for two-step
> composition up to the declared gauge **exactly when the 4-cycles of Γ
> generate its cycle lattice**. That holds unconditionally at full
> support (§16) and at every admissible support class for n = 2 and
> n = 3; it is **false at n = 4**, with an exact unitary witness. The
> missing datum is the **cross-block content of the path-amplitude Gram
> form 𝒢**, minimally carried by 𝒦; adjoining it restores completeness
> at the full declared scope.

---

## W7-4 — RECORD DESCENT

### 20. The two hypotheses, and what each one buys

W3′'s record structure is a label list: the record map is k ↦ part[k]
and the sectors are its fibres. Its two hypotheses are pure **support**
conditions:

- **(H-avail)** for every i, the row support of U₂ lies in **one**
  sector;
- **(H-corr)** for every j, k ↦ part[k] is **injective** on the column
  support of U₁.

**Theorem W7-4A.** (H-avail) *alone* ⟹ 𝒞 is **block-diagonal by record
sector**: 𝒞^{ij}_{kℓ} = 0 whenever r(k) ≠ r(ℓ).
*Proof.* If r(k) ≠ r(ℓ) then for every i at most one of (U₂)_{ik},
(U₂)_{iℓ} is nonzero, so w_k^{ij} conj(w_ℓ^{ij}) = 0. ∎

**Theorem W7-4B.** (H-avail) **and** (H-corr) ⟹ 𝒞 is **fully
diagonal**, hence Δᴮ = 0 by the readout identity.
*Proof.* Block-diagonality by W7-4A; within a sector (H-corr) leaves at
most one live k per column j, so the surviving off-diagonal entries are
empty too. ∎

This recovers W3′'s Theorem 1 (LOG #14) as a corollary — anchored, not
re-proved — and it **separates the two hypotheses' roles**: (H-avail)
buys the *block structure*, (H-corr) buys the *collapse inside a block*.

Gated over 8 declared dim-4 operators × the 15 partitions of 4
configurations: **336** triples satisfy (H-avail) and all 336 give a
block-diagonal 𝒞, 0 violations (G4.1); **190** satisfy both hypotheses
and 𝒞 is fully diagonal in all 190, 0 violations, with 0 counterexamples
to Δᴮ = 0 there (G4.2).

### 21. Not phase triviality

Within an **unresolved** sector the off-diagonal entries of 𝒞 survive:
block-diagonalization is a statement about *cross-sector* coherence
only. At the declared coarse structure [0,0,1,1], 𝒞 is block-diagonal —
no cross-sector entry — yet carries **16 nonzero off-diagonal entries
inside the blocks**, and Δᴮ ≠ 0 there (G4.3). This is exactly what
T3′'s v2.2 gloss and W3′'s A2 require, and it is what the pin forbids
overstating.

### 22. The eraser control

W3′'s own dim-4 control: the same record-writing first leg
U₁ = CNOT·(H⊗I) and the same declared structure [0,1,0,1]; only the
later operation changes. The preserving leg is H⊗I; the eraser is
(H⊗I)·CNOT, which still **makes** the record — (H-corr) holds — but
destroys its availability.

- preserving leg: 𝒞 is block-diagonal *and* fully diagonal, 0
  cross-sector and 0 off-diagonal entries (G4.4);
- **eraser: 16 nonzero cross-sector entries of 𝒞 return** — coherent
  recombination puts back exactly what the record removed (G4.4);
- and the defect returns with them, D₂₁₀ maximally, entries 0 and ±½,
  reproducing W3′'s Part E (G4.4);
- the cause is exactly W7-4A's hypothesis: (H-avail) fails while
  (H-corr) still holds (G4.4).

### 23. The undefined-phase bookkeeping, and the limit of the descent

A zero entry of 𝒞 has two quite different causes: the record forbids the
pair (W7-4A), or an amplitude simply vanishes. The distinction is
decidable by W3′'s O(n²) criterion, and the measurement is a
**substantive negative**, reported as one:

> On the committed **unitary** families a fully diagonal 𝒞 *always*
> carries a record. 50 of 64 declared dim-4 pairs and 10,000 of 10,000
> block-4 pairs have a fully diagonal 𝒞, and in **0** of either does
> W3′'s criterion fail to find a record structure (G4.5). This agrees
> with W3′'s own sharpness result — 318 of 318 on unitary-realizable
> supports at n = 3 — and disagrees with the abstract support count of
> 5,490 of 94,746. **Unitarity is doing the work.**

And then the limit, which is the sharpest form of the pin's warning:

> **THE LIMIT OF RECORD DESCENT.** The §18 witness *carries* a record
> structure — merge classes [0,0,2,2], W3′'s criterion returns True —
> and its 𝒞 is **fully diagonal**, so the record account is complete at
> the level of 𝒞. Yet its composite still carries a boundary-gauge phase
> invariant that 𝒞 cannot see. **Block-diagonalization of 𝒞 under
> records is not phase triviality of the composite** (G4.5).

---

## W7-5 — ONTOLOGICAL ADJUDICATION

### 24. The pre-registered outcomes

| outcome | verdict |
|---|---|
| **W7-PHASE-REFERENT** | **OBTAINS, SCOPED.** A gauge-invariant phase-retaining compositional signature exists and is exhibited: cycle holonomies (W7-1), relation-loop phases β (W7-2), the cut-coherence tensor 𝒞 and the cross-block datum 𝒦 (W7-3). It is complete only once 𝒦 is adjoined; the pinned triple alone is not. |
| **W7-SINGLE-ARROW-INSUFFICIENT** | **OBTAINS.** On monomial supports μ = 0 and the single-arrow sector is empty, while β separates all N Weyl classes at N = 2..6. Family/relation loops are necessary. |
| **W7-SEAM-TORSOR-REQUIRED** | **OBTAINS.** Isolated factor orbits carry no composition law (§12). The seam datum is named and it is **two-layered**: 𝒞 (the seam 4-cycles) plus 𝒦 (the cross-block 8-cycles). The declared gauge is vertex switching on Γ, and the seam torsor is the K-vertex switching. |
| **W7-FULL-SCHUR-ANNIHILATION** | **does not obtain.** The reduction is *derived* (§3, §4), not postulated. Verdict G-REDUCED. |
| **W7-NO-RECORD-BRIDGE** | **does not obtain.** W7-4A/4B descend the signature under W3′'s hypotheses, with the eraser control restoring the off-diagonal blocks. |
| **W7-BARGMANN-INSUFFICIENT** | **does not obtain** for the declared loop family as a whole — β clears the W2 collapse anchors. It **does** obtain for the single-arrow Bargmann/Haagerup layer taken alone, which is the previous outcome. |

### 25. O2's four earning conditions

1. **PRECISE REFERENT — HOLDS.** Defined from committed primitives only:
   the boundary gauge is derived, the invariants are cycle holonomies of
   a graph built from the committed matrices, and every object is
   exhibited in exact arithmetic.
2. **COMPOSES — HOLDS, with a named seam datum and a scope.** Isolated
   orbits do not compose (§12). With the seam datum they do: proved
   unconditionally at full support (§16), gated at every admissible
   support class at n = 2, 3 for the pinned triple, and **false at n = 4
   for the pinned triple** (§17, §18) until 𝒦 is adjoined (§19). *This
   condition is met by the completed signature, not by the pinned one.*
3. **CONTROLS A COMMITTED PHENOMENON — HOLDS.** 𝒞's readout identity
   *is* Δᴮ, the programme's committed interference invariant. Scoped
   honestly: the control runs one way. §18 exhibits a Δᴮ-**flat** pair
   whose composite still carries a phase, so the signature is strictly
   finer than the phenomenon it controls.
4. **RECORD DESCENT — HOLDS.** W7-4A/4B, with the two hypotheses' roles
   separated, the coarse-record control showing phases survive inside a
   sector, and the eraser restoring the off-diagonal blocks — bounded by
   §23's limit.

### 26. W2's successor target

**Met, at two levels and by two objects.** β at family level (B∘ρ is
identical across all N classes while β separates them) and the
Γ-holonomies at arrow and pair level (B gives moduli only). Both are
invariants of the projective map, not of a lift — which is the direction
[W2] §20's correction insisted on.

### 27. What W7 does not deliver

1. **The pinned triple is not complete.** The no-go is this unit's main
   theorem, and n = 4 is where it bites.
2. **Completeness of the completed signature is gated at a declared
   finite scope** — all admissible support classes, n ≤ 4 — and proved
   unconditionally only at full support. The general-n statement is
   open. The natural conjecture, untested here, is that L₄ + 𝒦 = Z(Γ)
   for every unitary-admissible Γ.
3. **The record descent has a measured limit** (§23): a record can be
   present, 𝒞 fully diagonal, and the composite still phase-nontrivial.
4. **No ontological conclusion is drawn.** O2 gains a referent that
   meets its four conditions in the scoped forms above; whether that
   referent is *law* rather than surplus representation is not decided
   here, and W7 does not decide it.
5. **W7 is one-chart mathematics.** Cross-chart co-reference is W6's.

---

## 28. Antecedents

- **[GG]** Gain graphs / switching classes: phases on a cycle basis
  classify edge-phase assignments up to vertex switching, componentwise,
  with cycle rank |E| − |V| + c. See e.g. *On cospectrality of gain
  graphs*, DOI 10.1515/spma-2022-0169. **W7-1's classification statement
  is this theorem, cited not claimed.** W7's own contribution is the
  exact adaptation to the committed matrix families, to support changes,
  and to the composable-pair graph Γ of W7-3 — where the K-vertex
  switching is identified with the compensated cut gauge.
- **[MSS]** N. Mukunda et al., *Bargmann invariants and off-diagonal
  geometric phases for multi-level quantum systems*,
  arXiv:quant-ph/0107006. The ray/Gram setting: Bargmann triple products
  are invariants of a **one-index** ray gauge on a single Hilbert space.
  They are not invariants of the committed bipartite matrix gauge —
  gated both ways at G0.3–G0.4.
- **[B1]** Barandes, arXiv:2302.10778 — the identification of the
  Born-projection cross terms with interference. The readout identity is
  his cross-term sum, rewritten in the cut-coherence tensor; not
  originated here.
- **[B3]** Barandes, arXiv:2507.21192 — the Schur–Hadamard gauge, one
  U(1) per **ordered pair** of configurations (p.12 eqs. 29–30; p.27
  eq. 106), and unitarity as a "partial fixing of the gauge freedom"
  (p.19). Carried verbatim in W5's recast at I-13 and I-14. §4 supplies
  the exact residual stabilizer that phrase leaves open.
- **[W]** Weyl relations / noncommutative torus (e.g. arXiv:1606.01829).
  W7-2's mandatory anchors are W2's own realizations.
- **[SvN]** Stone–von Neumann, finite form. **Cited**, not proven here;
  used only for the dimension-quantization reading of β at §11.
- **[W1′]** `note-w1p-three-class.md` + `code/w1p_three_class_exact.py`,
  TERMINAL at LOG #7 — sliced and reused; its committed gate values are
  anchors.
- **[W2]** `note-w2-multiplier-ladder.md` +
  `code/w2_multiplier_ladder_exact.py`, TERMINAL at LOG #16 — the
  committed torus and compensated-cut gauges, the monomial annihilator,
  the B4x cap-free collapse with six distinct β, the B5 conjugation
  defects, the B7 ±14/625 odd-channel witness, and the successor target.
- **[W3′]** `note-w3p-records-kill-defect.md` +
  `code/w3p_records_exact.py`, TERMINAL at LOG #14 — the record model,
  the two support hypotheses, Theorem 1, the O(n²) decision procedure,
  and the dim-4 eraser control.
- **[REV3]** the external ontology/W7 review sequence, adjudicated at
  LOG #18–#19: the gauge-census correction, the cut-coherence tensor,
  and the two owned errors of the founding Bargmann sketch.

---

## 29. Scope

1. **No claim about nature.** Every result is a statement about declared
   matrix families, a declared gauge group, and declared finite scopes.
2. **The gauge reduction is scoped to composable unitary systems.** For
   an isolated non-unitary arrow the full Schur gauge stands and no
   phase invariant exists (§2, §5).
3. **§17's sweep runs over a NECESSARY condition for unitary
   realizability**, not over realizable patterns themselves. It is a
   superset, so the clean n ≤ 3 result transfers; the n = 4 failure is
   separately witnessed by exact unitaries (§18), so it does not depend
   on the superset.
4. **§16's completeness theorem is a hand proof** with gated
   ingredients; the quantifier over pairs is carried by the functional
   equation, and the sweeps corroborate it on committed families.
5. **§19's completion is gated, not proved.** L₄ + 𝒦 = Z(Γ) is verified
   at every Γ-class for n ≤ 4; no general-n proof is offered.
6. **§20–§23 are statements about 𝒞 under W3′'s hypotheses**, which are
   sufficient and never necessary — W3′'s own engraving, carried.
   W3′'s theorem is anchored, not re-proved.
7. **Nothing here reopens W2b.** The Δᴮ-family still cannot see the
   projective class; what §11 exhibits is an invariant of ρ that is
   *not* a functional of the Δᴮ-family, which is exactly what [W2] §20
   asked a successor to supply.
8. Paper 0 v2.2 §6's non-claims stand unmodified.

## 30. What this unit hands over

- **W7-0 delivers** the gauge census with a **derived** reduction
  (G-REDUCED), two independent theorems for it, the exact residual
  stabilizer of unitarity fixing, and the correct typing of the Bargmann
  triple product — the founding sketch's error closed on both sides.
- **W7-1 delivers** the single-arrow orbit theorem with a *constructive*
  completeness proof, the support stratification, and the
  undefined-phase discipline.
- **W7-2 delivers** β: a phase-retaining invariant of ρ strictly finer
  than B∘ρ, clearing W2's collapse anchors at N = 2..6 — **W2's
  successor target, met at family level.**
- **W7-3 delivers** the pair-orbit theorem (the declared gauge *is*
  switching on Γ, and the seam torsor *is* the K-vertex switching), the
  exact identification of what 𝒞 sees, unconditional completeness at
  full support, and **the main theorem: the completeness no-go at n = 4
  with the missing seam datum named and its completion gated.**
- **W7-4 delivers** the record descent with the two W3′ hypotheses'
  roles separated — (H-avail) buys blocks, (H-corr) buys the collapse
  inside them — the eraser control, and the measured limit of the
  descent.
- **W6 receives** the scope engraving: everything above is one-chart.
  The co-reference bridge is untouched and remains W6's.
- **O2 receives** a referent meeting all four earning conditions in the
  scoped forms of §25, and the standing warning of §27: the pinned
  signature was incomplete, and it took a named repair to make it
  compose.
