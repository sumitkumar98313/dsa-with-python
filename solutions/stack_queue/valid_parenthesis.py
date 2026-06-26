"""
Problem: Valid Parentheses
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/
Approach:
- Use a stack to track opening brackets
- For each closing bracket, check if it matches the top of the stack
Time Complexity: O(n)
Space Complexity: O(n)
"""
def isValid(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0

# Test cases
if __name__ == "__main__":
    print(isValid("()"))        # Expected: True
    print(isValid("()[]{}"))    # Expected: True
    print(isValid("(]"))        # Expected: False
    print(isValid("([)]"))      # Expected: False
    print(isValid("{[]}"))      # Expected: True