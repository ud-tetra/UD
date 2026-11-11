import itertools,json,math,re
from fractions import Fraction
from pathlib import Path
root=Path(__file__).parent
ids=['P01','P02','P03','P04','P05','P06','P07','P08','P09','C01','C03']
text=(root/'20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md').read_text()
old={}
for line in text.splitlines():
 parts=[p.strip() for p in line.split('|')[1:-1]]
 if parts and parts[0] in ids:
  # Escaped vertical bars in P03/P04 symbols affect column positions.
  old[parts[0]]=line
new={r['id']:r for r in json.loads((root/'UD_COEFFICIENT_PROVENANCE_LEDGER_v0.85_OPTICAL_NOISE_RECONCILIATION.json').read_text())['rows']}
assert set(old)==set(ids)
for key in ids:
 for field in ['exact_form','claim_bin','status','next_gate']:
  assert new[key][field] in old[key],(key,field)
perms=list(itertools.permutations(range(4)));bits=list(itertools.product([0,1],repeat=3))
assert len(perms)==24 and len(bits)==8
for p in perms:
 assert {tuple(sorted((p[i],p[j]))) for i in range(4) for j in range(i+1,4)}=={(i,j) for i in range(4) for j in range(i+1,4)}
r=Fraction(len(bits)-1,len(perms)*len(bits))
assert r==Fraction(7,192) and r/4==Fraction(7,768)
assert r/12==Fraction(7,2304) and (r/4)/(r/12)==3
assert math.gcd(7,768)==1
print(json.dumps({'status':'PASS','source_rows_compared':ids,'K4_automorphisms_enumerated':len(perms),'declared_Theta_bitstrings_enumerated':len(bits),'r_Delta':str(r),'default_conditional_ratio':str(r/4),'dense_conditional_control':str(r/12),'verification_scope':'arithmetic, K4 permutations, declared bitstring count, cross-ledger field consistency; no reference-state predicate or selector replay','independent_review':'pending','physical_promotion':0},indent=2))
