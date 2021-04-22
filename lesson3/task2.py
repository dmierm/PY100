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

N = len(matrix)
M = len(matrix[0])
s = 0
s1 = 0
sum_rows = []
for i in range(N):
    s1 = 0
    for j in range(M):
        ceil = matrix[i][j]
        s += ceil
        s1 = s
    sum_rows.append(s1)
    print(s1)
print(s)
