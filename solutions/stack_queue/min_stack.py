"""
Problem: Min Stack
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/min-stack/

Approach:
- Use two stacks: one normal stack and one min_stack
- min_stack always tracks the current minimum at every level
- On push, append min(val, current_min) to min_stack
- On pop, pop from both stacks

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Test cases
if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())  # Expected: -3
    s.pop()
    print(s.top())     # Expected: 0
    print(s.getMin())  # Expected: -2