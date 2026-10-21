"""Read source data only. Imported notebooks are parsed as JSON, never executed."""
from pathlib import Path
import csv,gzip,hashlib,io,json,sys,zipfile,xml.etree.ElementTree as ET
import numpy as np

HERE=Path(__file__).resolve().parent
INPUT=Path(sys.argv[1]) if len(sys.argv)>1 else HERE.parents[2]/'data-audit-inputs'
def sha(b):return hashlib.sha256(b).hexdigest()
def md5(b):return hashlib.md5(b).hexdigest()
sources=[]
def source(name,url,expected):
 p=INPUT/name;b=p.read_bytes();assert md5(b)==expected,name+' checksum'
 sources.append({'name':name,'url':url,'bytes':len(b),'md5':md5(b),'sha256':sha(b),'checksum_matches_declared_source':True})
 return b

b=source('rydberg_Data.zip','https://doi.org/10.5281/zenodo.18012627','ba2e952d6a35e79306f90e34d88eac92')
files=[];arrays={}
with zipfile.ZipFile(io.BytesIO(b)) as z:
 for n in z.namelist():
  if not n.endswith('.csv'):continue
  raw=z.read(n);rows=list(csv.reader(io.StringIO(raw.decode('utf-8-sig'))));a=np.array(rows,dtype=float)
  assert a.ndim==2 and np.isfinite(a).all()
  arrays[n]=a;files.append({'member':n,'rows':a.shape[0],'columns':a.shape[1],'sha256':sha(raw),'all_finite':True,'header':'No explicit text header; no column roles inferred from position alone'})
assert len(files)==27
top=arrays['Data/Figure2a_Top_OmegaT.csv'].ravel();bottom=arrays['Data/Figure2a_Bottom_OmegaT.csv'].ravel()
assert len(top)==21 and len(bottom)==42 and np.array_equal(bottom,np.tile(top,2))
rydberg={'archive_bytes':len(b),'csv_members':files,'time_axis_issue':{'top_length':21,'bottom_length':42,'bottom_equals_two_top_copies':True,'handling':'Preserve original 42 entries; collapse to 21 is a candidate documented preprocessing rule, not silently applied.'},'signed_meanZ_values':'Present negative expectations are not a signed field-quadrature or state-phase witness','action_anchor':'NOT_ESTABLISHED_IN_REVIEWED_RELEASE'}
(HERE/'RYDBERG_CONTENT_AUDIT.json').write_text(json.dumps(rydberg,indent=2)+'\n')

b=source('riechert_waveform.gz','https://heidata.uni-heidelberg.de/api/access/datafile/6385','81771941562f83818f3d905bd6f9e9e2')
d=np.loadtxt(gzip.open(io.BytesIO(b),'rt'));assert d.shape==(1000,16390) and np.isfinite(d).all()
assert np.unique(d[:,0]).tolist()==[1953125.0];channels,counts=np.unique(d[:,5],return_counts=True)
assert channels.tolist()==list(range(1,11)) and counts.tolist()==[100]*10
diagnostic=[]
for ch in range(1,10):
 r=d[d[:,5]==ch][0];v=r[206:];N=len(v);fs=r[0];window=np.hanning(N);f=np.fft.rfftfreq(N,1/fs)
 bins=[]
 for signal,lo,hi in [(v,10000,200000),(v*v,20000,400000)]:
  power=np.abs(np.fft.rfft((signal-signal.mean())*window))**2;band=np.flatnonzero((f>=lo)&(f<=hi));bins.append(int(band[np.argmax(power[band])]))
 diagnostic.append({'channel':ch,'record_index':0,'raw_peak_bin':bins[0],'squared_peak_bin':bins[1],'squared_minus_twice_raw_bins':bins[1]-2*bins[0],'raw_peak_hz':float(f[bins[0]]),'squared_peak_hz':float(f[bins[1]]),'frequency_ratio':float(f[bins[1]]/f[bins[0]])})
within=sum(abs(r['squared_minus_twice_raw_bins'])<=1 for r in diagnostic)
assert within==9
notebook=source('riechert_figures_original.ipynb','https://heidata.uni-heidelberg.de/api/access/datafile/6329?format=original','12371165255a9686eb4038b50b8b2e0c')
nb=json.loads(notebook);cell=''.join(nb['cells'][48]['source']);assert 'def energy(V, Verr, C=20e-9)' in cell and 'C/2 * V**2' in cell
acq=source('riechert_acquisition.md','https://heidata.uni-heidelberg.de/api/access/datafile/6322','573bc78abc98be01055b9a2e3eb1213b')
assert b'EXT_TRIG' in acq
riechert={'waveform_shape':list(d.shape),'sample_rate_hz':1953125,'metadata_columns':6,'samples_per_full_trace':16384,
 'signed_trace_available':True,'records_per_channel':100,'diagnostic':{'scope':'Exploratory descriptive first-record FFTs, nine live channels; not a blinded statistical or period certificate','cropped_initial_samples':200,'postcrop_samples':N,'fft_bin_hz':float(fs/N),'window':'Hann; subtract mean separately from V and V^2','raw_band_hz':[10000,200000],'squared_band_hz':[20000,400000],'channels_with_doubling_within_one_bin':within,'channels':diagnostic},
 'notebook_static_audit':{'cells':len(nb['cells']),'energy_cell_index_zero_based':48,'energy_cell_sha256':sha(cell.encode()),'energy_rule':'E_cap=C*V_envelope^2/2','default_C_farads':'20/1000000000','notebook_executed':False},
 'open_requirements':['Acquisition synchronization is documented, but inter-device phase-skew uncertainty not certified here','No absolute same-carrier M or UD support anchor established','No native-energy functional G/baseline and joint uncertainty certificate established','Five-site/four-link nonlinear chain is not the filled-tetrahedron active carrier','Fast carrier frequency is not automatically the native Hodge recurrence'],
 'QPB1':'The observed near-2 frequency ratio under squaring is unrelated to eta_A=2/1 and cannot score that bridge'}
(HERE/'CIRCUIT_CONTENT_AUDIT.json').write_text(json.dumps(riechert,indent=2)+'\n')

b=source('yang_Fig4.tab','https://dataverse.harvard.edu/api/access/datafile/4013035?format=original','3afdee6e74c00dacdc8217115e362f7d')
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'};sheets=[]
with zipfile.ZipFile(io.BytesIO(b)) as z:
 wb=ET.fromstring(z.read('xl/workbook.xml'));names=[s.attrib['name'] for s in wb.find('m:sheets',ns)]
 strings=[''.join(si.itertext()) for si in ET.fromstring(z.read('xl/sharedStrings.xml'))]
 for i,name in enumerate(names,1):
  tree=ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'));cells=[]
  for c in tree.findall('.//m:c',ns):
   v=c.find('m:v',ns);val=v.text if v is not None else ''
   if c.attrib.get('t')=='s':val=strings[int(val)]
   if val!='':cells.append((c.attrib['r'],val))
  sheets.append({'name':name,'nonempty_cells':len(cells),'headers':[(a,v) for a,v in cells if int(''.join(filter(str.isdigit,a)))<=3]})
assert len(sheets)==4 and sheets[0]['name']=='Exp Data_state population'
(HERE/'YANG_ORIGINAL_FORMAT_AUDIT.json').write_text(json.dumps({'format':'OOXML workbook, despite requested .tab filename','original_bytes':len(b),'tabs':sheets,'scope':'Original workbook XML read only; no workbook changed or exported','action_anchor':'NOT_ESTABLISHED_IN_REVIEWED_FILE'},indent=2)+'\n')
(HERE/'SOURCE_BYTES.json').write_text(json.dumps({'sources':sources,'note':'Raw waveform and full notebook are external inputs, not re-mirrored here. Dataset DOI/API and hashes pin their provenance. No imported code executed.','physical_promotion':0},indent=2)+'\n')
print(json.dumps({'status':'PASS_CONTENT_AUDIT','rydberg_csv_members':27,'circuit_live_channels_doubling_within_one_bin':within,'yang_workbook_tabs':len(sheets),'admitted_action_anchor_datasets':0,'physical_promotion':0}))
