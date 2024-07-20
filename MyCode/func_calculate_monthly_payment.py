# func_calculate_monthly_payment.py
def func_calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    n = years * 12
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -n)

print(func_calculate_monthly_payment(100000, 5, 30))
