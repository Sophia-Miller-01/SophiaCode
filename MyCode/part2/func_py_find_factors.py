# func_py_find_factors.py
def func_py_find_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]
