# Problem 36: Search Insert position
Difficulty: Easy
Category: Array
Approach: Iteration (forloop)

# Goal 
- Given sorted ascending array (from smallest to bigest)
- Given target value
- Return:
    - Index of target value in array
    - If target value not in array give index of place where value would be inserted in the sorted array
- Optional: needs to be O(log n) runtime complexity

# Example
Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:

    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:

    Input: nums = [1,3,5,6], target = 7
    Output: 4

# Logic
1. Go through sorted array
2. Check values in array compared to target value
    - If value bigger then or equals target:
        - then return current index
    - If value smaller then target:
        - move to next element
    - If at end of array:
        - return current index + 1
3. Continue until end of array or target value found