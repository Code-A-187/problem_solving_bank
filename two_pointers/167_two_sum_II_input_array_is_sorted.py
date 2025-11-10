from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    # if two pointers whould be used
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        result = numbers[left] + numbers[right]
        if result == target:
            return [left + 1, right + 1]
        if result < target:
            left += 1
        else:
            right -= 1

    # faster approach with enumarate()
    # hmap = {}
    # for idx, num in enumerate(numbers):
    #     compliment = target - num
    #     if num not in hmap:
    #         hmap[compliment] = idx
    #     else:
    #         return [hmap.get(num) + 1, idx + 1]
    
    # return enumerate()

print(two_sum([2,7,11,15], 9))
print(two_sum([2,3,4] , 6))
print(two_sum([-1,0], -1))


