# Design note 6: the exact-determinism conjunct, priced — §4.1's magnitude clause vs §4.3's arena fixed point

**Status:** derivation document, 2026-07-02 (receipt-backed by `f6` check 7; no further code). **[Verdict upgraded same-date by design note 7 + receipt f7 (ledger #35): §3's "R3 tilted toward R2" becomes R2 MODULO THE ENUMERATED SET — the pinning reading R1 is closed against every current corpus principle, with the falsifier class and its 1e-3 precision requirement named in advance.]** This is the second decider of the post-`j4` plan: conjunct 2 of the records wall's standing conjunction — *exact per-mode determinism to sub-percent precision* — examined against what paper 1 actually licenses.

## 1. The tension, stated exactly

Paper 1 carries two clauses about the committed content:

- **§4.3 (the arena fixed point):** per mode, the committed content is deterministic — `Var[content | mode] = 0` — because the commitment potential `Φ(h) = ψ(h) + Σⱼe^{−hⱼ}` is strictly convex with a unique minimizer. The atoms `C(η_B), C(h_*), …` are the roots *of the admissible class*: complete primitive orthogonal parity ledgers **on the count-dual base `μ = (1/2, 1/2)`** (v6 paper 4 §73–76; the gate is load-bearing — `p2c`'s own exhibit shows a skewed base `μ(+) = 0.2` yields content `0.526 > W_*` and is excluded *from the admissible class* by the count-dual/orthogonality symmetry).
- **§4.1 (the coboundary clause):** the content clock's *form* is forced (a coboundary), but its **magnitude is physical configuration data — the law constrains differences only**.

The tension: §4.3's determinism is exact *at the exactly count-dual base*; §4.1 says the magnitude axis is configuration, not law. The question with teeth after `j4`: which clause governs the *realized* per-seal content in a physical web — and at what precision?

## 2. The three readings, priced

**(R1) Law-exact determinism.** The count-dual base holds exactly at every seal of every physical web; realized content = the atom, exactly. Status of the premise: **nowhere derived.** The count-dual base enters the corpus as the *admissibility gate* that makes the `W_*` ceiling a theorem of a class — a definition of the class, not a proof that physical configurations sit in it exactly. For the wall to stand on R1, count-dual exactness must hold web-wide to the precision `j4` measured — and `f6` check 7 now prices that precision: the content atom's base-skew sensitivity is **first order**, `dC/dp = −0.713404` at `p = 1/2` (the seal condition breaks the relabel symmetry — this is not a protected minimum), giving the map **`w ≈ 4.570·δp`**. So `j4`'s dispersion-passing spread (`w = 0.5%`) corresponds to base skew `δp ≈ 1.1×10⁻³`, and the robust full-cell width (`w = 10%`) to `δp ≈ 2.2×10⁻²`. **R1 therefore requires every seal's base to be count-dual to better than one part in a thousand across the entire web.** Nothing in the corpus forces, suggests, or even discusses that uniformity; it would be a new, strong, unstated physical postulate.

**(R2) Configuration-magnitude spread.** The §4.1 clause is read at face value: the realized magnitude is configuration data; local web inhomogeneity (base skew `δp`, or any other configurational modulation of the transported `σ`) spreads realized content around the arena root. Then `j4`'s route C is live *by default*: per-mille inhomogeneity already clears the statistical layer, and percent-scale inhomogeneity delivers the full manifoldlike cell. Under R2 the content-degeneracy wall is **down** — not by a new mechanism, but because the wall's precision demand (R1) was never a corpus commitment.

**(R3) Undecidable in-corpus.** The corpus genuinely does not fix which of R1/R2 physical webs realize (the placement sector is explicitly undelivered). Then the spread width `w` joins paper 1 §4.4's ledger as **[PHYSICAL] configuration data** — with the sharp, receipt-backed statement that the manifoldlikeness gate sits at `w ≈ 0.5%`, i.e. `δp ≈ 10⁻³`.

## 3. Verdict of this note

Reading the sources, R1 is not available as a *derived* position: the count-dual base is a class gate, the sensitivity is first-order, and the required uniformity (`10⁻³` web-wide) is a physical postulate the corpus has never made. The honest standing is **R3 tilted toward R2**: `w` is [PHYSICAL], unforced, and generically nonzero — and any generic nonzero value at or above the per-mille scale defeats the degeneracy wall's second conjunct. Combined with `f6`'s regime bridge (conjunct 1 = "realized regime sparse", experiment-facing via the echo floor) and `j4`'s route-A refusal (conjunct 3 held: the menu alone cannot rescue the strict model), the records wall now stands only on the *conjunction of a knife-edge precision postulate and a specific regime realization* — both named, both priced, one of them lab-addressable with an instrument the corpus already built (paper 10).

**Consequence for the program:** the default modeling position for record-native supplies is now *spread-bearing* (route B or C statistics — which are rank-equivalent continuum classes at the `j3`/`j4` scales), and the burden of proof has flipped: it is the *wall* that requires special assumptions, not the cell. Paper 16 should state exactly this inversion, with this note and `f6`/`j4` as its receipts.

## 4. What would refute this note

A derivation, from corpus principles, that physical webs realize the count-dual base exactly (or to better than `10⁻³`) at every seal — i.e., an upgrade of the §4.1 cochain identification that *pins the magnitude* rather than leaving it configurational. That is paper 1 §7's own named open ("whether the cochain identification can be upgraded to a derivation"); if it lands with exactness, R1 revives and the wall's second conjunct stands. The refutation path is stated so the inversion above is falsifiable, not rhetorical.
