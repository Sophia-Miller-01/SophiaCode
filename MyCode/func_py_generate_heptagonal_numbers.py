# func_py_generate_heptagonal_numbers.py
def func_py_generate_heptagonal_numbers(n):
    return [i * (5 * i - 3) // 2 for i in range(1, n + 1)]

print(func_py_generate_heptagonal_numbers(10))
