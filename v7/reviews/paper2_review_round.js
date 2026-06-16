export const meta = {
  name: 'review-v7-paper2-content-supply',
  description: 'Hostile review of v7 Paper 2 (the content supply), round 4 (CONFIRMING): verify the forced coboundary clock + the forced capacity ceiling d<=W_*; confirm the de-escalated centerpiece (s5 capacity-constant and s71-76 seal-firing vector law are DISTINCT & CONSISTENT, no corpus contradiction; only P-sat contradicted; firing root MODE-DEPENDENT) still reads clean end-to-end; and ADVERSARIALLY stress the NEW round-3 STRUCTURAL strengthening -- the claim that C(eta_B)=0.428 W_* is the SUPREMUM over admissible modes (monotone content + forced cochain unit lambda=1 + coupling-dilutes), the C->log2 bound, the sharpened s69 citation, and the kappa-blocking of the evidence clock. Confirm no manufactured contradiction NOR under-statement; pre-geometric, high-precision, single-threaded; hunt overclaims.',
  phases: [{ title: 'Review', detail: '3 referees on Paper 2' }],
}

const P2 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper2-content-supply.md'
const P1 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper1-record-click-law.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const P4 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper4-sealed-record-events-and-born-composition.md'
const REC = '/Users/felixrobles/workspace/isp/v7/code/p2a_content_supply.py'
const REC2 = '/Users/felixrobles/workspace/isp/v7/code/p2b_event_law_saturation.py'
const REC3 = '/Users/felixrobles/workspace/isp/v7/code/p2c_vector_ledger_roots.py'

const RULES = `
STANDING RULES to enforce:
- PRE-GEOMETRIC DISCIPLINE (load-bearing): every Tier-A claim must use NO spacetime, Lorentz, light cone, metric, interval s^2, or proper time. The only "time" is the commit order; the only state variable is the weight-0 KL content chi. FLAG any geometry leak.
- HIGH PRECISION: every numeric claim reproducible at mpmath dps>=100 / sympy-exact. RUN all THREE receipts: python3 ${REC} , python3 ${REC2} , python3 ${REC3} (if mpmath/sympy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python), plus your own checks. In particular re-derive INDEPENDENTLY: eta_A (C=J)=1.0903 & W_*=0.36478; the one-mode seal root eta_B (tanh eta = e^-eta)=0.6094 with C(eta_B)=0.1561; the COUPLED {x,y,xy} vector seal root h_*=0.4951 (grad psi(h)=exp(-h)) with C(h_*)=0.1090; confirm BOTH seal contents < W_*.
- SINGLE-THREADED: the paper reads written-once. FLAG "previously / we now / earlier version / corrected / round N / campaign / version N" (a bare date stamp is allowed).
- HONESTY / FORBIDDEN OVERCLAIMS (the central ones for this round): (a) the paper must NOT claim d=W_* is FORCED -- only d<=W_* (the capacity CEILING) is forced. (b) DE-ESCALATION CHECK (both directions): the paper now claims paper4 s5 (capacity constant eta_A) and s71-76 (seal-firing vector law) are DISTINCT & MUTUALLY CONSISTENT -- NO contradiction within the corpus -- and that ONLY the postulate (P-sat) "seal at capacity" is contradicted (by the sub-capacity firing law). VERIFY this is FAITHFUL to paper4 s5/s7/s71-76 and NOT (i) manufacturing a corpus contradiction, NOR (ii) UNDER-stating: is it right that s5 fixes a structural constant (s7: single diamond 'has no memory, no previous/next diamond') while s71-76 is the firing law? Is 'contradicts (P-sat)' correctly scoped (P-sat IS a fire-at-capacity statement, so a sub-capacity firing law does contradict it), and is it never sloppily widened to 'contradicts s5/the corpus'? (c) MODE-DEPENDENCE: the paper says the firing root is mode-dependent (eta_B one-mode-parity slice, h_*=0.495 coupled) and leads with the INEQUALITY 'committed content < W_* in every mode' rather than a magic number. Is that honest and is the inequality robust (check both modes)? Is calling eta_B 'the one-mode-parity slice, not the canonical root' correct? (d) THREE OBJECTS: tilt eta_B vs random evidence I~Exp(1) (mean 1) vs DETERMINISTIC content C(eta_B)=0.156 -- confirm the paper no longer mislabels C(eta_B) as 'a random Poisson variable'. (e) s69: the paper cites s69 as finding a FIXED-CONTENT threshold non-canonical (selected eta drifts with shape/unit). Is that faithful to s69? (f) increment MAGNITUDE physical, kappa the one no-go floor; ceiling d<=W_* justified by monotone-opposition + named no-over-sat premise; coboundary form grounded with form-vs-identification honest; no geometric content as Tier-A.
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
    pre_geometric_violations: { type: 'array', items: { type: 'string' } },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    new_paths_opened: { type: 'array', items: { type: 'string' }, description: 'genuinely new issues/paths (investigated before the next round)' },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['The FORCED results: (Q1) dchi = coboundary h_{i+1}-h_i (telescope; discrete Poincare lemma / Paper I odometer / corpus coboundary law) -- is the FORM genuinely forced, and is the form-vs-identification distinction (s2: lemma forces a coboundary of SOME potential; identifying it with the holonomy cochain is the physical layer) honest? (Q2) W_* is a forced CAPACITY: C(eta) rises, J(eta)=sech^2 falls, single crossing at eta_A, W_*=max_eta min(C,J)=0.36478..., and the named no-over-saturation premise => d<=W_* forced. RUN p2a and re-derive the monotonicity + single-crossing + the max-min identity independently at dps>=100. Is the d<=W_* ceiling airtight given its named premise (and the single-channel reduction of min(C,J), credited to Paper I s3.1)?'],
  ['Honesty & scope of the DE-ESCALATED framing: (1) is the claim "s5 (eta_A capacity constant) and s71-76 (seal-firing vector law) are DISTINCT & MUTUALLY CONSISTENT, no corpus contradiction" faithful and correctly stated -- NOT manufacturing a contradiction, NOT under-stating? (2) is "only (P-sat) is contradicted" correctly scoped (never widened to "s5/corpus is contradicted")? (3) is the THREE-OBJECTS distinction clean (tilt eta_B / random evidence I~Exp(1) mean 1 / DETERMINISTIC content C(eta_B)=0.156 -- no longer mislabeled "random Poisson variable")? (4) is the s69 citation (fixed-content threshold non-canonical) faithful? Plus: d<=W_* tagged FORCED-given-no-over-saturation; d=W_* NOT forced; magnitude PHYSICAL; kappa no-go floor; pre-geometric; single-threaded; references (incl. p2c). Confirm no overclaim of closure.'],
  ['ADVERSARIAL on the NEW round-3 STRUCTURAL strengthening -- the SUPREMUM claim. The paper now claims (s3.3, abstract, s7) that C(eta_B)=0.428 W_* is the SUPREMUM over admissible (complete-ledger) modes, via: (a) seal content C(eta) MONOTONE increasing in the coefficient (C\\u2032=eta sech^2 eta>0); (b) reaching content W_* needs coefficient eta_A, attainable only at cochain unit lambda~0.208<1 (inadmissible under-count, same argument that rejects lambda=2); (c) coupling more modes only DILUTES (h_*=0.495<eta_B=0.609). STRESS HARD: RUN p2c (now 24 checks incl. a SUPREMUM SCAN over ledgers (x,y),(x,xy),(y,xy),(x,y,xy)). Then INDEPENDENTLY try to BREAK the supremum: solve grad psi(h)=exp(-h) for OTHER complete ledgers on {+-1}^2 or {+-1}^3 (asymmetric couplings, more statistics) and check whether ANY per-mode coefficient EXCEEDS eta_B (=> C would exceed C(eta_B), breaking the sup). Is "supremum over admissible modes" airtight, or only "sup over the ledgers checked"? Also verify the C->log2 bound, the lambda~0.208 number, and that coupling always dilutes. If the sup is not provably universal, the paper should say "sup over the complete ledgers exhibited" not "over admissible modes". Deliver the sharpest correct statement of the robustness.'],
].map(([f]) => () => agent(
  `Hostile, high-precision review of v7 Paper 2 (the content supply) at ${P2}. Your focus: ${f}\nRead the paper, the plan ${PLAN}, Paper I ${P1}, the source paper4 ${P4} (esp. s5, s7, s69-76 VERBATIM), and the receipts ${REC} , ${REC2} , ${REC3} (run them + your own sympy/mpmath). ${RULES}\nReturn the schema.`,
  { label: `P2:${f.slice(0,30)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
