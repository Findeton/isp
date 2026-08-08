# BRG — THE MORPHISM-CENSUS BRIDGE: FROM, OR ALONGSIDE?

**Status:** `TERMINAL (v13 BRG)` — panel #270–#272, adjudicated #273 ACCEPT-WITH-MAJOR-REPAIRS, repair B-1..B-7 verified byte-identical and conferred terminal at v13 LOG #276.
**Pin:** `v13/note-brg-bridge-pin.md` (STRICT; frozen, sha256
`56ce4a7e2dee…`, immutable base commit `b632f59`).
**Binding:** the pin's four HA-§14 requirements, verbatim in force; RUNBOOK §13
(verdict-in-gate with computed qualifiers, verdict-flip mutants,
cell-completeness, independent routes), §14 (symmetry self-tests, all addenda)
and §15 (declared-arena discipline, all addenda).
**Sources, hash-pinned and anchored exit-1:** `v13/paper-ha-successor.md` +
`ha_successor_receipt.json`; `v13/paper-nt-nomological-transport.md` +
`nt_transport_receipt.json`; `v13/paper-gen-generality-check.md` +
`gen_generality_receipt.json`; `v13/paper-xba-crossbase.md` +
`xba_crossbase_receipt.json`; `v13/paper-psi-curvature.md` +
`psi_curvature_receipt.json`.
**Verdict:** **`BRG-EMPTY-AT-CARRIER`** — at the committed carriers, over the
arena-invariant content, with **two** obstructions named: **order-coprimality**
forward, and the **2-group abelianisation** reverse.
**Deliverables:** this note; `v13/code/brg_bridge_exact.py`,
`v13/code/brg_bridge_output.txt`, `v13/code/brg_bridge_receipt.json`.

---

## Scope box

This unit answers exactly one question and no other: **does a structure-preserving
morphism exist between the two measured geometric structures** — the deformation
side's `⟨R_HH⟩` acting on its total-record carrier, and the transport side's
`⟨W, D⟩` acting on its wing carrier? It is a census, not a construction: nothing
here builds a spacetime, derives a field equation, or identifies any two of
`Δ^B`, `Ω_hypersurface`, `R^ρ_{σμν}`. HA's three-defect separation is engraved and
is not relaxed anywhere below.

**No claim is made that the two structures are unrelated in some absolute sense.**
The verdict is a census result at a declared finite scope, over the content that
survives the declared arena action. What is measured EMPTY is the set of
non-degenerate structure-preserving maps between the committed carriers, in both
directions. What is measured NON-EMPTY — at the extended scopes only, and then
excluded from the verdict by the pin's own requirement 4 — is a family of
morphisms that exists at two of the seven declared primes and not at the other
five; §8.3 reports it at the standard at which it was actually measured, under
the label **FOUND-AT-DELIVERED-STANDARD-OUTSIDE-COMMITTED-SCOPE**, and §5 states
what that standard is worth.

Everything below is at ONE declared finite arena, set out as data in §2.

---

## 1. The question, and what the pin required

HA measured the two objects' coordinates and refused to answer the morphism
question, registering it OPEN in its §14 with four requirements a successor
must meet. The pin restates them as binding and adds the outcome vocabulary.
Quoting the pin's own statement of the stake:

> FOUND ⟹ this program's spacetime is built FROM its quantum geometry; EMPTY ⟹
> alongside, at the committed carriers, with the obstruction named.

The four requirements, and where each is discharged:

| requirement | discharged |
|---|---|
| (1) a **carrier functor** declared as data before any morphism is evaluated, non-triviality gated, a degenerate collapse a named kill | §2.2, §2.3; gates G01, G06 — **at the level of group actions on carriers.** The arena-component correspondence (fronts/registers/lapses $\leftrightarrow$ wings/pointers/completions) is NOT posed; see §14 open 3 |
| (2) a **morphism census** at a declared finite scope, never one expression, with the preservation predicate declared as data | §2.4, §4, §5, §7, §8; gates G02, G09, G10, G11, G17, G18, G19, G42 |
| (3) **two-way gates**, each outcome reachable, each reachability demonstrated by a declared falsifier; FOUND requires predictive held-out verification | §8; gates G21–G25, G36 — at **asymmetric evidential standards**, disclosed at X08 and measured at G41 |
| (4) **arena-invariance gating**: the prime, the naming and the coordinate artifacts may not carry the verdict either way | §6; gates G12, G13, G14, G15, G16, G40 |

The pin also names the lead to be tested rather than assumed — the
record-is-metric identity against the completion encoding — and the candidate to
be killed if it turns out prime-tracking: morphism-by-spectrum. Both are carried
below as declared candidates, F1 and F3.

---

## 2. The declarations

Everything in this section is **declaration**, recorded before any candidate
morphism is evaluated. The instrument measures its candidate-evaluation counter
to be **zero** at the freeze point (G01), and the `freeze-lax` mutant, which
evaluates one candidate first, dies there.

### 2.1 The arena (RUNBOOK §15, declared as data)

| coordinate | declaration |
|---|---|
| **boundary** | two measured group actions: the deformation side $\bigl(C_{HA}(p) = \mathbb F_p^{k}\times\mathbb F_p^{d},\ \langle R_{HH}\rangle\cong\mathbb Z/p$ acting by translation of the address register by $\rho \bmod p\bigr)$, and the transport side $\bigl(C_{TR} = \text{system pair}\times\text{pointer pair},\ \langle W,D\rangle$ dihedral of order $2\,\mathrm{ord}(D)$, the dihedral form FORCED by the one law $D = [W,u]$ with $W^{2}=1$ — §9.2$\bigr)$ |
| **family** | 7 declared primes $\times$ 8 committed transport instances $\times$ 2 directions; extended scopes: GEN's 12 rebuilt completion classes, and the whole $8! = 40{,}320$-member completion family |
| **law** | the structure-preservation predicate SP1–SP3 of §2.4; a candidate morphism is a **pair** $(\varphi,\Phi)$ of a group map and a carrier map |
| **state** | the deformation side's base total record $(n_{\text{sym}},0)$; the transport side's initial configuration $j_0 = 0$ |
| **arena action** | the prime sweep; relabelling of either carrier; conjugation of the transport action by a carrier permutation; replacement of the source generator $R\mapsto R^{j}$ |
| **provenance** | five committed terminal receipts and one committed paper, hash-pinned; every reused number read from them and reproduced |
| **admission** | a candidate survives only if SP holds **and** the non-triviality clauses NT1, NT2 hold |

The declared primes are HA's own sweep, $\{5,7,11,13,17,19,23\}$. The
deformation side's exact residual is $\rho = (1/6,\,1/6)$, the same at every
prime, and $k = 2$ (the rank of the declared lapse span), $d = 2$.

### 2.2 The carrier functors, declared as data

Eight candidates are declared, each with its data. A **carrier functor** from
the deformation arena to the transport arena is a triple

$$\Phi \;=\; \bigl(\Phi_{\mathrm{obj}} : C_{HA}\to C_{TR},\quad
\varphi : \langle R_{HH}\rangle \to \langle W,D\rangle,\quad
\Phi_{\mathrm{enc}}\bigr),$$

with $\Phi_{\mathrm{enc}}$ the dictionary between the two sides' encodings.

| id | the functor, as data |
|---|---|
| **F0-IDENT** | the identity self-functor inside one arena. **Positive control**: the census machinery must FIND it. |
| **F1-RECORD-COMPLETION** | *the pin's declared lead.* Object part: a dictionary $\delta$ from the deformation side's geometry records to the transport side's completions. Group part: the induced $\langle R_{HH}(r)\rangle\to\langle W,D(\delta(r))\rangle$. Encoding part: HA's record-is-metric datum (counts $\leftrightarrow q$, HA G28, determinant 2) against GEN/XBA's completion datum ($Q\mapsto D$). |
| **F2-CARRIER** | $\Phi_{\mathrm{obj}}$ between the carriers with $\varphi$ between the groups; the space of $\varphi$-equivariant $\Phi_{\mathrm{obj}}$ enumerated by orbit representatives, its size computed. |
| **F3-SPECTRUM** | *the pin's named lead-to-be-killed.* A morphism is declared to exist at $p$ iff $p$ lies in GEN's **defect** order spectrum. **Prime-tracking control.** |
| **F4-DEGENERATE** | constant carrier map at $j_0$, trivial group map. **Named kill: DEGENERATE-COLLAPSE.** |
| **F5-REVERSE** | the same data in the direction transport $\to$ deformation. |
| **F6-BREAK-A** | **negative control with teeth**: carrier map $=$ the register doubling $(f,m)\mapsto(f,2m)$, group map $=$ the identity. Bijective, non-degenerate, and differing from an ACCEPTED morphism (the same carrier map with $R\mapsto R^{2}$) **only in the group map**. |
| **F6-BREAK-B** | **negative control**: the identity carrier map with two points of different orbits transposed, group map $=$ the identity. |

### 2.3 Non-triviality, gated

$$\textbf{NT1: } \varphi \text{ is non-trivial.}\qquad
\textbf{NT2: } \Phi_{\mathrm{obj}} \text{ is non-constant.}$$

F4 is built and measured: it **satisfies** the whole preservation predicate and
is **rejected** by NT1 and NT2 (G06). A census that could be won by collapsing
either side to a point would decide nothing, and the gate that stops it is
falsifiable — `nontrivial-lax`, which blinds the clauses, dies there.

NT2 asks only that $\Phi$ take at least two values, and §5 measures exactly how
little that is: a carrier map sending **124 of 125** source orbits into a single
target orbit passes it.

### 2.4 The structure-preservation predicate, declared as data

| clause | statement | measured over |
|---|---|---|
| **SP1** | $\varphi(gh) = \varphi(g)\varphi(h)$ — composition preserved | all $\lvert G_{\mathrm{src}}\rvert^{2}$ ordered pairs |
| **SP2** | $\varphi(1) = 1$ | one cell |
| **SP3** | $\Phi(g\cdot x) = \varphi(g)\cdot\Phi(x)$ — the group actions preserved | all $\lvert G_{\mathrm{src}}\rvert\times\lvert C_{\mathrm{src}}\rvert$ cells |
| **arena-invariance** | SP references only the group actions, the composition and carrier incidence — never a prime value, never a label name, never a carrier index | the §6 self-tests |

The predicate's teeth are measured, not asserted. A declared non-homomorphism
that fixes the identity is rejected by SP1 at **10 of 25** composition cells
(G08). F6-BREAK-A is rejected by SP3 at **2,500 of 3,125** cells while *the same
carrier map with the group map $R\mapsto R^{2}$ is accepted* — so the predicate
is sensitive to exactly the structure it claims to test, not to gross
malformation (G07). F6-BREAK-B is rejected at 16 cells. The `break-blind`
mutant, which replaces the breaking map by its accepted counterpart, dies at
G07; `predicate-lax`, which evaluates SP3 at the base point only, and
`equivariance-side`, which reverses the action's orientation convention, both
die.

**Where the predicate is weak, stated here and measured at §5:** the source
action is free, so once $\varphi$ is fixed SP3 imposes no constraint at all —
an equivariant $\Phi$ is one free choice of image per orbit. At the functor
layer the predicate therefore has exactly one biting clause. That makes the
EMPTY verdict correspondingly strong and any live cell correspondingly weak, and
both halves of that are recorded (G37, X11).

### 2.5 The held-out set, declared before any morphism is constructed

| id | quantity |
|---|---|
| H1 | the orbit-size multiset on each side |
| H2 | the fixed-point count of each generator |
| H3 | the element-order multiset of each group |
| H4 | the source group's composition table, all $\lvert G\rvert^{2}$ cells |
| H5 | the equivariance equations on every HELD orbit — never imposed by the construction, verified afterwards |

**Split rule:** the source orbits are ordered lexicographically by their minimal
element; **FIT** = orbit 0 only; **HELD** = every other orbit; sizes computed.

**Construction rule, in full.** The morphism is fitted on the FIT orbit and
extended to every other orbit by the declared **source** symmetry. Each orbit's
minimal element decodes to a front translation $\delta = (\delta_0,\delta_1)$ and
a register shift $c$ transverse to $\rho$; the declared assignment carries that
pair into the target group by the **left** action

$$\Phi\bigl(T_\delta S^{c} y\bigr) \;=\; \tau(\delta,c)\cdot\Phi(y),
\qquad
\tau(\delta,c) \;=\; D^{\,r},\quad
r \;=\; (\delta_0 + 2\delta_1 + c) \bmod \mathrm{ord}(D),$$

for the rotation-valued extension **E-ROT**, and $\tau = W\!\cdot\! D^{\,r}$ where
$\delta_0$ is odd for the reflection-valued **E-REF**, which is declared in
advance to be the teeth: it must FAIL the held-out check.

Equivariance on the HELD orbits is therefore **verified, not imposed**. What it
discriminates is measured and stated at its strength: it separates a
rotation-valued extension from a reflection-valued one, and it is **insensitive
to which rotation rule is declared** — under five declared rotation rules the
held-out violations are 0 at every cell, and under their five reflection-valued
counterparts 54 at every one, because $\langle D\rangle$ is abelian and the
held-out equation is then an identity (G39, X07). The content the 234 cells
carry is **centraliser membership**.

### 2.6 The strengthened standard, registered and untested

The predicate above is the standard this unit measures against. The standard a
live-cell morphism would have to meet before the word *bridge* is earned is
declared here as the **successor's gate**, and **no cell of any scope in this
unit is evaluated against it, in either direction** (X11):

| id | requirement |
|---|---|
| **S1** | **ENCODING INTERTWINING — the non-negotiable.** A *commuting square* at the encoding layer, not a triangle at the group layer: HA's record-is-metric linear map (determinant 2) intertwined with GEN/XBA's $Q\mapsto\delta(Q) = \Sigma Q^{\mathsf T}\Sigma Q$. |
| **S2** | **CARRIER RIGIDITY.** SP3 supplemented so $\Phi$ is *determined*, not chosen — e.g. the fixed-configuration stratification $\{9,18,27,36,45,54,81\}$ carried across. |
| **S3** | **NON-DEGENERACY WITH TEETH.** NT2 replaced by injectivity on orbits, or a measured lower bound on $\lvert\mathrm{image}(\Phi)\rvert$ as a fraction of the orbit count. |
| **S4** | **FUNCTORIALITY IN THE FAMILY.** Naturality across the declared base-change maps, so a live cell is not an isolated coincidence at one $(p,\mathrm{ord}(D))$. |
| **S5** | **HELD-OUT AT A LIVE CELL WITH A TRANSPORTED QUANTITY.** A computed physical quantity carried out of sample, not equivariance alone. |
| **S6** | **AN IN-ARENA READING OF REQUIREMENT 4.** Either the prime declared a parameter with per-prime verdicts, or a corpus-internal fixing of $p$. |

---

## 3. The two sides, rebuilt

Neither side is quoted; both are rebuilt here from their own units' published
laws and anchored exit-1, quantity by quantity, against the committed receipts.
**87 anchors, all reproduced.**

### 3.1 The transport side, from GEN §8.1's defect law and PSI's one law

With the carrier factorised as system pair $\times$ pointer pair, $\Sigma$ the
label exchange, $W = \Sigma\otimes\Sigma$ and
$D = (\Sigma Q^{\mathsf T}\Sigma Q)\otimes I$:

| rebuilt | measured | anchored against |
|---|---|---|
| base G's declared defect permutation | $[0,2,1,6,4,5,3,7,8]$ | GEN receipt; **and PSI's recorded commutator $\delta(Q)$, entry by entry** |
| its order / fixed configurations | 2 / **45** of 81 | GEN receipt; PSI's group-order reading |
| $W$'s fixed configurations at base G | **9** of 81 | XBA receipt |
| $\lvert\langle W,D\rangle\rvert$ at base G | **4** | XBA receipt; **PSI's measured based-holonomy order at GP-E** |
| base 1's wing exchange and its two factors, fixed configurations | **6**, 18, 12 of 36 | NT receipt |
| species 4: defect / exchange fixed configurations, $\lvert\langle W,D\rangle\rvert$ | **192**, **16** of 256, **4** | XBA paper (hash-pinned, X12) |
| species 4's own 120-member transposition family, split by defect order | **12 / 60 / 48** | XBA paper §9.4 (hash-pinned, X12) |
| base T: $\mathrm{ord}(D)$, $\lvert\langle W,D\rangle\rvert$ | **3**, **6** | XBA receipt; **PSI's Q-negA commutator and its measured holonomy order** |
| base S′ (the equivariant control): $\lvert\langle W,D\rangle\rvert$ | **2** | XBA receipt |
| the whole declared completion family | **40,320** members | GEN receipt |
| its defect order spectrum | $\{1{:}96,\,2{:}1440,\,3{:}4224,\,4{:}4608,\,5{:}4608,\,6{:}6912,\,7{:}9216,\,15{:}9216\}$ | GEN receipt |
| its fixed-configuration spectrum | $\{9{:}16704,\,18{:}11520,\,27{:}5376,\,36{:}4608,\,45{:}864,\,54{:}1152,\,81{:}96\}$ | GEN receipt |
| identity-defect / geometry-bearing members | **96** / **40,224** | GEN receipt |
| members where $\Sigma D\Sigma = D^{-1}$ fails | **0** | GEN receipt |
| each of GEN's 12 rebuilt classes: defect order, fixed configurations, element orders of $\langle W,D\rangle$ | all reproduced | GEN receipt |

The family sweep is cell-complete: 40,320 members classified exactly once, both
spectra summing to the swept count (G02); `family-drop` and `anchor-gen-family`
die there.

### 3.2 The deformation side, from HA's G28/G29

$\langle R_{HH}\rangle$ acts on $C_{HA}(p) = \mathbb F_p^{k}\times\mathbb F_p^{d}$
as translation of the address register by $\rho \bmod p$, the front sector fixed
(HA G29). The exact residual $\rho = (1/6,1/6)$ is read from HA's receipt and its
reduction recomputed here at every prime:

| $p$ | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---|---|---|---|---|---|---|
| carrier $p^{k+d}$ | 625 | 2401 | 14 641 | 28 561 | 83 521 | 130 321 | 279 841 |
| $\rho \bmod p$ | $(1,1)$ | $(6,6)$ | $(2,2)$ | $(11,11)$ | $(3,3)$ | $(16,16)$ | $(4,4)$ |
| $\lvert\langle R_{HH}\rangle\rvert$ | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
| orbits (the action is free) | 125 | 343 | 1331 | 2197 | 4913 | 6859 | 12 167 |

Every row is anchored against HA's own prime sweep. The record-is-metric
re-encoding is rebuilt and its determinant measured **2** (HA G28). And one
measurement is recorded here because §9 turns on it: **$\rho$ does not reduce
at exactly the primes $\{2,3\}$** — the denominator is 6 — so those two primes
are not an omission from HA's list, they are inadmissible on the deformation
side.

### 3.3 The committed instances, and two that are under-determined

| instance | carrier | $\mathrm{ord}(D)$ | $\lvert\langle W,D\rangle\rvert$ | rebuilt as permutations |
|---|---|---|---|---|
| base 1 @ SP-E | 36 | 2 | 4 | no |
| base 1 @ SP-F | 36 | 2 | 4 | no |
| base G @ GP-E | 81 | 2 | 4 | yes |
| base G @ GP-F | 81 | 2 | 4 | yes |
| base S | 81 | 2 | 4 | no |
| base S′ | 81 | 1 | 2 | yes |
| base T | 81 | 3 | 6 | yes |
| species 4 | 256 | 2 | 4 | yes |

Base 1's defect and base S's defect are **not determined** by the published
receipts. Neither is guessed. The whole set of candidates consistent with every
committed datum is swept — **2** candidates for base 1 (the $\Sigma$-invariant
involutions of the four system-pair labels with 18 fixed configurations closing
to a group of order four) and **864** for base S (the whole (ord 2, 45 fixed)
class) — and every member of each set gives the same group order, so the
ambiguity cannot move a census count (G04). `ambiguity-lax`, which truncates the
sets to a single guess, dies there.

The abstract dihedral model that the census consumes is audited by a comparator
built **independently of it** — the permutation rebuild from $Q$ and $\Sigma$ —
at the five rebuilt instances and all twelve rebuilt classes, and the audit is
an **isomorphism** check, not an order check: the explicit map
$(i,k)\mapsto D^{i}W^{k}$ from the model into the permutation group is measured
bijective and multiplicative on **every ordered pair** (G03, RUNBOOK §14
addendum #219). Order agreement would not have implied isomorphism, and both
census routes consume this model (X09). `comparator-self`, which routes the
comparator through the audited component, and `model-lax`, which replaces the
model by the abelian group of the same order, both die there.

---

## 4. The census at the group level, both directions

A candidate morphism is a pair, so the census factorises: for each group map
$\varphi$ the equivariant carrier maps are enumerable (§7), and a
**non-degenerate** pair requires a **non-trivial** $\varphi$. The group-level
census is therefore the load-bearing one, and it is exhaustive.

**Scope 1 — the committed instances.** 7 primes $\times$ 8 instances = **56
cells**, **112 directed cells**, each visited exactly once, the count computed
from the declared sets and asserted against the declared scope constant (G09).

| $p$ | every committed instance |
|---|---|
| 5, 7, 11, 13, 17, 19, 23 | $\lvert\mathrm{hom}(\mathbb Z/p,\langle W,D\rangle)\rvert = 1$; non-trivial **0** |
| 5, 7, 11, 13, 17, 19, 23 | $\lvert\mathrm{hom}(\langle W,D\rangle,\mathbb Z/p)\rvert = 1$; non-trivial **0** |

$$\boxed{\text{non-degenerate group morphisms, forward: } \mathbf{0}\ \text{of 56 cells};\qquad
\text{reverse: } \mathbf{0}\ \text{of 56 cells.}}$$

**The routes, described as measured (G10, X09).** The forward count is computed
twice: by the **element-power route** (iterated multiplication in the target,
testing $g^{p} = e$) and by the **cyclic-subgroup-lattice route** (each element's
span built as a *set*, the spans deduplicated into the lattice, the ones whose
order divides $p$ kept and their generators counted). These are two
implementations of **one criterion** — $g^{p} = e$ and $\mathrm{ord}(g)\mid p$
are the same predicate — over the **same abstract model**, and they are
disclosed as such rather than advertised as independent computations; what they
catch is a single-route implementation error, and what audits the shared model
is G03's isomorphism and G27's abelianisation. The **reverse** count is computed
by two genuinely different computations: one that works **in $G$** (generator
images swept, extended by breadth-first word evaluation, verified on the whole
multiplication table) and one that works **in the abelianisation** (the
commutator subgroup built by closing the set of commutators, the quotient's own
table formed, its generators' images swept). Neither route reads the other: the
taint counter is measured **0** and both invocation counters are nonzero.
`route-b-lax`, which omits the trivial subgroup from the lattice, and
`route-alias`, which returns the first route's own answer, both die at G10.

The counting identity $\lvert\mathrm{hom}(\mathbb Z/p, D_n)\rvert = \gcd(n,p)$ is
**analytically forced for odd $p$** and is recorded as a disclosure (X01), not
used as a gate: neither route invokes it. It is *false* at $p = 2$ — measured,
not assumed: at $p = 2$ it fails at every $n \le 20$ tested — and $p = 2$ is
inadmissible on the deformation side, so nothing turns on it.

**Scope 2 — GEN's twelve rebuilt classes.** 7 primes $\times$ 12 classes = **84
cells** (G11). Here the answer is different, and it is what §8.3 and §9.5 are
about:

| cell | non-trivial forward morphisms | non-trivial reverse morphisms |
|---|---|---|
| $p = 5$, class $\mathrm{ord}(D) = 5$ | 4 | **0** |
| $p = 5$, class $\mathrm{ord}(D) = 15$ | 4 | **0** |
| $p = 7$, class $\mathrm{ord}(D) = 7$ | 6 | **0** |
| every other cell of the 84 | 0 | 0 |

**14 non-trivial group morphisms exist over scope 2** — at two of the seven
declared primes and at none of the other five — and **the reverse census is
empty even there**. That asymmetry is the second obstruction (§9.3).

---

## 5. The functor level: the carrier maps themselves

The source action is measured **free** (translation by $\rho\not\equiv 0$), so
every stabiliser is trivial and, given $\varphi$, an equivariant $\Phi$ is
exactly a free choice of image per source orbit. The number of
structure-preserving pairs is therefore

$$\#\{(\varphi,\Phi)\ \text{satisfying SP}\}\;=\;
\sum_{\varphi\in\mathrm{hom}(\mathbb Z/p,\,\langle W,D\rangle)}
\lvert C_{TR}\rvert^{\,\#\text{orbits}},$$

computed exactly as an integer at each of **35** cells — the rebuilt instances at
the seven primes, a count computed from the declared sets with every cell
visited exactly once (G17; `functor-cell-drop` dies there). The counts are
astronomical — from 793 bits at $p=5$ to 97,337 bits at $p=23$ — and **entirely
degenerate**: the non-degenerate count is **0** at every cell, because the only
$\varphi$ available is the trivial one.

**What that formula asserts, and how much of it is validated.** Two independent
routes again:

- the **orbit count** is computed by union-find over the generator's own edges
  and by dividing the carrier size by the orbit length; the two agree at all 35
  cells (G17), and `orbit-lax` dies there;
- the **count formula** is checked against an **exhaustive brute-force
  enumeration of every function** from the source carrier to the target carrier,
  filtered by the very predicate the census uses, at declared tiny cells (G18).
  The validation set is cell-complete against its declaration, every cell's
  generator is measured to satisfy $\mathrm{gen}^{p} = \mathrm{id}$ (so the
  declared group really acts), and the **orbit exponent** — the thing the
  formula actually asserts — is exercised above 1:

| tiny cell | source | target | orbits | group maps | formula | brute force | non-degenerate |
|---|---|---|---|---|---|---|---|
| TINY-A | $\mathbb Z/2$ acting freely on 4 points, generator $(0\,1)(2\,3)$ | Klein four, regular on 4 | **2** | 4 | 64 | **64** | 48 |
| TINY-B | $\mathbb Z/3$ on 3 points | $D_3$, regular on 6 | 1 | 3 | 18 | **18** | 12 |
| TINY-C | $\mathbb Z/5$ on 5 points | Klein four, regular on 4 | 1 | 1 | 4 | **4** | **0** |
| **TINY-NEG** (negative control) | declared $p=2$ but generator of order 3 on 3 points — the group does **not** act | $D_3$, regular on 6 | 1 | 4 | 24 | **6** | 0 |

The tiny set includes a cell with non-trivial group maps and a cell with none,
so the brute-force route validates the formula on both sides of the question it
is used to answer; TINY-A exercises orbit exponent 2; and TINY-NEG measures that
the formula's **hypothesis** is load-bearing — where the declared group does not
act, formula and brute force **disagree, 24 against 6** (G42). `formula-lax`,
`tiny-drop` and `arena-order-lax` (which builds a generator whose order does not
divide $p$) all die at G18/G42.

**What the predicate is worth at this layer, measured (G37).** Because the
source action is free, SP3 constrains nothing once $\varphi$ is fixed, and NT2
asks only for two distinct images. The example is built and evaluated rather
than argued: at $p = 5$ on the defect-order-15 class, a carrier map sending
**124 of the 125 source orbits into a single target orbit** satisfies the whole
predicate and is **ACCEPTED**. Consequently:

> The census is, at the functor layer, a group-homomorphism census. That makes
> the EMPTY verdict **strong** — the filter is as loose as it can be and the
> answer is still zero — and it makes any live cell **weak**: a live cell is not
> one bridge but an unconstrained family of them, of the sizes reported in §8.3.

Both halves are recorded; the strengthened standard of §2.6 is what a successor
must impose to make a live cell mean anything, and it is tested nowhere here.

---

## 6. Arena-invariance: what may carry the verdict, and what may not

RUNBOOK §15 and the pin's requirement 4 are the same instruction: a quantity not
gated invariant across the unit's admissible arenas may serve as an instrument
reading and may **never** enter as a conclusion. HA's own G30 established that
$\lvert\langle R_{HH}\rangle\rvert$ is exactly such a quantity — it equals the
declared reduction prime.

**The committed-scope verdict is invariant across the whole declared prime
sweep** (G12): the census answer is the same at every one of the seven primes.
The gate requires more than one prime to be posable, so `prime-single` dies
there.

**The prime-tracking gate bites, measured** (G13). The declared
morphism-by-spectrum candidate F3 survives at $p\in\{5,7\}$ and dies at
$p\in\{11,13,17,19,23\}$; the same reading is anchored against HA's own
`membership_in_the_defect_spectrum_by_prime`. And the candidate's verdict is
measured to coincide, prime by prime, with the **extended-scope census's own
answer** of §4. That coincidence is not a curiosity: it is the identification of
what the spectrum criterion actually is.

> **$p$ lies in GEN's defect order spectrum $\iff$ some completion in the family
> has $\mathrm{ord}(D) = p$ $\iff$ the group $\langle W,D\rangle$ of that
> completion admits a non-trivial homomorphism from $\mathbb Z/p$.**
> The spectrum criterion *is* the extended-scope morphism census, and both are
> prime-tracking.

`tracking-blind`, which makes F3 prime-uniform, and `spectrum-swap`, which reads
the holonomy spectrum where the defect spectrum belongs (the like-for-like
coordinate, RUNBOOK §15 addendum #196), both die at G13.

**The exclusion, applied** (G14). Requirement 4 forbids the prime from carrying
the verdict *either way*. Operationally: the morphism question is posed over the
content invariant under the arena action, i.e. **the intersection over the
declared prime sweep**. Measured over all **20** instances of both scopes: no
instance admits a non-trivial morphism at every declared prime, and **none
admits even two**. **The reason is structural, and it is scoped to the
nine-label arena:** admitting two declared primes requires $2\,\mathrm{ord}(D)$
divisible by at least $5\times 7 = 35$, and the whole nine-label family's
maximum is $2\times 15 = 30$ (both numbers computed in the run; the Landau
maximum for nine labels is **20**); admitting all seven requires divisibility by
**37,182,145**. **At species 4's sixteen-label arena the same clause is
contingent, not forced** — the Landau maximum there is **140**, and a declared
deterministic sample of 2,000 completions of that arena contains **162** whose
defect order is divisible by 35, with an explicit witness completion printed
(G40). What
carries G14 at species 4 is that instance's own measured $\mathrm{ord}(D) = 2$.
`invariance-lax`, which reads the test as a union, dies at G14; `landau-lax`,
which runs the contingency sweep in the nine-label arena, dies at G40.

**The symmetry self-tests** (RUNBOOK §14; G15, G16). The predicate's verdict is
measured invariant under the arena's own action — relabelling the source carrier
(625 points moved), relabelling the target carrier (81 moved), conjugating the
transport action by a carrier permutation (81 moved), and replacing the source
generator $R$ by $R^{j}$ for every $j\not\equiv 0$ — **on an ACCEPTED
non-degenerate candidate as well as on the degenerate one**: the source side
carries the register doubling with the group map $R\mapsto R^{2}$, the target
side carries its translation self-morphism (carrier map $=$ the action of $W$,
group map $=$ the identity automorphism), and each is transported through the
declared action rather than rebuilt inside the new arena. A verdict that could
not move would test nothing, and these can: `selftest-blind`, which applies one
declared action to the candidate the wrong way round, dies at the invariance
clause. The generator sweep **consumes the arena it builds**: at each $R^{j}$ the
arena's orbit count is recomputed by union-find (125 at every $j$), its action is
measured free, and the accepted candidate is re-evaluated inside it —
`generator-blind`, which sweeps the identity permutation instead of the
generators, dies there. The tested set is fixed by declaration and is measured to
be the declared one, never selected by the verdicts under audit;
`selftest-select` dies there, as do `relabel-lax` and `conj-lax`, which would
relabel and conjugate by the identity.

Every self-test evaluation **bypasses the memo cache** (35 bypasses, **0**
self-test cache hits) while the cache is measured, at that gate, to have been
looked up **132** times and hit **25** times elsewhere in the run, so the
zero-hit clause is not vacuous (§14 addenda #185 and #219); `cache-lax` and
`cache-unused` die at G16. (The end-of-run cache table records a larger count
than the gate-time snapshot; the qualifier "at that gate" is doing real work.)

---

## 7. The pin's declared lead: the record ↔ completion dictionary

F1 is the pin's own lead, and it is swept rather than argued. A dictionary
assigns to each of the deformation side's **9** geometry records a completion
from the transport side's **40,320**-member family; the space has
$40{,}320^{9}$ points, **42 digits**, computed by exponentiation from the two
measured set sizes. The admissible count is a **product over the records** of
per-record counts, each obtained by sweeping the whole defect order spectrum —
504 spectrum cells swept, never one expression (G19); `dict-drop` dies there.

| $p$ | admissible completions per record | admissible dictionaries |
|---|---|---|
| 5 | 13 824 | $1.84\ldots\times10^{37}$ (38 digits) |
| 7 | 9 216 | $4.79\ldots\times10^{35}$ (36 digits) |
| 11, 13, 17, 19, 23 | **0** | **0** |

The same prime-tracking pattern, in the pin's own lead. And **at the committed
scope the count is zero at every prime**: when the dictionary's image is
restricted to the committed completions — defect order 2 — the per-record
admissible count is 0 at all seven primes, so the product over the nine records
is 0 and no dictionary survives (G20). `dict-scope-lax`, which lets the
committed-scope census read the extended family, dies there.

The dictionary is swept at the **group** layer. The encoding layer — HA's
record-is-metric map against $Q\mapsto\delta(Q)$ — factorises through it and is
therefore **not tested**; that is requirement S1 of §2.6 and open 3 of §14.

---

## 8. Both outcomes reachable, and the held-out verification

A predicate that cannot return its other value anywhere is not a measurement.
Both values are exhibited, by the same machinery — and at **different evidential
standards**, which is disclosed rather than smoothed (X08, §8.4).

### 8.1 FOUND is reachable, and its verification is predictive (G21–G24)

A **declared synthetic compatible pair** is injected: source
$\mathbb Z/3$ acting on $\mathbb F_3^{2}\times\mathbb F_3^{2}$ (81 points, 27
free orbits) by translation by $(1,1)$; target base T's rebuilt
$\langle W,D\rangle$ of order 6, whose defect has order 3. It is declared
**synthetic** and outside the committed arena for a measured reason: HA's own
$\rho = (1/6,1/6)$ does not reduce at $p = 3$ (§3.2, X04).

The census returns **2 non-trivial group maps**. The carrier morphism is then
built under the declared protocol of §2.5: fitted on the **FIT orbit alone** — 1
orbit, **3 points touched** — and extended to the other **26** orbits by the
declared source symmetry. Its equivariance is then verified on every HELD orbit:
**234 held-out cells, 0 violations**, equations the construction never imposed.
The morphism is ACCEPTED by the full predicate. `heldout-leak`, which fits on
the held-out orbits, dies at G21, G22 and G23. (Of G23's two clauses, the
fit-touch identity $\#\text{touched} = \lvert\mathrm{FIT}\rvert\cdot p$ is forced
whenever every source orbit has size $p$; the falsifiable clause is
$\lvert\mathrm{FIT}\rvert = 1$, and it is what kills `heldout-leak`.)

**The held-out gate has teeth** (G22). The *same* construction with the declared
reflection-valued extension E-REF fails the held-out check at **54 of 234**
cells and is rejected by the census, while E-ROT passes at every one. The
mechanism is exactly the one under test: a reflection does not commute with the
rotation that carries the group map, so the prediction breaks on precisely the
orbits the fit never saw. `teeth-off`, which makes E-REF silently
rotation-valued, dies there. What the check measures is centraliser membership,
and it is blind to which rotation rule is declared (§2.5, G39, X07).

**The declared held-out quantities transport** (G24): H1 the orbit-size multiset
$[3] = [3]$; H2 the generators' fixed-point counts; H3 the source element orders
$\{1,3\}$ inside the target's $\{1,2,3\}$; H4 the whole composition table, 9
cells, **0** violations. `quantity-lax`, which reads a held-out quantity off the
wrong action, dies at G24.

### 8.2 EMPTY is reachable by the same machinery (G25)

A **declared synthetic incompatible pair**: source $\mathbb Z/5$ against the same
target of order 6. The census returns **1** group map and **0** non-trivial ones.
`empty-block`, which makes the pair compatible, and `found-block`, which makes
the compatible pair incompatible, both die — each proving that the outcome it
attacks is genuinely reachable.

### 8.3 FOUND-AT-DELIVERED-STANDARD-OUTSIDE-COMMITTED-SCOPE (G36)

The FOUND machinery is **not** exercised only at an inadmissible prime. At each
of the three live cells of §4 — at $p = 5$ and $p = 7$, both **declared
admissible** on the deformation side, on classes the transport side itself
rebuilt — an explicit pair $(\varphi,\Phi)$ is constructed in this delivery and
run through the **full delivered predicate** and through **this unit's own
held-out protocol**:

| cell | $\lvert\langle W,D\rangle\rvert$ | SP1 cells / bad | SP3 cells / bad | NT1, NT2 | FIT points | held-out cells / violations | non-degenerate pairs |
|---|---|---|---|---|---|---|---|
| $p=5$, $\mathrm{ord}(D)=5$ | 10 | 25 / **0** | 3,125 / **0** | both | 5 | 3,100 / **0** | **240** digits |
| $p=5$, $\mathrm{ord}(D)=15$ | 30 | 25 / **0** | 3,125 / **0** | both | 5 | 3,100 / **0** | **240** digits |
| $p=7$, $\mathrm{ord}(D)=7$ | 14 | 49 / **0** | 16,807 / **0** | both | 7 | 16,758 / **0** | **656** digits |

$\varphi$ sends the source generator to an element of order exactly $p$ (measured
$p$, not merely dividing it); $\Phi$ is fitted on the FIT orbit alone and
extended by the declared source symmetry, exactly as in §8.1. All three are
**ACCEPTED**, and the held-out equations hold at every predicted cell.
`live-order-lax`, which builds the group map from the defect itself instead of
its element of order $p$, dies at G36.

**The label, and why it is that label.** Two *distinct* exclusions keep these
cells out of the verdict, and they are not the same exclusion:

1. **The scope declaration.** The verdict's decision variable is the emptiness
   of the **scope-1** census, so the live cells — which live at scope 2 — never
   enter it. That is deviation 2's declared choice, not an arena argument. Note
   the shape: the decision variable is a *union over primes at scope 1* (any
   live scope-1 cell anywhere would make it false).
2. **Requirement 4, measured separately.** G14 tests the *intersection over the
   prime sweep* and measures it empty at every instance of **both** scopes. The
   live cells' existence is a function of the declared reduction prime, so
   requirement 4 excludes them independently of the scope choice.

The two readings agree in this run only because scope 1 is empty at every cell.
Under both, the cells are reported and not counted:
**FOUND-AT-DELIVERED-STANDARD-OUTSIDE-COMMITTED-SCOPE**.

**The reconciliation, stated plainly.** The delivered standard is provably weak
at the functor layer (§5, G37): the free source action makes SP3 vacuous once
$\varphi$ is fixed, and NT2 admits the 124-of-125 collapse. So these FOUNDs are
**necessary but weak** evidence — necessary because a bridge must at least be a
morphism of the group actions, weak because at this standard a "morphism" is a
divisibility fact about one integer plus an unconstrained choice of images, and
the digit counts in the table above are the size of that choice. Against the
**strengthened** standard of §2.6 — S1 encoding intertwining first — **neither
side has been tested**: not the committed instances, not the live cells. That is
the successor's gate, registered here (X11).

### 8.4 The two outcomes are held to different standards (G41, X08)

EMPTY is measured against the intersection-over-primes reading at every instance
of both scopes. FOUND is exhibited at one declared synthetic pair, and at the
live cells requirement 4 excludes. Under this unit's declared reading of
requirement 4 an **in-arena FOUND was foreclosed before any census ran**, by an
arithmetic the unit computes: two declared primes need $2\,\mathrm{ord}(D)$
divisible by 35 and all seven need 37,182,145, while the declared family's
maximum $2\,\mathrm{ord}(D)$ is **30**. The two-way gate is two-way across the
synthetic boundary and across the scope boundary — not inside the committed
arena. G41 records this as a **disclosure-grade measurement**, not as a
must-pass gate, because it is analytically forced (RUNBOOK §14 addendum #208).

---

## 9. The obstructions, named

The verdict is EMPTY, so the pin requires the obstruction to be named: **which
preserved structure cannot be matched.** There are **two**, and they are
different in kind.

### 9.1 The forward obstruction: order-coprimality

> **The forward obstruction is order-coprimality**, and it is measured
> **coextensive with the forward census's emptiness — in both directions of the
> equivalence** — over every cell of every declared scope: of 140 cells,
> **137** are empty and **3** are live, and the forward census is empty
> **exactly** where $\gcd\bigl(p,\lvert\langle W,D\rangle\rvert\bigr) = 1$ (G26).

The naming is falsifiable because cells of both kinds occur — a criterion that
held vacuously everywhere would name nothing. `obstruction-misname`, which
substitutes a cardinality claim, dies at G26. (No cardinality test is used as a
criterion anywhere in this unit; equal carrier size is neither necessary nor
sufficient, and HA said so first.)

**The theorem, complete: Lagrange one way, Cauchy the other, no dihedral
hypothesis.** For a finite group $G$ and a prime $q$:

$$\mathrm{hom}(\mathbb Z/q,\,G)\ \text{is trivial}
\quad\Longleftrightarrow\quad q \nmid \lvert G\rvert .$$

*Forward.* A non-trivial image of $\mathbb Z/q$ needs an element of order exactly
$q$; it would generate a subgroup of order $q$, and by **Lagrange** $q$ would
divide $\lvert G\rvert$. *Converse.* If $q \mid \lvert G\rvert$ then by
**Cauchy's theorem** $G$ contains an element $g$ of order $q$, and $1\mapsto g$
is a non-trivial homomorphism; explicitly, in a dihedral group of order
$2\,\mathrm{ord}(D)$ with odd $q \mid \mathrm{ord}(D)$ the rotation
$D^{\mathrm{ord}(D)/q}$ is such an element. Both halves are swept over a declared
group zoo that is deliberately **not only dihedral** — cyclic, dihedral,
symmetric, alternating and direct products, abelian and non-abelian: **189
group $\times$ prime cells over 21 groups, 0 failures** (G33). `cauchy-narrow`,
which narrows the zoo to dihedral groups, dies there.

**So the geometric content is the order formula, not the hom count.** With
$\lvert G\rvert = 2\,\mathrm{ord}(D)$ substituted, the criterion reads
$q \mid 2\,\mathrm{ord}(D)$ — and *that* reading needs the dihedral form: applied
to non-dihedral groups of the same order it is measured to **fail at 5 of 117
non-dihedral cells** (G33). Everything geometric in this obstruction is carried
by $\lvert\langle W,D\rangle\rvert = 2\,\mathrm{ord}(D)$.

### 9.2 The order formula is forced by the one law — so the obstruction is a theorem about the whole family

PSI's one law states that the wing exchange $P_W$ is an involution and the defect
**is** the group commutator, $D = [P_W, u] = P_W u^{-1} P_W u$. Given only those
two ingredients — $W^{2} = 1$ and $D = [W,u]$ — the dihedral relation is forced
by one line of algebra:

$$W D W \;=\; W\,(W u^{-1} W u)\,W \;=\; u^{-1} W u W \;=\;
\bigl(W u^{-1} W u\bigr)^{-1} \;=\; D^{-1}.$$

Hence $\langle W,D\rangle$ is dihedral of order $2\,\mathrm{ord}(D)$ whenever
$W\notin\langle D\rangle$. Measured over a randomised family sweep whose seed is
the sha256 of declared data alone — 400 draws of an involution $W$ and a
permutation $u$ on 4 to 8 points: **0 violations of $WDW = D^{-1}$, 0 violations
of the order formula, 0 draws with $W\in\langle D\rangle$**, and the defect
orders $\{1,2,3,4,5,6,7,15\}$ drawn — the sweep is not vacuous in either
direction. The hypothesis is load-bearing and measured to be so: in the
declared control where $W$ is a general permutation rather than an involution,
the relation **fails at 145 of 168 draws** (G35). `psi-noninvolutive`, which
draws a general permutation where the law declares an involution, dies there.

Therefore:

> **The obstruction is not a contingent feature of eight measured instances. It
> is a theorem about the commutator law's entire group family:** for any base
> whose defect is the commutator of an involutive exchange, and any prime
> $q$, a non-trivial homomorphism $\mathbb Z/q\to\langle W,D\rangle$ exists iff
> $q \mid 2\,\mathrm{ord}(D)$ — covering every base the corpus builds under that
> law, including ones not yet prepared.

**The only contingent content of this unit's verdict is one sentence:**
$\mathrm{ord}(D)\le 3$ at the committed instances. Everything else about the
forward obstruction is forced.

### 9.3 The reverse obstruction: a 2-group abelianisation, and a one-way street

Every homomorphism $\langle W,D\rangle\to\mathbb Z/p$ kills the commutator
subgroup, and the abelianisation is measured — by building the commutator
subgroup explicitly, not by citing the presentation — to be a **2-group** at
every instance of every scope (orders $\{2,4\}$). For every **odd** declared
prime the reverse census is therefore trivial, **with no dependence on the prime
at all** (G27). `abelianization-lax` dies there, as does `model-lax`.

That is a *second* obstruction, and it is first-class because of what it does at
the live cells (G34):

> **The reverse census is empty at all 140 cells — including the 3 where the
> forward census is not.** Reverse emptiness is therefore **not** coextensive
> with order-coprimality: at exactly those 3 cells $\gcd(p,\lvert G\rvert)\ne 1$
> and the reverse count is still zero, a measured mismatch of 3 cells.
> `reverse-alias`, which reads the reverse count off the forward one, dies there.

**The measured consequence.** At every declared cell of every declared scope,
structure-preserving maps run in **one direction only**: deformation $\to$
transport, and never back. Where a morphism exists at all it can only exhibit
the deformation side **as a sub-object** of the transport side. So even at the
extended scopes, and even if a successor promoted a live cell to a committed one,
"spacetime built FROM quantum geometry" could not mean an identification in this
census's sense; it could at most mean an embedding, one way.

### 9.4 The two prime sets, both computed

Both sets are now computed in the run and gated against each other (G32):
`prime_radical(2·ord(D))` by trial division over the measured defect orders, and
the reduction test on $\rho$'s denominator. `radical-inject`, which injects an
instance of defect order 5, dies there.

| measured | value |
|---|---|
| primes dividing $2\,\mathrm{ord}(D)$ at the committed instances | $\{2,3\}$ |
| primes at which $\rho = (1/6,1/6)$ fails to reduce | $\{2,3\}$ |
| instances whose radical contains 2 | **8 of 8** |
| instances whose radical contains 3 | **1 of 8** (base T) |
| the union with that one instance deleted | $\{2\}$ |

**The coincidence has one degree of freedom, and this is what it is.** The prime
**2** is *forced*, not coincidental: every group $\langle W,D\rangle$ of the
one-law family has order $2\,\mathrm{ord}(D)$, so 2 divides it always — 8 of 8.
The prime **3** is supplied by **one instance**, base T; delete it and the union
is $\{2\}$. So the claim that carries logical weight is the **inclusion** — the
committed transport orders are 3-smooth, hence inside the two inadmissible
primes — and the *equality* of the two sets rests on a single instance. Both are
reported at that strength.

### 9.5 The statement, scoped

> **At the committed instances — and only there — the primes dividing
> $2\,\mathrm{ord}(D)$ are 3-smooth, so they lie inside the two primes at which
> the deformation side's residual does not reduce: the deformation side cannot be
> built at the primes at which the match would be possible.**

That is scoped deliberately, because **it is false one scope out**. At GEN's
twelve rebuilt classes the primes dividing $2\,\mathrm{ord}(D)$ are
$\{2,3,5,7\}$, of which **5 and 7 are admissible** on the deformation side —
which is exactly the scope-2 table of §4 and the FOUNDs of §8.3. The general
sentence "the deformation side cannot be built where the match would be
possible" is **not** a claim of this unit at any scope beyond the committed
instances.

*One correction of record.* The ledger's own summary of this unit at v13 #267
("the two structures miss each other ARITHMETICALLY: the gravity side needs odd
primes to exist") was unscoped and imprecise — the deformation side needs primes
**not dividing 6**, not "odd" primes, and the disjointness statement holds at the
committed carriers only; it is corrected at v13 LOG #273, whose adjudication
also carries the external constructions this delivery gates natively: the
live-cell pairs of §8.3, the one-law derivation of §9.2, the sector statistics
of §14 open 2, the sixteen-label witness of §6 and the count formula's negative
control in §5. §9.5 above is the statement that survives.

---

## 10. The verdict

$$\textbf{BRG-EMPTY-AT-CARRIER}$$

derived **inside gate G31** from the measured counts; recomputed there by a
second expression over the same five booleans; and derived a **third** time from
the recorded census tables by re-summing the per-cell counts of the *other*
route — so neither a hand-typed verdict nor a corrupted count survives.
`verdict-flip`, `count-flip` and `qualifier-typo` all die at G31, as do twenty
other mutants whose damage propagates to the derivation — 23 of the 65 in
total. **Every qualifier below is recomputed
inside that gate from its own source** (13 of them, 0 disagreements), so a typed
qualifier cannot reach the receipt.

| qualifier | value |
|---|---|
| scope | the committed transport instances at the declared primes |
| primes | 7 |
| instances | 8 |
| directed cells | 112 |
| extended-scope cells | 168 |
| completion-family members | 40 320 |
| non-degenerate group morphisms, forward | **0** |
| non-degenerate group morphisms, reverse | **0** |
| non-degenerate functor pairs | **0** |
| live extended-scope cells | 3 |
| admissible-prime cells FOUND outside the committed scope | 3 |
| obstruction (forward) | order-coprimality |
| obstruction (reverse) | 2-group abelianisation (prime-independent) |
| prime-tracking candidates excluded | 1 |

**What this says, and at what strength.** At the committed carriers, over the
arena-invariant content, this program's spacetime structure is **alongside** its
transport geometry, not built from it — because the only structure-preserving map
between the two measured group actions is the one that collapses the deformation
side's dynamics, and the named reason is that a prime-order group and a group of
order 2, 4 or 6 share no non-identity element order. The reverse census adds
that the maps could only ever have run one way (§9.3).

**What it does not say.** It does not say the two structures are unrelated. Over
the extended scopes a non-trivial morphism **does** exist — 14 non-trivial group
maps, at $p\in\{5,7\}$ into the defect-order-5, -15 and -7 classes, and, because
the source action is free, each extends to non-degenerate structure-preserving
pairs in counts of **240, 240 and 656 digits**; at those cells explicit pairs
satisfy the full delivered predicate and pass the held-out protocol with zero
violations (§8.3). They are measured, reported (X05), and excluded from the
verdict by the pin's own requirement 4, because their existence is a function of
the declared reduction prime. It does not say the group-level obstruction is
universal — completions with $\mathrm{ord}(D)\in\{5,7,15\}$ are 57% of the
declared family (§14 open 2). And it does not say anything about whether such a
morphism could be promoted to a map of the two sides' **encodings**: that is the
strengthened standard of §2.6 and it is untested in both directions.

---

## 11. The receipt

`v13/code/brg_bridge_exact.py` emits `brg_bridge_output.txt` and
`brg_bridge_receipt.json`. Interpreter `/opt/homebrew/bin/python3.13` (3.13.2).
Exact arithmetic throughout: integers, `fractions.Fraction` and exact
$\mathbb F_p$; no float or complex literal and no `float()`/`complex()` call
appears in the source, and the scanner that measures it is validated by a
synthetic injection it must flag (G28). No function that registers a gate reads
a mutant switch, a mutant name, a run-mode boolean or `sys.argv`, measured by an
AST guard that is itself validated by a synthetic sample it must flag (G29).
Anchor failures are exit-1, and the anchor policy is measured (G30). The two
randomised sweeps (G35, G40) draw from streams seeded by the sha256 of declared
byte strings alone — no wall-clock value and no operating-system entropy — so two
runs draw the same sequence.

| item | value |
|---|---|
| anchors (exit-1-only) | **87**, all reproduced |
| gates | **42** — **40** must-pass, **0** failures; **2** disclosure-grade (G39, G41), recorded and not must-pass because analytically forced |
| disclosures | **12** (X01–X12) |
| mutants | **65**, **0** survivors, `never_falsified` **empty** |
| runs | two full delivery runs, byte-identical output and receipt |

**Hash pins.**
`v13/note-brg-bridge-pin.md` sha256
`56ce4a7e2deeaaa24dd9cedf43e117f5c0d68774d48ac62a0120786bdba99b1b`;
`v13/code/ha_successor_receipt.json`
`542b8735daf0ebc6fc0063068e85c76f05cbca53b7f1174968f6ca79dc0068d4`;
`v13/code/nt_transport_receipt.json`
`d256891b479a8636fe88df5e9b0f553998140f1553fdfc167662220b44eeb03e`;
`v13/code/gen_generality_receipt.json`
`e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292`;
`v13/code/xba_crossbase_receipt.json`
`6015708df2a437a61955c1e194a0273b0eb712699844c9e6eb567cc3536db053`;
`v13/code/psi_curvature_receipt.json`
`7c7b91a9257e3888f3e1048366d728b5adead82b84cc9ef36175c0ba3e99fa75`;
`v13/paper-xba-crossbase.md`
`2041ebcd8b3c70f9d637f02764db438c393bf58f4b90a1cec2d807502f8e16f5`.

### Disclosures

| id | disclosure |
|---|---|
| X01 | $\lvert\mathrm{hom}(\mathbb Z/p,D_n)\rvert = \gcd(n,p)$ is analytically forced **for odd $p$**; it FAILS at $p = 2$ (measured, at every $n\le 20$ tested), which is inadmissible on the deformation side. Recorded, never gated; neither census route invokes it. |
| X02 | At GEN's equivariant class $\lvert\langle W,D\rangle\rvert = 2$ while GEN's measured based-holonomy group order is 1, because that base refuses the links altogether. Two coordinates; this unit's census consumes the $\langle W,D\rangle$ coordinate (XBA's), and the agreement anchor is taken at the eleven classes of defect order $\ge 2$ where the two coincide. |
| X03 | Base 1's and base S's defects are not determined by the published receipts; neither is guessed, both candidate sets are swept, and every member gives the same group order. |
| X04 | The synthetic FOUND branch is exhibited at a declared synthetic pair, at $p = 3$, outside the deformation side's admissible primes. It is **not** the only exercise of the FOUND machinery: the same held-out protocol runs at the three live extended-scope cells, at the admissible primes 5 and 7, and passes there too (G36). What excludes those cells is requirement 4, not a failure of the verification. |
| X05 | Over the extended scopes a non-trivial group morphism does exist, at $p = 5$ into the defect-order-5 and -15 classes and at $p = 7$ into the defect-order-7 class, and each extends to non-degenerate pairs of 240, 240 and 656 digits. Measured, reported, and excluded from the verdict by requirement 4. |
| X06 | The functor-level census counts SP-satisfying pairs by the orbit-representative formula; the counts are astronomically large and entirely degenerate. Only the non-degenerate count enters any argument. |
| X07 | The held-out check is a two-valued measurement (rotation vs reflection), not a test of the declared extension formula: for a rotation-valued extension the held-out equations hold identically because $\langle D\rangle$ is abelian. Measured under five rotation rules and five reflection rules (G39). |
| X08 | EMPTY and FOUND are demonstrated at different evidential standards, and an in-arena FOUND was foreclosed before any census ran by an arithmetic the unit computes (G41). |
| X09 | The two FORWARD census routes are two implementations of one criterion over a shared abstract model, disclosed as such; the model is audited at G03 (explicit isomorphism) and G27 (abelianisation). The two REVERSE routes are genuinely different computations. |
| X10 | G27's outcome is analytically forced for the dihedral family, and the dihedral form is itself forced by the one law (G35); the gate is retained because the commutator subgroup is BUILT, not cited. G14's outcome is forced in the nine-label arena only — G40 measures that it is contingent at sixteen labels. |
| X11 | The strengthened standard of §2.6 is REGISTERED and UNTESTED: no cell of any scope is evaluated against S1–S6, in either direction. |
| X12 | Three anchors carry values published in the XBA paper's committed table rather than in a receipt's JSON (species 4's two fixed-configuration counts and its 120-member split). The paper file is hash-pinned so those anchors are hash-protected, and all three are recomputed from the rebuilt permutations. |

### The mutant table

65 declared mutants, every one exiting 1 with a named kill, no survivor, and no
must-pass gate left unfalsified. Twelve anchor mutants (each of the seven hash
pins, the rebuilt defect permutation, the family sweep, the $\mathbb F_p$
reduction, the instance orders, and the anchor-failure policy); three discipline
mutants (freeze, float scanner, AST scanner); five functor/predicate mutants;
ten census mutants (route B, route aliasing, cell drop, class drop, family drop,
count formula, orbit count, scope leak, dictionary drop, functor-cell drop);
twelve arena-invariance and self-test mutants (single prime, blinded tracking,
null relabelling, null conjugation, cache leak, cache disuse, verdict-selected
self-test set, spectrum swap, self-routed comparator, blinded self-test, blinded
generator sweep, nine-label contingency); six reachability/held-out mutants; and
seventeen obstruction, family-theorem, live-cell and verdict mutants (obstruction
misnaming, abelianisation, model replacement, reverse aliasing, radical
injection, narrowed group zoo, non-involutive exchange, live-cell group map,
collapse map, sector bound, tiny-cell drop, tiny arena order, dictionary scope,
invariance union, verdict flip, count flip, qualifier typo).

---

## 12. Deviations and declared choices

1. **Base 1 @ SP-E/SP-F and base S enter the group-level census by their
   measured group order, from which the isomorphism type follows**, not by a
   rebuilt permutation action. NT's base has an exchange-*anti*-invariant
   preparation, so GEN §8.1's Householder cancellation does not apply and the
   defect is not a function of a completion permutation that the receipts
   publish. The group order is what a group morphism census consumes, it is
   anchored exit-1 from XBA, and the whole ambiguity set is swept (§3.3, X03).
   Those three instances are outside the **functor-level** census of §5, which
   runs at the five rebuilt instances only; that restriction is declared, and it
   costs nothing at the committed scope, because the functor-level count is zero
   wherever the group-level count is zero. It does mean the functor level is
   measured only where it is already zero; §8.3 measures the live cells directly
   instead.
2. **The extended scopes are not committed carriers.** GEN's twelve classes were
   each rebuilt in full by GEN itself, so their numbers are committed
   measurements of GEN's; they are not committed *instances* of the corpus's
   prepared bases, and this unit's verdict is taken at scope 1. The
   40,320-member family is a swept declaration. The extended scopes are reported
   as instrument readings (X05, G36). This scope choice is one of the two
   exclusions that keep the live cells out of the verdict (§8.3); it is a
   declaration, not an arena argument, and the verdict's decision variable is a
   union-over-primes reading at scope 1 while G14's is an intersection reading.
   A reader who prefers to call the twelve classes "committed carriers" gets the
   same verdict, because the arena-invariant intersection is empty at every one
   of them too — **for the structural reason recorded at G14, not for a
   contingent one**, and that reason is scoped to the nine-label arena (G40).
3. **The FOUND branch is exhibited twice, at two standards.** The pin asked for a
   compatible pair to be *injected*; it is, and it is labelled synthetic in the
   paper, the output and the receipt. Separately, the same machinery is run at
   the three live extended-scope cells at admissible primes (§8.3, G36) and
   reported under its own label. Neither is evidence about the committed arena;
   the first is a reachability demonstration, the second is an instrument
   reading requirement 4 excludes.
4. **The verdict's arena-invariance reading is the intersection over the prime
   sweep.** Requirement 4 forbids the prime from carrying the verdict either way;
   the operational form of that — "a morphism must exist at every admissible
   arena point, not at a convenient one" — is this unit's declared reading,
   recorded in §2 before any census ran, and it is what G14 gates. A reader who
   rejects that reading is rejecting requirement 4, not this measurement: the
   per-prime table is printed in full so the alternative reading can be taken
   directly from it. Its consequence — that an in-arena FOUND was unreachable a
   priori — is disclosed at X08 and measured at G41.
5. **`sys.set_int_max_str_digits` is raised, precautionarily.** The functor-level
   census produces exact integers of tens of thousands of digits; only their
   **bit length** is printed, and the largest string-formatted integer in the run
   is the 42-digit dictionary space. This raises a printing limit, never a
   precision one; the arithmetic is exact integer arithmetic throughout.
6. **Base S's 864-member ambiguity sweep uses the family sweep's own
   classification** rather than recomputing each defect, to keep the run inside
   budget. The classification is the one anchored against GEN's receipt; the two
   constraint values that select the class are read from the pinned XBA receipt
   and anchored exit-1, and the class size is computed from the classification,
   not typed (G04).
7. **Two measurements are sampled, and say so.** The one-law family sweep (G35)
   draws 400 pairs on 4–8 points, and the sixteen-label contingency sweep (G40)
   draws 2,000 completions; both streams are seeded by the sha256 of declared
   byte strings, so both are deterministic and reproduce across runs. Their
   claims are existential ("the relation holds at every draw"; "witnesses with
   $35 \mid \mathrm{ord}(D)$ exist, and here is one") and are stated as sampled.
   Everything else in the unit is exhaustive at its declared scope.
8. **Gate identifiers are not numerically monotone in the run.** G01–G31 keep
   the meanings they carry throughout this unit; the eleven added gates are
   numbered G32–G42 and are registered where they are measured, which places
   some of them before G28–G31 in the output and the receipt's gate list.
9. **No Lean.** The pin says Lean NONE.

---

## 13. Non-claims

- **No claim that the two structures are unrelated.** The census is EMPTY at a
  declared scope over arena-invariant content; §4, §7 and §8.3 measure the
  opposite at two of seven primes, one scope out, and report it.
- **No claim that spacetime is or is not built from quantum geometry in general.**
  The pin's FOUND/EMPTY reading is stated at the committed carriers; nothing here
  is a statement about the corpus's programme as a whole, about the continuum, or
  about any limit.
- **No claim that a live cell is a bridge.** At the delivered standard a live
  cell is a divisibility fact about one integer plus a free choice of images
  (§5, G37). The standard that would earn the word is registered and untested
  (§2.6, X11).
- **No Einstein-dynamics claim of any kind**, and no identification of $\Delta^B$,
  $\Omega_{\text{hypersurface}}$ and $R^\rho{}_{\sigma\mu\nu}$.
- **No cardinality criterion.** Equal carrier size is neither necessary nor
  sufficient and is used nowhere.
- **No claim about the group orders themselves.** $\lvert\langle R_{HH}\rangle\rvert$
  moves with the declared prime (HA G30) and appears here only as an instrument
  reading.
- **No claim that the found synthetic morphism means anything physical.** It is a
  reachability demonstration at an inadmissible prime.
- **No claim about why the prepared bases sit where they do.** §14 open 2 records
  the measurement and refuses the explanation.
- **No repair, extension or criticism of HA, NT, GEN, XBA or PSI.** Their numbers
  are reproduced, not adjusted; where two of their coordinates differ (X02) both
  are reported at their own coordinate.
- Nothing here is citable before an external hostile round confers TERMINAL.

---

## 14. Opens

1. **Can the reduction prime be fixed by anything other than declaration?**
   This is the single gate on the successor. Every live morphism in this unit
   lives at a prime-dependent cell, so requirement 4 excludes it however good the
   transport side gets — and the transport half is easy: **4,608** of the
   40,320 declared completions have $\mathrm{ord}(D) = 5$, and the smallest of
   them moves just **3** labels (both measured at G38). The successor's
   dichotomy is therefore stated as a
   dichotomy: **derive the prime**, and the extended-scope census of §4 becomes a
   physical statement this unit hands over already computed; or **accept
   declaration-relative bridging** and say so in those words, in which case the
   from-vs-alongside question is answered only relative to a declaration.
2. **Why do the prepared bases concentrate in the closed sector?** Measured
   (G38): of the 40,320-member declared family, $5{,}760 = 1/7$ have
   $\mathrm{ord}(D)\le 3$ — the band every committed instance occupies, 8 of 8 —
   while $23{,}040 = 4/7$ admit some declared prime. The family is
   **majority-live**; the corpus's prepared bases are not. Is that a physical
   selection rule of the preparation, or an artifact of which six bases happen to
   have been built? The numbers are in hand and the question is open.
3. **A morphism of the richer structures.** This unit's carrier functor relates
   two group actions. Whether a functor relating the two sides' *encodings* —
   HA's record-is-metric linear map and GEN/XBA's completion-to-defect map — can
   be posed without passing through the group actions is not decided; F1 was
   swept at the group layer and the encoding layer factorised through it. This is
   requirement S1 of §2.6, and it is the non-negotiable one.
4. **The arena-component correspondence.** Requirement (1) asks for a mapping
   between the arenas — fronts/registers/lapses $\leftrightarrow$
   wings/pointers/completions. This unit abstracts both sides to (group, set)
   pairs, which is strictly more exhaustive for an EMPTY verdict and strictly
   weaker for any FOUND. No component dictionary is posed.
5. **Base 1's and base S's defects.** Publishing them as permutations would let
   the functor-level census run at all eight committed instances rather than five.
6. **The sixteen-label arena.** G40 exhibits completions there whose defect order
   is divisible by $5\times 7$: the first objects in this corpus on which
   requirement 4's intersection reading would have something to bite. Building one
   as a prepared base, rather than sampling it, is a transport-side question the
   successor can pose immediately.
7. Untouched, and inherited: everything HA §14 lists beyond the morphism
   question — the divided form with its decoder, a record-derived direction
   labelling, a geometry-update law, $R_{DD}$, $R_{DH}$, general $d$, general $L$.
