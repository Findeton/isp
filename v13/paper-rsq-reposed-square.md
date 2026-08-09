# RSQ — THE RE-POSED SQUARE AT THREE WINGS

**Status:** `TERMINAL` — panel #308/#309/#312 (3× ACCEPT-WITH-FIXES),
adjudicated #314; repairs R-RSQ-1…R-RSQ-10 delivered #318 and
adjudicator-verified (independent plain-run byte-identity + full
falsification selftest, 76/76 mutants dead, zero never-falsified
gates); v13 ledger #319, 2026-08-09.  **Pin:**
`v13/note-rsq-reposed-square-pin.md` (STRICT, sha256 `bc79fb6111ff…`, commit
`d9e3a66`).  **Code:** `v13/code/rsq_reposed_square_exact.py`, with
`_output.txt` and `_receipt.json`.  **Lean:** none.

$$\boxed{\textbf{RSQ-SQUARE-FOUND-BRIDGE-EMPTY}}$$

with **both halves of the name computed**:

| half | computed qualifier | what it says |
|---|---|---|
| **FOUND** | `FOUND-ONLY-AT-UNMOTIVATED-IDENTIFICATIONS` | the candidates that pass the stillborn precheck are exactly the identifications with no stated motivation; every motivated one is stillborn |
| **EMPTY** | `UNIVERSAL-BY-THEOREM-AT-EVERY-PRIME-GE-5` | the census is empty not by coverage but by a theorem about the readout's rows, at every prime $p \ge 5$ |
| the motivated sub-family, censused separately | `RSQ-NO-COMPATIBLE-SQUARE` | restricted to the identifications anybody has argued for, this instrument's own pre-registered outcome |

Both readings ship. The premise of the FOUND branch is genuinely reached —
580 of 1 440 covariant cells survive the precheck at $p = 5, 7$ (652 at
$p \ge 11$) — and the bridge is nevertheless empty, for a **new, arena-free**
reason that is proved rather than swept.

---

## Scope box

**What is decided.** At one declared pairing — HA's deformation side rebuilt
at $d = 3$ against TB3's three-wing transport side — the commuting square of
BRG's requirement S1, taken together with BRG's registered injectivity horn
S3 and the additivity clause S1b, is **unsatisfiable at every cell of the
covariant family, in both directions, at every wing symmetry, and at every
prime $p \ge 5$** — not only the seven declared. The obstruction is derived,
not censused: it is the **order obstruction** $(I - E)^{\mathrm{ord}(\pi)} =
I$, and §7.2 proves from the readout's own row structure that the deformation
side's readout never satisfies it. The pin's minimum candidate — the
$\mathbb F_p[S_3]$-module square at an $S_3$-equivariant identification — dies
one level earlier, at the **stillborn precheck**, and for a reason that is
sharper still: the record datum space at $d = 3$ carries the $S_3$
**permutation** module.

**What is not decided.** Nothing about other encodings, other deformation
sides, other transport bases, or the set-level relaxation at a grown arena.
The FOUND half is a statement about which identifications survive a structural
precheck and about nothing else; it is not a bridge. No physical claim about
spacetime, gravity, or the from-question is entered here; this is a
measurement about one square between two committed encodings.

**Provenance.** TB3 (#299), LCB (#297), HA (#262), BRG (#276) and PSI (#265)
are terminal; their papers and receipts are hash-pinned in the receipt and
every reused number is recomputed here and anchored exit-1 against them.

---

## 1. The question, and what the pin required

LCB proved the OLD square — records↔metric against completions↔commutators,
with scalar intertwining — **empty universally**, by the fixed-point mismatch
in its registered clauses. The from-question therefore moved to the flesh: is
there a **different, honestly-motivated encoding pairing at three wings**
whose square is not stillborn, and if so does a bridge exist through it?

The pin fixed six construction items, all as data before fixture truth: HA
rebuilt at $d = 3$; TB3's terminal three-wing machinery as the transport side;
a **declared family** of candidate squares including the $d = 3$
record-is-metric encoding against the three-wing commutator encoding with
**module-level intertwining over $\mathbb F_p[S_3]$**; the **stillborn
precheck** run first, per candidate, as a structural stage; the full
strengthened test for survivors; and a prime section recomputing the
scale-threshold table and testing R2-LCB's predicted $p = 7$ spectral
meeting as a measurement.

The pin's question names the sub-family it cares about — *honestly-motivated*
— and this paper answers it in that sub-family's own terms as well as over
the whole declared covariant closure. §6.3 reports the two separately; §12
names both.

---

## 2. The pairing as data

Everything in this section is **declaration**, recorded before any candidate is
evaluated. The instrument measures its candidate-evaluation counter to be
**zero** at the freeze point (G01), and the `freeze-lax` mutant, which
evaluates one candidate first, dies there.

| coordinate | declaration |
|---|---|
| **boundary** | one PAIRING at three wings. **Deformation side:** HA rebuilt at $d = 3$ — $X = (\mathbb Z_3)^3$ (27 sites), 6 links (the 3 axes and the 3 positive diagonals), the record datum space $V = \mathbb F_p^6$ (the six link counts at a site), HA's record↔metric readout $E$, and the arena $C_{HA}(p) = \mathbb F_p^{k}\times\mathbb F_p^{3}$ with a **3-dimensional address register**. **Transport side:** TB3's three-wing base — the 8 system-triple labels $\mathbb F_2^3$, the completion group $G_C$ of permutations fixing label 0, the wing symmetry group $S_3$ acting by bit permutation, and the three-wing commutator encoding $\delta_\pi(Q) = \Sigma_\pi Q^{-1}\Sigma_\pi^{-1}Q$ — TB3's $F_3$. |
| **family** | the candidate-square family: (i) the $S_3$-**equivariant** identifications of the six metric slots with the six links, their number COMPUTED by an exhaustive equivariance test and never typed, $\times$ 2 directions — the MODULE cells; (ii) HA's own `sym_index` ordering $\times$ 2 directions — the LEX cells; (iii) the whole **covariant orbit** of the slot-relabelling group, $6! = 720$ slot orders $\times$ 2 directions, of which the remainder are the **GENERIC** cells — an arbitrary relabelling of the six metric slots, with no stated motivation; (iv) the declared census cells, chosen by a rule stated before any fixture truth; (v) 7 declared primes; (vi) the 6 wing symmetries; (vii) two arena scales — the NATIVE 8-label arena and the GROWN family $L_m$; (viii) the dimensions $d = 2,3,4,5$ at the fixed-space, criterion and spectral sweeps |
| **law** | BRG's S1–S6 as its terminal §2.6 registers them, with **S1c generalised** per R2-LCB's F-10 from the two-wing $\mathbb Z/2$ SIGN condition to the $\mathbb F_p[S_3]$ MODULE condition: $\alpha$ intertwines the $S_3$-action on the record datum space with the wing action on the image |
| **state** | the base geometry record `G3-FLAT` $= (1,1,1,2,2,2)$ (HA's own declared $d = 3$ record); TB3's five declared ord-target completions; the detector site $x^\ast = (0,0,0)$ |
| **arena action** | the DIRECTION sweep; the choice of wing symmetry inside $S_3$; the prime sweep; change of basis of $V$ by a declared element of $GL_6(\mathbb F_p)$; the arena scale. The **metric-slot relabelling group $S_6$ is declared as FAMILY, not as arena action**: it does not act by conjugation on the readout (it permutes columns only), so the fixed-space dimension and the precheck status move under it, and the 1 440-cell sweep is a **coverage sweep over distinct encodings** rather than an invariance orbit. $GL_6$ conjugation is this unit's one genuine covariance, and §11 measures it. The three-wing 8-label arena is INHERITED from TB3; its effect is reported at both scales rather than tested by re-declaration |
| **admission** | a candidate is ACCEPTED only if every clause of S1 holds and S2, S3 hold. A candidate is **STILLBORN** if the precheck fails, and then no census is run for it and the mismatch is recorded |

### 2.1 The square

$$\begin{array}{ccc}
V & \xrightarrow{\;E\;} & V\\[2pt]
\downarrow{\scriptstyle\alpha} & & \downarrow{\scriptstyle\alpha}\\[2pt]
G_C & \xrightarrow{\;\delta_\pi\;} & G_C
\end{array}
\qquad\qquad \delta_\pi\circ\alpha \;=\; \alpha\circ E$$

with $\delta_\pi(Q) = \Sigma_\pi Q^{-1}\Sigma_\pi^{-1}Q$. At two wings, where
$\Sigma$ is an involution, that is GEN's $\delta(Q) = \Sigma Q^{\mathsf T}
\Sigma Q$ verbatim.

---

## 3. Item 1 — HA constructs at $d = 3$

The deformation side is rebuilt, not cited. Every number below is measured in
the run.

| measured | value |
|---|---|
| sites / links | **27** / **6** (the 3 axes and the 3 positive diagonals), both agreeing with the counts the declaration forces |
| HA's three declared $d = 3$ records | all **3 admissible** by the exact Sylvester criterion at every site |
| the two declared negative controls (one singular, one indefinite) | both **REJECTED** by the same test |
| HA's own G28 readout at $d = 3$ (rows the links sorted, columns `sym_index`) | $\det = \mathbf 8$ |
| the natural identification's readout, $q\to$counts | $\det = \mathbf 8$, spectrum $\{1,1,1,2,2,2\}$ |
| $q$ reproduces every declared link count | **81 of 81** sites |
| the general law, re-measured at $d = 2,3,4,5$ | $\det = 2^{d(d-1)/2}$, spectrum $\{1^d, 2^{d(d-1)/2}\}$ |

That is exactly the object R2-LCB's F-10(d) specified for the successor:
$\det 8$ and spectrum $\{1,1,1,2,2,2\}$. `arena3-lax`, `readout3-lax` and
`posdef-lax` all die (G04, G05).

### 3.1 The residual, and G29 at $d = 3$

$R_{HH}$ is computed by two comparators that share no code — the literal
five-map composition on exact rational fields, and the closed form built from
the drag rule and the record readout — and they agree at **27 of 27** sites.
The exact rational residual at the detector site is

$$\rho(x^\ast) \;=\; \bigl(\tfrac16,\ \tfrac16,\ 0\bigr),$$

nonzero at 1 of the 27 sites, with the same denominator 6 the $d = 2$ arena
has. The reduced carrier is then built with a **3-dimensional address
register**, and HA's G29 holds verbatim at $d = 3$:

| $p$ | carrier $p^{k+3}$ | $\rho \bmod p$ | $\lvert\langle R_{HH}\rangle\rvert$ | translation-by-$\rho$ |
|---|---|---|---|---|
| 5 | 3 125 | $(1,1,0)$ | **5** | measured configuration by configuration |
| 7 | 16 807 | $(6,6,0)$ | **7** | measured configuration by configuration |
| 11 | 161 051 | $(2,2,0)$ | **11** | measured configuration by configuration |
| 13 | 371 293 | $(11,11,0)$ | — | carrier not built (declared cap) |
| 17 | 1 419 857 | $(3,3,0)$ | — | carrier not built (declared cap) |
| 19 | 2 476 099 | $(16,16,0)$ | — | carrier not built (declared cap) |
| 23 | 6 436 343 | $(4,4,0)$ | — | carrier not built (declared cap) |

> $R_{HH}$ acts on the reduced carrier as the **translation of the
> 3-dimensional address register by $\rho \bmod p$**, with the front sector
> returning to itself — verified configuration by configuration at every built
> prime. Hence $\langle R_{HH}\rangle\cong\mathbb Z/p$.

The build cap is a declared computational scope (the carrier has $p^{k+3}$
configurations), not a measured boundary (X04); $\rho$ is reduced at all seven
declared primes. **No claim below depends on it:** the deciding criterion takes
the readout and the wing-symmetry order as its only inputs, and §7.2 decides
the four primes the cap excludes — 13, 17, 19, 23 — by the same theorem that
decides every other prime $\ge 5$ (G40). `carrier3-lax` and `residual3-lax`
die (G06, G07). And the holonomy order is again measured to be an **arena
coordinate** — it equals the declared prime at every built prime while the
exact rational residual is prime-independent — so RUNBOOK §15 excludes it from
every argument below (G08); `prime-single` dies there.

**The deformation side therefore CONSTRUCTS at $d = 3$**, and the pin's
`RSQ-BLOCKED-AT-⟨the d=3 arena⟩` branch is not taken.

---

## 4. Item 2 — the transport side at three wings

| measured | value |
|---|---|
| $\lvert G_C\rvert$ | **5 040**, by enumeration and independently as the factorial the declaration forces |
| the wing symmetry group | order **6**, measured **NON-ABELIAN**, element orders $\{1,2,2,2,3,3\}$, closed over all 36 compositions |
| labels fixed by EVERY wing symmetry | $\{0, 7\}$ — label 7 is $\lvert111\rangle$ |
| wing symmetries with $P^2 = \mathbf 1$ | **4** of 6 |
| $\delta_\pi = F_3$ at $6\times5 = 30$ (wing, completion) cells | **30 of 30** — a code-duplication check, since the live branch and $F_3$ are the same four-factor expression written twice |
| $F_1 = \delta_\pi$ | at **20** cells, and at **20 of 20** involution cells and nowhere else — the contingent measurement in that table |
| the twisted cocycle identity for $F_2$ | **0** deviations of 150 cells (an identity in any group; a disclosure) |

The $F_1$/$F_3$ split reproduces TB3's own measurement — the four-factor
writing agrees with the commutator exactly at the cells whose wing symmetry
squares to the identity — with $20 = 4\ \text{such symmetries}\times 5\
\text{completions}$, computable in advance. `wing-lax` and `encoding-lax` die
(G09, G10).

### 4.1 The ladder as the structure-group family

TB3's ladder is rebuilt here as this pairing's own structure-group family: at
each of TB3's five declared ord-target completions the defect subgroup
$K = \langle\delta_\pi(Q) : \pi\in S_3\rangle$ is closed explicitly as a
permutation group on the 8 labels.

| completion | $\lvert K\rvert$ rebuilt | TB3's committed $\lvert K\rvert$ |
|---|---|---|
| ord 1 | **1** | 1 |
| ord 3 | **12** | 12 ($A_4$) |
| ord 2 | **168** | 168 ($\mathrm{GL}(3,2)$) |
| reference (GHZ) | **360** | 360 ($A_6$) |
| ord 6 | **2 520** | 2 520 ($A_7$) |

Five for five, anchored exit-1 against TB3's receipt. `ladder-lax` dies at G11
and `anchor-ladder` at the anchors.

### 4.2 The fixed-point wall transports

$$\delta_\pi(Q) = Q \iff \Sigma_\pi Q^{-1}\Sigma_\pi^{-1} = e \iff Q = e,$$

because conjugation is injective. There is **no hypothesis on the arena** in
that line, and it is measured rather than argued:

| arena | members | $\lvert\mathrm{fix}(\delta_\pi)\rvert$ |
|---|---|---|
| the three-wing 8-label arena, at each of the **6** wing symmetries | 5 040 | **1**, and the fixed point is the identity |
| LCB's own two-wing 9-label arena (external anchor) | 40 320 | **1** |

So LCB's F-1 wall **transports to three wings unchanged**, exactly as R2-LCB
predicted. `fixpoint-lax` dies at G12.

---

## 5. Item 3 — the candidate-square family, declared as data

### 5.1 The identifications

HA's datum is one datum in two coordinate systems, so the readout becomes an
endomorphism of one space only after an **identification** of the six metric
slots with the six links and a **direction**. Both are declarations and both
are swept: the identification's whole orbit under the slot-relabelling group
is covered.

The $S_3$-**equivariant** identifications — the ones at which the module
condition is natively posable — are found by an **exhaustive equivariance
test over all 720 slot orders**, and the count is computed, never typed:

| | slot order | reading |
|---|---|---|
| **NATURAL** | $(q_{11},q_{22},q_{33},q_{12},q_{13},q_{23})$ | each diagonal slot with its axis link, each off-diagonal slot with the diagonal link of the same pair |
| **SWAP** | $(q_{23},q_{13},q_{12},q_{33},q_{22},q_{11})$ | each diagonal slot with the diagonal link of the complementary pair |

**Exactly two**, and that is what the orbit structure forces: both index sets
are two free copies of the natural $S_3$-set, and the centraliser of $S_3$ in
$S_3$ is trivial. `equi-lax` dies at G13.

### 5.2 The covariant family, and the declared census cells

| | count |
|---|---|
| slot orders enumerated | **720** (the factorial the declaration forces) |
| covariant cells (slot orders $\times$ 2 directions) | **1 440**, cell-complete |
| of them MODULE / LEX / GENERIC cells | **4** / **2** / **1 434** |
| declared census cells, by the rule below | **9** (computed, and reproduced exactly by an independent rebuild) |

The **motivated** identifications are the 4 MODULE cells and the 2 LEX cells:
the two $S_3$-equivariant orderings, at which the module clause is natively
posable, and HA's own `sym_index` ordering, which is the coordinate HA
delivers its readout in. The other 1 434 are GENERIC — an arbitrary
relabelling of the six metric slots, argued for by nobody. That distinction is
not decoration: §6.3 measures which class the precheck's survivors lie in, and
§12's FOUND qualifier is derived from that measurement.

The census-cell rule is stated in the instrument before any census runs: every
equivariant identification, both directions; HA's own `sym_index` (LEX)
ordering, both directions; per direction the lexicographically first slot order
whose fixed space is trivial at every declared prime; and per direction the
lexicographically first slot order that both survives the precheck at the
reference prime and admits the order-3 demanded eigenvalue there. The rule
returns a set containing both module cells and cells of **every measured
precheck status**, so the census is not run only where it is expected to be
empty; its return is rebuilt cell by cell by a second equivariance test that
shares no code with it, and the two agree exactly, so the cell count is a
measured **equality** and not a bound (G15). `cell-orbit-drop`, `cell-drop` and
`censuscell-lax` die (G14, G15).

### 5.3 The two encodings, stated

**The deformation side.** With the natural identification and the
$q\to$counts direction,

$$E \;=\;
\begin{pmatrix}
1&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&1&0&0&0\\
1&1&0&2&0&0\\
1&0&1&0&2&0\\
0&1&1&0&0&2
\end{pmatrix},
\qquad \det E = 8,\qquad \mathrm{spec}\,E = \{1,1,1,2,2,2\}.$$

In block form, on (axis links, diagonal links),

$$E \;=\; \begin{pmatrix} I & 0 \\ J - I & 2I \end{pmatrix},$$

with $J$ the all-ones matrix in the missing-index labelling. The reversed direction is $E^{-1}$, with spectrum
$\{1,1,1,\tfrac12,\tfrac12,\tfrac12\}$.

**The transport side.** $\delta_\pi(Q) = \Sigma_\pi Q^{-1}\Sigma_\pi^{-1}Q$,
with $\Sigma_\pi$ the bit permutation of the eight labels.

**The intertwining condition, stated exactly.** A candidate is a map
$\alpha : V\to G_C$ with

$$\textbf{S1a}\ \ \delta_\pi(\alpha(r)) = \alpha(Er)\ \ \forall r;\qquad
\textbf{S1b}\ \ \alpha\ \text{additive};\qquad
\textbf{S3}\ \ \alpha\ \text{injective};$$

$$\textbf{S1c-module}\ \ \alpha\circ\rho_V(\pi) = \rho_A(\pi)\circ\alpha
\ \ \forall\pi\in S_3,$$

where $\rho_V$ is the $S_3$-action on the record datum space and $\rho_A$ is
conjugation by $\Sigma_\pi$ on the image. **This is the module condition, not
a scalar or a sign:** it is R2-LCB's proper generalisation of the two-wing
$\mathbb Z/2$ parity clause.

---

## 6. Item 4 — the stillborn precheck

### 6.1 The precheck, and its two-way calibration

The commuting square forces $\alpha(\mathrm{fix}\,E)\subseteq
\mathrm{fix}\,\delta_\pi$. §4.2 measures $\lvert\mathrm{fix}\,\delta_\pi\rvert
= 1$ at every wing symmetry and every arena. So an **injective** candidate
needs $\lvert\mathrm{fix}\,E\rvert = 1$, i.e.

$$\boxed{\dim\ker(E - I) = 0 \ \text{over}\ \mathbb F_p.}$$

A candidate failing that is **STILLBORN**: the mismatch is computed and no
census is run. The precheck is calibrated in both directions before it is
applied, through the same function — a synthetic compatible pair
($\dim\mathrm{fix} = 0$) **PASSES**, and a synthetic **invertible** matrix with
$\dim\mathrm{fix} = 1$, measured to be none of the 1 440 encodings of the
family under audit, **FAILS**. The negative arm is therefore independent of the
objects it is used to judge; `precheck-lax`, `precheck-blind` and
`negcontrol-lax` all die at G16.

### 6.2 The candidate table, with per-candidate precheck results

| candidate | role | slot order | direction | $\dim\ker(E-I)$ | $\lvert\mathrm{fix}\,E\rvert : \lvert\mathrm{fix}\,\delta\rvert$ at $p=7$ | precheck |
|---|---|---|---|---|---|---|
| **C1** | MODULE (natural) | $(q_{11},q_{22},q_{33},q_{12},q_{13},q_{23})$ | $q\to$counts | **3** | $343 : 1$ | **STILLBORN** |
| **C2** | MODULE (natural) | same | counts$\to q$ | **3** | $343 : 1$ | **STILLBORN** |
| **C3** | LEX (HA's `sym_index`) | $(q_{11},q_{12},q_{13},q_{22},q_{23},q_{33})$ | $q\to$counts | **1** | $7 : 1$ | **STILLBORN** |
| **C4** | LEX | same | counts$\to q$ | **1** | $7 : 1$ | **STILLBORN** |
| **C5** | MODULE (swap) | $(q_{23},q_{13},q_{12},q_{33},q_{22},q_{11})$ | $q\to$counts | **2** | $49 : 1$ | **STILLBORN** |
| **C6** | MODULE (swap) | same | counts$\to q$ | **2** | $49 : 1$ | **STILLBORN** |
| **C7** | GENERIC, lex-first trivial-fix | $(q_{22},q_{33},q_{12},q_{11},q_{13},q_{23})$ | $q\to$counts | **0** | $1 : 1$ | **PASS** |
| **C8** | GENERIC, lex-first meeting | $(q_{22},q_{33},q_{12},q_{13},q_{11},q_{23})$ | $q\to$counts | **0** | $1 : 1$ | **PASS** |
| **C9** | GENERIC, lex-first trivial-fix | $(q_{22},q_{33},q_{12},q_{11},q_{13},q_{23})$ | counts$\to q$ | **0** | $1 : 1$ | **PASS** |

The dimensions are the same at every declared prime (at $p = 5$ the mismatches
read $125 : 1$, $5 : 1$ and $25 : 1$ respectively), and each recorded mismatch
is checked against $p^{\dim} : 1$ recomputed from the measured dimension
(G17), so `stillborn-lax` dies in the delivered run. Over the whole covariant
family:

| $p$ | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---|---|---|---|---|---|---|
| precheck **survivors** of 1 440 | **580** | **580** | **652** | **652** | **652** | **652** | **652** |
| **stillborn** | 860 | 860 | 788 | 788 | 788 | 788 | 788 |

### 6.3 The motivated sub-family, censused separately

The precheck's survivors are not spread across the family. Censusing the
motivated identifications on their own:

| motivated cell | $\dim\ker(E-I)$, every declared prime | precheck |
|---|---|---|
| MODULE natural, $q\to$counts / counts$\to q$ | 3 / 3 | **STILLBORN** |
| MODULE swap, $q\to$counts / counts$\to q$ | 2 / 2 | **STILLBORN** |
| LEX (HA's own `sym_index`), $q\to$counts / counts$\to q$ | 1 / 1 | **STILLBORN** |

| measured | value |
|---|---|
| motivated cells $\times$ declared primes | **6** $\times$ 7 = **42** rows |
| motivated cells surviving the precheck | **0** of 42 |
| precheck survivors that are GENERIC cells | **4 420** of 4 420 — all of them |
| the identification qualifier, derived from those two counts | `FOUND-ONLY-AT-UNMOTIVATED-IDENTIFICATIONS` |
| the motivated sub-family's **own** census, run over its own rows | **0** of 84 satisfy the order criterion |
| the verdict function's return when it is fed the motivated sub-family — every argument measured | `RSQ-NO-COMPATIBLE-SQUARE` |

Two things are measured here and both matter. **The pin's minimum candidate is
stillborn** — both $S_3$-equivariant identifications, in both directions, at
every declared prime — **and so is HA's own coordinate**. **And the precheck is
not a wall that everything hits**: the generic covariant family has survivors
at every declared prime, so the premise of the pin's `RSQ-SQUARE-FOUND-…`
branches is genuinely reached, and the census below is run on candidates that
are alive at this stage. But those survivors are exactly the identifications
nobody has argued for, selected — in the census rule's own words — as *the
lexicographically first slot order whose fixed space is trivial*, i.e. by the
property under test. The FOUND half of the verdict is therefore reported with
the class it is true of, and the motivated sub-family's own outcome is
reported beside it (G39, G35). `fixpoint-lax` dies at G16 and G17,
`motivated-lax` and `ident-flip` at G39.

---

## 7. Item 5 — the strengthened test, and the order obstruction

### 7.1 The criterion, derived

Let $\alpha$ satisfy S1a, S1b and S3, and let $A = \alpha(V)$.

1. S1a forces $\Sigma_\pi A\Sigma_\pi^{-1} = A$: for every $r$,
   $\Sigma_\pi\alpha(r)^{-1}\Sigma_\pi^{-1} = \alpha(Er)\alpha(r)^{-1}\in A$.
2. On the abelian $A$, writing $\rho$ for conjugation by $\Sigma_\pi$,
   $\delta_\pi\vert_A = I - \rho$ additively.
3. The square reads $(I-\rho)\circ\alpha = \alpha\circ E$; with $\alpha$ an
   isomorphism onto $A$, $\rho = I - \alpha E\alpha^{-1}$ — the **master
   equation** of §8, $I - E = \alpha^{-1}\rho\,\alpha$.
4. $\rho^{\mathrm{ord}(\Sigma_\pi)} = I$, because conjugation by
   $\Sigma_\pi^{\mathrm{ord}}$ is the identity.

$$\boxed{(I - E)^{\mathrm{ord}(\pi)} \;=\; I \ \text{over}\ \mathbb F_p
\quad\text{is NECESSARY.}}$$

Equivalently, since $E$ is invertible: at an **involution** it is $E = 2I$; at
an **order-3** wing symmetry it is $E^2 - 3E + 3I = 0$, whose roots are
exactly $1-\omega$ for $\omega$ a primitive cube root of unity. The matrix
power and the polynomial are **one condition in two encodings**, related by
$(I-E)^3 - I = -E(E^2-3E+3I)$; they are computed separately and agree at
**0 disagreements of 20 160 rows**, which is a redundant-encoding check and is
reported as one (G18).

### 7.2 The emptiness is a theorem

The sweep does not need to be a sweep. Write $A$ for the **integer**
$q\to$counts readout at a slot order; the other direction is $A^{-1}$.

> **Lemma (row profiles).** Every row of $A$ is a link's row in some column
> order, so its multiset of entries is one of exactly two profiles: an axis
> link gives $(0,0,0,0,0,1)$ and a diagonal link gives $(0,0,0,1,1,2)$.
> *Measured: 2 profiles over $720\times 6 = 4\,320$ rows, 2 160 of each.*
>
> **Corollary (the unit row).** Row 0 — the axis link $e_0$ — is the unit
> vector $e_k$, where $k$ is the position the identification gives the metric
> slot $(0,0)$. *Measured at 720 of 720 slot orders.*
>
> **Lemma (invertibility).** $\det A = \pm 8$, measured at 720 of 720, so $E$
> is invertible at every odd prime and the criterion is equivalent to a
> polynomial identity with integer coefficients:
> $A = 2I$ and $2A = I$ at an involution, $A^2-3A+3I = 0$ and $3A^2-3A+I = 0$
> at an order-3 wing symmetry, in the two directions respectively.

**Theorem.** *For every slot order, both directions, both wing-symmetry orders
and every prime $p \ge 5$, the order criterion fails.*

*Proof.* Read the identity at row 0. Since $\mathrm{row}_0(A) = e_k$ we have
$\mathrm{row}_0(A^2) = e_k A = \mathrm{row}_k(A)$, so each of the four
identities becomes an equation between explicit **integer** vectors:

| direction, order | row-0 witness $v$ |
|---|---|
| $q\to$counts, ord 2 | $e_k - 2e_0$ |
| counts$\to q$, ord 2 | $2e_k - e_0$ |
| $q\to$counts, ord 3 | $\mathrm{row}_k(A) - 3e_k + 3e_0$ |
| counts$\to q$, ord 3 | $3\,\mathrm{row}_k(A) - 3e_k + e_0$ |

The criterion at a prime $p$ forces $v \equiv 0 \bmod p$, hence
$p \mid \gcd(v)$. Over all $720\times2\times2 = \mathbf{2\,880}$ triples the
gcds are measured to be 1 or 2, so **no prime $\ge 5$ divides any of them**. ∎

The three branches that could have gone the other way are worth naming. At
$q\to$counts, ord 3 the identity demands $A[k][k] = 3$ while every entry of
$A$ lies in $\{0,1,2\}$ — the obstruction is $p \mid 3, 2$ or $1$. At
counts$\to q$, ord 3 it demands a row with exactly one 1 and one $-3^{-1}$ and
nothing else; $-3^{-1} \in \{0,1,2\}$ at exactly one declared prime, $p = 7$,
where $-3^{-1} = 2$ — so the identity there demands a row of profile
$(0,0,0,0,1,2)$, and by the Lemma **no readout row has that profile**. The
theorem's decision function is calibrated on exactly that near-miss: fed a
**synthetic** readout row of the forbidden profile, it reports $p = 7$ as
admissible (G40). The gate can return the other way, and what it measures is a
property of the readout and not of the test.

**Three consequences.** (i) The emptiness holds at **every prime $p \ge 5$**,
not only the seven declared — including the four the carrier build cap
excludes, which the criterion decides without ever building a carrier. (ii)
The `UNIVERSAL` qualifier is earned by algebra, not by coverage, and §12 names
it accordingly. (iii) The theorem evaluates no matrix over $\mathbb F_p$ and
runs no census, so it is a genuinely independent route to the same emptiness —
and the independence is **measured structurally**, not argued: the whole
2 880-witness sweep is recomputed with the names of *both* writings of the
order criterion unbound in the namespace, and it must both answer and return
the same admitted-prime set (G40). A theorem that reached the criterion
through any call, counted or silent, could not answer at all; `theorem-alias`,
which reaches it silently, dies there.

### 7.3 The sweep, as the theorem's confirmation

| | measured |
|---|---|
| (cell, prime, wing-order) rows swept — the WHOLE covariant family, exhaustive, no sampling | **20 160**, against the forced product $1\,440\times7\times2$ (G43) |
| rows satisfying $(I-E)^{\mathrm{ord}} = I$ | **0** |
| matrix-power vs polynomial writing: disagreements | **0** of 20 160 |
| the criterion's positive control (the synthetic encoding $\mathrm{diag}(6,6,6,4,4,4)$ at $p = 7$) | **satisfies it**, by both writings |
| **the exact extension**: the same identity as an integer matrix, whose gcd decides every prime at once | over **2 880** (slot order, direction, order) triples, the primes $\ge 5$ at which it can vanish: **none** |
| the extension calibrated against the field computation | the integer identity and $(I-E)^{\mathrm{ord}} = I$ over $\mathbb F_p$ agree at **252 of 252** calibration rows |
| **the wide corroboration census**: the same identities swept row by row against every prime from 5 to the declared ceiling 293 — 60 primes, sieved not typed | **0** of **172 800** (cell, prime, wing-order) rows, against the forced product $1\,440\times60\times2$ |
| the module obstruction's own reach, beyond its printed table | **0** of **50 400** (cell, prime, wing) rows (§8.1) |

So the criterion is a condition **something can meet** — the gate could have
come out otherwise — and HA's readout meets it nowhere, at no prime whatever.
`criterion-lax` dies at G18, G19, G28, G31, G35, G36, G41, G46 and G37 while
leaving the theorem's own gate G40 untouched; `profile-lax`, `theorem-lax`,
`theorem-alias` and `theorem-floor` all die at G40 while leaving the sweep's
count untouched — so the two routes to the emptiness are separated by mutants
as well as by namespace. `extension-lax` and `wide-drop` die at G41,
`crit-row-drop` at G43.

Both criterion censuses are corroboration, not evidence — 20 160 rows at the
seven declared primes and 172 800 at sixty primes to 293, both **0**, and both
decided in advance by §7.2. The module equality's own 50 400-row reach is
decided in advance too, by the algebra of §8.1 rather than by this theorem.

### 7.4 The criterion and the precheck

$(I-E)^{\mathrm{ord}} = I$ forces $I - E$ invertible, hence
$\dim\ker(E-I) = 0$. That implication is a theorem. What is measured is
stated as what is measured:

| measured | value |
|---|---|
| rows satisfying the criterion, out of the rows swept | **0** of 20 160 |
| (cell, prime) pairs surviving the precheck, out of the pairs swept | **4 420** of 10 080 |
| the containment as a set predicate, cell by cell | **0** violations at **0** witnesses — **VACUOUS at this family** |
| the implication exercised on the one non-vacuous instance available | the synthetic $\mathrm{diag}(6,6,6,4,4,4)$ satisfies the criterion at $p = 7$ **and** has trivial fixed space |

The precheck is therefore the structural **shadow** of the census criterion —
which is exactly the LCB lesson, installed as an instrument stage — and the
strictness of the containment is the two counts against their own
denominators, not a set relation the family has any witness for. `subsume-lax`
dies at G19.

### 7.5 The census

The candidate space is enumerated, never solved for by one expression, by two
routes:

- **Route A (linear algebra).** $\ker(E^{\mathsf T} - (1-s)I)$ by Gaussian
  elimination, multiplied by the **measured** count of subgroups the wing
  symmetry normalises with exponent $s$.
- **Route B (permutation enumeration, no linear algebra).** Every cyclic
  subgroup of order $p$ in $G_C$ is enumerated, its $\delta$-exponent table is
  built from permutations, and every covector is enumerated projectively with
  the measured redundancy $p-1$ restored.
- **Route C (literal).** At declared instances a candidate route A admits is
  rebuilt as an **actual permutation** and the square is compared entry by
  entry at every one of the $p^6$ record cells.

Route independence is **measured structurally**, not self-reported: route B is
re-evaluated with the name of route A removed from the module namespace, and
it must both answer and return the same number — 745 against 745 — so a route
B that reached route A through any call, counted or silent, could not pass.
`route-alias` and `route-silent-alias` die at G42.

| measured | value |
|---|---|
| census rows (9 declared cells $\times$ 7 primes $\times$ 5 non-identity wing symmetries) | **315**, against the forced product (G43) |
| rows whose **S1a + S1b** census is NON-EMPTY | **25** of 315 |
| rows admitting an **injective** candidate — *the order criterion restricted to the declared cells, a coverage check and not a source; see below* | **0** of 315 |
| route A vs route B disagreements | **0** of 315 |
| route B's redundancy calibration (projective vs the FULL $p^6$ enumeration at a declared cell and prime) | **745** vs **745** |
| route C | **4 rows from 2 declared instances** — an admitted and a rejected covector at each |

**The injective column is forced twice over, and is reported as a disclosure**
(X07). It is `order_criterion` evaluated at the nine declared cells, so it is
a restriction of the sweep in §7.3 and not an independent measurement; and
independently of the criterion, injectivity is impossible at the native arena
on cardinality — no census row has $p^6 \le \lvert G_C\rvert$ (0 of 315), and
$v_p(\lvert G_C\rvert)\le 1$ at every declared prime, so every elementary
abelian $p$-subgroup of $G_C$ is cyclic and every additive $\alpha$ has image
of order at most $p$. That last fact is what makes route A's restriction to
$\alpha(r) = g^{\lambda(r)}$ a **complete census** at this arena rather than a
sample.

**Route C, in full.** Two instances — the module cell, $q\to$counts, at an
involution at $p = 5$, and the module cell, counts$\to q$, at an order-3 wing
symmetry at $p = 7$ (the spectral-meeting cell) — each contributing an
admitted row and a rejected row:

| instance | record cells | admitted candidate's violations | declared rejected covector's violations |
|---|---|---|---|
| $p = 5$, involution | 15 625 | **0** | **12 500** |
| $p = 7$, order 3 | 117 649 | **0** | **100 842** |

So a candidate satisfying BRG's registered square really does exist at the
meeting cell, verified as literal permutations at every one of its 117 649
record cells. The rejected control's violation count is $p^5(p-1)$ — the
complement of a hyperplane, forced — and is reported at that strength.

The gap between the two census rows is the whole content of the strengthened
standard here: **candidates satisfying BRG's square and the homomorphism
clause do exist** — 25 rows of them — **and not one of them is injective**.
`route-a-lax`, `route-b-lax`, `literal-lax`, `census-lax` and
`census-row-drop` all die (G20–G22, G43).

---

## 8. The master equation, and the three walls as its readings

Steps 1–3 of §7.1 give more than the criterion. With $A = \alpha(V)$ and
$\rho$ the conjugation action of $\Sigma_\pi$ on $A$:

$$\boxed{I - E \;=\; \alpha^{-1}\,\rho\,\alpha.}$$

*$I - E$ is the conjugation automorphism, read through $\alpha$.* Every wall
this unit reports is a reading of that one equation:

| reading | consequence | the wall |
|---|---|---|
| $\rho\in GL(A)$ | $I-E$ invertible, i.e. $\dim\ker(E-I) = 0$ | LCB's **fixed-point mismatch** — the stillborn precheck |
| $\rho^{\mathrm{ord}(\Sigma_\pi)} = I$ | $(I-E)^{\mathrm{ord}(\pi)} = I$ | the **order obstruction** |
| $\rho = \rho_V(\pi)$ (the module clause) | $E = I - \rho_V(\pi)$ | the **permutation-module obstruction** |

The equation is verified, not asserted: at the in-arena control of §9 it holds
on the generating set at **6 of 6** and record by record at **71 of 71**
declared records, and given that $\alpha$ is a measured homomorphism it is
equivalent to the commuting square, which holds at all **117 649** record
cells (G44).

The first two readings are nested — "$\rho$ invertible" is the first-order
shadow of "$\rho^{\mathrm{ord}} = I$", which is why the order obstruction
subsumes the precheck. **The third is not.** Feeding the module-forced
$E = I - \rho_V(\pi)$ back through the other two walls, at all
$7\times5 = 35$ (prime, wing) rows:

| measured on the module-forced $E$ | value |
|---|---|
| $\dim\ker(E - I) = \dim\ker(-\rho_V(\pi))$ — LCB's precheck | **0** at 35 of 35 → **PASSES** |
| $(I-E)^{\mathrm{ord}} = \rho_V(\pi)^{\mathrm{ord}} = I$ — the order criterion | **True** at 35 of 35 → **PASSES** |
| $\dim\ker E = \dim\ker(I - \rho_V(\pi))$ | **4** at an involution, **2** at order 3 → **SINGULAR** |

So the module reading clears both other walls and dies anyway, on a third
fact: $E$ must be invertible and $I - \rho_V(\pi)$ is not. That contradiction
uses nothing about the arena, the prime part, or cardinality. The
permutation-module obstruction is **arena-free and transport-free**, and a
strictly disjoint reading of the master equation rather than a corollary of
either other wall. `master-lax` and `independence-lax` die at G44.

### 8.1 The permutation-module obstruction, measured

Suppose $\alpha$ satisfies S1a, S1b, S3 **and** S1c-module. Then
$\rho_A(\pi)\alpha = \alpha\rho_V(\pi)$, so the square gives
$\alpha(I - \rho_V(\pi)) = \alpha E$, and injectivity cancels $\alpha$:

$$\boxed{E \;=\; I - \rho_V(\pi).}$$

But $\rho_V(\pi)$ is a **permutation matrix** — the chart symmetry permutes
links, it does not mix them — so $I - \rho_V(\pi)$ annihilates the all-ones
link vector $\mathbf 1$, while $E$, being invertible, does not.

| measured | value |
|---|---|
| rows in the printed table: 6 motivated cells $\times$ 7 primes $\times$ 5 wings | **210**, against the forced product (G43) |
| rows where $E = I - \rho_V(\pi)$ | **0** |
| rows where $(I - \rho_V(\pi))\mathbf 1 = 0$ | **210** of 210 |
| rows where $E\mathbf 1 = 0$ | **0** of 210 |
| the $S_3$-action on $V$ is by permutation matrices | **6** of 6 elements, image closed with 6 distinct matrices |
| **the reach, beyond the table**: $(I-\rho_V)\mathbf 1 = 0$ | at **6 of 6** wing symmetries |
| **the reach**: $E\mathbf 1 = 0$ over the WHOLE covariant family | **0** of 10 080 (cell, prime) pairs — so the forced equality fails at all 50 400 (cell, prime, wing) rows |

Two of those columns are analytically forced and are disclosed as such (X07):
$(I-\rho_V)\mathbf 1 = 0$ holds for any permutation matrix, and $E\mathbf 1 = 0$
fails for any invertible $E$. The contingent measurement is the two-way
control: a synthetic $S_3$-action that is *not* a permutation action — the
standard representation, whose order-3 element has the primitive cube roots as
eigenvalues — has $I - \rho$ **invertible**, and the module square is
satisfiable there. So the gate can return the other way, and what it measures
is a property of the record datum space and not of the test. `module-lax`,
`module-blind` and `module-row-drop` die (G23, G43).

> **The record datum space at $d = 3$ carries the $S_3$ permutation module,
> and permutation modules always have invariants. That is why the module-level
> square cannot close.** The statement is not about HA's readout in
> particular: the contradiction is "$E$ invertible" against
> "$I - \rho_V(\pi)$ singular", so it closes the module-level square for **no
> invertible readout whatever**, at any prime, identification, direction or
> dimension, whenever the chart symmetry acts on the record datum space by
> permutations. HA's readout is one instance of a wall it does not own.

---

## 9. Both outcomes reachable, and the controls

### 9.1 FOUND is reachable, in-arena, with a synthetic encoding

At the **grown arena** of the declared growth family $L_m = \{0\}\cup
(\mathbb F_2^3\setminus\{0\})\times\{1..m\}$ — $m$ copies of TB3's seven moved
labels, $S_3$ acting on the $\mathbb F_2^3$ factor alone — with $m = 6$
(**43 labels**) and $p = 7$:

| measured | value |
|---|---|
| the six blocks, each identified with $\mathbb Z/7$ so the wing symmetry acts as multiplication by $c_k$ | $c = (2,2,2,4,4,4)$, the primitive cube roots mod 7 |
| $A = \langle g_1,\dots,g_6\rangle$ | elementary abelian of order $7^6$; generators measured to commute |
| $\Sigma g_k\Sigma^{-1} = g_k^{c_k}$ | measured at 6 of 6 |
| $\tilde E := I - \rho = \mathrm{diag}(6,6,6,4,4,4)$ | invertible, and $(I-\tilde E)^3 = I$ |
| the square $\delta_\Sigma(\alpha(r)) = \alpha(\tilde E r)$ | holds at **117 649 of 117 649** record cells |
| $\alpha$ injective / a homomorphism | **yes** / **0** violations on the declared $\{0,1\}^6\times\{0,1\}^6$ grid of 4 096 pairs |

**What this control is, exactly.** Its encoding is the **synthetic** $I-\rho$
— the arena's own conjugation action, read backwards — and not HA's readout
(X05). Given the two measured premises ($\Sigma g_k\Sigma^{-1} = g_k^{c_k}$
and $[g_i,g_j] = e$), the square $\delta(\alpha(r)) = \alpha(\tilde E r)$ is an
**algebraic identity** in $r$; the 117 649 verified cells confirm an identity.
The rung it earns is precise and it is worth having:

| rung | claim | status |
|---|---|---|
| 1 | the instrument is not a constant-EMPTY function | **earned** |
| 2 | **EMPTY is not caused by the arena, the prime, or the instrument** — the same arena and the same prime return FOUND for a different encoding | **earned**, and this is the strongest rung the control reaches |
| 3 | bridges exist in-family at scale | **not earned** — $\mathrm{diag}(6,6,6,4,4,4)$ is neither HA's readout nor any of its 1 439 relabellings |

### 9.2 The verification is exhaustive, and nothing in it is fitted

The candidate is built from the declared exponents $c$ before any record cell
is read, so the declared FIT/HELD split is a **partition** of the record space
and not an estimation. It is reported as such:

| id | measured |
|---|---|
| cells verified (the complement of the single FIT cell $e_1$) | **117 648** |
| **H1** the square at every one of them | **117 648 / 117 648** |
| **H2** the defect permutation entry by entry | the **same boolean as H1** — a tuple equality *is* the entry-by-entry comparison; reported once and disclosed |
| **H3** the fixed-label count, a transport-side quantity | read at every cell, taking the **7 distinct values** $\{1,8,15,22,29,36,43\}$ |
| **X-NOSQUARE**, **X-FLATFIX** (declared in advance to fail) | **0** passes each — and both are **analytically forced** to fail off the zero record ($\tilde E - I = \mathrm{diag}(5,5,5,3,3,3)$ is invertible mod 7; the fixed-label count is $1 + 7\cdot\#\{k : r_k = 0\}$), so they are carried as disclosures (X07) |
| cells where both extensions are analytically FORCED (the zero record, where every candidate returns the identity) | **1**, computed and gated to be exactly one |

The must-pass content of G25 is the computed exempt count: an instrument that
exempted more could not pass. `found-block`, `witness-blank`, `partition-lax`
and `teeth-off` die (G24, G25).

### 9.3 At the grown arena the criterion is also SUFFICIENT

At $p = 7$ the polynomial $x^3 - 1$ is measured to have **three distinct
roots** $\{1,2,4\}$, so any $\rho$ with $\rho^3 = I$ is diagonalisable; and
invertibility of $E = I-\rho$ excludes the eigenvalue 1. Hence every $E$
satisfying the criterion at an order-3 wing symmetry is conjugate to
$I - \mathrm{diag}(c)$ with $c \in \{2,4\}^6$ — **64 patterns**, and the
census runs over all of them:

| measured, at every one of the 64 patterns | value |
|---|---|
| the declared growth family realises the encoding | **64 of 64** |
| generators of order $p$ on pairwise disjoint supports, commuting | **64 of 64** |
| $\Sigma g_k \Sigma^{-1} = g_k^{c_k}$ at 6 of 6 | **64 of 64** |
| $\tilde E$ invertible and $(I-\tilde E)^3 = I$ | **64 of 64** |
| the square at every record of a declared 71-cell sample (exhaustively at the distinguished pattern) | **0 violations** |

$$\textbf{At } L_6,\ p = 7,\ \mathrm{ord}\ 3\textbf{, the order criterion is
not merely necessary but SUFFICIENT.}$$

At that scope the bridge question reduces **exactly** to
$(I-E)^{\mathrm{ord}} = I$ — and HA's readout fails it at every cell, every
direction and every prime $\ge 5$ (§7.2). The scope is honest and is stated:
the argument uses $p \equiv 1 \bmod 3$; at $p \not\equiv 1 \bmod 3$, $\rho$
acts irreducibly on blocks of dimension $> 1$ that the declared growth
family's diagonal $\Sigma$ cannot realise, and the converse there is open
(§16). `sufficiency-lax` dies at G45.

### 9.4 EMPTY at the same arena, and why no comparison is needed

Replacing the synthetic encoding by HA's own $d = 3$ readout at the grown
arena, the order criterion fails and the census is empty (G26). The two
procedures are not the same procedure — FOUND is a 117 649-cell permutation
construction, EMPTY is a matrix identity — and the honest statement does not
need them to be: **the order criterion takes no arena argument at all.** It is
a condition on $E$ and the wing-symmetry order alone, so no arena can rescue
HA's encoding, and growing the arena removes the cardinality obstruction
($p^6 > 5\,040$) while leaving the order obstruction exactly where it was.
What the pair of runs establishes is rung 2 of §9.1 and nothing beyond it.
`empty-block` dies at G26.

### 9.5 The negative control with teeth

**BREAK-HOM** multiplies an admitted exponent by a 1-eigencovector raised to
the $(p-1)$st power. It satisfies the commuting square at **0 violations of
117 649** cells — differing from an admitted candidate only in the
**linearity** of its exponent — and is rejected at **1 536** measured
homomorphism violations of the declared 4 096-pair grid. **The rejecting
clause is S1b, and it is named.** It is built at the **native** 8-label arena
with a rank-1 exponent (X09), and it is the one teeth-bearing control in §9.
`break-blind` dies at G27.

### 9.6 S2 and S4

**S2 (carrier rigidity):** the transport side's fixed-label stratification is
measured **carried** — the defect permutations take the seven distinct
fixed-label values $\{1,8,15,22,29,36,43\}$, so the stratification is a real
invariant and not a constant — and the clause that decides it is calibrated
the other way inside the same gate (G28), so `s2-lax` dies there.

**S4 (functoriality)** is *computed*, and the true statement is stronger than
a robustness sweep. The deciding quantity $(I-E)^{\mathrm{ord}(\pi)} = I$ has
**no base input**: the candidate enumeration ranges over every cyclic subgroup
of order $p$ in $G_C$ and every wing symmetry, and the completion that names a
ladder base never enters it. So base-independence holds **by construction**,
and the instrument measures the construction: the census's deciding inputs are
fingerprinted *inside* the per-base loop and the fingerprint is identical at
all five bases, while the bases are measured genuinely different — their
defect subgroups $1, 12, 168, 360, 2\,520$ spanning more than three orders of
magnitude — and the criterion, re-evaluated at each base's own live primes
(0, 18, 0, 36, 18 rows), is hit at **0** everywhere. The fingerprint function
is calibrated to separate different inputs inside the same gate (G46), so
`baseindep-lax` and `s4-lax` die there.

---

## 10. Item 6 — the prime section

### 10.1 The scale-threshold table, recomputed at the new pairing

Three thresholds are computed per prime: the smallest arena whose completion
group's order is divisible by $p^6$ (Legendre's formula, a genuine search),
the smallest arena containing an elementary abelian subgroup of rank 6 (the
minimal faithful permutation degree $6p$ of $(\mathbb Z/p)^6$, a closed form),
and the smallest member of the declared growth family that reaches it.

| $p$ | $p^6 \mid (n-1)!$ | elementary abelian | growth $m$ | growth labels | $d = 2$ analogue ($3p+1$) |
|---|---|---|---|---|---|
| 5 | **26** | **31** | 5 | 36 | **16** |
| 7 | **43** | **43** | 6 | **43** | **22** |
| 11 | 67 | 67 | 10 | 71 | 34 |
| 13 | 79 | 79 | 12 | 85 | 40 |
| 17 | 103 | 103 | 15 | 106 | 52 |
| 19 | 115 | 115 | 17 | 120 | 58 |
| 23 | 139 | 139 | 20 | 141 | 70 |

Two measurements are recorded here. **Divisibility is strictly weaker than
realisability** — at $p = 5$ the two thresholds are 26 and 31, so an arena
whose order is divisible by $p^6$ need not contain the subgroup an injective
homomorphism requires. And **the native three-wing arena admits an injective
candidate at NO declared prime**: $\lvert V\rvert = p^6$ exceeds
$\lvert G_C\rvert = 5\,040$ already at $p = 5$. The $d = 2$ analogue,
recomputed by the same function, reproduces LCB's own $3p+1$ thresholds (16 at
$p=5$, 22 at $p=7$) and is anchored exit-1 against them. `threshold-lax` dies
at G29.

**What the column measures, and what it does not.** It answers *does the arena
contain an elementary abelian subgroup of rank 6?* — a **capacity** question —
and not *does $\Sigma_\pi$ normalise one with the demanded exponent?* At the
native arena only 6 of the 126 order-5 subgroups are normalised, so the gap
between capacity and admissibility is real and is measured elsewhere in this
same paper (§10.2). And the threshold that opens is an arena size **defined by
the rank and the prime it is said to open** — $6p+1$ at rank 6, $3p+1$ at
rank 3 — which is the same circularity LCB reported at its own scope and
explicitly declined to read as a derivation of $p$: *"a derivation of $p$ that
must first be handed the arena $p$ chooses is not a derivation of $p$"* (LCB
§12.3). Nothing here is entered as one. This unit's own strongest result runs
the other way: the order obstruction is **arena-free**, growth removes only
the capacity obstruction, and the wall is exactly where it was.

### 10.2 The $p = 7$ spectral meeting, tested as a measurement

R2-LCB's F-10(c) predicted that at three wings the spectral obstruction moves:
for a wing symmetry of order 3 the square demands the eigenvalue $1 - s$ with
$s^3 = 1$, instead of the two-wing $2$. That is tested here **in-arena**: the
values actually realised are read off the conjugation exponents of the
subgroups each wing symmetry normalises.

| $p$ | cube roots of 1 | demanded $1-s$ (order 3) | HA's $1/2 \bmod p$ | realised in-arena | **MEETING** |
|---|---|---|---|---|---|
| 5 | $\{1\}$ | — | 3 | — | no |
| **7** | $\{1,2,4\}$ | $\{4,6\}$ | **4** | $\{4,6\}$ | **YES** |
| 11 | $\{1\}$ | — | 6 | — | no |
| 13 | $\{1,3,9\}$ | $\{5,11\}$ | 7 | — | no |
| 17 | $\{1\}$ | — | 9 | — | no |
| 19 | $\{1,7,11\}$ | $\{9,13\}$ | 10 | — | no |
| 23 | $\{1\}$ | — | 12 | — | no |

The in-arena column is measured, not assumed: at $p = 5$ only the three
**involutions** normalise a subgroup of order 5 (6 each, exponent $s = 4 = -1$,
demanding the two-wing eigenvalue 2); at $p = 7$ only the two **order-3** wing
symmetries normalise a subgroup of order 7 (6 each, exponents $\{2,4\}$ — the
primitive cube roots — demanding $\{4,6\}$); at $p \ge 11$ there is no
$p$-torsion in $G_C$ at all, which is why the demanded values at 13 and 19 are
never realised.

$$\textbf{The meeting is real, it is unique to } p = 7,
\text{ and R2-LCB's prediction is confirmed at the } d=3 \text{ pairing.}$$

**And its price is measured with it.** The meeting occurs at the *equivariant*
identification — the one whose counts$\to q$ spectrum contains $1/2 = 4 \bmod
7$ — and the precheck has already declared that cell **STILLBORN**. Where a
cell survives the precheck instead, the order obstruction still empties it. So
what the meeting buys is a non-empty S1a + S1b census and nothing more.

The near-miss is not a coincidence, and §11 says why: the meeting needs the
eigenvalue $1/2$, which lives in the counts$\to q$ direction, and in that
direction the readout at a motivated identification also carries the
eigenvalue 1 — which is exactly the stillborn condition. The two are forced by
the same spectrum. `meeting-lax` dies at G30.

### 10.3 The prime as a parameter (S6)

The partial clause list is measured prime-**dependent** — the S1a+S1b census is
live at 5 and 7 and dead above, because $G_C$ has $p$-torsion only there —
while the full clause list is measured prime-**uniform**: EMPTY at all seven
declared primes, and by §7.2 at every prime $\ge 5$. The verdict therefore does
not ride on the declared prime, and the difference between the two readings is
itself a measurement (G31).

---

## 11. The spectral reading, and the self-tests

### 11.1 The spectral reading at every swept dimension

| measured | value |
|---|---|
| $\dim\ker(E-I)$ at the NATURAL identification, $d = 2,3,4,5$, both directions, every declared prime | $= d$ at every row |
| $\dim\ker(E-I)$ at HA's own `sym_index` ordering, same sweep | $= 1$ at every row |
| rows where the eigenvalue 1 is present | **112 of 112** |

So at every motivated identification HA's readout carries the eigenvalue 1,
hence $0 \in \mathrm{spec}(I-E)$. A bridge at a wing symmetry of order $n$
forces $\mathrm{spec}(I-E)\subseteq\mu_n$, and **0 lies on no unit circle**:
the obstruction is dimension-independent in *proof* form, and it is stated
here at exactly the scope it is measured (G47). `spectral-lax` dies there.

### 11.2 The symmetry self-tests

| self-test | measured |
|---|---|
| the $S_3$-action on the record datum space | by **permutation matrices** at 6 of 6 elements, image closed with 6 distinct matrices — the fact the module obstruction turns on, measured rather than assumed |
| $\mathrm{fix}(\delta)$ recomputed **inside** a declared relabelled arena | the relabelling moves **7** labels; $\lvert\mathrm{fix}\rvert$ is still **1** at every wing symmetry |
| the tested set | fixed by DECLARATION — the whole covariant family, **1 440** cells, including the ones the precheck kills — measured strictly larger than the set the verdicts would have selected, and **consumed**: the decision quantity is recomputed at all 1 440 and agrees at 1 440 |
| change of basis of $V$ by a declared element of $GL_6(\mathbb F_p)$ | both decision quantities (the fixed-space dimension and the order criterion) recomputed inside the new basis and unchanged; the basis change measured non-trivial |
| cache discipline | **2 000** self-test bypasses, **0** self-test cache hits, against **39 741** lookups and **9 501** hits measured *before* the self-tests begin |

The two invariance clauses are analytically forced and are reported at that
strength; what the gates measure that is not forced is that the actions are
non-trivial, that the recounts are taken inside the transported arena, and
that the tested set is the declaration rather than the verdicts' own
selection. `selftest-lax`, `selftest-select`, `basis-lax`, `cache-lax` and
`cache-unused` all die (G32–G34).

---

## 12. The verdicts

$$\boxed{\textbf{RSQ-SQUARE-FOUND-BRIDGE-EMPTY}}$$

$$\texttt{FOUND-ONLY-AT-UNMOTIVATED-IDENTIFICATIONS}\qquad
\texttt{UNIVERSAL-BY-THEOREM-AT-EVERY-PRIME-GE-5}$$

$$\text{and, at the motivated sub-family: }\ \boxed{\textbf{RSQ-NO-COMPATIBLE-SQUARE}}$$

all derived **inside gate G35** from three sources that are genuinely
independent computations:

| source | what it computes | measured |
|---|---|---|
| **1** the order-criterion sweep over the WHOLE covariant family, which runs no census | $(I-E)^{\mathrm{ord}} = I$ over $\mathbb F_p$ at 20 160 rows | **0** |
| **2** the permutation-module equality count, which runs no criterion | $E = I - \rho_V(\pi)$ at 210 rows | **0** |
| **3** the readout-profile theorem, which evaluates no matrix over $\mathbb F_p$ at all | the primes $\ge 5$ admitted by any of 2 880 integer witnesses | **0** |
| *a coverage check, not a source* | the criterion restricted to the 9 declared census cells | **0** of 315 |
| a candidate PASSES the precheck | 580 of 1 440 cells at $p = 5,7$; 652 at $p\ge11$ | **yes** |
| FOUND reachable / EMPTY reachable | | **yes** / **yes** |

Sources 1 and 3 decide the **same** emptiness by disjoint computations — one
by matrix powers over $\mathbb F_p$ at 20 160 rows, one by integer gcds at
2 880 row-0 witnesses — and their disjointness is measured twice over: by
namespace (§7.2) and by mutants that move one and not the other (§7.3).
Source 2 decides a different obstruction and runs no criterion. The census
table's injective column is not a fourth source and is not conjoined here: it
is `order_criterion` evaluated at the nine declared cells, a **restriction**
of source 1, forced twice over and disclosed as such (X07).

Source 3 is what makes the second half of the name a theorem rather than a
coverage statement: the emptiness holds at **every prime $p \ge 5$**, so no
prime is left to the declared sweep, including the four the carrier build cap
excludes.

Each of the three sources is separately a deciding variable of the printed
name: `criterion-lax` (source 1 $\to$ 8 840), `module-lax` (source 2 $\to$
210) and `theorem-floor` (source 3 $\to$ 1) each move one source and one only,
and each flips the printed verdict to `RSQ-SQUARE-FOUND-BRIDGE-FOUND` at G35.
Each half of the *name* can also fail without the verdict string moving:
`ident-flip` moves the FOUND qualifier alone and `emptiness-flip` the EMPTY
qualifier alone, and G35 dies on that clause with
`RSQ-SQUARE-FOUND-BRIDGE-EMPTY` still printed. `verdict-flip` dies at G35 and
G37, `universal-lax` at G36, `qualifier-typo` at G48, where every recorded
qualifier is re-derived from its own source.

### The obstructions, named

> **THE MASTER EQUATION.** S1a, S1b and S3 force $I - E = \alpha^{-1}\rho\alpha$
> with $\rho$ the conjugation action of $\Sigma_\pi$ on the image. Every wall
> below is a reading of it.
>
> **THE ORDER OBSTRUCTION** ($\rho^{\mathrm{ord}} = I$). S1a (BRG's registered
> commuting square), S1b (additivity) and S3 (BRG's registered injectivity
> horn) jointly force $(I - E)^{\mathrm{ord}(\pi)} = I$ over $\mathbb F_p$ —
> equivalently $E = 2I$ at an involution and $E^2 - 3E + 3I = 0$ at an order-3
> wing symmetry — and HA's record-is-metric readout satisfies it at **0 of
> 20 160** swept rows and, by the readout-profile theorem, at **no prime
> $\ge 5$ whatever**. No cardinality, no $p$-part, no census enters the
> derivation, and it **subsumes** the fixed-point mismatch, which is its
> first-order shadow.
>
> **THE PERMUTATION-MODULE OBSTRUCTION** ($\rho = \rho_V(\pi)$). S1c-module
> forces $E = I - \rho_V(\pi)$, and the record datum space carries the $S_3$
> **permutation** module, so $I - \rho_V(\pi)$ always annihilates the all-ones
> link vector while $E$, being invertible, never does. It clears both other
> walls at 35 of 35 (prime, wing) rows and kills the candidate anyway.

### What this says, and at what strength

The flesh-question is answered, and the answer has two halves, each reported
with the scope it was measured at.

**The premise is reached, at the identifications nobody argued for.** A
re-posed square at three wings does pass the structural precheck — the LCB
wall, transported verbatim, does not by itself close the new pairing, and
4 420 of 10 080 (cell, prime) pairs survive it. But every survivor is a GENERIC
identification; the two $S_3$-equivariant orderings and HA's own `sym_index`
ordering are stillborn at every declared prime, in both directions, 6 cells and
42 rows of them. Restricted to the sub-family the pin's question names —
*honestly-motivated* — this instrument's own pre-registered outcome is
`RSQ-NO-COMPATIBLE-SQUARE`.

**And the bridge is empty, as a theorem.** At the strengthened standard the
census returns nothing, for an obstruction that is new, arena-free, stronger
than the one LCB found, proved at every prime $\ge 5$ rather than swept at
seven — and, for the module clause the pin named as its minimum, universal for
a structural reason about what kind of $S_3$-module the record datum space is.

### What it does not say

It does not say that no encoding pairing at three wings can work; it says this
declared family does not. It does not say that bridges exist at scale: the
FOUND control's encoding is synthetic, and what it establishes is that EMPTY is
not an artefact of the arena, the prime or the instrument. It does not decide
the **set-level** relaxation — dropping S1b removes the order criterion's
derivation, and while the native arena closes the set level anyway on
cardinality ($p^6 > 5\,040$ at every declared prime), at the grown arena the
set-level question is open and is recorded as such (X06). It enters no
physical claim.

---

## 13. The receipt

| | |
|---|---|
| anchors | **26** — **15 COMMITTED-NUMBER** anchors against TB3, LCB and HA receipts and papers, **11 ARTIFACT-HASH** pins of other units' files |
| anchor failures | **0**, and the fail-closed policy is itself gated and calibrated (G38) |
| gates | **48**, all must-pass |
| must-pass failures | **0** |
| disclosures | **9** |
| covariant cells swept | **1 440** |
| order-criterion rows swept | **20 160** at the declared primes; **172 800** at sixty primes to 293 (theorem triples: **2 880**) |
| census rows | **315** |
| module rows | **210** (family-wide reach: 10 080 (cell, prime) pairs) |
| mutants | **76**, **0** survivors |
| must-pass gates never falsified by any mutant | **none** |
| determinism | two full runs, byte-identical |

### Disclosures

| id | statement |
|---|---|
| **X01** | The pin's phrase "the encoding $V:\mathbb F_p^3\to\mathbb F_p^6$" is read here as: the record datum space at $d = 3$ is $\mathbb F_p^6$ (the six link counts at a site of a 3-dimensional chart), and the readout is the endomorphism of that space with determinant 8 and spectrum $\{1,1,1,2,2,2\}$. That is the object R2-LCB's F-10(d) measured, and the only reading under which the stated determinant and spectrum are correct. |
| **X02** | Routes A and B are genuinely different computations over SHARED data: both read the same measured subgroup set and the same encoding matrix. Route A decides by Gaussian elimination; route B decides from a $\delta$-exponent table built by permutation arithmetic with no linear algebra in it. Route C verifies the permutation square literally. Independence is measured structurally (G42), not by the taint counter, which is retained as a disclosure. |
| **X03** | The census's enumeration is scoped: route B enumerates covectors PROJECTIVELY with the measured redundancy $p-1$ restored, calibrated at a declared cell and prime against the FULL $p^6$ enumeration. The order-criterion sweep, which carries the verdict, is exhaustive over the whole covariant family at every declared prime with no sampling anywhere, and its exact extension decides every prime. |
| **X04** | The reduced carrier is BUILT as explicit permutations only at the declared build primes (its size is $p^{k+3}$); $\rho$ is reduced and the arena coordinate reported at every declared prime. A declared computational cap, not a measured boundary — and no claim depends on it: the four excluded primes are decided by the criterion, which takes no carrier as input. |
| **X05** | The in-arena FOUND control is a control, not a bridge: its encoding is the SYNTHETIC $I - \rho$, not HA's readout, and no record, metric, chart or readout of the deformation side enters it. It establishes exactly one thing — that EMPTY is not caused by the arena, the prime or the instrument. Its square is an algebraic identity once the two measured premises hold, and it is reported at that strength. |
| **X06** | The set-level relaxation is NOT decided here. Dropping S1b removes the order criterion's derivation; at the native arena the set level is closed anyway on cardinality, but at the grown arena it is open. |
| **X07** | FORCED CLAUSES, disclosed and not conjoined into any verdict gate: (a) the census's injective column is the order criterion restricted to the declared cells, forced twice over — no row has $p^6\le\lvert G_C\rvert$, and $v_p(\lvert G_C\rvert)\le1$ at every declared prime, so every additive candidate has image of order at most $p$; (b) the module table's two structural columns are algebra — $(I-\rho_V)\mathbf 1 = 0$ for any permutation matrix, $E\mathbf 1\ne0$ for any invertible $E$; (c) X-NOSQUARE and X-FLATFIX cannot pass off the zero record; (d) the matrix-power and polynomial writings of the criterion are one condition in two encodings. |
| **X08** | THE FOUND HALF'S SCOPE: the precheck's survivors are measured to be exactly the identifications with no stated motivation. Restricted to the motivated sub-family the pre-registered outcome is `RSQ-NO-COMPATIBLE-SQUARE`, and both readings ship. |
| **X09** | SCOPES OF THE CONTROL MEASUREMENTS: the homomorphism checks of the in-arena control and of BREAK-HOM run over the declared grid $\{0,1\}^6\times\{0,1\}^6 = 4\,096$ pairs, where modular wrap-around is not exercised; the master equation is verified on the generating set and on a declared 71-record sample and is equivalent to the square, which is verified at every record cell; the sufficiency census verifies the square on a declared sample per pattern, exhaustively at the distinguished pattern; BREAK-HOM lives at the NATIVE 8-label arena with a rank-1 exponent. |

---

## 14. Deviations and declared choices

1. **The pin's $\mathbb F_p^3\to\mathbb F_p^6$ is read as $\mathbb F_p^6$
   throughout** (X01). At $d = 3$ the six link counts and the six metric
   components determine each other; a $3\to6$ map would have no determinant.
   The stated determinant 8 and spectrum $\{1,1,1,2,2,2\}$ fix the reading.
2. **S1b (additivity) is carried into the module formulation rather than
   declared separately.** "Module homomorphism over $\mathbb F_p[S_3]$" *is*
   additivity plus equivariance; the unit measures the set-level consequence
   separately and discloses it as undecided at the grown arena (X06).
3. **The census cells are 9, chosen by a declared rule**, and the full
   covariant family is swept by the criterion instead. The enumerative census
   at all 1 440 cells $\times$ 7 primes was not run; the criterion sweep and
   the theorem, which carry the verdict, were.
4. **The reduced carrier is built at three primes**, not seven (X04).
5. **The growth family is one declared extension**, $m$ copies of TB3's seven
   moved labels with $S_3$ on the first factor. Other growth rules exist and
   are not tested; and $L_m$ for $m > 1$ carries **no system-triple reading** —
   it is a combinatorial capacity extension, in-family as a declared scale
   parameter and not as an interpretation.
6. **The wing symmetry $\pi$ is a parameter, not a choice**: all five
   non-identity elements are swept at every census row, and the identity is
   handled separately ($\delta_e \equiv e$, so the square forces the constant
   map and injectivity fails at once).
7. **The declared negative records at $d = 3$** (`G3-SINGULAR` $(1,1,1,4,2,2)$
   and `G3-INDEF` $(1,1,1,6,2,2)$) are this unit's own construction; HA
   declares negative controls only at $d = 2$.
8. **The basis-change invariance is analytically forced** and is reported at
   that strength (§11.2). The slot-relabelling group is declared as FAMILY,
   not as an arena action, because it is not an invariance of the object: it
   permutes the readout's columns only, so the decision quantities move under
   it (§2).
9. **The three-wing 8-label arena is inherited from TB3** and is not
   re-declared; its effect is reported at both scales (§10.1) rather than
   tested by counterfactual re-declaration.
10. **`anchor-soft` is a compound mutant**: it softens the anchor policy *and*
    perturbs one pin, because softening alone perturbs nothing and would be a
    mutant that could not die. Anchor failures are recorded and carried to the
    totals block rather than exiting on the spot, so every falsifier is scored
    at a gate against the same denominators as the honest run.
11. **The FOUND control's grown arena is in-family as a SCALE**, declared
    before fixture truth, and its encoding is out of family (X05); the control
    is stable under a $\mathbb Z/3$ wing symmetry, which is the one its
    construction uses.

---

## 15. Non-claims

- No claim that a bridge is impossible at three wings in general.
- No claim about any encoding other than HA's record-is-metric readout and
  TB3's commutator encoding.
- No claim that the set level is empty at a grown arena.
- No claim that $p = 7$ is derived rather than declared; the prime section
  reports thresholds and the meeting, not a derivation of $p$, and §10.1
  records why the threshold table cannot be read as one.
- **No claim that anything "opens with growth."** The measured scale facts are
  these and only these: a prime becomes realisable at an arena size defined by
  that prime and the rank (LCB declined to read the same pattern as a
  derivation, at its own scope); the 43-label control earns rung 2 —
  reachability and the exclusion of arena/prime/instrument artefacts — and no
  more; and TB3's torsion at three wings is a group-level fact about which
  completion is taken, at constant arena — not a growth result. This unit's
  own strongest result is arena-free.
- No claim that the FOUND half means a bridge exists.
- No physical, causal, geometric or gravitational claim of any kind.

---

## 16. Opens

1. **The set level at a grown arena.** With S1b dropped, is there an injective
   set map intertwining $E$ with $\delta_\pi$ at an arena large enough to hold
   one? The fixed-point argument is the only arena-free constraint left, and
   it does not close the precheck-surviving cells.
2. **Other record adjacencies.** The permutation-module obstruction is a
   statement about link sets that the chart symmetry permutes. A record
   adjacency whose datum space carries a non-permutation $S_3$-module would
   evade it; whether any such adjacency is honestly motivated is open — and
   an adjacency invented *because* it evades the obstruction would repeat the
   FOUND half's own weakness one level up, so its motivation must be declared
   in the deformation side's vocabulary before its module type is computed.
3. **The order obstruction at other transport bases.** $(I-E)^{\mathrm{ord}} =
   I$ is a condition on the *deformation* side alone once the wing symmetry's
   order is fixed. Bases whose symmetry group has elements of order 4, 5, 6
   would demand different eigenvalue sets, and those are not swept here.
4. **The converse away from $p \equiv 1 \bmod 3$.** §9.3 proves sufficiency at
   $L_6$, $p = 7$, ord 3. At $p\not\equiv1\bmod n$, $\rho$ acts irreducibly on
   blocks of dimension $> 1$ that the declared growth family's diagonal
   $\Sigma$ cannot realise, and whether the criterion is still sufficient
   there is open.
5. **Whether the 25 live S1a+S1b rows carry anything.** They are non-injective
   by measurement; whether their images say anything about a weaker notion of
   bridge is not asked here.

### What a successor inherits

Not the thresholds table — it measures a **capacity** obstruction, the minimal
faithful degree $rp$ of $(\mathbb Z/p)^r$, which vanishes at any large enough
arena and whose death changes nothing. What carries is the master equation,
its three readings, and one spectral invariant that scales: at every motivated
identification HA's readout carries the eigenvalue 1 at every dimension
$d = 2,3,4,5$ and every declared prime (112 of 112 rows), so
$0\in\mathrm{spec}(I-E)$ — and a bridge at a wing symmetry of order $n$ forces
$\mathrm{spec}(I-E)\subseteq\mu_n$, where 0 never lies. **The obstruction
against unitary-compatible bridges is dimension-independent in proof form**,
and a successor at a larger or continuous scale inherits a theorem rather than
a census.
