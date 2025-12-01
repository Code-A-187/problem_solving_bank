from typing import List


def visible_people(heights: List[int]) -> List[int]:
    n = len(heights)
    stack = []

    res = [0] * n

    for i in range(n):
        while stack and heights[i] > heights[stack[-1]]:
            idx = stack.pop()
            res[idx] += 1
        if stack:
            res [stack[-1]] += 1
        
        stack.append(i)

    
    return res

print(visible_people([10,6,8,5,11,9]))
print(visible_people([5,1,2,3,10]))