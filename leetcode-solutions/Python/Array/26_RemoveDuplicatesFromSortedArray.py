# ID: 26
# Problem: Removed Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Approch: Double Iteration (sorted array)

from typing import List

def removeDuplicates( nums: List[int]) -> int:
    # Counter for new elements
    new_num = 0

    # pointer 1 starting position
    p1 = 0
   
    while p1 < len(nums):
        # pointer 2 starting positions
        p2 = p1 + 1
        while p2 < len(nums):
                # compares pointer 1 and pointer 2 values      
                if nums[p1] == nums[p2]:
                    del nums[p2] 
                else:
                    p2 += 1 
        new_num += 1    
        p1 += 1
    return f"{new_num}, nums = {nums}"
    # In leetcode it just want the unique element count as integer
    # return nums

# Example test cases
if __name__ == "__main__":
    print(removeDuplicates([1,1,2,3]))    # Output 3, [1,2,3]
    print(removeDuplicates([0,0,1,2,2,2,3,3,4,5,5])) #Ouput 6, [0,1,2,3,4,5]