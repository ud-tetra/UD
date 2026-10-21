"""Independent source/phase/packed-row/norm/true-RHS audit, supporting provisional checkpoints."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json,gzip,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);ap.add_argument('--frame',type=Path,required=True);ap.add_argument('--checkpoint',action='store_true');a=ap.parse_args();W=a.workspace;P=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest();refb=gzip.decompress((P/'REFERENCE_RHS.json.gz').read_bytes());ref=json.loads(refb);reference_check=json.loads((P/'REFERENCE_CHECKS.json').read_text());assert sha(refb)==reference_check['reference_decoded_sha256']
sb=(W/'c33_source/FULL_SLICE.json').read_bytes();sl=json.loads(sb);assert sha(sb)==ref['source_slice_sha256'];byfreq={r['frequency_integer']:r for r in ref['phase_tables']}
oldbase=W/'ud-repo/captures/2026-10-21T022602Z-codex-reusable-compression-8fd46991/frame';oldb=(oldbase/'PARTIAL_FRAME.json').read_bytes();assert sha(oldb)=='1c8e2f214c7e832afbaff324524a12dc3dbdd9bb126e031d2a71f84c437fe015';old={r['column']:r for r in json.loads(oldb)['rows']}
freeze=json.loads((W/'c33_INITIAL_FREEZE.json').read_text());expected_exe=freeze['source_hashes']['c31_action'];assert sha((W/'c31_action').read_bytes())==expected_exe
if a.checkpoint:
 raw=(a.frame/'CHECKPOINT.jsonl').read_bytes();lines=raw.splitlines(keepends=True);lines=[line for line in lines if line.endswith(b'\n')];snapshot=b''.join(lines);rows=[json.loads(line)for line in lines];meta=None
else:
 snapshot=(a.frame/'FULL_FRAME.json').read_bytes();meta=json.loads(snapshot);rows=meta['rows'];assert meta['status']=='PASS_FULL1999_SOURCE_FRAME_CONSTRUCTION' and meta['actual_rows_constructed_or_authenticated']==1999 and meta['new_native_adjoint_rows']==1983 and meta['authenticated_reused_C32_rows']==16 and meta['full_required_rows']==1999
 assert meta['trial_slice_sha256']==sha(sb) and meta['reuse_receipt_sha256']==sha(oldb) and meta['build_receipt_sha256']==sha((W/'c31_BUILD_RECEIPT.json').read_bytes()) and meta['operator_sha256']==ref['operator_sha256']
 assert meta['phase_tables_constructed']==119 and meta['unique_phase_scalar_checks']==974848 and meta['logical_phase_binding_checks']==1998*8192
assert len({r['column']for r in rows})==len(rows)
if not a.checkpoint:assert [r['column']for r in rows]==list(range(1999))
EY=Q(3,2**127)+Q(504,2**96);errornum2=0;reused=new=logical=packed_bytes=0;freqset=set();manifest=[]
for row in rows:
 c=row['column'];assert 0<=c<1999;plan=sl['columns'][c];assert (row['mode'],row['frequency_integer'])==(plan['mode'],plan['frequency_integer'])
 frequency=row['frequency_integer'];assert row['phase_table_sha256']==byfreq[frequency]['phase_table_sha256'];checks=0 if c==0 else8192;assert row['phase_enclosure_checks']==checks;logical+=checks
 if c:freqset.add(frequency)
 assert row['native_executable_sha256']==expected_exe and row['state_integer_scale_bits']==96 and row['rhs_dot_denominator_power2']==192 and row['status']=='PASS_SOURCE_BOUND_FULL_FRAME_ROW'
 assert len(row['input_text_sha256'])==64 and set(row['input_text_sha256'])<=set('0123456789abcdef')
 name=f'row_{c:04d}.i128.gz';assert row['output_row_file']==name;packed=(a.frame/name).read_bytes();packed_bytes+=len(packed);raw=gzip.decompress(packed);assert sha(packed)==row['output_row_sha256'] and sha(raw)==row['output_decoded_sha256'] and len(raw)==2640*16
 values=[int.from_bytes(raw[i:i+16],'little',signed=True)for i in range(0,len(raw),16)];assert sum(v*v for v in values)<9*2**192
 interval=ref['true_RHS_intervals'][c];assert interval['column']==c and interval['denominator_power2']==160;z=int(row['rhs_dot_integer']);lo=int(interval['lower_integer'])*2**32;hi=int(interval['upper_integer'])*2**32;debit=max(abs(z-lo),abs(z-hi));assert Q(debit,2**192)<2*EY;errornum2+=debit*debit
 if c in old:
  reused+=1;o=old[c];assert row['origin']=='REUSED_PINNED_C32_ROW' and packed==(oldbase/o['output_row_file']).read_bytes()
  for k in ['input_text_sha256','phase_table_sha256','rhs_dot_integer','output_row_sha256','output_decoded_sha256']:assert row[k]==o[k]
 else:new+=1;assert row['origin']=='NEW_C31_NATIVE_ADJOINT'
 manifest.append({'column':c,'packed_sha256':sha(packed),'decoded_sha256':sha(raw),'RHS_integer':str(z),'phase_sha256':row['phase_table_sha256']})
assert reused<=16 and new<=1983
if not a.checkpoint:assert reused==16 and new==1983 and len(freqset)==119
RHS2=Q(errornum2,2**384);assert RHS2<(90*EY)**2
if meta:
 data=[3*(((13*i+7)%17)-8)*2**84 for i in range(253952)];assert sum(v*v for v in data)==int(meta['data_norm_squared_integer']) and sum(v*v for v in data)<(2*2**96)**2
result={'status':'PROVISIONAL_CHECKPOINT_PASS' if a.checkpoint else'PASS_FULL1999_ROWS_AND_TRUE_RHS','source_slice_sha256':sha(sb),'frame_or_checkpoint_prefix_sha256':sha(snapshot),'rows_checked':len(rows),'reused_rows_checked':reused,'new_rows_checked':new,'decoded_integer_coordinates_checked':len(rows)*2640,'decoded_raw_bytes':len(rows)*2640*16,'packed_row_bytes':packed_bytes,'distinct_nonzero_phase_hashes_checked':len(freqset),'logical_phase_bindings_checked':logical,'RHS_error_squared_upper':[RHS2.numerator,RHS2.denominator],'RHS_encoding_bound_2eta_squared':[(90*EY)**2 .numerator,(90*EY)**2 .denominator] if False else str((90*EY)**2),'direct_true_RHS_bound_pass':True,'ordered_audited_payload_manifest_sha256':sha(json.dumps(sorted(manifest,key=lambda r:r['column']),sort_keys=True,separators=(',',':')).encode()),'input_text_hash_semantics_not_all507million_coordinates_recomputed':True,'scope':{'native_calls_not_rerun':True,'all_source_rows_and_phase_tables_previously_independently_reconstructed':True,'saved_row_bytes_hash_shape_norm_and_reused_payloads_checked':True,'RHS_error_verified_against_independent_trueY_period17_Arb256_reference':True,'provisional_is_not_final_frame_certificate':a.checkpoint,'solve_not_certified_here':True,'physical_promotion':0,'external_review':'PENDING'}}
name=f'ROW_CHECKPOINT_{len(rows):04d}.json'if a.checkpoint else'ROWS_CHECKS.json';(P/name).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'rows':len(rows),'RHS2':float(RHS2)}))
