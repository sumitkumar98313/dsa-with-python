"""
Problem: Largest Rectangle in Histogram
Platform: LeetCode
Difficulty: Hard
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Approach:
- Use a Monotonic Stack storing indices
- Append 0 to heights to flush remaining bars at the end
- For each bar, while current height < stack top height, pop and calculate area
- Width = i - stack[-1] - 1 if stack exists, else width = i

Time Complexity: O(n)
Space Complexity: O(n)
"""

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


# Test cases
if __name__ == "__main__":
    print(largestRectangleArea([2,1,5,6,2,3]))  # Expected: 10
    print(largestRectangleArea([2,4]))           # Expected: 4