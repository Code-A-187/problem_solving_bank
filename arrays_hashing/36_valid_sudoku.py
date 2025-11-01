# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
# need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# 
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict
from typing import List


def valid_sudoku(board: List[List[str]]) -> bool:
    # use hashset to store elements of each rol, column and box
    # row defaultdict(set) (idx -> hashset)
    # column defaultdict(set) (idx -> hashset)
    # box defaultdict(set) (idx -> hashset)
    # we have to be able to convert some (r, c) in some identifier for its coresponding box
    # [4, 4] => [4 // 3, 4 // 3] => (1,1)
    # [2, 2] => [2 // 3, 2 // 3] => (0,0)
    # [8, 8] => [8 // 3, 8 // 3] => (2,2)

    # row 0: 0,1,2
    # row 1: 3,4,5
    # row 2: 6,7,8

    # col 0: 0,1,2
    # col 1: 3,4,5
    # col 2: 6,7,8


    row = defaultdict(set) # we utilize rows[0] => set() we can use to check in O(1) time if the digit already exists in row 0
    column = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if board[r][c] in row[r]:
                return False
            if board[r][c] in column[c]:
                return False
            if board[r][c] in boxes[(r//3, c//3)]:
                return False
            
            row[r].add(board[r][c])
            column[c].add(board[r][c])
            boxes[(r//3,c//3)].add(board[r][c])

    return True



board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

print(valid_sudoku(board))