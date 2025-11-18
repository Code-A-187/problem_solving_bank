from itertools import accumulate
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    # we have second array
    running_sum = []
    # append to second array the first el from nums array
    running_sum.append(nums[0])
    # starting from second element append sum from current element in nums with previous element in running_sum
    for i in range(1, len(nums)):
        running_sum.append(running_sum[i-1] + nums[i])

    return running_sum
    
    # make it in place
    # for i in range(1, len(nums)):
    #     nums[i] = nums[i-1] + nums[i]
    #     nums = [i + i - 1 for i in nums]
    
    # return nums

    # some hack staff
    # nums = list(accumulate(nums))
    # return nums

    # with wallrus operator 
    # s = 0
    # nums = [s := s + x for x in nums]
    # return nums


print(running_sum([1,2,3,4]))
print(running_sum([1,1,1,1,1]))
print(running_sum([3,1,2,10,1]))