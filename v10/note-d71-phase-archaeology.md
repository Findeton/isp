# D71 — phase archaeology: where the imaginary exponential is, where it died, and where the empty slot is

**Status: ARCHAEOLOGY SURVEY, 2026-07-27. NOT a pin, NOT a receipt, NOT a
result.** Nothing below is new evidence. Every number and every quoted
sentence is copied from a committed file and attributed by path and line.
The only forward-looking object is §4's closing paragraph, which is a
suggestion for the principal to freeze, amend or discard.

**The question, as put:** *"Regarding phase — are we missing 'an
exponential with imaginary numbers' somewhere along the towering
construction of the records? Don't go from memory: search the whole
v1–v10 corpus."*

**The short answer, before the evidence.** No — and the true situation is
more interesting than a gap. **The corpus already found the imaginary
exponential it needs and then stopped.** v7 paper 30 ran a dedicated,
receipted complex-amplitude campaign: it *falsified* the naive `e^{iS}`
continuation, proved that making the decay constant complex breaks dual
conjugation, and identified the one form that survives —
**`A(R) ~ e^{-K(E)}·e^{iΦ(O)}`: real decay on the even channel, phase on
the odd channel, positive record-projected shadow** — with reflection
positivity supplying the reason. It was never lifted to a theorem. In
parallel, v6 paper 7 **derived** the complex phase group, the submitted
batch (paper Va) **downgraded that to an admitted input**, v8 paper 2
**proved the records cannot force it**, v8 paper 7 left "complex weights"
as one of three surviving routes, `v9/PLAN.md` scheduled **one triage
note** on it — **which was never written** — and v10's generated line was
then built entirely on positive real weights without the question being
reopened. The imaginary exponential is not missing from the corpus. It is
missing from **v10**, its supporting documents contradict each other, and
the deferral was a descoping decision, not a finding. Details in §4.

**Provenance labels** (book §0.1 convention): `[THEOREM]` / `[EXACT]` =
argued depth-free and gated; `[MEASURED]` = true on a declared finite
window; `[OPEN]`; `[MY READING]` = this note's inference, load-bearing on
nothing. Where the corpus is silent, this note says **silent** rather
than resolving it.

**Method.** Corpus-wide greps over `v1 … v10`, `publishable/`,
`v6/publishable/`, the isp-root loose papers and `code/`, for: `e^{iS}`,
`exp(iS)`, `e^{i`, `imaginary`, `complex`, `phase`, `amplitude`,
`interference`, `Born`, `Wigner`, `negativity`, `Bhattacharyya`,
`signature`, `Hilbert`, `unitary`, `cocycle`, `holonomy`, `Wick`,
`Euclidean`, `positive weight`, `1j`, `sqrt(-1)`; every hit that mattered
was followed into its paper or note and read in context.

---

## §0. Three homonyms, cleared first — they contaminate every grep

The word-frequency tables are close to useless until the collisions are
removed. All were verified by reading, not by counting.

1. **"complex" is usually a *cell complex*.** In v10 the token has 405
   hits; the dominant collocations are `cut complex` (26), `action
   complex` (19), `opportunity complex` (16), `clock complex` (5).
   `relativistic-isp-v10-paper29-where-the-action-cocycle-lives.md:141` —
   "flat square on the **registered action complex**" — is a
   *polyhedron*, not a number field.

2. **"BORN" in capitals is a carrier *mode*, not Born's rule.**
   `note-d37-regional-history-specifications.md:211` —
   `mode_v in {NO_BIRTH, TOKEN, BORN}`; `:220` — `BORN` = "a new record
   point with declared causal parent is created". This accounts for a
   large share of v10's 665 `Born` hits.

3. **"phase" in D66/D67 is a *scheduling* phase**
   (`note-d67-k4-double-grid-result.md:79`, "mints-first,
   **phase-separated**"), and in v1/v4 it is overwhelmingly a *programme*
   phase ("Phase 9 → Paper 10").

Full false-friend table, all verified by reading:

| token | raw count | what it actually is |
|---|---|---|
| `phase` | v1 = 210, v4 = 240 | **programme phase**; `relativistic-isp-paper-roadmap.md:142–291` is most of it |
| `amplitude` | v3 = 266 | real signed **polymer / "bridge amplitude"** in the Kotecký–Preiss confinement ledger (`v3/…paper30…:2732`) |
| `modulus` | v3 = 280 | **loop-modulus debit**, a Wilson-loop normalisation budget (`v3/…paper18…:195`) |
| `coherence` | v4 = 36 | **quadratic/parallelogram coherence** gate (`v4/…paper25…:124`) |
| `signature` | v4 = 52, v6 ≈ 60 | **metric signature** `(1,3)`/`(-,+,+,+)`; the rest is "signature" as *empirical fingerprint* |
| `cocycle` | v4 = 299, v6 = 95 | **not phase-valued** — see §1.J |
| `Wigner` | v1 = 2 | raised **once as an open question** (`v1/…paper22…:983`) and never taken up; **zero hits in v2, v3, v4** |

**Silent by absence:** the literal string `e^{iS}` occurs in the entire
corpus as a live object **exactly twice**, both in the v8 causal-set probe
(§1.Q). It occurs **nowhere** in v10 and **nowhere** in the
generated-record line. The two places the corpus builds a *genuine*
imaginary exponential of its own data are v7 paper 30's `e^{iθ q(δ)}` /
`e^{iθO}` (§1.N2) and v6 paper 7's `U(1)` phase group (§1.F) — neither
cited anywhere in v10.

Four further terms are **silent in v7–v9**, verified by exhaustive grep:
`Wilson loop` (zero hits); `Wick rotation` (zero — `Wick` appears only as
combinatorial Wick *sums*); `Wigner` (one citation only, `v8/LEDGER.md:224`
— no Wigner function, no quasiprobability negativity); and `signature` in
v7–v9 **never** means metric signature (200+ hits, all "record
signature"/"order-geometry signature").

---

## §1. EVERY APPEARANCE of complex / phase structure

### A. The primitive representation map — `Γ = |U|²`. **The oldest and largest reduction in the corpus.**

* `v1/relativistic-isp-v1-paper1-collar-excision-exchange-defect.md:65` —
  "`\Gamma(U)_{AB} = |U_{AB}|^2`", introduced at `:63` as "The ISP kernel
  for **any** unitary one-particle propagator `U`".
* `v1/…paper2…:57`; `v1/…paper0…:318`, `:606`; `v1/…paper18…:48` ("The
  primitive **positive** slab kernels are… `\Gamma(e^{-i\Delta H_D})`").
* Carried verbatim into v2 (`v2/…paper1…:90`, `…paper6…:317`,
  `…paper10…:327`, `…paper5…:453`) and v3 (`v3/…paper4…:237`,
  `…paper1…:322`, `…paper5…:708`).
* `code/magic_vs_indivisibility.py:5` states it as the inherited Barandes
  representation: "`Gamma = |U|^2` (**entrywise squared modulus**)".

**Role.** The bridge from unitary dynamics to the record level: an
imaginary exponential goes in, a positive real stochastic kernel comes
out. **Fate: reduced to real, and the corpus flags the loss at the point
of definition** — `v1/…paper0…:35`: "`\Gamma_{ij}=|\Theta_{ij}|^2`, but
that representation is **not unique: phases and other lift data are not
fixed by `\Gamma` alone**."

The loss is then made an obstruction, `v1/…paper0…:578`:

> "Take two Dirac wave-packet superpositions `ψ_A + e^{iφ}ψ_B` whose
> packets remain spatially disjoint… For different relative phases `φ`,
> the entire local probability history on that interval can be identical…
> Once the packets later overlap, however, the subsequent probabilities
> generally depend on `φ`. Therefore future probabilities are **not
> determined uniquely by past local probability histories alone.** Any
> exact memory-kernel formulation on retained probability data must
> either fail to close uniquely or else carry **hidden coherence data**
> through its kernel or initial-slip term."

`[THEOREM]`-grade, and the corpus's earliest statement that a real-weight
record history is **not closed** without phase. Immediately after, `:582`,
a **recorded decision not to fix it**:

> "A direct generator on `\Theta` or on any equivalent lifted object
> **abandons the `\Gamma`-level spirit of ISP. Ontologizing internal
> phase or proper-time variables risks reintroducing hidden phase data in
> disguise.**"

Related: `:419` — a mass term "contributes only a phase at this order and
so **drops out** of the bare probability generator"; `:1107` — "Nor is
this loss of information a removable nuisance."

### B. The Schur–Hadamard rephasing gauge — **the prototype phase-invisibility theorem, v1**

`v1/…paper22-entropy-indivisible.md:172` — "`Θ'_{ij}(t) =
e^{iφ_{ij}(t)}Θ_{ij}(t)` … leaves `Γ_{ij}` invariant"; `:176` — "a novel
symmetry **without a classical analogue**: it modifies the density matrix
`ρ` without affecting any observable transition probability."

**Theorem 2**, `:456`: "(a) The Shannon entropy `S[p(t)]` is **invariant**
under every Schur–Hadamard gauge transformation… (b) The von Neumann
entropy `S_vN[ρ(t)]` is **gauge-dependent** for generic mixed initial
distributions." Witness at `:577`: `S[p] = ln 2` flat in `φ` while
`S_vN(φ)` slides from `0.611` nats to `0`; reading at `:594` — "the gauge
freedom acts as a **transfer between coherence and von Neumann
entropy**". `v1/…paper21…:431` prices it: "Gauge-dependence range:
`[0, ln 2]`."

**Fate: kept as a gauge, used as a no-go instrument.** Restated as
discipline in v2 (`v2/…paper6…:95`): "Schur-Hadamard gauge is real gauge.
**Phases in a chosen lift are not automatically physical beables.**"

### C. The v2 no-gos — **phase is proved un-representable at Γ level, three times, `[THEOREM]`**

* **Mach–Zehnder.** `v2/…paper6-qft-reconstruction-no-go-investigation.md:330`
  — "`\Gamma(D_\phi)= I` … **for every phase `\phi`**." And `:397` — "the
  coherent quantum circuit assigns different predictions: `P_0(0|0)=1`,
  while `P_\pi(0|0)=0`." The verdict, `:533`:
  > "The phase shifter has no visible effect at the stochastic component
  > level… Yet it controls the final interference pattern. Therefore
  > **phase is not an optional bookkeeping convention. It is
  > operationally real when coherent recombination is allowed.**"
  **Fate: the escape is a *bigger real kernel*** — `Γ(H D_φ H)` (Prop 1B,
  `:415`) is phase-dependent and still real. Phase is never represented;
  it is absorbed. Scope guard `:294`: this refutes "a Markovized
  `Gamma`-only reconstruction strategy, **not** the stochastic-quantum
  correspondence itself."
* **The phase fiber (Prop 2).** Same file `:554` — "`U' = D_1 U D_2` …
  `\Gamma(U')_{ij}=\Gamma(U)_{ij}`. Hence `\Gamma(U)` **cannot determine
  `U` as a complex unitary matrix**." Prop 3 (`:585`) extends it to every
  algebraic function of component shadows.
* **The metric no-go — the strongest "what is lost" result in v1–v4.**
  `v2/…paper10-metric-data-from-stochastic-exchange-curvature-investigation.md:1315`
  — "`h_0^{12} = \operatorname{Re}(z_1\overline z_2)` … is **absent**.
  The Born-squared leading coefficient keeps `|z_1|^2` and `|z_2|^2`, but
  **loses the relative phase**." `:1421` — "This failure is **not a
  harmless gauge term**." Proposition 10.6 (`:1659`) makes it all-order.

**And this paper names the attachment point, in the corpus's own words.**
`v2/…paper10…:1440`, escape route 4 of four:

> "**Different primitive stochastic rule.** Design a local stochastic
> comparison map whose elementary coefficient **retains oriented frame
> interference**. That would be **a new ISP postulate**, not a
> consequence of the current Born-squared endpoint rule."

`[OPEN]`, never taken up. The earliest explicit statement that the phase
slot is a *postulate-level* addition.

### D. The one place a `U(1)` phase survives the squaring — **and only as `2cos`**

`v1/…paper10-minimal-u1-gauge-coupling-holonomy.md`. At floor order the
Peierls phases enter "only through moduli or through bond/inverse-bond
cancellation" (`:489`), so `L_0[A]` is holonomy-blind. The survivor, at
order `Δ^{L+2}` — a full trip around the ring — is `:520`, whose holonomy
factor is `W + W^{-1}` with `W = e^{-iqΦ}` (`:176`), i.e. **`2cos(qΦ)`**.

**Fate: survives, real, even, sign-blind.** The flux's sign is lost,
exactly as `h^{12}`'s is. Ledger summary `v1/…paper17…:167` — "local
rephasings cancel at the `\Gamma` level **except for ring holonomy**."
`[THEOREM]`. **The corpus's only positive phase-survival result, and it is
a cosine.**

### E. v3–v4 — complex quarantined, then declared non-primitive

* **v3 makes complex data a typed, forgettable enrichment layer.**
  `v3/…paper1-minimal-enriched-isp-data-qft-reconstruction.md:215`
  Definition 4.1 quarantines it into named slots (`\mathsf H` = "Hilbert/
  GNS lift and readout map, **if used**"; `\mathsf F` = field algebra);
  `:249` — "A theorem is Gamma-level only when all entries beyond
  `\mathfrak D^\Gamma` are **unused** in its hypotheses and proof."
  Theorem 6.1 (`:406`) demands **conservativity**: enrichment must not
  change any Γ-level conclusion. `:66` — "Hilbert-space ingredients are
  **not ontological beables by default**."
* **v4 states the programme's thesis on phase.**
  `v4/…paper33-formal-hardening-of-relativistic-qft-descent.md:435`,
  §*"Spin, Statistics, And Phase As Transport Holonomy"*:
  > "**The corpus-wide thesis is that quantum phase is not primitive.**
  > `phase/statistics = finite exchange holonomy of source-response
  > transports.` Thus spin/statistics behavior is **not inserted as a
  > complex amplitude axiom**."
  **Fate: a programme statement, gated on a stable exchange defect being
  printed, never discharged. `[OPEN]`.** But it establishes intent: the
  programme did not *omit* the imaginary exponential — it **committed to
  deriving phase from real transport instead of postulating it**.
  Enforced downstream, e.g. `v4/…paper24…:57` — may use "finite
  stochastic kernels or finite **positive weights**"; may **not** use
  "Hilbert phase space… or continuum path integrals as ontology".
* Where the commitment strains:
  `v4/…paper40-conditional-fixed-ir-center-sign-certificate.md:32293` —
  "This is the desired modulus test. It **passes for real `Z_2`
  conditional signs. It fails for complex phase-valued residual
  kernels.**" Filed `OPEN_kernel` (`:32287`). **Note the shape: real signs
  pass, complex phases fail** — the same `Z_2`-vs-`U(1)` boundary that
  reappears at D66 (§1.J, §3.5).

### F. **v6 paper 7 §7 — THE COMPLEX PHASE GROUP IS DERIVED. This is the corpus's high-water mark, and v10 does not cite it.**

`v6/relativistic-isp-v6-paper7.md`. Four theorems, in sequence:

* **Thm 7.1 (canonical phase group), `:612`** — "The retained holonomy of
  a closed route pair on a sealed screen is valued in… the defect-free
  rotation group **SO(2) = U(1)** with canonical period `2π`… **the value
  space of an alternative is `R+ × U(1) ∪ {0} = C` as a SET**."
* **Thm 7.2 (quaternionic exclusion), `:623`** — screen-plane holonomies
  commute, unit quaternions do not (`|ij − ji| = 2.000`), "**Hence the
  phase object cannot be H-valued.**"
* **Thm 7.3 (the algebra is `C`), `:629`** — "By the Frobenius/
  Gelfand-Mazur classification the algebra is `R` or `C`; **`R` contains
  no nontrivial compact one-parameter group; hence the algebra is `C`**,
  merging is complex addition, independence is complex multiplication."
* **Thm 7.4 (split-signature exclusion), `:641` — and this is the one
  that matters most for the principal's question.** Taking the phase group
  *non-compact* (split-complex `e^{jφ}`, `j² = +1`) gives "`W- = -0.5431`
  at `φ = 1`… **Negative event weights violate positivity: REJECTED.**
  The phase group must be the **compact** normal factor."

**Read the direction of that argument carefully.** Positivity of record
weights does **not** kill the phase — it *selects* `U(1)` over the
split-complex alternative. In v6 the corpus's own positivity constraint is
what **forces the imaginary unit**, not what excludes it.

Also `Thm D3`, `:676` — "two-route interference is exactly the loop-phase
law `P = |A|² + |B|² + 2|A||B| cos(arg B(loop))` (machine gap `2.8e-17`)",
and `:719` — "L1. Non-triviality of nature's Bargmann loop phases.
STATUS: **empirically confirmed** — every interference experiment is a
measurement of a non-trivial loop class."

And the Lorentzian metric signature, derived and real, `:432` Thm 4.1 /
`:448` — "Lorentzian signature is not an input: it is **the shadow of
irreversible commitment**."

### G. **The submitted batch retracts it — paper Va makes ℂ an INPUT**

`v6/publishable/paper-Va-foundations-1.md` (*Born composition, Lorentz
signature, and the arrow of time*) — the submitted version of the same
layer.

* `:143` — "**What is and is not claimed.** We do not offer a
  Gleason-style or decision-theoretic derivation of the Born rule…
  probabilities here are *primitive* (record weights)…"
* `:159` — "Let a record screen carry a finite **complex weight vector**
  `a = (a_1, …, a_n)`" — ℂ is **given in the premise**. Only `p = 2` is
  derived, via the imported **Banach–Lamperti** theorem (`:177`).
* `:184`, input (0) — "the screen weight is a componentwise power-sum…
  **phase-blind per component**… itself an assumed form, **not derived
  from R/S/C**"; audit row `:423` — "power-sum weight ansatz **INPUT**".
* **"Signature" in Va is the *metric* signature**, `:28`, and it is
  graded down to corpus-bound `[P]`. It plays **no** role in the Born
  argument. (Lead 2 of the brief, resolved: signature and phase are
  unconnected here.)

**And the governing exclusion principle is an axiom.** `Va:73`:

> "**Axiom S (silent-seam exclusion).** Any datum that no sealed record
> registers — a silent label, **phase**, or holonomy — is **not part of
> the physics**; constructions requiring one are excluded or must be
> quotiented to gauge."

`v6/publishable/paper-Vb-foundations-2.md:94` gives the discriminating
criterion: "The `2π` rotation sign is **silent** on every single record…
**a relative phase *within* a sector changes seam interference weights
(receipted), so intra-sector superpositions survive**". And Thm 3.1
(`:133`) reduces the *exchange* phase to a real sign: "**Sealed positivity
on the exchange collar forces the exchange phase `(-1)^{2m}`.**"

**Fate: global phase abandoned by axiom; relative intra-sector phase
kept; exchange phase reduced to `{±1}`.**

### H. **v8 declares the bit un-forceable — and the two v6 documents are never reconciled**

* `v6/publishable/companion-B-almost-quantum.md:306` — "The one missing
  input is the **composite state space**… and, within it, local
  tomography (**the complex-over-real selector**); **the seal is blind to
  both** (receipt `t2`: `E = E² = E*` over `ℝ` **and** `ℂ`)." Non-claims:
  "This companion does **not** derive complex quantum theory."
* `v8/relativistic-isp-v8-paper2-envelope-unforceability.md:9` — "**field
  blindness** (the moment algebra `M` is invariant under the
  **complex→real reduction `R`**, while the selecting datum… lies in
  **`ker R`**)"; `:105` — "**the bit is invisible.** `χ_AB` is
  unreachable **not by weight but by symmetry**."
* `:115`, escape 1 closed — "the forced `q = 2` orthogonal-projection
  calculus (`E = E² = E*`, `q² = 1`) is **real-closed** — it holds over ℝ
  with no imaginary unit, so **the seal never manufactures a phase**."
  With a positive control so the instrument is not blind:
  "`Tr(P_X P_Y P_Z) = 0.25 + 0.25i` … the probe *would* see a phase if
  the substrate carried one, so '`Im = 0` on shared seals' is a **result,
  not a blind instrument**."
* Seen twice, `:192` — "**the unitary phase that would promote
  doubly-stochastic → unistochastic is the *same* `ker R` bit**… a
  conjugate pair `U, U*` with *identical* records carries opposite
  Jarlskog sign `±0.0521`."
* Status classified, `:9` — "three different epistemic statuses — scale
  *measured*, mode *import-fixed*, **tensor product *contested
  convention***", with Renou 2021 and the 2026 Hoffreumon–Woods / Maioli
  reopening catalogued at `:180`.

> **THE UNRECONCILED CONTRADICTION.** v6 paper 7 Thm 7.3 **derives** that
> the algebra is `C`. v6 companion-B says **the seal is blind to** the
> complex-over-real selector. v6 paper Va lists complex weights as an
> **INPUT**. v8 paper 2 proves the bit lies in **`ker R`**. Nothing in
> `v6/ERRATA.md` addresses this — its sweep covers only the Renou/real-QM
> citation issue and reports "**ZERO Renou citations in any v6 paper**."
> **`[OPEN]`, and unowned.** See §4.

### I. **The corpus's action is real: `A_D = log dP_AB/dP_BA`, not `iS`**

`v6/relativistic-isp-v6-paper4-sealed-record-events-and-born-composition.md:2679`
— "**The real `A_D` law is the sealed RN exchange cocycle.** It resolves
the `T_D` coefficient problem at the action level." Defined at `:2594`;
antisymmetry at `v6/…paper9…:389` — "`A_D = log dP_AB/dP_BA`". Its
expectation is the KL entropy production.

**Fate: kept, and it is the corpus's action analogue — a real
log-likelihood-ratio cocycle.** A fitted/complex surrogate (the `T_D`
family) was tried and **refuted**: `paper4:2972`,
`REFUTES-ACTION-DETERMINATION`.

The matching real exponential is the survival law,
`v6/…paper4…:5798` / `v10/…paper13…:151` — "`S(I)=e^{-I}`", with
`∇ψ(h) = e^{-h}` (`paper13:180`). **The corpus's characteristic
exponential is Boltzmann-shaped, not Feynman-shaped, at every layer.**

**And the corpus says so, in one sentence.** `v6/…paper4…:124`:

> "There are two faces of the law. The single-diamond event law is a
> **real positive** RN/readout law… **Phase, interference, and the Born
> role live in the retained exchange-holonomy composition law between
> diamonds. A purely real Gibbs tilt is only the positive readout face;
> it is not the whole phase-sensitive ISP process.**"

Backed by a gated receipt, `:483`:

| composition | operation | result | receipt |
|---|---|---|---|
| classical | **discard retained holonomy** | **no interference** | phase span = 0.000 — **FAIL-BORN** |
| complex holonomy | amplitudes add before event readout | interference appears | `P+ = 1.000, 0.750, 0.500, 0.000` — PASS-INTERFERENCE |

**This is the corpus's own experiment on the principal's question, and it
returns FAIL for the real-only branch.** `[EXACT]` at its fixture scope.

### J. Cocycles and signatures — **real everywhere; the one U(1) cocycle is proved not to exist**

* **v4's 299 hits**: `Z_2 = {±1}` centre-section cocycle
  (`v4/…paper40…:1345`, an SO(3)→SU(2) lifting obstruction — a **sign**);
  strictly positive Radon–Nikodym cocycle (`v4/…paper19…:2322`,
  "`A_\tau(q)>0`"); finite corner/index cocycle (`v4/…paper24…:1377`).
* **v6's 95 hits**: the real `A_D` cocycle (§1.I); Connes–Radon–Nikodym
  modular cocycles (real/positive); real additive consistency receipts.
* **The single genuinely phase-valued cocycle in the corpus is the one
  proved unavailable.** `v6/publishable/companion-F-chiral-matter.md:58`:
  > "the orientation data is **strictly `ℤ₂`-valued (character signs)**…
  > so **no `U(1)`-valued 2-cocycle can arise from `K` alone**… A
  > nontrivial projective phase would need a continuous gauge on a
  > *spatial* lattice, which is absent."
  `:61` — "needs **emergent geometry** — and the program's absolute
  geometric structure is behind the scale (`l_step`) wall."

**There is no `e^{iS}`-type cocycle anywhere in v1–v6.**

### K. The Bhattacharyya quarter law — **BC is real by construction, and the corpus's own correction was never back-propagated**

* **Definition and proof**, `v6/relativistic-isp-v6-paper26.md:231`:
  "The record imprint sends `rho_01 -> <e_1|e_0> rho_01` with
  **`|e_chi> = sum_b sqrt(P_chi(b)) |b>`**, so the per-cycle multiplier
  is exactly `BC`… `-ln BC / sigma = 1/4 + eps^2/6 + O(eps^4)`. QED"

  **So `BC` is purely real by construction — no modulus is taken and no
  phase is discarded, because none was ever put in.** The pointer states
  are real nonnegative square roots in a fixed basis.
  **paper 26 is SILENT on the phase question**: it contains no occurrence
  of "modulus", "Cauchy–Schwarz", "relative phase" or "pointer phase".

* **But the corpus knows the objection, and recorded it elsewhere.**
  `v6/relativistic-isp-v6-paper7.md:1178`, §12/B1:
  > "**B1. Duality law, CORRECTED. Cauchy-Schwarz gives
  > `|<phi0|phi1>| <= B = sum sqrt(p0 p1)`, with equality iff the
  > relative pointer phase is constant.** Phase-structured pointers with
  > IDENTICAL densities give `alpha = 0: V_QM = 1.000000, B = 1.000000` /
  > `alpha = 3: V_QM = 0.056135, B = 1.000000`… **A classical-record
  > (Bhattacharyya) clock is FALSIFIED by phase-structured which-path
  > marking**; SHARD, through its own dilation, carries pointer holonomy
  > and uses the dilation overlap."

  Version history confirms the correction was deliberate: the pre-
  correction v6.2 edition proposed BC as a physical law *with* a
  phase-based falsifier
  (`v6/paper7-superseded-editions/…-v62-extended.md:408`), and
  `…-v63-final.md:281` performs the retraction.

> **A LIVE ERRATUM, filed here, owned by nobody.** `BC` is only the
> **Cauchy–Schwarz upper bound** on `|<φ_0|φ_1>|`, saturated **iff the
> relative pointer phase is constant**. The quarter law therefore holds on
> the phase-constant (real-pointer) sub-class its own monitor
> construction silently assumes. `v6/ARCHIVE-STATUS.md:9` cites the
> quarter law with **no phase caveat**, and v10 paper 18 §2 (`:17`) uses
> it as the metric of the no-silent-erasure principle, likewise without
> the caveat. **This is not a phase gap in the theory; it is a
> propagation failure in the ledger.** `[MY READING]` for the
> significance; both quoted clauses verbatim.

### L. The decoherence functional — **complex in v6, modulus-only in v5/publishable**

* **v6 keeps it complex and makes its off-diagonal part the central open
  question.** `v6/publishable/paper-X-gravitational-decoherence.md:104` —
  the Gell-Mann–Hartle `D(α, α′)`; `:110` — "Chapman–Kolmogorov holds
  across `t′` ⟺ **the off-diagonal (interference) part of `D` vanishes**";
  `:118` — "Genuine indivisibility requires *intervals on which `D` is
  non-diagonal*… **This is a computation on the off-diagonal support of
  `D`, not on `|ρ₀₁|`**… It is the correct target, **and it is open.**"
  Same at `v6/…paper56…:92`. Note the deliberate inversion: the modulus
  is declared the **wrong** object.
* **v5/publishable reduces it to a modulus, with a stated reason.**
  `publishable/paper1-nonmarkovian-gravitational-decoherence.md:189` —
  "`C(T)/C(0) = ⟨e^{iφ(T)}⟩`"; `:196` — "**the coherence modulus is
  `|⟨e^{iφ}⟩| = exp(−½ Var φ)` exactly (any nonzero mean of `δE`
  contributes only the unitary phase of §2)**"; `:200` — "it is the
  *randomness* of `δE` that decoheres."
  **Fate: the complex object is formed and immediately reduced to its
  modulus. Ground: the mean phase is unitary/reversible, hence not
  decoherence.** A referee flagged the asymmetry
  (`publishable/…-review2.md:213`). **The discarded imaginary part is
  never estimated anywhere. Silent.**

### M. Magic, Wigner negativity, and the trade of phase for a **signed real** weight

* The verdict, `v6/relativistic-isp-v6-paper40.md:386` — "**magic =
  Wigner negativity is strictly finer than indivisibility.** The thesis
  lives on the dynamics/geometry/thermodynamics side, not the
  resource-theory side." Registered as binding constraint C7 at
  `v6/…paper56…:140`: "**Do not claim the sealed-holonomy channel is a
  nonclassical *resource*.**"
* What it says about phase content: `v6/…paper26.md:546` — the qutrit
  phase-point frame, stabilizer states at `min W = -9.0e-16`
  (nonnegative), the strange state at "**min W = -1/3 EXACTLY**",
  `sum|W| = 5/3`. **Complex amplitudes are traded for a real Wigner
  function whose *negativity*, not its phase, prices the resource.**
  Graded `CONJECTURE (QC-adv)` at `:565`, not theorem.
* And the representation choice is recorded as a decision:
  `publishable/paper2-hypersurface-deformation-obstruction.md:150` —
  "**Barandes' construction is configuration-space, not phase-space;
  `|Ψ[φ]|²` stays positive** for interacting fields, with the negativity
  carried by the **non-Markovian transition structure**, not by a signed
  'probability.' **Hudson obstructs the phase-space route, not the
  config-space ISP.**"

### N. Complex spectrum derived from **time-asymmetry** — the corpus's most interesting imaginary result

`v6/publishable/paper-I-psd-words.md:11` Theorem A — "If the necklace of
`W` is **achiral**, then `W(A,B)` has **real nonnegative spectrum** for
all PSD letters… The obstruction to it is precisely the **chirality — the
time-asymmetry**"; `:75` — "the first chiral classes occur at length six,
and… **complex spectra are realized on every probed chiral class**."
Theorem B: "the entire **complex-spectrum phenomenon begins at dimension
three**." Machine confirmation at `v6/…paper30.md:420` — "Achiral classes:
**imaginary parts at machine zero** in every random trial at lengths
6–10."

**Fate: kept, `[THEOREM]`.** This is a genuine derivation of *imaginary
structure from the arrow of time* — but it is a **spectral** imaginary
part of a real record word, unrelated to a Born phase. The corpus never
connects it to §1.F. **Silent on the connection.**

### N2. **v7 paper 30 §24–25 — THE dedicated complex-amplitude campaign. It rejected `e^{iS}` and found the form that survives.**

`v7/relativistic-isp-v7-paper30-rooted-boundary-law.md`, receipt
`v7/code/p30_complex_amplitude_campaign.py`, 11/11. **This is the corpus's
one deliberate, receipted attempt to make the click law a squared
amplitude, and the principal's question is its opening sentence.**

* **The framing**, `:2663`:
  > "The complex-number idea is tempting because the primitive record law
  > has the shape of a **real decay: `e^{-kx}`**. A Feynman-like
  > continuation would introduce a phase: `e^{-(k+i\omega)x}`. **But Paper
  > XXX cannot allow complex probabilities.** The only admissible
  > possibility is: **a complex amplitude layer whose committed-record
  > shadow is real, positive, dual-compatible, and non-reconstructive.**"
* **Naive path interference — FALSIFIED**, `:2757`. The coherent
  multiplicity `M_θ(P,C) = (1/D)|Σ_δ e^{iθ q(δ)}|²` was run at
  `θ ∈ {0, π/12, π/8, π/6, π/4, π/3, π/2, π}`; total variation degrades
  from `1.68e-5` at `θ = 0` to `0.611` at `θ = π/2`:
  > "**So naive path interference is not the missing law. Most phases
  > destroy the prediction.**"
* **Hidden phases — FAILED**, `:2791`: the inversion phase is "**pure
  gauge on committed records**" (TV `2.34e-140`); the descent phase "**is
  not record-intrinsic and fails**" (74,292 bad records).
* **AND THE FORM THAT SURVIVES**, `:2855`:
  > "So the complex rule is **not**: make the whole decay constant
  > complex. It is: **keep the even channel real and decaying; put phase
  > only on dual-odd channels; take a positive record-projected
  > shadow.**"
  With the arithmetic: `L_naive = e^{-(k+iθ)E}e^{iθO}` fails dual
  conjugation at error `1.82`; **`L_dual = e^{-kE}e^{iθO}` gives error
  exactly `0`.**
* **The reflection-positivity reason — the deepest imaginary-structure
  claim in the corpus**, `:3018`:
  > "This is the finite reflection-positive meaning of the complex idea:
  > **odd directions cannot be real positive observables; they become
  > positive as imaginary amplitude channels.**"
  (Real odd reflected diagonal `-26.05, -16.53, -29.78`; after the
  `i`-twist all principal minors nonnegative.)
* **The resulting diagnostic rule**, `:4191`:
  > "`A(R) ~ e^{-K(E(R))}e^{i\Phi(O(R))}`, with the physical click weight
  > obtained only after a positive record projection… **even data
  > contributes as real decay/volume; odd data contributes only through a
  > quadratic amplitude norm**; the real odd reflection form is negative;
  > the `i`-twisted odd reflection form is positive semidefinite."
* Abstract verdict, `:89` — "**The answer is yes, but only in a
  constrained sense. Complex probabilities are rejected. A positive
  record-projected amplitude shadow survives.**" Falsified list at
  `:4648`.

**Fate: the naive `e^{iS}` is falsified; a constrained even-real /
odd-imaginary amplitude algebra with a positive record shadow SURVIVES —
as an unproved theorem target.** `[OPEN]`. **This is the single most
important find in this survey, and §3.5/§4 turn on it.**

### N3. **v7 paper 42 — the amplitude object is defined, and deliberately deferred**

`v7/relativistic-isp-v7-paper42-spacetime-closure-to-qft-gates.md`.

* **Theorem 26 (Positive Committed Histories Have No Unprinted
  Interference)**, `:2031`; and its meaning, `:2046`:
  > "This does **not** say quantum interference is impossible. It says
  > that interference **cannot be a *silent* effect of two already-
  > committed positive alternatives**. It must either be: 1. not yet
  > committed; 2. carried by a typed residue; 3. represented by an
  > **amplitude/decoherence layer whose diagonal projection is the
  > committed record law.**"
* **§39 / Theorem 28 (Amplitude Necessity Fork)**, `:2123` — the explicit
  complex object:
  > "An amplitude model assigns `\mathcal A_D(\Gamma)\in\mathbb C` or more
  > generally a finite decoherence functional `\mathfrak D_D(U,V)\in\mathbb
  > C`… The committed positive history weight is then the **diagonal
  > shadow**: `h_D^\star(H) = \mathfrak D_D(c^{-1}H,c^{-1}H)`."
  **Note the shape: this is v10 paper 29's `D(α,β)` and paper 15's
  `D_R(α,β) = δ_{αβ}(…)`, written down in v7 three versions earlier, with
  its trichotomy** (all witnesses typeable ⇒ positive suffices; some
  witness untypeable ⇒ **a pre-commitment amplitude layer is necessary**;
  witness dissolves ⇒ artefact).
* **The decision, stated as a fork, twice.** `:937` — "Review E: 'QFT
  needs amplitudes, not positive weights.' **Accepted as an open fork**…
  That is a separate campaign." `:2498` — "**The delay is intentional.**
  The committed record law is primary. **Amplitude is introduced only if**
  committed positive histories plus printed typed residues cannot carry
  stable finite interference."
* `v7/relativistic-isp-v7-paper38-bounded-history-weight-onset-theorem.md:1375`
  — "**complex phases, if real, belong upstream of committed records**…
  A future complex-amplitude theory **must reproduce this positive
  projected history weight, not replace** the experimental probability
  formula."
* Positivity is load-bearing, not decorative:
  `v7/…paper41…:760` Theorem 6 — "**the barrier is finite only for
  positive weights;** then `\mathcal F_B` is coercive and strictly convex
  … `h_B` exists uniquely."
* And the fork was routed to the lab:
  `v7/relativistic-isp-v7-paper50-realistic-qft-deviation-experiments.md:69`
  — "**Amplitude/decoherence gate:** persistent unprinted interference
  forces a decoherence-functional layer"; `:489` — "**Priority 1:
  Multipath Born/Sorkin Tests.**"

**Fate: the complex amplitude layer is fully specified and consciously
not built. `[OPEN]`, by decision, with a stated trigger condition that
was never met — because it was never tested.**

### N4. v8/v9 — the surviving complex route, and the note that was never written

* **The no-go that made complex weights live.**
  `v8/relativistic-isp-v8-paper7-manifoldlikeness-flanks.md:88` Theorem
  4.1 — no *extensive positive* weight suppresses the layered bulk; `:99`
  — "`pE` showed **positive real weights cannot produce the *cancellation
  mechanism* (interference)**; Theorem 4.1 shows extensive positive
  weights cannot even produce *suppression by magnitude*. **What survives
  … is exactly: super-extensive positive actions, complex weights, or
  measures outside the counting class.**"
* **And the follow-up was scheduled, then dropped.** `v9/PLAN.md:211`,
  under *"Deliberately deferred (named so the omissions are choices)"*:
  > "**Complex weights** — paper 7 §4.2's third surviving suppression
  > route: **one triage note only this campaign.**"
  **The triage note was never written.** A grep of `v9/` and `v8/`
  returns only this line and its v8 source. **A recorded, deliberate,
  unexecuted abandonment** — and v9 then closed (`v9/LOG.md`, "No further
  v9 review rounds will run").
* **A quantified price of realness.** `v8/LEDGER.md:230` (#132) —
  "**complex enrichment makes every interact gate two-way** (`Tr[ρ_T R†]`
  mechanism; **real targets kill the J-term** — why the T3b ledger is
  exactly `×7/25`)."
* **A retired complex diagnostic.** `v8/LEDGER.md:68` (#34) —
  "PRE-REGISTERED CLARIFYING NEGATIVE CONFIRMED: **raw off-diagonal
  magnitude does NOT decide**… §7's phrase must be read as
  record-witnessed" — the naive complex/off-diagonal dense-vs-sparse
  decider was replaced by a **real** record-witnessed overlap functional
  `Ω`.
* **Where the corpus locates quantumness, and leaves it open.**
  `v8/relativistic-isp-v8-paper1-foundations-click-law.md:57` — "**That
  free profile *is* the genuine-quantum content the dense limit
  annihilates**" (the inter-seal coherence profile). `[OPEN]`, never
  pinned. And `:28` — "`q = 2` screen calculus (Born) | **[IMPORT],
  [CONDITIONAL]**".
* **Euclidean, chosen and disclosed.** `v9/note-h1-mode-hamiltonian.md:15`
  — "Equilibrium selection = Γ-minimization (**the standard Euclidean
  premise, disclosed as such**)"; `:34` — "**The selection premise is
  Euclidean equilibrium**; a dynamical-selection alternative is **out of
  scope**." **Silent on Wick rotation: the string does not occur in v7–v9
  in that sense at all.**

### N5. The programme's slogan, and its own grading

`README.md:107` — "**the complex phase behavior of quantum mechanics is
the effective shadow of this stochastic curvature. Interference is not
inserted as a mysterious complex rule at the beginning.** … In slogan
form: `quantum phase = stochastic holonomy`."

`first-principles-conceptual-leap.md:31` — "**Quantum phase is not a
hidden supplement to probability; it is the curvature data required for
consistent stochastic transport across incompatible hypersurface cuts.
This is not yet a theorem.**"

**Fate: the founding decision to exclude primitive complex amplitude,
stated as an explicit conjecture, and explicitly graded as unproved by
the corpus itself.** `[OPEN]`, since v1.

### O. The action line in v10 — **complex by construction, supplied, and immediately re-diagonalised**

* `relativistic-isp-v10-paper15-…:104` — "`Z:FSDiam(Sigma) -> Mat_C`";
  `:125` — "the finite path-amplitude or regional-action form. **It sums
  unrecorded alternatives coherently.**"
* `relativistic-isp-v10-paper13-…:265` — "`U_theta=e^{i theta X_ex}`";
  `:299` — "**All arithmetic lies in `Q(sqrt(2),i)`.**" **Fate: kept, and
  spent on a negative** — Theorem 2 (`:271`): the frozen principles "do
  **not** uniquely select the two-leg interaction."
* **The reduction**, `paper15:229` — "`D_R(alpha,beta) =
  delta_{alpha,beta} Tr(C_alpha rho C_alpha^dagger)`", with `:236` — "The
  bare system functional… **need not be diagonal**"; `:240` — "**Born
  weighting appears once, at the state/effect pairing; there is no later
  stochastic repainting of amplitudes.**"
* `paper29:266` — the Gram functional `D(alpha,beta) = <v_alpha,v_beta>`,
  strongly positive by construction (`:272`). **Its fixture, however, is
  real — see §2.3.**
* **The live interference exhibit.** `paper29:311` — unrecorded path `p`:
  "alternatives sum coherently and the visible `(s,o)` law is
  `(0, 1/2, 1/2, 0)`… The functional has eight nonzero off-diagonal
  entries." Recorded: `(1/4,1/4,1/4,1/4)` (`:325`). `:329` — "**The record
  instrument is part of the click law.**"

### P. The v10 generated line — **positive real weights end to end, and one explicit positive-root amplitude**

* `note-d42b4-quantum-lift.md:15` — "The lift assigns each complete
  depth-D history the amplitude **∏ √q**… every mu-ratio is preserved
  exactly (**Born = mu/Σmu**)." Its coherence exhibit, `:47` — "COARSE
  sealing leaves exactly 1/6 (the path's **√(1/6)·√(1/6)**)."
  Round 1 retracted the claim built on it: `:80` — "the pinned Q1 claim
  **RETRACTED as stated**… **is the classical gradient completion at unit
  boundary, in Hilbert dress — no evasion**"; `:99` — "**every identified
  object is classical**."
* `note-d43c-pincer-vs-escape-classes.md:101` — "`|rec> -> sum_w
  **sqrt(1/2)** |rec, w, v(C,w)>`"; `:104` — "**Born branch weights = the
  committed K1 kernel**". Summarised at `note-d43e-…:57`.
  **This is the "Born = K1" of the S3 result, and it carries no phase:**
  the entries are positive real square roots of the classical kernel, so
  `|√(1/2)|² = 1/2` reproduces K1 tautologically. Its own residue says so
  — `note-d44f-…:48`: "the operator carries the branch split only; the
  **CROSS-component weights remain the classical `q`'s**."
* **The v10 design decision, and it is recorded.**
  `note-d44f-foliation-and-measure.md:130` — "**The battery is
  real-valued; complex phases belong to the same zero-`|amp|^2` gauge
  sector (declared in-gate).**" With `:126` rescoping the forcing lemma to
  "`|amp|^2` content (**the forced object is the WEIGHTS**)". Its referee:
  `reviews/d44f-round1-hostile-review.md:236` — "**Complex phase
  (i/√2, 1/√2): convicted, but spuriously (real-only battery; nit-3) —
  not a battery pass, and not honestly a battery test either.**"
* One computed imaginary part, identically zero: `LOG.md:6661` — "every
  off-ray component, **imaginary part**… **vanishes AS A POLYNOMIAL**
  (YG2)."

### Q. The one `e^{iS}` in the corpus — **v8's causal-set probe, and it states the principal's question verbatim**

`v8/code/pE_phase_causalset.py:1` (identical at `v7/code/`):

> "DOES A COMPLEX PHASE WEIGHT `e^{i beta S_BD}` MAKE THE GENERIC…
> CAUSAL-SET BULK DESTRUCTIVELY CANCEL… AND DOES A REAL WEIGHT
> `e^{-beta S_BD}` (**the click-law survival form**) FAIL TO PRODUCE THAT
> SELECTION? … The creative hook (the SHARD reading): a REAL survival
> weight `e^{-kappa chi}` can only SUPPRESS (monotone reweight), **never
> CANCEL — you need the i**."

Result: a **designed null**. `v8/relativistic-isp-v8-paper4-gravity-continuum.md:94`
— "returned a clean **artifact/null** at reachable sizes… `R_bulk` landed
inside the shuffle band, so 'artifact/null' is a **designed outcome, not a
shrug**." One route left open: the `n`-trend, "an analytic problem, not a
computational one."

**And the paper states the physics conclusion in one sentence** (same
line): "the suppression mechanism itself runs on the **complex weight**
`e^{iS}` — **positive (Boltzmann) real weights provably cannot produce
the phase cancellation** — **signed real weights are a different, un-run
class**."

### R. Cohomology in v10 — the one **non-zero** phase-like class, and it is `Z/2`

* Trivial on the wide record: `note-d64-cocycle-result.md:1` — "**THE
  CLASS IS A COBOUNDARY — H¹ = 0.**"
* **Non-zero on the odd pair-conflict ring**,
  `note-d66-arbitration-crystal-result.md:373` ff:

  | ring | `M/2` | C7 obs | PARITY obs |
  |---|---|---|---|
  | `RING(4, 6)` | EVEN | **0** | **0** |
  | `RING(6, 6)` | ODD | **5** | **5** |
  | `RING(8, 6)` | EVEN | **0** | **0** |
  | `RING(10, 6)` | ODD | **5** | **5** |
  | `RING(12, 6)` | EVEN | **0** | **0** |
  | `RING(6, 10)` | ODD | **9** | **9** |
  | `RING(10, 10)` | ODD | **9** | **9** |

  `:390` — "**The parity reading survives at five ring sizes, not
  three**"; honesty clause `:398` — the magnitude "is `R − 1`, a count of
  **rounds**… **the only invariant statement available is `≠ 0`.**"
  **Role: a labeling/gauge obstruction. Fate: kept — never read as a
  dynamical phase.**

### S. D68 — the current frontier, and it reverses the old phase slogan

* `note-d68-functional-slot-result.md:127` — "the **Hermitian extension**
  (`D = S + iA`) is carried as a separate column throughout."
* `:318` **the lemma** — "**F4(e)'s zero is a tautology of the row shape
  the first version chose. It carries no information about records.**"
* `:330` **C2 sees `A`** — "an imaginary entry of `9/2048` leaves
  determinant `3887/67108864 > 0` and one of `9/1024` gives
  `−1/67108864 < 0`. ***The linear system is phase-blind; the constraint
  set C1–C4 is not.***"
* `:336` — "the constraint rank on the antisymmetric block is **268** at
  depth 2 and **3,739** at depth 3… **A record demand of paper 29's shape
  does see a phase.**"
* `:714` **WITHDRAWN 2**, verbatim: "~~'a record measure of that shape
  cannot see a phase'~~ … are **false as physics sentences**."
* `:396` **the dynamical demand** — "C1(block) + C3(one-step) + C5 ⇒
  `cohdim = 0` at `D = 2, 3, 4 AND 5`"; `:417` — "Superposition must
  therefore either **break state-generation**… or enter somewhere else
  entirely: **transport scope, a different record functor, or a different
  joint in the map**." Explicitly not licensed (`:606`): "**the map is
  untouched**."

### T. Where the two lines are declared not to meet

`note-d59-click-law-identity.md:44` — "**NOT the same object; NO identity
theorem; the relation is a named MISSING MAP**". The phase lives entirely
on the action line (`:16`).

---

## §2. THE REDUCTION POINTS — where amplitude became real weight, and on what authority

Seven, in construction order. For each: the step, and whether the
reduction was **proved lossless**, **chosen**, or **silent**.

### 2.1 `Γ(U)_{AB} := |U_{AB}|²` — v1, the substrate map

Step: `v1/…paper1…:65`. **Not lossless, and the corpus proves it**
(`v1/…paper0…:578`). Verdict: **a chosen projection whose loss is
theorem-grade and flagged at the point of definition** (`:35`), retained
because the programme's object of study *is* the record layer, and
reinforced by an explicit prohibition on repairing it (`:582`, "risks
reintroducing hidden phase data in disguise"). **The honest one.**

### 2.2 Axiom S — v6, the reduction promoted to an axiom

Step: `v6/publishable/paper-Va-foundations-1.md:73` — "Any datum that no
sealed record registers — a silent label, **phase**, or holonomy — is
**not part of the physics**."

**CHOSEN, at axiom level, and the corpus supplies the discriminator**
(`Vb:94`): silent global phase is quotiented; **relative intra-sector
phase survives because it changes seam interference weights, receipted.**
Verdict: **chosen, argued, and correctly scoped.** Axiom S does *not* say
"no phases"; it says "no *unrecorded* phases."

### 2.3 The power-sum weight ansatz — v6, phase-blindness as an admitted input

Step: `Va:184` input (0) — "componentwise additivity, **per-component
phase-blindness**, single exponent; **not derived from R,S,C**"; audit
row `:423` marks it **INPUT**.

**CHOSEN, and graded honestly as unearned.** The corpus does not pretend
this one is derived. Note what it costs: with per-component
phase-blindness assumed, Banach–Lamperti delivers `p = 2`, but the phase
was never at risk in that argument — it was excluded before it began.

### 2.4 `D_R(α,β) = δ_{αβ} Tr(C_α ρ C_α†)` — v10 paper 15

Step: `paper15:229`, with the rider `:236` — the bare functional "**need
not be diagonal**". **Lossless *conditionally*, and the condition is
named**: the seal isometries "accumulate **mutually orthogonal**
protected record strings" (`:222`); paper 29 §4.3 makes it hypothesis 2
of five (`:298`), and §5 shows the unconditioned case differs
(`(0,1/2,1/2,0)` vs `(1/4,1/4,1/4,1/4)`). Verdict: **proved lossless on
the decoherent branch; the branch is a hypothesis, not a fact.**

### 2.5 The Gram fixture is over a **real** field — v10 paper 29. **SILENT.**

`paper29:877` — "**All theorem arithmetic is integer, rational or exact
`Q(sqrt(2))`.**" `Q(√2)` is totally real. Every gate is real:
`B0=(Z+X)/sqrt(2)` (`:496`), `|Phi+>` (`:489`), `CNOT`, `Z`, `H`
(`:246`).

Paper 29 defines a complex Hermitian object (`:136`, "Hermiticity, strong
positivity") and then evaluates it entirely inside a real quadratic field.
The interference it exhibits — the eight nonzero off-diagonals of `:318` —
is **sign** interference, `E11 = -1/sqrt(2)` (`:503`), not phase
interference. **The corpus nowhere remarks on this.** `[MY READING]`; the
field statement at `:877` is verbatim. **The most consequential silence
found in v10.**

### 2.6 `amplitude = ∏√q` and the "zero-`|amp|²` gauge sector" — v10

Steps: `note-d42b4-…:15`; `note-d43c-…:101`; `note-d44f-…:130`, `:126`.
**CHOSEN, and — uniquely in v10 — the choice is written down.** But the
grounds are procedural, not physical: the phase sector is declared out of
scope because the battery cannot see it, which its own referee flags as
circular (`reviews/d44f-round1-hostile-review.md:236`). Verdict: **chosen,
declared, un-argued.** The corpus is **silent** on why the positive root
rather than any other section of the phase bundle.

### 2.7 `K_h(e|x) = h(y)/h(x)` — Born demoted to one reading among three

`paper29:452` Theorem 4; the gate list at `note-d40-…:176` — `H =`
continuation count / positive classical terminal weight / decoherent
Born cylinder weight. `paper29:478` — "A Born/decoherence-functional
terminal weight is **one possible `h`**… **The form neither selects `h`
nor diagnoses a quantum origin.**"

**Not a reduction but a de-licensing**, `[THEOREM]`: a positive real `h`
reproduces the Born-shaped form exactly. **This is why the corpus cannot
read "Born = K1" as evidence of phase content.**

### 2.8 The recorded rejections of `e^{iS}` as a measure

`v5/…paper3-unimodular-beable-gravity-cosmological-term.md:460` — "the
**Euclidean measure** (`e^{-S_E}` is a **positive weight**…)" against "the
real-time path integral has **oscillatory `e^{iS}` weights**"; the
four-way route table `:707` sacrifices the complex-weight route with the
ground "**complex weights: the sign problem**". Programme goal statement,
`publishable/paper2-…obstruction.md:139` — "a relativistic stochastic
mechanics for fields **with honest probabilities (not complex weights,
not a fictitious diffusion time)**."

**CHOSEN, argued, and consistent across v5–v10.** The corpus wants a
probability measure; `e^{iS}` is not one. **This is the real reason the
generated line is Euclidean, and it is stated.**

---

## §3. THE EMPTY SLOTS — where an `e^{iS}` factor could attach, and what the corpus already proves about each

### 3.1 The per-event weight → a complex weight. **Walled at the substrate, `[NO-GO]`-grade.**

v8 paper 2's field blindness (§1.H): the records factor through `M`, `M`
is `R`-invariant, the selecting bit lies in `ker R`, and the `q = 2`
calculus is "real-closed… **the seal never manufactures a phase**"
(`:115`) — with a positive control. Not "we haven't found it": **proved
invisible by symmetry**, at the stated scope (degree-`(1,1)` commitments;
higher-word substrates `[OPEN]`, `:196`).

**Verdict: not empty — walled.** Anything placed here is an import, filed
as the third of three blind imports, status *contested convention*.

### 3.2 The arbitration winner `W`. **The slot that survives D68's own collapse — the sharpest theorem, and the runner-up to §3.5.**

The brief asked for this one to be worked out carefully. It works out **in
favour** of the slot, for a non-obvious reason. Unlike §3.5 it has no
proposed functional form; unlike §3.5 it has an `[EXACT]` theorem naming
exactly why the corpus's own collapse result does not reach it.

**The two theorems.**

* `note-d62-h2-update-table.md:543` `[EXACT] T1(e)` — "**The arbitration
  WINNER is invisible to `sigma`.** Rows R3/R4 use `W` only through
  `vname(b, W, x)`, which the table abstracts to one fresh token. So
  `sigma(h+e)` **does not depend on `W` at all**… across the 52
  `(sigma, ckey)` groups, **0** have split targets." Rider: "*the `PK1`
  split moves menu **weight** between the two winners but never the
  successor **state***."
* `note-d68-…:380` — C5 is `E(h,h') = μ(h)μ(h')·K(σ(h), σ(h'))`, and under
  it `cohdim = 0` at every depth tried.

**The interaction.** C5 kills coherence *because* it demands the excess be
a function of the **σ-state pair**. D62 proves `W` is **not** a function
of σ. Therefore:

> **A phase carried on `W` is exactly a phase that C5 cannot express — so
> the D68 collapse does not reach it.**

D68 names this escape in the same sentence (`:417`): "either **break
state-generation — the excess is not a function of the closed law's own
variables** — or enter somewhere else entirely." **`W` is the corpus's one
identified, theorem-grade piece of the law's own data that σ provably does
not carry.** It is that escape, instantiated.

**D68's ansatz-free half points the same way**, `:373` — "**Every σ-state
pair that carries a permitted coherence also carries a forbidden one.**
The first version's geography is *not a function of the closed law's state
variables at all*; it is a function of the **serialisation labels**."
The coherence D68 finds permitted **already lives on non-σ data**.

**The asymmetry that makes the slot non-vacuous.** `W` is not invisible to
everything: `PK1` moves menu weight between winners
(`note-d62-…:547`; `note-d60p-h1-probe.md:290`, "`(1/4) · PK1(ckey,
et)[W]`"). So `W` is **weight-visible and state-invisible** — precisely
the position D42b4's positive root already occupies, since the `√q` there
*is* a `PK1` branch amplitude and `PK1 = (1/2, 1/2)` on the pair
(`note-d60p-…:293`). **The slot is already built; it is filled with `+1`.**

**Caveats.** D62's theorem is about **states**, and says so. Nothing in the
corpus says a `W`-phase would be *observable*, and this section does not
claim it would. The corpus is **silent** on whether a `W`-carried phase
has any record consequence — which is what makes it a first computation
rather than a first claim (§4).

### 3.3 The `PK1` split. **Live, and the smallest.**

The referee mutation `reviews/d43bc-round1-hostile-review.md:388` —
"mutation cmut1, `PK1` tilted to 1/3-2/3, **fails R3**" — pins the
*modulus*. `LOG.md:6248` records "PK1/BORN/amplitude tilts all fail
E2-E4/R3 exit 1". **But per `note-d44f-…:130` those batteries are
real-valued, so a unit-modulus phase tilt was never in their tilt space.**
`[OPEN]`, and cheap.

### 3.4 The order/height data D67 showed is load-bearing. **Structurally the most `e^{iS}`-like slot. Silent.**

`note-d67-…:297` — "**Height alignment is a DESIGN REQUIREMENT that the
grammar's own [idle event supplies]**"; `:306` — "*the `k` depth-1
consumers must sit at height + 1*". Height is integer-valued and additive
along a history — **structurally an action**. `e^{i·height}` would be an
imaginary exponential *of an existing corpus observable*. **The corpus has
never proposed it. Silent.** `[OPEN]`.

### 3.5 **The odd channel. This is the slot the corpus already found, wrote down, and did not connect to v10.**

Three independent results, from three versions, describe the same
even/odd split. Nobody has put them side by side.

**(i) v7 proved the *form*.** `v7/…paper30…:2855` — "**keep the even
channel real and decaying; put phase only on dual-odd channels; take a
positive record-projected shadow**", with `L_dual = e^{-kE}e^{iθO}` at
**dual-conjugation error exactly `0`** while the naive
`e^{-(k+iθ)E}e^{iθO}` fails at `1.82`. And the reason is reflection
positivity, `:3018` — "**odd directions cannot be real positive
observables; they become positive as imaginary amplitude channels**"
(real odd reflected diagonal `-26.05, -16.53, -29.78`; after the `i`-twist
all principal minors nonnegative).

**(ii) v10 found a non-zero class, and it lives exactly on the odd
objects.** `note-d66-…:383` — the `Z/2` PARITY obstruction is **`0` on
every even ring and `≠ 0` on every odd ring**, at five sizes, with
`M = 12` "the clean row that could have killed it" (`:390`).

**(iii) v8 named the gap between them as un-run.** `v8/…paper4…:94` —
"**signed real weights are a different, un-run class**"; and `Z/2 = {±1}`
is precisely `U(1)` restricted to `θ ∈ {0, π}`, i.e. the first
non-trivial rung of exactly the phase v7's `e^{iθO}` puts on odd data.

**The same boundary is drawn independently in two more places.**
`v4/…paper40…:32293` — the modulus test "**passes for real `Z_2`
conditional signs. It fails for complex phase-valued residual kernels**";
`v6/publishable/companion-F-chiral-matter.md:58` — "orientation data is
**strictly `ℤ₂`-valued**… **no `U(1)`-valued 2-cocycle** can arise from
`K` alone." **Five strata of the corpus draw the line at the same place:
signs are available, phases are not** — and v7 is the one stratum that
says *the phase belongs on the odd channel specifically*, with a receipt.

**Why this is the best slot, not merely the prettiest.** It is the only
candidate where the corpus supplies **all three** of: a proposed
functional form (`e^{-kE}e^{iθO}`), a proof that the form is the *only*
one compatible with an existing hard constraint (dual conjugation, error
`0` vs `1.82`), and an independently-discovered non-zero object in v10
carrying the right index (odd parity). Slots 3.1–3.4 supply at most one.

**Counter-caveats, load-bearing.** D66's honesty clause (`:398`) — the
class is non-zero but its *content* is not an invariant ("the only
invariant statement available is `≠ 0`"), and D64 found `H¹ = 0` on the
wide record, so a phase built here lives on the narrow ring only. And
v7's `E`/`O` are the *even/odd deletion-score channels of a rooted
boundary law*, while D66's parity is a *height-layer parity of a conflict
ring* — **the corpus nowhere shows these are the same index, and this
note does not claim it.** `[MY READING]`, flagged; every quoted clause
verbatim. **The identification is precisely what the first unit should
test.**

---

## §4. THE VERDICT

**Clause 0 — the direct answer. No, and the sharper statement is that the
corpus already found the imaginary exponential it needs, wrote it down
with a receipt, and then stopped. `[OPEN]`, by decision.**
`v7/…paper30…:2855` and `:4191` give the surviving form —
**`A(R) ~ e^{-K(E(R))}·e^{iΦ(O(R))}`**: real decay on the even channel,
**phase on the odd channel**, positive record-projected shadow. It is not
a guess. The naive `e^{iS}` continuation was run and **falsified** (TV
`1.68e-5 → 0.611` across eight phases, `:2757`); making the decay
constant complex **breaks dual conjugation** (error `1.82`); the surviving
`L_dual = e^{-kE}e^{iθO}` passes at **error exactly `0`**; and reflection
positivity supplies the reason — "**odd directions cannot be real positive
observables; they become positive as imaginary amplitude channels**"
(`:3018`). The corpus's own abstract grades it: "**Complex probabilities
are rejected. A positive record-projected amplitude shadow survives**"
(`:89`). **It survives as an unproved theorem target and was never
lifted.**

**Clause 1 — and there is a contradiction the ledger never resolved.
`[THEOREM]` / `[NO-GO]` / `[OPEN]`, as marked.** v6 paper 7 Theorems
7.1–7.3 **derive** that the value space of an alternative is
`R+ × U(1) ∪ {0} = C`, exclude quaternions, and — crucially — use
**positivity to select the compact phase group `U(1)` over the
split-complex alternative** (Thm 7.4: split-complex gives negative event
weights, "**REJECTED**"). In v6, positivity *forces* the imaginary unit.
Meanwhile v6 companion-B says "**the seal is blind to**" the
complex-over-real selector, v6 paper Va lists complex weights and
per-component phase-blindness as an admitted **INPUT** ("not derived from
R,S,C"), and v8 paper 2 proves the selecting bit lies in **`ker R`** —
invisible **by symmetry, not by weight**, with a positive control so the
instrument is not blind. `v6/ERRATA.md` addresses none of this. **These
four documents disagree, and nobody owns the disagreement.**

**Clause 2 — the corpus ran the experiment, and the real-only branch
FAILS. `[EXACT]` at fixture scope, and it is the single most direct answer
to the question asked.** `v6/…paper4…:483` is a gated receipt table whose
"classical composition / **discard retained holonomy**" row returns
"**no interference**, phase span = 0.000, **FAIL-BORN**", against
"complex holonomy composition … PASS-INTERFERENCE". The same paper states
it in prose at `:124`: "**A purely real Gibbs tilt is only the positive
readout face; it is not the whole phase-sensitive ISP process.**" And v8
generalises it: "**positive (Boltzmann) real weights provably cannot
produce the phase cancellation — signed real weights are a different,
un-run class**" (`v8/…paper4…:94`). **The corpus's own position is that a
positive-real weight sum is not the whole law. v10's generated line is a
positive-real weight sum.**

**Clause 3 — v10 does contain an imaginary exponential in disguise, and
it is `√`. `[MEASURED]`, un-argued.** The generated line's amplitude
objects — D42b4's `∏√q` and D43c's `sqrt(1/2)` — are the phase-free
section of an amplitude bundle whose base is the classical weight. "Born
= K1" holds tautologically because `|√p|² = p`, and paper 29 Theorem 4
independently de-licenses the inference (`:478`, the form "neither selects
`h` nor diagnoses a quantum origin"). D44f then declares complex phases
into a "zero-`|amp|²` gauge sector", and its own referee calls the
resulting conviction of `(i/√2, 1/√2)` **spurious**. **The phase slot on
the generated line is not empty and not full: it is occupied by `+1`
without an argument.**

**Clause 4 — at closed scope, D68 proves a coherent state-generated layer
cannot exist, and the phase-blindness slogan that used to cover this is
withdrawn. `[MEASURED]`, depths 2–5, one functor, one ansatz.** Under the
faithful paper-29 reading records **do** constrain phases — antisymmetric
rank **268** and **3,739** — and positivity sees the imaginary part too.
What kills coherence is the *dynamical* demand C5, completely
(`cohdim = 0`). Both old headline sentences are **WITHDRAWN, verbatim**
(`:689`, `:714`).

**Clause 4b — the deferral is documented three times, and each trigger
was never tested. `[OPEN]`, by decision, not by evidence.** v7 paper 42
defines the complex object outright — `\mathfrak D_D(U,V) ∈ ℂ` with the
committed weight as its **diagonal shadow** `h_D^\star(H) = \mathfrak
D_D(H,H)` (`:2123`) — which is v10 paper 29's `D(α,β)` and paper 15's
`D_R`, written three versions earlier, and then declares "**The delay is
intentional**" (`:2498`) with a trigger: amplitudes enter "**only if**
committed positive histories plus printed typed residues cannot carry
stable finite interference". v8 paper 7 Theorem 4.1 then proves extensive
**positive** weights cannot even suppress by magnitude, leaving "**complex
weights**" as one of three surviving routes (`:99`), and `v9/PLAN.md:211`
schedules exactly "**one triage note**" on it — **which was never
written**, before v9 closed. **The trigger condition was never evaluated;
the campaign was descoped.** That is a very different epistemic state
from "we looked and there is nothing there."

**Clause 5 — the honest residuals.** Four silences, none of them no-gos.
(i) **A live erratum:** the quarter law's `BC` is only the Cauchy–Schwarz
bound on `|⟨φ_0|φ_1⟩|`, saturated **iff the relative pointer phase is
constant**, and a Bhattacharyya clock is **falsified** by phase-structured
which-path marking (`v6/…paper7…:1178`) — a correction paper 7 made and
paper 26, `ARCHIVE-STATUS.md` and v10 paper 18 never received (§1.K).
(ii) Paper 29's Gram fixture is evaluated entirely over `Q(√2)` (`:877`);
its interference is **sign** interference and the corpus never remarks on
the restriction (§2.5). (iii) The signed-real class between positive-real
and complex is flagged **un-run** in v8, and D66 carries a **non-zero
`Z/2` class on odd rings** — nobody connected them (§3.5). (iv) Every
forcing battery that convicted a weight tilt was real-valued, so no sweep
has entered a pure-phase direction (§3.3).

**The best slot, with its grounds: the ODD CHANNEL (§3.5).** It is the
only candidate for which the corpus supplies all three of — a proposed
functional form (`e^{-kE}·e^{iθO}`, v7 paper 30 `:4191`); a proof that
this form is the *only* one compatible with an existing hard constraint
(dual conjugation: error `0`, against `1.82` for the naive complex decay,
`:2855`); and an **independently discovered non-zero object in v10 carrying
the right index** — D66's `Z/2` parity class, zero on every even ring and
non-zero on every odd ring at five sizes (`:383`). Reflection positivity
supplies the mechanism: odd directions are *not* real positive
observables and become positive only as imaginary amplitude channels
(`:3018`). The runner-up, on independent grounds, is the arbitration
winner `W` (§3.2): D62 proves `[EXACT]` that `W` is invisible to `σ`, and
D68's C5 collapse is powered entirely by σ-generation, so a `W`-phase is
one C5 cannot express and the zero does not reach it — but `W` has no
proposed form, only the sharper theorem.

**The first pinnable unit.** Three candidates, in priority order. The
first two are free.

**(a) THE INDEX QUESTION — the whole survey points here.** A single
question, decidable at fixture scale with committed objects: *is v7 paper
30's odd/even deletion-score channel split the same index as D66's
odd/even ring parity?* If yes, the corpus has a proposed imaginary
exponential (`e^{iθO}`) and a non-zero object for it to act on (the odd
parity class), discovered eleven versions apart and never introduced to
each other — and the successor is to evaluate `L_dual` on the generated
line's own odd channel and check the dual-conjugation error that v7
measured at `0`. If no, the coincidence is named and killed, cheaply, and
§3.5 collapses to §3.2. **This note does not claim the identification;
§3.5 flags it `[MY READING]`. Testing it is one computation on two
committed receipts.**

**(b) THE RECONCILIATION — free, and overdue.** A reading unit, no
receipt, in the D59 mould: *does v6 paper 7 Thm 7.3 (the algebra is `C`)
survive companion-B's blindness claim, paper Va's INPUT grading, and v8
paper 2's `ker R` no-go — or was it superseded without an erratum?* All
four documents are committed; decidable by reading. Load-bearing either
way, and the quarter-law caveat of §1.K — that `BC` is only the
Cauchy–Schwarz bound, saturated iff the relative pointer phase is
constant, a correction paper 7 made and paper 26 never received — should
be propagated in the same pass. **Exactly the kind of unowned
contradiction D43's corpus audit exists to catch.**

**(c) THE VISIBILITY MEASUREMENT, if (a) and (b) leave the slot open.**
Not a phase proposal — a measurement of the shape D62 and D68 already
support. *Take the committed D42b4/D43c lift at fixture scale, replace
the positive root `√(1/2)` on the `PK1` branch by `e^{iθ}√(1/2)` with `θ`
free, and run the existing committed batteries — isometry, Born = K1,
menu reconstruction at both cuts, the D44f foliation gates — and report
which of them can reject any `θ ≠ 0`.* Two pre-registered outcomes, both
results: if **no** committed gate moves, the phase slot is a proved gauge
freedom at fixture scale, D44f's declaration is upgraded from a
declaration to a theorem, and the honest statement becomes *the corpus
cannot host a phase, and now knows it by computation rather than by
scope*; if **some** gate moves, the corpus has its first record-visible
phase observable on the generated line. Every object it needs is
committed. **It turns §2.6's silence into evidence either way.**

---

## §5. Coverage and limits of this survey

Searched: `v1 v2 v3 v4 v5 v6 v7 v8 v9 v10`, `publishable/`,
`v6/publishable/`, `v6/paper7-superseded-editions/`, the isp-root loose
papers, `code/`, `v7/code/`, `v8/code/`. `~/workspace/physics` was checked
and is a **superseded HTML mirror of the v1 relativistic-ISP material**;
it is referenced nowhere in the corpus and adds nothing.

**Not done here, and it matters:** this note read the *arguments*, not the
receipts. **No number above was recomputed.** The v6 paper 7 §7 theorem
chain, v7 paper 30's `p30_complex_amplitude_campaign` (11/11), D66's
parity table, D68's ranks 268/3,739, the quarter-law derivation and the
v8 `pE_phase_causalset` null were all taken at their published grade.

**Two claims in §4 are reading claims, and are flagged as such.** Clause 1
asserts that four documents **disagree**; §3.5 and §4(a) assert that v7's
even/odd channel split and D66's odd-ring parity **might be the same
index** — `[MY READING]`, explicitly not established, and the proposed
first unit is precisely the test of it. Everything else in §4 is quoted.

**One premise in the brief was not confirmed.** v7 contains **51 papers**
(54 `.md` including the plan and status files); no "18 terminal papers"
claim was found anywhere in scope — **silent**.

The §4 recommendations are a **draft**, offered in D69's sense: to be
frozen, amended or discarded.
