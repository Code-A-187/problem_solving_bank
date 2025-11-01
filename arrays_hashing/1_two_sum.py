# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums: list[int], target:int) -> list[int]:

    for i in range(len(nums)):
        for j in range( i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    # faster approach with enumarate()+
    # hmap = {}
    # for idx, num in enumerate(nums):
    #     compliment = target - num
    #     if num not in hmap:
    #         hmap[compliment] = idx
    #     else:
    #         return [hmap.get(num), idx]

print(two_sum([2,5,5,11], 10))
print(two_sum([2,11,7,15], 9))