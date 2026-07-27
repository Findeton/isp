# D71c — what the "something 2" actually was: the rank-2 metric hunt, its three no-gos, and whether `SU(2)` has any corpus foothold

**Status: ARCHAEOLOGY SURVEY (third in the D71 series), 2026-07-27. NOT a
pin, NOT a receipt, NOT a result.** Nothing below is new evidence. Every
number and every quoted sentence is copied from a committed file and
attributed by path and line. The only forward-looking objects are §7's
pinnable claim and its falsifiers, which are a suggestion for the
principal to freeze, amend or discard.

**The question, as put.** *"If the holonomy-phase identity works, the real
part makes spacetime/gravity and the phase makes the quantum layer.
Earlier in the corpus we were trying to find traces of 'something 2' to
find gravity — is it `SU(2)` or something else?"*

**The short answer, before the evidence.** **It was not `SU(2)`. It was
`h^{ij}` — the inverse spatial metric, a symmetric positive contravariant
RANK-2 TENSOR — hunted as the coefficient of the stochastic exchange
curvature; and the hunt has a name, a date, a gate number and a verdict.**
The search is `stochastic-curvature-gravity-investigation.md`
(2026-05-12), **Gate 2: "Metric-from-Stochastic-Curvature Lemma"**
(`:139-169`) — *"In more than one spatial dimension, can the exchange
curvature determine the tensor `h^{ij}`?"* (`:143`) — with **Gate 4**
asking for the matching rank-2 **response**,
`T_{ij}^{ISP} ~ δ log W[Γ,J,E] / δ h^{ij}` (`:200`). It was executed, as
that memo instructed by name (`:318`), as
`v2/…paper10-metric-data-from-stochastic-exchange-curvature-investigation.md`,
and it **half-failed at theorem grade**: the *diagonal* entries `h^{11}`,
`h^{22}` are visible in `Γ`-level data, but the **off-diagonal `h^{12}` is
provably not** — Proposition 10.6, an **all-order sign-ambiguity no-go**
(`:1659`). The corpus states exactly *what* is missing:
`h_0^{12} = Re(z_1 \bar z_2)` (`:1315-1322`), so *"the Born-squared
leading coefficient keeps `|z_1|^2` and `|z_2|^2`, but **loses the
relative phase between `z_1` and `z_2`***" (`:1325-1327`).

**That sentence is the direct answer to the principal's framing, and it
runs against it.** The corpus does not divide as *real part → gravity,
phase → quantum*. It divides as: **the real/even part gives the DIAGONAL
of the rank-2 gravity object; the off-diagonal — the part the
hypersurface-deformation bracket actually needs — is carried by the same
orientation datum the quantum layer needs.** Three campaigns, in three
versions, on three substrates, put the missing gravity datum in a **sign
on a closed route**: v2 p10's frame sign-flip `E_2 → −E_2` leaving every
`Γ` invariant while `h^{12} → −h^{12}` (`:1666-1671`); v6 p5's
`χ^{NN}_n ∈ {−1,+1}` with `Var(χ^{NN}|S) = 1` and best predictor `1/2`,
whose *minimal* determining datum is the **oriented** `SO(1,1)` holonomy
`Z^⊥_{a,ij}` because *"scalar work, magnitude-only holonomy, and
unoriented holonomy all forget the sign of the normal-route comparison"*
(`:795-797`); and v6 p52's spin-2 blindness, where the modular currency
prices the **trace** and the traceless part is *"Frobenius-orthogonal to
it and is projected out"* (`:21`). **`Z/2` is the missing datum on the
gravity side exactly as D71 §3.5 found it to be on the phase side.**

**And there is a second, sharper find the corpus made and never
generalised.** v6 papers 53/54 discovered, on the modular-congruence
substrate, that the **commutator** of two transports is *antisymmetric →
a rotation*, and dies against a symmetric source by an exact selection
rule, while the **anticommutator** of two transports *"is a traceless
symmetric rank-2 tensor that **can** couple to the spin-2 shear (measured
symmetric fraction = 1.000)"* (`paper54:22-24`). **The corpus therefore
already owns the algebraic form of the principal's dichotomy — odd part →
rotation/phase, even part → rank-2 metric/gravity — twice: once in v6
p53/p54's boost algebra, and once in v2 p10's Clifford repair
`½{γ^i, γ^j} = h^{ij} I` (`:1825`).** It has never been stated as a
dichotomy, and never carried to the generated line. §3.

**And `SU(2)`?** Four roles, none a derived gravity object: (i) the v3/v4
**lattice Yang–Mills** fixture, where `SU(2)` is *"the baby version"*
(`youtube-ym-production-pack.md:55-56`) and is **assumed everywhere and
derived nowhere**; (ii) v10 paper 11's **supplied** Bloch/celestial
connection, whose own §7 is titled *"Why `SU(2)` is not yet Lorentz
covariance"* (`:331`); (iii) v4 paper 40's `SO(3) → SU(2)` lifting
obstruction, which is a **sign**; (iv) v6 paper 7 §10.4's
**posed-not-solved** Standard-Model inverse problem, where
`U(1) × SU(2) × SU(3)` would arise as *degeneracy groups of internal
ledger fibers* — explicitly *"one level up"* from the screen phase,
*"exactly where Yang-Mills structure lives relative to
electromagnetism"* (`v6/…paper7…:1064-1066`), i.e. in the **matter/gauge
sector, not the gravity sector**. The only selection screen the corpus
ever ran on gauge groups **rejected `SU(2)`** (`v3/…paper22…:5754-5757`),
and that screen was itself later voided. **On the gravity line `SU(2)` has
zero foothold; importing it would be an import.** §5.

**Provenance labels** (book §0.1 convention, as in D71/D71b):
`[THEOREM]`/`[EXACT]` = argued depth-free and gated; `[DERIVED]`,
`[NO-GO]`, `[OBSTRUCTED]`, `[OWNED]`, `[LEVER]`, `[BLIND]`, `[PROBE]` =
the gravity line's own tags, reproduced as written (§8 notes that the
gravity papers do **not** use the book's tag scheme); `[MEASURED]` = true
on a declared finite window; `[DEFINITIONAL]`; `[STATED]` = asserted
without derivation; `[POSITED]`; `[IMPORT]`; `[SILENT]` = the corpus does
not address it; `[OPEN]`; `[MY READING]` = this note's inference,
load-bearing on nothing.

**Relation to D71 and D71b.** D71 (`note-d71-phase-archaeology.md`) asked
*where is the imaginary exponential* and found the surviving form
`A(R) ~ e^{-K(E)}e^{iΦ(O)}`. D71b (`note-d71b-holonomy-phase-identity.md`)
asked *is that phase the holonomy of probability transport* and found the
identity in two unwelded halves. **Both looked only at the odd/phase
channel.** This note takes the other half of the principal's dichotomy —
the **even/real channel and the gravity side** — and asks what the corpus
already did there. It does **not** repeat either survey. Its one
substantive correction to the shared framing is §6 Clause 2: the even/odd
split does **not** align with the gravity/quantum split, and the corpus
proves it does not.

---

## §1. The "something 2", located and dated

### 1.1 The hunt, in the founding memo

`stochastic-curvature-gravity-investigation.md` (isp root; byte-identical
copy in `~/workspace/physics`), authored 2026-05-12 — **the same
founding-memo family as the README's `quantum phase = stochastic
holonomy` slogan and `first-principles-conceptual-leap.md`.** This is
important on its own: **the phase hunt and the "2" hunt are siblings,
written in the same week, by the same hand, about the same object.**
`[MY READING]` on the significance; the dates and the file family are
facts.

The memo's own verdict, `:9-11`:

> "The path is scientifically interesting, but **gravity is not yet
> earned**."

The conceptual hinge, `:78-90` — and this is where the "2" enters:

> "The hinge is the normal-normal surface-deformation bracket:
> `[H[N],H[M]] = D[β]`, `β^i = h^{ij}(N∂_jM − M∂_jN)`.
> For ordinary QFT on a fixed background, `h^{ij}` is fixed geometry. For
> canonical general relativity, `h^{ij}` is a dynamical phase-space
> field. **This distinction is the whole gravity question.**"

And the research question, verbatim, `:92-96`:

> "**Can the coefficient of the stochastic exchange curvature be read as
> an inverse spatial metric, rather than inserted from outside?**
> That is the first true gravity gate."

**Gate 2**, `:139-169` — the object, named:

> "**Question.** In more than one spatial dimension, can the exchange
> curvature determine the tensor `h^{ij}` … ? **Lemma schema.** … if
> `C^{ij}` is **symmetric, positive, and transforms tensorially** under
> changes of hypersurface coordinates, then `C^{ij}` can be identified as
> an inverse spatial metric or inverse metric density."

**Gate 4**, `:191-209` — the *response*, i.e. the differentiation of a
log-weight with respect to the rank-2 object, which is exactly what the
brief asked whether the corpus contains:

> "`T_{ij}^{ISP} ~ δ log 𝒲[Γ,J,E] / δ h^{ij}` … The symbol `𝒲` is
> deliberately schematic: **the program must decide whether the varied
> object is likelihood, entropy production, exchange curvature, an
> induced action, or a reconstruction functional.**"

`:256` names the far-downstream spin-2 requirement — *"Around flat
backgrounds, the dynamical geometry excitations must behave like the
correct massless spin-2 degrees of freedom"* — but it is a **requirement
list item at Gate 6**, not the object being hunted.

**So the "something 2" is unambiguous. Grade: `[STATED]`, self-graded
"not yet earned".**

| what | which "2" | where |
|---|---|---|
| `h^{ij}` / `C^{ij}` | **tensor rank 2**, symmetric positive contravariant | Gate 2, `:139-169` |
| `T_{ij}^{ISP}` | **rank-2 response** = variation of a log-weight w.r.t. `h^{ij}` | Gate 4, `:200` |
| massless spin-2 | **representation spin 2** | Gate 6 item 4, `:256` |
| `SU(2)` | **does not occur in the memo at all** (`grep`: zero hits) | — |

### 1.2 The instruction, and the paper that discharged it

`:316-322`:

> "The next legitimate paper is not yet `Gravity from ISP`. It is:
> **`Metric Data from Stochastic Exchange Curvature`**"

That paper exists:
`v2/relativistic-isp-v2-paper10-metric-data-from-stochastic-exchange-curvature-investigation.md`
(2042 lines). Its §4 (`:150-207`) defines the **metric-candidate
coefficient** `C^{ij}` exactly as the memo's Gate 2 specified, and §5
(`:210-303`) sets **six gates** it must pass: M1 locality/first-derivative
form, M2 tensorial coordinate behaviour, **M3 symmetry** (`:244` — "The
symmetric part is the metric candidate `C^{(ij)}`"; the antisymmetric part
`C^{[ij]}` "has no ordinary inverse-metric interpretation"), M4 positivity
(`C^{ij}ξ_iξ_j > 0`), M5 regulator stability, M6 no hidden lift
dependence.

**And it states, in one sentence, why the "2" needed `d ≥ 2`**, `:203-205`:

> "This is the first-principles reason Paper 10 must go to `d>=2`: **only
> then can we test tensor structure, cross terms, symmetry, and positivity
> rather than merely fit one scalar coefficient.**"

---

## §2. What the hunt found — three no-gos, one derived metric, and one refuted overclaim

### 2.1 v2 paper 10: the diagonal survives, the off-diagonal does not. `[THEOREM]` (all-order no-go)

**Proposition 10.4 (leading first-moment audit)**, `:1237` ff. The leading
Born-squared Dirac coefficient is `A_x^{(1)} = κ_1 L_{x,1} + κ_2 L_{x,2}`
with `κ_j = h_0^{jj}/16a²` (`:1301-1312`) — **the two diagonal entries and
nothing else.** Then `:1315-1327`, verbatim:

> "The off-diagonal frame entry
> `h_0^{12} = E_1^{\ 1}E_1^{\ 2} + E_2^{\ 1}E_2^{\ 2} = Re(z_1 \bar z_2)`
> with `z_j = E_1^{\ j} + i E_2^{\ j}`, **is absent**. The Born-squared
> leading coefficient keeps `|z_1|^2` and `|z_2|^2`, but **loses the
> relative phase between `z_1` and `z_2`.**"

The concrete benchmark is the rotated anisotropic metric
`h_0 = [[5/2, −3/2], [−3/2, 5/2]]` (`:2019-2027`), and `:1415-1417`:

> "**No scalar normalization `R_a` can turn zero off-diagonal entries into
> `−3/2`.** The leading site/cell Born-squared Dirac coefficient therefore
> fails Gate M2 for rotated metrics."

`:1421-1428` — and the corpus refuses the easy exit:

> "**This failure is not a harmless gauge term.** The missing quantity is
> the relative frame phase/interference information `Re(z_1 \bar z_2)`,
> which is exactly the off-diagonal metric coefficient."

**Proposition 10.5** (`:1464`) searches the first higher-order
frame-interference channel and recovers only **signless** invariants —
`(h^{12})²` and `det h = h^{11}h^{22} − (h^{12})²` (`:1802-1812`).

**Proposition 10.6 (all-order sign-ambiguity no-go)**, `:1659-1700`. The
mechanism is a `Z/2`:

> "Let `E` be a constant frame and define the sign-flipped frame
> `\tilde E_A^{\ 1} = E_A^{\ 1}`, `\tilde E_A^{\ 2} = −E_A^{\ 2}`. Then
> `\tilde h^{11} = h^{11}`, `\tilde h^{22} = h^{22}`,
> **`\tilde h^{12} = −h^{12}`**. Thus a full metric reconstruction must
> distinguish `E` from `\tilde E` whenever `h^{12} ≠ 0`."

and the two frames give *the same endpoint probabilities on the same
labelled finite configuration space* (`:1782-1789`):

> "The ambiguity is a **phase/lift ambiguity** … **`Gamma`-level data
> retain transition probabilities, not the oriented Clifford phase data
> needed to reconstruct the full frame metric.** This is not a
> coordinate-reflection theorem. … The missing information is
> **representational phase data**, not a relabelling convention."

**Verdict, `:2001-2032` and the export ledger `:1934-1966`.** Paper 10
closes as *"a metric-data gate and Gamma-level obstruction paper"*, with
Prop 10.6 graded **"Negative theorem"** and the named repair being an
**enriched** datum (§3.2).

### 2.2 v6 paper 5: the same no-go, at sealed-record scope, on the *response*. `[MEASURED]`, verdict tag `ENRICHMENT-NOT-DERIVATION`

`v6/relativistic-isp-v6-paper5-born-and-gr-verdict.md` §10-§11 runs the
successor question on SHARD's own substrate. The object is
**`χ^{NN}_{a,ij}` — two indices, the normal-normal response** (`:494`,
"In the older V4 language it is the normal-normal coordinate
`χ^{NN}_{a,ij}`"), i.e. Gate 2's `h^{ij}` in sealed-diamond dress.

The campaign result, `:662-668`, verbatim rows:

> | same sealed shadow | … | sealed data have one value while `chi_NN` has two values | … | **SAME-SEALED-DATA** |
> | positive actual split | `Var(chi_NN \| sealed shadow)` | **normal-normal response is not measurable with respect to current sealed data** | vars=[1.0, …] | **SPLIT-POSITIVE** |
> | determinacy refuter | best `K(sealed_shadow)->chi_NN` predictor | no intrinsic map can succeed with probability tending to one | **success=[0.5, …]** | **REFUTES-DETERMINACY** |
> | completion check | include `chi_NN` in the sealed primitive ledger | determinacy becomes tautological, showing exactly what must be added | completed_var=0.0e+00 | **ENRICHMENT-NOT-DERIVATION** |
> | campaign verdict | current sealed data versus `chi_NN` | same sealed finite record data can hide two normal-normal responses cofinally | | **NN-SPLIT-PROVED** |

And the fixture's `χ^{NN}` is literally a sign: `:573-580` sets
`χ^{NN}_n(b,k) = −1` for `b=0`, `+1` for `b=1`.

**§11 then computes the *minimal* datum that removes the split**, and the
answer is a **closed-route oriented holonomy** — the founding
exchange-defect loop (`:780-792`):

> "The oriented normal-frame holonomy center realizes exactly that
> quotient. It is **not a raw `chi_NN` label because it is a closed-route
> record**: `perform the two normal transports in opposite orders, compare
> the returned normal frames at the same screen, and keep the oriented
> boost holonomy.` … `χ^{NN}_{a,ij} = read_{ij}(Z^{⊥}_{a,ij})`."

with, `:717-723`,
`Z^{⊥}_{a,ij} = [ T^⊥_j T^⊥_i (T^⊥_i T^⊥_j)^{-1} ]_{boost}` — a
**group commutator of two transports**, valued in `SO(1,1)`.

**And the decisive sentence, `:795-797`:**

> "**Scalar work, magnitude-only holonomy, and unoriented holonomy all
> forget the sign of the normal-route comparison. They therefore leave the
> same split alive.**"

The diagnostic table `:837-846` prices every candidate: current sealed
shadow **FAILS** (success 0.5), scalar work shadow **FAILS**,
magnitude-only holonomy **FAILS**, unoriented holonomy **FAILS**, oriented
`SO(1,1)` holonomy **PASS-MINIMAL** (success 1.0, cells 2), raw label
**PASS-TAUTOLOGICAL**.

**Read against §2.1 this is the same theorem twice.** v2 said: the
`Γ`-shadow keeps `|z|²` and loses the sign of `Re(z_1\bar z_2)`. v6 says:
the sealed shadow keeps magnitudes and loses the **orientation of a closed
route**, and only the *oriented* holonomy restores it. `[MY READING]` on
the identification; both clauses quoted verbatim. Note also, against
D71b's Clause 3: **this is a corpus object whose loop is explicitly the
`T_iT_j` vs `T_jT_i` commutator square — the founding loop — and it is on
the gravity side, not the phase side.**

### 2.3 v6 paper 52: spin-2 blindness, mechanically. Verdict `SPIN-2-BLIND`

The corpus's "spin-2-blind" phrase belongs to **paper 52**, not paper 57
(see §8, correction 1). `v6/relativistic-isp-v6-paper52.md:17-28`:

> "The answer is **SPIN-2-BLIND**, and the verdict's spine is a theorem.
> *Analytically*, by Bisognano–Wichmann the static vacuum modular
> Hamiltonian of a wedge is the boost generator `K = 2π∫ x T₀₀` — built
> entirely from the energy density, whose field-sector content is the
> **trace** `(∇φ)²`; the traceless combination `(∂ₓφ)² − (∂_yφ)²` is
> **Frobenius-orthogonal to it and is projected out, by construction and
> geometry-independently.** *Numerically*, the traceless (spin-2) response
> `c₂/c₀` … **collapses 14.6× under a controlled refinement at matched
> relative depth** — 19.56% → 1.34% from `L=12` to `L=16` … The currency
> prices the trace of the stress and is blind to the traceless spin-2
> part."

**Mechanically, then: the blind object is the modular currency `K`; what
it is blind to is the TRACELESS part of a rank-2 tensor; and it is blind
because `K` is a pure-TRACE functional.** `[THEOREM]`-carried (BW), with
the numerical leg self-graded weak — `V6_STATUS_AUDIT.md:37`: *"the
continuum collapse rests on a **2-point matched-depth lattice trend**;
verdict carried by the theorem, not the ladder."*

The four-probe ladder, `_archive_low_value_2026-06-14/papers/…paper54.md:43-47`:
P51 reaches multipole structure, blind to quadrupole dominance; P52 reaches
`T₀₀`, blind to `T_ij^TL`; P53 reaches the rotation/spin-1 sector, blind to
`T_ij^TL`; P54 reaches `T_{0i}`, blind to `T_ij^TL`.

### 2.4 Paper 57 and v7 paper 10: what IS derived on the "2"

The headline the brief carried — *"Einstein FORM derived, graviton
spin-2-blind"* — is **two claims that paper 57 explicitly separates**,
`v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md:57`:

> "*The distinction this section turns on:* the linearized spin-2 Einstein
> *equation* `G_⟨ab⟩ = 8πG T_⟨ab⟩` **is derived geometrically in §1.4**
> (the null-cone lemma fixes all 9 traceless components) … What is
> obstructed below is the *distinct* claim that the matter modular
> *currency* independently **prices** `T_⟨ij⟩` as a universal first-law
> charge — i.e. the propagating graviton / quantum spin-2 operator, *not*
> the equation."

Grade table, `:104-106`: linearized spin-2 (traceless) Einstein equation
**`[DERIVED, mod (R) + gates]`**; spatial-stress pricing (5 of 9)
**`[OBSTRUCTED]`** — *"spanned by the rank-5 boosted congruence, but only
at a non-universal, boost-dependent, second-order coupling `χ·sinh²η`"*;
spin-2 matter charge / propagating graviton **`[OBSTRUCTED→OPEN]`**.
Reading, `:63`: *"SHARD's emergent geometry is thus **spin-2-active but
not-a-graviton**"*.

The derived rank-2 statement itself,
`v6/publishable/paper-XI-sealed-record-gravity-no-go.md:33`:

> "the null-cone lemma — *a symmetric tensor `S_ab` with `S_ab k^a k^b = 0`
> for every null `k` is pure-trace, `S_ab = Φ g_ab`* — fixes **all 9
> traceless components at once** (rank `9` on the `10` symmetric
> components; sympy)."

And **v7 paper 10** — the corpus's dedicated spin-2 paper, which the brief
did not name — prices the "2" in three layers
(`v7/relativistic-isp-v7-paper10-spin2-carried-helicity2-modeblind.md:9`):
**`[OWNED]`** the record matter stress carries the rank-2 *tensor
structure* (traceless quadrupole, `Q_xx = 1 + 3cos 2t`, period `π`, pure
`l ≥ 2`, sympy-exact); **`[LEVER]`** it is a *conserved symmetric* rank-2
current, the exact source Weinberg's soft-graviton theorem needs;
**`[BLIND / WALL]`** the two propagating polarizations are record-blind —
the TT projection `5 → 2` needs a direction `n̂` in an unbuilt emergent
metric continuum and a canonical mode frame.

**Note the shape of what is owned and what is not.** *Tensor rank 2* is
owned outright. *Spin-2 as a universal modular charge* is obstructed.
*Helicity-2* is walled. **Nothing here is a group-theoretic `SU(2)`
question at any point.** `[MY READING]` for the summary; every grade tag
quoted.

### 2.5 The one place a rank-2 metric IS derived: the causal-set arc. `[PROBE]`

`v6/relativistic-isp-v6-paper1-indivisible-causal-set-gravity.md:148-165`:

> "the commutator of two normal deformations drags the slice labeling by
> `ξ = g^{ij}(N∂_jM − M∂_jN)` … **the flow-drift *coefficient* recovered
> from order + number is the curved inverse metric `g^{ij}`**
> (correlation `+0.99` against `1/Ω²` …) … **The full spatial-metric
> *tensor* is recovered in `2+1` and the physical `3+1`** (the drift
> vector rotates by an angle consistent with the tensor's prediction
> within the discreteness noise, **excluding an isotropic/scalar
> coefficient**)."

**This is Gate 2 passed — on a different substrate.** Grade `[PROBE]`,
self-limited at `:155` to *"an illustrative finite-sprinkling receipt, not
an error-barred discriminant"*, and `:248` *"it does not derive a graviton
or a holographic area law"*. **The substrate is order + number of a
sprinkled causal set — not the record weights, and not the generated
line.** `[MY READING]`: this is the corpus's proof that a rank-2 metric
*can* be extracted from discrete relational data; it is also the corpus's
proof that the datum which does it (**order**, i.e. orientation) is
exactly the datum `Γ` and the sealed shadow provably lack (§2.1, §2.2).

### 2.6 And the corpus already refuted the "scalar → rank-2" shortcut

`v6/relativistic-isp-v6-paper4-…:1021-1029`:

> "A scalar potential equation has **one** response component per screen
> atom. **A two-dimensional symmetric tensor equation has three components
> per atom**, with differential constraints. The diagnostic therefore
> rejects the overclaim: `screen conductance tensor geometry closes the
> scalar Laplace-Beltrami gate; it does not by itself derive the full
> Einstein tensor.`"

with the receipt row `:1064` — **`missing_components=8193`, verdict
`FAILS-FULL-GR`**.

**This is the single most important precedent for the even-channel
proposal in §4, and it is a negative one.** Any programme that hopes to
get gravity out of a *scalar* real channel has to answer this row.
`[MEASURED]`.

---

## §3. The commutator/anticommutator split — the corpus's own version of the principal's dichotomy

This section is the note's main positive find, and it was not visible from
the phase side.

### 3.1 v6 papers 53 → 54: the corpus tried the odd part first, and it died by selection rule

`_archive_low_value_2026-06-14/papers/relativistic-isp-v6-paper53.md:24-30`:

> "The congruence of two wedges boosted in orthogonal directions supplies
> two genuinely new cross-region objects: the *antisymmetric* commutator
> `B_AB = ½(K_A K_B − K_B K_A)` and the *symmetric* product
> `C_AB = ½(K_A K_B + K_B K_A)`.
> - **The antisymmetric sector is settled by a selection rule
>   (lattice-exact, but not contingent).** `B_AB` is exactly antisymmetric
>   … and the spin-2 shear source is exactly symmetric, so their
>   contraction is *identically* zero — **antisym·sym = 0**."

Then `_archive…/paper54.md:18-24`:

> "`C(θ) = ½{K(0), K(θ)}` as the symmetric cross-region structure. **The
> anticommutator is the methodological advance over P53:** where P53's
> object was the *commutator* `[K_x, K_y]` (**antisymmetric → a rotation**,
> forced to zero against a symmetric source by an algebraic selection
> rule), **the anticommutator of two boosts is a *traceless symmetric*
> rank-2 tensor that *can* couple to the spin-2 shear (measured symmetric
> fraction = 1.000).**"

**This is the principal's dichotomy, discovered independently, in the
corpus's own gravity line, and stated as a methodological remark rather
than a structure.** Odd/antisymmetric part of a pair of transports → a
**rotation** (the phase sector). Even/symmetric part → a **traceless
symmetric rank-2 tensor** (the gravity sector). `[MEASURED]` on the
symmetric fraction `1.000`; `[STATED]` on the framing.

Its own result was still negative — `paper54:32`, the boosted-to-static
spin-2 ratio is **`0.925`**, *"the boost slightly suppresses, never
enhances, the traceless coupling"* — and the file is **archived**, with
`V6_STATUS_AUDIT.md:71` recording it as the corpus's only
`slightly-rosy` rating on review-incompleteness grounds. **It is the
weakest-graded object cited in this note, and nothing here rests on its
numbers — only on its algebraic observation.**

### 3.2 The same split, eleven versions earlier, as v2 paper 10's named repair

`v2/…paper10…:1814-1830`, the "Enriched-representation alternative":

> "If Paper 10 allows the enriched Dirac representation, **the full metric
> is immediately available from the Clifford principal symbol.** Define
> `γ^i := α^A E_A^{\ i}`. Then
> **`½{γ^i, γ^j} = h^{ij} I`.** This recovers the signed off-diagonal
> entry: `h^{12} = ¼ tr(γ^1γ^2 + γ^2γ^1)`.
> **But this is *not* `Gamma`-level metric reconstruction.** It is an
> enriched-representation metric diagnostic: the Hilbert lift, Clifford
> matrices, **and oriented frame phase have been supplied** as part of the
> representation."

**The anticommutator of two directional generators IS the rank-2 metric.
The corpus writes the identity, uses it as a repair, and labels it
`[IMPORT]`.** And the *other* half of the same Clifford algebra — the
commutator `[γ^i, γ^j]`, which generates the spin group — is **never
written anywhere in the corpus.** `grep` for `Spin(3)`, `Spin(4)`,
`spin group`, `spinor bundle` across v1–v10 returns **only prohibitions**:
`v7/…paper8…:15` (*"no continuum field, spinor bundle, or mass scale is
used as input"*) and the matching review scripts
(`v7/reviews/paper8_review_round.js:19`). **The spin group is never
constructed anywhere in the corpus.** `[SILENT]`.

**`[MY READING]`, load-bearing on nothing but §7's pin.** If one takes the
corpus's own repair seriously, the map is:

| algebraic part of a transport pair | corpus object | sector |
|---|---|---|
| **anticommutator / even / symmetric** | `½{γ^i,γ^j} = h^{ij}I` (v2 p10 `:1822`); `C(θ)=½{K(0),K(θ)}` traceless symmetric rank-2 (v6 p54 `:18`) | **metric / gravity** |
| **commutator / odd / antisymmetric** | `[K_x,K_y]` → *"antisymmetric → a rotation"* (v6 p53 `:28`); `Z^⊥ = [T_jT_i(T_iT_j)^{-1}]_{boost}`, `SO(1,1)` (v6 p5 `:717`); `Δ_AB = T_BT_A − T_AT_B` (v6 p4 `:187`) | **rotation / holonomy / phase** |

**Three of the four cells are quoted corpus objects. The corpus has never
drawn the table.** `[SILENT]` on the join — the same shape of silence
D71b Clause 3 found on the phase side.

---

## §4. The even channel, mechanically: `K` is a scalar, and the corpus computed the rank-2 object and threw it away

### 4.1 What `K(E)` actually is. `[DEFINITIONAL]` + `[MEASURED]`

The brief asked whether `K` carries paired-direction structure. **It does
not.** `v7/…paper30…:4193-4206`, the entire definition:

> `A(R) ~ e^{-K(E(R))}e^{iΦ(O(R))}` … "`E(R)` is dual-even record data;
> `O(R)` is dual-odd record data; **`K` is a real decay/cost**; `Φ` is a
> phase on the odd channel only."

The only instantiated form is linear with a constant coefficient,
`:2838-2842`: `L_dual = e^{-kE}e^{iθO}`, and in the receipt
`v7/code/p30_complex_amplitude_campaign.py:532,544` `kappa` is a single
`Decimal` (`D("0.03125")` at `:725`) applied to a **scalar** `x`. So
**`K(E) = k·E`, `k` a constant.** `Φ(O) = θ·O`, `θ` a constant angle.

**And `E` is a 3-vector that the law immediately traces.** `:2986` — "Let
`E_j` be the three dual-even channels and `O_j` the three dual-odd
channels", with the three dual pairs named at `:2700-2702`
(`(24576,540672)`, `(25488,525208)`, `(24606,549648)`). Then `:2958-2968`:

> `E_total = Σ_j E_j`, `Q_odd = Σ_j O_j²`

with the reading `:2976-2982`:

> "total even data plus an odd quadratic norm is enough in the audited
> window. … This matters because **`Q_odd` looks like a real Hilbert norm
> of an imaginary/odd channel.**"

**Note the asymmetry, and it is exactly backwards from what a gravity
reading wants: the ODD channel is promoted to a quadratic form; the EVEN
channel is contracted to its trace.** `[MEASURED]` at the `N=9` window.

`grep` over all 4726 lines of paper 30 for `Hessian`, `second derivative`,
`second-order`, `susceptibility`, `two-point`, `cross-term`,
`off-diagonal`: **zero hits.** **Nothing in paper 30 is differentiated
with respect to anything, once, let alone twice.** `[SILENT]`.

### 4.2 The rank-2 object the corpus DID build on the even channel — and discarded

§25.4, `:2984-3022`. The instrument is a **3×3 reflected Gram matrix**
indexed by dual-pair channel, defined in the receipt
`v7/code/p30_reflection_positive_campaign.py:394-406` as

> `G_{jk} = Σ_R P(R) · f_j(R) · g_k(R*)`

with `R*` the dual-reversed record, `P(R) = count/9!` the uniform record
measure, and `f_j = E_j` (even) or `f_j = O_j` (odd). **This is a
reflected two-point function between channel `j` at a record and channel
`k` at the order-reversed record** — a genuine covariance/Gram structure,
with the off-diagonals computed and used (the `2×2` minors at `:2994-2996`
are `m_ii m_jj − m_ij m_ji`).

The reported principal minors of the **even** Gram, `:2991-2997`:

```text
98.669736552028218695      40.375198412698412698     35.754938271604938272
3798.5649484525034294      3207.5483571583854735     1163.0945373694745388
103363.83796002682333
```

— three `1×1`, three `2×2`, one `3×3`: **a positive-definite symmetric
`3×3` form on the even channel, computed exactly, printed, used as a
positivity check, and never used again.** The law consumes only its
trace-like contraction `E_total`.

**And the odd sector's rank-2 slot is asserted but unexplored.** `:3174-3190`:

> `Q_M(O) = O^⊤ M O`, not necessarily `Σ_j O_j²`. … "`M` is a positive
> semidefinite **metric or endpoint-effective metric** on the odd sector"

with `:3284` recording that the campaign scans **253 normalized *diagonal*
quadratic metrics** and `:3305-3314` selecting `M_9 = diag(5,5,3)`. **The
off-diagonal sector of `M` was never scanned.** `[SILENT]`.

The paper's own limit, `:3204`:

> "reflection positivity identifies the **type** of geometry. It does not
> yet select the physical coordinates."

### 4.3 The structural parallel, stated once

**v6 p52's blindness mechanism and v7 p30's even-channel compression are
the same move, two versions apart, on two substrates:** the modular
currency `K = 2π∫x T₀₀` prices the **trace** of a rank-2 object and is
Frobenius-orthogonal to its traceless part (`p52:21`); the click-law
diagnostic `K(E) = k·E_total` prices the **trace** `Σ_j E_j` of the even
channel and discards the traceless part of the Gram it had already
computed (`p30:2961`, `:2991`). **In both cases the discarded object is
exactly the traceless symmetric rank-2 part — the graviton's index
structure.** `[MY READING]` on the parallel; both mechanisms quoted
verbatim, and this note claims no numerical relation between them.

### 4.4 Where a rank-2 response could live in the generated line: nowhere, currently

Sweep of `v10/` for `metric`, `Gram`, `inner product`, `bilinear`,
`quadratic form`, `two-point`, `Hessian`, `second derivative`, `distance
function`:

| object | path | index structure | can host rank-2? |
|---|---|---|---|
| D64 chart transitions `g_{ee'}` | `note-d64-cocycle-pin.md:46-52` | chart pair × direction pair | **in form yes; measured `H¹ = 0`, "the transitions are pure gauge"** (`note-d64-cocycle-result.md:40-56`) |
| D58 `ω(e,e')` | `note-d58-atlas-instrument-result.md:79-87` | pair-indexed but **factorizes** to `\|D_{e'}(d−1)\|/\|D_e(d)\|` | **no** — a chart-size ratio (`:116-117`) |
| homogeneity / width / crystal profile | d58, d60, d63, d66 | scalar per event/record | no |
| D32 distance proxy | `note-d32-dimension-map.md:11` | pair of **points**, ranking-only (`:51` "**No absolute scale, no calibrated distance**") | no |
| D47 sky | `note-d47-sphere-rung-result.md:92,172` | set cardinality + ternary betweenness; **no pairwise angle or inner product exists in v10** | no |
| D42b4 `∏√q` | `note-d42b4-quantum-lift.md:15` | per-history scalar amplitude | no |

**`Gram`, `bilinear`, `Hessian`, `inner product`, `quadratic form` return
zero substantive hits across `v10/code/`.** And there is a hard structural
cap: `note-d64-cocycle-pin.md:105-107` — *"Chart width is capped at 4 by
W4b on every delivery substrate — **any tensor statement is a width-≤ 4
statement and must say so.**"*

**Verdict: the generated line currently contains no object of rank 2 in
the paired-direction sense. The atlas came closest and measured
trivial.** `[MEASURED]`.

---

## §5. `SU(2)`: the complete corpus inventory, and its grade

Every occurrence, sorted by whether the group is derived, selected,
assumed, or imported.

**(a) DERIVED: none.** The corpus never derives `SU(2)`.
`v7/…paper42…:2470` lists **"gauge group selection"** among the things
explicitly not proven.

**(b) The nearest thing to a derivation is `U(2)`, in the matter sector,
with the `2` an INPUT.** v6 paper 7 Theorem 10.3 (`:1070-1077`):

> "**Theorem 10.3 (degeneracy gauge).** Let two ancilla directions of the
> dilation fiber be exactly degenerate. Then any `U(2)` rotation of that
> pair leaves every sealed marginal invariant (machine: max change
> `1.7e-16`) … **continuous gauge groups are degeneracy groups of the
> representation**, with the finite ledger automorphisms as their discrete
> skeleton."

And §10.4, `:1079-1097` — **"The Standard-Model inverse problem (posed,
not solved)"**: find the minimal oriented ledger whose
*"automorphism/fiber-degeneracy structure realizes `U(1) × SU(2) × SU(3)`
(degeneracy fibers of dimensions 1, 2, 3)"*, with the closing sentence
**"No claim is made that the solution exists or is unique."**

The parallel Doplicher–Roberts reconstruction reaches
`S(U(3)×U(2)) ≅ (SU(3)×SU(2)×U(1))/ℤ_6`
(`v6/…paper31…:242-244`), **but the fiber dimensions are inputs** —
`v6/…paper29…:14-15`: *"reads (1,d) THEOREM + **d = 3 MINIMALITY INPUT**
(d ≥ 4 not excluded)"*, and `v6/…paper18…:17-19`: *"'Gauge from exchange'
delivers the GLOBAL internal symmetry group; **gauging (locality,
connection, dynamics) is an additional input.**"* `[THEOREM]` on the
commutant identity; **`[IMPORT]` on the `2`.**

**(c) ASSUMED, everywhere in the Yang–Mills arc.** `v3/…paper10…:10`
("a **declared** `SU(2)` Peter-Weyl finite-battery cutoff");
`v3/…paper11…:44`; `v4/…paper43…:26`; `v4/…paper44…:26`. The corpus's own
public framing, `youtube-ym-production-pack.md:55-56`:

> "To keep the pictures simple I'll often use the **baby version, SU(2)**."

The one clean `SU(2)` theorem is 2-dimensional and self-declared trivial —
`v6/…paper8…:825-845`: exact area law `⟨½tr W⟩ = r^{RT}`, machine gap
`≤1.1e-16`, followed by *"The 2d area law is **KINEMATIC**: two-dimensional
gauge theory confines trivially - abelian included - so Theorem 9.2 by
itself is not evidence of confinement dynamics."*

**(d) SELECTED — and the one screen the corpus ran REJECTED it.**
`v3/…paper22…:5754-5757`:

> "`SU(2)` and `SU(3)` **fail** the time half on the active row, while
> `SU(4)` passes time but fails escape by Theorem 29.5. However, the
> large-`N` fundamental channel has a positive verdict: for every
> `N ≥ 4096` …"

That screen was subsequently voided by `v3/ERRATA.md:7-18` (paper 25
Thm 16.8: *"the current v3 corpus supplies none of the five same-law
sources"*). **So the corpus's only recorded verdict on `SU(2)` as a
selected group is negative, and then withdrawn.**

**(e) IMPORTED, explicitly.** `v10/note-d15-maximal-low-energy-action.md:65-71`:

> "**Given, rather than deriving,** `3+1` local Lorentzian QFT;
> **`SU(3) x SU(2) x U(1)`**; the observed chiral fermion representations
> …"

**(f) `SU(2)` as a SIGN.** `v4/…paper40…:1345` — the `SO(3) → SU(2)`
lifting obstruction, a `Z/2` centre-section cocycle (catalogued in
D71 §1.J).

**(g) `SU(2)` in the kinematic/celestial line — supplied, and explicitly
insufficient.** `v10/…paper11…:325-357`, §7 titled *"Why `SU(2)` is not
yet Lorentz covariance"*:

> "This supplies covariance **after a relative `SU(2)` connection is
> given.** It does not derive link birth, values, ownership, calibration,
> transport instruments, or a physical holonomy seal. … A full
> Bloch–celestial theory needs a consistent `SL(2,C)` event/effect gauge
> and Born weight law, **not only local `SU(2)` rotations.**"

with `:475` listing *"full Lorentz covariance from `SU(2)`"* under
non-claims, and `v10/note-d10-bloch-celestial-investigation.md:276`:
*"**`SU(2)` covariance cannot be advertised as Lorentz covariance.**"*

**(h) On the GRAVITY line: `SU(2)` occurs zero times as an object.** The
founding gravity memo has zero hits. Paper 57, paper-XI, papers 51–55,
v7 paper 10, v8 paper 4, v6 paper 1, v6 paper 5: the "2"s are tensor rank,
component counts (`4/9`, `5`, `5→2`), codimension (`SO(1,1)` on a
codimension-2 normal plane), helicity count, and metric signature.
**No gauge group appears.** `[MEASURED]` by exhaustive grep (§8).

**Does the YM line touch the gravity line or the generated line?**
Structurally yes to the first (v4 papers 25/26 treat GR and finite QCD as
parallel "finite descent extensions", `v4/…paper26…:29-33`), and
`v6/…paper46…:1` registers a **conjecture** joining the YM tower gap to
the modular currency. **No shared theorem.** To the generated line: v6
paper 39 is the deliberate bridge (*"The first campaign where the
program's two lines physically join"*, `:10`) and its finding is a
negative — *axiom C alone does not select Yang–Mills*; and v10's only
technical reuse is the `Z_2` gauge-matter fixture
(`note-d46e-smeared-interacting.md:32-36`, `:52-55`, verdict: does **not**
collapse). **Otherwise the YM arc terminates at v6 —
`v10/note-d71…:94` records `Wilson loop` at zero hits in v7–v9.**

---

## §6. Non-abelian traces: the flat answer

**The corpus contains ZERO genuine non-abelian composition on the
generated-record line, and the corpus's own measurement says so in the
strongest possible terms.**

`v10/LOG.md:7574-7577`, D46f RD3:

> "**ALL 7,163 co-receivable pairs COMMUTE — including the 63 with
> overlapping footprints: the reception state is an ABELIAN MONOID under
> reception**, strictly stronger than the pin asked"

and it is definitional, `v10/THE-THEORY-SO-FAR.md:8909-8914`:

> "true, structural (the committed `View` builds every field from a
> **down-closed** index set, so order-independence is **definitional**) …
> **ACT commutes on all 170,820 pairs**, not just the 7,163."

The atlas gauge group is at most `Z/2` and is a coboundary
(`note-d64-cocycle-result.md:1`, `:256-258`, `:264-268` — *"the name of
the group is undetermined by the data anyway"*; 10 subgroups of `S₄` are
consistent, and 7 transitions are length-changing and *"belong to no
permutation group"*, `:295-303`). D66/D67 add nothing
(`note-d66…:554-563`; `note-d67…:425-428`, the free-relabelling route —
*"the largest possible gauge group"* — clean everywhere). PK1 is a
probability split on winners, not a transformation with a composition law
(`note-d60p-h1-probe.md:290`, `note-d62-h2-update-table.md:547`); the
`k = 3,4,5,6` proposer counts index a combinatorial ceiling
`max|D| = k²`, not a group order.

**False friend, flagged:** v10's `S_n` is the **Dushnik–Miller standard
example** (an order-dimension crown poset), **not** the symmetric group —
`v10/code/d45b_sn_ladder_exact.py:14-24`,
`v10/…paper32…:71`, `:297`.

**Every non-abelian object in the corpus lives off the generated line, and
each has a defect:**

| object | where | verdict |
|---|---|---|
| `S_3` exchange-curvature commutator `ρ(s)ρ(r) − ρ(r)ρ(s) = −[[0,√3],[√3,0]]` | `v3/…paper9…:998-1014` | **genuine and computed** — but a **declared** model (`:1192`), and **Theorem 9.2 proves the corpus's own probes are blind to it**: *"for all `a,b ∈ G` and all `c ∈ 𝒞(G)`, `c(ab) = c(ba)`"* (`:1041-1052`) |
| braid representation `ρ(B)` | `v5/…paper9…:138-140`, `:200` | **posited, not constructed** — a dictionary slot, no matrix, no receipt |
| braid → `S_n` | `v6/…paper18…:168-172` | **the theorem KILLS it**: the braid rep factors through `S_n`, `‖holonomy − 1‖ = 2.2e-14`, and the physical operator is `ε = (−1)^{2m}P` — a `Z/2` (`:203-210`) |
| "non-abelian Wilson holonomy on internal fibers", Thm 10.2 | `v6/…paper7…:1058-1063` | **the receipt is four random Haar `U(2)` matrices** — `code/v6_p7g_sresolution_matter2_campaign.py:88-92`, `U1,U2,U3,U4 = (haar_u(2) for _ in range(4))`; `‖[U1,U2]‖ = 1.136` is generic non-commutation of random unitaries, connected to no record transport. **`[POSITED]` with a vacuous witness — the corpus's most misleading non-abelian claim.** |
| `Aut` of the 3-spin ledger contains `S_3` | `v6/…paper7…:1055` | genuine and enumerated — but an **automorphism** group: the observables are invariant under it |
| `SU(2)` link products | `code/su2_loops.py`, `code/v6_p8f_…py` | genuine — **imported lattice YM**, no record object |
| Pauli/`Q8` 2-cocycle | `v6/…paper9…:288-290` | genuine, but the record symmetry group is `V4 = Z₂×Z₂` (abelian); all commutators central |

And the corpus's own founding disclaimer, never retracted,
`v1/…paper10…:37`:

> "**No non-Abelian extension is claimed here.** … A genuine non-Abelian
> analogue would require new primitive-kernel control of path-ordered
> Wilson-line data, together with the corresponding **matrix-valued**
> wrapped exchange coefficients. **None of that structure is derived in
> this paper.**"

`grep` for path-ordered / matrix-valued transports in v7–v10 returns zero
substantive hits; every v7 "non-commutative" hit is microcausality proving
a commutator is **zero** (`v7/…paper13…:47`).

**So: the only realised composition law on the record line is `A_D = log
dP_AB/dP_BA` — a real additive, hence abelian, cocycle — and the only
non-zero cohomology class is a `Z/2` coboundary of a naming convention.**
`[MEASURED]`.

---

## §7. THE VERDICT

**Clause 0 — what "something 2" WAS. `[STATED]` at the memo, discharged at
`[THEOREM]` grade.** It was **`h^{ij}`, the inverse spatial metric — a
symmetric, positive, contravariant rank-2 TENSOR** — hunted as the
coefficient of the stochastic exchange curvature in the
hypersurface-deformation bracket
`β^i = h^{ij}(N∂_jM − M∂_jN)`. Location:
`stochastic-curvature-gravity-investigation.md` **Gate 2** (`:139-169`),
with **Gate 4**'s rank-2 response `T_{ij}^{ISP} ~ δ log 𝒲/δh^{ij}`
(`:200`) as its successor. It was *not* a representation-theoretic search
and *not* a group search: **`SU(2)` does not occur in the memo at all.**

**Clause 1 — what the hunt concluded, at what grade.** Three verdicts,
three substrates, one shape.
(i) **v2 paper 10, `[THEOREM]` (negative):** `Γ`-level Born-squared data
see `h^{11}`, `h^{22}` and the signless invariants `(h^{12})²`, `det h`,
and **provably cannot see `h^{12}`** — Prop 10.6's all-order
sign-ambiguity no-go, driven by the frame `Z/2` flip `E_2 → −E_2`.
(ii) **v6 paper 5, `[MEASURED]`, `ENRICHMENT-NOT-DERIVATION`:** the sealed
record packet does not determine the normal-normal response `χ^{NN}_{a,ij}`
(`Var = 1`, best predictor `0.5`); the **minimal** datum that does is the
**oriented** `SO(1,1)` closed-route holonomy `Z^⊥_{a,ij}`, and every
unoriented or magnitude-only variant fails.
(iii) **v6 paper 52, verdict `SPIN-2-BLIND`, theorem-carried:** the modular
currency is a pure-**trace** functional and the traceless rank-2 part is
Frobenius-orthogonal to it; numerically `c₂/c₀` collapses `14.6×` under
refinement.
Against these: **one positive** — v6 paper 1's causal-set arc **does**
recover the full inverse spatial metric tensor from *order + number*, at
`[PROBE]` grade, correlation `+0.99`, explicitly *"excluding an
isotropic/scalar coefficient"*.

**Clause 2 — the principal's split is NOT the corpus's split, and the
corpus proves it is not. `[THEOREM]`, and this is the note's main
correction.** The reading *real part → gravity, phase → quantum* fails at
the first component. The rank-2 gravity object decomposes as
**diagonal + off-diagonal**, and the corpus's own arithmetic
(`v2/…paper10…:1315-1327`) is that the real/squared channel keeps the
diagonal `|z_1|²`, `|z_2|²` and **loses the off-diagonal
`Re(z_1 \bar z_2)` — "the relative phase"**. Restated at sealed scope
(`v6/…paper5…:795-797`): magnitude-only and unoriented data **leave the
`χ^{NN}` split alive**; only the *oriented* holonomy closes it. **The
gravity side needs the orientation datum too. The even channel alone
delivers a diagonal metric — an axis-aligned geometry with no rotation
content — which is exactly what
`v2/…paper10…:1653` offers as the fallback: "restrict the Gamma-level
theorem to diagonal/axis-aligned metrics."**

**Clause 3 — spin-2 vs `SU(2)`: not conflated in the corpus, and the
adjudication is clean. `[MEASURED]` by exhaustive grep.** Every "2" on the
gravity line is one of: **tensor rank** (`h^{ij}`, `T_⟨ij⟩`, `C^{ij}`,
`χ^{NN}_{a,ij}`, the quadrupole `Q_{ij}`); a **component count**
(`4/9` priced, `5` traceless, `5→2` after TT projection, `9` traceless of
`10` symmetric); a **codimension or signature** (`SO(1,1)` on the
codimension-2 normal plane); a **helicity count**; or a **spatial
dimension** (`d ≥ 2` for Gate 2). **None is a gauge group.** Symmetrically,
every `SU(2)` in the corpus is a **gauge/internal-symmetry** object living
in the Yang–Mills arc, the Bloch/celestial kinematic line, or the
Standard-Model floor — never in a gravity paper. **The two "2"s are
disjoint in the corpus. The conflation is not there to be found; it would
be introduced by importing it.**

**Clause 4 — `SU(2)`'s foothold, priced exactly. `[IMPORT]`.** On the
gravity line: **zero**. Elsewhere: assumed as the *"baby version"* in the
YM arc; **rejected** by the one selection screen ever run
(`v3/…paper22…:5754`), which was then voided; **supplied** and explicitly
insufficient in v10 paper 11; **imported** in v10 D15; present as a `Z/2`
lifting *sign* in v4 paper 40; and reachable only as a `U(2)` degeneracy
group of an **assumed** 2-dimensional ledger fiber (v6 p7 Thm 10.3), inside
a Standard-Model inverse problem the corpus **poses and does not solve**.
**Bringing `SU(2)` into the gravity/even-channel reading would be a pure
import, and would be the first gauge group ever attached to a gravity
paper in this corpus.**

**Clause 5 — the corpus already owns the ALGEBRAIC form of the
principal's dichotomy, in two places, and has never stated it.
`[MEASURED]` + `[STATED]`, joined here.** v6 paper 53 (`:24-30`): the
**commutator** of two transports is *"antisymmetric → a rotation"* and
dies against a symmetric source by an exact selection rule
(*antisym·sym = 0*). v6 paper 54 (`:22-24`): the **anticommutator** of two
transports *"is a traceless symmetric rank-2 tensor that **can** couple to
the spin-2 shear (measured symmetric fraction = 1.000)"*. And v2 paper 10
(`:1825`): `½{γ^i, γ^j} = h^{ij} I` — **the anticommutator of two
directional generators IS the metric.** **Odd part → rotation/phase; even
part → rank-2 metric/gravity. That is the principal's reading, and it is
the corpus's own algebra.** What the corpus does *not* have is the other
half of the Clifford pair: `[γ^i, γ^j]`, the spin-group generator, is
**written nowhere in v1–v10.** `[SILENT]`.

**Clause 6 — why the generated line cannot currently carry it, stated
concretely. `[MEASURED]`.** The even channel in the surviving form is
`K(E) = k·E_total` with `k = 0.03125` a constant and
`E_total = Σ_{j=1}^{3} E_j` a **trace** (`p30:2961`,
`p30_complex_amplitude_campaign.py:725`); nothing in paper 30 is
differentiated with respect to anything; the `3×3` **even reflected Gram**
`G^{even}_{jk} = Σ_R P(R) E_j(R) E_k(R^*)` exists, is computed exactly,
its principal minors printed (`:2991-2997`), and is then **discarded**;
the odd metric `M_{jk}` is asserted but only its **diagonal** was ever
scanned (253 diagonal triples, `:3284`, selecting `diag(5,5,3)`). In v10
the picture is starker: **no Gram, no bilinear form, no Hessian, no
inner product, no pairwise angle exists anywhere**, D58's `ω` factorizes
to a chart-size ratio, D32's distance is ranking-only, and the one genuine
two-index object — D64's chart transitions — **measured `H¹ = 0`, pure
gauge**, under a hard width-≤4 cap.

**Clause 7 — the precedent that any even-channel gravity proposal must
answer, and it is negative. `[MEASURED]`.**
`v6/…paper4…:1021-1029` + `:1064`: a scalar potential equation supplies
**one** response component per screen atom; a symmetric rank-2 equation
needs **three** in `d=2`; the corpus ran the count and printed
**`missing_components = 8193`, `FAILS-FULL-GR`**. **A scalar `K` cannot
become a metric by interpretation. It has to become a form.**

---

### THE PINNABLE CLAIM

> **P2 (the even-channel rank-2 pin).** *The gravity-side counterpart of
> D71b's P1 is not a group but a FORM: the corpus's rank-2 gravity object
> is the SYMMETRIC (anticommutator/even) part of a transport pair —
> `½{γ^i,γ^j} = h^{ij}I` (`v2 p10:1825`), `C(θ)=½{K(0),K(θ)}`
> (`v6 p54:18`) — and the generated line's realisation of it is the EVEN
> REFLECTED GRAM `G^{even}_{jk} = Σ_R P(R) E_j(R) E_k(R^*)` already
> computed at `v7 p30:2991-2997` and discarded in favour of its trace
> `E_total`. Concretely: `K` should be `K(E) = E^⊤ N E` for a
> positive-definite `N_{jk}`, not `k·ΣE_j`; the corpus's own no-go says a
> scalar cannot be a metric (`v6 p4:1064`, `missing_components = 8193`);
> and the datum that decides whether this is geometry or bookkeeping is
> the ORIENTATION — the same `Z/2` that Prop 10.6 and `χ^{NN}` both turn
> on.*

**Attachment point, named.** `G^{even}_{jk}` on the three dual-even
channels of the rooted boundary law, receipt
`v7/code/p30_reflection_positive_campaign.py:394-406` — **already written,
already run, already exact.** The corresponding v10 object does not exist;
the nearest slot is D64's chart-pair transition, and it measured trivial.

**Testable how, at fixture scale, on committed objects.**

1. **The un-tracing test (free, the receipt exists).** Re-run
   `p30_reflection_positive_campaign.py` and report the **off-diagonal**
   entries of `G^{even}_{jk}`, not only its principal minors. Ask: is
   `G^{even}` proportional to the identity (then `E_total` loses nothing
   and the even channel is genuinely scalar), or does it have non-trivial
   anisotropy (then the law has been throwing away a metric)? **The corpus
   printed the minors and never printed the matrix.**
2. **The generalised-`K` test.** Replace `K(E) = k·E_total` by
   `K(E) = E^⊤ N E` on the same `N=5..9` window and re-run the four
   campaign checks paper 30 already gates on (even-absolute compression,
   dual conjugation, atom-average collapse, `TV_9`). Pre-registered: if
   **every** `N` matches `diag(k,k,k)`'s `TV_9 = 1.676e-5`, the even
   channel is provably trace-only at this window and the gravity reading
   dies on this substrate. If some `N` improves it, the even channel
   carries anisotropy and §7's pin has its first evidence.
3. **The orientation test (the cross-link to D71b's P1).** `χ^{NN}` is
   determined by the *oriented* `SO(1,1)` holonomy and undetermined by the
   unoriented one (`v6 p5:837-846`). D71b's P1 asks whether `A_D` is odd
   under paper 30's order-dual `*`. **These are the same question asked of
   the two channels.** Run them in one unit: form the even and odd parts
   of the same transport pair and ask whether the even part carries the
   Gram anisotropy while the odd part carries the sign.

**Falsifiers, pre-registered.**

* **F1.** `G^{even}_{jk}` is diagonal, or is a multiple of the identity.
  Then `E_total` is lossless, `K` is correctly scalar, and the even
  channel provably cannot host a metric on this substrate. **P2 dies
  cleanly, and the corpus gains a no-go it does not have.**
* **F2.** A quadratic `K(E) = E^⊤NE` cannot match the committed `TV_9` for
  any `N` including `N = diag(k,k,k)`. Then the generalisation is
  inconsistent with the receipted law and the form is wrong.
* **F3.** The even/odd algebraic split of §3 does not survive transfer:
  the anticommutator of the generated line's own transports is not
  symmetric, or is not rank-2. Then §3.2's table is a coincidence of two
  imported representations and should be struck.
* **F4.** `χ^{NN}`-analogues on the generated line are determined by
  unoriented data. Then the orientation is not the shared missing datum,
  Clause 2's unification of the gravity and phase no-gos fails, and the
  principal's clean split survives after all — **which would be the most
  interesting outcome and is the one this note would most like to be
  wrong about.**

**F1 and F4 are the outcomes that settle the question negatively, and both
are as publishable as a positive.**

---

## §8. Coverage, limits, and four corrections to the brief's premises

**Searched.** Corpus-wide `grep -rniI` over `v1 … v10`, `publishable/`,
`v6/publishable/`, `v6/paper7-superseded-editions/`,
`_archive_low_value_2026-06-14/`, `external/`, isp-root loose papers and
`.html`, `code/`, `v7/code/`, `v8/code/`, `v10/code/`, plus
`~/workspace/physics`, for: `spin-2`, `spin 2`, `rank-2`, `rank 2`,
`graviton`, `SU(2)`, `SU(3)`, `SU(N)`, `tensor mode`, `quadrupole`,
`helicity`, `traceless`, `h_{mu nu}`, `linearized`, `Weyl`,
`Einstein equation`, `stress tensor`, `T_{mu nu}`, `Clifford`, `Spin(3)`,
`spinor bundle`, `anticommutator`, `extrinsic curvature`,
`second fundamental form`, `Hessian`, `Fisher`, `susceptibility`,
`Gram`, `bilinear`, `inner product`, `quadratic form`, `two-point`,
`metric`, `non-abelian`, `braid`, `path-ordered`, `matrix-valued`,
`Wilson loop`, `commutator`, `structure constant`. Read in full or in the
relevant sections: `stochastic-curvature-gravity-investigation.md`,
`v2/…paper10…` §4–§8 and §11–§14, `v3/…paper9…` §9,
`v3/…paper22…` §31, `v6/…paper1…`, `v6/…paper4…` §, `v6/…paper5…` §10–§12,
`v6/…paper7…` §10, `v6/…paper8…` §9, `v6/…paper18…`, `v6/…paper31…`,
`v6/…paper39…`, `v6/…paper52…`, `v6/…paper57…`,
`v6/publishable/paper-IV-graded-weyl.md`, `paper-XI…`, `companion-E…`,
`_archive…/paper53.md`, `_archive…/paper54.md`,
`v7/…paper10-spin2-carried…`, `v7/…paper30…` §24–§27,
`v8/…paper4-gravity-continuum.md`, `v8/LEDGER.md` #103–#130,
`v10/…paper11…`, `v10/THE-THEORY-SO-FAR.md` §C2, `v10/note-d15…`,
`v10/note-d32…`, `v10/note-d47…`, `v10/note-d58…`, `v10/note-d64…`,
`v10/note-d66…`, `v10/note-d67…`, and both baseline notes.

**Not done here, and it matters. No number above was recomputed.** v2 p10's
propositions, v6 p5's determinacy campaign, v6 p52's `14.6×` collapse,
v6 p54's `0.925` and `1.000`, v6 p1's `+0.99`, v7 p10's sympy receipts,
v7 p30's Gram minors and `TV_9` values, and v10's D64/D66/D67 censuses
were all taken at their published grade. **In particular §7's test 1 —
printing `G^{even}`'s off-diagonals — is a claim about what the receipt
*would* show; it has not been run, and if `G^{even}` is diagonal, F1 fires
immediately.**

**Correction 1 to the brief.** *"Graviton spin-2-blind"* is not paper 57's
statement. Paper 57 §3 exists precisely to split it: the linearized spin-2
**equation** is `[DERIVED, mod (R) + gates]`; only the spin-2 **charge** /
propagating graviton is `[OBSTRUCTED]`. The unqualified "spin-2-blind"
belongs to **paper 52** (about the static modular *currency*) and to
`V6_STATUS_AUDIT.md:128` (about papers 52–55 as a block).

**Correction 2.** Paper 57 does **not** use the book's
`[THEOREM]/[MEASURED]/[STATED]/[POSITED]` scheme. Its tags are
`[DERIVED]/[NO-GO]/[OBSTRUCTED]/[OPEN]` (`paper-XI:5`). v7 paper 10 uses a
third scheme, `[OWNED]/[LEVER]/[BLIND]/[WALL]` (`:5`). This note reproduces
each paper's own tags rather than translating them.

**Correction 3.** Paper IV, *"graded-Weyl"*, is **not gravity and has no
rank-2 object.** It is `Hearing the regularity of a diffusion coefficient:
a graded local Weyl law` — a 1-D Sturm–Liouville heat-kernel paper on a
**scalar** coefficient `c(x)`, where "Weyl" is Weyl's eigenvalue-counting
law. Grade: `v6/publishable/PLAN.md:71` — *"READY as EXPERIMENTAL
MATHEMATICS"*. Its 2-D port keeps `c` scalar and isotropic, and `:470`
names the anisotropic (genuinely rank-2) generalisation as an **unbuilt
sequel**. The rank-2 elliptic theorem that would be that sequel exists
elsewhere: `v6/relativistic-isp-v6-paper15.md:37-45`, a `Sym_d` symmetric
tensor class with `l₀|ξ|² ≤ ξ^⊤C(x)ξ ≤ L₀|ξ|²`, **`THEOREM`, proved modulo
two audited cell constants** — but `C` there is an *assumed class*, not a
derived field, and the paper is homogenization, not gravity.

**Correction 4.** The v5P2 gravitational-decoherence line is **rank 0
throughout**: `spin-2`, `rank-2`, `graviton`, `traceless`, `quadrupole`,
`helicity`, `tensor` return **zero hits** in
`v5/…paper2…` and in `gravitational-decoherence-indivisible.tex`; the
coupling is the scalar Newtonian self-energy
`E_G = (G/2)∫∫ δρ(x)δρ(y)/|x−y|` (`:139-143`). And the corpus itself names
the type mismatch that matters most here —
`v6/publishable/companion-E-covariant-decoherence.md:48`:

> "the natural Tier-A object — the odometer content `χ` — is a **weight-0
> scalar KL *number*, the wrong *type* to be a two-point correlation
> function `G(s²)`**; it cannot even be evaluated on the kernel's
> spacetime-interval domain without importing the very emergent geometry
> under test."

**A live inconsistency, flagged, owned by nobody.** `V6_STATUS_AUDIT.md:138`
states *"the corpus has … **no Einstein equation**, no Newton constant on
any free record lattice, and no graviton"*, while paper 57 `:105` and
paper-XI `:110` grade the linearized traceless Einstein equation
**`[DERIVED, mod (R) + gates]`**. The audit either predates or discounts
paper 57 §1.4's null-cone lemma, and no erratum owns the disagreement.
**This is the gravity-line twin of D71 Clause 1's unowned phase
contradiction, and it should be resolved in the same reading pass.**

**Reading claims, flagged.** §1.1's observation that the "2" hunt and the
phase hunt are sibling memos; §2.2's identification of v2 p10's lost sign
with v6 p5's lost orientation; §3's table joining the
commutator/anticommutator split across v2 p10, v6 p53 and v6 p54; §4.3's
parallel between v6 p52's trace-pricing and v7 p30's `E_total`; and
Clause 5's reading of the Clifford pair are all **`[MY READING]`**. Every
constituent clause is quoted verbatim with file and line; the joins are
this note's and are load-bearing on nothing except §7's pin.

**§7's pin is a draft**, offered in D69's sense: to be frozen, amended or
discarded.
