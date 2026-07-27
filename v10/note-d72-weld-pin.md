# D72 — THE WELD: the reversal-holonomy identity (PIN)

**Status:** PIN, STRICT, 2026-07-27 — frozen verbatim from the D71b
identity note's pinnable-claim section (P1), unchanged except this
header.  Parents: D71b (#485 — the identity in two unwelded halves;
the bridge sentence p30:2846-9; the missing weld = order-dual vs
transport reversal), D71 (#483 — the odd-channel survivor), v6 paper
7 (holonomy = phase, Thm 7.1/D3), v6 paper 4 §34 (A_D), v7 paper 30
§24-25 (the surviving form; dual-conjugation error 0), D42b4 (the
sqrt(q) lift).  House rules: exact arithmetic; committed layers by
AST/text-slice; no leans beyond the note's own; substantive
negatives exit 0.  F2/F4 settle the founding slogan negatively and
are as publishable as a positive — NO NULL OUTCOME.


---

### THE PINNABLE CLAIM

> **P1 (the reversal-holonomy identity).** *v7 paper 30's odd channel is
> the reversal-odd channel of a probability-transport holonomy, and its
> phase `e^{iΦ(O)}` is that holonomy: concretely, the order-dual `*` on a
> five-record type (`paper30:2511`) coincides, on the generated line's own
> objects, with the transport-order reversal `AB → BA` that defines
> `A_D = log dP_AB/dP_BA` (`v6 p4 §34`), and the amplitude
> `A(R) ~ e^{-K(E)}e^{iΦ(O)}` is the `U(1)` holonomy of `√q`-transport
> around delete-then-insert round trips of the record deletion graph, with
> `A_D` as its real part (log-modulus) and `Φ(O)` as its argument.*

**Why this is the right pin and not the previously scheduled one.** D71
§4(a) proposed testing whether v7's channel index equals D66's ring
parity. §4.1 above shows that identification has to cross a
label/probability divide first, so it is no longer the cheapest decisive
unit. **P1 crosses no such divide: both of its objects are functions of
the process's own probabilities.**

**Testable how, at fixture scale, on committed objects.**

1. **The reversal test (free, one computation).** Take the D42b4 lift at
   the F-PAIR fixture (`note-d42b4-quantum-lift.md:62-64`), form
   `A_D = log dP_AB/dP_BA` for the two orderings of an incomparable event
   pair (the receipt already exists as `code/v6_p4n_exchange_cocycle_law.py`),
   and separately form `F* ` by dualising the record's order relations.
   **Ask: is `A_D` odd under `*`?** The corpus has both halves receipted
   (`v6 p4:2636` at gap `2.2e-16`; `paper30:2848` at error `0`) and has
   never applied them to the same object.
2. **The closure test.** Compute the delete-then-insert round-trip transport
   of `∏√q` on the generated line's own deletion/insertion moves
   (`paper30:1999`) and ask whether the round-trip ratio is `1`. If it is
   `1` identically, there is no holonomy to have and P1 is dead on this
   substrate. If it is not, **its logarithm is a real holonomy and its
   argument is the empty phase slot D71 Clause 3 found filled with `+1`.**
3. **The dual-conjugation re-run.** Evaluate `L_dual = e^{-kE}e^{iθO}` on
   the *generated line's* even/odd channels — not v7's five-record
   flags — and check the dual-conjugation error that v7 measured at exactly
   `0`. This is D71 §4(a)'s successor step, and it survives intact.

**Falsifiers, pre-registered, each of which kills P1 cleanly.**

* **F1.** `A_D` is **not** odd under the order-dual `*` at the fixture —
  then v6's reversal and v7's reversal are different operations, Clause 3's
  bridge fails, and the corpus has two unrelated reversal-odd channels.
  P1 dies; the honest residue is a named coincidence.
* **F2.** The `√q` round-trip transport is **identically `1`** on every
  delete-then-insert cycle of the generated line — then the generated line
  is flat, has no holonomy of any kind, and D71 Clause 3's `+1` is a
  **theorem** rather than an unargued choice. P1 dies, and the corpus gains
  a no-go it does not currently have.
* **F3.** `L_dual`'s dual-conjugation error on the generated line's channels
  is non-zero — then the surviving v7 form does not transfer to v10's
  substrate, and the odd channel is a v7-local fact. P1 dies at the
  transfer step.
* **F4.** The round-trip defect exists but is **not** `U(1)`-valued — e.g.
  it is `R+`-valued only (pure modulus, no argument) — then the corpus has
  a real holonomy of probability transport and **no phase**, which is
  precisely Clause 5's tension resolved *against* the imaginary reading.
  P1 dies in its interesting direction and the founding slogan is refuted
  on its own substrate.

**Note that F2 and F4 are the outcomes that would settle the founding
question negatively, and both are as publishable as a positive.** The pin
is designed so that no outcome is a null result.

---

