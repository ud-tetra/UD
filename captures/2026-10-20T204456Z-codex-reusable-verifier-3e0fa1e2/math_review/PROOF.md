# Generic projected-record verifier: independent mathematical review

Development — no registry entry. Same-team review; external promotion review PENDING. Physical Promotion = 0. This specification is frozen before testing the reusable implementation.

## Accepted-output mathematical contract

The supplied projected record defines a real matrix Z=N/2^bZ, where N is an m by n signed int64 matrix and bZ is an explicit nonnegative denominator exponent. The full saved singular list s1>=...>=sn>=0 is real binary64 interpreted exactly as dyadic rationals. Its saved right-transpose matrix is n by n. The cutoff tau and accuracy delta are explicit positive rational protocol controls, not theory constants. Default controls are tau=2^-24 and delta=2^-41.

Reject any exact proposal-cutoff equality. Set q to the number of proposals strictly above tau and require 1<=q<n<=m. Retained U chunks must collectively supply exactly m rows and q columns, with exact once-only declared row coverage. Retained V is the first q saved right columns, and Vd consists of the remaining d=n-q columns. S is the retained diagonal. Full shapes and finiteness must be checked before using the matrices. All loaded binary64 entries are exact real dyadics; no floating residual or SVD computation is needed.

Fresh actual operator-norm bounds must be established for

\[
\|U^TU-I\|\le a<1,\quad\|V^TV-I\|\le b<1,
\quad\|ZV-US\|\le f,\quad\|Z^TU-VS\|\le g,
\quad\|V_d^TV_d-I\|\le\eta<1,\quad\|ZV_d\|\le r.
\]

Small exact matrix witnesses can supply them. Gram defects use square-root enclosures of the sum of all squared defect entries. If a residual norm is obtained through its output Gram F^TF, its operator bound is a **fourth-root** enclosure of the sum of all squared Gram entries. A direct adjoint residual can use its Frobenius square root; an adjoint Gram route instead requires a fourth root. These alternatives must be fixed by the protocol before seeing outcomes. A scalar enclosure or PASS string alone does not prove the matrix product identity.

Since eta<1, Vd is injective and spans d=n-q input dimensions. Courant–Fischer gives

\[
\sigma_{q+1}(Z)\le t=\frac r{1-\eta}.
\]

No orthogonality between retained and discarded saved columns is required. No exact singular-subspace assumption is required.

Using separate polar orthonormalizations of U and V, define

\[
c=\frac{s_1[a/(2-a)+b/(2-b)]+f}{1-b},\qquad
e=\max\left(\frac f{1-b},\frac g{1-a}\right),\qquad
\epsilon=c+e.
\]

The compression C differs from S by at most c, and the two off-diagonal blocks jointly have norm at most e. If sq-c>t+e, the block-diagonal comparison has its q leading singular values exactly in C: Weyl bounds its (q+1)st singular value by t+e, while all q singular values of C exceed that threshold. Thus every j<=q satisfies |sigma_j(Z)-sj|<=epsilon. The denominator sq-epsilon is positive.

For j>q, both 0<=sigma_j(Z)<=t and 0<=sj<=s_(q+1), so their absolute difference is at most max(t,s_(q+1)). The full n-list bound is

\[
E=\max(\epsilon,t,s_{q+1}).
\]

An accepted numerical accuracy certificate must prove E<delta. The exact actual cutoff count additionally requires t<tau<sq-epsilon; check this separately, including for configurable controls. It is a cutoff count rather than algebraic rank. The leading-q ambient condition report is

\[
\kappa_q(Z)=\frac{\sigma_1(Z)}{\sigma_q(Z)}
\le\frac{s_1+\epsilon}{s_q-\epsilon}.
\]

It is not the condition down to sigma_n, and no historical1888 threshold should become a generic gate unless explicitly declared as a new protocol control.

This finite theorem requires no nominal/source singular bound, prior certificate, model, generator, estimator, character sector, phase target or source lower L. All six numerical norm premises should be computed freshly from the supplied projected record and saved factors. Projected-record lineage remains a separate provenance premise; it does not follow from these algebraic checks and is not a physical bridge.

## Program-level qualifications

Mathematical soundness of a genuinely accepted output is distinct from all-input backend success, exact implementation of every product, intake correctness, termination, resource guarantees and whole-program correctness. An independent matrix audit can validate witness products for particular runs. Finite positive/negative fixtures can falsify bugs and supply regression evidence but do not prove universal program soundness or completeness. This review will state separately which functions and actual fixtures were exercised.

Intake must bind explicit input bytes and reject invalid types, shapes, finite-value conditions, sortedness, exact cutoff ties, endpoint orders, invalid row coverage, bad identities, path escapes, symlinks, output overlap and overwrite attempts. Header/uncompressed resource limits should be checked before allocating arrays. N extrema need exact Python integer operations; abs on an int64 minimum can overflow. Pickle/object deserialization is forbidden. A hash binds bytes, not algebraic truth or provenance beyond the supplied record.

No prior scientific verdict, all-history guarantee, independent physical acquisition, SI/six-ratio result, exact shift spectrum, native1893/747 interpretation or physical promotion follows.
