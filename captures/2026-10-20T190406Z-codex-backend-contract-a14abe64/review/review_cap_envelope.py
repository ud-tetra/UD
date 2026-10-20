"""Independent original-cap endpoint arithmetic and analytic monotonicity premises.
No solver, raw record or actual output factor is read. Source proof premises inherited.
"""
import argparse,hashlib,importlib.util,json
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx,fmpq
ctx.prec=512
P=Path(__file__).resolve().parent
J=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
q=lambda p:F(int(p[0]),int(p[1]))
def aa(p):
 v=q(p)if not isinstance(p,F)else p
 return arb(fmpq(v.numerator,v.denominator))
def up(x):return [int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180]
def down(x):return [int((arb(x.lower())*(1<<180)).floor().unique_fmpz()),1<<180]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--producer',required=True);ap.add_argument('--result',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();repo=Path(a.repo);producer=Path(a.producer);result=Path(a.result);out=Path(a.out);assert not out.exists();f=J(P/'CAP_ENVELOPE_REVIEW_FREEZE.json');assert sha(__file__)==f['code_sha256']
 for name,h in f['local_inputs'].items():assert sha(P/name)==h
 for name,h in f['repository_sources'].items():assert sha(repo/name)==h
 prior=J(P/'CERTIFICATE.json');root=J(result/'CERTIFICATE.json');pf=J(producer/'FREEZE.json')
 for name,h in pf['local_files'].items():assert sha(producer/name)==h
 for name,h in pf['repository_files'].items():assert sha(repo/name)==h
 old=repo/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase';u=J(old/'inputs/PARENT_UNIFORM.json');source=J(old/'inputs/PARENT_PHASE.json')['metrics'];caps=J(producer/'inputs/EQUATION_CAPS.json')['quality_caps'];g={key:aa(caps[key])for key in ['etaU','etaV','xi','sA','rho','h','eV','a']};C=aa(prior['noise_multiplier_upper']);delta=aa(prior['noise_radius']);smin=aa(prior['source_scale_floor']);r=aa(u['baseline_low_rank_residual_upper']);beta=aa(u['deleted_two_rows_beta_lower']);sigma=aa(u['comparison_shift_residual_upper']);M=aa(u['comparison_shift_norm_upper']);eta0=aa(source['basis_orthogonality_upper']);h0=aa(source['source_inverse_norm_upper']);rho0=aa(source['source_inverse_residual_upper']);d0=aa(source['source_reduction_norm_upper']);LJ=aa(source['intertwining_residual_upper']);sep=aa(source['minimum_target_chord_lower']);signs={}
 for name,value in [('C',C),('delta',delta),('source_r',r),('source_sigma',sigma),('source_M',M),('source_eta0',eta0),('source_h0',h0),('source_rho0',rho0),('source_d0',d0),('source_LJ',LJ),('source_sep',sep),*g.items()]:
  assert value>=0,name;signs[name]=True
 assert eta0<1 and rho0<1 and h0>0 and g['etaU']<1 and g['etaV']<1 and g['rho']<1 and g['h']>0 and smin>0 and sep>0 and beta>0
 t=((r+C*delta)*(1+g['etaV']).sqrt()+g['xi'])/(smin*(1-g['etaU']).sqrt());assert 0<=t<1
 D=t*(2/(1+(1-t*t).sqrt())).sqrt();assert 0<=D<beta
 b=(sigma+g['sA']/(1-g['etaU']).sqrt()+D*(1+M))/(beta-D);assert b>=0
 ka=((1+g['etaU'])/(1-g['etaU'])).sqrt();k0=((1+eta0)/(1-eta0)).sqrt();hD=h0/(1-rho0);Delta=g['eV']*g['h']/(1-g['rho']);R=hD*LJ+k0*hD*d0*(b+ka*Delta);assert 0<=R<1 and R<sep/2
 angle=R.asin()+g['a'];assert 0<=angle<sep/2
 # Conservatively report rational3.612e-7, proven above the validated interval upper.
 report=F(903,2500000000);assert angle<=aa(report)
 rootphase=root['conditional_phase_at_original_caps'];exact={'offspan_sine_upper':up(t),'polar_distance_upper':up(D),'shift_distance_upper':up(b),'eigenvalue_radius_upper':up(R),'phase_error_upper':up(angle),'phase_matching_margin_lower':down(sep/2-angle)}
 for key,value in exact.items():assert q(value)==q(rootphase[key]),key
 # Strict endpoint checks alone do not prove monotonicity. The source-bound analytic
 # proof is stated in CAP_ENVELOPE_THEOREM.md and separately reviewed by humans.
 output={'status':'PASS_INDEPENDENT_CONDITIONAL_CAP_ENVELOPE_AND_STRICT_MARGINS','producer_freeze_sha256':sha(producer/'FREEZE.json'),'producer_certificate_sha256':sha(result/'CERTIFICATE.json'),'independent_phase_bounds_exactly_match':True,'nonnegative_source_and_caps':signs,'strict_premises':{'source_Gram_and_inverse_debits_below1':True,'proposed_floor_positive':True,'t_below1':True,'beta_exceeds_polar_frame_distance':True,'R_below1':True,'R_below_half_chord':True,'phase_below_half_chord':True,'phase_below_3p612e_neg7':True},'validated_endpoint_bounds':exact,'reported_phase_upper':[str(report.numerator),str(report.denominator)],'phase_units':'radians per TWOstep modulo2pi; not SI or six-ratio error','counterexample_scope':'No fixed-implementation bug or uniform backend success asserted','monotonicity_scope':'Analytic proof for nonnegative quality metrics at fixed source constants and positive denominators; endpoint signs/margins independently checked here','source_proof_premises':'Inherited hash-bound; not independently rederived','new_estimator_calls':0,'new_raw_or_factor_copies':0,'external_review':'PENDING','physical_promotion':0}
 with out.open('x')as ff:json.dump(output,ff,indent=2);ff.write('\n')
 print(json.dumps({'status':output['status'],'readable_endpoint':float(aa(exact['phase_error_upper'])),'report':output['reported_phase_upper']}))
if __name__=='__main__':main()
