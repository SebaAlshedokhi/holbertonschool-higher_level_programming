#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_list = []
        for j in range(len(matrix[i])):
            new_list.append((matrix[i][j]) ** 2)
        new_matrix.append(new_list)
    return new_matrix
