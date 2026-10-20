# Conditional saved-factor perturbation boxes

Development — no registry entry; Physical Promotion=0. All norms below are operator2norm unless F is explicitly shown. Z8191x321 is fixed. The two saved tuples U8191x209, V321x209, real diagonal Sigma209, T209x209 are fixed centers. The eigenbasis W, eigenvalue proposal Lambda, approximate inverse H and emitted phase list remain fixed. Let U'=U+EU, V'=V+EV, Sigma'=Sigma+ES, T'=T+ET, with ES real diagonal and ||EU||<=u, ||EV||<=v, ||ES||<=s, ||ET||<=t. These are separate typed internal coordinates; equal numerical radii do not identify their units or provenance.

Let p>=||U||, q>=||V||, z>=||Z||, d>=||Sigma||, a>=||T||, w>=||W|| and m=min diagSigma. Let etaU,etaV,xi,ell,e bound the source Gram defects, retained singular equation ZV-U Sigma, lag U[2:]-U[:-2]T and eigenpair TW-W Lambda, respectively. Then every tuple in the declared box satisfies

etaU' <= etaU+2pu+u²;
etaV' <= etaV+2qv+v²;
xi' <= xi+zv+du+ps+us;
ell' <= ell+(1+a)u+pt+ut;
e' <= e+wt;
min diagSigma' >= m-s.

Proof: Expand each expression and apply triangle inequality/submultiplicativity; row deletion is a contraction. For the singular equation, its change is Z EV-EU Sigma-U ES-EU ES. For lag, change is EU[2:]-EU[:-2]T-U[:-2]ET-EU[:-2]ET. The eigenpair change is ET W. Gram change is U^T EU+EU^T U+EU^T EU, with V analogous. A real diagonal perturbation changes each diagonal entry by at most s. Inverse/argument/emission diagnostics depend only on unchanged W,Lambda,H/list and stay identical. No assertion about what a rerun numerical eigensolver would return follows.

If all these envelopes satisfy the fixed source quality caps, minSigma' satisfies the original positive source floor, and the unchanged conditional source phase implication passes at these worst-case envelopes, it covers every tuple in this box. The implication is monotone on the valid nonnegative domain: t_subspace increases with Gram/equation envelopes and decreasing positive singular floor; polar distance increases with t_subspace; the deleted-row denominator decreases; remaining positive inverse/condition factors increase. Thus worst-case substituted envelopes suffice. In particular, use the inflated envelopes, not center values. Fixed direct phase-list accuracy is inherited, not a new extraction.

For lag-only u=t=epsilon, K=1+a+p and margin b=tau-ell>0, epsilon²+K epsilon<=b proves the unchanged lag cap tau=2^-34. The conservative continuous radius is 2b/[K+sqrt(K²+4b)]. A lag-only radius does not by itself preserve the other quality caps. The common full-quality grid box is an intersection of all conditions, not the lag-only budget.

Norm premises are source-bound: p<=sqrt(1+etaU), q<=sqrt(1+etaV), a<=||T||F, w<=||W||F. For exact Z=N/2^55, ||Z||<=||Z||F<=sqrt(8191*321)*max|N|/2^55, using the prior exact projection receipt. Maximum/minimum retained diagonal entries are exact saved values; they are not declared exact singular values of Z. All source-proof dependencies and original-noise radius3*2^-49 stay fixed; Z itself is not perturbed here.

The largest certified dyadic box on the declared grid is a sufficient certificate, not the actual maximal radius. Failure of a larger envelope proves insufficient certification, not existence of a failed tuple. No raw noise tolerance, solver conditioning/rounding branch map, unaliased/SI/six-ratio/native1893 or physical identification follows. The old Frobenius-route HOLD and reconstruction NO-GO remain unchanged.
