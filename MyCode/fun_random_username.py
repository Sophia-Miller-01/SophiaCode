# fun_random_username.py
import random
import string

def generate_username(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

print(generate_username(8))
