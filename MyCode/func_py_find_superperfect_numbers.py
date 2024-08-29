# func_py_find_superperfect_numbers.py
def func_py_find_superperfect_numbers(limit):
    def sum_of_divisors(n):
        return sum(i for i in range(1, n) if n % i == 0)
    
    def superperfect_check(n):
        return sum_of_divisors(sum_of_divisors(n)) == 2 * n
    
    return [n for n in range(1, limit) if superperfect_check(n)]

print(func_py_find_superperfect_numbers(100))
