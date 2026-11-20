# UD Whitney S4 Dual-Coframe Audit v0.1

Run in this directory with Python 3 and SymPy:

```bash
python verify.py
python replay_stdlib.py
```

`verify.py` independently constructs oriented edge forms and checks all signed S4 actions, full 64-sign classification, exact D1 eigenspace determinant, counterexample and Whitney/dual source typing. `replay_stdlib.py` checks the central facts with standard-library `fractions.Fraction` and independently coded determinants.

**Outcome:** 4 signed S4 sign orbits, rank3 on 8+8, rank2 at barycenter on 24+24; the D1 eigensector determinant is `abc*sum(lambda_i^2)`; no source-selected signs, rates, physical metric or correspondence. Both programs are author/constructor checks, NOT a non-constructor review. Physical Promotion 0. See `REPORT.md`.
