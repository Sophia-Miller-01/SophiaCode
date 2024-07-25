# fun_py_calculate_age_in_days.py
from datetime import datetime

def fun_py_calculate_age_in_days(birth_date):
    today = datetime.today()
    delta = today - birth_date
    return delta.days

birth_date = datetime(2000, 1, 1)
print(fun_py_calculate_age_in_days(birth_date))
