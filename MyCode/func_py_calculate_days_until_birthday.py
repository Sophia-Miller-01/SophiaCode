# func_py_calculate_days_until_birthday.py
from datetime import datetime

def func_py_calculate_days_until_birthday(birthday):
    today = datetime.today()
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)
    return (next_birthday - today).days

birthday = datetime(2023, 12, 31)
print(func_py_calculate_days_until_birthday(birthday))
