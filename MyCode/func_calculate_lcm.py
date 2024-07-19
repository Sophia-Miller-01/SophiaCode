# func_calculate_lcm.py
def func_calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

print(func_calculate_lcm(12, 15))
