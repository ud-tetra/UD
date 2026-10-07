# UD constitutive current identifiability — v0.1

5 October 2026. Development addendum. Constructor: Codex for Benjamin Walker Mayes. Reviewers: none; independent review pending. Physical promotion 0.

## 1. Instruction refresh and source scope

The user-supplied **UD PROJECT RESPONSE INSTRUCTIONS — v1.0** govern this run: typed claims, source-bound derivation, scoped verification, review gates, and development notes on Updates. This records activation in this conversation; persistent ChatGPT project settings were not modified because no available settings operation exposes that field.

Sources: **UD_HASSE_CURRENT_CURL_AUDIT_v0.1**, sections 2 and 4, with its exact `audit/MATRICES.json`; attached **UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md**, Q169–Q172; **UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md**, sections 5–6. The ledger is a historical baseline, not a replacement for newer sources. Repository version 175 deployment was confirmed succeeded during this run. No retained result is overwritten, and no bridge review level advances.

## 2. Declared inference problem

Let G be the connected, finite Hasse incidence graph. D maps oriented real edge currents to simplex-address stock derivatives. The known generator has entries A[t,s]=b[s,t] in {−1,1} for lower-to-upper incidences and A[s,t]=−b[s,t]. Work at one instant with **real** amplitudes c_i=x_i a_i, where positive magnitudes a_i are known from stocks rho_i=a_i², and signs x_i belong to {−1,1}. Then

\[
j_{s,t}=2b_{s,t}x_sx_ta_sa_t,\qquad \dot\rho=Dj.
\]

The unknown current belongs to a finite constitutive class, rather than all of R^E. Normalization by Q=sum a_i² divides both stocks and currents by Q and changes no identifiability conclusions. This is an inference audit of the supplied law, not derivation of a native open-system law.

## 3. EXACT: generic stock-and-derivative identifiability

On a connected graph with all a_i>0 and nonzero known edge coefficients, two sign configurations give identical edge currents if and only if they differ by one global sign. For any two different sign rays, at least one edge changes its sign product. At an endpoint i of such an edge, the difference of stock derivatives is a polynomial containing a nonzero coefficient of a_i a_j. Distinct neighboring addresses supply distinct monomials, so that polynomial is not identically zero.

There are finitely many pairs of sign rays. Their collision sets lie in a finite union of proper polynomial zero sets. Outside that exceptional set, known stocks and all stock derivatives determine the sign ray and every current uniquely. “Generic” here means outside that finite algebraic exceptional set; it supplies neither noise robustness nor an experimental probability model.

This narrows the earlier 14-dimensional result without contradicting it: that count concerns unrestricted real currents. A finite sign-constrained current class is a different domain.

## 4. EXACT: a constructive positive profile and an exceptional profile

Choose a_i=2^i for an ordered list of addresses. The largest magnitude in any neighbor subset exceeds the sum of every smaller magnitude. If two sign rays have the same derivative at i, divide the equality by the known nonzero 2a_i. The remaining difference is a signed sum of neighbor magnitudes with coefficients 0 or ±2. Strict dominance forces every coefficient to vanish. Hence every adjacent sign product agrees, and connectivity implies global-sign equivalence.

This proves a concrete unique-reconstruction profile on any finite graph with the declared unit coefficients, even though its dynamic range may be unattractive. On the filled tetrahedron Q=(4^15−1)/3; normalized stocks are 4^i/Q. This is a mathematical witness, not a recommended preparation protocol.

Conversely, the equal-stock profile rho_i=1/15 is exceptional. Exhaustively enumerating 2^14=16,384 global-sign-fixed rays gives 16,256 distinct derivative signatures, with 128 repeated encounters, all involving different currents. These counts do not specify collision-class sizes. The receipt includes two explicit rays, their currents, their common derivative, and the ordering of all addresses and edges in the packaged matrix source. Displayed integer currents and derivatives must be divided by 15 for normalized stocks. Their nonzero current difference has zero divergence, so a genuine circulation ambiguity survives even within the real bilinear law.

## 5. EXACT: signed tree-current probes and defect bounds

If all magnitudes are positive, signed current observations on a spanning tree give every adjacent sign product on that tree. Fix one root sign and propagate products to all addresses. This reconstructs every current, including off-tree currents, without needing stock derivatives. It requires V−1 probes as a sufficient scheme; **no minimum-probe theorem is claimed** for this nonlinear class. For the one-, two-, and three-tetrahedron graphs this is 14, 22, and 26 probes, versus 14, 25, and 33 additional probes for the earlier unrestricted-current problem with derivatives supplied.

If an observed tree current has additive error e and |e|<2a_sa_t on each tree edge, its sign is correct. Exact known stocks and coefficients then recover the same sign ray. An edgewise bound, or the sufficient uniform bound |e|<min_tree 2a_sa_t, is needed; equality can erase a sign. Unknown stock errors require a separate bound. Vanishing amplitudes split the active induced graph: propagate within each connected component, while currents incident to inactive vertices are zero. There is no justified robustness claim when active stocks approach zero.

For direct derivative discrimination define d_x=Dj_x and
\[
\Delta(a)=\min_{[x]\ne[y]}\|d_x-d_y\|_\infty.
\]
For a uniquely identifiable positive profile this finite minimum is positive. With exact magnitudes, nearest-candidate reconstruction is unique for derivative error strictly below Delta(a)/2. Exceptional profiles have Delta=0. This formula is an acceptance contract, not a measured sensor budget; efficient search and useful margins remain open.

## 6. Limits and next trajectory

For complex c, stock flux uses only Re(conjugate(c_t)c_s). Complex conjugation preserves every stock and real flux for this real generator while reversing imaginary bilinear parts. Real-flux probes therefore cannot reconstruct the full complex PSR receipt. One must specify whether the target is real current or full phase receipt and obtain the corresponding observation channels. Real-state sign results do not transfer silently to complex phase reconstruction.

The release passes eight grouped exact checks, including exhaustive enumeration of 16,384 rays for each of two stock profiles and tree propagation over all rays. These are finite constructor checks plus the arguments above, not independent review. No sensor, preparation channel, physical unit map, native source law, or large-controller resource reduction is supplied. The controller WBS and Papers I–IV remain unchanged.

**Gap impact:** narrows transport identifiability under the retained real constitutive law; proves a degeneracy and a sufficient tree-probe repair. Highest-value next step: optimize a bounded-dynamic-range stock profile against derivative separation and stock/readout uncertainty, with a frozen noise contract. Priority judgment 92/100. This can distinguish feasible reconstruction from mere generic uniqueness before any physical bridge.

Unavailable attachment `Gap2_FINAL_Finite_Genesis.png` was not read or used; retry its upload if it should inform later work.
