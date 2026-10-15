#!/usr/bin/env python3
"""Computer-assisted constructor certificate. No floating residual is accepted as proof."""
from pathlib import Path
import json,hashlib,time
from flint import fmpz_mat,fmpz_poly
from scaled_model import *
O=Path(__file__).resolve().parent;cap=arb('1/100000');ti=cap/2+ball(cap/2)
inputs=json.loads((O/'CERTIFICATE_INPUTS_v0.1.json').read_text());Ncells=inputs['cells_per_family'];assert Ncells==512 and inputs['region']==['0','1/100000'];bases=json.loads((O/'SECTOR_BASES_v0.1.json').read_text());sectors={n:sector_arrays(n,bases) for n in ['radial','angular']}
Dmap=Bmap*Cmat*Y;eye=arb_mat(18,18)
for i in range(18):eye[i,i]=1
fastmap=(eye-L*L.transpose()/Gamma)*Cmat*Y
Jn=arb_mat([[int(i==j)-fmpq(1,4) for j in range(4)] for i in range(4)])
sel={}
for d,(i,j,h,k) in enumerate(diamonds):
 if len(nodes[i])==1:sel.setdefault(tuple(a for a in nodes[k] if a not in nodes[i]),d)
def ceilint(a):return int(a.upper().ceil().fmpz())
def interval(a):return bounds(a,20)
Tbase=[[0]*15 for _ in range(15)]
for i,j in edges:Tbase[i][j]=Tbase[j][i]=1
poly=fmpz_mat(Tbase).charpoly();xpoly=fmpz_poly([0,1]);assert poly==xpoly**5*(xpoly-2)**3*(xpoly+2)**3*(xpoly**4-16*xpoly**2+24)
assert rho>arb('37/10') and lp>5 and Gamma>324
# The factorization gives exactly one positive eigenvalue above 3: rho.
# Other positive roots are 2 and sqrt(8-2 sqrt(10))<3.
assert (8-2*D0).sqrt()<3
from critical_interval_certificate import certificate,Q
from curved_mode_model import model
cert=certificate(model());AA=arb(fmpq(int(cert['A4']['lower_numerator']),Q)).union(arb(fmpq(int(cert['A4']['upper_numerator']),Q)));BB=arb(fmpq(int(cert['B4']['lower_numerator']),Q)).union(arb(fmpq(int(cert['B4']['upper_numerator']),Q)))
(O/'INHERITED_CRITICAL_CERTIFICATE_v0.1.json').write_text(json.dumps(cert,indent=2)+'\n');results=[];global_centres=[];start=time.monotonic()
for k in [1,2,3]:
 centre=[point(a) for a in inputs['global_centres'][k-1]['centre']];global_cert=validate_scaled(centre,ti);assert global_cert
 X=global_cert['X'];_,J,Gt=eval_scaled(X,ti,True,True);ds=entries(-(global_cert['A']*J).inv()*global_cert['A']*Gt)
 cc=col(X[3:28]);h=col(X[:3])+ti*Dmap*cc;dh=col(ds[:3])+Dmap*cc+ti*Dmap*col(ds[3:28]);Lh=sum(a.abs_upper()*a.abs_upper() for a in entries(dh)).sqrt();Lhi=ceilint(Lh)
 qk=AA+3*BB/4-BB/(2*k);r0=(Gamma/(4*qk)).sqrt();C_amp=ceilint(2*Lhi/r0+Lhi*Lhi*cap/(r0*r0))
 fast=entries(fastmap*cc);Fbound=ceilint(sum(a.abs_upper()*a.abs_upper() for a in fast).sqrt())
 u=Z*col(X[:3])+ti*Y*cc;du=Z*col(ds[:3])+Y*cc+ti*Y*col(ds[3:28]);phi=Cmat*u;dphi=Cmat*du
 Del=arb_mat(4,4);Delp=arb_mat(4,4)
 for (i,j),d in sel.items():Del[i,j]=Del[j,i]=phi[d,0]*phi[d,0]/(lp*lp);Delp[i,j]=Delp[j,i]=2*phi[d,0]*dphi[d,0]/(lp*lp)
 G=-Jn*Del*Jn/2;Gp=-Jn*Delp*Jn/2;tr=sum(G[i,i] for i in range(4));tp=sum(Gp[i,i] for i in range(4));Su=sum(G[i,i]*G[i,i] for i in range(4));Sp=2*sum(G[i,i]*Gp[i,i] for i in range(4));etap=Sp/(tr*tr)-2*Su*tp/(tr*tr*tr);C_eta=ceilint(etap.abs_upper())
 assert tr>4
 # Positivity and chart bounds hold for every true solution in this tube.
 f=[v0[i]+ti*X[28+i] for i in range(15)];assert min(a.lower() for a in f)>arb('1/5')
 assert cap.sqrt()*maxupper(entries(phi))<arb('1/16')
 assert 4*cap.sqrt()*maxupper(entries(u))<arb('1/10')
 lam=-rho+ti*X[43];assert lam<arb('-37/10')
 hnorm=sum(a*a for a in entries(h)).sqrt();assert hnorm>2 and hnorm<arb('5/2')
 assert C_amp<=25 and C_eta<=41 and Fbound<=297
 qmax=arb(0);incmax=arb(0);minspectral=arb('1e10');covered=0
 for j in range(Ncells):
  ec=cap*arb(fmpq(2*j+1,2*Ncells));width=cap/(2*Ncells);cell=ec+ball(width);xc=refine_scaled(centre,ec);rc=validate_scaled(xc,cell);assert rc,('cell contraction',k,j)
  # A child root is the unique global root: its entire enclosing box lies inside the global nominal box.
  assert all((rc['X'][i]-centre[i]).abs_upper()<global_cert['r'][i].lower() for i in range(44)),('nested child',k,j)
  assert configuration_inertia(rc['X'],cell)==k-1,('Morse',k,j)
  if k==1:
   for name,lo,hi in [('radial',arb('1417/100'),arb('71/5')),('angular',arb('149/50'),arb('1499/500'))]:
    low=sector_spectral(rc['X'],cell,lo,sectors[name]);high=sector_spectral(rc['X'],cell,hi,sectors[name]);assert low and high and low['negative']==0 and high['negative']==1,('spectral',j,name,low,high)
    minspectral=min(minspectral,low['margin'],high['margin'])
  qmax=max(qmax,rc['q']);incmax=max(incmax,rc['inc']);covered+=1
  if j%64==0:print('CERTIFIED',k,j,'/',Ncells,flush=True)
 row={'family_k':k,'oriented_branches':{1:6,2:12,3:8}[k],'global_contraction_norm_upper':interval(global_cert['q']),'global_self_map_ratio_upper':interval(global_cert['inc']),'child_cells':covered,'child_contraction_norm_upper':interval(qmax),'child_self_map_ratio_upper':interval(incmax),'scalar_Morse_index':k-1,'amplitude_h_derivative_bound':Lhi,'relative_radius_squared_error_coefficient':C_amp,'fast_loop_error_coefficient':Fbound,'real_fingerprint_bias_coefficient':C_eta,'trace_of_normalized_distance_Gram_lower':interval(tr.lower()),'leading_radius_squared_coefficient':interval(r0*r0),'minimum_spectral_margin':interval(minspectral) if k==1 else None}
 results.append(row);global_centres.append({'family_k':k,'centre':[a.mid().str(70,radius=False) for a in centre]});print('FAMILY_PASS',row,flush=True)
ratio_lo=arb('7085/1499');ratio_hi=arb('710/149');limit=1+4*AA/BB;freq_lo=ratio_lo.sqrt();freq_hi=ratio_hi.sqrt();flimit=limit.sqrt();assert max((freq_lo-flimit).abs_upper(),(freq_hi-flimit).abs_upper())<arb('1/200')
# Deterministic real-channel error proof constants.
assert arb('41/100000')+arb('9/500')<arb('1/24')
res={'status':'PASS','claim_type':'COMPUTER-ASSISTED DERIVED CONDITIONAL; constructor certificate, not independent review','parameter_region':'0 < epsilon <= 1/100000, epsilon=kappa/(r*N)-k_star','closed_regularized_region':'0 <= epsilon <= 1/100000','normalization':'Stationary states and observable errors: any N>0, finite r embeddings, a>0. Finite scalar mode bounds: a=N=r=1. Scalar Morse/stability: r=1, any a>0,N>0 after corresponding canonical scaling.','global_boxes':3,'parameter_cells_per_family':Ncells,'validated_child_boxes':3*Ncells,'spectral_sector_cut_tests':4*Ncells,'precision_bits':ctx.prec,'arithmetic':'python-flint Arb balls; polynomial remainders bounded by geometric tails; floating eigensolvers propose congruences only','stationary_variable_count':44,'global_ground_gap_lower':'3/5','matter_component_lower':'1/5','absolute_diamond_phase_upper':'1/16','critical_radius_bounds':'2 sqrt(epsilon) < R < (5/2) sqrt(epsilon)','uniform_relative_radius_squared_error':'|R^2/(Gamma*epsilon/(4*q_k))-1| <= 25 epsilon','uniform_fast_loop_error':'||(I-L L^T/Gamma) phi||_2 <= 297 epsilon^(3/2)','uniform_real_fingerprint_bias':'|eta_a-eta_k| <= 41 epsilon','oriented_phase_noise_sufficient':'||delta phi||_2 <= 5 sqrt(epsilon) guarantees nearest-P4 classification on 26 branch families','real_channel_noise_sufficient':'max of six labeled |delta Re z_d| <= epsilon/40 guarantees nearest-eta classification, after clipping to [-1,1]; overall sign remains invisible','soft_squared_coefficients':{'radial':['1417/100','71/5'],'angular':['149/50','1499/500'],'scope':'a=N=r=1; same interval; angular mode twice by exact symmetry'},'soft_squared_ratio_bounds':['7085/1499','710/149'],'soft_frequency_ratio_bounds':[interval(freq_lo.lower()),interval(freq_hi.upper())],'absolute_frequency_ratio_error_from_limit':'<1/200','families':results,'ground_spectrum_characteristic':str(poly),'scope_limits':['No claim that these tubes exhaust all stationary states at each finite offset','Full-rank finite-offset orbital stability of stable embeddings not certified here; stationary embeddings and readout bounds are','Finite mode-ratio bound fixes a=N=r=1; no uniform bound in arbitrary electric coefficient','No empirical data, physical correspondence or independent review'],'physical_promotion':0,'independent_review':'PENDING'}
(O/'FINITE_OFFSET_CERTIFICATE_v0.1.json').write_text(json.dumps(res,indent=2)+'\n')
print('CERTIFICATE_PASS',time.monotonic()-start,flush=True)
