# Problem 1: Two Sum
Difficulty: Easy
Category: Array

## Goal
- Find two numbers in the array that add up to the target value.
- Only one valid solution exists per array.
- Cannot reuse the same index twice.
- Return the indices of the two numbers.

## Logic
1. Start with an empty list (or structure) that will keep track of numbers we have already seen, along with their index.
2. Go through the array one number at a time.
   - For each number, calculate the missing number needed to reach the target: `missing = target - current`
   - Check if the missing number is already in the list of seen numbers:
     - If yes → return the index of the missing number and the current index.
     - If no → add the current number and its index to the list of seen numbers.
3. Continue until the solution is found.