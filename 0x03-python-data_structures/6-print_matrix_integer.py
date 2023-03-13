#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for i in row:
            print("{:d}".format(i), end=(" " if count < len(row) else ""))
            count = count + 1
        print()
