# Problem 228: Summary Ranges
Difficulty: Easy  
Category: Array
Approach: Two pointers (check for consecutive numbers)

# Goal
- Given an array of numbers
    - Each number is unique
    - Sorted in ascending order (smallest to biggest)
- Find all ranges of consecutive numbers in the array.
    - Each range goes from the first number to the last consecutive number (a-b, including b).
    - If a number stands alone, just return that number as its range.

# Example
Example 1:

    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]

    Explanation: 
    The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"

Example 2:

    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]

    Explanation: 
    The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"

# Approach
1. Initialize two pointers and the start of the range:  
   - `p1` → current value  
   - `p2` → next value  
   - `start` → start of the current range  
2. Loop through the array:  
   - If `p2 == p1 + 1`: the sequence is consecutive → move `p2` to the next value  
   - If `p2 != p1 + 1`: the sequence broke →  
       - Add the range from `start` to `p1` to the list  
       - Set `start = p2` for the next range 
3. Continue this process until the end of the array.  
4. Return the list of ranges.  

# Why This Works
- `start` marks the beginning of each range, while `p1` and `p2` let us check consecutive numbers.  
- When the sequence breaks, we record the range (or single number) and start a new range.  
- This ensures we capture all consecutive ranges and single numbers correctly.