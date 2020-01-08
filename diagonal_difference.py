def diagonal_difference(matrix):
    ltr, rtl = 0, 0
    for i in range(len(matrix)):
        ltr += matrix[i][i]
        rtl += matrix[i][(len(matrix) - 1) - i]

    return abs(ltr - rtl)
