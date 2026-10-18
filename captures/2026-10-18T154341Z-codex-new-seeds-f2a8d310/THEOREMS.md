# Fixed-reference temporal-span certificate

Development — no registry entry. Physical promotion 0. Exact conditional
finite-matrix theorem with validated constructor computations; independent
review pending. The reference phases are fitted parameters, not physical truth.

## 1. Amplitudes and the temporal frame are separate objects

Let n=8191, q=105 and let F have columns 1 and exp(plus/minus i k theta_j),
using the fixed 52 positive dyadic reference phases. Let P have the real columns
1, cos(k theta_j), sin(k theta_j). The complex change of columns from F to P has
singular values 1 (stationary column) and 1/sqrt(2) (each paired column). If

\[
 aI\preceq F^*F/n\preceq bI,
\]

then sigma_min(P)>=sqrt(na/2). These constants and the minimum reference
unit-circle chord separation s are recomputed from the fixed phases by validated
finite geometric sums and Gershgorin bounds, not accepted merely from a receipt.
The recomputation must agree with the pinned PR184 source values.

For any coefficient matrix C with row rank q, col(P C)=col(P). Changing a
stationary amplitude or any other coefficient while preserving row rank therefore
leaves the temporal subspace unchanged. A norm bound on P C-P C0 can nevertheless
be large. This explains a limitation of a fixed-amplitude residual proof without
establishing success of the estimator in general. Rank-deficient excitation is
not repaired by this identity.

## 2. Direct subspace residual

Take the actual captured binary64 basis U (n by q). Let
eta>=||U*U-I||_2 with eta<1. Its polar factor Q is orthonormal, has exactly the
same column space, and ||U-Q||_2<=d_U=eta/(1+sqrt(1-eta)). For any untrusted
auxiliary matrix D, suppose L>=||P-U D||_2 is validated. Because
(I-Q Q*)U=0 exactly,

\[
 \|(I-QQ^*)P\|_2\le L,\qquad
 \|(I-QQ^*)Q_0\|_2\le t:=L/\sqrt{na/2},
\]

where Q0 is any orthonormal basis of col(P). No d_U||D|| term is required in
this projection: the exact polar factor and U have the same range. D need not
be a least-squares solution and is never trusted on numerical accuracy alone.

For t<1, a unitary alignment O exists with

\[
 \|UO-Q_0\|_2\le d:=d_U+\sqrt{2-2\sqrt{1-t^2}}.
\]

This is the usual equal-dimension principal-angle alignment identity. It is
valid in the complexified real temporal span, so Q0 may be the orthonormalized
complex Vandermonde frame used for the shift bounds.

## 3. Exact residual evaluation

Every actual binary64 value in U,D is encoded without extra quantization using
as_integer_ratio. Let P_tilde be a dyadic real frame whose nonstationary entries
are each validated within 2^-60 of the true sine/cosine values. Then

\[
 L:= \|\widetilde P-UD\|_{2,upper}
       +\sqrt{n(q-1)}\,2^{-60}.
\]

The triangle inequality makes this a valid upper bound on ||P-U D||_2. The first
term is computed from an exact integer residual N/2^b. A q-by-q exact integer
Gram gives

\[
 \|N/2^b\|_2^2\le
 2^{-2b}\min\{\operatorname{tr}(N^TN),\max_i\sum_j|(N^TN)_{ij}|\}.
\]

This is an upper bound, not an exact computation of the largest eigenvalue.
512-bit interval arithmetic and outward dyadic rounding enclose the square
roots and phase approximation. The actual basis, proposal, parent receipts and
new reduction witness are hash-bound. The original estimator is not rerun or
modified in this return.

## 4. Transport through the actual shift and eigensolver outputs

With K=sqrt(b/a), beta=sqrt(1-q/(na)), the orthonormalized reference frame has
Q0_+=Q0_- J, ||J||<=K, sigma_min(Q0_-)>=beta and a diagonalizer condition<=K.
Let T be the actual captured shift and r_T>=||U_+-U_-T||_2. If d<beta, unitary
alignment and the triangle inequality give

\[
 \|O^*TO-J\|_2\le
 \Delta_T=(r_T+d(1+K))/(\beta-d).
\]

The actual returned eigenvalues lambda, an untrusted eigenvector witness V and
an inverse witness H obey validated bounds
rho>=||VH-I||_2<1, h>=||H||_2, r_lambda>=||TV-V diag(lambda)||_2.
Then V is invertible and A=V diag(lambda) V^-1 satisfies
||A-T||_2<=Delta_lambda=r_lambda h/(1-rho).
Consequently every returned eigenvalue lies within
R=K(Delta_T+Delta_lambda) of a reference unit-circle eigenvalue.
If 2R<s, disjoint disks and the reference-to-A homotopy give exactly one returned
eigenvalue in each disk, counting multiplicity.

Actual angle outputs and emitted dyadic phase numerators are checked with the
unchanged exact ties-to-even and validated complex-argument routines from PR186.
For R<1 the emitted phase error is at most asin(R)+epsilon_arg. The checker
retains the stricter sufficient gate 2(asin(R)+epsilon_arg)<s.
The basis/shift/eigenpair/inverse/argument residual computations and these
strict separation gates remain unchanged. Only the route to d changes.

## 5. Scope and limitations

This is an a posteriori certificate for actual saved floating outputs about a
fixed fitted reference. It may certify amplitude changes without treating their
full size as phase uncertainty. It does not remove the requirement that the
captured basis pass the direct frame residual; arbitrary amplitude changes,
loss of excitation, arbitrary noise patterns and optimizer convergence are not
certified. Reading a known reference is explicit here and is not independent
frequency discovery or physical-frequency truth.

No new raw-to-sketch projection, estimator execution, full-Hankel signature,
independent replay/review, acquisition/metrology qualification, hidden-state
recovery or CRL promotion is asserted. Parent exact sketches and their raw-source
custody remain separate obligations. All old HOLD receipts remain immutable;
a new sufficient proof does not retroactively change an old verdict. The
nominal 747-dimensional dynamical observer kernel is unchanged. O03 tolerances
remain protocol controls, never theory constants.
