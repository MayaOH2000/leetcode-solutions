# Problem 303: Range Sum Query - Immutable
Difficulty: Easy  
Category: Array
Approach: Prefix Sum

# Goal
- Given an array oof integers:
    - calculate the sum of numbers in the range from left to right ( including left and right  index numbers)
- Multiple calls of ranges can be used
- Return sum if each range given

# Example
Example 1:

    Input
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output
    [null, 1, -1, -3]

    Explanation
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# Approach
1. Build a prefix sum array that stores the running total at each index.
2. Start with the first element as the initial sum.
3. For each next element, add it to the running total and store it in the prefix sum array.
4. To calculate the sum of a range [i, j], use:
   - range_sum = prefix[j] - prefix[i - 1]
   - Special case: if i = 0, then just return prefix[j].
5. Return the sum for each query (request).

# Why It Works
- The prefix sum array avoids recalculating sums for every query (request).
- `prefix[j]` = total sum up to index j  
- `prefix[i - 1]` = total sum before index i  
- Subtracting gives the sum of just the range [i, j].

## Dry Run Example
Input: nums = [1, 2, 3, 4, 5], query = (2, 4)

- prefix[0] = 1  
- prefix[1] = 3 (1+2)  
- prefix[2] = 6 (1+2+3)  
- prefix[3] = 10 (1+2+3+4)  
- prefix[4] = 15 (1+2+3+4+5)

Range sum (2, 4): prefix[4] - prefix[1] = 15 - 3 = 12  
Which matches 3 + 4 + 5 = 12.
 