# Relativistic ISP V5 Paper 7: Quantum Error Correction As Same-Actual Preservation

Preprint, not peer reviewed, version 2026-05-29.

Author: Felix Robles Elvira

Date: May 29, 2026

Status: V5 developed draft consequence paper.  This paper interprets quantum error
correction as protection of a logical same-actual record class while allowing
selected error records to become actual.

## Abstract

Quantum error correction is one of the best ISP examples in quantum
technology.  It works by extracting syndrome records that reveal physical
errors while hiding the logical computational record.  ISP turns this into a
clean ontology: error correction stabilizes the error ledger, not the logical
branch ledger.

The central claim is:

$$
quantum error correction = same-actual preservation under controlled syndrome records
$$

Searchable paper tag:

`V5P7-QUANTUM-ERROR-CORRECTION-SAME-ACTUAL-PRESERVATION`.

## 0. Purpose

This paper explains why quantum error correction is possible in ISP without
contradicting the rule that records destroy coherence.  The answer is that the
syndrome is designed not to record the logical alternative.

## 1. Allowed And Forbidden Records

| Record | Allowed? | Reason |
| --- | --- | --- |
| error location | yes | reveals physical fault class |
| error type | yes | guides recovery |
| logical branch | no | would collapse the computation |
| final answer | yes, at output | intended stabilization |

The code succeeds when:

$$
record(error) actual, record(logical branch) unresolved
$$

## 2. Stabilizer Codes

In stabilizer language, syndrome measurements read commuting constraints.
In ISP language, they stabilize compatibility records for the code subspace.

The logical information remains same-actual when two physical histories differ
only by a correctable error record.

## 3. Recovery As Record Reidentification

Recovery is not time reversal of the microscopic noise.  It is reidentifying
the damaged physical record as the same logical actual record.

The ISP recovery condition is:

$$
R_damaged equivalent R_logical modulo syndrome ledger
$$

## 4. Main Gate

| Gate | Meaning |
| --- | --- |
| QEC1 | finite logical record class is encoded into many physical records |
| QEC2 | syndrome records distinguish correctable faults |
| QEC3 | syndrome records do not distinguish logical branches |
| QEC4 | recovery maps damaged representatives back to the same logical class |

## 5. Surface-Code Reading

The surface code becomes a two-layer record system:

1. local syndrome records are repeatedly stabilized;
2. global logical records remain protected by topology and distance.

This is ISP-native: local records may be actual without making the logical
computation actual.

## 6. Falsifier Gates

| Gate | Failure |
| --- | --- |
| QECF1 | syndrome extraction necessarily records logical branch information |
| QECF2 | recovery cannot be defined as same-actual reidentification |
| QECF3 | logical error rate does not track distinguishability of logical records |
| QECF4 | code distance has no record-stability interpretation |

## 7. Initial Verdict

Quantum error correction is one of the strongest pieces of evidence that ISP
is the right language for quantum computing.  It shows that the art is not
avoiding all records.  The art is choosing which records are allowed to become
actual.

## 8. Developed Code-Space Record Model

A code defines an equivalence class of physical records that represent one
logical record:

$$
[R]_L = {R_phys compatible with the same logical record}
$$

Noise moves the system within or near this class.  Syndrome extraction records
which correction class occurred.  Recovery maps the damaged representative
back into the intended logical class.

The key ISP distinction is:

$$
physical representative may change; logical actual record must remain same
$$

## 9. Knill-Laflamme In Record Language

The standard error-correction condition says correctable errors must be
distinguishable by syndrome without distinguishing logical information.

ISP translation:

| Standard condition | Record condition |
| --- | --- |
| errors map code states to distinguishable syndrome sectors | error record can stabilize |
| logical inner products are preserved | logical branch record remains unresolved |
| recovery exists | same-actual logical representative can be restored |

Thus QEC is not anti-measurement.  It is selective measurement.

## 10. Syndrome Ledger

Let S_t be the syndrome record at correction cycle t.  The full syndrome
history is:

$$
S = (S_1, S_2, ..., S_m)
$$

The decoder computes a recovery class:

$$
Rec(S)
$$

The ISP success condition is:

$$
Rec(S) identifies the physical fault class without identifying the logical branch
$$

If the syndrome history carries logical branch information, the code has
failed as a coherent record-preserving device.

## 11. Distance As Record Separation

Code distance becomes the minimum physical record disturbance required to
stabilize a wrong logical record.

The mature record statement is:

$$
distance d = minimum weight of a physical record path connecting logical alternatives
$$

Below threshold, typical error records have weight below that distance and are
absorbed by the syndrome ledger.  Above threshold, error records percolate into
logical records.

## 12. Surface Code Development

The surface code is a finite record lattice with two record layers:

| Layer | Record status |
| --- | --- |
| plaquette/star checks | repeatedly stabilized local syndrome records |
| logical string operators | protected global record alternatives |

The code works because local checks can be actualized repeatedly without
collapsing the global logical record.  The logical record becomes vulnerable
only when a chain of local faults forms a global distinguishing record.

## 13. Mature Verdict

Paper 7 turns error correction into the central ISP engineering principle:
record the errors, not the computation.  It explains why measurement can be
both dangerous and essential, depending on which finite record is stabilized.

## 14. Formal Closure

### Definition 14.1: Same-Actual Code Packet

A code packet consists of:

$$
\boxed{
{\mathcal Q}
=
(
{\mathcal H}_{code},
{\mathcal E},
{\mathcal S},
{\mathcal R},
{\mathcal L}
).
}
$$

Here \({\mathcal E}\) is the correctable error set, \({\mathcal S}\) is the
syndrome record algebra, \({\mathcal R}\) is the recovery map, and
\({\mathcal L}\) is the logical record algebra.

### Lemma 14.2: Knill-Laflamme Is Same-Actual Preservation

The standard condition:

$$
\boxed{
P E_a^\dagger E_b P
=
c_{ab}P
}
$$

is equivalent to saying that correctable error records do not distinguish
logical alternatives.

Proof.  The operator \(E_a^\dagger E_b\) compares two error histories inside
the code space.  If its compression is proportional to the code projector,
then it has the same value on every logical vector.  The syndrome can identify
the error class, but it cannot identify the logical branch.

$$
\square
$$

### Lemma 14.3: Syndrome Measurement Is Harmless Exactly When It Commutes With
Logical Distinguishability

For a syndrome history \(S\), QEC preserves same-actual logical records when:

$$
\boxed{
I(S;L)=0
}
$$

for the protected logical label \(L\), while:

$$
\boxed{
I(S;E)>0
}
$$

for the physical error class \(E\).

Proof.  Syndrome measurement is useful only if it records error information.
It is harmful only if it records logical information.  Thus the two mutual
information statements are exactly the selective-measurement criterion.

$$
\square
$$

### Lemma 14.4: Distance Is Minimum Logical Record Path

The code distance is the minimum weight of a physical record path that can
separate logical alternatives:

$$
\boxed{
d
=
\min
\{
|P|:
P\hbox{ creates a logical distinguishing record}
\}.
}
$$

Proof.  In stabilizer and topological codes, errors below distance are either
detectable syndrome records or stabilizer-equivalent changes.  A logical
operator is precisely an undetected path connecting distinct logical records.
The minimum weight of such a path is the distance.

$$
\square
$$

### Theorem 14.5: Paper 7 Closure

Quantum error correction is same-actual preservation:

$$
\boxed{
\hbox{QEC succeeds}
\Longleftrightarrow
\hbox{errors are recorded while logical branches remain unresolved}.
}
$$

Proof.  Lemma 14.2 translates the Knill-Laflamme condition.  Lemma 14.3 states
the syndrome criterion.  Lemma 14.4 identifies distance as the minimum
forbidden logical record path.  Therefore Paper 7 is closed.

$$
\square
$$
