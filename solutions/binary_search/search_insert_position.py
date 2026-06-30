"""
Problem: Search Insert Position
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/search-insert-position/

Approach:
- Standard binary search
- If target is found, return mid
- If not found, left ends up at the correct insertion index

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def searchInsert(nums, target):
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

    return left


# Test cases
if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 5))  # Expected: 2
    print(searchInsert([1,3,5,6], 2))  # Expected: 1
    print(searchInsert([1,3,5,6], 7))  # Expected: 4