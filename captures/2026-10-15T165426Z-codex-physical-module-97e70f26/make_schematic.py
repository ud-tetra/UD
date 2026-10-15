from pathlib import Path
p=Path(__file__).resolve().parent
s=['''<svg xmlns="http://www.w3.org/2000/svg" width="1420" height="900" viewBox="0 0 1420 900">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#176c9b"/></marker></defs>
<rect width="1420" height="900" fill="#fbfcfe"/>
<style>text{font-family:DejaVu Sans,Arial,sans-serif;fill:#172d42}.title{font-size:29px;font-weight:700}.sub{font-size:19px}.label{font-size:21px}.small{font-size:17px}.wire{fill:none;stroke:#253c50;stroke-width:3}.box{fill:#eef5fa;stroke:#afc9da;stroke-width:2}.sense{fill:none;stroke:#176c9b;stroke-width:3;stroke-dasharray:7 6}</style>
<text x="55" y="55" class="title">Four-coordinate module: a passive electrical realization</text>
<text x="55" y="89" class="sub">Two loops · seven equal capacitors C · two equal inductors L · balanced charge preparation</text>
<rect x="40" y="120" width="715" height="615" rx="16" fill="white" stroke="#d0dce6"/>
<text x="70" y="157" class="label">Primary network</text>
<path class="wire" d="M140 205H650M140 655H650"/>
<circle cx="395" cy="205" r="5" fill="#253c50"/><circle cx="395" cy="655" r="5" fill="#253c50"/>
<text x="377" y="190" class="label">A</text><text x="377" y="689" class="label">B</text>
''']
def cap(x,y,label):
 s.append(f'<path class="wire" d="M{x} {y-29}V{y-6}M{x-20} {y-6}H{x+20}M{x-20} {y+6}H{x+20}M{x} {y+6}V{y+29}"/><text x="{x+29}" y="{y+7}" class="label">{label}</text>')
for x,idx in [(140,1),(650,2)]:
 s.append(f'<path class="wire" d="M{x} 205V240M{x} 320V351M{x} 409V441M{x} 499V531M{x} 589V655"/>')
 # square-ended coil loops as actual inductance symbol oriented vertically
 s.append(f'<path class="wire" d="M{x} 240c-25 0 -25 20 0 20c-25 0 -25 20 0 20c-25 0 -25 20 0 20c-25 0 -25 20 0 20"/><text x="{x+25}" y="287" class="label">L</text>')
 for y in [380,470,560]:cap(x,y,'C')
 ax=x-52 if idx==1 else x+65
 s.append(f'<path d="M{ax} 352V425" stroke="#176c9b" stroke-width="3" marker-end="url(#arrow)"/><text x="{ax-14}" y="341" class="label">I{idx}</text>')
s.append('<path class="wire" d="M395 205V401M395 459V655"/>')
cap(395,430,'C shared')
s.append('''<path d="M327 520V451" stroke="#176c9b" stroke-width="3" marker-end="url(#arrow)"/>
<text x="289" y="550" class="small">I1 + I2</text>
<text x="72" y="718" class="small">Branch signs are chosen to match the signed face matrix B3.</text>
<rect x="795" y="120" width="585" height="275" rx="16" class="box"/>
<text x="823" y="160" class="label">F · shared-face voltage</text>
<text x="823" y="205" class="label">V_F = X_shared / C</text>
<text x="823" y="244" class="label">Sum mode: Ω+ = √5 / √(LC)</text>
<text x="823" y="287" class="small">Finite probe: add Cp and conductance Gp</text>
<text x="823" y="318" class="small">across the shared capacitor.</text>
<path class="sense" d="M478 430H770V265H795"/>
<rect x="795" y="420" width="585" height="315" rx="16" class="box"/>
<text x="823" y="461" class="label">P · opposing-winding inductive pickup</text>
<text x="823" y="506" class="label">Mutual inductances +μ and −μ</text>
<text x="823" y="547" class="label">U_P = −μ d(I1 − I2)/dt  (open circuit)</text>
<text x="823" y="591" class="label">Difference mode: Ω− = √3 / √(LC)</text>
<text x="823" y="636" class="small">Finite secondary: Ls, Rs and current J</text>
<text x="823" y="668" class="small">Measured loaded voltage: V_R = Rs J</text>
<path class="sense" d="M182 270H227V170H766V570H795"/>
<path class="sense" d="M685 270H766"/>
<rect x="40" y="765" width="1340" height="101" rx="12" fill="#e7f0e9"/>
<text x="66" y="804" class="label">Physical state: loop currents I1, I2 and face-capacitor charges X = I0 √(LC) B3 M⁻¹v</text>
<text x="66" y="840" class="sub">E = L I0² H4 · both voltage histories reconstruct the ideal module · finite passive loads dissipate energy</text>
</svg>''')
(p/'Four_Coordinate_Circuit.svg').write_text('\n'.join(s))
