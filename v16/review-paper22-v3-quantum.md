# Paper 22 v3 delta review — Seat Q: quantum / no-hiding / instrument-physics lens

Date: 2026-08-22

Reviewer seat: **Q — unitarity, no-hiding, kickback, closure, residual
environments, visibility controls**. Blind, repo read-only; rebuilt from
published prose only. This report is evidence for adjudication, not
itself an adjudication.

## 0. Verdict

**ACCEPT-WITH-FIXES.**

The repaired quantum content is correct. I rebuilt the apparatus chain
(purification, controlled witness computations, closure), re-proved the
kickback identity, re-derived law (V) from the residual-environment Born
rule, and fired every registered visibility control including the two the
v2 adjudication made mandatory: `gamma=i, phi=pi/2 -> I_2` (deterministic
self-return) and the pure-fringe family `gamma=e^{i theta}` (shift
`+theta`). Both repairs hold; all v2 quantum survivors pass regression.
The findings are four MINOR defects in the repaired prose — one shared
arithmetic slip in the Theorem 7 proof narrative, a contradiction between
Corollaries 7.1 and 7.3, a ket-exemplar sign error at the registered
control point, and an unscoped joint-law equation — none of which moves a
number or weakens a theorem. No third independent semantic counterexample
was found by this seat; the one-strike condition is not triggered here.

## 1. Method and independence statement

Sources read: the frozen v3 pin, the candidate, the construction note,
Paper 13D, Paper 21 (Sections 4.2 and 7 for the gamma-overlap law and
visibility labels), the v1 candidate (restoration source), and the v2
record for survivor context. Nothing was imported from any implementation;
the unit contains no code. All quantum claims below were rebuilt
symbolically and checked numerically in exact or high-precision arithmetic
of my own devising. All fourteen bound-input hashes were recomputed and
match the pin's Section 2 table.

## 2. Regression sweep of the adjudicated v2 quantum survivors

| # | Survivor | v3 locus | Attack run | Result |
|---|---|---|---|---|
| R1 | Homogeneous source refusal before evaluation | Prop 1 | heterogeneous pair, sort-changing arrows, empty/one-active families | holds |
| R2 | Total typed child pair | Thm 1 | naturality via presentation maps and equivariant kernels | holds |
| R3 | Reversible-erasure obstruction + no-hiding | Thms 2–3 | complement must distinguish collisions; orthogonal inputs with equal accessible state force orthogonal complements — both re-proved | holds |
| R4 | Coherent `C_phi`, stable record, commit, restriction, external composition | §§6–11 | see §4 rebuild; all reproduce | holds |
| R5 | Numerical anchors | §§6–7 | full exact recomputation | holds |

The five new control-matrix rows name exactly the failure classes that
killed v1/v2 and each has a named enforcement point. The mandatory
regressions are discharged in §4.

## 3. Repair 1 — apparatus restoration, quantum audit

- **Purification (7)–(8).** `|Omega_X>` has unit norm since
  `(5^{-|P_X|})^2·25^{|P_X|}=1`. `S_X=I-2|v><v|` with unit `|v_X>`
  (`(|0>-|Omega>)/sqrt2` of two orthonormal states) is Hermitian
  involutive; `S_X|0_Xi>=|Omega_X>` verified by direct expansion:
  `|0> - 2|v><v|0> = |0> - 2·(1/sqrt2)·|v> = |0>-(|0>-|Omega>) =
  |Omega>`. Restoration matches v1 Eqs (3)–(4).
- **Witness computations (9)–(10).** `C_{T,X}` reads no seed (tensor
  child draws no cross-pair seed — consistent with the 13D kernel
  structure); `C_{F,X}` reads the complete assignment. Both injective on
  declared subspaces, extended by inverse pairing; controlled sum of
  unitaries under orthogonal mode projectors is unitary. Matches v1
  (5)–(6).
- **Closure (11).** Fusion block reversal: `C_{F,X}^{-1}` then
  `(S_X^{-1}\otimes I)=S_X\otimes I`. Every register returns to blank.
  Matches v1 Thm 5. A seed traced into recombination would contradict
  (11); the control row is enforced by this theorem, not asserted.
- **Kickback (12)–(13).** `P_phi` commutes with all classical registers;
  on the fused witness subspace it multiplies by `e^{i phi}`, so
  conjugation by `U_{Q,X}` pulls it back to `D_phi\otimes I` on mode
  space. The held-out discriminator (second tensor query kills the
  relative phase for every requested `phi`) is reproduced. Matches v1
  (8)–(9).
- **Theorem 4 (new).** Naturality of preparation under source arrows:
  basis permutations leave the uniform superposition fixed;
  Householder vector transports as a linear combination of transported
  states. Correct, and needed for item 2 of Theorem 11's list.

No biased carrier, coarse bond bit, fine-to-coarse isometry, reader change,
phase reconvention, or coefficient change exists anywhere in Section 5.

## 4. Repair 2 — partial visibility, full quantum rebuild

State before recombination after kickback:
`b_T|T>|e_T>+b_F e^{i phi}|F>|e_F>`, `gamma=<e_T|e_F>`, first-lift route
amplitudes `(b_T,b_F)=(3/5,4/5)` (tensor input) and `(-4/5,3/5)` (fusion
input). Second lift `R`; detector amplitudes `b_Tr_{jT}|e_T> +
b_Fr_{jF}e^{i phi}|e_F>`. Born:

```
p_j = |b_T r_{jT}|² + |b_F r_{jF}|² + 2 Re[(b_T r_{jT})(b_F r_{jF}) e^{i phi} gamma].
```

Route products per cell: `-144/625, +144/625, +144/625, -144/625`
(ordering (T,0),(T,1),(F,0),(F,1)); baselines `337/625` diagonal-type,
`288/625` crossed-type. Collection gives exactly (17) with
`q_phi = Re(gamma e^{i phi})`. Verified against direct computation over a
dense admissible sweep: zero disagreement.

Controls:

1. **Registered regression control (mandatory).** `gamma=i, phi=pi/2`:
   `q=Re(i·i)=-1`, so `C=[[625,0],[0,625]]/625=I_2`. Deterministic return
   through own detector for both inputs — maximal interference whose
   phase cancels the kickback exactly. The rejected `Re(v)` rule prints
   `q=0` here (`B^2`, phase-flat): false, as v2's Seat Q already
   demonstrated with `v=i`. Regression passes.
2. **Endpoints.** `gamma=1 -> C_phi`; `gamma=0 -> B^2` (stable record or
   orthogonal erasure trace — both physically distinct routes to the same
   reduced law, correctly not distinguished by (V)); complete reversible
   erasure returns `gamma=1`. Passes.
3. **Pure-fringe family (mandatory).** `gamma=e^{i theta}`:
   `q=cos(phi+theta)`; law equals `C_{phi+theta}` — a rigid displacement
   of the fringe with unchanged contrast. Passes.
4. **Visibility audit.** Own-detector row `(288/337)|gamma|`, crossed row
   `|gamma|`; coherent values `288/337` and `1`; both vanish at
   `gamma=0`. Row labels agree with Paper 21 Eqs (20)–(21). Passes.
5. **Positivity/normalization envelope.** Columns sum to one (zero-sum
   signed correction); entries nonnegative on the whole admissible disk,
   hitting the deterministic corners only at `|q|=1`. Passes.
6. **`K_phi` scope.** Corollary 7.4 refuses any generalized continuation
   through partial coherence; consistent with the pin's scope clause.
   Passes.

## 5. Findings

Ranked most severe first. No FATAL, no MAJOR.

### F-Q1 (MINOR, proof-narrative arithmetic) — intermediate scalar mislabeled in Theorem 7's proof

"The interference term carries the product
`(b_Tr_{jT})(b_Fr_{jF})=\pm12/25`, whose phase-free magnitude gives
exactly the coefficient `288/625`."

The product is `±144/625`: each factor is a route amplitude like
`(3/5)(4/5)=12/25`, and the product of the two factors enters, doubled by
the real-part prefactor: `2·144/625=288/625`. As printed, the sentence's
own arithmetic does not close (`2·12/25=24/25≠288/625`). Matrix (17),
all baselines, and all controls are unaffected — this is the proof's
narration, not its result. The printed sign pattern "`(-,+;+,-)` on the
diagonal" also does not parse against the actual cell signs
`(-,-,+,+)` over (T,0),(T,1),(F,0),(F,1).

**Replacement sentences (verbatim):**

> "The interference term carries the route-amplitude product
> `(b_Tr_{jT})(b_Fr_{jF})=\pm144/625`, whose magnitude with the leading
> factor `2\operatorname{Re}(\cdot)` gives exactly the coefficient
> `288/625`; substituting (16), it contributes
> `-(288\,q_\phi)/625` to each diagonal entry and
> `+(288\,q_\phi)/625` to each off-diagonal entry."

### F-Q2 (MINOR, internal contradiction) — "unit visibility on both rows" vs Corollary 7.3

Corollary 7.1's fringe-shift sentence asserts unit visibility on both
rows; Corollary 7.3 states `(288/337)|gamma|` and `|gamma|`. At
`|gamma|=1` the own-detector row still has visibility `288/337<1`. The
candidate contradicts its own registered audit.

**Replacement sentence (verbatim):**

> "along `gamma = e^{i\theta}` the law is (15) with `phi` shifted by
> `+theta`: a pure fringe displacement preserving the coherent-row
> visibilities `(288/337)` and `1`."

### F-Q3 (MINOR, exemplar sign) — control-point kets realize `gamma = -i`, not `+i`

Corollary 7.1 illustrates with `|e_T>=i|e_0>, |e_F>=|e_0>`; the overlap
is `\bar i=-i`. At `phi=pi/2` that realizes
`q=Re((-i)(i))=Re(1)=1`, i.e. `C_0` — not the registered `I_2` control.
The exemplar therefore fails to illustrate the very corollary it sits in.
Negate the second ket: `<i e_0|-e_0>=(-i)(-1)=+i`.

**Replacement sentence (verbatim):**

> "The environment states `|e_T> = i|e_0>`, `|e_F> = -|e_0>` represent
> the same ray and retain no which-route information; their overlap is
> `gamma=<e_T|e_F>=i`, and the interference phase cancels the route
> phase exactly at this setting."

### F-Q4 (MINOR, unscoped equation) — Theorem 9's joint law silently fixes gamma = 1

Equation (20) composes the mode law `C_phi` with the child kernel. Under
partial uncomputation the mode law is `C_{phi,gamma}`; the joint law at
general residual overlap is its product with the child kernel, reducing
to (20) at `gamma=1` — which the constructed instrument always attains
via closure (11). The restriction should be stated where the equation is
printed, since Section 7 admits arbitrary `gamma` as apparatus state.

**Replacement sentence (verbatim):**

> "For mode input `j`, phase `phi`, fixed admitted source `X`, and
> residual overlap `gamma`, the accessible joint law is
> `widehatGamma_{phi,gamma,X}(m,[H]\mid j)=
> C_{phi,gamma}(m\mid j)\,Gamma_m([H]\mid[X])`; for the constructed
> instrument `gamma=1` by exact closure (11), which recovers the
> printed `C_phi` form and equation (21)."

### F-Q5 (NOTE) — inherited pseudo-math rendering

Stray-parenthesis inline math throughout inherited sections, verbatim
from v2/v1. Cosmetic only.

## 6. Fresh attacks beyond the mandated regressions

1. **Environment-model independence.** (V) was derived without assuming
   anything about `|e_T>,|e_F>` beyond existence, typing, and overlap —
   mixed witness/record/environment residuals, entangled among
   themselves. I re-derived with explicit product environments and with
   one entangled pair; only `gamma` enters. Robust.
2. **Phase-convention attack.** Global redefinition `phi -> phi+chi`
   (moving the phase onto the environment instead of the witness):
   equivalent to `gamma -> gamma e^{-ichi}`, absorbed identically in
   `q_phi`. No physical sentence changes. Convention, not content.
3. **Same-ray degenerate case.** `|e_T>,|e_F>` on one ray with
   `gamma=|gamma|e^{i theta}`, `|gamma|=1`: which-route information
   absent yet fringes displaced — the pure-fringe family. The paper's
   claim that visibility audits *residual which-route information*
   (Cor 7.3 last sentence) survives: contrast carries `|gamma|`,
   position carries `arg(gamma)`.
4. **Closure-vs-commit boundary.** After (11) the query registers are
   blank but the commit writes new records; could the commit re-introduce
   residual overlap? No — the commit acts after recombination, on the
   blank subspace, and its records are classical and orthogonal by
   construction (18). No defect.
5. **No-hiding consistency.** Thm 3 forces colliding inputs to stash the
   distinction in orthogonal complements; the apparatus stashes it in
   the partition/seed fields and uncomputes them. If uncomputation were
   imperfect, `gamma` would drop below 1 continuously — exactly law (V)'s
   family. The three regimes (coherent/record/fringe) are one continuum,
   which is the repair's point. Consistent.
6. **Anchor mutation probes.** Flipping one `R` sign, swapping beta's
   split point, or perturbing any anchor breaks `C_{pi/2}=B^2` or the
   endpoint factorization loudly. No silent deformation found.

## 7. What would have killed this candidate

The two v2 killers were re-attempted explicitly. A biased-seed
substitution cannot be stated within Section 5's bound inventory (pin
bars + control rows + my byte-level comparison to v1). An `Re(v)`
sentence appears only inside sentences marking it false. A third class —
a wrong general law from special cases — was hunted directly: (V) is the
*general* law, its special cases are derived corollaries, and the
registered control discriminates it from the rejected special-case rule.
None fired.

## 8. Disposition requested

Verdict **ACCEPT-WITH-FIXES**: confirm both repairs, all nine CONSTRUCTED
coordinates, and order F-Q1–F-Q4 as a bounded prose repair; alternatively
zero-touch acceptance with ledger errata. One strike is not triggered by
this seat.
