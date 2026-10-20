# Square Gram eigenproposal residual alternative

Let G=Y-transpose Y be the complete r-by-r real Gram, V a square real r-by-r proposal, d a real diagonal. Suppose eta>=norm(V-transpose V-I)<1, and beta>=norm(GV-Vd). Then

    lambda_min(G)>=min(d)-beta/sqrt(1-eta).

For any unit left eigenvector w of G with eigenvalue lambda, set a=w-transpose V and b=w-transpose(GV-Vd). Then b_j=(lambda-d_j)a_j. Since norm(a)>=sigma_min(V)>=sqrt(1-eta) and norm(b)<=beta, the distance of lambda from the diagonal spectrum is at most beta/sqrt(1-eta). This applies to every Gram eigenvalue; it is not an assertion of indexed matching. The lower bound follows immediately.

If only a dyadic midpoint G0 is used and norm(G-G0)<=zeta, a sufficient beta is norm(G0V-Vd)+zeta norm(V), with norm(V)<=sqrt(1+eta). Frobenius bounds for the first norm and eta are conservative valid choices. Any entrywise enclosure of G must be converted to an operator bound (for example Frobenius<=r times a uniform entry error); an unscaled scalar entry error is insufficient.

The square/full-rank condition is necessary. For G=diag(1,0), a single proposed vector V=e1 with d=1 has exact zero residual and exact column orthogonality but gives no lower bound on G's missing eigenvalue0. For V=0 square, zero residual alone is likewise useless: eta<1 excludes it.

For finite equally spaced temporal samples, K and minus K have identical singular spectra: if T=(M-1)h, row reversal of F_K followed by exp(-TK) equals F_minusK. This equivalence permits a whole-generator sign reversal for condition assessment; it does not equate signed individual predictions or justify reversing only selected channels without an explicit conjugacy argument.

Development — no registry entry. No candidate numerical certificate has been evaluated by this lemma. Same-team review; external review PENDING; Physical Promotion=0.
