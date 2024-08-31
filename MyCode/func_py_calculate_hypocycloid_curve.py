# func_py_calculate_hypocycloid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_hypocycloid_curve(R, r, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = (R - r) * np.cos(t) + r * np.cos((R - r) * t / r)
    y = (R - r) * np.sin(t) - r * np.sin((R - r) * t / r)
    plt.plot(x, y)
    plt.title("Hypocycloid Curve")
    plt.show()

func_py_calculate_hypocycloid_curve(5, 3, 1000)
