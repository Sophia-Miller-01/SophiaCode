# func_py_find_average.py
def func_py_find_average(lst):
    total_sum = 0
    for num in lst:
        total_sum += num
    return total_sum / len(lst)
