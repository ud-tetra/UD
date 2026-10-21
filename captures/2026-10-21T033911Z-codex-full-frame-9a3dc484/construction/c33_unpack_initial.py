"""Restore authenticated row witnesses; archive contents are data only."""
from pathlib import Path
import argparse,json,hashlib,struct,gzip
ap=argparse.ArgumentParser();ap.add_argument('--parts',type=Path,required=True);ap.add_argument('--index-sha256',required=True);ap.add_argument('--metadata',type=Path,required=True);ap.add_argument('--metadata-sha256',required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();H=lambda b:hashlib.sha256(b).hexdigest();ib=(a.parts/'FRAME_INDEX.json').read_bytes();assert H(ib)==a.index_sha256;index=json.loads(ib);fb=a.metadata.read_bytes();assert H(fb)==a.metadata_sha256==index['frame_receipt_sha256'];meta=json.loads(fb);assert [r['column']for r in meta['rows']]==list(range(1999));a.out.mkdir(parents=True,exist_ok=False);seen=[]
for part in index['parts']:
 assert part['file']==f'FRAME_{part["start_row"]//200:02d}.bin';b=(a.parts/part['file']).read_bytes();assert len(b)==part['size_bytes']and H(b)==part['sha256']and b[:8]==b'UD33FRM1';at=8
 for c in range(part['start_row'],part['start_row']+part['row_count']):
  col,n=struct.unpack_from('<II',b,at);at+=8;assert col==c and 0<n<=100000;packed=b[at:at+n];at+=n;row=meta['rows'][c];assert row['output_row_file']==f'row_{c:04d}.i128.gz'and H(packed)==row['output_row_sha256'];raw=gzip.decompress(packed);assert len(raw)==2640*16 and H(raw)==row['output_decoded_sha256'];(a.out/row['output_row_file']).write_bytes(packed);seen.append(c)
 assert at==len(b)
assert seen==list(range(1999));(a.out/'FULL_FRAME.json').write_bytes(fb);print('PASS restored all1999 exact original row gzip files')
