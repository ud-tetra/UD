#!/usr/bin/env python3
"""Read-only audit of archived QE rigid lateral coordinates, inputs and XML."""
import argparse
import hashlib
import json
import math
import tarfile
from pathlib import Path
from xml.etree import ElementTree

EXPECTED_SHA = {
    "qe-21-vdw-df3-3.34A-h30A.tar.gz": "5d6efcbd67db3093711ed92bd06d7098254fbe21680a869dd941664ad6190443",
    "qe-21-vdw-df3-3.4022A-h30A.tar.gz": "05e5e995d70ad83a98f8b534addb3dcff51ff3422c8f24dcba25453c3e76e228",
    "qe-21-vdw-df3-aa.tar.gz": "6abb5cd8064d7f3edbabbafb8d7f2c68f6468b7b5bf8c15e035e0c1efa01e12a",
    "qe-21-vdw-df3-ab.tar.gz": "c2c03213386df2e090dd42357d9ab4a3b4ad0e38907fb2265c0515e750d489d8",
    "qe-21-vdw-df3-opt-dist.tar.gz": "1a7e4d6c1ea466448436db2507da75c33216c7b09995547f7fd8a0731f873de0",
    "qe-21-vdw-df3-sp.tar.gz": "75a1e5d2a311d45ee8985b17d6567e05f38e7cec17d1dec6dc4d766b580734b4",
}
BOHR_A = .529177210903
AB_REL_A = (0., -1.0762682221329958)
N = (.5, -math.sqrt(3)/2)
T = (math.sqrt(3)/2, .5)


def project(x, y):
    dx, dy = x-AB_REL_A[0], y-AB_REL_A[1]
    return dx*N[0] + dy*N[1], dx*T[0] + dy*T[1]


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("archive_dir", type=Path)
    a = p.parse_args()
    results = []
    for filename, expected in EXPECTED_SHA.items():
        path = a.archive_dir / filename
        assert digest(path) == expected, filename + " SHA mismatch"
        input_projections, xml_projections = [], []
        with tarfile.open(path, "r:gz") as tf:
            for member in tf:
                if not member.isfile():
                    continue
                if member.name.endswith("/struct.in"):
                    data = tf.extractfile(member).read().decode("ascii")
                    rows = data.split("ATOMIC_POSITIONS angstrom\n", 1)[1].splitlines()
                    assert len(rows) >= 28
                    low = [float(x) for x in rows[0].split()[1:4]]
                    top = [float(x) for x in rows[14].split()[1:4]]
                    input_projections.append(project(top[0]-low[0], top[1]-low[1]))
                elif member.name.endswith("/data-file-schema.xml"):
                    root = ElementTree.fromstring(tf.extractfile(member).read())
                    rows = root.findall("./output/atomic_structure/atomic_positions/atom")
                    assert len(rows) == 28
                    low = [float(x) for x in rows[0].text.split()]
                    top = [float(x) for x in rows[14].text.split()]
                    xml_projections.append(project((top[0]-low[0])*BOHR_A, (top[1]-low[1])*BOHR_A))
        assert input_projections
        assert max(abs(v[0]) for v in input_projections) < 1e-12
        assert max(abs(v[0]) for v in xml_projections) < 1e-12
        results.append({"archive": filename, "sha256": expected,
                        "input_count": len(input_projections), "xml_count": len(xml_projections),
                        "max_abs_input_transverse_A": max(abs(v[0]) for v in input_projections),
                        "max_abs_xml_transverse_A": max((abs(v[0]) for v in xml_projections), default=None),
                        "input_tangential_range_A": [min(v[1] for v in input_projections), max(v[1] for v in input_projections)]})
    print(json.dumps({"status": "SIX_ARCHIVE_COLLINEAR_INPUT_AND_XML_AUDIT",
                      "reference": "AB upper-minus-lower first-C coordinate, common Cartesian frame",
                      "unit_normal_xy": N, "bohr_to_A": BOHR_A,
                      "input_total": sum(x["input_count"] for x in results),
                      "xml_total": sum(x["xml_count"] for x in results),
                      "archives": results,
                      "interpretation": "No distinct off-line lateral coordinate within these six archives; no inference about uninspected data elsewhere."}, indent=2))


if __name__ == "__main__":
    main()
