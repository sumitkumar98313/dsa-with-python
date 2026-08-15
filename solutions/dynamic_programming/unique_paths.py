"""
Problem: Unique Paths
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/unique-paths/

Approach:
- Space optimized 1D DP
- dp[j] represents unique paths to reach column j
- dp[j] = dp[j] (from above) + dp[j-1] (from left)

Time Complexity: O(m*n)
Space Complexity: O(n)
"""

def uniquePaths(m, n):
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]

    return dp[n - 1]


# Test cases
if __name__ == "__main__":
    print(uniquePaths(3, 7))  # Expected: 28
    print(uniquePaths(3, 2))  # Expected: 3
    print(uniquePaths(1, 1))  # Expected: 1