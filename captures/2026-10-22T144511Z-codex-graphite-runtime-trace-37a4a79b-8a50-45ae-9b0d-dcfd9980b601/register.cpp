#include "pair_rebo.h"
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
