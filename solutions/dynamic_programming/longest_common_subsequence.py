"""
Problem: Longest Common Subsequence
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/longest-common-subsequence/

Approach:
- 2D DP table of size (m+1) x (n+1)
- If characters match: dp[i][j] = dp[i-1][j-1] + 1
- Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- Answer is dp[m][n]

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Test cases
if __name__ == "__main__":
    print(longestCommonSubsequence("abcde", "ace"))   # Expected: 3
    print(longestCommonSubsequence("abc", "abc"))      # Expected: 3
    print(longestCommonSubsequence("abc", "def"))      # Expected: 0