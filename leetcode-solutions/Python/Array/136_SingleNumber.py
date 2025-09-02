# ID: 136
# Problem: Single Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/single-number/
# Approch: XOR Bit Manipulation

from typing import List

def singleNumber(nums: List[int]) -> int:
    result = 0

    # Duplicates cancel out via XOR, single number remains
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    print(singleNumber([2,2,1]))    # Output 1
    print(singleNumber([4,1,2,1,2]))    # Ouput 4
    print(singleNumber([1])) # Output 1
    print(singleNumber([1,0,1,2,3,2,3,4,4])) # Ouput 0