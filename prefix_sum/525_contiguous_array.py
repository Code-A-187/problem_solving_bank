from typing import Counter, List


def find_max_length(nums: List[int]) -> int:
    seen_dict = {0:-1}
    max_len = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if count in seen_dict:
            max_len = max(max_len, i - seen_dict[count])
        else:
            seen_dict[count] = i
            
    return max_len


print(find_max_length([0,1]))
print(find_max_length([0,1,0]))
print(find_max_length([0,1,1,1,1,1,0,0,0]))
