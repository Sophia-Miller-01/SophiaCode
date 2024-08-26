# func_py_calculate_spherical_wedge_volume.py
import math

def func_py_calculate_spherical_wedge_volume(radius, theta):
    return (2/3) * math.pi * radius**3 * (theta / 360)

print(func_py_calculate_spherical_wedge_volume(5, 60))
