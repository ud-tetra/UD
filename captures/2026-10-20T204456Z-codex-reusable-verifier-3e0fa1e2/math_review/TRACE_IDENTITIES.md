# Fresh Frobenius norms from exact sufficient statistics

Independent proof addendum, frozen before exercising the new reusable implementation. Development — no registry entry. Physical Promotion = 0.

Write Z=N/2^bN, U=Ui/2^bU, V=Vi/2^bV, and retained S=diag(si)/2^bS. Every integer matrix is decoded exactly from its supplied bytes. Define fresh sufficient statistics M=N^T N, K=N^T Ui, A=Ui^T Ui, B=Vi^T Vi. Let

\[
C_{\rm cross}=\sum_{i,j}K_{ij}(V_i)_{ij}s_j.
\]

For the forward residual choose kF=max(bN+bV,bU+bS), alphaF=2^(kF-bN-bV), betaF=2^(kF-bU-bS). Its exact integer numerator is alphaF NVi-betaF Ui diag(si). Expanding the Frobenius square gives

\[
\|ZV-US\|_F^2=\frac{
\alpha_F^2\operatorname{tr}(V_i^T M V_i)
-2\alpha_F\beta_F C_{\rm cross}
+\beta_F^2\sum_j s_j^2 A_{jj}}
{2^{2k_F}}.
\]

Indeed tr(Vi^T MVi)=||NVi||F^2, while <NVi,Ui diag(si)>=sum_j sj (Vi^T N^T Ui)jj=Ccross. No assumption that factors are orthogonal or S commutes with their Gram matrices is used.

For the adjoint residual choose kG=max(bN+bU,bV+bS), alphaG=2^(kG-bN-bU), betaG=2^(kG-bV-bS). Its integer numerator is alphaG K-betaG Vi diag(si), yielding

\[
\|Z^TU-VS\|_F^2=\frac{
\alpha_G^2\sum_{ij}K_{ij}^2
-2\alpha_G\beta_G C_{\rm cross}
+\beta_G^2\sum_j s_j^2 B_{jj}}
{2^{2k_G}}.
\]

The cross sum is the same integer scalar in both formulas; its scale factors and denominator exponents are independently selected for each residual. These are exact integer identities, so cancellation cannot be treated by a floating tolerance. A negative computed squared numerator is an invalid computation/witness and must HOLD, not be clamped to zero.

Upward square-root enclosures of these exact residual squares bound their operator norms via ||F||2<=||F||F. The retained Gram defects follow from A-2^(2bU)I and B-2^(2bV)I divided by their corresponding dyadic scales. The tail Gram defect and output Gram are E=Vdi^T Vdi-2^(2bD)I and H=Vdi^T M Vdi. Tail output operator enclosure still requires the fourth root of the sum of squared **rational H entries**, while residual Frobenius enclosures require square roots of the trace-expanded squares.

Consequently independently verifying the six integer matrices M,K,A,B,E,H suffices to establish every fresh scalar norm premise of the generic singular-value proof. M,A,B,E,H are symmetric and may be losslessly triangular-packed with an explicit dimension/order convention; K is full rectangular. Norm sums of a triangular-packed symmetric matrix must count each off-diagonal entry twice. The K cross sum and norm sum count each full entry once. Hashes and scalar identities do not replace the six matrix-product identity checks.
