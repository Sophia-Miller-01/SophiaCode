# fun_py_reverse_string.py

def fun_py_reverse_string(s):
    return s[::-1]

def test_reverse_string():
    text = "Python"
    print(f"Reversed string: {fun_py_reverse_string(text)}")

if __name__ == "__main__":
    test_reverse_string()
