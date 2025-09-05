# ID: 219
# Problem: Contains Duplicate II
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# Approach: 

from typing import List

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:



if __name__ == "__main__":
    print(containsNearbyDuplicate([1,0,1,1], 1)) # Output True  (index 3-2 = 1 <= 1)
    print(containsNearbyDuplicate([1,2,3,1,4], 3)) # Output Ture (index 3-0 = 3 <= 3)
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))    # Ouput False 