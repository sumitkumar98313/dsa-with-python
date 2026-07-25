"""
Problem: Coin Change
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change/

Approach:
- Bottom-up DP
- dp[i] = minimum coins needed to make amount i
- For each amount, try all coins and take minimum
- Return -1 if dp[amount] is still infinity

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Test cases
if __name__ == "__main__":
    print(coinChange([1,2,5], 11))   # Expected: 3
    print(coinChange([2], 3))         # Expected: -1
    print(coinChange([1], 0))         # Expected: 0