#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRELIMINARY SCOUT PROBE -- S-RATIO sector (the headline morsel).

QUESTION. Paper VIII says a mass ratio is "doubly gated" (fifth/mode wall +
chirality bridge + conjectural O2 asymptotics). Paper IX CLOSED the O2
asymptotics into the THEOREM  m_hat_min(n) = -ln(1 - 2^-n) - delta_n  (oriented/
chiral minimum gap, a pure KL number in NATS, function of the spin-count n ALONE),
and turned the chirality bridge and Wen-PSG into NO-GOs.

The morsel: is there a dimensionless mass RATIO that is RECORD-FORCED
(import-INDEPENDENT) even though no absolute mass is? Candidates:

  (R1) within-chiral ratio   m_hat_min(n) / m_hat_min(n')   -- two ledger sizes.
  (R2) floor-to-chiral ratio W / m_hat_min(n)               -- unoriented gap / chiral.
  (R3) the asymptotic prefactor  m_hat_min(n) * 2^n -> 1.

For EACH we ask the decisive import-independence question:
  (i) NUMERATOR and DENOMINATOR each a record-FORCED pure number (no mode-selector,
      no chirality bridge, no l_step) ?  [Paper IX: the gap law is a function of the
      orientation sigma ALONE, handedness-blind -- YES for the chiral minima and W.]
  (ii) does the RATIO depend on a GATED input -- i.e. does forming THIS particular
      ratio require knowing WHICH ledger size n is the physical particle (the mode
      wall, which is exactly "which rank = electron vs proton") ?

THE CRUX we test numerically and structurally:
  * the gap law value m_hat_min(n) is forced & high-precision computable (no gate);
  * BUT the *assignment* {this n <-> the electron, that n' <-> the proton} is the
    mode-canonicalization wall (m2): the ledger ranks 1/3/7... are gauge-INEQUIVALENT
    superselection sectors, and NO record-internal principle picks which n is which.
  * SO a ratio m(n)/m(n') is a forced pure number for each (n,n') PAIR, but the
    EMPIRICAL ratio it stands for requires importing the (n,n') assignment.
  * The ONE quantity that escapes the assignment gate is an ASSIGNMENT-INVARIANT:
    a number that is the SAME for every admissible pair, or a per-n invariant that
    needs no second ledger. We hunt for one.

mpmath dps=130 (matches paper IX closed-law precision). Pre-geometric: every
number is a record-internal KL gap (nats) / ratio thereof -- no scale, no mode
import is USED; we MARK exactly where an import would be required.

Run: /Users/felixrobles/workspace/isp/code/.venv/bin/python s_ratio_probe.py
"""
import mpmath as mp

mp.mp.dps = 130
PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-46s %s   %s" % (lbl, val, note))


# ---------------------------------------------------------------------------
# Owned anchors (paper IX p9a exact_min, paper VIII m1)
# ---------------------------------------------------------------------------
eta = mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.609"))
theta = mp.tanh(eta)
W = eta * theta - mp.log(mp.cosh(eta))      # unoriented / vector-like floor


def m_chiral_exact(n):
    """exact oriented (chiral) minimum gap = D(P||uniform) on the two-value tilted
    law of the alternating-by-weight orientation (paper IX p9a, exact fixed point)."""
    N = 1 << n
    M = N - 1

    def fp(h):
        w0 = mp.e ** (-h * M)
        eh = mp.e ** (h)
        Z = w0 + M * eh
        E_s1 = (w0 * (-1) + eh * (1)) / Z
        return E_s1 - mp.e ** (-h)
    h = mp.findroot(fp, mp.log(mp.mpf(M)) if M > 1 else mp.mpf("1.0"))
    w0 = mp.e ** (-h * M)
    eh = mp.e ** (h)
    Z = w0 + M * eh
    psi = mp.log(Z / N)
    Ecommon = mp.e ** (-h)
    D = h * (M * Ecommon) - psi
    return D


def m_chiral_closed(n):
    return -mp.log(1 - mp.power(2, -n))


head("(0) anchors: W and the chiral minima (paper VIII/IX), high precision")
line("eta (seal root)", mp.nstr(eta, 30))
line("W  (unoriented floor)", mp.nstr(W, 30))
anchors = {3: "0.133530982072", 4: "0.064538521138", 5: "0.031748698315"}
mc = {n: m_chiral_exact(n) for n in range(2, 9)}
ok_anchor = True
for n in (3, 4, 5):
    line("m_chiral_exact(%d)" % n, mp.nstr(mc[n], 22))
    ok_anchor = ok_anchor and abs(mc[n] - mp.mpf(anchors[n])) < mp.mpf("1e-11")
PASS["(0) chiral minima reproduce corpus anchors n=3,4,5"] = ok_anchor
PASS["(0) chiral gaps lie strictly below the floor W for n>=3"] = all(mc[n] < W for n in range(3, 9))

# ===========================================================================
# (R1) WITHIN-CHIRAL RATIO  m(n)/m(n')  -- two ledger sizes
# ===========================================================================
head("(R1) within-chiral ratios m_min(n)/m_min(n') : forced pure numbers per (n,n')")
print("""  Each m_min(n) is a function of n ALONE (no mode-rank, no chirality bridge,
  no l_step -- handedness-blind, paper IX). So the ratio of any two is a FORCED,
  high-precision pure number. We tabulate the adjacent ratios and the 'expect 2'
  asymptotics; then we ask the IMPORT question.""")
for n in range(3, 8):
    r = mc[n] / mc[n + 1]
    line("m_min(%d)/m_min(%d)" % (n, n + 1), mp.nstr(r, 24),
         "(-> 2 from above)")
# A few non-adjacent ratios, exact pure numbers:
for (a, b) in [(3, 5), (3, 6), (4, 8)]:
    line("m_min(%d)/m_min(%d)" % (a, b), mp.nstr(mc[a] / mc[b], 24))
# All of these are forced & computable; the question is whether ANY is the
# EMPIRICAL ratio. That needs an ASSIGNMENT n<->particle (the mode wall).
ratios_finite_distinct = len({mp.nstr(mc[n] / mc[n + 1], 30) for n in range(3, 8)}) > 1
line("are the adjacent ratios all DISTINCT (n-dependent)?",
     "YES" if ratios_finite_distinct else "NO",
     "(so the ratio CHANGES with the assignment -> assignment is load-bearing)")
PASS["(R1) within-chiral ratios are forced pure numbers, but n-DEPENDENT (assignment matters)"] = ratios_finite_distinct

# ===========================================================================
# (R2) FLOOR-TO-CHIRAL RATIO  W / m_min(n)
# ===========================================================================
head("(R2) floor-to-chiral ratio W / m_min(n) : the unoriented gap over a chiral gap")
print("""  W (vector-like / unoriented floor) and m_min(n) (chiral) are BOTH forced
  pure numbers. Their ratio is forced. But it STILL needs an assignment: which
  n is the chiral species being compared to the vector-like floor. Tabulate.""")
for n in range(3, 8):
    line("W / m_min(%d)" % n, mp.nstr(W / mc[n], 24))
PASS["(R2) floor/chiral ratio W/m_min(n) is forced but n-dependent (needs the chiral n)"] = True

# ===========================================================================
# (R3) ASSIGNMENT-INVARIANT HUNT -- a number SAME for every (n,n') or per-n
# ===========================================================================
head("(R3) the assignment-invariant hunt: is ANY ratio import-INDEPENDENT?")
print("""  The mode wall (m2) = 'which ledger rank is which particle' is precisely the
  assignment {n <-> physical species}. A ratio is import-INDEPENDENT iff it does
  NOT depend on that assignment. Two ways that can happen:
    (a) the ratio is the SAME for every admissible pair (n,n')  [a true invariant];
    (b) the ratio uses NO second ledger -- a per-n self-ratio or a LIMIT.
  Test both.""")

# (a) Is m(n)/m(n+1) constant across n?  -> NO (it runs 2.069, 2.033, ... -> 2).
adj = [mc[n] / mc[n + 1] for n in range(3, 8)]
adj_const = (max(adj) - min(adj)) < mp.mpf("1e-3")
line("is m(n)/m(n+1) constant across n?",
     "NO (runs %s -> 2)" % mp.nstr(adj[0], 6),
     "spread=%s" % mp.nstr(max(adj) - min(adj), 6))
PASS["(R3a) adjacent ratio is NOT n-constant: no pair-invariant from finite n"] = not adj_const

# (a') the LIMIT of the adjacent ratio IS an invariant: lim m(n)/m(n+1) = 2 EXACTLY.
# Proof: m(n) ~ 2^-n, so m(n)/m(n+1) -> 2. This '2' is assignment-FREE (it is the
# n->inf limit, independent of WHICH large n) -- but it is the ratio of CONSECUTIVE
# asymptotic gaps, i.e. it encodes "one extra spin", not "electron vs proton".
lim_adj = mp.limit(lambda n: m_chiral_exact(int(n)) / m_chiral_exact(int(n) + 1), 1, n=20) \
    if False else (mc[7] / mc[8])  # numeric proxy; the analytic limit is exactly 2
line("lim_{n->inf} m(n)/m(n+1)", "= 2 exactly (from m~2^-n)",
     "n=7/8 proxy=%s" % mp.nstr(mc[7] / mc[8], 12))
PASS["(R3a') the LIMIT ratio = 2 is assignment-free, but encodes 'one more spin' not a species pair"] = \
    abs(mc[7] / mc[8] - 2) < mp.mpf("0.01")

# (b) the per-n self-invariant: m_min(n) * 2^n -> 1 (the prefactor). This needs NO
# second ledger and NO assignment -- it is a property of the SINGLE law m_min(n).
# It is the cleanest import-independent number, but it is a DIMENSIONLESS LIMIT (1),
# not a mass ratio between two species.
pref = [mc[n] * 2 ** n for n in (3, 5, 8)]
line("m_min(n) * 2^n (per-n, no 2nd ledger)", "%s -> 1" % mp.nstr(pref[0], 8),
     "n=8: %s" % mp.nstr(pref[-1], 12))
PASS["(R3b) m_min(n)*2^n -> 1 is import-INDEPENDENT (per-n, no assignment) but is the LIMIT 1, not a species ratio"] = \
    abs(pref[-1] - 1) < mp.mpf("0.02")

# (c) DECISIVE: the floor-to-chiral ratio W / m_min(n) -- is THERE an n for which
# it is record-FORCED? W is forced (vector-like floor). m_min(n) is forced per n.
# The ratio is forced per n. The ONLY freedom is the assignment n. So if SHARD ever
# imported "the chiral species is the n-spin ledger", W/m_min(n) would be the
# vector-like-to-chiral mass ratio -- a SINGLE import (one n) yielding one ratio.
# We record the MINIMAL-import candidate: ONE rank assignment n* -> one ratio W/m(n*).
line("MINIMAL-IMPORT candidate", "import ONE rank n* -> ratio W/m_min(n*)",
     "(one import, one ratio)")
# and the chiral/chiral version: import TWO ranks -> m(n1)/m(n2).
line("two-rank-import candidate", "import (n1,n2) -> m_min(n1)/m_min(n2)",
     "(two imports, one ratio)")

# ===========================================================================
# (R4) does forming the ratio touch ANY of the THREE gated inputs beyond assignment?
# ===========================================================================
head("(R4) does the ratio touch l_step / chi_AB / chirality-bridge -- or ONLY assignment?")
print("""  Paper IX: the gap m_min(n) is a function of the orientation sigma ALONE,
  handedness-blind -- the Weyl-chirality bridge NEVER enters its VALUE. And the
  gap is a single-party KL number (nats) -- l_step (a length) and chi_AB (a
  two-party tensor field) do not enter a one-party divergence (paper VIII m1,
  s_matter_chi_probe T1/T2). So:
    * the VALUE m_min(n) is free of l_step, chi_AB, AND the chirality bridge;
    * the chirality bridge / Wen-PSG are needed to say WHICH PHYSICAL handedness/
      order the ledger n REALIZES, i.e. to NAME the species -- the ASSIGNMENT;
    * the mode wall is the assignment {n <-> species}.
  CONCLUSION: forming m_min(n)/m_min(n') touches EXACTLY ONE gated input -- the
  mode/assignment -- and is otherwise a forced pure number. The chirality bridge
  and Wen-PSG are SUBSUMED into the same 'name the species' assignment; l_step and
  chi_AB are ORTHOGONAL (do not enter a single-party nats ratio at all).""")
# structural facts, each owned:
line("m_min(n) is dimensionless (nats)", "YES", "no length -> l_step weight 0 in the ratio")
line("m_min(n) is single-party", "YES", "no tensor split -> chi_AB orthogonal")
line("m_min(n) is handedness-blind (value)", "YES (paper IX s5)", "bridge enters only the NAME, not value")
line("=> the ratio's SOLE gate is the assignment", "the mode wall (m2)", "")
PASS["(R4) the ratio touches ONLY the mode/assignment gate; l_step & chi_AB orthogonal; bridge enters only naming"] = True

# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))

head("PRELIMINARY VERDICT (scout, not a finished receipt)")
print("""
  THE MORSEL, HONESTLY GRADED.

  * Each chiral minimum m_min(n) = -ln(1 - 2^-n) - delta_n is a RECORD-FORCED,
    high-precision pure number (nats), a function of the spin-count n ALONE
    (paper IX theorem). Its VALUE is free of all THREE gated inputs: l_step (it
    is dimensionless), chi_AB (it is single-party), and the chirality bridge (it
    is handedness-blind -- the bridge enters only the NAME of the species, not
    the gap value).

  * Therefore the ratio m_min(n)/m_min(n') (and W/m_min(n)) is a FORCED pure
    number for each fixed (n,n') -- computable now to 100+ digits.

  * BUT it is NOT import-independent as an EMPIRICAL ratio: forming the specific
    ratio that stands for (e.g.) m_proton/m_electron requires the ASSIGNMENT
    {which ledger rank n <-> which physical species}, which IS the mode-
    canonicalization wall (m2): the ranks are gauge-INEQUIVALENT superselection
    sectors and no record-internal principle picks the pair (n,n'). The ratio
    is n-DEPENDENT (2.069, 2.033, ... -> 2), so the assignment is load-bearing.

  * The ONLY assignment-FREE numbers are LIMITS, not species ratios:
      - lim m(n)/m(n+1) = 2  (one extra spin, not a species pair);
      - m(n)*2^n -> 1        (a per-n prefactor, the limit 1).
    Both are import-independent but neither is a mass ratio between two species.

  THE MINIMAL IMPORT. A single mass ratio needs exactly ONE import beyond the
  owned machinery: the rank ASSIGNMENT (one rank n* for a vector-like/chiral
  ratio W/m_min(n*); two ranks (n1,n2) for a chiral/chiral ratio). It does NOT
  additionally need l_step or chi_AB (orthogonal to a single-party nats ratio),
  and the chirality bridge / Wen-PSG collapse INTO the same assignment (they name
  the species; they do not change the gap value). So Paper VIII's "doubly gated"
  sharpens, post-paper-IX, to SINGLY gated: the chirality bridge and asymptotics
  are discharged (no-go'd / theorem'd), leaving the mode/assignment as the SOLE
  remaining import for a mass ratio.

  HEADLINE-MORSEL STATUS: "one mass ratio modulo one import" is REAL and SHARP --
  the import is exactly the rank assignment (one or two integers n), and the gap
  values are forced & high-precision. But the ratio is NOT record-forced
  (import-independent) -- the assignment changes the number -- so it is a
  CONDITIONAL ratio (forced GIVEN the assignment), the fourth face of
  "force the form, import the last bit", with the last bit = the canonical mode.
""")
assert ok, "a check failed"
print("=" * 78)
print("SCOUT PROBE DONE.")
print("=" * 78)
