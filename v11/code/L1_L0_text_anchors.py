#!/usr/bin/env python3.13
"""
v11 L-1 + L0 — TEXT-ANCHOR RECEIPT.

Every passage quoted verbatim in
    v11/note-L1-lorentz-no-go-lemma.md
    v11/note-L0-scale-no-go-lemma.md
is verified twice:

  (A) the quote appears verbatim in the CITED COMMITTED SOURCE FILE,
      inside the cited line span;
  (B) the quote appears verbatim in the LEMMA NOTE that cites it.

Verbatim means: identical after whitespace normalization only
(runs of whitespace collapsed to one space).  Markdown hard-wrapping
is the only thing normalized away.  Blockquote markers ('>') are
stripped from the note side before normalization; nothing else is
altered on either side, so emphasis markers, backticks, dashes,
minus signs and superscripts must match exactly.

Exit 0 = every anchor clean.  Exit 1 = one or more mismatches.

Deterministic, single-threaded, no dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # .../isp

NOTE_L1 = "v11/note-L1-lorentz-no-go-lemma.md"
NOTE_L0 = "v11/note-L0-scale-no-go-lemma.md"

P8 = "v3/relativistic-isp-v3-paper8-continuum-qft-reconstruction-no-go.md"
P57 = "v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md"
P17 = "v7/relativistic-isp-v7-paper17-three-walls-classification-theorem.md"
LEDGER = "v8/LEDGER.md"
PAPER0 = "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
CAT = "v11/note-v11p0a-reproduction-catalog.md"

# (anchor id, note file, source file, (first_line, last_line), quote)
ANCHORS: list[tuple[str, str, str, tuple[int, int], str]] = [
    # ---------------- L-1 ----------------
    (
        "L1-A1 v3p8 Lemma 2.3",
        NOTE_L1, P8, (110, 114),
        "Let `K:X\\to X` be a stochastic map on a finite set, represented by a "
        "row-stochastic matrix. If `K` has an inverse `L` that is also stochastic, then "
        "`K` is a permutation matrix.",
    ),
    (
        "L1-A2 v3p8 Corollary 2.4",
        NOTE_L1, P8, (132, 137),
        "An exact covariance action by invertible stochastic maps on a fixed finite "
        "configuration set can only act by permutations. Therefore a nontrivial Lorentz "
        "boost cannot be represented in this paper as an exact stochastic automorphism "
        "of one fixed finite regulator state space.",
    ),
    (
        "L1-A3 v3p8 admissible finite covariance statements",
        NOTE_L1, P8, (139, 147),
        "The only admissible finite covariance statements in this paper are: "
        "1. equality or convergence of declared finite-battery statistics for sampled "
        "Lorentz-related tests; "
        "2. projective compatibility of different finite batteries approximating "
        "Lorentz-related continuum tests; "
        "3. an imported continuum covariance representation listed as enrichment. "
        "None of these is a finite-regulator proof of full Lorentz covariance.",
    ),
    (
        "L1-A4 v3p8 'can only act by permutations'",
        NOTE_L1, P8, (132, 137),
        "can only act by permutations",
    ),
    (
        "L1-A5 catalog 1.3(d) presuppositions",
        NOTE_L1, CAT, (312, 314),
        "a finite configuration set and row-stochastic maps. "
        "**Nothing else — no background metric, no action, no Hilbert space.**",
    ),
    (
        "L1-A6 paper0 §4 fixed-configuration posit",
        NOTE_L1, PAPER0, (146, 149),
        "because renewals reset to the root: the configuration space at division "
        "events is small, fixed, and identical across runs.",
    ),
    (
        "L1-A7 paper0 §7 the bound",
        NOTE_L1, PAPER0, (272, 275),
        "v11 may expect at most statistical/approximate Lorentz invariance at "
        "renewal grain, never exact covariance",
    ),
    (
        "L1-A8 paper0 §7 the prohibition",
        NOTE_L1, PAPER0, (276, 277),
        "Any v11 claim of exact finite covariance is pre-refuted by this lemma "
        "and forbidden.",
    ),
    (
        "L1-A9 catalog 1.3(e) the collision",
        NOTE_L1, CAT, (320, 321),
        "on exactly such a space, no nontrivial boost can act as an invertible "
        "stochastic map",
    ),
    (
        "L1-A10 catalog 1.3(e) binding constraint",
        NOTE_L1, CAT, (324, 325),
        "**binding constraint that paper 0 does not currently carry**",
    ),
    (
        "L1-A11 catalog 1.3(e) the two non-invertibilities",
        NOTE_L1, CAT, (325, 327),
        "the very non-invertibility that Cor 2.4 treats as the obstruction to "
        "covariance is what Barandes treats as the signature of indivisibility.",
    ),
    (
        "L1-A12 catalog §7 rank 2 the same, sharpened",
        NOTE_L1, CAT, (3135, 3137),
        "the non-invertibility Cor 2.4 treats as the obstruction to covariance is "
        "the same non-invertibility Barandes treats as the signature of "
        "indivisibility.",
    ),
    (
        "L1-A13 catalog 1.5(d) the sprinkling presupposition",
        NOTE_L1, CAT, (380, 381),
        "a background Minkowski space to sprinkle into",
    ),
    (
        "L1-A14 catalog 1.6(e) the BHS block on v11's carrier",
        NOTE_L1, CAT, (417, 422),
        "v11's crystals are finite-valency by construction, so BHS says their renewal "
        "sublattice **cannot** be statistically Lorentz-invariant in the sprinkling "
        "sense.  U4 must therefore test a *weaker* covariance (order-level, per "
        "P-Lor) and say so in advance — otherwise it will manufacture a false "
        "negative.",
    ),
    # ---------------- L0 ----------------
    (
        "L0-A1 p57 §2.1 the result",
        NOTE_L0, P57, (33, 33),
        "SHARD does not, and provably cannot, fix the absolute scale `σ_A` — which "
        "has length-weight −2 and is in bijection with Newton's `G` (weight +2) via "
        "`G·σ_A = 1/4`, so fixing one fixes the other (they are linked, never equal). "
        "This is not an absence of success but a single structural theorem.",
    ),
    (
        "L0-A2 p57 the two weight-zero invariants",
        NOTE_L0, P57, (35, 35),
        "**`κ·σ_A = 2π`  and (separately)  `G·Λ² = const`**  (two weight-zero "
        "invariants — *each* a fixed pure number, not numerically equal to one "
        "another; what they share is the structure, not a value; paper6 Corollary 2; "
        "the structural lemma *invariant ⟺ weight-zero*, not the implementation-audit "
        "monomial count; here `Λ` is the inverse-length UV/spectral cutoff, distinct "
        "from the unimodular cosmological constant `Λ₀` of §1.5)",
    ),
    (
        "L0-A3 p57 §2.2 the weight-counting lemma",
        NOTE_L0, P57, (39, 39),
        "*every dimensionful record quantity is `(pure number) × l^{±k}` (one record "
        "length), and every intrinsic record functional factors through the record "
        "sector, hence is `g_λ`-invariant (paper6 Theorem G), hence weight-zero; so "
        "no intrinsic quantity can have the weight −2 that `σ_A` needs.*",
    ),
    (
        "L0-A4 p57 the unification",
        NOTE_L0, P57, (51, 51),
        "*deriving `1/G` always trades it for a labeling-equivalent cutoff; the "
        "missing datum is exactly one absolute length unit, which no weight-zero "
        "record functional can be.*",
    ),
    (
        "L0-A5 p57 gate G1",
        NOTE_L0, P57, (37, 37),
        "**gate G1** — *no sealed law consumes the record area `A_rec` (a "
        "weight-`±k` dimensionful datum) except through the continuum labeling map "
        "`ℓ`.*",
    ),
    (
        "L0-A6 p57 airtight iff G1",
        NOTE_L0, P57, (37, 37),
        "the no-go is airtight *iff* G1 holds",
    ),
    (
        "L0-A7 p57 l_step the unique dimensionful primitive",
        NOTE_L0, P57, (37, 37),
        "the seal-spacing length `l_step` is provably the unique dimensionful "
        "primitive and the sole gauge direction.",
    ),
    (
        "L0-A8 p57 abstract, c_m eligible",
        NOTE_L0, P57, (9, 9),
        "not the dimensionless gravitational coupling-per-species `c_m = Gm²/ℏc`, "
        "which is weight-zero and intrinsic and therefore *eligible* to be a record "
        "output (the open hierarchy question)",
    ),
    (
        "L0-A9 v8 LEDGER correction #13",
        NOTE_L0, LEDGER, (47, 47),
        "per v7 paper 16 §5 / paper 57, these are *separate* record-scale invariants "
        "(each constant under `l → μl`), **not numerically equal to each other** — "
        "the \"= const\" chain must not read as an equality between them.",
    ),
    (
        "L0-A10 catalog 2.2(c) the compressed form is wrong",
        NOTE_L0, CAT, (765, 768),
        "the compressed form *\"`κ·σ_A = G·Λ² = const`\"* is **WRONG AS AN EQUALITY** "
        "— these are two *separate* weight-zero invariants, each a fixed pure number, "
        "**not numerically equal**.",
    ),
    (
        "L0-A11 catalog 2.2(c) grade",
        NOTE_L0, CAT, (756, 757),
        "**[THEOREM], and structurally UNCONDITIONAL**",
    ),
    (
        "L0-A12 catalog 2.2(d) presuppositions",
        NOTE_L0, CAT, (774, 776),
        "the sealed-record weight calculus (Theorem G / Corollary 2 of v6 paper 6) "
        "and **gate G1**",
    ),
    (
        "L0-A13 catalog 2.2(e) the transfer reading",
        NOTE_L0, CAT, (779, 781),
        "**KINEMATICS** — a theorem about what a counting ontology can carry — and it "
        "**transfers to v11 almost unchanged**, since v11's kinematics is also a bare "
        "causal order with no absolute length.",
    ),
    (
        "L0-A14 catalog 2.2(e) the corpus against itself",
        NOTE_L0, CAT, (788, 791),
        "the grading-homomorphism and weight-zero-subring structure is **standard** — "
        "it is the algebra of a graded ring and the content of dimensional analysis "
        "(Buckingham-Π; Coleman–Weinberg).  **This note proves no new mainstream "
        "theorem.**",
    ),
    (
        "L0-A15 catalog 0.5 the two unbridged rows",
        NOTE_L0, CAT, (120, 123),
        "the v10 generated grammar is not derived from the sealing formalism",
    ),
    (
        "L0-A16 catalog 0.5 actors are not division events",
        NOTE_L0, CAT, (120, 123),
        "v10's actors are not v6's division events",
    ),
    (
        "L0-A17 p17 §4.1 the derivation does not stand alone",
        NOTE_L0, P17, (119, 119),
        "the SHARD *derivation* that `G` is record-un-derivable does **not** stand on "
        "its own. It rides the entropic equation-of-state route",
    ),
    (
        "L0-A18 p17 §4.1 the four named premises",
        NOTE_L0, P17, (121, 126),
        "Concretely the `G` leg is conditional on **four** named premises, all "
        "isolated in Paper 57 §1: "
        "- **(i) the Jacobson–Clausius premise itself** — that `δQ = T dS` over all "
        "local horizons *is* the equation of state of spacetime; the locus of the "
        "Padmanabhan \"interpretation-not-derivation\" critique; "
        "- **(ii) AXIOM (R)** — the modular / Euclidean-rotation identification "
        "fixing the temperature *value* `β = 2π`. Gibbs thermality at *some* `β` is "
        "unconditional (record passivity / a finite Lenard theorem), but the value "
        "`2π` — hence `T = a/2π` and the Clausius coefficient `η = 1/4G` — rests on "
        "this unproven axiom; "
        "- **(iii) Jacobson's LOCAL-EQUILIBRIUM premise** `θ = σ = 0` at the "
        "bifurcation surface — presumed, not derived — which selects pure Einstein "
        "over the nonequilibrium `f(R)` / Lovelock branch (Eling–Guedens–Jacobson "
        "2006: dropping it forces a dissipative treatment); "
        "- **(iv) the CONTINUUM FOCUSING GATE** `θ' = −R_{kk}`, the one imported "
        "continuum input (now reduced to two native conditional gates: a finite "
        "double-null affine-pair readout and a cofinal-tightness / "
        "no-silent-refinement condition).",
    ),
    (
        "L0-A19 p17 §4.1 the internal asymmetry",
        NOTE_L0, P17, (128, 128),
        "**The internal asymmetry, stated honestly.** Paper 57's §2 **scale no-go "
        "proper** — the weight-counting lemma that every intrinsic record functional "
        "is weight-`0` while `σ_A` is weight `−2`, so the absolute unit is outside "
        "the `g_λ` gauge orbit — does **not** itself depend on axiom (R). That part "
        "is the structural fact the receipt verifies. But the classification *claim* "
        "that this missing weight-`(−2)` unit **is gravity's Newton `G`** is "
        "delivered through the Jacobson / Clausius Einstein-form route. So the `G` "
        "**leg of the classification** is honestly a **conditional no-go** — "
        "conditional on the Jacobson–Clausius premise plus the three Paper 57 "
        "conditionals. We do **not** present it as a clean structural no-go on a par "
        "with tensor and mode. The headline is **two structural no-gos + one "
        "conditional**, never a clean threefold all-experiment-fixed symmetry — a "
        "load-bearing honesty constraint of this paper.",
    ),
    (
        "L0-A20 p17 c_m rides the MODE axis",
        NOTE_L0, P17, (25, 25),
        "carrying with it the matter hierarchy `c_m = Gm²/ℏc`, which is itself "
        "weight-`0` and so *not* a scale-orbit datum, but whose value is import-fixed "
        "through the same mode-canonicalization the rank label awaits, per Papers "
        "5/VIII",
    ),
    (
        "L0-A21 catalog 2.3(a) v10's compression",
        NOTE_L0, CAT, (807, 809),
        "the wall stands unconditionally, the `G`-naming of it is conditional.",
    ),
    (
        "L0-A22 catalog 2.3(e) the discipline",
        NOTE_L0, CAT, (831, 834),
        "must state, separately, what identifies the missing quantity with a physical "
        "constant — and grade that identification on its own.",
    ),
    (
        "L0-A23 paper0 §7 L0's corrected form",
        NOTE_L0, PAPER0, (280, 283),
        "only κ·σ_A = 2π and, separately, G·Λ² = const are weight-zero",
    ),
    (
        "L0-A24 paper0 §11 no constant reproduced",
        NOTE_L0, PAPER0, (456, 458),
        "No coupling constant or dimensionless number of nature is reproduced "
        "anywhere in v1–v10",
    ),
    (
        "L0-A25 paper0 §11 the one open eligible target",
        NOTE_L0, PAPER0, (457, 458),
        "the one open eligible target is c_m, and it belongs to Phase IV under L0's "
        "bound.",
    ),
]

WS = re.compile(r"\s+")
BQ = re.compile(r"^[ \t]*(?:>[ \t]?)+")


def norm(text: str) -> str:
    return WS.sub(" ", text).strip()


def note_body(text: str) -> str:
    """Strip markdown blockquote markers, then normalize."""
    return norm("\n".join(BQ.sub("", line) for line in text.splitlines()))


def read(rel: str) -> list[str]:
    p = ROOT / rel
    if not p.is_file():
        raise SystemExit(f"FATAL: missing file {p}")
    return p.read_text(encoding="utf-8").splitlines()


def main() -> int:
    src_cache: dict[str, list[str]] = {}
    note_cache: dict[str, str] = {}
    failures: list[str] = []
    out: list[str] = []

    out.append("v11 L-1 + L0 — TEXT-ANCHOR RECEIPT")
    out.append("=" * 72)
    out.append(f"repo root : {ROOT}")
    out.append(f"anchors   : {len(ANCHORS)}")
    out.append("check A   : quote verbatim in cited source file, inside cited span")
    out.append("check B   : quote verbatim in the lemma note that cites it")
    out.append("normalization: whitespace only (+ blockquote markers on the note side)")
    out.append("=" * 72)
    out.append("")

    for aid, note_rel, src_rel, (lo, hi), quote in ANCHORS:
        if src_rel not in src_cache:
            src_cache[src_rel] = read(src_rel)
        if note_rel not in note_cache:
            note_cache[note_rel] = note_body((ROOT / note_rel).read_text(encoding="utf-8"))

        lines = src_cache[src_rel]
        if hi > len(lines):
            failures.append(f"{aid}: cited span {lo}-{hi} exceeds {src_rel} ({len(lines)} lines)")
            out.append(f"[FAIL] {aid}  (span out of range)")
            continue

        span = norm("\n".join(lines[lo - 1:hi]))
        q = norm(quote)

        a_ok = q in span
        b_ok = q in note_cache[note_rel]

        if a_ok and b_ok:
            out.append(f"[ OK ] {aid}")
            out.append(f"       source {src_rel}:{lo}-{hi}   note {note_rel}")
        else:
            out.append(f"[FAIL] {aid}")
            out.append(f"       source {src_rel}:{lo}-{hi}   note {note_rel}")
            out.append(f"       A (in source span): {a_ok}")
            out.append(f"       B (in note)       : {b_ok}")
            out.append(f"       quote: {q[:220]}")
            if not a_ok:
                out.append(f"       span : {span[:220]}")
            failures.append(f"{aid}: A={a_ok} B={b_ok}")

    out.append("")
    out.append("=" * 72)
    if failures:
        out.append(f"RESULT: {len(failures)} / {len(ANCHORS)} ANCHORS FAILED")
        for f in failures:
            out.append(f"  - {f}")
        out.append("EXIT 1")
    else:
        out.append(f"RESULT: {len(ANCHORS)} / {len(ANCHORS)} ANCHORS CLEAN")
        out.append("Every quoted passage in both lemma notes is verbatim in its")
        out.append("cited committed source file, inside its cited line span.")
        out.append("EXIT 0")
    out.append("=" * 72)

    report = "\n".join(out)
    print(report)
    (Path(__file__).resolve().parent / "L1_L0_anchors_output.txt").write_text(
        report + "\n", encoding="utf-8"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
