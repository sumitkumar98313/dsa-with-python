"""
Problem: House Robber
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

Approach:
- Dynamic programming with two variables (no array needed)
- At each house, choose max of skipping current or robbing current + prev2
- Track prev1 and prev2 as rolling variables

Time Complexity: O(n)
Space Complexity: O(1)
"""

def rob(nums):
    if len(nums) == 1:
        return nums[0]

    prev2 = 0
    prev1 = 0

    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current

    return prev1


# Test cases
if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))     # Expected: 4
    print(rob([2, 7, 9, 3, 1]))  # Expected: 12
    print(rob([5]))               # Expected: 5