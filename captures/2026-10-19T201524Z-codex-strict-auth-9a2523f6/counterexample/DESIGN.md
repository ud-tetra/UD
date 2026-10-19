# One encoded family member and minimal-frame obstruction

Same-team mathematical investigation; external review PENDING; Physical Promotion=0.

The target is an actual floating-output counterexample to universal admission by
the unchanged PR224 strict source-frame gate. It is not a phase-error
counterexample, a claim that ideal leading singular vectors fail, or a universal
no-go theorem for different algorithms. A noncounterexample or numerical HOLD is
retained without retry, replacement or retuning.

Choose exactly the PR233 `reverse_stationary` same-parity signed-permutation
anchor T. Its distance to the family anchor is zero. Compute the spatial table
once from its saved weakest retained right singular vector v209: binary64
w=(Aint/128)v209; for each preparation a choose the smallest channel c maximizing
abs(w[37c+a]), with sign +1 for a nonnegative selected coefficient and -1
otherwise. For every time k put exactly one encoded perturbation
1127*2^-48*sign[a]*(-1)^k into that preparation's chosen channel.

Every preparation/time 62-vector has exact noise norm1127*2^-48. Thus this
record is inside the existing PR233 family, not the original one-quantum ball.
All18,790,154 scalar differences,303,067 integer squared vector norms, raw SHA,
and exact anchor nominal SHA are checked and frozen before ONE call to the
byte-identical existing integer-projection/SVD/learned-cutoff/lag2-LS/eig/angle
estimator. The learned order is not forced.

Storage is an anonymous RAM-backed Linux memfd, same-process raw hashing and
np.memmap access via /proc/self/fd. No persistent raw record is required: its
complete bytes are reproducible from the pinned nominal baseline and frozen
spatial table. Saved numerical factors are retained losslessly. A full exact
integer projection is independently recomputed after the fit and its hashes
compared. The original frozen estimator's code hash remains unchanged.

For a learned209-column returned basis U1 and pinned reference U0, let a finite
dyadic auxiliary X be proposed and frozen before exact verification. Set
R=U1-U0X, G=U0^T U0, N=U0^T R. If a validated ell>0 satisfies G>=ell I,

min_Y ||U1-U0Y||F^2 = ||R||F^2-tr(N^T G^-1 N)
                      >= ||R||F^2-||N||F^2/ell.

All residuals are exact rational functions of the saved binary64 arrays, and
ell can be a dyadic lower bound1-eta0 using the exact Frobenius Gram defect.
If this exact lower bound is strictly larger than the unchanged squared raw
frame cap, no alternate auxiliary alignment can repair admission for THIS
returned basis. This is stronger than merely observing one proposed-X gate
refusal. Actual Gram/normal/cutoff checks have their own scopes and cannot be
inferred from an auxiliary-X value. No ideal-SVD conclusion follows without a
separate numerical subspace bridge.

Prior one-quantum source outputs and the wide-family analytical enclosure were
known when this targeted source-selected design was chosen. The new amplified
record and new numerical output were not known. This is an openly targeted
adversarial investigation, not a blinded or externally independent experiment.
