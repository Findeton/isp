export const meta = {
  name: 'review-v7-paper6-transverse-almost-quantum',
  description: 'Hostile review of v7 Paper VI (the transverse entangling content is free up to the almost-quantum set Q-tilde; Tsirelson inherited): verify the no-go spine (any record self-consistency principle = moment-positivity at level 1+AB => lands on Q-tilde = Q^{1+AB}, NECESSARY-not-sufficient: reproduces no-signaling + Tsirelson 2sqrt2 + PR-box exclusion, but strictly overshoots Q on I3322); the one-name diagnosis (the missing input is uniquely the global tensor product / local tomography K_AB=K_A*K_B, the complex-over-real selector, the seal blind to it: E=E^2=E* over R and C, rebit foil deficit 1); the positive corollary (Tsirelson INHERITED as a bound via the static IC core: KL non-neg + no-signaling-consistency + DPI + chain-rule residual 3.6e-122; facet saturates at E=1/sqrt2; ONE operational lever short of full IC, NOT pinned). RUN all 3 receipts. Hunt overclaims BOTH directions (must NOT claim Q-tilde=Q, derive complex QT / local tomography / tensor product, or derive IC in full; must correctly credit the envelope + Tsirelson-inherited). Pre-geometric (no tensor product/Hilbert arena smuggled as INPUT -- its absence IS the result), single-threaded, high precision, faithfulness to NGHA 2015 / NPA / Tsirelson / Pawlowski IC / Hardy / Wootters / CDP / Barandes and to companion Papers I/III/IV.',
  phases: [{ title: 'Review', detail: '3 referees on Paper VI' }],
}

const P6 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper6-transverse-almost-quantum.md'
const P1 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper1-record-click-law.md'
const P3 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper3-seal-spacing-no-go.md'
const P4 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper4-entanglement-graph-not-metric.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const T1 = '/Users/felixrobles/workspace/isp/v7/code/t1_npa_q_vs_qtilde.py'
const T2 = '/Users/felixrobles/workspace/isp/v7/code/t2_purification_uniqueness.py'
const T3 = '/Users/felixrobles/workspace/isp/v7/code/t3_tsirelson_derivation.py'

const RULES = `
STANDING RULES to enforce:
- PRE-GEOMETRIC DISCIPLINE: every quantity must be a record-internal probability / KL / moment of the transition law. NO spacetime / metric / Hilbert TENSOR PRODUCT used as a derivation INPUT. The tensor product / local tomography appears ONLY as the thing that CANNOT be supplied (the no-go). FLAG any global Hilbert tensor arena, or an a-priori bipartite state space, smuggled in as a premise rather than derived/absent. The chains must meet ONLY via the shared joint moment <A_x B_y> (commutation on the state), never a tensor factorization -- verify the paper holds this line.
- HIGH PRECISION: every numeric claim reproducible at mpmath dps>=100 / SDP. RUN all three receipts: python3 ${T1} , ${T2} , ${T3} (if cvxpy/mpmath missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python), plus your own checks. Re-derive: the NPA-1 CHSH ceiling = 2sqrt2 (gap ~2.8e-10) and PR-box infeasible (t1); local tomography K_AB=K_A*K_B holds for complex (16=4*4) and FAILS for real (10!=9, deficit 1) and the seal field-blindness E=E^2=E* over R and C (t2); the static IC core (KL non-neg, I=0 iff product, DPI, chain rule residual 3.6e-122) and the IC facet V(E)=E^2-1/2 saturating at E=1/sqrt2 (t3).
- SINGLE-THREADED: reads written-once. FLAG 'previously / we now / earlier version / corrected / round N / campaign / version N' (a bare date stamp is allowed).
- HONESTY / OVERCLAIM HUNT (BOTH directions):
  (a) MANUFACTURED POSITIVE: the paper must NOT claim it DERIVES complex quantum theory, local tomography, or the tensor product from the records (it proves their ABSENCE is the obstruction); must NOT claim Q-tilde = Q (the gap is strict + permanent); must NOT claim chi_AB is pinned/forced (it is FREE up to Q-tilde); must NOT claim Information Causality is derived IN FULL (only its static functional core, one operational RAC lever short). CHECK each is correctly disavowed in sec 7.
  (b) UNDER-STATEMENT: the paper must correctly CREDIT what the substrate DOES fix -- the whole Paper IV envelope (no-signaling + Tsirelson + PR-box exclusion) as NECESSARY, and Tsirelson as an INHERITED bound (not merely "consistent with"). Is "necessary-not-sufficient" the right strength? Is "Tsirelson inherited as a bound" correctly NOT overstated to "pinned" and correctly NOT understated to "assumed"?
  (c) THE NO-GO FAITHFULNESS: is "any record self-consistency principle is a moment-positivity condition at level 1+AB" genuinely the only arena the records provide (is there a self-consistency principle the substrate could host that is NOT a 1+AB moment condition -- e.g. one reaching a higher NPA level, or a non-moment functional)? Is the feasible set genuinely Q-tilde = Q^{1+AB} (faithful to NGHA 2015)? Is "necessary" (Q subseteq Q-tilde, envelope reproduced) AND "not sufficient" (Q-tilde strictly contains Q, I3322 needs level >=4) both correct and correctly sourced?
  (d) THE ONE-NAME: is the missing input genuinely AND uniquely the global tensor product / local tomography (not something else, e.g. a purification or a positivity axiom)? Is the seal field-blindness genuine (E=E^2=E* really hold identically over R and C; is the rebit really a foil with same marginals + same Tsirelson but different chi_AB)? Is "two faces of one obstruction" (moment-matrix form vs state-space form) honest?
  (e) THE FIFTH-WALL FRAMING: is "same shape as the l_step / scale no-go" (Paper III) faithful -- self-consistency fixes the envelope, never the last record-blind input (there a length, here the tensor product)? Or is the analogy strained?
- FAITHFULNESS to sources: NGHA 2015 (Q-tilde definition), NPA hierarchy, Tsirelson, Pawlowski et al IC, Hardy (local tomography axiom), Wootters (rebit), Chiribella-D'Ariano-Perinotti (purification/local tomography), Barandes; and companion Paper I (forced single-chain law), Paper III (the grading no-go / fifth-wall shape), Paper IV (the joint click-law, chi_AB the free complement, E_cl). Read them.
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['focus', 'verdict', 'must_fix', 'overclaims', 'math_or_claim_errors', 'pre_geometric_violations', 'single_threaded_violations', 'new_paths_opened', 'summary'],
  properties: {
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue', 'where', 'severity', 'fix'], properties: { issue: { type: 'string' }, where: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'major', 'critical'] }, fix: { type: 'string' } } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    math_or_claim_errors: { type: 'array', items: { type: 'string' } },
    pre_geometric_violations: { type: 'array', items: { type: 'string' } },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    new_paths_opened: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['THE NO-GO SPINE (secs 2-3). Is "any transverse self-consistency principle the record substrate can host is a moment-positivity condition at level 1+AB" FAITHFUL and EXHAUSTIVE -- is there any self-consistency principle the substrate could express that is NOT a 1+AB moment condition (a higher-NPA-level balance, a non-moment functional, a purification-based closure)? If so the no-go is scoped wrong. RUN t1. Re-derive: the NPA-1 CHSH ceiling = 2sqrt2 (gap ~2.8e-10), PR-box (CHSH=4) INFEASIBLE, the sharp boundary (just past 2sqrt2 infeasible), the chains meeting via <A_x B_y> commutation ON THE STATE not a tensor product. Is the feasible set genuinely Q-tilde = Q^{1+AB} (NGHA 2015)? Is the NECESSARY half (Q subseteq Q-tilde, envelope reproduced) right? Is the NOT-SUFFICIENT half (Q-tilde strictly contains Q; I3322 separates them; needs NPA level >=4) correct and correctly attributed? Is "chi_AB free within Q-tilde, the gap permanent" honest?'],
  ['THE ONE-NAME + THE TSIRELSON POSITIVE (secs 4-5). RUN t2 + t3. (4) Is the missing input genuinely AND uniquely the global tensor product / local tomography K_AB=K_A*K_B (verify complex 16=4*4 holds, real 10!=9 deficit 1)? Is the record seal genuinely BLIND to it (E=E^2=E* hold IDENTICALLY over R and C; the rebit foil = same marginals + same Tsirelson 2sqrt2 but different chi_AB)? Is "two faces of one obstruction" (moment-matrix Q-tilde vs state-space local-tomography) honest, or are they actually different claims? (5) Is Tsirelson genuinely INHERITED -- does the record KL really have all four IC properties (non-neg, I=0 iff product, DPI, chain rule residual 3.6e-122), and does the facet V(E)=E^2-1/2 really saturate at exactly E=1/sqrt2 (CHSH=2sqrt2)? Is "inherited as a BOUND, not pinned" correct (the bound is field-blind, rebit saturates too)? Is "one operational RAC lever short of full IC" honest (the static substrate present but the operational protocol NOT forced by the seal-law, t3 check 3b)?'],
  ['OVERCLAIM HUNT BOTH directions + discipline + faithfulness (secs 1,6,7,8). (a) Does the paper AVOID claiming it derives complex QT / local tomography / the tensor product, AVOID Q-tilde=Q, AVOID pinning chi_AB, AVOID deriving IC in full? Confirm each disavowal in sec 7. (b) Does it correctly CREDIT the envelope (necessary) + Tsirelson (inherited) without under-stating? Is "necessary-not-sufficient" the right strength label? (c) THE FIFTH-WALL framing (sec 6): is "same shape as the l_step/scale no-go" (Paper III) faithful (self-consistency fixes the envelope, never the last record-blind input -- there a length, here the tensor product), or strained? (d) Pre-geometric discipline: is any global Hilbert tensor arena / a-priori bipartite state space smuggled in as INPUT (it must be ABSENT = the result)? Single-threaded? Do the references resolve and is the citation of NGHA 2015 (Q-tilde), NPA, Tsirelson, Pawlowski IC, Hardy, Wootters (rebit), CDP, Barandes, and Papers I/III/IV faithful? Hunt any remaining overclaim or unfaithful citation.'],
].map(([f]) => () => agent(
  `Hostile, high-precision review of v7 Paper VI (the transverse entangling content is free up to the almost-quantum set) at ${P6}. Your focus: ${f}\nRead the paper, the plan ${PLAN}, and companion Papers I ${P1}, III ${P3}, IV ${P4}. Run the receipts ${T1} , ${T2} , ${T3} + your own SDP/sympy/mpmath checks. ${RULES}\nReturn the schema.`,
  { label: `P6:${f.slice(0, 24)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
