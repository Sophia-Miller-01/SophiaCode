# func_py_find_narcissistic_numbers.py
def func_py_find_narcissistic_numbers(limit):
    return [n for n in range(1, limit) if n == sum(int(digit) ** len(str(n)) for digit in str(n))]

print(func_py_find_narcissistic_numbers(1000))
