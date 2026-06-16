export const meta = {
  name: 'review-v7-paper7-covariance-round2-confirming',
  description: 'Round-2 CONFIRMING review of v7 Paper VII (covariant decoherence) verifying the round-1 fixes hold and opened no new defect. FIX 1 (was MAJOR, faithfulness): the statevector wall is no longer mis-attributed to Fedida as PROVING unitary-inequivalence; it is re-attributed to the HAAG obstruction (unitary inequivalence of interacting reps; TS equation invalid in d>2), with Fedida 2025 correctly cited for its POSITIVE Einstein-causality result (spacelike commutation / no-signalling) derived ASSUMING the equivalence -- corroborating the sec-4 spacelike-microcausality side, NOT proving the wall. Confirm sec6/abstract(iii)/sec7-claim(4)/refs now attribute correctly. FIX 2 (was minor): "reproduces the GDC recursion / inherits verbatim" downgraded to "reproduces the locality<=>spacelike-commutation HINGE on which the GDC recursion turns" (single point-local density => higher orders vanish trivially once order-1 does; the all-orders recursion is borrowed not re-derived). FIX 3 (minor scoping): only the MICROCAUSALITY half is inherited; the GDC finite-energy RATE additionally needs normal-ordering SHARD lacks. FIX 4 (minor): kernel "supplied OUTRIGHT" -> "supplied at TIER B" (f(s^2) is a Tier-B object); positive-type is SHARD strengthening (GDC needs only finite heating); the +2.78e-9 is a finite-SAMPLE certificate, positivity exact-by-Bochner. FIX 5 (minor): B=B1xB2 -- B2 discharged MODULO the sec-4 point-local premise (B1 unconditional shared Haag wall; B2 conditional). FIX 6 (minor): GDC reference title corrected (was a fabricated descriptive title). RUN c1/c2. Final sweep: overclaims BOTH directions, the conditional-positive grade, pre-geometric (Lorentz EMERGENT-only), single-threaded, faithfulness to GDC 2507.06954 / Haag / Fedida 2506.14693 / Tumulka / GRW-CSL.',
  phases: [{ title: 'Review', detail: '3 referees confirming Paper VII fixes' }],
}

const P7 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper7-covariant-decoherence.md'
const P1 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper1-record-click-law.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const C1 = '/Users/felixrobles/workspace/isp/v7/code/c1_lorentz_scalar_seal_mcc.py'
const C2 = '/Users/felixrobles/workspace/isp/v7/code/c2_derived_noise_kernel.py'

const RULES = `
Confirm the six round-1 fixes are correctly integrated and opened NO new defect. Enforce: pre-geometric discipline (Lorentz/metric only EMERGENT, never a derivation INPUT; microcausality stated against the frame-invariant record causal order), high precision (RUN python3 ${C1} , ${C2} ; if mpmath missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python -- reproduce: E=E*=E^2 exact, kernel Gram min-eig +2.78e-9 (positive-type exact by Bochner), point-local commutator vanishes / region-smeared fails at order 1, white-noise heating diverges while quartic = Gamma(3/4)/4), single-threaded (no round/version/'we now'/'corrected' narration; bare date stamp OK), BOTH-direction honesty.
SPECIFIC CONFIRMATIONS:
- FIX 1 (THE BIG ONE -- faithfulness): is the statevector wall now correctly attributed to the HAAG obstruction (not Fedida-as-prover)? Is Fedida 2025 now cited for its ACTUAL result (positive Einstein-causality / spacelike-commutation under the TS-unitarity ASSUMPTION, corroborating sec 4, NOT proving the wall)? Check sec 6, abstract (iii), sec 7 claim (4) + non-claims, and the reference list. Confirm no residual "Fedida shows generic interacting QFT lacks..." phrasing.
- FIX 2: is "reproduces the GDC recursion/inherits verbatim" gone, replaced by "the locality<=>spacelike-commutation HINGE" with the honest note that higher orders vanish trivially for a single point-local density and the all-orders recursion is BORROWED?
- FIX 3: is the inheritance correctly scoped to the MICROCAUSALITY half (finite-energy rate needs GDC normal-ordering SHARD lacks)?
- FIX 4: is the kernel "supplied at TIER B" (not outright), positive-type flagged as SHARD's strengthening, and the +2.78e-9 a finite-sample certificate (positivity exact-by-Bochner)?
- FIX 5: is B=B1xB2 now "B2 modulo the sec-4 point-local premise" (B1 unconditional Haag wall; B2 conditional)?
- FIX 6: is the GDC reference now free of a fabricated title (author+arXiv+descriptive gloss)? Are any remaining external citations (Haag, Fedida, Tumulka, GRW/CSL, Diosi-Penrose) faithful and not over-attributed?
- Any NEW overclaim/understatement or internal inconsistency (abstract vs body vs claims) introduced by the edits? Confirm the 4 disavowals (no full covariance theory; no objective interacting-field statevector; no derived kernel; point-local premise not a theorem) all still present, and the overall "conditional positive" grade is right.
Read companion Paper I ${P1} and the plan ${PLAN}.
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['focus', 'verdict', 'fixes_confirmed', 'must_fix', 'overclaims', 'new_problems_introduced', 'single_threaded_violations', 'summary'],
  properties: {
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    fixes_confirmed: { type: 'array', items: { type: 'string' } },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue', 'where', 'severity', 'fix'], properties: { issue: { type: 'string' }, where: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'major', 'critical'] }, fix: { type: 'string' } } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    new_problems_introduced: { type: 'array', items: { type: 'string' } },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['FIX 1 (the Fedida->Haag re-attribution, secs 1/6/7 + refs) -- THE LOAD-BEARING faithfulness fix. Confirm the statevector wall is attributed to the HAAG obstruction (unitary inequivalence of interacting reps; TS invalid in d>2), NOT to Fedida-as-prover. Confirm Fedida 2025 is cited for what it ACTUALLY does (positive Einstein-causality / spacelike-commutation ASSUMING the equivalence, corroborating sec 4). Check abstract (iii), sec 6 para 1, sec 7 claim (4) + non-claims, reference list -- no residual "Fedida shows generic interacting QFT lacks". Is the [WALL] verdict (SHARD no worse off than Tumulka/CSL) still sound under the corrected attribution? Is the Haag/Streater-Wightman citation appropriate?'],
  ['FIX 2 + FIX 3 + FIX 4 (the inheritance scoping, secs 2-4 + abstract). RUN c1 + c2. Confirm FIX 2: "reproduces the GDC recursion/inherits verbatim" is replaced by "the locality<=>spacelike-commutation HINGE on which the GDC recursion turns", with the honest note that higher orders vanish trivially for a single point-local density (recursion BORROWED, not re-derived). Confirm FIX 3: only the MICROCAUSALITY half is inherited (finite-energy needs GDC normal-ordering SHARD lacks) -- stated in abstract + claim (2). Confirm FIX 4: kernel "supplied at TIER B" (not outright), positive-type = SHARD strengthening of the bare GDC finite-heating requirement, and +2.78e-9 a finite-SAMPLE certificate (positivity exact-by-Bochner, stable across samples). Re-verify the c1/c2 numerics (E=E*=E^2, point-local vanishes/region-smeared fails order 1, white heating diverges).'],
  ['FIX 5 + FIX 6 + FINAL SWEEP (secs 5-8 + whole-paper coherence). Confirm FIX 5: B=B1xB2 is now "B2 modulo the sec-4 point-local premise" (B1 = unconditional shared Haag wall; B2 = conditional on the one premise) -- the two-layer status honest. Confirm FIX 6: the GDC reference no longer carries a fabricated descriptive title (author+arXiv+gloss); Haag/Fedida/Tumulka/GRW-CSL/Diosi-Penrose citations faithful, none over-attributed. FINAL: all 4 disavowals present (sec 7 non-claims: no full covariance theory; no objective interacting-field statevector; no derived kernel -- only coloring structural; point-local premise NOT a theorem); the "conditional positive" overall grade calibrated in both directions; pre-geometric (Lorentz EMERGENT-only, kernel a Tier-B statement); single-threaded; abstract<->body<->claims internally consistent after the edits. Hunt any new or residual overclaim/inconsistency.'],
].map(([f]) => () => agent(
  `Round-2 CONFIRMING hostile review of v7 Paper VII at ${P7}. Your focus: ${f}\n${RULES}\nReturn the schema (fixes_confirmed = which round-1 fixes you verified; new_problems_introduced = anything the edits broke).`,
  { label: `P7r2:${f.slice(0, 22)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
