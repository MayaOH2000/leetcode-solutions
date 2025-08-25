# ID: 66
# Problem: Plus One
# Difficulty: Easy
# Link: https://leetcode.com/problems/plus-one/
# Approach: String Conversion Method 

from typing import List

def plusOne(digits: List[int]) -> List[int]:
  # Helper reference:
    # map(func, iterable) -> apply func to each element
    # 'sep'.join(iterable) -> join strings with separator
    
    # Convert digit array to integer: [1,2,3] -> 123
    number = int("".join(map(str, digits)))
    
    # Add one: 123 -> 124
    number += 1
    
    # Convert back to digit array: 124 -> [1,2,4]
    return list(map(int, str(number)))


if __name__ == "__main__":
    print(plusOne([1,2,3]))   # Output [1,2,4]
    print(plusOne([4,3,2,1]))  # Output [4,3,2,2]
    print(plusOne([1,1,1,9]))  # Output [1,1,2,0]