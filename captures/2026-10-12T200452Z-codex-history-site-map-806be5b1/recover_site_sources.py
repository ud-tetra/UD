import argparse,concurrent.futures,datetime,hashlib,json,re,urllib.parse,urllib.request
from pathlib import Path
from html.parser import HTMLParser
parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path,required=True);args=parser.parse_args()
root=args.destination
if root.exists():raise FileExistsError('Choose a new destination; existing output is never replaced')
root.mkdir(parents=True);out=root/'sources';out.mkdir()
base='https://stablerelease.me/UD/'
app=(Path(__file__).resolve().parent/'site/app.js').read_text();paths=sorted(set(re.findall(r'(?:file|source):"(\./[^"]+)"',app)+['./content/primer.html','./','./app.js','./wbs.html','./dashboard.html']))
records=[]
def get(path):
 url=urllib.parse.urljoin(base,path)
 try:
  with urllib.request.urlopen(url,timeout=25) as r:
   b=r.read();status=r.status;final=r.url;headers={'last_modified':r.headers.get('Last-Modified'),'etag':r.headers.get('ETag'),'content_type':r.headers.get('Content-Type')}
  name='index.html' if path=='./' else path.removeprefix('./');p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
  s=b.decode('utf-8',errors='replace');lines=s.splitlines();matches=[]
  for label,pat in [('target',r'238\s*[.,]\s*14'),('rational_rewrite',r'11907\s*/\s*50'),('toroidal',r'toroid'),('cascade',r'cascade')]:
   for i,line in enumerate(lines):
    if re.search(pat,line,re.I):matches.append({'pattern':label,'line':i+1,'text':line[:1000]})
  return {'url':url,'final_url':final,'relative_path':name,'http_status':status,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'size_bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'headers':headers,'matches':matches}
 except Exception as e:return {'url':url,'error':type(e).__name__+': '+str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for r in pool.map(get,paths):records.append(r)
receipt={'scope':'Live root/app registered files, primer, and two previously supplied historical pages; not an exhaustive server inventory','source_base_url':base,'registered_document_count':8,'records':records,'physical_promotion':0,'independent_review':'pending','missing_attachments':['image(1).png','Gap2_FINAL_Finite_Genesis.png']}
(root/'SOURCE_SCAN.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'requested':len(paths),'fetched':sum('error' not in r for r in records),'failed':[r for r in records if 'error' in r],'matches':[{k:r[k] for k in ['url','matches']} for r in records if r.get('matches')]},indent=2))
