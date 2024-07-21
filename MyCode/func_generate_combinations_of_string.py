# func_generate_combinations_of_string.py
from itertools import combinations

def func_generate_combinations_of_string(string, r):
    return list(combinations(string, r))

print(func_generate_combinations_of_string("abcd", 2))
