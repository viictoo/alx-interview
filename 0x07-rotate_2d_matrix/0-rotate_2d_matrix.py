#!/usr/bin/python3
"""rotate a matrix by 90 degrees"""


def rotate_2d_matrix(mat):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Do not return anything. The matrix must be edited in-place
    """
    N = len(mat)
    # Consider all squares one by one
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            # store current cell in temp variable
            temp = mat[x][y]
            # Move values from left to top
            mat[x][y] = mat[N-1-y][x]
            # move values from bottom to left
            mat[N-1-y][x] = mat[N-1-x][N-1-y]
            # move values from right to bottom
            mat[N-1-x][N-1-y] = mat[y][N-1-x]
            # assign temp to left
            mat[y][N-1-x] = temp
