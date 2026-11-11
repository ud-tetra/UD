# Received review script: hash binding and verification coverage

**SCRIPT RECEIVED AND REPRODUCED; FULL AUDIT CERTIFICATE NOT ESTABLISHED.** Development — no registry entry. Physical promotion: 0. Devin Ramos's user-attested non-constructor attribution and disclosed AI assistance remain recorded. This intake is a constructor check of the supplied program, not a new independent review.

## Binding mismatch

The uploaded7858-byte program has SHA-256:

`507fb13d83438a8462d74adff20f66b823397facf71115a1b31c41b9fb343e81`

The current message and updated receipt instead specify:

`627cfd3b28693b2f8e7574dccc35ac231b0fd4b958c589a234a96cb29807f660`

These do not match. The earlier amendment's different hash is a prior declaration, not silently replaced. Preserve this uploaded version byte-for-byte and either supply the exact bytes associated with the current declared hash or issue an explicit new version bound to the actual received bytes. A line-ending or other transfer change could explain a mismatch, but no cause is inferred without evidence.

## Fresh execution

The code was read before execution. It contains arithmetic, assertions, printing and standard-library imports; it does not read evidence files or access a network. The exact captured bytes were run in a disposable working directory. Return code0, stdout and empty stderr are captured. This establishes a constructor reproduction now, not the date or environment of a historical external run. Full stdout equality with the pasted user transcript is not asserted; the decisive false PASS line appears in both.

The run prints:

`Sample Lehmann-Maehly / Temple enclosure half-width ||r||^2 / gap: 6.0186e-23 (< 1e-23) -> PASS`

But its own sample inputs give exactly

\[
\frac{(2\times10^{-13})^2}{0.000664605}
=\frac{1}{16615125000000000000000}
\approx6.01861255934\times10^{-23}>10^{-23}.
\]

The claimed inequality is false. The program has no assertion testing it and prints its all-eight-checks-passed footer unconditionally after its functions return. Return code0 therefore does not validate the claimed enclosure precision. This is a defect in the submitted verification program; it does not refute the original PR358 enclosure, which uses a much smaller certified rational trial variance.

## Coverage audit

| Claim area | What this program actually checks | What it does not establish |
|---|---|---|
| Topology | Arithmetic identity4^(L-3)=4^L/64 for L3,4,5 | Edge construction or connected-component enumeration |
| Theta spectrum | Evaluates stipulated formulas and sums stipulated ranks | Laplacian spectrum, projector ranks and reconstruction |
| Diagnostic | Uniform/empty-channel controls | General component identity or full degeneracy tests |
| Coupled sector | Checks delta²=49/36864 and prints trial-vector properties | Matrix Rayleigh quotient, orthogonality, intertwining, uniqueness |
| Shift-invert | Computes illustrative transformed distances from assigned values | ARPACK run or actual stored probe coverage |
| Six-coordinate sector | Checks one weighted-variance control |32/6-coordinate reductions, inherited metric, eigenvalue/weight intervals |
| Error budget | Compares two assigned shift/norm numbers; prints sample scale and variance ratio | Payload hashes, exact perturbation bound, all12 residuals or certified intervals |
| Non-constructor provenance | No computational check | Authorship/separation, input bindings or run history |

Correct mathematical explanations in the previous amendment can remain useful review statements. This table addresses the narrower claim that this script computationally verifies all C01–C08. It does not.

## Operator norm mismatch

The submitted program assigns A_inf=52.20296 as a sample scale. For the hash-verified PR352 full512-coordinate matrix, the exact infinity norm computed from its binary64 bytes is

\[
\|A\|_\infty=\frac{28105596915389682213}{288230376151711744}
\approx97.51087755093564.
\]

The assigned52.20296 value is close to a Theta spectral value; it is not the stored full matrix's infinity norm. The script's displayed maximum allowed residual therefore does not reproduce the frozen full-matrix acceptance calculation. Neither the sample scale nor assigned perturbation constants bind to evidence files. The new checker reads the actual payload, verifies its SHA-256 and computes the row sum exactly; it does not change the original threshold.

The program calls its Temple sample a half-width, whereas the original receipt uses a one-sided enclosure [mu-s²/(beta-mu),mu]. A complete reproduction must show the actual normalized trial vector, Rayleigh quotient, residual variance, certified beta and denominator, rather than substitute a convenient sample residual or generic acceptance tolerance.

## Disposition

The previously missing script has now been received, inspected and run. Keep that progress distinct from the unresolved hash binding and insufficient claimed coverage. The user-provided reviewer attribution remains accepted as attested; no additional identity authentication is requested. The submitted all-PASS computational certification is not adopted.

Next: correct the hash binding, replace unconditional PASS labels with checked conditions, and either narrow the receipt to the controls actually implemented or provide the missing source/payload-bound verification. Preserve the original file and this failed precision claim. Any corrected program and run should receive a new version and append-only receipt; do not silently edit the supplied evidence or rewrite its declared hash.

This intake makes no source edits, promotion ruling or physical identification. The original constructor evidence remains scoped as before; reviewer execution success cannot retroactively establish target blindness. `Gap2_FINAL_Finite_Genesis.png` remains unavailable and unused.
