# func_py_calculate_time_difference.py
from datetime import datetime

def func_py_calculate_time_difference(time1, time2):
    delta = time2 - time1
    return delta

time1 = datetime(2024, 1, 1, 12, 0)
time2 = datetime(2024, 1, 1, 18, 0)
print(func_py_calculate_time_difference(time1, time2))
