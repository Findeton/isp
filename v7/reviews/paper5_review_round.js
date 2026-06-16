export const meta = {
  name: 'review-v7-paper5-cm-free-calibration',
  description: 'Hostile review of v7 Paper 5 (the c_m free-calibration result), round 3 (CONFIRMING): verify the round-2 fixes -- (1) the WINDOW claim is REMOVED (the toy record-gap m̂ in nats does NOT bound the physical c_m=1.75e-45, which sits ~44 orders below; this now reinforces "awaits the matter sector" rather than constraining c_m); (2) the nu_m/m̂ relabel is CORRECT (c_m = m̂ = gamma_G*nu_m^2 the content/coupling; nu_m = sqrt(m̂/gamma_G) the mass-amplitude; the two on different axes, not conflated); (3) the §3 blindness leans only on the G1-FREE sub-results (EP theorem + algebraic c_m-independence), not the pinned-sector Thm 6.1; (4) receipt label fixed. Confirm the thesis (weight-0/permitted; gravity-blind; currently free; shares d-s mode-canonicalization gate; not pinned) is clean end-to-end -- faithfulness, no overclaim BOTH directions, pre-geom, high precision, single-threaded.',
  phases: [{ title: 'Review', detail: '3 referees on Paper 5' }],
}

const P5 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper5-cm-free-calibration.md'
const P3 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper3-seal-spacing-no-go.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const P6 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper6-arec-gauge-closure-v6.1.md'
const P7 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper7.md'
const P57 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md'
const PXI = '/Users/felixrobles/workspace/isp/v6/publishable/paper-XI-sealed-record-gravity-no-go.md'
const R5 = '/Users/felixrobles/workspace/isp/v7/code/p5_cm_calibration.py'
const R2C = '/Users/felixrobles/workspace/isp/v7/code/p2c_vector_ledger_roots.py'
const R3 = '/Users/felixrobles/workspace/isp/v7/code/p3_d_nogo.py'

const RULES = `
STANDING RULES to enforce:
- HIGH PRECISION: every numeric claim reproducible at mpmath dps>=60 (CODATA SI) / sympy-exact. RUN the receipts: python3 ${R5} , ${R2C} , ${R3} (if mpmath/sympy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python), plus your own checks. Re-derive: c_m(e)~1.75e-45, c_m(p)~5.9e-39, c_m=(m/M_Planck)^2, c_m∝m^2; weight(c_m)=+2+2(-1)-0=0 and gauge invariance under l->mu*l; eta_B=0.609 vs h_*=0.495 (mode-dependent gap).
- FAITHFULNESS (load-bearing -- this paper leans on the v6 corpus): (a) Thm 6.1 / paper7 -- does the corpus genuinely prove the gravity sector is COMPLETE-AND-BLIND to c_m (c_m = the matter ledger's spectral gap, no gravity identity constrains it, 'exactly as the Einstein equations do not determine the electron mass')? READ paper7. (b) the toy-value NOT-SELECTED (paper6 s9: c_m=12 and c_m=1200 both pass kappa*sigma_A/2pi=1) -- faithful? (c) c_m weight-0 / intrinsic-eligible and the H1(EP)/H2(hierarchy) gate framing (paper6 s9, paper57, paperXI) -- faithful? (d) the spectral action lands on G*Lambda^2 not c_m -- faithful?
- HONESTY / OVERCLAIM HUNT (BOTH directions):
  (a) MANUFACTURED DERIVATION: the paper must NOT pin a c_m VALUE, must NOT claim the hierarchy H2 is solved, must NOT present any record number (gamma_G*eta_B^2=0.093, theta_B^2, 1/eta_B) as c_m. CHECK the illustrative 0.093 is clearly flagged 'NOT a prediction' and the numerology is refuted algebraically.
  (b) UNDER-STATEMENT / mis-scoping: c_m must be correctly PERMITTED (weight-0, the no-go does NOT forbid it) and a FREE CALIBRATION (the gravitational analog of the no-go floor kappa) -- NOT mislabeled a 'third no-go' (it is not forbidden, only not-gravity's-to-give). Is 'complete-and-blind' correctly distinguished from 'forbidden'? Is the SHARED-bottleneck-with-d claim (both reduce to matter sector + mode canonicalization) correct and not overstated?
  (c) GATE G1: the package rests on G1 (same scope premise as the scale no-go) -- is that disclosed?
- PRE-GEOMETRIC: c_m is weight-0 (a ratio of record numbers); the gravitational constants (G, hbar, c, masses, Lambda) enter ONLY to exhibit the hierarchy and confirm the weight bookkeeping, where the POINT is gravity cannot output c_m. FLAG any claim that treats c_m as a Tier-A pre-geometric primitive without the matter sector.
- SINGLE-THREADED: reads written-once. FLAG 'previously/we now/earlier version/corrected/round N/campaign/version N' (a bare date stamp is allowed).
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['focus', 'verdict', 'must_fix', 'overclaims', 'math_or_claim_errors', 'faithfulness_violations', 'single_threaded_violations', 'new_paths_opened', 'summary'],
  properties: {
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue', 'where', 'severity', 'fix'], properties: { issue: { type: 'string' }, where: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'major', 'critical'] }, fix: { type: 'string' } } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    math_or_claim_errors: { type: 'array', items: { type: 'string' } },
    faithfulness_violations: { type: 'array', items: { type: 'string' }, description: 'claims about paper6/7/57/XI that are NOT supported by those texts' },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    new_paths_opened: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['THE THESIS (sections 1-4): is c_m correctly (i) weight-0/intrinsic-eligible (RUN p5: weight=0, gauge-invariant; the no-go does NOT forbid it), and (ii) provably NOT a gravity output via the complete-and-blind theorem? READ paper7 -- does it genuinely prove gravity is blind to c_m (= matter ledger spectral gap, "as Einstein eqs do not fix m_e")? Is the toy-value NOT-SELECTED (paper6 s9, c_m=12/1200 both pass) faithful and correctly used as the proof of CURRENT FREEDOM? Is "free calibration = strength-axis analog of the no-go floor kappa" the right characterization (NOT a third no-go, NOT derivable-now)?'],
  ['THE FACTORIZATION + SHARED GATE (sections 5-6) + numerics: is c_m=gamma_G*nu_m^2 correct (gamma_G area-norm/convention, nu_m matter gap, both weight-0)? Is the UNIFICATION claim -- c_m and the spacing d reduce to the SAME open obligation (matter sector + mode canonicalization, nu_m mode-dependent eta_B vs h_*) -- correct and not overstated? RUN p5/p2c: re-derive eta_B=0.609, h_*=0.495 independently. Are the requirements (matter sector ABSENT, EP/H1 proved-conditional, spectral action lands on G*Lambda^2 not c_m) faithful to paper6 s9 / paper7 / paper57? Is "beyond all current corpus technology" honestly conveyed?'],
  ['OVERCLAIM HUNT BOTH directions + discipline (sections 7-8): (a) does the paper AVOID pinning a c_m value / claiming H2 solved? Confirm the illustrative 0.093 is flagged NOT-a-prediction and the theta_B^2/Srednicki numerology is refuted ALGEBRAICALLY (cubic irreducible). (b) Does it AVOID under-stating -- c_m correctly PERMITTED/weight-0 (not a third no-go), correctly FREE (not a hidden hole in gravity)? Is "complete-and-blind" cleanly distinguished from "forbidden"? (c) Is gate G1 disclosed as the load-bearing scope premise? (d) pre-geometric discipline (c_m a weight-0 ratio; gravity constants only for hierarchy/bookkeeping; no treating c_m as a built Tier-A primitive); single-threaded; references resolve. Hunt any remaining overclaim.'],
].map(([f]) => () => agent(
  `Hostile, high-precision review of v7 Paper 5 (the c_m free-calibration result) at ${P5}. Your focus: ${f}\nRead the paper, the plan ${PLAN}, Paper III ${P3}, and the sources paper6 ${P6}, paper7 ${P7}, paper57 ${P57}, paper-XI ${PXI} (for faithfulness -- esp. Thm 6.1 in paper7 and s9 in paper6). Run the receipts ${R5} , ${R2C} , ${R3} + your own sympy/mpmath. ${RULES}\nReturn the schema.`,
  { label: `P5:${f.slice(0, 26)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
