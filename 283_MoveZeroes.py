# ID: 283
# Problem: Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/
# Approach: Two Pointer

from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    p1 = 0
    p2 = len(nums)  # track end of array

    while p1 < p2:
        if nums[p1] == 0:
            nums.pop(p1)      # remove zero
            nums.append(0)    # push zero to end
            p2 -= 1           # end moves one step left
            # don't move p1, check this index again (new value is here now)
        else:
            p1 += 1           # move to next index

    return nums  # for testing

if __name__ == "__main__":
    print(moveZeroes([0,1,0,3,12])) # Output [1,3,12,0,0]