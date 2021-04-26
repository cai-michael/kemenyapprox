"""
Defines some matrix operations using on the Python standard library
"""

def generate_zeros_matrix(rows, columns):
    """
    Generates a matrix containing only zeros
    """
    matrix = [[0 for col in range(columns)] for row in range(rows)]
    return matrix

def get_column_as_list(matrix, column_no):
    """
    Retrieves a column from a matrix as a list
    """
    column = []
    num_rows = len(matrix)
    for row in range(num_rows):
        column.append(matrix[row][column_no])
    return column

def calculate_cell(matrix_a, matrix_b, row, column):
    """
    Calculates an individual cell's value after multiplication
    """
    matrix_b_column = get_column_as_list(matrix_b, column)
    column_length = len(matrix_b_column)
    products = [matrix_a[row][i]*matrix_b_column[i] for i in range(column_length)]
    return sum(products)

def matrix_multiplication(matrix_a, matrix_b):
    """
    Multiplies two matrices by each other
    """
    a_rows = len(matrix_a)
    a_columns = len(matrix_a[0])
    b_rows = len(matrix_b)
    b_columns = len(matrix_b[0])

    if a_columns != b_rows:
        raise Exception(f'Dimension mismatch: {a_columns}, {b_rows}')

    result = generate_zeros_matrix(a_rows, b_columns)
    for i in range(a_rows):
        for j in range(b_columns):
            result[i][j] = calculate_cell(matrix_a, matrix_b, i, j)
    return result
