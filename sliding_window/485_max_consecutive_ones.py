from typing import List


def max_consecutive_ones(nums: List[int]) -> int:
    max_count = 0
    count = 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0


    return max(max_count, count)

print(max_consecutive_ones([1,1,0,1,1,1]))
print(max_consecutive_ones([1,0,1,1,0,1]))