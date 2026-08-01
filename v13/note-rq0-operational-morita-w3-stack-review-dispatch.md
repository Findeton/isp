# External hostile review dispatch — higher stack, localization and rigidification

**Mode:** repo-read-only, independent categorical rebuild

**Governing pin commit:** `35a4878`

**Immutable paper commit:** `a1fa2c9`

**Paper SHA-256:**
`cb36418645f845fc35b9e1c77e71a37f1c5a9d6779cae8526a2dfba2ff138537`

**Target:** `v13/paper-rq0-operational-morita-w3.md`

---

## Mandate

Independently review the paper as a bicategory/localization,
higher-stack/rigidification and Grothendieck-fibration referee. The repository
is read-only. Do not repair the paper. Use `/private/tmp` only for scratch.

## Required attacks

1. **Localization order.** Determine whether the operational Morita
   localization is genuinely constructed before seams or merely named before
   a representative-level seam category is formed. Check the universal
   property, objects, 1-morphisms, 2-morphisms and coherence actually used.

2. **Typed bicategory.** Audit the separation between Hilbert-bimodule
   correspondences, CP maps, instruments and adjointable intertwiners. Reject
   any untyped mixture. Determine whether a double category/equipment is
   implicitly needed and missing.

3. **Descent of classical actions.** Check that the W3 assignment is a genuine
   pseudofunctor on the localized base and that its Grothendieck category is
   not a quotient-after-the-fact. Attack associators, units and dependence on
   chosen quasi-inverses.

4. **Effective isotropy.** Verify that $K_s$ is a subgroup, that the family is
   conjugation-stable, and that the double-coset relation on hom-sets gives a
   well-defined quotient groupoid. Check whether defining $K_s$ using the
   later addressability category is circular.

5. **Spectator kernel.** Determine whether inner spectator automorphisms are
   actually objects/arrows of the raw marked groupoid and act trivially on
   every marked datum. Reject hand-waving that “Morita localization” alone
   removes them. Check that effective physical symmetries survive.

6. **Use of stack language.** Decide whether the finite rigidified groupoid
   justifies the registered word “stack” at its explicitly narrow scope. No
   sheaf, topology or general algebraic-stack claim may be inferred.

7. **Full addressability pseudofunctor.** Check its variance, descent through
   rigidification, coherence and object/morphism typing. Verify that the
   Grothendieck construction is a fibration (and, if claimed, opfibration)
   without assuming fiber arrows invertible.

8. **Noninvertible arrows.** Rebuild $e_me_n$ as a Karoubi arrow and determine
   whether the full fiber is closed under every admitted composite. Check that
   “all admitted” is not an unspecified class that makes the theorem
   tautological.

9. **Branch symmetry groupoid.** Independently verify the
   $U(1)\times S_4$ raw symmetry claim, ineffective phase kernel, two
   effective components and retention of stabilizers. Distinguish connected
   components from quotient objects.

10. **No-selection and claim ceiling.** Ensure no representative is chosen
    from a physical orbit and no groupoid result is promoted to spatial
    localization or overlap.

## Mandatory counterexamples

Try:

- a normal isotropy family that is not conjugation stable;
- ineffective automorphisms acting only up to natural isomorphism, not
  strict equality;
- a pseudofunctor whose kernel acts nontrivially on fiber morphisms;
- a covariant Grothendieck construction incorrectly called a fibration;
- a noninvertible base arrow (which is outside the declared seam groupoid);
- two Morita presentations requiring nontrivial associator coherence; and
- a physical symmetry stabilizing an object while permuting its fine
  alternatives.

## Verdict

Return `ACCEPT`, `ACCEPT-WITH-FIXES`, `HEADLINE-DOWNGRADE`, or `REJECT`.
State separately which registered rungs survive. A failure of effective
rigidification or the full fibration must not erase a sound
complete-instrument or Morita-invariance rung.

Return the complete report with exact counterexamples and line references in
your final message. Do not mutate the repository.

No topology, influence, causality, field or gravity work belongs in this
review.
