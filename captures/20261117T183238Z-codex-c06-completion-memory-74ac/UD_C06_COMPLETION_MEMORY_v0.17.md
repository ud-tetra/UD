# C06 completion memory v0.17

**EXACT / CONDITIONAL** for the bounded recorder composition and the false-arm witness. **CANDIDATE (agile)** for reserving and coupling the last Fire to C06. **OPEN** for native event authorization, capability reservation, reset and Stage 2. Physical Promotion = 0.

## 1. Source boundary and v0.16 audit

C06 v0.16, §§1–3, provides the declared Whitney port, its directed odd balance, and the selective hold. Write \(P\) for the odd orthogonal projector on the source and \(R_y\) for the orthogonal projector onto \(G(\operatorname{im}P)\) on the metric record space. With the metric adjoint, the post-event generator \(G_{\rm hold}=G(I-P)\) conserves total stock for any \(G\). The orthogonal-range condition \(R_yG(I-P)=0\) gives zero odd-record drift for all carrier states. It is separate from total stock conservation and holds for the declared port. Orthogonal subspaces can share coordinate support. For an initially empty record the zeros of \(Q_y-Q_x\) are \((2k+1)\pi/(4\omega_-)\) for \(k\ge0\); the upward zeros are \((4k+1)\pi/(4\omega_-)\). The initial ratio is undefined when the record has zero stock; the signed stock guard is defined.

The dated *UD capacity mechanisms and native crossing bridge audit* (UD@957d443, *Finite recorder mechanism* and *Bridge requirements*) captures a logical bounded recorder from SA-TIME-018. It defines a width-\(w\) completed count \(R\), a pending event bit \(h=p_a\mathbin{\mathrm{XOR}}\alpha\), and an admitted event count \(N_a=R+h\). Fire requires \(h=0\). At exhaustion the recorder preserves the all-ones word and old acknowledgment, with \(R=2^w-1,\ h=1,\ N_a=2^w\). The pending flag marks an event that already occurred. Use the abstract \(R\), whose definition accounts for carry, for any decoder. The underlying manuscript bytes were unavailable to the later *Sequential receipts and finite recorder source gate* v0.1, which confirms the bounded count semantics and missing amplitude-to-Fire bridge. This is evidence for a conditional logical recorder.

Ledger v0.85 Q194–Q210 in the sequential and sourced history audits supplies the conditional obligation-space event and distinguishes endpoint from predecessor lineage. It does not identify an irreversible edge-saturation predicate for the C06 balance. The Q156 closure/integrity source has Boolean update conditions given factor histories. In the unitary-only integrity branch, both the active and selective-hold skew flows preserve norm, so a loss of unitarity cannot provide the C06 Fire. An edge saturation interpretation would need its own polarity, state map, threshold, and actuator update.

## 2. Reserved terminal Fire comparator

Let \(M=2^w-1\) for any \(w\ge1\). Compare the following abstract states for one nonzero odd preparation and the declared parity-separated port.

| Mode | \((R,h)\) | Completion readout | Amplitude flow |
| --- | --- | --- | --- |
| Reserved Ready | \((M,0)\) | \(0\) | \(G\) |
| Fired / overflow handling / terminal FULL | \((M,1)\) | \(1\) | \(G(I-P)\) |

Use \(b_{\rm latch}=\mathbf1[N_a=2^w]\) in this reserved state space. Make the following interface assumptions explicit. Initialize at known \((M,0)\) with an empty C06 record. Authorize precisely one use of the slot, exclusively by the first incoming positive-slope balance with nonzero odd stock. On that balance, commit Fire and the port-selection change in one abstract event with \(x^+=x^-\), \(y^+=y^-\). The actuator reads the committed record from Fire onward, during any overflow detection and after FULL. Stage 2 requires its own prerequisites.

The Fire changes \((M,0)\) to \((M,1)\). Its acknowledgment would exceed the width and is unavailable under the no-wrap rule. Pending blocks another Fire. As long as the declared recorder is retained with no reset, \(b_{\rm latch}=1\) persists and the odd carrier and record hold their exact half stocks. The even flow remains its original v0.16 flow. The switch preserves norm through the skew operator and identity amplitude reset. This proves persistence conditional on the reservation and explicit wiring. Reserving the slot and selecting the moment of Fire are additional hypotheses.

## 3. Exact discriminants

**NO-GO for an unreserved count decoder.** Start both histories at the reserved numeric state. At the same external event time, a designated C06 Fire and an unrelated admissible Fire can each change \((M,0)\) to \((M,1)\) in the abstract recorder. If unrelated Fire arrives at the v0.15 under-transfer witness, a count-only actuator would freeze \(f=1/50\). The resulting recorder state is identical to the one reached on \(f=1/2\). The collision concerns the recorder readout under the unreserved product model. The full amplitude states differ. A source-proved reservation or retained event identity removes this witness and is precisely the datum to test.

**Pending alone can clear.** For a nonterminal Fire starting at \(R<M\), successful Ack clears \(h\) while \(N_a\) remains at the increased count. Reading only \(h\) would restart a hold on acknowledgment. This is distinct from the terminal slot where acknowledgment is blocked.

**Early or late execution is consequential.** With ideal rotation still active and a dimensionless delay \(\delta\) between the first crossing and actual cut, the latched fraction is \(1/2+\sin(2\omega_-\delta)/2\). Transfer is exact at the first arrival with zero delay; subsequently there are isolated coincidences, so a delayed implementation cannot assume exactness. A logical commit proof alone leaves the relative timing between the recorder and amplitude actuator open.

The replay exhausts ordinary and terminal Fire/Ack cases for widths 1–8, checks the under-transfer false-arm witness, and checks rational two-sector stock and held-block equations. It exercises the abstract counter contract rather than the cursor-level recorder implementation. Run python3 replay_c06_completion_memory.py.
