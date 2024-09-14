# func_py_generate_fibonacci_series.py
def func_py_generate_fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

print(func_py_generate_fibonacci_series(10))
