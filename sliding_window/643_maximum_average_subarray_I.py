from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    
    # with for cycle

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


    # whith while condition

    # i, j = 0, k
    # four_sum = sum(nums[i:j])
    # max_avg = four_sum / k
    
    # while j < len(nums):
    #     four_sum = four_sum-nums[i]+nums[j]
    #     current_avg = four_sum/k
    #     max_avg = max(max_avg, current_avg)

    #     i += 1
    #     j += 1

    # return max_avg
 
    
print(find_max_average([1,12,-5,-6,50,3], 4))
print(find_max_average([5], 1))
print(find_max_average([-1], 1))