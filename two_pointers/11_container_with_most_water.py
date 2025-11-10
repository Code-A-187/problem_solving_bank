from typing import List

def most_water(height: List[int]) -> List[int]:
    i = 0
    j = len(height) - 1
    max_area = 0

    while i < j:
        cur_area = (min(height[i], height[j])) * (j-i)
        
        max_area = max(cur_area, max_area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area

print(most_water([1,8,6,2,5,4,8,3,7]))
print(most_water([1,1]))
