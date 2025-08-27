# Problem 88: Merge Sorted Array
Difficulty: Easy
Category: Array
Approach: Two Pointer (from back)

# Goal
- Given two integer arrays sorted in ascending order (smallest to largest):  
    - m = number of elements in array 1 that need to be merged  
    - n = number of elements in array 2  
- Merge array 1 and array 2 in ascending order (smallest to largest)  
- Store the final merged array in array 1  
    - Final length of array 1 = m + n  
    - The last n elements in array 1 are extra space (0 placeholders) to store elements from array 2

# Example
Example 1:

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: 
    The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


Example 2:

    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation:
    The arrays we are merging are [1] and [].
    The result of the merge is [1].


Example 3:

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: 
    The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# Approach
1. Use three pointers to merge the arrays in place:
   - Pointer 1 → Points to the last valid element in array 1 (the numbers that need to be merged)
   - Pointer 2 → Points to the last element in array 2
   - Pointer 3 → Points to the last index of array 1 (where the merged numbers will go)
2. Compare the values at Pointer 1 and Pointer 2:
   - If the value at Pointer 1 is greater than or equal to the value at Pointer 2:
       - Place the value from Pointer 1 into the position of Pointer 3
       - Move Pointer 1 one step backward
   - Else:
       - Place the value from Pointer 2 into the position of Pointer 3
       - Move Pointer 2 one step backward
   - Move Pointer 3 one step backward each time
3. Continue this process until Pointer 2 is finished (Pointer 2 < 0):
   - If any values remain in Pointer 2, copy them into array 1
   - If any values remain in Pointer 1, they are already in the correct place
4. Result:
   - Array 1 now contains all numbers from both arrays in ascending order, merged **in place**


# Note
- Key trick: fill nums1 from the back to avoid overwriting