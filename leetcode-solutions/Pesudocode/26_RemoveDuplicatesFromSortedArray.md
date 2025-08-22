# Problem 26: Removed Duplicates from Sorted Array
Difficulty: Easy
Category: Array
Approach: Double Iteration (sorted array)

## Goal
- Array given in ascending order (smallest to biggest)
- Remove duplicates **in-place** (one array)
- Return:
    - First part of the array with **unique values in original order**
    - **Number of unique elements**
- After the unique elements:
    - Remaining values **do not matter**
    - Duplicates can be left out

## Examples
 Example 1:

    Input: nums = [1,1,2]

    Output: 2, nums = [1,2,_]

    Explanation: 
    Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
 Example 2:

    Input: nums = [0,0,1,1,1,2,2,3,3,4]

    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

    Explanation:
   Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

## Logic
1. Store unique element counter
2. Go through the array with two pointers:  
   - **Pointer 1** → marks the current element.  
   - **Pointer 2** → starts at the element right after Pointer 1. 
3. Compare values at Pointer 1 and Pointer 2:  
   - If they **match**:  
     - Remove duplicate from array 
     - Keep Pointer 2 at the same index, since the next element shifts into its place.
     - Continue until a different value is found.  
   - If they **don’t match**:  
     - Move on to the next comparison.  
4. After finishing with a value:  
   - Increase the unique element counter.  
   - Move Pointer 1 to the next element.  
   - Reset Pointer 2 to the element after Pointer 1.  
   - If either pointer reaches the end of the array → stop.  
5. Repeat until the array is fully checked.  
6. **Return**:  
   - The count of unique elements.  
   - The array with unique elements kept in order at the front and duplicates removed  

    