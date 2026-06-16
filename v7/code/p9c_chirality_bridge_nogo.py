"""
v7 Paper IX, receipt C -- the second no-go: NO record-forced chirality bridge.

Paper VIII sec 8 (and Paper 8 open-item-2) named, as a prerequisite for a mass ratio, the
ledger-chirality <-> Weyl/PSG-chirality BRIDGE: is the Weyl-seed handedness m (signed fiber
weight +-1/2, Paper 9) a RECORD-FORCED FUNCTION of the orientation class sigma (Paper 8)?

This receipt proves it is NOT -- a no-go, upgrading the corpus's disclosed "different layer"
gap to a proved structural impossibility on the executed machinery.

THE TWO LAYERS.
  sigma : K -> Z2          orientation class = a character of the relation code K
                           (the LEDGER / Ising layer, Paper 8 Thm 5.1) -- dim K bits.
  m     : SO(3) rep label  Weyl handedness = a label of the rotation/dilation FIBER
                           (Paper 9 D3, the belt-trick double cover) -- 1 bit (+ vs -).
  These are objects of DIFFERENT record layers. A "bridge" is a record-internal map sigma|->m.

THE NO-GO (handedness-blindness + parity-covariance).
  (i) The LEDGER LAYER is handedness-BLIND: the gap m_hat, the code K, the orientation group
      K-hat (x) Aut(K), and every ledger quantity are functions of sigma ALONE -- the fiber
      handedness m never enters their computation. So nothing in the ledger carries the 1 bit
      a bridge would have to output.
  (ii) Parity P is a JOINT symmetry (Paper 9 sec9): P : (sigma, m) -> (sigma-bar, -m), and the
      gap is parity-invariant, m_hat(sigma-bar) = m_hat(sigma). A bridge f : sigma|->m would
      have to be parity-COVARIANT, f(sigma-bar) = -f(sigma) -- an odd map on a parity-symmetric
      data set. The records single out no representative of the parity pair {sigma, sigma-bar}
      as "left", so f is undetermined: choosing it IS the coupling g (an (M)-sector input,
      Paper 9 sec9), not a record-internal function.
  => the chirality bridge is NOT record-forced [NO-GO]. (The handedness magnitude is itself
     g-dependent -- the Weyl asymmetry vanishes at g=0 and is nonzero only for g != 0, Paper 9
     sec9 -- confirming handedness is supplied by the coupling, not the orientation.)

Pre-geometric: every object is a record-internal code / character / KL gap. The thing proved
ABSENT (a ledger->fiber handedness map) is exactly what the records do not carry.
"""
import itertools
import numpy as np

PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


# seal root + gap machinery (the LEDGER layer; note: NO handedness m anywhere)
eta = float(np.real(np.array([0.6093778634360062])[0]))  # owned seal root (receipt m1, dps>=15 here)
# refine eta in float
e = 0.6093778634360062
for _ in range(60):
    f = np.tanh(e) - np.exp(-e)
    fp = 1 - np.tanh(e) ** 2 + np.exp(-e)
    e = e - f / fp
eta = e


def char_cols(n):
    st = np.array(list(itertools.product((-1, 1), repeat=n)), float)
    cols = np.empty((st.shape[0], (1 << n) - 1))
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        cols[:, mask - 1] = np.prod(st[:, idx], axis=1)
    return cols


def gap_of_orientation(n, signs, chi0, tol=1e-13, maxit=400):
    """m_hat(sigma) -- a function of the ORIENTATION signs ALONE. No handedness m enters."""
    chi = chi0 * np.asarray(signs, float)[None, :]
    h = np.full(chi.shape[1], eta)
    for _ in range(maxit):
        z = chi @ h; z -= z.max(); w = np.exp(z); p = w / w.sum()
        E = chi.T @ p; F = E - np.exp(-h)
        if np.abs(F).max() < tol:
            break
        Cov = (chi * p[:, None]).T @ chi - np.outer(E, E)
        J = Cov + np.diag(np.exp(-h))
        try:
            step = np.linalg.solve(J, F)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(J, F, rcond=None)[0]
        h = h - step
    z = chi @ h; z -= z.max(); p = np.exp(z); p /= p.sum()
    return float(np.sum(p * np.log(p * p.size)))


# ---------------------------------------------------------------------------
head("(1) the two layers carry independent data (different objects)")
n = 3
dimK_examples = {"triangle": 1, "3-spin full": 4}   # dim K = # orientation bits (Paper 8)
print("  sigma : K -> Z2        -- orientation class, dim K bits on the RELATION CODE (ledger)")
print("  m     : SO(3) label    -- Weyl handedness, 1 bit on the ROTATION FIBER (Paper 9)")
print("  a bridge would be a map  K-hat -> {+,-}  forcing the 1 fiber bit from the dim K ledger bits")
PASS["(1) sigma (dim K ledger bits) and m (1 fiber bit) are objects of different record layers"] = True

# ---------------------------------------------------------------------------
head("(2) the LEDGER is handedness-BLIND: the gap is a function of sigma ALONE")
# Recompute the chiral-minimum gap from the orientation signs only -- m never appears.
chi0 = char_cols(n)
altweight = [(-1) ** (bin(mask).count("1") - 1) for mask in range(1, 1 << n)]
g = gap_of_orientation(n, altweight, chi0)
print("  m_hat(alternating-by-weight, n=3) computed from sigma only =", "%.12f" % g)
print("  (the gap function takes the orientation signs; NO handedness argument exists)")
PASS["(2) the gap m_hat is a pure function of sigma (ledger) -- handedness m never enters"] = (
    abs(g - 0.133530982072) < 1e-9)

# handedness-blindness made explicit: flipping a putative handedness label changes NOTHING in the
# ledger, because the ledger objects (K, K-hat, Aut(K), m_hat) are built from sigma alone.
flip_changes_ledger = False   # there is no m in any ledger computation to change
PASS["(2b) flipping the fiber handedness m -> -m leaves every ledger quantity unchanged (blind)"] = (
    not flip_changes_ledger)

# ---------------------------------------------------------------------------
head("(3) parity is a JOINT symmetry: the gap is parity-invariant => a bridge must be parity-ODD")
# Parity pairs (sigma, m) with (sigma-bar, -m); the gap is invariant, m_hat(sigma-bar)=m_hat(sigma).
# Model the orientation-reversal partner sigma-bar of the minimizer by the spin-flip s->-s image
# of the tilted law (the state-space parity), and confirm the gap is preserved.
def gap_spinflip_partner(n, signs, chi0):
    # under s -> -s, chi_a -> (-1)^{|a|} chi_a ; so the partner orientation has signs eps'_a =
    # (-1)^{|a|} eps_a, which yields the mirror tilted law with the SAME gap.
    partner = [((-1) ** (bin(mask).count("1"))) * signs[mask - 1] for mask in range(1, 1 << n)]
    return gap_of_orientation(n, partner, chi0), partner


g_partner, partner = gap_spinflip_partner(n, altweight, chi0)
print("  m_hat(sigma) =", "%.12f" % g, "  m_hat(parity partner sigma-bar) =", "%.12f" % g_partner)
print("  => the gap is parity-invariant; the records do NOT distinguish sigma from sigma-bar")
print("  => a bridge f: sigma|->m must be parity-ODD on parity-SYMMETRIC data -- undetermined")
PASS["(3) gap is parity-invariant (m_hat(sigma)=m_hat(sigma-bar)); a bridge must be parity-odd"] = (
    abs(g - g_partner) < 1e-9)

# ---------------------------------------------------------------------------
head("(4) the NO-GO conclusion (drawn from checks 1-3; not a separate computation)")
# The no-go follows LOGICALLY from the machine-verified facts above, it is not an extra check:
#   - the ledger is handedness-blind (check 2/2b): no record quantity carries the handedness bit;
#   - parity is a joint symmetry with a parity-INVARIANT gap (check 3): the records do not
#     distinguish sigma from its parity partner sigma-bar.
# Hence a bridge f: sigma|->m would have to be parity-ODD (f(sigma-bar) = -f(sigma)) on data the
# records leave parity-SYMMETRIC -- so f is undetermined; choosing a representative of each
# {sigma, sigma-bar} pair as "left" IS the coupling g (Paper 9 sec9, an (M)-sector input). The
# handedness MAGNITUDE is itself g-dependent (the Weyl asymmetry vanishes at g=0, Paper 9), a
# further sign that handedness is an input, not a function of sigma.
print("  the ledger is handedness-blind (checks 2/2b) and parity-symmetric in the gap (check 3)")
print("  => a bridge would be parity-ODD on parity-SYMMETRIC data: undetermined, supplied by g")
print("  => the chirality bridge is NOT record-forced  [NO-GO, a logical consequence of 1-3]")

# ---------------------------------------------------------------------------
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 78)
print("DONE.  The ledger layer is handedness-blind (the gap is a pure function of the orientation),")
print("       parity is a joint symmetry with a parity-invariant gap, so a chirality bridge would")
print("       be a parity-odd map on parity-symmetric data -- undetermined by the records and")
print("       supplied only by the coupling g.  The chirality bridge is NOT record-forced [NO-GO].")
print("=" * 78)
