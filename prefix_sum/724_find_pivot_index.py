from typing import List


def pivot_index(nums: List[int]) -> int:
    # we pre-sum the right sum
    l_sum, r_sum = 0, sum(nums)
    # we iterate with enumerate so we can find index
    for idx, el in enumerate(nums):
        # we exclude the current element from right sum
        r_sum -= el
        # check if left sum and right sum are equal
        if l_sum == r_sum:
            # if equal return pivot index
            return idx
        # include the current number in left sum and move to next element
        l_sum += el
    
    return -1


print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
print(pivot_index([2,1,-1]))