# UD-PM-PRED01-001 v1.0 — WBX1 four-event invariant and singular branch

Kind: IDENTITY, exact conditional.
Proof status: VERIFIED_SCOPED (author/independent-method check, not outside peer review).
Review: DEFERRED. Physical promotion: 0.
Source: UD preregistration v1.0 Part A, blob c5ddbb6f4df4ba3ff5c6b39895b58c6e955fc82b; errata v1.1 sections E.1-E.2, blob 6961b917f4f1ca470127aa0b7d3c1b59693f4373; research PR #475 (unmerged).

## Statement

Let A>0, C,kappa be real scalars. For nonnegative integer j assume f_0=0,
epsilon_j=A+C*j+kappa*f_j and f_(j+1)=f_j+epsilon_j.
Here f and epsilon are abstract native cost readouts, not calibrated laboratory energies or qualified native winding carriers. Define d_j=epsilon_(j+1)-epsilon_j.

Then epsilon_(j+1)=(1+kappa)*epsilon_j+C,
d_(j+1)=(1+kappa)*d_j, d_0=C+kappa*A, and
(d_0)*(d_2)=(d_1)^2.
For four events this is
(epsilon_1-epsilon_0)*(epsilon_3-epsilon_2)=(epsilon_2-epsilon_1)^2.

If d_0 != 0, the WBX1 family uniquely identifies kappa=d_1/d_0-1 and C=d_0-kappa*A from the first three event readouts. If d_0=0, all epsilon_j=A and any kappa with C=-kappa*A fits, so kappa is nonidentifiable even with all events.

## Proof

Subtract consecutive definitions of epsilon:
epsilon_(j+1)-epsilon_j=C+kappa*(f_(j+1)-f_j)=C+kappa*epsilon_j.
This gives the first-order recurrence. Subtract the recurrence at successive indices to obtain d_(j+1)=(1+kappa)*d_j. At j=0, f_0=0 and epsilon_0=A, hence d_0=C+kappa*A. Therefore d_1=(1+kappa)*d_0 and d_2=(1+kappa)^2*d_0; multiplying gives d_0*d_2=d_1^2.

When d_0 != 0, division determines kappa and substitution determines C. When d_0=0, all successive differences vanish; epsilon_j=A. Conversely C=-kappa*A satisfies the generating equation for every kappa. QED.

## Counterexample and limits

The four-event identity is necessary but NOT sufficient: the proposed sequence (1,1,1,2) has d=(0,0,1) and satisfies 0=0, but cannot be produced by a constant-coefficient WBX1 recurrence. Positive increment costs alone do not eliminate the nonidentifiable branch: A=1, C=-2, kappa=2 yields epsilon_j=1 for all j.

## Verification and disposition

Separate SymPy expansion in the current session gave differences
[A*kappa+C, (1+kappa)*(A*kappa+C), (1+kappa)^2*(A*kappa+C)]
and simplified the determinant identity exactly to 0; substitution C=-kappa*A yielded epsilon=[A,A,A,A]. This is a method check, not a non-constructor review.

Result: VERIFIED_SCOPED EXACT_CONDITIONAL. Missing native carrier qualification, independent leakage, units, calibrated physical readout, real data and physical promotion remain OPEN_GATED. This proof narrows the prior unqualified three-event parameter inference without overwriting its source.
