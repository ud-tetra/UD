# Two-level selector coherence: exact conditional result

Status: conditional mathematical theorem and exact replay. Native adoption OPEN; independent human review PENDING; physical promotion 0.

Write `S10:C0→C1`, `S21:C1→C2`, and affine chain retractions `R10`, `R21`, with `Ri Si=I`. Set `Qi=I−Si Ri`, `S20=S21 S10`, `R20=R10 R21`, and `Q20=I−S20 R20`. Each boundary commutes with its respective subdivision and retraction.

## Exact split

The elementary identity

`Q20 = Q21 + S21 Q10 R21`

follows by expanding the right-hand side. Therefore every fine state has the unique hierarchical decomposition

`x = S20(R20 x) + S21(Q10 R21 x) + Q21 x`.

The last two components are in the old and new residual sectors respectively. Their uniqueness follows by first applying `R21`, then `R10`, and then the relevant `Q`.

## Sequential and one-shot metrics differ

The previous conditional one-step selector with unit residual calibration gives

`H1 = R10ᵀ G0 R10 + Q10ᵀ Q10`.

Applying it again gives

`H2_seq = R21ᵀ H1 R21 + Q21ᵀ Q21`

`= R20ᵀ G0 R20 + (Q10 R21)ᵀ(Q10 R21) + Q21ᵀ Q21`.

The direct unit-final-residual rule gives instead

`H20_unit = R20ᵀ G0 R20 + Q20ᵀ Q20`.

Both preserve the original code metric, chain map, and weighted-adjoint dynamics. They need not agree on retained residual states. This is a failure of additional path coherence, not a failure of those previously established one-step properties.

Take the degree-1 vector `z=[({0}⊂{0,1})]+[({1}⊂{0,1})]` in `C1`. Its affine retraction vanishes; its Euclidean norm squared is 2. For `x=S21 z`, `R20 x=0`, `Q21 x=0`, and `Q20 x=x`. Thus

`||x||²_H2_seq = 2`, while `||x||²_H20_unit = 4`.

For a pure degree-k old residual, subdivision has disjoint signed support and `S21ᵀ S21=(k+1)! I` in that grade. The direct-to-sequential ratio is therefore `(k+1)!`: 2, 6, 24 in degrees 1, 2, 3. Degree-zero has ratio 1. Explicit canceling determinant pairs witness each positive degree.

## Coherent direct residual calibration

If retained lower-level receipts must remain unchanged, replace unit final-coordinate calibration by the positive form on `ker R20`

`W20(q,q) = ||Q10 R21 q||² + ||Q21 q||²`.

For `q=Q20 x`, the first term equals `||Q10 R21 x||²` and the second equals `||Q21 x||²`. It follows that the corrected direct metric equals the sequential metric exactly. Positivity follows because simultaneous zero residual components imply `q=0` by the split. This is a hierarchy-dependent calibration requirement; the existing sources do not select it as a native constitutive law.

For a general positive old residual pairing `W1` and new residual pairing `W2`, the analogous form is

`W20(q,q)=W1(Q10 R21 q,Q10 R21 q)+W2(Q21 q,Q21 q)`.

## Coherent observable partition

For source coordinate effects `D_i≥0` summing to `G0`, retain the 15 coarse effects `K_i=R20ᵀ D_i R20`, the old residual effect `(Q10 R21)ᵀ(Q10 R21)`, and the new residual effect `Q21ᵀQ21`. These 17 positive effects sum to `H2_seq`. The source-region effect is subdivision compatible and blind to both residual sectors. The residual receipts also preserve their previous-level values on encoded old states. Unit-final-residual calibration instead changes their normalized shares in mixed coarse/residual states.

More levels follow recursively: each level contributes one retained residual pairing and coarse effects transport by the composed retraction. No arbitrary target spectrum or measured output was used to choose a metric.
