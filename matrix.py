"""A matrix e.g. [[1,2,3], is defined as a list of lists where the inner lists represent the rows.
                  [4,5,6]]  e.g. the first element in every row translate to the first column
"""

def is_matrix(matrix):
    for i in range(1, len(matrix)):
        if len(matrix[i-1]) != len(matrix[i]):
            raise Exception("Rows must have the same length")
