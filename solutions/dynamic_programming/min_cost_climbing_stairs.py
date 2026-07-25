"""
Problem: Min Cost Climbing Stairs
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/min-cost-climbing-stairs/

Approach:
- dp[i] = cost[i] + min(dp[i-1], dp[i-2])
- Answer is min(dp[n-1], dp[n-2])

Time Complexity: O(n)
Space Complexity: O(n)
"""

def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 2:
        return min(cost[0], cost[1])

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[n - 1], dp[n - 2])


# Test cases
if __name__ == "__main__":
    print(minCostClimbingStairs([10,15,20]))       # Expected: 15
    print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # Expected: 6