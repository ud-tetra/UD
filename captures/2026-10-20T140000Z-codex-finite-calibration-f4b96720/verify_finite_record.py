"""Exact symbolic norm bounds for the proposed local CD-1 certificate."""
import json
import sympy as s
t=s.symbols('t0:4',real=True);E=s.symbols('E0:4',real=True)
x=s.symbols('x0:4',real=True);y=s.symbols('y0:4',real=True)
u=s.symbols('u0:4',real=True);v=s.symbols('v0:4',real=True)
q=list(t+x+u);p=list(E+y+v);z=list(t+E+x+y+u+v)
b=[-1,1,-1,-1];c=s.Matrix([1,1,-1,-1])
R=s.Matrix([[1,0,1,0],[-1,1,0,0],[0,0,-1,1],[0,-1,0,-1]])
edges=[(0,1),(1,3),(0,2),(2,3)]
phi=sum(c[i]*t[i] for i in range(4))
H=sum(a*a for a in E)/2+s.Rational(1,16)*(1-s.cos(phi))
for e,(i,j) in enumerate(edges):
    H+=b[e]*((x[i]*x[j]+y[i]*y[j]+u[i]*u[j]+v[i]*v[j])*s.sin(t[e])+
       (x[i]*y[j]-y[i]*x[j]+v[i]*u[j]-u[i]*v[j])*s.cos(t[e]))
def pb(f,h):return s.expand(sum(s.diff(f,Q)*s.diff(h,P)-s.diff(f,P)*s.diff(h,Q) for Q,P in zip(q,p)))
field=s.Matrix([pb(a,H) for a in z])
G=R*s.Matrix(E)-s.Matrix([(x[i]**2+y[i]**2)/2 for i in range(4)])+s.Matrix([(u[i]**2+v[i]**2)/2 for i in range(4)])
def bound(expr):
    expr=s.expand(expr)
    atoms=sorted(expr.atoms(s.sin,s.cos),key=str)
    aa=s.symbols('a:'+str(len(atoms)))
    expanded=expr.xreplace(dict(zip(atoms,aa)))
    P=s.Poly(expanded,*(z+list(aa)))
    return sum(abs(coef) for _,coef in P.terms())
J=field.jacobian(z)
rows=[sum(bound(J[i,j]) for j in range(24)) for i in range(24)]
speeds=[bound(f) for f in field]
gauss_rows=[sum(bound(s.diff(G[i],a)) for a in z) for i in range(4)]
assert max(rows)==s.Rational(97,4)
assert max(speeds)==s.Rational(129,16)
assert gauss_rows==[6]*4
wrong=field.copy()
for j in range(16,24):wrong[j]=-wrong[j]
frozen=field.copy()
for j in range(4,8):frozen[j]=0
for F in [wrong,frozen]:
    assert max(sum(bound(s.diff(F[i],a)) for a in z) for i in range(24))<=s.Rational(97,4)
def along(f,F):return s.expand(sum(s.diff(f,a)*F[j] for j,a in enumerate(z)))
assert all(s.simplify(along(G[i],field))==0 for i in range(4))
jw=[]
for e,(i,j) in enumerate(edges):
    jw.append(b[e]*((u[i]*u[j]+v[i]*v[j])*s.cos(t[e])-
                   (v[i]*u[j]-u[i]*v[j])*s.sin(t[e])))
assert all(s.simplify(along(G[i],wrong)+2*(R*s.Matrix(jw))[i])==0 for i in range(4))
# Frozen-electric exact propagator uses A^2=-2I.
D=s.zeros(4)
for e,(i,j) in enumerate(edges):D[i,j]=b[e]
A=D.T-D;uu=s.ones(4,1)/2
assert A*A==-2*s.eye(4)
assert A*uu==s.Matrix([1,-1,0,0])
zero_phase=dict(zip(list(t+E),[0]*8))
matter_psi=s.Matrix([(field[8+i]+s.I*field[12+i])/s.sqrt(2) for i in range(4)])
matter_w=s.Matrix([(field[16+i]-s.I*field[20+i])/s.sqrt(2) for i in range(4)])
psi_raw=s.Matrix([(x[i]+s.I*y[i])/s.sqrt(2) for i in range(4)])
w_raw=s.Matrix([(u[i]-s.I*v[i])/s.sqrt(2) for i in range(4)])
assert s.simplify(matter_psi.subs(zero_phase)-A*psi_raw)==s.zeros(4,1)
assert s.simplify(matter_w.subs(zero_phase)+A*w_raw)==s.zeros(4,1)
cc,ss=s.symbols('cc ss',real=True)
psi=cc*uu+ss/s.sqrt(2)*(A*uu)
w=cc*uu-ss/s.sqrt(2)*(A*uu)
expected=s.Matrix([-s.sqrt(2)*cc*ss,s.sqrt(2)*cc*ss,0,0])
assert s.simplify(s.Matrix([w[i]**2-psi[i]**2 for i in range(4)])-expected)==s.zeros(4,1)
result={'status':'PASS','L':str(max(rows)),'speed_target':str(max(speeds)),
        'Gauss_L':6,'Jacobian_row_bounds':[str(a) for a in rows],
        'speed_component_bounds':[str(a) for a in speeds],
        'wrong_sign_source_identity':True,'frozen_electric_exact_propagator':True,
        'nominal_Gauss_identity':True,'frozen_matter_generator_signs':True,
        'fault_laws_share_bounds':True,'verification_kind':'exact symbolic constructor majorants and identities',
        'physical_promotion':0}
print(json.dumps(result,indent=2))
