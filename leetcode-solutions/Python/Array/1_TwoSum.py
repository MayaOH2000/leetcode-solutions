#ID: 1
#Problem: Two Sum
#Difficulty: Easy
#Link: https://leetcode.com/problems/two-sum/

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    #Empty list to store values
    seenNum = []

    #Loop trough array 
    #enumerate (iterable, start) ->  creates a collection of index + value
    #i: index, num: element/value
    for i, num in enumerate(nums): 
        #calculate missing number
        missing = target - num

        #Check if missing already in the seen
        for index , val in seenNum:
            if val == missing:
                return [index, i]
            
        #Add new values to empty list (index, value)
        seenNum.append((i,num))


# Example test cases
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(twoSum([3,2,4], 6))         # Output: [1, 2]

