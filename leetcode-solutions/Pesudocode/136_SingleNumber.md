# Problem 136: Single Number
Difficulty: Easy
Category: Array 
Approach: XOR Bit Manipulation

# Goal
- Given non empty array
- Find non repeating Number
    - there is only one single number in the array
    - The numbers can only appears twice at most
- Needs to be:
    - Linear run time complexity O(N)
    - Only constant extra space  O(1)

# Example
Example 1:

    Input: nums = [2,2,1]
    Output: 1

Example 2:

    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:

    Input: nums = [1]
    Output: 1

# Approach
1. set variable for result
2. XOR each number in List
3. return result 
    - result will contain single number because of xor properties
    
# XOR Bit Manipulation

## XOR Truth Table

| A | B | A ⊕ B |
|---|---|--------|
| 0 | 0 |    0   |
| 0 | 1 |    1   |
| 1 | 0 |    1   |
| 1 | 1 |    0   |

## Key Properties
- XOR the order does not matter (commutative)
- Same values cancel out from the xor truth table above
    - A ^ A = 0 (same value cancel out)
    - A ^ 0 = A ( return same number back)
- Binary values 0's and 1's

## Dry Run logic
Input : [1,4,1,2,2]
1. result = 0
2. 0 ^ 1 = 1 -> result = 1 (00 xor 01) -> 1
3. 1 ^ 4 = 5 -> result = 5 (01 xor 100) -> 101 = 5 
4. 5 ^ 1 = 4 -> result = 4 (101 xor 01) -> 100 = 4 (see the 1's cancel each other out)
5. 4 ^ 2 = 8 -> result = 8 (100 xor 10) -> 110 = 8
6. 8 ^ 2 = 4 -> result = 4 (110 xor 10) -> 100 = 4 ( 2's cancel each other)
7. End of array, return result = 4
8. 4 is the single number in array, which is correct