"""Independent metadata arithmetic ONLY. No source-code import or time profile."""
import ast,json,hashlib
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
from datetime import datetime,timezone
ROOT=Path('/workspace/scratch/f3d1c2f040c9');S=ROOT/'phase-prospective-protocol-20261019';P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
fr=lambda x:F(int(x[0]),int(x[1]));pair=lambda x:[str(x.numerator),str(x.denominator)]
def run():
    f=load(P/'REVIEW_FREEZE.json');assert sha(Path(__file__))==f['script_sha256']
    for n,h in f['files'].items():assert sha(S/n)==h,n
    build=load(S/'BUILD_FREEZE.json')
    for n,h in build['files'].items():assert sha(S/n)==h,n
    index=load(S/'SOURCE_INDEX.json');roles={r['role']:r for r in index['sources']}
    for r in index['sources']:
        src=ROOT/'ud-repo'/r['repository_source'];assert sha(src)==r['sha256']
        cap=ROOT/'ud-repo'/Path(*Path(r['repository_source']).parts[:2]);assert sha(cap/'MANIFEST.json')==r['capture_manifest_sha256']
    for r in load(S/'INPUT_PROVENANCE.json')['copied_inputs']:assert sha(S/r['destination'])==sha(ROOT/'ud-repo'/r['repository_source'])==r['sha256']
    c=load(S/'CONTRACT.json');anchors=load(ROOT/roles['anchor_data']['workspace_source'])['records'];assert len(anchors)==6
    D=(1<<44)+1;a=(1<<44)-1;b=1<<23;assert a*a+b*b==D*D
    prep_rows=[]
    for prep in c['preparations']:
        M=prep['matrix_numerator'];assert prep['denominator']==D and len(M)==37 and all(len(r)==37 for r in M)
        old=next(r for r in anchors if r['case']==prep['existing_family_reference_anchor']);N=old['transform_integer_matrix'];assert old['transform_denominator']==1
        assert all(sum(M[i][k]*M[j][k] for k in range(37))==D*D*int(i==j) for i in range(37) for j in range(37))
        assert all(not M[i][j] or i%2==j%2 for i in range(37) for j in range(37)) and max(sum(v!=0 for v in r) for r in M)==2
        # Recover the relative transform from M*Told^T independently of recipes.
        H=[[sum(M[i][k]*N[j][k] for k in range(37)) for j in range(37)] for i in range(37)]
        assert all(H[i][i] in [a,D] for i in range(37))
        assert all(H[i][j]==-H[j][i] and abs(H[i][j]) in [0,b] for i in range(37) for j in range(37) if i!=j)
        delta=[[H[i][j]-D*int(i==j) for j in range(37)] for i in range(37)]
        gram=[[sum(delta[i][k]*delta[j][k] for k in range(37)) for j in range(37)] for i in range(37)]
        assert all(gram[i][j]==0 for i in range(37) for j in range(37) if i!=j)
        assert set(gram[i][i] for i in range(37))=={0,4*D}
        distance=F(4,D);assert distance==fr(prep['exact_squared_operator_distance_to_reference'])<F(1,1<<42)<F(1,1<<40)
        assert distance<fr(prep['operator_distance_upper'])**2 and fr(prep['operator_distance_upper'])<fr(prep['existing_PR233_rho'])
        for prior in anchors:
            den=prior['transform_denominator'];A=prior['transform_integer_matrix']
            assert any(M[i][j]*den!=A[i][j]*D for i in range(37) for j in range(37))
        prep_rows.append({'id':prep['id'],'orthogonality_equalities':1369,'relative_delta_Gram_diagonal_nonzero':4*D,'exact_operator_distance_squared':pair(distance),'distinct_from_all_six_anchors':True})
    targets=load(S/'inputs/SOURCE_PHASE.json');bylabel={r['label']:r for r in targets['target_matches']};assert len(bylabel)==209
    oldsp=load(ROOT/roles['old_spatial_selection']['workspace_source']);A=[{'preparation':i,'channel':oldsp['channels'][i],'sign':oldsp['signs'][i]} for i in range(37)]
    B=[]
    for i in range(37):
        digest=hashlib.sha256(f'UD_PHASE_PROSPECTIVE_V1_20261019|B|spatial|{i}'.encode('ascii')).digest();B.append({'preparation':i,'channel':int.from_bytes(digest[:8],'little')%62,'sign':1 if digest[8]&1 else -1})
    expected=[('new_A_control','A','zero'),('new_A_ramped_low','A','ramped_low_sine'),('new_B_control','B','zero'),('new_B_chirped_high','B','chirped_high_cosine')]
    assert c['fixed_case_order']==[r[0] for r in expected] and len(c['cases'])==4
    for case,(name,prep,kind) in zip(c['cases'],expected):
        assert (case['case'],case['preparation_id'],case['noise_kind'])==(name,prep,kind)
        assert case['spatial']==(A if prep=='A' else B)
        assert case['carrier_target_label']==('j0:rate1:sign1' if prep=='A' else 'j51:rate-1:sign1') and case['carrier_omega']==bylabel[case['carrier_target_label']]['omega']
        amp=0 if kind=='zero' else 1127
        assert case['integer_noise_absolute_max']==amp and fr(case['per62_vector_noise_norm_upper'])==F(amp,1<<48)
    sep=fr(targets['metrics']['minimum_target_chord_lower']);assert fr(c['strict_finite_emission_circular_error_cap'])==sep/2
    oldcaps=load(S/'inputs/OLD_POLICY.json')['gates'];assert set(c['unchanged_phase_quality_caps'])=={'inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error'}
    assert all(v==oldcaps[k] for k,v in c['unchanged_phase_quality_caps'].items())
    family=load(S/'inputs/FAMILY_CERTIFICATE.json');assert fr(family['rho'])==F(1,1<<20) and fr(family['delta_per_62_vector'])==F(1127,1<<48)
    assert all(r['existing_family_reference_anchor'] in family['anchor_cases'] for r in c['preparations'])
    assert c['unchanged_actual_estimator_source_sha256']==roles['actual_estimator']['sha256']
    assert c['new_raw_records_this_turn']==c['new_estimator_SVD_eigenvalue_inverse_alignment_calls_this_turn']==0
    # Parse only: NEVER import/call raw/profile/carrier routines or source code.
    for name in ['build_contract.py','static_replay.py']:
        tree=ast.parse((S/name).read_text());called={n.func.id for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name)}
        assert not called.intersection({'carrier_sign','noise_value','nominal_block'})
    assert [round(F(n,2)) for n in [-3,-1,1,3]]==[-2,0,0,2]
    # Pure path guard scenarios; no actual archive writes or replay invocation.
    cap=PurePosixPath('/repo/captures/frozen');sub=cap/'protocol'
    def guard(out):return out!=sub and sub not in out.parents and out not in sub.parents and out!=cap and cap not in out.parents and out not in cap.parents
    checks=[('sibling_inside_manifested_capture',cap/'new-replay',False),('protocol_descendant',sub/'out',False),('capture_itself',cap,False),('capture_ancestor',cap.parent,False),('external_tmp',PurePosixPath('/tmp/new-prospective-replay'),True)]
    assert all(guard(path)==want for name,path,want in checks)
    result={'status':'PASS_INDEPENDENT_METADATA_ONLY_PROSPECTIVE_PHASE_REVIEW','utc':datetime.now(timezone.utc).isoformat(),'freeze_sha256':sha(P/'REVIEW_FREEZE.json'),'preparations':prep_rows,'orthogonality_equalities_checked':2738,'relative_delta_Gram_equalities_checked':2738,'SHA_spatial_selectors_checked':37,'nearest_even_half_tie_controls':4,'output_guard_path_cases':[{ 'id':name,'expected_allowed':want,'actual_allowed':guard(path)} for name,path,want in checks],'odd_denominator_nominal_rounding_error_upper_in_raw_quanta':pair(F(D-1,2*D)),'fixed_phase_cap':pair(sep/2),'scope':'Prospective contract/static metadata only, not an observed future phase/frame/cutoff result or2^-39 calibration guarantee.','carrier_profile_tables_generated':0,'raw_records_generated':0,'estimator_SVD_eigenvalue_inverse_alignment_calls':0,'external_review':'PENDING','physical_promotion':0}
    out=P/'REVIEW_RECEIPT.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'receipt_sha256':sha(out)}))
if __name__=='__main__':run()
