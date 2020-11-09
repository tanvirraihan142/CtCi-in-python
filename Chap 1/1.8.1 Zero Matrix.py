def set_zeros(matrix):
    row = [False for i in range(len(matrix))]
    column = [False for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 0):
                row[i] =  True
                column[j] = True

    for i in range(len(row)):
        if (row[i]):
            nullify_row(matrix,i)

    for i in range(len(column)):
        if (column[i]):
            nullify_column(matrix,i)

def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0

def nullify_column(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
