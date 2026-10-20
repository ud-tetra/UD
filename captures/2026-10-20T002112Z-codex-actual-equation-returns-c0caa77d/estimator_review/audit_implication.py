"""Independent source-field and conditional implication arithmetic, no fits/imports."""
import json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
read=lambda p:json.loads(Path(p).read_text())
def f(q):return F(int(q[0]),int(q[1]))
def a(q):
 if not isinstance(q,F):q=f(q)
 return arb(fmpq(q.numerator,q.denominator))
def pair(q):return [str(q.numerator),str(q.denominator)]
def up(v):return [int((arb(v.upper())*(1<<180)).ceil().unique_fmpz()),1<<180]
def compare(v,p):assert abs(v-a(p))<a([1,1<<170])
def evaluate(g,C,u,m,o):
 etaU,etaV,rho=[a(g[k])for k in ['etaU','etaV','rho']];assert 0<=etaU<1 and 0<=etaV<1 and 0<=rho<1
 noise=a([3,1<<49]);floor=a(o['qth_sigma_lower'])-C*noise-a([1,1<<41]);assert floor>0 and a(g['proposed_smin'])>=floor
 # Stable algebraically equivalent form of Procrustes distance.
 z=((a(u['baseline_low_rank_residual_upper'])+C*noise)*(1+etaV).sqrt()+a(g['xi']))/(a(g['proposed_smin'])*(1-etaU).sqrt());assert 0<=z<1
 d=z*(2/(1+(1-z*z).sqrt())).sqrt();beta=a(u['deleted_two_rows_beta_lower']);assert beta>d
 shift=(a(u['comparison_shift_residual_upper'])+d*(1+a(u['comparison_shift_norm_upper']))+a(g['sA'])/(1-etaU).sqrt())/(beta-d)
 e0=a(m['basis_orthogonality_upper']);k0=((1+e0)/(1-e0)).sqrt();ka=((1+etaU)/(1-etaU)).sqrt();hinv=a(m['source_inverse_norm_upper'])/(1-a(m['source_inverse_residual_upper']));eigen=a(g['eV'])*a(g['h'])/(1-rho)
 radius=hinv*(a(m['intertwining_residual_upper'])+k0*a(m['source_reduction_norm_upper'])*(shift+ka*eigen));half=a(m['minimum_target_chord_lower'])/2;angle=radius.asin()+a(g['a'])
 assert radius<1
 status='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'if 2*radius<a(m['minimum_target_chord_lower']) and angle<half else 'HOLD_DISKS_NOT_STRICTLY_DISJOINT'
 return {'offspan_sine_upper':z,'polar_distance_upper':d,'shift_distance_upper':shift,'eigenvalue_radius_upper':radius,'phase_error_upper':angle,'phase_matching_margin_lower':half-angle},floor,status

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--producer',required=True);ap.add_argument('--certificate',required=True);q=ap.parse_args();repo=Path(q.repo);p=Path(q.producer);freeze=read(P/'IMPLICATION_AUDIT_FREEZE.json');assert sha(__file__)==freeze['code_sha256'];base=repo/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase';u=read(base/'inputs/PARENT_UNIFORM.json');m=read(base/'inputs/PARENT_PHASE.json')['metrics'];o=read(base/'inputs/PARENT_ORDER.json');C=a(read(base/'primary/CERTIFICATE.json')['sketch']['per_62_vector_noise_multiplier_upper']);caps=read(p/'inputs/EQUATION_CAPS.json')['quality_caps'];cert=read(q.certificate);rows=[]
 assert read(p/'inputs/PARENT_ORDER.json')==o
 assert read(p/'inputs/SOURCE_PHASE.json')==read(base/'inputs/PARENT_PHASE.json')
 for row in cert['rows']:
  if 'measured'not in row:rows.append({'case':row['case'],'status':'RETAINED_HOLD_NO_MEASUREMENTS'});continue
  g={k:row['measured'][k]for k in ['etaU','etaV','xi','sA','proposed_smin']}
  for k,name in [('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:g[k]=row['phase']['metrics'][name]
  gates={k:f(g[k])<=f(caps[k])for k in ['etaU','etaV','xi','sA','rho','h','eV','a']}
  for k,value in gates.items():assert value==row['gates'][k]
  values,floor,status=evaluate(g,C,u,m,o);assert status==row['conditional_implication']['status'];assert row['gates']['measured_singular_floor']
  for k,value in values.items():compare(value,row['conditional_implication'][k])
  compare(floor,row['required_singular_floor_lower'])
  rows.append({'case':row['case'],'status':'PASS_INDEPENDENT_SOURCE_FIELD_AND_EXPRESSION_AUDIT','fixed_caps':gates,'fixed_caps_all_pass':all(gates.values()),'conditional_measured_pointwise_status':status,'finite_list_status':row['phase']['observed']['status'],'overall_actual_status_unchanged':row['status'],'independent_values':{k:up(v)for k,v in values.items()}})
 out={'status':'PASS_INDEPENDENT_SOURCE_EXPRESSION_AUDIT','rows':rows,'freeze_sha256':sha(P/'IMPLICATION_AUDIT_FREEZE.json'),'scope':'Same measured dyadic bounds checked against pinned source fields by independent stable algebra; source H/full-factor proofs inherited, not rerun; fixed cap failure cannot be overridden by pointwise or direct finite matching.','new_estimator_calls':0,'physical_promotion':0,'external_review':'PENDING'};target=P/'IMPLICATION_AUDIT_RECEIPT.json';assert not target.exists();target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'rows':[{k:r[k]for k in ['case','fixed_caps_all_pass','conditional_measured_pointwise_status']}for r in rows]}))
if __name__=='__main__':main()
