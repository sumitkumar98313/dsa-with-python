"""
Problem: Binary Search
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/binary-search/

Approach:
- Use two pointers left and right
- Calculate mid, compare with target
- If match return mid, if target > mid move left up, else move right down

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test cases
if __name__ == "__main__":
    print(search([-1,0,3,5,9,12], 9))   # Expected: 4
    print(search([-1,0,3,5,9,12], 2))   # Expected: -1