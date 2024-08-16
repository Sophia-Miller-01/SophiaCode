# func_py_calculate_hypersphere_volume.py
import math

def func_py_calculate_hypersphere_volume(radius, dimension):
    return (math.pi**(dimension / 2) * radius**dimension) / math.gamma(dimension / 2 + 1)

print(func_py_calculate_hypersphere_volume(3, 4))
