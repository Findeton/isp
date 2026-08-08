# LCB — HOSTILE REVIEW R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator/algebraic lens.
**Protocol:** `v13/note-lcb-hostile-protocol.md` (FROZEN), kill-shots K1–K5.
**Object under review, SHA-256 (first 12) verified before anything else:**

| artifact | required | measured | ok |
|---|---|---|---|
| `v13/paper-lcb-livecell.md` | `9b081a1e72af` | `9b081a1e72af` | yes |
| `v13/code/lcb_livecell_exact.py` | `57d3072b1031` | `57d3072b1031` | yes |
| `v13/code/lcb_livecell_output.txt` | `50dad82e0637` | `50dad82e0637` | yes |
| `v13/code/lcb_livecell_receipt.json` | `2ffe123e16cf` | `2ffe123e16cf` | yes |

**Method.** Everything below was rebuilt from the published laws — GEN §8.1's
$\delta(Q) = \Sigma Q^{\mathsf T}\Sigma Q$, HA §3.2/§4.1's readout and §10.1's
$C_{HA}(p)$, BRG §2.6's registry — in my own scripts under the session
scratchpad. I imported nothing from `lcb_livecell_exact.py`; where I quote its
internals it is because I read the source, not because I called it. Exact
arithmetic throughout (integers, `fractions.Fraction`, exact $\mathbb F_p$).
**134 quantities recomputed independently; one byte-identical reproduction of the
delivery run** (`--falsification-selftest`, exit 0, `diff` against the committed
`lcb_livecell_output.txt` = 0 lines, 34 gates PASS, all 55 mutants exit 1).
No repository mutation; no git; one file written.

**Headline.** I could not break a single computed number. Every quantity in the
paper reproduces exactly, and the delivery run is byte-reproducible. What I did
break is the **interpretation layer**: the named obstruction is not the operative
one, the FOUND-reachability control at the full clause list is obtained by an
undisclosed substitution of the declared base record, disclosure X10 is false
outside the declared two-of-six identification family, and the pre-registered
Open-1 verdict **flips from `LCB-PRIME-DECLARED` to `LCB-PRIME-DERIVED` at
$p = 7$** when one further encoding cell — the chart-involution conjugate of the
unit's own declared `index` cell — is admitted. Details and witnesses below.

---

## 1. K1 — THE SPECTRAL OBSTRUCTION

### 1.1 The squaring-forcing, derived independently

I derived the forcing myself before reading §4.3, and it is **correct**. Set
$\sigma(\cdot) = \Sigma(\cdot)\Sigma$, so that GEN's law is the
$\sigma$-twisted cocycle $\delta(Q) = \sigma(Q)^{-1}Q$.

1. **S1b + Sylow.** $V = (\mathbb Z/p)^3$ is elementary abelian, so
   $\mathrm{im}\,\alpha$ is a $p$-subgroup of $G_C$. I compute the $p$-part of
   $\lvert G_C\rvert = 8!$ by exact division: $p^1$ at $p = 5$ and at $p = 7$,
   $p^0$ at every declared prime above 7. Hence $\mathrm{im}\,\alpha$ is cyclic
   of order 1 or $p$, and $\alpha(r) = g^{\lambda(r)}$ with $\lambda$ additive,
   hence $\mathbb F_p$-linear.
2. **The sign.** For $r$ with $\lambda(r) = t \ne 0$ the square gives
   $\sigma(g)^{-t}g^{t} = g^{\lambda(Er)}$, so $\sigma(g)^{t}\in\langle g\rangle$
   and therefore $\sigma(g) = g^{c}$. Since $\Sigma^2 = 1$, $\sigma^2 = \mathrm{id}$
   and $g^{c^2} = g$, so $c^2 \equiv 1$, i.e. $c \equiv \pm 1$ ($p$ odd).
3. **The $c = +1$ branch is empty by measurement.** $c = +1$ means $g$ commutes
   with $\Sigma$; I count the order-5 elements of $G_C$ commuting with $\Sigma$:
   **0**, against **48** with $\sigma(g) = g^{-1}$. (At $p = 7$: **0** against
   **96**.) So $c = -1$ for every nontrivial candidate.
4. **Squaring.** $c = -1$ gives $\delta(g^{t}) = g^{t}g^{t} = (g^{t})^2$
   identically on $\langle g\rangle$, and the square reads
   $\lambda\circ E = 2\lambda$, i.e. $\lambda \in \ker(E^{\mathsf T} - 2I)$.

That is exactly §4.3 and X01, and it is sound. One clarification the paper
should carry: step 2 is what forces $\sigma(g)\in\langle g\rangle$ in the first
place, and the paper's phrasing ("The square forces $\Sigma g\Sigma = g^{c}$")
states the conclusion without the one-line argument that a nonzero $\lambda$
supplies it. NOTE-level.

### 1.2 $\mathrm{spec}(E)$ and the $p$-sweep — reproduced exactly

Rebuilt from $q_{ij}\ell^i\ell^j = n_\ell$ with rows the links
$(e_1,e_2,e_1{+}e_2)$:

| identification | direction | $\det$ | spectrum over $\mathbb Q$ | $E \bmod 5$ | mine |
|---|---|---|---|---|---|
| natural | counts$\to q$ | $1/2$ | $\{1,1,\tfrac12\}$ | `[[1,0,0],[0,1,0],[2,2,3]]` | identical |
| natural | $q\to$counts | $2$ | $\{1,1,2\}$ | `[[1,0,0],[0,1,0],[1,1,2]]` | identical |
| index | counts$\to q$ | $-1/2$ | $\{1,\tfrac12,-1\}$ | `[[1,0,0],[2,2,3],[0,1,0]]` | identical |
| index | $q\to$counts | $-2$ | $\{1,2,-1\}$ | `[[1,0,0],[0,0,1],[1,2,1]]` | identical |

The $p$-sweep to 60, solving $\dim\ker(E^{\mathsf T}-2I)$ over $\mathbb F_p$ at
every prime below 60 at all four cells: in the **registered** direction
2 enters the spectrum at $p = 3$ **and nowhere else**, at *both* declared
identifications; in the reversed direction at every prime. Reproduced exactly.
The algebra behind it is also right: $2 \in \{1,1,\tfrac12\}$ iff $4\equiv 1$,
and $2\in\{1,\tfrac12,-1\}$ iff $4\equiv 1$ or $3\equiv 0$ — both give $p = 3$.

### 1.3 FINDING F1 (MAJOR) — the four-cell sweep is 4 of 12, and the missing cells kill the spectral obstruction

The paper's family is "2 identifications $\times$ 2 directions". There are
$3! = 6$ slot identifications between the count triple and the metric triple,
not 2, and the paper itself calls one of the two it declares "a naming
artifact" (§2.4). If a naming artifact earns a cell, all of them do.

I swept all $6\times 2 = 12$ cells. **Two of the four undeclared
identifications put 2 in the spectrum at $p = 7$ in the REGISTERED direction**,
and $p = 7$ is admissible on the deformation side ($\rho$ reduces, 96
anti-invariant order-7 elements exist):

| metric slot order | declared? | direction | primes with $2\in\mathrm{spec}$ |
|---|---|---|---|
| $(q_{11},q_{22},q_{12})$ | natural | counts$\to q$ | $\{3\}$ |
| $(q_{11},q_{12},q_{22})$ | index | counts$\to q$ | $\{3\}$ |
| $(q_{22},q_{11},q_{12})$ | — | counts$\to q$ | $\{3\}$ |
| $(q_{22},q_{12},q_{11})$ | — | counts$\to q$ | $\mathbf{\{3,7\}}$ |
| $(q_{12},q_{11},q_{22})$ | — | counts$\to q$ | $\mathbf{\{3,7\}}$ |
| $(q_{12},q_{22},q_{11})$ | — | counts$\to q$ | $\{3\}$ |

The cell $(q_{22},q_{12},q_{11})$ is **not** an exotic choice. It is exactly the
unit's own declared `index` identification with the metric's axes named in the
other order — that is, the `index` cell composed with the chart involution
$\tau$ on the metric side, since $\tau$ acts on `sym_index` order as the
reversal $(q_{11},q_{12},q_{22})\mapsto(q_{22},q_{12},q_{11})$. The unit
*measures* (G09) that the `index` identification does not carry $\tau$; that
measurement is precisely the notice that this cell exists and is distinct.

**An explicit witness at that cell, $p = 7$, REGISTERED direction.** With
$E \bmod 7 = [[0,1,0],[3,3,4],[1,0,0]]$, the 2-eigencovector is
$\lambda = (3,4,1)$; take $g = [0,2,4,5,6,7,3,1,8]$ (order 7,
$\Sigma g\Sigma = g^{-1}$) and $\alpha(r) = g^{\lambda\cdot r}$. Measured by me,
entry by entry as permutations:

- **S1a violations: 0 of 343.**
- **S1b violations: 0 of 117,649.**
- **S1d: passes** — $\lambda(r_0) = 2 \ne 0$, $\delta(\alpha(r_0))$ has order 7
  and $\mathrm{fix}_{81} = 18$, matching an $\mathrm{ord}(D) = 7$ transport base.
- S1c violations: 294 of 343 (the same chart-parity failure as the reversed
  cells).

So at that cell the census in the **data $\to$ geometry** direction is
**non-empty (96 distinct maps)** at an admissible prime, and the clause that
bites is S1c, not the spectrum.

**What this refutes, as stated.** Three statements are true only of the declared
two-of-six family and are written unscoped:

- The boxed §4.2 claim: "S1a+S1b at the REGISTERED direction: **0** candidates,
  at both identifications." (True as written — "at both identifications" — but
  the sentence carries the weight of a direction-level fact.)
- §4.3 / §13: "2 enters it at exactly one prime, $p = 3$."
- **X10**, verbatim: "$p = 3$ is the only prime at which the registered
  intertwining is solvable, swept over every prime below 60, and it is
  inadmissible on the deformation side." This disclosure is **false** outside
  the declared identification family, and it is stated without an
  identification scope tag. That is the §40-F1/F2 failure the RUNBOOK
  catalogues: descent measured at one setting, stated unscoped.
- §5's rhetorical spine — "The two directions fail at **different clauses**, and
  that is the point" — is identification-relative: at $(q_{22},q_{12},q_{11})$
  both directions fail at S1c.

**Repair.** Either (a) declare and sweep all six identifications (the census is
cheap; the bridge verdict does **not** move — see F3 — but the obstruction
narrative and the Open-1 table do), or (b) scope every spectral sentence to the
declared pair. Replacement sentence for X10, verbatim:

> X10 | At the two DECLARED identifications, $p = 3$ is the only prime at which
> the registered intertwining is solvable, swept over every prime below 60, and
> it is inadmissible on the deformation side. The spectral condition is
> identification-relative: at two of the four undeclared slot identifications —
> including the $\tau$-conjugate of the declared `index` cell — 2 enters the
> spectrum at $p = 7$ as well, and the registered-direction census there is
> non-empty at S1a and S1b and is emptied by S1c.

### 1.4 FINDING F2 (MAJOR) — the one-$\alpha$ reading is the load-bearing declaration, and it is not swept

Deviation 1 licenses "the naturality reading of S1 (one morphism, two charts)
rather than two independent vertical arrows" and then sweeps the identification
and the direction. It does **not** sweep the choice it names. I ran the
two-arrow reading $\delta\circ\alpha_1 = \alpha_2\circ E$ with
$\alpha_1,\alpha_2$ both homomorphisms into $G_C$:

| cell | two-arrow S1a+S1b | $+$S1c | $+$S1d |
|---|---|---|---|
| natural, counts$\to q$ (REGISTERED) | **5,952** | 192 | **0** |
| natural, $q\to$counts | 5,952 | 192 | **0** |
| index, counts$\to q$ (REGISTERED) | 5,952 | 0 | 0 |
| index, $q\to$counts | 5,952 | 0 | 0 |

The **spectral obstruction dissolves completely** under the two-arrow reading:
$\lambda_2 := 2\lambda_1E^{-1}$ solves the square for *every* invertible $E$ and
every anti-invariant $g$, at every prime, in every direction. $48\times124 =
5{,}952$ pairs, at the registered cell included.

This is not a fatal objection to the unit's choice — the endomorphism reading is
defensible and declared — but the paper reports a 2$\times$2 sweep as if the
declaration-relativity had been bounded by it, when the unswept declaration is
the one carrying the whole spectral result. Deviation 1 should say so.

**Replacement sentence** for deviation 1, appended verbatim:

> The cost of the naturality reading is measured, not only argued: under the
> alternative two-vertical-arrow reading the commuting square is solvable at
> every encoding cell, at every prime and in both directions (5,952 pairs per
> cell), because $\lambda_2 := 2\lambda_1E^{-1}$ solves it for any invertible
> $E$. The SPECTRAL form of the obstruction is therefore a consequence of the
> one-morphism reading; the CHART-PARITY form and the base-point conflict of
> §5 survive both readings.

---

## 2. K2 — CHART-PARITY, SUB-OBJECT, AND WHETHER THE FORMS ARE INDEPENDENT

### 2.1 The chart-parity computation — reproduced exactly

$\ker(E^{\mathsf T}-2I)$ in the reversed cells is one-dimensional, spanned by
$\lambda = (1,1,1)$; $\tau\lambda = \lambda$, chart-**symmetric**. The required
antisymmetry is not an assumption but a consequence I re-derived: S1c says
$\alpha(\tau r) = \Sigma\alpha(r)\Sigma = g^{c\lambda(r)}$, and $c = -1$ is
already forced by S1a, so S1c $\iff \lambda\circ\tau = -\lambda$. Violations per
candidate: $125 - \lvert\{r : \lambda(r)=0\}\rvert = 125 - 25 = \mathbf{100}$,
exactly as reported, at both reversed cells. All 48 maps (192 pairs) die; S1d
passes at all 48 ($\lambda(r_0) = 4$). Every number identical.

### 2.2 The sub-object form — reproduced exactly

5-part of $8!$ is $5^1$; 5-part of $15!$ is $5^3$; three disjoint 5-cycles on 16
labels generate a subgroup of order exactly $125 = \lvert V\rvert$. All
reproduced. X02 and X07 scope it honestly.

One NOTE: the exhibited 16-label witness is **not** $\Sigma_{16}$-anti-invariant
(I checked all three generators), so it cannot satisfy the square there. X07
already says the square is untested at 16 labels; §6's sentence "the same clause
is satisfiable" should read "the same **injectivity** clause is satisfiable" so
that no reader carries it further.

### 2.3 FINDING F3 (FATAL) — the three forms are not independent, and none of them is what empties the census

**Theorem (mine).** At this pairing, with the declared base record
$r_0 = $ `G-FLAT`$= (1,1,2)$ and any odd prime $p$, **no candidate satisfies
S1a $\wedge$ S1b $\wedge$ S1c $\wedge$ S1d — for any chart map $E$ whatsoever.**

*Proof.* S1b + Sylow give $\alpha(r) = g^{\lambda(r)}$ with $\lambda$ linear.
For nontrivial $\alpha$, S1a forces $\Sigma g\Sigma = g^{c}$, $c^2\equiv 1$, and
$c = +1$ is empty by measurement, so $c = -1$. S1c then forces
$\lambda\circ\tau = -\lambda$. But $\tau r_0 = r_0$ — the declared base record is
$\tau$-**fixed** — so $\lambda(r_0) = -\lambda(r_0)$, hence $2\lambda(r_0) = 0$,
hence $\lambda(r_0) = 0$. Then $\delta(\alpha(r_0)) = e$, of order 1 with
$\mathrm{fix}_{81} = 81$, while S1d demands order 5 and $\mathrm{fix}_{81} = 36$.
The trivial $\alpha$ fails S1d for the same reason. $\square$

**Verified exhaustively, with no $E$ in the computation at all**, over all
$1{,}344 \times 124 = 166{,}656$ pairs $(g,\lambda)$:

- pairs satisfying S1c: **192** (= 48 anti-invariant generators $\times$ the 4
  nonzero antisymmetric covectors $(a,-a,0)$);
- of those, satisfying S1d at $r_0 = $ `G-FLAT`: **0**;
- of those, satisfying S1d at `G-ANISO` $= (1,4,5)$: **192**;
- $\tau(1,1,2) = (1,1,2)$ (fixed); $\tau(1,4,5) = (4,1,5)$ (not fixed).

**Consequences, all three severe.**

1. **`LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD` is analytically forced by the
   clause list, not measured off the encodings.** No property of HA's readout,
   no identification, no direction, no prime and no completion enters. The
   paper's §13 "The obstruction, named" attributes emptiness to two measured
   properties of the two encodings; the operative fact is that two clauses the
   unit added itself (deviation 2: S1c and S1d are **not** in BRG's S1) are
   jointly unsatisfiable at the base record the unit declared. RUNBOOK §14
   addendum (#208) is explicit: *analytically-forced clauses — true by algebra
   for every input — are disclosures, not must-pass gates*. Gate G13's headline
   quantity `S1 survivors across all cells: 0` is such a clause.

2. **The three "forms" collapse.** The spectral form and the sub-object form
   both descend from one measured arithmetic fact, the $p$-part of
   $\lvert G_C\rvert = 8!$ being $p^1$ (it is what makes the image cyclic in
   §4.3 step 1 *and* what forbids injectivity in §6). The spectral form and the
   chart-parity form are one spectral fact read in two directions
   ($\mathrm{spec}(E^{-1}) = \mathrm{spec}(E)^{-1}$). And all three are
   *dominated* by the base-point conflict, which needs none of them. The
   protocol's K2 question — "genuinely independent facts or one fact in three
   costumes" — answers: **one arithmetic fact and one spectral fact, in three
   costumes, worn over an unstated fourth fact that alone decides the verdict.**
   §13's "And, **independently of both**, SUB-OBJECT" is wrong as written.

3. **G31 is coextensive with the wrong thing.** G31 measures the named
   obstruction coextensive with the *S1a/S1c* clause failures, which is true;
   it cannot see that S1c $\wedge$ S1d was empty before either was consulted.

**Repair.** The unit must either (a) re-declare the base record as a
$\tau$-asymmetric one (`G-ANISO` is the obvious candidate; the census machinery
already runs there — see F4) and re-run, at which point the obstruction really
is the encodings'; or (b) keep `G-FLAT`, disclose the conflict as a theorem, and
demote the full-clause-list emptiness from a measurement to a disclosure, with
the *measured* content re-stated as the S1c-alone result. Replacement paragraph
for §13, verbatim:

> **THE BASE-POINT CONFLICT, and it is prior to both forms.** The declared base
> record `G-FLAT` $=(1,1,2)$ is fixed by the chart involution, while S1c forces
> every admissible candidate's exponent covector to be chart-antisymmetric.
> An antisymmetric covector annihilates a $\tau$-fixed record, so
> $\lambda(r_0) = 0$ and $\delta(\alpha(r_0))$ is the identity, of order 1 —
> failing S1d, which demands order 5. S1c and S1d are therefore jointly
> unsatisfiable at this base record **for every chart map whatsoever**:
> measured over all 166,656 $(g,\lambda)$ pairs, 192 satisfy S1c and none of
> those satisfies S1d. The full-clause-list emptiness is in that sense forced by
> the clause list and is disclosed as such; what the encodings themselves
> measure is the SPECTRAL result at the registered direction and the
> CHART-PARITY result at the reversed one, reported separately below.

### 2.4 FINDING F4 (MAJOR) — the FOUND-reachability control evades F3 by silently swapping the declared base record

`lcb_livecell_exact.py`, gate G22:

```
r0s = tuple(x % P for x in RECORDS["G-ANISO"])
synth_d = [(g, lam) for (g, lam) in synth_c
           if pord(defect_cached(alpha_gl(g, lam, r0s))) == P]
```

while the in-arena S1d (gate G13) uses `base_record(RECORDS)` = `G-FLAT` and
checks order **and** fixed-configuration count. So:

- SYNTH-COMPATIBLE's "192 pass S1d" is measured at **`G-ANISO`**, not at the
  declared base record. At `G-FLAT` it would be **0** (F3), and the run's only
  demonstration that a candidate can pass the full S1 clause list would vanish.
- The substitution `G-FLAT` $\to$ `G-ANISO` is *exactly* what the declared
  mutant `s1d-lax` ("the base-point clause reads the wrong base record")
  performs. The positive control's base record is the falsifier's value.
- G22's receipt records `synthetic_chart_map` but **not** the base record, so
  the substitution is invisible in the receipt as well as in the paper.
  §2.7 and §10 both say only "passing S1a–S1d".

The pin requires "both FOUND and EMPTY reachable w/ mutants proving it". At the
**declared** arena, FOUND at the full clause list is **unreachable by
construction**, and the control that claims otherwise is run at a different base
point. This is the §36 failure ("22 circular/vacuous gates carried a table") in
its live form: the gate cannot fail at the declared arena, and the control that
makes it look falsifiable moved the arena.

**Repair.** Either move the declared base record (F3 repair (a)), in which case
the control and the census agree; or keep `G-FLAT`, state in §2.7 and §10 that
SYNTH-COMPATIBLE's base-point clause is evaluated at `G-ANISO` and *why*, record
the base record in G22's detail, and add a gate measuring that S1c $\wedge$ S1d
is empty at `G-FLAT` for every chart map (it is a one-line exhaustive sweep and
it is the unit's most interesting single measurement).

---

## 3. K4 — S1c / S1d LEGITIMACY

### 3.1 Does any verdict depend on the added clauses alone?

Read off §5's table, which is honest and does support the exercise:

| reader rejects | registered direction | reversed direction | bridge verdict |
|---|---|---|---|
| nothing | 0 | 0 | EMPTY |
| S1d only | 0 | 0 | EMPTY (S1c alone) |
| S1c only | 0 | **48** | **not empty** |
| S1c and S1d | 0 | **48** | **not empty** |

So the EMPTY verdict rests on **S1c alone** in the reversed direction — a clause
BRG's S1 does not name and this unit added. Combine with F1 (a cell in the same
natural family where the *registered* direction is also non-empty at S1a+S1b and
dies only at S1c) and the picture is: at every non-empty cell anywhere in the
12-cell family, the clause that empties it is S1c, LCB's own addition.
Deviation 2's promise ("a reader who rejects either can read the alternative
directly from §5's table") is kept for the 4 declared cells; it should be
extended with a sentence naming S1c as the sole load-bearing added clause.

### 3.2 FINDING F5 (MINOR) — S1d forces $\mathrm{ord}(D)\in\{1,p\}$, not $\mathrm{ord}(D)=p$; two printed counts are consequently wrong

§5: *"For a candidate with cyclic image, $\delta(\alpha(r_0))$ has order $p$ or
1, so S1d forces $\mathrm{ord}(D) = p$."* The premise names the order-1 branch
and the conclusion drops it without argument. At $\mathrm{ord}(D) = 1$ the
declared base completion's defect *is* the identity — order 1,
$\mathrm{fix}_{81} = 81$ — which is exactly what $\delta(\alpha(r_0))$ delivers
when $\lambda(r_0) = 0$. S1d as operationalised in §5 (order **and** fixed count
matched) is therefore **satisfied** at $\mathrm{ord}(D) = 1$.

The grid hard-codes the dropped branch: `s1d_live = s1ab_live and (n == p)`.
Recomputed by me over the declared grid (4 cells $\times$ 7 primes $\times$ 8
defect-order classes = 224, reproduced):

| quantity | as printed | under §5's own S1d ($n\in\{1,p\}$) |
|---|---|---|
| live grid cells after the base-point clause | **4** | **8** |
| distinct $(p,\mathrm{ord}D)$ pairs after the clause | **2** | **4** |

The first of these is a **printed verdict qualifier**
(`live_grid_cells_after_the_base_point_clause`), recomputed inside G30 from the
same proxy, so the qualifier-recomputation gate cannot see it. The narrowing
claim that matters — *BRG's* three live cells become two — is **unaffected**
(BRG's live cells all have $p\mid\mathrm{ord}(D)$, so none has
$\mathrm{ord}(D)=1$), which is why this is MINOR and not MAJOR.

**Replacement sentence** for §5, verbatim:

> **S1d's structural consequence, and it narrows BRG's own live cells.** For a
> candidate with cyclic image, $\delta(\alpha(r_0))$ has order $p$ or 1, so S1d
> forces $\mathrm{ord}(D)\in\{1,p\}$ — not $p \mid 2\,\mathrm{ord}(D)$. Since
> every one of BRG's live cells has $p\mid\mathrm{ord}(D)$ with $p$ odd, the
> order-1 branch meets none of them: measured on the grid of §7, BRG's **3**
> live $(p,\mathrm{ord}(D))$ cells become **2** under the base-point clause and
> **0** under the full clause list, while the grid's own live-cell count after
> the clause is **8** of 224.

### 3.3 The added clauses' justifications

S1c's justification (the involution is one and the same across PSI, GEN's
$\Sigma D\Sigma = D^{-1}$ and HA's chart involution) is the strongest structural
argument in the paper and I do not contest it. S1d's justification ("what makes
the *pairing* the object under test") is reasonable but is the clause that
collides with S1c (F3); the collision is a property of the *choice of base
record*, not of the clause, and the paper never says which.

---

## 4. K3 — THE PRIME-DECLARED VERDICT

### 4.1 The P1–P12 table reproduces

I rebuilt the whole table independently: P1 $\{5\}$; P2 all; P3 $\{5\}$;
P4 $\{5,7\}$; P5 $\{5,7\}$; P6 all-but-2; P7 all-but-2,3; P8 $\varnothing$;
P9 $\varnothing$; P10 $\{5,7\}$; P11 $\varnothing$; P12 $\{5,7\}$;
`unique_forced` False; verdict `LCB-PRIME-DECLARED`. Identical.

### 4.2 FINDING F6 (FATAL) — the Open-1 verdict flips under one additional encoding cell from the unit's own family

`spec2` (candidate P8) is computed as a **union over the declared cells** in the
registered direction. Add the $\tau$-conjugate of the unit's own declared
`index` cell (F1) and re-run the *unmodified* Open-1 logic:

| | as delivered | with `index`$\circ\tau$ added |
|---|---|---|
| P8 admissible part | $\varnothing$ (NO-ADMISSIBLE-PRIME) | $\{7\}$ (NARROWING) |
| P9 admissible part | $\varnothing$ | $\{7\}$, unique |
| **P12, the tightest declaration-free narrowing** | $\{5,7\}$ | $\mathbf{\{7\}}$ |
| `unique_forced` | False | **True** |
| `derive_prime_verdict` | `LCB-PRIME-DECLARED` | **`LCB-PRIME-DERIVED`** |
| `prime_recomputed` ($\lvert\mathrm{inter}\rvert = 1$) | `LCB-PRIME-DECLARED` | **`LCB-PRIME-DERIVED`** |

A **pre-registered verdict** — one of the two the pin names — is a function of a
declaration the unit's own arena action generates, and the flip is to the
*stronger* outcome. The bridge verdict does not move (F3 keeps every cell empty
at the full clause list), but `LCB-PRIME-DECLARED` is not established at the
scope it is stated. §12's summary sentence — "the tightest declaration-free
narrowing is $\{5,7\}$ — two primes, so nothing in the committed structure of
this pairing selects 5 over 7" — is refuted by a cell inside the pairing's own
declared family of readings.

This is not repairable by wording. It requires re-running §12 over the full
identification family and re-deriving the verdict, and the outcome may be
`LCB-PRIME-DERIVED-⟨from the intertwining condition at the τ-conjugate index
cell⟩`, which is a materially different scientific claim.

### 4.3 FINDING F7 (MAJOR) — P8 carries a declaration by the paper's own P3 standard

P3 is disqualified because "$\mathrm{ord}(D) = 5$ is THIS unit's own selection
rule; the candidate contains its own conclusion". P8 is "the primes at which
$2\in\mathrm{spec}(E)$" — computed **only over `dr == "counts->q"`**, the
direction the unit itself registered (§2.4: "The **registered** direction is
counts$\to q$"), and X03 records that HA's prose and HA's code put the
determinant-2 matrix on opposite sides of the arrow. Read in the other declared
direction, P8 admits *every* prime and narrows nothing. P8's whole content —
"unique, and the prime is 3" — is therefore a function of a declaration of this
unit, exactly as P3's is. It is classified `declaration_free = True`.

The verdict does not move on this alone (P8's admissible part is empty, so it
never enters `unique_forced`), but §12's most quoted sentence does:

> "the one declaration-free candidate that does determine a unique prime — the
> intertwining condition itself — determines $p = 3$"

is not supported at the paper's own standard. **Replacement**, verbatim:

> The only candidate that determines a unique prime at all is the intertwining
> condition itself, and it determines $p = 3$ — but it does so only in the
> registered direction, which is a declaration of this unit (X03); read in the
> reversed direction the same candidate admits every prime. Like P1 and P3, P8
> is therefore reported as declaration-carrying, and it is excluded from the
> intersection.

### 4.4 FINDING F8 (MINOR) — "declaration-free" is typed, not measured; P11's set is typed and wrong

`declaration_free(pid, computed)` returns a per-candidate boolean that is a
**hard-coded literal** in each `add(...)` call. G29's own text says "Both
properties are computed"; only uniqueness is. The pin requires the Open-1
outcome "measured, not argued", and half the criterion is argued. The `open1-lax`
mutant only flips the classifier wholesale; it does not establish that the
classification is derived from anything.

Relatedly, P11's admitted set is typed `[]` with the note "the $p$-part … is
$p^1$ at every prime, against $\lvert V\rvert = p^3$: no prime admits an
injective candidate here". Computed rather than typed, the set is $\{2\}$: the
2-part of $8!$ is $2^7 \ge 2^3$ and three disjoint transpositions in $S_8$
generate an injective image of $(\mathbb Z/2)^3$. Immaterial (2 is inadmissible),
but it is a typed count that is wrong — the §24 failure pattern.

### 4.5 The standing interpretation

§12's closing paragraph states the declaration-relative reading and does **not**
adjudicate it. That requirement of the pin is met.

---

## 5. K5 — INSTRUMENT

### 5.1 What is genuinely strong

- **Byte-identical reproduction.** `--falsification-selftest` in place: exit 0,
  `diff` against the committed output = **0 lines**, 34 gates PASS, 55 mutants
  all exit 1, `never_falsified` empty, survivors empty. This is the cleanest
  instrument reproduction I have audited in this arc.
- **30 anchors**, every one reproduced against the upstream receipts; I
  independently recomputed A01 (base-G defect $[0,2,1,6,4,5,3,7,8]$, order 2,
  $\mathrm{fix}_{81}=45$), A04 (9), A05–A11 (40,320; both spectra; 96/40,224;
  4,608; fewest-moved 3; $\mathrm{fix}_{81}$ 36), A12 (10), A13–A16 (625;
  $\rho\bmod 5 = (1,1)$; $\lvert\langle R_{HH}\rangle\rvert = 5$; 125 free
  orbits, all of length 5, shift $(1,1)$ at all 625 configurations), A17 (4),
  A18 (2), A22 (3), A23 $[4,4,6]$. All identical. Twelve anchor mutants
  corrupt-and-fire correctly.
- **The 41,665 enumeration.** Reproduced by an independent route: 1,344 order-5
  elements $\Rightarrow$ 336 distinct order-5 subgroups $\Rightarrow$
  $336\times 124 + 1 = 41{,}665$, image-size spectrum $\{1{:}1,\,5{:}41{,}664\}$.
  `enum-drop` dies at G11. My own brute-force census over all
  $1{,}344\times124$ candidate pairs at all 125 record cells reproduces
  $0/48/0/48$ distinct maps exactly.
- **S5's numbers.** 6,336 FIT-admitted, 6,144 out-of-sample deaths, 192
  survivors, H2/H3 at 124/124, teeth at 99/99, `BREAK-HOM` S1a $0/125$ and S1b
  $6{,}000/15{,}625$ — every one reproduced. The held-out split is genuinely
  frozen and the FIT cell genuinely admits far more than survive.
- **No sampling.** Confirmed: no `random`, no seed, no `sample`/`choice` in the
  source; the two sub-total sweeps are named, not drawn.

### 5.2 FINDING F9 (MAJOR) — S5 is discharged entirely against the SYNTHETIC chart map, and neither the paper nor the receipt says so

`Esy = synth_compatible_matrix(P)` — the declared **synthetic** control matrix
$[[4,2,0],[2,4,0],[0,0,1]]$ — is the chart map used at every line of the S5
block: the FIT admission, the HELD verification, H2, H3, X-NOSQUARE and
X-FLATSTRAT. HA's readout appears nowhere in §8.

§8 is headed "S5: the held-out verification", sits in the S2–S6 sequence at the
pairing, and names no chart map; §2.5's S5 row names none; the G18 and G19
receipt details record none (G19's `witness_lambda = [1,4,0]` is the *synthetic*
map's antisymmetric eigencovector, which is the only tell). A reader has no way
to learn from the paper or the receipt that BRG's S5 requirement was exercised
on a synthetic pair.

Mitigation, measured by me: the numbers happen to be identical on the real
reversed cell (FIT-admitted 6,336, survivors 192, deaths 6,144) because both
maps have a one-dimensional 2-eigenspace and 48 anti-invariant generators; on
the **registered** cell they would be 6,336 admitted and **0** survivors. So no
number is wrong — but the labelling is, and S5 is one of the six registered
requirements the unit claims to run "per the registry".

**Replacement sentence** for the head of §8, verbatim:

> **S5: the held-out verification, on the declared compatible pair.** The
> registered direction's census is empty and the reversed direction's candidates
> are all rejected by S1c, so there is no FOUND at this pairing to hold out on.
> The protocol is therefore exercised on the declared SYNTHETIC compatible pair
> of §2.7 — the same transport side against the synthetic chart map
> $[[4,2,0],[2,4,0],[0,0,1]]$ — and is reported as a demonstration that the
> machinery predicts out of sample, not as a discharge of S5 at the pairing. The
> same protocol run against HA's own reversed-direction readout gives the same
> three counts (6,336 / 6,144 / 192) and against the registered direction gives
> 6,336 / 6,336 / 0.

### 5.3 FINDING F10 (MINOR) — the two symmetry self-tests are analytically forced and their mutants die only on the non-triviality clause

G25: with $\Sigma' = \pi\Sigma\pi^{-1}$,
$\delta_{\Sigma'}(\pi Q\pi^{-1}) = \pi\,\delta_\Sigma(Q)\,\pi^{-1}$ **identically**
for every $\pi$ and every $Q$ — it is conjugation-covariance of a word in
$\Sigma$ and $Q$. Likewise the recount `anti_r == 48`: conjugation is a bijection
preserving $\Sigma'$-anti-invariance. G26: $\ker((BEB^{-1})^{\mathsf T}-2I)$ has
the same dimension as $\ker(E^{\mathsf T}-2I)$ because
$(BEB^{-1})^{\mathsf T}-2I = B^{-\mathsf T}(E^{\mathsf T}-2I)B^{\mathsf T}$.
Neither invariance clause can fail on any input.

Confirmed by reading the gate predicates: `relabel-lax` sets $\pi = \mathrm{id}$,
which leaves `reb_ok == reb_cells` and `anti_r == len(ANTI)` **true** and dies
only on `pi != pident(NLAB)` / `pmoved(pi) > 0`; `basis-lax` likewise dies only
on `B != I`. So the declared falsifiers falsify "did you act at all", never "is
the right invariant computed" — the §14 lesson (branch A's gauge-variant
holonomy) in a milder key. RUNBOOK §14 addendum #208 says such clauses are
disclosures. §11's "A basis change that changed nothing could not test this" is
the only thing these gates measure.

Note the contrast with F1: the arena action that is **not** forced — the chart
involution acting on the *identification* — is the one the self-tests do not
cover, and it is the one under which the decision quantity is **not** invariant.

### 5.4 FINDING F11 (MINOR) — the "third" verdict derivation and several qualifier recomputations read the same object

`empty_from_tables` reads `tables["s1_clause_census"]`, which *is* the same list
`s1_rows` that `found_at_standard` was summed from — a different aggregation of
one object, not a third source. Similarly `candidates_passing_S1a_S1b`,
`candidates_passing_all_of_S1`, `cells_passing_S2/S3` and
`live_grid_cells_after_the_base_point_clause` are "recomputed" from the same
in-memory rows. Genuinely double-sourced: `completion_family_members`,
`ord5_class_size`, `homomorphisms_enumerated`, `encoding_cells`, `primes`.
`qualifier-typo` perturbs exactly one qualifier (`encoding_cells`), one of the
genuinely double-sourced five, so the flip probe exercises 1 of 15. The second
source (`empty_recount` from the S4 grid's Gaussian elimination) *is* genuinely
independent, and it is the one deviation 6 leans on — but it is a
necessary-condition proxy that can only corroborate EMPTY, never FOUND, and it
uses the grid's own S1 predicate, which omits S1d's non-vanishing condition.
§13's "derived a **third** time" should read "aggregated a second way from the
same clause table".

### 5.5 FINDING F12 (NOTE) — two smaller instrument overstatements

- G11 asserts "every candidate is tested at every one of the $p^3$ record
  cells" but measures `len(square_cells(V)) == P**3` — the size of the cell
  list. Route B breaks at the first violating cell. The decision is unaffected;
  the gate text is not what the gate measures.
- G10 calls route A and route B "two genuinely independent computations". Route
  A *is* the closed form of the structure theorem route B tests
  ($\lvert\mathrm{ANTI}\rvert\cdot(p^{\dim\ker}-1)/(p-1)$). X09 half-concedes it.
  It is a worthwhile cross-check — it would catch an error in either — but under
  the §13 addendum ("a pair related by an algebraic identity is one route") it
  should be described as *theorem-versus-enumeration*, not as two independent
  routes. The unconditional route is route B alone, and that is enough.

---

## 6. INDEPENDENT NUMBERS TABLE (claimed vs. mine)

Every load-bearing quantity, recomputed from the published laws:

| quantity | paper | mine |
|---|---|---|
| completion family | 40,320 | 40,320 |
| defect-order spectrum | $\{1{:}96,2{:}1440,3{:}4224,4{:}4608,5{:}4608,6{:}6912,7{:}9216,15{:}9216\}$ | identical |
| $\mathrm{fix}_{81}$ spectrum | $\{9{:}16704,18{:}11520,27{:}5376,36{:}4608,45{:}864,54{:}1152,81{:}96\}$ | identical |
| $\mathrm{ord}(D)=5$ class | 4,608 | 4,608 |
| $Q_0$ / labels moved | $[0,1,2,3,4,5,7,8,6]$ / 3 | identical |
| $D=\delta(Q_0)$ / ord / $\mathrm{fix}_{81}$ | $[0,1,8,3,4,2,7,5,6]$ / 5 / 36 | identical |
| $\lvert\langle W,D\rangle\rvert$ / element orders | 10 / $[1,2,2,2,2,2,5,5,5,5]$ | identical |
| $\lvert\mathrm{hom}(\mathbb Z/5,\langle W,D\rangle)\rvert$ | 5 (4 non-trivial) | identical |
| $C_{HA}(5)$: carrier / $\rho\bmod 5$ / orbits | 625 / $(1,1)$ / 125 free | identical |
| order-$p$ elements: total / anti / $\Sigma$-commuting, $p{=}5$ | 1,344 / 48 / 0 | identical |
| same, $p = 7$ | — / 96 / 0 | 5,760 / 96 / 0 |
| $p$-part of $8!$ at 5, 7, $\ge 11$ | $p^1,p^1,p^0$ | identical |
| $p$-part of $15!$ at 5 | $p^3$ | identical |
| homomorphisms enumerated | 41,665 | 41,665 (336$\times$124+1) |
| census, four cells (distinct maps) | 0 / 48 / 0 / 48 | identical |
| 2-eigencovector, reversed cells | $(1,1,1)$, chart-symmetric | identical |
| S1c violations per candidate | 100 of 125 | 100 ($=125-25$) |
| S1d passes, reversed cells | 48 | 48 |
| grid cells / live at S1a+b / after S1d | 224 / 32 / 4 | 224 / 32 / 4 (8 under §5's S1d — F5) |
| BRG live cells reproduced | $(5,5),(5,15),(7,7)$ | identical |
| anti-invariant by prime | $\{5{:}48,7{:}96\}$, 0 above | identical |
| S5: FIT-admitted / died / survived | 6,336 / 6,144 / 192 | identical (on `Esy`; see F9) |
| BREAK-HOM S1a / S1b | 0/125, 6,000/15,625 | identical |
| 16-label $p$-part / witness subgroup | $p^3$ / 125 | identical |
| Open-1 P1–P12 | as tabled | identical |
| $2\in\mathrm{spec}$, registered direction, declared cells | $\{3\}$ | $\{3\}$ |
| $2\in\mathrm{spec}$, registered direction, **all 6 identifications** | not swept | $\{3\}$ or $\mathbf{\{3,7\}}$ — **F1** |
| S1c $\wedge$ S1d satisfiable at `G-FLAT`, any $E$ | not measured | **0 of 166,656** — **F3** |

**No computed number in the delivery is wrong.** Two printed counts are wrong
relative to the paper's own definitions (F5), and one disclosure is false
outside its unstated scope (F1/X10).

---

## 7. FINDINGS, RANKED

| # | severity | finding | moves a number or verdict? |
|---|---|---|---|
| F3 | **FATAL** | S1c $\wedge$ S1d is unsatisfiable at the declared base record for **every** chart map (`G-FLAT` is $\tau$-fixed; S1c forces antisymmetry). The full-clause-list emptiness is analytically forced, not measured off the encodings; the three "obstruction forms" are two facts in three costumes over an unstated fourth that alone decides it. | verdict stands, its **grounds** change |
| F6 | **FATAL** | The Open-1 verdict flips `LCB-PRIME-DECLARED` $\to$ `LCB-PRIME-DERIVED` ($p{=}7$) when the $\tau$-conjugate of the unit's own declared `index` cell is admitted. A pre-registered verdict is a function of an unswept declaration. | **verdict** |
| F1 | MAJOR | The identification family is 2 of 6; two undeclared cells put $2\in\mathrm{spec}$ at the admissible prime 7 in the REGISTERED direction, with an explicit witness passing S1a (0/343), S1b (0/117,649) and S1d. X10 is false as scoped. | **disclosure X10** |
| F4 | MAJOR | SYNTHETIC-COMPATIBLE's S1d is evaluated at `G-ANISO`, not the declared `G-FLAT` — the same substitution the `s1d-lax` falsifier performs — undisclosed in paper and receipt. FOUND at the full clause list is unreachable at the declared arena. | control validity |
| F9 | MAJOR | All of §8 (S5) runs against the synthetic chart map; neither paper nor receipt records it. | labelling |
| F7 | MAJOR | P8 embeds the registered-direction declaration and is classified declaration-free, contrary to the standard applied to P3. §12's "the one declaration-free candidate that does determine a unique prime" is unsupported. | claim |
| F2 | MAJOR | The one-$\alpha$ reading — the declaration the spectral obstruction actually rests on — is not swept; under two vertical arrows the square is solvable at every cell, prime and direction (5,952 pairs/cell). | scope |
| F5 | MINOR | S1d forces $\mathrm{ord}(D)\in\{1,p\}$; the grid's `n == p` proxy makes the printed qualifier 4 instead of 8 and "2 distinct pairs" instead of 4. | **two printed counts** |
| F8 | MINOR | `declaration_free` is a typed literal, contrary to G29's text and the pin's "measured, not argued"; P11's set is typed `[]` and is $\{2\}$ when computed. | claim |
| F10 | MINOR | G25/G26 invariances are analytically forced; their mutants die only on the non-triviality clause. | gate teeth |
| F11 | MINOR | The "third" verdict derivation and 10 of 15 qualifier recomputations read the same in-memory object; the typo probe exercises 1 of 15. | claim |
| F12 | NOTE | G11's "every cell" is a size check (route B breaks early); G10's "two genuinely independent computations" is theorem-versus-enumeration. | wording |
| F13 | NOTE | The 16-label injectivity witness is not $\Sigma_{16}$-anti-invariant; §6's "the same clause is satisfiable" should say "the same injectivity clause". | wording |

---

## 8. WHAT SURVIVES EVERY ATTACK

For the adjudicator's benefit, stated as plainly as the findings:

- **`LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD` is correct and, if anything,
  under-stated.** It survives the identification sweep to all 12 cells, the
  two-arrow reading, the prime sweep to 60, and the base-change sweep. I found
  no candidate anywhere satisfying the full declared clause list. The verdict is
  overdetermined, which is the opposite of the usual failure mode.
- The squaring-forcing derivation is sound and I reproduced every step of it
  from the published laws.
- The census is genuinely exhaustive at $p = 5$; the enumeration count is
  independently confirmed by two routes I built myself.
- The delivery is byte-reproducible and the mutant harness is real: 55 mutants,
  all exit 1, `never_falsified` empty.
- The unit's honesty about its own weak points (X01–X10, deviations 1–8) is
  above the arc's average. X03 in particular anticipates part of F1's terrain
  without following it to the identification family.

## 9. REPAIR ORDER (minimum to reach a defensible terminal)

1. **Re-declare the base record** to a $\tau$-asymmetric admissible record
   (`G-ANISO`), or keep `G-FLAT` and demote the full-clause emptiness to a
   disclosure with F3's theorem stated and gated. Either way, add the
   166,656-pair sweep as a gate — it is the unit's sharpest measurement.
2. **Widen the encoding-cell family to all six identifications** ($\times$ 2
   directions = 12 cells), re-run, and re-derive §4.2, §4.3, §5, §7, §9, §12,
   §13 and X10 from it. Expect the bridge verdict to stand and the Open-1 verdict
   to move.
3. **Re-derive the Open-1 table** at the widened family, reclassify P8 as
   declaration-carrying (F7), compute P11 rather than type it, and derive
   `declaration_free` from a stated predicate or rename the gate's claim.
4. **Disclose S5's chart map** in §8, in §2.5's S5 row and in G18/G19's receipt
   detail; record SYNTH-COMPATIBLE's base record in G22's detail.
5. **Fix the grid's S1d** to $n\in\{1,p\}$ and re-print the two counts.
6. Demote G25/G26's invariance clauses to disclosures or give them a mutant that
   can make the invariant itself fail; correct §13's "third derivation" and
   G10/G11's gate texts.

---

## GRADE

**REJECT.**

Not for a wrong number — I found none, and the delivery reproduces
byte-identically. For two verdict-level defects that cannot be repaired by
wording:

1. **F6.** A pre-registered outcome, `LCB-PRIME-DECLARED`, flips to
   `LCB-PRIME-DERIVED` at $p = 7$ under one further encoding cell that the
   unit's own measured chart involution generates from a cell it declared. The
   §12 table must be re-run before either outcome can be entered.
2. **F3 with F4.** The full-clause-list emptiness is forced by a clause conflict
   at the declared base record, independent of both encodings — so the named
   obstruction is not the operative one — and the sole demonstration that the
   full clause list is satisfiable at all is obtained by silently substituting
   the base record that the unit's own `s1d-lax` falsifier substitutes. Both the
   obstruction naming (G31) and the FOUND-reachability control (G22) must be
   rebuilt, and the paper's §13 must be rewritten around a different fact.

Supporting these, F1 falsifies disclosure X10 as scoped and F9 mislabels one of
BRG's six registered requirements.

The bridge verdict itself is safe and the repair path is concrete and cheap —
this is a REJECT-and-re-run, not a REJECT-and-abandon. Re-submitted at the
widened cell family with F3's theorem stated and gated, I expect this unit to
be stronger than it is now, because its most interesting single measurement is
currently the one it does not report.

**Recomputation count: 134 independent recomputations, plus one byte-identical
reproduction of the delivery run (exit 0, diff 0 lines, 34/34 gates, 55/55
mutants killed).**
