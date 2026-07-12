# D7 final receipt — extension rulebook characterization and nonselection

**Date:** 2026-07-11

## Scope

D7 characterizes the complete missing extension rulebook, audits V1–V9,
constructs candidate architectures before literature search, compares them
against primary literature, and supplies exact finite nonselection witnesses.
It does not claim a unique interacting click law or literature priority.

## Reproduction

```text
python3 v10/code/d7_rulebook_nonselection_exact.py
python3 -O v10/code/d7_rulebook_nonselection_exact.py
```

Both runs pass 68/68 checks and produce byte-identical stdout.

```text
D7 RULEBOOK NONSELECTION RECEIPT
checks=68
flat_transfer_product=6/1
normalized_path_A_then_B=1/4
normalized_path_B_then_A=1/3
activity=1/2 P_terminal_AB=4/5 P_terminal_C=1/5
activity=1/1 P_terminal_AB=2/3 P_terminal_C=1/3
activity=3/1 P_terminal_AB=2/5 P_terminal_C=3/5
KL(Bernoulli(1/3)||Bernoulli(2/3))=0.23104906018664843647241070715272552269183337812008508470689333649779787398989823853528777566547289584733382701
receipt_sha256=1feaa1fb2aeadf539f8e3f33ac670c673a1ef538ba708ad3936cea0dc2fb4a9e
```

Stdout SHA-256:

```text
0bfb3413516003895bdb099e6904794badb12d1920d2ceea7e4b4fbe7bcf6ab5
```

## Frozen file hashes

```text
9395ec726c84cd1d3bb152faac89c11d791700879a12e2ffc9291f52918b7020  v10/code/d7_rulebook_nonselection_exact.py
328f5e5c0deb1f3aa2444e55651e2da9149f1025d44388593446a5b7556b3c9f  v10/note-d7-extension-rulebook-characterization.md
05d5efa0b8c671905f7ec55b88082172224fa5a6b8847bfbf764e5a579399212  v10/note-d7-independent-rulebook-architectures.md
fa69127c3dbf79c67621f4f70261402eb677e1ebc550dbbd8dd220285fcde07c  v10/note-d7-literature-and-priority-audit.md
953a3279a2b2d62bdd123af08582fb8327fa2bc2276ed14bb8a2066aa3926598  v10/relativistic-isp-v10-paper8-the-extension-rulebook-is-extra-physics.md
```

## Claim boundary

```text
RULEBOOK-MATHEMATICALLY-CHARACTERIZED
+ V1–V9-NO-COMPLETE-SELECTION
+ EXACT-STRUCTURAL-NONSELECTION
+ FOUR-LAYER-ADMISSIBLE-CLASS
+ COMPONENTS-PRECEDED-IN-LITERATURE
+ FINAL-LAW-REQUIRES-NEW-PRIMITIVE-OR-EMPIRICAL-POSTULATE
```

The self-containment audit passes 4/4: all D7 executable source is under
`v10/code/`, uses only the Python standard library, has no duplicate source
outside that directory, and leaves no cache artifact under `v10/`.
