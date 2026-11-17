# C06 asynchronous sector latches v0.12

**Status.** EXACT / CONDITIONAL for the specified switched conservative exchange. CANDIDATE (agile) for native sensing, isolation and event handoff. Physical Promotion = 0.

**Sources.** [UD #532](https://github.com/ud-tetra/UD/pull/532) gives the two-stage norm-preserving records, [UD #536](https://github.com/ud-tetra/UD/pull/536) the signed stock-balance guard, [UD #537](https://github.com/ud-tetra/UD/pull/537) the port sectors and [UD #539](https://github.com/ud-tetra/UD/pull/539) / [Discovery #415](https://github.com/ud-tetra/UD-Physics/pull/415) the unweighted-action rates. In v0.11, irrationality follows because the prime valuations of 6/53 are not all even. The obstruction concerns a simultaneous half phase under a running constant-rate generator.

## Declared switched interaction

Let X=E⊕T2 be the mean-zero ordinary edge-current space with its Euclidean metric. Let F be the v0.11 flag-copy port with the unweighted action metric on records. On X, F*F=ω_E²P_E+ω_T2²P_T2 with both rates positive. The two record ranges F(E), F(T2) are orthogonal. Each is identified isometrically with its source sector by F/ω_k. Any orthogonal record complement has zero initial amplitude and is uncoupled. Start with source x0 and all records zero. Time is dimensionless, all ports are closed, and the only continuous dynamics are the declared skew exchanges.

For each sector with initial stock C_k>0, let its normalized balance be B_k=(||y_k||²−||x_k||²)/C_k. Run its source/record exchange at ω_k until the first upward zero of B_k. Set a persistent completion bit and disable **both** directions of that sector's coupling, using identity on the amplitude state at the switch. A sector with exactly zero initial stock starts complete with zero amplitudes. Stage two is enabled when both bits are complete. The bits here are new event memory. This protocol does not identify them with the native matching parity bits.

## Exact retention and handoff

Each active block has x_k=cos(ω_k t)x_{0,k} and y_k=(F/ω_k)sin(ω_k t)x_{0,k} until its first stop. That stop occurs at t_k=π/(4ω_k) and B'_k=2ω_k. The zeroed generator leaves both amplitudes fixed, so the faster sector retains its half record and half residual throughout the wait for the other. Orthogonality prevents the still-running block from altering the held one. Each block conserves its metric stock, the amplitude does not jump, and the hold has zero stock flux. No simultaneous crossing or shared phase is needed. The protocol still requires sector-resolved sensing, persistent completion states, isolation, and a joint readiness event.

For the unweighted unit cell, t_E=π√3/8 and t_T2=3π/(4√106); the latter is earlier. At the readiness event, the direct record has squared gain 1/2 on both sectors. A subsequent complete matching swap of the retained E amplitude gives record gains (1,1/2). With the v0.6 Frobenius-to-edge factors (1/2,1), the final readout is (1/2)I_W. Including the retained source gives unit edge-stock gain on both sectors, by conservation. The result is conditional on full Stage 2 transfer. The first-stage test supplies neither the execution of that swap nor a physical clock.

If the first completion bit is set but the exchange keeps running, the faster sector cannot still have exact half stock at the slower sector's first half time for the v0.11 irrational ratio. A completion receipt alone therefore cannot substitute for isolation or a retained record.

## Error budget and source gate

Assume the v0.8 bracket and derivative conditions hold sector by sector. A measured normalized balance error bounded by ε_k then gives |f_k−1/2|≤ε_k/2 at each detection. Under exact hold, this bound survives the waiting interval. If Stage 2 transfers a fraction η of the retained even stock, the final shear weights are

```math
w_E=\frac{1-(1-f_E)(1-\eta)}{2},\qquad w_{T_2}=f_{T_2}.
```

Consequently |w_E−w_T2|≤ ε_T2/2 + (1/2+ε_E/2)(1−η)/2. For a complete swap, the error in f_E cancels from the final shear weight. These are conditional bookkeeping bounds, not a result for leaky holds or misidentified zero-stock sectors.

No constitutive rule has yet been sourced for sector-resolved readout, opening the hold, or coordination of the two completion bits. Pure continuous unweighted exchange remains a negative comparator. Deficit allocation is separate. No empirical data enter; the desired half split was known.

## Replay

The exact replay checks both event orders, simultaneous and absent-sector controls, conservative rational stock accounts and the error envelope. First-phase times and transversality follow from the analytic solutions above, and are not numerically rounded.
