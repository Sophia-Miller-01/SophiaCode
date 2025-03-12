# func_py_fibonacci_memoization.py
from functools import lru_cache

@lru_cache(maxsize=None)
def func_py_fibonacci_memoization(n):
    if n < 2:
        return n
    return func_py_fibonacci_memoization(n-1) + func_py_fibonacci_memoization(n-2)

print([func_py_fibonacci_memoization(i) for i in range(20)])
