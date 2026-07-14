# D35 round 1 — birth/quantum/ontology hostile review

**Frozen candidate:** commit
`b08249c71ab42b839d43ec240aa8d0d8f7cfc902`.

**Review lane:** D24 birth timing, D25/D27 Busch/NSE typing, event-record
factors, quantum-instrument completeness, interaction/merge typing and the
physical meaning of acquired ancestry.

**Verdict:** **REVISE — THE TIMELESS CLASSICAL FAMILY SURVIVES, BUT THE
FLAG/NSE AND PHYSICAL-EVIDENCE CLAIMS EXCEED THE EXECUTABLE.**

**Count:** **0 blockers / 2 majors / 1 minor / 2 nits.**

The candidate has a real result. Its recursive rooted-call law is exactly
normalized, the actor rebuild agrees, the D24 newborn marginal is evaluated
at the correct instant, the exact branch arithmetic is sound, and two
different parameter cells establish nonselection. The defects are not in
those numbers. They are in what the classical event metadata is said to earn:
the program has not implemented orthogonal durable quantum record factors,
and its ancestry gate proves graph membership rather than physical evidence
transport.

## 1. Reproduction and exact-arithmetic audit — pass

I reran

```text
v10/code/d35_timeless_causal_actor_exact.py
```

under fresh hash seeds `314159` and `271828`. Both runs exited zero, were
byte-identical to the committed receipt and reproduced:

```text
source SHA-256
06c997a195294991293fdedc9edce005a3f8ad1d23bfd8f73a5a08490163fa26

stdout SHA-256
24a5cdfe35e1a85b25929217def4bede01e57169a14789392e7e5a7947a11656

internal science SHA-256
1f7b39ddaea634c1444695e5e536d528be45785e8c9997eba1388ed22cfe8aa6

verdict
PASS 18/18
```

I also reran the D24, D25 and D27 exact executables. Each fresh output was
byte-identical to its committed receipt. Thus none of the findings below is a
failure of the inherited exact receipts.

### 1.1 The 16 branches are correct

On the frozen tree `A->{B,C}, B->{D}`, the root alternatives give:

```text
root idle or birth        2 completed branches
root visits C             2 completed branches
root visits B             4 completed branches
root forks to B and C     8 completed branches
total                    16 completed branches
```

Both Q1 and Q2 therefore correctly print 16 branches and total mass one.
The next-A kind distributions are exactly the supplied root menu because
unavailable-action folding occurs only below A in this specimen.

The old `BD` event reaches A exactly when the root query includes B. Hence

```text
P(BD reaches A) = q_visit/2 + q_fork = 1/4
```

for both parameter cells. This is a disclosed coarse-observable collision,
not a hidden equality.

The expected number of transaction births has the independent recursion

```text
E_C = b,
E_B = b(1+v),
E_A = b + (v/2+f)(E_B+E_C)
    = b[1+(v/2+f)(2+v)].
```

It gives `25/64` for Q1 and `63/200` for Q2, exactly as printed. Independent
enumeration also reproduces the complete birth-count distributions and the
two expected newborn-one sums.

### 1.2 The D24 marginal is checked at the correct instant

`create_birth` computes `before = P(parent=1)` immediately before the fresh
actor is appended. Appending the actor and event changes only structural
metadata. The controlled rotation is then applied to a carrier in which the
new actor is absent from every occupied-set basis key, which is precisely the
implicit tensor factor `|0>_child`. `after = P(child=1)` is computed
immediately after that rotation and before any later return operation.

The identity is therefore analytically

```text
P(child=1 after birth) = sin(theta)^2 P(parent=1 before birth)
                       = g P(parent=1 before birth).
```

The 12 branch-cell incidences in each parameter cell reduce to these exact
distinct triples:

```text
Q1, g=9/25:
16/25       -> 144/625
144/625     -> 1296/15625
1296/15625  -> 11664/390625

Q2, g=16/25:
16/25       -> 256/625
256/625     -> 4096/15625
4096/15625  -> 65536/390625
```

Every equality is exact and every completed branch retains norm one. I find
no instant-of-evaluation defect.

## 2. Major findings

### M1 — the advertised orthogonal durable flags do not exist in the quantum object

Section 11.4 says every event receives a fresh orthogonal bounded-rank durable
type flag “as required by D33,” and section 13.5 uses those flags to place the
executable inside the D25/D27 reception class. The executable instead has:

```text
Event.flag: str
World.amplitudes: Dict[FrozenSet[str], Fraction]
```

The flag string is stored only in classical event metadata. It is never
tensored into `World.amplitudes`, never appears as an orthogonal output range,
and never enters an operator, density matrix, Gram functional or trace-norm
calculation. There is no fresh event-record Hilbert factor and no gate proving
that old factors persist support-excluded.

The distinction is load-bearing, not representational taste. D27 admits a
preparation-independent mixture of isometries only when their ranges are
mutually orthogonal. D28 A0c explicitly records the negative control: a
preparation-independent lottery over nonorthogonal isometries can contract
trace distance. D33/D34c then required one actual fresh bounded event-record
factor per click and operator-gated the exhaustive flagged event isometry.

The current code does prove that each selected birth branch is an isometry and
each selected visit/fork carrier update is unitary. That does **not** prove
that the unconditioned classical lottery is NSE. Nor does the pair

```text
classical q + one pure carrier vector per sampled branch
```

by itself define the claimed finite typed quantum instrument or a quantum
history law. The missing construction is, for example, an explicit

```text
rho -> direct_sum_D P(D) V_D rho V_D^dagger
```

with event-local orthogonal factors, correctly typed branch Kraus operators,
operator completeness, finite restriction and durable-factor persistence.
Nothing here requires coherent superposition over support graphs, but the
classical output still has to be represented as a physical orthogonal record
if Busch/NSE is claimed.

**Required repair:** choose one of two honest routes.

1. Implement the D34c-style fresh event factors and the associated
   operator/instrument gates for idle, birth, visit and fork, including the
   multi-leg case; or
2. narrow the result to a classical timeless history family with conditional
   branchwise carrier isometries. Replace `D24/NSE-member` and “finite typed
   quantum instruments” by branchwise D24/unitary compatibility, and state
   that the NSE/quantum-history lift is open.

This finding does not destroy the normalized classical rooted-call law. It
does prevent O6 and the quantum/reception wording from passing as written.

### M2 — LDAP proves structural ancestry, not physical evidence transfer

The LDAP receipt checks that every transaction event belongs to
`Anc(A2)-Anc(A1)` and that an unqueried branch does not. That is an exact graph
fact. It does not establish that the new ancestry is a durable physical
evidence channel rather than a structural correlation written by the
constructor.

The sharp witness is a nested A-to-B-to-D call. A generated D-birth can be:

```text
Event(
  name='E0:0.0',
  kind='birth',
  actors=('D','N0:0.0'),
  predecessors=('BD','A1'),
  flag='birth'
)
```

The event touches D and its newborn, yet `A1` is inserted as a direct
predecessor. The machine did pass ephemeral `Query` objects along A->B->D,
but those query transfers are absent from the retained event history. No
sealed message record, evidence payload, quantum operation or intervention
witness carries A1 at either edge. The final persistent DAG therefore contains
the desired ancestry because the code wrote the reference, not because the
receipt independently reconstructed a chain of physical record transfers.

The note already correctly warns that ancestry may encode common-cause
correlation and is not automatically interventionist causation. Section 13.4
nevertheless calls the ancestry result acquisition and says the ambiguity is
resolved. At present only the realized-versus-pre-click-probability ambiguity
is resolved. The structural-versus-physical-evidence ambiguity remains.

**Required repair:** either retain typed query/return transfer records in the
physical history and demonstrate their local evidence payloads, or explicitly
rename the earned result `STRUCTURAL LDAP` and leave physical/operational
evidence reception open. A stronger route would add interventions on the
declared message content and prove that changing the source can change a
licensed downstream record law while common cause alone cannot.

Because CAP/LDAP is the candidate's strong causal principle, this is a major
scope repair even though the structural ancestry arithmetic itself is true.

## 3. Minor finding

### m1 — interaction and multi-leg event typing is constructor-implied, not fail-closed

The generated specimen uses only legal owned-child targets, so no existing
branch is malformed. But the persistent `Event` schema stores only an
unordered actor tuple, `kind`, predecessors and a string flag. It does not
store initiator/control role, ordered target roles, the selected operation or
coupling. `create_merge` labels every target count other than one as `fork`,
and validates stale tips but not target count, target distinctness or owned
parent-child incidence. The malformed battery attacks Query/Return messages,
not malformed birth/visit/fork event cells.

At the frozen global-parameter tree scope, roles can usually be inferred from
parentage and the constructor only supplies one or two distinct children.
So this is not a counterexample to the enumerated law. It is a gap in the
claim that the history object itself is fully typed and rejects malformed
multi-leg operations.

**Required repair:** store explicit initiator and ordered typed legs (or prove
and gate unique reconstruction from the retained event plus parentage), store
the operation/coupling tag, validate kind-specific arity and ownership, and add
malformed direct event/merge tests.

## 4. Nits

### n1 — the top-level status is stale

The note still opens with `PIN before corpus receipt, derivation, simulation or
result` even though sections 10--13 contain the corpus result, executable and
provisional verdict. Preserve the historical pin in the ledger, but give the
current note an explicit provisional-after-receipt status.

### n2 — “24 birth cells” means branch-cell incidences

The receipt counts 12 `birth_checks` across the 16 completed branches in each
parameter cell. Several are repeated occurrences of the same local cell in
different completed branches. Section 13.5's “Across the 24 enumerated birth
cells” should say “24 branch-cell incidences” or print unique cell types and
incidence counts separately. No probability is wrong.

## 5. Claims that survive this attack

The following statements are supported at the candidate's frozen scope:

- one root call terminates on every finite rooted pre-call tree because calls
  descend strictly and newborns are not queried in the same call;
- the completed classical call-tree weights normalize recursively;
- the actor mailbox implementation reproduces the recursive history law on
  the specimen under FIFO, LIFO and canonical serializers;
- the D24 birth marginal is evaluated at the correct instant and is exact;
- each selected birth map is a D24 isometry and each selected return carrier
  map is unitary;
- Q1 and Q2 are two distinct, executable local parameter cells, so inherited
  principles do not select `q`, `g`, root data or omitted sectors;
- D24 is correctly called the right **inherited one-parent newborn-content
  family for this frozen exhibit**, not the unique universal birth law;
- cycles, peer joins, disconnected joins, coherent graph-sector sums,
  Lorentzian geometry and nature's law remain explicitly open.

The phrase “D24 is right” is therefore adequately scoped in section 13.5. I
find no overclaim there once it is read with both numbered clauses.

## 6. Openings exposed by this review

1. **Flagged CQ lift:** construct the explicit classical-output/quantum-carrier
   instrument for the timeless rooted-call law with one fresh bounded event
   factor per realized cell.
2. **Quantum restriction:** prove the flagged operator family is consistent
   under finite causal down-set restriction, not only that its classical first
   call is the marginal of two calls.
3. **Physical transfer:** replace ephemeral query provenance with persistent
   local transfer records or an intervention-indexed evidence theorem.
4. **Typed multi-leg grammar:** formalize visit/fork legs and test malformed
   merges before extending to peer or disconnected joins.
5. **NSE scope:** decide explicitly whether D35 seeks only a classical history
   measure with conditional quantum carriers or a full NSE quantum history
   law. The present executable delivers the former.

## 7. Disposition

| Audit target | Disposition |
|---|---|
| D35 exact receipt | reproduces byte-for-byte |
| Branch counts and probabilities | exact |
| D24 marginal instant | correct |
| Branchwise birth isometry | pass |
| Branchwise return unitarity | pass |
| Orthogonal durable event factors | **not implemented** |
| Busch/NSE closure of the q-mixture | **not proved** |
| Complete quantum history law | **not constructed; appropriately open only after wording repair** |
| Structural ancestry acquisition | pass |
| Physical evidence transfer | **not established** |
| D24 “right kernel” scope | adequately narrow |
| Multi-leg event typing | generated paths legal; schema/gates incomplete |

**Final count:** **0B / 2M / 1m / 2n.**

**Final verdict:** retain the timeless normalized classical family and the
exact D24 branchwise birth result. Do not promote the provisional row-2 noun
under the full pinned O6/physical-acquisition wording until M1 and M2 are
repaired or explicitly narrowed. No exact arithmetic repair is requested.
