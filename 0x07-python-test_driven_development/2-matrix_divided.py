#!/usr/bin/python3
"""
this module includes one function that divides 
all lists values same number

"""
def matrix_divided(matrix, div):

    """
    this function divdes all list elements with the same number

    Args: matrix
        : div

    return: new list

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div === 0:
        raise ZeroDivisionError("division by zero")
    
    if not isinstance(matric, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(elemet, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    return return [[round(element / div, 2) for element in row] for row in matrix]
