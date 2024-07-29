# func_py_calculate_seconds_between_dates.py
from datetime import datetime

def func_py_calculate_seconds_between_dates(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()

date1 = datetime(2023, 1, 1, 12, 0)
date2 = datetime(2024, 1, 1, 12, 0)
print(func_py_calculate_seconds_between_dates(date1, date2))
