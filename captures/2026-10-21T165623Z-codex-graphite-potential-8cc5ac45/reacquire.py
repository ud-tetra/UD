from pathlib import Path
import urllib.request,json,hashlib
p=Path(__file__).parent
root='https://raw.githubusercontent.com/lammps/lammps/8de817dd79bfe4525d5d39246a212d833e6dee07/'
urls={'CH_taper.KC':root+'potentials/CH_taper.KC','pair_kolmogorov_crespi_full.cpp':root+'src/INTERLAYER/pair_kolmogorov_crespi_full.cpp','data.zip':'https://zenodo.org/records/14283098/files/data.zip?download=1','lammps_relax_bond.tar.gz':'https://zenodo.org/records/14283098/files/lammps_relax_bond.tar.gz?download=1'}
expected=json.loads((p/'RESULTS.json').read_text())['source_files']
for name,url in urls.items():
 data=urllib.request.urlopen(url,timeout=45).read()
 assert hashlib.sha256(data).hexdigest()==expected[name]['sha256'],name+' source mismatch'
 (p/name).write_bytes(data)
 print(name,'verified')
