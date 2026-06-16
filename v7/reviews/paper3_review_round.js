export const meta = {
  name: 'review-v7-paper3-seal-spacing-no-go',
  description: 'Hostile review of v7 Paper 3 (the seal-spacing no-go), round 2 (CONFIRMING): verify the round-1 fixes -- (1) the spectral M0/M1 is now HEDGED to a candidate/plausible moment-labelling ambiguity (NOT a verified resolution), with "fixes only a ratio, never the absolute scale" the load-bearing point; (2) the numerology refutation rests on ALGEBRAICITY + the converging-away sequence, NOT on an unproven transcendence of Srednicki a; (3) coefficient-vs-content disambiguated (0.609/0.495/0.368 are coefficients, contents 0.156/0.109/0.063); (4) "closed within the weight grading (modulo G1)". Confirm d is NOT a fixed quantity + the no-go is correctly scoped (airtight modulo G1; seal-rate REFUTES not CLOSES; c_m + external-identity open). Pre-geometric, high precision, single-threaded; hunt overclaims BOTH directions.',
  phases: [{ title: 'Review', detail: '3 referees on Paper 3' }],
}

const P3 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper3-seal-spacing-no-go.md'
const P2 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper2-content-supply.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const P4 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper4-sealed-record-events-and-born-composition.md'
const P6 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper6-arec-gauge-closure-v6.1.md'
const P57 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md'
const PXI = '/Users/felixrobles/workspace/isp/v6/publishable/paper-XI-sealed-record-gravity-no-go.md'
const R3 = '/Users/felixrobles/workspace/isp/v7/code/p3_d_nogo.py'
const R2B = '/Users/felixrobles/workspace/isp/v7/code/p2b_event_law_saturation.py'
const R2C = '/Users/felixrobles/workspace/isp/v7/code/p2c_vector_ledger_roots.py'

const RULES = `
STANDING RULES to enforce:
- PRE-GEOMETRIC DISCIPLINE (Tier-A): every Tier-A claim (d, the content C(h), the evidence clock, the capacity W_*) must use NO spacetime/Lorentz/light-cone/metric/s^2. The gravitational coefficients (1/4, 2pi, G, Lambda, sigma_A, M0/M1) are allowed ONLY in the cross-tier no-go sections 5-6, where the POINT is they cannot fix the Tier-A spacing. FLAG any geometry leak into a Tier-A claim.
- HIGH PRECISION: every numeric claim reproducible at mpmath dps>=100 / sympy-exact. RUN the receipts: python3 ${R3} , ${R2B} , ${R2C} (if mpmath/sympy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python), plus your own checks. In particular re-derive: E[I]=Var[I]=1; eta_B/C(eta_B), h_*/C(h_*), W_* (mode-dependent, both < W_*); the grading c=2(e-b); theta_B root of t^3+t^2+t-1 and theta_B^2 of s^3+s^2+3s-1 (both irreducible /Q) vs Srednicki 0.295417; M0/M1=2pi.
- SINGLE-THREADED: reads written-once. FLAG "previously/we now/earlier version/corrected/round N/campaign/version N" (a bare date stamp is allowed).
- HONESTY / OVERCLAIM HUNT (BOTH directions -- this is a NO-GO paper):
  (a) MANUFACTURED IMPOSSIBILITY: the paper must NOT claim the no-go is unconditional. It must be airtight ONLY MODULO gate G1 (the sole load-bearing premise), and G1 must be stated as a SCOPE ASSUMPTION (proved-finite for the executed corpus, interface-level for un-imported texts, NOT a closure theorem). The seal-rate primitive must be described as REFUTING THE SHARPEST COUNTEREXAMPLE to G1, NEVER as "closing G1". CHECK this wording is exact.
  (b) BURIED CRACK: conversely the paper must NOT under-disclose a genuine crack. The c_m=Gm^2/hbar-c strength lane and the external structural-identity must be tagged OPEN/permitted (weight-0 eligible), not silently closed. The "scale-blind => vacuous for d" step is rigorous ONLY for record-INTERNAL coefficients (d is itself weight-0, so two weight-0 numbers can coincide); confirm the paper does not over-extend it to forbid an external identity.
  (c) FAITHFULNESS to paper4/paper6/paper57/paperXI: the trichotomy (paper6 Theorem G grading homomorphism), the firing law (paper4 s71-76 vector fixed point), G1 (paper6), the spectral M0/M1 and SIGMA-SPLIT (paper57/paperXI). Read them. Is the M0-vs-M1 "factor-2pi gap resolved" claim faithful (or is it a new claim the corpus does not support)?
  (d) THE d-STATUS: is the layered (c)+(b)/(d) verdict correct -- content deterministic-per-mode + mode-dependent set + bound-only W_* + random Exp(1) clock? Is "the only robust quantitative statement is d < W_*" right, or is there in fact a canonical d the paper misses?
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['focus', 'verdict', 'must_fix', 'overclaims', 'math_or_claim_errors', 'pre_geometric_violations', 'single_threaded_violations', 'new_paths_opened', 'summary'],
  properties: {
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue', 'where', 'severity', 'fix'], properties: { issue: { type: 'string' }, where: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'major', 'critical'] }, fix: { type: 'string' } } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    math_or_claim_errors: { type: 'array', items: { type: 'string' }, description: 'each with the high-precision check you ran and its residual' },
    pre_geometric_violations: { type: 'array', items: { type: 'string' } },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    new_paths_opened: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['THE d-STATUS (sections 1-4): is the three-object discipline (content C(h) / capacity W_* / evidence clock I) correct and the layered verdict "d is NOT a fixed quantity -- mode-dependent content (a finite set {0.156,0.109,...}, no canonical member, all < W_*) + bound-only W_* + random Exp(1) clock" faithful? RUN p3/p2b/p2c; re-derive E[I]=Var[I]=1, the two mode contents, W_*, independently dps>=100. Is "the only robust quantitative statement is d < W_*" right -- or is there a canonical d (e.g. a mean across modes, or eta_B as THE root) the paper wrongly denies? Is the content/evidence/capacity separation rigorous (does the random clock really NOT propagate into the content)?'],
  ['THE NO-GO (section 5) + faithfulness: is the grading-homomorphism trichotomy (paper6 Theorem G) faithfully stated and genuinely EXHAUSTIVE? Re-derive the monomial weight 2b+c-2e and the dimensionless case c=2(e-b) (sympy). Is the TRIBONACCI algebraic refutation correct AND now correctly framed (theta_B root of t^3+t^2+t-1, theta_B^2 of s^3+s^2+3s-1, both irreducible /Q; the refutation must rest on ALGEBRAICITY + the partial-wave sequence converging AWAY from theta_B^2, NOT on an unproven transcendence of Srednicki a -- confirm the paper no longer claims a is transcendental)? Is the SPECTRAL-ACTION discussion now correctly HEDGED -- M0/M1 differ by 2pi is arithmetic, "which moment is the EH coefficient" is convention-dependent and a CANDIDATE correction to the [CONJECTURED] corpus value (paper57 s2.3 / paperXI s7), NOT a verified resolution, and the load-bearing point is "fixes only the ratio G/l_step^2, never absolute G, regardless"? FLAG any residual "resolved/no gap" overclaim. Try to BREAK the no-go: find a coefficient outside the trichotomy.'],
  ['SCOPE & HONESTY (sections 6-9) -- overclaim hunt BOTH directions. (a) Is the no-go correctly NON-unconditional -- airtight MODULO gate G1 (the sole premise), with G1 a SCOPE ASSUMPTION and the seal-rate REFUTING-not-CLOSING it? FLAG any wording that says "closes G1" or implies unconditionality. (b) Is the c_m strength lane + the external structural-identity correctly tagged OPEN/permitted (weight-0 eligible), not buried? Is the "scale-blind => vacuous for d" step correctly limited to record-INTERNAL coefficients (since d is itself weight-0)? (c) pre-geometric discipline (gravity only in 5-6, not in the Tier-A d-claims); single-threaded; references resolve. Is the completeness sweep (section 7) honest -- every other crack closed, the ONE residual (G1) named?'],
].map(([f]) => () => agent(
  `Hostile, high-precision review of v7 Paper 3 (the seal-spacing no-go) at ${P3}. Your focus: ${f}\nRead the paper, the plan ${PLAN}, Paper II ${P2}, and the sources paper4 ${P4}, paper6 ${P6}, paper57 ${P57}, paper-XI ${PXI} (esp. for faithfulness). Run the receipts ${R3} , ${R2B} , ${R2C} + your own sympy/mpmath. ${RULES}\nReturn the schema.`,
  { label: `P3:${f.slice(0, 28)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
