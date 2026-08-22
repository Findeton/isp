# Paper 22 v3 delta review — Seat C: category / source / functor lens

Date: 2026-08-22

Reviewer seat: **C — source groupoid, child functors, naturality,
restriction, composition**. Blind, repo read-only; rebuilt from published
prose only. This report is evidence for adjudication, not itself an
adjudication.

## 0. Verdict

**ACCEPT-WITH-FIXES.**

Both repairs are genuine and confirmed on my independent rebuild: repair 1
restores the v1 fine-seed apparatus verbatim on the homogeneous domain
(content identity of every formula against the v1 candidate, Sections
5.1–5.3), and repair 2 states the correct general complex-visibility law
(V) with `q_phi = Re(gamma e^{i phi})` before deriving it. The two defects
that killed v2 are gone. The surviving findings below are prose-level
errors inside the repaired material — none moves a number, a definition,
or a scope wall — plus one inherited rendering blemish and one precedent
request. No third independent semantic counterexample was found; the
one-strike condition is not triggered by this seat.

Mandatory regressions: PASS (§§3–4). Fresh attacks: six (§6).

## 1. Method and independence statement

I read the frozen v3 pin, the v3 candidate, the construction note, the v1
candidate, the v2 candidate and its three seat reports and adjudication,
Paper 13D, and Paper 21. No implementation or receipt was imported; the
unit is prose-only and I checked that claim (the only fenced code blocks
in the candidate are the outcome product). I re-derived every load-bearing
object from the definitions: coproduct membership, child functors,
apparatus maps, kickback, restriction, external composition. Numbers were
recomputed independently in exact rational arithmetic; hashes were
recomputed with `shasum -a 256` and match the pin's Section 2 table on all
fourteen rows.

## 2. Regression sweep of every adjudicated v2 survivor

| # | Survivor | v3 locus | Attack run | Result |
|---|---|---|---|---|
| R1 | Homogeneous-source coproduct groupoid, refusal predicates | Defs 1–2, Prop 1, Eq (1) | heterogeneous `(B^0_1,B^0_2)` pair refused pre-evaluation; sort-changing arrow absent from hom-sets; no arrow between summands | holds |
| R2 | Total typed tensor/fusion child pair with carried spectators | Thm 1, Eqs (3)–(6) | naturality squares via accepted presentation maps and equivariant kernels; no undefined value assigned probability zero | holds |
| R3 | Source-indexed dependent commit isometry, no dormant child | Thms 8–10, Eqs (18)–(19) | exhaust labels `[X]`-indexed; coproduct target holds one mode record and one history block only | holds |
| R4 | Positive restriction naturality with seed marginalization | Thm 12 | deleted seed addresses carry product weight one; retained incidence kept exactly | holds |
| R5 | Branchwise zero/one-active restriction retaining `(m_R)` | Thm 13, Eq (22) | no target identification, no new mode opportunity, pushforward not new law | holds |
| R6 | External-tensor-only composition | Thm 14, Eq (23) | bifunctoriality and symmetric braiding; no internal union of marks | holds |
| R7 | Local process plurality at neutral input | Thm 15, Eq (21) | `49/625`, `576/625` recomputed from `B^2` entries | holds |
| R8 | Activity/root noninheritance | Thm 16 | arbitrary normalized source propensity multiplies the joint law without changing the local instrument | holds |
| R9 | Numerical anchors `B, R, C_phi, B^2, K_phi`, neutral odds | §6, §7 Cor 7.4 | full exact rebuild, see §6 item 6 | holds |

No v2 survivor is weakened anywhere in v3. The five new hostile-control
rows in the Section 13 matrix name exactly the v2 failure modes (biased
carrier, coarse bond bit, `[25]` repartition, `Re(v)` sentences,
recombination-time seed trace) and each is enforced by a named theorem or
predicate, not asserted.

## 3. Repair 1 (apparatus restoration) — independent confirmation

Diffed against the v1 candidate Sections 5.1–5.3:

- Seed space, law, purification: `Xi_X=[25]^{P_X}`, `mu_X=25^{-|P_X|}`,
  `|Omega_X>=5^{-|P_X|} sum|xi>`, `S_X=I-2|v_X><v_X|`,
  `S_X|0_Xi>=|Omega_X>`, `S_X^{-1}=S_X` — identical content to v1 Eqs
  (3)–(4), retagged (7)–(8). The coefficient identity
  `sqrt(25^{-|P_X|})=5^{-|P_X|}` is printed and exact.
- Witness computations `C_{T,X}`, `C_{F,X}`, controlled composition
  (9)–(10), closure theorem (11), kickback (12)–(13), and the
  second-tensor-query discriminator — identical content to v1 (5)–(9).
  v3 also repairs v1's duplicate "5.3" numbering.
- The nine/sixteen split appears only through the accepted 13D beta
  clause `beta(a,u)=a` for `u<9`, `1-a` otherwise; verified against
  Paper 13D's displayed beta definition and its use in the `Q_J`
  kernels. It is read, never redefined.

New relative to v1: only Theorem 4 (seed-preparation naturality). Its
proof is correct: a source arrow permutes `P_X`; the uniform superposition
is permutation-invariant; `|v_X>` transports as a fixed linear combination
of transported states; blank maps to blank.

Pin Section 4's bars are all satisfied: no biased carrier, no coarse bond
bit, no fine-to-coarse isometry, no reader-statistic change, no phase
reconvention, no coefficient change. Because no coarse binning occurs, no
coarse-bin reversibility proof is owed; the pin says so and the
construction agrees.

## 4. Repair 2 (partial visibility) — independent confirmation

Rebuilt law (V) from scratch, not from the paper's proof: kickback state
`b_T|T>|e_T> + b_F e^{i phi}|F>|e_F>`, second lift `R`, Born probabilities
at both detectors for both inputs, residual overlap
`gamma=<e_T|e_F>` symbolic. Result:

$$
C_{\phi,\gamma}=\frac1{625}
\begin{pmatrix}337-288q_\phi&288(1+q_\phi)\\288(1+q_\phi)&337-288q_\phi\end{pmatrix},
\qquad q_\phi=\operatorname{Re}(\gamma e^{i\phi}),
$$

with baselines `337/625` (diagonal-type cells) and `288/625`
(off-diagonal-type cells) and per-cell route-amplitude products
`±144/625` — matching (17) entry for entry. I verified a 10^5-point
admissible `(gamma,phi)` grid against the direct Born rule with
first-lift amplitudes `(3/5,4/5)` and `(-4/5,3/5)`: zero mismatches at
sample precision. All four pin-registered consequences check:

1. **Control.** `gamma=i, phi=pi/2`: `q=Re(i·i)=-1`; matrix
   `[[625,0],[0,625]]/625=I_2`. Deterministic return. The rejected
   `Re(v)` rule prints `B^2` here for every phase; the control genuinely
   discriminates.
2. **Endpoints.** `gamma=1` gives (15); `gamma=0` gives `B^2`; along
   `gamma=e^{i theta}` the law is (15) with `phi -> phi+theta`, since
   `Re(e^{i theta} e^{i phi})=cos(phi+theta)`.
3. **Visibility audit.** Row extrema over `phi`: diagonal row
   `337±288|gamma|` over 625, off-diagonal row `288(1±|gamma|)` over
   625; visibilities `(288/337)|gamma|` and `|gamma|`, agreeing with
   Paper 21 Eqs (20)–(21) row labels.
4. **Scope.** Columns sum to one for all admissible `gamma` (the signed
   interference matrix has zero column sums); entries lie in `[0,1]`
   since `337-288q in [49,625]` and `288(1+q) in [0,576]`. `K_phi` and
   its interval stay pinned at `gamma=1` (Cor 7.4).

## 5. Findings

Ranked most severe first. Severities: FATAL / MAJOR / MINOR / NOTE. None
is FATAL or MAJOR.

### F-C1 (MINOR, proof-narrative arithmetic) — wrong scalar in the Theorem 7 proof

Proof of Theorem 7: "The interference term carries the product
`(b_Tr_{jT})(b_Fr_{jF})=\pm12/25`, whose phase-free magnitude gives
exactly the coefficient `288/625`."

The route-amplitude product is `±144/625`, not `±12/25`. For tensor input
at the crossed detector: `(b_Tr_{jT})(b_Fr_{jF})=(3/5·4/5)(4/5·3/5)
=(12/25)(12/25)=144/625`; the leading `2\operatorname{Re}(\cdot)` then
gives `2·144/625=288/625`. The printed `12/25` is one route amplitude
factor, not the product, and `|12/25|=0.48` does not give `288/625`.
The baseline sentence in the same proof is correct (`337/625`,
`288/625`), and the final matrix (17) is correct — this is an
intermediate-sentence defect only. The sign phrase is also ambiguous:
the per-cell products are `(-,+,+,-)` reading `(T,0),(T,1),(F,0),(F,1)`,
so the diagonal cells both carry `-` and the off-diagonal cells both `+`.

**Replacement sentence (verbatim):**

> "The interference term carries the route-amplitude product
> `(b_Tr_{jT})(b_Fr_{jF})=\pm144/625`, whose magnitude with the leading
> factor `2\operatorname{Re}(\cdot)` gives exactly the coefficient
> `288/625`; substituting (16), it contributes
> `-(288\,q_\phi)/625` to each diagonal entry and
> `+(288\,q_\phi)/625` to each off-diagonal entry."

### F-C2 (MINOR, internal contradiction) — Corollary 7.1 contradicts Corollary 7.3 on visibility

Corollary 7.1 ends: "along `gamma = e^{i\theta}` the law is (15) with
`phi` shifted by `+theta`: a pure fringe displacement with unit
visibility on both rows." Corollary 7.3 prints row visibilities
`(288/337)|gamma|` and `|gamma|`. Even at `|gamma|=1` the diagonal row
has visibility `288/337 < 1`; "unit visibility on both rows" is false and
contradicts the paper's own registered audit.

**Replacement sentence (verbatim):**

> "along `gamma = e^{i\theta}` the law is (15) with `phi` shifted by
> `+theta`: a pure fringe displacement preserving the coherent-row
> visibilities `(288/337)` and `1`."

### F-C3 (MINOR, exemplar mismatch) — Corollary 7.1's residual kets give the wrong overlap sign

Corollary 7.1: "The environment states `|e_T> = i|e_0>`,
`|e_F> = |e_0>` represent the same ray". Their overlap is
`<e_T|e_F>=\overline{i}=-i`, not the registered `+i`. Same-ray is right;
the sign is not. Negate the second exemplar:
`|e_T>=i|e_0>`, `|e_F>=-|e_0>` gives `<e_T|e_F>=(-i)(-1)=+i`, both kets
still on one ray.

**Replacement sentence (verbatim):**

> "The environment states `|e_T> = i|e_0>`, `|e_F> = -|e_0>` represent
> the same ray and retain no which-route information; their overlap is
> `gamma=<e_T|e_F>=i`, and the interference phase cancels the route
> phase exactly at this setting."

### F-C4 (MINOR, unscoped equation) — Theorem 9's joint law is printed at gamma = 1 only

Theorem 9 states `widehatGamma_{phi,X}(m,[H]\mid j)=C_phi(m\mid j)
Gamma_m([H]\mid[X])` — the fully coherent mode law. After repair 2 the
mode law is `C_{phi,gamma}`; a joint law consistent with Section 7 at
arbitrary residual overlap must use it, reducing to the printed form at
`gamma=1`. The constructed instrument does force `gamma=1` by exact
closure (11), so no number moves — but the sentence as printed is
silent about this, while Section 7 explicitly contemplates partial
uncomputation.

**Replacement sentence (verbatim):**

> "For mode input `j`, phase `phi`, fixed admitted source `X`, and
> residual overlap `gamma`, the accessible joint law is
> `widehatGamma_{phi,gamma,X}(m,[H]\mid j)=
> C_{phi,gamma}(m\mid j)\,Gamma_m([H]\mid[X])`; for the constructed
> instrument `gamma=1` by exact closure (11), which recovers the
> printed `C_phi` form and equation (21)."

### F-C5 (NOTE, inherited rendering) — parenthesized pseudo-math in inherited sections

Definition 1 items 2/5/6 print `(X_\alpha\in B_s(I_\alpha))` and similar
with a stray leading parenthesis; the same pattern recurs in Definitions
2–4, Propositions 1–2, Theorems 1–4, 8–9, and Section 8's opening
(`([H])`, `(Gamma_m([H]\mid[X]))`). All of it is inherited verbatim from
the v2 survivors (and partly v1). Rendering blemish only; the mathematics
reads unambiguously. Recorded so no future reviewer rediscovers it.
Fixing is optional under a bounded whitespace-class repair and touches
no adjudicated content.

### F-C6 (NOTE, precedent request, no byte change) — gauge reading of "physically typed modes"

Theorem 6's gauge statement makes `R` unique up to diagonal input phases,
diagonal output phases, and simultaneous exchange of the two physically
typed modes. A hostile reader may ask whether that exchange is gauge or a
different instrument. The v2 adjudication already binds the answer:
naked label swaps are not gauge arrows (hostile-control matrix row), and
the exchange here is the simultaneous one inside the calibrated-lift
gauge group. No v3 change requested; the adjudicator is asked to rebind
this reading as precedent for downstream consumers.

## 6. Fresh attacks beyond the mandated regressions

1. **Seed-trace hunt.** A residual seed address at recombination would
   make `gamma` seed-dependent and decohere (17) into a `q_phi`
   mixture. Theorem 5's closure returns every seed address to blank,
   and the fused-witness computation consumes the complete assignment
   `xi` into `F(X,xi)`, so no unread address can be stranded. Attempted
   counterexample failed; no defect.
2. **Sort leakage through spectators.** Spectator sorts may differ from
   `s`; could spectator transports smuggle a sort-changing arrow? No:
   spectator transports preserve each spectator's own sort and are
   identity-carried in both children; every source arrow preserves the
   common active sort by definition. No leakage.
3. **Restriction vs seeds.** Positive restriction deletes seed
   addresses; the remaining law is independent of which, because the
   product law has total weight one per address. Degenerate restriction
   is branchwise and retains `(m_R)`. Both hold.
4. **External composition vs fusion algebra.** The two factors of (23)
   act on disjoint carriers with separate records; no shared register
   exists for a commutator to live in. Same-source multi-mark
   composition remains unconstructed, as declared.
5. **Phase-convention equivariance.** Swapping printed T/F labels sends
   `phi -> -phi` and `gamma -> conj(gamma)`; (V) is invariant since
   `Re(conj(gamma) e^{-i phi})=Re(gamma e^{i phi})`. Convention, not
   physics; no defect.
6. **Anchor mutation sweep.** `B` from the beta-clause marginals;
   `R^TR=I` with entries `±3/5,±4/5`; `C_0=[[49,576],[576,49]]/625`,
   `C_{pi/2}=B^2`, `C_pi=I`; `K_phi=C_phi B^{-1}` reproduces the
   printed `1/175` matrix; positivity endpoints `-7/32, 7/18` via
   `(63+288c)^2-(112-288c)^2=175(576c-49)`; neutral odds `49/625`,
   `576/625`. All exact; nothing moves.

## 7. What would have killed this candidate

Recorded to show the attack was genuinely attempted. The v1 killer
(heterogeneous active sorts) is refused at Proposition 1 before any
evaluation. The v2 killers are absent: no biased or coarse seed carrier
exists in Section 5 (pin bars + control matrix), and the only
occurrences of the rejected `Re(v)` rule in v3 are sentences marking it
false. A recombination-time seed trace would violate closure (11) and is
caught by construction. I found no third independent semantic
counterexample.

## 8. Disposition requested

Verdict **ACCEPT-WITH-FIXES**: confirm both repairs and all nine
CONSTRUCTED coordinates, and order F-C1–F-C4 as a bounded prose repair —
no number, definition, theorem statement, control, or scope wall moves.
Alternatively the adjudicator may take zero-touch acceptance and record
F-C1–F-C4 as ledger errata; either route preserves the science. F-C5 is
a note; F-C6 is a precedent request. One strike is not triggered.
