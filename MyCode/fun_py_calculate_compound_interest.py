# fun_py_calculate_compound_interest.py
def fun_py_calculate_compound_interest(principal, rate, times_compounded, years):
    return principal * (1 + rate / times_compounded) ** (times_compounded * years)

print(fun_py_calculate_compound_interest(1000, 0.05, 4, 5))
