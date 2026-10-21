"""Inventory every recovered row; scoped action-unit audit, no global unit inference."""
import collections,csv,hashlib,json,re
from fractions import Fraction
from pathlib import Path

here=Path(__file__).resolve().parent
p=here/'library_LEDGER_v0.85.json';data=p.read_bytes();d=json.loads(data);rows=d['rows'];by={r['id']:r for r in rows}
assert data==(here/'portal_LEDGER_v0.85.json').read_bytes()
assert hashlib.sha256(data).hexdigest()=='8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec'
assert d['typed_objects']==len(rows)==len(by)==723
fields=['id','symbol','exact_form','claim_bin','status','next_gate','use_class','claim_bin_meaning','display_symbol','reconciliation_notes']
assert all(all(k in r and isinstance(r[k],str) for k in fields) for r in rows)
assert all(all(r[k].strip() for k in fields if k!='reconciliation_notes') for r in rows)
bins=dict(collections.Counter(r['claim_bin'] for r in rows));names=dict(collections.Counter(re.match('[A-Z]+',r['id'])[0] for r in rows))
assert bins==d['claim_bin_counts'];assert names==d['namespace_counts'];assert d['physical_promotion']==0
assert by['O14']['exact_form']=='A_0/hbar; equivalently A_0 = eta_A hbar'
assert '[B_0]=M' in by['O15']['exact_form']
assert by['Q288']['claim_bin']=='QUARANTINED_CANDIDATE'
assert by['Q287']['claim_bin']=='QUARANTINED_CANDIDATE'
assert 'POSTULATED_BRIDGE' in by['Q287']['status']
assert '2=2/1' in by['Q288']['exact_form']
assert by['O55']['status']=='FROZEN PRETARGET / NO EMPIRICAL SCORE'
# Dimension vectors M,L,T, under explicit native length/time interpretation.
dim={'A0':(1,2,-1),'hbar':(1,2,-1),'B0':(1,0,0),'a0':(0,1,0),'tau0':(0,0,1),'eta_A':(0,0,0),'xi_phys_native':(0,0,0),'xi_native_phys':(0,0,0)}
assert tuple(b+2*a-t for b,a,t in zip(dim['B0'],dim['a0'],dim['tau0']))==dim['A0']
assert tuple(a-h for a,h in zip(dim['A0'],dim['hbar']))==dim['eta_A']
assert Fraction(1,2)*2==1 # I/(pi) for unit support and 2*pi lifted phase.
assert 'A_0 = xi_hbar^[native/phys] hbar = 1/xi_hbar^[phys/native]' in by['O13']['exact_form']
assert dim['A0']!=dim['xi_phys_native'] # Literal final equality in O13 fails.
overlay={'source_sha256':hashlib.sha256(data).hexdigest(),'row_id':'O13','operation':'APPEND_ONLY_CORRECTION_PROPOSAL','original_exact_form':by['O13']['exact_form'],'replacement_equalities':['xi_hbar[native/phys] = A0/hbar','xi_hbar[native/phys] = 1/xi_hbar[phys/native]','A0 = xi_hbar[native/phys]*hbar'],'assumptions':['hbar != 0','A0 != 0 for reciprocal identity','A0 and hbar have action dimensions'],'status':'CONSTRUCTOR_CHECKED; NON_CONSTRUCTOR_REVIEW_PENDING','physical_promotion':0}
(here/'O13_CORRECTION_OVERLAY.json').write_text(json.dumps(overlay,indent=2)+'\n')
with (here/'ROW_COVERAGE.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','claim_bin','schema','dimension_status'])
 for r in rows:w.writerow([r['id'],r['claim_bin'],'PASS','LITERAL_CHAIN_DEFECT' if r['id']=='O13' else 'NOT_GLOBALLY_TYPED_FROM_PROSE'])
out={'status':'INVENTORY_PASS__EXIT03_HOLD','source_sha256':hashlib.sha256(data).hexdigest(),'rows_scanned':len(rows),'unique_ids':len(by),'schema_pass':723,'claim_bin_histogram_pass':True,'namespace_histogram_pass':True,'literal_action_dimension_defects':['O13'],'structured_dimension_fields_present':0,'full_dimensional_typecheck':'NOT_COMPLETED; prose expressions lack structured unit/dependency schema','EXIT03_specification':'NOT_RECOVERED_IN_DECLARED_ARCHIVE_TEXT_SEARCH','QPB1_eta_A_prediction':'2/1; QUARANTINED_CANDIDATE, not measured normalization','primitive_holonomy_derivation':'NOT_INDEPENDENTLY_REPRODUCED','physical_promotion':0}
(here/'PREFLIGHT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
