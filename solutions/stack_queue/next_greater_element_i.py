"""
Problem: Next Greater Element I
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/next-greater-element-i/
Approach:
- Use a monotonic stack to find next greater element for each number in nums2
- Store results in a hashmap, then look up each number from nums1
Time Complexity: O(n + m)
Space Complexity: O(n)
"""
def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)

    while stack:
        next_greater[stack.pop()] = -1

    answer = []
    for num in nums1:
        answer.append(next_greater[num])

    return answer

# Test cases
if __name__ == "__main__":
    print(nextGreaterElement([4,1,2], [1,3,4,2]))  # Expected: [-1,3,-1]
    print(nextGreaterElement([2,4], [1,2,3,4]))    # Expected: [3,-1]