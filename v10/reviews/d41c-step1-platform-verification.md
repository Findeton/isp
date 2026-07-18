# D41c / D26 laboratory discriminator — §5 step (1): platform-table verification

**Status:** LITERATURE-VERIFICATION PASS, 2026-07-18. Executes exactly step (1) of
`isp/v10/note-d41c-d26-laboratory-discriminator.md` §5: verify the §2 platform table
against current primary literature. The physics of the bound is untouched. Convention
throughout: κ(9/25) = ½ln(25/16) ≈ 0.2231, so a null at relative visibility precision
δ ≡ δV/V₀ gives **N ≤ δ/0.2231 = 4.48·δ per dwell**; rate = N/T_dwell. Every number
is tagged **[MEASURED]** (demonstrated in the cited experiment), **[FIT]** (fitted
decay constant, not a directly held duration), **[PROJECTED]** (proposal/forecast in
the source), or **[UNVERIFIED]** (searched, not found demonstrated). No number from
the note was adopted without an independent source.

---

## 1. Corrected platform table (replacement candidate for note §2)

```text
platform                     T_dwell (status)          δ = δV/V₀ (status)         N ≤ 4.48δ /dwell → rate
1. trapped-ion hyperfine     960 s probed [MEASURED];  ~10⁻² per-point [MEASURED-  4.5×10⁻² → 8×10⁻⁶–1.4×10⁻⁴ /s
   ¹⁷¹Yb⁺ + DD (Wang 2021)   T₂ = 5500±670 s [FIT]     class]; 10⁻³ at hour dwell  (measured-anchored);
                                                       [PROJECTED, needs arrays]   8×10⁻⁷ /s [PROJECTED corner]
2. atom interferometer       2.3 s fountain ceiling;   ~2×10⁻² per fringe point    δ=2×10⁻²: 9×10⁻² → 1.3×10⁻³ /s
   (Cs lattice-hold /        20 s, 70 s lattice-hold   [MEASURED]; 10⁻³ campaign   [MEASURED]; δ=10⁻³ @70 s:
   Rb fountain)              spatial superposition     stat. [PROJECTED-plausible] 4.5×10⁻³ → 6.4×10⁻⁵ /s [PROJ.]
                             [MEASURED]
3. macromolecule/nanoparticle 7–12 ms transit          3×10⁻²–10⁻¹ at frontier     4.5×10⁻²–0.45 → ~4–40 /s
   beam TL interferometry    [MEASURED]                mass [MEASURED]; 10⁻²       [MEASURED]; mass record now
   (LUMI; Na clusters)                                 established species          >170 kDa (was 25 kDa)
4. levitated nanoparticle    ~4×10⁻⁵ s coherence       NO fringe visibility        bound NOT mountable today;
   (~10⁸ amu, optical trap)  window [MEASURED];        observable exists yet       [PROJECTED] (10⁻³ s, 10⁻²):
                             10⁻³ s [PROJECTED]        [MEASURED absence]          4.5×10⁻² → ~45 /s at 10⁸ amu
```

Additional platforms the note's table missed (task item 5):

```text
5a. ¹⁵¹Eu³⁺:Y₂SiO₅ nuclear-  2.2×10⁴ s (370±60 min)   ~10⁻² echo-amplitude        4.5×10⁻² → 2.0×10⁻⁶ /s —
    spin ensemble (solid)    T₂ [MEASURED, ZEFOZ+DD]   class [MEASURED-class]      best raw product on the board,
                                                                                   but ensemble+solid bridge
5b. ⁸⁷Sr optical-lattice-    118(9) s T₂* single       ~10⁻² per shot (QPN, 10⁴    δ=10⁻³: 4.5×10⁻³ → 3.8×10⁻⁵ /s;
    clock line (Wannier-     ensemble [MEASURED];      atoms) [MEASURED-class];    campaign δ=10⁻⁴ → 3.8×10⁻⁶ /s
    Stark; erasure-conv.)    >100 s Ramsey / >150 s    10⁻³–10⁻⁴ campaign          [PROJECTED-plausible] — rivals
                             echo differential [MEAS.] [PROJECTED-plausible]       the single ion; OPTICAL line
Excluded: superconducting qubits (T₂ ms-class — product 5+ orders worse; knowledge-based,
not re-verified this pass); NV-diamond nuclear memories (minute-class — below 5a/5b/1).
```

---

## 2. Platform 1 — trapped-ion hyperfine qubits with dynamical decoupling

**Coherence time.** The standing single-qubit record is the ¹⁷¹Yb⁺ hyperfine qubit of
Wang, P. et al., *Nat. Commun.* **12**, 233 (2021) (arXiv:2008.00251): sympathetic
cooling by ¹³⁸Ba⁺ plus KDDxy dynamical decoupling; **superposition coherence time
5500 ± 670 s [FIT]** — an exponential-decay constant fitted to Ramsey-contrast data
**actually probed only to 960 s [MEASURED]** (population lifetime 16000 ± 3200 s).
The prior record was 667 s (>10 min) in the same system class: Wang, Y. et al.,
*Nat. Photonics* **11**, 646 (2017). Searches for anything longer through mid-2026
("trapped ion coherence record 2024/2025", "single qubit coherence record 2026")
returned nothing beyond 5500 s — found instead: 136(42) s in a metastable
¹³⁷Ba⁺ 5D₅/₂ qubit (*Phys. Rev. A* **111**, L020601 (2025); arXiv:2408.00975)
and an order-of-magnitude logical-memory extension via a decoherence-free-subspace
code on Quantinuum H1 (Dasu et al., arXiv:2503.22107, 2025) — neither exceeds the
2021 record. **Verdict on the note's "~10³–5×10³ s": CONFIRMED in order, with the
mandatory caveat that the 5×10³ endpoint is a fitted constant; the longest held-and-
probed dwell is 960 s.**

**Visibility precision.** Published long-hold Ramsey-contrast points in Wang 2021
carry few-percent error bars (Fig. 3) — per-point δ ≈ (2–5)×10⁻² [MEASURED-class].
The binary-outcome projection-noise floor is δ ≈ M^(−1/2) for M shots; at hour-scale
dwell a single ion collects only ~10²–10³ shots in any realistic campaign, so
**δ = 10⁻³ jointly with T ≈ 5×10³ s is UNVERIFIED as demonstrated** (searched for
sub-percent contrast determinations at hour dwells; none found) and is reachable
only by multiplexing many ions (ion strings/arrays) — mark [PROJECTED]. The note's
δ range "10⁻²–10⁻³" is therefore half right: 10⁻² measured-class, 10⁻³ projected.

**Corrected bound.** Measured-anchored: (T = 960 s, δ = 3×10⁻²) → N ≤ 0.13 →
rate ≤ 1.4×10⁻⁴ /s; record-anchored (T = 5500 s [FIT], δ = 10⁻²) → N ≤ 4.5×10⁻² →
**8×10⁻⁶ /s**. Projected corner (5500 s, 10⁻³): 8×10⁻⁷ /s. The note's "10⁻⁵–10⁻⁶ /s"
band sits between the measured and projected anchors — mildly optimistic as a
measured claim, conservative against the projected corner.

---

## 3. Platform 2 — atom interferometers

**Dwell time.** Fountains: free-fall interrogation is capped at ~2.3 s in 10-m
towers — Kovachy et al., *Nature* **528**, 530 (2015) (half-metre superposition,
2.08 s); Asenbaum et al., *Phys. Rev. Lett.* **125**, 191101 (2020)
(arXiv:2005.11624) ran the dual-species equivalence-principle test at
η ≈ 10⁻¹² with 2 s of free fall [MEASURED]. Optical-lattice-hold interferometry
broke this ceiling: 20 s holds (Xu et al., *Science* **366**, 745 (2019);
arXiv:1907.03054) and now a **spatial superposition maintained 70 s** — Panda,
Tao, Egelhoff, Ceja, Xu, Müller, *Nat. Phys.* **20**, 1234–1239 (2024)
(arXiv:2210.07289), Cs atoms, Δz = 1.9 µm arm separation, fringe contrast non-zero
at 30/60/70 s at 3.0/2.6/2.9σ, contrast-decay slowdown beyond 20 s (τ_C1 ≳ 58 s)
[MEASURED]. Companion instrument-grade result: minute-scale gravimetry of a
cm-scale source mass, Panda et al., *Nature* (2024), doi:10.1038/s41586-024-07561-3.
Longer baselines (MAGIS-100: Abe et al., *Quantum Sci. Technol.* **6**, 044003
(2021)) are [PROJECTED]. **Verdict on the note's "~1–10 s": OUTDATED by an order —
70 s is measured.** (Attribution note for the caller: the minute-scale holds are
the Müller group, Berkeley; the Kasevich group's records are the 10-m-fountain
class.)

**Visibility precision.** In Panda 2024 the fringe asymmetry data carry 1σ error
bars ≈ 0.01 absolute against C₀ ≈ 0.5 → per-fringe-point δ ≈ 2×10⁻² [MEASURED].
Campaign-statistical averaging to δ ≈ 10⁻³ at ≤20 s dwell is projection-noise-
plausible (10²–10³ fringe sets) but not itself a published contrast-precision
demonstration — [PROJECTED-plausible]. The note's "~10⁻³" is a fair campaign-level
order but is not the demonstrated per-point precision.

**Corrected bound.** Measured-anchored: (70 s, 2×10⁻²) → N ≤ 9×10⁻² →
**1.3×10⁻³ /s** (the note's "≲10⁻³ /s" — right order, now on 70 s not 1–10 s).
Projected: (70 s, 10⁻³) → 6.4×10⁻⁵ /s — 1.5 orders better than the note credited
the platform, closing most of the gap to the trapped ion.

---

## 4. Platform 3 — macromolecule / nanoparticle beam interferometry (Vienna class)

**Mass record — the note is superseded.** The note cites "~25 kDa oligoporphyrin"
(Fein et al., *Nat. Phys.* **15**, 1242–1245 (2019): functionalized oligoporphyrins
beyond 25 kDa, up to 2000 atoms, λ_dB down to 53 fm, in the 2-m LUMI Talbot–Lau
interferometer) [MEASURED]. The current record is **quantum interference of sodium
nanoparticles of 143–197 kDa (>7000 atoms each)**: Pedalino, Ramírez-Galindo,
Ferstl, Hornberger, Arndt, Gerlich, *Nature*, doi:10.1038/s41586-025-09917-9
(published Jan 2026; arXiv:2507.21211 "Probing quantum mechanics using nanoparticle
Schrödinger cats") — cryogenic Na-cluster source, three 266-nm standing-wave
photodepletion gratings (d = 133 nm) in near-field Talbot–Lau configuration,
grating separation L = 0.983 m ≈ Talbot distance, v ≈ 160 m/s, λ_dB = 10–22 fm,
**fringe visibility V = 0.10 ± 0.01 [MEASURED]**, macroscopicity μ = 15.5 — an
order of magnitude beyond all previous experiments, and the most stringent generic
macrorealism exclusion to date. Fringes are also observed for 0.4–1 MDa clusters
at V = 0.66 ± 0.09, but the paper itself states λ_dB ≲ 3 fm there is too short to
discriminate quantum from classical in this configuration — so **the
quantum-certified record is ~1.7–2.0×10⁵ Da (≈7× the note's number), with
non-discriminating fringes to 1 MDa**.

**Dwell time.** LUMI transit: 2 m at v ≈ 280 m/s (from m > 25 kDa, λ = 53 fm)
→ ≈ 7 ms [derived from the paper's measured parameters]. Na-cluster machine:
G1→G3 = 2×0.983 m at 160 m/s → ≈ 12 ms [derived from measured parameters].
OTIMA-type time-domain machines (Haslinger et al., *Nat. Phys.* **9**, 144 (2013))
sit at shorter pulse separations. **Verdict on the note's "10⁻³–10⁻² s":
CONFIRMED; the frontier instruments now sit at the upper (10⁻² s) end.**

**Visibility precision.** At the frontier mass, δV/V = 0.01/0.10 = 10⁻¹
[MEASURED]; for heavy non-discriminating clusters 0.09/0.66 ≈ 1.4×10⁻¹; for
established species at optimal velocity classes, published visibilities carry
few-percent relative errors → δ ≈ (a few)×10⁻² [MEASURED-class]. **The note's
"~10⁻²" is right for established species but 10× optimistic at the record mass.**

**Corrected bound.** (12 ms, δ = 10⁻²) → N ≤ 4.5×10⁻² per transit → 3.7 /s;
(12 ms, 10⁻¹) → 0.45 → 37 /s. **The note's "≲10 /s": CONFIRMED as the geometric
middle of the honest 4–40 /s range.** This platform now carries a measured mass
ladder 10²–2×10⁵ amu inside one instrument family (fullerene → oligoporphyrin →
Na cluster) — exactly the mass/complexity axis the D26 discriminator needs.
(Related context: native-polypeptide interference, Shayeghi et al., *Nat. Commun.*
**11**, 1447 (2020).)

---

## 5. Platform 4 — levitated nanoparticles

**What is measured.** Center-of-mass ground-state cooling is established: cavity
cooling of a ~150-nm silica particle (~10⁸ amu), Delić et al., *Science* **367**,
892 (2020); 2D ground-state cooling, Piotrowski et al., *Nat. Phys.* **19** (2023,
doi:10.1038/s41567-023-01956-1); six modes of two particles, arXiv:2604.07971
(2026); librational ground state of a nanorotor, arXiv:2509.13398 (2025) — all
[MEASURED]. The coherence frontier: **quantum delocalization of a 1.2 fg
(≈7×10⁸ amu), 100-nm silica particle to a coherence length ξ = 73 ± 34 pm**
(initial ξ₀ ≈ 21 pm; ground-state 32 pm), with total decoherence rate
Γ_tot = (23.7 ± 1.6)×10³ s⁻¹ — i.e. a **coherence window of ~4×10⁻⁵ s**,
photon-recoil dominated — Rossi, Militaru, Zambon, Riera-Campeny, Romero-Isart,
Frimmer, Novotny, *Phys. Rev. Lett.* **135**, 083601 (2025) (arXiv:2408.01264)
[MEASURED]. Crucially, coherence there is verified by retrodiction-based state
estimation, **not by interference fringes: no interference-visibility observable
has been demonstrated on any levitated nanoparticle to date** (searched
"levitated nanoparticle interference/fringes/visibility 2024–2026"; none found).

**What is projected.** The near-term fringe route is Neumeier, Ciampini,
Romero-Isart, Aspelmeyer, Kiesel, *PNAS* **121**, e2306953121 (2024)
(arXiv:2207.12539): single-particle interference at >10⁸ amu, delocalization of
several nm, on **millisecond timescales** [PROJECTED]. Second-scale coherence
exists only in space-mission-class proposals [PROJECTED].

**Verdict on the note's "~10⁻³–1 s": WRONG as a measured claim.** Measured
coherence is ~4×10⁻⁵ s — a factor ≥25 below the note's lower edge and ~4.5 orders
below its upper edge; the entire 10⁻³–1 s band is proposal-stage. Today the
levitated column **cannot host the bound at all** (no δ exists); as a
[PROJECTED] row, (10⁻³ s, δ ≈ 10⁻²) → N ≤ 4.5×10⁻² per dwell → ~45 /s at
~10⁸ amu (≈500–5000× the beam-interferometry record mass). The mass-scaling-axis
role survives, but explicitly as the successor axis, not a current instrument.

---

## 6. Missed platforms with materially better raw T/δ (task item 5)

**(5a) ¹⁵¹Eu³⁺:Y₂SiO₅ nuclear-spin ensemble.** Zhong, Hedges, Ahlefeldt,
Bartholomew, Beavan, Wittig, Longdell, Sellars, *Nature* **517**, 177–180 (2015):
hyperfine coherence time **370 ± 60 min (six hours = 2.2×10⁴ s)** at a
clock/ZEFOZ point with dynamical decoupling; optically detected spin-echo
amplitude is a genuine coherence observable [MEASURED]. Raw product (2.2×10⁴ s,
δ ≈ 10⁻²): N ≤ 4.5×10⁻² → **2.0×10⁻⁶ /s — the best raw number on the board**,
4× better than the ion's record-anchored cell. Heavy caveats for D26 use: it is
a ~macroscopic ensemble in a solid host (per-line O-V identification is murky;
the structured spin bath makes the confound budget (a) hard), and the DD drive
is itself a massive intervention on the monitored line. Related: one-hour
coherent optical AFC storage, Ma et al., *Nat. Commun.* **12**, 2381 (2021).

**(5b) ⁸⁷Sr optical-lattice-clock transitions.** Three mutually consistent
2022–2025 records: (i) single-ensemble **T₂* = 118(9) s** in a shallow
Wannier-Stark lattice, ³P₀ lifetime 174(28) s (the hard ceiling), instability
1.5×10⁻¹⁸ at 1 s — Kim, Aeppli, Warfield, Chu, Rey, Ye (JILA), *Phys. Rev. Lett.*
(2025), arXiv:2505.06444 [MEASURED]; (ii) differential-comparison atomic
coherence **>100 s Ramsey / >150 s spin-echo** via erasure conversion
(Kolkowitz group), *PRX Quantum* (2025), arXiv:2505.06437 [MEASURED];
(iii) 26 s atom-atom coherence and 8.9×10⁻²⁰ statistical frequency uncertainty
after 3.3 h in a multiplexed clock — Zheng et al., *Nature* **602**, 425 (2022),
arXiv:2109.12237 [MEASURED]; background: half-minute tweezer-clock coherence,
Young et al., *Nature* **588**, 408 (2020). The Ramsey fringe contrast of the
ensemble is a genuine visibility observable on ONE optical line (shared by ~10⁴
identical atoms — the per-line bridge needs the ensemble-average declaration);
per-shot quantum-projection δ ≈ 10⁻² [MEASURED-class], campaign 10⁻³–10⁻⁴
[PROJECTED-plausible]. Bound: (118 s, 10⁻³) → 3.8×10⁻⁵ /s; (118 s, 10⁻⁴) →
**3.8×10⁻⁶ /s** — rivals the single-ion projected corner, on an optical rather
than hyperfine line, and the erasure-conversion accounting is philosophically
matched to the note's excess-loss confound budget (a). **This is a genuine
omission in the note's table.**

**Excluded.** Superconducting qubits: best T₂ is millisecond-class (fluxonium;
knowledge-based, not re-verified this pass) — the raw product is ≥5 orders below
the leaders even at generous δ. NV-diamond nuclear-spin memories: minute-class
[knowledge-based] — below 1/5a/5b. Neither changes the table.

---

## 7. Two-platform pair recommendation (feeds note §5 step 2)

**Best raw bound: the ¹⁷¹Yb⁺ single-ion hyperfine qubit (Wang 2021 configuration).**
Its record-anchored cell (5500 s [FIT], δ = 10⁻²) gives 8×10⁻⁶ /s, and it is the
only long-T platform where the monitored object IS a single line: the O-V bridge
declaration (note §3(d)) can be written for one ion, one hyperfine transition,
with no ensemble-average clause, and T₂ characterization — the subtraction step
(a) of the confound budget — is the platform's core competency. The nominally
better raw products both fail a note-§3 clause today: Eu³⁺:Y₂SiO₅ (2×10⁻⁶ /s) is
a 6-hour record on a solid-state ensemble whose structured spin bath and
macroscopic line-count make the bridge and the excess-loss subtraction
proposal-hostile; the Sr lattice clock (118 s, ensemble δ statistics → 10⁻⁶-class
per line with campaign averaging) is the strongest *upgrade path* and should be
named in the proposal as the successor raw instrument once an identical-atom
ensemble bridge declaration is written — its erasure-conversion bookkeeping is
exactly an excess-loss analysis and would slot into the pre-registration
framework naturally.

**Best mass/complexity-scaling axis: Talbot–Lau beam interferometry of
macromolecules/nanoparticles (Arndt-class: LUMI + the Na-cluster instrument).**
This is now the only platform with MEASURED interference visibility across a
mass ladder spanning 10²–2×10⁵ amu within one instrument family (C₆₀/C₇₀ →
oligoporphyrins at >25 kDa → Na clusters at 143–197 kDa, V = 0.10 ± 0.01), which
is precisely what the D26 discriminator's separation axis requires: N_records
scaling with system size at roughly fixed environmental coupling, dwell (7–12 ms),
and readout. The per-dwell bound is weak (~4–40 /s) but the AXIS — the slope of
excess visibility loss vs mass — is what discriminates record-birth from ordinary
decoherence (note §2's closing paragraph), and only this platform can measure that
slope today. The levitated column (Rossi 2025 delocalization; Neumeier 2024
protocol) is the designated successor at 10⁸⁺ amu but currently has no visibility
observable at all and must stay [PROJECTED] in any proposal.

---

## 8. Corrections ledger (note §2 vs verified literature)

1. **Levitated row misclassified (biggest correction).** Note: T ~ 10⁻³–1 s.
   Verified: measured coherence window ≈ 4×10⁻⁵ s (Rossi 2025, PRL 135, 083601)
   and NO demonstrated interference-visibility observable; 10⁻³ s is the Neumeier
   2024 PNAS proposal, 1 s exists nowhere near-term. The row must be re-labeled
   [PROJECTED] wholesale; as written it overstates measured coherence by 1.4–4.4
   orders and implies a δ that does not exist.
2. **Mass record superseded.** Note: ~25 kDa (Fein 2019). Verified: 143–197 kDa
   quantum-certified (Pedalino et al., Nature, Jan 2026; μ = 15.5), fringes
   (non-discriminating) to 1 MDa. ≈7× jump, in the note's favor — it strengthens
   the mass-scaling axis.
3. **Atom-interferometer dwell outdated.** Note: 1–10 s. Verified: 70 s spatial
   superposition (Panda 2024, Nat. Phys. 20, 1234). Corrected projected rate
   6.4×10⁻⁵ /s (vs note's 10⁻³ /s) — 1.5 orders stronger than credited.
4. **Ion row caveats.** 5500 s is a FITTED constant (decay probed to 960 s);
   the joint cell (T = 5×10³ s AND δ = 10⁻³) is undemonstrated — the note's
   10⁻⁶ /s endpoint is a projected corner, not a measured anchor. Measured-anchored
   band: 1.4×10⁻⁴–8×10⁻⁶ /s.
5. **Frontier-mass δ.** Note: 10⁻² for macromolecules. Verified: 10⁻¹ at the
   record mass (V = 0.10 ± 0.01); 10⁻² only for established species.
6. **Missing platforms.** Eu³⁺:Y₂SiO₅ six-hour nuclear ensemble (best raw
   product, 2×10⁻⁶ /s, dirty bridge) and ⁸⁷Sr lattice-clock lines (118 s
   optical-line coherence, ensemble δ statistics; cleanest upgrade path) are
   absent from the note's table.
7. **Attribution (from the tasking, not the note text):** minute-scale holds are
   Müller group (Berkeley), not Kasevich (Stanford); Kasevich-group records are
   the 10-m fountain (2.3 s / half-metre / 10⁻¹² EP) class.

---

## 9. Source list

Trapped ions
- Wang, P., Luan, C.-Y., Qiao, M., Um, M., Zhang, J., Wang, Y., Yuan, X., Gu, M., Zhang, J., Kim, K. — "Single ion qubit with estimated coherence time exceeding one hour," *Nat. Commun.* 12, 233 (2021); arXiv:2008.00251. [5500±670 s FIT; 960 s probed; 16000±3200 s population; ¹³⁸Ba⁺ sympathetic; KDDxy]
- Wang, Y. et al. — "Single-qubit quantum memory exceeding ten-minute coherence time," *Nat. Photonics* 11, 646 (2017). [667 s]
- "Long-lived metastable-qubit memory," *Phys. Rev. A* 111, L020601 (2025); arXiv:2408.00975. [136(42) s, ¹³⁷Ba⁺ 5D₅/₂; context]
- Dasu, S. et al. — "Order-of-magnitude extension of qubit lifetimes with a decoherence-free subspace quantum error correction code," arXiv:2503.22107 (2025). [Quantinuum H1; logical memory; context]

Atom interferometry
- Panda, C. D., Tao, M., Egelhoff, J., Ceja, M., Xu, V., Müller, H. — "Coherence limits in lattice atom interferometry at the one-minute scale," *Nat. Phys.* 20, 1234–1239 (2024); arXiv:2210.07289. [70 s hold; Cs; Δz=1.9 µm; C₀≈0.5; σ_C≈0.01/point; τ_C1≳58 s; 2.3 s fountain ceiling]
- Panda, C. D. et al. — "Measuring gravitational attraction with a lattice atom interferometer," *Nature* (2024), doi:10.1038/s41586-024-07561-3.
- Xu, V., Jaffe, M., Panda, C. D., Kristensen, S. L., Clark, L. W., Müller, H. — "Probing gravity by holding atoms for 20 seconds," *Science* 366, 745 (2019); arXiv:1907.03054.
- Kovachy, T. et al. — "Quantum superposition at the half-metre scale," *Nature* 528, 530 (2015).
- Asenbaum, P., Overstreet, C., Kim, M., Curti, J., Kasevich, M. A. — "Atom-interferometric test of the equivalence principle at the 10⁻¹² level," *Phys. Rev. Lett.* 125, 191101 (2020); arXiv:2005.11624. [2 s free fall]
- Abe, M. et al. — "Matter-wave Atomic Gradiometer Interferometric Sensor (MAGIS-100)," *Quantum Sci. Technol.* 6, 044003 (2021). [PROJECTED]

Macromolecule / nanoparticle beams
- Pedalino, S., Ramírez-Galindo, B. E., Ferstl, R., Hornberger, K., Arndt, M., Gerlich, S. — "Probing quantum mechanics with nanoparticle matter-wave interferometry," *Nature*, doi:10.1038/s41586-025-09917-9 (Jan 2026); arXiv:2507.21211. [143–197 kDa, >7000 atoms, V=0.10±0.01, μ=15.5; d=133 nm, L=0.983 m, v≈160 m/s, λ_dB=10–22 fm; 0.4–1 MDa fringes V=0.66±0.09 non-discriminating]
- Fein, Y. Y., Geyer, P., Zwick, P., Kiałka, F., Pedalino, S., Mayor, M., Gerlich, S., Arndt, M. — "Quantum superposition of molecules beyond 25 kDa," *Nat. Phys.* 15, 1242–1245 (2019). [2-m LUMI; λ_dB→53 fm; 2000 atoms]
- Shayeghi, A. et al. — "Matter-wave interference of a native polypeptide," *Nat. Commun.* 11, 1447 (2020); arXiv:1910.14538. [context]
- Haslinger, P. et al. — "A universal matter-wave interferometer with optical ionization gratings in the time domain," *Nat. Phys.* 9, 144 (2013). [OTIMA]

Levitated nanoparticles
- Rossi, M., Militaru, A., Zambon, N. C., Riera-Campeny, A., Romero-Isart, O., Frimmer, M., Novotny, L. — "Quantum Delocalization of a Levitated Nanoparticle," *Phys. Rev. Lett.* 135, 083601 (2025); arXiv:2408.01264. [1.2 fg ≈ 7×10⁸ amu; ξ=73±34 pm; Γ_tot=(23.7±1.6)×10³ s⁻¹ ⇒ ~42 µs; no fringes]
- Delić, U. et al. — "Cooling of a levitated nanoparticle to the motional quantum ground state," *Science* 367, 892 (2020).
- Piotrowski, J. et al. — "Simultaneous ground-state cooling of two mechanical modes of a levitated nanoparticle," *Nat. Phys.* 19 (2023), doi:10.1038/s41567-023-01956-1.
- arXiv:2604.07971 (2026) — six-mode ground-state cooling of two nanoparticles. [context]
- arXiv:2509.13398 (2025) — librational two-mode ground-state cooling of a nanorotor. [context]
- Neumeier, L., Ciampini, M. A., Romero-Isart, O., Aspelmeyer, M., Kiesel, N. — "Fast quantum interference of a nanoparticle via optical potential control," *PNAS* 121, e2306953121 (2024); arXiv:2207.12539. [PROJECTED: >10⁸ amu, nm delocalization, ms timescales]

Additional platforms
- Zhong, M., Hedges, M. P., Ahlefeldt, R. L., Bartholomew, J. G., Beavan, S. E., Wittig, S. M., Longdell, J. J., Sellars, M. J. — "Optically addressable nuclear spins in a solid with a six-hour coherence time," *Nature* 517, 177–180 (2015). [370±60 min]
- Ma, Y. et al. — "One-hour coherent optical storage in an atomic frequency comb memory," *Nat. Commun.* 12, 2381 (2021). [context]
- Kim, K., Aeppli, A., Warfield, W., Chu, A., Rey, A. M., Ye, J. — "Atomic Coherence of 2 Minutes and Instability of 1.5×10⁻¹⁸ at 1 s in a Wannier-Stark Lattice Clock," *Phys. Rev. Lett.* (2025); arXiv:2505.06444. [T₂*=118(9) s; ³P₀ lifetime 174(28) s]
- "Enhancing optical lattice clock coherence times with erasure conversion," *PRX Quantum* (2025); arXiv:2505.06437 (Kolkowitz group). [Ramsey >100 s; echo >150 s]
- Zheng, X. et al. — "Differential clock comparisons with a multiplexed optical lattice clock," *Nature* 602, 425 (2022); arXiv:2109.12237. [26 s atom-atom; 8.9×10⁻²⁰ @ 3.3 h]
- Young, A. W. et al. — "Half-minute-scale atomic coherence and high relative stability in a tweezer clock," *Nature* 588, 408 (2020). [context]

Method note: searches run July 18, 2026 (WebSearch + primary-source fetches of
arXiv/PMC/publisher pages; the Panda 2024 manuscript PDF read directly). Negative
searches recorded in-line wherever a claimed order could not be confirmed.
