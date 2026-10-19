"""Post-known finite inherited-source instantiation and same-sketch provenance."""
import argparse,hashlib,io,json
from pathlib import Path
from zipfile import ZipFile
import numpy as np
from flint import arb
import certify_v2 as c
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(repo):
    freeze=json.loads((P/'SUPPLEMENT_FREEZE_v2.json').read_text())
    for n,h in freeze['files'].items():assert sha(P/n)==h,n
    for row in freeze['repository_sources']:assert sha(repo/row['path'])==row['sha256'],row['path']
    c.binding(repo);sp=c.sketch_power_bounds();old=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());expected=[63152,1233436656,534960210172866048]
    assert [int(z['exact_max_absolute_row_sum']) for z in sp['power_bounds'][:3]]==expected
    assert [int(z['max_absolute_row_sum']) for z in old['exact_sketch_power_bounds']]==expected
    base='captures/2026-10-19T134625Z-codex-uniform-output-73b6e18a/admission/'
    fc=json.loads((repo/base/'inputs/ACTUAL_SVD.json').read_text());ad=json.loads((repo/base/'ACTUAL_ADMISSION.json').read_text());sf=json.loads((repo/base/'FREEZE.json').read_text())
    assert sha(repo/base/'inputs/ACTUAL_SVD.json')==sf['input_sha256']['ACTUAL_SVD.json']
    archive=repo/'captures/2026-10-19T132221Z-codex-rounding-replay-82e4a9b7/WITNESS_03.zip';member='results/legacy_gemm/SVD_META.npz'
    with ZipFile(archive) as z:body=z.read(member)
    h=hashlib.sha256(body).hexdigest();assert h==sf['actual_arrays_sha256'][member]==ad['bindings'][member]
    with np.load(io.BytesIO(body),allow_pickle=False) as z:s=z['singular']
    assert s.shape==(321,) and s.dtype==np.float64 and np.isfinite(s).all() and np.all(s[:-1]>=s[1:]) and np.all(s>=0)
    etaL=c.aa(fc['eta_left_upper']);etaR=c.aa(fc['eta_right_upper']);raw=c.aa(fc['reconstruction_residual_upper']);proj=c.aa(fc['projection_error_upper']);smax=c.aa(float(s[0]).as_integer_ratio());s210=c.aa(float(s[209]).as_integer_ratio())
    polar=lambda e:e/(1+(1-e).sqrt())
    cost=smax*(polar(etaL)*(1+etaR).sqrt()+polar(etaR));tail=((1+etaL)*(1+etaR)).sqrt()*s210
    eps=proj+raw+tail+cost;caps=json.loads((P/'FREEZE_v2.json').read_text())['conditional_quality_caps'];g=ad['rows'][0]['metrics'];assert all(v is True for v in ad['rows'][0]['gates'].values())
    gates={'retained_order209':fc['learned_order']==209,'retained_Gram':bool(etaL<=c.aa(caps['retained_Gram'])),'retained_approximation_error':bool(eps<=c.aa(caps['retained_rank209_approximation_error']))}
    for n in ['raw_shift_residual','inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error']:gates[n]=bool(c.aa(g[n])<=c.aa(caps[n]))
    assert all(gates.values())
    recordfreeze=json.loads((repo/'captures/2026-10-19T132221Z-codex-rounding-replay-82e4a9b7/FREEZE.json').read_text())
    rawreplay=json.loads((repo/'captures/2026-10-19T132221Z-codex-rounding-replay-82e4a9b7/RAW_PROJECTION_REPLAY.json').read_text())
    assert rawreplay['raw_sha256']==recordfreeze['record_sha256']=='fd819bea491085f222d9ad7fef325b922ec75a8690c7b6ac69b2429617c67339'
    assert rawreplay['baseline_sha256']=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59' and rawreplay['readings_checked']==18790154 and rawreplay['vector_integer_squared_error_max']==1
    return {'status':'PASS_FINITE_BASELINE_INHERITED_PREMISE_INSTANTIATION_AND_SAME_SKETCH_BINDING','supplement_freeze_sha256':sha(P/'SUPPLEMENT_FREEZE_v2.json'),'same_sketch_first_three_exact_power_rows':expected,'same_sketch_Gram_int64le_sha256':sp['Gram_int64le_sha256'],'baseline_mode':'legacy_gemm; exact input identity to integer_projection inherited from sourceadmission','raw_record_noise_relative_original_baseline_upper':[1,1<<48],'record_sha256':rawreplay['raw_sha256'],'original_baseline_sha256':rawreplay['baseline_sha256'],'record_membership_scope':'Inherited complete raw replay of oneq/vector cyclicunit, NOT zero-noise baseline; original raw bytes not reread this supplement','metadata_member':member,'metadata_sha256':h,'proposed_tail_sigma210_exact':[str(x) for x in float(s[209]).as_integer_ratio()],'retained_operator_error_upper':c.up(eps),'raw_full_tail_operator_upper':c.up(tail),'retained_polar_correction_upper':c.up(cost),'readable_retained_operator_error_upper':float(eps.upper()),'conditional_quality_gates':gates,'interpretation':'One EXISTING nonzero-oneq cyclicunit returned output meets the new retained-phase premises conditional on cached exact parentfullfactor and admission certificates. No new raw, factor, estimator fit or fullparentarithmetic rerun; no PR250 output admission or all-input library guarantee.','new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'external_review':'PENDING','physical_promotion':0}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);args=ap.parse_args();lex=Path(args.out).absolute();out=lex.resolve();protected={P.absolute(),P.resolve()}
    for a in [P,*P.parents]:
        if (a/'MANIFEST.json').is_file():protected.update([a.absolute(),a.resolve()])
    for x in [lex,out]:assert all(x!=a and a not in x.parents and x not in a.parents for a in protected),'HOLD protected output'
    out.mkdir(parents=True,exist_ok=False);result=run(Path(args.repo).resolve());(out/'SUPPLEMENT_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
