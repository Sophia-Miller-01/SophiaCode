# func_py_multiply_matrices.py
def func_py_multiply_matrices(matrix1, matrix2):
    result = [[sum(a * b for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print(func_py_multiply_matrices(matrix1, matrix2))
