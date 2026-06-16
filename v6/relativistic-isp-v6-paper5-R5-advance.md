# R5 / Born reconstruction — Advance: the import is exactly one axiom (2026-06-14)

Addendum to Paper 5. The corpus audit found SHARD "derives p=2 *given* the Hilbert structure, which
it imports." This note sharpens that into a precise, minimal, named axiom and a classical theorem that
discharges it — reducing R5 from "is Born derived?" to a single decidable question about record dynamics.
Code: `code/` tightness check (in `/tmp/r5_born_tightness.py`, analytic).

## The residue
Paper 5 §3 derives the Born rule `P(i)=|a_i|^2/Σ|a_j|^2` (exponent **p=2**) from premises B1–B6, the
load-bearing ones being **B2** (alternatives add *linearly* before division) and **B3** (admissible
screen transports are *norm-preserving*), via weight-invariance under the equal-split isometry
`(1,0,…,0) ↦ n^{-1/2}(1,…,1)`. Paper 5 itself concedes (§5) this is "not yet a theorem that every
standard Hilbert-space measurement [follows]." R5 = are B2/B3 derived from the record primitive, or imported?

## 1. The import is localized exactly: p = q
The equal-split map `(1,0,…) ↦ n^{-1/q}(1,…,1)` is an `ℓ_q`-isometry, and weight-invariance of
`W_p = Σ|a_i|^p` under it forces **p = q** (verified to machine precision for q = 1, 1.3, 2, 3, 4: the
forced exponent equals q exactly). So **the derived Born exponent is identically the assumed
admissible-transport norm.** B3's "norm-preservation, with the n^{-1/2} amplitude" *is* the 2-norm
(Hilbert) input; p=2 is downstream of it, not independently derived. The audit's "imports the Hilbert
structure" is precise: the import is B3, and it is exactly as strong as the Born exponent.

## 2. The real load-bearing axiom is continuous reversibility (and it forces q=2 uniquely)
The import is *not* arbitrarily "choose q=2." There is a classical uniqueness:

> **Banach–Lamperti.** For `q ≥ 1, q ≠ 2`, the linear isometries of `ℓ_q^n` are exactly the signed
> permutations — a **finite** group. Only `q = 2` admits a **continuous** isometry group acting
> **transitively** on the unit sphere: `U(n)`.

So if the admissible screen transports are required to form a **continuous reversible group** (a Lie
group of symmetries, not just discrete relabelings), then `q = 2` is **forced uniquely**, hence p=2.
This is the standard "why 2" (Wootters; Hardy's continuity axiom; the reconstruction-of-QM literature):
the quadratic/Hilbert structure is singled out among all `ℓ_q` precisely by *continuous reversibility*.

## 3. The reduction (R5, sharpened)
R5 therefore reduces from a vague "is Born derived?" to a single, named, **decidable** question:

> **Does the SHARD record/holonomy dynamics force the admissible screen transports to be a
> CONTINUOUS reversible group (forcing q=2 → Born), or does it only justify discrete relabelings
> (leaving q — hence the Born exponent — underdetermined)?**

This is concretely connectable to the corpus: Paper 16 already characterizes the {reversible, valid,
finite-rank} record laws (its Theorem B is a no-go *within* that class). The open piece is **continuity**
— whether the record-transport group is a Lie group (continuous) or discrete. If the holonomy transports
between screens form a connected continuous family (as a "retained holonomy" carried continuously across
diamonds would suggest), q=2 follows by Banach–Lamperti and **Born is genuinely derived**, modulo only
that continuity. If the records support only discrete permutation symmetries, the exponent is not forced.

## Honest verdict
- The Born **exponent** p=2 is correctly derived by SHARD's equal-split argument — a clean
  Gleason/Hardy-style result.
- The import is **minimal and named**: a *single* axiom — continuous reversibility of screen transports
  (equivalently B3's 2-norm) — not the full Hilbert apparatus. By Banach–Lamperti this axiom forces
  q=2 uniquely, so nothing beyond it is assumed.
- This is **not a SHARD-specific deficiency**: *every* Born derivation imports an equivalent 2-encoding
  (Gleason: the Hilbert lattice; Hardy: continuity ⇒ K=N²; Zurek: unitary-swap symmetry; Barandes:
  unistochasticity). SHARD's is among the most explicit and minimal.
- **The sharp residue** is now: *do records force continuous reversibility of screen transports?* —
  a decidable question (check whether Paper 16's reversible record-law group is continuous/Lie or
  discrete), not the open-ended "derive QM."

So R5 is reduced from "imports the Hilbert structure" to "imports exactly one classical axiom
(continuous reversibility), which a single named theorem (Banach–Lamperti) converts into the full
Born rule — and whether records force that axiom is a decidable corpus-internal question."
