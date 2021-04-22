def print_matrix(matrix, length=3):
    """
    Функция печатает отформатированную матрицу

    Parameters:
    matrix: список списков
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    length: ширина столбца

    Returns:
        None

    """
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print("{:{}}".format(matrix[row][col], length), end=" ")
        print()

table = []
N = 9
M = 9
a = 0

for i in range(1, N + 1):
    row = []
    for j in range(1, M +1):
        ceil = i * j
        row.append(ceil)
    table.append(row)

print_matrix(table)
