# ISP v17 — SPB primary-source receipt manifest

**Status:** AUTHOR-SIDE EXACT RECEIPTS FOR P0 / NOT AN EVALUATION SOURCE PIN
**Retrieval date:** 2026-08-24
**Scientific result awarded:** none

---

## 1. Receipt distinction

This file authenticates the exact primary scholarly and author-repository
objects consumed by SPB-P0. It does not vendor the external bytes, guarantee
their future availability, authenticate an unlisted supplement, or freeze the
future apparatus packet.

An SPB evaluation pin must retrieve the then-consumed sources again, compare
them with these receipts, and separately hash every apparatus file, raw record,
supplement, calibration object, analysis environment, and immutable code
commit. A mismatch is a differential-audit event, not an automatic update.

## 2. Scholarly objects

| id | exact object | resolved locator | bytes | SHA-256 | consumed claim |
|---|---|---|---:|---|---|
| `SPB-S1` | Pollock et al., *Operational Markov condition for quantum processes*, `arXiv:1801.09811v1` | <https://arxiv.org/pdf/1801.09811v1> | 896,695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` | causal break and operational memory criterion |
| `SPB-S2` | Giarmatzi et al., *Multi-time quantum process tomography on a superconducting qubit*, `arXiv:2308.00750v3` | <https://arxiv.org/pdf/2308.00750v3> | 6,601,486 | `ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28` | full system-side three-time tomography, device scope, limitations, simple memory model |
| `SPB-S3` | Xiang et al., *Quantify the Non-Markovian Process with Intervening Projections in a Superconducting Processor*, `arXiv:2105.03333v2` | <https://arxiv.org/pdf/2105.03333v2> | 1,276,514 | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` | engineered system--memory transmons and restricted process-tensor control |
| `SPB-S4` | Ławniczak et al., *Isoscattering strings of concatenating graphs and networks*, publisher PDF | <https://www.nature.com/articles/s41598-020-80950-6.pdf> | 1,835,223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` | physical different-interior microwave networks and transplantation relation |
| `SPB-S5` | Kostrykin and Schrader, *The Generalized Star Product and the Factorization of Scattering Matrices on Graphs*, arXiv PDF `math-ph/0008022` | <https://arxiv.org/pdf/math-ph/0008022> | 307,827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` | graph scattering composition and associativity control |
| `SPB-S6` | Farooq et al., *Isoscattering non-isospectral quantum graphs*, publisher PDF | <https://www.nature.com/articles/s41598-025-23400-5.pdf> | 3,291,194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` | literal fixed-one-port different-interior substitution control |

The arXiv history for `SPB-S1` lists only `v1`; the downloaded unversioned
endpoint is byte-identical to the receipt recorded here. The explicit `v1`
locator is the registered scholarly identity.

## 3. Author repositories and data

### 3.1 Giarmatzi et al. `NMN-tomo`

Repository: <https://github.com/Christina-Giar/NMN-tomo>

Retrieved commit:

```text
154235f8bbf5e70eb71c325370a67b1894490452
```

Selected file receipts:

| path | bytes | SHA-256 | role |
|---|---:|---|---|
| `README.md` | 904 | `fcd27b514890614b03a26f7ec84a879962feccdb846fd00de103b9631c46a593` | repository scope statement |
| `All codes.ipynb` | 1,399,666 | `b0a2e041ef1616f8c0cff8e2536a892a260820d16fbd8343d22e898b0441c2a1` | reconstruction, metrics, simulations, bootstrap code and stored outputs |
| `NMN_lab_rslts.json` | 20,177 | `b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43` | UQ experimental counts |
| `NMN_tomog_rerun.json` | 176,825 | `450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657` | nine IBM experimental count packets |

The repository also contains derived matrix/metric files. They are not
load-bearing for the P0 conclusion and are not individually authenticated
here. A future analysis pin must hash every consumed derived object or rebuild
it from the raw counts.

### 3.2 Xiang et al. `qucse`

Repository: <https://github.com/xlelephant/qucse>

Retrieved commit:

```text
81998e861ae43541d03738c15d7c60715be37309
```

The commit contains source, fitted process matrices, entropies, fidelities,
and plotting scripts. Several figure/reconstruction scripts instantiate an
external laboratory `DataVaultWrapper`; the corresponding raw laboratory
DataVault is not present in the retrieved repository. SPB-P0 therefore treats
this repository as an analysis/fitted-object packet, not a closed raw-data
packet.

## 4. Source-role ceilings

| source | permitted role | forbidden promotion |
|---|---|---|
| `SPB-S1` | theoretical definition and counterexample control | no physical memory carrier or apparatus selected |
| `SPB-S2` plus `NMN-tomo` | complete system-side process reconstruction and public count evidence | process matrix not a physical boundary; nearby qubit not complete environment |
| `SPB-S3` plus `qucse` | explicit engineered memory architecture and system intervention predecessor | restricted process tensor not full memory grammar; fitted matrices not raw apparatus closure |
| `SPB-S4` | different physical interiors with measured conjugate multiport response | trace/spectrum/conjugacy not equal fixed-port screening; no public raw bytes or triple gluing |
| `SPB-S5` | exact graph-scattering composition theorem | theorem not direct physical reconnection evidence |
| `SPB-S6` | different interiors with measured equal scalar response at one fixed contact | one-port equality not multiport completeness or physical gluing; no public raw bytes |

## 5. Fail-closed evaluation rule

An evaluation-source pin fails if:

1. any load-bearing primary PDF, supplement, raw record, calibration file, or
   apparatus description is missing;
2. a moving repository branch is substituted for an immutable commit;
3. a publisher or arXiv object differs without a differential claim audit;
4. derived matrices are supplied without their consumed raw records and
   reconstruction lineage;
5. request-only microwave data are treated as public evidence;
6. an old device dataset is substituted for the newly required memory or
   reconnection interventions; or
7. a numerical simulation is placed in an empirical source role.

This manifest closes the exact P0 receipts listed above. It does not close the
SPB experimental packet.
