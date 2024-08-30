# func_py_find_semiprime_numbers.py
def func_py_find_semiprime_numbers(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    return [n for n in range(4, limit) if len([i for i in range(2, n) if n % i == 0 and is_prime(i)]) == 2]

print(func_py_find_semiprime_numbers(100))
