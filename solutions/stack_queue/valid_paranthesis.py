"""
Problem: Valid Parentheses
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Approach:
- Use a stack to track opening brackets
- For every closing bracket, check if top of stack matches
- At the end, stack must be empty

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


# Test cases
if __name__ == "__main__":
    print(is_valid("()"))       # Expected: True
    print(is_valid("()[]{}"))   # Expected: True
    print(is_valid("(]"))       # Expected: False
    print(is_valid("([)]"))     # Expected: False
    print(is_valid("{[]}"))     # Expected: True