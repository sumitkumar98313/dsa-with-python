"""
Problem: Search in Rotated Sorted Array
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Approach:
- Use binary search
- Determine which half is sorted
- If left half is sorted and target is in range, go left
- If right half is sorted and target is in range, go right

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

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Test cases
if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))   # Expected: 4
    print(search([4,5,6,7,0,1,2], 3))   # Expected: -1
    print(search([1], 0))                # Expected: -1