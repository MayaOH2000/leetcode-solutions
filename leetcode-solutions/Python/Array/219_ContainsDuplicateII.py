# ID: 219
# Problem: Contains Duplicate II
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# Approach: Hasmap (dictionary)

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    seen = {}   # Track most recent index of each number

    # i = index, num = value for enumarator
    for i, num in enumerate(nums):
        # Check if we've seen this number before within distance k
        if num in seen and i - seen[num] <= k:
            return True
        
        # Update with current index (overwrite previous occurrence)
        seen[num] = i   # dictionary [key] = value

    return False

if __name__ == "__main__":
    print(containsNearbyDuplicate([1,0,1,1],1)) # Output True  (index 3-2 = 1 <= 1)
    print(containsNearbyDuplicate([1,2,3,1,4],3)) # Output Ture (index 3-0 = 3 <= 3)
    print(containsNearbyDuplicate([1,2,3,1,2,3],2))    # Ouput False 
    print(containsNearbyDuplicate([1,0],1)) # Ouput False (no duplicates found)