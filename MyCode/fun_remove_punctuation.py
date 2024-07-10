# fun_remove_punctuation.py
import string

def fun_remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

print(fun_remove_punctuation("Hello, world!"))
