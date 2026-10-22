from pathlib import Path
import subprocess
root=Path(__file__).resolve().parent.parent
subprocess.run(['g++','-std=c++17','-O2','-fPIC','-shared','-DUD_SWITCH_WIDTH=2.0','-I',str(root/'lammps-runtime/lammps/include/lammps'),'-I',str(root/'mpi-runtime/include'),'-I',str(root/'graphite-width/plugin'),str(root/'graphite-width/plugin/pair_kcz_width.cpp'),'-L',str(root/'lammps-runtime/lammps'),'-llammps',f'-Wl,-rpath,{root}/lammps-runtime/lammps','-o',str(root/'graphite-width/plugin/kcz_width2.so')],check=True)
