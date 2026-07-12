# D13 hostile review, round 1: independent corpus/action rebuild

**Referee:** independent clean-room corpus, literature, and exact-witness audit  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION / INCOMPLETE-INVESTIGATION**

D13's central mathematical conclusion is correct: locality, unitary diamond
composition, the listed finite symmetries, record readout, and construction
gauge do not select one interaction/action coefficient.  The exact
quarter-/half-iSWAP pair reproduces and the continuum EFT argument is valid.
The corpus-specific conclusion also survives the targeted checks: V4 Paper
25, V6 Paper 4, V7 Papers 29 and 40, V8 growth actions, and V9's Hamiltonian
attempt contain strong conditional selectors or diagnostics, not a complete
universe action.

The submission nevertheless fails its own frozen gates A0 and A12.  The
machine inventory has a moving, self-including corpus boundary; its advertised
`4/4` checks are four printed quantities rather than assertions; it truncates
every file to the first 24 headings and first 24 scope guards; and the
interpretive ledger does not adjudicate several later V7 action/selector
campaigns.  Its counts already disagree with its prose.  The exact action
script also requires an undeclared, unpinned SymPy installation and fails
under the workspace's default Python.  Two prose claims are false: the two
exact models do not have the same positive outcome support, and the iSWAP
action counterexample is not a new D13 result because D12 already states and
executes it.

These defects do not rescue unique action selection.  They prevent the
stronger claim that D13 has completed a reproducible V1--V10 census and cleanly
located its originality boundary.

## 1. Executable reproduction

### 1.1 Corpus inventory

Frozen source reviewed:

```text
4b021f2d0ceb64c92d5ad49d22b367cdf4ea276a38593c93e968d27576d8aa82  v10/code/d13_corpus_action_inventory.py
```

On the last complete pre-review rerun, normal Python printed:

```text
MARKDOWN FILES SCANNED: 532
ACTION-RELEVANT FILES: 509
CORPUS STREAM SHA256: 7222b679f92a087c3aa65410a7ef2ac5a0f6c48363864b9a08c3423d94526d45
INVENTORY SHA256: 93c44713b66369e1f9f6c3fe80965b51828950e5e629a65194da197b13ef9016
CHECKS PASSED: 4/4
```

Normal and optimized stdout were byte-identical at that instant:

```text
f6951a88463db065935496a0ff7d4ed60c3bfa3736e640be3765708802549479
```

The generated JSON then had hash:

```text
93c44713b66369e1f9f6c3fe80965b51828950e5e629a65194da197b13ef9016
```

Those numbers are not stable receipts.  Earlier in this same review, without
a source-code change, successive scans reported first `528/505` and later
`532/509`, with different corpus, inventory, and stdout hashes as other D13
Markdown artifacts entered `v10`.  The interpretive ledger still says the
"first D13 run" scanned `525/502`.  Writing this hostile review adds another
Markdown file and therefore changes the inventory again.

The cause is exact and visible in the source:

```python
for version in range(1, 11):
    paths.extend((ROOT / f"v{version}").rglob("*.md"))
```

The inventory includes the D13 notes it is meant to audit and every later
hostile review.  It has no frozen cutoff, committed path manifest, exclusion
for generated D13 artifacts, or expected corpus hash.  Consequently a
review-complete D13 can never retain the pre-review inventory receipt.

There is a second receipt problem.  No Boolean checks or expected constants
exist in this script.  `CHECKS PASSED: 4/4` merely labels four values that were
printed: file count, relevant count, corpus digest, and payload digest.  A
missing mandatory paper, an empty category, or a changed corpus still prints
`4/4`.  This is a census output, not a four-gate executable.

### 1.2 Local action family

Frozen source reviewed:

```text
1674fc60dffbefd2d39e8ce24e65ffa6e05af3982c38f8268e718ffbe727dd57  v10/code/d13_local_action_family_exact.py
```

Direct execution with the workspace's default Python fails before any check:

```text
ModuleNotFoundError: No module named 'sympy'
```

No D13 requirements file, lock file, interpreter path, or SymPy version is
declared.  I installed SymPy 1.14.0 plus mpmath 1.3.0 into an isolated
temporary directory and reran without changing the workspace source.  It then
printed:

```text
P(pi/4): 1/2
P(pi/2): 0
CHECKS PASSED: 12/12
SEMANTIC SHA256: 474a234e1eb51100aef57ed658ae3c5fa0a3e2236af88b64d14f0070a6de84ea
VERDICT: LOCAL-COVARIANT-ACTION-UNIQUENESS-REFUTED
```

Normal and optimized stdout were byte-identical:

```text
46274e849e095f4cf78630bdf46efe640d88bb04e45a49eaa0ddaf0ef1090e10
```

The generated semantic JSON hash matches the printed semantic digest:

```text
474a234e1eb51100aef57ed658ae3c5fa0a3e2236af88b64d14f0070a6de84ea
```

Thus the arithmetic is reproducible in a supplied SymPy runtime, but the
repository does not presently supply or pin that runtime.  Either port the
small calculation to the already used exact `Q(sqrt(2),i)` standard-library
implementation or add a frozen dependency/runtime receipt.

## 2. Independent reconstruction of the exact theorem

Let

```math
X_{ex}=|01\rangle\langle10|+|10\rangle\langle01|,
\qquad U_\theta=e^{i\theta X_{ex}}.
```

On the one-excitation subspace,

```math
U_\theta=
\begin{pmatrix}
\cos\theta&i\sin\theta\\
i\sin\theta&\cos\theta
\end{pmatrix},
```

and it is identity on `|00>` and `|11>`.  Therefore:

- every member is unitary;
- every member commutes with leg exchange and total excitation number;
- `U_(pi/4)^2=U_(pi/2)`, giving exact shared-screen composition;
- operations on disjoint two-leg factors commute;
- an overlapping local `Z` operation fails to commute for the nontrivial
  family members;
- independent unitary input/output frame changes cancel in the instrument
  probability;
- the pointer-copy isometry makes the selected pointer alternatives exactly
  orthogonal; and
- both chosen gates have a maximal-entanglement witness.

For input `|10>` and final effect `|10><10|`, the probability is
`cos^2(theta)`, hence exactly `1/2` at `pi/4` and `0` at `pi/2`.  The actions
are physically inequivalent under D13's own equivalence criterion.

This independently proves the limited no-go:

```text
the shared finite structural gates do not select theta,
equivalently the product J tau / hbar.
```

The exact program does not establish a general nonunitary Lorentz gauge,
diffeomorphism covariance, arbitrary field-theory gluing, or durable-record
persistence under an unbounded extension.  Those are inherited/conditional
architecture claims, not consequences of these 12 finite checks.  The theorem
note mostly keeps that distinction.

## 3. The corpus inventory is not a complete action adjudication

### 3.1 Keyword breadth is not interpretive completeness

The current JSON labels 509 of 532 Markdown files action-relevant, largely
because `diamond`, `boundary`, and broad selector words occur throughout the
program.  It records category hit counts, hashes, up to 24 headings, and up to
24 scope-guard lines.  It does not record each theorem's hypotheses,
supersession, final verdict, or relation to action selection.

For long cumulative papers, the 24-item truncation hides precisely the late
campaigns that matter:

- V4 Paper 25 has 8,254 lines; its stored headings stop near section 7,
  before the later Einstein-source and Cartan/Wilson closure campaigns.
- V6 Paper 4 has 7,025 lines; its stored headings stop at section 22,
  while the commitment selector is in sections 69--76.
- V7 Paper 29 has 5,054 lines; its stored headings stop at section 23,
  before the effective-action projection identity in section 36.
- V7 Paper 40 has 4,823 lines; its stored headings stop at the first attack,
  before most of its derivation and final conditional theorem.
- V7 Paper 48 has 6,282 lines; its stored headings stop around section 20,
  before the later Einstein, QFT/amplitude, and onset campaigns.

The interpretive ledger manually recovers some of these late results, but the
machine inventory does not certify that recovery.  A0 requires a theorem-level
ledger, not only proof that a file contains the word `action`.

### 3.2 Material V7 omissions

The V7 row and "apparent exceptions" section discuss Papers 25, 26, 29, and
40.  They omit the later selector/action sequence:

```text
Paper 47  finite Einstein residual and variational stationarity;
Paper 48  selector coefficient calibration, Einstein residual,
          finite QFT-ready typed net, amplitude-necessity fork, and onset weight;
Paper 49  calibrated manifold-work selection;
Paper 51  entropy-versus-action manifoldlikeness gate and coercive response.
```

These omissions do not overturn D13.  Clean-room inspection gives the same
ultimate disposition:

- Paper 47 requires an Einstein-ready carrier, scale/source anchors, typed
  residual separation, an interior minimizer, and projective stability.
- Paper 48 repeatedly describes finite constrained-selector calibration and
  retains physical satisfaction, unique amplitudes, numerical couplings, and
  initial absolute seed selection as conditional or open.
- Papers 49 and 51 require calibrated manifold work, response separation,
  coercive margins/noncollapse, entropy-action summability, and a spacetime
  request.  They select within that calibrated panel, not the microscopic
  amplitude functor or all-universe action.

But A0 says no older action route may remain outside the ledger.  A conclusion
can be right while its promised completeness proof is incomplete.  These
papers need explicit rows with their assumptions and disposition.

## 4. Targeted reconstruction of the named older candidates

### 4.1 V4 Paper 25

D13's disposition is accurate.  V4 Paper 25 constructs powerful finite
metric, connection, curvature, path-kernel, source, Ward, Cartan, and Wilson
normal forms.  Its strongest Einstein uniqueness statements assume packages
such as EU1--EU9, source completeness, minimal curvature order, a calibration,
and the active move/cohomology alphabet.  Its path law explicitly contains a
supplied sector action `S_alpha` and positive reference `mu_alpha^0`.

It therefore conditionally selects an effective GR response inside a declared
sector.  It does not select the microscopic history measure, field alphabet,
reference, boundary state, or full action of nature.

### 4.2 V6 Paper 4: commitment and holonomy

This is the strongest apparent internal exception and D13's main conclusion
about it is correct.

V6 Paper 4's late commitment campaign derives

```math
S(I)=e^{-I},
\qquad \nabla\psi_G(h_G)=e^{-h_G},
```

and proves a unique convex minimizer, cofinal stability, and admissible-cover
stability.  But its own text makes the domain load-bearing: the positive
history support, count reference, primitive oriented quotient ledger,
retained modes, and log-partition functional must already be fixed.  Mixed
bases are rejected as different primitive-unit assignments, and changing
physical source/period data changes the unique response.  Earlier attacks in
the same paper show support, scalar work, least work, maximum entropy, and
fixed-point stability do not select the transport law.

Thus the commitment law is a real coefficient selector **inside a chosen
primitive ledger**.  It neither selects that ledger/support nor supplies the
complex interaction phase, field content, initial state, or record instrument.
D13 should retain this nuanced positive result rather than abbreviating it as
mere reconstruction, but it is not the missing complete action.

### 4.3 V7 Paper 29

Paper 29 proves an important exact statement:

```math
S_G^{eff}(R)=-\log E_P[L\mid G](R)+\text{constant},
\qquad L=dQ/dP.
```

The predictive field for a chosen committed filtration is uniquely the
conditional likelihood, and the KL projection identity is exact.  This is
not a free variational guess.

It still presupposes baseline/alternative laws `P,Q` and a physically
admissible projective filtration `G`; the paper ends with the admissibility
and compression theorem open.  D13 correctly treats it as the unique
record-visible representation of a supplied law, not selection of the law.

### 4.4 V7 Paper 40

Paper 40's finite action

```math
F=BW+Lambda+X+ISP+Commit
```

has a unique positive projective minimizer under nonempty convex admissible
space, convexity/strict convexity, coercivity, nonlookup, exact or controlled
projective penalties, typed center channels, committed masses, scales, and
boundary-growth assumptions.  The paper itself says convexity is a sufficient
condition rather than a proved physical law and that a potential can be
invented for any target minimizer.

D13's conditional classification is therefore correct.  Paper 40 is a
serious action architecture after its channel data are supplied, not a
universal selector of those data.

### 4.5 V8 and V9 growth/Hamiltonian routes

D13 also gets the main disposition right:

- the V8 interval-local `r+link` action has `S(antichain)=0`; arrival-only
  growth drives the sparse pathology while equilibrium sampling had a dense
  pathology;
- V8's growth paper explicitly says no placement/growth law is derived and
  treats victim/committer choices as candidate families;
- V8 Paper 1's commitment fixed point is inherited from V6 and remains
  mode/ledger dependent, while cross-sector Hamiltonian comparison lacks a
  record-supplied common energy zero; and
- V9's H1 mode-Hamiltonian selection was voided at the Legendre link: omitted
  tadpole families reverse the uncentered coefficient and nonzero `W_3` trees
  split the exact deciding coefficient across the grid.

The diffusion-churn result is evidence about a useful dynamical property,
not an amplitude or coupling selector.  No overlooked V8/V9 route supplies
the final action.

## 5. Prose and originality defects

### 5.1 The exact models do not have the same positive support

The theorem note says:

```text
Every theta has the same types, support, symmetry, conservation and local ownership.
```

The program itself proves that the recorded `|10>` proposition has probability
`1/2` for one packet and `0` for the other.  Their positive pointer/history
supports therefore differ for the displayed preparation.  What is shared is
the ambient Hilbert carrier, typed grammar, pointer alphabet, ownership,
symmetries, and allowed outcome set—not the positive measure support.

This should be corrected exactly as D12 corrected `Ext_G` versus positive
`Ext_(G,mu)`.  The nonuniqueness theorem does not require equal positive
support.

### 5.2 The iSWAP action witness is inherited from D12

The literature note's originality boundary calls the exact action-level
nonuniqueness witness a new D13 result.  Paper 13/D12 already defines the same

```math
U_\theta=e^{i\theta X_{ex}},
```

uses the same `pi/4` and `pi/2` members, proves the same unitarity/exchange/
excitation/entangling/locality/construction-order properties, obtains the same
`1/2` versus `0` durable record, and explicitly writes

```math
H_J=-JX_{ex},\qquad \theta=J\tau/\hbar
```

to identify the free action/coupling parameter.  D13 adds a compact SymPy
record-isometry and frame/gluing packaging, but the counterexample and
action-parameter conclusion are not new.

The defensible D13 originality boundary is narrower:

```text
a V1--V10 action-level synthesis;
the explicit boundary-amplitude-functor formulation for SHARD screens/collars;
the modulus/phase placement of evidence and holonomy;
and a consolidated gate protocol for future action selection.
```

Even these should be described as corpus-specific synthesis, not a general
priority claim over general-boundary QFT, decoherent histories, amplitude
functors, polar decomposition, or EFT.

## 6. Primary-literature audit

The main external claims were checked against the cited primary sources and
are mostly accurate:

- [Oeckl's 2003 proposal](https://arxiv.org/abs/hep-th/0306025) associates
  state spaces to boundaries of finite regions, and the
  [foundational paper](https://arxiv.org/abs/hep-th/0509122) develops arbitrary
  region amplitudes, axioms, probability, and ordinary-QM recovery.  It
  supports D13's architecture-not-law distinction.
- [Gell-Mann and Hartle](https://arxiv.org/abs/gr-qc/9509054) explicitly make
  permanence of generalized records under history extension part of strong
  decoherence.  D13's summary is accurate and appropriately notes that the
  Hamiltonian/state/coarse graining remain inputs.
- [Deser](https://arxiv.org/abs/gr-qc/0411023) derives Einstein and Yang--Mills
  nonlinearities from locality and gauge consistency after the linear gauge
  seed is supplied.  D13 correctly treats this as conditional sector
  completion.
- [Donoghue](https://arxiv.org/abs/gr-qc/9512024) supports gravity as a
  low-energy EFT, and the
  [Warsaw-basis paper](https://arxiv.org/abs/1008.4884) explicitly classifies
  many independent dimension-six operators modulo redundancies.  These
  support the coefficient-freedom claim.
- [Benincasa--Dowker](https://arxiv.org/abs/1001.2725) constructs a causal-set
  d'Alembertian/curvature and approximately local action;
  [Rideout--Sorkin](https://arxiv.org/abs/gr-qc/9904062) derive a family of
  covariant causal sequential-growth laws, not one law; and
  [Carlip--Carlip--Surya](https://arxiv.org/abs/2209.00327) show strong path-
  integral suppression of KR orders with evidence for a wider bad class.
  D13's cautious causal-set assessment is accurate.
- The [S-matrix bootstrap survey](https://arxiv.org/abs/2203.02421) explicitly
  describes an infinite-dimensional allowed S-matrix space with special
  boundary points, matching D13's conditional-selector characterization.
- The asymptotic-safety examples are represented cautiously.  The
  [Higgs-mass paper](https://arxiv.org/abs/0912.0208) makes substantial fixed-
  point and no-intermediate-scale assumptions, while the
  [gravity--matter study](https://arxiv.org/abs/1710.04669) works in functional-
  RG approximations.  Neither is misrepresented as a complete established
  universe selector.

One citation should be repaired.  D13 cites
[arXiv:1801.09811](https://arxiv.org/abs/1801.09811), whose title and main
result are the operational Markov condition, for the claim that process
tensors are complete reconstructible containers.  The direct primary source
for that claim is
[Pollock et al., arXiv:1512.00589](https://arxiv.org/abs/1512.00589), which
states a universal framework for arbitrary non-Markovian processes and
experimental reconstruction.  The current citation is related but imprecise.

The Lovelock and maximum-entropy/caliber paragraphs also need explicit primary
citations if the document retains its label `primary-source audit`.

## 7. Required repairs before round 2

### R1 — Freeze a non-self-referential corpus boundary

Create a manifest of the exact V1--V10 Markdown paths/hashes that existed at a
declared pre-D13 cutoff, or explicitly exclude D13 notes, data manifests, and
reviews.  Gate the expected path count and corpus hash.  A later review must
not alter the census it is reviewing.

### R2 — Replace printed `4/4` with actual coverage gates

At minimum, assert:

- the frozen path manifest and corpus digest;
- mandatory presence of every named key paper;
- one untruncated theorem/scope extraction artifact per key paper;
- agreement between JSON counts and ledger prose; and
- deterministic normal/optimized output against a frozen receipt.

Do not call counts/digests themselves checks.

### R3 — Complete the interpretive action ledger

Add explicit hypothesis/result/disposition rows for V7 Papers 47, 48, 49,
and 51 and any supersession relations.  Expand the V8 row to distinguish the
inherited commitment selector from growth placement and the common-energy-
zero obstruction.  A broad keyword JSON is not a substitute.

### R4 — Repair exact-witness wording

Replace "same support" with "same ambient carrier, grammar, and pointer
alphabet; packet-specific positive supports may differ."  Narrow all
finite-frame claims to the unitary examples actually executed.

### R5 — Repair reproducibility

Declare and pin SymPy, interpreter, and dependency hashes, or port the exact
12 checks to the standard-library `Q(sqrt(2),i)` arithmetic already frozen in
D12.  Add source/stdout/semantic receipts under normal and optimized modes.

### R6 — Repair literature/originality boundaries

Use the direct process-tensor reconstruction paper, add primary Lovelock and
maximum-entropy/caliber references, and state that the iSWAP action
counterexample is inherited from D12.  Reserve D13 novelty for the new corpus
synthesis and boundary-amplitude SHARD packaging, subject to hostile closure.

## 8. Final determination

| Gate | Independent result | Status |
|---|---|---|
| exact `U_theta` nonuniqueness | independently reconstructed | pass |
| local-action script arithmetic | 12/12 with temporary SymPy 1.14 | pass conditionally |
| default-workspace execution | missing SymPy | fail |
| inventory normal/-O equality | equal at one moving snapshot | pass only instantaneously |
| inventory frozen corpus | self-including and changed during review | **fail** |
| inventory `4/4` validation | no assertions/expected receipt | **fail** |
| V4 P25 disposition | conditional GR normal form, not microscopic selector | pass |
| V6 P4 commitment/holonomy disposition | real fixed-ledger selector, not arena/action selector | pass |
| V7 P29/P40 disposition | supplied likelihood/action data remain | pass |
| V7 P47--P51 coverage | absent from interpretive ledger | **fail** |
| V8/V9 growth/Hamiltonian disposition | failures/openings accurately identified | pass |
| positive-support prose | falsely says supports are shared | fail |
| primary literature substance | mostly accurate | pass with citation repairs |
| originality boundary | reclaims D12's exact action witness | fail |

The strongest defensible theorem after round 1 is:

```text
V6--V10 plus the tested finite amplitude/gluing/record principles
do not select one interaction coefficient or complete physical action;
the maximal candidate form is a boundary-amplitude architecture whose
field content, grammar, couplings, state, record instrument, and scales
remain primitive or empirical.
```

That theorem is supported.  The claimed completed corpus census and D13
priority boundary are not.

**Round-1 independent-rebuild verdict: MAJOR REVISION /
INCOMPLETE-INVESTIGATION.**
