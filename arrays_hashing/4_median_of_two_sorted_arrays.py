# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # merge the two sorted arrays
    merged_array = sorted(nums1 + nums2)
    # length of merged
    length = len(merged_array )

    if length % 2 == 0:
        return (merged_array[length // 2 - 1] + merged_array[length // 2]) / 2
    else:
        return merged_array[length // 2]

    

print(find_median_sorted_arrays(nums1 = [1,2], nums2 = [3,4]))
print(find_median_sorted_arrays(nums1 = [1,3], nums2 = [2]))