# Reversible receipt majority and its resource gate

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Result and source scope

A three-receipt majority module is constructed as a reversible gate sequence and integrated with the existing twelve-bit ground encoding. It reduces a declared independent receipt-error rate, but costs additional workspace, carrier hold time, gates and garbage reset. Faults in the majority/copy operation impose a second accuracy requirement. The calculation is conditional on source-receipt independence and specified fault channels; it does not derive their actual probabilities or energy environment from UD.

Native P_f supplies the carrier observable. The four-incidence hold and bath-isolated memory write are the prior candidate controls. Native autonomous timing, coupling switches, G05/G06 normalization and horizon map remain open. G is unused.

## 1. Acquire three receipts of the held observable

Use three distinct, initially blank receipt bits a,b,c and a separate initially blank output o. Hold A=P_f by removing its four cross-incidence couplings, so its binary label R is constant throughout acquisition and cleanup. Acquire A into each receipt by the corresponding controlled bit flip. Declare independent XOR acquisition errors E_i with probability p, giving

\[
(a,b,c)=(R\oplus E_1,R\oplus E_2,R\oplus E_3).
\]

These are independent errors conditional on R, not independent receipts marginally: all receipts share the source label. Their error environments must be independently supplied by a future physical model. Fresh bits and repetition alone do not prove that independence.

The native source is only copied as a binary observable during its hold. This is not a three-copy measurement of an arbitrary unknown quantum state.

## 2. Reversible majority and cleanup

Boolean majority satisfies

\[
\operatorname{maj}(a,b,c)=ab\oplus ac\oplus bc.
\]

Apply three Toffoli gates controlled respectively by (a,b), (a,c), and (b,c), each targeting o. From o=0, this computes the majority. Copy o into boundary-memory seed bit 0. Reverse the three majority gates. Finally apply the carrier-controlled receipt copy again to each receipt, converting its value R XOR E_i into E_i. The truth-table checker verifies all input and fault patterns.

With ideal decision gates the output o returns to zero, the three receipt bits retain their error flags, and the memory seed is

\[
S=R\oplus\operatorname{maj}(E_1,E_2,E_3).
\]

Fan the seed out along the previous eleven neighboring CNOTs, starting from the otherwise blank twelve-bit boundary. This generates the same conditional all-zero/all-one codeword family used in the earlier thermal replay.

Primitive counts are three acquisition gates, three majority Toffolis, one seed copy, three reverse Toffolis, three carrier receipt uncopies, and eleven fanout gates: 24 total. The carrier hold lasts through the first 13 gates; thereafter carrier and memory can decouple. The decision module uses four extra workspace bits. Its Toffolis are three-body gate primitives, not a proven two-local decomposition. Routing among receipt bits and the memory seed is declared local to an added decision module, whose physical geometry is not derived.

## 3. Receipt and decision fault laws

For independent acquisition errors the majority seed error is

\[
p_3=3p^2-2p^3.
\]

Exact enumeration gives p3=1499/500000000 at p=1/1000 and p3=149/500000 at p=1/100. This quadratic reduction is conditional on the independent error source.

Now declare an independent target XOR fault of probability q after each of the three forward majority gates and after the seed-copy gate. The four faults combine as a parity error

\[
u_4=\frac{1-(1-2q)^4}{2}.
\]

The effective seed error is therefore

\[
\boxed{p_{\rm eff}=p_3+u_4-2p_3u_4.}
\]

The receipt gates' p and the decision gates' q are different typed probabilities. Reverse computation, carrier uncopies and downstream fanout are ideal in this release. Adding their faults requires a new channel; it cannot be inferred from the four-event model above.

For storage error e_r conditional on a perfect seed, final error is exactly

\[
e_{\rm final}=p_{\rm eff}+(1-2p_{\rm eff})e_r.
\]

## 4. Retention and latency test

The replay derives the same Gibbs storage kernel on the twelve-face graph at beta J=(ln3)/2. Exact rational propagation gives e20 approximately 0.001912274 and e32 approximately 0.009238832. The gate clock again assigns one complete gate round and one collision/refresh round to one slot; this is a declared ratio.

At a common 44-slot deadline, the majority write takes 24 slots and leaves 20 storage updates. The previous single-seed ground write took 12 slots and left 32. The one-hot write took one slot and left 43. Receipt reset is deferred after readout in this schedule; charging its duration before the deadline requires a new time allocation.

| Acquisition p | Decision q | Error after 32 storage updates | Error at 44-slot deadline, 20 storage updates |
|---:|---:|---:|---:|
| 1/1000 | 0 | 0.00924177 | 0.00191526 |
| 1/1000 | 1/10000 | 0.00963426 | 0.00231361 |
| 1/1000 | 1/1000 | 0.01315608 | 0.00588800 |
| 1/100 | 0 | 0.00953133 | 0.00220913 |
| 1/100 | 1/10000 | 0.00992358 | 0.00260725 |
| 1/100 | 1/1000 | 0.01344332 | 0.00617953 |

All criterion comparisons use exact rationals. Decimal errors are displays. For the declared one-percent final-error target after 32 storage updates, acquisition p=1/100 combined with decision q=1/10000 passes; decision q=1/1000 fails. At the common deadline the lower thermal exposure improves the error, but spends more time in bath-isolated writing. It is not an intrinsic lifetime improvement at equal post-write age.

At 32 updates the seed ceiling remains (1/100−e32)/(1−2e32), approximately 0.000775498. Majority helps only if both the acquisition majority error and the added decision parity fit inside this ceiling.

## 5. Workspace, energy and reset

Declare the four workspace bits energetically degenerate during the decision stage. This permits ideal logic with zero workspace endpoint energy change, but requires pure blanks and driven control. It does not assign zero total controller cost.

After noisy forward decision gates and ideal reverse computation, o retains the parity of the three forward majority faults, with probability

\[
u_3=\frac{1-(1-2q)^3}{2}.
\]

The receipt uncopies leave E_1,E_2,E_3. The workspace's marginal entropy is

\[
H_{\rm garbage}=3h(p)+h(u_3).
\]

For a blind isothermal reset of that degenerate workspace to its original pure blanks, the necessary work bound is kBT H_garbage. At p=1/100,q=1/10000 this is approximately 0.170738 kBT; at q=0 it is approximately 0.168005 kBT. These are workspace-reset bounds additional to boundary memory reset, drive and source-hold resources. Exact finite pure reset is not provided; accessible side information can change the reset bound but must be physically specified.

The original carrier hold is used explicitly to uncopy R from the receipts. Error flags remain because their stochastic origins are not reversibly controlled in this model. They may correlate with the memory label. Logical uncomputation cannot silently erase an inaccessible noise environment or those flags.

The noise environments themselves still lack Hamiltonian, preparation and renewal laws. Therefore this calculation is not a complete energetic implementation of faulty majority. The twenty-four gate schedule, four workspace blanks, garbage entropy, hold duration and deferred reset are concrete new resource obligations.

The boundary-memory energy still ends at zero for either ideal ground codeword; the earlier 10J fanout path barrier remains. Those facts do not cancel the added decision-module resource costs. The nominal boundary remains 12a0, but the physical area occupied by added workspace is unknown. Retained information per total apparatus area cannot be computed by ignoring that workspace.

## 6. Independence and common-mode failure

To expose the source assumption, let every receipt error contain a shared XOR component C with probability c, plus independent components with probability p. Then

\[
p_{\rm maj}=c+(1-2c)(3p^2-2p^3).
\]

A perfectly shared error is not reduced by majority. The total single-receipt marginal error is c+(1−2c)p, so c and p cannot be conflated with one quoted receipt-error rate. A future source law must establish independent components or directly bound shared error; repeating the same faulty source mechanism is insufficient.

## Disposition and next gate

CHECKED: reversible majority truth table; independent-error reduction; decision parity penalty; workspace garbage; exact storage and common-deadline errors. CANDIDATE: independent acquisition source, degenerate workspace, primitive Toffoli clock and ideal cleanup. OPEN: physical source/decision fault energy, shared-error bound, native clock and local implementation, workspace geometry, pure preparation/reset, extensive area density and horizon normalization.

The next source task is to derive or bound common-mode receipt error and the decision-module error channel while supplying its resource state. The present construction closes the conditional logic and exposes what its claimed robustness requires. Physical promotion remains 0; independent review OPEN. No ledger, registry, site or repository changes. Gap2_FINAL_Finite_Genesis.png remained unavailable and unused.
