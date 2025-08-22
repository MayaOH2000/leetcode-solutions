# Problem 27: Remove Element
Difficulty: Easy
Category: Array
Approach: Double Iteration

# Goal
- Given an array of intergers and value to remove
- Remove all values of given element **in place** (one array)
-   Order of elements can be changed
- Return:
    - **numbers not equal to value of Removal**
    - First values of array need to  elements not equal to removal value
    - Elements can appear in any order
- After the elements that are numbers not equal to value of Removal:
    - Remaining values **do not matter**
    - Removal element can be left out

# Example

Example 1:

    Input: nums = [3,2,2,3], val = 3

    Output: 2, nums = [2,2,_,_]

    Explanation: 
    Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:

    Input: nums = [0,1,2,2,3,0,4,2], val = 2

    Output: 5, nums = [0,1,4,0,3,_,_,_]

    Explanation: 
    Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).

# Logic
1. Store value for numbs not equal to removal value (k)
2. Go through array with two pointers:
    - **Pointer 1** -> Current element
    - **Pointer 2** -> Same place as pointer 1
3. Compare Pointer 2 Values to removal value:
    - If **match**:
        - Remove element
        - Keep pointer 2 at same index
    - If **no match**:
        - Move to next element
4. After finishing with a value:
    - Add 1 to k (numbers not euqal to removal value)
    - Move pointer 1 to next value
    - Reset pointer 2 back to pointer 1 value
    - Pointer 1 or pointer 2 reaches end of array -> stop
5. Continue until array been fully checked
6. **Return:**
    - The count of elements not equal to removal value  
    - The array with all elements not equal to removal value in front and removal value gone
    