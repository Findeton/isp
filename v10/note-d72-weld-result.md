# D72 — result: **the weld is not made, and it fails at the holonomy leg, not at the identification leg.** The two reversals *do* admit a common carrier and coincide exactly on the F-PAIR fixture — but on that carrier `A_D` is **identically zero**, and `√q`-transport around **every** delete-then-insert round trip of the record deletion graph returns **exactly 1**, on 758 independent cycles of one grammar and 1,069 more of a second. **Falsifier F2 FIRES.** The generated line is flat; there is no holonomy for the phase to be. `L_dual`'s dual-conjugation error transfers at exactly `0` — and the receipt then shows that `0` is an identity of the ansatz, reproduced by adversarial integers drawn from nowhere, and that v7's own `1.82` control is exactly `2·e^{−3/32}`, a closed-form constant of the same ansatz rather than a measurement of its record universe.

**Status: GREEN-UNREVIEWED, 2026-07-27.** First delivery. No independent
hostile round has been run against this unit. Nothing here is
review-hardened and nothing here may be cited as such.

Pin `v10/note-d72-weld-pin.md` (STRICT, frozen and committed before any
code was written). Parents: D71b
(`note-d71b-holonomy-phase-identity.md`, the identity in two unwelded
halves), D71 (`note-d71-phase-archaeology.md`, the reduction points and
the empty slots). Receipt `v10/code/d72_weld_exact.py`, output
`v10/data/d72_weld_exact.out` — run from the repository root, **exit 0**,
**50 PASS / 0 FAIL**, 343 s wall clock (of which 296 s is anchor A2's
re-derivation of v7's `N = 9` record universe). Byte-identical output at
`PYTHONHASHSEED ∈ {1, 3, 7, 99, 12345}` apart from the echoed seed.

Every number below is quoted from the receipt's own stdout. **Where the
receipt and this note disagree, the receipt is authoritative** (LOG
#477's standing rule).

---

## 0. The one-paragraph answer

P1 asked whether v7 paper 30's odd channel is the reversal-odd channel of
a probability-transport holonomy. The unit built the common carrier the
pin's own honesty clause said was the hard part, ran all three of the
pin's tests exactly, and gated all four pre-registered falsifiers. **The
identification leg survives and the holonomy leg dies.** The order-dual
`*` and the transport reversal `AB → BA` *do* have a canonical common
carrier — the linear extensions of a record, on which `*` acts by
sequence reversal (gated, exact, on every history of the family) — and on
2-event histories, which is exactly the F-PAIR fixture the pin names,
the two operations are **literally the same partial map**. So "is `A_D`
odd under `*`?" answers **yes**. It answers yes because `A_D` is
**identically zero**: every one of the 2,227 closed exchange squares of
the generated line at depth ≤ 5 has `dP_AB/dP_BA` **exactly** `1` as a
Fraction, so the oddness test reads `0 = −0`. The closure test then
generalises that from squares to the whole loop space: the `√q`
connection **descends** from sequences to records (every up-edge of the
record deletion graph carries a single step weight, 2,322/2,322), and its
holonomy is **exactly 1 on every one of the 758 independent cycles** —
with a negative control confirming the detector fires when one weight is
tampered. Two grammars, three arms, same answer. **F2 fires**, which the
pin pre-registered as a publishable negative: the generated line has no
holonomy of any kind, so D71 Clause 3's `+1` in the phase slot is
**forced at the measured window**, not chosen.

---

## 1. What each test returned

### T1 — the reversal test

| gate | result |
|---|---|
| T1.0 operationalisation fidelity | our exact-Fraction `dP_AB/dP_BA` agrees with v6's own `rn_action(exchange_laws(·))` atom by atom, gap `2.2e-16` (v6's float) |
| T1.1 `A_D` content | **2,227 closed squares, ratio multiset `{1: 2227}`** — `A_D ≡ 0` |
| T1.2 half-open squares | **none** (`AB-only = 0`, `BA-only = 0`, `both-blocked = 610`) — so no `±∞` support defect either |
| T1.3 CARRIER A well-founded | `rev : LinExt(P) → LinExt(P*)` is a bijection on **all 6,464** histories of depth 2..5 |
| T1.4 the coincidence | on the **32** 2-event histories (`= d42b4`'s 32) `*_seq` and `AB→BA` are the same partial map, term by term; 28 have an admissible reverse |
| T1.5 the divergence | on **2,214** closed squares with `|h| ≥ 1` the two maps agree on **0**; 578 of those have an admissible `*_seq` image |
| T1.6 oddness under `AB→BA` | exact inverse on all 2,227 squares — v6:2636's `gap=2.2e-16` reproduced at gap **exactly 0** |
| T1.7 oddness under `*` | **YES, vacuously**: `0 = −0` |
| T1.8 CARRIER B | `mu` constant on all **1,565** record classes, so `A_D` descends to records — as the zero function |
| T1.9 CARRIER C | **294** records have an in-family labelled order-dual, **1,264** do not — `*` is a *partial map* on v10's objects |

### T2 — the closure test

| gate | result |
|---|---|
| T2.1 the connection descends | 2,322 up-edges, **0 multi-valued** |
| T2.2 round-trip closure | **758 independent cycles** (`E − V + C`), **0** with holonomy `≠ 1`, holonomy value set `{1}` |
| T2.3 explicit delete-then-insert round trips | **1,355** record-closing exchange loops, all holonomy `1`; `2·log Hol_√q = A_D = 0` |
| T2.NC negative control | tampering each of twenty stable-ordered up-edges by `3/2`, one at a time, produces a non-trivial holonomy in **20/20** cases, defect counts `[136, 200, 42, 42, 10, 10, 145, 105, 30, 30, 12, 12, 62, 43, 11, 11, 41, 41, 3, 7]`, values `{2/3, 3/2}` — the detector is not blind |
| T2.4 `U(1)` content | holonomy group is the **trivial group** — neither `R+` nor `U(1)` is realised |
| T2.5 second grammar (d42b1) | `(A,B)` depth ≤ 4: 424 cycles, 0 defects. `(A,B,C)` depth ≤ 3: 645 cycles, 0 defects |

### T3 — the `L_dual` re-run

The port, stated before it was run: v7's `F` ranges over **five-record
types** = isomorphism types of induced 5-element sub-posets of a
2-dimensional poset on `N = 9` points, and `F*` is that type with every
order relation reversed (`paper30:2506-2511`, quoted verbatim in the
receipt's registry). v10's records carry at most `DEPTH` events, so `k =
5` does not exist here; the faithful analogue is the isomorphism type of
an induced **k-element** sub-poset of the record's own causal order
`event_poset(h)`, dualised by v7's own `opposite_bits` transcribed to `k`
points. `k ∈ {2,3,4}` are all run and printed.

| gate | result |
|---|---|
| T3.·.a | `*` fixes `E` and negates `O` on every record, every `k`, every reading — the port satisfies its own definition |
| T3.·.A / .B | the float port agrees with the **exact closed form** `2·e^{−κE}·|sin(θE)|` at `|float − exact| = 0.000e+00` in every one of the twelve `(k, reading, domain)` cells; `L_dual` error `0` throughout |
| T3.A | the odd channel is **not** identically zero on v10's objects — at `k = 3` the family realises a non-self-dual order type |
| T3.B1 | **the depth-4 headline was wrong and this gate caught it**: at record depth 3 and 4 the fork type `V` does **not occur at all**; at depth 5 it does (fork:merge = `216:1592`). The type-level one-sidedness is a window artifact |
| T3.B2 | what survives: `O` is **sign-definite on every record**, spectrum `{0: 1063, −1: 8, −2: 80, −3: 160, −4: 224}` — merges always outnumber forks *inside* a record, so `O` never changes sign |
| T3.CTRL | adversarial `(E,O)` integers drawn from nowhere give `L_dual` error `0` and `L_naive` error `1.821021` — **the `0` is an identity of the ansatz, not a fact about v10** |
| T3.C | on the **odd-orbit** reading restricted to the v10-closed domain (275 records) the even channel is identically `0`, so `L_naive` also scores `0` and there is nothing to discriminate |
| T3.D | on the **all-orbits** reading the discrimination *does* reappear on the same domain (`E ∈ {2,8,20}`, `L_naive = 1.627111`, `L_dual = 0`) — the reading, not the substrate, decides which way this looks |

---

## 2. The falsifier board

| falsifier | verdict |
|---|---|
| **F1** `A_D` not odd under `*` at the fixture | **does not fire as written; fires in its spirit.** `A_D` *is* odd under `*` — as `0 = −0`. The two reversals are the same map only on 2-event histories (T1.4) and different maps everywhere else (T1.5), and `*` is not an operation on v10's records at all (T1.9). Clause 3's bridge is **not** established. |
| **F2** `√q` round trip identically `1` | **FIRES.** Every up-edge single-valued; every one of 758 + 424 + 645 independent cycles has holonomy exactly `1`; every exchange square exactly `1`; negative control confirms the detector. |
| **F3** `L_dual` error non-zero on v10's channels | **does not fire.** The error is exactly `0` at `k = 2,3,4`, both domains, both readings — and T3.CTRL plus anchor A2c show that means nothing about the substrate. |
| **F4** defect exists but is not `U(1)`-valued | **not reached, vacuously.** F2 removes its premise. The holonomy group is `{1}`, so "R+ or U(1)?" has no subject. The founding slogan is refuted on this substrate one step *earlier* than F4 anticipated. |

---

## 3. Anchors

| anchor | result |
|---|---|
| **A1** v6 paper 4 §34's antisymmetry row (`v6 p4:2636`, `gap=2.2e-16`) | reproduces at `2.220e-16`; eventless loop rms `0.0e+00` (`:2637`) |
| **A2** v7 paper 30's dual-conjugation numbers at `N = 9` | reproduces: naive `1.8210207227600682556870097725525` (`p30:2838`), `L_dual` `0` (`p30:2851`), on the full 131,526-record universe |
| **A2b** v7's own `*` is an involution on its own universe (`N = 7`) | holds on all 1,956 records |
| **A2c** the closed form reaches the same constant with no `N = 9` run | `2·exp(−3/32) = 1.8210207227600682556870097725525`, and `E = 3` is the argmax of `2e^{−E/32}|sin(πE/6)|` over `E ∈ 0..399` |
| **A3** the F-PAIR fixture reproduces d42b4's anchors | 32 depth-2 sequences, `Z_seq = 4`, `Z_class = 3`, one `mu` per class |

---

## 4. The findings the pin did not pre-register

**(a) v7's `1.82` is a constant of the ansatz, not a measurement.** The
dual-conjugation error of v7's two modes has an exact closed form:
with `* : E → E`, `O → −O` and `ρ = e^{iθ}`,

```
  | L_dual(R*)  − conj L_dual(R)  |  =  0
  | L_naive(R*) − conj L_naive(R) |  =  2 e^{−κE} |sin(θ E)|
```

because `L_naive(R*) − conj L_naive(R) = e^{−κE} ρ^{−O} (ρ^{−E} − ρ^{E})`.
At v7's own `κ = 1/32` and `θ = π/6` this is maximised over integer `E`
at `E = 3`, giving `2·e^{−3/32} = 1.8210207227600682556870097725525` —
**every published digit of `paper30:2838`**. So the campaign's headline
contrast "`0` versus `1.82`" says: the dual form is conjugation-symmetric
by construction, and the naive form is not, by construction; the only
information the `1.82` carries about the `N = 9` record universe is that
**some record has `E = 3`**. This does not weaken paper 30's conclusion —
its conclusion was about *where the phase can sit*, and that is exactly
what an algebraic identity should decide — but it does mean the receipt
is not evidence about records, and D71b Clause 2's reading of it as "the
strongest single piece of bridge evidence in the corpus" should be
downgraded to what it is: a correct algebraic observation about the
transformation law. `[EXACT]`.

**(b) The v10 phase slot's `+1` is forced, not chosen.** D71 Clause 3 and
D71 §4.2 both record that D42b4's `∏√q` has "the phase slot filled with
`+1` without an argument". The argument exists and is F2: on the
generated line the `√q` connection **descends to records** and its
holonomy group is trivial, so no other section of the phase bundle is
reachable by transport. At the measured window (two grammars, three arms,
1,827 independent cycles in total) the `+1` is a **theorem**, not a
convention. `[MEASURED]` on the window; the depth-independent argument is
**not** given here and is the unit's sharpest residue.

**(c) The two reversals have a common carrier, and it is one-dimensional.**
D71b §3.4 flagged as `[SILENT]` whether v7's order-relation reversal and
v6's transport-order reversal are the same operation. They are — on
exactly one fixture. The order-dual of a poset induces on its linear
extensions the map "reverse the sequence" (T1.3, gated on every history),
and on a 2-event history that *is* the transposition `AB → BA`. For every
larger history the induced map reverses the whole sequence while the
transport reversal transposes the top two, and they agree on **zero** of
the 2,214 closed squares with a non-empty base. The bridge is real, and
it is exactly one fixture wide.

**(d) The order-dual is not an operation on v10's records.** 1,264 of
1,558 record classes have no in-family labelled order-dual (T1.9). v7's
universe is dual-closed for free — the order-dual of a permutation poset
is a permutation poset — and v10's is not, because admissibility is
directional (an arbitration cannot precede the proposals it consumes).
Any future attempt to run a `*`-based construction on the generated line
must either restrict to the 294-record closed sub-family or adjoin
out-of-family duals as abstract posets. Both are done here and both are
reported.

**(e) A correction to this unit's own first reading, caught by its own
gate — and a second one, caught by the determinism probe.** At depth ≤ 4 the fork type `V` does not occur in the generated
line at all, and the first draft of T3.B claimed that as a structural
fact ("merges, never forks"). At depth 5 forks appear (216 against 1,592
merges) and the gate **failed**, which is what a gate is for. What
survives the widening is weaker and measured: `O` is **sign-definite on
every record** — merges outnumber forks *within* each record at every
depth measured — so the odd coordinate never changes sign inside the
family, which is a different and softer obstruction than type-level
absence. `[MEASURED]`, depth ≤ 5.

The second correction: the negative control's first version selected the
edge to tamper with `sorted(..., key=repr)`, and the record classes are
nested **frozensets**, whose `repr` depends on insertion order and
therefore on `PYTHONHASHSEED`. Two runs of the same code reported `130`
and `61` defects. The *verdicts* never moved — the holonomy census itself
is order-independent and D2 gates that — but a *reported number* did. The
receipt now sorts class-keyed collections with a recursive
hash-order-independent `stable_key`, tampers twenty edges rather than
stopping at the first hit, and gates the hit pattern under a reversed
spanning-forest build (D4). Full output is byte-identical at
`PYTHONHASHSEED ∈ {1, 3, 7, 99, 12345}` apart from the echoed seed.
**Recorded because `repr` on a `frozenset` is a standing trap for any
v10 receipt that keys on `canon(h)`.**

---

## 5. Licensed claims — no wider than the fixtures run

1. On the d42b3 placement grammar with actors `(A,B)` at depth ≤ 5, and
   on the d42b1 transport grammar at `(A,B)` depth ≤ 4 and `(A,B,C)`
   depth ≤ 3, **every closed exchange square has `dP_AB/dP_BA` exactly
   `1`, every up-edge of the record deletion graph carries a single step
   weight, and every independent cycle of that graph has `√q`-transport
   holonomy exactly `1`.** `[MEASURED]` on those windows, exact
   arithmetic. Not claimed at any greater depth, at any other actor pool,
   or for any other grammar.
2. **The order-dual `*` and the transport reversal `AB → BA` coincide, as
   partial maps, on 2-event histories, and on nothing larger.**
   `[EXACT]` on the enumerated family.
3. **`A_D` is odd under the order-dual on the common carrier** — and this
   is true only in the degenerate sense `0 = −0`. `[EXACT]`.
4. **`L_dual`'s dual-conjugation error is `0` on v10's ported even/odd
   channels** at `k = 2,3,4`, both orbit readings, both domains — and
   this is an identity of the ansatz, demonstrated by the adversarial
   control. `[EXACT]`.
5. **`2·e^{−3/32}` equals `paper30:2838`'s published constant to all 32
   published significant digits, and `E = 3` is the argmax of the closed
   form.** `[EXACT]`.
6. **Not claimed:** that the generated line is flat at all depths; that
   `A_D ≡ 0` is a theorem rather than a measurement; that P1 is false for
   any substrate other than v10's generated line; that v7 paper 30's
   result is wrong (it is not — it is narrower than D71b read it); that
   the corpus contains no holonomy of probability transport anywhere
   (v6 paper 4 §34's `A_D` is non-zero on *its* transports, as anchor A1
   re-confirms — it is v10's substrate that is flat, not v6's).

---

## 6. Residues, ranked

1. **Why is the generated line flat?** The measurement is exhaustive on
   its window and the negative control shows the instrument works, but
   the *reason* is not derived here. The candidate is structural: the
   step weight `q(e|h)` is a function of the *view* at `h` (the past-local
   candidate relation of the d42a admission layer), and for an
   incomparable pair neither event is in the other's view, so the two
   step weights cannot depend on the order. If that argument closes it
   turns F2 from `[MEASURED]` into `[THEOREM]` and gives the corpus a
   depth-free no-go. **This is the unit's sharpest open obligation.**
2. **The `√q` connection descends — is *that* the theorem?** T2.1 (every
   up-edge single-valued) is logically prior to T2.2 and is the stronger
   statement; a graph whose edge weights are single-valued can still have
   non-trivial holonomy, so T2.2 is not implied by T2.1, but T2.1 is
   where the flatness is *visible*. Neither is derived.
3. **D71b Clause 2 needs a downgrade.** Finding (a) shows the "error
   exactly 0" receipt is an algebraic identity. D71b called it "the
   strongest single piece of bridge evidence in the corpus". That
   sentence should be corrected wherever it is carried. This unit does
   **not** edit D71b; the correction is recorded here and is the
   principal's to route.
4. **The `k = 5` port is not available.** v7's channels are built on
   5-element sub-poset types; v10's records at the enumerated depths
   carry at most 5 events, so `k = 5` exists on exactly the deepest layer
   and was not run. Whether the verdicts move at `k = 5` is `[OPEN]`.
5. **The sign-definiteness of `O` (T3.B2) is unexplained.** It is the one
   non-trivial structural asymmetry the odd channel shows on this
   substrate, it survived the depth-4→5 widening that killed the stronger
   claim, and nothing here says why merges outnumber forks within every
   record.
6. **The F4 branch was never reachable.** If a later, non-flat substrate
   is found, F4's question — `R+`-valued or `U(1)`-valued — is still the
   right next question, and this unit supplies the instrument (an exact
   spanning-forest holonomy census with a working negative control) but
   no data for it.

---

## 7. What this unit does *not* touch

No committed file was edited. No paper, no LOG entry, no pin, no earlier
note. The three deliverables are `v10/code/d72_weld_exact.py`,
`v10/data/d72_weld_exact.out`, and this note. The corrections this unit
implies for D71b Clause 2 and for D71 Clause 3's `+1` are **recorded
here and routed to the principal**, not applied.
