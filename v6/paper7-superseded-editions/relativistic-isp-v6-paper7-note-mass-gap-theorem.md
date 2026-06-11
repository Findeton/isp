# Note: Mass and the Gap Theorem of the Commitment Spectrum

Preprint, not peer reviewed, version 2026-06-10.

(Addendum to Papers 7 v6.2-v6.4; diagnostic: code/v6_p7j_mass_gap_verification.py)

## 1. What mass is

A species is a ledger type. Its mass is its cost of persistence:

    m_hat = committed RN evidence per commitment-renewal cycle
          = D(P_h || U)   [nats],   modular energy E = T x evidence rate,
    T = 1/(2*pi).

A persistent record pattern must renew its commitments to remain itself;
the irreducible evidence per renewal is its rest mass. This gives mass the
same structural role the Compton clock gives it in quantum mechanics: the
internal renewal frequency of the pattern. Massless excitations are exactly
the EVENTLESS sector - retained holonomy propagating with zero commitment
per cycle, which is why they ride the null directions: the null cone is the
eventless characteristic of the signature theorem. Binding follows the
Triangle Law; masses are bounded above by cell capacity (record-Bekenstein)
and, by the theorem below, bounded BELOW by a universal gap.

## 2. The Gap Theorem

**Theorem.** Every nontrivial species (any ledger with at least one mode)
satisfies

    m_hat >= m_hat(P1) = D(eta_hist) = 0.156109200157240 nats,

with equality iff the ledger is a single free mode (up to relabeling).
Massless excitations exist only in the eventless sector: the committed
spectrum is gapped, and the gap equals the gravitational work quantum W.

**Proof.** (1) At any commitment fixed point all coefficients are strictly
positive (tanh(h_a + c_a) = e^{-h_a} with tanh < 1 forces h_a > 0), so the
tilted law is a generalized ferromagnet (all interaction coefficients of
spin products positive). (2) Griffiths' second inequality then makes every
magnetization E[chi_a] nondecreasing in every coefficient h_b; freezing all
b != a at zero gives E[chi_a](h) >= tanh(h_a). (3) At the fixed point
e^{-h_a} = E[chi_a] >= tanh(h_a), and since e^{-h} - tanh(h) crosses zero
once, h_a <= eta_hist for EVERY mode of EVERY ledger, with equality iff
mode a is decoupled. (4) Hence every mode magnetization obeys
mu_a = e^{-h_a} >= theta_hist. (5) Data processing: D(P||U) >= d(mu_a),
the binary divergence of mode a's marginal, which is increasing in mu; and
d(theta_hist) = eta_hist*theta_hist - log cosh(eta_hist) = m_hat(P1)
identically (verified to 15 digits). Chaining (4)-(5) gives the bound;
the equality analysis follows from strictness in (2) and (5). QED

**Machine verification.** Exhaustive over all 127 ledgers on 3 spins, fixed
points Newton-polished to 1e-13: max mode coefficient = 0.609377863436 =
eta_hist exactly (attained only by free modes, never exceeded; 0 violations
at 1e-9); minimum m_hat = 0.156109200157, attained exactly and only by the
7 single-mode ledgers; Griffiths-II monotonicity: 0 violations in 2000
randomized trials.

**Corollary (one constant, three roles).** The spectral gap, the lightest
mass, and the deletion work per primitive event are the same number:
Delta = m_hat(P1) = W = 0.156109200157240 nats - equivalently, in closed
form, eta*theta - log cosh(eta) at theta^3 + theta^2 + theta = 1.

## 3. Relation to the Yang-Mills mass gap (honest statement)

This is NOT a solution of the Clay problem, and the differences are
structural: the Clay problem asks for (a) EXISTENCE of quantum Yang-Mills
on R^4 in the Osterwalder-Schrader sense and (b) a spectral gap of its
Hamiltonian. What is proved here is a gap for the commitment spectrum of
FINITE record ledgers - a different object, with no continuum limit and no
Yang-Mills dynamics constructed.

What the framework does do is relocate the problem onto named walls it
already owns. Clause (a) is literally OS reconstruction - this program's
(R-) kernel, discharged here for nearest-neighbor, Gaussian, and Bernstein
sectors and open exactly where constructive field theory is open. Clause
(b), within the ontology, stops being mysterious: anything that exists as
matter must commit, the commitment fixed point repels zero and Griffiths
caps it, so a gap is AUTOMATIC at finite scope and would be inherited by
any record sector surviving the continuum limit. The gap's physical value
in GeV is not predicted: the nat-to-energy calibration is part of kernels
(C)/(M). Summary: gap defined and proved for the framework's own spectrum;
Yang-Mills gap converted into (R-)''' + (C) plus a finite theorem now in
hand; difficulty relocated, not dissolved.
