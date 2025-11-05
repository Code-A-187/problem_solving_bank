from typing import List

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
# need to find the borders of the matrix when it is reached to switch to next diagonal


def find_diagonal_order(mat: List[int]) -> List[int]:
    rows, cols = len(mat), len(mat[0])

    cur_row = 0
    cur_col = 0

    diag_arr = []

    going_up = True

    while len(diag_arr) != rows * cols:
        if going_up:
            while cur_row >= 0 and cur_col < cols:
                diag_arr.append(mat[cur_row][cur_col])

                cur_row -= 1
                cur_col += 1

            if cur_col == cols:
                cur_row += 2
                cur_col -= 1
            else:
                cur_row += 1
                
            going_up = False
        else:
            while cur_row < rows and cur_col >= 0:
                diag_arr.append(mat[cur_row][cur_col])

                cur_row += 1
                cur_col -= 1

            if cur_row == rows:
                cur_row -= 1
                cur_col += 2  
            else: 
                cur_col += 1  
                
            going_up = True

    return diag_arr

print(find_diagonal_order([[1,2],[3,4]]))
print(find_diagonal_order([[1,2,3],[4,5,6],[7,8,9]]))

