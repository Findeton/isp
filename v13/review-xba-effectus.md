# XBA — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens. **Date:** 2026-08-08.
**Protocol:** `v13/note-xba-hostile-protocol.md` (K1–K5 binding), frozen at
v13 #238. **Object, verified before reading:**

| file | sha256 (12) | verified |
|---|---|---|
| `v13/paper-xba-crossbase.md` | `284a51e88e6f` | yes |
| `v13/code/xba_crossbase_exact.py` | `91677df8bbc7` | yes |
| `v13/code/xba_crossbase_output.txt` | `603a6eab18cf` | yes |
| `v13/code/xba_crossbase_receipt.json` | `1945dbb12eb1` | yes |

The instrument's own four external pins were also verified against the real
files: `note-xba-crossbase-pin.md` `7cbde5da4280`, `nt_transport_receipt.json`
`d256891b479a`, `gen_generality_receipt.json` `e0b2f444f6a9`,
`review-gen-operator.md` `1d17534ef9f4`. All four match.

**Method.** Everything below was rebuilt in
`/private/tmp/.../scratchpad/r2_*.py` from the paper's prose, not from the
delivered instrument: my own graph, my own reduced-walk enumerator, my own
cycle basis and F2 linear algebra, my own quartic-field arithmetic (generic
polynomial reduction modulo $8y^4-8y^2+1$, not the delivery's hand-coded
coefficient formulas), my own rebuilds of both bases, of the third instance,
of the equivariant control, and of ~100 instances that do not appear in the
delivery. I also re-read both terminal receipts' admission tables directly and
recomputed the 24-cell comparison. The delivered script was run once to
completion (`--no-census`) and three mutants were run to completion.

**Recomputation count: ≈450.** Of these, **258 are delivered values**
independently recomputed — every number in §1.1, §1.2, §1.3, §1.4, §2, §3,
§4, §5, §6, §8, §9 and §12 that I could reach, including the 24/24 admission
agreement read from the two receipts themselves. **All 258 agreed at first
attempt. I found no computed-number error anywhere in this unit.** The
remaining ≈190 are new constructions and censuses that the delivery does not
contain; they are what the findings below rest on. The delivered script
reproduces `xba_crossbase_output.txt` byte-identically through §10 on my
machine.

**What that means for what follows.** The arithmetic of this unit is clean.
Every failure I report is a failure of *what the numbers are said to mean* —
of the derivation's premises, of the property's name, and of the steering
defence. Three of them are refutations by explicit construction, not
objections.

---

## Summary of findings

| # | severity | finding |
|---|---|---|
| **F1** | **MAJOR — false step in the load-bearing derivation** | §7.1's `SQ_REAL_1 = D` is false without an un-named fifth premise $D^2=\mathbf 1$; two constructed instances satisfy E0–E4 verbatim on the common graph and carry a **different profile** |
| **F2** | **MAJOR — the verdict's name is refuted by the unit it cites** | GEN's declared species has four clauses; E3 and E4 are not among them; GEN measures the equivariant completion to satisfy **every clause of the species** — so the control's 172/192 *is* a species-compliant base with a different profile |
| **F3** | **MAJOR — the steering defence fails (K4)** | the third instance varies exactly the two parameters that provably cannot move the answer and selects the one that decides it; and by §7.1 it could not have come out otherwise |
| **F4** | MODERATE — false printed lemma | D4's "an involutive defect needs a system dimension of at least three" is refuted by construction; I built a 36-configuration instance with an involutive defect that reproduces 82/86/90/106 |
| **F5** | MODERATE — instrument (K4 mechanism) | the "derivation" is a typed constant equal to the measured answer; C4 is defined as equality with it; the engraved lesson of ledger #24 at the unit's central object |
| **F6** | MODERATE — the honest open is incomplete (K3) | a second input of exactly the admission table's kind is used and not named: both completions' defects are involutive (2.14% of GEN's family) |
| **F7** | MINOR (K3) | §10's closing sentence reads as giving a mechanism for the common *graph* as well as the connection |
| **F8** | MINOR (K5) | §9's "every candidate's subset size identical" is measured on 9 of 12 candidates |
| **F9** | MINOR (K5) | A01, the pin's own hash pin, is the one of four with no mutant |
| **F10** | MINOR (K1) | the pre-registered outcome vocabulary is satisfied by a predicate that names the answer; the object that carries the content is not a connection-space property at all |

**Confirmed, could not be refuted:** the two bases realize one point of the
4,096 at all four readings by both routes; the 96 / 16 / six-relabelling
structure; C1 PARTIAL at 42 with residual 6; C2a's vacuity (real, and
structurally unavoidable on this graph); C2b/C2c refuted at membership; C3
necessary-not-sufficient at 1,728 with 0 violating hits; the whole
necessity/sufficiency table row by row; every declared violator's profile;
the chain 4,096→3,072→768→192→12→6 with all six survivors carrying the
profile; the equivariant control at $D=\mathbf 1$, 2 holonomies, 172/192;
the third instance at 82/86/90/106.

---

## K4 — THE STEERING AUDIT (primary)

### F1 (MAJOR). The four clauses do not force the profile. The derivation has a fifth premise, and it is not named.

§7.1 is the object the paper designates as carrying the result ("What carries
the result is the derivation of §7.1", §11.4). Its third line is

$$\texttt{SQ\_REAL\_1} = \bigl(u^{-1} P u\bigr)\cdot P = D \quad (\mathbf{E4})$$

Write $Y = u^{-1}Pu$ and $D = P u^{-1} P u = PY$. The line asserts $YP = PY$.
With $P^2 = \mathbf 1$ and $Y^2 = \mathbf 1$, the group $\langle P, Y\rangle$
is dihedral, and it is abelian **iff $(PY)^2 = D^2 = \mathbf 1$**. So the step
is valid only under a fifth premise: *the defect is an involution*. That
premise is nowhere in E0–E4, nowhere in §6's chain, not in the abstract's
enumeration, not in §10's verdict sentence, and not in the receipt's `thesis`.
It appears only as an ambient arena declaration (§1.0 "the $4^6$ Klein-four
connections", §11.3) and as one clause of the instrument's
`XBA-SPECIES-CLAUSES-MEASURED`.

**Measured, not argued.** I built an instance in the same H·Q completion
family, same carrier as base 1 (36 configurations, qubit systems, qutrit
pointers), exchange-invariant preparation $\psi = (1/3,2/3,2/3,0)$, completion
permutation $\pi = (1,0,2,3)$, and walked the `SQ_REAL_1` cycle node by node
as an actual closed walk:

| instance | $\mathrm{ord}(D)$ | `SQ_REAL_1` $= D$? | $= D^{2}$? |
|---|---|---|---|
| $\pi=(1,0,3,2)$ | **2** | **yes** | no |
| $\pi=(1,0,2,3)$ | **3** | **no** | **yes** |

The step fails exactly where the premise fails.

**And the consequence is a counterexample to the headline, not a technicality.**
Two instances, both satisfying **E0, E1, E2, E3 and E4 verbatim** — measured,
not asserted: preparation leg common to the two frames, local legs commute,
wing exchange intertwines the local legs, wing exchange does **not** intertwine
the preparation leg — read on the **common declared graph** at a symmetric
setting, by the paper's own gauge-free route (raw matrix product along all 364
based closed walks), i.e. at exactly the scope the paper's own base S and base
S′ are read at:

| instance | carrier | $\mathrm{ord}(D)$ | E1 | E2 | E3 | E4 | distinct holonomies | class counts |
|---|---|---|---|---|---|---|---|---|
| base G's carrier, $\pi = (0,1,2,3,4,5,6,8,7)$ | 81 | 3 | ✓ | ✓ | ✓ | ✓ | **6** | **42 / 46 / 46 / 72 / 78 / 80** |
| base 1's carrier, $\pi = (1,0,2,3)$ | 36 | 3 | ✓ | ✓ | ✓ | ✓ | **6** | **42 / 46 / 46 / 72 / 78 / 80** |

So the abstract's "that point is forced, cycle by cycle, by four clauses both
bases satisfy", §2's E4 row "E4 forces `SQ_REAL_1` $= D$", §10's verdict
sentence and the receipt's `thesis` are **false as stated**. What forces the
point is the four clauses **together with the involutivity of the defect** —
and involutivity is not a species fact, it is a fact about the declared
completion.

**Its rarity is the point, not a footnote.** Recomputed from scratch over the
completion family (the defect permutation is $D = \sigma\pi^{-1}\sigma\pi$,
which I verified against the measured 81×81 defect for two completions):

| family | involutive and non-trivial, $\mathrm{fixed}(D)=45$ |
|---|---|
| all $9! = 362{,}880$ | 4,320 = **1.19%** |
| GEN's $8! = 40{,}320$ | 864 = **2.143%** |
| the 36 single transpositions | **12** (6 give $D=\mathbf 1$; **18** give $\mathrm{ord}(D)=3$) |

The 864/40,320 reproduces GEN's terminal "Klein-four is the fixed(D)=45 class,
≈2.14%" exactly, from an independent construction; and within the same $8!$
family I count **96** completions with $D = \mathbf 1$, reproducing GEN's "the
96 exceptions are exactly the exchange-equivariant locus" and its 99.76%
geometry-bearing figure to the digit. Two GEN terminal numbers recovered from
a rebuild that shares no code with it — which is why I take the census below
to be sound. The order spectrum over all $9!$ is
$\{1{:}288,\,2{:}9504,\,3{:}42048,\,4{:}41472,\,5{:}20736,\,6{:}62208,\,7{:}41472,\,10{:}20736,\,12{:}41472,\,15{:}82944\}$.

**Repair (one pass).** Name the premise **E5 — the defect is an involution**.
It cannot be added to §6's chain, because every element of the 4,096 is an
involution by construction; that is precisely why it must be stated as the
**arena's admission condition** and why the honest chain has one more step at
the front:

> completions (40,320) → **864** ($D$ involutive, $D \neq \mathbf 1$) → the
> Klein-four arena, 4,096 → E0 → 3,072 → E1 → 768 → E2 → 192 → E3 → 12 →
> E4 → 6.

The first cut is the one that does the work of putting the two bases in the
same connection space at all, and it is missing from the paper's table.

### F2 (MAJOR). SPECIES-FORCED-SPLIT is refuted as a name by the terminal unit whose species it invokes.

The protocol asks: *what would a species-compliant base with a different
profile look like, and does the equivariant control's 172/192 prove such bases
exist?* It does — and the corpus already said so.

GEN's terminal paper (`v13/paper-gen-generality-check.md`), §1, declares the
species in terms:

> "**It must be of the same species.** Two wings; a preparation common to both
> frames; local legs on the wings that commute; records at the final division
> event."

XBA's **E1** is GEN's second clause and **E2** is GEN's third. **E3 and E4 are
not clauses of the species.** GEN says so explicitly, twice:

> "The species does **not** select the completion: both completions of §7.2
> are measured to satisfy every clause of it." (§11.7)
>
> "The alternative completion is measured to satisfy **every clause of the
> declared species** — the four clauses of §1 hold on it entry for entry — so
> the choice between them is not a species question. It is a free
> declaration." (GEN **D2**)

And that alternative completion — the bare Householder — has, by GEN's own
terminal measurement, **holonomy group order 1 at every setting**; by XBA's
own §7.3, on XBA's own graph, **172 / 192**. So a species-compliant base with
a different profile does not merely exist; it is printed in this paper's own
§7.3, and mis-described there as one that "satisfies every clause but E4" —
true of XBA's silently enlarged clause set, false of the species XBA is
naming the verdict after.

**E1, E2, E3 are not discriminating facts.** I measured them on 90 constructed
symmetric-setting instances (6 quaternions × 3 exchange-invariant preparations
× 5 completions, including the bare Householder): **90 of 90** satisfy E1 and
E2 and E3. At an asymmetric setting E3 fails, as expected. So three of the four
clauses are consequences of the species *plus the symmetric-setting
declaration* — true by construction of any instance in the arena — and the
fourth, E4 ($D \neq \mathbf 1$), holds at 362,592 of 362,880 completions
(**99.92%**; the equivariant locus is 288). So the discriminating content of
the whole "four clauses" story is: E1–E3 exclude **nothing** in the arena, and
E4 excludes **288 of 362,880** — the equivariant locus, which is the paper's
own control and nothing else. All of the remaining selection sits in
involutivity: a further factor of **38** down to the order-2 defects
(9,504 of 362,592), or **84** down to GEN's $\mathrm{fixed}(D)=45$ class
(4,320 of 362,592). That factor is the one that delivers the Klein-four arena,
and it is not named.

**Is the finding a tautology, then, or contentful?** Contentful — but not the
content claimed. Stated honestly it is: *the class-count profile depends on a
base only through (i) the symmetric-setting species structure and (ii) two
invariants of the declared completion — that its non-equivariance defect is
non-trivial and involutive.* That is a genuine factorisation result: a priori
the profile could have depended on the field, the carrier dimension, the
preparation's Schmidt rank or the measurement rotation, and I verified
directly that it depends on none of them (F3). The tautology charge bites only
on the *name*: "the species forces the split" is false, and "the declaration
forces the split" is right but is **GEN's law, not a new one** (see the
cross-unit section).

**Repair.** Rename the property — `COMPLETION-FORCED-SPLIT`, or
`SPECIES-AND-COMPLETION-FORCED-SPLIT` — and state it as what it is: the
refinement of GEN's completion-selection law from the group's isomorphism type
to the connection's gauge class. Delete "for reasons that have nothing to do
with holonomy" (the reason that does the work is a property of the
completion's defect, which is the holonomy's own generator). Correct §7.3's
"satisfies every clause but E4" to note that E4 is not a species clause and
that GEN measures the control species-compliant.

### F3 (MAJOR). The third-instance prediction does not answer D1.

The paper offers the third instance as the answer to the steering residual
(D1: "the third instance of §7.2 was constructed to satisfy the clauses and
its profile measured afterwards"; §11.4: "What carries the result is … the
third instance"). It cannot carry that weight, for three independent reasons,
each measured.

**(a) Two of its three advertised variations provably cannot move the
outcome.** The abstract sells the instance as "a fresh integer quaternion, a
different preparation vector of Schmidt rank two, a different completion
transposition".

*The preparation is inert.* GEN's adjudicated defect law
$D = (\Sigma V^{\mathsf T}\Sigma V)\otimes I_9$ has the Householder cancelling
identically, so $D$ is independent of $\psi$ for any exchange-invariant $\psi$.
I verified this directly rather than citing it — three different
exchange-invariant preparations (base G's rank-3, base S's rank-2, and a third
of my own), at four different completions:

| completion | $\psi_G$ | $\psi_S$ | $\psi_T$ |
|---|---|---|---|
| $(1,2)$ | fixed 45, ord 2 | fixed 45, ord 2 | fixed 45, ord 2 |
| $(1,5)$ | fixed 45, ord 2 | fixed 45, ord 2 | fixed 45, ord 2 |
| $(0,4)$ | fixed 81, ord 1 | fixed 81, ord 1 | fixed 81, ord 1 |
| $(2,7)$ | fixed 45, ord 2 | fixed 45, ord 2 | fixed 45, ord 2 |

*The quaternion is inert.* Five different integer quaternions at the same
completion give **byte-identical link labels** and identical class counts
82/86/90/106. At a symmetric setting the two local legs are the same operator
on disjoint tensor factors, so they commute and the wing exchange intertwines
them whatever the rotation — the quaternion cannot reach the connection.

**(b) The one variation that decides the outcome had to be selected.** Among
the 36 single transpositions on that carrier: 12 give $\mathrm{ord}(D)=2$ and
reproduce the profile; 6 give $D = \mathbf 1$ (the equivariant locus, 172/192);
**18 give $\mathrm{ord}(D)=3$ and a six-value profile**. (The 6/12/18 split is
computed exactly from the permutation algebra; I then built and measured one
representative of each class end to end — $(1,2)$ and $(1,5)$ → 82/86/90/106,
$(0,4)$ → $D=\mathbf 1$ and 172/192, $(7,8)$ → six holonomies and
42/46/46/72/78/80.) The delivered instance uses $(1,5)$ — one of the 12. Half
the available "different transpositions" would have refuted the delivered
thesis. Calling $(1,5)$ "a **different** transposition" presents a decisive
selection as a free variation.

**(c) The prediction was not risky in any case.** §7.1 is a proof. Any
instance satisfying its premises must reproduce the profile; the third
instance could not have come out otherwise unless the implementation were
wrong. What it genuinely establishes is that the clause set is non-empty
beyond the two bases, and that the implementation is sound. That is worth
having and should be claimed at that strength. It is not evidence that the
clauses were not read off the answer, because a clause set read off the answer
would pass this test identically.

**Steering audit, candidate by candidate** (the protocol's explicit ask):

| candidate | source | reverse-engineerable from the known answer? | forces? |
|---|---|---|---|
| C1 source-split | pin | **no** — pin-declared before the unit | no |
| C2a/b/c equivariance | pin | **no** — pin-declared; the three-way split is *anti*-steering (it reports two membership failures the pin did not have to expose) | no |
| C3 admission pattern | pin | **no** — pin-declared | no |
| C4 species-split (named) | worker | **yes, transparently** — its predicate is literally equality with the realized cycle values | **yes** |
| C5 species-split (naming-closed) | worker | **yes** — C4 with the naming quotiented; its subset is the relabelling orbit of the answer | **yes** |
| C6 common preparation leg | worker | **yes** — the first coordinate of the answer | no |
| C7 commuting local legs | worker | **yes** — the second coordinate | no |
| C8 intertwined local legs | worker | **yes** — the fourth and fifth coordinates | no |
| C9 unintertwined preparation leg | worker | **yes** — the third coordinate, stated as a two-value exclusion | no |
| C10 group of order four | worker | **no** — it is the *prior* unit's offered explanation, adopted and refuted | no |

Every candidate that forces is reverse-engineerable; every candidate that is
not reverse-engineerable fails to force. That is the exact shape the D1
residual predicts, and the third instance does not disturb it.

**The paper's choice to record D1 rather than argue it away.** I endorse the
choice and reject the execution. Recording a residual is right; but D1 then
offers three things "in place of a blindness the instrument cannot provide",
and all three are weaker than advertised: the clause↔species correspondence is
false for E3/E4 (F2), the chain measures cuts inside an arena whose admission
condition is the unrecorded fifth premise (F1), and the third instance is
non-risky (F3c). The honest form of D1 is: *the worker candidates are the
answer's coordinates; what makes them more than a restatement is the
derivation, and the derivation's premises are all independently measurable on
a base without computing any holonomy.* That last clause is true and is the
real defence — it should be stated, and it requires the fifth premise to be
listed among the measurables (it is, in the instrument; it is not, in the
paper).

### F4 (MODERATE). D4 is a false lemma, and it cost the unit a stronger test.

D4 states: "A completion $V = H\cdot Q$ over an exchange-invariant preparation
has a defect of order 1 or 3 whenever the system dimension is two, so an
involutive defect … needs a system dimension of at least three. The third
instance therefore has base G's carrier shape."

At system dimension two the system-pair index has four values and
$\sigma = (1\,2)$; $D = \sigma\pi^{-1}\sigma\pi$ is a product of two
transpositions, which has order 2 whenever the two are **disjoint**. The order
spectrum over $S_4$ is $\{1{:}4,\ 2{:}4,\ 3{:}16\}$ — four permutations give an
involutive defect. D4 is true only within the sub-family of *single
transpositions* (there, at $d=2$, the spectrum is $\{1{:}2,\ 3{:}4\}$), and it
is not stated with that restriction.

I built the instance. Base 1's carrier — 36 configurations, qubit systems,
qutrit pointers — exchange-invariant $\psi = (1/3,2/3,2/3,0)$,
$\pi = (1,0,3,2)$:

| measured | value |
|---|---|
| $D$ order / fixed configurations | **2** / 0 of 36 |
| E1 / E2 / E3 / E4 | ✓ / ✓ / ✓ / ✓ |
| the 13 gauge-fixed labels | identical to the delivered connection |
| distinct holonomies over the 364 walks | **4** |
| class counts | **82 / 86 / 90 / 106** |

So a third instance sharing *base 1's* carrier shape — a genuinely different
system dimension, a different arithmetic, a different pointer geometry — was
available and would have been a strictly stronger test than the one delivered.
D4's "It is a third instance of the species, not a third species" is a real
limitation that the false lemma presents as forced.

### F5 (MODERATE). The derivation is a typed constant.

`derive_from_species` returns

```python
val = {"SQ_FULL_1": 0, "CANON": 0, "SQ_REAL_1": 2, "SQ_REAL_2": 0,
       "SQ_REAL_3": 0, "BIGON_0": 1}
```

— that is, $(\mathbf 1, \mathbf 1, D, \mathbf 1, \mathbf 1, W)$, the measured
answer, typed. The algebra lives only in the docstring. C4's predicate is
`beta(p) == derive_from_species(BKEYS)`, so the candidate the positive verdict
rests on is *defined* as equality with that constant, and
`XBA-DERIVATION-MATCHES-THE-BASES` compares a typed answer against a measured
one. `species-lax` flips one entry of the same dict: it measures that the
constant matters, not that a derivation happened. The abstract's "The
connection is **derived** symbolically from the four clauses" is not what the
instrument does.

This is ledger #24's engraved lesson ("counts computed, never typed") landing
on the unit's central object, and it is the precise mechanism by which the D1
residual could operate undetected — there is nothing in the instrument that
distinguishes a constant typed from a derivation from one typed from the
measurement.

**Repair, and it is cheap.** Evaluate the six cycle words in an abstract group
presented by the clauses — generators $u, a, b, P$, relations $P^2 = 1$,
$PaP = b$, $PbP = a$, $ab = ba$, $D := Pu^{-1}Pu$, and the involutivity
premise **stated as a relation**. Then the derivation is computed, the
`species-lax` mutant kills a real inference, and — decisively — the abstract
computation *cannot* return `SQ_REAL_1 = D` unless the fifth premise is
supplied, so F1 becomes impossible to omit. A derivation that cannot be run
without naming its premises is the whole point of running it.

---

## K3 — THE HONEST OPEN

### F6 (MODERATE). The residual-open list is incomplete by one item of exactly the same kind.

§11.2, the abstract's "What is *not* explained is stated as plainly", and the
receipt's `residual_open` all name **one** input: the 24-cell admission
agreement. There is a second, and it is load-bearing in the same way:

> **both bases' completions have non-trivial involutive defects** — which is
> what puts them in the same 4,096-element connection space at all.

It is 864 of GEN's 40,320 completions (2.14%), and the two bases arrive there
by unrelated routes: base 1's involutivity comes from the singlet completion
(its defect is NT's qubit-only wing swap, an involution by construction), base
G's from a transposition drawn from 12 of 36. Two independent reasons for one
coincidence is exactly what makes a coincidence an open question rather than a
consequence. §11.3 mentions the other defect orders, but as an *arena scope*
statement ("Connections valued in a larger group are outside this arena
entirely"), which frames a substantive unexplained agreement as a bookkeeping
boundary.

**Repair.** Add it to §11.2, to the abstract's "not explained" sentence, and
to the receipt's `residual_open`, with the 864/40,320 figure. The unit then
closes one open and leaves **two** — which is a better result than it looks,
because the second open is sharp, quantified and posable, where the admission
one is not.

### A calibration note on the 24/24 agreement (not a finding)

I re-read both terminal receipts' admission tables directly and confirm
24 cells compared, 24 agreeing, and that the graph the paper builds from them
is right (FULL drawn at $t \in \{0,1,3\}$, REAL at $t \in \{0,1,2,3\}$). But
the 24 cells take only **four distinct values** between them —
$(\text{FULL: identity},\ \text{REAL: —}) \times 12$;
$(—,\ —) \times 4$;
$(\text{identity},\ \text{wing exchange}) \times 6$;
$(—,\ \text{wing exchange}) \times 2$ — because wherever either rule draws at
all, FULL always draws the identity and REAL always draws the wing exchange.
The permutation coordinate is constant across the whole table; the agreement
is an agreement of two admission *masks*, not of 24 independent draws from a
rich space. §1.1's "cells where the two bases draw the same rule **and the
same permutation**: 24" is therefore a weaker statement than its phrasing
suggests. This cuts in the unit's favour on the residual open — the surviving
question is far more tractable than "why do 24 coincidences hold?" — but the
phrasing should be calibrated, and the constancy of the permutation coordinate
should be printed, because it is itself a clue to the open's answer.

### Hunt for sentences overclaiming the graph commonality as explained

I read every occurrence of "explain", "close", "answer", "force", "confirm"
and "coincidence" in the paper. The scoping is honest in the abstract
(line 77), §11.2 and D5/D6. **One sentence is loose (F7, MINOR):**

> §10: "What the frozen review called 'the same gauge class of connection on
> the same graph' is confirmed, and given its mechanism."

A mechanism is given for the connection; none is given for the graph, and the
quoted phrase covers both. One-word fix: "…is confirmed, and the connection
half of it is given its mechanism."

I found no other sentence claiming the graph commonality as explained. §11.2's
"this unit closes the class-count one" I judge defensible for the two
delivered bases *after* the F1/F2 repairs, and not before, because as written
it attributes the closure to the species.

### C2a's vacuity and its missing violator — legitimate

C2a is satisfied by all 4,096 because the rule-preserving automorphism group
has order 2, is generated by the frame swap, and acts trivially on the cycle
space. I recomputed all four numbers independently: $|\mathrm{Aut}|$
rule-preserving **2** with **1** induced cycle action; the bare multigraph
**16** with **8**. The vacuity is structural and unavoidable on this graph:
each doubled rung carries one FULL and one REAL link, so no rule-preserving
map can move them, so no non-trivial cycle action can exist and no violator
can exist. The paper measures it, reports it twice (§5, §8), and names the
control gap in D7. **This is the correct handling of a vacuous candidate and
I have no repair to propose.** It is also, incidentally, the only place in the
paper where a pin candidate is reported in a way that makes the pin look worse
than it had to — which counts in the unit's favour on the steering audit.

### F8 (MINOR). "Every candidate's subset size identical" is 9 of 12.

`tree_flip_test` calls `declare_candidates` with empty automorphism-action
lists and then excludes every `C2*` row from the comparison
(`if not n.startswith("C2")`). The receipt shows 12 first-tree sizes against 9
second-tree sizes, and `subsets_identical: True` is computed over the 9. §9's
sentence should say so, or the automorphism actions should be recomputed on
the second tree (cheap — the flip only changes the cotree basis).

### F9 (MINOR). One hash pin has no falsifier.

Three mutants cover the NT, GEN and review pins. A01, the pin file's own
sha256, has none — §12's "Four hash-pin the frozen sources" and the protocol's
"THREE hash pins" disagree by exactly that one. I confirmed `anchor-nt-hash`
exits 1. Add a fourth mutant or disclose the gap.

### F10 (MINOR, K1 boundary). The pre-registration is satisfied by a predicate that names the answer.

The pin's `XBA-SHARED-STRUCTURE-IDENTIFIED` asks for "a declared property both
realized connections satisfy, whose satisfaction FORCES the profile
(exhaustive over the connection space)". Only C4 (subset 1) and C5 (subset 6)
qualify, and as *properties of connections* they are the answer written as a
predicate. The object that actually carries this unit's content — the
implication *species facts (+E5) ⟹ that orbit* — is not a property of
connections at all, so the pin's vocabulary cannot grade it. The paper owns
the triviality honestly (D2, §11.4, §5) and does not trade on it rhetorically;
but it still enters the positive pre-registered outcome on it. My reading: on
the pin's own candidates the honest outcome is **XBA-PARTIAL** (C1 shrinks
97.5× with 6 of 42; C3 shrinks 2.37× and is necessary), with the derivation
reported as a separately named theorem-level result that the pin's outcome
vocabulary did not anticipate. The verdict as delivered satisfies the letter
and not the intent.

---

## K1, K2, K5 (lower depth, as the protocol directs)

**K1 — the chain.** Recomputed with my own predicates on my own cycle basis:
4,096 → **3,072** → **768** → **192** → **12** → **6**, with profile hits
96 / 96 / 24 / 12 / 6 / 6. All six survivors carry 82/86/90/106; they are
exactly the relabelling orbit of the realized connection (verified as a set
identity, not by counting); and the 96 multiset hits are exactly the 6
relabellings of the 16 element-wise hits (also verified as a set identity).
C4's subset-size-1 forcing is honestly scoped at §5, §11.4 and D2 — the
scoping is carried everywhere I looked. **K1 passes**, with the caveat that
the chain runs inside an arena whose admission condition is F1's missing
premise.

**K2 — the prediction.** Attacked via D4/D5/D6 above. D5 (the third instance
tests labels on a declared graph, admission table not recomputed) is honestly
stated and I hold the paper to no more, since my own counterexamples are read
at the same scope. D4 is false (F4). D6 is honest. **The sharper predictive
test the protocol asks me to construct, if one exists within budget, is the
36-transposition sweep**: the derivation with E5 restored predicts *which* 12
of the 36 reproduce the profile, which 6 give 172/192, and which 18 give a
six-value profile — 36 pre-registered binary predictions instead of one
non-risky instance. I verified the order spectrum $\{1{:}6,\,2{:}12,\,3{:}18\}$
and measured one representative of each class. That sweep is the unit's real
prediction and it costs an afternoon.

**K5 — instrument.** At the depth the protocol assigns me: the four hash pins
verify against real files; I ran three mutants to completion and all three die
(`anchor-nt-hash` exit 1, `species-lax` exit 1, `freeze-lax` exit 1); the
delivered script reproduces its frozen output byte-identically through §10
(diff over all 147 lines up to the census section); the receipt
carries 28 gates (24 must-pass, 4 disclosures), 36 anchors, 35/35 mutants
dead, `never_falsified` EMPTY at denominator 23 with both denominators printed
and the four waiver-only gates named. The cache gating is real as described
(the sweep's lookups are counted and refused; the priming pass is measured to
return its values). I did not attempt the full 35-mutant census — that is R3's
lens. My instrument findings are F5, F8, F9.

---

## Cross-unit consistency: do the three declaration→structure laws compose?

They compose — into **one** statement, and XBA's headline attributes it to the
wrong declaration.

- **GEN:** the completion selects the holonomy group's isomorphism type (the
  dihedral family, orders 2–30; Klein-four is the fixed(D)=45 class, 2.14%).
- **COC:** closure ⟺ the chart-generating group **centralises** the level-1
  holonomy (abelian → forced closure; the extension's non-abelian 8-group,
  4/8 centralise → 32,256 escapes).
- **XBA:** the connection's cycle values are $(\mathbf 1,\mathbf 1,D,\mathbf 1,\mathbf 1,W)$.

Read at the level of the operators, XBA's clauses **are** centraliser
conditions, and its defect **is** a commutator: with $P^2 = \mathbf 1$,

$$D \;=\; P u^{-1} P u \;=\; [P, u].$$

E1/E2 say the two frames' legs agree up to a commutation; E3 says $P$
normalises the local-leg pair, so the loops around the local legs close; E4
says $P$ fails to centralise the preparation leg, and *that failure is the
holonomy*. This is COC's criterion with the chart-generating group replaced by
$\langle P\rangle$ and the level-1 holonomy by the legs: where the declared
symmetry centralises, the loop closes; where it does not, the commutator is the
curvature. And the *order* of that commutator — which decides whether the
connection is Klein-four-valued at all, and hence which profile — is an
invariant of the declared completion, which is GEN's law.

**One statement covering all three:**

> A declared symmetry's centraliser decides the geometry. Where the declared
> exchange centralises a declared leg, the loop around that leg closes (XBA
> E1–E3; COC's abelian → forced closure). Where it fails to centralise, the
> commutator **is** the holonomy (XBA E4, $D = [P,u]$; COC's non-abelian →
> escapes). And the order of that commutator — a property of the declared
> completion, not of the species — selects the group, hence the profile (GEN's
> completion-selection; XBA's unnamed E5).

XBA is therefore **not a third law**. It is GEN's completion-selection law
refined from the isomorphism type to the gauge class, expressed in COC's
centraliser vocabulary. Stating it that way costs the unit its claim to a new
declaration→structure law and gains it something better: the three units
become one theorem with three witnesses. I recommend the repair take that
form.

One consistency check the unit fails on its own terms: §11.10 says "this unit
adds that their *values* are forced by declared **species** clauses too, which
sharpens that reading rather than softening it." GEN's adjudication established
that both curvature sources are declaration-side and that $D$ is *manufactured
by the declared transposition alone*. §11.10 relocates the forcing declaration
from the completion to the species — the same misattribution as F2, and it
contradicts the terminal unit it cites as agreeing with it.

---

## Repair order I would put to the adjudicator

1. **X-1 THE FIFTH PREMISE.** Name E5 (the defect is an involution) in the
   abstract, §2's clause table, §7.1's derivation, §10 and the receipt's
   `thesis`; state it as the arena's admission condition; prepend the
   864/40,320 cut to §6's chain; correct §2's E4 row (E4 alone does not force
   `SQ_REAL_1` $= D$, and the counterexample is measurable).
2. **X-2 THE NAME.** Rename the property to `COMPLETION-FORCED-SPLIT` (or
   `SPECIES-AND-COMPLETION-FORCED-SPLIT`); correct §7.3 and D6 to record that
   GEN measures the equivariant control **species-compliant**; fix §11.10.
3. **X-3 THE PREDICTION AT ITS TRUE STRENGTH.** State that the third instance
   varies two inert parameters and one selected one; give the 36-transposition
   sweep as the unit's actual predictive test (12/6/18, predicted class by
   class); delete D4 or restrict it to single transpositions, and record that
   a 36-configuration instance with an involutive defect exists and reproduces
   the profile.
4. **X-4 THE DERIVATION COMPUTED.** Replace the typed tuple with an abstract
   group computation from the stated relations; `species-lax` then kills an
   inference rather than a constant.
5. **X-5 THE SECOND OPEN.** Add the involutivity coincidence to §11.2, the
   abstract and `residual_open`.
6. **X-6 HYGIENE.** §9's flip-test coverage (9 of 12); a mutant for A01;
   §10's closing sentence.
7. **X-7 THE UNIFICATION.** State the centraliser reading and its relation to
   COC and GEN; drop the implicit claim to a third independent law.

---

## Grade

The census is exact, the rebuilds are honest, and I found **zero
computed-number errors in 258 independently recomputed delivered values**.
But the paper's designated carrier — the §7.1 derivation — contains a step
that is false without an unnamed premise; the headline thesis ("four clauses
force the point") is refuted by two constructed instances that satisfy all
four and carry a different profile; the verdict's property name is
contradicted in terms by the terminal unit whose species it invokes; D4 is a
false printed lemma, refuted by an instance I built that reproduces the
profile at the carrier D4 says cannot support it; and the answer offered to
the unit's own steering residual does not answer it. These are not scoping
quibbles: three of the five are refutations by construction, at the same scope
the paper reads its own third instance and its own control.

The repaired result is real, reachable in one pass, and better than the
delivered one — it welds this unit to GEN and COC instead of standing beside
them. But it is not the result that was delivered.

# **REJECT** — as delivered; mandatory re-derivation on X-1 … X-7.
