import os,pathlib,json,re,hashlib,time
from lammps import lammps
root=pathlib.Path(__file__).resolve().parent
cases=[('21','dir_0'),('21','dir_10024'),('31','dir_10084'),('31','dir_10134')]
params=pathlib.Path('/workspace/scratch/9a7ae24f2263/lammps-runtime/lammps/share/lammps/potentials')
contract={'cases':cases,'energy_tolerance_eV_per_cell':1e-7,'selected_before_replay':True,'target':'archived final minimization E_pair, not held-out friction','runtime':'20250722','historical_runtime':'20221103','potential_hashes':{n:hashlib.sha256((params/n).read_bytes()).hexdigest() for n in ['CC.KC','CH.rebo']},'scope':'modern compatibility replay; original parameter bytes not recovered from scanned prefixes; checksum pending'}
(root/'REPLAY_FREEZE.json').write_text(json.dumps(contract,indent=2)+'\n')
results=[]
for pat,name in cases:
 p=root/'selected'/pat/name
 log=(p/'log.lammps').read_text()
 match=re.search(r'Energy initial, next-to-last, final =\s*\n\s*([^\n]+)',log)
 if not match:raise ValueError('no archived energy')
 target=float(match.group(1).split()[-1]);os.chdir(p)
 l=lammps(cmdargs=['-screen','none','-log','compatibility.log'])
 try:
  commands=['units metal','boundary p p p','atom_style full','box tilt large','read_data struct.inp.data','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z 16.0',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096','thermo_modify format float %18.18g','fix 2 all lineforce 0.0 0.0 1.0','min_style cg','min_modify dmax 0.005','minimize 1.0e-15 1.0e-15 30000 30000']
  for command in commands:l.command(command)
  actual=l.get_thermo('pe');n=l.get_natoms();delta=actual-target
  result={'pattern':pat,'case':name,'atoms':n,'archived_final_Epair_eV':target,'replayed_pe_eV':actual,'difference_eV':delta,'passes_frozen_tolerance':abs(delta)<=1e-7,'log_sha256':hashlib.sha256((p/'compatibility.log').read_bytes()).hexdigest()}
 except Exception as e:result={'pattern':pat,'case':name,'error':str(e),'passes_frozen_tolerance':False}
 finally:l.close()
 results.append(result);(root/'REPLAY_RESULTS.json').write_text(json.dumps({'results':results,'physical_promotion':0,'independent_review':'pending'},indent=2)+'\n');print(json.dumps(result),flush=True)
