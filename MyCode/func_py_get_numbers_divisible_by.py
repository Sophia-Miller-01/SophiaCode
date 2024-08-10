# func_py_get_numbers_divisible_by.py
def func_py_get_numbers_divisible_by(lst, divisor):
    return [i for i in lst if i % divisor == 0]

print(func_py_get_numbers_divisible_by([1, 2, 3, 4, 5, 6], 2))
