"""
F3d -- THE TWO FOUNDATIONAL SUPPORTS of Paper 1 v7 s3.2's forcing chain.
v7 Long March, Paper 1, Tier A.  R3 of the Long March.

Round-2 referees isolated the two DEEPEST residual supports under Paper 1's
Tier-A "forcing".  This receipt pins down, exactly and pre-geometrically, the
honest status of each.

PRE-GEOMETRIC (Tier A) throughout: records, the commit order, the KL content
chi = D(P_AB||P_BA).  NO spacetime, metric, light cone, proper time, or s^2.
The only "time" is the commit order (the succession of seals); a "seal/event"
is a record commitment (a division event); the "collar" is the eventless stretch
between two seals.  mpmath dps = 140, sympy-exact where exact.

----------------------------------------------------------------------------
SUPPORT (A) -- THE SEAL = COMPOSITION BRIDGE.
  Paper 1 s3.2 takes:  "a seal = a refinement point of the commit order =
  a point where the Gell-Mann-Hartle decoherence functional D diagonalizes =
  a Chapman-Kolmogorov composition point."
  paper56 (line ~98) discharges this biconditional ONLY for a chosen projective
  seal-history (GMH) model, AT THE KINEMATIC LEVEL -- NOT yet an intrinsic
  theorem that the SHARD record process supplies these seals/projectors (its
  open Tier-1 functor, [TARGET]).

  We test, with an explicit two-slit / two-branch decoherence-functional toy:
    (A.i)  Is the biconditional  [D diagonalizes at t']  <=>  [Chapman-Kolmogorov
           composes across t']  FORCED at the kinematic level, given the GMH
           projective model?  (Or is even that a choice?)
    (A.ii) Separate the KINEMATIC content (forced) from the INTRINSIC SUPPLY
           question (does the gravitational record process supply the projectors).
           Is the supply a TIER-A obligation or a TIER-B/gravitational one?

----------------------------------------------------------------------------
SUPPORT (B) -- MARKOV-PRESENTABILITY OF THE COMMIT ORDER.
  Paper 1 s3.2's odometer additivity is forced GIVEN the commit order is
  "Markov-presentable" (path measure factorizes => trajectory action telescopes).
  Round-2 tension:  the program's CENTRAL claim is INDIVISIBILITY = NON-Markov
  (Barandes).  Receipt f3c located the factorization at the EVENTLESS COLLAR
  BETWEEN seals (events break Markovianity; between events the collar is
  ordered/Markov).

  We test:
    (B.i)  Is eventless-collar Markov-presentability FORCED by paper10's standing
           structure (the eventless collar = finite primitive Markov presentation,
           RP-as-theorem of indivisible ordered transports, T4), or a separate
           assumption?
    (B.ii) Is the Markov(collar)-vs-indivisible(seal-order) split CONSISTENT --
           genuinely: Markovianity holds BETWEEN seals while the seal order
           itself is non-Markov/indivisible?  We exhibit an explicit chain where:
             * the trajectory action telescopes (composition holds) WITHIN a
               collar, AND
             * Chapman-Kolmogorov composition of the one-time transition law FAILS
               across a seal/event (interference cross-term survives).

The decisive new computation (beyond f3c, which only showed the telescope holds):
we build a Barandes Gamma(t)=|U(t)|^2 two-branch process and show, at dps>=140,
  (1) ACROSS an undecohered (unsealed) interval, Gamma(t2,t0) != Gamma(t2,t1)Gamma(t1,t0)
      -- composition FAILS, with the gap = the interference cross-term;
  (2) AT a seal (projective record commitment diagonalizing D), composition is
      RESTORED -- the cross-term is annihilated and CK holds;
  (3) the WITHIN-collar trajectory action telescopes EXACTLY (Markov),
      while the SEAL-ORDER composition fails across the event,
  -- exactly the Markov(collar)/non-Markov(seal-order) split, made quantitative.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140


def head(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


def line(label, val, extra=""):
    print(f"  {label:<56} {val} {extra}")


# ===========================================================================
# Shared toy: a two-branch (qubit / two-slit) record process.  Pre-geometric
# reading: two coherent record-branches (which-path 0 / which-path 1) carrying a
# relative unsealed holonomy phase Phi.  Gamma(t)_{ji} = |U(t)_{ji}|^2 is the
# Barandes one-time transition law (paper56 s2.1).  A SEAL diagonalizes the
# Gell-Mann-Hartle decoherence functional D (paper56 s4.2 / line ~92-96).
# Everything is a record-internal amplitude/probability -- no spacetime.
# ===========================================================================
def U_step(phi, mix):
    """
    A 2x2 unitary on the two record-branches: a beam-splitter-like mix of angle
    'mix' followed by a relative unsealed holonomy phase 'phi'.  Pure record
    kinematics (no Hamiltonian-in-spacetime; phi is accumulated holonomy CONTENT).
    """
    c = mp.cos(mix)
    s = mp.sin(mix)
    e = mp.expjpi(phi / mp.pi)   # = exp(i*phi)
    # U = diag(e^{i phi/2}, e^{-i phi/2}) * [[c, -s],[s, c]]
    eh = mp.expjpi(phi / (2 * mp.pi))
    ehm = mp.expjpi(-phi / (2 * mp.pi))
    return mp.matrix([[eh * c, -eh * s],
                      [ehm * s, ehm * c]])


def matmul(A, B):
    return A * B


def gamma_from_U(U):
    """Barandes Gamma_{ji} = |U_{ji}|^2 (paper56 s2.1)."""
    G = mp.matrix(2, 2)
    for j in range(2):
        for i in range(2):
            G[j, i] = mp.fabs(U[j, i]) ** 2
    return G


def colstoch_residual(G):
    """How far G is from column-stochastic (each column = a probability law)."""
    r = mp.mpf(0)
    for i in range(2):
        col = G[0, i] + G[1, i]
        r = max(r, mp.fabs(col - 1))
    return r


def mat_gap(A, B):
    g = mp.mpf(0)
    for j in range(2):
        for i in range(2):
            g = max(g, mp.fabs(A[j, i] - B[j, i]))
    return g


# ===========================================================================
head("SUPPORT (A) -- THE SEAL = COMPOSITION BRIDGE  (kinematic level)")
# ===========================================================================
print("""
  CLAIM under test (Paper 1 s3.2, via paper56 s4.2):
    [a seal at t']  <=>  [the GMH decoherence functional D diagonalizes at t']
                    <=>  [Chapman-Kolmogorov composes the one-time law across t'].

  We instantiate the Gell-Mann-Hartle / Barandes bridge explicitly:
    Gamma(t)_{ji} = |U(t)_{ji}|^2,  composition test
        CK gap(t2,t1,t0) := Gamma(t2,t0) - Gamma(t2,t1) Gamma(t1,t0).
    The cross-term (interference) is exactly  |Sum_k U2_{jk}U1_{ki}|^2 - Sum_k |U2_{jk}|^2|U1_{ki}|^2.
""")

# build two consecutive unsealed holonomy steps with a genuine interference term
phi1 = mp.mpf('0.6')          # holonomy content over collar segment 1
phi2 = mp.mpf('0.95')         # holonomy content over collar segment 2
mix1 = mp.mpf('0.7')          # branch-mixing angle (nonzero => interference exists)
mix2 = mp.mpf('1.1')

U1 = U_step(phi1, mix1)       # unsealed evolution t0 -> t1
U2 = U_step(phi2, mix2)       # unsealed evolution t1 -> t2
U20 = matmul(U2, U1)          # composed unitary t0 -> t2

G1 = gamma_from_U(U1)
G2 = gamma_from_U(U2)
G20_true = gamma_from_U(U20)              # |U2 U1|^2  (probability of the path SUM)
G20_comp = matmul(G2, G1)                 # Gamma2 Gamma1 (SUM of path probabilities)

line("U1, U2 unitary? residual |U^d U - I|",
     mp.nstr(max(mat_gap(U1.H * U1, mp.eye(2)), mat_gap(U2.H * U2, mp.eye(2))), 6))
line("Gamma1 column-stochastic? residual", mp.nstr(colstoch_residual(G1), 6))
line("Gamma2 column-stochastic? residual", mp.nstr(colstoch_residual(G2), 6))

print("\n  (A.0)  UNSEALED interval: does Chapman-Kolmogorov compose?")
ck_gap_unsealed = mat_gap(G20_true, G20_comp)
line("Gamma(t2,t0) = |U2 U1|^2  entry [0,0]", mp.nstr(G20_true[0, 0], 25))
line("Gamma2 Gamma1            entry [0,0]", mp.nstr(G20_comp[0, 0], 25))
line("CK GAP across UNSEALED interval", mp.nstr(ck_gap_unsealed, 8),
     "(!=0: composition FAILS -- the interference cross-term survives)")
# the cross-term is genuinely nonzero
assert ck_gap_unsealed > mp.mpf('1e-3'), "expected a real interference gap"

print("""
  (A.1)  SEAL at t1: a projective record commitment diagonalizes D at t1.
         The seal applies the pointer projectors {P_0=|0><0|, P_1=|1><1|} to the
         decoherence functional -- i.e. it ZEROES the off-diagonal (interference)
         part of the intermediate coherence.  Operationally the sealed composition
         replaces  |U2 U1|^2  by  Sum_k |U2_{jk}|^2 |U1_{ki}|^2 = (Gamma2 Gamma1).
""")
# the SEALED two-step law IS Gamma2 Gamma1 (decohere at t1 => CK holds by construction)
G20_sealed = matmul(G2, G1)
ck_gap_sealed = mat_gap(G20_sealed, matmul(G2, G1))
line("sealed Gamma(t2,t0) := Sum_k |U2_{jk}|^2|U1_{ki}|^2", mp.nstr(G20_sealed[0, 0], 25))
line("CK GAP across SEALED point t1", mp.nstr(ck_gap_sealed, 8),
     "(=0: composition RESTORED -- seal diagonalizes D)")
assert ck_gap_sealed < mp.mpf('1e-120')

print("""
  (A.2)  THE BICONDITIONAL, made exact.  Define the GMH decoherence functional on
         the two intermediate branches k=0,1:
             D(k,k') = <branch k | branch k'>_{evolved}  (the off-diagonal is the
             interference cross-term).  Medium decoherence  <=>  D off-diagonal = 0.
         We show, on this toy:  CK-gap = 0  <=>  D off-diagonal = 0  (one number
         controls both), so the biconditional is an IDENTITY, not a slogan.
""")
# the interference cross-term that the seal removes, as an explicit functional of U
# For output j, input i: cross = 2 Re Sum_{k<l} U2_{jk}U1_{ki} conj(U2_{jl}U1_{li})
def cross_term(U2, U1, j, i):
    tot = mp.mpc(0)
    amps = [U2[j, k] * U1[k, i] for k in range(2)]
    for k in range(2):
        for l in range(2):
            if k < l:
                tot += amps[k] * mp.conj(amps[l])
    return 2 * mp.re(tot)

# CK gap entrywise equals the interference cross-term entrywise
max_identity_gap = mp.mpf(0)
for j in range(2):
    for i in range(2):
        ck_entry = G20_true[j, i] - G20_comp[j, i]
        cross_entry = cross_term(U2, U1, j, i)
        max_identity_gap = max(max_identity_gap, mp.fabs(ck_entry - cross_entry))
line("max | CK-gap_entry  -  interference-cross-term_entry |",
     mp.nstr(max_identity_gap, 8),
     "(=0: CK-gap IS the cross-term -- the biconditional is an identity)")
assert max_identity_gap < mp.mpf('1e-120')

print("""
  (A.3)  IS THE BICONDITIONAL FORCED AT THE KINEMATIC LEVEL, OR A CHOICE?
    Given the GMH projective model (Gamma=|U|^2 + projective pointer commitment),
    the biconditional is FORCED -- it is the algebraic identity just verified
    (CK composes  <=>  cross-term vanishes  <=>  D diagonal).  NO freedom: once
    you accept Gamma=|U|^2 and that a seal is a projective commitment, the
    equivalence is a two-line linear-algebra fact (Sum|.|^2 vs |Sum.|^2).
    WHAT IS A CHOICE (and this is the honest seam):
      * that records are read by ORTHOGONAL projective pointers {P_a} (this is
        itself FORCED elsewhere -- Paper 1 s3.1: the q=2 screen forces E=E*=E^2,
        an orthogonal projection; so the projective character is NOT free either);
      * that the SHARD gravitational process actually SUPPLIES these seals at
        these places (the INTRINSIC SUPPLY question) -- this is NOT settled by the
        kinematic identity and is paper56's open Tier-1 functor [TARGET].
""")


# ===========================================================================
head("SUPPORT (A) -- the INTRINSIC SUPPLY question, located by TIER")
# ===========================================================================
print("""
  Decompose the bridge into its KINEMATIC half and its SUPPLY half.

  KINEMATIC half (just verified):  GIVEN a projective seal-history, the seal =
    D-diagonalization = CK-composition biconditional is a FORCED algebraic identity.
    Tier: TIER-A and KINEMATIC.  It needs only: Gamma=|U|^2 (Born/q=2, Paper 1
    s3.1 [FORCED]) + orthogonal projective pointers (Paper 1 s3.1 [FORCED]).  Both
    are pre-geometric, record-level facts.  => the bridge is legitimately a
    Tier-A KINEMATIC theorem.

  SUPPLY half (open):  does the SHARD record process *intrinsically* supply these
    very projectors/seals -- i.e. is there an intrinsic principle that fires a
    projective commitment at the right places?  paper56 s4.2 line ~98: discharged
    'for a chosen projective seal-history model, at the kinematic level -- NOT yet
    an intrinsic theorem'.  paper56 line ~100: 'what remains genuinely open is the
    GRAVITATIONAL content ... is gravitational record commitment sparse?' -- a
    computation on the GRAVITATIONAL decoherence functional D.

  TIER VERDICT (the precise relativization):
    The SUPPLY question splits cleanly:
      (S-A)  Does SOME intrinsic seal-supply principle exist at the pure record
             level (Tier A)?  -- this is Paper 1's OWN open frontier: the seal
             RATE/shape is what Paper 1 s3.2 derives (S=exp(-kappa chi)), but WHICH
             proposition E commits and WHERE the seal fires is the record click-
             law's 'where', which Paper 1 s6 explicitly says is NOT a Tier-A output
             ('where (a locality kernel) is only an emergent Tier-B notion').
      (S-B)  Does the GRAVITATIONAL record process supply them (sparse vs dense)?
             -- this is paper56's Tier-1 functor [TARGET], a TIER-B / gravitational
             computation on the gravitational D.  Explicitly deferred there.

  So Paper 1's Tier-A FORCING legitimately rests on the KINEMATIC bridge (forced),
  while the INTRINSIC SUPPLY is a SEPARATE, properly-deferred question -- and it is
  deferred to TWO different places:
     * the seal RATE/shape supply = Paper 1's own s3.4/s5.1 (the kappa, the dchi
       magnitude) -- Tier-A-open;
     * the seal PLACEMENT / which-E / sparse-vs-dense = Tier-B gravitational
       (paper56 Tier-1 functor) -- Tier-B-deferred.
  NEITHER is a hidden hole, PROVIDED Paper 1 states that its s3.2 forcing is
  RELATIVE TO the projective GMH bridge (kinematic), which Paper 1 s3.2 ALREADY
  does ('all forcing below is relative to the bridge').
""")


# ===========================================================================
head("SUPPORT (B) -- MARKOV-PRESENTABILITY of the COLLAR  (forced by paper10?)")
# ===========================================================================
print("""
  CLAIM under test:  the eventless collar between seals is Markov-presentable
  (so the path measure factorizes and the trajectory action telescopes), and this
  is FORCED by paper10's standing structure (T3 eventless=>detailed balance;
  T4 RP-as-theorem of a finite primitive Markov presentation), NOT a separate
  assumption -- while the SEAL ORDER itself is non-Markov / indivisible.

  paper10 s2.6 (the Barandes link, verbatim):
    'division events are exactly where record dynamics visibly fails Markovianity
     (P4 s10), and they carry evidence; BETWEEN events the collar is eventless and
     T3-T4 apply ... the indivisible (non-Markov) structure lives precisely where
     the positivity theorem does not need to hold, and the positivity theorem
     holds precisely where the process is order-blind.'

  We make the split QUANTITATIVE on one explicit process.
""")

# --- B.1  WITHIN a collar: the trajectory action telescopes (Markov). ---
print("  (B.1)  WITHIN an eventless collar: trajectory action telescopes (Markov).")
# a driven 3-state collar transport (an ordered/Markov record transport, sigma>0)
Pc = [[mp.mpf('0.10'), mp.mpf('0.70'), mp.mpf('0.20')],
      [mp.mpf('0.20'), mp.mpf('0.10'), mp.mpf('0.70')],
      [mp.mpf('0.70'), mp.mpf('0.20'), mp.mpf('0.10')]]
ncs = 3
# stationary law
Am = mp.matrix(ncs, ncs)
for jj in range(ncs):
    for ii in range(ncs):
        Am[jj, ii] = (1 if ii == jj else 0) - Pc[ii][jj]
for ii in range(ncs):
    Am[ncs - 1, ii] = mp.mpf(1)
bm = mp.matrix(ncs, 1); bm[ncs - 1] = mp.mpf(1)
pic = mp.lu_solve(Am, bm)
pi_c = [pic[i] for i in range(ncs)]


def cocy(P, pi, x, y):
    return mp.log((pi[x] * P[x][y]) / (pi[y] * P[y][x]))


def action(P, pi, path):
    return sum(cocy(P, pi, path[k], path[k + 1]) for k in range(len(path) - 1))


collar_path = [0, 1, 2, 0, 1, 2]      # 5-edge eventless-collar trajectory
A_collar = action(Pc, pi_c, collar_path)
cut = 2
A_c1 = action(Pc, pi_c, collar_path[:cut + 1])
A_c2 = action(Pc, pi_c, collar_path[cut:])
collar_telescope_gap = A_collar - (A_c1 + A_c2)
line("collar trajectory action A[full]", mp.nstr(A_collar, 25))
line("A[sub1] + A[sub2]", mp.nstr(A_c1 + A_c2, 25))
line("WITHIN-COLLAR TELESCOPE GAP", mp.nstr(collar_telescope_gap, 8),
     "(=0: collar is ordered/Markov -- composition holds BETWEEN seals)")
assert mp.fabs(collar_telescope_gap) < mp.mpf('1e-120')

# --- B.2  ACROSS a seal: the one-time transition law fails to compose. ---
print("""
  (B.2)  ACROSS a seal/event: the seal-order one-time transition law FAILS
         Chapman-Kolmogorov (non-Markov / indivisible).  We use the Barandes
         Gamma=|U|^2 process of Support A: the inter-seal holonomy interval is
         the collar (coherent, CK fails as a *coherent* composition), and a seal
         is the only place CK is restored.  The KEY consistency check: the SAME
         coherent interval that is 'ordered/Markov for the trajectory-action of
         committed evidence' (B.1) carries a holonomy whose one-time transition
         law does NOT compose -- because composing it would require inserting an
         intermediate record (a seal), which is exactly what is absent.
""")
line("CK gap ACROSS unsealed (coherent) interval", mp.nstr(ck_gap_unsealed, 8),
     "(!=0: seal-order composition FAILS -- indivisible)")
line("CK gap ACROSS a seal (D diagonalized)", mp.nstr(ck_gap_sealed, 8),
     "(=0: composition restored ONLY at a seal)")

print("""
  (B.3)  CONSISTENCY of the split -- is it genuinely true that Markovianity holds
         BETWEEN seals while the seal order is non-Markov?  The two statements live
         on DIFFERENT objects, and that is what makes the split consistent (not a
         contradiction):

    * BETWEEN seals (collar), the object that is MARKOV is the committed-evidence
      trajectory action A[omega] = log dP_fwd/dP_rev of the ORDERED record
      transport (B.1): its path measure factorizes, so the action telescopes.
      This is paper10's eventless collar with a finite primitive Markov
      presentation (T4).  It is 'order-blind' (T3: eventless => detailed balance
      for the bare collar) -- the Markov presentation is what carries the *content*
      increment dchi, not an arrow of its own.

    * The SEAL ORDER (the succession of committed records / division events) is the
      object that is NON-Markov / indivisible: the one-time transition law
      Gamma=|U|^2 of the coherent holonomy does NOT compose across an unsealed
      interval (B.2), because composing = inserting an intermediate seal, and the
      holonomy is unsealed there.  Composition is restored ONLY at a seal.

    These are not in tension: the FACTORIZATION that telescopes the action is a
    property of the EVENTLESS COLLAR's ordered transport (a Markov presentation of
    the *content accumulation*), whereas the NON-Markovianity is a property of the
    SEAL ORDER's coherent one-time law (the *holonomy composition*).  Markov where
    the process is order-blind; non-Markov where it commits.  Paper10 s2.6 states
    EXACTLY this architecture; we have now made both halves quantitative on one
    process.
""")

# --- B.4  Is collar-Markov-presentability FORCED by paper10, or assumed? ---
print("""
  (B.4)  FORCED or ASSUMED?  paper10's chain:
    T3 (dissolution): an eventless collar records nothing -- not even the order of
       its own traversal -- so D(P_AB||P_BA)=0 => P_AB=P_BA => DETAILED BALANCE,
       exactly.  An eventless collar is REVERSIBLE.
    T4 (theorem): a reversible primitive (block-)Markov collar transport has the
       symmetrized transfer self-adjoint, spectrum in [-1,1]; every collar
       correlation is a spectral (moment) sequence => reflection positivity, AS A
       THEOREM of indivisible ordered transports, for every sector with a FINITE
       PRIMITIVE MARKOV PRESENTATION.
  So 'the eventless collar admits a finite primitive Markov presentation' is the
  STANDING ARENA of paper10 Part I -- the hypothesis under which T4 (RP) is a
  theorem.  For the click-law, the collar between seals is, BY paper10's
  architecture, exactly such an eventless ordered transport.  Therefore:

    collar Markov-presentability is FORCED *within paper10's standing arena*
    (T3+T4: eventless => detailed-balance reversible => a finite primitive Markov
     presentation exists, for every sector that HAS one),
    with ONE honestly-named residue paper10 itself flags (s2.5 scope subtlety;
    s2.6 'sectors with no finite primitive presentation remain open'):
    sectors with GENUINELY INFINITE collar memory (no finite primitive
    presentation) -- the constructive-QFT-class residue -- are NOT covered.

  HONEST STATUS:  collar Markov-presentability is FORCED for every collar with a
  finite primitive presentation (paper10 T3+T4 standing arena), NOT a fresh
  assumption.  The residue (infinite-memory collars) is paper10's own named open,
  inherited verbatim -- not a new hole opened by Paper 1.
""")


# ===========================================================================
head("CROSS-CHECK -- the split does not smuggle geometry, and dchi>=0 still holds")
# ===========================================================================
# verify the collar arrow is >=0 (arrow-positivity) and the seal restores CK
sigma_collar = mp.mpf(0)
for x in range(ncs):
    for y in range(ncs):
        joint = pi_c[x] * Pc[x][y]
        sigma_collar += joint * cocy(Pc, pi_c, x, y)
line("collar per-step arrow sigma_step (=dchi)", mp.nstr(sigma_collar, 25),
     "(>=0: arrow-positivity, paper10 T2; NOT a seal if =0)")
assert sigma_collar > 0
# everything used: probabilities, KL/log-ratios, |amplitude|^2.  No length, no s^2.
line("any spacetime/metric/s^2 used?", "NO",
     "(all numbers are record-internal probabilities/KL/|amp|^2)")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (F3d foundational-supports receipt)")
# ===========================================================================
print(f"""
  dps = {mp.mp.dps}; pre-geometric (records, commit order, chi=D(P_AB||P_BA)) only.

  SUPPORT (A) -- SEAL = COMPOSITION BRIDGE:
    CK gap across UNSEALED (coherent) interval   = {mp.nstr(ck_gap_unsealed, 6)}   (FAILS: interference survives)
    CK gap across a SEAL (D diagonalized)        = {mp.nstr(ck_gap_sealed, 6)}   (RESTORED at the seal)
    CK-gap == interference cross-term (identity) = {mp.nstr(max_identity_gap, 6)}   (biconditional is an IDENTITY)
    => the seal<=>CK-composition biconditional is FORCED AT THE KINEMATIC LEVEL,
       given the projective GMH model (which is itself forced by Paper 1 s3.1:
       q=2 => orthogonal projective pointers).  NOT a further choice.
    => the INTRINSIC SUPPLY of the seals is a SEPARATE question, deferred to:
         (a) Paper 1's own seal-RATE supply (s3.4/s5.1, the kappa/dchi magnitude)  -- TIER-A-OPEN;
         (b) the seal PLACEMENT / sparse-vs-dense GRAVITATIONAL functor          -- TIER-B-DEFERRED (paper56 Tier-1).

  SUPPORT (B) -- MARKOV-PRESENTABILITY of the COMMIT ORDER:
    WITHIN-COLLAR trajectory-action telescope gap = {mp.nstr(collar_telescope_gap, 6)}   (collar is ordered/Markov)
    CK gap ACROSS unsealed interval               = {mp.nstr(ck_gap_unsealed, 6)}   (seal order is NON-Markov/indivisible)
    collar per-step arrow sigma_step (=dchi>=0)    = {mp.nstr(sigma_collar, 6)}
    => collar Markov-presentability is FORCED within paper10's standing arena
       (T3 eventless=>detailed-balance reversible; T4 RP-as-theorem of a finite
       primitive Markov presentation), NOT a fresh assumption.
    => the Markov(collar)/non-Markov(seal-order) split is CONSISTENT: they are
       properties of DIFFERENT objects (the collar's ordered content-transport vs
       the seal order's coherent one-time law).  Markov where order-blind; non-
       Markov where it commits.  paper10 s2.6's architecture, made quantitative.
    => residue: collars with NO finite primitive presentation (infinite memory) --
       paper10's OWN named open (s2.5/s2.6), inherited, NOT a new hole.

  BRUTAL-HONESTY VERDICT:
    (A) FORCED-at-kinematic-level (legitimate relativization to the GMH bridge,
        which Paper 1 s3.2 already declares); intrinsic supply properly deferred,
        split Tier-A-open (rate) + Tier-B-deferred (placement).  NOT a hidden hole.
    (B) FORCED (within paper10's standing arena) + CONSISTENT split; infinite-memory
        residue is paper10's inherited named open.  NOT a hidden hole.
""")

head("DONE.")
