# D71b — is the odd-channel phase the holonomy of probability transport? A dichotomy/identity adjudication

**Status: ARCHAEOLOGY SURVEY (extension of D71), 2026-07-27. NOT a pin,
NOT a receipt, NOT a result.** Nothing below is new evidence. Every number
and every quoted sentence is copied from a committed file and attributed
by path and line. The only forward-looking objects are §5's pinnable claim
and its falsifiers, which are a suggestion for the principal to freeze,
amend or discard.

**The question, as put.** *Very early ISP framed itself as asking whether
quantum interference can be understood as the HOLONOMY OF PROBABILITY
TRANSPORT itself. v7 paper 30's surviving amplitude form is
`A(R) ~ e^{-K·even}·e^{iΦ·odd}`. Is this a DICHOTOMY — two rival phase
origins to adjudicate — or does `e^{iΦ·odd}` COME FROM the holonomy of
probability transport, an IDENTITY in which holonomy is what the phase IS
and the odd channel is where it SITS?*

**The short answer, before the evidence.** **Neither a dichotomy nor a
completed identity: the corpus contains the identity in two halves,
written eleven years of programme-time apart, each half stated
explicitly, and the one sentence that welds them is nowhere in the
corpus.** The v6 half says *holonomy is the phase*: v6 paper 7 Theorem 7.1
derives that the retained holonomy of a **closed route pair** is valued in
`SO(2) = U(1)`, and Theorem D3 proves that two-route interference **is**
the loop-phase law `P = |A|²+|B|²+2|A||B|cos(arg B(loop))` at machine gap
`2.8e-17`. The v7 half says *the phase sits on the reversal-odd channel*:
v7 paper 30 defines `*` as **order reversal** (`:2506`–`:2511`), defines
`O = F − F*` as what is odd under it (`:2732`), and then states in its own
words the exact algebraic signature of a holonomy — "**dual reversal sends
`O` to `−O`; therefore dual reversal sends `L` to its complex
conjugate**" (`:2848`–`:2849`) — with dual-conjugation error **exactly
`0`** against `1.82` for the naive alternative. Conjugation under reversed
traversal is *the* defining property of a holonomy phase. **The corpus
therefore nearly states the identity, from both ends, and never says it.**
Two things stop it from being a finished identity, and both are
load-bearing: v7's reversal is reversal of a **record's own order
relations**, not demonstrably reversal of a **closed transport loop**
(§3.4, `[SILENT]`); and v10's only non-zero phase-like class — D66/D67's
odd-ring parity — is provably **label-holonomy**, built from port-naming
conventions and touching the weights `q` **nowhere** (§4.1, `[MEASURED]`).
So: **IDENTITY at the level of *what a phase is*, BRIDGE-NEEDED at the
level of *which loop*.** Verdict and the pin in §5.

**Provenance labels** (book §0.1 convention, as in D71):
`[THEOREM]`/`[EXACT]` = argued depth-free and gated; `[MEASURED]` = true
on a declared finite window; `[DEFINITIONAL]`; `[STATED]` = asserted in
the corpus without derivation; `[SILENT]` = the corpus does not address
it; `[OPEN]`; `[MY READING]` = this note's inference, load-bearing on
nothing.

**Relation to D71.** D71 (`v10/note-d71-phase-archaeology.md`) answered
*where is the imaginary exponential*. It found the surviving form
(§1.N2), catalogued the reduction points (§2), ranked the empty slots
(§3), and flagged as `[MY READING]` that v7's even/odd channel split and
D66's odd-ring parity **might** be the same index (§3.5, §4(a)). **This
note does not repeat that survey.** It answers a different question — *is
the phase in that form the holonomy the programme set out to find* — and
in the course of answering it, **it settles D71 §3.5's flagged
identification in the negative at the mechanical level** (§4.1) while
finding a *different* and stronger bridge D71 did not see (§3.2, §3.3).

---

## §1. The original framing, exactly as written

### 1.1 The sentence

The target sentence exists in the corpus **exactly twice**, byte-identical,
and nowhere else:

* `/Users/felixrobles/workspace/isp/README.md:43-44`
* `/Users/felixrobles/workspace/physics/README.md:17-18`

Verbatim, with the thesis it unpacks (`README.md:37-44`):

> The central thesis is:
>
> > Quantum phase is not a primitive add-on to probability.  It is the
> > geometric curvature, or exchange defect, of real stochastic transports
> > across incompatible Cauchy hypersurfaces.
>
> Put more simply: the framework asks whether quantum interference can be
> understood as the holonomy of probability transport itself.

`physics/README.md` is an earlier snapshot of the same document; D71 §5
already established that `~/workspace/physics` is a superseded HTML mirror
of the v1 material. Nothing there adds to this.

### 1.2 What "probability transport" MEANT operationally

The same README defines it, mechanically, immediately below
(`README.md:87-115`):

> ## Exchange Defect As Stochastic Curvature
>
> In differential geometry, curvature can be detected by parallel
> transporting a vector around a small loop.  If the vector comes back
> rotated, the loop has holonomy; the holonomy measures curvature.
>
> ISP applies the same idea to probability transport.
>
> The objects being transported are not vectors in a primitive Hilbert
> space.  They are finite probability records and stochastic kernels.  But
> the same logic appears:
>
> 1. Start with a finite record distribution on a hypersurface.
> 2. Apply one localized stochastic deformation.
> 3. Apply another localized stochastic deformation.
> 4. Reverse the order.
> 5. Compare the two resulting transports.
>
> If the two orders disagree, the stochastic transport has curvature.
>
> The thesis is that the complex phase behavior of quantum mechanics is the
> effective shadow of this stochastic curvature.  Interference is not
> inserted as a mysterious complex rule at the beginning.  It is recovered
> as the observable effect of noncommuting finite probability transports.
>
> In slogan form:
>
> ```text
> quantum phase = stochastic holonomy
> ```

**So, operationally, at the founding:**

| slot | the founding answer |
|---|---|
| what is transported | finite probability records and stochastic kernels (`:95-96`) — **not** Hilbert vectors |
| along what | localized stochastic deformation maps, playing the role of parallel transports (`:89-90`, `:100-101`) |
| what closes the loop | **do A then B; do B then A; compare** (`:99-103`) — the loop is the commutator square, and its defect is the "exchange defect" |
| what the holonomy is | the disagreement between the two orders (`:105`) — a **reversal/reordering defect** |

The same construction in bundle language,
`first-principles-conceptual-leap.md:11` (byte-identical in `physics/`):

> "Treat a relativistic indivisible stochastic process as a **stochastic
> connection on the bundle of configuration probability simplices over
> Cauchy hypersurfaces**, with localized finite deformation maps as
> parallel transports and exchange defects as the curvature/holonomy of
> that connection."

And the programme's own grade on it, `first-principles-conceptual-leap.md:31`:

> "Quantum phase is not a hidden supplement to probability; it is the
> curvature data required for consistent stochastic transport across
> incompatible hypersurface cuts. **This is not yet a theorem.**"

**Grade: `[STATED]`, self-graded as not-yet-a-theorem, since v1.**

**The single most important structural fact in this section, and it is
what makes the whole question tractable: the founding loop is a
REVERSAL.** The loop that carries the holonomy is not an arbitrary closed
curve. It is *do-then-undo-the-order*: `T_B T_A` against `T_A T_B`. Every
downstream appearance of the object inherits that shape, and §3 shows the
v7 amplitude form inherits it too.

---

## §2. The holonomy thread, end to end

`grep -rni holonomy` over `v1 … v10`, isp root, `code/`, and `physics/`
returns hits in 60+ files. Removing the gauge-theory homonym (`v1` p10,
`v3` p10, `v4`'s YM/GCR line, the loose `.html` papers — these are Wilson
loops of a *gauge field*, not of probability, and are not this thread),
the actual thread has **nine** members. For each: **what the object IS**,
**whether it is a loop object and what loops**, **what rides on the
loop**, and **its grade**.

| # | where | the object, mechanically | loop? | what rides | grade |
|---|---|---|---|---|---|
| 1 | `README.md:99-105` | order-comparison defect of two localized stochastic deformations | yes — the commutator square | probability records / stochastic kernels | `[STATED]` |
| 2 | `v5/…paper4…:69-73`, `:257-271` | `H(A,B) = compare(A after B, B after A)`; formally `H_γ = K_{γ_n}⋯K_{γ_1}K_{γ_0}^{-1}` | yes — a word γ comparing two licensed transport paths with the same endpoints | abstract "transport comparison maps" `K`, never tied back to `q` | `[STATED]` |
| 3 | `v6/…paper4…:187-191` | `Δ_AB = T_B T_A − T_A T_B` — the exchange defect | commutator square | record transports | `[STATED]`/`[POSITED]` |
| 4 | `v6/…paper4…:396-403` | "retained exchange holonomy": complex amplitudes `c_0, c_1 = e^{iφ}c_0` per alternative | **not defined as a loop here** | complex amplitudes | `[STATED]` (posited) |
| 5 | `v6/…paper4…:2607-2645`, §34–35 | `A_D = log dP_AB/dP_BA`, the exchange cocycle | **yes** — "eventless exchange … commuting/eventless **loop** has zero action" (`:2637`) | **probability**: an RN derivative of two ordered path laws | `[MEASURED]`, 6 PASS rows, gaps `≤ 6.7e-16` |
| 6 | `v6/…paper4…:3052-3059`, §40 | the **closed-holonomy cochain**: Walsh/Möbius contrasts `χ_C(ω) ∈ {−1,+1}` on closed exchange/intervention experiments | **yes** — closed histories | sign-valued (`Z/2`) contrast coefficients of a log-density | `[MEASURED]`, and `FINITE-NO-GO` for selection (`:5033`) |
| 7 | `v6/…paper7…:612-618`, Thm 7.1 | **the retained holonomy of a closed route pair, valued in `SO(2) = U(1)`** | **yes — explicitly "a closed route pair on a sealed screen"** | a rotation-group element = **the phase itself** | `[THEOREM]` at v6 scope, **contested** (D71 Clause 1) |
| 8 | `v6/…paper7…:676-689`, Thm D3 | Bargmann loop products `B(ℓ)=∏_k U_{i_{k+1}i_k}`; interference `= P = \|A\|²+\|B\|²+2\|A\|\|B\|cos(arg B(loop))` | **yes** | unitary matrix elements; **the gauge-invariant content is the loop class** | `[THEOREM]`, machine gap `2.8e-17` |
| 9 | `v10/note-d64-…:54`, `note-d66-…:567`, `note-d67-…:431` | Čech 1-cochain on the SKY-B chart-atlas nerve; `H¹ = 0` wide, non-zero `Z/2` "port-flip obstruction" on odd rings at `ARBLOSE` | yes — loops in the **nerve** | **wire-word / port LABELS. No weights.** (§4.1) | `[MEASURED]`, five ring sizes, explicitly **not** claimed as `H¹ ≠ 0` |

Three further members are downstream re-uses rather than new objects, and
are listed for completeness: `v5/…paper9…` (braid-group representation
`ρ(B)` — a *non-abelian* holonomy, explicitly contrasted with phase:
"exchange operations **do not merely add phases**", `:138-140`);
`v6/…paper5…:717-723` (`Z^⊥_{a,ij}`, the oriented `SO(1,1)` normal-frame
boost holonomy of the gravity channel — a genuine loop object, but
transporting **frames**, not probability); and `v6/…paper56…:72` (the
gravitational which-path `U(1)` holonomy `e^{iΦ}` accumulated **between
seals** — a *temporal* interval, not a spatial loop).

### 2.1 Three findings from the thread that bear directly on the question

**(a) The programme's own primitive IS a holonomy object, and v7/v8 say so
in their opening line.** `v7/relativistic-isp-v7-paper1-record-click-law.md:15`:

> "A record is a *sealed finite **holonomy** diamond* (the primitive of
> SHARD): a self-contained finite parcel
> `D = (Ω_D, μ_D, screens, collar, transports)` whose **physical content
> is the closed exchange-defect holonomy `Δ_AB = T_B T_A − T_A T_B`**, and
> which becomes an **event** when a count-symmetric idempotent proposition
> `E` commits."

Repeated verbatim at
`v8/relativistic-isp-v8-paper1-foundations-click-law.md:13`, there tagged
**`[POSITED]`, v6 Paper 4**. **This matters more than any other single
line in this note: v7 paper 30's `R` — the record whose even/odd channels
carry `K` and `Φ` — is, by the same version's own definition, a closed
holonomy object.** The odd channel is therefore not *rival* territory to
the holonomy; it is a decomposition of the holonomy diamond's own boundary
data. `[STATED]`.

**(b) The programme's clock is already a forward-vs-reverse transport
comparison, and it is REAL.**
`v7/…paper1…:32` — the content `χ` is

> "the arrow/entropy-production functional — a *pure number*, the relative
> entropy between the **forward and reverse holonomy-transport laws**."

`v8/…paper1…:19` grades it **`[IMPORT]`** (Schnakenberg entropy
production). And `v6/…paper4…:2636`, the receipt row:

> `| antisymmetry | reverse ordering has action -A_D | orientation reversal is fixed | gap=2.2e-16 | PASS |`

So the corpus **already has** a reversal-odd probability-transport object,
receipted, and it is **`A_D`, a real logarithm** — not a phase. `[MEASURED]`.

**(c) On a commit path the holonomy is trivial by construction — so any
non-trivial phase must live off it.**
`v8/…paper1…:77`:

> "On a one-dimensional commit path `H¹ = 0`, so 'concatenation-additive
> content ⟺ coboundary of a potential' is an *identity* — a lemma sitting
> on the `[DEFINITIONAL]` odometer of §3.2, **not new dynamics**."

And v7 paper 2 makes the same point positively:
`v7/…paper2…:23` — "**The content increment is the coboundary of the
holonomy potential. [FORCED]**", with `:31` naming the identification of
that potential with the corpus's closed-holonomy cochain as **the
physical-input layer**, not the theorem.

**This is a hard structural constraint on the whole question and it has
never been stated as one.** `[MY READING]`, from three quoted
`[DEFINITIONAL]`/`[FORCED]` clauses: *along the commit order there is no
holonomy to have.* Whatever non-trivial holonomy the programme is looking
for must live on a cycle that is **not** a commit path — which is exactly
where D64 found `H¹ = 0` (wide record) and where D66 found its only
non-zero class (the odd conflict **ring**). The geometry of the search is
already fixed by the corpus; nobody has written it down.

---

## §3. The identity test: is there a mechanical bridge?

### 3.1 What `E` and `O` actually are

The brief asked whether v7 paper 30's `O` is loop-shaped or
reflection-shaped. It is **reversal-shaped**, and the definition is
unambiguous.

`v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2506-2511`:

> Let `\ast` denote the order-dual operation on a five-record sector:
>
> ```math
> F^\ast = \text{the same five-record type with every order relation reversed}.
> ```

`:2724-2735`:

> For a dual pair `(F,F*)`, define:
>
> ```math
> E_F(R)=F(R)+F^\ast(R),
> ```
>
> the even count, and:
>
> ```math
> O_F(R)=F(R)-F^\ast(R),
> ```
>
> the dual-odd imbalance.

**So `E` and `O` are the even and odd parts of a record observable under
REVERSAL OF ALL ORDER RELATIONS.** `[DEFINITIONAL]`. Not under a spatial
reflection; not under a parity of counts; under **reversal of the record's
own order** — which, in a programme whose time *is* the commit order
(`v7/LONG_MARCH_PLAN.md:25`: "time from the commit order"), is reversal of
traversal.

### 3.2 The near-statement — and it is nearer than D71 recorded

`v7/…paper30…:2843-2849`, immediately after `L_dual = e^{-kE}e^{iθO}`:

> Here:
>
> - `E` is dual-even data, such as `F+F*`;
> - `O` is dual-odd data, such as `F-F*`;
> - **dual reversal sends `O` to `-O`;**
> - **therefore dual reversal sends `L` to its complex conjugate.**

repeated in the paper's own headline rule, `:4205-4207`:

> - `\Phi` is a phase on the odd channel only;
> - **dual reversal conjugates `A`;**

with the receipt result `:2838`, `:2851`:

> ```text
> max dual-conjugation error = 1.8210207227600682556870097725525   (naive)
> max dual-conjugation error = 0                                    (L_dual)
> ```

**This is the mechanical core the brief asked whether anyone had stated.**
Spelled out:

> *A holonomy phase is precisely the object that conjugates when you
> traverse the loop backwards.* `Hol(γ^{-1}) = Hol(γ)^{-1} = \overline{Hol(γ)}`
> for a `U(1)`-valued holonomy. v7 paper 30 proves, at receipt grade with
> error exactly `0`, that **its surviving amplitude has exactly this
> transformation law under reversal of the record's order** — and that
> the *only* placement of the phase with this property is on the
> reversal-odd channel. Any other placement (the naive complexified decay)
> fails at `1.82`.

**The corpus states the transformation law. It never names it a holonomy.**
`grep -n holonomy` in `v7/…paper30…` returns hits at **`:3364`** and
**`:3395` only** — both inside Campaign T's corpus audit ("the transports
carry the internal exchange-defect holonomy"; "the record diamond has
intrinsic holonomy, screen, and collar data"), i.e. in the section that
rebases the paper onto the v6 diamond, and **neither is within 400 lines
of the `e^{iΦ(O)}` result.** The two halves are in the same paper, nine
sections apart, and never introduced. `[SILENT]` on the join.

### 3.3 The v6 half already says holonomy IS the phase — as a theorem

`v6/relativistic-isp-v6-paper7.md:612-618`, **Theorem 7.1**:

> "The **retained holonomy of a closed route pair** on a sealed screen is
> valued in the holonomy group of the 2-dimensional screen plane: the
> defect-free rotation group `SO(2) = U(1)` with canonical period `2*pi`
> (the silent-seam theorem). A retained alternative therefore carries
> canonically a nonnegative RN weight and a `U(1)` phase: the value space
> of an alternative is `R+ x U(1) cup {0} = C` as a SET, with the
> canonical `2*pi`. ∎"

`:676-689`, **Theorem D3 (loop phases are the retained holonomy)**:

> "…the Bargmann loop products `B(\ell)=\prod_{k}U_{i_{k+1}i_k}` are
> invariant (machine: `0.0e+00`), and **two-route interference is exactly
> the loop-phase law `P = |A|^2+|B|^2+2|A||B| cos(arg B(loop))`** (machine
> gap `2.8e-17`). Hence the gauge-invariant content of the dilation is its
> **loop class** — which is precisely the corpus' **closed-exchange
> holonomy cochain**, and Paper 4 Section 40 proves the complete ledger
> reconstructs that class uniquely (Möbius inversion). ∎"

And `:1529-1533` names the same object a **reflection** structure:

> "the exchange-cocycle antisymmetry `A_D = log dP_AB/dP_BA` (Paper 4
> Section 34) **is a reflection structure on ordered transports**"

with the Paper 10 update, `:1527`:

> "the exchange cocycle **is** the reflection structure (its expectation IS
> the entropy production = the order evidence) … and **reflection
> positivity becomes a THEOREM** for every eventless sector with a finite
> primitive Markov presentation."

**Read together with §3.2 this is the identity, in two documents:**

1. v6 p7 D3 — *interference **is** the phase of a loop holonomy*.
   `[THEOREM]`, machine `2.8e-17`, v6 scope, **contested** (D71 Clause 1:
   paper Va regrades `C` to an INPUT, v8 paper 2 puts the selecting bit in
   `ker R`, and no erratum owns the disagreement).
2. v6 p7 `:1529` / v6 p4 §34-35 — *the reversal structure on ordered
   transports is the exchange cocycle, and "reflection" in this corpus
   **means** order-reversal.* `[THEOREM]` at eventless scope,
   `[MEASURED]` gaps `≤ 6.7e-16`.
3. v7 p30 `:2848` — *the surviving amplitude conjugates under order
   reversal, and only the odd channel can carry the phase.*
   `[MEASURED]`, error exactly `0`.

**(1) says holonomy is what the phase is. (2) says the corpus's
"reflection" is loop-reversal. (3) says the phase must sit where
reversal acts by `−1`. Chain them and you get the principal's identity.
No document in the corpus chains them.** `[MY READING]`, and the whole of
§5's pin is the test of it.

### 3.4 Where the chain is genuinely weak — the one real gap

The chain has one soft link, and it should not be papered over.

**v7's reversal reverses the ORDER RELATIONS OF A RECORD TYPE. v6's
reversal reverses the TRAVERSAL ORDER OF TWO TRANSPORTS.** These are not
proved to be the same operation.

* v6: `A_D = log dP_AB/dP_BA` — reverse *which transport you applied
  first*. The "loop" is the commutator square `T_A T_B` vs `T_B T_A`
  (`v6/…paper4…:2637`: "commuting/eventless **loop** has zero action",
  rms `0.0e+00`).
* v7: `F^* =` the same five-record type with **every order relation
  reversed** (`:2511`) — reverse the *causal order inside the record*,
  a poset-dualisation of a boundary flag in the record deletion graph.

There is a natural reading on which these coincide — in a programme where
time *is* the commit order, dualising a record's order relations *is*
running its transports backwards — but **the corpus nowhere argues it, and
this note does not claim it.** `[SILENT]`. This is precisely the
`[MY READING]` boundary, and §5's pin is designed so that a *negative*
answer is as informative as a positive one.

A second, smaller gap: v7's `F` is a **five-record type**, i.e. a
*path/order-type* object, and reversing it is a path reversal, **not
manifestly the traversal of a closed cycle**. The corpus's own closure
device for the deletion graph is **deletion/insertion drift** — the
round-trip defect of going down one level and back up
(`v7/…paper30…:1999`: "the receipt measures deletion drift from `N=9` to
`N=8` and insertion drift from `N=8` to `N=9`"; `:2332`: "`E_drift` is
normalized deletion/insertion pair-conflict **drift**"). **A
delete-then-insert round trip that fails to return you where you started
is loop-shaped in exactly the founding README's sense.** But the corpus
measures it in *pair-conflict counts*, never as a weight ratio or a phase,
and never calls it a holonomy. `[MY READING]` that it is the natural loop;
`[SILENT]` in the corpus.

### 3.5 One further link the corpus supplies and nobody used

v6 p7 D3 (`:687-689`) identifies the loop class with **the closed-exchange
holonomy cochain**, and v6 p4 §40 (`:3052-3059`) says that in a binary
finite presentation that cochain is **`χ_C(ω) ∈ {−1,+1}`** — sign-valued,
i.e. `Z/2`-valued, on **closed** exchange/intervention experiments.

`Z/2 = {±1}` is `U(1)` restricted to `θ ∈ {0, π}` — the first non-trivial
rung of exactly the phase v7 puts on odd data (D71 §3.5(iii) makes the
same arithmetic observation about v8's un-run signed-real class). **So the
corpus's own closed-loop holonomy object is, in binary presentation,
sign-valued** — which is the strongest available *a priori* reason to
expect any v10 realisation of it to show up as a `Z/2` class rather than a
`U(1)` one. That prediction is *correct* about D66 — and §4.1 shows the
D66 class is nevertheless the **wrong** `Z/2`.

---

## §4. The v10 objects, tested against both readings

### 4.1 D66/D67's odd-ring parity is LABEL-holonomy, not probability-holonomy. `[MEASURED]`, and it settles D71 §3.5's flag.

D71 §3.5 flagged `[MY READING]` that v7's even/odd channel and D66's
odd-ring parity **might** be the same index, and made testing it the
priority-1 unit. **The mechanical part of that test can be settled by
reading, and the answer is no.**

The instrument is D64's, re-run unmodified
(`note-d66-arbitration-crystal-result.md:306-308`). What D64's cochain is
built *from* is stated in its own pin, `note-d64-cocycle-pin.md:19-21`:

> "At grammar layer the charts exist (D63) and their overlaps are events
> shared between nearby skies — but as SET maps the overlaps are
> inclusions (D58's containment). **The transition content must therefore
> be in the per-chart LABELING of directions.**"

and `:34-37`:

> "**Coordinates (the committed-layer labeling):** each direction
> `f ∈ D_e(d)` is reached from `e` by P-paths… The label of `f` in chart
> `e` is the SET of register sequences (**wire words**, length `d` over the
> record's register alphabet) realized by P-paths from `e` to `f`."

The five instruments swept are **port-ordering conventions**
(`note-d66-…:313-321`): `REG`, `REGA`, `ARBLOSE` (losers, winners,
version), `ARBVFIRST`, `COV`. D67 says which one fires and what that
means, `note-d67-k4-double-grid-result.md:431-438`:

> "**What is NOT zero is the PARITY route, at ARBLOSE and nowhere else** —
> the **winner/loser port order**, on the DOUBLE-GRID schedule… **it is a
> property of the schedule and of that port convention, not of the
> proposer count.**"

and it is gauge-trivial in the larger group,
`note-d66-…:409-411`:

> "**The free-relabelling route trivializes every one of those cells** (0
> obstructions, 0 survivors, at every cell of the entire census). **What
> is obstructed is the *port* gauge group, not the existence of a global
> labelling.**"

with the licensed claim, `note-d66-…:558-563`:

> "the pair-conflict rings with an **odd** number of pairs per round carry
> a non-zero port-flip obstruction count at five measured ring sizes,
> whose magnitude is `R − 1` and therefore **not a ring quantity**, which
> does **not** survive the free-relabelling test, has **no** testable Čech
> triple behind it, and is therefore reported and **not** claimed as
> `H¹ ≠ 0`."

**And the crux, decided by absence:** the tokens `weight`, `probabilit`,
and a bare `q` occur **zero** times in the construction of the class
across `note-d64-cocycle-pin.md`, `note-d64-cocycle-result.md`,
`note-d66-arbitration-crystal-result.md` and
`note-d67-k4-double-grid-result.md`. **The class is a function of wire
words and port-naming conventions. It does not touch the arbitration
weights at any point.**

**Verdict on §4's first question: D66/D67's odd-ring holonomy is
label-holonomy — a gauge obstruction of a naming convention on the atlas
nerve — NOT the holonomy of probability transport.** `[MEASURED]`. It
transports *labels*; the founding object transports *probability records
and stochastic kernels* (`README.md:95-96`). **The identification D71
§3.5 flagged therefore needs a bridge it does not have, and this note
recommends the flag be downgraded rather than tested first** — the
cheaper and more decisive unit is §5's pin. (Note also: D66 *calls* its
own residue "the odd-ring **holonomy**", `note-d66-…:567`, and D67 never
uses the word at all — grep returns zero hits for `holonomy`, `loop`,
`cycle`, `traversal`, `reversal`, `orientation` in `note-d67-…`. The word
is D66's, not the instrument's.)

**One thing the parity class does keep.** It is `Z/2`, it is zero on every
even ring and non-zero on every odd ring at five sizes, and §3.5 above
gives the corpus's own reason to expect a *closed-loop* holonomy to be
sign-valued in binary presentation. That the right-shaped object turned up
on the wrong substrate is worth recording as a coincidence to be explained
or killed — **not** as evidence. `[MY READING]`.

### 4.2 The `∏√q` amplitude and the `W` slot — the right stuff, no loop

The brief's strongest candidate was D42b4's `∏√q`: transporting `√q`
around a loop with phases is *literally* the holonomy of probability
transport, since `√q` is an amplitude modulus. The object exists:

`note-d42b4-quantum-lift.md:15-18`:

> "**Q1 (the completion).** The lift assigns each complete depth-D
> **history** the amplitude **∏ √q** (the #152 budget amplitudes) on record
> ancillas; the global state is unit-normalized; incomparable-event
> isometries act on DISJOINT registers (the carrier structure) and
> therefore COMMUTE — so the decoherence functional is
> foliation-invariant BY OPERATOR IDENTITY… and every mu-ratio is
> preserved exactly (**Born = mu/Σmu**)."

**But it is assigned per complete history — a path object — and there is
no closure.** `loop`, `cycle`, `closure`, `holonomy` return **zero hits**
in `note-d42b4-quantum-lift.md`. So:

* **It is the right carrier.** `√q` of the record's own weights is exactly
  what the founding framing says should be transported (`README.md:95-96`),
  and unlike D66's class it *is* a function of the weights.
* **It has no loop.** It is transport along a history, not around a cycle.
  A holonomy needs a closure, and the only closure device in scope is
  deletion/insertion round trip (§3.4) — un-run in this form.
* **The phase slot on it is filled with `+1` without an argument** — D71
  Clause 3's finding, unchanged here.

Two small corrections to the brief's premises, both from reading:
(i) **"Born = K1" is not a D42b4 statement.** D42b4 says "Born = mu/Σmu"
(`:22`, `:72`); "Born = K1" is D44f's, about the `V_single/V_pair`
fixture (`note-d44f-foliation-and-measure.md:26`, `:59`) with `K1` the
uniform recorded order-click kernel of
`note-d42b2-elementary-click-refinement.md:23`. Different fixtures,
different claims. (ii) The **`W` slot** (D71 §3.2) is a *state-invisible,
weight-visible* datum — D62 `[EXACT]` T1(e) — but nothing in the corpus
makes `W` a loop variable either. `W` remains the sharpest *theorem*, and
the odd channel remains the only candidate with a *proposed form*; §4.2
does not change D71's ranking, it explains why: **the corpus has amplitude
moduli on paths and holonomy language on loops, and has never put them on
the same object.** `[SILENT]`.

### 4.3 Summary table — the four objects against the two readings

| object | is it a loop? | does it touch the weights `q`? | is it reversal-odd? | verdict |
|---|---|---|---|---|
| founding exchange defect (`README:99-105`, `v6 p4 Δ_AB`) | **yes**, the order-commutator square | **yes** — records and kernels | **yes**, by construction | the target object; `[STATED]` |
| `A_D = log dP_AB/dP_BA` (v6 p4 §34-35) | yes ("eventless **loop** has zero action") | **yes** — an RN derivative of two path laws | **yes**, `→ −A_D`, gap `2.2e-16` | **the holonomy of probability transport, realised — and REAL, not a phase** |
| v7 p30 `O = F − F*`, phase `e^{iΦ(O)}` | **not shown** — order-type reversal, no closure | yes — via `F` on records, and the click weight | **yes**, `→ −O`, and `A → Ā` at error `0` | **the phase with the holonomy transformation law, on an unclosed loop** |
| D66/D67 odd-ring parity `Z/2` | yes, in the atlas **nerve** | **no — zero occurrences of weight/probability/`q`** | not framed that way | **label-holonomy; not this thread's object** |
| D42b4 `∏√q` | **no** — per-history | **yes** — it *is* `√` of the weights | not framed that way | **right carrier, no loop, phase slot = `+1`** |

**The one row that answers the brief's question directly is row two.** The
corpus's realised holonomy of probability transport is `A_D`, it *is*
reversal-odd, and it is **real**. v7's phase sits on a *different*
reversal-odd channel of the *same* records. Whether these are one channel
or two is the pin.

---

## §5. THE VERDICT

**Clause 0 — the shape of the answer. NOT a dichotomy. `[MEASURED]` +
`[THEOREM]`, as marked.** There are not two rival phase origins in this
corpus. There is **one** origin, stated twice at theorem grade in v6
(`paper7:612` Thm 7.1: the retained holonomy of a **closed route pair** is
`U(1)`-valued; `paper7:676` Thm D3: two-route interference **is** the
loop-phase law, machine `2.8e-17`), and **one** placement, established at
receipt grade in v7 (`paper30:2848`: dual reversal sends `O → −O`,
therefore sends `L` to its complex conjugate; dual-conjugation error
exactly `0` against `1.82`). Nothing in the corpus proposes a *second*,
non-holonomic origin for the odd-channel phase. **A dichotomy would need a
rival, and there is none.** The discriminating experiment a dichotomy
would require is therefore **not** the right unit to run.

**Clause 1 — IDENTITY, at the level of what a phase IS. `[THEOREM]` at v6
scope, CONTESTED.** *Holonomy is what the phase is* is not a metaphor in
this corpus; it is v6 paper 7's Theorem 7.1 and Theorem D3, machine-gated,
with the interference cross-term literally equal to `cos(arg B(loop))`.
The contest is D71's Clause 1 and is unchanged: `v6/publishable/paper-Va`
regrades `C` to an admitted **INPUT**, companion-B calls the seal blind to
the selector, `v8/…paper2` puts the selecting bit in `ker R`, and
`v6/ERRATA.md` owns none of it. **The identity's *what* half is
established-but-disputed, and the dispute is a reading unit, not an
experiment** (D71 §4(b) already scheduled it; this note seconds it).

**Clause 2 — IDENTITY, at the level of the transformation law. `[MEASURED]`,
error exactly `0`, and this is the strongest single piece of bridge
evidence in the corpus.** A `U(1)` holonomy is *defined* by
`Hol(γ^{-1}) = \overline{Hol(γ)}`. v7 paper 30 proves its surviving
amplitude obeys that law under order reversal, and proves that **no other
placement of the phase does** — the naive complexified decay fails at
`1.82`. The corpus writes the law (`:2848-2849`, `:4205-4206`) and never
names it. **The odd channel is not an arbitrary slot that happens to hold
a phase; it is the unique slot on which a phase can transform like a
holonomy.** `[MEASURED]` on the claim; `[SILENT]` on the naming.

**Clause 3 — BRIDGE-NEEDED, at the level of WHICH LOOP. `[SILENT]`, and
this is the whole residual.** v6's reversal reverses **transport order**
(`T_A T_B` vs `T_B T_A`); v7's reversal reverses a **record's own order
relations** (`F*` = every order relation reversed). The corpus nowhere
argues these are the same operation, and v7's `F` is a *path* type with no
closure device attached — the only closure in scope is deletion/insertion
round-trip drift (`paper30:1999`, `:2332`), which the corpus measures in
pair-conflict counts and never as a weight or a phase. **The bridge is one
identification and one closure, and neither is written.**

**Clause 4 — the v10 candidate for the loop is the WRONG object.
`[MEASURED]`.** D66/D67's odd-ring `Z/2` is built from wire words and
port-ordering conventions; `weight`, `probabilit` and bare `q` occur
**zero** times in its construction; it is trivialised by free relabelling
(`d66:409-411`); and D67 scopes it to "**a property of the schedule and of
that port convention**" (`:435-438`). **It is label-holonomy, not
probability-holonomy.** D71 §3.5's flagged index identification would
therefore need its own bridge before it could even be tested, and should
be **demoted below** the pin proposed here.

**Clause 5 — the corpus's actual realised holonomy of probability
transport is REAL, and that is the deepest thing this survey found.**
`A_D = log dP_AB/dP_BA` is reversal-odd (`v6 p4:2636`, gap `2.2e-16`), is
zero on commuting/eventless loops (`:2637`, rms `0`), is built from
genuine path *probabilities*, and is v6 paper 7's own "**reflection
structure on ordered transports**" (`:1529`). It is the founding object,
realised — **and its value is a real logarithm whose expectation is
entropy production** (`v6 p7:1527`). Meanwhile v7 paper 30's reflection
audit says the *real* odd form is **negative definite** (reflected diagonal
`−26.05, −16.53, −29.78`) and becomes positive **only** after the `i`-twist
(`:3020`: "odd directions cannot be real positive observables; they become
positive as imaginary amplitude channels"). **So the corpus has a real
reversal-odd object where it needs a positive one, and a proof that the
odd sector is positive only when imaginary — and has never put those two
sentences on the same page.** `[MY READING]` on the juxtaposition; both
clauses quoted verbatim.

**Clause 6 — the structural constraint nobody stated. `[DEFINITIONAL]` +
`[FORCED]`, assembled here.** `v8/…paper1…:77` — "On a one-dimensional
commit path `H¹ = 0`"; `v7/…paper2…:23` — the content increment is
`[FORCED]` to be the **coboundary** of the holonomy potential, with `:31`
naming the identification of that potential with the closed-holonomy
cochain as **physical input**. **Along the commit order there is no
holonomy to have.** Any non-trivial phase must therefore live on a cycle
transverse to the commit order — which is where D64 looked (`H¹ = 0`) and
where D66 found its only non-zero class. The search geometry is already
determined by the corpus; §5's pin respects it.

---

### THE PINNABLE CLAIM

> **P1 (the reversal-holonomy identity).** *v7 paper 30's odd channel is
> the reversal-odd channel of a probability-transport holonomy, and its
> phase `e^{iΦ(O)}` is that holonomy: concretely, the order-dual `*` on a
> five-record type (`paper30:2511`) coincides, on the generated line's own
> objects, with the transport-order reversal `AB → BA` that defines
> `A_D = log dP_AB/dP_BA` (`v6 p4 §34`), and the amplitude
> `A(R) ~ e^{-K(E)}e^{iΦ(O)}` is the `U(1)` holonomy of `√q`-transport
> around delete-then-insert round trips of the record deletion graph, with
> `A_D` as its real part (log-modulus) and `Φ(O)` as its argument.*

**Why this is the right pin and not the previously scheduled one.** D71
§4(a) proposed testing whether v7's channel index equals D66's ring
parity. §4.1 above shows that identification has to cross a
label/probability divide first, so it is no longer the cheapest decisive
unit. **P1 crosses no such divide: both of its objects are functions of
the process's own probabilities.**

**Testable how, at fixture scale, on committed objects.**

1. **The reversal test (free, one computation).** Take the D42b4 lift at
   the F-PAIR fixture (`note-d42b4-quantum-lift.md:62-64`), form
   `A_D = log dP_AB/dP_BA` for the two orderings of an incomparable event
   pair (the receipt already exists as `code/v6_p4n_exchange_cocycle_law.py`),
   and separately form `F* ` by dualising the record's order relations.
   **Ask: is `A_D` odd under `*`?** The corpus has both halves receipted
   (`v6 p4:2636` at gap `2.2e-16`; `paper30:2848` at error `0`) and has
   never applied them to the same object.
2. **The closure test.** Compute the delete-then-insert round-trip transport
   of `∏√q` on the generated line's own deletion/insertion moves
   (`paper30:1999`) and ask whether the round-trip ratio is `1`. If it is
   `1` identically, there is no holonomy to have and P1 is dead on this
   substrate. If it is not, **its logarithm is a real holonomy and its
   argument is the empty phase slot D71 Clause 3 found filled with `+1`.**
3. **The dual-conjugation re-run.** Evaluate `L_dual = e^{-kE}e^{iθO}` on
   the *generated line's* even/odd channels — not v7's five-record
   flags — and check the dual-conjugation error that v7 measured at exactly
   `0`. This is D71 §4(a)'s successor step, and it survives intact.

**Falsifiers, pre-registered, each of which kills P1 cleanly.**

* **F1.** `A_D` is **not** odd under the order-dual `*` at the fixture —
  then v6's reversal and v7's reversal are different operations, Clause 3's
  bridge fails, and the corpus has two unrelated reversal-odd channels.
  P1 dies; the honest residue is a named coincidence.
* **F2.** The `√q` round-trip transport is **identically `1`** on every
  delete-then-insert cycle of the generated line — then the generated line
  is flat, has no holonomy of any kind, and D71 Clause 3's `+1` is a
  **theorem** rather than an unargued choice. P1 dies, and the corpus gains
  a no-go it does not currently have.
* **F3.** `L_dual`'s dual-conjugation error on the generated line's channels
  is non-zero — then the surviving v7 form does not transfer to v10's
  substrate, and the odd channel is a v7-local fact. P1 dies at the
  transfer step.
* **F4.** The round-trip defect exists but is **not** `U(1)`-valued — e.g.
  it is `R+`-valued only (pure modulus, no argument) — then the corpus has
  a real holonomy of probability transport and **no phase**, which is
  precisely Clause 5's tension resolved *against* the imaginary reading.
  P1 dies in its interesting direction and the founding slogan is refuted
  on its own substrate.

**Note that F2 and F4 are the outcomes that would settle the founding
question negatively, and both are as publishable as a positive.** The pin
is designed so that no outcome is a null result.

---

## §6. Coverage and limits

**Searched.** `grep -rniI holonomy` over `v1 … v10`, `publishable/`,
`v6/publishable/`, `v6/paper7-superseded-editions/`, isp-root loose papers
and `.html`, `code/`, `v7/code/`, `v8/code/`, plus
`~/workspace/physics`. Sixty-plus files with hits; the gauge-field
homonym (v1 p10's Peierls/Wilson `W[A] = e^{-iqΦ}`, v3 p10, v4's
GCR/YM line, the loose `.html` benchmarks) was separated by reading and is
**not** part of this thread — it is a holonomy of a *gauge connection*,
not of probability, and it is the largest false friend in the grep.
Read in full or in the relevant sections: `README.md`,
`first-principles-conceptual-leap.md`, `v5/…paper4…`, `v5/…paper9…`,
`v1/…paper10…`, `v6/…paper4…`, `v6/…paper5…`, `v6/…paper7…`,
`v6/…paper56…`, `v7/…paper1…`, `v7/…paper2…`, `v7/…paper30…` §23–25 and
§28 and §30, `v7/…paper42…`, `v8/…paper1…`, `v10/…paper7…`,
`v10/note-d64-*`, `v10/note-d66-*`, `v10/note-d67-*`,
`v10/note-d42b4-*`, `v10/THE-THEORY-SO-FAR.md` §C1/C3 and glossary.

**Not done here, and it matters.** **No number above was recomputed.**
v6 paper 7's Theorem 7.1/D3 machine gaps, v6 paper 4's exchange-cocycle
diagnostic, v7 paper 30's `p30_complex_amplitude_campaign` (11/11) and
`p30_reflection_positive_campaign`, and D64/D66/D67's censuses were all
taken at their published grade. The `weight`/`probabilit`/`q` absence in
the D64/D66/D67 construction was verified by grep over those four notes
**only**; the underlying receipt code was not read, and if the executable
consults weights the notes do not mention, Clause 4 weakens. **That is the
one check that would most cheaply falsify this note's own §4.1.**

**Reading claims, flagged.** Clause 2's *naming* of the transformation law
as a holonomy law, Clause 5's juxtaposition of `A_D`'s realness against
v7's negative real odd form, Clause 6's assembly of the `H¹ = 0` commit-path
constraint, §3.4's suggestion that deletion/insertion drift is the natural
closure, and §3.5's `Z/2`-expectation are all `[MY READING]`. **Every
constituent clause is quoted verbatim with file and line; the joins are
mine and are load-bearing on nothing except the choice of pin.**

**One correction to a premise in the brief.** "Born = K1" is D44f's
statement about the `V_single/V_pair` fixture
(`note-d44f-foliation-and-measure.md:26`), **not** D42b4's; D42b4 says
"Born = mu/Σmu" (`:22`, `:72`) about the `∏√q` lift. The two are different
fixtures and different claims (§4.2).

**A relevant v10 self-description found in passing.**
`v10/THE-THEORY-SO-FAR.md:12263`, glossary — "**holonomy (sealed)**: the
coherent, uncommitted relative phase a system carries **between** seals;
sealing destroys it." **v10's own book therefore already defines holonomy
AS the phase** — the identity reading, in the reference layer — while
`:9501` still lists *"sealed-holonomy-between-seals ≟ the interference
cross-term"* as an open `[TARGET]` whose realising functor "is itself the
open obligation, not yet written." **The book asserts the identity in the
glossary and marks it open in the chapter.** That is the same unowned
inconsistency D71 Clause 1 found at v6 scope, reproduced at v10 scope, and
it should be resolved in the same reading pass.

**§5's pin is a draft**, offered in D69's sense: to be frozen, amended or
discarded.
