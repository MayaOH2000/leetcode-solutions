# ID: 119
# Problem: Pascal's Triangle II
# Difficulty: Easy
# Link: https://leetcode.com/problems/pascals-triangle-ii/
# Approch: Build row by row using previous row (DP)

from typing import List

# Similar approach as problem 118 except just need the row

def getRow(rowIndex: int) -> List[int]:
    # Row 0 is always just [1]
    row = [1]   

    # Make rows (add + 1 to include last row value)
    for rindex in range(1,rowIndex + 1):
        new_row = [1]

        # Middle elements in new row
        for num in range (1, rindex ):
            new_row.append(row[num -1] + row[num])
        
        # Adding 1 to end of row
        new_row.append(1)

        # Update row to the new row
        row = new_row

    # Return the final row (at rowIndex)
    return row

if __name__ == "__main__":
    print(getRow(3))  # Output [1,3,3,1]
    print(getRow(0))  # Output [1]
    print(getRow(1))  # Output [1,1]