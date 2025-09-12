# Problem 349 : Intersection of Two Arrays
Difficulty: Easy
Category: Array
Approach: AND operator with sets

# Goal
- Given two arrays of integers:
    - Find the common numbers between the two arrays (intersection)
    - Result must be unique 
    - Can be return in any order

# Example
Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.

# Approach
1. Convert the lists into sets.
2. Perform set intersection operation using `&`.
3. Return the result as a list.

# Why it works?
- The set intersection (`&`) returns only the elements that appear in both sets.
- Converting the lists to sets allows us to use this intersection operation easily and ensures uniqueness.
