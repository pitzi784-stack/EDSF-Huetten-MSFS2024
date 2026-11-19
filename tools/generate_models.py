"""Erzeugt vier vorläufige 3D-Modelle als GLB (kein MSFS-SDK-Build).
Abhängigkeiten: pip install trimesh numpy
Ausführen: python tools/generate_models.py
Alle Maße sind KONZEPTWERTE, keine Vermessungsdaten von EDSF.
"""
from pathlib import Path
import numpy as np
import trimesh

OUT = Path("PackageSources/model_concepts")
OUT.mkdir(parents=True, exist_ok=True)

def cuboid(dim, center, rgba):
    mesh = trimesh.creation.box(extents=dim)
    mesh.apply_translation(center)
    mesh.visual.face_colors = rgba
    return mesh

def roof(w, d, h, rise, rgba):
    vertices = np.array([
        [-w/2, -d/2, h], [w/2, -d/2, h], [0, -d/2, h+rise],
        [-w/2, d/2, h], [w/2, d/2, h], [0, d/2, h+rise]
    ], dtype=float)
    faces = [[0,1,2], [3,5,4], [0,3,4], [0,4,1],
             [0,2,5], [0,5,3], [1,4,5], [1,5,2]]
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)
    mesh.visual.face_colors = rgba
    return mesh

models = [
    ("hangar_large", 30, 22, 5.8, 3.4),
    ("hangar_small", 22, 18, 4.8, 2.5),
    ("clubhouse", 15, 10, 3.3, 2.1),
    ("equipment_shed", 9, 7, 3.0, 1.3),
]
for name, w, d, h, rise in models:
    scene = trimesh.Scene()
    scene.add_geometry(cuboid([w, d, h], [0, 0, h/2], [196, 199, 191, 255]))
    scene.add_geometry(roof(w, d, h, rise, [90, 98, 101, 255]))
    if name.startswith("hangar"):
        scene.add_geometry(cuboid([w*0.82, 0.08, h*0.73],
                                   [0, -d/2-0.05, h*0.365],
                                   [83, 96, 100, 255]))
    scene.export(OUT / f"{name}.glb")
    print("Created", OUT / f"{name}.glb")
