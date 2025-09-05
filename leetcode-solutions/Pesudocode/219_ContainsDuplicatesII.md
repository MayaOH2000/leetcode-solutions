# Problem 219: Contains Duplicate II
Difficulty: Easy  
Category: Array, Hasmap
Approach: Hasmap (dictionary)

# Goal
- Given a list of intergers and target number (k)
    - Find Duplicate(s) in array that the distance is less then or equal to k
        - Index value of duplicates need to be abs(j - i <= k)
            - i = first index of number occurance
            - j = second index of number occurance


# Example
Example 1:

    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:

    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

# Approach
1. Create empty dictionary 
2. Loop through array with index i:
    - If value exists in dictionary:
        - Get previous index
          - If (current_index - previous_index) <= k:
                - Return True
    - Always update dictionary with current value and index
    - Move to next index
3. If loop completes without finding solution:
   - Return False

# Why Hasmap?
- Can store the number and the index where I saw it last.
- Super quick to check if I’ve seen a number before.
- Can easily compare the old index with the current one to see if they’re close enough. 