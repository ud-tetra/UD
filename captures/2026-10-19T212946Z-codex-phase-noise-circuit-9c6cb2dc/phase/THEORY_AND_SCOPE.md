# New preparation points, fixed phase-focused directions, no execution

Development; external review PENDING; Physical Promotion=0. This packet is
prospective for future records ONLY. All older directional frame, saved-phase
and exact-T outcomes are known. This is post-known design, not a blinded or
external registry, and same-team review does not supply external promotion.

## Exact new preparations inside the existing family

Let D=2^44+1, a=2^44-1 and b=2^23. Each paired same-parity preparation block
is R=[[a,-b],[b,a]]/D, with an unpaired coordinate unchanged. Since
a^2+b^2=D^2, R is exactly orthogonal. Moreover

||R-I||2^2=((a-D)^2+b^2)/D^2=4/D < 2^-42 < 2^-40.

Disjoint blocks have the same maximum norm. Right multiplication by the
existing exact orthogonal reference preparation preserves that operator norm.
The two new points use pairing offset0 at reverse_stationary and offset1 at
shuffle_cycle, preserving preparation parity. Their operator distance to the
respective existing PR233 anchors is at most2^-21<rho=2^-20. Existing family
anchors are not redefined. These are genuinely new exact preparation points:
their nonzero small off-diagonal entries have reduced denominator D>25,
whereas all six previous anchor matrices had denominators1,5 or25.

Only37x37 preparation METADATA is constructed this turn. No baseline raw
coordinates, temporal carrier/profile tables or state records are generated.
The metadata check proves orthogonality and parity, not an actual future
floating rank/order or phase result.

## Exactly one nominal rounding and separate encoded noise

With original pinned quantized synthetic baseline Y0, the future new nominal
is Ynew=round_nearest_even(Y0*Tnew^T) on the h=2^-48 raw grid. Products and sums
use Python arbitrary-precision integers BEFORE division; int64 multiplication
would overflow and is forbidden. The per-coordinate nominal rounding error is
at most h/2 (indeed slightly smaller for odd D). Signed ties-even is specified
exactly using floor quotient/remainder; no floating conversion is used.

Future recorded input is Ynew+E. E is an integer-grid perturbation relative
to THIS rounded new nominal, not the inherited rounded anchor. Every62-vector
has at most one nonzero integer, of magnitude<=1127. Hence ||E||2<=1127h per
vector. The old PR233 family proof already accounts for baseline error,
orthogonal preparation change and one new h/2 nominal rounding; that rounding
is not charged again as E. The global Frobenius transform is orthogonal before
rounding, but no per-preparation norm/physical-energy conservation is assumed.
Any old-anchor-relative raw difference has additional preparation and rounding
terms and is NOT claimed to lie in a one-quantum or1127-quantum old-anchor ball.

## Four future cases and phase relevance

The fixed cases are A0, A_ramped_low, B0 and B_chirped_high in the exact order
stored in CONTRACT.json. A0/B0 are matched new-preparation zero-noise controls.
They do not reuse existing recorded controls. The two noise cases have bound
1127h, with no amplitude search or replacement.

A uses the fixed prior weak-mode spatial channels/signs, but a genuinely new
temporal direction: round_even(1127*(k-4095)/4095) times sign(sin(omega_low*k)).
B uses new SHA-derived spatial channels/signs and sign(cos(omega_high*k+
k/8191+(k/8191)^2)) at constant magnitude1127. The carrier omega values are
the fixed source labels j0:rate1:sign1 and j51:rate-1:sign1, not values selected
from new records. These are targeted clock-frequency/ramped/chirped directions,
not assumptions that a particular phase error or failure must occur. A sign
carrier includes harmonics; it is not an exact pure sinusoidal perturbation.

All arguments are exact rationals. Future trig sign evaluation uses fixed
512-bit directed intervals, positive/negative only when certified; sin(0) has
the declared sign+1. No floating sign, epsilon or precision escalation is
allowed. Unresolved sign, overflow or other data-eligibility failure causes a
GLOBAL_DATA_HOLD before any fitting. No carrier table is evaluated this turn.

## Phase and frame verdicts remain separately typed

The209 source targets, per-TWO-step interpretation and numerical-quality caps
are unchanged from PR244. The fixed matching threshold is HALF the source
minimum chord lower bound: a conservative identity/bijection radius because
chord distance is no larger than shortest angular distance. It is NOT a
calibration2^-39 accuracy guarantee, an observed-error-derived tolerance, a
uniform noise-ball accuracy claim, SI identification or removal of modulo-pi
primitive-clock ambiguity. Achieved finite error bounds will be reported
separately without tightening targets/caps after outcomes.

The old strict source-frame/Gram/normal lane is checked independently. A frame
refusal never implies phase failure, and finite accurate phases never rewrite
that refusal or the prior necessary noise-ball exclusion. The optional PR244
exact-T extension uses its unchanged diagonal-normal similarity/disjoint-disk,
origin exclusion and half-source-angle predicates on newly saved witnesses.
No verification-stage eigenvalue/inverse/alignment solver is introduced.
