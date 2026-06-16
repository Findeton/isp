export const meta = {
  name: 'review-v7-paper1-clicklaw',
  description: 'Hostile review of v7 Paper 1 (the record click-law): verify the Tier-A derivation at high precision, enforce the pre-geometric discipline, hunt overclaims, check single-threaded style, surface any hidden geometric assumption or any way the "forced" claim fails.',
  phases: [{ title: 'Review', detail: '3 referees on Paper 1 v7' }],
}

const P1 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper1-record-click-law.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const P4 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper4-sealed-record-events-and-born-composition.md'
const P56 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper56-indivisible-gravitational-channel.md'
const F3 = '/Users/felixrobles/workspace/isp/v7/code/f3_self_consistency.py'

const RULES = `
STANDING RULES to enforce:
- PRE-GEOMETRIC DISCIPLINE (the load-bearing one): the Tier-A claims must use NO spacetime, NO Lorentz frame, NO light cone, NO metric, NO interval s^2, NO proper time. The only "time" allowed at Tier A is the commit order; the only state variable is the record-internal KL content chi. FLAG any place a geometric notion sneaks into a Tier-A claim. Geometric constraints are allowed ONLY in Tier B (the conditional "if spacetime emerges, then ..." regime).
- HIGH PRECISION: every numeric claim reproducible at mpmath dps>=100 / sympy-exact. You MAY (and should) run the receipts: python3 ${F3}, python3 v7/code/f3b_sparse_seal_shape.py, python3 v7/code/f3c_sequential_odometer.py (if mpmath/sympy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python), plus your own checks.
- CONFIRMING ROUND (verify the now-integrated claims; run all receipts f3, f3b, f3c, f3d, f3e). Specifically: (1) the dense step now names BOTH premises — dense seals AND "survival a function of accumulated content alone = a single scalar channel supplied by the q=2 one-contrast screen of §3.1" (receipt f3e shows a multi-channel screen breaks multiplicativity, gap 0.317) — verify this is correct and complete, not still hiding a premise. (2) the seal⟺composition bridge is a forced kinematic IDENTITY (CK-defect = interference cross-term entrywise, f3d ~1e-142), ingredients Tier-A-forced by §3.1, intrinsic supply split (Tier-A-rate / Tier-B-placement) outside the forcing chain. (3) collar Markov-presentability FORCED (paper10 T3+T4); Markov(collar)/non-Markov(seal-order) consistent. (4) odometer: dchi>=0 unconditional, additivity forced given chi:=accumulated sigma. (5) sparse skeleton S(nd)=S(d)^n + free profile (f3b). This is intended as the TERMINAL round: report whether any LOAD-BEARING issue remains, or only cosmetic/future-paper items. Flag any overstatement, geometry leak, or single-threaded slip.
- SINGLE-THREADED STYLE: the paper must read written-once. FLAG "previously / we now / earlier version / corrected / round / campaign / version N" (a bare date stamp is allowed).
- HONESTY: hunt OVERCLAIMS. The paper must claim ONLY what is FORCED. Forbidden overclaims: (a) claiming kappa (the one free scale) is fixed; (b) claiming the content increment d chi is derived (it is OPEN); (c) claiming the entanglement correlation is derived (OPEN); (d) claiming gravitational sealing is genuinely indivisible / sparse (OPEN); (e) presenting ANY geometric/relativistic content as a Tier-A axiom rather than a Tier-B conditional consequence; (f) claiming S=exp(-kappa chi) is forced without the Cauchy-equation + content-additivity(cocycle) + monotonicity premises stated.
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['focus', 'verdict', 'must_fix', 'overclaims', 'math_or_claim_errors', 'pre_geometric_violations', 'single_threaded_violations', 'new_paths_opened', 'summary'],
  properties: {
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue','where','severity','fix'], properties: { issue:{type:'string'}, where:{type:'string'}, severity:{type:'string',enum:['minor','major','critical']}, fix:{type:'string'} } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    math_or_claim_errors: { type: 'array', items: { type: 'string' }, description: 'each with the high-precision check you ran and its residual' },
    pre_geometric_violations: { type: 'array', items: { type: 'string' }, description: 'any place a Tier-A claim secretly uses geometry/spacetime' },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    new_paths_opened: { type: 'array', items: { type: 'string' }, description: 'genuinely new issues or investigation paths (these get investigated before the next review round)' },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['The Tier-A derivation: (3.1) seal=orthogonal projection from q=2 screen-isometry; (3.2) self-consistency under refinement = the Cauchy multiplicative equation -> S(chi)=exp(-kappa chi) UNIQUELY, p=1-only, content-additivity from the cocycle; (3.3) no-revival structural; (3.4) one free scale kappa. RUN f3_self_consistency.py and independently re-derive the Cauchy-equation uniqueness and the p=1-only check at high precision. Is each claim genuinely FORCED, or is a premise hidden/unstated?'],
  ['The PRE-GEOMETRIC discipline and the two-tier separation: does the paper EVER let a geometric notion (metric, s^2, Lorentz, light cone, proper time, locality) into a Tier-A claim? Is the Tier-A/Tier-B boundary clean? Is the entanglement guardrail (3.5) correctly stated as a SEPARATE Tier-A correlation that the sequential multiplicative law neither forces nor forbids (and is it honestly OPEN)? Is the residue (5: content-increment supply, entanglement, sparsity) honestly OPEN, not quietly claimed?'],
  ['The Tier-B conditional limit (4: exp/Gaussian as one law under reparametrization; X/XI as the spacetime limit; the shared single scale kappa), single-threaded style, the references, and an ADVERSARIAL hunt: find any way the "forced" claim of S=exp(-kappa chi) could FAIL (non-measurable solutions of Cauchy? a non-additive content? a seal that is not a refinement point? a revival that IS a seal?), and any overclaim across the whole paper.'],
].map(([f]) => () => agent(
  `Hostile, high-precision review of v7 Paper 1 (the record click-law) at ${P1}. Your focus: ${f}\nRead the paper, the plan ${PLAN}, the source paper4 ${P4} and paper56 ${P56}, and the receipt ${F3} (run it + your own sympy/mpmath). ${RULES}\nReturn the schema.`,
  { label: `P1:${f.slice(0,30)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
