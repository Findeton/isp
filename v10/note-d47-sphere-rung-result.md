# D47 — result: the sky is an ACTOR-WIDTH phenomenon

**Status:** GREEN-UNREVIEWED, 2026-07-25.  Receipts
`v10/code/d47a_sky_instrument_exact.py` (19 PASS / 0 FAIL) and
`v10/code/d47b_transport_skies_exact.py` (13 PASS / 0 FAIL), both
exit 0; outputs under `v10/data/`.  Pin:
`note-d47-sphere-rung-pin.md` (LOG #408).

**HEADLINE.**  The pin's §5 pre-registered expectation — CAPACITY
INSUFFICIENT — is CONFIRMED, and the deliverable is the one
pre-registered for that case: a validated instrument plus a
certified statement of the scale required.  The scale statement
came back in an unexpected variable.  **Sky size in the transport
layer is bounded by ACTOR WIDTH and is essentially independent of
DEPTH**, whereas in a Minkowski sprinkling it is bought with EVENT
COUNT.  Depth cannot buy what only width can.

## 1. The instrument (D47a), and why it got its own receipt

Every one of the D46 sweep's five reversals came from an
instrument nobody had checked independently.  D47a therefore reads
NO transport data at all.

**The separator is constructed, not cited.**  Arcs on 4/5/6/7
points shatter 3 and never 4.  Caps on an exact-rational
tetrahedron on the unit sphere (Fraction norms exactly 1) realize
all 16 subsets by exact rational halfspaces — including the hard
opposite-edge case, exhibited with its certificate `u = (1,1,1)`,
`t = 1/3`.  So a shattered 4-set proves a system is not an arc
system, by construction rather than by citation.

Both instruments show a true positive and a true negative, and
SG1(d) exhibits a system circular-ones rejects while shatter-4
finds nothing — so the two are strictly ordered and can never be
substituted for one another.

## 2. THE DEMOTION — the sharpest result of the unit

**Circular-ones rejected 121 of 554 genuine 2+1 skies.**

D47a's SG3b runs the instrument on exact-rational M^{2+1} records
at a scale where it actually decides (554 decidable (base event,
sky definition) pairs across N = 40/80/160).  Zero shattered
4-sets, as the separator predicts.  But circular-ones — the
instrument I had planned to make primary — rejects roughly 22% of
genuine Minkowski skies as non-arc systems.

**A discrete sky of real Minkowski is not generally an arc
system.**  Arc-realizability is therefore NOT a usable proxy for
2+1, Instrument 1 is DEMOTED to a diagnostic, and D47b rests on
shatter-4 alone.  Any earlier framing of circular-ones as "the
primary, two-sided test" is WITHDRAWN: it is two-sided on
arc-realizability, which is a different question.

This is the empirical vindication of the pin's ONE-SIDEDNESS
DOCTRINE.  The doctrine was written as caution; SG3b shows it was
necessary.

## 3. SG3 was VACUOUS, and that is gated as its own finding

D46c's committed `W3_CERT` — 18 exact M^{2+1} points, read
verbatim, max denominator 64 — yields skies of **at most 2
directions against the 4 the test needs**: decidable at **0 of 54**
base-event/definition pairs.  The original consistency check
carried ZERO information.

That is stated in a dedicated gate rather than left inside a
passing check, because a vacuous pass reads exactly like a
confirmation.  **The pin's pre-registered "capacity insufficient"
outcome was realized at the CONTROL, before any transport data was
examined.**

## 4. The capacity law, in two different variables

**Minkowski buys sky size with EVENT COUNT** (D47a SG10, exact
integer-lattice records): max |SKY-A| = 3, 8, 10, 14 at N = 20,
40, 80, 160.  Shatter-4 first becomes decidable at **N ~ 40**.

**Transport buys it only with ACTOR WIDTH** (D47b TG2, 400
deterministic deep walks per width to depth 20): max |directions|
= 2, 3, 4, 4, 4, 4 at widths 2, 3, 4, 5, 6, 8.  At width 2 the sky
stays at 2 **no matter how deep the walk runs**.

On the EXHAUSTIVE stratum — three fully enumerated families,
30,729 + 243,769 + 764,584 histories — the largest sky under any
committed definition has **3** directions.  The shatter-4 question
is therefore UNDECIDABLE there, and is reported as undecidability,
never as a 2+1 cap.

On the SAMPLED stratum: **44 decidable triples, 0 shattered
4-sets.**  Under the one-sidedness doctrine that absence is not
evidence for 2+1 — SG3b is the reason.

## 5. NO CEILING IS CLAIMED (a correction made in-receipt)

TG2's table plateaus at 4 directions from width 4 through width 8,
which invites a structural-ceiling reading.  **It is not a
ceiling.**  A denser probe at width 10, with SKY-B's depth
parameter varied over {1,2,3} instead of pinned at its committed
2, reaches **5**.

So the plateau was an artifact of my own sampling density and of a
pinned parameter — caught by chasing a suspicious flat line rather
than shipping it.  The sky keeps growing with width, slowly, and
sensitively to the sky definition's own parameter.  **No ceiling
and no saturation may be quoted from this unit.**

## 6. The null separates

The construction-matched null (D46f's lesson) replaces cross-actor
causation with per-actor chains over the same carriers.  It
produces skies of at most **1** direction against transport's 4.
The measured sky sizes are therefore produced by cross-actor
causation, not by carrier size — a null that had matched would
have voided TG2 exactly as D46f's commutation headline was voided.

## 7. What this means for the 3+1 question

The user's binding doctrine — 3+1 is not four clocks but
infinitely many — now has a measured counterpart.  **The number of
directions in a transport sky is set by the number of ACTORS.**  A
sky rich enough to be even a candidate for a 2-sphere of
directions therefore requires many actors, and no amount of
running the record longer will produce one.

That is a scale statement in the right variable, and it is the
unit's real deliverable.  It also relocates the successor: the
question "can transport produce sphere-like skies" is not
answerable at fixture width, and the thing to build is a
width-scaling fixture, not a deeper one.

## 8. What may NOT be said

- No absence of shattering is evidence for 2+1 (pin §2, SG3b).
- No statement of the form "the sky IS a circle" is licensed
  anywhere by either receipt.
- Circular-ones counts are DIAGNOSTIC and license nothing.
- The TG2 plateau is not a ceiling (§5).
- Every conclusion is conditional on the committed sky
  definitions; SKY-A, SKY-B and SKY-C disagree materially (SKY-A
  never reached 4 at all, SKY-B reached it at width 4, SKY-C at
  width 5), so any single-definition result is READING-RELATIVE.

## 9. Residues / successors

1. **A width-scaling fixture** — the only route to a decidable
   sky.  Width, not depth.
2. **Which sky definition is physically privileged?**  SKY-A
   never reaches decidability while SKY-B does; that difference is
   currently unexplained and is the D46e-class question for this
   unit.
3. The exhaustive/sampled boundary: TG2's numbers are SAMPLED and
   labelled as such; an exhaustive width-4 run at depth >= 10 is
   not currently feasible and is named rather than quietly
   omitted.
