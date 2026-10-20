"""Conditional input-to-projector/phase region. No actual solver, raw record or factor loading."""
import argparse,hashlib,json,os,resource,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,fmpq,ctx
P=Path(__file__).resolve().parent
OLD='captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase'
BASE='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
CAPS='captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation/FREEZE.json'
ctx.prec=512;GRID=(None,*range(20,101))
def req(x,s):
 if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fr(p):return F(int(p[0]),int(p[1]))
def pair(x):return [str(x.numerator),str(x.denominator)]
def aa(x):return arb(fmpq(x.numerator,x.denominator))
def up(x):return pair(F(int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180))
def down(x):return pair(F(int((arb(x.lower())*(1<<180)).floor().unique_fmpz()),1<<180))
def guard(arg):
 lex=Path(os.path.abspath(arg));out=lex.resolve();protected={P,P.resolve()}
 for p in (P,*P.parents):
  if(p/'MANIFEST.json').is_file():protected.update((p.absolute(),p.resolve()))
 for x in (lex,out):req(all(x!=p and p not in x.parents and x not in p.parents for p in protected),'protected output or ancestor')
 req(not out.exists(),'new output required');return out

def bind(repo):
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():req(sha(P/n)==h,'frozen local changed '+n)
 s=json.loads((P/'SOURCE_BINDINGS.json').read_text())
 for row in s['pins']:req(sha(repo/row['path'])==row['sha256'],'source changed '+row['path'])
 return f

def source(repo):
 u=json.loads((repo/OLD/'inputs/PARENT_UNIFORM.json').read_text());m=json.loads((repo/OLD/'inputs/PARENT_PHASE.json').read_text())['metrics'];o=json.loads((repo/BASE/'estimator/inputs/PARENT_ORDER.json').read_text());c=json.loads((repo/OLD/'primary/CERTIFICATE.json').read_text())['sketch'];caps=json.loads((repo/CAPS).read_text())['quality_caps']
 out={k:fr(v)for k,v in caps.items()};out.update(C=fr(c['per_62_vector_noise_multiplier_upper']),r=fr(u['baseline_low_rank_residual_upper']),s0=fr(o['qth_sigma_lower']),tail0=min(fr(o['qplus1_sigma_upper']),fr(u['baseline_low_rank_residual_upper'])),cutoff=fr(o['source_precision_cutoff']),beta=fr(u['deleted_two_rows_beta_lower']),lag0=fr(u['comparison_shift_residual_upper']),M0=fr(u['comparison_shift_norm_upper']),eta0=fr(m['basis_orthogonality_upper']),hD0=fr(m['source_inverse_norm_upper']),rhoD=fr(m['source_inverse_residual_upper']),dD=fr(m['source_reduction_norm_upper']),LJ=fr(m['intertwining_residual_upper']),sep=fr(m['minimum_target_chord_lower']),delta0=F(3,1<<49),quantum=F(1,1<<48))
 return out

def evaluate(zeta,c):
 req(zeta>=0,'nonnegative additional sketch perturbation required');req(c['C']>0,'positive sketch multiplier required')
 req(0<=c['etaU']<1 and 0<=c['etaV']<1 and 0<=c['eta0']<1 and 0<=c['rho']<1 and 0<=c['rhoD']<1,'valid Gram/inverse premises required')
 req(all(c[k]>=0 for k in ('xi','sA','eV','a','r','delta0','singular_floor_debit','lag0','M0','hD0','dD','LJ'))and c['h']>0,'nonnegative quality/source bounds required')
 noise=c['C']*c['delta0']+zeta;e=c['r']+noise;floor=c['s0']-noise-c['singular_floor_debit'];low=c['s0']-noise;tail=c['tail0']+noise;margin=min(low-c['cutoff'],c['cutoff']-tail);nu=zeta/c['C'];total=c['delta0']+nu
 out={'additional_sketch_radius':pair(zeta),'future_proposed_singular_floor_required':pair(floor),'status':'HOLD_SOURCE_OR_PHASE_MARGIN','additional_raw_radius_conditional_on_projection':pair(nu),'additional_encoded_ball_only_zero':nu<c['quantum'],'total_raw_radius':pair(total),'total_encoded_local_patternset_unchanged':2*c['quantum']**2<=total*total<3*c['quantum']**2,'exact_data_singular_q_lower':pair(low),'exact_data_singular_qplus1_upper':pair(tail),'exact_order_209_at_cutoff':margin>0,'required_computed_singular_error_strictly_below':None if margin<=0 else pair(margin),'future_output_quality_must_be_measured':True,'uniform_solver_success':False}
 if floor<=0:out['status']='HOLD_POSITIVE_PROPOSED_FLOOR';return out
 t=(aa(e)*(1+aa(c['etaV'])).sqrt()+aa(c['xi']))/(aa(floor)*(1-aa(c['etaU'])).sqrt())
 if not 0<=t<1:out['status']='HOLD_PROJECTOR_GAP';return out
 d=t*(2/(1+(1-t*t).sqrt())).sqrt();beta=aa(c['beta'])
 out.update(projector_distance_upper=up(t),Procrustes_distance_upper=up(d),readable_projector_upper=float(t.upper()),readable_Procrustes_upper=float(d.upper()))
 if not beta>d:out['status']='HOLD_DELETED_ROW_MARGIN';return out
 b=(aa(c['lag0'])+aa(c['sA'])/(1-aa(c['etaU'])).sqrt()+d*(1+aa(c['M0'])))/(beta-d)
 kA=((1+aa(c['etaU']))/(1-aa(c['etaU']))).sqrt();k0=((1+aa(c['eta0']))/(1-aa(c['eta0']))).sqrt();hD=aa(c['hD0'])/(1-aa(c['rhoD']));Delta=aa(c['eV'])*aa(c['h'])/(1-aa(c['rho']));R=hD*aa(c['LJ'])+k0*hD*aa(c['dD'])*(b+kA*Delta);half=aa(c['sep'])/2
 ls_exact=d*(1+1/beta)/(beta-d)+d*aa(c['lag0'])/(beta-d)**2
 out.update(aligned_shift_distance_upper=up(b),polar_similarity_condition_upper=up(kA),unpolarized_deleted_basis_sigma_lower=down((1-aa(c['etaU'])).sqrt()*(beta-d)),exact_aligned_LS_map_change_upper=up(ls_exact),reference_exact_LS_to_comparison_upper=up(aa(c['lag0'])/beta),target_disk_radius_upper=up(R),source_half_chord_lower=down(half))
 if not R<1:out['status']='HOLD_DISK_ORIGIN';return out
 angle=R.asin()+aa(c['a']);out.update(phase_error_upper=up(angle),matching_margin_lower=down(half-angle),readable_phase_upper=float(angle.upper()),readable_matching_margin_lower=float((half-angle).lower()))
 if margin>0 and R<half and angle<half:out['status']='CERTIFIED_CONDITIONAL_GAUGE_ALIGNED_REGION'
 return out

def run(repo,out):
 bind(repo);c=source(repo);start=time.perf_counter();out.mkdir(parents=True,exist_ok=False);rows=[]
 for k in GRID:
  row=evaluate(F(0)if k is None else F(1,1<<k),c);row['grid_k']=k;rows.append(row)
 positives=[r for r in rows if r['grid_k']is not None and r['status']=='CERTIFIED_CONDITIONAL_GAUGE_ALIGNED_REGION'];chosen=positives[0]if positives else None
 result={'artifact_type':'CONDITIONAL_GAUGE_ALIGNED_INPUT_REGION','status':'COMPLETE_FROZEN_CONDITIONING_GRID','freeze_sha256':sha(P/'FREEZE.json'),'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'constants':{k:pair(v)for k,v in c.items()},'original_quality_caps_unchanged':True,'rows':rows,'largest_positive_grid_certified':chosen,'source_rank_and_frame_proofs_inherited':True,'future_output_quality_measured_or_HOLD_required':True,'new_estimator_calls':0,'new_raw_records':0,'new_retained_factor_copies':0,'uniform_backend_success':False,'not_a_transfer_into_prior_2minus49_factor_box':True,'old_campaign_relabelled':False,'external_review':'PENDING','physical_promotion':0}
 bind(repo);(out/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');(out/'RESOURCE.json').write_text(json.dumps({'elapsed_seconds':time.perf_counter()-start,'process_max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Host-specific conditional arithmetic only; no estimator/Hankel benchmark'},indent=2)+'\n');print(json.dumps({'rows':len(rows),'selected_k':None if chosen is None else chosen['grid_k'],'selected_phase_upper':None if chosen is None else chosen.get('readable_phase_upper'),'additional_encoded_ball_only_zero':None if chosen is None else chosen['additional_encoded_ball_only_zero']}))

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(Path(a.repo).resolve(),guard(a.out))
if __name__=='__main__':main()
