# Problem 66: Plus One
Difficulty: Easy
Category: Array
Approach: String Conversion 

# Goal
- Array given in interger example: 123 = [1,2,3]
- Most singificat in front (left) and least significatn in back (right)
- Does not contain any leading zeros ( no zeros at the begining of the number)
- Increment entire integer by 1
- Return
    - Return number in array

# Example
Example 1:

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].

Example 2:

    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: 
    The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].

Example 3:

    Input: digits = [9]
    Output: [1,0]
    Explanation: 
    The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].

# Approach
1. Convert the array of digits into a full number.
2. Add 1 to this number.
3. Convert the result back into an array of digits.
    - Each digit is stored in its own index.
4. Return the array of digits.
    - Example: 123 → [1, 2, 3]
