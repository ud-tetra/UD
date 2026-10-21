On the known real equal-stock U6×V2 family, two opposite-polarity pulses on the existing D3 port produce exact ray agreement, and zero-gain matched native flow retains it. The complete basin includes unequal stocks and compatible harmonic components; the second pulse is proved on the actual intermediate-state class. Incomplete and uncertain PSR records admit exact identifiability gates and deterministic channel error bounds. Native readout, polarity schedule, gain and physical clock remain OPEN. Development addendum only; independent review pending; physical promotion 0.

## Finite capture across intermediate states

On the unit-metric filled tetrahedron let A=Dᵀ−D, E=D3, W=E+Eᵀ and B=AW/4. Prior completed-port certificates give W²=4P_V, AW=−WA and WU=0. Then B is real symmetric and B²=P_V. Hold k=+1 and then k=−1, each for h=pi/(4sqrt(2)). The paired V generators square to −8I, so their quarter-pulse product is

`T_minus T_plus=[[0,−B],[B,0]] on V`.

In complex notation it is `(A−iW)(A+iW)/8=iB`. The complement follows exp(2hA). For x=u+v,y=sigma(u−v), sigma=±1, the endpoint is

`x_after=exp(2hA)u+sigma Bv`, `y_after=sigma x_after`.

Each packet has its original stock a+b and ray overlap r=1. Let F_sigma be the initial preparation subspace and K_sigma=T_plus F_sigma. The second pulse maps K_sigma into agreement by the full operator product; it does not reuse an initial-family theorem on K_sigma.

The complete nonzero-ray capture basin for this fixed sequence is broader: x=p+v,y=lambda p−lambda^(-1)v, where p∈V-perp, v∈V, lambda is finite real nonzero, and p,v are not both zero. This is necessary and sufficient, by projecting the endpoint relation y_after=lambda x_after onto the complement and V and using invertibility of their respective maps. The complement may include other active sectors and the harmonic mode; initial stocks need not be equal. Basin membership concerns actual amplitudes and can change under independent rescaling of the two packets. Endpoint stocks are a+b/lambda² and lambda²a+b. For p=h+(e0−e3),v=D e0123,lambda=2, stocks 7,13 become 4,16 and r goes from 16/91 to 1.

At capture stop coupling. Matched native dynamics then retain y=lambda x indefinitely under the stated model. For unequal captured stocks, unnormalized score feedback need not vanish, so the stop gate must inhibit feedback as well as probing. Repeating the pulse pair acts as −I on V and reintroduces disagreement. A stop gate is essential. The path need not improve r monotonically: the witness passes through r=0 during the first pulse, then reaches r=1 after the second. This finite capture theorem complements the earlier smaller-sector progress theorem.

For arbitrary pairs the exact endpoint forecast is r_echo=(x_Cᵀy_C−x_Vᵀy_V)²/[(||x_C||²+||y_V||²)(||y_C||²+||x_V||²)]. Require positive forecast stocks, absolute stocks or a known relative packet stock scale, and execute only if this exceeds the initial r. Independent packet root signs do not affect the forecast. A pair outside the exact basin, x=p+v,y=2p−v/3 with p=h+(e0−e3),v=D e0123, improves 1/4→121/124. Immediate repetition restores the original r and is rejected by the same gate; no iterative convergence theorem is asserted.

Universal capture remains false for harmonic-preserving controls: individual harmonic components are fixed, so an initial harmonic component in one packet and none in a nonzero neighbor preclude finite nonzero-ray alignment. Away from the special family, the local objective derivative is

`rprime=k[2QF/(Sx Sy)−2Q² C(Sx−Sy)/(Sx Sy)²]`, `C=xᵀWy`.

Independent packet sign reversal leaves PSR quadratic records unchanged but reverses this bracket. No arbitrary-pair blind fixed-polarity monotonic guarantee is inferred.

## Incomplete and uncertain receipts

Connected retained nonzero-support incidence receipts reconstruct the real ray from stocks and a spanning forest. Disconnected components have independent signs. A quadratic channel is pointwise identified exactly when c_CᵀO c_D=0 for every pair of distinct components; otherwise it varies over admissible component signs.

On full nonzero support the 15-node, 28-incidence Hasse graph gives the binary cut code [28,14,3], with 14 cycle checks. Exact enumeration establishes the distance. With a declared corruption bound, one sign error is uniquely correctable, two are detectable, and `2e+s<3` guarantees unique recovery with e errors and s erasures. Partial support and tree-only acquisition require their own graph codes. This result concerns real incidence signs, not continuous phase noise.

Given valid stock/current uncertainty bounds, retain only positive-stock endpoints and currents whose intervals exclude zero. If that reliable graph is connected, a reconstructed vector chat has

`||c−chat||²≤e²=sum_retained epsilon_i²/(4tau_i)+sum_discarded U_i`,

where true and estimated retained stocks exceed tau_i>0 and U_i upper-bound discarded stock. Thus

`|cᵀOc−chatᵀOchat|≤||O||[2||chat||e+e²]`.

For nonzero chat and e<||chat||, normalized projector error is at most beta=min(sqrt(2),2sqrt(2)e/||chat||). Two packets give |r−rhat|≤min(1,beta_x+beta_y). Certify progress only if the clipped post-pulse lower bound exceeds the pre-pulse upper bound. A disconnected reliable graph retains unresolved signs and cannot use an arbitrary component-sign estimate with this small error bound.

For pre-execution certification, orthogonality of the paired echo bounds each forecast vector error by sqrt(e_x²+e_y²). Use the corresponding forecast r interval and execute only when its lower bound exceeds the initial upper bound. This presumes exact pulse timing/gains; readout bounds alone do not bound actuation errors.

The exact four-epoch support theorem supplies no uniform noise floor: a sector approaching zero makes stocks and cross-sector currents arbitrarily small. Lower sector-stock bounds or observed confidence margins are necessary for a uniform robustness claim. Synthetic exact controls validate the mathematics; no measured noise corpus or calibration is asserted.

Ledger Q166 and Q170 support current and stock formulas; Q173 leaves gate-transition receipts open. These results close conditional finite capture and reconstruction questions while readout/switching authority, other control sequences and capture basins, calibrated uncertainty and physical implementation remain open. Physical promotion 0.

## Verification receipt

891 new exact checks passed: 862 construction checks and 29 integration checks. Authenticated parent replay and clean-extraction replay reproduced result bytes exactly; inherited checks are excluded from this count. The release contains 14 files. SHA256: `5e9dd00f45411c0ec4965e0d0d5cd46bce018d03bf70688017b6186bd8736079`. Independent review remains pending. Physical promotion is 0.