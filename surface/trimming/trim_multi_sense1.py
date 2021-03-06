#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from matplotlib import cm
from geomdl import BSpline
from geomdl import exchange
from geomdl import tessellate
from geomdl.visualization import VisMPL as vis
from geomdl.shapes import analytic


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("../ex_surface01.cpt", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set sample size
surf.sample_size = 30

# Set surface tessellation component
surf.tessellator = tessellate.TrimTessellate()

# Set visualization component
visconf = vis.VisConfig(ctrlpts=False, legend=False, trims=False)
surf.vis = vis.VisSurface(config=visconf)

# Generate circular trim curves with different sense
tcrv1 = analytic.Circle(origin=(0.25, 0.25), radius=0.20)
tcrv1.opt = ['sense', 1]
tcrv2 = analytic.Circle(origin=(0.75, 0.75), radius=0.20)
tcrv2.opt = ['sense', 1]
trim_curves = [tcrv1, tcrv2]

# Set trim curves (as a list)
surf.trims = trim_curves

# Visualize surface
surf.render(colormap=cm.copper)

# # Save as Wavefront OBJ file
# exchange.export_obj(surf, "trim_multi_sense.obj")

# Good to have something here to put a breakpoint
pass
