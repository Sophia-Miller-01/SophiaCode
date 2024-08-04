# func_py_generate_subsets.py
from itertools import chain, combinations

def func_py_generate_subsets(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

print(func_py_generate_subsets([1, 2, 3]))
