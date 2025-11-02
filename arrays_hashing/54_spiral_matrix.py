from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])

    spiral_arr = []

    top = 0
    bottom = m - 1
    left = 0
    right = n - 1

        # start from first [0,0] and go right
        # if hit end of arr go down
        # if hit end of matrix go right
        # if hit start of arr go up
        # if hit already in spiral array go right
    
    while top <= bottom and left <= right:

        # top row from left to right
        
        for i in range(left, right + 1):
            spiral_arr.append(matrix[top][i])
        top += 1

        # right column from top bottom

        for i in range(top, bottom + 1):
            spiral_arr.append(matrix[i][right])
        right -= 1

        # bottom row from left to right

        if top <= bottom:
            for i in range(right, left -1, -1):
                spiral_arr.append(matrix[bottom][i])
            bottom -= 1

        # left row from left to right

        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral_arr.append(matrix[i][left])
            left += 1
 
    return spiral_arr

          
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(spiral_matrix(matrix))

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print(spiral_matrix(matrix))
