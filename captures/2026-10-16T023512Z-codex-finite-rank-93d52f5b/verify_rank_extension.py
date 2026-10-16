#!/usr/bin/env python3
"""Exact inequalities and rigorous replay of the inherited global solution tubes."""
from pathlib import Path
from fractions import Fraction
import json,hashlib
from flint import arb
from scaled_model import *
O=Path(__file__).resolve().parent;checks=[]
def check(name,value):
 assert bool(value),name;checks.append(name);print('PASS',name,flush=True)
check('diamond_support_four',all(sum(abs(a) for a in row)==4 for row in C))
counts=[sum(abs(C[d][e]) for d in range(18)) for e in range(28)]
check('maximum_diamond_incidence_three',max(counts)==3)
Ai=[[0]*15 for _ in range(15)]
for i,j in edges:
 b=(-1)**nodes[j].index(next(x for x in nodes[j] if x not in nodes[i]));Ai[i][j]=-b;Ai[j][i]=b
check('exact_inactive_hopping_square',all(-sum(Ai[i][k]*Ai[k][j] for k in range(15))==4*int(i==j)-int(i<4 and j<4) for i in range(15) for j in range(15)))
check('critical_stiffness_lower',kc>arb('3/80'))
check('finite_stiffness_upper',kc+arb('1/100000')<arb('1/25'))
check('inactive_positive_gap',rho>arb('37/10'))
# Exact rational constants; these do not depend on a floating estimate.
matter=Fraction(2,25)*(1-Fraction(1,2*40**2));mag=4*3*Fraction(1,25)*Fraction(1,32);remaining=matter-mag
check('matter_link_lower_3199_over_40000',matter==Fraction(3199,40000))
check('magnetic_upper_3_over_200',mag==Fraction(3,200))
check('normal_margin_exceeds_one_sixteenth',remaining==Fraction(2599,40000) and remaining>Fraction(1,16))
check('vacuum_unweighted_curl_gap',arb(2).sqrt()<arb('3/2'))
check('vacuum_frequency_margin',Fraction(5,2)*Fraction(3,80)==Fraction(3,32))
check('unit_color_radial_separation_over_twenty',Fraction(1,16)/(Fraction(71,5)*Fraction(1,100000))>20**2)
check('unit_vacuum_radial_separation_over_twenty_five',Fraction(3,32)/(Fraction(71,5)*Fraction(1,100000))>25**2)
inputs=json.loads((O/'CERTIFICATE_INPUTS_v0.1.json').read_text());ti=arb('1/200000')+ball(arb('1/200000'));rows=[]
for k in [1,2,3]:
 x=[point(a) for a in inputs['global_centres'][k-1]['centre']];cert=validate_scaled(x,ti);check('family_'+str(k)+'_global_contraction_replay',cert is not None)
 box=cert['X'];u=Z*col(box[:3])+ti*Y*col(box[3:28]);Xmax=arb('1/100000').sqrt()*maxupper(entries(u));Phmax=arb('1/100000').sqrt()*maxupper(entries(Cmat*u));f=[v0[i]+ti*box[28+i] for i in range(15)];fmin=min(a.lower() for a in f);lam=-rho+ti*box[43]
 check('family_'+str(k)+'_matter_denominator',fmin>arb('1/5'))
 check('family_'+str(k)+'_link_phase',Xmax<arb('1/40'))
 check('family_'+str(k)+'_diamond_phase',Phmax<arb('1/16'))
 check('family_'+str(k)+'_inactive_Rayleigh_gap',lam.upper()<arb('-37/10'))
 rows.append({'family_k':k,'max_link_phase_upper':bounds(Xmax.upper()),'max_diamond_phase_upper':bounds(Phmax.upper()),'matter_component_lower':bounds(fmin),'lambda_upper':bounds(lam.upper()),'global_contraction_upper':bounds(cert['q'].upper())})
r={'status':'PASS','type':'EXACT rational constructor inequalities plus inherited rigorous Arb interval-tube replay; nonlinear energy proof in manuscript','check_count':len(checks),'checks':checks,'region':'0<epsilon<=1/100000, epsilon=kappa/(r*N)-k_star','parameters':'every finite rank r>=2, N>0,a>0','quadratic_energy_convention':'coefficient of t^2 in the fixed-norm rotating energy, not the raw second derivative','one_color_lower_bound':'a||e||^2+(17/10)||Q||^2+(N/16)||beta||^2, in the P=0 matter-aligned gauge','stronger_beta_margin':'(2599/40000)N','reduced_color_squared_frequency_lower':'a*N/16','vacuum_squared_frequency_lower':'3*a*N/32','unit_normalization_separation':{'parameters':'a=N=1; all finite ranks','color_frequency_over_radial_soft':'>20','vacuum_frequency_over_radial_soft':'>25'},'full_rank_conclusion':'six balanced branches are nonlinearly orbitally stable for every finite r on the certified interval; twelve and eight saddle embeddings remain unstable','endpoint':'at epsilon=0 use the inherited positive scalar quartic; the six branches coalesce','linear_slice_warning':'color and vacuum oscillator lists precede the residual global U(r-1) moment-map constraint and quotient; no free-mode count on the final singular quotient is asserted','limits':['Sufficient coefficient interval, not maximal','No explicit nonlinear perturbation or attraction radius','No uniform nonlinear neighborhood in r or epsilon down to zero','No full higher-rank equilibrium classification or exact finite-offset color spectrum','No physical correspondence or empirical result'],'replayed_families':rows,'physical_promotion':0,'independent_review':'PENDING'}
(O/'FINITE_RANK_CERTIFICATE_v0.1.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':'PASS','checks':len(checks),'normal_margin':str(remaining)},indent=2))
