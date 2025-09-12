# ID: 349
# Problem: Intersection of Two Arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Approach: Set intersection using & operator

from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    # Make the list inot set to contain unique values
    s1 = set(nums1)
    s2 = set(nums2)

   # Use set intersection (&) to find common elements, then convert back to list
    return list(s1 & s2)


if __name__ == "__main__":
    print(intersection([1,2,4,5,6,7,8,3],[1,0,5,9,8,7,0,5,4,1])) # Ouput [1,4,5,7,8]