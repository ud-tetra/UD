# Broader prospective preparation campaign: design review

Same-team mathematical/design review only. No new transform tables, raw
records, fits, or estimator outcomes were executed here. Physical promotion 0.

## Exact campaign domain

If the proposed six transforms are crossed with six noise recipes, freeze an
explicit 36-case table. If only six paired cases are intended, freeze that
table instead. Do not leave pairing or Cartesian-product interpretation implicit.
All fixtures remain deterministic same-constructor controls, not independent
population samples or physical preparation data.

Each transform creates its own fresh integer nominal. Eligibility is exactly
one signed quantum per 62-vector relative to THAT nominal, not old baseline
eligibility. Same-parity preparation mixing preserves the nominal per-class
rate/jitter family before rounding, with old origins absorbed into coefficients.
It does not guarantee fresh fixed-sketch excitation or conditioning, individual
preparation normalization, or the later measured-frame policy gates.

## Six concrete transform suggestions

For parity p=0,1 let Gp=(p,p+2,...) have size m=19 or18. Local list indices
are i=0,...,m-1. These recipes are suggestions to freeze, not executed matrices.

1. Signed reverse: output Gp[i] receives (-1)^(i+p) times input Gp[m-1-i].
2. Signed permutation A: PCG64 seed219237; permute even list, then odd list;
   output Gp[i] receives (-1)^(i+p) times the corresponding permuted input.
3. Signed permutation B: identical call/sign order with seed219238.
4. Offset rational pairs R1: roll each Gp list one position left, then pair
   adjacent list entries with [[3,-4],[4,3]]/5. Leave the last listed member of
   the odd-size group unchanged.
5. Two-pass exact product R1 R0, where R0 pairs ordinary Gp and R1 is recipe4.
6. Inverse two-pass exact product (R1 R0)^T.

Freeze literal numerator matrices, denominators, RNG versions/call order,
seeds, and names. Runtime versions should be pinned. Seeds may be replaced at
the design stage, but not after raw/fitting outcomes become known.

For recipes5/6 compose the exact integer numerator matrices first, over
denominator25; round the final transformed raw value ONCE. Sequential raw
rounding between passes defines a different experiment and a larger error term.

## Exact multi-pass error and range bounds

Let d0 bound old encoded scalar error relative to its declared modal waveform,
and let qraw=2^-48. One disjoint rotation pass has row L1<=7/5 and rational
rounding error<=2/5 quantum. Two exact-composed passes have row L1<=49/25,
denominator25, and one final rounding error<=12/25 quantum. Therefore

    d_nom <= (49/25)d0+(12/25)qraw

for the two-pass recipes. More generally use the actual final rational row L1
norm and nearest-rounding bound floor(d/2)/d for its denominator d. The source
vector bound after onehot noise remains

    62*d_nom^2+2*d_nom*qraw+qraw^2.

Signed permutations add no rounding. There are no half-ties for denominators5
or25; nearest-even can still be the declared general rule. Check exactly
|5*round(n/5)-n|<=2 or |25*round(n/25)-n|<=12, including negative numerators.

Before any int64 numerator dot product, bound every partial absolute sum by
max_abs_raw times the row numerator L1. A safe two-pass guard is
49*max_abs_raw<2^63; one-pass uses7*max_abs_raw<2^63. Use arbitrary integers if
that guard is not available. After final rounding and noise, verify raw range.
Before sketching require max_abs_fresh_raw*max_column_L1(A)<2^63. Before
binary64 conversion require every integer sketch numerator |N|<2^53, followed
by exact power-of-two scaling. A failed guard is HOLD, not silent clipping or
a switch of projection arithmetic after seeing outcomes.

## Six concrete onehot-noise suggestions

For preparation a=0,...,36 and time k=0,...,8190, define b_a=(7a+3) mod62.
Add s(a,k) at exactly channel c(a,k), zero elsewhere. All amplitudes are one
raw quantum. No floating trigonometry is required.

| Name | Channel | Sign |
| --- | --- | --- |
| stationary | b_a | (-1)^a |
| period2 | b_a | (-1)^(a+k) |
| period4 | b_a | [1,1,-1,-1][(k+a) mod4] |
| block1024 | b_a | (-1)^(a+floor(k/1024)) |
| prep_channel_cycle | (a+k) mod62 | (-1)^(a+floor(k/62)) |
| fixed_spatial_direction | (a*a+7a+11) mod62 | (-1)^floor(a/2) times [1,1,-1,-1][k mod4] |

The last pattern is fixed spatial direction, not a proven worst-case or
source-optimal direction. If a source-directed pattern is preferred, freeze
its literal channel/sign table and pinned old-source dependency before this
campaign's generation; label that source-engineered provenance explicitly.
prep_channel_cycle is a noise-index recipe, not evidence of a physical clock.

Period2/period4/block noise need not lie exactly in the nominal209-waveform
family. Source-family preservation is a nominal statement; subsequent frame
tests decide whether actual returned subspaces satisfy the fixed contract.

## Storage-limited chronology

The suggested sequential workflow is valid with these conditions:

1. Freeze all code, input hashes, exact transforms, noise recipes, complete case
   table, runtime, source constants, and existing caps before first generation.
2. Generate each case, hash its nominal/raw bytes, check every noise difference,
   source/range bounds and counts, then retain its complete first-pass receipt.
3. Remove only verified regenerable scratch raw files. Do not delete pinned
   source data, published captures, diagnostic receipts, irreplaceable failed
   evidence, or saved estimator witnesses. A verified regenerable raw file may
   be released even for a later estimator HOLD; its rejection and witnesses
   remain. This is a storage policy, not removal of rejected runs.
4. Freeze the entire ordered dataset ledger with every first-pass raw/nominal
   hash before ANY estimator fit. Preserve failures and duplicates explicitly.
5. Regenerate one case at a time and compare against its already frozen hashes,
   counts and recipe. A mismatch is HOLD/stop for that case, not an excuse to
   replace the expected hash or tune a seed. Only fit a matching case.
6. Bind each run to that regenerated raw hash and frozen recipe. Retain all
   learned-order changes, numerical exceptions and measured-cap HOLDs. No retry,
   fallback, forced209, new sketch, or post-outcome cap update.
7. Delete a regenerated raw scratch file only after its final hash check and
   custody receipt. Keep numeric witnesses and exact certificates. Full replay
   regenerates bytes again without pretending raw acquisition is bundled.

The old PR224 Gram, normal, strict frame and shift caps remain exact inherited
fractions. They are not re-estimated from this larger campaign. The old finite
normal maximum supplies a prospective test cap, not a prediction of future
numerical behavior. Local prospective freezing is not independent/blinded
registration. Finite success rates are descriptive for these36 fixtures only.

The measured-frame theorem is not a new full-factor SVD proof, exact-order
count, phase certificate, all-gates admission, full-Hankel result, or physical
promotion. External review remains pending.
