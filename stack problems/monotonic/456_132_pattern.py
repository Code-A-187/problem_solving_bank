#Given an array of n integers nums, 
# a 132 pattern is a subsequence of three integers nums[i], 
# nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

from typing import List


def find_132_pattern(nums: List[int])-> bool:

    minimums = [0] * len(nums)
    stack = []
  
    for i in range(len(nums)):    
     #setup minimums
        if i == 0:
            minimums[i] = 0
        else:
            if nums[i] < nums[minimums[i - 1]]:
                minimums[i] = i
            else: 
                minimums[i] = minimums[i - 1]
    
        # using template for finding previous greater elements
    
        #find previous greater element, build monotonic decreasing stack
        while stack and nums[stack[-1]] <= nums[i]:
            stackTop = stack.pop()
        
        #if there is a previous greater element, stack will not be empty
        if stack:
        # if the previous minimum for the previous greater element is
        #less than the current number, then we return true
            if nums[minimums[stack[-1]]] < nums[i]:
                return True

        stack.append(i)

    return False

    # third = -float('inf')
    # stack = []
    # for i in range(len(nums) - 1, - 1, -1):
    #     if third > nums[i]:
    #         return True
            
    #     while stack and stack[-1] < nums[i]:
    #         third = stack.pop()
            
    #     stack.append(nums[i])
        
    # return False

print(find_132_pattern([1,2,3,4]))
print(find_132_pattern([3,1,4,2]))
print(find_132_pattern([-1,3,2,0]))
print(find_132_pattern([-2,1,2,-2,1,2]))
