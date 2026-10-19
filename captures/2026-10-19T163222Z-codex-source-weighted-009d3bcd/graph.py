"""Validated Riccati graph envelope under explicitly typed approximation premises."""
import json,argparse
from flint import arb
from common import P,freeze,a,up,down
def certify(mode,delta,nu):
 f=freeze();u=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());o=json.loads((P/'inputs/PARENT_ORDER.json').read_text());g=json.loads((P/'inputs/PR210_FREEZE.json').read_text())['gates'];w=json.loads((P/'WEIGHTS_CERTIFICATE.json').read_text())
 assert mode in f['modes'] and delta in f['deltas'] and nu in f['normal_ceilings']
 r=a(u['baseline_low_rank_residual_upper']);alpha=a(o['qth_sigma_lower'])-r
 eta0=a(w['source_Gram_defect_F_upper']);rho=a(w['right_inverse_residual_F_upper']);assert eta0<1 and rho<1
 M=(1+eta0).sqrt()*a(w['source_coefficient_F_upper'])
 eps=arb(0) if mode=='ideal' else a(g['full_SVD_error']);eta=arb(0) if mode=='ideal' else a(g['full_left_orthogonality'])
 eps_projected=eps*(arb(209).sqrt() if mode=='returned_operator_only' else 1)
 e=r+a(u['per_vector_noise_multiplier_upper'])*a(delta)+eps
 ef=r+a(u['per_vector_noise_multiplier_upper'])*a(delta)+eps_projected
 weighted=(a(w['baseline_weighted_F_upper'])+a(w['weighted_noise_multiplier_upper'])*a(delta))/((1-rho)*(1-eta0).sqrt())+eps_projected/alpha
 z=weighted+e*ef/(alpha*alpha);ac=(2*M*e+2*e*e)/(alpha*alpha);bc=e*(M+e)/(alpha*alpha)
 discriminant=(1-ac)**2-4*bc*z;assert ac<1 and discriminant>0
 root=2*z/(1-ac+discriminant.sqrt());x=a(up(root))
 selfmap=bool(z+ac*x+bc*x*x<x);contraction=bool(ac+2*bc*x<1);separation=bool(alpha>2*e)
 leading_lower=((alpha-e)**2-2*e*(M+e)*x)/(1+x*x);leading=bool(leading_lower>e*e)
 assert selfmap and contraction and separation and leading
 polar=eta/(1+(1-eta).sqrt());distance=x+2*polar
 beta=a(u['deleted_two_rows_beta_lower']);assert distance<beta
 J=(1+eta).sqrt()*(a(u['comparison_shift_residual_upper'])+distance*(1+a(u['comparison_shift_norm_upper'])))
 amin=(1-eta).sqrt()*(beta-distance);actual=(J*J+(a(nu)/amin)**2).sqrt()
 allowance=a(json.loads((P/'inputs/PUBLISHED_ALLOWANCE.json').read_text())['raw_shift_strict_upper_allowance_lower'])
 return {'mode':mode,'encoded_radius':delta,'normal_residual_ceiling':nu,'weighted_forcing_upper':up(weighted),'graph_tangent_F_upper':up(x),'basis_distance_F_and_operator_upper':up(distance),'graph_gates':{'selfmap':selfmap,'contraction':contraction,'spectral_separation':separation,'leading_subspace':leading},'deleted_sigma_lower':down(amin),'exact_LS_shift_upper':up(J),'returned_shift_upper':up(actual),'published_shift_allowance_sufficient':bool(actual<allowance),'readable':{'weighted_forcing_upper':float(weighted.upper()),'graph_tangent_upper':float(x.upper()),'exact_LS_shift_upper':float(J.upper()),'returned_shift_upper':float(actual.upper())},'no_uniform_solver_or_all_other_gate_success_claim':True,'physical_promotion':0}
def verify():
 f=freeze();rows=[certify(mode,d,nu) for mode in f['modes'] for d in f['deltas'] for nu in f['normal_ceilings']]
 return {'status':'CERTIFIED_SOURCE_WEIGHTED_ENCODED_BALL_GRAPH_BOUNDS','rows':rows,'scope':'Whole encoded radius through separately stated SVD quality and normal-residual premises. Only shift allowance sufficiency; no uniform solver or other seven gates success.','physical_promotion':0,'external_review':'PENDING'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');args=p.parse_args();r=verify();q=P/'GRAPH_CERTIFICATE.json'
 if args.replay:assert json.loads(q.read_text())==r
 else:assert not q.exists();q.write_text(json.dumps(r,indent=2))
 print(json.dumps({'status':r['status'],'rows':[{'mode':x['mode'],'delta':x['encoded_radius'],'normal':x['normal_residual_ceiling'],'readable':x['readable'],'sufficient':x['published_shift_allowance_sufficient']} for x in r['rows']]}),flush=True)
