"""Exact symbolic majorants on the CD-1 preparation box."""
import json
import sympy as s
t=s.symbols('t0:4',real=True);E=s.symbols('E0:4',real=True)
x=s.symbols('x0:4',real=True);y=s.symbols('y0:4',real=True)
u=s.symbols('u0:4',real=True);v=s.symbols('v0:4',real=True)
q=list(t+x+u);p=list(E+y+v);z=list(t+E+x+y+u+v)
b=[-1,1,-1,-1];c=[1,1,-1,-1]
R=s.Matrix([[1,0,1,0],[-1,1,0,0],[0,0,-1,1],[0,-1,0,-1]])
edges=[(0,1),(1,3),(0,2),(2,3)]
phi=sum(c[i]*t[i] for i in range(4))
H=sum(a*a for a in E)/2+s.Rational(1,16)*(1-s.cos(phi))
for e,(i,j) in enumerate(edges):
    H+=b[e]*((x[i]*x[j]+y[i]*y[j]+u[i]*u[j]+v[i]*v[j])*s.sin(t[e])+
      (x[i]*y[j]-y[i]*x[j]+v[i]*u[j]-u[i]*v[j])*s.cos(t[e]))
def pb(f,h):return s.expand(sum(s.diff(f,Q)*s.diff(h,P)-s.diff(f,P)*s.diff(h,Q) for Q,P in zip(q,p)))
field=s.Matrix([pb(a,H) for a in z])
limits=[s.Rational(1,100)]*4+[s.Rational(1,50)]*4+[s.Rational(3,4)]*4+[s.Rational(1,50)]*4+[s.Rational(3,4)]*4+[s.Rational(1,50)]*4
def bound(expr):
    expr=s.expand(expr);atoms=sorted(expr.atoms(s.sin,s.cos),key=str)
    aa=s.symbols('a:'+str(len(atoms)));extra=[]
    for a in atoms:
        if a.func==s.cos:extra.append(s.Integer(1))
        else:
            poly=s.Poly(a.args[0],*z)
            val=0
            for powers,coef in poly.terms():
                mon=abs(coef)
                for lim,k in zip(limits,powers):mon*=lim**k
                val+=mon
            extra.append(min(s.Integer(1),val))
    poly=s.Poly(expr.xreplace(dict(zip(atoms,aa))),*(z+list(aa)))
    val=0
    for powers,coef in poly.terms():
        mon=abs(coef)
        for lim,k in zip(limits+extra,powers):mon*=lim**k
        val+=mon
    return val
J=field.jacobian(z)
rows=[sum(bound(J[i,j]) for j in range(24)) for i in range(24)]
speeds=[bound(a) for a in field]
G=R*s.Matrix(E)-s.Matrix([(x[i]**2+y[i]**2)/2 for i in range(4)])+s.Matrix([(u[i]**2+v[i]**2)/2 for i in range(4)])
grows=[sum(bound(s.diff(G[i],a)) for a in z) for i in range(4)]
assert max(rows)<4
assert max(speeds)==s.Rational(3751,2500)
assert max(grows)==s.Rational(177,50)<4
assert max(speeds)+s.Rational(1,100)<s.Rational(8,5)
wrong=field.copy()
for j in range(16,24):wrong[j]=-wrong[j]
frozen=field.copy()
for j in range(4,8):frozen[j]=0
for F in [wrong,frozen]:
    assert max(sum(bound(s.diff(F[i],a)) for a in z) for i in range(24))<=max(rows)
    assert max(bound(a) for a in F)<=max(speeds)
print(json.dumps({'status':'PASS','method':'exact polynomial majorants; abs(sin linear phase)<=abs linear phase, abs(cos)<=1',
 'Jacobian_row_bounds':[str(a) for a in rows],'max_Jacobian':str(max(rows)),
 'speed_bounds':[str(a) for a in speeds],'max_target_speed':str(max(speeds)),
 'Gauss_rows':[str(a) for a in grows],'adopted_L':'4','adopted_Gauss_L':'4','adopted_actual_speed':'8/5',
 'all_three_laws_share_bounds':True,'physical_promotion':0},indent=2))
