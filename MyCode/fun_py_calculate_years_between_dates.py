# fun_py_calculate_years_between_dates.py
from datetime import datetime

def fun_py_calculate_years_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days // 365

date1 = datetime(2000, 1, 1)
date2 = datetime(2024, 1, 1)
print(fun_py_calculate_years_between_dates(date1, date2))
