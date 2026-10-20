# Evidence content, units and review sequence

Development — no registry entry. Physical Promotion = 0. These are source-conditional review requirements, not verified metrology or laboratory design.

## Keep the three interfaces separate

| Lane | Current mathematical/data object | What this packet does not infer |
|---|---|---|
| Synthetic temporal/sketch | Original encoded synthetic 37-preparation,62-channel nominal; projected 209 temporal modes, internal quantum q=2^-48 and two-step phases | No volts, seconds, physical clock, six-ratio calibration or apparatus tolerance follows from this quantum or phase theorem |
| Native history observer | Separate 62 history channels×37 preparations, inherited 1893 observable/747 unobservable dimensions; 189 diagnostic outputs are different readouts | No padding of 10-channel data, recovery of the hidden kernel or automatic observer/state map |
| Published circuit component | Source-specific 10-channel recording lane, including filename-defined empty channel; known 05-21 and 05-28 exposure | Nominal V/Hz labels and author equations do not establish calibrated physical UD correspondence |

The 128-path crosswalk belongs to the original published ten-channel request. A new source, native observer or physical realization needs its own exact identity, channel/state/readout/unit map and justified domain. Equal numbers or terminology do not identify these objects. Physical realization and source/action/measurement assumptions must be independently tested before a UD bridge.

## Conditional error propagation to request

Use only independently supported bounds covering the actual acquisition/domain. Let a channel's applied-transform error terms be gain error d_g, nominal-input bound Y, offset error d_b, post-decoder nonlinearity/noise term n and quantization/serialization term q_ser. Then

    a_c = d_g*Y + d_b + n + q_ser

is a conservative per-sample amplitude allowance in volts if each premise is valid. q_ser is not the synthetic model quantum q=2^-48. Different physical error components add by the triangle inequality unless a separately justified stronger result applies. Missing terms remain unknown.

For nominal timestamps t_n=t0+n/f0, suppose actual times satisfy

    t_actual,c,n = t0 + delta_origin + delta_skew,c + n/[f0*(1+e_c)] + j_c,n,
    |delta_origin|<=o, |delta_skew,c|<=s, |j_c,n|<=j, |e_c|<=rho<1.

With origin defined at the actual cropped start and independently supported derivative bound |dv_c/dt|<=L_c on the entire enlarged time domain,

    tau_N = o+s+j + (N-1)*rho/[f0*(1-rho)],
    epsilon_time,c <= sqrt(N)*L_c*tau_N.

If origin is instead defined at a trigger, include the actual crop offset in the drift index or debit it in origin. For a proved finite multitone domain, L_c<=2*pi*sum(A_k*F_k) is a possible bound; a finite FFT peak or nominal Nyquist label does not prove that domain. The conditional rate allocation rho<=b*f0/[(N-1)+b*f0] requires b=eta_time/[sqrt(N)*L_c]-(o+s+j)>0 and L_c>0. No numerical o,s,j,rho,L_c,eta_time,N or accepted f0 is supplied for a new acquisition here; N=1 is handled directly by the time formula. Special zero-derivative cases must not be forced through division by L_c.

A per-trace vector allowance is, conservatively,

    epsilon_c <= sqrt(N)*a_c + epsilon_time,c + epsilon_inband,c + epsilon_alias,c.

These terms must cover the same coordinate grid and simultaneous event, without duplication. For disjoint record/channel coordinate blocks, a stacked Euclidean budget can use sqrt(sum(epsilon_block^2)); that is geometry, not stochastic independence. Within each block, component-error allocations still add as justified. A global max-absolute budget has its own declared allocation. The old per-vector budget is not automatically a stacked-score or fresh-source budget.

Validated computational debits remain separate. Under the source's declared DC/RMS operator, each corresponding data-error allowance is at most epsilon_c/sqrt(N), plus its proven computational debit. For the source's one-sided spectral-amplitude convention and declared nonzero window,

    L_w=sqrt(2/sum(w_n^2))*max|w_n|,
    amplitude_error <= L_w*epsilon_c + eta_computation.

A strict amplitude margin greater than twice that allowance suffices for a unique selected discrete bin under the declared operator. Otherwise HOLD. This does not give sub-bin frequency confidence. Centroids require a positive denominator bound; calibrated frequency axes require valid clock/grid and anti-alias evidence. FFT/bin/normalization/rounding and stored-versus-analytic window terms need their own proof.

For a declared norm p score, if measurement-vector error is bounded by epsilon_obs,p and prediction/readout/initial-state/numerical allowance by epsilon_pred,m,p in the same coordinates, a conservative score interval is

    [ max(0, observed_score_m,p - b_m,p), observed_score_m,p + b_m,p ],
    b_m,p = epsilon_obs,p + epsilon_pred,m,p.

Keep model discrepancy, state-estimation, solver and acquisition terms distinct and do not spend one component twice. The frozen selection rule requires both declared aggregate L2 and global max score intervals to separate in the same direction beyond the independently justified predeclared margin. Overlap or failed enclosures mean HOLD. This is a sufficient conditional comparison rule, not causal identification or a new margin value. No numeric target is obtained by backsolving a native phase/six-ratio gate.

## Ordered independent review and return

1. Declare the physical question, source/analysis lane, realization and state/action/readout/unit maps. Record every open bridge assumption.
2. Establish actual source custody, domain and all exposure/selection/parameter dependencies through an independent review. 05-28 remains retrospective in the current lineage; calibration received later cannot erase exposure.
3. Obtain acquisition-specific calibration, timing/transfer, joint-domain and validated-computation evidence. Planning assumptions are not acceptance of the subsequently acquired domain; retain a rule to HOLD any sample outside coverage.
4. Before new fits or relevant outcome access, freeze the justified physical model/comparator, preparation and drive/loss assumptions, solver/error/failure rules, selection, scores and margin rationale. Calibration-only data and training data must be distinguished from scored holdouts.
5. Nonconstructor content review inspects the premises; an actual custodian records a separate ruling under governance. The requested 14 artifacts and a completed receipt do not grant approval themselves.
6. Data release/acquisition requires separately established authorization and accepted scope. This packet triggers neither. On later authorized analysis, execute the frozen rule and retain every failure/HOLD without outcome-selected repair.
7. External review returns the attributable commands, logs, discrepancies and verdict. Independent replication and physical identification remain separate governance rungs; no rung is advanced here.

Hash checking is custody only. Correct arithmetic conditional on fabricated bounds is not calibration. A complete JSON form is not a reviewed scientific premise, and an author-reported analysis uncertainty is not automatically a simultaneous source-bound enclosure.
