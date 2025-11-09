from typing import List


def remove_duplicates(nums: List[int]) -> int:

    #two pointers with for 
    # k = 1

    # for i in range(1, len(nums)):
    #     if nums[i] != nums[k-1]:
    #         nums[k] = nums[i]
    #         k += 1

    # return k

    # two pointers with while
    i = 1
    j = 1
    count = 1

    while j < len(nums):
        if nums[i-1] == nums[j]:
            j +=1
        else:
            nums[i] = nums[j]
            j += 1
            i += 1
            count += 1

    return count

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))


    