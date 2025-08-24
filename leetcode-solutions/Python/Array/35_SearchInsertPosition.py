# ID: 35
# Problem: Search Insert Position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/
# Approch: Iteration (for loop)

from typing import List

def searchInsert( nums: List[int], target: int) -> int:
    #Going throught array
    for index in range(len(nums)):
        #Comparring values to target
        if nums[index] >= target:
            return index
        else:
            #What to do when reached last element of array and no target value
            if index == len(nums) - 1:
                return index + 1
            

# Example test cases
if __name__ == "__main__":
    print(searchInsert([1,3,5,6],5))    # Output 2
    print(searchInsert([1,3,5,6],2))    # Output 1
    print(searchInsert([1,3,5,6],7))    # Output 4