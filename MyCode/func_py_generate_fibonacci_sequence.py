# func_py_generate_fibonacci_sequence.py
def func_py_generate_fibonacci_sequence(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

print(func_py_generate_fibonacci_sequence(10))
