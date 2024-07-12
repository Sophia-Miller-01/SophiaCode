# func_generate_even_numbers.py
def func_generate_even_numbers(n):
    return [x for x in range(n) if x % 2 == 0]

print(func_generate_even_numbers(10))
