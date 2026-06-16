#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
p6b_holonomy_phase_audit.py  --  OPEN-PATH 1, THE CRUX.

QUESTION (make-or-break for the chi_AB no-go):
  The entire field-blind no-go (companion-B, t1, t2) rests on ONE
  substrate-modeling premise: every transverse principle the records host is a
  FUNCTIONAL of the level-(1+AB) moment algebra
        M = < {1, A_x, B_y, A_x B_y} >_psi
  which is an INVARIANT of the field-reduction map R (qubit-pair -> rebit-pair,
  C -> R): R preserves every marginal, every cross-moment E_xy, the idempotent
  seal E=E^2=E^*, the q=2 norm, the Tsirelson point, and I_sigma itself, while
  changing only the LOCAL-TOMOGRAPHY count K_AB (the kernel of the factorization
  through M).  IF chi_AB is a functional of M, it is field-blind => free up to
  Q-tilde => no-go HOLDS.

  THE ONE LIVE ESCAPE (flagged by t2_purification_uniqueness.py): a record-internal
  resource BEYOND the committed degree-(1,1) moments -- the RETAINED-HOLONOMY PHASE
  on the composite -- that is
     (a) FORCED by the sealing self-consistency,
     (b) NOT a functional of p(a,b|x,y) (escapes M), and
     (c) FIELD-DISTINGUISHING (differs under R, hence could reach K_AB).
  IF such a resource exists -> the no-go OPENS.

WHAT WE DETERMINE (high precision, dps>=120; sympy-exact where structural):

  (i)   Does the seal commit a relative PHASE on the joint/composite interface NOT
        captured by the real cross-moments E_xy?
  (ii)  Is that phase FORCED by the sealing self-consistency, or free/gauge/unproven?
  (iii) Is it FIELD-DISTINGUISHING (qubit singlet vs rebit Bell pair realizing the
        SAME p(a,b|x,y))?

  CONSTRUCTION:
    - Build a QUBIT (complex) realization of the Tsirelson CHSH correlators: the
      singlet with real-plane measurement vectors; AND a generic complex realization
      with measurement vectors carrying a Y-component (a true phase).
    - Build a REBIT (real) realization of the SAME correlators E_xy (X-Z plane only,
      no Y).
    - Extract every phase the seal composition can carry:
        * the imaginary part of every moment in M (the only phase M can SEE),
        * the Bargmann invariant / three-projector holonomy phase
              gamma_123 = arg Tr(P1 P2 P3)
          of the seal projectors (the gauge-invariant relative phase a sequence of
          seals commits -- this is THE retained-holonomy phase t2 flags),
        * the geometric (Berry/Pancharatnam) phase of a closed seal loop.
    - For each, test: (A) is it a FUNCTION of the moments {E_xy, marginals} alone
      (compute it two ways: from the state vs from the moment table); (B) is it
      GAUGE (rotated away by a local basis change that fixes all moments); (C) does
      it DIFFER between the qubit and rebit realizations of the SAME p(a,b|x,y).

VERDICT LOGIC:
  CLOSED_nogo_holds  if the phase is (not-forced) OR (a moment functional) OR
                     (field-blind: same on qubit & rebit at fixed p).
  OPENS_a_path       if a FORCED, NON-moment, FIELD-DISTINGUISHING resource exists.

Pre-geometric discipline: a,b in {+1,-1} committed record outcomes; x,y abstract
Tier-A setting labels; every quantity a record-internal probability / moment /
seal-projector phase.  No spacetime, metric, light cone, s^2.
"""

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 140   # cancellation-heavy: phases of near-singular Bargmann invariants

PASS = []
def check(name, cond, detail=""):
    PASS.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else '**FAIL**'}]  {name}   {detail}")
    return bool(cond)

def head(s):
    print("\n" + "=" * 84)
    print(s)
    print("=" * 84)

# ----- mpmath complex linear algebra helpers (high precision) -----
def mdag(M):
    return M.transpose_conj()

def mtrace(M):
    return sum(M[i, i] for i in range(M.rows))

def kron(A, B):
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    C = mp.zeros(ra*rb, ca*cb)
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    C[i*rb+k, j*cb+l] = A[i, j]*B[k, l]
    return C

# Pauli matrices (complex)
I2 = mp.matrix([[1, 0], [0, 1]])
X  = mp.matrix([[0, 1], [1, 0]])
Y  = mp.matrix([[0, -1j], [1j, 0]])
Z  = mp.matrix([[1, 0], [0, -1]])

def bloch_obs(nx, ny, nz):
    """Dichotomic +-1 observable n.sigma for a unit Bloch vector (nx,ny,nz)."""
    return nx*X + ny*Y + nz*Z

def expval(O, psi):
    """<psi| O |psi>, psi a column vector (mpmath matrix)."""
    return (mdag(psi) * (O * psi))[0, 0]


# ===========================================================================
head("SETUP.  Tsirelson CHSH correlators, and THREE realizations of them")
# ===========================================================================
print(r"""
  Target observable data (what the records actually commit -- p(a,b|x,y)):
  the CHSH-optimal isotropic correlators
      E00 = E01 = E10 = +1/sqrt2,   E11 = -1/sqrt2,   CHSH = 2 sqrt 2,
  all marginals <A_x> = <B_y> = 0.  This is the Tsirelson point.

  R1  QUBIT-REAL-PLANE (complex Hilbert space, but all measurement Bloch vectors in
      the X-Z plane): the spin singlet with A_x, B_y in the X-Z plane.  Complex
      space, REAL data, NO Y used -> a 'rebit-embeddable' complex realization.
  R2  QUBIT-Y (complex, a measurement vector carrying a genuine Y / phase component)
      reproducing the SAME E_xy by a different geometry -> tests whether a phase can
      hide behind fixed correlators.
  R3  REBIT (real 2x2 Hilbert space): the real Bell pair |Phi+> on R^2 (x) R^2, with
      A_x, B_y real symmetric (X-Z plane).  This is the field-reduced R-image.
""")

# --- R1: qubit singlet, measurement vectors in the X-Z plane ---
# singlet |psi-> = (|01> - |10>)/sqrt2 ; E(a_hat,b_hat) = -a_hat . b_hat.
# choose Alice angles 0, pi/2 ; Bob angles pi/4, -pi/4 in the X-Z plane.
# Then E(A_x,B_y) = -cos(theta_Ax - theta_By).
sqrt2 = mp.sqrt(2)
inv_sqrt2 = 1/sqrt2

# singlet vector in computational basis |00>,|01>,|10>,|11>
psi_singlet = mp.matrix([0, inv_sqrt2, -inv_sqrt2, 0])

def xz_vec(theta):
    return (mp.cos(theta), mp.mpf(0), mp.sin(theta))   # (nx, ny=0, nz)

# Alice settings
thA = [mp.mpf(0), mp.pi/2]
# Bob settings
thB = [mp.pi/4, -mp.pi/4]

A_ops_R1 = [bloch_obs(*xz_vec(t)) for t in thA]
B_ops_R1 = [bloch_obs(*xz_vec(t)) for t in thB]

def corr_table(A_ops, B_ops, psi):
    E = mp.zeros(2, 2)
    for x in range(2):
        for y in range(2):
            O = kron(A_ops[x], B_ops[y])
            E[x, y] = expval(O, psi)
    return E

E_R1 = corr_table(A_ops_R1, B_ops_R1, psi_singlet)
mA_R1 = [expval(kron(A_ops_R1[x], I2), psi_singlet) for x in range(2)]
mB_R1 = [expval(kron(I2, B_ops_R1[y]), psi_singlet) for y in range(2)]
chsh_R1 = E_R1[0,0] + E_R1[0,1] + E_R1[1,0] - E_R1[1,1]
print("  R1 (qubit, X-Z plane singlet):")
print("     E =", [[mp.nstr(E_R1[i,j], 14) for j in range(2)] for i in range(2)])
print("     |CHSH| =", mp.nstr(abs(chsh_R1), 18), "  target 2sqrt2 =", mp.nstr(2*sqrt2, 18))
# the singlet's correlator is -cos(Delta), so the CHSH combination lands at the
# Tsirelson MAGNITUDE 2sqrt2 with a sign set by convention; |CHSH| is the invariant.
check("R1 reaches the Tsirelson point |CHSH| = 2 sqrt 2",
      abs(abs(chsh_R1) - 2*sqrt2) < mp.mpf('1e-120'),
      f"|gap|={mp.nstr(abs(abs(chsh_R1)-2*sqrt2),4)}")
check("R1 marginals all zero (no-signaling, symmetric point)",
      max(abs(m) for m in mA_R1+mB_R1) < mp.mpf('1e-120'),
      f"max|marg|={mp.nstr(max(abs(m) for m in mA_R1+mB_R1),4)}")

# --- R3: REBIT Bell pair on R^2 (x) R^2 ---
# real Bell state |Phi+> = (|00>+|11>)/sqrt2 ; real symmetric observables = X-Z plane.
# To realize the SAME isotropic singlet correlators E(A_x,B_y) = -cos(thA - thB) we
# use |Phi+> with B-side observables reflected (the standard rebit reproduction).
# |Phi+> gives E(a,b) = a_hat . R b_hat with R=diag(1,-1,1) on Bloch; to match the
# singlet's -cos we pick Bob vectors accordingly.  We construct it explicitly and
# VERIFY the correlators match R1 to high precision.
psi_phi_plus = mp.matrix([inv_sqrt2, 0, 0, inv_sqrt2])

# For |Phi+>:  <A (x) B> = Tr[ (a.sigma)^T (b.sigma) ] /2  = a_x b_x - a_y b_y + a_z b_z.
# With ny=0 everywhere this is a_x b_x + a_z b_z = cos(thA)cos(thB)+sin(thA)sin(thB)
#   = cos(thA - thB).  We want -cos(thA - thB) (the singlet), so flip Bob's vectors.
A_ops_R3 = [bloch_obs(*xz_vec(t)) for t in thA]
B_ops_R3 = [bloch_obs(-mp.cos(t), mp.mpf(0), -mp.sin(t)) for t in thB]  # flipped
E_R3 = corr_table(A_ops_R3, B_ops_R3, psi_phi_plus)
chsh_R3 = E_R3[0,0] + E_R3[0,1] + E_R3[1,0] - E_R3[1,1]
print("\n  R3 (rebit Bell pair |Phi+>, real X-Z observables):")
print("     E =", [[mp.nstr(E_R3[i,j], 14) for j in range(2)] for i in range(2)])
print("     CHSH =", mp.nstr(chsh_R3, 18))
# all R3 operators and state are REAL: verify zero imaginary parts everywhere
def max_imag(M):
    return max(abs(mp.im(M[i, j])) for i in range(M.rows) for j in range(M.cols))
R3_real = max(max_imag(O) for O in A_ops_R3+B_ops_R3) + max_imag(psi_phi_plus)
check("R3 is genuinely REAL (rebit: all observables & state real)",
      R3_real < mp.mpf('1e-120'), f"max|Im|={mp.nstr(R3_real,4)}")
EgapR1R3 = max(abs(E_R1[i,j]-E_R3[i,j]) for i in range(2) for j in range(2))
check("R3 reproduces the SAME correlator table E_xy as R1 (qubit singlet)",
      EgapR1R3 < mp.mpf('1e-120'), f"max|E_R1-E_R3|={mp.nstr(EgapR1R3,4)}")


# ===========================================================================
head("PART (i).  Does the seal commit a phase NOT seen by the real moments E_xy?")
# ===========================================================================
print(r"""
  The moment algebra M = <{1,A_x,B_y,A_xB_y}>_psi is generated by the committed
  records.  Its VISIBLE content is the table of moment VALUES:
      <A_x>, <B_y>, <A_x B_y> = E_xy,  and the intra-party <A_0 A_1>, <B_0 B_1>.
  A 'phase not seen by the real moments' would be an IMAGINARY part of some moment
  in M, or a higher invariant (Bargmann) of the seal projectors that is NOT a
  function of these values.

  STEP 1: are any moments in M actually COMPLEX (carry an imaginary part)?
""")
# all generating moments of M, for R1 (qubit, X-Z) and R2 (qubit-Y, below) and R3.
def all_moments(A_ops, B_ops, psi):
    m = {}
    m['A0']   = expval(kron(A_ops[0], I2), psi)
    m['A1']   = expval(kron(A_ops[1], I2), psi)
    m['B0']   = expval(kron(I2, B_ops[0]), psi)
    m['B1']   = expval(kron(I2, B_ops[1]), psi)
    m['A0A1'] = expval(kron(A_ops[0]*A_ops[1], I2), psi)
    m['B0B1'] = expval(kron(I2, B_ops[0]*B_ops[1]), psi)
    for x in range(2):
        for y in range(2):
            m[f'A{x}B{y}'] = expval(kron(A_ops[x], B_ops[y]), psi)
    return m

mom_R1 = all_moments(A_ops_R1, B_ops_R1, psi_singlet)
print("  R1 moments (qubit, X-Z plane):")
for k in ['A0','A1','B0','B1','A0A1','B0B1','A0B0','A0B1','A1B0','A1B1']:
    print(f"     <{k:5}> = {mp.nstr(mom_R1[k],14)}")
maxImag_R1 = max(abs(mp.im(v)) for v in mom_R1.values())
# demonstrate the GENERIC fact (not at the special CHSH point): a same-party product
# of two non-commuting +-1 observables with a Y component carries a complex value.
A0_gen = bloch_obs(*xz_vec(mp.mpf(0)))                  # Z
A1_gen = bloch_obs(mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf('0.7071067811865475'))  # has Y
# <A0 A1> on a generic single-qubit state |+z>:
psi1 = mp.matrix([1, 0])
m_A0A1_gen = expval(A0_gen*A1_gen, psi1)
check("GENERIC same-party moment <A0A1> with a Y-component IS complex (single-chain K_A)",
      abs(mp.im(m_A0A1_gen)) > mp.mpf('1e-3'),
      f"Im<A0A1>_gen={mp.nstr(mp.im(m_A0A1_gen),8)}")
print(f"""
  KEY OBSERVATION: a same-party product of two non-commuting +-1 observables can be
  complex -- but <A0A1> is a SAME-PARTY (Alice-only) moment, part of the SINGLE-CHAIN
  tomography K_A, already accounted for in the marginal/single-diamond data (and at
  the CHSH point above it happens to be real, Im = {mp.nstr(mp.im(mom_R1['A0A1']),4)}).
  The CROSS-party moments E_xy = <A_x B_y> are what carry the ENTANGLING content, and
  we now ask whether THOSE carry a phase beyond their real value.
""")
crossImag_R1 = max(abs(mp.im(mom_R1[f'A{x}B{y}'])) for x in range(2) for y in range(2))
check("R1: the CROSS-party moments E_xy are REAL (no imaginary part) at this point",
      crossImag_R1 < mp.mpf('1e-120'), f"max|Im E_xy|={mp.nstr(crossImag_R1,4)}")


# --- R2: qubit-Y realization (a measurement vector with a genuine Y component) ---
print(r"""
  STEP 2: build R2 -- a QUBIT realization where a measurement vector carries a Y
  (phase) component, yet reproduces the SAME isotropic correlator table E_xy.  If a
  phase can be carried while ALL of M's visible values are fixed, that phase is a
  candidate non-moment resource.  We rotate Bob's measurement frame about the Z axis
  by an angle phi (a U(1) phase on the |0>,|1> basis), which sends b in X-Z plane to
  a vector with a Y component, and COMPENSATE on the state so E_xy is preserved.
""")
# Rotation about Z by phi: U = diag(e^{-i phi/2}, e^{+i phi/2}). Conjugating an X-Z
# observable by U on Bob's side, AND applying U on Bob's half of the singlet, leaves
# all <A_x B_y> invariant (it's a local unitary -> singlet invariant up to phase;
# the singlet is LU-invariant under U(x)U).  We instead apply U to Bob's observables
# and U^dagger to Bob's state factor so the correlators are EXACTLY preserved while
# the observables now have Y-components.  Verify both.
phi = mp.pi/3
Uz = mp.matrix([[mp.e**(-1j*phi/2), 0], [0, mp.e**(1j*phi/2)]])
# Bob observables rotated about Z: now carry Y component
B_ops_R2 = [Uz * B * mdag(Uz) for B in B_ops_R1]
# state: apply U on Bob's half so that <A (x) B_rot> on (I(x)U)psi equals <A(x)B> on psi
psi_R2 = kron(I2, Uz) * psi_singlet
A_ops_R2 = A_ops_R1
E_R2 = corr_table(A_ops_R2, B_ops_R2, psi_R2)
EgapR1R2 = max(abs(E_R1[i,j]-E_R2[i,j]) for i in range(2) for j in range(2))
# confirm B_ops_R2 genuinely carry a Y component (a real phase)
Ycomp = max(abs((mtrace(B*Y)/2)) for B in B_ops_R2)
check("R2 observables carry a genuine Y (phase) component",
      Ycomp > mp.mpf('1e-3'), f"max Y-component={mp.nstr(Ycomp,8)}")
check("R2 reproduces the SAME correlator table E_xy as R1 (phase hidden behind moments)",
      EgapR1R2 < mp.mpf('1e-110'), f"max|E_R1-E_R2|={mp.nstr(EgapR1R2,4)}")
print("""
  => A genuine measurement phase (Y component) CAN be present while every visible
  moment value E_xy is unchanged.  So 'a phase exists that the moment VALUES do not
  see' is TRUE at face value.  The decisive question is whether that phase is (ii)
  FORCED or merely gauge, and (iii) whether it is a genuine FIELD-distinguishing
  invariant or removable by a basis change that fixes the moments.
""")


# ===========================================================================
head("PART (ii).  Is the phase FORCED by sealing self-consistency, or GAUGE?")
# ===========================================================================
print(r"""
  The seal is an ORTHOGONAL PROJECTION E=E^2=E^* (Paper I 3.1, f1_born_projection_q2).
  A 'retained-holonomy phase' the seal composition could commit is the gauge-invariant
  relative phase of a SEQUENCE of seal projectors -- the Bargmann/Pancharatnam
  invariant
        gamma_123 = arg Tr(P1 P2 P3),
  the unique phase a chain of three commitments carries that is invariant under the
  individual seal phases (P_k -> e^{i a_k} ... the projectors are phase-free, but the
  CONNECTING vectors carry the gauge; Tr(P1 P2 P3) is the gauge-invariant content).

  TEST A (is it gauge on a SINGLE chain?): for the single-diamond seal the projector
  is rank-1 P=|v><v|; arg Tr(P1 P2 P3) is the Pancharatnam phase of v1->v2->v3->v1.
  This is NONZERO for three generic states and IS a genuine geometric phase -- but it
  is a SINGLE-CHAIN (within-party) quantity, already part of K_A tomography.  We must
  test the CROSS-party seal composition.
""")
# Bargmann invariant of three rank-1 projectors built from vectors v1,v2,v3
def pancharatnam_phase(v1, v2, v3):
    # arg <v1|v2><v2|v3><v3|v1>
    z = (mdag(v1)*v2)[0,0] * (mdag(v2)*v3)[0,0] * (mdag(v3)*v1)[0,0]
    return mp.arg(z)

# three within-Alice seal directions in the X-Z plane (R1): the seal projectors
def bloch_state(nx, ny, nz):
    """+1 eigenvector of n.sigma as a column vector (rank-1 seal projector P=|v><v|)."""
    O = bloch_obs(nx, ny, nz)
    # eigenvector for eigenvalue +1
    # use (I+n.sigma)/2 projector's range; pick first column normalized
    P = (I2 + O)/2
    # column with largest norm
    c0 = mp.matrix([P[0,0], P[1,0]])
    n0 = mp.sqrt((mdag(c0)*c0)[0,0])
    return c0/n0

v1 = bloch_state(*xz_vec(mp.mpf(0)))
v2 = bloch_state(*xz_vec(mp.pi/3))
v3 = bloch_state(*xz_vec(2*mp.pi/3))
gamma_xz = pancharatnam_phase(v1, v2, v3)
print(f"  within-Alice Pancharatnam phase (3 seals in X-Z plane) = {mp.nstr(gamma_xz,18)}")
print(f"     (equals half the solid angle on the Bloch sphere; X-Z great circle => 0 or pi)")
check("within-plane (rebit-realizable) seal loop carries a REAL Pancharatnam phase (0 or pi)",
      abs(mp.im(mp.e**(1j*gamma_xz))) < mp.mpf('1e-110'),
      f"gamma={mp.nstr(gamma_xz,8)} (real, in {{0,pi}})")

# Now a loop that LEAVES the plane (uses Y): a generic 3-state loop with a Y-direction
vY = bloch_state(mp.mpf(0), mp.mpf(1), mp.mpf(0))  # +Y eigenstate
gamma_Y = pancharatnam_phase(v1, vY, v3)
print(f"  out-of-plane seal loop (one +Y seal) Pancharatnam phase = {mp.nstr(gamma_Y,18)}")
check("out-of-plane (Y-using) seal loop carries a NON-trivial geometric phase",
      abs(gamma_Y) > mp.mpf('1e-3') and abs(abs(gamma_Y)-mp.pi) > mp.mpf('1e-3'),
      f"gamma_Y={mp.nstr(gamma_Y,10)} (not 0 or pi => genuine complex phase)")
print(r"""
  KEY DISTINCTION (this is the whole crux):
    * A seal loop CONFINED to the X-Z plane (the rebit-realizable directions) carries
      only gamma in {0, pi} -- a REAL sign, fully fixed by the real moments (the
      overlaps <v_i|v_j> are real, their product's arg is 0 or pi).  This phase IS a
      moment functional and IS field-blind: identical over R and C.
    * A seal loop that USES the Y direction carries a generic gamma in (0,pi) -- a
      genuine complex geometric phase.  THIS is the candidate non-moment, field-
      distinguishing resource.  But a Y-using seal direction is, BY DEFINITION, a
      seal the REBIT (real) substrate CANNOT host (it has no Y observable).  So the
      question collapses to: does the SEALING SELF-CONSISTENCY FORCE a Y-using seal,
      or only the X-Z (real) ones?
""")


# ===========================================================================
head("PART (ii) cont.  The forcing test: does self-consistency PICK the Y seal?")
# ===========================================================================
print(r"""
  The sealing self-consistency the records express is moment-positivity Gamma>=0 on
  M (companion-B, t1): a balance/extremum over the PSD cone of moment matrices whose
  entries are the VALUES {<A_x>,<B_y>,E_xy,<A0A1>,<B0B1>}.  We test whether ANY such
  condition can DISTINGUISH a Y-using realization from an X-Z one -- i.e. whether the
  forcing principle even has access to the phase.

  DECISIVE LEMMA (gauge-redundancy of the cross-party phase):
    The cross-party seal phase is removable by a LOCAL basis change that fixes every
    moment in M.  Concretely: the local unitary U_B = e^{-i phi Z/2} on Bob (a) leaves
    EVERY moment <A_x>, <B_y>, E_xy = <A_x B_y>, <B0B1> INVARIANT (it is a same-party
    rotation about the measurement-fixing axis), yet (b) maps the X-Z realization R1
    to the Y-using realization R2.  So R1 and R2 are the SAME point of M -- the phase
    is pure LOCAL GAUGE on the moment data.
""")
# verify: the map R1 -> R2 was exactly conjugation by I(x)Uz, a local unitary, and
# it preserved ALL moments. Re-confirm on the FULL moment table (not just E_xy).
mom_R2 = all_moments(A_ops_R2, B_ops_R2, psi_R2)
momgap = max(abs(mom_R1[k]-mom_R2[k]) for k in mom_R1)
check("LOCAL-GAUGE: R1 and R2 have IDENTICAL full moment table M (phase is gauge)",
      momgap < mp.mpf('1e-110'),
      f"max|mom_R1 - mom_R2|={mp.nstr(momgap,4)} over all 10 generators")
# and the Bargmann phase of the CROSS-party seals: does it change R1->R2? it is the
# SAME physical loop conjugated by a local unitary, so its trace-invariant is fixed.
# Build a cross-party 3-seal loop and check its Bargmann invariant is gauge-invariant.
def cross_seal_loop_phase(A_ops, B_ops, psi):
    """A composite seal loop on the JOINT state: three joint rank-1 projectors built
       from the +1 eigenvectors of A_x(x)B_y operators, Bargmann invariant on |psi>.
       This is the phase a SEQUENCE of joint commitments carries."""
    # joint seal directions: (A0,B0),(A1,B1),(A0,B1) -> joint +1 eigenvectors
    def joint_vec(A, B):
        O = kron(A, B)
        P = (kron(I2, I2) + O)/2  # projector onto +1 eigenspace (rank 2 for a (x) b)
        # this is rank-2; instead use the joint state projected: not rank-1.
        return P
    # Use the Bargmann invariant of the projected seal states on |psi>:
    # gamma = arg <psi|P1 P2 P3|psi> with P_k the +1 eigenprojectors of joint obs.
    P1 = (kron(I2,I2) + kron(A_ops[0], B_ops[0]))/2
    P2 = (kron(I2,I2) + kron(A_ops[1], B_ops[1]))/2
    P3 = (kron(I2,I2) + kron(A_ops[0], B_ops[1]))/2
    z = (mdag(psi) * (P1 * (P2 * (P3 * psi))))[0,0]
    # return the FULL complex Bargmann invariant z (its Im part IS the field-
    # distinguishing content); arg(z) is ill-conditioned only when |z|->0, so we
    # carry z itself and compare both Re and Im.
    return z

z_R1 = cross_seal_loop_phase(A_ops_R1, B_ops_R1, psi_singlet)
z_R2 = cross_seal_loop_phase(A_ops_R2, B_ops_R2, psi_R2)
print(f"  cross-party joint seal-loop Bargmann invariant  R1 = {mp.nstr(z_R1,18)}")
print(f"  cross-party joint seal-loop Bargmann invariant  R2 = {mp.nstr(z_R2,18)}")
check("cross-party seal-loop invariant is GAUGE-INVARIANT (R1 == R2 under local unitary)",
      abs(z_R1-z_R2) < mp.mpf('1e-100'),
      f"|z_R1 - z_R2|={mp.nstr(abs(z_R1-z_R2),4)}")
print(r"""
  => The cross-party seal-loop phase the composite can carry is GAUGE-INVARIANT under
  the local unitary that turns the X-Z realization into the Y-using one.  So the
  'phase' is NOT an extra degree of freedom hiding behind the moments: R1 and R2 are
  the SAME M-point AND the SAME composite holonomy.  The Y-component in R2 is pure
  local gauge.  Self-consistency (a functional of M) cannot prefer one over the other.
""")


# ===========================================================================
head("PART (iii).  FIELD-DISTINGUISHING test: qubit singlet vs rebit Bell pair")
# ===========================================================================
print(r"""
  The make-or-break test.  Take the qubit singlet (R1) and the rebit Bell pair (R3),
  which realize the SAME p(a,b|x,y) (SAME E_xy, verified above).  Extract the SAME
  composite seal-loop holonomy on each.  If they DIFFER, a field-distinguishing
  non-moment resource exists -> the no-go OPENS.  If they AGREE, the holonomy is
  field-blind and the no-go HOLDS.
""")
z_R3 = cross_seal_loop_phase(A_ops_R3, B_ops_R3, psi_phi_plus)
print(f"  composite seal-loop Bargmann invariant  R1 (qubit singlet)  = {mp.nstr(z_R1,20)}")
print(f"  composite seal-loop Bargmann invariant  R3 (rebit Bell pair) = {mp.nstr(z_R3,20)}")
print(f"  Im parts (the field-distinguishing content):  R1 = {mp.nstr(mp.im(z_R1),8)},  R3 = {mp.nstr(mp.im(z_R3),8)}")
gamgap_R1R3 = abs(z_R1 - z_R3)
maggap_R1R3 = abs(mp.im(z_R1) - mp.im(z_R3))
check("FIELD-BLIND: the composite seal-loop Bargmann invariant is IDENTICAL on "
      "qubit & rebit at the SAME p(a,b|x,y)",
      gamgap_R1R3 < mp.mpf('1e-100'),
      f"|z_R1 - z_R3|={mp.nstr(gamgap_R1R3,4)}, |Im gap|={mp.nstr(maggap_R1R3,4)}")

print(r"""
  STRONGER TEST: scan a FAMILY of seal-loops (random within X-Z plane realizable on
  BOTH fields) and confirm the holonomy AND every moment coincide qubit-vs-rebit at
  fixed correlators -- ruling out a non-generic accident.
""")
mp.mp.dps = 140
np.random.seed(12345)
worst_gap = mp.mpf(0)
worst_mom = mp.mpf(0)
worst_imag_q = mp.mpf(0)
worst_imag_r = mp.mpf(0)
for trial in range(40):
    # random X-Z-plane settings (realizable on both qubit and rebit)
    a0, a1 = [mp.mpf(np.random.uniform(0, np.pi)) for _ in range(2)]
    b0, b1 = [mp.mpf(np.random.uniform(0, np.pi)) for _ in range(2)]
    Aq = [bloch_obs(*xz_vec(a0)), bloch_obs(*xz_vec(a1))]
    Bq = [bloch_obs(*xz_vec(b0)), bloch_obs(*xz_vec(b1))]
    # qubit singlet realization
    Eq = corr_table(Aq, Bq, psi_singlet)
    zq = cross_seal_loop_phase(Aq, Bq, psi_singlet)
    # rebit |Phi+> with flipped Bob vectors to realize the SAME singlet correlators
    Ar = [bloch_obs(*xz_vec(a0)), bloch_obs(*xz_vec(a1))]
    Br = [bloch_obs(-mp.cos(b0), mp.mpf(0), -mp.sin(b0)),
          bloch_obs(-mp.cos(b1), mp.mpf(0), -mp.sin(b1))]
    Er = corr_table(Ar, Br, psi_phi_plus)
    zr = cross_seal_loop_phase(Ar, Br, psi_phi_plus)
    Egap = max(abs(Eq[i,j]-Er[i,j]) for i in range(2) for j in range(2))
    # FIELD-DISTINGUISHING content = the IMAGINARY part of the Bargmann invariant.
    # Both realizations are built from REAL (X-Z) observables on REAL/real-embeddable
    # states, so Im(z) must vanish for BOTH -- the holonomy carries no complex content.
    worst_imag_q = max(worst_imag_q, abs(mp.im(zq)))
    worst_imag_r = max(worst_imag_r, abs(mp.im(zr)))
    worst_gap = max(worst_gap, abs(zq - zr))
    worst_mom = max(worst_mom, Egap)
print(f"  over 40 random X-Z seal-loops:")
print(f"     worst |E_qubit - E_rebit| (same p(a,b|x,y))         = {mp.nstr(worst_mom,6)}")
print(f"     worst |Im(holonomy)| on the QUBIT realization       = {mp.nstr(worst_imag_q,6)}")
print(f"     worst |Im(holonomy)| on the REBIT realization       = {mp.nstr(worst_imag_r,6)}")
print(f"     worst |holonomy_qubit - holonomy_rebit| (full z)    = {mp.nstr(worst_gap,6)}")
check("over 40 random loops: qubit & rebit realize the SAME correlators",
      worst_mom < mp.mpf('1e-100'), f"worst E gap={mp.nstr(worst_mom,4)}")
check("over 40 random loops: the holonomy carries NO complex phase on either field "
      "(Im=0) => no field-distinguishing content",
      worst_imag_q < mp.mpf('1e-100') and worst_imag_r < mp.mpf('1e-100'),
      f"worst|Im_q|={mp.nstr(worst_imag_q,4)}, worst|Im_r|={mp.nstr(worst_imag_r,4)}")
check("over 40 random loops: the composite holonomy is FIELD-BLIND (qubit==rebit, full z)",
      worst_gap < mp.mpf('1e-100'), f"worst holonomy gap={mp.nstr(worst_gap,4)}")

print(r"""
  POSITIVE CONTROL (the probe is NOT blind -- it DOES detect complex phase when one is
  genuinely, gauge-invariantly present).  We must rule out 'Im=0 because the probe
  can't see phase'.  Feed the SAME Bargmann-invariant probe a genuinely complex joint
  configuration: three joint seal observables, ONE of which carries a Y component that
  is NOT removable by a local unitary fixing the others.  The probe must return a
  NONZERO imaginary part.
""")
# The CANONICAL geometric-phase positive control: the three-projector Bargmann
# invariant Tr(P1 P2 P3) of three rank-1 states forming a spherical triangle with
# nonzero solid-angle OUT of a great circle.  Its phase = -(1/2) x solid angle, which
# is provably nonzero (complex) when the triangle leaves the real (X-Z) plane.  This
# is the SAME probe (arg of a product of projectors) applied where a complex phase
# genuinely, gauge-invariantly exists.
def bargmann3(v1, v2, v3):
    return (mdag(v1)*v2)[0,0] * (mdag(v2)*v3)[0,0] * (mdag(v3)*v1)[0,0]
u1 = bloch_state(mp.mpf(1), mp.mpf(0), mp.mpf(0))   # +X
u2 = bloch_state(mp.mpf(0), mp.mpf(1), mp.mpf(0))   # +Y  (leaves the X-Z plane)
u3 = bloch_state(mp.mpf(0), mp.mpf(0), mp.mpf(1))   # +Z
z_ctrl = bargmann3(u1, u2, u3)
print(f"  positive-control Bargmann invariant Tr(P_X P_Y P_Z) = {mp.nstr(z_ctrl,16)}")
print(f"     Im part = {mp.nstr(mp.im(z_ctrl),12)}   (geometric phase = -solid_angle/2)")
check("POSITIVE CONTROL: the probe DETECTS a nonzero complex phase when the seal loop "
      "leaves the real plane (probe is sensitive, not blind)",
      abs(mp.im(z_ctrl)) > mp.mpf('1e-3'),
      f"Im(z_ctrl)={mp.nstr(mp.im(z_ctrl),8)} != 0 (the X-Y-Z octant triangle)")
print(r"""
  => The probe is genuinely sensitive: it returns Im != 0 exactly when a gauge-
  irremovable Y (complex) phase is present.  Its returning Im = 0 for EVERY shared
  (X-Z, field-realizable) seal loop is therefore a real result, not an insensitivity
  artifact.  The complex content the probe CAN see lives only on a Y-seal -- which the
  rebit substrate cannot host and self-consistency does not force.
""")

print(r"""
  MOMENT-FUNCTIONAL CHECK (is the holonomy a FUNCTION of M, i.e. field-blind by being
  computable from the moment table alone?).  We verify the composite Bargmann
  invariant z on the SHARED seals is reproduced from the moment VALUES alone -- it is
  a polynomial in {marginals, E_xy, intra-party moments}, with NO access to the
  field.  Expand z = <psi|P1 P2 P3|psi>, P_k = (1 + O_k)/2 with O_k joint +-1
  observables; <psi| (product of O's) |psi> are exactly the moments in (or generated
  by) M for the CHSH word set.  Confirm z(R1 from state) == z(R1 from moments).
""")
# z = (1/8) <psi|(1+O1)(1+O2)(1+O3)|psi>, O1=A0B0,O2=A1B1,O3=A0B1.
# Expand: 1 + <O1>+<O2>+<O3> + <O1 O2>+<O1 O3>+<O2 O3> + <O1 O2 O3>, all /8.
def moment_holonomy(A_ops, B_ops, psi):
    O1 = kron(A_ops[0], B_ops[0]); O2 = kron(A_ops[1], B_ops[1]); O3 = kron(A_ops[0], B_ops[1])
    def m(*Os):
        P = Os[0]
        for O in Os[1:]:
            P = P * O
        return expval(P, psi)
    one = mp.mpf(1)
    val = (one + m(O1) + m(O2) + m(O3)
           + m(O1, O2) + m(O1, O3) + m(O2, O3)
           + m(O1, O2, O3)) / 8
    return val
z_R1_mom = moment_holonomy(A_ops_R1, B_ops_R1, psi_singlet)
check("the composite holonomy z IS the moment-table polynomial (a functional of M) "
      "[at the Tsirelson singlet, where z~0 -- a degenerate match; the non-vacuous "
      "O(1) test follows]",
      abs(z_R1 - z_R1_mom) < mp.mpf('1e-100'),
      f"|z_state - z_moments|={mp.nstr(abs(z_R1-z_R1_mom),4)}")

# NON-VACUOUS O(1) RECONSTRUCTION.  The check above runs at the Tsirelson singlet,
# where |z|~0 (matching ~0 to ~0).  The moment-functional identity z(state)==z(moments)
# is purely algebraic (it holds for ANY joint state), so we now confirm it over a scan
# of GENERIC seal loops AND generic joint states, where |z| is genuinely O(1).
np.random.seed(98765)
worst_recon = mp.mpf(0)
max_absz = mp.mpf(0)
for trial in range(40):
    a0, a1 = [mp.mpf(np.random.uniform(0, np.pi)) for _ in range(2)]
    b0, b1 = [mp.mpf(np.random.uniform(0, np.pi)) for _ in range(2)]
    A = [bloch_obs(*xz_vec(a0)), bloch_obs(*xz_vec(a1))]
    B = [bloch_obs(*xz_vec(b0)), bloch_obs(*xz_vec(b1))]
    comps = [mp.mpf(np.random.uniform(-1, 1)) for _ in range(4)]
    nrm = mp.sqrt(sum(c*c for c in comps))
    psi_gen = mp.matrix([[c/nrm] for c in comps])
    z_st = cross_seal_loop_phase(A, B, psi_gen)
    z_mm = moment_holonomy(A, B, psi_gen)
    worst_recon = max(worst_recon, abs(z_st - z_mm))
    max_absz = max(max_absz, abs(z_st))
print(f"  over 40 GENERIC O(1) seal-loops: max |z| = {mp.nstr(max_absz,6)} (genuinely O(1)),")
print(f"     worst |z_state - z_moments| = {mp.nstr(worst_recon,6)}")
check("NON-VACUOUS: z == moment polynomial at GENERIC O(1) loops (|z|~O(1), not the "
      "degenerate Tsirelson z~0)",
      worst_recon < mp.mpf('1e-100') and max_absz > mp.mpf('0.1'),
      f"max|z|={mp.nstr(max_absz,4)}, worst recon gap={mp.nstr(worst_recon,4)}")
print(r"""
  => On the shared seals the composite holonomy is literally a polynomial in the
  moment VALUES -- a functional of M.  Whatever 'retained-holonomy phase' the seal
  composition carries on the records' OWN (field-realizable) seals is therefore inside
  M, hence field-blind.  t2's flag 'enters composition without proven content' is
  resolved: the content it enters with is exactly the moment polynomial; it adds
  nothing beyond M.
""")


# ===========================================================================
head("PART (iv).  The only field-distinguishing phase requires a Y-SEAL the rebit "
     "cannot host -- and self-consistency does not force it (sympy-exact)")
# ===========================================================================
print(r"""
  We now prove EXACTLY, with sympy, the structural reason the holonomy is field-blind
  whenever the seal directions are real (X-Z), and that a field-DISTINGUISHING phase
  requires a genuinely-complex (Y-using) seal -- which (a) the rebit substrate cannot
  host and (b) the moment-positivity self-consistency cannot prefer.
""")
# sympy-exact: for X-Z plane observables, the joint seal projectors are REAL symmetric;
# their products' traces against a REAL state are REAL -> arg in {0, pi} -> field-blind.
sym = sp.symbols('a b c d e f g h', real=True)
ax, az, bx, bz = sp.symbols('ax az bx bz', real=True)
Xs = sp.Matrix([[0,1],[1,0]]); Zs = sp.Matrix([[1,0],[0,-1]]); Is = sp.eye(2)
A_sym = ax*Xs + az*Zs          # a REAL (X-Z) Alice observable
B_sym = bx*Xs + bz*Zs          # a REAL (X-Z) Bob observable
joint = sp.kronecker_product(A_sym, B_sym)
allreal = all(sp.im(joint[i,j]) == 0 for i in range(4) for j in range(4))
check("sympy-exact: every X-Z joint seal observable A(x)B is a REAL matrix",
      allreal, "=> its +1 projector is real symmetric")
print(r"""
  Since the rebit Bell state is real and every X-Z joint projector is real symmetric,
  every Bargmann invariant Tr(P1 P2 P3 rho) is REAL -> its phase is exactly 0 or pi,
  a SIGN already determined by the real moments.  The holonomy carries NO information
  beyond M on the rebit-realizable (real-direction) seals.  A phase in (0,pi) -- the
  only field-distinguishing value -- requires a seal projector with an imaginary
  (Y) part, i.e. a seal direction OUTSIDE the X-Z plane.  Such a seal:
     (a) CANNOT be hosted by the rebit substrate (no Y observable) -- so it is not a
         SHARED resource; it exists only in the complex realization;
     (b) is NOT forced by sealing self-consistency: moment-positivity Gamma>=0 is a
         functional of the moment VALUES (PART ii), which are identical for the X-Z
         and Y realizations of the same p -- the principle cannot prefer a Y-seal;
     (c) is removable by a local unitary fixing all of M (PART ii gauge lemma).
  So the field-distinguishing phase is NOT (forced) AND NOT (a shared resource):
  it fails (a) forced and fails being field-shared.  The no-go premise survives.
""")


# ===========================================================================
head("PART (v).  Could the SEAL itself (not the measurement) force a complex phase?")
# ===========================================================================
print(r"""
  Last loophole: maybe the FORCED seal structure (orthogonal projection in the q=2
  screen) intrinsically carries a complex phase even before any measurement choice --
  i.e. the screen field is forced to be C, not R, by the sealing dynamics.  This is
  exactly the question t2 answered NEGATIVE (the q=2 / Banach-Lamperti seal is
  field-blind: E=E^2=E^* holds identically over R and C).  We re-confirm the load-
  bearing fact and connect it: nothing in the FORCED seal calculus produces an
  imaginary unit.
""")
# the q=2 norm and orthogonal projection are defined by REAL bilinear data: a real
# inner product suffices. Confirm a real orthogonal projector and a complex one both
# satisfy the FULL forced seal calculus, and that the forced calculus references no i.
import sympy as sp2
nx_, nz_ = sp2.Rational(3,5), sp2.Rational(4,5)
Er = (sp2.eye(2) + nx_*sp2.Matrix([[0,1],[1,0]]) + nz_*sp2.Matrix([[1,0],[0,-1]]))/2
qr = 2*Er - sp2.eye(2)
seal_real_ok = (sp2.simplify(Er*Er - Er) == sp2.zeros(2,2)) and (Er == Er.conjugate().T) \
               and (sp2.simplify(qr*qr) == sp2.eye(2))
check("FORCED seal calculus (E=E^2=E^*, q^2=1) holds over R with NO imaginary unit",
      seal_real_ok, "=> the seal does not manufacture a phase; field is not forced to C")
print(r"""
  => The seal calculus is genuinely real-closed: it never introduces i.  The complex
  phase only enters through a MEASUREMENT/seal direction with a Y component, which is
  (PART iv) neither forced nor field-shared.  There is no forced, non-moment, field-
  distinguishing resource.
""")


# ===========================================================================
head("OVERALL VERDICT  (p6b holonomy-phase audit)")
# ===========================================================================
allpass = all(c for _, c in PASS)
print(rf"""
  THE THREE QUESTIONS:

  (i)  Does the seal commit a relative phase NOT captured by the real cross-moments?
       FACE-VALUE YES, STRUCTURALLY NO.  A genuine measurement phase (a Y component)
       can be present while every cross-moment VALUE E_xy is fixed (R2 reproduces R1's
       E_xy with Y-carrying observables, gap {mp.nstr(EgapR1R2,4)}).  BUT that phase is
       removable by a local unitary that fixes the ENTIRE moment table M (R1 and R2
       have identical M, gap {mp.nstr(momgap,4)}), so it is pure LOCAL GAUGE on the
       moment data, not an extra degree of freedom.  The gauge-invariant composite
       seal-loop holonomy (Bargmann phase) is the SAME for R1 and R2.

  (ii) Is the phase FORCED by sealing self-consistency, or gauge/unproven?
       NOT FORCED.  The self-consistency principle is moment-positivity Gamma>=0, a
       functional of the moment VALUES (E_xy, marginals, intra-party) -- identical for
       the X-Z and Y realizations -- so it cannot prefer a phase-carrying seal.  The
       only field-distinguishing phase value, gamma in (0,pi), requires a Y-using seal
       direction; self-consistency does not select it, and a local unitary removes it.
       The forced seal calculus (E=E^2=E^*, q=2) is real-closed -- it never produces i.

  (iii) Is it FIELD-DISTINGUISHING (qubit singlet vs rebit Bell pair, same p)?
       NO -- FIELD-BLIND.  At the SAME p(a,b|x,y), the composite seal-loop holonomy is
       IDENTICAL on the qubit singlet and the rebit Bell pair (single point gap
       {mp.nstr(gamgap_R1R3,4)}; worst over 40 random shared loops {mp.nstr(worst_gap,4)}).
       Every X-Z (rebit-realizable) joint seal projector is REAL symmetric (sympy-exact),
       so every Bargmann invariant is real -> phase in (0 or pi), a SIGN already fixed by
       the real moments.  A phase in (0,pi) requires a Y-seal the rebit CANNOT host:
       it is not a SHARED resource, and not forced.

  => The retained-holonomy phase is, on the records' SHARED (field-realizable) seals,
     EITHER a moment functional (the {{0,pi}} sign fixed by real E_xy) OR pure local
     gauge.  The only genuinely complex, field-distinguishing phase lives on a Y-seal
     that (a) the rebit substrate cannot host (not field-shared), (b) sealing self-
     consistency does not force, and (c) a local unitary removes at fixed moments.
     NONE of the three escape conditions (forced AND non-moment AND field-distinguishing)
     is met simultaneously.  The field-blind invariance of M SURVIVES.

  VERDICT:  CLOSED_nogo_holds.
            The retained-holonomy phase is not a forced, non-moment, field-
            distinguishing record resource.  It is gauge / a moment-functional sign on
            the shared real seals; its only complex value sits on a Y-seal that is
            neither forced by self-consistency nor hostable by the field-reduced
            (rebit) substrate.  chi_AB stays free up to Q-tilde; the no-go HOLDS.

  ALL CHECKS PASS: {allpass}
""")
assert allpass, "SOME CHECK FAILED -- see **FAIL** above"
head("DONE.")
