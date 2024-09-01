# func_py_generate_happy_numbers.py
def func_py_generate_happy_numbers(limit):
    def is_happy_number(n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1

    happy_numbers = [n for n in range(1, limit + 1) if is_happy_number(n)]
    return happy_numbers

print(func_py_generate_happy_numbers(100))
