from typing import List


def remove_duplicates(nums: List[int]) -> int:
    # with for 
    # k = 2

    # for i in range(2, len(nums)):
    #     if nums[i] != nums[k-2]:
    #         nums[k] = nums[i]
    #         k += 1

    # return k

    # with while
    i = 2
    j = 2
    count = 2

    while j < len(nums):
        if nums[i-2] == nums[j]:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
            count += 1

    return count


print(remove_duplicates([1,1,1,2,2,3]))
print(remove_duplicates([0,0,1,1,1,1,2,3,3]))