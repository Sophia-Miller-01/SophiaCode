# func_py_fibonacci_sequence.py

def func_py_fibonacci_sequence(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def test_fibonacci_sequence():
    print(f"First 10 Fibonacci numbers: {func_py_fibonacci_sequence(10)}")

if __name__ == "__main__":
    test_fibonacci_sequence()
