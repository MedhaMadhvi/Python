def add_matrices(matrix1, matrix2):

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix1 = []
matrix2 = []

print("Enter elements for Matrix 1:")
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element at row {i+1}, column {j+1}: "))
        row.append(element)
    matrix1.append(row)

print("Enter elements for Matrix 2:")
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element at row {i+1}, column {j+1}: "))
        row.append(element)
    matrix2.append(row)

result_matrix = add_matrices(matrix1, matrix2)


if result_matrix is not None:
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nMatrix Sum (Result):")
    for row in result_matrix:
        print(row)
else:
    print("Matrix addition is not possible. Matrices must have the same dimensions.")
