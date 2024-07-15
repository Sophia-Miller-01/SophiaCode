# func_reverse_words_in_string.py
def func_reverse_words_in_string(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

print(func_reverse_words_in_string("Hello World"))
