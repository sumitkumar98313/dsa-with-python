"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Approach:
- Use a hashmap to store each number and its index
- For each number, check if (target - number) already exists in the map

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Test cases
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # Expected: [0, 1]
    print(two_sum([3, 2, 4], 6))         # Expected: [1, 2]
    print(two_sum([3, 3], 6))            # Expected: [0, 1]