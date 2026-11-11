import argparse,concurrent.futures,datetime,hashlib,json,urllib.parse,urllib.request,urllib.error
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path,required=True);args=parser.parse_args()
if args.destination.exists():raise FileExistsError('Choose a new destination')
args.destination.mkdir(parents=True)
base='https://stablerelease.me/UD/';data=json.loads((Path(__file__).resolve().parent/'SOURCE_RECORDS.json').read_text());names=[x['filename'] for x in data['artifacts']['source_records'] if 'filename' in x]+['UD_PROOF_DEBT_PACKET_001.pdf','UD_GLOSSARY_GOVERNANCE_v0.1','Final Ratification Receipt.pdf']
items=[]
for name in names:
 for prefix in ['', 'source/']:
  items.append({'filename':name,'candidate_url':base+urllib.parse.quote(prefix+name,safe='/'),'path_basis':'Filename explicitly named in supplied dashboard/WBS; root/source placement is an unconfirmed hypothesis'})
def get(item):
 r=dict(item);r['checked_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(r['candidate_url'],timeout=15) as response:
   b=response.read(4000001);r['http_status']=response.status;r['final_url']=response.url;r['content_type']=response.headers.get('Content-Type','')
  r['size_bytes']=len(b);r['sha256']=hashlib.sha256(b).hexdigest()
  expected=next((x for x in data['artifacts']['source_records'] if x.get('filename')==r['filename']),{})
  r['expected_sha256']=expected.get('sha256');r['source_hash_matches']=r['sha256']==r['expected_sha256'] if r['expected_sha256'] else None
  html=b.lstrip().lower().startswith((b'<!doctype html',b'<html'))
  if html and not r['filename'].endswith('.html'):r['status']='HTTP_200_HTML_FALLBACK_NOT_NAMED_ARTIFACT'
  elif len(b)>4000000:r['status']='HTTP_200_SIZE_LIMIT_UNVERIFIED'
  else:
   r['status']='REACHABLE_NAMED_CONTENT_HASH_MATCH' if r['source_hash_matches'] else 'REACHABLE_CONTENT_REQUIRES_IDENTITY_REVIEW'
   dest=(args.destination/'candidate_sources')/urllib.parse.urlparse(r['candidate_url']).path.removeprefix('/UD/');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b);r['local_path']=str(dest)
 except urllib.error.HTTPError as e:r['http_status']=e.code;r['status']='NOT_RETRIEVED'
 except Exception as e:r['status']='REQUEST_FAILED';r['error']=type(e).__name__+': '+str(e)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 rs=[]
 for i,r in enumerate(pool.map(get,items)):
  rs.append(r)
  if (i+1)%10==0:print('checked',i+1,flush=True)
(args.destination/'named-source-candidates.json').write_text(json.dumps(rs,indent=2)+'\n')
print(json.dumps({'checked':len(rs),'retrieved':[r for r in rs if r['status'].startswith('REACHABLE')],'fallbacks':sum(r['status'].startswith('HTTP_200_HTML') for r in rs),'status_counts':{str(code):sum(x.get('http_status')==code for x in rs) for code in sorted({x.get('http_status',0) for x in rs})}},indent=2))
