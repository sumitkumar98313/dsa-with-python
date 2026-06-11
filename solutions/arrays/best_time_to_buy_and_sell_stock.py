"""
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
- Track minimum price seen so far
- At every price, check if selling today gives better profit

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# Test cases
if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))  # Expected: 5
    print(maxProfit([7,6,4,3,1]))    # Expected: 0