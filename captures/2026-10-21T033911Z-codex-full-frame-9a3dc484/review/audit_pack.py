"""Independent bounded-part parser and exact compressed-payload restoration comparison."""
from pathlib import Path
import argparse,json,hashlib,gzip,struct
ap=argparse.ArgumentParser();ap.add_argument('--frame',type=Path,required=True);ap.add_argument('--packed',type=Path,required=True);ap.add_argument('--restored',type=Path);a=ap.parse_args();P=Path(__file__).resolve().parent
H=lambda x:hashlib.sha256(x).hexdigest();fb=(a.frame/'FULL_FRAME.json').read_bytes();meta=json.loads(fb);rb=json.loads((P/'ROWS_CHECKS.json').read_text());assert rb['status']=='PASS_FULL1999_ROWS_AND_TRUE_RHS'and rb['frame_or_checkpoint_prefix_sha256']==H(fb)
ib=(a.packed/'FRAME_INDEX.json').read_bytes();index=json.loads(ib);assert index['status']=='PASS_VERBATIM_FULL1999_ROW_WITNESSES_PACKED'and index['frame_receipt_sha256']==H(fb);assert index['rows']==1999 and index['rows_per_part']==64 and index['state_dim']==2640 and index['row_grid_bits']==96 and index['decoded_matrix_bytes']==1999*2640*16 and len(index['parts'])==32
seen=[];stored=0;payload=0;part_hashes=[];restored_checks=0
for partno,part in enumerate(index['parts']):
 assert part['file']==f'FRAME_{partno:02d}.bin'and part['start_row']==64*partno and part['row_count']==min(64,1999-64*partno)
 data=(a.packed/part['file']).read_bytes();assert H(data)==part['sha256']and len(data)==part['size_bytes']and data[:8]==b'UD33FRM1';stored+=len(data);cursor=8
 for local in range(part['row_count']):
  assert cursor+8<=len(data);column,length=struct.unpack_from('<II',data,cursor);cursor+=8;assert column==64*partno+local and 0<length<=100000 and cursor+length<=len(data)
  packed=data[cursor:cursor+length];cursor+=length;row=meta['rows'][column];original=(a.frame/row['output_row_file']).read_bytes();assert packed==original and H(packed)==row['output_row_sha256'];raw=gzip.decompress(packed);assert len(raw)==2640*16 and H(raw)==row['output_decoded_sha256'];payload+=length;seen.append(column)
  if a.restored is not None:
   assert (a.restored/row['output_row_file']).read_bytes()==packed;restored_checks+=1
 assert cursor==len(data);part_hashes.append({'file':part['file'],'sha256':H(data),'bytes':len(data)})
assert seen==list(range(1999))and stored==payload+1999*8+32*8 and stored==index['stored_part_bytes']
if a.restored is not None:assert(a.restored/'FULL_FRAME.json').read_bytes()==fb
out={'status':'PASS_INDEPENDENT_VERBATIM_BOUNDED_PART_RESTORE_AUDIT','frame_sha256':H(fb),'index_sha256':H(ib),'part_count':32,'all_row_payloads_compared':1999,'restored_row_payloads_compared':restored_checks,'decoded_signed_int128_matrix_bytes':1999*2640*16,'stored_gzip_payload_bytes':payload,'part_overhead_bytes':1999*8+32*8,'stored_part_bytes':stored,'part_hashes':part_hashes,'scope':{'archive_byte_identity_not_independent_native_execution':True,'manifest_or_expected_index_hash_must_be_authenticated_externally':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'PACK_CHECKS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k]for k in ['status','part_count','all_row_payloads_compared','stored_part_bytes']}))
