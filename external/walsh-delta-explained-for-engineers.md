# The Walsh Delta Problem, Explained For Engineers

A plain-language but fully correct walkthrough of the Walsh Delta
Global-Optimality Problem (`walsh-delta-global-optimality-problem.md`).
No prior exposure to Fourier analysis or statistical mechanics assumed.
Companion technical files: `walsh-delta-gibbs-route.md` (current proof
state), `walsh-delta-solve-log.md` (working log), `walsh-delta-code/`
(computations).

---

## 1. The playing field: bit-strings = corners of a hypercube

Imagine a control panel with n on/off switches. A **bit-string of length
n** is one complete setting of the panel — one 0 or 1 per switch. For
n = 3, one example is `011`.

How many settings exist? Each switch doubles the count: 2 × 2 × 2 ··· =
2ⁿ. Call that number **N**.

- n = 1: `0`, `1` → N = 2
- n = 2: `00`, `01`, `10`, `11` → N = 4
- n = 3: `000` … `111` → N = 8
- n = 10: N = 1024; n = 20: N ≈ one million

If you have ever written a truth table: the rows of an n-variable truth
table are exactly these N strings.

**Why "corners of a hypercube"?** Read each bit as a coordinate. For
n = 2, the string `10` is the point (1, 0); the four strings are the four
corners of a unit square. For n = 3 the eight strings are the eight
corners of a cube (check against a die: 2³ = 8 corners). For n ≥ 4 you
can't draw it, but nothing changes: a length-n bit-string *is* a point in
n-dimensional space with 0/1 coordinates, and the N of them are the
corners ("vertices") of the **n-dimensional hypercube**. Bonus intuition:
two corners are joined by an edge exactly when they differ in one bit —
"flip one switch" = "walk along one edge" (same geometry as Gray codes
and Hamming distance).

**A small convention.** Rename the switch states: +1 instead of 0, −1
instead of 1. Same cube, recentered — it makes parity computable by
multiplication.

## 2. The parity features

Pick any non-empty subset of the switch positions — say {1, 3} out of
n = 3. The **parity feature** for that subset asks one question about a
corner s: *among the switches in my subset, is an even or odd number
on?* It answers +1 for even, −1 for odd. In the ±1 labeling that is just
the product of the chosen coordinates: χ(s) = s₁·s₃.

Example, subset {1,3}, n = 3:

| corner | switches on in {1,3} | feature value |
|---|---|---|
| `000` | none (even) | +1 |
| `100` | one (odd)   | −1 |
| `001` | one (odd)   | −1 |
| `101` | two (even)  | +1 |
| `010` | none (even) | +1 |

Every non-empty subset of positions gives one feature, so there are
2ⁿ − 1 = **N − 1 parity features**. Engineers meet them as XOR functions
(the {1,3} feature is ±(s₁ XOR s₃)). They are the "frequency components"
for functions on bit-strings — the Boolean world's Fourier basis (the
Walsh basis).

## 3. Probability distributions on the cube

A **distribution P** is just a table assigning a non-negative number to
each of the N corners, summing to 1 — a loaded N-sided die whose faces
are the corners. Example for n = 2:

| corner | `00` | `01` | `10` | `11` |
|---|---|---|---|---|
| P | 0.10 | 0.20 | 0.30 | 0.40 |

The **uniform** distribution is the fair die: exactly 1/N per corner.

**Correlation of P with a feature:** roll the die, read off the
feature's ±1 answer, average over many rolls. Formally
E_P[χ] = Σ_s P(s)·χ(s). With the table above and the feature "parity of
both bits" (+1 on `00`,`11`; −1 on `01`,`10`):
(+1)(0.10) + (−1)(0.20) + (−1)(0.30) + (+1)(0.40) = 0.0 — this die is
invisible to that feature. The uniform die has correlation exactly 0
with *every* feature.

## 4. The machine: a softmax with one knob and one sign per feature

We never pick P's table by hand. Each parity feature a gets a **weight**
h_a ≥ 0 (how much it matters) and a **sign** ε_a = ±1 (which direction
it pushes). Then for every corner s:

    P(s) ∝ exp( Σ_a  h_a · ε_a · χ_a(s) ),

normalized to sum to 1. This is literally a softmax over the N corners:
a corner earns score for agreeing with each feature's preferred sign,
weighted by h_a; probability is exponential in score. Standard names:
log-linear model, Boltzmann/Gibbs distribution, maximum-entropy model.

The N−1 signs ε = (ε_a) are **your one design choice**, called an
**orientation**. There are 2^(N−1) possible orientations.

## 5. The seal: the self-consistency loop that fixes the weights

The weights h_a are NOT free. They must solve one equation per feature:

    (correlation P produces on feature a, in direction ε_a)  =  e^(−h_a).

Read as a loop: the weight shapes P → P produces a correlation → that
correlation must equal a specific *decreasing* function of the very
weight that produced it. Two crucial consequences:

1. **Built-in tension.** A heavier weight must yield a *smaller*
   correlation — the opposite of what a softmax weight naturally does.
2. **No opting out.** e^(−h) is always strictly positive, so the sealed
   distribution is forced to have nonzero correlation, of your chosen
   sign, with **every one** of the N−1 features. In particular P can
   never be exactly uniform.

**Fully worked example (n = 1).** Two corners, one feature (the bit
itself), one sign. The softmax gives correlation tanh(h) in the chosen
direction, so the seal reads tanh(h) = e^(−h). The two curves cross at
h ≈ 0.61, where both sides ≈ 0.543. The sealed distribution puts
(1 + 0.543)/2 ≈ **77.2%** on the preferred corner, 22.8% on the other.

For general n it's the same but simultaneous: N−1 coupled equations in
N−1 weights. **Theorem (proved):** this system has *exactly one*
solution for every orientation. So the machine is deterministic:

    signs in  →  sealed distribution out.

## 6. The score

Measure the distance from uniform with the KL divergence
D(P‖U) = Σ_s P(s)·log(N·P(s)). All you need: it is ≥ 0, it is 0 only for
the exactly-uniform table, and smaller = closer to fair-die behavior.
Because of consequence (2) above, every orientation scores strictly
above 0. The contest: **which of the 2^(N−1) orientations scores
lowest?**

## 7. The delta orientation and the conjecture

Pick a corner s\* and choose every sign to *disagree* with that corner:
ε_a = −χ_a(s\*). This is the **delta orientation** at s\*. Its sealed
distribution, computed exactly at n = 2 with s\* = `00`:

| corner | `00` | `01` | `10` | `11` |
|---|---|---|---|---|
| P_delta | **0.004** | 0.332 | 0.332 | 0.332 |

One corner nearly erased; a perfectly even split on the rest. Every
feature carries correlation 0.328 in its chosen direction (seal
satisfied), yet the table is nearly flat. Score: 0.2667 nats. The other
four orientations at n = 2 all score 0.4599 — worse.

**The Real Novel Problem** ([WD] §4): prove that for every n, the delta
orientations (N of them, one per corner) are the *strict global minimum*
of the score among all 2^(N−1) orientations, with no ties except the N
deltas themselves.

Intuition for the delta's trick: the seal demands nonzero correlation
with all N−1 features simultaneously. Deleting the single corner that
disagrees with every chosen sign tilts *all* features at once, at the
price of one corner — and the surviving N−1 corners stay perfectly even.
The conjecture says nothing cleverer exists.

## 8. Why it is hard (and what the score race really looks like)

Suppose you want a very small score. Then P is nearly uniform, so all
its correlations are tiny. But the seal says h_a = −log(correlation), so
tiny correlations force *huge* weights on every feature — and huge
weights in the exponent force P to be violently non-uniform somewhere.
The delta resolves the paradox by concentrating all the violence in one
corner. Its score behaves like **1/N** — vanishingly small as n grows.

Here is what makes the proof brutal (discovered during the 2026-07-02
full-proof campaign): the best known rival — erase *three* corners of a
2-dimensional sub-plane and boost the fourth plane corner to exactly 4×
uniform — scores about **5.5/N** (exactly 4·log4/N in the limit). Same
1/N scaling, just a constant factor worse. So the theorem is a
photo-finish between quantities that both vanish; any proof with slack
anywhere gets swallowed by that factor ~5. This is why 47 sections of
prior attempts (and several refuted lemmas of this campaign) failed:
every relaxation that forgets part of the seal admits phantom
competitors in the gap.

## 9. Where it stands: SOLVED (2026-07-02)

**The conjecture is now a theorem, for every n** (deliverable §6d,
Theorems E and F; audited by four hostile independent verifiers, zero
fatal findings; ~55,000-solve adversarial hunt, zero violations):

- **n ≤ 5**: certified computation (exhaustive at n ≤ 4; at n = 5 the
  2³¹ orientations reduce to 176 symmetry classes, each certified).
- **n ≥ 6**: a two-branch analytic proof. Either the score already
  exceeds 1/60 (which beats the delta's < 1/63), or the score is small —
  and then the seal *forces* at least three corners to be erased to
  depth ≥ 5 (the "deep-dip trichotomy": zero, one, or two deep dips each
  lead to contradiction), and three near-erased corners alone cost
  N·D ≥ 2.879, while the delta costs < 64/63 ≈ 1.016.

The winning insight: the "photo-finish" of §8 was a mirage. The best
*rival* costs ≈ 5.5/N, but the proof never needed to locate the rival —
it only needed every non-delta to cost more than the delta's ≈ 1/N, and
3 erased corners vs 1 is a 2.8× margin, not a photo-finish. What remains
open is only the *sharp* asymptotic rival constant (conjectured
4·log 4 = 5.545), a refinement, not a gap.

Trust base: the analytic part is self-contained (Pinsker's inequality
plus one page of explicit-constant arguments); the n ≤ 5 part is
computer-assisted with margins 8–30 orders above certified errors
(directed-rounding interval arithmetic is the one remaining formality).

## 10. Why anyone cares (one paragraph)

In the SHARD/ISP program (v8 Paper 5, "Matter"), the cube corners are
configurations of an n-bit record ledger, the orientation encodes the
record's chirality (handedness), and the sealed law is the equilibrium
distribution the chirality forces. The score — the **seal/chiral gap** —
measures the minimal distortion chiral structure must inflict. Delta
optimality is what makes the gap values "record-owned pure numbers"
(m̂_min(n) = −ln(1−2⁻ⁿ) − δ_n, the two-branch gap law) that the
phenomenology paper then consumes. The ledger flags it [OPEN]: "the
entire gap between 'theorem at n ≤ 4' and 'theorem' is (Lμ)" — now
'theorem at n ≤ 5' after this campaign.

The problem appears to be genuinely new as posed: its ingredients are
classical (Walsh analysis, exponential families, Littlewood ±1
polynomials, bent functions), but the seal's fixed point — correlation
equals e^(−weight) of its own weight — has no known occurrence in the
literature; its nearest relatives are the flat-Littlewood/merit-factor
problems, open for decades.
