# ID: 350
# Problem: Intersection of Two Arrays II
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Approach: Counter Intersection (to keep duplicates)

from typing import List
from collections import Counter

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    # Counter intersection gives common elements including duplicates
    return list((Counter(nums1) & Counter(nums2)).elements())

if __name__ == "__main__":
    print(intersection([1,2,2,0,1],[1,0,5,1])) # Ouput [1,1,0]