from typing import List

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(nums: List[int]) -> bool:

    if len(set(nums)) == len(nums):
        return False
    else:
        return True

    # nums.sort()
    #
    # for i in range(len(nums) -1):
    #     if nums[i] == nums[i+1]:
    #         return True
    #
    # return False

print(contains_duplicate([1,3,5,4,2]))

