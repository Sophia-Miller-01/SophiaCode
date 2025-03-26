# fun_py_generate_prime_numbers.py

def fun_py_generate_prime_numbers(n):
    primes = []
    for num in range(2, n+1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

def test_generate_prime_numbers():
    print(f"Primes up to 20: {fun_py_generate_prime_numbers(20)}")

if __name__ == "__main__":
    test_generate_prime_numbers()
