# Fixed-sketch blindness and a bounded high-rank record

Development — no registry entry. Physical promotion 0. Constructor checks only;
independent review is not established. These are statements about the frozen
numeric-record pipeline, not the physical 747-dimensional unobservable subspace.

## 1. The declared compression map

Write D[k,37c+a]=Y[a,k,c], with 8191 time rows and 2294 preparation/channel
columns. The proposer uses Z=D W/64, where W is the fixed 2294×160 sign matrix
from seed 172026. An exact nonzero determinant of its first 160 rows proves
rank(W)=160, hence dim ker(W^T)=2134.

The supplied integer witness v has 250 nonzero entries, maximum absolute
coefficient 23 and squared Euclidean norm 16228. Every one of the 160 integer
entries of v^T W is exactly zero. All coordinates after index319 vanish.
The witness was found by LLL on rows [I_320 | 2^36 W_320]. The exact checker
needs only the witness, not trust in that search or an optimality claim.

For every temporal vector f and scale s,

    E = (s/2^48) f v^T  implies  (D+E)W/64 = DW/64.

This is exact mathematical equality. Floating evaluation of two differently
encoded records can differ by roundoff. In particular the complete numerical
proposer need not output byte-identical phases: it also fits coefficients
against the full D after discovery. Discovery alone cannot determine the
full record. No universal complete-record or residual certificate follows
from this fixed sketch without additional restrictions or verification.

## 2. Both additive gates are satisfied by the bounded family

Let s=floor(2^25/23)=1458888 and take an integer clock with |f_k|<=1.
The largest coordinate error numerator is33554424<2^25, and the maximum
62-vector squared error numerator is2145381030116352<2^56.
With encoding denominator2^48, every scalar obeys the sufficient2^-23
gate and every62-vector obeys the2^-20 gate. The latter norm is at most
1.646e-7. This establishes these two additive gates, not the complete
acquisition contract or its calibration, timing, disturbance or custody clauses.

## 3. Exact singular structure of the two noise clocks

Let B[c,a]=v[37c+a]. Exactly eight channel rows are nonzero. Its rank is8.
The leading principal minors of B_active B_active^T -4I are all positive;
they are stored in EXACT_BLIND_FAMILY_CERTIFICATE.json. Sylvester's criterion
therefore gives sigma_min_nonzero(B)>2. This uses exact integer determinants,
not a floating eigenvalue estimate. Its Frobenius norm is sqrt(16228).

Index the normalized Hankel by rows(i,c), columns(j,a), with0<=i,j<4096
and entries Y[a,i+j,c]/4096 in decoded model units.

For f_k=1 at k=4095 and zero elsewhere,

    H(E) = s/(4096*2^48) (J_4096 tensor B),

where J is the reversal permutation. Consequently rank H(E)=32768;
its positive singular values exceed ell=2s/(4096*2^48).

For f_k=(-1)^k, write u_i=(-1)^i. Then

    H(E) = s/2^48 ((u u^T/4096) tensor B).

Its rank is8 and its nonzero singular values are exactly s/2^48 times
those of B. Thus two clocks invisible to the same sketch give very different
Hankel ranks. For a fixed s, their Hankel Frobenius norms are respectively
s sqrt(16228)/(64*2^48) and s sqrt(16228)/2^48.

## 4. At least 30,875 nonzero singular values in the bounded impulse record

The pinned clean record's earlier record-only certificate supplies a real
rank-at-most1893 approximation A_r with ||H_clean-A_r||_F<=tau, where

    tau = 1434089336178995862 / 1267650600228229401496703205376
        < 1.132e-12.

This baseline certificate and its raw-record hash are inherited explicitly;
the new exact checker does not rerun that earlier spectral proof. It makes no
assertion that the clean quantized Hankel has exact rank1893.

The rank perturbation inequality gives

    sigma_(32768-1893)(H(E)+A_r) >= sigma_32768(H(E)) > ell.

Weyl's bound and ||H_clean-A_r||_2<=tau imply

    sigma_30875(H_clean+H(E)) > ell-tau > 1.399e-12 > 0.

All fractions and the positivity comparison are checked exactly. Therefore
the complete bounded impulse record has algebraic rank at least30875.
Its independently executed full-record signature check is a separate
calculation: rank at least30875 is compatible with only1893 singular values
above the much larger frozen selection threshold (about1.504e-5).
No increase in exact rank relative to the clean quantized record is asserted.

## 5. Scope of the oversized control

The third case uses s=floor(2^40/23) and the alternating clock. It remains
exactly invisible to the sketch, but deliberately violates both additive
error gates. Its role is to test whether full-record verification can refuse
a proposal that discovery did not reject. A HOLD is refusal to certify that
proposal; it does not by itself prove the true signature fails, identify a
failure mechanism, or expose the nominal observer's hidden747 dimensions.

The campaign is constructor-predeclared on a previously known synthetic
baseline. It is not independent preregistration, independent data or blinded
review. Universal phase-fitting convergence remains open.
