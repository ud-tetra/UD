"""Source-bound retained singular-equation phase implication; no estimator fit."""
import argparse, hashlib, importlib.util, io, json
from pathlib import Path
from zipfile import ZipFile
from fractions import Fraction
import numpy as np
from flint import arb

P=Path(__file__).resolve().parent
OLD='captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def bound(repo):
    f=json.loads((P/'FREEZE.json').read_text())
    for name,h in f['local_files'].items():assert sha(P/name)==h,('local source changed',name)
    b=json.loads((P/'SOURCE_BINDINGS.json').read_text())
    for row in b['repository_files']:assert sha(repo/row['path'])==row['sha256'],('repository source changed',row['path'])
    for row in b['governance_attachments']:assert sha(repo/row['repository_path'])==row['sha256'],('governance source changed',row['repository_path'])
    spec=importlib.util.spec_from_file_location('inherited_phase_arithmetic',repo/OLD/'certify_v2.py')
    c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
    c.binding(repo)
    return f,c

def evaluate(repo,c,C,noise,overrides=None):
    f=json.loads((P/'FREEZE.json').read_text());g={k:c.aa(v) for k,v in f['quality_caps'].items()};ov={} if overrides is None else overrides
    q=ov.get('q',209);g.update({k:c.aa(v) for k,v in ov.items() if k!='q'})
    out={'noise_radius':noise,'status':'HOLD_INVALID_PREMISE','uniform_solver_success_claimed':False,'requires_measured_singular_floor':True}
    delta=c.aa(noise)
    if not(q==209 and delta>=0 and 0<=g['etaU']<1 and 0<=g['etaV']<1 and 0<=g['rho']<1 and g['h']>0 and all(g[k]>=0 for k in ['xi','sA','eV','a','singular_floor_debit'])):return out
    u=json.loads((repo/OLD/'inputs/PARENT_UNIFORM.json').read_text());m=json.loads((repo/OLD/'inputs/PARENT_PHASE.json').read_text())['metrics'];o=json.loads((repo/OLD/'inputs/PARENT_ORDER.json').read_text())
    r=c.aa(u['baseline_low_rank_residual_upper']);s0=c.aa(o['qth_sigma_lower']);e=r+C*delta
    required_floor=s0-C*delta-g['singular_floor_debit'];smin=g.get('proposed_smin',required_floor)
    if not(required_floor>0 and smin>=required_floor):out['status']='HOLD_PROPOSED_SINGULAR_FLOOR';return out
    t=(e*(1+g['etaV']).sqrt()+g['xi'])/(smin*(1-g['etaU']).sqrt())
    out.update(required_proposed_singular_floor_lower=c.down(required_floor),readable_required_singular_floor_lower=float(required_floor.lower()))
    if not(0<=t<1):out['status']='HOLD_SUBSPACE_GAP';return out
    d=(2-2*(1-t*t).sqrt()).sqrt();beta=c.aa(u['deleted_two_rows_beta_lower'])
    if not beta>d:out['status']='HOLD_DELETED_ROW_MARGIN';return out
    b=(c.aa(u['comparison_shift_residual_upper'])+g['sA']/(1-g['etaU']).sqrt()+d*(1+c.aa(u['comparison_shift_norm_upper'])))/(beta-d)
    eta0=c.aa(m['basis_orthogonality_upper']);k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+g['etaU'])/(1-g['etaU'])).sqrt();hD=c.aa(m['source_inverse_norm_upper'])/(1-c.aa(m['source_inverse_residual_upper']));dD=c.aa(m['source_reduction_norm_upper']);LJ=c.aa(m['intertwining_residual_upper'])
    Delta=g['eV']*g['h']/(1-g['rho']);R=hD*LJ+k0*hD*dD*(b+ka*Delta);sep=c.aa(m['minimum_target_chord_lower'])
    out.update(status=c.phase_decision(R,g['a'],sep),offspan_sine_upper=c.up(t),polar_distance_upper=c.up(d),shift_distance_upper=c.up(b),eigenvalue_radius_upper=c.up(R),source_half_chord_lower=c.down(sep/2),readable_half_chord_lower=float((sep/2).lower()))
    if R<1:
        angle=R.asin()+g['a'];out.update(phase_error_upper=c.up(angle),phase_matching_margin_lower=c.down(sep/2-angle),readable_phase_error_upper=float(angle.upper()),readable_matching_margin_lower=float((sep/2-angle).lower()))
    return out

def inherited_example(repo,c,C):
    base=repo/'captures/2026-10-19T134625Z-codex-uniform-output-73b6e18a/admission';fc=json.loads((base/'inputs/ACTUAL_SVD.json').read_text());ad=json.loads((base/'ACTUAL_ADMISSION.json').read_text());sf=json.loads((base/'FREEZE.json').read_text())
    assert sha(base/'inputs/ACTUAL_SVD.json')==sf['input_sha256']['ACTUAL_SVD.json']
    archive=repo/'captures/2026-10-19T132221Z-codex-rounding-replay-82e4a9b7/WITNESS_03.zip';member='results/legacy_gemm/SVD_META.npz'
    with ZipFile(archive) as z:body=z.read(member)
    digest=hashlib.sha256(body).hexdigest();assert digest==sf['actual_arrays_sha256'][member]==ad['bindings'][member]
    with np.load(io.BytesIO(body),allow_pickle=False) as z:s=z['singular']
    assert s.shape==(321,) and s.dtype==np.float64 and np.isfinite(s).all() and np.all(s[:-1]>=s[1:]) and np.all(s>=0)
    etaL=c.aa(fc['eta_left_upper']);etaR=c.aa(fc['eta_right_upper']);rfull=c.aa(fc['projection_error_upper'])+c.aa(fc['reconstruction_residual_upper']);smax=c.aa(float(s[0]).as_integer_ratio());smin=c.aa(float(s[208]).as_integer_ratio())
    xi=rfull*(1+etaR).sqrt()+(1+etaL).sqrt()*smax*etaR
    caps=json.loads((P/'FREEZE.json').read_text())['quality_caps'];metrics=ad['rows'][0]['metrics'];assert all(ad['rows'][0]['gates'].values())
    override={'etaU':c.up(etaL),'etaV':c.up(etaR),'xi':c.up(xi),'proposed_smin':c.down(smin)}
    for own,old in [('sA','raw_shift_residual'),('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:override[own]=metrics[old]
    gates={'order209':fc['learned_order']==209,'etaU':bool(etaL<=c.aa(caps['etaU'])),'etaV':bool(etaR<=c.aa(caps['etaV'])),'xi':bool(xi<=c.aa(caps['xi']))}
    for k in ['sA','rho','h','eV','a']:gates[k]=bool(c.aa(override[k])<=c.aa(caps[k]))
    row=evaluate(repo,c,C,[1,1<<48],override);gates['measured_singular_floor']=row['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION';assert all(gates.values())
    return {'status':'PASS_ONE_INHERITED_NONZERO_RECORD_ADMISSION','metadata_member_sha256':digest,'record_noise_relative_original_baseline':[1,1<<48],'equation_residual_upper':c.up(xi),'readable_equation_residual_upper':float(xi.upper()),'proposed_s209_exact':list(float(s[208]).as_integer_ratio()),'readable_s209':float(s[208]),'gates':gates,'evaluated_phase':row,'full_factor_arithmetic_rerun':False,'new_estimator_calls':0,'scope':'Cached exact full-factor and admission receipts qualify one existing cyclic-oneq tuple; no factor/raw loading, copying or new fit; no PR250 admission or all-input guarantee.'}

def controls(repo,c,C):
    rows=[]
    def add(name,got,expect):assert got==expect,(name,got,expect);rows.append({'id':name,'observed':got,'expected':expect})
    n=[3,1<<49];ok='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'
    add('closed_three_halves_q',evaluate(repo,c,C,n)['status'],ok)
    add('two_q_phase_route_hold',evaluate(repo,c,C,[2,1<<48])['status'],'HOLD_DISKS_NOT_STRICTLY_DISJOINT')
    for name,ov in [('wrong_retained_order',{'q':208}),('left_Gram_one',{'etaU':[1,1]}),('right_Gram_one',{'etaV':[1,1]}),('inverse_residual_one',{'rho':[1,1]}),('negative_eq_residual',{'xi':[-1,1<<41]})]:add(name,evaluate(repo,c,C,n,ov)['status'],'HOLD_INVALID_PREMISE')
    add('negative_noise',evaluate(repo,c,C,[-1,1<<48])['status'],'HOLD_INVALID_PREMISE')
    add('missing_source_scale_floor',evaluate(repo,c,C,n,{'proposed_smin':[1,1<<24]})['status'],'HOLD_PROPOSED_SINGULAR_FLOOR')
    add('zero_proposed_singular_floor',evaluate(repo,c,C,n,{'proposed_smin':[0,1]})['status'],'HOLD_PROPOSED_SINGULAR_FLOOR')
    add('inflated_eq_error',evaluate(repo,c,C,n,{'xi':[1,1<<30]})['status'],'HOLD_DISKS_NOT_STRICTLY_DISJOINT')
    # Exact rational tail/equation distinction, not a new data measurement.
    A=((Fraction(3),Fraction(0)),(Fraction(0),Fraction(1)));u=(Fraction(1),Fraction(0));v=u;s=Fraction(3)
    F=tuple(sum(A[i][j]*v[j] for j in range(2))-u[i]*s for i in range(2));residual=tuple(tuple(A[i][j]-u[i]*s*v[j] for j in range(2)) for i in range(2))
    add('zero_equation_residual_with_nonzero_tail',F==(0,0) and residual==((0,0),(0,1)),True)
    add('two_one_quantum_coordinates_in_ball',4*(1+1)<=9,True)
    add('three_one_quantum_coordinates_outside_ball',4*(1+1+1)<=9,False)
    add('single_two_quantum_coordinate_outside_ball',4*(2*2)<=9,False)
    add('strict_disks_touch_refused',c.phase_decision(c.aa([1,4]),arb(0),c.aa([1,2])),'HOLD_DISKS_NOT_STRICTLY_DISJOINT')
    return {'status':'PASS_SIXTEEN_CONTROLS','rows':rows}

def protected_output(out_arg):
    lex=Path(out_arg).absolute();out=lex.resolve();protected={P.absolute(),P.resolve()}
    for a in [P,*P.parents]:
        if (a/'MANIFEST.json').is_file():protected.update([a.absolute(),a.resolve()])
    for x in [lex,out]:assert all(x!=a and a not in x.parents and x not in a.parents for a in protected),'HOLD protected output'
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);args=ap.parse_args();repo=Path(args.repo).resolve();out=protected_output(args.out);out.mkdir(parents=True,exist_ok=False);f,c=bound(repo)
    prior=json.loads((repo/OLD/'primary/CERTIFICATE.json').read_text());C=c.aa(prior['sketch']['per_62_vector_noise_multiplier_upper']);rows=[evaluate(repo,c,C,n) for n in [[0,1],[1,1<<48],[3,1<<49],[2,1<<48],[1127,1<<48]]]
    control=controls(repo,c,C);example=inherited_example(repo,c,C);bound(repo)
    receipt={'status':'COMPLETE_CONDITIONAL_SINGULAR_EQUATION_PHASE_IMPLICATION','freeze_sha256':sha(P/'FREEZE.json'),'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'quality_caps':f['quality_caps'],'rows':rows,'inherited_example':example,'new_estimator_calls':0,'universal_numerical_backend_success':False,'full_rank209_approximation_gate_revised':False,'physical_promotion':0,'external_review':'PENDING','lane':'development — no registry entry'}
    for name,obj in [('CERTIFICATE.json',receipt),('CONTROLS.json',control)]: (out/name).write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps({'status':receipt['status'],'rows':[{k:v for k,v in r.items() if k in ['noise_radius','status','readable_phase_error_upper','readable_matching_margin_lower']} for r in rows],'example_equation_error_upper':example['readable_equation_residual_upper'],'controls':len(control['rows'])}),flush=True)

if __name__=='__main__':main()
