# d41c step 3 — the two O-V bridge declarations

**Status:** DECLARATION DRAFT awaiting the author's sign-off,
2026-07-19.  Parent: `note-d41c-d26-laboratory-discriminator.md`
(§3 bridge items (a)-(d); §4 the falsifier; §5 step (3); §6 the
step-(1)/(2) forward corrections and the adopted pair).  User
direction (LOG #393) placed this after the D46 review sweep.

**WHY THIS FILE IS NOT A RESULT.**  Every line below is an
INTERPRETIVE COMMITMENT — an assertion that a corpus object *is* a
laboratory object.  Nothing here is derived, measured, or gated,
and no receipt can gate it: a bridge is a choice, and its cost is
that every bound downstream inherits it.  The corpus has been
burned by exactly this class once already (the d41a "empirical"
wording, audit verdict A1: fixture-extracted numbers described as
laboratory ones).  Therefore **every correspondence is tagged
[POSITED] with its assumptions written out and its failure mode
named, and §7 is a sign-off block the author must countersign
before any bound is quoted against these platforms.**  Until that
signature exists, this file is a PROPOSAL, and any downstream use
must say so.

## 1. What a bridge declaration must fix

Per the parent note §3(d), a declaration is complete only if it
fixes four things, each of which can be wrong independently:

- **(I) the line identification** — which laboratory degree of
  freedom is asserted to BE one monitored record line;
- **(II) the birth events** — which physical process is asserted
  to constitute a record birth on that line;
- **(III) the parent line** — what plays the role of the base
  version the monitored line descends from, and when it was
  established;
- **(IV) the background** — what is assumed about the kernel
  parameter g over the dwell, since the laboratory neither sets
  nor reads it.

A declaration that leaves any of the four implicit is not
criticizable, and an uncriticizable bridge is worse than none.

## 2. DECLARATION A — ¹⁷¹Yb⁺ single-ion hyperfine

Adopted at parent §6 as the RAW-BOUND platform: the only long-T
system where the monitored object is a single line, so the bridge
is minimal and native T₂ subtraction exists.

**(A-I) Line identification [POSITED].**  The ground-state
hyperfine pseudo-spin of ONE trapped ¹⁷¹Yb⁺ ion — the
|F=0,m=0⟩ ↔ |F=1,m=0⟩ pair — is identified with exactly ONE
monitored record line.  *Assumptions:* (1) the ion's motional and
electronic degrees of freedom carry no separately-monitored line
that could contribute births to the same coherence; (2) the trap,
lasers, and vacuum apparatus are NOT part of the monitored line —
they are environment, and their decoherence contribution is the
subtraction of parent §3(a).  *Failure mode:* if the correct
identification is "one line per ion INCLUDING its motional state",
every rate below is a sum over lines and the extracted N is an
overcount.

**(A-II) Birth events [POSITED].**  A record birth on this line is
identified with any event that WRITES A NEW VERSION on it — in the
grammar's terms, an arbitration click whose created version
supersedes the line's current base.  *Assumptions:* (1) births are
NOT laboratory operations: gates, measurements and state
preparation are excluded by construction, so a birth is a
spontaneous event of the record law, not an experimental one;
(2) births are the ONLY record-law contribution to visibility loss
on this line (no separate dispersal channel), so excess loss is
N·κ(g) and nothing else.  *Failure mode:* if laboratory operations
DO constitute births, the experiment measures its own gate count
and the bound is vacuous; if a second record-law channel exists,
the excess loss over-attributes to N.

**(A-III) Parent line [POSITED].**  The base version is
established at STATE PREPARATION: the initialization pulse that
sets the qubit is the moment from which the monitored line's
current base dates, and dwell T is measured from it.  *Assumption:*
preparation does not itself constitute a birth (else T starts one
birth late).  *Failure mode:* if the ion's line descends
continuously from a much earlier base (e.g. from loading), the
relevant dwell is longer than T and the per-dwell bound is
mis-normalized.

**(A-IV) Background [POSITED].**  g is assumed CONSTANT over the
dwell and equal across repetitions of the same protocol.
*Assumption:* nothing in the laboratory environment modulates the
kernel parameter — an assumption the corpus cannot check, since it
has no theory of what would.  *Failure mode:* a g that drifts with
any lab variable (temperature, magnetic field, duty cycle) turns a
null into an average over unknown values of κ(g), and the
functional-form cross-check of parent §4 is the ONLY thing that
would reveal it.

## 3. DECLARATION B — Arndt-class Talbot–Lau interferometry

Adopted at parent §6 as the MASS-AXIS platform: the only family
with a measured visibility ladder from ~10² to ~2×10⁵ amu in one
instrument.  **This declaration is strictly weaker than A**, and
the reason is item (I).

**(B-I) Line identification [POSITED, and the weak point].**  The
CENTRE-OF-MASS coherence of one interfering molecule is identified
with ONE monitored record line.  *Assumptions:* (1) the molecule's
internal degrees of freedom (vibration, rotation, constituent
nuclei) do NOT each carry a monitored line, or if they do, they do
not contribute births to the centre-of-mass coherence; (2) the
grating structures and beam optics are environment, not record
lines.  *Failure mode — and it is a live one:* if the correct
identification scales with constituent count (one line per nucleon
or per atom), then N is NOT a per-molecule number and the entire
mass axis measures the line count rather than any property of the
law.  **The mass ladder therefore tests the CONJUNCTION of (B-I)
and the law, and cannot separate them.**  A declaration that
pretends otherwise would be the d41a error repeated.

**(B-II) Birth events [POSITED].**  As in A-II: a birth writes a
new version on the monitored line, and is not a laboratory
operation.  *Additional assumption specific to B:* the passage
through gratings, the collisional background, and thermal photon
emission are DECOHERENCE, not births — they belong to the
subtraction of parent §3(a), not to N.  *Failure mode:* the
known-decoherence budget in these instruments is large and
mass-dependent; if any of it is mis-assigned, the mass trend is an
artifact of the subtraction rather than of the law.

**(B-III) Parent line [POSITED].**  The base version dates from
SOURCE EMISSION (the molecule's entry into the beam); dwell T is
the time of flight through the interferometer.  *Failure mode:* if
the base dates from molecular synthesis, T is wrong by orders of
magnitude and the extracted rate is meaningless.

**(B-IV) Background [POSITED].**  As A-IV, with the additional
assumption that g does not vary along the beam path or with
species — otherwise the mass ladder confounds a g-trend with an
N-trend.

## 4. What the pair would make falsifiable, if signed

Under A alone: a reproducible excess-visibility-loss floor Δ over
dwell T on a single Yb⁺ line asserts N·κ(g) = Δ births occurred on
that line, with the parameter-free cross-check that the SAME N
must appear in a second coherence observable on the same line
through the functional form (1−g)^{N/2} — the form, not the value,
is the signature (parent §4).  A null at improving δ drives the
record-birth rate on monitored lines toward zero, which is the
first experimental back-pressure on the generated-law arc.

Under B: the mass ladder tests whether the excess-loss floor
scales with mass — but ONLY as the conjunction with (B-I), which
must be stated wherever the result is quoted.

## 5. What is NOT claimed

No measurement is reported here.  No platform has been contacted.
No bound is asserted.  The corpus's own numbers remain
fixture-extracted (audit A1), and nothing in this file changes
that.  These declarations do not become physics by being written;
they become *criticizable*, which is their entire purpose.

## 6. Named risks, in priority order

1. **(B-I) line-count degeneracy** — the mass axis may measure how
   many lines a molecule carries, not the law.  Highest risk;
   would hollow out declaration B.
2. **(A-II)/(B-II) birth misattribution** — if laboratory
   operations are births, the bound is vacuous.
3. **(A-IV) g-stability** — unfalsifiable within the corpus; only
   the functional-form cross-check can expose it.
4. **(A-III)/(B-III) dwell normalization** — cheap to get wrong,
   cheap to state precisely.

## 7. SIGN-OFF BLOCK (the author's; unsigned as of 2026-07-19)

Signing means accepting, as interpretive commitments, the eight
[POSITED] correspondences above — and accepting that every bound
quoted against these platforms inherits them.

- [ ] **A-I** Yb⁺ hyperfine pseudo-spin = one record line
- [ ] **A-II** births = version-writing events, excluding lab operations
- [ ] **A-III** base dates from state preparation; T from preparation
- [ ] **A-IV** g constant over dwell and across repetitions
- [ ] **B-I** molecular centre-of-mass coherence = one record line
      *(the weak point — see §6.1)*
- [ ] **B-II** gratings/collisions/thermal emission = decoherence, not births
- [ ] **B-III** base dates from source emission; T = time of flight
- [ ] **B-IV** g constant along the path and across species

Until every box is checked, this file is a PROPOSAL.  Any citation
of it must carry the word.
