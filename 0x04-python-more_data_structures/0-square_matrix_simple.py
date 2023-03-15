#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square =[]

    for row in matrix:
        rows = []
        for i in row:
            rows.append(i**2)
        square.append(rows)
    return square
