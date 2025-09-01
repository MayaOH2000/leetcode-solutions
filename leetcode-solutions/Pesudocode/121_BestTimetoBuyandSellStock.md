# Problem 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Category: Array (Dynamic Programming (DP) -> leetcode tag)
Approach: Two Pointer + Greedy Algorithm (local optimize)

# Goal
- given array of of stock prices (each index represents 1 day)
- Find maximum profit
    - Buy on a day (choose the lowest price **so far**)
    - Sell on a later day (must come after buy)
- Need to have stock before you can sell
- If no profit then return 0

# Example
Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5

    Explanation: 
    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0

    Explanation: 
    In this case, no transactions are done and the max profit = 0.

# Approach
1. Initialize:
    - `max_profit = 0`
    - `p1 = 0`  # buy day (current lowest price)
    - `p2 = 1`  # sell day (price after buy day)
2. Iterate through prices with two pointers:
    - While `p2` is within array bounds:
        - If `prices[p1] < prices[p2]`:
            - Calculate profit: `profit = prices[p2] - prices[p1]`
            - Update `max_profit` if `profit > max_profit`
            - Move `p2` to next day
        - Else (`prices[p1] >= prices[p2]`):
            - Update `p1 = p2`  # new potential buy day
            - Move `p2` to next day
3. Repeat until `p2` reaches the end of the array.
4. Return `max_profit`
    - Default is `0` if no profitable transaction exists.