# func_py_get_even_numbers.py

def func_py_get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def test_get_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    print(f"Even numbers: {func_py_get_even_numbers(numbers)}")

if __name__ == "__main__":
    test_get_even_numbers()
