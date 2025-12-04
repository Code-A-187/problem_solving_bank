# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


from typing import List
from math import floor

def search(nums: List[int], target: int) -> int:

    # half = nums

    # while len(half) > 1:   
    #     middle = floor(len(half) / 2)
    #     if half[middle] == target:
    #         return nums.index(target)
    #     elif half[middle] > target:
    #         half = half[:middle]
    #     elif nums[middle] < target:
    #         half = half[middle:]
    
    # else: return -1

    for n in range(len(nums)):
        if nums[n] == target:
            return n

    return -1


    



print(search(nums = [-1,0,3,5,9,12], target = 9))
print(search(nums = [-1,0,3,5,9,12], target = 2))