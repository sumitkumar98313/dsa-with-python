"""
Problem: Maximum Subarray
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Approach:
- Kadane's Algorithm
- current_sum = max of current number alone or extending previous subarray
- max_sum = track the best result seen so far

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test cases
if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
    print(maxSubArray([1]))                        # Expected: 1
    print(maxSubArray([5,4,-1,7,8]))               # Expected: 23