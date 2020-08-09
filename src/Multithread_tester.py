import ghpythonlib.components as ghcomp
import ghpythonlib.parallel
import subprocess


def slice_at_angle(plane):
    result = ghcomp.BrepXPlane(brep, plane)
    if result: return result.curves

if parallel:
    slices = ghpythonlib.parallel.run(slice_at_angle, planes, True)
else:
    # slices = ghcomp.BrepXPlane(brep, planes).curves
    slices = ghcomp.BrepXPlane(brep, planes).curves
