# -*- coding: utf-8 -*-

def elements_sum(matrix):
    """
    Esta función debe devolver la suma de todos los elementos de la matriz cuadrada dada
    :param matrix: matriz cuadrada
    :return: La suma de todos los elementos de la matriz
    """
    if all(len(row) == len(matrix) for row in matrix):
        return sum(sum(row) for row in matrix)
    else:
        return 'Error, matrix is not square'


def diagonal_sum(matrix):
    """
    Esta función debe devolver la suma de los elementos de la diagonal principal
    de la matriz cuadrada dada
    :param matrix: matriz cuadrada
    :return: La suma de los elementos de la diagonal principal de la matriz
    """
    if all(len(row) == len(matrix) for row in matrix):
        return sum(matrix[i][i] for i in range(len(matrix)))
    else:
        return 'Error, matrix is not square'



