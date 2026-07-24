# D46c — Minkowski-dimension certificates (the 2+1 rung)

**Status:** CAMPAIGN PIN (strict), 2026-07-19; user-ordered before
D46b. Parents: the §1 doctrine of note-d45b (order dim vs Minkowski
dim; Meyer [LITERATURE]); d43d/d45b terminal witnesses.
Receipt: `v10/code/d46c_minkowski_certificates_exact.py`.
GREEN-UNREVIEWED discipline per the D46 program pin.

## 1. The question and its honest shape

POSITIVE CERTIFICATES ONLY: an M^{2+1} causal-order certificate for
a finite poset = an assignment of rational events (t, x, y) with
p < q in the poset IFF q - p is future-causal ((dt)^2 >= (dx)^2 +
(dy)^2 AND dt > 0), verified EXACTLY in rationals, both directions
(order implies causal, incomparability implies spacelike). Failure
to find a certificate is OPEN, never a negative claim (recognition
is hard). This is the first rung of the physical dimension ladder:
"escaped 1+1" (order dim >= 3) upgraded, where certified, to "fits
in 2+1".

## 2. Gates (pre-registered)

- **KG0 (the checker is the gate):** an exact rational causal-order
  checker; regression: the 1+1 two-clock certificates of the
  committed 2D chains (SIG_KR, h5, CH or a subset — light-cone
  coordinates from their realizer pairs) verified as M^{1+1}
  certificates; a deliberately broken certificate must FAIL.
- **KG1 (the crowns):** M^{2+1} certificates for the standard
  examples S_3..S_6 via the doctrine's antipodal construction made
  RATIONAL (rational points on the unit circle by Pythagorean
  parametrization; rational heights between the separation bounds)
  — each verified exactly, all pairs both directions.
- **KG2 (the committed witnesses):** certificates ATTEMPTED for the
  committed dimension witnesses — the W6/S3 event poset (6 events)
  and the W(n) courier records (2n^2 events, n = 3 at minimum;
  larger n as constructions succeed). Every found certificate
  gated; every not-found DECLARED OPEN with the attempt census.
- **KG3 (doctrine compliance):** no claim that a certificate is
  spacetime; no negative embeddability claim anywhere; the sphere
  (3+1) rung explicitly out of scope (successor).
- **KG4:** allow-list purity; determinism; no check(True);
  GREEN-UNREVIEWED banner verbatim per the program pin.

## 3. Scope

Finite rational certificates at fixture scale; exact integer/
rational arithmetic only (squared-interval comparisons — no square
roots needed). Typicality is D46d's; transport-scope machinery
untouched.

## 4. First-run amendments (2026-07-19, pre-round; author-built,
## GREEN-UNREVIEWED)

**A1 (direction selection uses floats as a SEARCH heuristic).**
spread(n) orders the rational-unit-vector pool by atan2 and picks
the nearest candidate to each equal-spacing target — floats appear
ONLY in that selection; every SELECTED vector is an exact rational
unit vector (gated) and every certificate check is exact Fractions.
Declared in the function's docstring and in KG4-a's label.

**A2 (T by smallest-denominator search).** The crown height is the
smallest-denominator rational T with max|d_i+d_j|^2 <= T^2 < 4
(exact search over denominators) — T = 3/2 (S_3, S_4), 5/3 (S_5),
7/4 (S_6).

**A3 (KG2-b ran TWO families, both open).** Family A
(interpolating: courier layers placed on the segment from the
minimum toward the upper's antipode) and family B (hub-clustered:
each hub's C-layer near that hub's own antipode, the chain TIMES
crossing the distance threshold) — 3,840 + 9,396 = 13,236 exact
rational parameter tuples, no certificate. The census localizes
the difficulty: the dominant first-violations are
CHAIN-ACCUMULATION pairs (a minimum required below a LATE member
of a hub chain while spacelike from that hub's earlier members) —
the courier firewall's own signature. DECLARED OPEN, never a
negative embeddability claim.

**A4 (self-scan needles).** KG3-a/b and KG4-b build their needles
by concatenation and carry marker words, so the discipline scanners
cannot self-trip (the d45b ZG6.2 lesson).

## 5. Result (GREEN-UNREVIEWED; round queued behind paper-32's)

11 PASS / 0 FAIL, 1 declared OPEN. **The first geometric
realization of a generated record beyond the two-clock rung: the
committed W6 witness — the transport record whose order dimension
is 3 — is CERTIFIED in M^{2+1} causal order**, exactly, on all 30
ordered pairs, by transporting the rationalized antipodal
certificate along its crown shape. The standard examples S_3..S_6
are certified likewise (T = 3/2, 3/2, 5/3, 7/4 on unit-circle
directions). The checker is regression-anchored on the 1+1 rung
(light-cone coordinates from a realizer pair) with a firing broken-
certificate control. The full 18-event W(3) courier record is
OPEN per A3. Doctrine held throughout: certificates are statements
about the CAUSAL ORDER's embeddability; the sphere (3+1) rung and
typicality are named successors (D46d).

## 6. Round-1 amendments (2026-07-19; round frozen at
## reviews/d46ac-round1-hostile-review.md: REVISE, 1B/4M/6m/1n)

**B1 (THE HEADLINE SURVIVES, independently verified).** The
referee rebuilt the W6 poset from scratch (= the committed d43d
anchor = the crown S_3), pinned its order dimension independently
at EXACTLY 3 (so "beyond the two-clock rung" is earned, not
assumed), and re-verified the certificate with their OWN
coordinates and their OWN checker: 0 violations on all 30 ordered
pairs. The S_3..S_6 M/T values, the minimal-denominator property,
the 13,236 tuple count, the 1/68 weight and the S_3 subposet are
all confirmed; no negative embeddability claim appears anywhere.

**B2 (MAJOR C2 — THE OPEN IS DISCHARGED; a POSITIVE REVERSAL, and
my localization was FALSE).** The referee FOUND an exact rational
M^{2+1} certificate for the FULL 18-event W(3) courier record
(hill-climb, rationalized at denominator 64), verified on all 306
ordered pairs by their checker AND by this receipt's own verify().
Consequences, owned: (i) KG2-b's OPEN is retired — the record IS
certified; (ii) §4 A3's and §5's "the difficulty sits at the
CHAIN-ACCUMULATION pairs — the courier firewall's own signature"
is WITHDRAWN as FALSE: the two searched families failed only
because BOTH fix all minima at t = 0 and force a common upper
height T, neither of which is necessary. The failure was my
parameterization's, not the record's. Forward-corrected at LOG
#394.

**B3 (BLOCKER C1 — nothing controlled the SPACELIKE direction).**
KG0-c exercised only the causal half: a mutant whose verify checks
`order => causal` alone ran 11 PASS / 0 FAIL, exit 0, ZERO OPEN,
and printed a FABRICATED headline claiming W(3) certified on all
306 pairs. The incomparability half is now controlled in-receipt.

**B4 (C3/C4/C5 + minors).** The first-violation census was
scan-order biased (all buckets in i-block 0; the all-violation
census is dominated by L-vs-C pairs and the top printed bucket was
the crown diagonal, not a chain pair) — replaced by an
order-independent census; KG0-b's regression used an ad-hoc
realizer rather than a committed 2D chain (now a committed chain,
or declared); KG4-a's "813 leaves" was a mutable-default
accumulation artifact (true count 281 — corrected); the relative
_SRC path, family-B's dropped dc, the console count mismatch, the
3-of-614-line KG3-a scan, and the un-regated "not 1+1" half are
repaired or declared.
