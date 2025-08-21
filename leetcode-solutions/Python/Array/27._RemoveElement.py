# ID: 26
# Problem: Removed Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Approch: 

from typing import List

def removeElement(nums: List[int], val: int) -> int:



# Example test cases
if __name__ == "__main__":
    print(removeElement([1,1,2,2,3,1,0]),1)    #Output 4, [2,2,3,0]
    #print(removeElement([0,1,2,2,3,0,4,2]),2)  #Output 5, [0,1,3,0,4,]