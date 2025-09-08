# Problem 283: Move Zeroes
Difficulty: Easy  
Category: Array
Approach: Two Pointer

# Goal
- Given an array of intergers
    - Put all 0's at the end of array
    - Keep order of other non zero numbers
- Must be done `in-place` (no copying array)

# Example
    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:

    Input: nums = [0]
    Output: [0]

# Approach
1. Set two pointers:
    - p1 → pointer starting at index 0 (check numbers one by one)
    - p2 → always points to end of array (used as "insert at end")
2. Loop through array with p1:
    - If nums[p1] == 0:
        - Remove this zero from array
        - Append a 0 to the end of array
        - Do NOT move p1 forward (check this index again, since it now has a new number)
        - Move p2 one step left (end moves closer)
    - Else:
        - Move p1 forward (go to next number)
3. Repeat until p1 passes p2 

# Why It Works?
- Every time a zero is found, it is removed and pushed to the back
- Non-zero numbers shift left automatically, keeping their relative order
- Loop stops once all zeros are at the back