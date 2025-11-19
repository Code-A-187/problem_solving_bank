from typing import List


def check_subarray_sum(nums: List[int], k: int) -> bool:
    remainder_dict = {0: -1}
    moving_sum = 0

    for i in range(len(nums)):
        moving_sum += nums[i]
        remainder = moving_sum % k

        if remainder in remainder_dict:
            if i - remainder_dict[remainder] > 1:
                return True
        else:
            remainder_dict[remainder]  = i
    return False
        
print(check_subarray_sum(nums = [23,2,4,6,6], k = 7))
print(check_subarray_sum(nums = [23,2,6,4,7], k = 13))
