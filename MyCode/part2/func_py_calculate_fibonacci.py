# func_py_calculate_fibonacci.py
def calculate_fibonacci(n):
    """
    Calculate the first n Fibonacci numbers.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence[:n]

# Example usage
if __name__ == "__main__":
    n = 10
    fib_sequence = calculate_fibonacci(n)
    print(f"First {n} Fibonacci numbers: {fib_sequence}")
