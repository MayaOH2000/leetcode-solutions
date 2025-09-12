# Problem 350 : Intersection of Two Arrays II
Difficulty: Easy
Category: Array
Approach: Counter Intersection (to keep duplicates)

# Goal
- Given two arrays of integers:
    - Find the common elements between the two arrays (intersection)
    - Include duplicate occurrences if they exist
    - Result can be returned in any order

# Example
Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.

# Approach
1. Use `Counter` to count occurrences of each element in both arrays.
2. Use Counter intersection (`&`) to get common elements with their minimum counts.
3. Convert the resulting Counter to a list using `.elements()` and return it.

# Why it works
- The Counter intersection keeps the **minimum count** for each common element.
- `.elements()` expands the Counter back into a list including duplicates.
