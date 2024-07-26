# func_py_calculate_days_between_dates.py
from datetime import datetime

def fun_py_calculate_days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days

date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 1, 1)
print(fun_py_calculate_days_between_dates(date1, date2))
