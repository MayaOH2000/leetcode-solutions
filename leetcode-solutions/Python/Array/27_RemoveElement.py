# ID: 26
# Problem: Removed Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-element/
# Approch: Double Iteration

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    # Element != to removal value
    k = 0

    # Pointer 1 starting value
    p1 = 0

    while p1 < len(nums):
        #P2 starting position
        p2 = p1

        while p2 < len(nums):
            # Comapare values
            if nums[p2] == val:
                del nums[p2]
            else:
                p2 += 1 
        p1 += 1
        k +=1 
    return f"{k}, nums = {nums}"
    # In Leet Code they only want element value != to removal value
    # return k

# Example test cases
if __name__ == "__main__":
    print(removeElement([1,1,2,2,3,1,0], 1))   # Output 4, [2,2,3,0]
    print(removeElement([0,1,2,2,3,0,4,2],2))  # Output 5, [0,1,3,0,4,]