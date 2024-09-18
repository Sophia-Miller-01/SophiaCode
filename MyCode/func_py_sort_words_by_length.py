# func_py_sort_words_by_length.py
def func_py_sort_words_by_length(sentence):
    words = sentence.split()
    return sorted(words, key=len)

print(func_py_sort_words_by_length("Python is fun and powerful"))
