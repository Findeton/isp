# PRIVATE PREFLIGHT AUDIT — dual-route operational-clock package

Date: 2026-08-23

Status: **PRIVATE / OFF-TREE / NO OFFICIAL REVIEW**

Disposition: **REVISE BEFORE AUTHORIZATION**

This is a hostile root audit of the private v9 package. It is not an independent
panel report and awards no result. The audit preserves the useful record-to-clock
and scheduled-simulator no-gos but finds one central ambiguity and seven required
scope corrections before the proposed pin is suitable for an official cycle.

## 0. Authenticated inputs

```text
repository HEAD
1e27457a62ac32dc85e41ca8bc36bc3f4d52702f

private manifest v9
ce65db1a3784b1c0396a511b1caa6e22e0d9f4626fa4164363d8a82d154cb6bd

dual-route pin draft v1
d80f9b6bb981c48c36e0d671af775d5a3bee024085797cd08ce7621a29b8ed43

generic theorem package
77a6c898164463d8fbc8c55033df3fbc9a345fdfa21e62efc76d9911c897b4b6

architecture selection
83f4ffa68ee2a98c32a5c48086ca80b7c83cd9bb87d1ae54c3fca38944dc36b0

record-to-clock bridge
80b6c0e071dba6e19482f4e6db4dbe61bacde3ca9e2f84f4989db7879095e070
```

Repository tracked and staged diffs were empty. The unrelated untracked v16 note
was not opened.

## 1. Central semantic correction — one law, two derivations

The v1 package sometimes describes the constrained and autonomous routes as
"independently constrained" parents and sometimes as two descriptions of the
same experiment. These are not the same scientific claim.

If they are unrelated laws fitted to the same transcript, agreement is ordinary
model underdetermination and does not establish one clock-neutral physics. If the
autonomous route is obtained by generically dilating the constrained instrument,
agreement is automatic representation theory. Neither is the desired result.

The correct structure is:

1. freeze one physical parent law P;
2. derive its constrained/clock-neutral semantics by route F_con;
3. derive its autonomous complete-experiment semantics by route F_aut;
4. prove those derivations agree internally; and
5. test P against an independently frozen laboratory comparator on held-out
   interventions and readers.

Thus

$$
\mu^{\rm con}_e=F_{\rm con}(P,e),
\qquad
\mu^{\rm aut}_e=F_{\rm aut}(P,e),
$$

and route equality is a consistency coordinate. The empirical coordinate is

$$
\mu^{P}_e\stackrel{?}{=}\mu^{\rm lab}_e
$$

on frozen held-out experiments. The routes may be independently derived, but they
may not be different physical laws.

This changes the evidential interpretation, not the record mathematics.

## 2. External parameter versus supplied schedule

The v1 question says the predictor should work "without a runtime schedule
input." Yet its complete transcript and adaptive experiments contain supplied
ordered slots. The intended claim is narrower:

- remove the external scalar/orbit/runtime parameter from the predictor;
- retain the experiment identity, policy, and causal-slot order as supplied
  physical context; and
- do not claim that chronology has been derived.

The corrected pin must use this wording everywhere. Otherwise a successful model
would either fail its own interface or overclaim causal-order removal.

## 3. Autonomous realization is not autonomy selection

The scheduled-simulator theorem correctly proves that no finite transcript family
can exclude all externally scheduled completions. A fixed Hamiltonian or endpoint
law may construct an autonomous realization, but finite operational data do not
select it uniquely as nature's mechanism.

The positive coordinate must therefore be:

```text
FINITE-AUTONOMOUS-REALIZATION-CONSTRUCTED
```

not an unqualified proof that the physical mechanism is autonomous. Its evidential
weight comes from predeclared locality/resource restrictions and held-out
interventions, while the ontology remains underdetermined.

## 4. Physical evidence must not be route agreement

The v1 headline risks making dual-route equality the main positive event. That is
still largely representational. The promotion-bearing observations must instead
include:

1. nontrivial clock intervention response;
2. no-clock, mistuned-clock, stopped-clock, and interaction-deletion separation;
3. finite-clock/resource effects predicted before held-out data;
4. complete adaptive transcript prediction;
5. an independently calibrated comparator; and
6. where claimed, second-clock held-out agreement.

Route equality verifies internal coherence. It does not replace empirical
adequacy.

## 5. Scheduled-simulator theorem must use one parent

The theorem package constructs a simulator "for each experiment e." A critic
could object that this silently changes laws between experiments. The stronger and
correct statement is immediate: include e as a physical input to one universal
simulator, use one external random seed, and sample from the kernel mu(dx|e). This
single parent reproduces the entire finite experiment family.

The corrected theorem should print this version.

## 6. Nonideal-measurement scope

The finite Gram-matrix formula is a useful coherence-versus-diagonal instrument
schema. It is not a general derivation of the full twirled-observable versus
purified-measurement frameworks in the literature. The corrected package must
call it a finite operational discriminator and require model-specific derivation
before applying it to those approaches.

## 7. Provenance is a certificate, not a theorem

Whether two derivations copied one another's held-out outputs is a chronology and
dependency fact about the construction process. It is not a theorem of the
physical model. Rename T8 to a route-provenance certificate and bind it to frozen
artifacts, dependency graphs, and parameter ledgers.

## 8. Architecture selection may use public results

Stage B's statement that no outputs may be calculated during selection is too
broad. Selection must use published theory, public benchmark results, and
calibration evidence. The prohibition should cover only the future candidate's
registered held-out outputs and any outcome-dependent parameter/model choice.

## 9. The first empirical target remains standard quantum physics

The record and clock constructions currently sit inside standard quantum theory.
A successful laboratory test may validate the finite clock architecture and
exclude particular noise/mechanism models, but cannot confirm the native ontology.
Any genuinely new physical prediction must be separately identified and frozen.

This is not a reason to stop. It is a reason to keep the result label honest.

## 10. What survives unchanged

The following private results survive this preflight:

- the record/clock/chronology/metric hierarchy;
- record does not entail clock;
- finite periodic phase does not entail global time;
- clock correlation does not entail chronology;
- two clocks do not entail metric;
- invariant finite record mathematics;
- complete transcript measure criterion;
- endpoint transcript compilation without a path realizer;
- scheduled-simulator nonselection;
- generic dilation nonselection;
- local stopped/recurrent clock rules;
- native endpoint-law commuting square;
- chronology, metric, gravity, and actuality walls; and
- the one-attempt/no-automatic-model policy.

## 11. Required forward repair

One clean private v2 pin should:

1. replace two-parent language with one-parent/two-derivation language;
2. demote route equality to internal consistency;
3. make held-out physical response the promotion-bearing evidence;
4. distinguish external scalar parameter removal from supplied slot order;
5. rename autonomy and provenance coordinates;
6. strengthen the single-parent scheduled-simulator no-go;
7. narrow the finite measurement-fork schema; and
8. clarify public-evidence use during model-family selection.

No model, parameter, or repository action is justified before that repair.

## 12. Disposition

```text
RECORD-TO-CLOCK-BRIDGE:          SURVIVES
ARCHITECTURE-FAMILY:             REVISE TO ONE PARENT / TWO DERIVATIONS
DUAL-ROUTE-EQUALITY:             INTERNAL-CONSISTENCY ONLY
PROMOTION-BEARING EVIDENCE:      HELD-OUT PHYSICAL RESPONSE
AUTONOMOUS MECHANISM:            REALIZATION / NOT ONTOLOGY SELECTION
EXTERNAL-TIME CLAIM:             SCALAR-PARAMETER TASK REDUNDANCY ONLY
PRIVATE PIN v1:                  REVISE BEFORE AUTHORIZATION
REPOSITORY UNIT:                 CLOSED
```

No repository file was edited.
