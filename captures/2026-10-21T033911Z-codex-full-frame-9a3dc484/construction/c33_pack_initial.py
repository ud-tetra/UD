"""Group verbatim compressed row witnesses into bounded binary parts."""
from pathlib import Path
import argparse,json,hashlib,struct,gzip
ap=argparse.ArgumentParser();ap.add_argument('--frame',type=Path,required=True);ap.add_argument('--frame-sha256',required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);H=lambda b:hashlib.sha256(b).hexdigest();fb=(a.frame/'FULL_FRAME.json').read_bytes();assert H(fb)==a.frame_sha256;meta=json.loads(fb);assert [r['column']for r in meta['rows']]==list(range(1999));parts=[]
for start in range(0,1999,200):
 content=bytearray(b'UD33FRM1');subset=meta['rows'][start:start+200]
 for row in subset:
  packed=(a.frame/row['output_row_file']).read_bytes();assert H(packed)==row['output_row_sha256'];raw=gzip.decompress(packed);assert len(raw)==2640*16 and H(raw)==row['output_decoded_sha256'];content.extend(struct.pack('<II',row['column'],len(packed)));content.extend(packed)
 name=f'FRAME_{start//200:02d}.bin';(a.out/name).write_bytes(content);parts.append({'file':name,'start_row':start,'row_count':len(subset),'size_bytes':len(content),'sha256':H(content)})
index={'status':'PASS_VERBATIM_FULL1999_ROW_WITNESSES_PACKED','format':'UD33FRM1 then repeated little-endian uint32 column,uint32 gzip_length,verbatim row gzip bytes','frame_receipt_sha256':H(fb),'rows':1999,'state_dim':2640,'row_grid_bits':96,'decoded_matrix_bytes':1999*2640*16,'stored_part_bytes':sum(x['size_bytes']for x in parts),'parts':parts};(a.out/'FRAME_INDEX.json').write_text(json.dumps(index,indent=2,sort_keys=True)+'\n');print(json.dumps({'parts':len(parts),'stored_bytes':index['stored_part_bytes']}))
