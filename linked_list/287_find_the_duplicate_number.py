from typing import List


def find_duplicate_number(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    
    return slow

print(find_duplicate_number(nums = [1,3,4,2,2]))