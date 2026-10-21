// Derived from LAMMPS KCz compute routine, GPL; original notice retained below.
/* ----------------------------------------------------------------------
   LAMMPS - Large-scale Atomic/Molecular Massively Parallel Simulator
   https://www.lammps.org/, Sandia National Laboratories
   LAMMPS development team: developers@lammps.org

   Copyright (2003) Sandia Corporation.  Under the terms of Contract
   DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains
   certain rights in this software.  This software is distributed under
   the GNU General Public License.

   See the README file in the top-level LAMMPS directory.
------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------
   Contributing author: Jaap Kroes (Radboud Universiteit)
   e-mail: jaapkroes at gmail dot com
   based on previous versions by Merel van Wijk and by Marco Raguzzoni

   This is a simplified version of the potential described in
   [Kolmogorov & Crespi, Phys. Rev. B 71, 235415 (2005)]
   The simplification is that all normals are taken along the z-direction
------------------------------------------------------------------------- */


#include "pair_kolmogorov_crespi_z.h"
#include "lammpsplugin.h"
#include "atom.h"
#include "force.h"
#include "neigh_list.h"
#include <cmath>
using namespace LAMMPS_NS;
static constexpr double switch_width = UD_SWITCH_WIDTH;
namespace LAMMPS_NS {
class PairKCzSmooth : public PairKolmogorovCrespiZ {
 public:
  PairKCzSmooth(LAMMPS *lmp) : PairKolmogorovCrespiZ(lmp) {}
  void compute(int,int) override;
};
}
void PairKCzSmooth::compute(int eflag, int vflag)
{
  int i, j, ii, jj, inum, jnum, itype, jtype;
  double xtmp, ytmp, ztmp, delx, dely, delz, evdwl, fpair, fpair1;
  double rsq, r, rhosq, exp1, exp2, r6, r8;
  double frho, sumC, sumC2, sumCff, fsum, rdsq;
  double energy_raw, sw, dsw;
  int *ilist, *jlist, *numneigh, **firstneigh;

  evdwl = 0.0;
  ev_init(eflag, vflag);

  double **x = atom->x;
  double **f = atom->f;
  int *type = atom->type;
  int nlocal = atom->nlocal;
  int newton_pair = force->newton_pair;

  inum = list->inum;
  ilist = list->ilist;
  numneigh = list->numneigh;
  firstneigh = list->firstneigh;

  // loop over neighbors of my atoms
  for (ii = 0; ii < inum; ii++) {
    i = ilist[ii];
    xtmp = x[i][0];
    ytmp = x[i][1];
    ztmp = x[i][2];
    itype = type[i];
    jlist = firstneigh[i];
    jnum = numneigh[i];
    for (jj = 0; jj < jnum; jj++) {
      j = jlist[jj];
      j &= NEIGHMASK;
      jtype = type[j];

      delx = xtmp - x[j][0];
      dely = ytmp - x[j][1];
      delz = ztmp - x[j][2];
      // rho^2 = r^2 - (n,r) = r^2 - z^2
      rhosq = delx * delx + dely * dely;
      rsq = rhosq + delz * delz;

      if (rsq < cutsq[itype][jtype]) {

        int iparam_ij = elem2param[map[itype]][map[jtype]];
        Param &p = params[iparam_ij];

        r = sqrt(rsq);
        r6 = rsq * rsq * rsq;
        r8 = r6 * rsq;
        rdsq = rhosq * p.delta2inv;    // (rho/delta)^2

        // store exponents
        exp1 = exp(-p.lambda * (r - p.z0));
        exp2 = exp(-rdsq);

        // note that f(rho_ij) equals f(rho_ji) as normals are all along z
        sumC = p.C0 + p.C2 * rdsq + p.C4 * rdsq * rdsq;
        sumC2 = (2 * p.C2 + 4 * p.C4 * rdsq) * p.delta2inv;
        frho = exp2 * sumC;
        sumCff = p.C + 2 * frho;

        // derivatives
        fpair = -6.0 * p.A * p.z06 / r8 + p.lambda * exp1 / r * sumCff;
        fpair1 = exp1 * exp2 * (4.0 * p.delta2inv * sumC - 2.0 * sumC2);
        // New model: quintic C2 switch on the unshifted full KCz energy.
        energy_raw = -p.A * p.z06 / r6 + exp1 * sumCff;
        sw = 1.0;
        dsw = 0.0;
        if (r > cut_global - switch_width) {
          double t = (r - (cut_global - switch_width)) / switch_width;
          // Factored form avoids loss of significance near the cutoff.
          double u = 1.0 - t;
          sw = u*u*u*(1.0 + 3.0*t + 6.0*t*t);
          dsw = -30.0*t*t*u*u/switch_width;
        }
        fpair = sw * fpair - energy_raw * dsw / r;
        fpair1 *= sw;
        fsum = fpair + fpair1;

        f[i][0] += delx * fsum;
        f[i][1] += dely * fsum;
        // fi_z does not contain contributions from df/dr
        // because rho_ij does not depend on z_i or z_j
        f[i][2] += delz * fpair;
        if (newton_pair || j < nlocal) {
          f[j][0] -= delx * fsum;
          f[j][1] -= dely * fsum;
          f[j][2] -= delz * fpair;
        }

        if (eflag) { evdwl = sw * energy_raw; }

        if (evflag) {
          ev_tally(i, j, nlocal, newton_pair, evdwl, 0.0, fpair, delx, dely, delz);
          if (vflag_either) {
            double fi[3], fj[3];
            fi[0] = delx * fpair1;
            fi[1] = dely * fpair1;
            fi[2] = 0;
            fj[0] = -delx * fpair1;
            fj[1] = -dely * fpair1;
            fj[2] = 0;
            v_tally2_newton(i, fi, x[i]);
            v_tally2_newton(j, fj, x[j]);
          }
        }
      }
    }
  }

  if (vflag_fdotr) virial_fdotr_compute();
}


static void *creator(void *lmp) { return new PairKCzSmooth((LAMMPS *)lmp); }
extern "C" void lammpsplugin_init(void *lmp, void *handle, void *regfunc) {
 lammpsplugin_t plugin;
 plugin.version = "22 Jul 2025";
 plugin.style = "pair";
 plugin.name = "kolmogorov/crespi/z/smooth";
 plugin.info = "KCz unshifted quintic C2 switch, compile-time width1/2/3 Angstrom, v0.2";
 plugin.author = "Codex; based on LAMMPS KCz";
 plugin.creator.v1 = creator;
 plugin.handle = handle;
 ((lammpsplugin_regfunc)regfunc)(&plugin,lmp);
}
