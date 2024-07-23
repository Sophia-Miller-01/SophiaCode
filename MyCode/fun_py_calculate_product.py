# fun_py_calculate_product.py
def fun_py_calculate_product(lst):
    product = 1
    for i in lst:
        product *= i
    return product

print(fun_py_calculate_product([1, 2, 3, 4]))
