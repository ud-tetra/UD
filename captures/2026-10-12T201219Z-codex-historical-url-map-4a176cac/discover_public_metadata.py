import argparse,urllib.request,concurrent.futures,json,datetime
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path,required=True);args=parser.parse_args()
if args.destination.exists():raise FileExistsError('Choose a new destination')
args.destination.mkdir(parents=True)
base='https://stablerelease.me'
paths=['/robots.txt','/sitemap.xml','/sitemap_index.xml','/UD/source/','/UD/content/']
def get(path):
 u=base+path
 try:
  with urllib.request.urlopen(u,timeout=15) as r:b=r.read();status=r.status;final=r.url
  p=(args.destination/'discovery')/path.lstrip('/');p=p/'index.html' if path.endswith('/') else p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
  return {'url':u,'status':status,'final_url':final,'bytes':len(b),'local_path':str(p),'text':b.decode('utf-8',errors='replace')[:20000]}
 except Exception as e:return {'url':u,'error':type(e).__name__+': '+str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rs=list(pool.map(get,paths))
(args.destination/'discovery.json').write_text(json.dumps(rs,indent=2)+'\n')
for r in rs:print(json.dumps({k:v for k,v in r.items() if k!='text'}));print(r.get('text','')[:1000])
