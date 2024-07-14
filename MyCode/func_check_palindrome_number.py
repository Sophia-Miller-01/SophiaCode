# func_check_palindrome_number.py
def func_check_palindrome_number(number):
    return str(number) == str(number)[::-1]

print(func_check_palindrome_number(121))
print(func_check_palindrome_number(123))
