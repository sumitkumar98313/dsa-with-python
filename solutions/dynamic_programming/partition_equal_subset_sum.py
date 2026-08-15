"""
Problem: Partition Equal Subset Sum
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/partition-equal-subset-sum/

Approach:
- If total sum is odd, return False
- Find if any subset sums to total // 2
- 0/1 knapsack with reverse iteration to avoid reusing elements

Time Complexity: O(n * target)
Space Complexity: O(target)
"""

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


# Test cases
if __name__ == "__main__":
    print(canPartition([1,5,11,5]))  # Expected: True
    print(canPartition([1,2,3,5]))   # Expected: False