# JCV solver post-commit verification

Status: **GENERIC-SOLVER-POSTCOMMIT-VERIFIED**.

Verified commit:
`aa9a54af19f445e3a2067bf12abb603564c10016`.

The physical JCV fixture, scorer, output, receipt, and paper paths were absent
for every check in this note.

## Checks

- A normal execution from the committed worktree returned exit code 0 and
  reproduced `jcv_public_output.txt`, `jcv_public_receipt.json`, and
  `note-jcv-solver-freeze.md` byte-for-byte.
- `--selftest` returned exit code 0 by killing its injected anchor mutation at
  `G-ANCHORS`, without changing an artifact.
- `git diff --exit-code` found no movement in the three generated artifacts.
- `git archive` exported exactly the committed solver and declared source
  anchors into `/private/tmp/jcv-git-offtree.VzsDE2`.
- That archive contained no `.git` path, was executed from the alien working
  directory `/private/tmp`, returned exit code 0, and reproduced all three
  artifacts byte-for-byte.

The temporary directory name is evidence only, not a source dependency.  No
JCV physical result is licensed by this verification.  The next authorized
event is the separate physical fixture and verdict-neutral scorer freeze.
