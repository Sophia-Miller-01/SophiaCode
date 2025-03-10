# func_py_random_password.py
import random
import string

def func_py_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

print(func_py_random_password(16))
