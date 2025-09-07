# ID: 268
# Problem: Missing Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/missing-number/
# Approach: Sort + Index Comparision

from typing import List

def missingNumber(nums: List[int]) -> int:
    # Return 0 if given empty array
    if not nums:
        return 0

    n = len(nums)
    nums.sort() # sorting array into ascending order (smallest to largest)

    # Checking if index number match value
    for i in range(len(nums)):
         # If mismatch then return missing number
        if i != nums[i]:   
            return i
    
    # If no mismatch found, missing number is n
    return n     


if __name__ == "__main__":
    print(missingNumber([0,1])) # Ouput 2
    print(missingNumber([0,2,4,1]))    # Output 3 
