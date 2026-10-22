import pathlib,urllib.request,concurrent.futures,hashlib,json
root=pathlib.Path(__file__).parent
specs=[('lammps_21.tar.gz',519350839,'d5f22f8d020936a9227c8005609460b1'),('lammps_31.tar.gz',724916000,'531242422071cd9a08d2a3296d633404')]
# Discover exact size using a byte-range response; never trust rounded record display.
for name,_,md5 in specs:
 u='https://zenodo.org/records/14283098/files/'+name+'?download=1'
 with urllib.request.urlopen(urllib.request.Request(u,headers={'Range':'bytes=0-0'}),timeout=30) as r:
  assert r.status==206; total=int(r.headers['Content-Range'].split('/')[-1]);r.read()
 chunk=16*1024*1024;out=root/(name+'.ranges');out.mkdir(exist_ok=True)
 def fetch(i):
  lo=i*chunk;hi=min(total,lo+chunk)-1;p=out/str(i)
  if p.exists() and p.stat().st_size==hi-lo+1:return
  with urllib.request.urlopen(urllib.request.Request(u,headers={'Range':f'bytes={lo}-{hi}'}),timeout=45) as r:
   assert r.status==206
   with p.open('wb') as f:
    while True:
     b=r.read(1024*1024)
     if not b:break
     f.write(b)
  assert p.stat().st_size==hi-lo+1
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(fetch,range((total+chunk-1)//chunk)))
 h=hashlib.md5()
 with (root/name).open('wb') as f:
  for i in range((total+chunk-1)//chunk):
   b=(out/str(i)).read_bytes();h.update(b);f.write(b)
 assert h.hexdigest()==md5
 print(json.dumps({'name':name,'size':total,'md5':h.hexdigest(),'verified':True}),flush=True)
