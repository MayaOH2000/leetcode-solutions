# Problem 217: Contains Duplicate
Difficulty: Easy  
Category: Array  
Approach: used Set to store numbers

# Goal
- Given an array of integers  
    - Return:
        - True → if any number appears at least twice
        - False → if all numbers are unique

# Example
Example 1:

    Input: nums = [1,2,3,1]
    Output: true

    Explanation:
    The element 1 occurs at indices 0 and 3.

Example 2:

    Input: nums = [1,2,3,4]
    Output: false

    Explanation:
    All elements are distinct.

Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

# Approach
1. Create an empty set to track seen numbers  
2. Loop through the array:
    - If number already in set:
        - Return True (duplicate found)
    - Else:
        - Add number to set
        - Move to next number
3. If loop finishes with no duplicates found:
    - Return False

# Notes on Set
- A set only stores **unique values** (no duplicates allowed)
- Example:
    
      set([3, 3, 1]) → {1, 3}  # order does not matter
