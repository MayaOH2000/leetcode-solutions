# Problem 118: Pascal's Triangle
Difficulty: Easy
Category: Array, Dynamic Programming (DP)
Approach: Build row by row using previous row (DP)

# Goal
- Given number of rows
- Return:
    - first number of rows of **Pascal's triangle**

### Pascal's Triangle
- Rule: each number is the **sum of the two numbers above it**  
- Always starts with `1` at the top  

Row 1:        1
Row 2:       1 1
Row 3:      1 2 1     (2 = 1+1)
Row 4:     1 3 3 1    (3 = 1+2, 3 = 2+1)
Row 5:    1 4 6 4 1   (4 = 1+3, 6 = 3+3, 4 = 3+1)
         1 5 10 10 5 1
# Example
Example 1:

    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

    Input: numRows = 1
    Output: [[1]]

# Approach
1. Start with the first row: `[1]`
2. Always add `1` at the **start and end** of each new row.
3. Fill in the middle numbers by **adding the two numbers above** from the previous row.
   - If the row has an **odd number of elements**, the middle number is unique.
   - If the row has an **even number of elements**, the middle numbers mirror each other.
4. Repeat until you reach the desired number of rows.
5. Return the list of all rows.

# Key DP idea
- Each row **reuses information from the previous row** to build the next row.
- No sums are recalculated unnecessarily — this is the core DP principle.