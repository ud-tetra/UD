"""Endpoint quartic certificate: Arb enclosures and exact rational budgets.
Floating eigensolvers propose congruences only; Arb accepts positivity.
Run: PYTHONPATH=../math-deps python3 certify_endpoint.py
"""
import json
from pathlib import Path
from endpoint_budget import budget
from fractions import Fraction as F
import numpy as np
from geometry import *
from critical_interval_certificate import certificate
from curved_mode_model import model

def positive(A):
 vals,V=np.linalg.eigh(np.array(A.tolist(),float))
 T=arb_mat([[point(str(t)) for t in row] for row in V/np.sqrt(abs(vals))])
 B=T.transpose()*A*T
 margins=[B[i,i].lower()-sum(B[i,j].abs_upper() for j in range(B.ncols()) if i!=j) for i in range(B.nrows())]
 assert all(t>0 for t in margins)
 # Strict diagonal dominance makes B positive; T is invertible since B is.
 return {'dimension':A.nrows(),'strict_positive_margin':bounds(min(margins)),
         'method':'192-bit Arb congruence; floating orthonormal eigenvectors propose decimal rational T only',
         'transformation':[[str(T[i,j].mid()) for j in range(T.ncols())] for i in range(T.nrows())]}


def main():
 vlev=[arb(1),rho/3,(1+D0)/3,4*(1+D0)/(3*rho)];ell=16*(10+D0)/9
 v=[vlev[len(t)-1]/ell.sqrt() for t in nodes]
 H0=diag([4*v[i]*v[j] for i,j in edges])-kc*Cmat.transpose()*Cmat
 G=Z.transpose()*Z;PZ=Z*G.inv()*Z.transpose()
 # Kernel identity is inherited exactly. Arb residual enclosure is an additional replay check, not an identity proof.
 residual=H0*Z;assert all(residual[i,j].contains(0) for i in range(28) for j in range(3))
 scalar=positive(H0+PZ-diag([arb(F(1,50).numerator)/50]*28))
 znorm=positive(50*diag([arb(1)]*3)-G)
 assert kc>arb('3/80') and kc<arb('1/25')
 assert min(v)>arb('1/5') and rho-2>arb('3/5')
 assert 4-arb(2).sqrt()>arb('5/2')
 g=model();quartic=certificate(g)
 # Derivative and polarization constants, proved without decimal rounding.
 assert F(24)**2*6<60**2
 assert F(24)**2*3<42**2
 assert 144+F(144,25)<150
 assert 144**2*6<360**2 and F(288,25)**2*3<20**2
 assert 62*F(3**3,6)==279
 assert 150*F(4**4,24)==1600
 fixtures=[budget(),budget(F(1,100000),F(1)),budget(F(100),F(3)),budget(F(1),F(1),F(1,10**16))]
 out={'status':'PASS','claim_bin':'DERIVED_CONDITIONAL','independent_review':'PENDING','physical_promotion':0,
 'precision_bits':192,'kernel_identity':'Inherited exact H0 Z=0; full Arb residual encloses zero',
 'fast_scalar_floor':{'lower_bound':'1/50','certificate':scalar},
 'critical_map_norm_squared':{'upper_bound':'50','certificate':znorm},
 'quartic_replay':quartic,'normal_relaxed_quartic_lower_coefficient':'N/200',
 'geodesic_derivative_bounds':{'M2':'max(a,25N)','M3':'62N','M4':'150N','M5':'380N'},
 'polarized_tensor_bounds':{'C3':'279N','C4':'1600N'},
 'full_normal_coercivity':'H-H_* >= (N/1600) d_g(x,orbit)^4 for d_g <= R_star',
 'budgets':fixtures,
 'verification_scope':'Analytic Taylor/jet proof in manuscript plus Arb scalar positive congruences, inherited directed-integer quartic replay and exact rational budget inequalities. No numerical orbit simulation or physical experiment.'}
 Path('ENDPOINT_QUARTIC_CERTIFICATE_v0.1.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'status':'PASS','scalar_margin':scalar['strict_positive_margin'],'Z_margin':znorm['strict_positive_margin'],'unit_budget':fixtures[0]},indent=2))
if __name__=='__main__':main()
