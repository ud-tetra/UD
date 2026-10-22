# Passive spring elimination, damping, and the octahedral metric sign test

22 October 2026. **EXACT conditional scalar-network calculation; CANDIDATE material interpretation; physical promotion 0.** Stacked on draft PR #410. This capture tests a simple microscopic response rule on the same 11-vertex midpoint-octahedral graph. The rule is specified here, not identified with graphite or derived as a UD law.

## Correct experimental target

The primary paper, Weipeng Chen *et al.*, “Observation of Superlubricity at Commensurate Moiré Graphite Interfaces,” *Physical Review Letters* **137**, 166201 (14 October 2026), DOI [10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2), reports **sharp friction peaks** at the complementary 21.8° and 38.2° orientations for the (2,1) commensurate moiré pattern. The peaks have **negligible load dependence**; the modeled sliding barrier is small but residual. The target is thus *angular peaks with negligible load slope and a small modeled residual barrier*, not a claim that friction is identically zero at the paired angles. The abstract is accessible; full measurement curves and Hessian entries were not supplied for this capture. Earlier conversation phrasing that called the paired-angle friction simply “vanishing” is corrected here. Prior octahedral captures did not fit either peak height or load slope.

## A specified passive scalar network

Partition vertices into four old corners \(v_i\), six old-edge midpoints \(m_{ij}\), and centroid \(o\). Assign positive scalar spring constants \(a\) to each of the twelve corner–midpoint edges, \(b\) to the six midpoint–centroid edges, and \(c\ge0\) to the twelve octahedral midpoint–midpoint edges. Pin each midpoint with \(\mu\ge0\); assign it mass \(m\ge0\) and an *externally supplied* viscous bath \(\eta\ge0\). For real Laplace \(s\ge0\), the dynamic stiffness is

\[
K(s)=\sum_{e} k_e (e_i-e_j)(e_i-e_j)^{\mathsf T}
 + (\mu+\eta s+m s^2)P_M.\tag{1}
\]

The midpoint block is \(K_{MM}(s)=[2a+b+4c+\mu+\eta s+m s^2]I-cA_{\rm oct}\), where \(A_{\rm oct}\mathbf1=4\mathbf1\). Put
\(d(s)=2a+b+\mu+\eta s+m s^2\). Every corner touches **three** midpoints. Eliminating the six midpoint displacements gives the exact Schur response on the retained corners and centroid,

\[
K_{\rm eff}(s)=K_{RR}-K_{RM}K_{MM}(s)^{-1}K_{MR},\quad
\boxed{(K_{\rm eff})_{o,v_i}(s)=-\frac{3ab}{d(s)}},\quad
\boxed{(K_{\rm eff})_{o,o}(s)=6b-\frac{6b^2}{d(s)}}.\tag{2}
\]

The octahedral coupling \(c\) cancels from these *centroid row* formulas because its graph Laplacian annihilates the uniform midpoint vector. It remains present in other entries and modes; no claim is made about the full reduced matrix's independence from \(c\). With \(a,b>0\), the static centroid–corner entry is strictly **negative**, while the normalized, \(S_4\)-invariant metric needed for exact seed intertwining in PR #410 has \((H_0)_{o,v_i}=+1/4\). Positive diagonal rescaling preserves the sign. Therefore **directly identifying this passive scalar spring stiffness, or its static midpoint-eliminated Schur complement, with that UD positive metric fails**. This does not exclude a distinct kinetic metric, tensor/vector interatomic force constants, a nonlocal coordinate map, or altered dynamics; those require explicit derivation.

## A conditional damping coefficient and load relation

For low frequency \(s\) with \(d_0=2a+b+\mu>0\), the centroid self response expands as

\[
(K_{\rm eff})_{o,o}(s)=6b-\frac{6b^2}{d_0}
  +s\underbrace{\frac{6b^2\eta}{d_0^2}}_{\Gamma_o}
  +O(s^2).\tag{3}
\]

Thus the stated *viscous midpoint bath* produces a nonnegative effective centroid damping \(\Gamma_o\); if \(\eta=0\), this linear coefficient is zero. \(\Gamma_o\) has units of damping when \(a,b,\mu\) are stiffnesses and \(\eta\) is a damping coefficient. It is **not** the measured sliding friction coefficient: the centroid displacement has no established map to interfacial translation, velocity, contact geometry, or force readout. A closed finite spring system cannot furnish irreversible loss by itself.

If these coefficients depend on normal load \(L\), then a flat *candidate damping* response would require

\[
\frac{\partial\log\Gamma_o}{\partial L}
=2\frac{b'}b+\frac{\eta'}\eta
 -2\frac{2a'+b'+\mu'}{2a+b+\mu}\simeq0.\tag{4}
\]

Equation (4) is a **conditional cancellation test**, not a prediction of observed load independence: no \(a(L),b(L),\mu(L),\eta(L)\) have been sourced. The network has no twist-angle variable or atomic registry, so it also cannot select peaks at 21.8° and 38.2°. Their complementarity belongs to the hexagonal/moiré baseline. A distinct UD residual requires a preselected angle/load kernel and a held-out quantitative comparison.

## Verification and limits

`verify_spring_response.py` reconstructs all 30 fine graph edges, performs rational 6×6 Schur elimination for five positive parameter controls, including an octahedral-edge contrast, and checks Eq. (2), including the factor three, sign, and \(c\) cancellation. It checks the low-frequency coefficient algebraically. `RESULTS.json` records the sample controls. The derivation is exact within the specified network; the sample controls are constructor validation, not a graphite fit or independent review. The supplied coefficient ledger v0.39(2) leaves physical normalization/source ports open; the CRL-2 subdivision remains a governance proposal. Physical promotion stays 0.
