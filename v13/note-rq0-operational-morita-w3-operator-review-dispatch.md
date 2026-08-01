# External hostile review dispatch — operator algebra and Morita theory

**Mode:** repo-read-only, independent mathematical rebuild

**Governing pin commit:** `35a4878`

**Immutable paper commit:** `a1fa2c9`

**Paper SHA-256:**
`cb36418645f845fc35b9e1c77e71a37f1c5a9d6779cae8526a2dfba2ff138537`

**Target:** `v13/paper-rq0-operational-morita-w3.md`

---

## Mandate

Independently review the paper as an operator-algebra/Morita-theory hostile
referee. Do not edit the repository, repair the paper, or defer to its theorem
labels. You may use `/private/tmp` for scratch. Rebuild every load-bearing
finite theorem from definitions.

## Required attacks

1. **Boundary-module theorem.** Check the orientation and fullness hypotheses
   for the imprimitivity bimodule, the equivalence
   $M\mapsto M\otimes_A X$, and the claimed *-isomorphism of adjointable
   endomorphism algebras. Test nonfree finite modules and direct-sum
   C*-algebras, not only $\mathbb C\sim M_n$.

2. **Marked Morita type.** Determine whether Definition 3.4 is a substantive
   operational equivalence or a tautology that simply demands an isomorphism
   of all represented process data. Check whether states, effects, CP maps,
   instruments and scalar contexts really transport coherently and whether
   the process grammar has a uniform type.

3. **Operational quotient.** Check that the represented image is actually
   formed before seams, and that equality is a congruence for every used
   constructor. Look for dormant or syntactic structure that remains in the
   moduli object.

4. **Classical-object typing.** Verify the PVM/*-homomorphism equivalence and
   decide whether the paper has really constructed a commutative
   dagger-Frobenius object in the declared CP/correspondence setting, or only
   a module representation of $\mathbb C^n$. Check that Morita transport does
   not falsely claim to transport a selected subalgebra of $A$ into $B$.

5. **Universal block theorem.** Verify
   $\operatorname{Fix}(\mathcal D_R)=C_R'$ and all four equivalences at the
   operator-system scope. Check the full-matrix unitary negative and the
   distinction between block preservation and sharp readout.

6. **W3 Morita theorem.** Recompute every write, no-write, preservation,
   readout and eraser scalar under the endomorphism *-isomorphisms. Determine
   whether nonzero W3 data survive a general marked imprimitivity equivalence
   without hidden representation choices.

7. **Spectator theorem.** Check the standard
   $\mathbb C$--$M_n$ imprimitivity module, the observable algebra of the
   amplified right module, and the difference between induced and physical
   spectator markings. Attack the claim that all raw spectator isotropy is
   operationally ineffective.

8. **Addressability.** Verify the full Karoubi category, its CP corner maps,
   Morita transport and the exact two-dephasing noninvertible arrow. Look for
   direction, unitality, Choi--Effros or admission defects.

9. **Branch benchmark.** Independently rebuild the nine-candidate result and
   the raw/effective symmetry calculation. Check the asserted
   $U(1)\times S_4$ group and whether $\mathbb C^2$ versus $\mathbb C^3$
   really blocks marked Morita equivalence.

10. **Scope and sources.** Check every use of standard Morita, CP-map,
    Frobenius and rigidification literature. Flag any result stronger than
    its cited theorem.

## Mandatory counterexamples

Try at least:

- a nonfull Hilbert module;
- a direct-sum algebra with center-changing correspondence;
- bare Morita-equivalent algebras with inequivalent complete markings;
- a CP map not induced by conjugating a fixed endomorphism algebra;
- a classical action that transports to a module action but not a subalgebra
  of the target coefficient algebra; and
- a matrix spectator with one extra accessible effect.

## Verdict

Return one of:

- `ACCEPT`;
- `ACCEPT-WITH-FIXES`;
- `HEADLINE-DOWNGRADE`;
- `REJECT`.

State separately whether each registered rung is earned:

- `RQ0-L0-COMPLETE-INSTRUMENT-W3`;
- `RQ0-L0-MORITA-INVARIANT-W3-SEAMS`;
- `RQ0-L0-EFFECTIVE-W3-SEAM-STACK`;
- `RQ0-L0-FULL-ADDRESSABILITY-FIBRATION`.

Preserve any earlier rung that survives a later failure. Give exact
counterexamples and line references. Return the complete report in your final
message; do not summarize it into a few bullets.

No topology, influence, causality, field or gravity objection is relevant to
this paper's declared ceiling.
