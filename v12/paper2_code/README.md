# Paper 2 code bundle

Reproduction bundle for *Record Co-reference and Effective Descent in
Local Stochastic Atlases* (`../paper2-record-coreference.md`).

- `core.py` — exact finite co-reference/descent machinery: fractions,
  permutations, stochastic charts, fact certificates, full/realized
  isomorphisms, descent solver, natural-choice test.
- `models.py` — exact fact controls and the five-configuration
  completion-sensitivity witness.
- `run_all.py` — executes every result; exits nonzero on any mismatch.
- `RUN.txt` — output of one complete run: 39 checks, 39 pass, 0 fail.

Python 3.11+, standard library only, no floating point.

```bash
cd paper2_code
python3 run_all.py
```
