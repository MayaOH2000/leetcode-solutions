# ID: 121
# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Approch: Two Pointer + Greedy Algorithm (local optimize)

from typing import List

def maxProfit(prices: List[int]) -> int:
    # Initlizing values
    max_profit = 0
    p1 = 0  # Buy Day
    p2 = 1  # Sell Day

    # Comparing prices
    while p2 in range(len(prices)):
        if prices[p1] < prices[p2]:
            # Calculate profit
            profit = prices[p2] - prices[p1]

            # Update profit
            if max_profit < profit:
                max_profit = profit
            
            # Move pointer
            p2 += 1 
            
        elif prices[p1] >= prices[p2]:
            p1 = p2
            p2 += 1
    return max_profit

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4])) # Output 5 (6-1)
    print(maxProfit([7,6,4,3,1]))   # Output 0
    print(maxProfit([2, 4, 1])) # Ouput 2 (4-2)