"""Replay the hollow first-jet ranks with exact SymPy arithmetic."""
from pathlib import Path
import sys

from sympy import diag, zeros

prior_capture = Path(__file__).resolve().parents[1] / "2026-11-15T174000Z-codex-aw5-7cf191"
sys.dont_write_bytecode = True
sys.path.insert(0, str(prior_capture))
from aw5 import build, hub, leaves, skew

basis, ds = build(leaves)
visible = [s for layer in basis for s in layer]
hb, hd = build([hub])
shell = hb[:-1]
for blocks in ([build([t]) for t in leaves], [(shell, hd[:-1])]+[build([t]) for t in leaves]):
    generator = diag(*[skew(b,d) for b,d in blocks])
    P = zeros(len(visible), generator.rows)
    column = 0
    for b,_ in blocks:
        for layer in b:
            for s in layer:
                P[visible.index(s),column] = 1
                column += 1
    first = P.col_join(P*generator)
    print(P.shape, P.rank(), first.rank(), first.col_join(P*generator**2).rank())
    assert P.rank() == 46 and first.rank() == generator.rows
