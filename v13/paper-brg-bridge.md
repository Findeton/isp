# BRG — THE MORPHISM-CENSUS BRIDGE: FROM, OR ALONGSIDE?

**Status:** `GREEN-UNREVIEWED` — delivered 2026-08-08; no hostile round has run.
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
`xba_crossbase_receipt.json`.
**Verdict:** **`BRG-EMPTY-AT-CARRIER`** — at the committed carriers, over the
arena-invariant content, with the obstruction named: **order-coprimality**.
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
non-degenerate structure-preserving maps between the committed carriers; what is
measured NON-EMPTY, and then excluded from the verdict by the pin's own
requirement 4, is a family of morphisms that exists at two of the seven declared
primes and not at the other five.

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
| (1) a **carrier functor** declared as data before any morphism is evaluated, non-triviality gated, a degenerate collapse a named kill | §2.2, §2.3; gates G01, G06 |
| (2) a **morphism census** at a declared finite scope, never one expression, with the preservation predicate declared as data | §2.4, §4, §5, §7, §8; gates G02, G09, G10, G11, G17, G18, G19 |
| (3) **two-way gates**, each outcome reachable, each reachability demonstrated by a declared falsifier; FOUND requires predictive held-out verification | §9; gates G21–G25 |
| (4) **arena-invariance gating**: the prime, the naming and the coordinate artifacts may not carry the verdict either way | §6; gates G12, G13, G14, G15, G16 |

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
| **boundary** | two measured group actions: the deformation side $\bigl(C_{HA}(p) = \mathbb F_p^{k}\times\mathbb F_p^{d},\ \langle R_{HH}\rangle\cong\mathbb Z/p$ acting by translation of the address register by $\rho \bmod p\bigr)$, and the transport side $\bigl(C_{TR} = \text{system pair}\times\text{pointer pair},\ \langle W,D\rangle$ dihedral of order $2\,\mathrm{ord}(D)\bigr)$ |
| **family** | 7 declared primes $\times$ 8 committed transport instances $\times$ 2 directions; extended scopes: GEN's 12 rebuilt completion classes, and the whole $8! = 40{,}320$-member completion family |
| **law** | the structure-preservation predicate SP1–SP3 of §2.4; a candidate morphism is a **pair** $(\varphi,\Phi)$ of a group map and a carrier map |
| **state** | the deformation side's base total record $(n_{\text{sym}},0)$; the transport side's initial configuration $j_0 = 0$ |
| **arena action** | the prime sweep; relabelling of either carrier; conjugation of the transport action by a carrier permutation; replacement of the source generator $R\mapsto R^{j}$ |
| **provenance** | four committed terminal receipts, hash-pinned; every reused number read from them and reproduced |
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
| **F1-RECORD-COMPLETION** | *the pin's declared lead.* Object part: a dictionary $\delta$ from the deformation side's geometry records to the transport side's completions. Group part: the induced $\langle R_{HH}(r)\rangle\to\langle W,D(\delta(r))\rangle$. Encoding part: HA's record-is-metric datum (counts $\leftrightarrow q$, G28, determinant 2) against GEN/XBA's completion datum ($Q\mapsto D$). |
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

**Construction rule:** the morphism is fitted on the FIT orbit and extended to
every other orbit by the declared **source** symmetry — the front translations
and a register translation transverse to $\rho$ — carried by a declared
assignment into the target group. Equivariance on the HELD orbits is therefore a
**prediction**, not an imposition. Two extensions are declared: **E-ROT**
(rotation-valued, inside $\langle D\rangle$) and **E-REF** (reflection-valued on
part of its domain), and E-REF is declared in advance to be the teeth: it must
FAIL the held-out check.

---

## 3. The two sides, rebuilt

Neither side is quoted; both are rebuilt here from their own units' published
laws and anchored exit-1, quantity by quantity, against the committed receipts.
**77 anchors, all reproduced.**

### 3.1 The transport side, from GEN §8.1's defect law

With the carrier factorised as system pair $\times$ pointer pair, $\Sigma$ the
label exchange, $W = \Sigma\otimes\Sigma$ and
$D = (\Sigma Q^{\mathsf T}\Sigma Q)\otimes I$:

| rebuilt | measured | anchored against |
|---|---|---|
| base G's declared defect permutation | $[0,2,1,6,4,5,3,7,8]$ | GEN receipt |
| its order / fixed configurations | 2 / **45** of 81 | GEN receipt |
| $W$'s fixed configurations at base G | **9** of 81 | XBA receipt |
| $\lvert\langle W,D\rangle\rvert$ at base G | **4** | XBA receipt |
| base 1's wing exchange and its two factors, fixed configurations | **6**, 18, 12 of 36 | NT receipt |
| species 4: defect / exchange fixed configurations, $\lvert\langle W,D\rangle\rvert$ | **192**, **16** of 256, **4** | XBA paper |
| species 4's own 120-member transposition family, split by defect order | **12 / 60 / 48** | XBA §9.4 |
| base T: $\mathrm{ord}(D)$, $\lvert\langle W,D\rangle\rvert$ | **3**, **6** | XBA receipt |
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
measurement is recorded here because §10 turns on it: **$\rho$ does not reduce
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
at the five rebuilt instances and all twelve rebuilt classes (G03, RUNBOOK §14
addendum #219); `comparator-self`, which routes the comparator through the
audited component, dies there.

---

## 4. The census at the group level, both directions

A candidate morphism is a pair, so the census factorises: for each group map
$\varphi$ the equivariant carrier maps are enumerable (§7), and a
**non-degenerate** pair requires a **non-trivial** $\varphi$. The group-level
census is therefore the load-bearing one, and it is exhaustive.

**Scope 1 — the committed instances.** 7 primes $\times$ 8 instances = **56
cells**, **112 directed cells**, each visited exactly once, the count computed
from the declared sets (G09).

| $p$ | every committed instance |
|---|---|
| 5, 7, 11, 13, 17, 19, 23 | $\lvert\mathrm{hom}(\mathbb Z/p,\langle W,D\rangle)\rvert = 1$; non-trivial **0** |
| 5, 7, 11, 13, 17, 19, 23 | $\lvert\mathrm{hom}(\langle W,D\rangle,\mathbb Z/p)\rvert = 1$; non-trivial **0** |

$$\boxed{\text{non-degenerate group morphisms, forward: } \mathbf{0}\ \text{of 56 cells};\qquad
\text{reverse: } \mathbf{0}\ \text{of 56 cells.}}$$

**Two independent routes, agreeing at every cell (G10).** The forward count is
computed by the **element-power route** (iterated multiplication in the target,
testing $g^{p} = e$) and by the **cyclic-subgroup-lattice route** (each element's
span built as a *set*, the spans deduplicated into the lattice, the ones whose
order divides $p$ kept and their generators counted). The reverse count is
computed by a route that works **in $G$** (generator images swept, extended by
breadth-first word evaluation, verified on the whole multiplication table) and
by a route that works **in the abelianisation** (the commutator subgroup built
by closing the set of commutators, the quotient's own table formed, its
generators' images swept). Neither route reads the other: the taint counter is
measured **0** and both invocation counters are nonzero. `route-b-lax`, which
omits the trivial subgroup from the lattice, and `route-alias`, which returns
the first route's own answer, both die at G10.

The counting identity $\lvert\mathrm{hom}(\mathbb Z/p, D_n)\rvert = \gcd(n,p)$ is
**analytically forced** and is recorded as a disclosure (X01), not used as a
gate: neither route invokes it.

**Scope 2 — GEN's twelve rebuilt classes.** 7 primes $\times$ 12 classes = **84
cells** (G11). Here the answer is different, and it is the whole finding of §6:

| cell | non-trivial forward morphisms |
|---|---|
| $p = 5$, class $\mathrm{ord}(D) = 5$ | 4 |
| $p = 5$, class $\mathrm{ord}(D) = 15$ | 4 |
| $p = 7$, class $\mathrm{ord}(D) = 7$ | 6 |
| every other cell of the 84 | 0 |

**14 non-trivial group morphisms exist over scope 2** — and they exist at two of
the seven declared primes and at none of the other five.

---

## 5. The functor level: the carrier maps themselves

The source action is measured **free** (translation by $\rho\not\equiv 0$), so
every stabiliser is trivial and, given $\varphi$, an equivariant $\Phi$ is
exactly a free choice of image per source orbit. The number of
structure-preserving pairs is therefore

$$\#\{(\varphi,\Phi)\ \text{satisfying SP}\}\;=\;
\sum_{\varphi\in\mathrm{hom}(\mathbb Z/p,\,\langle W,D\rangle)}
\lvert C_{TR}\rvert^{\,\#\text{orbits}},$$

computed exactly as an integer at each of **35** cells (the rebuilt instances at
the seven primes). The counts are astronomical — from 793 bits at $p=5$ to
97,337 bits at $p=23$ — and **entirely degenerate**: the non-degenerate count is
**0** at every cell, because the only $\varphi$ available is the trivial one.

Two independent routes again:

- the **orbit count** is computed by union-find over the generator's own edges
  and by dividing the carrier size by the orbit length; the two agree at all 35
  cells (G17), and `orbit-lax` dies there;
- the **count formula** is checked against an **exhaustive brute-force
  enumeration of every function** from the source carrier to the target carrier,
  filtered by the very predicate the census uses, at three declared tiny cells
  (G18):

| tiny cell | source | target | group maps | formula | brute force | non-degenerate |
|---|---|---|---|---|---|---|
| TINY-A | $\mathbb Z/2$ on 4 points | Klein four, regular on 4 | 4 | 16 | **16** | 12 |
| TINY-B | $\mathbb Z/3$ on 3 points | $D_3$, regular on 6 | 3 | 18 | **18** | 12 |
| TINY-C | $\mathbb Z/5$ on 5 points | Klein four, regular on 4 | 1 | 4 | **4** | **0** |

The tiny set includes a cell with non-trivial group maps and a cell with none,
so the brute-force route validates the formula on both sides of the question it
is used to answer. `formula-lax` dies at G18.

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
declared prime sweep**. Measured over all **20** instances of both scopes: **no
instance admits a non-trivial morphism at every declared prime** — indeed none
admits even
two of them, since that would require $2\,\mathrm{ord}(D)$ divisible by a product
of two declared primes, and $\mathrm{ord}(D)\le 15$ over the whole family. The
arena-invariant census is EMPTY at every instance of every declared scope.
`invariance-lax`, which reads the test as a union, dies at G14.

**The symmetry self-tests** (RUNBOOK §14; G15, G16). The predicate's verdict and
the census's counts are measured invariant under the arena's own action:
relabelling the source carrier (625 points moved), relabelling the target carrier
(81 moved), conjugating the transport action by a carrier permutation (81 moved),
and replacing the source generator $R$ by $R^{j}$ for every $j\not\equiv 0$. The
tested set is fixed by declaration and is measured to be the declared one, never
selected by the verdicts under audit; `selftest-select` dies there, as do
`relabel-lax` and `conj-lax`, which would relabel and conjugate by the identity
— the gate measures how many points each declared action moves and requires it
to be nonzero. Every self-test evaluation **bypasses the memo cache** (35
bypasses, **0** self-test cache hits) while the cache is measured, at that gate,
to have been looked up **100** times and hit **5** times elsewhere in the run, so
the zero-hit clause is not vacuous (§14 addenda #185 and #219); `cache-lax` and
`cache-unused` die at G16.

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

---

## 8. Both outcomes reachable, and the held-out verification

A predicate that cannot return its other value anywhere is not a measurement.
Both values are exhibited, by the same machinery.

### 8.1 FOUND is reachable, and its verification is predictive (G21–G24)

A **declared synthetic compatible pair** is injected: source
$\mathbb Z/3$ acting on $\mathbb F_3^{2}\times\mathbb F_3^{2}$ (81 points, 27
free orbits) by translation by $(1,1)$; target base T's rebuilt
$\langle W,D\rangle$ of order 6, whose defect has order 3. It is declared
**synthetic** and outside the committed arena for a measured reason: HA's own
$\rho = (1/6,1/6)$ does not reduce at $p = 3$ (§3.2, X04).

The census returns **2 non-trivial group maps**. The carrier morphism is then
built under the declared protocol: fitted on the **FIT orbit alone** — 1 orbit,
**3 points touched**, verified by the fit-touch counter — and extended to the
other **26** orbits by the declared source symmetry. Its equivariance is then
verified on every HELD orbit: **234 held-out cells, 0 violations**, equations the
construction never imposed. The morphism is ACCEPTED by the full predicate.
`heldout-leak`, which fits on the held-out orbits, dies at G21, G22 and G23.

**The held-out gate has teeth** (G22). The *same* construction with the declared
reflection-valued extension E-REF fails the held-out check at **54 of 234**
cells and is rejected by the census, while E-ROT passes at every one. The
mechanism is exactly the one under test: a reflection does not commute with the
rotation that carries the group map, so the prediction breaks on precisely the
orbits the fit never saw. `teeth-off`, which makes E-REF silently
rotation-valued, dies there.

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

---

## 9. The obstruction, named

The verdict is EMPTY, so the pin requires the obstruction to be named: **which
preserved structure cannot be matched.**

> **The obstruction is order-coprimality**, and it is measured **coextensive with
> emptiness in both directions** over every cell of every declared scope: of 140
> cells, **137** are empty and **3** are live, and the forward census is empty
> **exactly** where $\gcd\bigl(p,\lvert\langle W,D\rangle\rvert\bigr) = 1$ (G26).

The naming is falsifiable because cells of both kinds occur — a criterion that
held vacuously everywhere would name nothing. `obstruction-misname`, which
substitutes a cardinality claim, dies at G26. (No cardinality test is used as a
criterion anywhere in this unit; equal carrier size is neither necessary nor
sufficient, and HA said so first.)

Stated at its measured strength, in the two directions:

**Forward.** $\mathrm{hom}(\mathbb Z/p,\langle W,D\rangle)$ is trivial iff
$p \nmid 2\,\mathrm{ord}(D)$. The source group has prime order $p$, so a
non-trivial image needs an element of order exactly $p$; the transport group has
order $2\,\mathrm{ord}(D)$, and by Lagrange no such element exists unless
$p \mid 2\,\mathrm{ord}(D)$. Over the committed instances $\mathrm{ord}(D)\le 3$,
so $2\,\mathrm{ord}(D)\in\{2,4,6\}$ and **no declared prime divides any of them**.

**Reverse.** Every homomorphism $\langle W,D\rangle\to\mathbb Z/p$ kills the
commutator subgroup, and the abelianisation is measured — by building the
commutator subgroup explicitly, not by citing the presentation — to be a
**2-group** at every instance of every scope (orders $\{2,4\}$). For every **odd**
declared prime the reverse census is therefore trivial, **with no dependence on
the prime at all** (G27). `abelianization-lax` dies there.

And the obstruction is not an artifact of the declared prime list:

> At the committed instances the only primes dividing $2\,\mathrm{ord}(D)$ are
> $\{2,3\}$ — and $\{2,3\}$ are **exactly** the primes at which the deformation
> side's own exact residual $\rho = (1/6,1/6)$ fails to reduce. **The deformation
> side cannot be built at the primes at which the match would be possible.**

That is a measurement, not a rhetorical flourish: both sets are computed in the
run and printed beside each other.

---

## 10. The verdict

$$\textbf{BRG-EMPTY-AT-CARRIER}$$

derived **inside gate G31** from the measured counts, and recomputed there by an
independent expression over the same counts which must agree — so a hand-typed
verdict cannot survive. `verdict-flip` dies at G31, as do eleven other mutants
whose damage propagates to the derivation.

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
| obstruction | order-coprimality |
| prime-tracking candidates excluded | 1 |

**What this says, and at what strength.** At the committed carriers, over the
arena-invariant content, this program's spacetime structure is **alongside** its
transport geometry, not built from it — because the only structure-preserving map
between the two measured group actions is the one that collapses the deformation
side's dynamics, and the named reason is that a prime-order group and a group of
order 2, 4 or 6 share no non-identity element order.

**What it does not say.** It does not say the two structures are unrelated. Over
the extended scopes a non-trivial morphism **does** exist — 14 of them, at
$p\in\{5,7\}$ into the defect-order-5, -15 and -7 classes — and it is measured,
reported (X05) and excluded from the verdict by the pin's own requirement 4,
because its existence is a function of the declared reduction prime. A future
unit that could fix the reduction prime by something other than declaration would
have a different question to ask, and this unit's measurements are what it would
start from.

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
Anchor failures are exit-1, and the anchor policy is measured (G30).

| item | value |
|---|---|
| anchors (exit-1-only) | **77**, all reproduced |
| gates | **31**, all must-pass, **0** failures |
| disclosures | **6** (X01–X06) |
| mutants | **47**, **0** survivors, `never_falsified` **empty** |
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
`6015708df2a437a61955c1e194a0273b0eb712699844c9e6eb567cc3536db053`.

### Disclosures

| id | disclosure |
|---|---|
| X01 | $\lvert\mathrm{hom}(\mathbb Z/p,D_n)\rvert = \gcd(n,p)$ is analytically forced; recorded, never gated; neither census route invokes it. |
| X02 | At GEN's equivariant class $\lvert\langle W,D\rangle\rvert = 2$ while GEN's measured based-holonomy group order is 1, because that base refuses the links altogether. Two coordinates; this unit's census consumes the $\langle W,D\rangle$ coordinate (XBA's), and the agreement anchor is taken at the eleven classes of defect order $\ge 2$ where the two coincide. |
| X03 | Base 1's and base S's defects are not determined by the published receipts; neither is guessed, both candidate sets are swept, and every member gives the same group order. |
| X04 | The FOUND branch is exhibited only at a declared synthetic pair, at $p = 3$, outside the deformation side's admissible primes. Nothing about the committed arena is claimed from it. |
| X05 | Over the extended scopes a non-trivial group morphism does exist, at $p = 5$ into the defect-order-5 and -15 classes and at $p = 7$ into the defect-order-7 class. Measured, reported, and excluded from the verdict by requirement 4. |
| X06 | The functor-level census counts SP-satisfying pairs by the orbit-representative formula; the counts are astronomically large and entirely degenerate. Only the non-degenerate count enters any argument. |

### The mutant table

47 declared mutants, every one exiting 1 with a named kill, no survivor, and no
must-pass gate left unfalsified. Ten anchor mutants (each of the five hash pins,
the rebuilt defect permutation, the family sweep, the $\mathbb F_p$ reduction,
the instance orders, and the anchor-failure policy); three discipline mutants
(freeze, float scanner, AST scanner); five functor/predicate mutants
(non-triviality, base-point-only equivariance, orientation reversal, dropped
composition clause, blinded breaking map); nine census mutants (route B, route
aliasing, cell drop, class drop, family drop, count formula, orbit count, scope
leak, dictionary drop); nine arena-invariance mutants (single prime, blinded
tracking, null relabelling, null conjugation, cache leak, cache disuse,
verdict-selected self-test set, spectrum swap, self-routed comparator); six
reachability/held-out mutants (held-out leak, teeth removal, FOUND block, EMPTY
block, ambiguity truncation, held-out quantity); and five obstruction/verdict
mutants (obstruction misnaming, abelianisation, dictionary scope, invariance
union, verdict flip).

---

## 12. Deviations and declared choices

1. **Base 1 @ SP-E/SP-F and base S enter the group-level census by their
   measured isomorphism type, not by a rebuilt permutation action.** NT's base
   has an exchange-*anti*-invariant preparation, so GEN §8.1's Householder
   cancellation does not apply and the defect is not a function of a completion
   permutation that the receipts publish. The isomorphism type is what a group
   morphism census consumes, it is anchored exit-1 from XBA, and the whole
   ambiguity set is swept (§3.3, X03). Those three instances are outside the
   **functor-level** census of §5, which runs at the five rebuilt instances only;
   that restriction is declared, and it costs nothing, because the functor-level
   count is zero wherever the group-level count is zero.
2. **The extended scopes are not committed carriers.** GEN's twelve classes were
   each rebuilt in full by GEN itself, so they are committed measurements; the
   40,320-member family is a swept declaration. The verdict is taken at scope 1
   and the extended scopes are reported as instrument readings (X05). A reader
   who prefers to call the twelve classes "committed carriers" gets the same
   verdict, because the arena-invariant intersection is empty at every one of
   them too (G14).
3. **The FOUND branch is synthetic.** The pin asked for a compatible pair to be
   *injected*; it is, and it is labelled synthetic in the paper, the output and
   the receipt. It is not evidence about the committed arena in either
   direction.
4. **The verdict's arena-invariance reading is the intersection over the prime
   sweep.** Requirement 4 forbids the prime from carrying the verdict either way;
   the operational form of that — "a morphism must exist at every admissible
   arena point, not at a convenient one" — is this unit's declared reading,
   recorded in §2 before any census ran, and it is what G14 gates. A reader who
   rejects that reading is rejecting requirement 4, not this measurement: the
   per-prime table is printed in full so the alternative reading can be taken
   directly from it.
5. **`sys.set_int_max_str_digits` is raised.** The functor-level census produces
   exact integers of tens of thousands of digits; only their **bit length** is
   printed. This raises a printing limit, never a precision one; the arithmetic
   is exact integer arithmetic throughout.
6. **The three under-determined instances' 864-member ambiguity sweep uses the
   family sweep's own classification** rather than recomputing each defect, to
   keep the run inside budget. The classification is the one anchored against
   GEN's receipt.
7. **No Lean.** The pin says Lean NONE.

---

## 13. Non-claims

- **No claim that the two structures are unrelated.** The census is EMPTY at a
  declared scope over arena-invariant content; §4 and §7 measure the opposite at
  two of seven primes and report it.
- **No claim that spacetime is or is not built from quantum geometry in general.**
  The pin's FOUND/EMPTY reading is stated at the committed carriers; nothing here
  is a statement about the corpus's programme as a whole, about the continuum, or
  about any limit.
- **No Einstein-dynamics claim of any kind**, and no identification of $\Delta^B$,
  $\Omega_{\text{hypersurface}}$ and $R^\rho{}_{\sigma\mu\nu}$.
- **No cardinality criterion.** Equal carrier size is neither necessary nor
  sufficient and is used nowhere.
- **No claim about the group orders themselves.** $\lvert\langle R_{HH}\rangle\rvert$
  moves with the declared prime (HA G30) and appears here only as an instrument
  reading.
- **No claim that the found synthetic morphism means anything physical.** It is a
  reachability demonstration at an inadmissible prime.
- **No repair, extension or criticism of HA, NT, GEN or XBA.** Their numbers are
  reproduced, not adjusted; where two of their coordinates differ (X02) both are
  reported at their own coordinate.
- Nothing here is citable before an external hostile round confers TERMINAL.

---

## 14. Opens

1. **Can the reduction prime be fixed by anything other than declaration?** Every
   live morphism in this unit lives at a prime-dependent cell. If some other part
   of the corpus forces $p$, the extended-scope census of §4 becomes a physical
   statement rather than an arena reading, and this unit hands it over already
   computed.
2. **The two inadmissible primes.** $\{2,3\}$ are simultaneously the primes at
   which $\rho$ fails to reduce and the only primes that could break the
   obstruction at the committed instances. Whether that coincidence has a reason
   — whether the denominator 6 of the finite bracket covector and the order
   $2\,\mathrm{ord}(D)$ of the commutator group are two readings of one fact — is
   untouched here.
3. **A morphism of the richer structures.** This unit's carrier functor relates
   two group actions. Whether a functor relating the two sides' *encodings* —
   HA's record-is-metric linear map and GEN/XBA's completion-to-defect map — can
   be posed without passing through the group actions is not decided; F1 was
   swept at the group layer and the encoding layer factorised through it.
4. **Base 1's and base S's defects.** Publishing them as permutations would let
   the functor-level census run at all eight committed instances rather than five.
5. Untouched, and inherited: everything HA §14 lists beyond the morphism
   question — the divided form with its decoder, a record-derived direction
   labelling, a geometry-update law, $R_{DD}$, $R_{DH}$, general $d$, general $L$.
