# ISP v17 — MG0 B0-T review-pin source-closure failure

**Status:** PIN CREATION FAILED CLOSED / NO IMMUTABLE REVIEW PIN / REVIEW NOT DISPATCHED

**Date:** 2026-08-24

**Authorized operation:** one result-neutral B0-T review-pin creation followed,
only if valid, by one independent review cycle

**Parent repository head checked:**
`3e29f4d6d324967b724e9a6a43ba0c884ef79409`

**Scientific result awarded:** none

**B0 level awarded:** none

---

## 0. Disposition

The authorized pin creation was required to fail closed if any exact primary
scholarly object or load-bearing supplement was missing, mismatched, silently
updated, or substituted. That condition occurred before reviewer dispatch.

The disposition is therefore

$$
\boxed{
\begin{gathered}
\text{seven review objects and three governing dependencies rehashed},\\
15/26\ \text{registered primary PDFs retrieved as the exact named version},\\
11/26\ \text{registered primary objects not closed at byte level},\\
\text{load-bearing supplement closure also fails},\\
\text{therefore no B0-T review pin exists and no reviewer may begin.}
\end{gathered}}
\tag{1}
$$

This is a procedural invalidation of pin creation, not a scientific rejection
or acceptance of C1--C12. It does not alter the seven proposed review objects,
the terminal R1 baseline, the MG0 contract, the B0-L2 ceiling, or the empty
candidate roster.

---

## 1. Repository-byte reauthentication

Immediately before the source decision, the following current bytes matched
the authorized snapshot exactly.

| role | object | SHA-256 | LF / bytes |
|---|---|---|---:|
| lead | `v17_mg0_b0_matter_pre_authorization_readiness_audit.md` | `59bd04faa658040ec2f02e18c6cad2c06309436598116fb23c3f63453779fe29` | 1239 / 50284 |
| direct | `v17_mg0_b0_matter_exact_synthetic_witness.md` | `f25c192b92d00ebe9bb2836158cf83b47723e78cd8a17c8782556017b4d89d17` | 608 / 16529 |
| direct | `v17_mg0_b0_t_author_reconstruction_and_semantic_audit.md` | `0152ead7f37c6d8ed094550372bcb91984d77ffbebc9fc462d4608de810e533a` | 443 / 13766 |
| direct | `v17_mg0_b0_complete_record_information_feasibility_gate.md` | `8a8605337428412b83949c24802107ef6222ec9d1e58572849283c34731f75de` | 592 / 18368 |
| secondary | `v17_mg0_b0_platform_feasibility_and_selection_gate.md` | `2ee72aeaf8fe28885e99ae1527f202fa732d4e1a713f6816b8deb71002c29cb1` | 634 / 26600 |
| secondary | `v17_mg0_b0_primary_source_claim_and_version_audit.md` | `2dc7a57394a741c708c4c5b59495c8cd6423e0d31fa4e345937212a82be79946` | 228 / 15616 |
| secondary | `v17_mg0_b0_pre_pin_closure_and_common_packet_firewall.md` | `6810773f9b0a3737cee4ea9dfd8f2682ddd70c491aa5789dcbac1bb477d40694` | 639 / 25631 |

The governing dependencies also matched:

| dependency | SHA-256 | LF / bytes |
|---|---|---:|
| `note-r1-native-source-gap-independent-review-adjudication.md` | `53f38d9bdda430f41c857cb73d44f48c13be2f79f5432277fd217718a0f03668` | 646 / 26718 |
| `note-mg0-common-law-reciprocal-benchmark-pin.md` | `2355b2f6809b1ddaed8ec4a2dc8792980bcb051f075383d11ba240b21a27ade8` | 427 / 16227 |
| `note-mg0-common-law-reciprocal-benchmark-review-adjudication.md` | `94ad64a252280f9d299df7fa8f8b082d048c95964483842e6656a21e6fac3f58` | 688 / 27662 |

No bundle-byte drift caused the failure.

---

## 2. Exact primary PDFs retrieved before failure

These files were retrieved on 2026-08-24 from the explicit arXiv version
endpoint, the APS publisher full-text endpoint, or the Nature publisher PDF
endpoint and identified locally as PDF. Their hashes are retained here only
as partial source receipts; because the complete source set did not close,
they do not constitute a review pin.

| registered object | bytes | SHA-256 |
|---|---:|---|
| `arXiv:2502.12474v1` | 1977369 | `915511ed4d53f3475c14196e473bdf577d91143428da9e7259deaa78487eeb8e` |
| `arXiv:1512.00589v3` | 2153339 | `67b2e293fae23007e96b9d57356a079ac3057283eb8c814aa8b48da6dd8bb848` |
| `arXiv:1810.00698v4` | 1184600 | `19b364061b8e16e0b0762ded0f3d4d4b60ba5b9b57a938846ab2a49503d811ae` |
| `arXiv:1610.01829v3` | 1482332 | `9a4c993df5666273be1952d3cc20ef2dad25258d88f1ec60beddd625b7389e32` |
| `10.1103/PhysRevLett.131.183602` | 761201 | `c2e44fee12e9d4b34f67b62b629102ffc7d6efd4dedb9e3dce57b2f4122349ac` |
| `10.1103/y1q9-pnlc` | 534297 | `0e102a39d3d3edffa828610e695c8e341d35e84029ca9091d4469a9966b9f332` |
| `10.1103/PhysRevLett.75.3783` | 298066 | `f305ccb1bf3c33efecf7bb6501e857a681f51a3d8659db8b6b54cec9cfd7b34a` |
| `10.1103/PhysRevA.102.062807` | 685825 | `2459e63ba20ca08def3cbbef017036ae056b64720021d8e07a3929c30d605a43` |
| `10.1103/PhysRevResearch.5.043170` | 2137220 | `1ed6be1b7af1ca0332cf83a369e5b2eba415c3256f4b78da358ff5b914f29c42` |
| `10.1103/PhysRevResearch.6.013199` | 785571 | `353dce65df6f92c2024ba6722523bbcac8dc15cb46efb5546e3dd703fb4caf08` |
| `10.1103/l62d-gz5c` | 1136789 | `a20f52d5a558e4eebdcea1b4907a1443f84569bdb93a6af617b50d920d32e441` |
| `10.1038/ncomms3077` | 1003263 | `560e87f4ad55c7335275da08c636b9df09c1dbf6eda293fc572a3f271f15ae77` |
| `10.1038/s41467-024-49175-3` | 2114621 | `04ca70139a39fed42e13b0bb6b7f818609640a6d90ce1a9b7dea904061c7c436` |
| `10.1038/s41586-025-09595-7` | 3284282 | `04d600ab147362e4d58e9105212b380f732aff253dbc5f85e320aa5e4dad4d4e` |
| `10.1038/s41586-025-09917-9` | 6064622 | `b295bb51d14e8afe1d81bded215779bd4b0d139ab274f7167d965df892b18889` |

Several publisher supplements were also retrieved, but a partial supplement
set cannot satisfy the quantified contract.

---

## 3. Unresolved primary scholarly objects

### 3.1 Publisher subscription pages returned instead of seven Nature PDFs

The attempted publisher PDF endpoints returned subscription-preview HTML, not
PDF bytes, for:

1. Rosi *et al.*, `10.1038/nature13433`;
2. Westphal *et al.*, `10.1038/s41586-021-03250-7`;
3. Kovachy *et al.*, `10.1038/nature16155`;
4. Schumm *et al.*, `10.1038/nphys125`;
5. Fein *et al.*, `10.1038/s41567-019-0663-9`;
6. Tebbenjohanns *et al.*, `10.1038/s41586-021-03617-w`; and
7. Hackermüller *et al.*, `10.1038/nature02276`.

HTML with the expected filename is not a source receipt and was not relabelled
as a PDF.

### 3.2 Three Science versions of record lacked frozen local bytes

The official article or enhanced-PDF interface was reachable for the three
registered Science objects, but no stable exact publisher-PDF byte object was
obtained and frozen for:

1. Overstreet *et al.*, `10.1126/science.abl7152`;
2. Fixler *et al.*, `10.1126/science.1135459`; and
3. Bild *et al.*, `10.1126/science.adf7553`.

A rendered browser view is not a hashable receipt. Cloudflare or viewer HTML
was not accepted as the version-of-record PDF.

### 3.3 The frozen Moorthy accepted-manuscript locator is not byte-complete

The source audit names DOI `10.1103/3jjv-vwmv` and an accepted manuscript
posted 2026-08-12. The live official accepted-page route is under
`journals.aps.org/apsos/accepted/...`, whereas the frozen audit's locator omits
the `apsos` journal path. The official page identifies the accepted object but
did not expose the exact accepted-manuscript PDF through the tested full-text
endpoint.

Correcting the locator or substituting a later version of record would mutate
the source contract. Under the user's rule, either action requires a fresh
differential audit and cannot occur inside this pin creation.

---

## 4. Load-bearing supplement failure

The publisher pages mark the supplementary material for both

- Kamba and Aikawa, `10.1103/PhysRevLett.131.183602`; and
- Seta *et al.*, `10.1103/y1q9-pnlc`

as subscription-required. The corresponding main papers explicitly refer to
their supplements for experimental methods, analysis, or nuisance detail, so
the missing bytes are load-bearing for Seat P rather than optional decoration.

The Overstreet supplementary PDF was visible through an official viewer but
was not frozen as local exact bytes. Supplement discovery and authentication
for the remaining unresolved publisher objects therefore also cannot be
certified complete. The contract quantified over *every* identified
load-bearing supplement; one missing supplement would suffice to invalidate
the pin, and more than one is unresolved.

---

## 5. Fail-closed predicates triggered

The authorized gate required all of the following to be false. At least three
are true:

| predicate | result |
|---|---|
| an exact named source is missing | `TRUE` |
| a retrieved object has a mismatched MIME/content type | `TRUE` for multiple attempted `.pdf` endpoints returning HTML |
| the frozen locator identifies a different route/version than the live exact object | `TRUE` for the Moorthy accepted-object route |
| a substitute version is needed to make the packet complete | `TRUE`, unless the exact authorized bytes are supplied |
| every load-bearing supplement is authenticated | `FALSE` |

Therefore pin validity is exactly false. C1--C12, direct/secondary roles, the
evidence date, the allowed outcomes, and the B0-L2 ceiling were not promoted
into review authority.

---

## 6. Review-dispatch and successor firewall

No mathematics, physical-source/apparatus, or foundations/gravity reviewer
received a review task. No report exists. Root adjudication cannot begin.

This failed pin attempt authorizes none of:

- a source substitution or bundle repair;
- B0-E apparatus work;
- `P-B0-1` discharge;
- a gravity candidate, entrant, comparison, or ontology selection;
- implementation, clock, chronology, spacetime, or gravity construction; or
- an automatic successor.

Two conceptually different future routes exist, neither authorized here:

1. supply the exact named publisher/accepted-manuscript bytes and all
   load-bearing supplements, then create a new pin from a fresh total rehash;
2. explicitly authorize a changed source-equivalence contract and a fresh
   differential source audit, accepting any resulting scope demotion.

Silently choosing route 2 would defeat the purpose of the source gate.

---

## 7. Maximum legitimate statement

> The B0-T repository bundle itself remains byte-stable, and fifteen of its
> twenty-six registered primary PDFs were retrieved exactly. The authorized
> total source-byte contract nevertheless fails: eleven primary scholarly
> objects and multiple load-bearing supplement receipts remain unresolved,
> including subscription-gated sources and one frozen accepted-manuscript
> locator mismatch. Pin creation therefore failed closed. No immutable B0-T
> pin was created, no reviewer was dispatched, and no scientific or B0 result
> was awarded.
