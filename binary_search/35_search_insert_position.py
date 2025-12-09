from typing import List


def search_insert(nums: List[int], target: int) -> int: 
    # if target in nums:
    #     return nums.index(target)
    # else:
    #     nums.append(target)
    #     sorted_nums = sorted(nums)
    #     return sorted_nums.index(target)

    l = 0
    r = len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l

print(search_insert(nums = [1,3,5,6], target = 5))
print(search_insert(nums = [1,3,5,6], target = 2))
print(search_insert(nums = [1,3,5,6], target = 7))