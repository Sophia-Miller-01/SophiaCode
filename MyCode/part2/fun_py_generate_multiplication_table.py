# fun_py_generate_multiplication_table.py

def fun_py_generate_multiplication_table(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

def test_generate_multiplication_table():
    table = fun_py_generate_multiplication_table(5)
    for row in table:
        print(row)

if __name__ == "__main__":
    test_generate_multiplication_table()
