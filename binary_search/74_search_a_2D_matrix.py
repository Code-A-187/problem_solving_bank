from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    result = False
    l_row = 0
    r_row = len(matrix) - 1
    
    while l_row <= r_row:
        mid_row = (l_row + r_row) // 2
        if matrix[mid_row][0] < target:
            l_row = mid_row + 1
        elif matrix[mid_row][0] > target:
            r_row = mid_row - 1 
        else:
            return True
    
    l_col = 0
    r_col = len(matrix[0]) - 1
    
    while l_col <= r_col:
        mid_col = (l_col + r_col) // 2
        if matrix[r_row][mid_col] < target:
            l_col = mid_col + 1
        elif matrix[r_row][mid_col] > target:
            r_col = mid_col - 1 
        else:
            return True

    return result


    # for row in matrix:
    #     if target in row:
    #         return True
    # return False

print(search_matrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(search_matrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))