# Paper 22 v3 delta review — Seat P: probability / instrument lens

Date: 2026-08-22

Reviewer seat: **P — probability, stochastic matrices, identifiability,
instrument normalization**. Blind, repo read-only; rebuilt from published
prose only. This report is evidence for adjudication, not itself an
adjudication.

## 0. Verdict

**ACCEPT-WITH-FIXES.**

The probability core is sound and now complete: the anchors `B`, `R`,
`C_phi`, `B^2`, `K_phi`, the neutral odds `49/625` and `576/625`, commit
normalization, and child recovery all reproduce exactly on my independent
rebuild, and the repaired law (V) is the correct general partial-visibility
family — I confirm it against a direct residual-environment Born-rule
computation at every sampled admissible `(gamma, phi)`. The v2 defect (the
false `Re(v)` rule) is gone; the mandatory `gamma=i` control lands on
`I_2`. The findings are four MINOR prose defects inside the repaired
material — an arithmetic slip in the printed proof, a visibility
contradiction between two corollaries, a sign error in the control-point
exemplar, and an unscoped equation — none of which moves a number,
definition, or claim boundary.

## 1. Method and independence statement

I worked only from published prose: the frozen pin, the candidate, the
construction note, Paper 13D (anchors and beta clause), Paper 21 (Eqs.
19–21 for the visibility labels), and the v2 record for survivor context.
No code or receipt was imported; there is none in the unit. All arithmetic
below is my own exact rational computation (`fractions.Fraction`), with a
10^5-point float grid used only as a sweep over `(gamma, phi)` and compared
at sample precision. Hashes of all fourteen bound inputs were recomputed
and match the pin's Section 2 table.

## 2. Anchor rebuild

Every Section 3.2 anchor recomputed from first principles:

- **`B`.** From the accepted beta clause `beta(a,u)=a` for `u<9`,
  `1-a` for `u>=9` with uniform `[25]` inputs:
  `Pr(beta=0)=9/25`, `Pr(beta=1)=16/25`; one route gives
  `B=|R|^2=[[9,16],[16,9]]/25`. Matches.
- **`R`.** Orthogonal with entry moduli fixed by `B`: columns have norms
  `1` and rows orthogonal forces opposite signs in one column;
  `(3/5,4/5)` moduli give exactly (14). Gauge freedom: diagonal input
  phases, diagonal output phases, simultaneous exchange. Matches.
- **`C_phi`.** `A_phi=R D_phi R` has diagonal amplitude
  `(9-16e^{i phi})/25` and off-diagonal `12(1+e^{i phi})/25`;
  squared moduli give `[[337-288cos phi, 288(1+cos phi)],...]/625`.
  Spot values: `phi=0 -> [[49,576],[576,49]]/625`; `phi=pi/2 -> B^2`;
  `phi=pi -> I`. Columns sum to one. All match.
- **`B^2`.** `B·B = [[337,288],[288,337]]/625`. Matches.
- **Neutral odds.** `Pr(T)=49/625`, `Pr(F)=576/625` at tensor input,
  neutral phase: the `C_0` column. Matches Eq (21).
- **`K_phi`.** `K_phi=C_phi B^{-1}`; `B^{-1}=[[9,-16],[-16,9]]`
  (det `=-175/625`, so `B^{-1}=25[[9,-16],[-16,9]]/(-175)
  =[[-9,16],[16,-9]]/7`); product gives the printed `1/175` matrix
  `[[63+288c,112-288c],[112-288c,63+288c]]`. Entrywise positivity needs
  both `63+288c>0` and `112-288c>0`, i.e. `c>-7/32` and `c<7/18`;
  endpoints factor via `(63+288c)^2-(112-288c)^2=175(576c-49)` whose
  roots are exactly `-7/32` and `7/18`. Matches, including Corollary
  7.4's refusal to extend past `gamma=1`.

## 3. Law (V) — full independent verification

I derived the reduced probe law without reading the paper's proof first.
Setup per the prose: after kickback, open-route state
`b_T|T>|e_T>+b_F e^{i phi}|F>|e_F>`; second lift `R` sends detector `j`
the amplitude `b_T r_{jT}|e_T>+b_F r_{jF} e^{i phi}|e_F>`; Born probability

```
p_j = |b_T r_{jT}|^2 + |b_F r_{jF}|^2
      + 2 Re[(b_T r_{jT})(b_F r_{jF})^* e^{i phi} gamma].
```

Route products by cell (inputs T,F × detectors 0,1):
`(b_Tr_{jT})(b_Fr_{jF})` equals `-144/625` at (T,0), `+144/625` at
(T,1), `+144/625` at (F,0), `-144/625` at (F,1). Baselines
`|b_Tr_{jT}|^2+|b_Fr_{jF}|^2 = 337/625` at own-detector cells and
`288/625` at crossed cells. Collecting:

```
p_j = [337 - 288 q_phi]/625   (own-detector cells)
p_j = [288(1 + q_phi)]/625    (crossed cells)
```

which is exactly (17). I then ran the direct Born rule against (17) over
a uniform sweep of `10^5` admissible `(gamma,phi)` points (`|gamma|<=1`
disk, `phi in [-pi,pi)`): zero disagreements beyond sample rounding.

Registered consequences, each re-derived:

1. **Control (mandatory).** `gamma=i, phi=pi/2`:
   `q=Re(i e^{i pi/2})=Re(i·i)=-1`; `C=[[337+288, 288·0],[0,337+288]]/625
   =I_2`. Deterministic self-return. The rejected `Re(v)` rule gives
   `q=Re(v)=0` here, i.e. `B^2` at every phase — false, as the v2
   adjudication found. Regression passes.
2. **Endpoints.** `gamma=1 -> C_phi`; `gamma=0 -> B^2`; along
   `gamma=e^{i theta}`, `q=cos(phi+theta)`, so the law is `C_{phi+theta}`
   — pure fringe displacement. Passes.
3. **Visibility audit.** Over `phi` at fixed `|gamma|`: own-detector row
   spans `337±288|gamma|` giving `(pmax-pmin)/(pmax+pmin)=(288/337)|gamma|`;
   crossed row spans `288(1±|gamma|)` giving `|gamma|`. Exactly Paper 21
   Eqs (20)–(21) with row labels preserved. Passes.
4. **Stochasticity scope.** Column sums: baseline columns already sum to
   one; the interference correction has zero column sums
   (`-288q+288q=0`). Entries in `[0,1]`: `337-288q in [49,625]`,
   `288(1+q) in [0,576]` for `|q|<=1`. Genuine column-stochastic
   matrix for every admissible `gamma`. `K_phi` correctly not
   continued. Passes.

## 4. Commit normalization and child recovery

- **Isometry (18).** Within fixed mode `m`: histories orthogonal,
  exhaust labels orthogonal, `sum_H Gamma_m([H]|[X])=1` gives unit norm.
  Across modes: stable records `|m_R>` orthogonal. Across sources:
  source-indexed exhaust labels. Isometry confirmed.
- **Joint law (20) and normalization.**
  `sum_{[H]} widehatGamma = C_phi(m|j)`, then `sum_m C_phi(m|j)=1`
  (column sums of (15)/(17)). Conditioning on the recorded mode divides
  by the positive marginal `C_phi(m|j)` and returns `Gamma_m([H]|[X])`
  exactly — recovery confirmed. See finding F-P4 on the `gamma` scope of
  this equation.
- **No dormant child.** The coproduct (19) contains one mode record and
  one history block; there is no register carrying the unchosen child's
  state space. Confirmed structurally.
- **Identifiability/gauge.** `R` is gauge-fixed only up to the three
  declared freedoms; no other orthogonal lift matches `B`'s entries
  (checked by brute enumeration of sign/phase patterns). Naked label
  swaps change typed controls and are not gauge arrows — consistent with
  the control matrix.

## 5. Findings

Ranked most severe first. No FATAL, no MAJOR.

### F-P1 (MINOR, proof-narrative arithmetic) — wrong intermediate scalar in Theorem 7's proof

"The interference term carries the product
`(b_Tr_{jT})(b_Fr_{jF})=\pm12/25`, whose phase-free magnitude gives
exactly the coefficient `288/625`."

The product is `±144/625` (e.g. `(3/5·4/5)(4/5·3/5)=(12/25)^2=144/625`);
with the leading `2 Re(.)` it yields `288/625`. As printed, `12/25` is a
single route amplitude factor and its magnitude does not give the stated
coefficient (`2·12/25=24/25 ≠ 288/625`). The final matrix (17) and every
number in Section 3 above are unaffected. Additionally the sign phrase
"`(-,+;+,-)` on the diagonal" reads ambiguous; the actual per-cell signs
are `-,-,+,+` ordered (T,0),(T,1),(F,0),(F,1).

**Replacement sentences (verbatim):**

> "The interference term carries the route-amplitude product
> `(b_Tr_{jT})(b_Fr_{jF})=\pm144/625`, whose magnitude with the leading
> factor `2\operatorname{Re}(\cdot)` gives exactly the coefficient
> `288/625`; substituting (16), it contributes
> `-(288\,q_\phi)/625` to each diagonal entry and
> `+(288\,q_\phi)/625` to each off-diagonal entry."

### F-P2 (MINOR, internal contradiction) — "unit visibility on both rows" in Corollary 7.1

Corollary 7.1's final sentence claims the pure-fringe family has "unit
visibility on both rows"; Corollary 7.3 states row visibilities
`(288/337)|gamma|` and `|gamma|`, so even at `|gamma|=1` the
own-detector row has visibility `288/337<1`. A candidate cannot assert
both.

**Replacement sentence (verbatim):**

> "along `gamma = e^{i\theta}` the law is (15) with `phi` shifted by
> `+theta`: a pure fringe displacement preserving the coherent-row
> visibilities `(288/337)` and `1`."

### F-P3 (MINOR, exemplar sign) — the `gamma = i` exemplar kets produce `gamma = -i`

Corollary 7.1 illustrates the control point with
`|e_T>=i|e_0>, |e_F>=|e_0>`. Their overlap is `\bar i·1=-i`, not `+i`;
as written they illustrate a different registered point
(`gamma=-i` at `phi=pi/2` gives `q=Re((-i)(i))=Re(1)=1`, i.e. `C_0`, not
`I_2`). Negate the second ket.

**Replacement sentence (verbatim):**

> "The environment states `|e_T> = i|e_0>`, `|e_F> = -|e_0>` represent
> the same ray and retain no which-route information; their overlap is
> `gamma=<e_T|e_F>=i`, and the interference phase cancels the route
> phase exactly at this setting."

### F-P4 (MINOR, unscoped equation) — Theorem 9 prints the joint law only at gamma = 1

Equation (20) uses `C_phi`, valid at complete closure. Under partial
uncomputation (explicitly contemplated by Section 7) the mode factor must
be `C_{phi,gamma}`. The constructed instrument always achieves
`gamma=1` via (11), so no constructed value moves; but the equation's
scope should be stated, since the paper elsewhere treats arbitrary
`gamma` as admissible apparatus state.

**Replacement sentence (verbatim):**

> "For mode input `j`, phase `phi`, fixed admitted source `X`, and
> residual overlap `gamma`, the accessible joint law is
> `widehatGamma_{phi,gamma,X}(m,[H]\mid j)=
> C_{phi,gamma}(m\mid j)\,Gamma_m([H]\mid[X])`; for the constructed
> instrument `gamma=1` by exact closure (11), which recovers the
> printed `C_phi` form and equation (21)."

### F-P5 (NOTE) — inherited parenthesized pseudo-math rendering

Stray-parenthesis inline pseudo-math (`(X_alpha...)`) throughout the
inherited sections, verbatim from v2/v1. Cosmetic; no content impact.

## 6. Fresh attacks beyond the mandated regressions

1. **Mixture attack on (V).** If `gamma` were itself random across
   trials (environment not re-prepared), observed statistics would be
   `(V)` averaged over the `gamma` distribution — still a legitimate
   stochastic matrix, but the paper never claims otherwise; (16) defines
   `gamma` per fixed apparatus state. No defect, but downstream consumers
   must hold the environment preparation fixed; noted for Paper 23.
2. **Positivity corner.** At `q=-1` the off-diagonal entries hit `0` and
   diagonal `1` — deterministic, still stochastic. At `q=1`, diagonal
   `49/625>0`. No negative entry is reachable for `|q|<=1`. Confirmed.
3. **Column-vs-row normalization.** (V) is column-stochastic; by the
   symmetry of the matrix each row also sums to
   `(337-288q+288(1+q))/625=1`, so both normalizations hold at every
   admissible `gamma`. Harmless, but worth stating: no reading of the
   law as row- or column-conditioned changes any value.
4. **Anchor mutation probes.** Perturbing any anchor (`B` weights,
   beta split, `R` signs) breaks at least one identity among
   `C_{pi/2}=B^2`, `K_phi` integrality at denominator 175, and the
   endpoint factorization — the anchor set is rigid, no silent
   deformation exists. Confirmed.
5. **Odds provenance.** `49/625` and `576/625` are conditional local
   probabilities given triggered instrument and neutral tensor input; the
   paper never converts them to occurrence frequencies (Thm 16). Scope
   respected.

## 7. Disposition requested

Verdict **ACCEPT-WITH-FIXES**: confirm both repairs, all nine CONSTRUCTED
coordinates, and order F-P1–F-P4 as a bounded prose repair. Alternatively
zero-touch acceptance with ledger errata. One strike is not triggered by
this seat: no semantic counterexample found.
