"""
Problem: Find Minimum in Rotated Sorted Array
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Approach:
- Use binary search with left < right
- If nums[mid] > nums[right], minimum is in right half
- Otherwise minimum is in left half (including mid)
- When left == right, that's the minimum

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# Test cases
if __name__ == "__main__":
    print(findMin([3,4,5,1,2]))      # Expected: 1
    print(findMin([4,5,6,7,0,1,2]))  # Expected: 0
    print(findMin([11,13,15,17]))    # Expected: 11