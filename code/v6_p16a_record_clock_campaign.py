#!/usr/bin/env python3
"""
v6_p16a: the record clock - the witness of the separation theorem
(Paper 16, process-O6).

THE WITNESS.  A stationary binary process built as a renewal clock:
3-dimensional observable-operator model with

   tau_1 = kappa * diag(R(theta), 1),   kappa = 1/2, theta = 1 rad,
   tau_0 = v (1^T - 1^T tau_1)          (reset to v after each 0),
   v = (0.07, 0, 0.93).

Validity is ANALYTIC (Lemma W in the paper): the run-survival sequence
g(n) = 1^T tau_1^n v = kappa^n (v3 + v1(cos n theta + sin n theta))
satisfies g(n) - g(n+1) >= kappa^n [v3(1-kappa) - A(1+kappa)] =
kappa^n * 0.3165 > 0, so every word probability is a product of
nonnegative renewal factors.  The process:

  - has HANKEL (record) RANK exactly 3;
  - has p(1^n) / kappa^n = a + b cos(n theta + c) EXACTLY, with b != 0
    and theta/2pi IRRATIONAL - oscillation ON the decay circle;
  - is REVERSIBLE (stationary renewal: iid blocks);
  - is NOT reflection-positive - and P8's typed moment theorem says it
    cannot be: oscillation on the decay circle is incompatible with
    RP's real spectrum (the diagonal of an RP process is a moment
    sequence);
  - and by THEOREM B (Frobenius peripheral spectrum) admits NO finite
    positive realization: it is not a record law at ANY finite ledger
    capacity, though its rank is 3.

Receipts: (i) validity (analytic margin + exhaustive word scan to
length 16 + stationary state nonneg); (ii) rank 3 (Hankel SVD);
(iii) the exact oscillation fit and its irrational-frequency
nonperiodicity (no period P <= 12 fits); (iv) reversibility
(p(w) = p(reverse w) machine-exact to length 12); (v) RP status: the
reflection Gram FAILS PSD and the diagonal Hankel FAILS the moment
test - consistently, per P8's typed theorem.
"""
import numpy as np
from itertools import product

kappa, theta = 0.5, 1.0
v1, v3 = 0.07, 0.93
R = np.array([[np.cos(theta), -np.sin(theta), 0],
              [np.sin(theta), np.cos(theta), 0],
              [0, 0, 1.0]])
tau1 = kappa * R
one = np.ones(3)
v = np.array([v1, 0.0, v3])
tau0 = np.outer(v, one @ (np.eye(3) - tau1))
tau = tau0 + tau1
ev, V = np.linalg.eig(tau)
i1 = np.argmin(np.abs(ev - 1))
om = np.real(V[:, i1]); om /= one @ om

def p_word(w):
    s = om.copy()
    for x in w:
        s = (tau1 if x == 1 else tau0) @ s
    return float(one @ s)

# ---------- (i) validity ----------
print("== (i) validity: analytic margin + exhaustive scan ==")
A = np.sqrt(2) * v1
marg = v3 * (1 - kappa) - A * (1 + kappa)
print(f"  analytic run margin v3(1-kappa) - A(1+kappa) = {marg:.4f} > 0"
      f"   (Lemma W: validity at ALL orders)")
print(f"  stationary state omega = {np.round(om, 6)}   (min component"
      f" {om.min():.4f} >= 0)")
worst = np.inf
for L in range(1, 17):
    states = [om]
    # breadth-first over words, tracking the minimum word probability
    vecs = np.array([om])
    for _ in range(L):
        vecs = np.concatenate([(tau0 @ vecs.T).T, (tau1 @ vecs.T).T])
    worst = min(worst, (vecs @ one).min())
print(f"  exhaustive scan, all 2^16 words to length 16: min p(w) = "
      f"{worst:.3e}  (>= 0)")
print("  -> the clock is a VALID stationary process, proven analytically")
print("     and scanned exhaustively.")

# ---------- (ii) record rank 3 ----------
print("\n== (ii) the record (Hankel) rank is exactly 3 ==")
words = [tuple(w) for L in range(0, 6) for w in product((0, 1), repeat=L)]
H = np.array([[p_word(list(u) + list(w)) for w in words] for u in words])
sv = np.linalg.svd(H, compute_uv=False)
print(f"  Hankel ({len(words)}x{len(words)}) singular values: "
      f"{sv[0]:.4f}, {sv[1]:.4f}, {sv[2]:.4f}, then {sv[3]:.1e}")
print("  -> rank 3: the process has a FINITE record dimension.")

# ---------- (iii) the oscillation on the decay circle ----------
print("\n== (iii) p(1^n)/kappa^n = a + b cos(n theta + c), exactly ==")
ns = np.arange(0, 25)
pn = np.array([p_word([1] * n) for n in ns]) / kappa ** ns
M = np.column_stack([np.ones_like(ns, float), np.cos(ns * theta),
                     np.sin(ns * theta)])
coef, res, *_ = np.linalg.lstsq(M, pn, rcond=None)
fit = M @ coef
b_amp = np.hypot(coef[1], coef[2])
print(f"  fit residual = {np.abs(pn - fit).max():.2e}   a = {coef[0]:.6f}"
      f"   |b| = {b_amp:.6f}  (b != 0)")
dev = []
for P in range(1, 13):
    dev.append(max(abs(pn[n] - pn[n + P]) for n in range(len(ns) - P)))
print(f"  best periodicity over P <= 12: min_P max_n |p_n - p_(n+P)| = "
      f"{min(dev):.4f}  (bounded away from 0)")
print("  -> the normalized diagonal sequence oscillates at theta = 1 rad")
print("     (theta/2pi irrational) ON the decay circle and fits NO")
print("     rational period: exactly the structure Theorem B forbids for")
print("     finite positive realizations.")

# ---------- (iv) reversibility ----------
print("\n== (iv) reversibility ==")
worst_rev = 0.0
for L in range(2, 13):
    for w in product((0, 1), repeat=L):
        worst_rev = max(worst_rev, abs(p_word(list(w))
                                       - p_word(list(w)[::-1])))
print(f"  max |p(w) - p(reverse w)| over all words to length 12 = "
      f"{worst_rev:.2e}")
print("  -> the clock is REVERSIBLE (stationary renewal: iid blocks):")
print("     the separation lands INSIDE the corpus' eventless-compatible")
print("     class.")

# ---------- (v) RP status: the typed-theorem alignment ----------
print("\n== (v) RP status: reversible but NOT reflection-positive ==")
words_r = [tuple(w) for L in range(0, 5) for w in product((0, 1), repeat=L)]
G = np.array([[p_word(list(u)[::-1] + list(w)) for w in words_r]
              for u in words_r])
G = (G + G.T) / 2
evG = np.linalg.eigvalsh(G)
print(f"  reflection Gram on words to length 4 ({len(words_r)}x"
      f"{len(words_r)}): min eigenvalue = {evG.min():.3e}  (FAILS PSD)")
hd = np.array([[p_word([1] * (i + j)) for j in range(8)] for i in range(8)])
evH = np.linalg.eigvalsh(hd)
print(f"  diagonal Hankel [p(1^(i+j))] 8x8: min eigenvalue = "
      f"{evH.min():.3e}  (FAILS the moment test)")
print("  -> the clock is reversible yet NOT RP - and P8's typed theorem")
print("     says it CANNOT be: site-RP forces the diagonal to be a")
print("     Hamburger moment sequence (real spectrum); oscillation on")
print("     the decay circle requires complex eigenvalues kappa e^(+-i),")
print("     which the failed Hankel PSD test detects.  Consistency note:")
print("     reversibility does NOT imply RP without a Markov")
print("     presentation - exactly P10 T4's hypothesis, here sharp.")
print("  THE SEPARATION (Theorem B + this witness):")
print("       { finite record laws }  STRICTLY INSIDE")
print("       { reversible, valid, finite-record-rank processes }.")
print("  THE RESIDUE (named (PR-RP)): whether RP + finite rank implies")
print("     a finite record law - the clock mechanism is EXCLUDED from")
print("     that class by the moment theorem, so the separation witness")
print("     must be different there if it exists at all (Anderson's")
print("     positive-realization theorem suggests strictly-dominant RP")
print("     processes are realizable, possibly at higher dimension).")
print("== p16a done ==")
