# R2 — EFFECTUS / ORDER-LENS HOSTILE REVIEW

## ε-Admissibility and the Mixed-Law Arena (v13 stage 5, RQ0-L3)

**Reviewer:** R2, effectus lens. **Protocol:** `v13/note-rq0-epsilon-hostile-protocol.md` (commit `d670892`), judged against that protocol only.
**Object:** `v13/paper-rq0-epsilon-admissibility.md` + `v13/code/rq0_l3_epsilon_*` at commit `d5eca4e`; pin `6e1aa82`; base `267cb2a`.
**Primary:** K2 (the structural blindness proof, and the decisive ω-quadruple sub-question). **Also owned:** the ε = 0 reduction both directions; the entailment-converse lemma; monotonicity under refinement; the two-component (ε, ω) tolerance deviation and the full-support hypothesis.
**Method:** own exact code, written from the paper's stated definitions, importing nothing from the unit; `/opt/homebrew/bin/python3.13`; `fractions.Fraction` throughout, no float in any path. **85 independent recomputations.**

---

# VERDICT

$$\boxed{\textbf{ACCEPT-WITH-FIXES}}$$

Every number this lens re-derived reproduces exactly — the reduction counts (368 + 3435 = 3803), the census (687, 259, 428, 745/745), monotonicity (1790 pairs, 0 violations), the spectrum (0, 1/16, 1/8, 3/16, 1/4 at counts 1, 10, 25, 15, 1), the inverted ordering, the admitted counts (1, 11, 51), the cost tower (120, 360, 1260, 3120) and every graded-cost residue, ω at 0 against 2/3. **No computed number moved.** The paper-vs-receipt sweep on every gate this lens owns is clean.

The fixes are two **proof-level defects**, both real, both with explicit countermodels, and both repaired by a single missing hypothesis:

1. **Theorem 3.1's (⟸) direction is false as stated.** A composition-closed law of genuinely multi-valued admitted operations can be terminal-**admissible** with ε = 1/2. The ε-form at tolerance zero is *strictly stronger* than the terminal axiom there, not equal to it.
2. **Lemma 2.3's converse is false as stated** at support-valued laws — 20 countermodels at two configurations, 45 810 at three, **zero** of them at deterministic laws.

Neither defect touches a headline. Both live outside the deterministic law families where every substantive measurement was taken, and the measured sweeps that do cross into support-valued territory (the `ALL` rows) are *correct* — the counterexamples cannot arise there, for a reason given in F1 below. The registered outcomes stand as registered, and **`RQ0-L3-BLOCKED-AT-PROVENANCE` is correctly instantiated** (K2 adjudication below).

A third fix is expository but sits on the stage's central claim: the structural blindness proof is stated as a **non sequitur**, and the witness that actually carries it is introduced as decoration.

---

# K2 — THE ADJUDICATION (primary)

## K2.1 The decisive sub-question: is ω also a function of the quadruple?

## **YES. ω is a function of the quadruple. It does not escape the structural argument, and `RQ0-L3-BLOCKED-AT-PROVENANCE` is correctly instantiated.**

**Proved.** By Definition 9.2, $\omega(P)=\sum_{r\in A(B)}p_r\,\mathbb 1[q_r=0]$ where $p_r=\rho(r)$ depends on $(A(B),\rho)$, and $q_r=|r\cap\operatorname{Reach}(P)|/|\operatorname{Reach}(P)|$ depends on $(A(B),\operatorname{Reach}(P))$. $\operatorname{Reach}(P)$ is the declared preparation closed under the realized legs of the declared family, hence a function of $(X_0,\mathfrak F)$; and $\mathfrak F=\operatorname{Pres}_L(A(B))$ is a function of $(A(B),L)$ by clause (a). So

$$\omega \;=\; f\bigl(A(B),\ \operatorname{Pres}_L(A(B)),\ X_0,\ \rho\bigr),$$

a function of the quadruple and the declared state. ∎

**Measured, over the whole census.** Every (boundary, family, preparation) key over all 687 censused laws × all 5 records × all 7 non-empty preparations — **6118 distinct keys — carries exactly one (ε, ω) value. Zero keys carry two.** ω cannot read anything the quadruple does not carry. Separately: varying the preparation at fixed (boundary, family, law) moves ω in **469 of 600** triples and moves ε in **0 of 600** — ω's argument list is strictly larger than ε's, and strictly inside the quadruple.

**So the phrase "which claims to read the realized process" in the protocol does not survive contact.** ω reads the *declared* preparation and the family's *declared* legs. "The patch's own realized process" is a derived object of two declared components; nothing in ω is laboratory data the adversary does not supply. §9.1's own sentence — "an adversary who declares the preparation moves ω exactly as one who declares the state moves ε" — is exactly right, and this lens confirms it rather than refuting it.

**Consequence for the escalation:** the escalation is correctly placed. ω is progress *in kind* (it is the first statistic in this corpus that reads the third component) but not *in level*. After stage 5 the four components are read as: boundary ✓ (both), family ✓ (both), preparation ✓ (ω only), law — **only through $\operatorname{Pres}_L(A(B))$**, which is strictly weaker than reading $L$ (F5 below). The block is at the declaration, as registered.

## K2.2 The structural proof: sound in substance, stated as a non sequitur

Theorem 5.3 reads: *"ε is a function of the quadruple… Provenance is not a component of the quadruple… **Hence** no statistic on the quadruple can separate a forged declaration from a legitimate one."*

**The "hence" does not follow from the premises as given.** "Provenance is not a component of X" does not entail "no function of X determines provenance" — a function of X determines Y whenever Y factors through X, and provenance could in principle have factored through the quadruple (had, say, forged declarations always produced a distinctive closure size). What is actually required is the strictly stronger statement

> **forgery is not a function of the quadruple**,

which needs a *collision witness*: two patches with identical quadruple and opposite provenance. Gate `L3-09` supplies exactly that witness — the manufactured $1{+}1{+}1{+}1$ context and the legitimate address context present the same carrier partition under the same law, "literally the same patch". **The witness is the load-bearing premise, not an illustration**, and the paper introduces it with "Exhibited rather than asserted", which reads as decoration. With the witness restored to premise position the theorem is sound, and this lens confirms it: same quadruple ⟹ same ε and same ω, over 6118 keys, zero exceptions.

**Two scope facts the theorem must carry with it.**

- **The witness lives at ε = 0, at the finest boundary.** The receipt records `epsilon_forged_declaration: "0"`, `epsilon_legitimate_declaration: "0"` — the collision is exhibited at the carrier's own configuration algebra, the one patch the terminal axiom *admits* and where the separation question does not arise. The separation *failure* of Theorem 5.1 is measured somewhere else entirely: at the coarse boundaries $\{01\mid2\mid3\mid4\}$, $\{01\mid23\mid4\}$, $\{0123\mid4\}$. The structural theorem therefore does not cover its own headline instance.
- **On those three coarse patches a quadruple statistic *does* separate — ε itself does.** ε takes three *different* values on them (1/16, 1/8, 3/16). What fails is not distinguishability but **order**: no threshold puts the legitimate one inside and both forged ones outside. Theorem 5.3's claim is true in the universal reading ("no statistic separates *all* forged from *all* legitimate", witnessed by the collision) and **false in the existential reading** ("no statistic tells these three apart"). §5's closing sentence — "It cannot be answered by any statistic on the declared data at this scope" — is only defensible in the universal reading and must say so.

## K2.3 What the structural claim *understates* (and this is the sharper result)

"ε is a function of the quadruple" is true but weaker than what is measured, and the weakness hides the real finding. The chain, each link verified here:

| ε's actual argument list | scope | verified |
|---|---|---|
| function of the **quadruple** | as claimed | trivially |
| function of the **triple** $(A(B),\operatorname{Pres}_L(A(B)),\rho)$ — the declared preparation is *not* an argument | everywhere | 0 of 600 triples move ε under preparation variation |
| function of $(A(B),\rho)$ **alone** — the law drops out | identity-containing laws (Thm 4.2) | 52 records × 4 laws, exact |
| **function of the number of atoms alone** | the committed state | all 52 records, every committed law |

The last line is a corollary the paper does not state and should:

> **Corollary (committed state).** $\varepsilon(\pi)=\dfrac{5-|\pi|}{16}$ for every record $\pi$ at the committed carrier under every identity-containing committed law.

Three consequences follow at once, each independently confirmed:

- The spectrum counts 1, 10, 25, 15, 1 **are the Stirling row $S(5,k)$** — the ε-spectrum is the partition lattice sorted by block count and nothing else.
- **The inversion is arithmetic, not subtlety.** The legitimate coarse patch has 2 atoms, the forged ones 3 and 4; fewer atoms ⟹ larger defect. The ordering could not have come out any other way.
- **Clause (b) at tolerance τ is exactly the condition "the declared boundary has at least $5-16\tau$ atoms."** Verified as a set identity at every candidate threshold. So "ε-admissibility" at the committed state is a *cardinality cut on the declared boundary* — it reads neither the shape of the boundary, nor the law, nor the preparation, nor provenance. This is a far stronger statement of `RQ0-L3-EPSILON-BLIND` than "ε grades coarseness against state mass", and it is free.

Relatedly, Theorem 4.2's closed form is worth restating in its recognizable form:

$$\varepsilon(\pi)\;=\;1-\sum_{r\in\pi}\max_{j\in r}\rho_j,$$

verified exactly on all 52 records. That is the **Bayes error** of inferring the configuration from the record under ρ. It makes monotonicity (Prop 6.1) a one-line consequence rather than a 1790-pair sweep, and it makes "ε grades coarseness against state mass" precise: ε is the residual Bayes error of the boundary. Forgery is not a Bayes error.

---

# FINDINGS, RANKED

## F1 — [MAJOR, proof] Theorem 3.1's (⟸) direction is false as stated. Minimal countermodel exhibited.

Theorem 3.1 carries exactly one hypothesis ("let ρ have full support") and claims an iff. The (⟸) proof runs: *"If admissible then (i-a) holds, so no declared task separates a pair inside a block, so every $d(F,\pi,\rho)=0$."* **The last step is invalid.** $d(F,\pi,\rho)=0$ requires more than "the task separates nothing inside the atom": with full support it requires every $j$ in the atom to have a **singleton** support, all equal. A genuinely multi-valued admitted operation separates nothing inside an atom and still leaks the atom's mass across two later configurations.

**Countermodel (minimal, exact, verified).** Two configurations. $L=\{F\}$ with $\operatorname{sup}_F(0)=\operatorname{sup}_F(1)=\{0,1\}$ — left-total and composition-closed ($F\circ F=F$). Boundary $\pi=\{01\}$, ρ uniform (full support), preparation the whole carrier.

| clause | value |
|---|---|
| (i-a) $\ker(\mathfrak F)=\pi$ | **holds** (both configurations carry the same support) |
| (ii-a) $\operatorname{comp}(F)=\pi$, $\mathfrak F\neq\varnothing$ | **holds** |
| (ii-b) occupancy + realized identifications | **holds** |
| **terminal verdict** | **ADMISSIBLE** |
| $\varepsilon$ | $\mathbf{1/2}$ |
| $\omega$ | $0$ |
| **(0,0)-admissible** | **NO** |

So at support-valued laws the ε-form at tolerance zero is **strictly stronger** than the terminal axiom — it rejects patches the axiom admits. Swept: **9 disagreements at two configurations** (every composition-closed law generated by one or two left-total operations, 38 laws) **and 124 at three** (every closure of a single left-total operation, 342 laws), across all non-empty preparations in both cases.

**Why the unit's own sweep could not see it, and why the measured numbers are nonetheless right.** The sweep's only support-valued law family is `ALL` (every left-total relation), which is included at $n\le4$ by `L2.committed_laws`. `ALL` is *too large* to be a countermodel: $\operatorname{Pres}_{\mathrm{ALL}}(\pi)$ always contains a deterministic separating map, so (i-a) or (ii-a) fails wherever ε > 0. Verified: **0 disagreements at `ALL` for $n=2,3,4$.** The counterexamples all live at *small* support-valued laws, which the census (deterministic maps only) and the committed families (all deterministic) both exclude by construction.

**Fix.** State Theorem 3.1 with the hypothesis that the admitted law's operations are **single-valued**, or state the general characterization, which is clean and true:

> With full support, $(0,0)$-admissible ⟺ terminal-admissible **and** every $F\in\operatorname{Pres}_L(A(B))$ has singleton supports.

Also: the scope box's law list omits `ALL`, which the reduction sweep actually uses at $n\le4$ (22 of the 368 instances). Add it.

## F2 — [MAJOR, proof] Lemma 2.3's converse is false at support-valued laws.

The (⇐) proof runs: *"(i-a)'s failure means some F separates a pair inside a block. Then $\operatorname{comp}(F)$ is strictly finer than π."* **This step assumes determinism.** (i-a)'s failure gives two configurations in one atom with *different* supports; $\operatorname{comp}(F)$ merges configurations whose supports *intersect*. Different-but-overlapping supports leave $\operatorname{comp}(F)=\pi$ intact.

**Countermodel (minimal).** $L=\{F\}$, $\operatorname{sup}_F(0)=\{0\}$, $\operatorname{sup}_F(1)=\{0,1\}$ (composition-closed), $\pi=\{01\}$: $\operatorname{Pres}_L(\pi)=\{F\}$ non-empty; $\operatorname{comp}(F)=\{01\}=\pi$ so **(ii-a) holds**; $\ker(\mathfrak F)=\{0\mid1\}\neq\pi$ so **(i-a) fails**.

**Census of countermodels:** over every composition-closed law generated by ≤2 left-total operations — **20 at two configurations, 45 810 at three, of which 0 at deterministic laws.** The forward direction (the inherited entailment theorem) survives everywhere tested: **0 failures** in every sweep run here.

This matters because Lemma 2.3 carries Definition 2.2's central design decision — *"(i-a) and (ii-a) are relaxed together because they are one condition"*. At support-valued laws they are two conditions, and ε grades only one of them. **Fix:** add the determinism hypothesis to Lemma 2.3 (it is then exactly right: the two clauses collapse because different supports means different values means different collision blocks), and scope the "one condition, not two" claim to match.

**A compensating strengthening, also verified.** The lemma's *non-emptiness* hypothesis is weaker than it looks: $\operatorname{Pres}_L(\text{one-atom boundary})=L$ for every censused law (verified, 687/687), so an empty $\operatorname{Pres}$ forces $\pi\neq$ the one-atom boundary, whence $\ker(\varnothing)=$ the one-atom boundary $\neq\pi$ and (i-a) fails alongside (ii-a). **974 census instances with empty $\operatorname{Pres}$ — the biconditional holds in all 974.** So for any non-empty admitted law the non-emptiness hypothesis can be dropped; it is load-bearing only against the *empty law*, which is what gate `L3-04` actually declares (`empty_law: list = []`). §3.1 should say "the empty law", not leave "the empty declared family" to be read as arising at a populated law.

## F3 — [MAJOR, gate scope] The reduction is gated with the declared preparation frozen at the whole carrier, where clause (c) is vacuous. All 3803 instances. Repaired here.

Definition 2.2 is a **two-component** tolerance and Theorem 3.1 is an iff about $(0,0)$-admissibility. But the reduction sweep — both the 368 committed instances and the 3435 census instances — sets `prep = frozenset(range(n))` throughout. At the full preparation $\operatorname{Reach}(P)\supseteq X_0=$ everything, so **ω ≡ 0 in every one of the 3803 gated instances**, and clause (c) never fires. The gate's claim ("gated both directions") is about a definition one of whose four clauses it never exercises.

**Repaired by this lens, and the theorem survives.** Re-run over the full census × all 7 non-empty preparations at three configurations: **24 045 instances, 0 disagreements**, of which **9837 have ω ≠ 0** — i.e. 9837 instances that exercise the clause the unit's sweep could not reach. Additionally, all 52 records × all 31 preparations at the committed carrier under DET: **1612 instances, 0 disagreements.**

**And clause (c) is not decorative — measured.** In the prep-varied census there are **3117** terminal rejections in which ω > 0 is the *only* thing blocking the ε-form (ε = 0, family non-empty, no unrealized identification). **Dropping clause (c) produces exactly 3117 disagreements.** This is the first *measurement* of Deviation 1's justification, which the paper asserts on structural grounds only ("a single-component form on δ alone cannot reduce… because δ does not read the declared preparation"). The assertion is correct and now has a number.

**Side observation for the record:** the second residue, clause (d), blocks *alone* in **0** of those instances — the unrealized-identification clause never independently bites anywhere in the prep-varied census.

**Side observation, committed carrier:** ω ≡ 0 at all 52 records × all 31 preparations under DET. The occupancy component is **inert at the committed carrier under the committed deterministic law**; it bites only at laws whose preservation family fails to reach (the counter-law, `law_example42`, the identity-free escape law). Worth one sentence in §9 so nobody reads ω as active machinery at the headline fixture.

## F4 — [MODERATE] Gate `L3-23` records the K2 crux as a hard-coded assertion, gated by an unrelated computation.

The receipt for `L3-23` reads `{"omega_is_a_function_of_the_quadruple": true}`. The gate's *condition* is `occupancy_defect(DISC5, famD, PREP_FULL, RHO, 5) == 0` — a single evaluation of ω at one patch. **That condition does not test the recorded value.** The claim happens to be true (proved and measured here across 6118 keys), but it is the single most load-bearing structural statement about ω in the unit and it is registered without measurement. The gate's claim text also says "the forged and the legitimate declarations of the same partition receive the same ω", which one evaluation establishes only because `L3-09` has separately shown they *are* the same patch — defensible, but the dependency is implicit.

**Fix.** Either re-gate `L3-23` on the factoring test (enumerate (boundary, family, preparation) keys; assert each carries one (ε, ω) value) or demote the value field to a claim string. Do not leave a bare `true` standing where the escalation's hinge is.

## F5 — [MODERATE] The block is one step earlier than registered: ε and ω do not read the declared law either.

Both statistics touch the admitted law **only** through $\operatorname{Pres}_L(A(B))$. Measured over the census: of **874** distinct (boundary, family) keys, **175 are reachable from more than one declared law**, and the worst key is reachable from **428 distinct declared laws** — every one of them indistinguishable to ε and ω at that boundary. Theorem 4.2 is the extreme case of the same phenomenon (inside the identity-containing class the law drops out entirely).

So the honest statement of `RQ0-L3-BLOCKED-AT-PROVENANCE` is stronger than the one registered: at the measured scope, the instruments are blind not only to *how a declaration came to be made* but to *which law was declared*, wherever two laws share a preservation family at the declared boundary. This does not weaken the outcome; it strengthens it, and it forecloses a repair the reader will otherwise reach for ("read the law harder"). It also means the declared data is **not** saturated by (ε, ω): a statistic reading $L$ directly would see strictly more — and by the L3-09 witness still not see provenance.

## F6 — [MODERATE] Prop 6.1's 1790 pairs measure only the class where monotonicity is already a corollary. The harder class is unmeasured — and holds.

Every law in `committed_laws(n)` for $n=3,4,5$ contains the identity. Inside that class Theorem 4.2 gives $\varepsilon(\pi)=1-\sum_r\max_{j\in r}\rho_j$, and monotonicity follows in one line (splitting a block cannot decrease $\sum_r\max$). **So all 1790 swept pairs lie where the result is free**, and the sweep tests the enumerator rather than the proposition. The identity-**free** side — the side of the dichotomy where proper charts live, and where the closed form does *not* apply — is not swept at all.

**Measured here:** over all 687 censused laws including the 428 identity-free ones — **4809 comparable pairs, 0 violations**; and at the identity-free escape law $\{(0,0,2,3,4)\}$ at five configurations — **306 pairs, 0 violations**. The closed form indeed fails off the identity class (**1712 of 3435** census instances; **46 of 52** at the escape law), confirming the scope tag on Theorem 4.2 is necessary and correctly placed. Prop 6.1 generalizes; say so with the identity-free evidence, and note that inside the identity class it is a corollary rather than a measurement.

## F7 — [MINOR] State-relativity is disclosed but its magnitude is not.

§3.1 says an adversary declaring the state "can drive any coarse boundary's defect as close to zero as the state's support allows". At the degenerate sink-only state this is total: **all 52 records have ε = 0**, not merely the forged one. The ε-form at that state admits *everything*, including the one-atom boundary. Worth the number — it converts a hedge into a measured limit, and it makes the point that the state is laboratory data carry its full weight.

## F8 — [MINOR] Scope-tag and prose fixes

- Theorem 5.3 carries `[FIN]`, `[ARENA]` but the state-relativity that drives the inversion is stated only in §3.1 and §5's prose. The common gates require state-relativity named at every ε claim; Theorem 5.1's inversion display and Theorem 5.2's table both quote numbers that move with ρ and neither names the state at the point of claim.
- Abstract, line 34: "over all 1790 strictly comparable pairs swept" — accurate, but the sentence sits beside claims that carry `[CEN]`; the pairs are committed-laws-only. Tag it.
- §12 "25 gates and 19 anchors" — confirmed against the receipt (25 / 19, all passed).
- Forbidden vocabulary: swept the paper for spatial/causal/temporal/QFT/gravity readings of *patch*, *coarse*, *atlas*, *reachable*, *occupied*. **Clean.** Reachability is presented as an order on configurations throughout; the scope box's disclaimer is honoured in the body, including §9's "realized process", which is defined from declared data and nowhere given a temporal reading.
- Single-threaded: the paper narrates no correction rounds and reads as authored. **Clean.**

---

# NUMBERS TABLE — independent recomputation

Recomputed from the paper's definitions with no import from the unit. "Paper" = the value as printed in the paper and receipt.

| # | quantity | paper | R2 independent | ✓ |
|---|---|---|---|---|
| 1 | record lattice, 1–5 configurations | 1, 2, 5, 15, 52 | 1, 2, 5, 15, 52 | ✓ |
| 2 | \|DET\|, \|REV\| at five | 3125, 120 | 3125, 120 | ✓ |
| 3 | \|FUNNEL\|, \|FUNNEL-CLOSURE\| at five | 21, 3006 | 21, 3006 | ✓ |
| 4 | $\lvert\operatorname{Pres}_{\mathrm{DET}}\rvert$: carrier algebra / 2+1+1 / 2+2 / tomo / limit | 120, 240, 420, 1280, 3125 | 120, 240, 420, 1280, 3125 | ✓ |
| 5 | ε-spectrum under DET (value : count) | 0:1, 1/16:10, 1/8:25, 3/16:15, 1/4:1 | identical | ✓ |
| 6 | spectra identical across the identity-containing laws | yes (5 laws) | yes (4 laws recomputed; 5th = COUNTER-LAW not rebuilt) | ✓ |
| 7 | closed form (Thm 4.2) vs max-over-family | agrees, 260 instances | agrees, all 52 × 4 laws | ✓ |
| 8 | **new:** ε = (5 − \|π\|)/16 at the committed state | — | holds, all 52 records, every committed law | ✓ |
| 9 | **new:** ε = 1 − Σ max ρ (Bayes error) | — | holds, all 52 | ✓ |
| 10 | ε on forged 2+1+1 / forged 2+2 / legitimate | 1/16, 1/8, 3/16 | 1/16, 1/8, 3/16 | ✓ |
| 11 | separating threshold set (9 candidates) | empty | empty | ✓ |
| 12 | admitted records at τ = 0, 1/16, 3/16 | 1, 11, 51 | 1, 11, 51 | ✓ |
| 13 | τ = 0 admits exactly the carrier's own algebra | yes | yes | ✓ |
| 14 | committed reduction instances | 368 | 316 + 52 (COUNTER-LAW row) = **368** | ✓ |
| 15 | committed reduction disagreements | 0 | 0 | ✓ |
| 16 | censused laws / identity-containing / identity-free | 687 / 259 / 428 | 687 / 259 / 428 | ✓ |
| 17 | census reduction instances / disagreements | 3435 / 0 | 3435 / 0 | ✓ |
| 18 | identity-free admissible patches, all ε = 0 | 745 / 745 | 745 / 745 | ✓ |
| 19 | total reduction instances | 3803 | 3751 + 52 = **3803** | ✓ |
| 20 | **F3:** prep-varied census instances / disagreements | not run | 24 045 / **0** | new |
| 21 | **F3:** of them with ω ≠ 0 (clause (c) exercised) | 0 | **9837** | new |
| 22 | **F3:** 52 records × 31 preparations under DET | not run | 1612 / 0 disagreements | new |
| 23 | **F3:** rejections where only ω > 0 blocks the ε-form | not measured | **3117** | new |
| 24 | **F3:** disagreements if clause (c) dropped | not measured | **3117** | new |
| 25 | **F3:** rejections where only clause (d) blocks | not measured | **0** | new |
| 26 | Lemma 2.3, committed laws: (i-a)-only / (ii-a)-only | 0 / 0 | 0 / 0 (316 instances) | ✓ |
| 27 | Lemma 2.3, census: (i-a)-only / (ii-a)-only | 0 / 0 | 0 / 0 (2461 instances) | ✓ |
| 28 | **F2:** converse countermodels, support-valued laws, n = 2 / n = 3 | none known | **20 / 45 810** | new |
| 29 | **F2:** of them at deterministic laws | — | **0** | new |
| 30 | **F2:** forward-direction failures, same hunt | — | **0** | new |
| 31 | **F2:** empty-Pres census instances, biconditional intact | not run | 974 / 974 | new |
| 32 | **F1:** Thm 3.1 disagreements at support-valued laws, n = 2 / n = 3 | none known | **9 / 124** | new |
| 33 | **F1:** the minimal countermodel (terminal-admissible, ε) | — | admissible, **ε = 1/2** | new |
| 34 | **F1:** reduction disagreements at `ALL`, n = 2, 3, 4 | 0 (implicit) | 0, 0, 0 | ✓ |
| 35 | monotonicity, committed laws | 1790 pairs / 0 violations | 1484 + 306 (COUNTER-LAW) = **1790** / 0 | ✓ |
| 36 | **F6:** monotonicity over the full census (identity-free included) | not run | **4809 pairs / 0 violations** | new |
| 37 | **F6:** monotonicity at the identity-free escape law, five configurations | not run | **306 / 0** | new |
| 38 | **F6:** closed-form failures off the identity class | — | 1712 of 3435; 46 of 52 | new |
| 39 | cost tower $\lvert\operatorname{Obs}_0\rvert$ | 120, 360, 1260, 3120 | 120, 360, 1260, 3120 | ✓ |
| 40 | graded costs, all four levels | as tabulated §6.2 | every entry reproduced | ✓ |
| 41 | tasks attaining the maximum (single-deletion insensitivity) | "many" | 120, 120, 120, 1280 | ✓ |
| 42 | ε at the degenerate sink-only state (forged 2+1+1) | 0 | 0 | ✓ |
| 43 | **F7:** records with ε = 0 at that state | not stated | **52 of 52** | new |
| 44 | ε of the empty family | 0 | 0 | ✓ |
| 45 | ω(W1), ω(W3) | 0, 2/3 | 0, 2/3 | ✓ |
| 46 | ε(W1), ε(W3) — identical, as δ is | 0, 0 | 0, 0 | ✓ |
| 47 | **K2:** (boundary, family, prep) keys over the full census | not run | **6118** | new |
| 48 | **K2:** keys carrying two different (ε, ω) values | asserted 0 | **0** | new |
| 49 | **K2:** triples where preparation moves ε / moves ω | not run | **0 / 469** of 600 | new |
| 50 | **F5:** (boundary, family) keys reachable from >1 declared law / of / worst fan-in | not run | **175 / 874 / 428** | new |
| 51 | **cross-check for K3:** ω on the three coarse patches, all 31 preparations, DET | not run | **identically 0 — ω does not separate them** | new |

Further recomputations not tabulated: Pres/comp/ker/Reach agreement at every fixture, the 687-law census rebuilt from generators, `Pres_L(indiscrete) = L` for all 687, Bell/Stirling identities, and the per-level distinct-defect ladders. **85 in total. No computed number moved.**

---

# PER-RUNG CONFIRMATIONS

**(a) `RQ0-L3-EPSILON-BLIND`, incl. the inverted ordering and the structural proof — CONFIRMED, and strengthened.**
The separating set is empty over all nine candidate thresholds; the ordering is inverted 3/16 > 1/8 > 1/16; τ = 0 admits 1 record, τ = 1/16 admits 11 including the forgery, τ = 3/16 admits 51. All reproduced exactly. The structural proof is **sound in substance** with the L3-09 witness promoted to premise (K2.2), and the blindness is *sharper* than claimed: at the committed state clause (b) is exactly a lower bound on the number of declared atoms (K2.3). Verdict-level registration is correct.

**(b) The ε = 0 reduction, both directions — CONFIRMED AT THE MEASURED SCOPE; the theorem statement needs a hypothesis.**
All 3803 gated instances reproduce with zero disagreements, and the theorem survives 25 657 further instances this lens ran with the preparation varied. But the *general* statement is false (F1) — one hypothesis (single-valued admitted operations, or the explicit characterization) repairs it, and every substantive measurement in the paper already satisfies it. The gate's coverage claim also needs the preparation caveat (F3).

**(c) The closed form (identity-containing ⟹ ε law-independent) — CONFIRMED, and it is the strongest statement in the paper.**
Verified on all 52 records against every identity-containing committed law, and verified to *fail* off that class (1712 of 3435 census instances), which is exactly what makes the scope tag necessary. Two free upgrades recommended: the Bayes-error form and the (5 − |π|)/16 corollary.

**(d) The mixed-law closures + the law-free-descent finding — NOT INDEPENDENTLY RECOMPUTED BY THIS LENS.** Out of my assignment; R1 and R3 own it. One effectus-lens remark only, offered as an argument check rather than a measurement: §8.1's charge against route (i) — that calling $L^\ast$ *admitted* infers admission from algebraic existence — is the same *shape* of inference this lens finds missing in Theorem 5.3 (existence of a structure vs. a property factoring through it). The paper is right to refuse it there; it should be equally explicit about what carries the inference in §5.

**(e) ω's separations — CONFIRMED, with two scope facts to add.**
ω(W1) = 0 against ω(W3) = 2/3 exactly, with σ and δ identical, reproduced. `RQ0-L3-OCCUPANCY-STATISTIC` is earned. Add: (i) ω is a function of the quadruple — proved and now measured over 6118 keys, not merely asserted in a receipt field (F4); (ii) ω is identically zero at all 52 records × all 31 preparations at the committed carrier under DET, so it is inert at the headline fixture and active only where the preservation family fails to reach (F3).

**(f) The rung set incl. combined `MIXED-LAW-CLOSED` + `PLURALISM-PRICED` — NO OBJECTION FROM THIS LENS on the combination itself (R3 owns the having-it-both-ways charge).** On the rung this lens does own: `RQ0-L3-BLOCKED-AT-PROVENANCE` is **correctly instantiated** — ω does not escape the quadruple, so the census-discipline slot is filled at the right level. It is also *understated*: the instruments do not read the declared law either (F5), and the honest version of the rung should say so. `RQ0-L3-EPSILON-ADMISSIBILITY` "earned in its constructive half only" is the right registration, subject to F1's hypothesis.

---

# SENTENCES TO REWRITE

1. **Theorem 3.1 statement (§3).** Replace *"Let ρ have full support."* with *"Let ρ have full support and let every admitted operation of L be single-valued."* Or state the general form: *"With full support, a patch is (0,0)-admissible iff it is admissible under the terminal axiom and every $F\in\operatorname{Pres}_L(A(B))$ has singleton supports; at a law of single-valued operations the second condition is automatic."* **(F1 — the claim is false without this.)**

2. **Theorem 3.1 proof, (⟸).** *"…so no declared task separates a pair inside a block, so every $d(F,\pi,\rho)=0$"* → *"…so no declared task separates a pair inside a block; since the admitted operations are single-valued, each atom's mass therefore lands entirely on one later configuration and every $d(F,\pi,\rho)=0$."* **(F1 — this is the invalid step.)**

3. **Lemma 2.3 statement (§2).** *"Let $\mathfrak F=\operatorname{Pres}_L(\pi)$ be non-empty."* → *"Let L consist of single-valued operations and let $\mathfrak F=\operatorname{Pres}_L(\pi)$ be non-empty."* Add a footnote: *"Determinism is not decorative: at a support-valued law the one-operation law $\operatorname{sup}(0)=\{0\}$, $\operatorname{sup}(1)=\{0,1\}$ at the one-atom boundary satisfies (ii-a) and fails (i-a)."* **(F2.)**

4. **§2 closing.** *"So the pair {(i-a), (ii-a)} is a single condition"* → *"So at a law of single-valued operations the pair {(i-a), (ii-a)} is a single condition"*. **(F2.)**

5. **Theorem 5.3 (§5) — the non sequitur.** Replace *"ε is a function of the quadruple… Provenance is not a component of the quadruple… Hence no statistic on the quadruple can separate…"* with the witness-first form: *"Forgery is not a function of the quadruple: the adversary's manufactured $1{+}1{+}1{+}1$ context and the legitimate address context present the same quadruple under the same law and the same state — by the terminal cycle's §6.5 literally the same patch — while differing in provenance. Hence no function of the quadruple, ε among them, can agree with provenance on both. The witness is at the carrier's own algebra, where ε = 0; the failure of separation measured above is at the coarse boundaries, where ε takes three distinct values but in the wrong order."* Delete *"Exhibited rather than asserted"* — the exhibit is the premise. **(K2.2.)**

6. **§5 closing.** *"It cannot be answered by any statistic on the declared data at this scope."* → *"No statistic on the declared data can agree with provenance in general, since two patches with the same declared data differ in it. This is compatible with a statistic telling these three particular boundaries apart — ε does — and that is precisely why the failure here is one of ordering, not of resolution."* **(K2.2.)**

7. **§3 (after the reduction).** Add: *"The gated sweep holds the declared preparation at the whole carrier, where ω vanishes identically; the occupancy component of the tolerance is exercised separately."* **(F3 — otherwise "gated in both directions" over-reads.)**

8. **Appendix A, Deviation 1.** After *"…because δ does not read the declared preparation"* add the number: *"Measured: over the census with the preparation varied there are 3117 instances in which ω > 0 is the only clause standing between the ε-form and a patch the terminal axiom rejects."* **(F3 — this converts the deviation's justification from structural assertion to measurement.)**

9. **§4, after Theorem 4.2.** Add the corollary: *"At the committed state the closed form collapses further, to $\varepsilon(\pi)=(5-|\pi|)/16$ — the defect reads the number of declared atoms and nothing else, which is why the spectrum's multiplicities are the Stirling row 1, 10, 25, 15, 1 and why admitting at tolerance τ is exactly the condition that the boundary declare at least $5-16\tau$ atoms."* **(K2.3 — the sharpest available statement of the headline.)**

10. **§6, Prop 6.1.** Add: *"Inside the identity-containing class this is a corollary of Theorem 4.2 rather than an independent measurement; the sweep's 1790 pairs all lie there. It holds off that class too — 4809 comparable pairs over the full census including the 428 identity-free laws, and 306 pairs at the identity-free escape law at five configurations, zero violations."* **(F6.)**

11. **§3.1, full support.** Add the magnitude: *"At the degenerate state the collapse is total — all 52 records have defect zero, the one-atom boundary included."* **(F7.)**

12. **§9.1, first honest half.** *"it is still a function of the quadruple"* → *"it is a function of the quadruple — indeed of $(A(B),\operatorname{Pres}_L(A(B)),X_0,\rho)$, which is strictly coarser than the quadruple, since the declared law enters only through the preservation family: 175 of the 874 (boundary, family) keys in the census are reachable from more than one declared law, one of them from 428."* **(F5.)**

13. **Scope box, Laws row.** Add `ALL` (every left-total relation at two to four configurations), which the reduction and monotonicity sweeps use. **(F1.)**

14. **§9 (after Definition 9.2).** Add: *"At the committed carrier under DET, ω vanishes at every record and every declared preparation; it is active only where the preservation family fails to reach, as at the counter-law."* **(F3.)**

---

# COMMON GATES

| gate | result |
|---|---|
| Paper-vs-receipt sweep (my rungs) | **CLEAN.** L3-01 (368/3435/0/0), L3-02 (745/745), L3-05, L3-07, L3-09, L3-10 (1790/0), L3-21, L3-22 (0, 2/3, 0, 15/16), L3-24 (260, five laws) — every receipt value matches the paper's prose and table. 25 gates, 19 anchors, none failed. |
| Scope tags | **ONE GAP.** State-relativity is disclosed in §3.1 and §11 but not named at the point of claim in Theorem 5.1's inversion display or Theorem 5.2's table (F8). Theorem 4.2's identity-containing restriction is correctly tagged and independently verified necessary. |
| Forbidden vocabulary | **CLEAN.** No spatial, causal, temporal, QFT or gravity reading of *patch*, *coarse*, *atlas*, *reachable*, *occupied*, or of "realized process" in §9. |
| Prose vs gates | **TWO GAPS.** F3 (the reduction gate never exercises clause (c); "gated both directions" over-reads Definition 2.2) and F4 (`L3-23`'s recorded value is not what its condition tests). |
| Deviations complete | **YES, and one is now measured.** All ten check out against the pin. Deviation 1 (the two-component tolerance) is **adjudicated SOUND and is now measured** — 3117 instances where ω alone carries the reduction (F3); the pin's H2 does ask for an occupancy-sensitive statistic, so welding it into the tolerance is within the pin, not around it. Deviation 2 (full support) is **adjudicated SOUND but incomplete**: the hypothesis is correctly declared load-bearing, but a *second* undeclared hypothesis — single-valued operations — is also load-bearing and is not declared (F1). Recommend an eleventh deviation, or fold it into Deviation 2. Deviation 3 (the pin's required outcome refuted, honest finding reported) is exactly what the pin instructed. |
| Mutants / determinism / floats | **Floats: CLEAN** — all statistics are exact rationals; my independent implementation used `Fraction` throughout and reproduced every value, which is an external check on the AST sweep's conclusion. Mutant and byte-identity checking is R3's (anchor fidelity); not duplicated here. |
| Single-threaded | **CLEAN.** No correction rounds narrated; the paper reads as authored. |

---

# NON-CLAIMS OF THIS REVIEW

- No claim about K1 (the inversion's state-quantifier robustness) beyond the one measurement at the degenerate state; R1 owns it.
- No claim about K3 (ω on the forged-vs-legitimate coarse comparison) beyond the cross-check recorded at row 51 — ω is identically 0 on all three named coarse patches at every one of the 31 preparations under DET, so it does not separate them there. Under the identity-free escape law ω does take several values, but the variation is driven by the declared preparation, which the adversary declares. **R3 owns the adjudication.**
- No claim about K4, the mixed-law closures, the law-free descent selector, or the anchor/mutant fidelity; R1 and R3 own those.
- The COUNTER-LAW at five configurations was not rebuilt independently; the two counts that depend on it (368 and 1790) are confirmed by exact arithmetic on the remaining rows plus its known row size (52 records, 306 comparable pairs).
- No claim that F1 or F2 overturns any registered outcome. Both are proof-statement defects at laws outside the families where the substantive measurements were taken, and every gated number stands.
- No spatial, causal, temporal or spacetime reading of any object in this review.

---

**FREEZE-ON-DELIVERY.** This file is final as of delivery.
