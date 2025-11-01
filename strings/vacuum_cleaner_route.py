class Solution(object):
    def vacuum_returns_start(self, moves: str):

        right = 0
        left = 0
        up = 0
        down = 0

        for move in moves:
            if move == "R":
                right += 1
            if move == "L" or move == "R":
                left += 1
            if move == "U":
                up += 1
            if move == "D":
                down += 1
        if right == left and down == up:
            return True
        else:
            return False

print(Solution().vacuum_returns_start("RUULLDRD"))