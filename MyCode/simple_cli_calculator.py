# simple_cli_calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

if __name__ == "__main__":
    while True:
        operation = input("Choose operation (add, subtract, multiply, divide) or 'quit': ").strip().lower()
        if operation == 'quit':
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        else:
            result = "Invalid operation"
        print(f"Result: {result}")
