from pathlib import Path
from fractions import Fraction as F
import hashlib,json,zipfile,tarfile
p=Path(__file__).parent
files=['CH_taper.KC','pair_kolmogorov_crespi_full.cpp','data.zip','lammps_relax_bond.tar.gz']
assert hashlib.md5((p/'data.zip').read_bytes()).hexdigest()=='ea3fd75cd88e4c405c14b6cc89ce473c'
assert hashlib.md5((p/'lammps_relax_bond.tar.gz').read_bytes()).hexdigest()=='04ef40c563d2d13c47d90e3afbbef747'
source=(p/'pair_kolmogorov_crespi_full.cpp').read_text()
assert '1.0e-3 * params[nparams].S' in source
assert 'calc_normal();' in source and 'dnormdri' in source and 'calc_dTap' in source
row=next(x for x in (p/'CH_taper.KC').read_text().splitlines() if x.startswith('C C'))
a=list(map(F,row.split()[2:]));assert len(a)==10
assert a[8]==1 and a[9]==2
assert a[1]/1000==F('0.020021583')
coef=[1,0,0,0,-35,84,-70,20]
def derivative(c):return [i*c[i] for i in range(1,len(c))]
def evaluate(c,x):return sum(v*x**i for i,v in enumerate(c))
assert evaluate(coef,F(0))==1 and evaluate(coef,F(1))==0
c=coef
for j in range(1,4):
 c=derivative(c);assert evaluate(c,F(0))==0 and evaluate(c,F(1))==0
ranges={}
with zipfile.ZipFile(p/'data.zip') as z:
 for name in z.namelist():
  if name.endswith('.dat'):
   rows=[list(map(F,line.split())) for line in z.read(name).decode().splitlines() if line.strip()]
   vals=[r[2] for r in rows];assert len(rows)==22801 and all(len(r)==3 for r in rows)
   assert len({(r[0],r[1]) for r in rows})==len(rows)
   ranges[name]={'rows':len(rows),'min_microeV_per_atom':str(min(vals)),'max_microeV_per_atom':str(max(vals)),'range_microeV_per_atom':str(max(vals)-min(vals))}
with tarfile.open(p/'lammps_relax_bond.tar.gz') as t:
 inputs=[x for x in t.getmembers() if x.isfile() and x.name.endswith('/input')]
 texts=[t.extractfile(x).read().decode() for x in inputs]
 assert all('pair_style rebo' in x for x in texts)
 # This archive optimizes intralayer bond length; it does not establish interlayer input.
 info={'input_files':len(inputs),'intralayer_only':'pair_style rebo; commented KC line is not active'}
result={'status':'PASS_SCOPED_SOURCE_AND_DATA_AUDIT','source_files':{n:{'sha256':hashlib.sha256((p/n).read_bytes()).hexdigest(),'size_bytes':(p/n).stat().st_size} for n in files},'CC_parameters_raw':dict(zip(['z0','C0','C2','C4','C','delta','lambda','A','S','normal_neighbor_rcut'],map(str,a))),'checks':['meV to eV factor','normal derivatives present','taper derivatives 1-3 vanish at endpoints','two archive MD5 matches','grid row and coordinate uniqueness'],'PES_model_grids':ranges,'bond_archive':info,'material_hessian_computed':False,'physical_promotion':0}
(p/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
