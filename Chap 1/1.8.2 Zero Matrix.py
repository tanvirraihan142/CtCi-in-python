def set_zeros(matrix):
    row_has_zero = False
    col_has_zero = False

    for j in range(len(matrix[0])):
        if(matrix[0][j]==0):
            row_has_zero = True
            break

    for i in range(len(matrix[0])):
        if(matrix[0][j]==0):
            row_has_zero = True
            break

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if (matrix[i][j]==0):
                matrix[i][0]=0
                matrix[0][j]=0

    for i in range(1,len(matrix)):
        if (matrix[i][0]==0):
            nullify_row(matrix,i)

    for j in range(1,len(matrix[0])):
        if (matrix[0][j]==0):
            nullify_col(matrix,j)

    if (row_has_zero):
        nullify_row(matrix,0)
    if (col_has_zero):
        nullify_col(matrix,0)


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][j] = 0

def nullify_column(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
