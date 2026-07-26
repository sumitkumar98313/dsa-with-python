"""
Problem: Longest Increasing Subsequence
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Approach:
- dp[i] = length of LIS ending at index i
- For each i, check all j < i, if nums[j] < nums[i], update dp[i]
- Answer is max(dp)

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Test cases
if __name__ == "__main__":
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))  # Expected: 4
    print(lengthOfLIS([0,1,0,3,2,3]))           # Expected: 4
    print(lengthOfLIS([7,7,7,7,7]))             # Expected: 1