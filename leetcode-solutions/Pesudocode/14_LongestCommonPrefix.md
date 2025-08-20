# Problem 14: Longest Common Prefix
Difficulty: Easy
Category: Array

## Goal
- Find longest prefix in array
- If no common prefix return empty string
- Only has lower case letters (characters)

## Examples
Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""

## Logic
1. Store the first word in the list as the starting prefix.  
2. Go through the remaining words in the list:  
   - Compare the current word with the prefix.  
   - While the current word does not start with the prefix:  
     - Remove the last character from the prefix.  
     - If the prefix becomes empty → return "".  
3. Continue until all words are checked.  
4. Return the prefix that remains after the comparisons.  
   - If empty → no prefix was found, return "".  
   - If characters remain → return them as the longest common prefix.  