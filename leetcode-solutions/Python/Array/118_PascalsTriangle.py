# ID: 118
# Problem: Pascal's Triangle
# Difficulty: Easy
# Link: https://leetcode.com/problems/pascals-triangle/
# Approach: Build row by row using previous row (DP)

from typing import List, Optional


def generate(numRows: int) -> List[List[int]]:




if __name__ == "__main__":
    print(generate(5))  # Output [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    # print(generate(1))  # Output [[1]]