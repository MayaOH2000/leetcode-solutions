# Problem 169: Majority Element
Difficulty: Easy
Category: Array, Hash Maps 
Approach: Hash map (dictionary)

# Goal
- Given an array of intergers
- Find majority element
    - There always exist a majority Element
    - Majority element appears more times then -> n/2 , where n is length of array
- Optional:
    - Linear time
    - O(1) Space

# Example
Example 1:

    Input: nums = [3,2,3]
    Output: 3

Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

# Approach
1. Calculate the minimum count needed for majority (n/2)
2. Create an empty dictionary to store number counts
3. Loop through the array:
    - If number seen:
        - Add 1 to its count
    - If number not seen:
        - Add number with count = 1
4. At end of array:
    - Return the number with count higher than n/2
