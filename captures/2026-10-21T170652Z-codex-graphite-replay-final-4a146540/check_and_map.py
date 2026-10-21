import pathlib,tarfile,hashlib,json,math,zipfile
root=pathlib.Path(__file__).parent
spec=[('21','d5f22f8d020936a9227c8005609460b1'),('31','531242422071cd9a08d2a3296d633404')];custody=[]
for pat,expected in spec:
 p=root/f'lammps_{pat}.tar.gz';h=hashlib.md5();h2=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b);h2.update(b)
 assert h.hexdigest()==expected
 custody.append({'pattern':pat,'archive':p.name,'md5':h.hexdigest(),'sha256':h2.hexdigest(),'size_bytes':p.stat().st_size})
 # Restore exact originally selected cases, not additional target-conditioned selection.
 names=['dir_0','dir_10024'] if pat=='21' else ['dir_10084','dir_10134']
 wanted={f'structure_{pat}_pes/{n}/{f}' for n in names for f in ['input','struct.inp.data','log.lammps','Output.out']}
 wanted.add(f'structure_{pat}_pes/dir_0/struct.inp.data')
 with tarfile.open(p,'r|gz') as t:
  for m in t:
   if m.isfile() and m.name in wanted:
    parts=pathlib.PurePosixPath(m.name).parts;out=root/'selected'/pat/parts[-2]/parts[-1];out.parent.mkdir(parents=True,exist_ok=True);b=t.extractfile(m).read()
    if out.exists():assert out.read_bytes()==b
    else:out.write_bytes(b)
# Exploratory source-to-grid coordinate reconciliation after energy replay.
def firsttop(p):
 rows=[l.split() for l in p.read_text().split('Atoms')[1].strip().splitlines() if l.strip()]
 return next(list(map(float,r[4:7])) for r in rows if r[1]=='2')
rr=json.loads((root/'REPLAY_RESULTS.json').read_text())['results'];maps=[]
with zipfile.ZipFile(root.parent/'graphite-potential-audit/data.zip') as z:
 for pat,m,n in [('21',2,1),('31',3,1)]:
  rows=[list(map(float,l.split())) for l in z.read(f'data/PES{pat}/pes_{pat}.dat').decode().splitlines()]
  c=(m*m+4*m*n+n*n)/(2*(m*m+m*n+n*n));phi=math.pi/6-math.acos(c)/2
  origin=firsttop(root/'selected'/pat/'dir_0'/'struct.inp.data')
  selected=[r for r in rr if r['pattern']==pat]
  vals=[]
  for r in selected:
   i=int(r['case'].split('_')[1]);x=(i%151)*.02;y=(i//151)*.02
   actual=firsttop(root/'selected'/pat/r['case']/'struct.inp.data');dx=actual[0]-origin[0];dy=actual[1]-origin[1]
   xp=dx*math.cos(phi)-dy*math.sin(phi);yp=dx*math.sin(phi)+dy*math.cos(phi)
   assert abs(xp-x)<1e-10 and abs(yp-y)<1e-10
   value=next(row[2] for row in rows if abs(row[0]-x)<1e-12 and abs(row[1]-y)<1e-12);vals.append(value)
   maps.append({'pattern':pat,'case':r['case'],'x_A':x,'y_A':y,'coordinate_rotation_error_A':max(abs(xp-x),abs(yp-y)),'grid_microeV_per_atom':value})
  replay_delta=(selected[1]['replayed_pe_eV']-selected[0]['replayed_pe_eV'])/(selected[0]['atoms']/2)*1e6
  maps.append({'pattern':pat,'comparison':'energy difference per atom of one layer','replay_delta_microeV_per_atom':replay_delta,'grid_delta_microeV_per_atom':vals[1]-vals[0],'difference_microeV_per_atom':replay_delta-(vals[1]-vals[0]),'status':'exploratory coordinate reconciliation; no predeclared grid tolerance'})
(root/'CUSTODY_AND_GRID.json').write_text(json.dumps({'archive_custody':custody,'grid_mapping':maps,'physical_promotion':0},indent=2)+'\n');print(json.dumps({'custody_verified':True,'grid_mapping':maps},indent=2))
