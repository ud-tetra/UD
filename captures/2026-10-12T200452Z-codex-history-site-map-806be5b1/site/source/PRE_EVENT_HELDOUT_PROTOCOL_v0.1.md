# Constitutive Receipt-Index Event Operator — Pre-Event Test Protocol v0.1

**Status:** `FROZEN CANDIDATE TEST PROTOCOL`  
**Target access:** forbidden until prediction artifact is sealed.

## Predictor inputs

Allowed:

1. frame-aligned current state \(\bar\theta_n^-\);
2. source-derived dimensions
   \[
   d_n^-=\dim\mathcal L_n^-,
   \qquad
   d_n^+=\dim\mathcal L_n^+;
   \]
3. pair-integrity vector \(T_n\);
4. pre-event quadratic burden vector \(W_n^{B2}\);
5. exact source receipts used to construct \(\mathcal L_n^\pm\).

Forbidden:

- observed \(\theta_n^+\);
- terminal residuals;
- target event polarity;
- target event multiplicity;
- post-event lineage repairs;
- target-aware tie breaking.

## Frozen law

\[
\mu_{\Theta,n}=d_n^- - d_n^+.
\]

\[
k_n^+=w_H(\bar\theta_n^-)+\mu_{\Theta,n}.
\]

If \(k_n^+\notin\{0,1,2,3\}\), verdict is `SOURCE_INFEASIBLE`.

Otherwise:

\[
\Theta_{{\rm opt},n}
=
\arg\min_{\theta\in\mathcal A_{k_n^+}(T_n)}
\sum_p\theta_pW_{p,n}^{B2}.
\]

- empty set -> `SOURCE_INFEASIBLE`;
- non-singleton optimum -> `HOLD_UNRESOLVED_SYMMETRY`;
- singleton -> freeze \(\theta_n^+\), \(c_{\Theta,n}\), \(o_{\Theta,n}\), \(a_n\), \(\mu_{\Theta,n}\), and gross toggle count.

## Test

Only after the prediction file hash is frozen may the actual endpoint receipt be released.

Exact endpoint equality is the primary finite test.

Diagnostics may decompose:
- Hamming shell;
- net multiplicity;
- close addresses;
- reopen addresses;
- gross toggle count.

Diagnostics cannot rewrite the primary verdict.

## Reopen rule

A failed held-out endpoint prediction does not permit changing:
- the index orientation;
- burden objective;
- integrity rule;
- tie rule;
- source-space construction.

Any repair requires a new version and a fresh held-out corpus.
