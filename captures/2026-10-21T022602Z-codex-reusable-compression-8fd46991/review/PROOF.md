# Independent exact compression derivation

Let F:X→D be the fixed real observation map, rankr, with V=ker(F)^perp and H=range(F), dimV=dimH=r. Assume the singular values of F|V lie in[s,1]. Let Y:R^r→D be injective with sigma_min(Y)>m, and assume ||FQ−Y||<e<m. These are explicit inherited PR307 premises, not a new materialization or measurement of C.

## Range, exact inversion and gain

Since FQ has range in H, ||P_Hperp Yu||≤e||u||. Hence ||P_H Yu||²≥(m²−e²)||u||² and, for W=F^T Y and C=Y^T F=W^T,

sigma_min(C)=sigma_min(W)≥s sqrt(m²−e²)>s(m−e)=h.

W hasr independent columns contained in V; therefore range(W)=V and ker(C)=ker(F). The exact decoder B=C^+Y^T=W(W^TW)^−1Y^T has BF=C^+C=P_V. It returns P_Vx for exact nominal data, not the hidden component.

For the gain, put U=Y(Y^TY)^−1/2. Then U^TU=I and ||P_Hperp U||≤e/m=eta, so U^TP_HU≥(1−eta²)I. Because dimH=r, T=U^T|H is bijective and its singular floor is≥sqrt(1−eta²). Invertible left changes of coordinates cancel in a full-row-rank pseudoinverse decoder: writing Y=U A with A=(Y^TY)^1/2 gives C=A^TU^TF and C^+Y^T=(U^TF)^+U^T. Thus

||B||=||(U^TF)^+||≤1/[s sqrt(1−eta²)].

No separate ||Y|| amplification is needed. In the frozen profile s=61/27648,m=1/384,e=1/8192, eta=3/64 and h=3721/679477248. The gain is bounded by64/(s sqrt4087)<454, verified by squaring an exact positive rational inequality. Rescaling Y by any nonzero invertible column coordinate change does not change this exact decoder.

Let L=Y^TY. Then YL^−1C=P_range(Y)F, and ||F−YL^−1C||≤eta||F||≤3/64, with the same exact kernel as F. Its action onQ is≤e; the full operator need not have residual≤e. A small trial amplitude can make e small without proportionally reducing the subspace angle.

## Stored compression

Let G=C+D be a stored full-row-rank proposal with a certified operator error||D||≤delta<h. Weyl gives sigma_min(G)≥h−delta. Let P_G=G^+G. For any n∈ker(G), ||P_V n||≤||C^+|| ||Cn||≤delta/h||n||. Equal-dimensional row spaces imply ||P_G−P_V||≤delta/h.

For v∈V,

(G^+C−P_V)v=−(I−P_G)v−G^+Dv.

The terms on the right lie in orthogonal subspaces ker(G) and range(G^T). The same defect vanishes on ker(F), since C vanishes there. Consequently

||G^+Y^TF−P_V||≤sqrt[(delta/h)²+(delta/(h−delta))²]
≤delta/h+delta/(h−delta).

A single delta/(h−delta) term is not generally sufficient: a rectangular rank2 perturbation can simultaneously rotate the row space and perturb the solve in orthogonal directions. The exact fixture C=[I2,0], D=[[0,0,d],[d,0,0]], d=1/16 has ||D||=d but violates that single-debit bound on v=e1.

The gain remains controlled without an artificial ||Y||/h loss. Because CB=Y^T,

G^+Y^T=(G^+C)B,  ||G^+C||≤1+delta/(h−delta)=h/(h−delta).

Thus ||G^+Y^T||≤gamma*h/(h−delta), gamma=1/[s sqrt(1−eta²)]<454.

If actual data compression uses an exact encoded matrix Ytilde with ||Ytilde−Y||≤eYop, add eYop/(h−delta) to both this gain bound and the full-state defect bound (using ||F||≤1). The finite arithmetic implementing that compression and solve needs its own absolute-error certificate. A C-only error certificate cannot silently certify a different RHS map.

## Constructing columns and finite solves

Each trial column has time-block form(a cos±b sin)/64 with ||a||,||b||<9/8. Validated phase errors<2^-127 yield stacked norm error<(9/4)2^-127<3*2^-127, because sqrt4096=64 cancels the normalization. Final coordinate encoding error<504*2^-96 gives EY=3*2^-127+504*2^-96. Each encoded input column remains inside the adjoint domain, subject to validating the same source/trial/phase bindings.

For every individually verified column, the adjoint oracle produces a stored W-column within adUpper+EY of exact F^TY-column. Only after ALL1999 columns have such certificates can one infer operator error delta≤sqrt1999(adUpper+EY)<45(adUpper+EY). Likewise eYop≤45EY requires all columns. Sixteen successfully constructed columns do not establish full-frame rank, delta, inverse or a full decoder.

With the C31 exact adjoint bound, these conditional quantities give delta≈5.751915e-23 and encoded-map full-state defect<2^-55; the gain is<455. These are conditional whole-frame profile consequences, not actual completion of that frame.

A finite solve may certify per-record errors without assuming an inverse. Put H_G=GG^T. For computed RHS zhat, coefficient vector a and delivered xhat, verify

||zhat−Y^Ty||≤ez,  ||H_G a−zhat||≤er,  ||xhat−G^Ta||≤elift.

Then ||xhat−G^+Y^Ty||≤(ez+er)/(h−delta)+elift, since ||G^TH_G^−1||=||G^+||≤1/(h−delta). An unverified floating residual is not an enclosure; dot-product, matrix, RHS and lifting errors all require inclusion. The conditional choice ez=er=2^-64,elift=2^-44 gives error<2^-43. No actual full-frame solve is claimed.

These facts are exact finite-dimensional theorems under the stated premises. They provide no new acquisition, physical correspondence, full8192 run, universal floating-backend completeness or hidden-state recovery. Source/native/floating realization and all physical application obligations remain separate.

## Selected-column subprojection distinction

For k selected columns, Y_I inherits the same m/e bounds by restriction. Even though dimH may exceedk, D_I=U_I^TF has D_I D_I^T=U_I^TFF^TU_I>=s²(1−eta²)I. Thus C_I has full row rankk and exact B_I=C_I^+Y_I^T has gain<454 and B_I F=P_row(C_I), a rankk subprojection inside V. The perturbation proofs apply with delta_k<=sqrtk(adUpper+EY) and eYop_k<=sqrtk EY, when every selected column is validated.

This does not supply the full projection. For any rank16 map B16F on a1999-dimensional V, a unit vector in V∩ker(B16F) exists, so ||B16F−P_V||>=1. Actual16-row algebra or a partial subprojection certificate cannot be promoted to full-state observable reconstruction. The source data example also need not be in range(F); interpreting B_I y as P_I x requires a separate y=Fx premise.
