# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
from typing import List


def longest_sequence(nums: List[int]) -> int:
    st = set()
    res = 0

    # add all elements in hash set
    for val in nums:
        st.add(val)

    for val in nums:

        # search if value is starting point of sequence
        if val in st and val-1 not in st:
            cur = val
            cnt = 0
            # removing current number to avoid recomputation
            while cur in st:

                st.remove(cur)
                cur += 1
                cnt += 1

            # update optimal length
            res = max(res, cnt)

    return res


    # Naive solution:   
    #  
    # if not nums:
    #     return 0
    # nums.sort()
    # res = 1
    # cnt = 1
    # for i in range(1, len(nums)):
    #     # Skip Duplicates     
    #     if nums[i] == nums[i - 1]:
    #         continue
    #     if nums[i] == nums[i - 1] + 1:
    #         cnt += 1
    #     else:
    #         res = max(res, cnt)
    #         cnt = 1

    # res = max(res, cnt)       


    # return res

print(longest_sequence([9,1,4,7,3,-1,0,5,8,-1,6]))
print(longest_sequence([]))