# D30 — the frozen-kernel cone comparison

**Status:** PIN (pre-receipt), 2026-07-12; committed before `code/d30_frozen_cone_comparison.py` runs. Provenance labels per D20. The final stage of the D28→D30 arc: the frozen kernels, measured by the frozen rulers, with the verdict computed by a pre-registered rule — no tuning anywhere.

## 1. Frozen inputs (nothing here may change after this pin)

- **The instrument card:** `data/d29_instrument_card.json`, sha256/16 = af5f6b011d3c48f8, commit 4d1d7e3 — consumed unchanged; comparisons at MATCHED N per its per-cell calibration (the disclosed V3 lesson).
- **The kernels, at their D28 definitions verbatim:** K_collar and K_tail(ε = 1/5) (the d28_opportunity_kernels weights: uniform over {none} ∪ births ∪ collar-interacts, tail adding ε·q^d beyond); K_flat at toy horizon (T ≤ 3 — its Φ recursion is exponential in the web space; scope disclosed, no approximation smuggled); plus the PURE-BIRTH control K_birth (births only — provably order-dimension ≤ 2 by the D28 mirror-DFS theorem, so it MUST read non-manifold: a falsifiable control on the whole pipeline).
- **The measured order:** the EVENT order via time-respecting op-chain reachability. Scope [disclosed]: influence = reachability is PROVEN at battery scale (D28b, 25 event pairs) with the positive side compositional (path products of couplings) and the zero side the wire-time lemma; D30 relies on the reachability order as the exact combinatorial object it is, with the influence reading carried at that scope.
- **Growth is classical** (kernel weights are graph-functions — no quantum state enters the growth law; declared); incremental all-pairs-distance maintenance for the tail weights; fixed seeds, printed; N targets {256, 512} matched to card cells (1024 excluded on compute budget, declared); 10 seeds per kernel per N; NO re-rolls, one run per cell.

## 2. The measurements and the pre-registered verdict rule

Per kernel per N, on the event order: **d̂_MM** on the maximal-cardinality Alexandrov interval (protocol: argmax |I(u,w)| via one matmul; require |I| ≥ 64, else the web-level fraction is reported with its caveat flag); **the chain constant** c = L/N^(1/d̂) against the card's c_d(N) at matched N; **the growth exponent** α from L vs N (the percolation-vs-manifold discriminator); **the 3-chain ratio**; **the tail signature** (beyond-collar opportunity rate — K_collar must read exactly 0, K_tail positive: the D28 opportunity-grade separation at scale).

**The verdict rule [pre-registered]:** a kernel ENTERS the M^d band at N iff (i) d̂ within the card's ±0.35 of an integer d ∈ {2, 3, 4}, (ii) chain_c within ±15% of the card's c_d(N), (iii) α within 1/d ± 0.10, and (iv) — the thin-V7 inheritance — it separates from the box-4 control's signature by ≥ 2 SE on at least one instrument (no manifold verdict may ride inside the polyhedral mimicry margin). The four branches: **(1)** some kernel enters a band → the bridge candidate; **(2)** several enter → freeze a higher-scale discriminator; **(3)** none enters → the growth law in this kernel class does not produce manifoldlike order at tested scale — a theorem-adjacent negative with named causes (which instrument excludes each kernel), feeding F12's selector; **(4)** n/a here (no kernel inserts geometry). The expectation is branch (3) and is stated BEFORE the run: uniform-weight graph-local kernels are percolation-adjacent; finding otherwise would be the surprise.

## 3. Discipline

V9 verbatim (no v9 measurement; these webs are the D28 kernels' own). No tuning: kernel parameters, ruler bands, and the verdict rule are all frozen at pins that precede this run. The D28 §2 alphabet pin is honored by measuring the reachability order (the channel-robust object at the pin). Outcome branch (3), if it lands, is a RESULT, not a failure — it is the first frozen-kernel cone measurement and the sharpest constraint yet on F12's selector.

## 4. Round-1 fronts (pinned)

(F1) Interval-selection bias on grown webs (the argmax interval is an extreme statistic — does it bias d̂ up or down; the web-level-fraction fallback's honesty). (F2) The reachability-order scope at growth scale (battery-proven, structurally extended — where could it leak). (F3) K_flat's toy-horizon row: is any comparison meaningful at T ≤ 3, or is it presence-only. (F4) Growth stationarity: does the kernel reach a steady op-mix regime before N target (the α fit's validity window). (F5) The verdict rule's (iv): is 2-SE-from-box-4 the right mimicry bar or should it be the joint signature.
