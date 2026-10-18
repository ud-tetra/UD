"""Fresh exact source construction and static coverage audit; archived runners never executed."""
import ast
import csv
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
from exact_selector_check import verify, mul, tr, z, eye, scale, add, SIM

ROOT = Path(__file__).parent

def parse_decimal(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return D(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        v = parse_decimal(node.operand)
        return -v if isinstance(node.op, ast.USub) else v
    if isinstance(node, ast.BinOp):
        a, b = parse_decimal(node.left), parse_decimal(node.right)
        if isinstance(node.op, ast.Add): return a+b
        if isinstance(node.op, ast.Sub): return a-b
        if isinstance(node.op, ast.Mult): return a*b
        if isinstance(node.op, ast.Div): return a/b
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'sqrt' and len(node.args) == 1 and not node.keywords:
        return parse_decimal(node.args[0]).sqrt()
    raise ValueError('non-arithmetic source expression')

def dm(a, b):
    return [[sum((x*y for x,y in zip(row,col)), D(0)) for col in zip(*b)] for row in a]

def numeric_csv_check(a, p0, p1):
    with localcontext() as ctx:
        ctx.prec = 100
        threshold = D('1e-85') # Numerical cross-check only; not a certified interval bound.
        cv = lambda q: D(q.numerator)/D(q.denominator)
        root = D(8065).sqrt()
        projector = [[cv(x)+root*cv(y) for x,y in zip(row,other)] for row,other in zip(p0,p1)]
        alpha = (D(1)+D(89)/root)/2
        u = [[D(0)]*3 for _ in range(30)]
        seeds = [[1,-1,0,0], [1,1,-2,0], [1,1,1,-3]]
        for k, den in enumerate([2,6,12]):
            for i,value in enumerate(seeds[k]): u[i][k] = D(value)/D(den).sqrt()
        q = [[x/alpha.sqrt() for x in row] for row in dm(projector,u)]
        p = [[x/D(5).sqrt() for x in row] for row in dm([[cv(x) for x in row] for row in a],q)]
        w = [x+y for x,y in zip(q,p)]
        rows = list(csv.DictReader((ROOT/'sources/UD_PACHNER_EVENT_DARBOUX_BASIS_v0.1.csv').open()))
        assert len(rows) == 30
        residual = D(0)
        for i,row in enumerate(rows):
            assert tuple(map(int,row['simplex'])) == SIM[i]
            for j,key in enumerate(['Q1_exact','Q2_exact','Q3_exact','P1_exact','P2_exact','P3_exact']):
                v = parse_decimal(ast.parse(row[key],mode='eval').body)
                residual = max(residual,abs(v-w[i][j]))
        assert residual < threshold
        return {'classification':'NUMERICAL_DIAGNOSTIC_NOT_INTERVAL_CERTIFICATE',
                'decimal_precision':100, 'max_entry_residual':str(residual),
                'predeclared_threshold':str(threshold)}

def literal_test_keys(text):
    tree = ast.parse(text)
    keys = set()
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys |= {x.value for x in node.keys if isinstance(x,ast.Constant) and isinstance(x.value,str)}
        if isinstance(node,ast.Subscript) and isinstance(node.value,ast.Name) and node.value.id == 'tests' and isinstance(node.slice,ast.Constant):
            keys.add(node.slice.value)
    return sorted(keys)

def main():
    exact,(a,p0,p1) = verify()
    inventory = json.loads((ROOT/'SOURCE_INVENTORY.json').read_text())
    for entry in inventory:
        b = (ROOT/entry['local']).read_bytes()
        expected = entry.get('sha256') or entry['provenance']['sha256']
        assert hashlib.sha256(b).hexdigest() == expected
    # Exact zero-residual fixtures satisfying the runners' written equations.
    w = [row[:6] for row in eye(30)]
    t = tr(w)
    r = [[F((1 if i<3 else -1) if i==j else 0) for j in range(6)] for i in range(6)]
    theta = mul(mul(w,r),t)
    assert mul(t,w) == eye(6) and mul(t,theta) == mul(r,t)
    j = [[F(-1) if col==row+3 else F(1) if row==col+3 else F(0) for col in range(6)] for row in range(6)]
    swap = [[F(col==(row+3)%6) for col in range(6)] for row in range(6)]
    assert mul(mul(r,j),r) == scale(j,-1)
    assert mul(mul(swap,r),swap) == scale(r,-1)
    assert mul(mul(a,a),w) != scale(w,-5) # Supplied W is not admitted to the claimed Hodge frequency sector.
    bad_ic = [[F((2 if i<3 else 3) if i==j else 0) for j in range(6)] for i in range(6)]
    assert mul(r,bad_ic) == mul(bad_ic,r)
    expected_ic = [[F((2 if i<3 else F(1,2)) if i==j else 0) for j in range(6)] for i in range(6)]
    assert bad_ic != expected_ic
    sources = ROOT/'sources'
    ckeys = literal_test_keys((sources/'UD_PARITY_CARRIER_CRL2C_RUNNER_v0.1.py').read_text())
    dtext = (sources/'UD_PARITY_CARRIER_CRL2D_REPLICATION_RUNNER_v0.1.py').read_text()
    dkeys = literal_test_keys(dtext)
    assert 'Q121_commutation' in ckeys and 'Ic_definition' not in ckeys
    assert 'Ic_definition' in dkeys
    assert not any(k in dkeys for k in ['native_A','selected_projector','full_composite'])
    # AST inspection does not execute imported code. c>0 is absent from the explicit premise expression.
    tree = ast.parse(dtext)
    assert not any(isinstance(n,ast.Compare) and isinstance(n.left,ast.Name) and n.left.id=='c' for n in ast.walk(tree))
    result = {'status':'PASS', 'exact_source_selector':exact,
              'csv_component_comparison':numeric_csv_check(a,p0,p1),
              'runner_static_test_keys':{'CRL2C':ckeys,'CRL2D':dkeys},
              'fresh_counterexamples':['orthonormal supplied W satisfies parity identities but not A^2 W=-5W',
                                       'commuting diag(2I,3I) is outside the reciprocal family and is caught by the added D-definition check'],
              'coverage_limits':['neither runner checks native A or selected projector membership',
                                 'neither runner checks the repaired full typed composite',
                                 'D explicitly checks reciprocal family but does not explicitly guard c>0'],
              'archived_runners_executed':False,'independent_review':False,'physical_promotion':0}
    print(json.dumps(result))

if __name__ == '__main__': main()
