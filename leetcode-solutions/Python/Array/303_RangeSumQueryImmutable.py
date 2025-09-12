# ID: 303
# Problem: Range Sum Query - Immutable
# Difficulty: Easy
# Link: https://leetcode.com/problems/range-sum-query-immutable/
# Approach: Prefix Sum

from typing import List

class NumArray:

    def __init__(self,nums: List[int]):
        # Creating an array of zeros the size of array length
        self.num = [0]* len(nums)

        if nums:
            self.num[0] = nums[0] # Setting first sum to first number
            # Added rest of running total 
            for i in range(1,len (nums)):
                # adding up running totals
                self.num[i] = self.num[i-1] + nums[i] 

    def sumRange(self, left: int, right: int) -> int:
        # Getting totals faster
            if left == 0:
                return self.num[right] # no subtraction needed
            return self.num[right] - self.num[left -1]

# From leet code
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# -------------------------------------

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    obj = NumArray(nums)

    queries = [(0, 2), (1, 3), (2, 4)]
    for left, right in queries:
        print(f"Sum of nums[{left}:{right}] = {obj.sumRange(left, right)}")