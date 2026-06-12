"""
Problem: Move Zeroes
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/move-zeroes/

Approach:
- Use an index pointer to track position for next non-zero element
- First pass: move all non-zero elements to the front
- Second pass: fill remaining positions with 0

Time Complexity: O(n)
Space Complexity: O(1)
"""

def moveZeroes(nums):
    index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1

    while index < len(nums):
        nums[index] = 0
        index += 1


# Test cases
if __name__ == "__main__":
    nums1 = [0,1,0,3,12]
    moveZeroes(nums1)
    print(nums1)  # Expected: [1,3,12,0,0]

    nums2 = [0]
    moveZeroes(nums2)
    print(nums2)  # Expected: [0]