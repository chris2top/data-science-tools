"""A matrix e.g. [[1,2,3], is defined as a list of lists where the inner lists represent the rows.
                  [4,5,6]]  e.g. the first element in every row translate to the first column
"""

def is_matrix(matrix):
    for i in range(1, len(matrix)):
        if len(matrix[i-1]) != len(matrix[i]):
            raise Exception("Rows must have the same length")

def create_matrix(rows, cols, creation):
    matrix = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = creation(i, j)
    return matrix
