# Uniform floating evaluator certificate for the fixed-P2 J1 port

DERIVED / EXACT CONDITIONAL on the declared IEEE binary64 operation model. Constructor checked; independent review OPEN. Development — no registry entry. Physical promotion=0. Refs #218 and #136. Extends PR253; prior captures remain unchanged.

## Result and scope

The saved P2 state now has a frozen scalar floating evaluator whose combined continuum-plus-evaluation bound passes the absolute 1/10 target for every accepted binary64 frequency in

    [8983/2000, 9017/2000] = [4.4915, 4.5085],  gamma=1/10.

The uniform radius is less than 0.099117. Floating evaluation contributes at most 7.318e-16. The interval is 70% wider than the earlier exact-model interval [4.495,4.505]. No new state solve, mesh refinement or flux optimization is required. The underlying scalar-wave action, source, metric and damping remain externally declared. Frequency is dimensionless under ct/a.

This is a new compact evaluator for the same exact corrected-output family, not the previous sparse-matrix output pipeline. Its newly rounded constants change the omega=4.5 reported center by at most 3.753605e-14 relative to that previous pipeline. This change is explicit; the old pointwise evidence remains valid for its original center.

The guarantee is conditional on binary64 round-to-nearest, ties-to-even for each explicit +, -, * operation, without contraction/FMA and with unchanged frozen coefficients. The native program and runtime controls match this model; they do not formally verify every compiler, platform or altered floating environment. Input frequency means its exact represented binary64 value. Decimal parsing, measurement uncertainty and physical Hertz calibration are outside the input contract.

## Frozen evaluator

Let v be the exact saved meanfree P2 state from PR251. Its corrected estimator family is

    J_w(v)=J_w0(v)-(z(w)-z(w0))*M,
    M=integral v^2 dmu,  z(w)=-w^2+2i gamma w,  w0=9/2.

J_w0 and M are reconstructed as exact rationals from the PR253 output record. Six constants are rounded once and frozen by actual binary64 hex words in EVALUATOR_WITNESS.json. Every constant's exact quantization error is included in the proof.

The native implementation uses twelve scalar operations:

    dw = w - w0
    sw = w + w0
    s  = dw * sw
    t  = TWO_GAMMA * dw
    pr = s * M_R
    qr = t * M_I
    cr = pr + qr
    real = J_R + cr
    pi = s * M_I
    qi = t * M_R
    ci = pi - qi
    imag = J_I + ci

The true arithmetic expansion equals J_w0-(z-z0)M exactly; the audit also checks this closed expression independently of the operation DAG on every runtime control input. Factoring w^2-w0^2 into (w-w0)(w+w0) avoids subtracting two nearby rounded squares. The AST is checked against the declared twelve-operation DAG so the error propagation covers the actual stored native sequence. The final complex constructor only packages the two scalar results.

The evaluator rejects nonfinite frequencies, non-native-float arguments and represented frequencies outside the rational interval. It does not silently round the interval endpoints outward or infer a physical frequency from the stored number.

## Uniform floating error proof

For any finite exact operation result x, binary64 spacing gives

    |RN(x)-x| <= u |x| + eta,
    u=2^-53,  eta=2^-1075.

For normal x, the half-spacing in its binade is at most u|x|. Subnormal rounding has half-spacing eta. All propagated exact-operation magnitudes plus input errors are below 16, excluding overflow. The additive eta is retained even though this evaluator operates far above subnormal scales.

For each node, propagate an exact ideal interval [l,h] and an absolute error upper E relative to that ideal expression. Let A and B bound the magnitudes of the two ideal operands. Before rounding,

    E_pre <= E_a+E_b                          for addition/subtraction,
    E_pre <= A E_b+B E_a+E_a E_b              for multiplication.

If C bounds the ideal result magnitude, then

    E_out <= E_pre+u(C+E_pre)+eta.

Only these bookkeeping bounds are rounded upward to the rational grid 2^-120; the native evaluator still performs binary64 operations. Each upward inequality is checked with exact fractions. Constant nodes start with their actual quantization errors; represented input w has zero input-representation error under the declared contract. The output complex error is at most sqrt(E_real^2+E_imag^2), rounded outward by an integer square-root construction.

This is a uniform analytic propagation, not an inference from sampled errors. The accepted interval contains exactly 19,140,298,416,325 binary64 inputs. Its binade spacing is 2^-50; the first/last accepted bit patterns and their immediately excluded neighbors are checked exactly.

## Continuum bound and enlarged band

The pointwise PR253 flux provides residual dual upper

    r0 <= sqrt(d^2)+sqrt(nu^2).

For the same state at nearby frequency,

    ||r_z|| <= r0 + (1/2)|z-z0| ||v||_L2.

For |w-w0|<=rho and fixed gamma=1/10,

    |z-z0|^2 <= [rho(2w0+rho)]^2+(2 gamma rho)^2,
    kappa <= sqrt(1+[(w0+rho)/(2 gamma)]^2).

The exact-model continuum radius is this kappa times the squared residual upper. Add the uniform complex evaluation error for the actual native output. This proves the declared target throughout each interval below, under the IEEE operation model. No interpolation of frequency samples is used.

Table decimals are approximations; FLOATING_BAND_RESULTS.json stores exact outward rational bounds.

| Frequency interval, gamma=0.1 | Uniform floating evaluation error | Combined continuum radius | 0.1 target |
| --- | ---: | ---: | --- |
| 4.499–4.501 | 6.70058e-16 | 0.018706507443 | PASS |
| 4.498–4.502 | 6.78278e-16 | 0.025753335951 | PASS |
| 4.495–4.505 | 7.02960e-16 | 0.053667145018 | PASS |
| 4.492–4.508 | 7.27674e-16 | 0.091772384456 | PASS |
| 4.4915–4.5085 | 7.31796e-16 | 0.099116932946 | PASS |

The parent exact-model bound on [4.49,4.51] exceeds 0.1. That is an unresolved upper-bound gap, not evidence that the actual error exceeds 0.1. The present evaluator explicitly rejects inputs outside [4.4915,4.5085]. No maximality, full-band guarantee or finite mesh-termination claim is made.

## Native trace/oracle controls

A separate integer/rational implementation supplies binary64 round-to-nearest, ties-to-even: find the binade exponent from integer bit lengths, divide by the exact binary64 quantum, round the integer quotient by its remainder and parity, then assemble the final bits. It does not call the native +, -, * operation being checked to compute its rounded answer.

1663 input traces cover the exact inside boundary words and their neighbors, omega=4.5 and adjacent words, an evenly spaced bit-index grid and a fixed-seed integer-generated sample. All 19,956 native intermediate words match the software oracle. Each observed error is also checked against its corresponding uniform node bound. The maximum observed complex evaluation error is at most 5.817921e-16. It is a diagnostic, not the uniform error certificate.

Six separate oracle controls check ordinary ties, odd/even significands, subnormal ties, the normal/subnormal boundary and negative values. Input controls reject below/above interval neighbors, NaN, infinities and integer/string arguments. A one-ULP output corruption differs from the frozen oracle; a zero constant-quantization budget is rejected because the center's stored output differs from the exact source J0. Constructor checks are not non-constructor review.

## Reproduction and provenance

Run `python3 captures/2026-10-19T231026Z-codex-j1-floating-band-2bbebc9d/replay.py` from the repository root. Standard-library exact arithmetic verifies frozen source hashes and the parent manifest bindings, reconstructs constants, checks the native AST, derives every uniform bound, audits native/oracle traces and compares FLOATING_BAND_RESULTS.json. The parent flux solve is not rerun here; its exact replay record and source bounds are hash-bound dependencies.

FLOATING_BAND_RESULTS.json is the final replay target. INITIAL_FLOATING_BAND_RESULTS.json preserves the initial record before two additional controls were added; the mathematical bounds did not change. EVALUATOR_WITNESS.json identifies the actual constants, evaluator.py is the frozen native function, and rounding.py is the software oracle. REPLAY.log records the completed comparison. Repository integrity separately checks the SHA-256 inventory and append-only event coverage.

The supplied coefficient ledger does not derive this benchmark's scalar-wave action or physical source/damping/metric bridge. The CRL2 governance amendment remains a proposal, not enacted by citation. Gap2_FINAL_Finite_Genesis.png was unavailable and was not read or used.

Independent review, the full [0,6] x [0.1,1] frequency/damping audit, finite mesh termination and native UD correspondence remain OPEN. Next: derive a validated neighboring-state or parameter-dependent estimator and extend coverage with explicit per-cell certificates. Development — no registry entry; physical promotion=0. No horn/material, GR/QFT or empirical identification follows.
