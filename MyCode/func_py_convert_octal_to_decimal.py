# func_py_convert_octal_to_decimal.py
def func_py_convert_octal_to_decimal(octal_str):
    try:
        return int(octal_str, 8)
    except ValueError:
        return None

print(func_py_convert_octal_to_decimal('17'))
