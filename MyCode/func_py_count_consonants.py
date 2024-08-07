# func_py_count_consonants.py
def func_py_count_consonants(text):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for char in text if char in consonants)

print(func_py_count_consonants("Hello, how are you?"))
