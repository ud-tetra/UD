"""Source-bound uniform phase-only implication. No estimator or matrix eigensolver."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from flint import arb,fmpq,fmpz_mat,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(v):
    if isinstance(v,(list,tuple)):v=Q(int(v[0]),int(v[1]))
    v=Q(v);return arb(fmpq(v.numerator,v.denominator))
def up(x):
    z=(arb(x.upper())*(1<<180)).ceil().unique_fmpz();assert z is not None
    return [int(z),1<<180]
def down(x):
    z=(arb(x.lower())*(1<<180)).floor().unique_fmpz();assert z is not None
    return [int(z),1<<180]
def binding(repo=None):
    f=json.loads((P/'FREEZE_v2.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,('freeze',n)
    b=json.loads((P/'INPUT_BINDINGS.json').read_text())
    for row in b['files']:
        assert sha(P/row['local_path'])==row['sha256'],('input',row['local_path'])
        if repo is not None:assert sha(repo/row['repository_path'])==row['sha256'],('repository_input',row['repository_path'])
    return f

def sketch_power_bounds():
    v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974))
    old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    assert int(v@v)==16228 and np.all(v@old==0)
    A=np.column_stack((2*old,v,2*new));G=fmpz_mat((A.T@A).tolist());power=G;rows=[]
    for k in [1,2,4,8,16,32]:
        if k>1:power=power*power
        bound=max(sum(abs(int(z)) for z in row) for row in power.tolist())
        rows.append({'power':k,'exact_max_absolute_row_sum':str(bound),'sketch_operator_norm_upper':up(arb(bound).root(2*k)/128)})
    norm=min((aa(z['sketch_operator_norm_upper']) for z in rows),key=lambda z:float(z.upper()))
    C=norm*arb(37*8191).sqrt()
    return {'Gram_int64le_sha256':hashlib.sha256(np.array(G.tolist(),dtype='<i8').tobytes()).hexdigest(),'power_bounds':rows,'sketch_operator_norm_upper':up(norm),'per_62_vector_noise_multiplier_upper':up(C),'readable_multiplier_upper':float(C.upper())}

def phase_decision(R,arg,sep):
    if not (sep>0 and R>=0 and arg>=0):return 'HOLD_INVALID_SEPARATION_OR_ERROR'
    if not R<1:return 'HOLD_ORIGIN_NOT_EXCLUDED'
    if not 2*R<sep:return 'HOLD_DISKS_NOT_STRICTLY_DISJOINT'
    if not 2*(R.asin()+arg)<sep:return 'HOLD_PHASE_MATCHING_MARGIN'
    return 'CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'

def evaluate(C,noise,kind='retained_conditional',overrides=None):
    u=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());m=json.loads((P/'inputs/PARENT_PHASE.json').read_text())['metrics'];o=json.loads((P/'inputs/PARENT_ORDER.json').read_text());f=json.loads((P/'FREEZE_v2.json').read_text());g={k:aa(v) for k,v in f['conditional_quality_caps'].items()};ov={} if overrides is None else overrides
    q=ov.get('q',209);g.update({k:aa(v) for k,v in ov.items() if k!='q'})
    row={'delta':list(noise),'kind':kind,'status':'HOLD_INVALID_PREMISE','uniform_solver_success_claimed':False}
    dlt=aa(noise)
    if q!=209 or not dlt>=0:return row
    if not (0<=g['retained_Gram']<1 and 0<=g['inverse_residual']<1 and g['proposed_inverse_norm']>0 and all(g[k]>=0 for k in ['retained_rank209_approximation_error','raw_shift_residual','eigenpair_residual','emitted_argument_error'])):return row
    r=aa(u['baseline_low_rank_residual_upper']);s0=aa(o['qth_sigma_lower']);tail=aa(o['qplus1_sigma_upper']);cut=aa(f['cutoff']);alpha=s0-r
    eta=g['retained_Gram'];eps=g['retained_rank209_approximation_error'];raw=g['raw_shift_residual'];eig=g['eigenpair_residual'];arg=g['emitted_argument_error'];rho=g['inverse_residual'];hinv=g['proposed_inverse_norm']
    if kind=='ideal':eta=eps=raw=eig=arg=arb(0)
    ex=r+C*dlt+eps;beta=aa(u['deleted_two_rows_beta_lower']);sigma=aa(u['comparison_shift_residual_upper']);M=aa(u['comparison_shift_norm_upper']);sep=aa(m['minimum_target_chord_lower'])
    row['exact_cutoff209_guaranteed']=bool(s0-C*dlt>cut and tail+C*dlt<cut)
    if not alpha>2*ex:row['status']='HOLD_SUBSPACE_GAP';return row
    # Conservative denominator below s0-C*delta-eps; no discarded left basis required.
    t=ex/(alpha-ex);dist=(2-2*(1-t*t).sqrt()).sqrt()
    if not beta>dist:row['status']='HOLD_DELETED_ROW_MARGIN';return row
    b=(sigma+raw/(1-eta).sqrt()+dist*(1+M))/(beta-dist)
    eta0=aa(m['basis_orthogonality_upper']);k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+eta)/(1-eta)).sqrt()
    hD=aa(m['source_inverse_norm_upper'])/(1-aa(m['source_inverse_residual_upper']));dD=aa(m['source_reduction_norm_upper']);LJ=aa(m['intertwining_residual_upper']);Delta=eig*hinv/(1-rho)
    R=hD*LJ+k0*hD*dD*(b+ka*Delta)
    row.update(status=phase_decision(R,arg,sep),subspace_sine_upper=up(t),polar_frame_distance_upper=up(dist),shift_distance_upper=up(b),eigenvalue_radius_upper=up(R),source_half_chord_lower=down(sep/2),source_minimum_chord_lower=down(sep))
    if R<1:
        angle=R.asin()+arg;row.update(two_step_phase_error_upper=up(angle),strict_phase_matching_margin_lower=down(sep/2-angle),readable_phase_upper=float(angle.upper()),readable_matching_margin_lower=float((sep/2-angle).lower()))
    if not row['exact_cutoff209_guaranteed']:row['status']='HOLD_EXACT_CUTOFF'
    return row

def controls(C):
    out=[]
    def add(n,got,expected):assert got==expected,(n,got,expected);out.append({'id':n,'observed':got,'expected':expected})
    q=1<<48
    add('closed_three_halves_q_ideal',evaluate(C,[3,2*q],'ideal')['status'],'CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION')
    add('closed_three_halves_q_retained_conditional',evaluate(C,[3,2*q])['status'],'CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION')
    add('two_q_sufficient_route_hold',evaluate(C,[2,q])['status'],'HOLD_DISKS_NOT_STRICTLY_DISJOINT')
    add('1127_q_not_uniformly_promoted',evaluate(C,[1127,q])['status'],'HOLD_DISKS_NOT_STRICTLY_DISJOINT')
    for n,ov in [('wrong_order',{'q':208}),('Gram_at_one',{'retained_Gram':[1,1]}),('inverse_at_one',{'inverse_residual':[1,1]}),('negative_eigen_residual',{'eigenpair_residual':[-1,100]})]:add(n,evaluate(C,[3,2*q],overrides=ov)['status'],'HOLD_INVALID_PREMISE')
    add('negative_noise',evaluate(C,[-1,q])['status'],'HOLD_INVALID_PREMISE')
    add('inflated_approximation_error',evaluate(C,[3,2*q],overrides={'retained_rank209_approximation_error':[1,1<<30]})['status'],'HOLD_DISKS_NOT_STRICTLY_DISJOINT')
    add('disk_touch_equality',phase_decision(aa([1,4]),arb(0),aa([1,2])),'HOLD_DISKS_NOT_STRICTLY_DISJOINT')
    add('origin_touch_equality',phase_decision(arb(1),arb(0),arb(4)),'HOLD_ORIGIN_NOT_EXCLUDED')
    add('angular_boundary_equality',phase_decision(arb(0),aa([1,4]),aa([1,2])),'HOLD_PHASE_MATCHING_MARGIN')
    # Independent integer-squared lattice checks, not floating norm thresholds.
    add('two_one_quantum_coordinates_admitted',4*(1+1)<=9,True)
    add('third_one_quantum_coordinate_excluded',4*(1+1+1)<=9,False)
    add('one_two_quantum_coordinate_excluded',4*(2*2)<=9,False)
    return {'status':'PASS_SIXTEEN_CONTROLS','rows':out,'all_expected_outcomes':True}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);args=ap.parse_args();repo=Path(args.repo).resolve();out_lexical=Path(args.out).absolute();out=out_lexical.resolve()
    protected={P.resolve(),P.absolute()}
    for a in [P,*P.parents]:
        if (a/'MANIFEST.json').is_file():protected.update([a.absolute(),a.resolve()])
    for candidate in [out_lexical,out]:
        assert all(candidate!=a and a not in candidate.parents for a in protected),'HOLD capture output write'
        assert all(candidate!=a and candidate not in a.parents for a in protected),'HOLD ancestor output write'
    out.mkdir(parents=True,exist_ok=False);f=binding(repo);sp=sketch_power_bounds();C=aa(sp['per_62_vector_noise_multiplier_upper']);rows=[]
    for d in [[0,1],[1,1<<48],[3,1<<49],[2,1<<48],[1127,1<<48]]:
        for kind in ['ideal','retained_conditional']:rows.append(evaluate(C,d,kind))
    ct=controls(C);binding(repo)
    result={'status':'COMPLETE_SOURCE_BOUND_PHASE_ONLY_UNIFORM_IMPLICATION','freeze_sha256':sha(P/'FREEZE_v2.json'),'input_bindings_sha256':sha(P/'INPUT_BINDINGS.json'),'scope':f['scope'],'sketch':sp,'conditional_quality_caps':f['conditional_quality_caps'],'rows':rows,'new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'actual_output_premise_admission_this_run':False,'PR250_outputs_not_admitted_by_this_theorem':True,'external_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry'}
    (out/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');(out/'CONTROLS.json').write_text(json.dumps(ct,indent=2)+'\n');print(json.dumps({'status':result['status'],'C':sp['readable_multiplier_upper'],'rows':[(r['delta'],r['kind'],r['status'],r.get('readable_phase_upper')) for r in rows],'controls':len(ct['rows']),'new_fits':0}),flush=True)
if __name__=='__main__':main()
