# func_py_calculate_median.py
def func_py_calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

print(func_py_calculate_median([4, 1, 3, 2]))
