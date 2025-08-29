# ID: 118
# Problem: Pascal's Triangle
# Difficulty: Easy
# Link: https://leetcode.com/problems/pascals-triangle/
# Approach: Build row by row using previous row (DP)

from typing import List, Optional

"""Generates Pascal's Triangle with the specified number of rows."""
def generate(numRows: int) -> List[List[int]]:
    # Base case row 1
    triangle = [[1]]
    
    # Build rest of rows
    for row_index in range (1,numRows):
     
        # Row above the current one
        prev_row = triangle[row_index -1] 
        new_row = [1] #start each row with 1

        # Compute middle numbers from row above
        for position in range(1,row_index):
            # Sum the two numbers directly above the current position
            new_row.append(prev_row[position -1] + prev_row [position])

        # Add 1 at the end of each new row
        new_row.append(1)

        # Add new completed row to triangle
        triangle.append(new_row)

    return triangle


if __name__ == "__main__":
    print(generate(5))  # Output [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    # print(generate(1))  # Output [[1]]