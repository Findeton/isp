# R3 — INSTRUMENT/SUFFICIENCY HOSTILE REVIEW

## Stage 5: ε-Admissibility and the Mixed-Law Arena

**Reviewer:** R3 (instrument lens; K3 primary, K4 secondary).
**Protocol:** `v13/note-rq0-epsilon-hostile-protocol.md` (frozen, d670892).
**Object:** `v13/paper-rq0-epsilon-admissibility.md` + `v13/code/rq0_l3_epsilon_*`
at d5eca4e. **Pin:** 6e1aa82. **Base:** 267cb2a.
**Method:** own exact-rational reimplementation from the committed definitions,
nothing imported from the unit or from the three terminal modules; 
`/opt/homebrew/bin/python3.13`; 30 independent recomputations plus one new
measurement the unit did not run.

**Verdict: ACCEPT-WITH-FIXES.**

No false number was found. Every substantive value in the paper reproduces
exactly by an independent route, including all four sweep cardinalities
(368, 3435, 1790, 260), the whole spectrum, the cost tower, the descent
counts and both ω separations. Eighteen of the nineteen anchors were
re-derived from scratch and all eighteen match. The fixes are claim-level:
three gates whose predicate is weaker than the sentence attached to it, one
escalation sentence that this unit's own second statistic falsifies as
written, a one-parameter search reported as exhaustive for a two-parameter
form, and one deviation that under-declares what it deviated from.

---

## 0. THE K3 ANSWER, FIRST AND PLAINLY

**The unasked question: run ω on the forged-versus-legitimate COARSE
comparison that ε failed.**

**It was run. ω does not separate. All three defects are exactly zero.**

At the committed state ρ = (1/16,1/16,1/16,1/16,3/4), the committed law DET
and the committed declared preparation (the whole carrier — the preparation
every patch in §§4–7 of the paper declares):

| coarse patch | provenance | \|Pres_DET\| | ε | **ω** | Reach(P) |
|---|---|---|---|---|---|
| forged aligned manufactured 2+1+1, {01\|2\|3\|4} | **FORGED** | 240 | 1/16 | **0** | {0,1,2,3,4} |
| forged aligned manufactured 2+2, {01\|23\|4} | **FORGED** | 420 | 1/8 | **0** | {0,1,2,3,4} |
| corrected tomographic minimum, {0123\|4} | **LEGITIMATE** | 1280 | 3/16 | **0** | {0,1,2,3,4} |
| the carrier's own configuration algebra | LEGITIMATE | 120 | 0 | **0** | {0,1,2,3,4} |

**And the zero is structural, not a coincidence of the fixture.** ω(P) sums
ρ(r) over atoms r disjoint from Reach(P), and Reach(P) ⊇ the declared
preparation by construction. At the committed preparation no atom of any
boundary is disjoint from the whole carrier, so ω vanishes identically:
measured over **260 instances** (all five committed laws × all 52 records at
the committed carrier), ω = 0 in **260 of 260**. On the committed patch data
the second component of Definition 2.2 is inert. It cannot separate the
forgery because it cannot separate anything.

**Consequence for the adjudication: the escalation HARDENS.** The
`RQ0-L3-BLOCKED-AT-PROVENANCE` registration survives its sharpest available
test. The unit's own new instrument, built precisely because σ and δ were
blind, is blind on the same comparison, and blind for a reason that has
nothing to do with the state (ε's exposure) and everything to do with the
declaration: the adversary declares the preparation, and a preparation of
the whole carrier zeroes ω by definition. Measured: under DET the forged
2+1+1 attains ω = 0 at **31 of 31** non-empty declared preparations. Under
REV and FUNNEL-CLOSURE likewise 31 of 31. The forger does not even need to
choose well.

### 0.1 The one genuine softening, and why it is thin

Two facts cut the other way and the adjudication should have them.

**First, ω's ordering is not inverted — it is the exact reverse of ε's.**
ε is monotone under refinement (coarsening never lowers it), which is why the
legitimate, coarsest patch carries the largest defect. **ω is
anti-monotone**: coarsening never raises it. Swept over every strictly
comparable pair at five configurations under every committed law at three
declared preparations — **4590 instances, 0 violations of anti-monotonicity**.
So wherever ω is non-zero it ranks the legitimate tomographic minimum as the
*most* admissible of the three, not the least. The inversion that damns ε
does not occur for ω.

**Second, separating rows exist — but only off the committed data, and only
one of them is at a genuine law.** Sweeping all five committed laws × all 31
non-empty declared preparations (155 rows), **15 rows** have ω(legitimate) <
both ω(forged):

| law | separating preparations | ω(legit) at the best row |
|---|---|---|
| DET | **0** of 31 | ω ≡ 0 |
| REV | **0** of 31 | ω ≡ 0 |
| FUNNEL-CLOSURE | **0** of 31 | ω ≡ 0 |
| FUNNEL *(a declared task family, not a law — inherited Prop 3.7)* | 12 of 31 | **0** vs 1/8, 1/8 at prep {0,4} |
| COUNTER-LAW | 3 of 31 | **3/4** vs 7/8, 7/8 at prep {0} |

The only rows where ω admits the legitimate coarse patch at tolerance zero
while rejecting both forgeries are at FUNNEL — which this corpus carries as
a declared task family and *not* as a law, so clause (a) of Definition 2.2
(𝔉 = Pres_L(A(B)) at an admitted law L) is not well posed there. At the one
genuine law that separates at all, COUNTER-LAW, the legitimate patch itself
carries ω = 3/4: admitting it requires τ_ω = 3/4, which is the same
"amnesty rather than discrimination" structure that Theorem 5.2 convicts ε
of, transplanted onto ω.

**And the separation, where it exists, is not a provenance separation.** ω is
a function of the quadruple exactly as ε is, so Theorem 5.3 applies to it
verbatim: a forged declaration and a legitimate declaration presenting the
same partition receive the same ω. What the FUNNEL rows separate is
coarseness-relative-occupancy — the legitimate patch wins there because it is
the *coarsest*, and a forgery of the same shape would win identically. The
grading exists; it is a grading of the same wrong thing, with the sign
flipped.

**Net:** report K3 as *ω does not separate; the escalation hardens*; add the
anti-monotonicity as the one honest consolation (it is a genuine structural
difference from ε and belongs in §9.1); and add the 260/260 identical-zero as
the sharpest available statement of ω's inertness on committed data.

---

## 1. FINDINGS, RANKED

### F1 (fix-real, highest) — §5's escalation sentence is broader than anything measured, and this unit's own second statistic falsifies it as written

§5 closes: *"It cannot be answered by any statistic on the declared data at
this scope."* §10 repeats: *"no statistic on declared data separates a forged
chart from a legitimate one."*

Both are false as worded, and the counterexample is built in this paper. ω is
a statistic on declared data. At FUNNEL with declared preparation {0,4},
ω(legitimate tomographic) = **0** while ω(forged 2+1+1) = ω(forged 2+2) =
**1/8**: a statistic on declared data that admits the legitimate coarse patch
and rejects both committed forged ones. Six such rows exist (preparations
{0,4}, {1,4}, {2,4}, {3,4}, {0,1,4}, {2,3,4}).

The claim the paper has actually *proved* is narrower and stronger, and it is
the one Theorem 5.3 and gate L3-09 establish: **no statistic on the quadruple
can separate a forged declaration from a legitimate declaration of the same
patch.** That is airtight — provenance is not a component, so two
declarations presenting the same quadruple are the same argument to every
such statistic. The over-broad version does not follow from it, because
different declarations generally present *different* quadruples, and a
statistic can then separate them for reasons unrelated to provenance (as ω
does, by coarseness). Rewrite to the proved claim.

### F2 (fix-real) — gate L3-23's claim asserts a measurement the gate never performs

The gate's claim string ends: *"Measured: at the committed carrier the forged
and the legitimate declarations of the same partition receive the same
omega."* The predicate is

```
occupancy_defect(DISC5, famD, PREP_FULL, RHO, 5) == 0
```

— a single ω on the carrier's own algebra at the full preparation. It never
computes a forged declaration's ω, never computes a legitimate declaration's
ω, and never compares them. The receipt value confirms it: the only recorded
field is `{"omega_is_a_function_of_the_quadruple": true}`. The word *Measured*
is doing work no computation supports.

The stated proposition is *true* — I verified it, and F-K3 above supplies the
whole comparison the gate should have carried — but a gate whose claim
outruns its predicate is exactly the failure mode the census discipline
exists to prevent. Either run the comparison (the two incidence-presented
declarations of §5's L3-09 fixture, and the three coarse patches of §0 above)
or delete the sentence.

### F3 (fix-real) — Theorem 8.4's load-bearing premise is asserted in a table string, never gated

Theorem 8.4 is registered as *"proved rather than sampled"*, and its entire
force rests on one proposition: **the terminal descent selector takes no law
argument.** That proposition appears in the code only as English inside
`TABLES["inter_law_descent"]["the_terminal_selector_reads_no_law"]` and as
deviation 6's *"measured by inspection of its three functions"*. Gate L3-19's
predicate checks only `len(free_cert) == 14 and discrete(4) in free_cert` —
the certification count at one run. Nothing mechanically verifies law-freeness.

**I verified it independently and it holds.** An AST pass over
`rq0_l1_composite_exact.py` computing the transitive call closure of
`certified_records`, `facts_realized` and `transports_without_collision`
returns `{certified_records, facts_realized, transports_without_collision,
transported_images, fact_of, parts_of}` plus builtins, and **no function in
that closure names any law-valued object** (parameters: `certified_records(
ctx_atoms, inc, partner_facts, n_overlap)`, `facts_realized(ctx_atoms, inc)`,
`transports_without_collision(part, inc)`). I also ran the selector under five
declarations of law and got 14 certified with the greatest record descending
in all five, invariant.

So the finding is *true but ungated*, and the gate is cheap: the AST check is
eight lines. Add it to L3-19 or the claim should read "verified by inspection,
not gated".

### F4 (fix-real) — Theorem 5.1 searches one tolerance parameter for a two-parameter form

Definition 2.2 defines ε-admissibility at a tolerance **pair** (τ_ε, τ_ω) —
that is deviation 1, declared and load-bearing. Theorem 5.1 then reports "no
threshold" separates, and `run_separation` searches nine values of a single
τ, passing it to *both* slots (`eps_adjudicate(..., tau, tau)`). The
separating set is therefore empty *on the diagonal of the tolerance square*,
not on the square.

The conclusion is unaffected at the committed scope — I verified that at the
committed preparation ω ≡ 0 on all 52 records, so the τ_ω axis is inert and
the diagonal result extends to the full square — but the theorem should say
so, because the reader has just been told the form has two components and the
whole point of the second one is that it sees something the first cannot.
One clause fixes it: *"and because ω vanishes identically at the committed
preparation (260 of 260 instances), the search over the diagonal is a search
over the whole tolerance square."*

### F5 (fix-real) — deviation 8 under-declares: the pin's defining condition for PLURALISM-PRICED is measured FALSE

The pin defines the outcome as: *"RQ0-L3-NOMOLOGICAL-PLURALISM-PRICED — **the
escape stands**; its exact price and scope stated (first-class)."* The unit
measures that the escape does **not** stand: it closes at route (i) and at
route (ii). Deviation 8 declares only that the two outcomes "read as
alternatives" and are "not exclusive", registering both because "the price of
closing it is the finding".

That is a redefinition of a pre-registered outcome, not a combination of two.
The registration is nevertheless *defensible* on the paper's own §8.2
reasoning — within the declared scope (one law family per context, which the
paper correctly calls the default) the escape does stand, and both closures
require leaving that scope — but that is the argument deviation 8 needs to
make and does not. As written it reads as having it both ways; with the scope
clause it reads as a finding. Rewrite deviation 8 to say: *the pin's
condition "the escape stands" is measured false at both routes; what is
registered is that the escape stands within the declared scope and that
neither closure runs on committed machinery alone.*

Relatedly, and this is the honest core of the K4 charge: **neither closure
runs on committed machinery alone.** Route (i) needs the uncommitted
amalgamation hypothesis (the paper says so, §8.1, and non-claims repeat it).
Route (ii) needs a selector constructed in this unit, because the terminal
one is law-free (the paper says so, deviation 6 and non-claims). So the boxed
`RQ0-L3-MIXED-LAW-CLOSED` should carry that qualifier where it is registered,
not only where it is discussed. The §10 bullet does say "each under a stated
cost"; the box does not, and the box is what gets cited downstream.

### F6 (fix-real, minor) — L3-09's structural exhibit is degenerate

The exhibit is offered as the measured half of Theorem 5.3: the adversary's
manufactured 1+1+1+1 context and the legitimate address context present the
same carrier partition, so their defects are identical. The receipt records
what those defects are: `epsilon_forged_declaration: "0"` and
`epsilon_legitimate_declaration: "0"`. Both declarations present the
**discrete** partition — the carrier's own configuration algebra, the unique
zero of the whole spectrum, and the one boundary the terminal axiom already
admits.

The equality is real and the theorem is structurally true regardless, but as
an *exhibit* for the separation question it bites on the one partition where
no separation question arises: both are admissible, at every tolerance, under
the terminal axiom and the ε-form alike. The corpus appears to contain no
committed pair of forged and legitimate declarations presenting the same
*coarse* partition, which is worth saying. Rewrite §5.3's "Exhibited rather
than asserted" sentence to state the value (0) and the limitation.

### F7 (adequate, recorded) — the mixed-law arena is measured at exactly one ordered pair of laws

`RQ0-L3-MIXED-LAW-CLOSED` and the route (i)/(ii) prices rest on a single
arena instance: member one at {(0,0,2,3,4)}, member two at DET, partner DET
or the escape law. Deviation 7 declares the substitution of a theorem for a
sweep and the §10 bullet scopes the tag correctly ("the committed arena, the
anchored escape law, DET as partner"). I record it as adequate rather than a
fix because the scope line is present and honest; but a corroborating sweep
over even a dozen law pairs from the 687-law census would cost minutes and
would convert a scoped single instance into a population claim.

### F8 (cosmetic) — L3-05's predicate is weaker than its claim

The claim names the values ("the values are 1/16, 1/8 and 3/16 and they are
the same under DET, REV, the funnel closure and the counter-law"); the
predicate checks only strict positivity over twelve rows. Both halves of the
claim are true (I verified the values and the cross-law identity) and L3-24
independently gates the identity, so nothing is at risk. Tighten the
predicate or shorten the claim.

### F9 (cosmetic) — quotation fidelity

§8.1 renders the inherited doctrine as *"admission is measured per law and
never inferred from algebraic existence."* That is verbatim from B″ §1.1 —
confirmed. (The Cycle B′ paper's variant reads "…and is never inferred…";
the paper quotes the B″ form, which is the right one to quote. No fix
needed; recorded because the sentence is set as a verbatim quotation and
carries the whole forbidden-inference charge.)

---

## 2. K4 AUDIT

### 2.1 The law-free-descent finding — CONFIRMED, twice, by independent routes

| check | R3's independent result | unit |
|---|---|---|
| `certified_records` parameters | `(ctx_atoms, inc, partner_facts, n_overlap)` — no law | as claimed |
| `facts_realized` parameters | `(ctx_atoms, inc)` — no law | as claimed |
| `transports_without_collision` parameters | `(part, inc)` — no law | as claimed |
| transitive call closure names any law object | **no** (AST sweep) | asserted, not gated (F3) |
| forged context certified, law-free | **14** of 15 | 14 of 15 |
| greatest record descends | **yes** | yes |
| invariance across DET/REV/FUNNEL/COUNTER/escape-law | **identical in all five** | claimed by inspection |

The finding stands as the section's strongest result, and the reasoning is
sound: because the selector is a function of (contexts, overlap) alone and
`partner_facts` is itself produced law-freely, the certification is invariant
under every declaration of law, so the attack is carried into the mixed-law
arena for free. The adversary who declares a law per context does keep both
verdicts and the attack.

One caution worth a sentence in §8: the finding is a property of the
*inherited machinery*, not a discovery about laws. The terminal selector was
never law-aware, so "the attack runs at every law" is the statement that
there was no law-dependence available to break it. The paper's framing
("settles a question the terminal cycle explicitly declined to guess at") is
accurate and deviation 6 declares the situation honestly; I flag it only so
that downstream citation does not read it as a measured invariance across a
population of laws.

### 2.2 Both closures' "imports the blockade" adjudication — CONFIRMED

**Route (ii).** The law-relative filter admits a partner fact only if it is an
admissible *boundary* at the partner's declared law. Under DET, rigidity
leaves exactly one admissible boundary, so the partner's assertable fact set
collapses to a single element. I recomputed it: `law_relative_facts` under DET
returns exactly `[((0,),(1,),(2,),(3,),(4,))]` — one fact, the discrete
boundary. Everything follows:

| | law-free | law-relative (DET) |
|---|---|---|
| forged 2+1+1 context certified | **14** of 15 | **0** |
| forged greatest record descends | **yes** | **no** |
| legitimate eraser certified | **51** of 52 | **1** |
| partner = escape law: partner admissible facts / forged certified | — | **1 / 1** |

All five figures reproduce exactly. The mechanism is exactly as adjudicated:
the forged context has four atoms, so its transported fact content can have
at most four blocks and can never equal the five-block discrete fact — hence
0, structurally, not marginally. The eraser has five atoms, so exactly one of
its 52 records produces that fact — hence 1. **"Route (ii) closes the escape
by importing the blockade it was invoked to escape" is correct, and the
mechanism is that rigidity is what does the filtering.** The 14→0 and 51→1
figures are the same theorem applied twice.

**Route (i).** The forbidden-inference charge is correctly stated and
correctly sourced. The least composition-closed law containing
{(0,0,2,3,4)} and DET is DET itself — I recomputed the generator union and
got 3125 — because the escape generator is already a deterministic map. At
DET member one is inadmissible by rigidity, so the escape closes; and member
one's declared family goes from **1** task at its own law to **240** at the
shared one, so the adjudicated patch is not the declared patch. Confirmed.
The doctrine quoted against it — "admission is measured per law and never
inferred from algebraic existence" — is verbatim in B″ §1.1. The charge
lands.

**Is the combined MIXED-LAW-CLOSED + PLURALISM-PRICED registration honest, or
having it both ways?** Honest *in the prose*, under-declared *in the
registration*. §8.2's three bullets are the correct statement of the
situation and are not self-contradictory: closure exists at both routes;
each route exits the declared scope; keeping the declared scope keeps the
escape and the attack. What is not honest enough is (a) deviation 8's account
of what was deviated from (F5) and (b) the unqualified box. Fix both and the
registration is defensible.

---

## 3. THE TEN DEVIATIONS, ADJUDICATED

| # | deviation | adjudication |
|---|---|---|
| 1 | ε-admissibility is a two-component tolerance (ε, ω), not one | **FIX-REAL (partial).** The deviation itself is legitimate and well-reasoned — δ cannot reduce to the terminal axiom alone because it does not read the preparation, and the pin's H2 asks for an occupancy-sensitive statistic. But its consequence is not carried into Theorem 5.1, which searches one parameter (F4). Declare the consequence, not only the change. |
| 2 | the reduction requires full support, which the pin does not name | **ADEQUATE.** Stated with the theorem, shown load-bearing by a degenerate-state control (ε = 0 at the forged boundary while the axiom rejects it — reproduced), and the state-relativity exposure is reported as a limit rather than assumed away. |
| 3 | the pin's required outcome for the ε-form is refuted | **ADEQUATE, and the headline.** The pin pre-authorized exactly this report ("if ε also re-admits it, that is RQ0-L3-EPSILON-BLIND, verdict-level"). The honest finding is delivered in place of the required one, which is what the pin instructed. |
| 4 | the census slot instantiated as BLOCKED-AT-PROVENANCE | **COSMETIC.** A slot fill; the object is measured, not chosen. K3 (§0) strengthens it. |
| 5 | the spectrum delivered stronger than asked (closed form) | **COSMETIC (positive).** Theorem 4.2 is genuine added value and its proof is correct: the identity lies in Pres_L(π) for every law and every boundary and attains the maximum per-task defect, so ε collapses to a law-free quantity. Reproduced over 260 instances. |
| 6 | route (ii) required a construction the pin assumed available | **ADEQUATE**, with F3's caveat: the premise that made the construction necessary is asserted rather than gated. The construction itself is declared, its collateral is measured, and the fact is elevated to Theorem 8.4 rather than buried. |
| 7 | route (i)'s cross-law census carried by a theorem, not a sweep | **ADEQUATE-BUT-THIN** (F7). The inherited comparable-boundaries theorem does quantify over every admitted law, and the §10 bullet scopes the tag to the anchored arena. A corroborating law-pair sample would be cheap. |
| 8 | two pre-registered outcomes registered together | **FIX-REAL** (F5). The pin's defining clause for PLURALISM-PRICED is "the escape stands", measured false at both routes. The registration is defensible on the declared-scope reading; the deviation must say so. |
| 9 | ω is a new statistic, though not a new primitive | **ADEQUATE.** Built from committed data only (declared preparation, inherited reachable subprocess, committed state, record instrument), declared rather than smuggled in as inherited. Verified: my reimplementation of ω from Definition 9.2's literal two-instrument reading agrees with the code's set-intersection route on every instance tested. |
| 10 | Lean none; no new primitive | **COSMETIC.** As pinned; confirmed — no Lean artifacts, no primitive outside Cycles B, B′, B″ and the three frozen panel reviews. |

**Completeness:** I looked for undeclared deviations and found one candidate,
which I record rather than charge: the reduction sweep (`run_reduction`) and
the separation sweep both construct the declared family as `Pres_L(A(B))`
internally, so clause (a) of Definition 2.2 is satisfied by construction and
is never *tested* against a patch that declares a different family. That is
harmless — (i-b) forces the closure anyway, and the terminal side of the
comparison uses the same construction — but Theorem 3.1 is stated for
arbitrary patches and gated only on closure-family patches. One scope clause
would close it.

---

## 4. NUMBERS TABLE — 30 INDEPENDENT RECOMPUTATIONS

All computed in exact rationals by my own code, importing nothing from the
unit. **Every one matches.**

| # | quantity | paper / receipt | R3 independent | ✓ |
|---|---|---|---|---|
| 1 | record-lattice sizes at 1..5 configurations | 1, 2, 5, 15, 52 | 1, 2, 5, 15, 52 | ✓ |
| 2 | DET, REV cardinalities at five configurations | 3125, 120 | 3125, 120 | ✓ |
| 3 | FUNNEL, FUNNEL-CLOSURE, COUNTER-LAW sizes | 21, 3006, 120 | 21, 3006, 120 | ✓ |
| 4 | ε spectrum over 52 records under DET | {0:1, 1/16:10, 1/8:25, 3/16:15, 1/4:1} | identical | ✓ |
| 5 | the same five spectra at law sizes 21/120/120/3006/3125 | identical | identical | ✓ |
| 6 | closed-form agreement (Thm 4.2) | 260 instances, all agree | 260, all agree | ✓ |
| 7 | \|Pres_DET\| at the four named boundaries | 240, 420, 1280, 120 | 240, 420, 1280, 120 | ✓ |
| 8 | ε at the four named boundaries | 1/16, 1/8, 3/16, 0 | 1/16, 1/8, 3/16, 0 | ✓ |
| 9 | thresholds tried in the separation search | 0, 1/32, 1/16, 3/32, 1/8, 5/32, 3/16, 7/32, 1/4 | identical | ✓ |
| 10 | separating thresholds | **empty** | **empty** | ✓ |
| 11 | ordering inverted (legit > forged 2+2 > forged 2+1+1) | true | true | ✓ |
| 12 | records admitted at τ = 0, 1/16, 3/16 | 1, 11, 51 | 1, 11, 51 | ✓ |
| 13 | forged 2+1+1 admitted at 1/16 and at 3/16 | yes, yes | yes, yes | ✓ |
| 14 | ε-monotonicity sweep | 1790 pairs, 0 violations | **1790**, 0 | ✓ |
| 15 | reduction, committed sweep | 368 instances, 0 disagreements | **368**, 0 | ✓ |
| 16 | reduction, census sweep | 3435 instances, 0 disagreements | **3435**, 0 | ✓ |
| 17 | censused laws; identity-containing; reversible-containing | 687, 259, 259 | 687, 259, 259 | ✓ |
| 18 | laws admitting a proper boundary; id-containing with one; id-free with none; discrete-iff-identity | 428, 0, 0, 687 | 428, 0, 0, 687 | ✓ |
| 19 | admissible pairs; comparable among them | 357, 0 | 357, 0 | ✓ |
| 20 | condition-(i) instances; at proper boundaries; (ii-a) failing | 1004, 745, 0 | 1004, 745, 0 | ✓ |
| 21 | identity-free admissible patches, of them ε = 0 | 745, 745 | 745, 745 | ✓ |
| 22 | the cost tower and its residues | 120/360/1260/3120; 3005/2765/1865/5 | identical | ✓ |
| 23 | graded costs at the record level (Obs_0, Obs_{1/16}) | 120 → 0 | 120 → 0 | ✓ |
| 24 | graded costs at the coarser level {0123\|4} | 1260, 1020, 120, 0 | 1260, 1020, 120, 0 | ✓ |
| 25 | control 1: forged member admissible / member two / δ | true, false, 0 | true, false, 0 | ✓ |
| 26 | control 2 (i-b′): records admissible; family sizes | 52 of 52; 120, 60, 20 | 52; 120, 60, 20 | ✓ |
| 27 | mixed-law: escape reproduced; \|L*\|; member-one family own vs shared | yes; 3125; 1 vs 240 | yes; 3125; 1 vs 240 | ✓ |
| 28 | descent, law-free: forged certified; greatest descends; eraser | 14/15; yes; 51/52 | 14/15; yes; 51/52 | ✓ |
| 29 | descent, law-relative DET: forged; eraser; escape-law partner | 0; 1; 1 | 0; 1; 1 | ✓ |
| 30 | ω separations: W1/W3 and counter-law | 0 vs 2/3; 0 vs 15/16 | **0 vs 2/3; 0 vs 15/16** | ✓ |

**New measurements not in the unit (K3):**

| # | quantity | R3 result |
|---|---|---|
| 31 | ω on the coarse comparison at the committed state/law/preparation | **0, 0, 0** (forged 2+1+1, forged 2+2, legitimate) |
| 32 | ω at the committed preparation over all laws × all records | **0 in 260 of 260** |
| 33 | ω anti-monotonicity under refinement | **0 violations in 4590 instances** |
| 34 | (law, preparation) rows where ω(legit) < both ω(forged) | **15 of 155**; 0 at DET/REV/FUNNEL-CLOSURE |
| 35 | preparations at which the forged 2+1+1 attains ω = 0 under DET | **31 of 31** |

**Anchor fidelity.** I re-derived **18 of the 19** anchors from the committed
definitions — N01–N11 and N13–N19 — and all eighteen match exactly, including
N05's pair (σ = 1 at the carrier algebra's closure, σ = 3/4 once the total
eraser is added to the declared family). N12 (the cost-criterion census
2748/1008/927) I did not re-derive; it is a B″ census fact outside this lens's
remit and it is carried exit-1-only.

**Common gates.** Source SHA-256 in the receipt matches the source file
byte-for-byte (`d0f8ad77…39a43a`). No float literal anywhere in the unit
(independent AST pass: zero). Forbidden vocabulary appears only inside the
scope box and the non-claims, never in a claim. 25 gates, 25 passed; 19
anchors, 19 passed; 8 anchor mutants + 8 derivation mutants declared. Scope
tags are present at every ε claim, and the state-relativity is named at §3.1,
§5.3's companion, non-claim 3 and deviation 2 — that discipline is well kept.
Prose and gates agree everywhere except at F2, F3 and F8.

---

## 5. PER-RUNG CONFIRMATIONS

**(a) `RQ0-L3-EPSILON-BLIND`, including the inverted ordering and the
structural proof — CONFIRMED.** The separating set is empty over all nine
candidate thresholds (reproduced); the ordering 3/16 > 1/8 > 1/16 is
reproduced; the least positive defect in the spectrum is 1/16, attained by
ten two-configuration merges of which the forged 2+1+1 is one (reproduced,
and I verified independently that all ten are two-configuration merges by the
closed form ε = (4 − k)/16, k = the number of atoms not containing the sink).
The structural proof is valid: ε is a function of the quadruple, provenance
is not a component, so no such statistic can read it. Two fixes attach to the
rung: the escalation sentence (F1) and the degenerate exhibit (F6). The
headline itself is untouched by both.

**(b) the ε = 0 reduction, both directions — CONFIRMED.** 368 committed
instances and 3435 census instances, zero disagreements, independently
reproduced at both counts. Both hypotheses reproduce as load-bearing: at the
degenerate sink state the forged boundary's ε is exactly 0 while the axiom
rejects it; the empty family has ε = 0 and ker(∅) = the one-atom boundary.
Proof of Lemma 2.3 checked and correct. One scope clause owed (§3, the
closure-family restriction noted in §3 above).

**(c) the closed form — CONFIRMED.** Theorem 4.2's proof is correct: the
identity's collision partition is discrete, hence refines every boundary, so
id ∈ Pres_L(π) always; and max_s Pr(r,s) ≥ max_{j∈r} ρ_j gives d(F) ≤ d(id).
Verified over 260 instances, and I re-derived the whole spectrum analytically
from the closed form (ε = (4 − k)/16 with block counts 1, 10, 25, 15, 1 summing
to Bell(5) = 52) — an independent confirmation of Theorem 4.1's table that
does not run the code at all. This is the sharpest result in the paper and it
is sound.

**(d) the mixed-law closures and the law-free-descent finding — CONFIRMED**
(§2 above). All descent counts reproduce; the AST verification of
law-freeness passes; the "imports the blockade" adjudication is correct at
both routes and the mechanism (rigidity leaves one admissible boundary) is
verified directly. Fixes: F3 (ungated premise) and F5 (deviation 8).

**(e) ω's separations — CONFIRMED, both, exactly.** W1 vs W3: σ = 1 and δ = 0
for both, ω = 0 against 2/3; I confirmed independently that Pres of the
discrete boundary at the committed three-configuration law is the identity
alone, so Reach({0}) = {0} and two atoms of mass 1/3 go unmet. Counter-law at
the committed carrier: σ = 1, δ = 0 for both, ω = 0 against 15/16; I
confirmed the counter-law is the 120-element monoid of order-decreasing maps,
that its Pres of the carrier algebra is again the identity alone, and that
1/16 + 1/16 + 1/16 + 3/4 = 15/16 is exactly the mass of the four unmet atoms.
Theorem 9.1's structural blindness claim is correct as stated. What must be
added to this rung is §0: ω separates *these* fixtures and does *not*
separate the coarse comparison, and §9.1 currently states the second fact as
a principle without ever measuring it.

**(f) the rung set, including the combined MIXED-LAW-CLOSED +
PLURALISM-PRICED registration — CONFIRMED WITH FIXES.** All five boxed tags
are supported by measurements that reproduce. `RQ0-L3-EPSILON-ADMISSIBILITY`
is correctly registered in its constructive half only.
`RQ0-L3-OCCUPANCY-STATISTIC` is earned. `RQ0-L3-BLOCKED-AT-PROVENANCE` is
earned and is *strengthened* by K3. The combined registration of the two
mixed-law tags is defensible on the declared-scope reading but is
under-declared at deviation 8 and unqualified in the box (F5).

---

## 6. SENTENCES TO REWRITE

1. **§5, final paragraph** — *"It cannot be answered by any statistic on the
   declared data at this scope."* → *"It cannot be answered by any statistic
   on the quadruple: two declarations that present the same quadruple are the
   same argument to every such statistic, whatever their provenance. A
   statistic may still order two **different** declarations — ω does, by
   coarseness — but that ordering tracks the declaration, not its history."*

2. **§10, `RQ0-L3-BLOCKED-AT-PROVENANCE` bullet, last sentence** and the
   parallel sentence in *"The next obstruction, named"* — replace *"no
   statistic on declared data separates a forged chart from a legitimate
   one"* with *"no statistic on the quadruple separates a forged declaration
   from a legitimate declaration of the same patch"*.

3. **§5.3, "Exhibited rather than asserted"** — add the value and the
   limitation: *"…so their defects are identical, both exactly 0. The exhibit
   is at the carrier's own algebra; no committed pair of forged and legitimate
   declarations presenting the same **coarse** partition was available, so the
   equality is exhibited where it can be exhibited, and the structural
   argument carries the rest."*

4. **Theorem 5.1** — add after "the separating set is empty": *"The search is
   over a single tolerance because ω vanishes identically at the committed
   preparation — 260 of 260 instances over every committed law and every
   record — so the diagonal of the tolerance square is the whole square
   here."*

5. **§9.1, "ω does not read provenance"** — replace the assertion with the
   measurement: *"Measured on the comparison ε failed: at the committed
   state, law and preparation the two forged coarse patches and the
   legitimate one carry ω = 0, 0 and 0. ω is anti-monotone under refinement
   (0 violations over 4590 comparable-pair instances), the exact reverse of
   ε's monotonicity, so where it is non-zero it ranks the legitimate coarsest
   patch as the most admissible — but that is a grading of coarseness with the
   sign flipped, not a reading of provenance, and under DET the forged patch
   attains ω = 0 at all 31 declared preparations."*

6. **Gate L3-23's claim string** — delete *"Measured: at the committed carrier
   the forged and the legitimate declarations of the same partition receive
   the same omega"*, or make the gate compute it (F2).

7. **Theorem 8.4 / gate L3-19** — either gate the law-freeness (an AST or
   signature check over the three selector functions) or downgrade *"proved
   rather than sampled"* to *"verified by inspection of the three selector
   functions; the certification count is gated at one run and is invariant
   because no law enters the selector"* (F3).

8. **Appendix A, deviation 8** — rewrite as: *"The pin's condition for
   `RQ0-L3-NOMOLOGICAL-PLURALISM-PRICED` is that **the escape stands**, and it
   is measured false: the escape closes at both routes. What is registered
   instead is that the escape stands **within the declared scope** — one law
   family per context, which is the default — and that neither closure runs on
   committed machinery alone: route (i) needs an uncommitted amalgamation
   hypothesis and route (ii) needs a selector constructed here. Both tags are
   registered on that reading."*

9. **§10, `RQ0-L3-MIXED-LAW-CLOSED` bullet, first line** — add the qualifier
   that appears only in the non-claims: *"occurs at both routes, **neither of
   which runs on committed machinery alone**, each under a stated cost."*

10. **§3.1 or Theorem 3.1's scope line** — add: *"gated over patches whose
    declared family is the closure `Pres_L(A(B))`, which clause (a) forces in
    any case."*

---

## 7. VERDICT

**ACCEPT-WITH-FIXES.**

The unit's central result survives every attack I could mount on it. ε is
built correctly on the terminal cycle's own statistic, reduces exactly in both
directions over 3803 gated instances, is monotone, welds to the cost tower by
an independent route, and fails to separate the forgery — and the failure is
reported first, plainly, at verdict level, with the inversion stated and the
structural reason given. Theorem 4.2 is the sharpest thing in the paper and it
is correct. The mixed-law section's strongest result, the law-freeness of the
terminal descent selector, is true and I confirmed it by a route the unit did
not use. Thirty independent recomputations, eighteen re-derived anchors, zero
numerical discrepancies.

**The K3 answer hardens the escalation rather than softening it.** ω — the
unit's own new instrument, built because the old two were blind — is
identically zero on the comparison ε failed, and identically zero on all 260
committed instances at the committed preparation. The block really is at the
declaration. What K3 adds that the unit should take: ω's anti-monotonicity
(the one structural respect in which it is *not* like ε), and the measurement
that under DET a forger zeroes ω at all 31 preparations, which is the sharpest
single statement of why reading the declared preparation is not reading
provenance.

The fixes are all claim-level and none of them moves a number: three gates
whose sentences outrun their predicates (F2, F3, F8), one over-broad
escalation sentence that this unit's own second statistic falsifies as written
(F1), one one-parameter search reported as exhaustive for a two-parameter form
(F4), one under-declared deviation (F5), and one degenerate exhibit (F6).
Ten sentences to rewrite; two gates to strengthen; one new measurement to
fold into §9.1.

---

*R3, instrument lens. Own exact code, no floats, nothing imported from the
unit. Frozen on delivery.*
