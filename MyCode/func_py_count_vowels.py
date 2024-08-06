# func_py_count_vowels.py
def func_py_count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

print(func_py_count_vowels("Hello, how are you?"))
