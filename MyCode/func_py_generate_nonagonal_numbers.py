# func_py_generate_nonagonal_numbers.py
def func_py_generate_nonagonal_numbers(n):
    return [4 * i**2 - 3 * i for i in range(1, n + 1)]

print(func_py_generate_nonagonal_numbers(10))
