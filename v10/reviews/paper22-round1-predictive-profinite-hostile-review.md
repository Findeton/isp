# Paper 22 round 1 — predictive/profinite hostile review

**Frozen target:** commit `a34b36e346126f7b5533aa4e0aa7bb3419f70ad1`  
**Manuscript:** `relativistic-isp-v10-paper22-the-predictive-record-dag-boundary.md`  
**Comparison base:** terminal D34e note, frozen exact code/output, and all three
round-3 closing reviews  
**Verdict:** **SCIENTIFIC CORE ACCEPTED; SMALL SOURCE REPAIRS REQUIRED — 0
blockers / 0 majors / 2 minors / 1 nit.**

Paper 22 is an accurate synthesis of the terminal D34e result.  The law,
queries, stopping scopes, five generator rows, exact B0/B1 obstructions,
nonexplosive all-future promotion, unbounded-width theorem, fixed-radius
ancestry no-go, component ceiling, strong-versus-weak distinction and finite
profinite ceiling all survive independent checking.  No theorem or branch
verdict needs to be withdrawn.

The nonterminal defects are narrow.  First, the manuscript calls the Branch-F
selector a **D-wire ordinal**, while the receipt actually pins D's **own-ring
ordinal** from the event identifier `D#r...`; those integers differ in the
registered construction once D has a passive birth record on its wire.
Second, the literature list is real and relevant but is never cited in the
body and is incomplete enough that the provenance of “causal state,”
“lumping” and the operational quantum comparison is unclear.  One residual
minimality slogan should also be softened.

## 1. Artifact and receipt reproduction

The frozen manuscript has SHA-256

```text
9cba1e40edfb875ade397bc32331ef0bcf5d91cb0c0a8e149c210e9e20292921.
```

The manuscript's pinned receipt hashes reproduce:

```text
code   e66490560f7c38af746b6fea144a4356dfdb3630205eab9f46723ed8c830bff8
stdout 3d12f6191883ee3790c78498bae4bb1971144765341a354df587d33188f54498
```

A fresh `PYTHONHASHSEED=999983` execution exits zero, is byte-identical to the
committed stdout, prints `13/13`, and reproduces internal digest

```text
a53fa0c18a5905f282cea4c283ec3061c049ad7378a00f624906c1d68091d701.
```

The D34e note at this commit has SHA-256

```text
c2c277ff25ffc91e55e330b9ae26f08f302a7503ed5ff2dd91f2db2eb5ec455d
```

and section 20 records all three closing streams at `0/0/0/0`.  Thus the
paper's claim that the underlying investigation is terminal at its declared
width has the stated provenance.

## 2. Law, query and stopping scopes — pass

The manuscript correctly freezes the chosen D34b exemplar:

```text
per active actor: birth 1/4, total interaction 1/4, idle 1/2;
per eligible degree-d target: interaction 1/(4d).
```

Birth joins only a fresh child to its parent, interactions use existing edges,
idle joins nothing, and no actor seals in this exemplar.  Consequently no law
row joins disconnected components.  The coefficients and grammar are clearly
identified as inputs, not derived SHARD dynamics.

The C, L and F query alphabets match the terminal note.  In particular every
non-silent C/L record carries elapsed time from the conditioning stop, event
kind/direction, post carrier, post A-own count and post A-wire count; L adds the
incident role.  F retains complete durable event ancestry.  The manuscript
does not infer interventions from a passive law.

The fixed-time, A-own hitting-time and A-wire hitting-time scopes are kept
separate from global embedded depth.  The common time-translation gauge and
elapsed-time convention close the old absolute-time seam.  A passive incoming
event increments only the wire counter, exactly as in the generator.

## 3. Generator, probability and all-future promotion — pass

The five printed row families agree term by term with the exact implementation:

```text
A birth                       1/4
A idle                        1/2
A outgoing, aggregated        1/4
degree-k-neighbor birth       n_k/4
degree-k-neighbor into A      n_k/(4k).
```

The counter and carrier updates are correct.  Neighbor births are internal
boundary transitions and emit no A-wire output.  Every other global row leaves
the declared boundary and C/L output unchanged.

The relevant boundary-transition intensity is also correct:

```text
q(c,h) = 1 + d_A/4 + sum_k n_k/(4k) <= 1 + d_A/2.
```

This formula is used only as a boundary rate, not as a false bounded-width
claim.  The load-bearing all-future promotion is the arbitrary-state row
partition plus D34b's Yule nonexplosion/strong-Markov theorem.  Since the
projected counters are monotone state coordinates, their hitting times inherit
the stopped law.  The paper does not mistake the one exponential
next-boundary survival check for the complete next-A-wire distribution.

Typed B3 updates, root/output covariance, disjoint construction swaps and
validated regional composition are accurately summarized.  The conclusion is
sufficiency of the constructed growing B3, not uniqueness or minimality.

## 4. B0 and B1 exact obstructions — pass

### 4.1 B0

When B births a child, A's actor row and tip remain unchanged while B's degree
changes from one to two.  The B-to-A intensity therefore changes exactly

```text
1/4 -> 1/8.
```

This changes the infinitesimal law of A's next wire event, so the proposition
has the advertised scope.

### 4.2 B1

The reachable witnesses are fair even after the repaired durable counters are
included.  Independent projection gives

```text
left  (carrier=0, hist={2,3,6}, own=2, wire=2, A tip=A#r2),
right (carrier=0, hist={2,4,4}, own=2, wire=2, A tip=A#r2).
```

Thus A's carrier, degree, counter baseline and aggregate incoming rate agree.
The exact arithmetic reproduces:

```text
f(H)=f(H')=1/4,
Lf(H)=61/1344,
Lf(H')=11/240,
Delta Lf=1/2240.
```

For the expected incoming count,

```text
E N_in(t) = f t + (Lf)t^2/2 + O(t^3),
```

so the manuscript's order-`t^2` coefficient difference `1/4480` is correct.
The separate finite strong-transition stress test is also correctly scoped:
the pair agrees at internal horizon one and splits at horizon two.

## 5. Strong refinement versus the weak predictive quotient — pass

The registered `111,111,111` census is never called a minimal causal-state
count.  The paper says explicitly that:

- non-silent marks contain the declared post carrier and counters;
- neighbor births are internal, not observable A-wire records;
- the finite object is a strong boundary-transition refinement;
- eliminating arbitrarily many hidden neighbor births is required for the
  canonical weak/timed observed-process quotient;
- that quotient and a bounded alternative remain open.

This matches the terminal predictive/profinite closing review exactly.  The
analytic B3 theorem needs an exact sufficient carrier and does not depend on a
minimal weak quotient.

## 6. Full ancestry and component ceiling — pass, subject to m1 terminology

The complete radius carrier includes the fields required by the terminal
theorem: owned actor rows/tips/counters, endpoint ports, every event touching an
owned wire, crossing records and opaque outside predecessor identifiers.  The
two constructed pasts agree on this object because D lies at distance `r+1`.

The exact positive lower bound is correct.  The path contains `r+3` active
actors, every selected initiator has degree two, and the `r+1` forced embedded
steps have mass

```text
p_r = [1/(8(r+3))]^(r+1).
```

This reproduces `1/24,1/1024,1/64000,1/5308416` at `r=0,1,2,3`.  The paper
correctly uses `p_r` only as a lower bound for the broader ancestry event.  Its
optional `Delta=1` factor is an Erlang completion lower bound, not a total event
probability.  The interaction branch has exact zero because the selected
pre-stop event's immutable kind is already interaction.

The complete component is sufficient because record ancestry and all future
law events stay inside the component.  Disconnected Poisson source families
factor at continuous time and component-local stops.  The manuscript correctly
leaves component necessity and the minimal adaptive Branch-F frontier open.

## 7. Profinite and quantum ceilings — pass

The finite diagram is stated in its only proved order:

```text
(u_3 o r_(4->3))_* mu_4 = (u_3)_* mu_3,
```

where labeled committed-prefix truncation precedes mark forgetting.  No
canonical unmarked `4 -> 3` map is invented.  The paper also refuses a
completed marked-history map, adapted stem-spectrum posterior and screening
factorization.  “Profinite structure hosts compatible finite data; it does not
select the law or boundary” is the correct D34e ceiling.

Likewise, the accepted finite D34c functional is not promoted to a timed,
controlled D34b-D34c process.  Without all-instrument kernels, the quantum
boundary and `d_carrier,d_op,chi_cut` remain undefined.  The outcome table's
two refusals and four classical rows agree with the executable scorecard.

## 8. MINOR findings

### m1 — the receipt pins an own-ring ordinal, not a D-wire ordinal

The manuscript repeatedly describes the Branch-F selector as

```text
(structural D role, D-wire ordinal k).
```

That is not the coordinate consumed by the frozen executable.  The code sets

```text
pre_stop_ordinal = state["actors"][D]["ring"]
selected_id = f"{D}#r{pre_stop_ordinal}".
```

This is D's **own initiated-ring ordinal**, which is embedded in the event ID.
It is not D's ordinal position among every event touching D's wire: passive
events advance the latter but not the former.

An exact reconstruction of the registered witnesses gives:

```text
r=0: selected ID B#r2,       own-ring ordinal 2, wire position 2;
r=1: selected ID B/1#r2,     own-ring ordinal 2, wire position 3;
r=2: selected ID B/1/1#r2,   own-ring ordinal 2, wire position 3;
r=3: selected ID B/1/1/1#r2, own-ring ordinal 2, wire position 3.
```

The theorem itself survives.  In each paired construction both coordinates
select the same immutable event, and all hostile interlopers occur after the
selection.  But the manuscript's code provenance is not exact.

**Required repair:** replace “D-wire ordinal” by “D-owned-ring ordinal” or
“initiator ring ordinal in the immutable event identifier `D#r_k`” throughout.
If a true wire-position selector is intended instead, implement and rerun that
different selector explicitly.  Also replace “already sealed event” in section
7 by “already immutable/persistent event”: section 2 correctly states that the
chosen D34b exemplar has no dynamic sealing.

### m2 — the external references are real but unanchored and incomplete

References 3--5 are legitimate and topic-relevant, but none is cited in the
body.  As written, a reader cannot tell whether they are proof dependencies or
conceptual background.  This matters because the SHARD strong CTMC projection
is proved by the D34e row partition; it is not an application of the finite
discrete-time theorem in reference 4, and the quantum refusal is not a result
derived from reference 5.

**Required repair:** add inline citations at the first discussions of causal/
predictive states, lumpability/strong refinement and operational quantum
memory.  Explicitly label them background rather than sources of the paper's
new theorems.  Complete the entries, for example:

```text
Shalizi & Crutchfield, J. Stat. Phys. 104, 817--879 (2001),
DOI 10.1023/A:1010388907793;

Geiger & Temmel, J. Appl. Probab. 51(4), 1114--1132 (2014),
DOI 10.1239/jap/1421763331;

Pollock et al., Phys. Rev. Lett. 120, 040405 (2018),
DOI 10.1103/PhysRevLett.120.040405.
```

Add the three D34e closing reviews or the terminal note commit `d10ca52` to the
internal provenance, since the manuscript relies on their clean disposition
rather than only on the preregistration/replacement sections of the note.

## 9. NIT

### n1 — two slogans momentarily sound stronger than the minimality ceiling

The abstract says “the behavioral state consists of” B2, and the conclusion
says prediction lives on “the smallest causal boundary.”  The rest of the
manuscript repeatedly and correctly says that the weak/timed quotient, bounded
alternative and minimal physical carrier are open.  No formal theorem actually
claims B2/B3 is smallest, so this is not a scope failure.

For consistency, write “one exact sufficient behavioral state consists of ...”
and recast the last slogan as an objective: “the task is to find the smallest
causal boundary ...; D34e constructs one sufficient boundary.”  The table's
“exactly sufficient” is harmless if “exactly” is understood as nonapproximate,
but “exact sufficient” would avoid the same ambiguity.

## 10. New-opening ledger

| Attack | Disposition |
|---|---|
| Fresh receipt salt and artifact hashes | Pass; byte-identical `13/13`. |
| Generator coefficients/counter marks | Pass exactly. |
| Boundary jump rate and nonexplosion promotion | Pass; no hidden finite-depth promotion. |
| Same B1 state after durable counters are appended | Pass; both witnesses have own/wire `2/2` and the same A tip. |
| `t^2` coefficient `1/4480` | Pass by independent Fraction arithmetic. |
| Strong census presented as weak/minimal | No; paper states the distinction correctly. |
| All-r Branch-F probability | Pass; exact lower bound and zero have the right scopes. |
| Moving-tip/selector provenance | **Terminology mismatch found:** code pins own-ring ordinal, paper says wire ordinal. |
| Finite unmarked map promoted to profinite posterior | No; explicitly refused. |
| Literature existence/relevance | Verified; citation placement and metadata require m2. |

## 11. Exact accepted ceiling

After the two minor source repairs and one wording cleanup, this stream accepts
Paper 22 at the following ceiling:

> For the chosen passive static-adjacency D34b law, B2 is an exact sufficient
> behavioral state for the coarse relative-time A-wire query and the physical
> distributed B3 star is an exact pointwise all-future sufficient, recursively
> updating, covariant and composable growing carrier for C/L at fixed time and
> local count stops.  The constructed B3 is unbounded.  B0 and B1 fail exactly.
> Every complete fixed actor radius fails for full durable ancestry, while the
> whole component is a sufficient but not proved necessary ceiling.  The
> finite strong-transition census is not the weak/timed minimal quotient, the
> finite labeled-truncation diagram is not a v9 posterior theorem, and the
> intrinsic timed quantum boundary remains undefined.

**Final count: 0B / 0M / 2m / 1n.  Theorems accepted; manuscript not yet
terminal-clean pending the listed source repairs.**
