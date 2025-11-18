from typing import List

class NumArray:
    
    def __init__(self, nums: List[int]):
        self.new_array = [0]

        for i in range(len(nums)):
            self.new_array.append(self.new_array[-1] + nums[i])
    
    def sum_range(self, left: int, right: int) -> int:
        return self.new_array[right+1] - self.new_array[left]
        
        

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    
    obj = NumArray(nums)

    print("Prefix array:", obj.new_array)
    print("sum_range(0, 2) = ", obj.sum_range(0, 2))
    print("sum_range(2, 5) = ", obj.sum_range(2, 5))
    print("sum_range(0, 5) = ", obj.sum_range(0, 5))

