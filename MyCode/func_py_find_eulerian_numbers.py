# func_py_find_eulerian_numbers.py
def func_py_find_eulerian_numbers(n, k):
    if k == 0:
        return 1
    elif k >= n or n == 0:
        return 0
    return (n - k) * func_py_find_eulerian_numbers(n - 1, k - 1) + (k + 1) * func_py_find_eulerian_numbers(n - 1, k)

print(func_py_find_eulerian_numbers(5, 2))
