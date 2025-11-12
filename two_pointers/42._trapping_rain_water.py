from typing import List

def trap(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    i_max, j_max = 0, 0
    result = 0

    while i < j:
        if height[i] <= height[j]:
            if height[i] >= i_max:
                i_max = height[i]
            else:

                result += i_max - height[i]
            
            i += 1
        else:
            if height[j] >= j_max:
                j_max = height[j]
            else:
                result += j_max - height[j]
            
            j -= 1

    return result


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))