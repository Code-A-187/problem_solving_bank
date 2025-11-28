from typing import List

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, 
# which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

def next_greater_elements(nums: List[int]) -> List[int]:
    n = len(nums)
    # stack that will store the indexes of the numbers that still don't have greater number found.
    stack = []

    
    # we have result array with len == nums and with -1 already it in
    next_greater = [-1] * n

    # we must have some criterium so for el in list while we found the next greater element
    # iterate twice nums array
    for i in range(2 * n):
        idx = i % n
        while stack and nums[idx] > nums[stack[- 1]]:
            index = stack.pop()
            next_greater[index] = nums[idx]
        if i < n:
            stack.append(idx)

        
    return next_greater

print(next_greater_elements([6, 8, 0, 1, 3]))
print(next_greater_elements([1,2,3,4,3]))