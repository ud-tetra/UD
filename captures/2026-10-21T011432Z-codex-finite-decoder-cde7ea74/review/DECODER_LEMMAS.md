# Independent Chebyshev decoder and full-space error derivation

Let F be the fixed PR307 map, ||F||<=1, rank1999/kernel641, and s=61/27648 strictly below its smallest positive singular value. Put A=F-transpose F, a=s², c=(1+a)/2, d=(1-a)/2, Z=(cI-A)/d and sigma=c/d>1. Write P for the Euclidean projector onto ker(F)-perpendicular. These are inherited model premises, not newly measured facts.

## Ideal polynomial and recurrence

For k>=0 let p_k(lambda)=T_k((c-lambda)/d)/T_k(sigma). Since p_k(0)=1, q_{k-1}(lambda)=(1-p_k(lambda))/lambda is a polynomial for k>=1. The ideal decoder B_k=q_{k-1}(A)F-transpose has range in P, satisfies

    ||B_k F-P||<=1/T_k(sigma)<=2 r^k,
    r=(1-s)/(1+s),
    ||B_k||<=(1+1/T_k(sigma))/s.

The zero eigenvalue is handled by B_k F=q(A)A, not by setting q(0) to zero. Indeed q_{k-1}(0)=k U_{k-1}(sigma)/(d T_k(sigma))>0. An error in g can therefore generate a hidden output component.

Let rho_k=T_k(sigma)/T_{k+1}(sigma). The Chebyshev recurrence gives rho_0=d/c, rho_k=1/(2sigma-rho_{k-1}), and0<rho_k<1. For g=F-transpose y, the iterate x_k=B_k y obeys

    x0=0, x1=g/c,
    x{k+1}=xk+rho_k*rho_{k-1}(xk-x{k-1})
              +(2rho_k/d)(g-Axk), k>=1.

Thus degree/iteration index k is correct. Exact integer powers establish2*r^8192<2^-51; the corresponding ideal gain is strictly below512. For every intermediate k>=1, |p_k|<=1 on the positive spectrum, hence ||B_k||<=2/s.

## Forced recurrence and every error insertion

Let the computed update differ from this exact recurrence by arbitrary full-state additive epsilon_j at iterate j, with x0 exactly zero and epsilon1 including the initialization. For N>=j>=1 the final error coefficient is exactly

    [T_j(sigma)/T_N(sigma)] U_{N-j}(Z).

This follows after multiplying the error at index k by T_k(sigma). It includes j=1 and j=N; the final-step factor is1. It does not assume local errors lie in the observable space.

The full A spectrum lies in[0,1], so the Z spectrum lies in[-1,sigma], including the hidden value sigma. For all l>=0, |U_l(z)|<=U_l(sigma) on that interval. Let theta>0 satisfy cosh(theta)=sigma. Then exp(-theta)=r and sinh(theta)=2s/(1-s²). Therefore

    ||[T_j(sigma)/T_N(sigma)]U_{N-j}(Z)||
       <=exp(theta)/sinh(theta)
       =(1+s)²/(2s)=G<256.

The bound uses cosh(jtheta)<=exp(jtheta), sinh((N-j+1)theta)<=exp((N-j+1)theta)/2 and cosh(Ntheta)>=exp(Ntheta)/2. Consequently final full-state arithmetic/action error is at most G*sum_j||epsilon_j||, including coherent hidden errors. Assuming epsilon0=0 is explicit; an erroneous x0 would need its own initial-condition term.

## Conditional action and update budgets

Suppose g is supplied with absolute error<=u=2^-67, every A action on the computed iterate has absolute error<=u, and the aggregate coefficient/rounding defect of each COMPLETE recurrence update is<=u. The latter includes every primitive operation and any rho/coefficient approximation; it is not a per-primitive budget. Since1/c<2 and2rho_k/d<5, initialization error is<=3u and every later local defect is<=11u. Conservatively counting N=8192 local terms gives

    total computed-versus-ideal error<256*8192*11*2^-67
       =11*2^-46<2^-42.

The strict inequalities follow from G<256. The controls do not establish these absolute oracle budgets for the actual weighted model.

For a declared data ball ||y||<=2, ideal iterate norm<=4/s. Adding the prefix error bound keeps every computed iterate strictly below2048. This bootstraps a uniform A-action contract on the state ball2048. A possible factorization is a forward F action with absolute error<=2^-68 on that ball, followed by an adjoint action with the same absolute error on data ball2049. The composed normal action error is<=2^-67 because ||F-transpose||<=1; the adjoint contract also covers initial data of norm<=2. These are required contracts, not actual implementations or certified runtimes.

A reference arithmetic implementation may validate each full-coordinate update against an Arb interval enclosing exact coefficients and current dyadic inputs. A coordinate defect<2^-80 gives vector defect<sqrt2640*2^-80<2^-74<2^-67 for n<=2640. This shows how to qualify the aggregate update budget; it does not make small-dimensional reference tests into an actual2640-dimensional oracle validation.

## Scope and downstream use

The ideal B_8192 supplies full-state operator conformance alpha<2^-51 and gain beta<512. Conditional implementation error below2^-42 would fit the C28 decoder slot. Acquisition/preparation/generator/timing/readout/noise/encoding assumptions in that slot remain separate. Actual forward and adjoint weighted actions, their domains and the actual implementation are still HOLD. No full Hankel is required by the recurrence, but no actual600-cell decoder runtime or physical precision is established by this theorem.

Development — no registry entry. Same-team mathematical review; external review PENDING; Physical Promotion=0.
