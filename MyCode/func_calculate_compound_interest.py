# func_calculate_compound_interest.py
def func_calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate/n) ** (n*time)
    return amount

print(func_calculate_compound_interest(1000, 0.05, 10, 12))
