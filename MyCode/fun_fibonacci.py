# fun_fibonacci.py
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

n = 10
print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
