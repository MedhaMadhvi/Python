#Python program to implement matrix multiplication.
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            cell_value = 0
            for k in range(len(matrix2)):
                cell_value += matrix1[i][k] * matrix2[k][j]
            row.append(cell_value)
        result.append(row)

    return result

rows1 = int(input("Enter the number of rows for Matrix 1: "))
columns1 = int(input("Enter the number of columns for Matrix 1: "))

rows2 = columns1
columns2 = int(input("Enter the number of columns for Matrix 2: "))

matrix1 = []
matrix2 = []

print("Enter elements for Matrix 1:")
for i in range(rows1):
    row = []
    for j in range(columns1):
        element = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix1.append(row)

print("Enter elements for Matrix 2:")
for i in range(columns1):
    row = []
    for j in range(columns2):
        element = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix2.append(row)

result_matrix = matrix_multiplication(matrix1, matrix2)

if result_matrix is not None:
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nMatrix Multiplication (Result):")
    for row in result_matrix:
        print(row)
else:
    print("Matrix multiplication is not possible. Number of columns in Matrix 1 must be equal to the number of rows in Matrix 2.")
