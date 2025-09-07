# Problem 268: Missing Number
Difficulty: Easy  
Category: Array
Approach: Sort + Index Comparision

# Goal
- Given an array of numbers
- Find the missing number in the range 
    - Range is length of array (n)
    - Numbers are all unique
    - Number range is `[0, n]` , n = array range
- Optional:
    - O(1) extra space complexity 
    - O(n) runtime complexity

# Example
Example 1:

    Input: nums = [3,0,1]

    Output: 2

    Explanation:
    n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

    Input: nums = [0,1]

    Output: 2

    Explanation:
    n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

    Input: nums = [9,6,4,2,3,5,7,0,1]

    Output: 8

    Explanation:
    n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# Appraoach
1. Sort the array in ascending order (smallest to biggest)
2. Get length of array -> `n = len(nums)`
3. Go through array
    - Compare current value if it matches index value
        - If at end array and all numbers are in sequence:
            - Then missing number is n
        - If value matched index:
            - Move to next position
        - If no match:
            - Return index since that will be missing number

# Why it works?
- Sorting puts numbers in order so the index should match its value.  
- The **first mismatch** between index and value gives the missing number.  
- If no mismatch is found, the missing number is `n` (since `[0, n-1]` are all present). 