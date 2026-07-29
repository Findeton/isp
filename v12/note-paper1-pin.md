# v12 PAPER 1 — SELF-CONTAINED BARANDES-EXTENSION RESULTS PAPER (PIN)

**Status:** PIN, STRICT, 2026-07-29.  **Binding:** the user's order
(2026-07-29): *"ensure the paper is self contained (apart from
code) and in a publishable state. so don't make reference to other
isp/shard papers, make it stand alone as a barandes extension."*
Terminal sources consolidated: W1′ (#7), W5 (#12), W3′ (#14),
W4′ (#15), W2 (#16), W7 (#24).  Paper 0 v2.2 remains the
programme charter and is NOT restated (the ontology stays out;
only the delimited relation-to-Barandes discussion appears).
v13/GW material out of scope.  Lean NONE.

## Self-containment rules (hard; each is a review gate)

1. **Citations: external literature ONLY.**  [B1] arXiv:2302.10778,
   [B2] arXiv:2309.03085, [B3] arXiv:2507.21192 (page-cited
   quotes); Fine, PRL 48, 291 (1982); Abramsky–Brandenburger, NJP
   13, 113036 (2011); Abramsky–Mansfield–Barbosa, arXiv:1111.3620;
   the Tsirelson-bound literature; Weyl/noncommutative-torus
   multipliers; finite Stone–von Neumann; T. Zaslavsky, *Signed
   graphs*, Discrete Appl. Math. 4 (1982) 47–74 (canonical for
   switching; the gain-graph cospectrality paper secondary);
   Mukunda et al., quant-ph/0107006; the decoherent-histories
   records antecedent (Gell-Mann–Hartle; Halliwell); CAZAC/
   Wiener-Khinchin signal-processing sources for the flat-spectrum
   identification.  ZERO references to ISP/SHARD papers, corpus
   versions, notes, ledgers, or units.
2. **Forbidden tokens in the paper text** (mechanical audit):
   unit labels (W1′, W2, W2a/b/c, W3′, W4′, W5, W6, W7, GW1, GW2,
   BC1, BC2, U1–U4, T1–T5), version labels (v1–v13 as corpus
   names), "LOG", "ledger", "pin", "hostile round", "terminal",
   "green-unreviewed", "ISP", "SHARD", file names of corpus notes.
   Fresh theorem/section numbering throughout.
3. **Every result carried in-paper:** each theorem PROVED in the
   paper; each antecedent cited to external literature with the
   paper's own contribution delimited; each computational
   proposition stated with its regenerating script named.
4. **Reconstructed witnesses:** the obstruction-independence
   section rebuilds ALL witness models inside the paper as
   explicit finite constructions with fresh bundle code — the
   two-frame composite Bell model and the division-event
   non-gluing model included.  No reliance on prior corpus
   measurements.
5. **The code bundle (the user's one exception):**
   `v12/paper1_code/` — standalone scripts, one per results
   section, adapted from the committed unit code where useful but
   each independently runnable; exact arithmetic only; a master
   runner `paper1_run_all.py` regenerating EVERY number in the
   paper and printing a receipts table; anchors within the bundle
   are self-anchors (the paper's own numbers), exit-1-only.
6. **House style:** single-threaded; no correction narrative; no
   process story; no ontologizing (the relation-to-Barandes
   section states faithful/extension/tension readings of HIS
   texts, with his hedges quoted; no claim about nature beyond
   the models); scope tags on every theorem (dimension, support
   class, sample scope).

## Content (sections, fixed)

1. **Introduction.**  Barandes' indivisible-processes formulation
   summarized from [B1–B3]; the question: what governs the
   composition of the stochastic representation across a cut.
   Contributions list (the paper's own, complete and scoped).
2. **The three defects and the coherence law.**  Δᴮ, the actual-law
   residual, existential divisibility; the rotation counterexample
   separating them; the cross-term identity; the coherence/tree
   law; the closed form; the annihilator theory (monomial group);
   outer-torus and compensated-cut gauges; the flat-spectrum
   (CAZAC) identification, credited.
3. **The CHSH three-class skeleton.**  The three convex bodies;
   2 / 2√2 / 4 exactly; completeness of the planar phase family;
   the anti-correlation exhibit; antecedents credited (Fine, AB,
   Tsirelson) with the paper's contribution delimited.
4. **Records.**  The record hypotheses (correlation,
   availability); THE RECORDS THEOREM: stable records ⟹
   divisibility on the recorded algebra under record-preserving
   dynamics; the O(n²) decision procedure; sharpness on realizable
   supports; the division-event biconditional on the Bell model;
   the eraser control; decoherent-histories antecedent credited.
5. **The gauge of a compositional law.**  [B3]'s entrywise gauge;
   THE TWO REDUCTION THEOREMS in their repaired forms (the placed
   rotation; the named admissible-class quantifier; the
   degenerate-support vacuity disclosed); the orbit classification
   by even-cycle holonomies with the Zaslavsky antecedent.
6. **The loop signature and its incompleteness.**  The relation-
   loop scalar β on Weyl families (finite Stone–von Neumann
   cited); β not a functional of the Born shadow (counterexample
   in-paper); the pair-orbit theorem (the tripartite path graph,
   switching, the seam torsor); PAIR-completeness ⟺ the 4-cycle
   lattice condition, with the φ-criterion realizing every
   failure; the n=4 witness in full exact arithmetic; the
   completion 𝒦 (lowest-degree, sufficiency not minimality; the
   Σ𝒦 identity); the n=5 sample; general n open.
7. **Record descent and its limit.**  Block-diagonalization by
   record sector; full recording ⟹ the shadow composes; the
   recorded-but-phased witness (the limit); the eraser restoring
   cross-sector coherence.
8. **Independence of the obstruction families.**  The exact
   relation table, every witness constructed in-paper (per rule
   4), each entry carried by an exact model.
9. **Relation to Barandes.**  What is taken from [B1–B3]; what is
   proved about the framework (the LTP-forcing lemma STATED AND
   PROVED against [B3]'s own equations, with the composite Bell
   model built in-paper); where the paper extends him (the
   composition subject; the gauge licensing) and where his texts
   resist, quoted fairly.
10. **Open problems.  Non-claims.**  General-n completeness;
    exhaustive n=5; converse record notions; beyond-CHSH; the
    scope of every claim restated.
- **Appendix: reproduction.**  The bundle inventory, per-number
  script map, runtimes.

**File:** `v12/paper1-composition-defect.md` (title finalized by
the writer; working title: *"Interference as the Composition
Defect of Stochastic Shadows: Records, Gauge, and the Loop
Signature of Indivisible Stochastic Processes"*).  Math in $/$$
throughout.

**Pre-registered outcomes:** PAPER1-PUBLISHABLE /
PAPER1-BLOCKED-AT-⟨item⟩ (with the census).

**Review plan (binding):** writer delivery → adjudicator
verification (mechanical forbidden-token audit; full bundle
regeneration; spot proof reads) → PAPER HOSTILE ROUND with
mandatory: self-containment audit, full number sweep vs the
bundle, proof audit, attribution audit, [B3]-quote verification
(quotes may be sourced from the committed W5 verbatim set but
cited to [B3] pages), publishable-register judgement → repairs →
terminal.  Quotes and receipts rules as house-standard;
GREEN-UNREVIEWED until its round.
