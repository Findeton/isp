# D73 — THE EVEN GRAM: does the real channel host a rank-2 metric response? (PIN)

**Status:** PIN, STRICT, 2026-07-27 — frozen verbatim from the D71c
spin-2 archaeology's pinnable-claim section (P2), unchanged except
this header.  Parents: D71c (#486 — the something-2 was h^{ij}; the
off-diagonal is phase-carried [v2 p10 Prop 10.6]; the even Gram
computed-and-discarded at v7 p30_reflection_positive_campaign.py:
394-406), v6 p54 (anticommutator -> spin-2 shear coupling), v6 p4
FAILS-FULL-GR (the blocking precedent to answer), D67 (the wide
charts a rank-2 form needs).  House rules as D72's.  Falsifier F1
(Gram proportional to identity => the even channel cannot host a
metric) is a first-class no-go — NO NULL OUTCOME.

become a metric by interpretation. It has to become a form.**

---

### THE PINNABLE CLAIM

> **P2 (the even-channel rank-2 pin).** *The gravity-side counterpart of
> D71b's P1 is not a group but a FORM: the corpus's rank-2 gravity object
> is the SYMMETRIC (anticommutator/even) part of a transport pair —
> `½{γ^i,γ^j} = h^{ij}I` (`v2 p10:1825`), `C(θ)=½{K(0),K(θ)}`
> (`v6 p54:18`) — and the generated line's realisation of it is the EVEN
> REFLECTED GRAM `G^{even}_{jk} = Σ_R P(R) E_j(R) E_k(R^*)` already
> computed at `v7 p30:2991-2997` and discarded in favour of its trace
> `E_total`. Concretely: `K` should be `K(E) = E^⊤ N E` for a
> positive-definite `N_{jk}`, not `k·ΣE_j`; the corpus's own no-go says a
> scalar cannot be a metric (`v6 p4:1064`, `missing_components = 8193`);
> and the datum that decides whether this is geometry or bookkeeping is
> the ORIENTATION — the same `Z/2` that Prop 10.6 and `χ^{NN}` both turn
> on.*

**Attachment point, named.** `G^{even}_{jk}` on the three dual-even
channels of the rooted boundary law, receipt
`v7/code/p30_reflection_positive_campaign.py:394-406` — **already written,
already run, already exact.** The corresponding v10 object does not exist;
the nearest slot is D64's chart-pair transition, and it measured trivial.

**Testable how, at fixture scale, on committed objects.**

1. **The un-tracing test (free, the receipt exists).** Re-run
   `p30_reflection_positive_campaign.py` and report the **off-diagonal**
   entries of `G^{even}_{jk}`, not only its principal minors. Ask: is
   `G^{even}` proportional to the identity (then `E_total` loses nothing
   and the even channel is genuinely scalar), or does it have non-trivial
   anisotropy (then the law has been throwing away a metric)? **The corpus
   printed the minors and never printed the matrix.**
2. **The generalised-`K` test.** Replace `K(E) = k·E_total` by
   `K(E) = E^⊤ N E` on the same `N=5..9` window and re-run the four
   campaign checks paper 30 already gates on (even-absolute compression,
   dual conjugation, atom-average collapse, `TV_9`). Pre-registered: if
   **every** `N` matches `diag(k,k,k)`'s `TV_9 = 1.676e-5`, the even
   channel is provably trace-only at this window and the gravity reading
   dies on this substrate. If some `N` improves it, the even channel
   carries anisotropy and §7's pin has its first evidence.
3. **The orientation test (the cross-link to D71b's P1).** `χ^{NN}` is
   determined by the *oriented* `SO(1,1)` holonomy and undetermined by the
   unoriented one (`v6 p5:837-846`). D71b's P1 asks whether `A_D` is odd
   under paper 30's order-dual `*`. **These are the same question asked of
   the two channels.** Run them in one unit: form the even and odd parts
   of the same transport pair and ask whether the even part carries the
   Gram anisotropy while the odd part carries the sign.

**Falsifiers, pre-registered.**

* **F1.** `G^{even}_{jk}` is diagonal, or is a multiple of the identity.
  Then `E_total` is lossless, `K` is correctly scalar, and the even
  channel provably cannot host a metric on this substrate. **P2 dies
  cleanly, and the corpus gains a no-go it does not have.**
* **F2.** A quadratic `K(E) = E^⊤NE` cannot match the committed `TV_9` for
  any `N` including `N = diag(k,k,k)`. Then the generalisation is
  inconsistent with the receipted law and the form is wrong.
* **F3.** The even/odd algebraic split of §3 does not survive transfer:
  the anticommutator of the generated line's own transports is not
  symmetric, or is not rank-2. Then §3.2's table is a coincidence of two
  imported representations and should be struck.
* **F4.** `χ^{NN}`-analogues on the generated line are determined by
  unoriented data. Then the orientation is not the shared missing datum,
  Clause 2's unification of the gravity and phase no-gos fails, and the
  principal's clean split survives after all — **which would be the most
  interesting outcome and is the one this note would most like to be
  wrong about.**

**F1 and F4 are the outcomes that settle the question negatively, and both
are as publishable as a positive.**

---

