# func_py_find_mode.py
from collections import Counter

def func_py_find_mode(lst):
    count = Counter(lst)
    return max(count, key=count.get)

print(func_py_find_mode([2, 4, 4, 6, 6, 4]))
