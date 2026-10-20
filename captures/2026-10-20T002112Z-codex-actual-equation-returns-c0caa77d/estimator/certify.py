"""Exact retained singular equation and phase gates for the two saved outputs."""
import argparse,json,os,tempfile,importlib.util
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpz_mat
from common import P,repo,freeze,sha,a,up,down,write_new,external_output
from numeric_math import encode
import records,estimator,phase

def fm(x):return fmpz_mat(np.asarray(x,dtype=object).tolist())
def squared_norm(x,bits):return F(sum(int(v)*int(v) for row in x.tolist() for v in row),1<<(2*bits))
def pair(x):return [str(x.numerator),str(x.denominator)]
def sq_arb(q):return a(pair(q)).sqrt()
def gram_squared(x,bits):
 G=fm(x).transpose()*fm(x);n=G.nrows()
 for j in range(n):G[j,j]-=1<<(2*bits)
 return squared_norm(G,2*bits)
def metrics(N,case):
 with np.load(case/'SVD_META.npz',allow_pickle=False) as z:s=z['singular'];vt=z['right_transpose']
 U=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
 with np.load(case/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift']
 assert U.shape==(8191,209) and vt.shape==(321,321) and s.shape==(321,) and T.shape==(209,209)
 assert np.all(np.isfinite(s)) and np.all(s[:-1]>=s[1:]) and np.all(s>=0)
 Ui,bu=encode(U);Vi,bv=encode(vt[:209,:].T.copy());si,bs=encode(s[:209].copy());Ti,bt=encode(T)
 gu=gram_squared(Ui,bu);gv=gram_squared(Vi,bv);vmat=fm(Vi);tmat=fm(Ti);eq=F(0);lag=F(0)
 for begin in range(0,8191,512):
  end=min(8191,begin+512);left=fm(N[begin:end])*vmat;right=fm(Ui[begin:end]*si[None,:]);bits=max(55+bv,bu+bs)
  residual=left*(1<<(bits-55-bv))-right*(1<<(bits-bu-bs));eq+=squared_norm(residual,bits)
 for begin in range(0,8189,512):
  end=min(8189,begin+512);left=fm(Ui[begin+2:end+2]);right=fm(Ui[begin:end])*tmat;bits=bu+bt
  residual=left*(1<<bt)-right;lag+=squared_norm(residual,bits)
 return {'etaU':up(sq_arb(gu)),'etaV':up(sq_arb(gv)),'xi':up(sq_arb(eq)),'sA':up(sq_arb(lag)),'proposed_smin':list(float(s[208]).as_integer_ratio()),'exact_squared':{'left_Gram_F':pair(gu),'right_Gram_F':pair(gv),'singular_equation_F':pair(eq),'raw_lag_F':pair(lag)},'matrix_shapes':{'Z':[8191,321],'U':[8191,209],'V':[321,209],'Sigma':[209,209]},'norm_scope':'Exact dyadic Frobenius norms upper bound required operator norms; no discarded-tail charge','readable':{'etaU':float(sq_arb(gu).upper()),'etaV':float(sq_arb(gv).upper()),'xi':float(sq_arb(eq).upper()),'sA':float(sq_arb(lag).upper()),'proposed_smin':float(s[208])}}

def inherited_equation():
 path=repo()/'captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation/certify.py';spec=importlib.util.spec_from_file_location('frozen_equation_implication',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);f,c=m.bound(repo());old=repo()/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase/primary/CERTIFICATE.json';C=c.aa(json.loads(old.read_text())['sketch']['per_62_vector_noise_multiplier_upper']);return m,c,C

def run(baseline,out):
 freeze();runs=json.loads((P/'RUN_EXECUTIONS.json').read_text());data=json.loads((P/'DATA_FREEZE.json').read_text());assert runs['data_freeze_sha256']==sha(P/'DATA_FREEZE.json');assert [r['case']for r in runs['rows']]==[r['case']for r in data['records']];m,c,C=inherited_equation();caps=json.loads((P/'inputs/EQUATION_CAPS.json').read_text())['quality_caps'];rows=[];setup=phase.target_setup()
 for source,datum,r in zip(records.recipes(),data['records'],runs['rows']):
  entry={'case':source['id'],'record_sha256':datum['record_sha256'],'execution_status':r['execution_status'],'learned_order':r.get('learned_order'),'old_rank209_reconstruction_verdict':'NO_GO_UNCHANGED_FROM_SOURCE_CERTIFICATE','old_sigma210_lower':source['sigma210_lower'],'physical_promotion':0}
  if r['execution_status']!='COMPLETED' or r.get('learned_order')!=209:entry['status']='HOLD_EXECUTION_OR_ORDER';rows.append(entry);continue
  try:
   case=P/'results'/r['case'];assert json.loads((case/'RUN.json').read_text())==r
   for name,h in r['numeric_witnesses'].items():assert sha(case/name)==h,name
   with tempfile.TemporaryDirectory(prefix='ud-adversarial-proof-') as td:
    raw=Path(td)/'record.i64le';actual=records.generate(baseline,raw,source);N,proj=estimator.project(raw);actual['projection']=proj;assert actual==datum
    measured=metrics(N,case);del N
   ph=phase.qualify(case/'PHASE_META.npz',case/'PHASE_PROPOSAL.npz',setup)
   overrides={k:measured[k]for k in ['etaU','etaV','xi','sA','proposed_smin']}
   for own,other in [('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:overrides[own]=ph['metrics'][other]
   gates={k:bool(a(overrides[k])<=a(caps[k]))for k in ['etaU','etaV','xi','sA','rho','h','eV','a']}
   floor_source=json.loads((P/'inputs/PARENT_ORDER.json').read_text());required_floor=a(floor_source['qth_sigma_lower'])-C*a([3,1<<49])-a(caps['singular_floor_debit']);gates['measured_singular_floor']=bool(required_floor>0 and a(measured['proposed_smin'])>=required_floor)
   implication=m.evaluate(repo(),c,C,[3,1<<49],overrides);gates['conditional_phase_implication']=implication['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION';gates['finite_saved_phase_quality']=ph['status']=='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY'
   entry.update(required_singular_floor_lower=down(required_floor),status='CERTIFIED_FINITE_ACTUAL_ESTIMATOR_EQ_AND_PHASE' if all(gates.values())else 'HOLD_ACTUAL_ESTIMATOR_EQ_OR_PHASE',gates=gates,measured=measured,phase=ph,conditional_implication=implication)
  except Exception as exc:entry.update(status='HOLD_CERTIFICATION_EXCEPTION',exception={'type':type(exc).__name__,'message':str(exc)},policy='Retain exception without precision/gate retry or replacement')
  rows.append(entry);print(json.dumps({'case':entry['case'],'status':entry['status'],'measurements':entry.get('measured',{}).get('readable'),'phase_error':entry.get('phase',{}).get('observed',{}).get('readable_maximum_circular_error_upper')}),flush=True)
 freeze();result={'status':'COMPLETE_TWO_FINITE_SAVED_OUTPUT_QUALIFICATIONS','protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'run_executions_sha256':sha(P/'RUN_EXECUTIONS.json'),'rows':rows,'new_estimator_calls_in_verifier':0,'old_reconstruction_no_go_unchanged':True,'uniform_floating_solver_success_claimed':False,'full_SVD_or_exact_spectrum_T_claimed':False,'phase_unit':'radians per TWO-step sample modulo2pi; primitive-frequency ambiguity modulo pi','external_review':'PENDING','physical_promotion':0};write_new(out/'CERTIFICATE.json',result)

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--baseline',required=True);p.add_argument('--out',required=True);q=p.parse_args();os.environ['UD_REPO']=str(Path(q.repo).resolve());out=external_output(q.out);out.mkdir(parents=True,exist_ok=False);run(Path(q.baseline).resolve(),out)
if __name__=='__main__':main()
