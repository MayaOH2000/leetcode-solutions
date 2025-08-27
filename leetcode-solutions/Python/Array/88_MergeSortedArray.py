# ID: 88
# Problem: Merge Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-sorted-array/
# Approach: Two Pointer (from back)

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    #Initilizing pointers
    p1 = m - 1  # last valid num array 1
    p2 = n -1   # last element in array 2
    p3 = m + n - 1 # last element in array 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            # Inserting value into array
            nums1[p3] = nums1[p1]
            p1 -= 1 # moving pointer
        else:
            nums1[p3] = nums2[p2] # Insert value of p2 two
            p2 -=1
        p3 -= 1

    # Copy any remaining values in array 2 into array 1
    # Any values remaing in array 1 would be correct
    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
        p3 -= 1

    #testing purposses
    print(nums1)

if __name__ == "__main__":
    print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))  # Output [1,2,2,3,5,6]
    print(merge([0], 0, [6], 1))    # Output [6]
    print(merge([5], 1, [0], 0))    # Outuput [5]