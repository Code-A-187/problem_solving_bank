from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_sum_count = {0: 1} # initial dict with prefix sum 0 and cpint 1

    for num in nums: # update prefix sum
        prefix_sum += num 
        if (prefix_sum - k) in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - k] # increasing count if prefix_sum-k is found
        if prefix_sum in prefix_sum_count:
            prefix_sum_count[prefix_sum] += 1 # update frecuency of current prefix sum
        else:
            prefix_sum_count[prefix_sum] = 1 # if prefix sum is seen for first time add it to dict
    
    return count

print(subarray_sum([-1,-1,1], k = 0))
print(subarray_sum(nums = [1,1,1], k = 2))
print(subarray_sum(nums = [1,2,3], k = 3))
if __name__=='__main__':
    pass