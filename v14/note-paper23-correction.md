# PAPER-23 — A CORRECTION ANNOTATION (not an erratum, not a scope note)

**Registered by:** the SMU adjudication (v14 ledger #242,
`v14/note-smu-adjudication.md`), on K2's ruling in
`v14/review-smu-effectus.md` §3.
**Object annotated:** `v14/paper-23-measure.md` (`79cc67b4f6cd`), terminal at
commit bb26ca4 — **untouched**. Its instrument, receipt, verdict, census and
every published number stand exactly as delivered.
**Successor that measured the defect:** SMU, paper-27, the stationary measure.

**Species.** The paper-12 / R4 precedent supplies the *mechanism* — a standing
note registered against a terminal paper, which is never edited — but not the
*ground*. Those notes are SCOPE annotations: two different objects, claims
form-scoped and true at their own scope. This is a different species. Here
there is one object (finite Markov chains) and one statement, and its
biconditional is simply too strong: paper-23 had no chains at all, so the
scope in which its converse is safe is empty. It is not an erratum either,
because nothing of paper-23 moves. It is a **correction annotation**.

---

## The four clauses

1. **The inherited form is sufficient and not necessary.** The sharp
   condition is `EXACTLY ONE CLOSED COMMUNICATING CLASS`; the stationary
   simplex has dimension (closed classes − 1); irreducibility implies one
   closed class and not conversely.

2. **The witness:** 3 states, 2 communicating classes, 1 closed, simplex
   dimension 0 — it derives, and it is not irreducible.

3. **Nothing of paper-23 moves**: the criterion was the forward requirement of
   a named-absent row and was never applied to a chain; on paper-27's census
   the two readings return the same 12 deriving instances (0 transient classes
   at 18 of 18).

4. **Corpus-wide caution, in the paper-12 register's voice:** any unit that
   inherits "derives iff irreducible" from paper-23's head is quoting a
   biconditional whose converse fails, and must gate on the **closed-class
   count**. Where the two coincide, say so and measure it (as paper-27 does);
   do not assume it.

---

## Where the correction is carried, and how it is gated

Paper-27 carries the sharp form in its own verdict string, exhibits the
witness on a declared three-state chain solved by the same exact elimination
every instance of its census uses, and verifies the dimension identity
exhaustively over the three-state and four-state layers — every chain solved,
zero mismatches between the kernel dimension and the closed-class count. The
two gates are `G-THE-INHERITED-LAW-IS-SUFFICIENT-NOT-NECESSARY` and
`G-SIMPLEX-DIMENSION-THEOREM` in `v14/code/smu_exact.py`.

The correction also reaches the boundary of paper-27's own price theorem: a
covariant chain at an invariant target *with zeros* has those zeros as
transient states and exactly one closed class, so under the sharp criterion it
derives, which is why the covariant-dynamics fibre surjects onto the **closed**
invariant simplex and not merely onto its interior. Under the superseded
biconditional that arm would have read as reducible and the theorem would have
been stated weaker than it is.

**Standing instruction.** This note is the register row. It is not an
instrument input, no gate reads it, and it does not change any pinned digest.
A successor inheriting paper-23's criterion cites this note beside it.
