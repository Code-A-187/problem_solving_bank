from typing import List

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# makin diagonal swop of rows with cols

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
rotate(matrix)

for row in matrix:
    print(' '.join(map(str, row)))

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]

for row in matrix:
    print(' '.join(map(str, row)))


