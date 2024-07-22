# fun_py_get_negative_numbers.py
def fun_py_get_negative_numbers(lst):
    return [i for i in lst if i < 0]

print(fun_py_get_negative_numbers([-1, 2, -3, 4, -5, 6]))
