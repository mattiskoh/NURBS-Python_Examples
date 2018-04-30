#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""
import os
from geomdl import NURBS
from geomdl import exchange

# Try to load the visualization module
try:
    render_curve = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_curve = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS curve instance (full circle)
curve = NURBS.Curve()

# Set up curve
curve.ctrlptsw = exchange.read_txt("ex_curve04.cptw")
curve.degree = 2
# Use a specialized knot vector
curve.knotvector = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_config = VisMPL.VisConfig(figure_size=[8, 8])
    vis_comp = VisMPL.VisCurve2D(config=vis_config)
    curve.vis = vis_comp
    curve.render()

# Good to have something here to put a breakpoint
pass
