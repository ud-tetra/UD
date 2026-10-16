#!/usr/bin/env python3
"""Constructor certificate: a scalar Hessian floor and exact nonlinear constants."""
from pathlib import Path
from fractions import Fraction as F
import json
from flint import fmpz_mat,fmpz_poly
from scaled_model import *
O=Path(__file__).resolve().parent;checks=[]
def check(name,value):
 assert bool(value),name;checks.append(name);print('PASS',name,flush=True)
cap=arb('1/100000');ti=cap/2+ball(cap/2)
inputs=json.loads((O/'CERTIFICATE_INPUTS_v0.1.json').read_text());centre=[point(a) for a in inputs['global_centres'][0]['centre']];global_cert=validate_scaled(centre,ti)
check('global_balanced_tube',global_cert is not None)
x=global_cert['X'];u=Z*col(x[:3])+ti*Y*col(x[3:28]);f=[v0[i]+ti*x[28+i] for i in range(15)]
check('positive_matter_denominators',min(v.lower() for v in f)>arb('1/5'))
check('link_phase_bound',cap.sqrt()*maxupper(entries(u))<arb('1/40'))
check('diamond_phase_bound',cap.sqrt()*maxupper(entries(Cmat*u))<arb('1/16'))
check('active_eigenvalue_upper',(-rho+ti*x[43]).upper()<arb('-37/10'))
check('stiffness_upper',kc+cap<arb('1/25'))
check('maximum_node_degree_four',max(sum(abs(a) for a in row) for row in R)==4)
check('diamond_four_edges',all(sum(abs(a) for a in row)==4 for row in C))
check('edge_diamond_incidence_three',max(sum(abs(C[d][e]) for d in range(18)) for e in range(28))==3)
Tbase=[[0]*15 for _ in range(15)]
for i,j in edges:Tbase[i][j]=Tbase[j][i]=1
p=fmpz_poly([0,1]);check('exact_unsigned_hopping_polynomial',fmpz_mat(Tbase).charpoly()==p**5*(p-2)**3*(p+2)**3*(p**4-16*p**2+24))
check('nonperron_hopping_below_three',(8-2*D0).sqrt()<3)
check('ground_gap_three_fifths',F(37,10)-F(31,10)==F(3,5))
check('matter_phase_shear_below_one_eighth',arb(2).sqrt()*arb('5/3')*arb('1/20')<arb('1/8'))
check('completed_square_norm_factor_two',1+2*F(1,8)**2<2)
check('scalar_floor_below_matter_and_color_floors',F(1,200000)<F(3,10) and F(1,200000)<F(1,32))
check('third_matter_derivative_below_sixty',24*arb(6).sqrt()<60)
check('third_magnetic_geometry_below_forty_two',24*arb(3).sqrt()<42)
check('global_third_derivative_below_sixty_two',60+F(42,25)<62)
check('global_second_derivative_below_twenty_five',24+F(12,25)<25)
cells=64;rows=[]
for j in range(cells):
 tm=cap*arb(fmpq(2*j+1,2*cells));cell=tm+ball(cap/(2*cells));xc=refine_scaled(centre,tm);rc=validate_scaled(xc,cell)
 check('cell_'+str(j)+'_contraction',rc is not None)
 check('cell_'+str(j)+'_nested_in_global_tube',all((rc['X'][i]-centre[i]).abs_upper()<global_cert['r'][i].lower() for i in range(44)))
 A,B,D,*_=scaled_hessians(rc['X'],cell);Di=certified_inverse(D)
 Tr=A-B*Di*B.transpose()-diag([arb(2)]*28)
 Fast=Y.transpose()*(H0+cell*Tr)*Y;Fi=certified_inverse(Fast)
 Cr=Z.transpose()*Tr*Z-cell*Z.transpose()*Tr*Y*Fi*Y.transpose()*Tr*Z
 cr=congruence(Cr);check('cell_'+str(j)+'_phase_Hessian_minus_two_epsilon_positive',cr is not None and cr['inertia']==0)
 rows.append({'cell':j,'interval':[str(F(j,100000*cells)),str(F(j+1,100000*cells))],'contraction_upper':bounds(rc['q'].upper())})
examples=[]
for ep in [F(1,100000),F(1,1000000)]:
 # Example a=N=1. All entries except delta are exact rational values.
 m=ep/2;J=F(25);L=F(62);radius=3*m/L;barrier=m*radius**2/2;delta=arb(str(radius))*arb(str(m/(2*J))).sqrt()
 examples.append({'a':'1','N':'1','epsilon':str(ep),'m':str(m),'R':str(radius),'barrier_B':str(barrier),'initial_radius_delta_enclosure':bounds(delta,30)})
r={'status':'PASS','type':'EXACT rational and integer checks plus 192-bit Arb interval certificate; constructor verification only','check_count':len(checks),'checks':checks,'parameter_region':'every fixed finite rank r>=1, a,N>0, 0<epsilon<=1/100000; epsilon=kappa/(r*N)-k_star','scalar_phase_hessian_lower':'C_phase > 2*epsilon*I_28 after eliminating normalized real common matter variations','new_balanced_parameter_cells':cells,'precision_bits':ctx.prec,'full_orbit_normal_quadratic_lower':'Q(v)>=m||v||_g^2, m=min(a,N*epsilon)/2','metric':'Product of Frobenius bi-invariant link metrics, Frobenius Euclidean electric metrics, and real round metrics on the unit spheres q=psi/sqrt(N), w=bar(chi)/sqrt(N)','global_second_geodesic_derivative_bound':'J=max(a,25*N)','global_third_geodesic_derivative_bound':'L=62*N','certified_outer_tube_radius':'R=3*m/(62*N)','energy_barrier':'B=m*R^2/2','sufficient_initial_ball':'delta=R*sqrt(m/(2*J)); d_g(x0,orbit)<=delta implies DeltaH<=B/2 and d_g(x(t),orbit)<R for all t','general_target_radius':'for 0<eta<=R, delta(eta)=eta*sqrt(m/(2*J)) traps d_g(x(t),orbit)<eta','energy_sublevel_condition':'d_g(x0,orbit)<R and DeltaH<B suffice even outside the smaller guaranteed ball','uniformity':'Constants hold for every finite rank in the declared Frobenius metric; no infinite-rank dynamical limit is asserted','examples':examples,'cells':rows,'scope_limits':['Explicit sufficient metric radii and local energy barrier, not maximal basin or nearest-saddle energy','Not a per-entry or componentwise perturbation budget','epsilon=0 excluded; quadratic floor degenerates there','No attraction, nonlinear mode independence or smooth final quotient claim','Frozen action and inherited stationary/normal certificates are explicit dependencies','No physical units, experimental samples or physical correspondence'],'independent_review':'PENDING','physical_promotion':0}
(O/'NONLINEAR_ENERGY_BARRIER_CERTIFICATE_v0.1.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(checks),'new_parameter_cells':cells,'examples':examples},indent=2))
