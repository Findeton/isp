# D28b — the D29 prerequisites: event-resolved influence, and the RS-covariance theorem

**Status:** PIN (pre-receipt), 2026-07-12; committed before `code/d28b_event_influence_exact.py` and `code/d28b_rs_covariant_kernel_exact.py` run. Provenance labels per D20. These are the two exact-grade prerequisites the D28 round-1 reviews established for D29 (math O1; physics O2): D29's order-based rulers need a well-posed order as input, and the kernel family deserving instrumentation is constrained by the covariance question.

## 1. Part 1 — event-resolved influence (the O1 repair)

**The defect being repaired:** at register level, the influence relation goes cyclic on re-touching webs (the D28 T4/kickback findings): registers are WORLDLINES, not events. **The repair:** events are (register, epoch) pairs — epoch = the position in the declared op sequence — with interventions inserted at the event's epoch and queries evaluated on the state truncated at the query epoch:

> I_ev((u, s) → (v, t)) = max over ACTIVE pairs α, α′ at (u, s), max q ∈ {Z, X} at (v, t) of TV — computed on the circuit truncated after epoch t.

**The conjecture (REPAIRED at the arc round — false as first pinned):** on the real family at the pinned active alphabet, **under the NON-DEGENERACY hypothesis (no same-pair op-suffix composing to the identity channel)**, event-resolved influence equals **time-respecting op-chain reachability**. The hypothesis is necessary: the E5 counterexample composes eight same-pair touches whose half-angles sum to 2π (asin(3/5) + asin(4/5) = π/2 exactly) — reachability TRUE, I_ev exactly 0 at the final epoch, influence positive mid-history (576/625 at epoch 3). This is the dynamical analog of the T1 g = 0 caveat: per-op couplings nonzero, composition null; and it is not measure-zero for grid-valued couplings (collar webs at N = 512 carry several ≥7-touch pairs). The battery results (E1–E4) are scope-true — no tested web is degenerate — and the reachability RELATION remains the well-defined combinatorial order D29/D30 consume; only its influence READING carries the hypothesis. Gated consequences: acyclicity (a strict partial order) on the tested webs; the register-level relation as the worldline quotient (E4's gated form is birth-epoch-to-final against reachability-any; the full epoch-max form inherits the same hypothesis).

**Receipt gates (`d28b_event_influence_exact.py`; exact rationals; exit 1 on failure):**
- **E1:** definition + alphabets printed; truncation machinery gated against the end-of-history machinery (t = final epoch reproduces D28's I exactly, spot battery).
- **E2 (the conjecture):** I_ev > 0 ⟺ time-respecting op-chain reachability, gated on: the re-touch web (the D28 T4 object — the child's event does NOT reach the parent's later event; the parent's early event reaches the child), the mailbox web (full event matrix: z1's post-birth event reaches A's post-write events and z3, NOT z2's events and NOT A's pre-write events — the worldline split), the diamond web, and a census subset.
- **E3 (acyclicity):** the transitive closure of the event relation is a strict partial order on every tested web (no 2-cycles; antisymmetry gated, not assumed).
- **E4 (the quotient):** register-level I (D28's pin) = max over epoch pairs of event-level I, gated on the mailbox and diamond webs — the round-1 register-cyclicity is the shadow of quotienting worldlines to points.

**What this buys D29:** a well-posed causal order per realized web (the event order), from which chain proper-time and interval dimension estimators are definable without the register-cyclicity pathology.

## 2. Part 2 — the RS-covariance theorem (the O2 question, answered constructively)

**The question (round-1 successor front):** does an NSE-compliant opportunity kernel satisfying the D28 battery AND the Rideout–Sorkin path-covariance analog exist — or does flags-observable make path-equality the wrong requirement?

**The pinned answer, to be receipt-carried: YES at every finite horizon, constructively — with the residual obstruction being STATIONARITY, not covariance.** The construction (the path-uniform kernel): on the none-free op grammar over a fixed horizon T, let Φ(H) = the number of none-free completions of history H to depth T, and set

> K_flat(o | H) = Φ(H + o) / Φ(H).

Then (i) K_flat is exactly normalized (Σ_o Φ(H+o) = Φ(H) by definition of completions); (ii) every path to the same final web carries the SAME path product (each product telescopes to 1/Φ(H_0)) — the RS path-covariance analog holds exactly; (iii) K_flat is NSE-compliant and battery-compliant: its weights are graph-isomorphism invariants (Φ is defined from the op grammar alone), preparation-independent by construction, sealed-protecting, cylinder-consistent within each fixed horizon (the {K_flat^T} family is not projective across horizons — R5's content), label-covariant. **The residual obstruction, exhibited:** K_flat is HORIZON-DEPENDENT — its step-1 weights at horizon T = 2 differ from horizon T = 3 (teleological weights; RS kernels are stationary). So the sharpened F12 statement: the kernel-selector must choose within {stationary but path-covariance-violating (K_collar/K_tail-class), path-covariant but horizon-dependent (K_flat-class), or a stationary-and-covariant kernel whose existence for this grammar is the remaining open question — the functional equation w(o₁|H)·w(o₂|H+o₁) = w(o₂|H)·w(o₁|H+o₂) for independent op pairs}.

**The flags-observable reading (stated, not dodged):** with flags recorded, two accretion orders are distinct observable histories, so "the same final web" is a quotient of the record. Path-covariance is then the requirement that the bookkeeping order carry no probability — exactly the cg-line's construction-order-gauge demand promoted to the stochastic kernel. K_flat satisfies it; the D28 kernels do not; both facts are physics, not conventions.

**Receipt gates (`d28b_rs_covariant_kernel_exact.py`; exact rationals; exit 1 on failure):**
- **R1:** the functional equation printed; K_collar and K_tail violate it (the N11 numbers re-gated: 1/40 vs 1/25; 2/81 vs 1/25).
- **R2:** K_flat constructed exactly on the D28 seed domain (none-free grammar, horizon T = 2): Φ computed by backward recursion on the history DAG; normalization gated at every node.
- **R3:** PATH-COVARIANCE gated exhaustively: for every reachable final web, all accretion paths carry the identical product (exact equality).
- **R4:** the D28 battery on K_flat: label-covariance (two relabeling classes), preparation-independence of the flag law, sealed protection, fixed-horizon cylinder consistency, nonzero weights.
- **R5:** the STATIONARITY obstruction exhibited: K_flat's step-1 weight vector at T = 2 vs T = 3 differ (exact inequality, printed) — the sharpened F12 front on the record.
- **R6 (honesty):** K_flat is none-free by construction; the none-op obstruction stated (a none step changes path length, so path-covariance across orders is posed on the none-free skeleton; the D28 kernels' none arm is one more reason they fail it).

## 3. What this does and does not claim

**Does:** repair the influence relation to a well-posed event order (D29's input); prove the RS-covariance question has a constructive YES at finite horizon with stationarity as the true residual; sharpen F12 into a three-way selector choice with an exact functional equation.
**Does not:** claim K_flat is THE kernel (it is teleological; selection stays empirical per D12/D28); extend beyond the pinned alphabets (the kickback scoping of D28 §2 applies verbatim); open D29's stochastic stage (separate pin).

## 4. Round-1 outcomes (arc round, 2026-07-12; LEDGER #135)

(F1) OPEN as posed (truncated queries are counterfactual-flavored; record-carrier epochs = the operational upgrade, a D31-class refinement). **(F2) ANSWERED — a leak class EXISTS beyond kickback: the same-pair cancellation** (E5, arc-round counterexample; the conjecture repaired with the non-degeneracy hypothesis; the battery scope-true). **(F3) CLOSED:** Φ is graph-blind for this grammar — the arc review's 3-line recurrence Φ(u, t) = u·Φ(u+1, t+1) + u(u−1)·Φ(u, t+1) with Φ(·, T) = 1 depends only on the unsealed-register count u (verified equal to the receipt tables at every node, T = 2 and 3), so isomorphism-invariance is trivial; the canonicalization is exercised by the R4 two-class gates. **(F4) SHARPENED AND MADE FINITE:** by F3's recurrence, the stationary-and-covariant existence question is a concrete computation on (u, t)-rational weight families at small horizons — the F12 trichotomy's open leg is now a finite problem. (F5) The flags-observable reading stands as stated in §2 (R6); the covariance object choice is declared physics. Battery upgrades applied at the arc round: E5; the fixed-horizon cylinder gate and two relabeling classes in R4 (the pinned battery as promised); §2(iii)'s "cylinder-consistent" scoped to within-horizon (the cross-horizon failure is R5's content — the {K_flat^T} family is not projective).
