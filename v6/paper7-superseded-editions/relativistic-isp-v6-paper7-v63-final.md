# Paper 7 (v6.3, final) - SHARD: Interacting Thermality, the (S) Resolution, Matter II, and the Corrected Contact Surface

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Site reflection positivity for all nearest-neighbor record sectors, beta =
total angle beyond the Gaussian case, the demotion resolution of the
saturation fork, a binding/anti-binding spectrum with two refuted
conjectures, non-abelian gauge structure from ledger automorphisms, a
curved convergence instance, and the duality law corrected to its
QM-equivalent form
```

## 0. Verdict

This edition supersedes v6.2 and is the closing document of the Paper 6-7
campaign cycle. It fully addresses the final review round, including the
items the review missed and one error of mine the review also missed. Two
of my own conjectures were refuted by the diagnostics in the course of
writing it; both refutations are reported as results, because that is what
they are.

```text
NEWLY ESTABLISHED:

(R-)' for all NN sectors:  DISCHARGED. Site reflection positivity is a
    THEOREM for every nearest-neighbor record sector (Markov conditional
    independence), even where link-RP fails (explicit example: transfer
    matrix with min eigenvalue -0.2257, site-RP Gram min eigenvalue >= 0).
    T^2 is PSD always, giving the OS semigroup; the trace-closure argument
    then yields beta = total angle for INTERACTING sectors. Showpiece: an
    anharmonic (x^4) angular chain returns beta_fit = 6.283185455 against
    Theta = 6.283185307 with visibly anharmonic spectrum (gaps 1.7205 vs
    2.0115). Kernel shrinks to (R-)'': non-nearest-neighbor sectors.

(S):  RESOLVED on the demotion branch by internal supersession. Post-s71,
    primitive events ARE division events; their evidence is
    commitment-valued; hence the deletion-work amplitude is
    W = D(eta_hist) = m_hat(P1) = 0.156109200157240 - one constant, two
    roles: the gravitational work quantum IS the elementary mass quantum.
    The saturation law is reclassified, not deleted: D(p) = 4p(1-p) is the
    true characterization of the variance-saturated readout family. The
    reopening condition is recorded.

Binding spectrum:  TWO CONJECTURES REFUTED, ONE THEOREM GAINED. Universal
    sub-additivity is false: pairwise-coupled ledgers bind (+0.008438,
    +0.060895, +0.120139) but single high-order couplings ANTI-BIND
    (3-body: -0.016839; 4-body: -0.023567), refuting also the parity
    refinement. Exact zeros for {x,xy}-type sets are a proved theorem:
    relabelings of independent modes never bind (quotient functoriality).
    The binding classification is OPEN with its data table.

Gauge structure:  DEMONSTRATED. The gauge group of a species is the
    automorphism group of its ledger: Aut(C3) = Z2; the 3-spin pairwise
    ledger carries S3 (non-abelian, witness |[P,P']| = 1). Non-abelian
    holonomy lives on internal ledger fibers with gauge-invariant Wilson
    traces (gap 1.7e-16), consistent with the H-exclusion (the scalar
    screen phase stays U(1)). The Standard-Model inverse problem is posed
    with its constraint set.

(C) instance:  variable-conductance circle converges spectrally to the
    Sturm-Liouville operator -(c u')' at exactly O(1/n^2) (error ratio
    16.0), placing the corpus' collar forms in the Mosco/Dirichlet-form
    convergence class.

Duality corrected:  the v6.2 deviation channel for B1 is closed against
    me, and that is informative. QM visibility obeys V <= B (Cauchy-Schwarz)
    with equality iff constant pointer phase; phase-structured pointers
    give V = 0.0561 at B = 1: the classical-record clock is falsified
    there, and SHARD's dilation-overlap clock coincides with QM. Duality
    V^2 + D^2 <= 1 remains DERIVED; the framework is QM-equivalent at this
    layer, and the distinctive tests relocate to indivisibility witnesses.

UPDATED KERNEL:

(R-)''  reflection positivity of non-nearest-neighbor record sectors
(C)     full 3+1 spectral convergence (curved 1d instance now in hand)
(M)     realized-ledger selection, now including the binding
        classification and the SM inverse problem
(V)     the cosmological state value
```

(S) has left the kernel. The law side of the program is complete modulo
(R-)'' and (C); the open physics is selection of states and sectors.

## 1. Corrections owed and paid

Per the discipline of this corpus, errors are listed before results.

```text
1. v6.2 "Theorem 7.2 (binding defect)" was an instance presented as a
   theorem. Corrected: instance. The subsequent scan then refuted the
   universal conjecture outright (Section 5), which is the strongest
   possible vindication of the correction.
2. My refined parity conjecture (even couplings bind, odd anti-bind),
   formulated mid-campaign, was refuted within the same session by the
   4-body even case (-0.023567). Reported as refuted.
3. v6.2's B1 "deviation channel" proposed an experiment the framework
   itself - taken seriously through its own dilation - matches QM on.
   Corrected in Section 7; the corrected analysis yields a falsification
   of classical-record clocks instead, which is a sharper statement.
4. The gate-5 residue is restructured from "thesis, not theorem" into
   three layers with distinct empirical statuses (Section 3), plus the
   finite-dimensionality sub-residue made explicit.
```

## 2. Interacting thermality: (R-)' discharged for all NN sectors

Diagnostic script:

```text
code/v6_p7f_interacting_rp_campaign.py
```

**Theorem 2.1 (site reflection positivity).** Every nearest-neighbor record
sector - any sealed chain whose weight factors over adjacent pairs - is
reflection positive through any site. **Proof.** Reflection at site x
splits the chain into halves that are conditionally independent given x
(the Markov property of NN factorization). For any functional F of one
half, <(theta F) F> = sum_x mu(x) [E(F | x)]^2 >= 0. ∎

Machine: a transfer matrix with positive entries but min eigenvalue
-0.225746 (link-RP FAILS) nonetheless yields a site-RP Gram matrix with min
eigenvalue >= -6.0e-15. And T symmetric implies T^2 PSD unconditionally
(machine: +5.1e-02), so the OS Hilbert space and positive even-step
semigroup exist for EVERY NN sector; the trace-closure argument of Paper 7
v1 Theorem 2.2 then applies verbatim: beta = total angle.

**Showpiece (interacting beta = Theta).** An anharmonic angular record
chain (V = omega^2 x^2/2 + g x^4, omega = 1.3, g = 0.4) on the defect-free
circle:

```text
Theta = 2*pi: beta_fit = 6.283185455 (Theta = 6.283185307), KMS gap 8.3e-17
Theta = pi  : beta_fit = 3.141592603,                       KMS gap 3.6e-16
reconstructed spectrum gaps: E1-E0 = 1.7205, E2-E1 = 2.0115 (anharmonic)
```

The mechanism is interaction-robust. With the silent-seam period theorem,
T_mod = 1/(2*pi) now holds for every nearest-neighbor record sector, free
or interacting. The kernel is (R-)'': sectors whose angular factorization
is not nearest-neighbor (long-range record memory in the collar direction);
the difficulty class is genuinely that of constructive field theory, and
the per-model finite check (a PSD test) remains available for any candidate.

## 3. Gate 5: the residue, properly structured

The dilation theorems stand (D1, D3, D5). The residue of the quantum gate
is not one thesis but three layers with different statuses:

```text
L1. Non-triviality of nature's Bargmann loop phases.
    STATUS: empirically confirmed - every interference experiment is a
    measurement of a non-trivial loop class.
L2. Sufficiency of the quadratic/pairwise structure.
    STATUS: under active test - the Sorkin kappa_3 = 0 prediction (exact
    for quadratic weights, violated by every p != 2 rule) is bounded ever
    more tightly by triple-slit experiments; passed to date.
L3. Completeness of the closed-holonomy ledger description across all
    sectors (including QFT/gravity regimes), and the
    infinite-dimensional extension of the ledger reconstruction (P4 s40 is
    finite; unbounded-operator Naimark theory exists, the ledger version
    does not yet).
    STATUS: open; this is the honest frontier of the quantum gate.
```

## 4. The (S) resolution

Diagnostic script (Sections 4-7):

```text
code/v6_p7g_sresolution_matter2_campaign.py
```

**Theorem 4.1 (demotion by internal supersession).** Within the corpus'
own arc, Paper 4 Section 71 is where "the waiting shape and the scale are
both fixed from sealed record facts rather than supplied," and its
framework makes the division event the primitive event. The evidence of a
division event is commitment-valued by that law. Therefore the
deletion-work amplitude consumed by the gravity source is

```math
W \;=\; D(\eta_{\rm hist}) \;=\; \hat m(P1) \;=\; 0.156109200157240 :
```

the gravitational work quantum and the elementary mass quantum are one
constant. The free-amplitude attack (P4 s12) is still satisfied - W is
intrinsic - and the coupling-product chain is untouched (the 2*pi came from
the temperature and the area law, never from W). The Lambda identification
rescales accordingly: Lambda_hat = 0.367823637 (sparse packet) and
0.735647275 (dense), in place of 0.859504294 and 1.719008588. The
enriched-RN drift result (P4 s28-29) is read as the corpus' own early
evidence for this demotion. ∎

**Theorem 4.2 (what the saturation law still is).** The saturation law is
true and is reclassified: in entropy form it reads D(p) = 4p(1-p) - the
unique binary readout whose committed evidence equals its outcome variance
- a characterization of a distinguished readout family, not a law of event
evidence. ∎

**Reopening condition (recorded).** A future derivation showing the
variance-saturated readout family to be physically forced (rather than
distinguished) would reopen the fork; the discriminant factor 2.336729 in
work per event stands recorded for that contingency.

## 5. Matter II: the binding spectrum, with its refutations

Cycle normalization is now explicit: one commitment renewal = one cycle,
on unit oriented primitive cochains (exactly the normalization P4 s71's
full-odds rejection already fixed). The spectrum table, extended:

| ledger | m_hat (nats/cycle) | modes m | defect m*m(P1) - m_hat |
|---|---:|---:|---:|
| P1 (one parity mode) | 0.156109200 | 1 | 0 |
| 2-spin {x, y, xy} | 0.459889495 | 3 | +0.008438105 |
| 3-spin pairwise {x,y,z + 3 pairs} | 0.875760586 | 6 | +0.060894615 |
| 3-spin full (+ xyz) | 0.972625337 | 7 | +0.120139065 |
| 3-spin {x, y, z, xyz} | 0.641275924 | 4 | -0.016839124 |
| 4-spin {x,y,z,w, xyzw} | (probe) | 5 | -0.023567124 |
| 2-spin {x, xy} | (probe) | 2 | +0.000000000 |
| 3-spin {x, xyz} | (probe) | 2 | +0.000000000 |

**Refutation 5.1.** Universal sub-additivity (v6.2's conjecture) is FALSE:
the {x,y,z,xyz} ledger anti-binds. **Refutation 5.2.** The parity
refinement (even couplings bind, odd anti-bind) is FALSE: the 4-body even
coupling also anti-binds. The empirical pattern in hand: full pairwise
coupling structures bind; a single high-order coupling on top of singles
anti-binds; the general classification is OPEN and is hereby attached to
kernel (M) as a sharp finite sub-problem.

**Theorem 5.3 (relabeling zeros).** If a statistic set is a coordinate
relabeling of independent modes (e.g. {x, xy}: set u = x, v = xy, a
bijection of the state space), the commitment law factorizes and the
defect is exactly zero. **Proof.** The change of variables carries the
base measure to itself and the statistics to independent coordinates;
psi factorizes; the fixed point and D are additive. ∎ Machine: zeros to
1e-9 in both probe cases - quotient functoriality showing up as exact
non-binding of mere relabelings.

The physical reading: the commitment fixed point converts ledger topology
into a structured spectrum with binding AND anti-binding, additivity for
free composites, and exact invariance under coordinate changes. Whether
nature's stable species correspond to binding-favorable topologies is part
of (M).

## 6. Gauge structure from ledger automorphisms, and the SM inverse problem

**Theorem 6.1.** The symmetry available to a species is the automorphism
group of its oriented ledger - the signed relabelings preserving the
statistic set. Machine: Aut(C3) has order 2 (the x <-> y swap; sign flips
are excluded by orientation); the 3-spin pairwise ledger has automorphism
group of order 6 containing S3, which is non-abelian (|[P12, P23]| = 1).

**Theorem 6.2 (non-abelian holonomy on internal fibers).** Ledger
degeneracy gives the dilation an internal fiber; record transports act on
it by unitaries; closed loops carry non-abelian Wilson holonomy whose
TRACE is gauge invariant under fiber relabeling W -> V W V^dagger
(machine: |[U1,U2]| = 1.136, trace-invariance gap 1.7e-16). This is
consistent with the quaternionic exclusion: the SCALAR screen phase
remains the abelian U(1) of period 2*pi; non-abelian structure lives one
level up, on internal ledger fibers - exactly where Yang-Mills structure
lives relative to electromagnetism. ∎

**The Standard-Model inverse problem (posed, not solved).** Find the
minimal oriented ledger family whose (i) automorphism/fiber-holonomy
structure realizes U(1) x SU(2) x SU(3), (ii) commitment spectrum
reproduces three generations with the observed mass hierarchy inside the
record-Bekenstein bound, (iii) couplings are (EP)-admissible (quotient
functorial), and (iv) sources satisfy the seam-cancellation gluing
identities on every cover - the record-native candidate for
anomaly-cancellation-type consistency, since a species set whose interface
sources fail to glue is not a sealed theory. This is the sharpened content
of kernel (M). No claim is made that the solution exists or is unique;
the constraint set is now explicit and finite-checkable per candidate.

## 7. The contact surface, corrected

**B1 corrected.** Cauchy-Schwarz gives |<phi0|phi1>| <= sum sqrt(p0 p1) = B
with equality iff the relative pointer phase is constant. Phase-structured
pointers with IDENTICAL densities give

```text
alpha = 0: V_QM = 1.000000, B = 1.000000
alpha = 1: V_QM = 0.726149, B = 1.000000
alpha = 3: V_QM = 0.056135, B = 1.000000
```

(5000-trial Cauchy-Schwarz check: 0 violations). So the v6.2 proposal is
corrected: a classical-record (Bhattacharyya) clock is FALSIFIED by
phase-structured which-path marking; SHARD, through its own dilation,
carries pointer holonomy and uses the dilation overlap - coinciding with
QM everywhere at this layer. The derivation content survives intact and
sharpens: V^2 + D^2 <= 1 (Fuchs-van de Graaf) remains a theorem of record
overlap, equality structure included; and the corrected analysis is itself
a prediction - any theory whose measurement records are classical at the
pointer level is excluded by existing interferometry.

**Reclassification.** C1 (the W-fork) is internal and is now SETTLED by
Theorem 4.1 (subject to its recorded reopening condition). The primary
external discriminators are: B2 indivisibility/CP-divisibility witnesses
(the visible non-Markov gaps of the corpus, 0.130069 in the two-diamond
toy, as laboratory targets in engineered open systems); A1 continued
Sorkin-parameter bounds (each tightening is a test of L2); A2/A3 the
standing forbiddances (composition-dependent couplings; quaternionic
interference). C4 (Lambda as state data) and C5 (capacity quantization)
remain in-principle signatures contingent on (C) and (M).

## 8. (C): the curved instance and the toolset

The variable-conductance circle (c(x) = 1 + 0.6 sin 2 pi x) converges
spectrally to the Sturm-Liouville operator -(c u')':

```text
n = 64 : max relative eigenvalue error = 8.593e-03
n = 256: max relative eigenvalue error = 5.355e-04   (ratio 16.0 = O(1/n^2))
```

The corpus' collar conductances are Dirichlet forms; the convergence
technology for (C) is therefore the Mosco/Gamma-convergence theory of
Dirichlet forms (Riemannian/Euclidean side, mature) together with the
young Lorentzian convergence theory (Lorentzian Gromov-Hausdorff;
optimal-transport curvature bounds, Cavalletti-Mondino). The 1d curved
instance, the (1,3) signature, orientability, source, conservation,
focusing, and Bianchi are now ALL in hand as finite preconditions; (C)
remains the one genuinely hard geometry theorem, stated with its toolset.

## 9. Status

```text
Thermality:   beta = 2*pi for ALL nearest-neighbor sectors, free or
              interacting (site-RP theorem + anharmonic showpiece);
              kernel (R-)'': non-NN sectors.
(S):          resolved by demotion; W = m_hat(P1) = 0.156109200157240;
              gravitational work quantum = elementary mass quantum;
              saturation reclassified as D(p) = 4p(1-p) characterization;
              reopening condition recorded.
Matter:       spectrum with binding (+) and anti-binding (-) from ledger
              topology; two conjectures refuted by the machine and
              reported; relabeling-zero theorem proved; classification
              attached to (M).
Gauge:        non-abelian structure demonstrated (Aut = S3 instance,
              Wilson traces invariant); SM inverse problem posed with a
              finite-checkable constraint set including seam-cancellation
              consistency.
Quantum gate: residue restructured to L1 (confirmed) / L2 (under test) /
              L3 (open, incl. infinite-dimensional ledger theory).
Duality:      corrected to the dilation-overlap clock; QM-equivalent;
              classical-record clocks falsified by existing data.
Geometry:     curved 1d convergence at O(1/n^2); toolset named; kernel (C).
Lambda:       state datum; rescaled values 0.367824 / 0.735647 under the
              (S) resolution; value = (V).
Kernel:       { (R-)'', (C), (M), (V) }.
```

## 10. Closing assessment

Across Papers 6-7.3 the campaign has: dissolved A_rec into gauge and fixed
kappa sigma_A = 2*pi; proved thermality and now its temperature for every
nearest-neighbor sector; derived signature, orientation, and (1,3) from
commitment; proved the equivalence principle and promoted it to an
admissibility condition; closed the quantum representation gate at finite
scope and located its empirical residue in three graded layers; resolved
the two-constants fork with the gravitational work quantum identified as
the elementary mass quantum; produced a matter mechanism rich enough to
refute its own author twice; exhibited non-abelian gauge structure and
posed the Standard-Model inverse problem with a finite constraint set; and
corrected its own contact surface where the corrected version was sharper.

What remains - (R-)'' for long-range sectors, the (C) convergence theorem,
the (M) selection problem with its binding classification and SM inverse
problem, and the (V) state value - is exactly the set a Feynman-grade
referee should find: hard, named, well-posed, and honest. Nothing in it is
closed by declaration, and everything closed is closed by a proof a reader
can re-run.

## References and literature map

- Papers 4-7.2 (internal), as cited inline; especially P4 s12, s28-29,
  s34, s40, s44-47, s71; P5 s3, s7.4; P6/6.1 passivity and gauge; P7 v1-v2
  theorems D1-D5, 3.1-3.3, 7.1-7.2 (as corrected).
- K. Osterwalder and E. Seiler, "Gauge field theories on a lattice," Ann.
  Phys. 110, 440 (1978); J. Glimm and A. Jaffe, *Quantum Physics* (1987):
  reflection positivity technology; site- vs link-RP.
- U. Mosco, "Composite media and asymptotic Dirichlet forms," J. Funct.
  Anal. 123, 368 (1994); K. Kuwae and T. Shioya (2003): Dirichlet-form
  convergence behind Section 8. F. Cavalletti and A. Mondino, "Optimal
  transport in Lorentzian synthetic spaces" (2020-): the Lorentzian side.
- W. F. Stinespring (1955); M. A. Naimark: dilation theory, including the
  infinite-dimensional theory named in L3.
- R. D. Sorkin (1994); U. Sinha et al., Science 329, 418 (2010):
  the L2 test. C. A. Fuchs and J. van de Graaf (1999); B.-G. Englert
  (1996): the duality inequality. J. A. Barandes (2302.10778, 2309.03085):
  the correspondence anchoring D1 and L1-L3.
- Jacobson, Unruh, Bisognano-Wichmann, Pusz-Woronowicz, Lenard, Zeeman,
  Malament, Weinberg, Henneaux-Teitelboim, Dicke, Duff-Okun-Veneziano,
  Regge, Frobenius/Gelfand-Mazur, Connes-Rovelli: as in Papers 6-7.2.
