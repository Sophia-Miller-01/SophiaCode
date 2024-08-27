# func_py_calculate_heptagonal_prism_volume.py
import math

def func_py_calculate_heptagonal_prism_volume(side_length, height):
    area_base = (7/4) * side_length**2 * (1 / math.tan(math.pi/7))
    return area_base * height

print(func_py_calculate_heptagonal_prism_volume(3, 10))
