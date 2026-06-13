"""
Problem: Merge Sorted Array
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/merge-sorted-array/

Approach:
- Start from the end of both arrays
- Compare and place the larger element at the end of nums1
- Handle remaining elements of nums2 if any

Time Complexity: O(m+n)
Space Complexity: O(1)
"""

def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# Test cases
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    merge(nums1, 3, [2,5,6], 3)
    print(nums1)  # Expected: [1,2,2,3,5,6]