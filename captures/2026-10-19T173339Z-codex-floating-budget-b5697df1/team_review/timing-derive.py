"""Same-team numerical source-frame ceiling; no fits or estimator execution."""
import hashlib,json
from pathlib import Path
from fractions import Fraction
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
ROOT=P.parent
paths={
 'allowance':ROOT/'source-shift-work/SOURCE_ALLOWANCE.json',
 'uniform':ROOT/'source-weighted-work/inputs/PARENT_UNIFORM.json',
 'normal':ROOT/'wholeball-shift-work/NORMAL_CERTIFICATES.json',
}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def a(v): return arb(fmpq(int(v[0]),int(v[1])))
def bound(v,up):
 n=(v*(1<<180)).ceil().unique_fmpz() if up else (v*(1<<180)).floor().unique_fmpz()
 assert n is not None
 return [int(n),1<<180]
f=json.loads((P/'INPUT_FREEZE.json').read_text())
assert f['code_sha256']==sha(Path(__file__))
assert f['inputs_sha256']=={k:sha(v) for k,v in paths.items()}
u=json.loads(paths['uniform'].read_text())
g=json.loads(paths['allowance'].read_text())
rows=json.loads(paths['normal'].read_text())['rows']
nupair=max((r['normal_residual_F_upper'] for r in rows),key=lambda x:Fraction(int(x[0]),int(x[1])))
A=a(g['raw_shift_strict_upper_allowance_lower'])
eta=a(g['other_seven_gates']['full_left_orthogonality'])
nu=a(nupair);beta=a(u['deleted_two_rows_beta_lower'])
sigma=a(u['comparison_shift_residual_upper']);M=a(u['comparison_shift_norm_upper'])
h=(1+eta).sqrt();gg=(1-eta).sqrt()
B=(A*A-(2*nu/(gg*beta))**2).sqrt()
D=(B/h-sigma)/(1+M)
assert B>h*sigma and D>0 and D<beta/2 and D<arb(2).sqrt()
S=D*(1-D*D/4).sqrt();safe=bound(S,False);ss=a(safe)
dist=(2-2*(1-ss*ss).sqrt()).sqrt()
J=h*(sigma+(1+M)*dist)
amin=gg*(beta-dist)
returned=(J*J+(nu/amin)**2).sqrt()
assert dist<D and returned<A
result={
 'status':'CERTIFIED_SAME_TEAM_ARCHIVED_SOURCE_FRAME_CEILING',
 'input_sha256':f['inputs_sha256'],
 'normal_upper_scope_cases':[r['case'] for r in rows],
 'normal_F_upper':list(map(int,nupair)),
 'retained_Gram_F_cap':g['other_seven_gates']['full_left_orthogonality'],
 'safe_sinTheta_F_strict_upper_ceiling':safe,
 'source_frame_residual_F_strict_upper_ceiling':bound(ss*gg,False),
 'returned_shift_upper_at_ceiling':bound(returned,True),
 'published_allowance_lower':g['raw_shift_strict_upper_allowance_lower'],
 'strict_shift_allowance_pass':bool(returned<A),
 'readable':{'sinTheta_F_ceiling_lower':float(ss.lower()),'raw_source_frame_residual_ceiling_lower':float((ss*gg).lower()),'returned_shift_upper':float(returned.upper())},
 'not_a_future_normal_residual_guarantee':True,
 'no_actual_basis_alignment_computed':True,
 'no_all_other_gates_or_uniform_solver_success_claim':True,
 'physical_promotion':0,
}
(P/'CEILING_CERTIFICATE.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
