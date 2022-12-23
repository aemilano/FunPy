# Import modules
import random

# Creating variables
row = []
matrix = []
transpose = []
no_of_columns = 3
no_of_rows = 8

# Function


def random_number_matrix(no_of_rows: int, no_of_columns: int) -> list:
    '''Create a matrix of random numbers in range 1 - 9.'''
    for i in range(no_of_rows):
        row = []
        for i in range(no_of_columns):
            row.append(random.randrange(1, 9))
        matrix.append(row)
    return matrix


def transpose_matrix(matrix: list) -> list:
    '''Transpose a matrix passed as a parameter.'''
    num_rows, num_cols = len(matrix), len(matrix[0])
    for i in range(num_cols):
        transpose.append([0] * num_rows)
    for row in range(num_rows):
        for column in range(num_cols):
            transpose[column][row] = matrix[row][column]
    return transpose


# Driver Code
matrix = random_number_matrix(no_of_rows, no_of_columns)
transpose = transpose_matrix(matrix)

# Output
print('This is the default matrix :\n')
for i in matrix:
    print(*i, sep=' ')
print('\n\nThis is the transposed matrix : \n')
for i in transpose:
    print(*i, sep=' ')
