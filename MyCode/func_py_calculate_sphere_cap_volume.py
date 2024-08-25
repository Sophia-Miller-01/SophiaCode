# func_py_calculate_sphere_cap_volume.py
import math

def func_py_calculate_sphere_cap_volume(radius, height):
    return (1/3) * math.pi * height**2 * (3 * radius - height)

print(func_py_calculate_sphere_cap_volume(4, 2))
