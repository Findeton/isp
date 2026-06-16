# The record chiral-matter machinery and two chirality no-gos: a companion to the Standard-Model floor

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, companion to publishable Paper VI, version 2026-06-15.

## Abstract

The Standard-Model-floor paper (Paper VI) runs its exhaustive chiral-matter searches on a derived charge lattice, and at two points it leans on the lattice chiral-fermion machinery — the four-dimensional record index theorem grounding the anomaly rows, and the exhaustion theorem that no genuinely chiral content survives below stack size three. This companion records, in one place and at honest grade, the constructive machinery underneath those steps and the two impossibility results that bound the matter sector beyond them. **What is external.** The constructive engine is inherited, not new: it is the Neuberger overlap operator, the Hasenfratz–Laliena–Niedermayer / Lüscher lattice index theorem, the Ginsparg–Wilson relation, and the Nielsen–Ninomiya no-go that the overlap construction is built to evade — the same machinery Paper VI's anomaly grounding already cites. Wen's projective symmetry group (PSG) and his anomaly-free-gated "mass without mass term" mirror-gapping are likewise external. We claim no priority for any of these. **What is the program-internal contribution.** It is two *statements about the records*, not new mainstream theorems. First: the record orientation classes and their relabeling automorphisms assemble into a genuine, computable finite group, `K̂ ⋊ Aut(K)` (with `|Aut(K)| = 168 = |GL(3,2)|` on the three-spin ledger), but this is the *split* PSG-ingredient group only — Wen's distinguishing content lives in `H²(SG, IGG)` over a *space group* `SG`, which needs emergent geometry, so there is **no Wen-PSG without an emergent space group**. Second: the ledger layer is **handedness-blind** — every record object is a function of the orientation alone, and parity acts jointly on `(orientation, Weyl-handedness)` under a parity-invariant gap, so a map from orientation to handedness would have to be parity-odd on parity-symmetric data — hence there is **no record-forced chirality bridge**. Both sharpen Paper VI's open matter-sector items (the global-to-local gauge promotion, the seam-existence inputs, the chiral content) into proved impossibilities at stated scope. No mass and no mass ratio is predicted; none is claimed.

## 1. What is inherited and what is the contribution

Paper VI is explicit that its chiral-matter steps stand on imported machinery. Its anomaly rows are grounded by a four-dimensional record index theorem whose mathematical foundation is "the Hasenfratz–Laliena–Niedermayer / Lüscher index theory," using "overlap fermions" (Neuberger); its floor search invokes "the program's exhaustion theorem (no genuinely chiral record content below stack size three)." This companion makes the surrounding machinery and its limits explicit, and the honesty mandate of the program requires stating up front which parts are known.

**External (inherited; no priority claimed).**

- The **exact lattice chiral operator** is the Neuberger overlap operator satisfying the **Ginsparg–Wilson relation**; that such an operator exists at all is the standard evasion of the **Nielsen–Ninomiya** doubling no-go.
- The **lattice index theorem** — that the overlap index equals the topological charge, exactly and sector by sector — is **Hasenfratz–Laliena–Niedermayer / Lüscher** index theory. Paper VI already uses precisely this (its Theorem 4.1, "overlap index `= c²f₁f₂`, exact in all sectors").
- **Anomaly cancellation as a content filter** is the standard chiral-gauge consistency condition; its use to gate chiral matter is classical (the same Geng–Marshak / Babu–Mohapatra lineage Paper VI cites for hypercharge).
- **Wen's projective symmetry group** (the extension `1 → IGG → PSG → SG → 1`, content in `H²(SG, IGG)`) and his **anomaly-free-gated mirror-gapping** ("mass without mass term") are external and, in his own statement, the gapping is unproven in general.

The strip test on this companion is therefore passed plainly: remove the program framing and the Ginsparg–Wilson / index / anomaly machinery is wholly inherited, exactly as it is already inherited inside Paper VI. There is no standalone novelty in the constructive engine.

**Program-internal contribution (a statement *about the records*, not a mainstream theorem).** Two no-gos and one positioning:

1. **A positioning.** The record orientation classes assemble into a real, computable finite group — the PSG *ingredients* — but provably not Wen's PSG (§4).
2. **No-go I.** No Wen-PSG without an emergent space group: the record group is split, and the cohomological content needs geometry that is behind the program's scale wall (§4).
3. **No-go II.** No record-forced chirality bridge: the ledger is handedness-blind, and a bridge would be parity-odd on parity-symmetric data (§5).

Each is a boundary statement on what the records can and cannot supply. None is a new theorem of lattice gauge theory or of Wen's framework. They convert Paper VI's *open* matter-sector residues into *proved* impossibilities at named scope, which is the contribution and the whole of it.

## 2. The inherited constructive pieces, as the records instantiate them

The records carry the three pieces the "it-from-qubit" string-net / PSG template assumes but does not itself build, and they carry them as instances of the inherited machinery above (the record-Ginsparg–Wilson operator, index theorem, and anomaly filter are the corpus results of v6 papers 9 and 14, reproduced here for context, not recomputed by this note's receipts):

1. **An exact record Ginsparg–Wilson operator.** The record Dirac operator satisfies the Ginsparg–Wilson identity to residual `4.0 × 10⁻¹⁵`, is covariant to `1.1 × 10⁻¹⁵`, and is exponentially local (decay `0.97` per unit), carrying a *single* species — one Brillouin-zone zero against the doubler's four. This is the Neuberger overlap construction realized on the record lattice; the Nielsen–Ninomiya no-go is evaded exactly as that construction is designed to evade it, not by hand.
2. **A lattice index theorem that holds.** `index(D) = Q` exactly in 14 of 14 flux sectors, with the vanishing theorem and integer quantization holding even on rough sectors carrying no continuum gauge field. This is the Hasenfratz–Laliena–Niedermayer / Lüscher index on record data — the same statement Paper VI grounds its anomaly rows with.
3. **Anomaly cancellation as a proved filter.** No chiral content survives below stack size three; the minimal anomaly-free chiral stack is `{1, 4, 4 | 2, 2, 5}`, with the index machine-exact. This is the standard anomaly gate, instantiated and lattice-grounded — it is exactly the exhaustion premise Paper VI invokes.

These are owned results reorganized against the external template, and on the chiral-fermion problem the records are *not behind* the field: the field's own fix (mirror-gapping) is unproven, and the records carry a doubling-free operator. But the engine is inherited; the legitimate claim is instantiation, not invention.

## 3. The gap mechanism, stated for scope (no mass)

On this base the matter sector has a literal gap mechanism — mass is the record gap left when protection breaks — recorded here only to fix the scope of the no-gos, since it predicts *no mass ratio*. The unoriented (vector-like, unprotected) branch is gapped at a single constant,

`W = η·θ − log cosh η = 0.156109200157240`,

with `η` the seal root (`e⁻η = tanh η`) and `θ = tanh η` the root of `θ³ + θ² + θ − 1 = 0`; `W` is simultaneously the spectral gap, the lightest record gap, and the price of a record event (receipt `v7_m1_psg_gap_chiral_receipt`, the three roles equal to better than `10⁻⁴⁰`). The oriented (chiral, protected) branch has its minimum gap *below* `W`, descending toward gapless: `0.133531` at `n = 3` and `0.064539` at `n = 4` (exact), at least as fast as `2⁻ⁿ` (receipt `v7_m1_psg_gap_chiral_receipt`, which anchors `W`, its three coincident roles, and the oriented descent; the closed form `m̂_min(n) = −ln(1 − 2⁻ⁿ) − δ_n` and its global-optimality lemma are receipted separately in `p9a_chiral_gap_closed.py` / `global_frustration_optimum.py`, and are not reproved here).

This is a *form-only* mechanism. It fixes the shape — vector-like gapped at `W`, chiral asymptotically gapless — but not a single physical magnitude, because computing a mass *ratio* requires selecting which mode is the electron and which the proton, and the seal modes are gauge-inequivalent superselection sectors differing by an invariant ledger rank (`1 / 3 / 7` orthogonal primitive characters; per-mode coefficients `0.609 / 0.495 / 0.368`, monotone as coupling dilutes), with no record-internal map identifying them (receipt `m2_mode_canonicalization`, 10 checks at `dps = 100`: the dilution ladder pushes *away* from any candidate mode, the external mass-gap-length identity `1/η = 1.6410` is the seal equation rewritten and selects nothing, and the variational routes point in opposite directions). The mode-selection escape — a constructed matter Hamiltonian whose energetics pick one rank — does not close the wall; it relocates the free choice to a matter sector that does not yet exist. No mass prediction is licensed, and none is made here.

## 4. No Wen-PSG without an emergent space group [NO-GO I]

The record orientation classes are the character group `K̂ = Hom(K, ℤ₂)` of the relation code `K`; the candidate symmetry group is `Aut(K)`, the position-permutations preserving `K`; the candidate gauge redundancy is the spin-flip group. These assemble into the semidirect product `K̂ ⋊ Aut(K)`, and receipt `p9b` verifies that `Aut(K)` acts on `K̂` by a well-defined permutation representation across the five smallest ledgers. The signature is exact: for the full three-spin ledger, `|Aut(K)| = 168 = |GL(3,2)| = (2³−1)(2³−2)(2³−4)`, reproducing the `GL(3,2)` orientation symmetry and its `1 + 7 + 7 + 1` orientation-class multiplet (receipt `p9b`). This is a genuine, computable Tier-1 object built from the relation code alone.

But it is the PSG-**ingredient** group, not Wen's PSG. Wen's distinguishing content — the data separating distinct quantum orders — is the extension class in `H²(SG, IGG)`, with `SG` a **space group** (lattice translations and point group). The record group lacks exactly that source (receipt `p9b`):

- `Aut(K)` is a **finite permutation group** — no translations, no lattice momentum, no projective spatial phases;
- the orientation data is strictly `ℤ₂`-valued (character signs) and `Aut(K)` acts by honest permutations, so no `U(1)`-valued 2-cocycle can arise from `K` alone, and the assembled `K̂ ⋊ Aut(K)` is **split by construction**. A nontrivial projective phase would need a continuous gauge on a *spatial* lattice, which is absent.

A nontrivial projective PSG needs a genuine 2-cocycle, which needs the space group `SG`, which needs **emergent geometry** — and the program's absolute geometric structure is behind the scale (`l_step`) wall. So the functor delivers the PSG ingredients — an `IGG`-like gauge, an `SG`-like relabeling group, the projective-protection phenomenology — but **not Wen's group**: its cohomological content is gated on emergent spacetime. The PSG-protection map can only ever be used phenomenologically, as far as the records reach. This is a statement about the records (their orientation data is `ℤ₂` and geometry-free), not a new theorem of Wen's framework — which is exactly why it is the program-internal contribution.

## 5. No record-forced chirality bridge [NO-GO II]

Paper VI takes the *existence* of chiral fermionic carriers (the Q-type `(3,2)` and L-type `(1,2)` seals) as its single largest empirical input. A natural hope is that the records nonetheless *force the handedness* — that Weyl chirality is a record-internal function of the orientation class. It is not, and receipt `p9c` makes the obstruction structural and proved.

**Two layers.** The orientation class `σ : K → ℤ₂` is a character of the relation code — the ledger / Ising layer, `dim K` bits. The Weyl handedness `m` is an `SO(3)`-representation label on the rotation/dilation *fiber* (the belt-trick double cover) — one bit. A bridge would be a record-internal map `K̂ → {+, −}` forcing that single fiber bit from the `dim K` ledger bits.

**Handedness-blindness.** The ledger layer carries no such bit. The gap `m̂`, the code `K`, the orientation group `K̂ ⋊ Aut(K)`, and every ledger quantity are functions of `σ` *alone* — the handedness `m` never enters their computation (receipt `p9c`: the chiral-minimum gap is recomputed from the orientation signs with no handedness argument anywhere). Flipping a putative handedness label changes nothing in the ledger; the records are blind to the very bit a bridge must output.

**Parity-odd on parity-symmetric data.** Parity is a *joint* symmetry, `P : (σ, m) ↦ (σ̄, −m)`, and the gap is parity-invariant — receipt `p9c` confirms `m̂(σ) = m̂(σ̄)` for the minimizer and its spin-flip partner (automatic: `σ̄` realizes the measure-preserving spin-flip `s → −s`, under which the divergence is invariant). A bridge `f : σ ↦ m` would therefore have to be parity-*odd*, `f(σ̄) = −f(σ)`, on data the records leave parity-*symmetric*. Nothing record-internal singles out one member of the pair `{σ, σ̄}` as "left," so `f` is undetermined; choosing it *is* an external coupling input. Consistently, self-mirror (achiral) orientations carry no handedness, matching the vanishing Weyl seed for achiral ledgers, and the handedness magnitude is itself coupling-dependent. So the ledger-chirality ↔ Weyl-chirality bridge is **not record-forced** — a proved no-go on the executed machinery, upgrading Paper VI's "the carriers' handedness is an empirical input" from a flagged residue to an impossibility.

## 6. Position relative to Paper VI

Paper VI's matter-sector residues are named inputs: the global-to-local gauge promotion, the seam-existence premises (including the carriers' chirality), and the minimality principle. This companion does not remove any of those inputs — it proves *why two of them cannot be supplied by the records*, sharpening them from "named input" to "proved impossibility at scope":

- The Paper VI gauge promotion (global commutant → local gauge symmetry with connection) needs spatial structure the records do not carry; No-go I is the matter-sector face of the same wall — a Wen-style projective gauge order needs an emergent space group, which is geometry-gated.
- The Paper VI input "the carriers' chirality is empirical" is now No-go II: the records are handedness-blind, so the chirality could not have been an output even in principle. The seam-existence input is thereby positioned as ineliminable, not merely unproven.

Two routes that *looked* open in the matter sector are closed; the residue that remains is exactly the walled import (emergent geometry, a mode-selecting matter Hamiltonian, and the interacting Ginsparg–Wilson flow — where the field's own mirror-gapping is likewise unproven, so the records inherit the field's open wall rather than closing it). This is progress in the program's idiom: it removes two questions from the search by proving them unanswerable from records alone, leaving Paper VI's input list complete and now partly *necessary* rather than merely *assumed*. No mass and no mass ratio follows, and none is claimed.

## Reproducibility

All numeric claims regenerate from fixed-seed scripts in `v7/code/` (mpmath at `dps ≥ 90`, the mode no-go at `100`; finite-group-exact / exhaustive where the structure permits), bit-identically. The gap constant `W = η·θ − log cosh η = 0.156109200157240` with its three coincident roles to `< 10⁻⁴⁰`, and the oriented descent, are checked in `v7_m1_psg_gap_chiral_receipt.py`. The **inherited constructive-piece numbers** — Ginsparg–Wilson residual `4.0 × 10⁻¹⁵`, covariance `1.1 × 10⁻¹⁵`, locality `0.97`, `index(D) = Q` in 14/14 sectors, the minimal anomaly-free stack `{1,4,4|2,2,5}` — are the record-Ginsparg–Wilson / index / anomaly results of v6 papers 9 and 14 (themselves the Neuberger overlap, Hasenfratz–Laliena–Niedermayer / Lüscher index, and the standard anomaly filter), reproduced for context, not recomputed by this note. The mode-canonicalization wall (the dilution ladder `0.609 > 0.495 > 0.368`, the `1/η = 1.6410` tautology with symbolic residual `0`, the mode-covariant `ξ(h_*) = 1.2814`, the invariant ranks `[1, 3, 7]`) is checked in `m2_mode_canonicalization.py` (10/10). The orientation-class group counts and the `|Aut(K)| = 168 = |GL(3,2)|` signature, with the split-extension / no-cocycle facts behind No-go I, are checked in `p9b_psg_ingredient_functor.py`. The handedness-blindness facts behind No-go II — the gap as a pure function of the orientation, and the parity-invariance `m̂(σ) = m̂(σ̄)` — are checked in `p9c_chirality_bridge_nogo.py`. All four receipts exit cleanly.

## References

**Companion (this program).**
- *The Standard-Model floor* (publishable Paper VI, same author) — the chiral-matter searches on a derived charge lattice; the four-dimensional record index theorem grounding the anomaly rows (its Theorem 4.1); the chirality exhaustion premise; and the named matter-sector inputs (the global-to-local gauge promotion, the seam-existence premises, the carriers' empirical chirality) that the two no-gos here sharpen.
- *The record click-law, VIII / IX* (v7, same author) — the matter-sector synthesis and the mode-canonicalization wall (VIII); the orientation-class group, the no-Wen-PSG-without-geometry no-go, and the no-record-forced-chirality-bridge no-go (IX).

**External (inherited; no priority claimed).**
- H. Neuberger, *Exactly massless quarks on the lattice*, Phys. Lett. B **417** (1998) 141 — the overlap operator.
- P. H. Ginsparg, K. G. Wilson, *A remnant of chiral symmetry on the lattice*, Phys. Rev. D **25** (1982) 2649 — the Ginsparg–Wilson relation.
- H. B. Nielsen, M. Ninomiya, *Absence of neutrinos on a lattice*, Nucl. Phys. B **185** (1981) 20 — the chiral lattice doubling no-go that the overlap construction evades.
- P. Hasenfratz, V. Laliena, F. Niedermayer, *The index theorem in QCD with a finite cut-off*, Phys. Lett. B **427** (1998) 125; M. Lüscher, *Exact chiral symmetry, topological charge and related topics in lattice QCD*, Nucl. Phys. B Proc. Suppl. **83** (2000) 34 — the lattice index theorem.
- X.-G. Wen, *Quantum orders and symmetric spin liquids*, Phys. Rev. B **65** (2002) 165113; arXiv:cond-mat/0107071 — the projective symmetry group `1 → IGG → PSG → SG → 1`, content classified by `H²(SG, IGG)` with `SG` the space group.
- X.-G. Wen, *Classifying gauge anomalies through symmetry-protected trivial orders…*, Phys. Rev. D **88** (2013) 045013; arXiv:1305.1045 — the anomaly-free-gated mirror gapping ("mass without mass term").
- M. A. Levin, X.-G. Wen, *String-net condensation*, Phys. Rev. B **71** (2005) 045110; arXiv:cond-mat/0404617 — emergent gauge bosons and fermions.
