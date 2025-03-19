# func_py_fibonacci.py

def func_py_fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def test_fibonacci():
    print(f"Fibonacci sequence: {func_py_fibonacci(10)}")

if __name__ == "__main__":
    test_fibonacci()
