# UD Q81-Q84 Signed-Reference and Source-Observer Gate v0.1

**Scientific date:** 2026-11-01  
**Status:** `EXACT_SCOPED` (K4 Hodge/reference mathematics, S4 covariance, phase quotient, cusp threshold, invariant-polynomial controls) / `DERIVED_CONDITIONAL` (paired context reference) / `NO-GO` (unique O09/Q81--Q84 cardioid observer not selected) / `OPEN_GATED` (context-to-Hodge and detector bridge).  
**Physical promotion:** **0**. **Non-constructor review:** pending. No laboratory or cosmology targets used.

## 1. Source objects and typing

Current recovered coefficient ledger: `library_LEDGER_v0.85.json` (published recovery 2026-10-21; **scientific_revision = v0.43**); source URL: <https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json>.

| ID | Exact source definition | Type and next gate |
|---|---|---|
| O09 | `I_lift=(1/2) sum_{omega>0} a_omega Delta(phi_tilde_omega)` | Modal history action/increments; **no local link-to-context map**, absolute phase reference, nor detector |
| Q81 | `Delta Phi_E(alpha,beta)=Arg[u(P_beta)^(-1)u(P_alpha)] mod 2pi` | Conditional **context/environment** relative phase; packet context forcing open |
| Q82 | `n_seam->chain in {+1,-1}` | Orientation convention; not a free continuous coefficient |
| Q83 | `phi_chain(P_alpha)=n Phi_E(P_alpha) mod 2pi; s_alpha=n Phi_E(P_alpha)/2 mod pi` | Conditional chain normalization; context source open |
| Q84 | `K_seam->chain(alpha,beta)=cos(Delta Phi_E(alpha,beta))` | Real **signed** relative coherence; apparatus forcing open |
| Q76/Q77 | `cos(Delta phi_chain)` / `abs(cos(Delta phi_chain))` | Signed versus unsigned kernels; branch-to-chain map open |
| Q85/Q87/Q92 | Context burden record; normalized signed record overlap; magnitude-sensitive signed overlap | Requires actual environment burden records; not a K4 modal-reference map |
| Q165/Q166/Q169/Q170 | Grade stocks; signed bilinear currents; skew Hodge generator; region stocks | Finite internal mathematical observables, not physical photon/instrument readouts |
| G05 | Former universal scalar retired | Must not be restored to normalize this bridge |

Historical baseline: [Paper I mathematical results, §4.3](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/mathematics/), full oriented Delta^3 with unit graded chain metric and `A=B^T-B`, `A^2=-4(I-P0)`. Previous quadratic-observer artifact: draft [PR #501](https://github.com/ud-tetra/UD/pull/501), `UD_NATIVE_QUADRATIC_OBSERVER_GATE_v0.1`.

These are **distinct carriers**: (i) graded real K4 chain state `X`, (ii) prepared reference `r` in K4, (iii) context phases `u(P_alpha)` in Q81, (iv) complex diagnostic outputs, and (v) a potential physical apparatus. Equal complex phase values would not identify their source spaces.

## 2. Exact prepared-reference theorem

**Assumptions:** Let `C=direct_sum_k C_k(Delta^3;R)` be the real 15-dimensional chain carrier, with native unit metric, `A=B^T-B`. Take any nonzero **pure edge** vector `r in C1`, fixed in the observer/preparation record; set `q=<r,r>` and `r_perp=A r/2`. Start `X(0)=r` and evolve by `X(s)=exp(sA)r`.

`A^2 r=-4r`, `<r,Ar>=0`, and `<Ar/2,Ar/2>=q`. Therefore

`X(s)=cos(2s)r+sin(2s)r_perp` and

`u_r(X)=<r,X>/q + i <r_perp,X>/q = exp(2is)`.

From source-defined Q165/Q166 stocks/currents the previously proved internal circular readout is `W=exp(4is)`, so **exactly on this orbit** `W=u_r^2`.

Under all 24 signed `S4` relabelings `g`, both `r` and `X` transform, and the reference readout stays unchanged: `<gr,gX>=<r,X>` and the same identity for `A r/2`, because `A` intertwines the signed action. If `r` is held fixed while `X` alone is relabeled, this covariance claim no longer follows: the observer is a marked carrier.

**Conclusion (`EXACT_CONDITIONAL`):** A *retained and oriented* initial reference supplies a unit-amplitude **sign-sensitive first harmonic** without parameter fitting. **OPEN:** UD source law has not shown how a detector/context prepares, retains and reads that reference, or why Q81's `u(P)` must equal this Hodge phase. An internal mathematical initial condition is not a calibrated physical reference.

## 3. Q81--Q84 can encode a signed relative phase, with two different gates

For unit complex context phase records `v_alpha=u(P_alpha)` and `v_beta=u(P_beta)`, Q81 defines the relative phasor `rho=v_beta^{-1} v_alpha=exp(i Delta Phi_E)`. This is invariant under **simultaneous** common rephasing `v_j -> exp(i gamma) v_j`. With `v_beta` held fixed, `v_alpha -> -v_alpha` sends `rho -> -rho`, so a sign reference is mathematically available.

Q84 selects only its **real component** `K=Re rho=cos Delta Phi_E`. Q82's orientation inversion `Delta->-Delta` leaves `K` unchanged and reverses the absent imaginary component. Q77's magnitude `|K|` also loses the sign under `Delta->Delta+pi`.

If **as a separately declared bridge** `Delta Phi_E(s)=2s-eta`, then Q84 reports the native first-frequency cosine `cos(2s-eta)`. A second *prepared context phase shifted by pi/2* reports `sin(2s-eta)`; the two form the complete `rho`. Q81's full `Arg` record itself can determine `rho` mathematically when the `u(P)` are available. But neither a physical apparatus generating the phase `2s-eta` nor its independent quadrature/reference preparation is sourced from O09 or Q81--Q84.

**Exact one-cosine incompleteness:** Let `c=cos theta` and even stock phase `W=exp(2i theta)`. At `theta=pi/2` and `theta=3pi/2`, `(c,W)=(0,-1)` in both cases, whereas `exp(i theta)=+i` and `-i`. One signed cosine plus `W` is not a globally injective instantaneous phase observer. A two-quadrature context record or additional history/branch convention resolves the discrete ambiguity. No assertion about actual detector errors follows.

**Additional Q83 half-phase obstruction:** The source normalized `s=n Phi_E/2 mod pi` lives in `R/(pi Z)`. The quantity `exp(2i s)` is single valued, but `exp(i s)` changes sign under replacing `s` by `s+pi`; therefore any **half-phase odd observable** requires a `Z2` branch lift. Changing Q82's `n=+1` to `n=-1` conjugates the full oriented phasor but does not choose between `s` and `s+pi`. This does **not** deny that Q81 supplies a complete **context** phasor `exp(i Phi_E)`; only the separately typed half-angle square root is ambiguous.

## 4. Cardioid coefficient is still not source-selected

On the prepared reference plane, the available normalized channels are `u=exp(i theta)` and `W=u^2`. A family of **candidate** complex observers is

`Z_(lambda,eta)=lambda exp(i(theta-eta)) - exp(2i(theta-eta))`, where `lambda>0` is an observational mixing gain and `eta` is a preparation alignment. Q81 gives relative phase only, Q84 fixes only one real phase kernel; Q165/Q166 fixes the native quadratic stock normalization. **None** of these source rules fixes `lambda` or the cross-carrier alignment `eta`.

Since `d Z_lambda/dtheta = i lambda u - 2i u^2`, a stationary trace exists iff `lambda=2` when `lambda>0` and the coefficient of `u^2` is fixed to `-1`. `lambda=1` and `lambda=3` give smooth traces with minimum derivative magnitude `1`, yet use the same native Hodge state and prepared relative reference. Thus the precise cardioid ratio is **not** independently derived by UD. More generally, the condition for `a u + b u^2` is `|a|=2|b|`, with nontrivial relative phase only changing cusp location.

**NO-GO / exact hypotheses:** Any assertion that Q81--Q84 and O09 uniquely choose the cardioid coefficient or optical detector is false without an additional dynamical/measurement source law. Supplying the coefficient from the observed cardioid geometry is an inverse problem, not a native prediction.

## 5. Representation audit: no invariant linear edge scalar, but cubic odd alternatives exist

The signed permutation representation of `S4` on oriented `C1(Delta^3)` (six edge coordinates) has no invariant vector:

`(1/24) sum_(g in S4) rho_C1(g) = 0_(6x6)`.

Therefore any **linear S4-invariant scalar readout of the unreferenced edge state** is identically zero. A nonzero linear signed readout needs a co-transforming prepared reference or a separately selected symmetry-breaking structure.

**Important scoped counterexample:** The stronger statement "S4 symmetry forbids all odd reference-free readouts" is **false**. For `x in C1`, define the *new candidate cubic scalar*

`C3(x)=sum_(v=0)^3 ((B1 x)_v)^3`.

Because `B1` intertwines the signed edge representation with vertex permutations, `C3(gx)=C3(x)`, while `C3(-x)=-C3(x)`. This is not Q165's quadratic stock or Q166's bilinear current; it is a mathematically compatible, **unselected** cubic observer.

For a pure-edge prepared `r`, the edge coordinate is `x_edge(s)=cos(2s)r`, so

`C3(x_edge(s))=C3(r) cos^3(2s)=C3(r)[3 cos(2s)+cos(6s)]/4`.

It produces native-frequency and third-harmonic *observed* components from one mode, for generic `C3(r) !=0`. It vanishes on an individual single-edge preparation. The symmetric-cube `S4` invariant dimensions for polynomial degree `0,1,2,3` on the six-edge carrier are exactly `(1,0,2,2)`; independently checked by character formula and monomial action on 24 permutations. **OPEN:** No source selects this cubic as the physical instrument. It is an adjacent possible observation mechanism, not a proof that an external reference is unnecessary in the accepted Q165/Q166 **even-only** observer lane.

## 6. Reproducibility, adversarial controls, and decision

1. `exact_reference_gate.py`: regenerates the complete 15-dimensional signed incidence and dynamics, arbitrary real edge initial reference, 24 signed permutations, Q83 projective lift, signed/magnitude kernel controls, cusp gain, cubic invariant and character counts. **PASS**.
2. `independent_reference_replay.py`: independently regenerates matrices, applies `scipy.linalg.expm` at 8192 points, tests simultaneous contextual phase rephasing and full quadrature, tests two unequal cardioid gains, checks all 24 cubic covariances, and independently computes symmetric-power invariants by monomial permutation traces. **PASS**; numerical maximal modal error about `6.11e-15`.
3. No experimental signal was scored; context-induced observer gains are not fitted, and physical measurement uncertainty remains separate from structural readout non-injectivity.

**AUTO_LOCK RECOMMENDATION (scoped exact):** Prepared co-transforming K4 reference provides `u_r=e^{2is}`, and Q81/Q84 provide a compatible, signed relative-phase syntax if a typed context-to-Hodge map is supplied. Q83 has a half-phase `Z2` branch ambiguity; one cosine combined with the even doubled phase is not globally injective. Existing source operators do not determine the cardioid gain. Signed `S4` permits generic cubic odd scalar observers outside the Q165/Q166 source-defined quadratic lane.

**AUTO_FREEZE:** any claim that O09/Q81--Q84 alone uniquely select the first-harmonic context, relative gain `lambda=2`, a physical detector or a measured mass/EM/cosmological correction.

**Next gate:** Obtain (i) the source-recovered context interaction `E_theta,env` producing `u(P)`, (ii) the typed intertwiner between that context and the K4 Hodge modal plane, (iii) reference preparation and protected/paid retention, (iv) two-quadrature or branch-tracked readout and its observer units, and (v) a target-blind normalized mixing law. Then freeze the apparatus covariance, uncertainty and failure controls before any physical comparison.

**Physical promotion remains 0.** No new source action or detector law has been adopted and independent non-constructor review remains pending.
