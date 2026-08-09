# RSQ — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens.  **Protocol:**
`v13/note-rsq-hostile-protocol.md` (FROZEN, K1–K5 binding).
**Object reviewed, SHA-256 verified before reading:**

| artifact | sha256-12 | verified |
|---|---|---|
| `v13/paper-rsq-reposed-square.md` | `f208ff12974b` | ✅ |
| `v13/code/rsq_reposed_square_exact.py` | `18eb651d1ab1` | ✅ |
| `v13/code/rsq_reposed_square_output.txt` | `810f923392d8` | ✅ |
| `v13/code/rsq_reposed_square_receipt.json` | `4db809f7b618` | ✅ |

**Method.** Independent recomputation from the paper's stated definitions,
in three scripts of my own (`r2_A.py`, `r2_B.py`, `r2_C2.py`) that import
none of the unit's code. **199 distinct quantities recomputed; 0
discrepancies with the paper.** In addition the unit was re-run in
`--falsification-selftest` mode (writes no artifacts) and its stdout is
**byte-identical** to the frozen `_output.txt`, with 57/57 mutants dead and
0 survivors reproduced independently. Two sweeps were run **beyond** the
unit's declared scope as refutation attempts (§1, P-2); both failed to
refute, and both strengthen the paper.

Findings are ranked by severity. Every one carries evidence and a repair.
The grade is last.

---

## 0. What I tried to break, and could not

I attacked five things and all five held:

1. **The order-obstruction derivation.** Re-derived independently, step by
   step. S1a forces $\Sigma_\pi A\Sigma_\pi^{-1}=A$ (because
   $\Sigma_\pi\alpha(r)^{-1}\Sigma_\pi^{-1}=\alpha(Er)\alpha(r)^{-1}\in A$
   and $A=A^{-1}$); S1b makes $A$ an abelian subgroup, on which
   $\delta_\pi(a)=\rho(a)^{-1}a=(I-\rho)(a)$ additively; S3 makes $\alpha$
   an isomorphism onto $A$, giving $\rho=I-\alpha E\alpha^{-1}$; and
   $\rho^{\mathrm{ord}(\Sigma_\pi)}=I$ because conjugation by
   $\Sigma_\pi^{\mathrm{ord}}$ is the identity. Hence
   $\alpha(I-E)^{\mathrm{ord}}\alpha^{-1}=I$, so
   $(I-E)^{\mathrm{ord}}=I$. **Sound.** The involution and order-3 reductions
   ($E=2I$; $E^2-3E+3I=0$) follow correctly from invertibility of $E$.
2. **Route A's structural premise.** I verified by exhaustive
   commuting-pair enumeration that **every elementary abelian
   $p$-subgroup of $G_C$ is cyclic** (0 commuting pairs of order-$p$
   elements generating rank $>1$, at $p=5$ over 504 elements and at $p=7$
   over 720). So $\alpha$ additive forces $\alpha(r)=g^{\lambda(r)}$ with
   $\lambda$ linear, and normalisation of $\langle g\rangle$ by
   $\Sigma_\pi$ is forced for $\lambda\ne0$. Route A's form is correct, not
   assumed.
3. **The permutation-module obstruction.** Reproduced exactly: 210 rows,
   $E=I-\rho_V(\pi)$ at 0, $(I-\rho_V)\mathbf1=0$ at 210, $E\mathbf1=0$ at
   0; $\rho_V$ by permutation matrices at 6 of 6 with 6 distinct images.
   The synthetic non-permutation control is a real two-way calibration.
4. **The transport side.** $|G_C|=5040$; wing group order 6, non-abelian,
   orders $\{1,2,2,2,3,3\}$, closed over all 36 compositions, labels fixed
   by every wing $=\{0,7\}$, 4 involutions; $|\mathrm{fix}\,\delta_\pi|=1$
   at all six wings over all 5 040 completions **and** 1 at a 40 320-member
   9-label arena; ladder $|K|=1,12,168,360,2520$ five for five;
   $F_1=F_3$ at 20 of 30 and at 20 of 20 involution cells; twisted cocycle
   0 deviations of 150. All reproduced.
5. **Every headline count.** 1 440 cells (4/2/1434); survivors
   580/580/652/652/652/652/652 and stillborn 860/860/788×5; the nine
   census cells' fixed dimensions 3,3,1,1,2,2,0,0,0; 20 160 criterion rows
   with 0 hits and 0 route disagreements; 4 420 precheck-surviving
   (cell, prime) pairs; 315 census rows with 25 live at S1a+S1b and 0 at
   S1a+S1b+S3; the thresholds 26/31, 43/43, 67, 79, 103, 115, 139 and the
   $d=2$ anchors 16 and 22; the $p=7$ meeting arithmetic; the grown-arena
   control's 117 649/117 649, 117 648/117 648, $\{1,8,15,22,29,36,43\}$,
   exempt $=1$; BREAK-HOM 0 square violations and 1 536 homomorphism
   violations. **Zero numerical errors found anywhere in the paper.**

**P-2 — the negative result is far more robust than the paper claims, and
I can prove it.** Two refutation sweeps of my own:

| my sweep | rows | criterion satisfied |
|---|---|---|
| $d=3$, **all 1 440 cells** × **all 60 primes from 5 to 293** × ord $\in\{2,3\}$ | **172 800** | **0** |
| $d=2$, all 6 identifications × 2 directions × 7 primes × 2 orders (exhaustive) | 168 | **0** |
| $d=4$, 3 000 sampled identifications × 2 directions × 7 primes × 2 orders | 84 000 | **0** |

So `UNIVERSAL-FOR-THIS-FAMILY` **understates** the measurement: the
emptiness is not an artefact of the seven declared primes, and it is not
special to $d=3$. I also verified analytically that the ord-2 half of the
sweep (10 080 of the 20 160 rows) collapses to a single question —
"is $2M^{-1}$ (resp. $(2M)^{-1}$) a permutation matrix mod $p$?" — whose
answer is No at every prime because the block $2I$ has diagonal entries 2
and $2\not\equiv0,1$. The ord-3 half is genuinely substantive.

**P-4 — a one-line strengthening the paper leaves on the table.** At the
NATURAL identification, $\dim\ker(E-I)=d$ at **every** dimension
(verified $d=2,3,4,5$ at $p=5,7$), because $E=\begin{psmallmatrix}I&0\\
J-I&2I\end{psmallmatrix}$ is block-triangular with spectrum
$\{1^d,2^{d(d-1)/2}\}$. So HA's readout **in its own motivated
coordinates is stillborn at every dimension and every prime**, by
inspection of the spectrum, with no census and no sweep. That is a
stronger and cheaper statement than §7.2's 20 160 rows, and it belongs in
§6.

---

## 1. Findings

### F-1 (HIGH, K5/verdict) — the verdict's "three sources that share no deciding variable" are two. Source 1 **is** source 2.

**Evidence.** `rsq_reposed_square_exact.py:2731`:

```python
"injective_possible": order_criterion(E, p, pord(SIGMA[pi]))
```

and `:2735` `live_full = sum(1 for r in census_rows if r["injective_possible"])`,
and `:3418` `src1 = live_full`. The census table's injective column is
**not** produced by routes A, B or C; it is `order_criterion` evaluated at
the 9 declared cells. Source 2 is `order_criterion` evaluated at all
1 440. I measured the containment directly: the 315 census rows reduce to
**126 distinct (cell, prime, ord) rows, every one of them inside the
20 160-row sweep**. Sources 1 and 2 are the same function on nested
inputs. The tell is in the unit's own mutant table: `criterion-lax` kills
G18, G19, G31, G35 **and** G36 in one shot, and **no** mutant separates
src1 from src2, because there is nothing to separate.

The paper states the opposite twice — §12 ("derived inside gate G35 from
three sources that share no deciding variable"; "**2** the order-criterion
sweep over the WHOLE covariant family, **which runs no census at all**")
and G35's own claim string. This is the RUNBOOK §13 addendum (v13 #234)
verbatim: *"'two independent routes' for a census must be genuinely
independent computations; a pair related by an algebraic identity is one
route."* Here they are not even related by an identity — they are the same
call.

**Not fatal:** src2 and src3 **are** genuinely independent
(`module_obstruction_measured` compares $E_p$ against $I-\rho_V$ and
touches neither the criterion nor the census), and G35 has five further
independent conjuncts. So the verdict does not flip on one variable — this
is not LCB's #293 failure. But the paper claims three and has two.

**Repair.** (a) Relabel the census table's injective column *"the order
criterion, restricted to the declared cells"* and mark it a **restriction
of source 2**, not a source. (b) State that the verdict rests on two
independent sources (the criterion sweep and the module-equality count)
plus the reachability conjuncts. (c) If a third is wanted, route C is
available: rebuild an *admitted* candidate at a criterion-satisfying
synthetic cell and at an HA cell and compare literally — that is a
permutation computation with no linear algebra in it.

---

### F-2 (HIGH, K5/§14-#208) — "0 of 315 rows admit an injective candidate" could not have come out otherwise. It is forced twice, independently.

**Evidence.** (i) It is the order criterion (F-1). (ii) **Independently of
the criterion**, injectivity is impossible at the native arena on
cardinality: $|V|=p^6\ge5^6=15\,625>5\,040=|G_C|$. I measured this at every
census row: **0 of 315 rows have $p^6\le|G_C|$.** And my exhaustive check
that every elementary abelian $p$-subgroup of $G_C$ is cyclic makes it
sharper still — the image of *any* additive $\alpha$ has order $\le p$, so
$\alpha$ can be injective only if $p^6\le p$.

The paper knows the cardinality fact — §10.1 states it — but never
connects it to §7.4's table or to §12's source 1. As presented, §7.4's
"rows admitting an INJECTIVE candidate (S1a+S1b+S3): **0** of 315" reads as
a census outcome that could have been positive. It could not. RUNBOOK §14
addendum (v13 #208): *"Analytically-forced clauses (true by algebra for
every input) are disclosures, not must-pass gates."* G35 carries
`src1 == 0` as a must-pass conjunct.

**A consequence worth stating plainly:** the entire three-route census
machinery (routes A/B/C, the projective calibration, the taint counter,
G20–G22) computes exactly one number that is *not* forced — `live_s1ab`
$=25$ — and that number plays no part in any verdict source. That is not
waste (the 25-vs-0 contrast is the paper's clearest sentence), but the
paper should say which half of the contrast is measured and which is
algebra.

**Repair.** Mark the row `FORCED (cardinality: p^6 > |G_C|; and the order
criterion)`, add the rank-1 measurement (every elementary abelian
$p$-subgroup of $G_C$ is cyclic) as the sharp form, and remove `src1` from
G35's conjunction.

---

### F-3 (HIGH, K2/K3/naming) — the verdict's FOUND half is carried entirely by identifications that have **no** motivation, and every motivated identification is stillborn. The paper never says so.

This is the finding I weight highest, and it goes to the boxed verdict.

**Measured (my recomputation, independent).** The identifications with a
stated motivation are exactly three — the two $S_3$-equivariant ones
(NATURAL, SWAP; the pin's minimum candidate) and HA's own `sym_index`
(LEX) ordering — each in two directions, six cells in all:

| motivated cell | $\dim\ker(E-I)$, every declared prime | precheck |
|---|---|---|
| NATURAL, $q\to$counts / counts$\to q$ | 3 / 3 | STILLBORN |
| SWAP, $q\to$counts / counts$\to q$ | 2 / 2 | STILLBORN |
| LEX (HA's own), $q\to$counts / counts$\to q$ | 1 / 1 | STILLBORN |

**Motivated cells: 6 of 6 stillborn, 0 survivors, at all 7 primes.** Every
one of the 580 (resp. 652) precheck survivors is one of the 1 434
identifications that are nothing but an arbitrary relabelling of the six
metric slots, selected — in the declared census rule's own words — as
*"the lexicographically first slot order whose fixed space is trivial"*,
i.e. selected **by the property under test**.

**Why this decides the verdict's name.** `any_survivor`
(`:2553`) is taken over the whole 1 440-cell family, and
`derive_verdict` branches on it: `if not any_precheck_survivor: return
"RSQ-NO-COMPATIBLE-SQUARE"`. The unit's own instrument probe G37 exercises
exactly that branch. So **restricted to the pin's motivated family, this
unit's pre-registered outcome is `RSQ-NO-COMPATIBLE-SQUARE`.** The first
word of the boxed verdict is a function of whether arbitrary relabellings
are admitted as candidates.

**The pin's text decides against the paper's silence.** The pin's question
is: *"is there a **DIFFERENT, honestly-motivated** encoding pairing at
three wings whose square is not stillborn"*. As measured, the answer to
that question is **no** — every honestly-motivated pairing in the declared
family is stillborn. The pin's *outcome list* is looser ("a candidate
passes the precheck"), and the widened family was declared before fixture
truth (G01: 0 candidate evaluations at the freeze point), so the name is
**pin-legal**. But the paper's §12 gloss —

> "**The premise is not empty:** a re-posed square at three wings *does*
> pass the structural precheck"

— is the sentence a reader will carry away, and it is true only of
identifications nobody has argued for. §6.2 says the module cells are
stillborn; it does not say that LEX is too, and it does not say that the
survivors are exactly the unmotivated ones. It calls them "the set-level
covariant family", which reads as a *class of candidate*, not as *the
complement of the motivated ones*.

**Repair (mandatory, in my view).** (a) Add the computed line: *"the
motivated identifications — both $S_3$-equivariant ones and HA's own
`sym_index` — are 6 of 6 stillborn in both directions at every declared
prime; every precheck survivor is an identification with no stated
motivation."* (b) Add a computed sub-qualifier to the verdict, e.g.
`FOUND-ONLY-AT-UNMOTIVATED-IDENTIFICATIONS`, derived in G35 from the
motivated-cell survivor count (which must be gated to be 0, with a mutant
that can flip it). (c) State in §12 that under the pin's motivated
sub-family the pre-registered outcome is `RSQ-NO-COMPATIBLE-SQUARE`, and
report both. The unit loses nothing by this: reporting both is *stronger*
than reporting one, and it is the honest answer to the flesh-question the
pin actually asked.

---

### F-4 (MEDIUM-HIGH, K5) — S4 (functoriality) is **typed, not measured**, and the paper says "measured".

**Evidence.** `:3127`:

```python
s4_rows.append({"base": nm, "K_order": len(K), "live_primes": live,
                "census_empty_at_this_base": True})
...
scale_rows = [{"scale": "native", "labels": NLAB, "census_empty": True}, ...]
```

Both `True`s are literals. G28's predicate reads only
`len(s4_rows) == len(DECL["ladder_completions"])` — it never inspects
`census_empty_at_this_base` at all. §9.5 states:

> "S4 (functoriality): the emptiness **is measured** at each of TB3's five
> declared ladder bases … and at **both** declared arena scales, and it does
> not move (G28)"

Nothing was measured at the five bases, and the native scale's entry is a
typed constant. This is failure-catalogue #24 (*hard-coded 6561, true 729
— counts computed, never typed*) and #38→#40 (*describe mechanisms as
measured, not as intended*).

**And the true statement is better than the claimed one.** The census
**cannot** depend on the ladder base: the loop at `:2708–2733` ranges over
`subs_by_pi[(p, pi)]`, built from *all* cyclic subgroups of order $p$ in
$G_C$ and *all* wing symmetries; the completion $Q$ never enters. So S4
holds **by construction, structurally** — a fact worth one sentence and a
gate that measures the independence (e.g. assert the census inputs contain
no reference to any ladder base), rather than five typed `True`s dressed
as a robustness sweep over defect subgroups "differing by more than two
orders of magnitude".

**Repair.** Replace the five typed rows with the structural statement plus
an independence gate; delete "is measured" from §9.5 for the native scale.

---

### F-5 (MEDIUM-HIGH, K2) — the grown-arena FOUND control is an algebraic identity, and its "held-out verification" holds out nothing.

**Evidence.** Rebuilt from scratch. With $g_k$ the block translations and
$\Sigma g_k\Sigma^{-1}=g_k^{c_k}$ (verified 6 of 6), for **every** $r$:

$$\delta_\Sigma(\alpha(r))=\Sigma\alpha(r)^{-1}\Sigma^{-1}\alpha(r)
=\textstyle\prod_k g_k^{-c_kr_k}\prod_k g_k^{r_k}
=\alpha\bigl((I-\rho)r\bigr)=\alpha(\tilde Er),$$

because $\tilde E$ is **defined** as $I-\rho$. So 117 649/117 649 is an
identity in $r$, not a measurement. Three consequences the paper does not
disclose:

1. **There is no fit.** `control_alpha` is built from `gens`/`powers`,
   which are constructed globally from the arena. The declared FIT cell
   $e_1$ is never consulted to determine anything; the loop simply skips
   $r=\text{fit}$ when tallying. G25's claim string —
   *"THE HELD-OUT VERIFICATION IS PREDICTIVE … the candidate is admitted on
   the single FIT cell alone and is then verified on every HELD cell"* — is
   not what the code does. The split is decorative.
2. **H1 and H2 are one boolean.** `:2951–2953`:
   `if lhs == rhs: h1 += 1; h2 += 1`. §9.2's table lists them as two
   verifications with the same denominator; they are one comparison of two
   permutation tuples, reported twice.
3. **The teeth are forced.** X-NOSQUARE tests $\alpha(\tilde Er)=\alpha(r)$,
   i.e. $(\tilde E-I)r=0$ with $\tilde E-I=\mathrm{diag}(5,5,5,3,3,3)$
   invertible mod 7 — impossible for $r\ne0$. X-FLATFIX tests
   $\mathrm{fix}=43$, and I verified the fixed-label count is exactly
   $1+7\cdot\#\{k:r_k=0\}$, so $=43$ only at $r=0$. Both "declared in
   advance to fail" controls **cannot pass** for any $r\ne0$; likewise S2's
   "stratification is carried" is the same forced arithmetic. §14-#208
   again: forced clauses are disclosures, not must-pass gates. (They do
   retain value as *instrument* probes — `teeth-off` kills G25 — and that is
   the honest description.)

**Repair.** State the identity in §9.1; collapse H1/H2 to one row; relabel
the teeth and S2 as instrument probes with their forcing stated; and
replace the "predictive" language in G25.

---

### F-6 (MEDIUM, K2) — the honest ladder for the FOUND control, and the theorem the paper is one step from and does not state

**The ladder, as I would write it:**

| rung | claim | status |
|---|---|---|
| 1 | the instrument is not a constant-EMPTY function — it returns FOUND on *some* input | **earned** (but trivially: any $E=I-\rho$ does it) |
| 2 | EMPTY is not caused by the arena, the prime, or the instrument — the same arena and prime return FOUND for a different encoding | **earned**; this is the strongest rung the control reaches, and it is genuinely worth having |
| 3 | bridges exist **in-family** at scale | **NOT earned.** The encoding is $\tilde E=\mathrm{diag}(6,6,6,4,4,4)$, which is neither HA's readout nor any of its 1 439 relabellings; it is not a member of the pin's candidate family (X05 says so) |
| 4 | the grown arena is a legitimate member of the pin's construction family | **partly.** The arena *scale* is declared in DECL family (vi) and enters the pin through item (6)'s threshold table, so it is in-family as a *parameter*. But $L_m$ for $m>1$ has **no declared reading in the transport side's own vocabulary** — TB3's 8 labels are system triples $\mathbb F_2^3$; "$m$ copies of the seven moved labels" indexes nothing. Deviation 5 owns the non-uniqueness of the growth rule but not its uninterpretedness |

**What the control could prove, and does not claim.** The order criterion
says exactly $E=I-\rho$ with $\rho^{\mathrm{ord}}=I$. I checked the
converse computationally: at $p=7$, $x^3-1$ has three distinct roots
$\{1,2,4\}$ mod 7, so every $\rho$ with $\rho^3=I$ is diagonalisable, and
invertibility of $E=I-\rho$ excludes eigenvalue 1 — hence **every** $E$
satisfying the criterion at $p=7$, ord 3 is conjugate to a diagonal matrix
over $\{6,4\}$. I then re-ran the control's own construction for four
different exponent patterns:

| $c$ | $\tilde E=I-\rho$ | normalisation | square violations | injective |
|---|---|---|---|---|
| $(2,2,2,4,4,4)$ | $(6,6,6,4,4,4)$ | ✅ | **0 / 117 649** | ✅ |
| $(2,2,2,2,2,2)$ | $(6,6,6,6,6,6)$ | ✅ | **0 / 117 649** | ✅ |
| $(4,4,4,4,4,4)$ | $(4,4,4,4,4,4)$ | ✅ | **0 / 117 649** | ✅ |
| $(2,4,2,4,2,4)$ | $(6,4,6,4,6,4)$ | ✅ | **0 / 117 649** | ✅ |

So: **at $L_6$, $p=7$, ord 3, the order criterion is not merely necessary
but sufficient.** Stated that way, §9 stops being a synthetic decoration
and becomes a converse theorem — *at a large enough arena the bridge
question reduces exactly to $(I-E)^{\mathrm{ord}}=I$, and HA's readout
fails it at every one of 1 440 cells and every prime tested up to 293*.
That is the result that would make the grown arena mean something, and it
is one gate away.

**Repair.** State and gate the sufficiency direction (with the
diagonalisability argument), scope it honestly ($p\equiv1\bmod3$ and ord 3;
open at $p\equiv2\bmod3$, where $\rho$ acts irreducibly on 2-dimensional
blocks that the declared growth family's diagonal $\Sigma$ cannot realise),
and disclose that $L_m$, $m>1$ carries no system-triple reading.

---

### F-7 (MEDIUM, terminology) — "SET-LEVEL" is used in two incompatible senses inside one paper

DECL family (ii) and §5.2 call the 1 434 non-equivariant identifications
"the **SET-LEVEL** cells" — but those cells are ordinary candidates with
S1b fully enforced. §12, X06 and Open-1 use "the **set-level** relaxation"
in the corpus's established sense: *dropping S1b* (LCB's own usage, where
the set-level census is $8.157\times10^{56}$ and the constant-identity map
is a witness). A reader who meets §6.2's *"the set-level covariant family
has survivors"* and then §12's *"It does not decide the set-level
relaxation"* will read one claim as bearing on the other. It does not.

**Repair.** Rename the cell role `GENERIC` or `NON-EQUIVARIANT` throughout;
reserve "set level" for the S1b-dropped question.

---

### F-8 (MEDIUM, §14/§15) — the slot-relabelling group is declared as an arena action "the verdict must be invariant under", but it is not a symmetry of the object

**Evidence.** I measured how the identification acts on the encoding:

```
E(perm) == E(nat) · P   (RIGHT multiplication):  True
E(perm) == P E(nat) P⁻¹ (conjugation):           False
```

`encoding_matrix` permutes **columns only** (`morder = [SLOTS3[i] for i in
perm]`). So the 1 440-cell "covariant family" is a coset $\{M P\}$, not a
conjugation orbit: the spectrum, the fixed-space dimension and the
precheck status all move (580 pass, 860 stillborn at $p=7$). Meanwhile the
one action that *is* an invariance — $GL_6$ conjugation, §11's
basis-change self-test — preserves both decision quantities **analytically**,
and the paper correctly says so.

The DECL "arena action" row bundles both under *"these six are THIS UNIT'S
OWN declared choices **and the ones the verdict must be invariant
under**"*. The verdict (aggregate EMPTY) is invariant under the slot
relabelling; the *decision quantities* are not, and the FOUND half of the
verdict name is exactly the non-invariant part (F-3). RUNBOOK §15's
principle — *arena-artifacts may serve as instruments but never as
conclusions* — is therefore breached at one point: the precheck-survivor
existence is an artifact of the relabelling choice, and it is entered into
the verdict's name.

**Repair.** Move the slot relabelling from "arena action" to "family";
describe the 1 440-cell sweep as a **coverage sweep over distinct
encodings**, which is what it is (and which makes §7.2 stronger, not
weaker); keep $GL_6$ conjugation as the unit's only genuine covariance and
keep its "analytically forced" tag.

---

### F-9 (MEDIUM, K2) — §9.3 is not "the same machinery at the same arena, changing nothing else"

`empty_at_grown = empty_branch(not order_criterion(Ereal, 7, 3))` — a
$6\times6$ matrix power. It takes **no arena argument at all**. Against it,
FOUND is decided by a 117 649-cell permutation construction. So the A/B
comparison compares two different procedures, and the phrase "changing
nothing else" is inaccurate; likewise the scope-box's "at both declared
arena scales".

The *conclusion* is right and is in fact stronger than stated: the order
criterion is arena-free, so **no** arena can rescue HA's encoding, and no
comparison is needed to establish it. §9.3's staging weakens a theorem into
an experiment.

**Repair.** Replace the comparison with the direct statement (the criterion
has no arena input; therefore growing the arena removes the cardinality
obstruction and leaves the order obstruction untouched), and keep the
FOUND control for rung 2 only.

---

### F-10 (LOW-MEDIUM, numerical scope) — §12's "580 of 1 440 … at the declared primes" is wrong at five of the seven

Survivors are **580** at $p=5,7$ and **652** at $p=11,13,17,19,23$ (the
paper's own §6.2 table and G35's qualifier row are correct; only the §12
prose is not). Failure-catalogue #40 F1/F2: *scope tags at the claim, not
just the receipt.*

**Repair.** "580 at $p=5$ and 7, 652 at $p\ge11$."

---

### F-11 (LOW-MEDIUM, K5) — two must-pass gates carry an undisclosed scope

Both homomorphism checks — the FOUND control's (G24) and BREAK-HOM's
(G27) — run over $\{0,1\}^6\times\{0,1\}^6=4\,096$ pairs only. Coordinate
sums never exceed 2, so **modular wrap-around is never exercised**. The
paper reports "$\alpha$ … a homomorphism / **0** violations" and "**1 536**
measured homomorphism violations" with neither denominator nor scope,
while X03 does disclose the analogous scoping for route B. I verified the
numbers are nonetheless right (0 violations on 20 000 random full-range
pairs), so this is a disclosure defect, not an error.

**Repair.** State the grid (or widen it); add "1 536 of 4 096".

---

### F-12 (LOW) — the three "both outcomes reachable" calibrations rest on one synthetic matrix

$\mathrm{diag}(6,6,6,4,4,4)$ is simultaneously G16's synthetic compatible
pair, G18's criterion positive control, and G24's $\tilde E$. Three
independent-looking calibrations, one object. My F-6 table supplies
alternatives at no cost.

**Repair.** Disclose the common origin, or use a structurally different
second control (e.g. $\mathrm{diag}(4,4,4,4,4,4)$, verified above).

---

### F-13 (LOW) — the anchor split is mislabelled

"26 anchors — 15 EXTERNAL …, **11 SELF (this file's own hash pins)**". The
11 are SHA-256 pins **of other units' artifacts** (TB3/LCB/HA/BRG/PSI
papers and receipts, and the RSQ pin). The classifier keys on the string
`"this file, pinned SHA-256 of a TERMINAL artifact"`, which describes who
*asserts* the pin, not what is pinned. "SELF" reads as self-hashes of the
RSQ source, which none of them is.

**Repair.** Rename to "11 artifact-hash pins / 15 committed-number anchors".

---

### F-14 (LOW) — "$\delta_\pi=F_3$ at 30 of 30" compares an expression with a copy of itself

`delta_pi`'s live branch and `form_F3` are the same four-factor formula
written twice; the comparison is a code-duplication check. It does die
under `encoding-lax`, so it is not vacuous, but §4's table row reads as a
verification "against the three forms". The real measurement in that row —
$F_1=F_3$ at exactly the 20 involution cells and nowhere else — is genuine
and I reproduced it. Cf. RUNBOOK §14 addendum (v13 #219).

---

### F-15 (LOW, K4) — the thresholds are not all "computed and never typed", and they measure capacity, not admissibility

`scale_threshold_elementary(p, rank) = rank*p + 1` is a **typed closed
form** (correct — the minimal faithful permutation degree of
$(\mathbb Z/p)^r$ is $rp$), and `growth_member_threshold` searches over that
typed quantity; only the divisibility column is a genuine Legendre search.
More substantively, the column answers *"does $G_C$ contain an elementary
abelian rank-6 subgroup?"* — not *"does $\Sigma_\pi$ normalise one with the
demanded exponent?"*. At the native arena only **6 of 126** order-5
subgroups are normalised (I reproduced this), so the gap between capacity
and admissibility is real and measured elsewhere in the same paper. §10.1's
prose is careful; the anchor's quantity string ("the smallest arena
**admitting an injective candidate**") is not.

---

## 2. K2, MEANING half — what the injective square at 43 labels proves

Collecting F-5, F-6, F-9 into the answer the protocol asks for:

**It establishes:** that the census instrument is not a dead branch, and —
the one genuinely informative rung — that the EMPTY verdict is caused by
the **encoding** and not by arena size, prime, or instrument. That is worth
having, and it is the correct answer to "is EMPTY an artefact?".

**It does not establish that bridges exist in-family at scale.** The square
at 43 labels is built by *defining* the deformation side to be $I-\rho$ for
the transport side's own conjugation action. Nothing about a record, a
metric, a chart or HA's readout enters it. The 117 649 verified cells are
an algebraic identity; the 117 648 "held-out" cells hold out nothing,
because no parameter was ever fitted.

**Is the grown arena in-family?** By the pin's text: the *scale* is, the
*encoding* is not. Item (6) of the pin requires "the scale-threshold table
recomputed", which makes arena growth a declared parameter of the
construction; DECL family (vi) declares both scales before fixture truth;
so $L_m$ is a legitimate family member as a *scale parameter*. But (a) the
pin's candidate family is "the $d=3$ record-is-metric encoding against the
three-wing commutator encoding", and $\mathrm{diag}(6,6,6,4,4,4)$ is
neither, and (b) $L_m$ for $m>1$ carries no system-triple interpretation —
it is a combinatorial capacity extension, and the paper should say so.
**Verdict on the control: legitimate arena, out-of-family encoding, and the
paper's X05 says exactly that — but §9.1's opening sentence, "The FOUND
branch is not demonstrated only synthetically", contradicts X05 and is the
single most misleading sentence in the paper.** It should read: *"The FOUND
branch is demonstrated with a synthetic encoding at a declared arena
scale — which is what makes §9.3's separation meaningful, and no more."*

---

## 3. K2 — the scale-convergence thesis, audited sentence by sentence

**Question: is "everything opens with growth" a measured pattern or a
narrative?** My finding: **narrative — and this paper's own strongest
result refutes it.**

The three data points do not form a pattern; they are three different
parameters:

| arc datum | what actually varies | does it support "opens with growth"? |
|---|---|---|
| LCB: primes derivable at **16 labels** | arena size, $=3p+1$ | **No — LCB itself refused it.** LCB §12.3: *"the arena that produces the tighter narrowing is itself a function of the declared prime … A derivation of $p$ that must first be handed the arena $p$ chooses is not a derivation of $p$."* Reported, explicitly **not adopted** |
| RSQ: injectives at **43 labels** | arena size, $=6p+1$ | **No.** 43 is $6p+1$ at $p=7$ — the threshold is *defined* by the rank and the prime it is said to open. Same circularity LCB rejected, one rung up. And what opens is a synthetic encoding, not the family's |
| TB3: torsion at **three wings** | the *base* (which completion), at fixed 8 labels | **Not a growth statement at all.** TB3's 7-torsion contrasts 720 order-7 elements at the richest holonomy against 0 at the reference — a base-dependence result at constant arena |

**And RSQ measures the opposite.** The order obstruction is
**arena-free**: $(I-E)^{\mathrm{ord}}=I$ is a condition on $E$ alone, with
no arena, no prime part, no cardinality in its derivation. Growth removes
the *capacity* obstruction ($p^6>|G_C|$) and leaves the order obstruction
exactly where it was. §9.3's own headline — *"the FOUND and EMPTY branches
are separated by the ENCODING, not by the arena, the prime, or the
instrument"* — is the antidote to the thesis, and it is this unit's best
sentence.

**Sentences that carry the narrative further than the measurements** (all
should be repaired):

1. Scope box, l.25: "at **both declared arena scales**" — one row was
   evaluated at the grown scale, by a function with no arena input (F-9).
2. §9.1, l.478: "The FOUND branch is **not demonstrated only
   synthetically**" — contradicts X05 (§2 above).
3. §9.3, l.513: "at the **same** grown arena and the **same** prime, and
   **changing nothing else**" — the decision procedure changed too (F-9).
4. §9.5, l.535: "at **both** declared arena scales, and it does not move" —
   the native entry is a typed `True` (F-4).

Everything else in §10.1 is careful and correct: "divisibility is strictly
weaker than realisability" (26 vs 31 at $p=5$) is a real measurement, and
"the native three-wing arena admits an injective candidate at NO declared
prime" is right and I verified it.

---

## 4. K3 — the precheck architecture as instrument doctrine

**Is stillborn-before-census the right permanent form? Yes — with one
amendment, and it should enter the RUNBOOK.**

What the architecture gets right, and why it generalises:

- It is a **structural necessary condition evaluated before any
  enumeration**, so a candidate that cannot possibly work is recorded with
  its *mismatch computed* ($343:1$, $49:1$, $7:1$) rather than disappearing
  into a zero row of a census table. That is strictly more informative than
  a census: the reader learns *how far* the candidate misses.
- It is **two-way calibrated** before use (G16: a synthetic
  $\dim\mathrm{fix}=0$ pair passes, a $\dim\mathrm{fix}=3$ pair fails,
  through the same function), so it cannot be a blind rejector.
- It is measured to be **subsumed** by the census criterion, strictly
  (0 vs 4 420) — so the paper can say *why* the precheck is the right first
  stage: it is the criterion's first-order shadow. This is the strongest
  methodological point in the paper and it is correctly made.
- The census cells are declared to include candidates of **every measured
  precheck status** (G15), so the census is not run only where it is
  expected to be empty.

**The amendment.** A precheck that decides which candidates are *worth
censusing* must not also decide the *name of the verdict*. In RSQ it does
both: `any_survivor` — a precheck-level quantity that varies over the
declared arena action (F-8) — selects between `RSQ-NO-COMPATIBLE-SQUARE`
and `RSQ-SQUARE-FOUND-…`. That is the doctrine's one failure mode, and it
is the mechanism behind F-3.

**Proposed RUNBOOK §13 addendum (from v13 RSQ):**

> **The stillborn precheck.** Where a pairing's admissibility has a
> structural necessary condition cheaper than its census, that condition is
> evaluated FIRST, per candidate, and a failing candidate is recorded
> STILLBORN with its mismatch COMPUTED — no census is run for it. The
> precheck must be calibrated in both directions through the same function
> before it is applied, and its relation to the census criterion (subsumes /
> is subsumed / independent) must be MEASURED, not argued. **A
> precheck-level quantity may gate which candidates are censused; it may
> never by itself select the verdict's name.** Where the precheck's outcome
> varies over the unit's declared arena action, the verdict must report the
> outcome on the MOTIVATED sub-family separately, and both readings ship.

**The $p=7$ meeting landing on the stillborn cell — how strong is the
framing?** Strong, and it is the paper's most disciplined moment. R2-LCB's
F-10(c) predicted that at three wings the spectral obstruction moves from
the eigenvalue 2 to $1-\omega$; RSQ tests it *in-arena* rather than
arithmetically — reading the realised values off the conjugation exponents
of the subgroups each wing symmetry actually normalises — and finds the
meeting real, unique to $p=7$, and confirmed. I reproduced every cell of
that table, including the two reasons the demanded values at 13 and 19 are
never realised ($G_C$ has no $p$-torsion above 7) and the exponent split
$\{2,4\}$ at the two order-3 wings.

And then the paper immediately prices it: *"the meeting occurs at the
equivariant identification … and the precheck has already declared that
cell STILLBORN … what the meeting buys is a non-empty S1a+S1b census and
nothing more."* That is exactly the right move — a confirmed prediction
reported with the measurement that neutralises it. **This is a near-miss
framing done properly, and it should be the corpus's model.** My only
addition: the paper could say *why* the meeting must land on a stillborn
cell — the meeting requires eigenvalue $1/2$, which lives in the
counts$\to q$ direction, and in that direction HA's readout also carries
eigenvalue 1 with multiplicity $d$ (P-4), which is precisely the stillborn
condition. The near-miss is not a coincidence; it is forced by the same
spectrum.

---

## 5. Verdict naming — does the pin's vocabulary carry it?

**`RSQ-SQUARE-FOUND-BRIDGE-EMPTY`:** pin-legal, and I will not ask for it
to be withdrawn. The pin's outcome reads *"a candidate passes the precheck;
the census returns empty; the obstruction named"*, and all three hold. The
widened family was declared before fixture truth and G01 measures the
freeze.

**But `FOUND` is not honest without its companion measurement**, for the
reason in F-3: the found squares are the ones the pin's own question
excludes ("honestly-motivated"), and they are the set-level candidates
whose weakness LCB's panel established — LCB measured the S1b-dropped
census at $8.157\times10^{56}$ with the constant-identity map as a witness,
precisely to show that a candidate class this large certifies nothing. RSQ
does not repeat that error (S1b is enforced at every census row), but it
does repeat its *shape*: the survivor class is 1 434 objects selected by
lexicographic-first-that-passes.

**`UNIVERSAL-FOR-THIS-FAMILY`:** earned, correctly computed
(`coverage_qualifier` returns `PARTIAL-k-OF-n` otherwise, probed in G37),
and — per P-2 — **understated**: the emptiness survives 60 primes to 293
and dimensions 2 and 4. The comparison to LCB (56 arena-free vs 28
arena-carried) is accurate to LCB's own numbers, though it compares a
12-cell family's 84 pairs against a 1 440-cell family's 20 160 rows, and
the denominators should be shown.

**Required naming repairs:** the sub-qualifier of F-3(b), the companion
`RSQ-NO-COMPATIBLE-SQUARE`-at-the-motivated-family reading of F-3(c), and
the source relabel of F-1.

---

## 6. K1 (relation), at my depth

Is the order obstruction genuinely new relative to LCB's fixed-point
mismatch, or the same wall in module clothing? **New as a condition, and I
verified the containment is strict (0 criterion cells against 4 420
precheck-surviving (cell, prime) pairs). But its entire marginal content
lies outside the pin's motivated family.**

The argument: the criterion implies the precheck (if $(I-E)^n=I$ then
$I-E$ is invertible, so $\ker(E-I)=0$). Therefore the criterion says
something *new* only where the precheck passes — the 4 420 pairs — and
every one of those is an unmotivated relabelling (F-3). At every motivated
identification, at every dimension $d=2,3,4,5$ and every prime, LCB's
transported wall already closes the square, because $\dim\ker(E-I)=d\ge2$
(P-4). So:

> **The order obstruction is a genuine strengthening of LCB's wall whose
> marginal content is confined to encodings nobody has argued for.**

That is not a criticism of the result — it is the scope sentence the paper
owes, and it is more interesting than "stronger than LCB's".

---

## 7. K4 and K5, at my depth

**K4.** The X01/Deviation-1 reading of the pin's "$V:\mathbb F_p^3\to
\mathbb F_p^6$" as $V=\mathbb F_p^6$ is **legitimate and forced**: a
$3\to6$ map has no determinant, and the pin's own stated $\det=8$ and
spectrum $\{1,1,1,2,2,2\}$ pin the object uniquely. I recomputed both from
scratch and also the general law $\det=2^{d(d-1)/2}$, spectrum
$\{1^d,2^{d(d-1)/2}\}$ at $d=2,3,4,5$. The reading matches R2-LCB's F-10(d)
and F-10(a)'s "$\ge6p+1$ (31 at $p=5$)" exactly. The $d=2$ anchors to LCB's
$3p+1$ (16, 22) reproduce. The carrier sizes $p^{k+3}$ and $\rho\bmod p$
all check ($6^{-1}\bmod p=1,6,2,11,3,16,4$ at the seven primes). No issue.

**K5.** 26 anchors, all matched (I printed and checked each); 38 gates,
0 must-pass failures; 57 mutants, 0 survivors — all reproduced by my own
re-run, which is byte-identical to the frozen output. The
9-declared-cells-vs-1 440-swept deviation (Deviation 3) is **honest and
correctly stated**: it says plainly that the enumerative census at all
1 440 cells was not run and that the criterion sweep is what carries the
verdict. The covariant sweep is cell-complete (I recount 4+2+1434=1440).
The instrument probe G37 is a real probe with 13 negative cases, including
the `RSQ-NO-COMPATIBLE-SQUARE` branch. Defects are F-4, F-11, F-12, F-13,
F-14; the verdict-in-gate defect is F-1/F-2.

---

## 8. Successor requirements — the continuum rung of the bridge question

Asked for explicitly. Given the thresholds table, five requirements,
measured:

**S-1. Do NOT carry the thresholds table to the continuum rung.** It
measures a *capacity* obstruction — the minimal faithful degree $rp$ of
$(\mathbb Z/p)^r$ — that **vanishes** in the continuum: an infinite arena
holds any separable image. Carrying it would manufacture exactly the false
"opens with growth" headline audited in §3. The table's honest successor
role is as a *negative* control: it is the obstruction that dies first, and
its death changes nothing.

**S-2. Carry the order obstruction, restated spectrally and basis-free.**
It is the only arena-free ingredient here, and it survives the passage to
the continuum unchanged in form:

$$\text{a bridge at a wing symmetry of order } n \implies
\mathrm{spec}(I-E)\subseteq\mu_n,$$

and for a continuous (compact one-parameter) symmetry group, $\rho=I-E$
must lie in a compact orbit, i.e. $\mathrm{spec}(I-E)$ on the unit circle.
**HA's readout in its motivated coordinates carries eigenvalue 1 with
multiplicity $d$ at every dimension (P-4), so $0\in\mathrm{spec}(I-E)$, and
$0$ lies on no unit circle.** The continuum rung therefore inherits a
*proof*, not a census — and the successor should be posed that way from the
start rather than as another enumeration.

**S-3. Prove the sufficiency direction, do not exhibit it.** F-6 shows the
criterion is sufficient at $L_6$, $p=7$, ord 3 for every diagonal pattern.
The general statement the successor needs is: *for every $E$ with
$(I-E)^n=I$ over $\mathbb F_p$, is there a member of the growth family and
an elementary abelian $A\le G_C$ normalised by $\Sigma_\pi$ realising
$\rho=I-E$?* **Open at $p\not\equiv1\bmod n$**, where $\rho$ acts
irreducibly on blocks of dimension $>1$ and the declared growth family
gives $\Sigma_\pi$ only block-diagonal (cyclic) actions. Without this, the
continuum rung has a necessary condition and no converse, and "the bridge
question reduces to the criterion" is unproven.

**S-4. Pose the motivated-identification question FIRST, and pre-register
its outcome separately.** Any successor that sweeps $n!$ relabellings will
*always* find precheck survivors and will *always* be able to report FOUND
on the technicality of F-3. The successor's pre-registered outcome list
must be **indexed by the motivated sub-family** — e.g.
`⟨OUTCOME⟩-AT-MOTIVATED` and `⟨OUTCOME⟩-AT-COVARIANT-CLOSURE`, both
computed, both reported — so that the covariance sweep required by §15
cannot silently supply the positive half of a verdict.

**S-5. Open 2 is the only live route named here, and it must be motivated
before it is built.** The permutation-module obstruction is a statement
about link sets that the chart symmetry *permutes*; a datum space carrying
a non-permutation $S_3$-module evades it (the paper's own synthetic control
proves the evasion is possible). But an adjacency invented *because* it
evades the obstruction repeats F-3 one level up. The successor must
declare the adjacency's motivation, in the deformation side's own
vocabulary, **before** computing its module type.

---

## 9. Summary of required repairs

| # | severity | repair |
|---|---|---|
| F-1 | HIGH | source 1 is a restriction of source 2; relabel, and state the verdict rests on two independent sources |
| F-2 | HIGH | mark "0 of 315 injective" FORCED (criterion **and** cardinality); remove from G35's conjunction; add the rank-1 measurement |
| F-3 | HIGH | add "motivated identifications 6 of 6 stillborn"; add a computed FOUND sub-qualifier; report the `RSQ-NO-COMPATIBLE-SQUARE` reading at the motivated family |
| F-4 | MED-HIGH | S4: replace five typed `True`s with the structural independence statement + a gate; drop "is measured" |
| F-5 | MED-HIGH | state the control's algebraic identity; collapse H1/H2; relabel the teeth and S2 as instrument probes; fix G25's "predictive" |
| F-6 | MED | state and gate the sufficiency direction with its scope; disclose that $L_m$, $m>1$ has no system-triple reading |
| F-7 | MED | rename the cell role GENERIC / NON-EQUIVARIANT |
| F-8 | MED | move slot relabelling from "arena action" to "family"; call the sweep a coverage sweep |
| F-9 | MED | replace §9.3's staged comparison with the arena-freeness statement |
| F-10 | LOW-MED | "580 at $p=5,7$; 652 at $p\ge11$" |
| F-11 | LOW-MED | disclose the $\{0,1\}^6$ homomorphism grid; "1 536 of 4 096" |
| F-12 | LOW | disclose the shared synthetic control, or add a second |
| F-13 | LOW | rename the anchor split |
| F-14 | LOW | own that "$\delta_\pi=F_3$ at 30/30" is a duplication check |
| F-15 | LOW | own the typed threshold formula; separate capacity from admissibility in the anchor's quantity string |

**Recommended additions (not defects):** P-2's extended sweeps (60 primes
to 293; $d=2$ exhaustive, $d=4$ sampled) and P-4's one-line spectral
argument. Both strengthen the paper at negligible cost, and P-4 replaces
20 160 rows with a sentence.

---

## 10. Assessment

The mathematics is right. The order obstruction is correctly derived, the
permutation-module obstruction is correct with a real two-way control, the
transport side is faithfully rebuilt against TB3, and **every one of the
199 quantities I recomputed matched, with the unit reproducing
byte-identically and all 57 mutants dying under my own re-run**. The
substantive conclusion — BRIDGE-EMPTY, arena-free, for an obstruction that
strictly subsumes LCB's — survives the hostile lens and is in fact
understated by its own qualifier.

What fails is the **verdict layer's account of itself** and **four
sentences of framing**: a claimed third source that is the first source's
superset, a must-pass conjunct that is forced twice over, a functoriality
claim carried by typed constants, and a FOUND that is true of the
identifications nobody motivated and false of all three that anybody did.
None of these is a false theorem or a false number; each is a
claim-versus-instrument gap of exactly the kind §13/§14/§15 were written to
catch, and each is repairable in place without re-running anything except
the gates that carry them.

# **ACCEPT-WITH-FIXES**
