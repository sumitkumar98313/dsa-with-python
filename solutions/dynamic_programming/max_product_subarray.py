"""
Problem: Maximum Product Subarray
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-product-subarray/

Approach:
- Keep track of the maximum and minimum product ending at the current position.
- If the current number is negative, swap the maximum and minimum.
- Update the answer after checking every element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProduct(nums):
    max_product = nums[0]
    min_product = nums[0]
    answer = nums[0]

    for i in range(1, len(nums)):

        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        answer = max(answer, max_product)

    return answer


# Test cases
if __name__ == "__main__":
    print(maxProduct([2, 3, -2, 4]))  # Expected: 6
    print(maxProduct([-2, 0, -1]))    # Expected: 0
    print(maxProduct([-2, 3, -4]))    # Expected: 24