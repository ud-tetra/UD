# C06 directed event authorization v0.18

**EXACT / CONDITIONAL** for the crossing and flux tests. **NO-GO** for authorization from the audited coarse receipts alone. **CANDIDATE (agile)** for event authorization that reads the projected balance and changes the port in the same event. **Physical Promotion = 0.**

## Balance, differential and directed flux

Use the aligned odd carrier and record coordinates \(u,v\) of v0.16 §§1–3 with common Hilbert metric and rate \(\omega_->0\). Let \(N=\|u\|^2+\|v\|^2>0\), \(B=\|v\|^2-\|u\|^2\), and let \(J=2\omega_-\langle u,v\rangle\) be inward odd-record stock flux on the incoming branch. Under reciprocal exchange \(\dot u=-\omega_-v,\ \dot v=\omega_-u\), conservation gives \(\dot B=2J\).

The covector \(dB=(-2u^\flat,2v^\flat)\) vanishes only at zero total stock. Restricted to the sphere \(N>0\), it is also nonzero at balance: the tangent vector \((-u,v)\) at \(B=0\) evaluates to \(2N\). A directed root witness is \(B=0\) with \(dB(\dot u,\dot v)>0\) on the incoming branch.

With empty records \(u=u_0\cos(\omega_-t)\), \(v=u_0\sin(\omega_-t)\). At the first half-transfer, \(J=\omega_-N>0\). The next flux sign reversal is at full record stock \(f=1\). In the fixed-stock witnesses \((7,1),(5,5),(1,7)\) along a unit mode, \(N=50\), so \(J/\omega_-=14,50,14\). All three flux signs agree. On this aligned model \(J=\omega_-N\) is an exact alternative to directed equality, because \(\omega_-N-J=\omega_-\|u-v\|^2\). On the prepared orbit it picks upward balances. Its maximum is tangential, so a zero-crossing detector on the flux deficit has no transversal sign change. Repeated upward balances still require first-event selection.

## Receipt sufficiency and the proposed transition

C06 v0.15 §2 keeps audited discrete receipt data and event time fixed across unequal odd-stock phases. The same receipt can therefore correspond to a guard that is true or false. Adding the sign of incoming \(J\) preserves this ambiguity for the exact witnesses above. Any deterministic authorization using only those fields must make the same decision on both. The Q156 native trigger audit §§2–2.1 supplies a closure/integrity predicate under admitted factor histories. Ledger v0.39 Q166–Q167 supplies signed chain-incidence stock currents. These constructs leave open a map that transmits the paired, aligned odd-stock guard to SA-TIME-018 Fire and changes the odd block at commit. C06 v0.17 §§1–3 supplies a terminal state that can retain an authorized event.

In a declared composition, initialize Ready with the final slot reserved. The transition domain contains only the first incoming \(B=0,\ J>0,\ N>0\) from this preparation. The authority reads the local model state directly and publishes a receipt bound to that transition. An unrelated event or a supplied tag carries no authority to change the reserved slot. At the root, execute one update from Ready to Hold, terminal Fire, and \(G\mapsto G(I-P_-)\), leaving amplitudes continuous. During Hold the slot rejects all further Fire. The same-event update preserves total stock, freezes both odd registers and preserves the even flow by the v0.16 orthogonal record-range condition. Exclusive access, direct guard access and same-event actuation are new hypotheses. The audited source admits a counter implementation but leaves this coupling and Stage 2 open.

A tag generated downstream of a shared Fire cannot undo a premature cut. Timing likewise matters. If active flow persists for \(\delta\) after the first root, it yields the v0.17 exact error \(\sin(2\omega_-\delta)/2\). The proposed receipt therefore binds authorization and selection of the held generator to the event, with no intermediate active-flow step.

## Replay

Run python3 replay_c06_directed_authorization.py. It checks exact signs, maximum flux, and candidate acceptance under unrelated events, a supplied tag, earlier/later transfer, descending balance, zero stock, repetition and Hold. The proof applies to the declared incoming odd model. The Boolean replay explores that candidate contract and does not establish a native issuer.
