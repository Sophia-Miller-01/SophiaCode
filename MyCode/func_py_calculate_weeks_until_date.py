# func_py_calculate_weeks_until_date.py
from datetime import datetime

def func_py_calculate_weeks_until_date(future_date):
    today = datetime.today()
    diff = future_date - today
    return diff.days // 7

future_date = datetime(2024, 12, 31)
print(func_py_calculate_weeks_until_date(future_date))
