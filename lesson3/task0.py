



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

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
