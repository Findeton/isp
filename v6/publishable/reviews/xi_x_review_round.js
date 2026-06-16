export const meta = {
  name: 'review-X-and-XI',
  description: 'Hostile review of publishable Paper X (decoherence undecidability) and Paper XI (sealed-record gravity no-go): verify all load-bearing math at high precision, hunt overclaims, enforce single-threaded discipline, surface anything missed.',
  phases: [
    { title: 'ReviewX', detail: '3 referees on Paper X' },
    { title: 'ReviewXI', detail: '3 referees on Paper XI' },
  ],
}

const X = '/Users/felixrobles/workspace/isp/v6/publishable/paper-X-gravitational-decoherence.md'
const XI = '/Users/felixrobles/workspace/isp/v6/publishable/paper-XI-sealed-record-gravity-no-go.md'
const SRC56 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper56-indivisible-gravitational-channel.md'
const SRC57 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md'
const VIII = '/Users/felixrobles/workspace/isp/v6/publishable/paper-VIII-horizons.md'
const RX = '/Users/felixrobles/workspace/isp/code/v6_pX_decoherence_undecidability_receipts.py'
const RXI = '/Users/felixrobles/workspace/isp/code/v6_pXI_sealed_record_gravity_nogo_receipts.py'

const RULES = `
STANDING RULES you must enforce:
- SINGLE-THREADED STYLE: the paper must read as written-once. FLAG any phrase that narrates the corpus's own editorial history or versions: "previously", "we now", "in an earlier version", "corrected", "round", "campaign", "updated", "asserted-then-proven", "version N". A bare date stamp is allowed.
- HIGH PRECISION: every numeric claim must be reproducible at mpmath dps>=80 / sympy-exact. You may RUN the receipt script and/or your own sympy/mpmath checks to verify. Float64 is not acceptable for modular-kernel / near-vacuum / small-argument / cancellation-heavy quantities.
- HONESTY: hunt OVERCLAIMS. The papers must NOT claim more than is proved. Specifically check the forbidden overclaims listed per paper.
`

const SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['paper', 'focus', 'verdict', 'must_fix', 'overclaims', 'math_or_claim_errors', 'single_threaded_violations', 'missed_or_new', 'summary'],
  properties: {
    paper: { type: 'string' },
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue', 'where', 'severity', 'fix'], properties: {
      issue: { type: 'string' }, where: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'major', 'critical'] }, fix: { type: 'string' } } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    math_or_claim_errors: { type: 'array', items: { type: 'string' }, description: 'each with the high-precision check you ran and its residual' },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    missed_or_new: { type: 'array', items: { type: 'string' }, description: 'anything missed, or a genuinely new issue/path' },
    summary: { type: 'string' },
  },
}

const X_FORBIDDEN = `Forbidden overclaims for Paper X (flag if present): (a) claiming the sealed-record/indivisible ontology is the UNIQUE mechanism (undecidability must cut both ways); (b) claiming the gravitational record process IS indivisible (must be OPEN); (c) claiming any OBSERVABLE non-Markovian fingerprint of indivisibility exists (ruled out for committed seals); (d) claiming the functor discharges the gravitational obligation (it is kinematic-only, for a chosen projective seal model); (e) deriving GR/graviton/Born from nothing.`
const XI_FORBIDDEN = `Forbidden overclaims for Paper XI (flag if present): (a) claiming to derive Newton's G (it is a NO-GO); (b) claiming a propagating graviton / quantum spin-2 charge (OBSTRUCTED, distinct from the derived equation); (c) claiming the real-time/radiative DYNAMICS of gravity (OPEN, emergent-continuum frontier); (d) claiming a covariant interacting-FIELD dynamics; (e) writing the two invariants as a chained numerical equality kappa*sigma_A = G*Lambda^2 (they are SEPARATE weight-0 invariants, NOT numerically equal); (f) stating the Einstein FORM as unconditional (it is modulo axiom R + theta=sigma=0 + focusing gate); (g) re-deriving the temperature from scratch (it must CITE the horizon paper VIII, not duplicate it).`

phase('ReviewX')
const xReviews = await parallel([
  ['the three core theorems (Gaussian-onset non-signature; CP-divisibility of irreversible sealing; the all-orders operational undecidability) — verify each at high precision by running the receipt and your own sympy/mpmath',],
  ['the conceptual frame (three orthogonal senses of Markovian; CP-divisibility vs Barandes-indivisibility independence; the functor as kinematic-only; the DP-kernel demotion) and honesty/scope',],
  ['the observability ledger, the experimental-bounds claims, the references, single-threaded discipline, and an adversarial hunt for any way the reduced channel COULD certify the mechanism after all',],
].map(([f]) => () => agent(
  `Hostilely review publishable Paper X at ${X}. Your focus: ${f}.\nRead the paper, its source ${SRC56}, and the receipt ${RX} (you may RUN it: \`python3 ${RX}\`). ${RULES}\n${X_FORBIDDEN}\nReturn the schema with paper="X".`,
  { label: `X:${f.slice(0,28)}`, phase: 'ReviewX', schema: SCHEMA }
)))

phase('ReviewXI')
const xiReviews = await parallel([
  ['the no-go spine (weight map, gate G1, SIGMA-SPLIT, the two separate invariants, the de Sitter weight-twin, every lever) — verify at sympy-exact / mpmath dps>=100 by running the receipt and your own checks; try hard to BREAK the no-go',],
  ['the derived equation of state (temperature-cited-from-VIII seam, geometry-universal, pure-area Wald, the nonlinear Clausius form, the null-cone lemma and its CORRECT timelike statement, the gates) — verify the math and that the gates are stated everywhere the DERIVED tag appears',],
  ['the spin-2 equation-vs-charge distinction, the QCD/dimensional-transmutation connection, the open frontiers (emergent vs intrinsic graviton; real-time dynamics), honesty/scope, single-threaded discipline, and the VIII seam (no duplication)',],
].map(([f]) => () => agent(
  `Hostilely review publishable Paper XI at ${XI}. Your focus: ${f}.\nRead the paper, its source ${SRC57}, the horizon paper it cites ${VIII}, and the receipt ${RXI} (you may RUN it: \`python3 ${RXI}\`). ${RULES}\n${XI_FORBIDDEN}\nReturn the schema with paper="XI".`,
  { label: `XI:${f.slice(0,28)}`, phase: 'ReviewXI', schema: SCHEMA }
)))

return { xReviews, xiReviews }
