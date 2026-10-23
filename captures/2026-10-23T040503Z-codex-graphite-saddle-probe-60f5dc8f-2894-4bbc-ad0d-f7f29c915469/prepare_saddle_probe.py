#!/usr/bin/env python3
"""Prepare source-matched off-line QE inputs; do not run imported archive code."""
import argparse
import hashlib
import json
import math
import re
import tarfile
from pathlib import Path

ARCHIVE_SHA256 = "05e5e995d70ad83a98f8b534addb3dcff51ff3422c8f24dcba25453c3e76e228"
PREFIX = "qe-21-vdw-df3-3.4022A-h30A/dir_30/"
U1 = 0.0793396654  # micro-eV per upper atom, previous full-profile fit
LATTICE_A = 2.4660  # angstrom, source paper convention
KY = 2 * math.pi * math.sqrt(7) / (math.sqrt(3) * LATTICE_A)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def make_input(source, offset):
    lines = source.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.strip() == "ATOMIC_POSITIONS angstrom") + 1
    assert len(lines) - start == 28, "unexpected atom count or trailing content"
    assert all(re.fullmatch(r"C\s+[-+\d.eE]+\s+[-+\d.eE]+\s+[-+\d.eE]+", line.strip()) for line in lines[start:])
    nx, ny = .5, -math.sqrt(3) / 2
    for i in range(14, 28):
        fields = lines[start + i].split()
        x, y, z = map(float, fields[1:])
        lines[start + i] = f"C {x + offset * nx:.16f} {y + offset * ny:.16f} {z:.4f}\n"
    return "".join(lines)


def signal(h, epsilon_ratio):
    beta = math.sqrt(3) * KY * h
    f = 4 * math.sin(beta / 2) ** 2
    F = (1 - math.cos(2 * beta)) * (1 + math.cos(beta)) ** 2
    return {"h_A": h, "delta_first_shell_microeV_atom": U1 * f,
            "F_dimensionless": F,
            "delta_counterexample_microeV_atom": U1 * (f + epsilon_ratio * F),
            "D_first_shell_microeV_atom": 2 * U1 * f,
            "D_counterexample_microeV_atom": 2 * U1 * (f + epsilon_ratio * F)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    assert sha256(args.archive.read_bytes()) == ARCHIVE_SHA256, "archive SHA mismatch"
    with tarfile.open(args.archive, "r:gz") as tf:
        def read(name):
            member = tf.getmember(PREFIX + name)
            assert member.isfile() and member.size < 5_000_000
            return tf.extractfile(member).read()
        source_bytes = read("struct.in")
        pseudo_bytes = read("C.upf")
    source = source_bytes.decode("ascii")
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "center.in").write_bytes(source_bytes)
    for h in (.04, .08):
        for sign, label in ((-1, "minus"), (1, "plus")):
            (args.output / f"{label}_{h:.2f}A.in").write_text(make_input(source, sign * h), encoding="ascii")
    result = {"status": "PROPOSED_NOT_RUN", "archive_sha256": ARCHIVE_SHA256,
              "source_member": PREFIX + "struct.in", "source_input_sha256": sha256(source_bytes),
              "pseudo_member": PREFIX + "C.upf", "pseudo_sha256": sha256(pseudo_bytes),
              "atom_count": 28, "upper_atom_indices_zero_based": [14, 28],
              "unit_normal_xy": [.5, -math.sqrt(3) / 2], "ky_inverse_A": KY,
              "U1_microeV_per_upper_atom": U1, "example_epsilon_over_U1": -.2,
              "predictions": [signal(h, -.2) for h in (.04, .08)],
              "local_first_shell_curvature_microeV_atom_A2": 6 * U1 * KY ** 2,
              "local_counterexample_curvature_microeV_atom_A2": (6 - 9.6) * U1 * KY ** 2,
              "meaning": "Model contrasts only; no new DFT output or graphite fit."}
    (args.output / "SADDLE_PROBE_DESIGN.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
