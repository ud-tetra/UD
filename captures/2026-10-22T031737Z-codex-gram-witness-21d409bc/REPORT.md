# Robust finite-mode leakage witness v0.1

21 October2026 America/Chicago. PASS_EXACT_CONDITIONAL_GRAM_WITNESS. Constructor checked; independent review pending. Development —no registry entry. Physical promotion0; EXIT-03 HOLD.

## Result

The finite-mode leakage witness now tolerates explicitly bounded frequency and duration error. A Gram lower bound replaces exact orthogonality. For100 nominal modes100–199Hz, per-mode frequency errors<=5mHz and relative monitor-duration error<=10ppb, exact rational row sums certify a Gram eigenvalue lower bound approximately0.9098874884, exceeding9/10.

| Proposed source/monitor requirement | Conditional result |
|---|---|
|1second nominal monitor; constant modes within±5mHz; duration within10ppb | Gram lower bound>0.9098 |
| Measured finite-mode complex RMS<=55microvolts | New prospective requirement |
| Total waveform monitor L2 error<=20microvolts | Includes outside-model contamination and clock normalization |
| Independent outside-model spectral TV<=200microvolts | Still an external premise |
| Tail spectral TV | <=793/800000V=0.00099125V |
| Full-state quadrature error with prior input budget | <0.008667V |
| Phase error at admitted amplitudes | <0.017509rad |

The10ppb interval bound belongs to the independent one-second monitor. It is distinct from the0.2ns acquisition time-error requirement and the50ps drift share over the shorter acquisition record. No observed clock capability is claimed.

## Theorem and proof

THEOREM.md derives T_tail<=sqrt(K/lambda_min(G))*(r_meas+epsilon_mon)+T_out. Each uncertain off-diagonal Gram entry is bounded by q/(d-q), where d is an integer nominal gap and q=d*rho+2*eta*T0*(1+rho). The maximum exact rational row sum gives the lower eigenvalue bound. No frequency grid, floating eigenvalue or unproved exact orthogonality is used for acceptance.

A common frequency shift cancels from Gram pair differences, although physical source-band membership still requires separate evidence. Frequency drift/nonstationarity or nonlinear clock warping is outside the constant-mode model. A monitor-error bound must cover any such residual it claims to absorb.

## Controls and limitations

The verifier checks nominal orthogonality, rejection of the old60microvolt RMS share under the robust sufficient budget, selected-gate failure at50mHz mode uncertainty, possible collision at500mHz, and excess300microvolt outside-model variation. Near-colliding distinct tones provide a true counterexample: two opposite1V coefficients can have RMS below10microvolts while their spectral TV remains2V. This exposes why a separation/coercivity condition is necessary.

Two optional100-by-100 floating Gram eigenvalue diagnostics exercise alternating and ramp frequency-offset patterns. They are synthetic diagnostics only and do not establish the continuum uncertainty bound; exact rational inequalities do that. NUMERICAL_DIAGNOSTICS.json records the actual outcomes or explicitly reports unavailable NumPy.

The new monitor error is a waveform L2 bound. A previously independently certified coefficient-vector bound remains a different valid route; the two must not be conflated. Projected outside-mode contamination remains part of the20microvolt total error requirement; source/model completeness and isolation are still unverified. The witness remains conditional, unexecuted and not an admitted calibration record.

## Reproduce and next

Run `python3 certify.py` with standard Python for exact acceptance; NumPy is optional for diagnostics. The script binds the frozen contract and inherited full-state certificate by hash, evaluates all rational row bounds and negative gates, and propagates the tail ceiling into the prior full-state budget. No imported archive or external source code executes; no raw experimental data are used.

Next replace the continuous-time Gram premise with a sampled-monitor witness that accounts for actual sample times, quadrature calibration and finite numerical reconstruction error. That step must preserve the outside-model/source restrictions and avoid using the candidate estimator as its own independent reference. Full energy, native support, primitive clock, action anchor and EXIT-03 remain open. Gap2_FINAL_Finite_Genesis.png is unavailable and unused.

A. CURRENT MISSION TRAJECTORY — Make leakage evidence robust to realistic measurement uncertainty.

B. WHAT WAS DONE — Gram/coercivity theorem, exact uncertain-frequency certificate and near-collision counterexample.

C. FINDING — The proposed tightened witness passes conditionally; small RMS alone cannot certify spectral variation.

D. UD GAP IMPACT — Source/monitor requirements sharpened; no new empirical evidence or physical promotion.
