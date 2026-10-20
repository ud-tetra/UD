#!/usr/bin/env python3
"""Bind the final finite review to stable final source and producer replay bytes."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
f=load(P/'FINITE_CHECKS.json');e=load(P/'EIGENPROPOSAL_CHECKS.json');b=load(W/'c27_cert_v2/SOURCE_BINDINGS.json');r=load(W/'c27_cert_v2/RESULT.json');freeze=load(W/'c27_work/VERIFIER_V2_FREEZE.json')
assert sha(W/'c27_verify.py')==freeze['sha256']['c27_verify.py']
assert b['source_archive_sha256']==f['inputs']['source_archive_sha256'] and b['Q_gzip_sha256']==f['inputs']['Q_gzip_sha256']
assert b['eigenproposal_gzip_sha256']==e['eigenproposal_gzip_sha256']
assert sha(W/'c27_cert_v2/TIME_KERNELS.json.gz')==f['inputs']['time_kernel_gzip_sha256']
assert sha(W/'c27_cert_v2/GRAM_MIDPOINT.npz')==f['inputs']['Gram_midpoint_npz_sha256']
rank=W/'ud-repo/captures/2026-10-20T232207Z-codex-weighted-history-359f283e'
assert sha(rank/'RESULT.json')==b['inherited_rank_result_sha256'] and sha(rank/'THEOREM.md')==b['inherited_rank_theorem_sha256']
assert r['inherited_history_and_sample_rank']==1999 and r['inherited_kernel']==641
assert r['positive_sigma_lower']=='>61/27648>1/512' and r['positive_condition_upper']=='<27648/61<512'
assert r['scope']['full_cross_channel_terms_retained'] and not r['scope']['old_nominal2029_certificate_transfer']
items={}
for name in ['RESULT.json','SOURCE_BINDINGS.json','ARITHMETIC_DIAGNOSTICS.json','TIME_KERNELS.json.gz','GRAM_MIDPOINT.npz','EIGENPROPOSAL.bin.gz']:
 a=W/'c27_cert_v2'/name;c=W/'c27_replay'/name;assert a.read_bytes()==c.read_bytes();items[name]={'primary_sha256':sha(a),'replay_sha256':sha(c),'byte_identical':True}
out={'status':'PASS_FINAL_SOURCE_WITNESS_AND_SIX_FILE_REPLAY_BINDING','root_checker_sha256':sha(W/'c27_verify.py'),'root_theorem_sha256':sha(W/'c27_THEOREM.md'),'scientific_output_bindings':items,'source_binding_values':b,'independent_full_Gram_entries':3996001,'independent_temporal_ball_checks':57600,'independent_saved_eigen_residual_entries':3996001,'scope':{'no_producer_checker_or_eigensolver_run_by_reviewer':True,'inherited_rank1999_kernel641':True,'same_team_development_review':True,'all_input_backend_or_race_guarantees':'NOT_ESTABLISHED','physical_promotion':0,'external_review':'PENDING'}}
(P/'FINAL_BINDING.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checker':out['root_checker_sha256'],'theorem':out['root_theorem_sha256']}))
