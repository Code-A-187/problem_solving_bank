
# Given an integer array nums of length n and an integer target, 
# find three integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

from typing import List

def three_sum_closest(nums: List[int], target: int) -> int:
# first sort the list
    nums.sort()

    # find the sum from first three nums in array

    closest_sum = nums[0] + nums[1] + nums[2]

# iterrate trough the list with two pinters
    for i in range(len(nums)-2):
        left, right = i+1, len(nums)-1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if curr_sum == target:
                return target

            if abs(curr_sum-target) < abs(closest_sum-target):
                closest_sum = curr_sum
            
            if target > curr_sum:
                left += 1
            else:
                right -= 1
                
    return closest_sum




print(three_sum_closest(nums = [-1,2,1,-4], target = 1))
print(three_sum_closest(nums = [0,0,0], target = 1))