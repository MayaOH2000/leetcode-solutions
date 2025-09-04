# ID: 217
# Problem: Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/
# Approach: Used set to store numbers 

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    seen = set()  # track seen numbers

    for num in nums:
        if num in seen:
            return True  # duplicate found
        seen.add(num)  # store number

    return False  # no duplicates found


if __name__ == "__main__":
    print(containsDuplicate([1,1,1,3,3,4,3,2])) # Output True
    print(containsDuplicate([1,3,1])) # Output True
    print(containsDuplicate([1,2,3]))   # Output False
    print(containsDuplicate([0]))   # Output False