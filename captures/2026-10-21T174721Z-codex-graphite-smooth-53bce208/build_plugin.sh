#!/usr/bin/env bash
set -euo pipefail
smooth_root="$(cd -- "$(dirname -- "$0")" && pwd)"
workspace_root="$(dirname -- "$smooth_root")"
g++ -std=c++17 -O2 -fPIC -shared -I "$workspace_root/lammps-runtime/lammps/include/lammps" -I "$workspace_root/mpi-runtime/include" -I "$smooth_root/plugin" "$smooth_root/plugin/pair_kcz_smooth.cpp" -L "$workspace_root/lammps-runtime/lammps" -llammps -Wl,-rpath,"$workspace_root/lammps-runtime/lammps" -o "$smooth_root/plugin/kcz_smooth.so"
