# Winding-to-Burden Source-Law Admission Protocol v0.1

**Status:** `FROZEN AFTER STRUCTURAL MAP CLOSURE`

The vector placement of isolated winding burden is fixed:

\[
b_W(n)=\frac{f_W(|n|)}4\mathbf1_4.
\]

A future proposal for the remaining scalar law \(f_W\) must specify:

1. formation/source variables;
2. why the law acts on \(|n|\), \(\eta_n\), or another declared winding
   observable;
3. neutral behavior \(f_W(0)\);
4. charge-conjugation behavior;
5. regularity at the neutral point;
6. scaling/homogeneity rule;
7. locality/composition rule;
8. normalization source;
9. no physical mass backsolve;
10. behavior on the frozen \(n=0,1,2\) ladder.

## Automatic tests

If the proposal is linear in signed \(n\), reject unless identically zero.

If it is differentiable and charge-even, require

\[
f_W'(0)=0.
\]

If it is one-homogeneous, require the exact \(|n|\) form.

If it claims to be derived from \(D_{\rm pair}\), \(D_{\rm chain}\), or a
context burden, require a typed bridge to \(C_0^{\rm burden}\) first.

## Re-score

Once \(f_W(1)\) and \(f_W(2)\) become source-complete, the matched ladder has

\[
z_0=0,\quad z_1=f_W(1),\quad z_2=f_W(2),
\]

and WBL1/WBQ1 may be scored under the existing frozen protocol.
