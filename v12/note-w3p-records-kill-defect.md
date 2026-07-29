# v12 W3′ — RECORDS KILL THE DEFECT: THE THEOREM AT FINITE DIMENSION,
# THE bc M-1 INSTANCE, THE GLOBAL COROLLARY SHAPE, THE SCOPED CONVERSE,
# AND THE ERASER CONTROL

**Status:** GREEN-UNREVIEWED, STRICT, 2026-07-28.
**Pin:** `note-w3p-records-kill-defect-pin.md` (frozen before this unit
began).
**Binding:** paper 0 v2.1 §1 T3′ (the record defined **independently**
of the defect: stable variable, mutually exclusive values, correlated
with the alternatives, available under the declared future dynamics;
claims only under record-**preserving** operations; no claim after
erasure) and T2′ (the three-defect distinction Δᴮ / D₂₁₀ / d_div), §4
W3′, §5 (non-claims); v12/LOG.md #1–#8; bc/LOG.md #4 (M-1);
v11/LOG.md #14, #21.
**Receipt:** `v12/code/w3p_records_exact.py` → `v12/code/w3p_output.txt`.
14 anchors, **103 gates, 103 pass, 0 fail**; runtime 7.5 s; rerun
byte-identical modulo timings.
**Verdict:** **W3′-PROVEN.**  The KILL condition is evaluated
explicitly and does **not** fire.

Arithmetic: `fractions.Fraction` for every rational; the cyclotomic
fields ℚ(ζ₁₆) and ℚ(ζ₁₂) (canonical representation modulo Φ_N, so tuple
equality *is* field equality) for every algebraic quantity — the Bell
model's cos(π/8) and sin(π/8) live in ℚ(ζ₁₆); the real quadratic field
ℚ(√2) for the exact ranks.  No float in any substantive path; no
tolerance anywhere.  Substantive negatives exit 0; exit 1 is
anchor-only.

---

## 1. The record, defined first

Per v2.1 T3′, and **before any defect is computed anywhere in this
unit**: a *record* of the alternatives {C_r} at a cut is a variable R
whose values label mutually exclusive record sectors, perfectly or
approximately correlated with those alternatives, and available under
the declared future dynamics.

At finite dimension, in [B1]'s unistochastic form — configuration set
C, amplitude propagators U₁ (time 0 → cut) and U₂ (cut → time 2), the
declared laws

    Γ₁₀ = B(U₁),   Γ₂₁ = B(U₂),   Γ₂₀ = B(U₂U₁),   B(U) = |U|^∘2,

so that the **actual residual** of T2′ is D₂₁₀ = Γ₂₀ − Γ₂₁Γ₁₀ =
Δᴮ(U₂,U₁) — a record structure is a partition of C into sectors {C_r}
(equivalently an orthogonal resolution P_r = Σ_{k∈C_r}|k⟩⟨k|), and
T3′'s three clauses become three conditions **on supports**:

- **(H-orth)** the sectors are mutually exclusive.  Definitional.
- **(H-corr) PERFECT CORRELATION.**  For every initial configuration j,
  the *live* alternatives at the cut — the k with (U₁)_{kj} ≠ 0 — lie
  in pairwise **distinct** record sectors.  Reading R then says which
  alternative occurred.  This is what "perfectly correlated with those
  alternatives" means.
- **(H-avail) AVAILABILITY.**  For every later configuration i, all cut
  configurations k with (U₂)_{ik} ≠ 0 lie in **one** record sector.
  The record value is still recoverable from the later configuration.
  This is what "available under the declared future dynamics" and
  "record-**preserving** operations" mean.

Neither hypothesis mentions Δ, D₂₁₀, d_div or divisibility.  The
theorem is therefore falsifiable, and the pin's kill condition is a
real target.

## 2. The theorem

**Lemma (the cross-term identity, [B1]).**

    Δᴮ_ij = 2 Re Σ_{k<ℓ} (U₂)_ik (U₁)_kj · conj( (U₂)_iℓ (U₁)_ℓj ).

Gated entrywise on four declared pairs (A1), re-derived here
independently of [W1′].

**THEOREM 1 (records kill the defect).**  *Let a record structure at
the cut satisfy (H-corr) and (H-avail).  Then every summand of the
cross-term identity vanishes individually, hence*

    Δᴮ(U₂, U₁) = 0   and   D₂₁₀ = 0 on the cut algebra,

*with the **canonical** divisor Γ₂₁ = B(U₂).*

*Proof.*  Fix i, j and k < ℓ.  If the summand is nonzero then all four
factors are nonzero: (U₂)_{ik} ≠ 0, (U₂)_{iℓ} ≠ 0, (U₁)_{kj} ≠ 0,
(U₁)_{ℓj} ≠ 0.  From the first two and **(H-avail)**, k and ℓ lie in
the same record sector.  From the last two and **(H-corr)**, k and ℓ
lie in distinct sectors unless k = ℓ.  But k < ℓ.  Contradiction; the
summand is zero.  Summing, Δᴮ = 0. ∎

The proof is a *support* argument: it uses no property of the
amplitudes.  The receipt gates it **termwise** — every individual
cross-term is checked to vanish, not merely their sum (A3: 96 terms;
D0: 96 overlaps) — and then **exhaustively**, at n = 3, over *all*
2⁹ = 512 support patterns for U₁, all 512 for U₂ and all 5 set
partitions of the three configurations: 146 536 admissible triples,
zero violations (A5b).  Because both hypotheses are monotone under
shrinking a support, that check covers **every** pair of 3×3 matrices
with any amplitudes whatever: at n = 3 no counterexample exists at all.

**THEOREM 1′ (the reading route).**  *If the record is physically
**read** at the cut — the channel is U₂ ∘ D ∘ U₁ with the pinching
D(ρ) = Σ_r P_r ρ P_r — and the record sectors are the singletons, then
for **any** later dynamics whatever*

    shadow(U₂ ∘ D ∘ U₁) = B(U₂) B(U₁),   so D₂₁₀ = 0.

*Proof.*  D(U₁|j⟩⟨j|U₁†) = Σ_k |(U₁)_{kj}|² |k⟩⟨k|; conjugating by U₂
and reading the diagonal gives Σ_k |(U₂)_{ik}|² |(U₁)_{kj}|² =
(B(U₂)B(U₁))_{ij}. ∎

The two routes are genuinely different: Theorem 1 needs **no
decoherence at all** — the record keeps the branches apart by itself —
while Theorem 1′ needs no hypothesis on the future.  Both are gated
(A2, A3).  **The reading route also needs (H-corr):** reading a
*coarse*, non-separating record leaves the intra-sector coherences
alive and D₂₁₀ ≠ 0 — gated on the same data where the fine reading
gives D₂₁₀ = 0 (A2).

**THEOREM 2 (the channel form; the conditional-expectation argument
with every hypothesis named).**  *Let H be finite-dimensional, {ρ_j}
declared initial states, Φ₁ and Φ₂ CPTP maps, {P_r} an orthogonal
resolution at the cut, {F_i} a POVM at time 2.  Put*

    Γ₁₀(r|j) = Tr[P_r Φ₁(ρ_j)],     Γ₂₀(i|j) = Tr[F_i Φ₂(Φ₁(ρ_j))],
    σ_{r|j}  = P_r Φ₁(ρ_j) P_r / Γ₁₀(r|j)   (where Γ₁₀(r|j) > 0).

*Assume*

- **(R1) NO RECOHERENCE:** Tr[F_i Φ₂(X)] = Tr[F_i Φ₂(D(X))] for every
  X = Φ₁(ρ_j), with D the pinching onto {P_r};
- **(R2) SUFFICIENCY:** there are states σ_r with
  Tr[F_i Φ₂(σ_{r|j})] = Tr[F_i Φ₂(σ_r)] =: Γ₂₁(i|r) for every j with
  Γ₁₀(r|j) > 0.

*Then Γ₂₀ = Γ₂₁ Γ₁₀ exactly.*

*Proof.*  Γ₂₀(i|j) = Tr[F_i Φ₂Φ₁(ρ_j)] —(R1)— =
Tr[F_i Φ₂(Σ_r P_r Φ₁(ρ_j) P_r)] = Σ_r Γ₁₀(r|j) Tr[F_i Φ₂(σ_{r|j})]
—(R2)— = Σ_r Γ₂₁(i|r) Γ₁₀(r|j). ∎

(R1) holds when the reading is applied physically, and when Φ₂'s Kraus
operators are sector-graded and the F_i commute with the P_r — which is
(H-avail) at the support level.  (R2) holds when the sectors are rank
one — which is (H-corr)'s strongest form.  Theorem 1 and Theorem 2 are
not verbatim reductions of one another: Theorem 1 does not need (R2),
because under (H-avail) the *later* configuration already determines
the record value.  Both are the same one-line mechanism: **interference
between record sectors is unobservable, and inside a sector there is at
most one live alternative.**  Theorem 2 is proven here and gated only
through its instances — Theorem 1's gates, the reading route's gates,
and Theorem 3's family; there is no separate CPTP census in the
receipt, and that is a declared limit.

**THEOREM 3 (approximately correlated ⇒ approximately divisible).**
*Under (R1), with the declared divisor Γ̂₂₁(i|r) = Tr[F_i Φ₂(σ_r)],*

    Σ_i |D₂₁₀(i|j)|  ≤  Σ_r Γ₁₀(r|j) · ‖σ_{r|j} − σ_r‖₁.

*Proof.*  D₂₁₀(i|j) = Σ_r Γ₁₀(r|j) Tr[F_i Φ₂(σ_{r|j} − σ_r)]; for a
POVM, Σ_i |Tr[F_i X]| ≤ Σ_i Tr[F_i |X|] = ‖X‖₁, and Φ₂ is trace-norm
contractive. ∎

Gated on a declared exact rational family at six deviation values,
where the bound is not merely satisfied but **tight — equality at every
point** — and the exact record (deviation 0) gives D₂₁₀ = 0 (A8).

## 3. The worked examples

| example | route | receipt |
|---|---|---|
| H∘H over ℚ(ζ₁₆), F₃∘F₃ over ℚ(ζ₁₂), two steps, record read | 1′ | A2 |
| coarse (non-separating) reading vs fine reading, same data | 1′ | A2 |
| branch qubit + record qubit, dim 4, **no decoherence anywhere** | 1 | A3 |
| three steps, records read at both cuts (2×2 and 3×3) | 1′ | A4 |
| three steps, a **growing** record (r₁, then (r₁,r₂)), dim 8, no reading | 1 | A4 |
| four steps, records at three cuts, dim 16 | 1 | A4 |

The two-step read examples reproduce [W1′] §8's seed from scratch: the
D-interleaved shadow is exactly B(U₂)B(U₁), is a genuine stochastic
matrix, and the unread shadow differs.  The dim-4 example is the
unit's cleanest exhibit: U₁ = CNOT∘(H⊗I) writes the branch into the
record qubit, U₂ = H⊗I acts on the branch alone, **nothing is
decohered**, and B(U₂U₁) = B(U₂)B(U₁) exactly, column 0 being
(¼,¼,¼,¼).  Removing the CNOT — the only change — breaks (H-corr) and
the defect returns.

**The censuses.**  Hypotheses are evaluated first, the defect second.

- dim 4, record = qubit 1: 320 declared pairs, 252 satisfy both
  hypotheses, **all** with Δᴮ = 0; 8 pairs fail the hypotheses *and*
  have Δᴮ ≠ 0 (non-vacuity); 60 have Δᴮ = 0 without any record (the
  converse's first failure).
- dim 4, **over all 15 set partitions** of the configuration space:
  4 800 (partition, U₂, U₁) triples, 3 280 with both hypotheses, zero
  violations.
- dim 9 over ℚ(ζ₁₂), record = the second trit: 64 pairs, 42 with both
  hypotheses, zero violations.
- n = 3, **exhaustive over supports** as described in §2.

**The two known monomial sufficiency conditions are this theorem at its
two extreme record structures** — verified over all 512 supports at
n = 3 (A5c):

    (H-avail) at the FINEST record  ⟺  U₂ is row-monomial
    (H-corr)  at the TRIVIAL record ⟺  U₁ is column-monomial

with the other hypothesis automatic in each case.  [W1′] §5's
structural conditions are therefore the two endpoints of one
record-indexed family, and the **intermediate** structures are strictly
stronger than both: 8 dim-4 pairs satisfy neither monomial condition
yet carry a middle record structure that kills the defect.

## 4. Both hypotheses are load-bearing; the kill, evaluated

**(H-corr) dropped** (U₁ = U₂ = H⊗I, record = qubit 1): (H-avail) still
holds, (H-corr) fails, and the defect survives — Δᴮ₀₀ = 1/2 (A6).

**(H-avail) dropped, exhibit 1** (U₂ = (I⊗H)∘CNOT): (H-corr) still
holds, (H-avail) fails — **and Δᴮ = 0 anyway.**  This negative is
reported, not hidden: the hypotheses are **sufficient and never claimed
necessary**, and dropping one does not by itself restore the defect.
It is the same fact [W1′] §5 established — Δᴮ = 0 is a phase-alignment
condition, strictly weaker than any support condition.

**(H-avail) dropped, exhibit 2** (the eraser, §8): the defect returns,
maximally.

**THE KILL CONDITION**, verbatim from the pin — *a stable record with
surviving D₂₁₀ on its own algebra under record-preserving dynamics* —
is evaluated in-receipt over the dim-4 census (320 pairs at the
declared record structure, and the 4 800 (partition, U₂, U₁) triples of
A5's all-partitions sweep, any violation of which would be a kill), the
dim-9 census (64 pairs), the Bell model's 12 cells × 16 declared record
structures, and exhaustively over all 512 × 512 supports and all 5
partitions at n = 3.  **IT DOES NOT FIRE.**

The phrase *on its own algebra* is load-bearing, and the receipt tests
exactly that (A7).  A6's first instance has a stable, preserved record
and a surviving D₂₁₀ — but the residual lives on the **branch** algebra,
of which R is not a record.  On the record's own algebra all three legs
are strongly lumpable, the lumped law is the identity, and it divides
exactly.  **The honest content: T3′'s clause "perfectly correlated with
those alternatives" is not decoration — it is the hypothesis (H-corr),
and without it a stable, preserved record leaves D₂₁₀ alive on the
alternatives it fails to separate.**

## 5. The instance — bc #4's M-1 on the committed Bell model

The model of [BC2] is **rebuilt independently** from its committed
specification (git object `cbb7279`; the bc working tree is dirty with
frozen partial edits and is never read, and no bc code is imported).
Configuration space (qA, qB, pA, pB), |C| = 36, index
i = ((qA·2 + qB)·3 + pA)·3 + pB, j₀ = 0; U_prep carries j₀ to the
singlet; U_X(θ) = Σ_s Π^θ_s ⊗ Sh^{n(s)} with Sh the 3-cycle
r → + → − → r; frames F1 = (prep, A, B) and F2 = (prep, B, A);
division events {0, 2, 3}; second-leg operator U_B in F1 and U_A in F2
([B3] eq. 25, p. 29).

**Anchors (exit-1) — every committed constant reproduces:**

| committed object | value |
|---|---|
| operators real and exactly orthogonal | 7 operators, U^T U = I entrywise |
| [U_A(a), U_B(b)] = 0 | 9 operator pairs |
| U_prep's j₀ column | (0, 1/√2, −1/√2, 0) on (00,01,10,11) |
| the singlet outcome law, both frames | 96 exact identities, P(α,β) = (1 − αβ cos(a−b))/4, marginals 1/2 |
| Γ(3←2)Γ(2←0) vs Γ(3←0), differing entries | SP-A 0/0, SP-B 0/0, SP-C 576/576, SP-D 576/576, SP-E 0/0, SP-F 576/576 |
| exact ranks of Γ(2←0) (F1, F2) | (18,18), (18,18), (9,18), (9,18), (18,18), (18,18) — never 36 |
| the basis-free pointer certificate | Pr[pointer B still ready] at Alice's division event = 1 in F1 (t = 2), 0 in F2 (t = 3), all six setting pairs |

**M-1's biconditional, derived.**  In [B3]'s own terms the law of total
probability at a declared division event (eqs. 19–20) *is* D₂₁₀ = 0
with the canonical divisor, so *"legitimate division event ⟺ the
process divides at it"* is that definition made explicit.  W3′ supplies
the missing **why**.

The declared record family is all **16** structures that read a subset
of the four configuration coordinates, from the one-sector trivial
structure to the 36-sector finest one; it is declared before any defect
is computed.  Gated facts:

- **Bob's operator preserves Alice's record exactly:** [U_B(b), P^A_s]
  = 0 for every b and every pointer-A sector.
- **The theorem's direction holds with no false positive**, and on this
  model the **biconditional holds at all 12 (setting pair, frame)
  cells**: the cut divides ⟺ some declared record structure satisfies
  (H-corr) and (H-avail).

| setting pair | F1 | winning structures | F2 | winning structures |
|---|---|---|---|---|
| SP-A (0°,45°) | divides | {qA}, {pA}, {qA,pA} | divides | {qA,qB,pB}, finest |
| SP-B (0°,135°) | divides | {qA}, {pA}, {qA,pA} | divides | {qA,qB,pB}, finest |
| SP-C (90°,45°) | indivisible | — | indivisible | — |
| SP-D (90°,135°) | indivisible | — | indivisible | — |
| SP-E (0°,0°) | divides | 14 of the 16 | divides | 14 of the 16 |
| SP-F (45°,45°) | indivisible | — | indivisible | — |

**The mechanism, exact.**  In F1 at a = 0° Alice's measurement is a
configuration *permutation*, so the two singlet branches leave the cut
in **different pointer-A sectors**, and Bob — who never touches pointer
A — cannot bring them back to one configuration: (H-corr) and
(H-avail) both hold and the law divides.  At a = 45° or 90° the pointer
still records Alice's **outcome**, but two live alternatives share a
pointer sector: (H-corr) fails, the cross-terms survive, the law does
not divide.  In F2 at a = 0° the divisibility comes from the *finest*
record instead, because U_A(0°) is monomial — the same theorem at its
other endpoint (§3).

**The reading repairs every illegitimate cut.**  Recomputed through
ρ → pinch → conjugate at all 12 cells: the read model's law is exactly
Γ(3←2)Γ(2←0), so it satisfies the law of total probability at *every*
declared division event, and it differs from the unread model in
exactly 576 entries at exactly SP-C/D/F.  **A legitimate division event
is a record event**, and reading the record at an illegitimate cut
makes it legitimate.

**Scope.**  One direction is Theorem 1.  The other — *divides ⇒ a
record structure exists* — is **measured** on this model over the
declared 16-member family at 12 cells, not proven; §7 shows it is false
in general.

## 6. The global case

**COROLLARY (multi-cut).**  *Let U₁, …, U_{m+1} be the legs of a chain
and let each cut t carry a record structure π_t satisfying (H-corr) for
the composite prefix U_t ⋯ U₁ and (H-avail) for the next leg U_{t+1}.
Then*

    B(U_{m+1} ⋯ U₁) = B(U_{m+1}) ⋯ B(U₁),

*i.e. D vanishes at every cut simultaneously and the chain is
Chapman–Kolmogorov.*

*Proof.*  Apply Theorem 1 at the last cut with the pair
(U_{m+1}, U_m ⋯ U₁) to get B(U_{m+1} ⋯ U₁) = B(U_{m+1}) B(U_m ⋯ U₁),
then recurse on the shorter chain, whose hypotheses are the remaining
π_t's. ∎  Gated on exact 3-step and 4-step chains, both routes (A4).

**Total factuality** — every alternative recorded at every cut, nothing
erased — is this corollary's global shape: the finest record structure
in force at every cut and preserved forever.

**v11's measured status, cited only.  v11 is frozen; no v11 file is
read by this receipt and no v11 number is claimed here.**

- **[V11] LOG #14 (U1 TERMINAL):** at every division-event cut with a
  biting test the law **divides**; the fifteen indivisibility verdicts
  are at *non*-division cuts.  Caveat carried from that same entry: the
  renewal-grain divisible verdicts there are **degenerate**-divisible (a
  column-constant transfer), so they corroborate the corollary only
  weakly.
- **[V11] LOG #21 (U1b TERMINAL):** at the record grain no two-sided
  test exists in the reachable class — *"the record-grain question is
  not closed, it is UNASKED below depth 15"*.

So v11 corroborates the corollary where it can ask, and does not test
it where it cannot.

## 7. The converse, scoped

The implication ladder, with this unit's theorem at the top:

    records ((H-corr) ∧ (H-avail))
       ⇒ medium decoherence at the cut
       ⇒ Δᴮ = 0
       ⇒ D₂₁₀ = 0 with the canonical divisor
       ⇒ d_div = 0.

The top link is gated (D0: on the dim-4 record instance all 96 branch
overlaps vanish — the overlaps themselves, not merely their real
parts).  **None of the reverse implications holds**, and each failure
is receipted:

- **d_div = 0 ⇏ D₂₁₀ = 0.**  The C+1 rotation pair, rebuilt here from
  scratch: U₁ = R(θ₁) with (24/25, 7/25) and U₂ = R(θ₂) with (4/5,
  3/5); B(R(θ)) = S(cos 2θ), c₁ = 527/625, c₂ = 7/25, c_tot = −7/25;
  Δᴮ₀₀ = −4032/15625 ≠ 0 while K = S(−175/527) is a genuine stochastic
  matrix with K·B(U₁) = B(U₂U₁) exactly and K ≠ B(U₂).
- **D₂₁₀ = 0 ⇏ a record.**  At that same cut, **no** record structure
  exists: of the two partitions of a two-element configuration space,
  the finest fails (H-avail) because U₂ is not monomial and the trivial
  fails (H-corr) because both alternatives are live.  Divisibility does
  **not** imply a record.
- **Δᴮ = 0 ⇏ medium decoherence.**  A witness from the declared family,
  (U₂, U₁) = (H, S·H) with S = diag(1, i): Δᴮ = 0 while the branch
  overlaps are nonzero, and it carries no record structure either.
  Δᴮ = 0 there is **phase alignment**, and it is **unstable**: 7 of 7
  declared diagonal phase insertions break it, whereas the same 7 kicks
  leave the record-killed defect at exactly 0 — the record hypotheses
  are support conditions and phases cannot break them.  This is a sharp
  operational difference between the two ways of killing the defect.
- **The all-readouts converse is vacuous.**  Quantifying over every
  final rank-one readout, canonical divisibility at the cut is
  equivalent to M + M† = 0 with M = Σ_{k<ℓ}|c_k⟩⟨c_ℓ| and
  c_k = U₂Π_kU₁|j⟩; the exact operator identity

      M + M† = |C⟩⟨C| − Σ_k |c_k⟩⟨c_k|,     C = Σ_k c_k = U₂U₁|j⟩,

  is gated on four declared pairs.  Since the c_k are orthogonal, the
  right side vanishes iff at most one c_k is nonzero — iff column j of
  U₁ is **monomial**: no branching at all.  Gated in both directions on
  the declared readout family.  So the strong converse delivers records
  only vacuously.

**The true converse is [GMH]'s and is not ours:** for a *pure* initial
state, a set of histories medium-decoheres **iff** generalized records
exist (Gell-Mann and Hartle 1993).  It is cited as the known result it
is and never re-derived; it is what licenses the reading of D1's
nonzero overlaps as *"no generalized records exist for that history
set"*.  v12's contribution is the translation into Barandes division
events and the record-indexed support criterion, nothing more.

## 8. The eraser — the mandatory negative control

Same record, same initial configurations, same first leg
U₁ = CNOT∘(H⊗I).  **Only the later operation changes:**

    PRESERVING:  U₂  = H ⊗ I            (acts on the branch alone)
    ERASING:     U₂′ = (H ⊗ I) ∘ CNOT   (coherently undoes the record)

Gated, exactly:

- (H-corr) still holds — the record is still **made**; only its
  availability changes.  (H-avail) **fails**: a later configuration
  receives amplitude from both record sectors.
- The erased composite law is the **identity** — coherent erasure
  recovers the initial configuration exactly.
- **D₂₁₀ returns, maximally:** every entry is 0 or ±1/2.
- **d_div > 0 as well**, by an exact argument rather than a search:
  columns 0 and 2 of Γ₁₀ are equal, so K·Γ₁₀ has equal columns 0 and 2
  for *every* stochastic K, while Γ₂₀ = I does not; the ℓ¹ floor is
  exactly 2.
- On the very same data the preserving leg still has D₂₁₀ = 0.

**An eraser inside the Bell model**, with one reported negative first:
undoing only Alice's measurement — second leg U_B(45°)·U_A(0°)^T — is
**not** an eraser, because U_A(0°) is a configuration permutation and
un-permuting *relabels* the record rather than recombining it; three
record structures survive and the defect stays 0.  The genuine eraser
is the exact time-reverse of the first leg, second = Θ(2←0)^T: it
destroys **every** one of the 16 declared record structures, and the
defect returns at a cut that divided (72 differing entries).

T3′'s "no claim after record erasure" is therefore not a disclaimer
but a boundary with a measured location.

## 9. Antecedents

Every result used carries its citation in the receipt output at the
gate where it is used.

- **[B1]** Barandes, arXiv 2302.10778 — the Born projection
  Γ = |U|^∘2 and the identification of its composition failure with
  interference.  The cross-term identity is his; re-derived and gated
  at A1, used in every proof here.
- **[B3]** Barandes, arXiv 2507.21192 — division events (p. 29), the
  law of total probability (eqs. 19–20), Θ(t←0) (eq. 25).  Used
  throughout §5.
- **[GMH]** Gell-Mann and Hartle, Phys. Rev. D 47, 3345 (1993) — for a
  pure initial state, medium decoherence ⟺ generalized records.
  **Cited, never re-derived, never claimed as this unit's.**  Used at
  D0, D1.
- **[W1′]** v12/note-w1p-three-class.md, TERMINAL at v12 LOG #7 — the
  cross-term identity, the Δᴮ = 0 census (phase alignment, **not**
  support), the three-defect separation C+1, and the §8 record example
  that is this unit's declared seed.  Used at A5, A5c, D1, D2.
- **[BC2]** bc/note-bc2-bell-two-frames.md and
  bc/code/bc2_two_frames_exact.py at git object `cbb7279`, with
  bc/LOG.md #2 and #4.  The Bell model's specification and every
  anchored constant of §5.
- **[V11]** v11/LOG.md #14 and #21 — cited only; v11 is frozen and
  nothing of it is re-run.
- **[GAUSS]** Φ_n is irreducible over ℚ — standard; it is what makes
  the cyclotomic representation canonical, hence tuple equality = field
  equality with no tolerance.

## 10. Scope

1. **No claim about nature.**  Every result is a statement about
   declared finite-dimensional models.
2. **The record is defined independently of the defect** (T3′) and is
   declared before any defect is computed, at every instance here.
3. **The hypotheses are SUFFICIENT, never necessary.**  They are
   *support* conditions; [W1′] proved Δᴮ = 0 is a *phase-alignment*
   condition, strictly weaker.  Records are one way to kill the defect,
   not the only way — §7 exhibits the other way and shows it is
   unstable under phase kicks while the record route is not.
4. **Δᴮ, D₂₁₀ and d_div stay three different objects** (T2′).  Every
   divisibility statement here names its divisor; where the divisor is
   the canonical B(U₂) it says so.
5. **No claim after erasure or under sector-recombining operations.**
   §8 is that boundary, exhibited rather than assumed.
6. **The bc instance's biconditional** is proven in one direction and
   *measured* in the other, over a declared 16-member family of record
   structures at 12 cells.  It is not a general converse.  Nothing is
   claimed about d_div on that model: SP-C/D/F carry D₂₁₀ ≠ 0 with the
   declared divisor, and existential divisibility there is untested.
7. **Out of scope, named:** (a) infinite dimension and continuum
   limits; (b) approximate record sectors that are only *nearly*
   orthogonal — Theorem 3 treats approximate *correlation*, with exactly
   orthogonal sectors; (c) the decoherence-functional converse itself,
   which is [GMH]'s; (d) any claim that these hypotheses are necessary
   at any grain; (e) v11's own record-grain question, which its LOG #21
   says is unasked below depth 15.
8. Paper 0 v2.1 §5's non-claims stand unmodified.

## 11. Disclosures

- 3 of the 103 gates are **declarative** — they print a stated scope or
  re-assert an already-gated fact rather than computing something new
  (the multi-cut induction's re-assertion of A4; the v11-cited-not-run
  statement; the ℓ¹ floor computed by hand in §8).
- The Bell model is **rebuilt** from the committed specification; no bc
  code is imported and no bc working-tree file is read.
- The exact ranks are computed over ℚ(√2) after an exactness-checked
  conversion (gate B0), not over ℚ(ζ₁₆).
- The exhaustive support verification is at **n = 3 only**; at n = 4
  and above the verification is algebraic over declared families, not
  exhaustive.
- One negative found mid-construction and kept: A6's (H-avail)
  exhibit 1 has Δᴮ = 0 despite the hypothesis failing.  The exhibit was
  not replaced; a second exhibit (the eraser) was added beside it.

## 12. What this unit hands over

- **T3′ is a theorem**, at finite dimension, with both of T3′'s
  definitional clauses identified as the two hypotheses that do the
  work, and with the pin's kill condition evaluated and not fired.
  Paper 0's boxed T3′ can be restated with (H-corr) and (H-avail)
  named; its "perfectly or approximately correlated" clause is
  load-bearing and now carries an exact, tight quantitative bound.
- **W5** (Barandes recast) receives §5: on the committed Bell model a
  *legitimate division event is a record event*, and reading the record
  repairs every illegitimate cut.  [B3]'s "division events are
  generated during a measurement process" sharpens to: not the
  measurement — the **record**.
- **W4′** receives §7's ladder as a fixed relation table between the
  Δᴮ-family objects and the record structure, with all three reverse
  implications refuted by receipted counterexamples, and §3's
  observation that [W1′]'s two monomial sufficiency conditions are one
  record-indexed family.
- **W2a** receives nothing beyond the cross-term identity it already
  has.
- The eraser control marks the programme's boundary: every claim of
  this unit dies the moment a record is coherently recombined, and the
  receipt shows exactly how it dies.
