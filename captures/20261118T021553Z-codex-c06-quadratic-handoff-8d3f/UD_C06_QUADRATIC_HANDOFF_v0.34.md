# C06 quadratic capture and separate handoff v0.34

**EXACT / CONDITIONAL** for the aligned odd model and the stated resets. **CANDIDATE** for archive and fresh-epoch wiring. **OPEN** for native capture authority, stage-2 semantics and a sourced archive/donor mechanism. **Physical Promotion = 0.**

## Guard and scope correction

Use the three-dimensional odd Hilbert space \(W=T_2\) and aligned carrier and record \(u,v\in W\). Let \(N=\|u\|^2+\|v\|^2>0\), \(B=\|v\|^2-\|u\|^2\). For the incoming common-rate flow \(\dot u=-\omega_-v,\ \dot v=\omega_-u\), \(\dot B=4\omega_-\langle u,v\rangle\). An armed epoch starts with \(u=s\ne0,\ v=0\). At the first upward root, \(u=v=a=s/\sqrt2\) and \(\dot B_{\rm in}=2\omega_-N\). The declared capture transaction reads the incoming guard, records the epoch and selects the full live cut \(G(I-P_-)\) with the reciprocal adjoint and identity amplitude reset. Given the v0.20 orthogonal record ranges, odd stock stays on both sides at \(N/2\), even exchange continues and publication cannot change selection.

The v0.33 no-go covers the tested fixed scalar linear observation. It leaves other multi-observation or nonlinear constructions open. For the complete active port the delay overshoot is strict for \(0<\delta<\pi/(2\omega_-)\), with isolated later returns to half stock. The source detector rearms on the expected outgoing nonzero side. A terminal hold has neither that side nor a positive outgoing slope.

## Identity-reset rearm fails on the same stock

If the old epoch stores \(u=v=a\ne0\), rearming its detector with the cut maintained leaves \(B=\dot B=0\), so it cannot produce a new directed crossing. Restoring the original rate with identity reset gives \(\dot B(0^+)=4\omega_-\|a\|^2>0\) immediately and \(f(\tau)=\tfrac12+\tfrac12\sin(2\omega_-\tau)\), with \(f=\|v\|^2/N\). The same-stock restart therefore loses the exact hold for every sufficiently small positive elapsed time. It also lacks the required empty record. This obstruction applies to that restart, independently of receipt metadata.

## Stock-preserving separate handoff

Declare a new epoch only upon a separate typed handoff. Supply an empty isolated archive \(h=0\in W\) and an independent fresh donor \(s\ne0\in W\). In normalized Hilbert coordinates a candidate handoff is the orthogonal map
\[
(u,v,h,s)\longmapsto \left(s,\ (u-v)/\sqrt2,\ (u+v)/\sqrt2,\ h\right).
\]
Its output blocks are the active carrier, active record, archive and donor. It fixes even coordinates. On \(u=v=a,\ h=0\) it gives \((s,0,\sqrt2a,0)\). Orthogonality follows from the sum/difference norm identity and block permutation. The archive preserves old stock \(2\|a\|^2\) and recovers both held vectors by dividing its amplitude by \(\sqrt2\). The new active stock equals the donor's prior stock. A declared disconnected archive keeps old stock fixed while the fresh epoch starts at \(B=-\|s\|^2\) and can reach its own first directed root. This model grants a new epoch and an actual stock transfer. It requires neither republishing the previous root nor counting a second tick for it.

A lossless linear archive of the complete aligned held family needs dimension at least three because \(a\mapsto(a,a)\) has a three-dimensional domain and the readback must be injective. The construction attains this bound for one held epoch. With an empty donor and empty archive initially, conservation and full retention of old stock leave zero norm available for a nonzero concurrent fresh epoch. This is a resource bound for separate stock accounting. It permits different scoped branches that consume or release old stock. Unlimited retention would require further capacity or a defined source-side archive release.

The mode rule accepts capture only in the armed epoch at a resolved directed guard. An authenticated handoff must refer to the current held epoch and satisfy archive and donor preconditions. Its atomic update commits the transfer and a fresh epoch identity. Publication and acknowledgment affect receipt history alone. Duplicate or stale messages have no authority under the declared interface. The construction makes no claim that the project sources implement these transaction preconditions, provide the donor or archive or identify this operation with the native Stage 2.

## Verification

Run the adjacent exact replay. It checks guard directions, full map stock and inverse identities on bounded integer coordinates using rational sum/difference coordinates, old/new resource accounting, and stale or missing handoff conditions. Analytical proofs supply the unrestricted statements above.
