"""Build an instrumented copy of the version-pinned LAMMPS REBO pair style.

Source code is unmodified in the original checkout. The plugin exports a
read-only 17-double record for each direct angular force contribution.
"""
from pathlib import Path
import hashlib
R=Path(__file__).resolve().parent
src=R/'lammps-source/src/MANYBODY/pair_airebo.cpp'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='cbe2b802e554212d2a2244d30ecd26f4d48c1fcebe5a9cb20610b643c12b0a58'
out=R/'graphite-trace';out.mkdir(exist_ok=True)
s=src.read_text();s=s.replace('#include <cstring>','#include <cstring>\n#include <array>\n#include <vector>\n#include <algorithm>',1)
marker='using namespace LAMMPS_NS;'
assert s.count(marker)==1
trace='''
// Serial diagnostic API: 3 atom tags, cos, Nij, spline segment, g, dgdc,
// and three Cartesian direct-angular force vectors on center/bond/angle atoms.
static std::vector<std::array<double,17>> ud_angle_records;
extern "C" size_t ud_trace_count() { return ud_angle_records.size(); }
extern "C" size_t ud_trace_copy(double *out, size_t cap) {
  size_t n = std::min(cap,ud_angle_records.size());
  for (size_t i=0;i<n;++i) std::copy(ud_angle_records[i].begin(),ud_angle_records[i].end(),out+17*i);
  return n;
}
static int ud_segment(double c) { return c < -0.6666666667 ? 0 : c < -0.5 ? 1 : c < -0.3333333333 ? 2 : 3; }
'''
s=s.replace(marker,marker+'\n'+trace,1)
old='''void PairAIREBO::FREBO(int eflag)
{'''
assert s.count(old)==1
s=s.replace(old,old+'\n  ud_angle_records.clear();',1)
old_i='''      fk[2] = -tmp2*dcosjikdrk[2];

      tmp2 = VA*.5*(tmp*wik*g*exp(lamdajik)*4.0*kronecker(itype,1));'''
new_i='''      fk[2] = -tmp2*dcosjikdrk[2];
      ud_angle_records.push_back({double(atom->tag[atomi]),double(atom->tag[atomj]),double(atom->tag[atomk]),cosjik,NijC+NijH,double(ud_segment(cosjik)),g,dgdc,fi[0],fi[1],fi[2],fj[0],fj[1],fj[2],fk[0],fk[1],fk[2]});

      tmp2 = VA*.5*(tmp*wik*g*exp(lamdajik)*4.0*kronecker(itype,1));'''
assert s.count(old_i)==1
s=s.replace(old_i,new_i,1)
old_j='''      fl[2] = -tmp2*dcosijldrl[2];

      tmp2 = VA*.5*(tmp*wjl*g*exp(lamdaijl)*4.0*kronecker(jtype,1));'''
new_j='''      fl[2] = -tmp2*dcosijldrl[2];
      ud_angle_records.push_back({double(atom->tag[atomj]),double(atom->tag[atomi]),double(atom->tag[atoml]),cosijl,NjiC+NjiH,double(ud_segment(cosijl)),g,dgdc,fj[0],fj[1],fj[2],fi[0],fi[1],fi[2],fl[0],fl[1],fl[2]});

      tmp2 = VA*.5*(tmp*wjl*g*exp(lamdaijl)*4.0*kronecker(jtype,1));'''
assert s.count(old_j)==1
s=s.replace(old_j,new_j,1)
(out/'pair_airebo_trace.cpp').write_text(s)
reg='''#include "pair_rebo.h"
#include "lammpsplugin.h"
using namespace LAMMPS_NS;
static void *create_rebo_trace(void *p) { return new PairREBO((LAMMPS*)p); }
extern "C" void lammpsplugin_init(void *lmp, void *handle, void *regfunc) {
  lammpsplugin_t p;
  p.version="22 Jul 2025";p.style="pair";p.name="rebo/udtrace";
  p.info="Version-pinned direct REBO gSpline angular force trace";
  p.author="Codex; instrumented LAMMPS source";
  p.creator.v1=create_rebo_trace;p.handle=handle;
  ((lammpsplugin_regfunc)regfunc)(&p,lmp);
}
'''
(out/'register.cpp').write_text(reg)
print(out)
