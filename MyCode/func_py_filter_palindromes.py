# func_py_filter_palindromes.py
def func_py_filter_palindromes(lst):
    return [word for word in lst if word == word[::-1]]

print(func_py_filter_palindromes(["madam", "hello", "racecar", "world"]))
