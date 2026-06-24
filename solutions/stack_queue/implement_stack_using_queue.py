"""
Problem: Implement Stack using Queues
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/implement-stack-using-queues/

Approach:
- Use a single deque
- After every push, rotate all previous elements to the back
- This makes the newest element always at the front (LIFO behavior)

Time Complexity: O(n) for push, O(1) for others
Space Complexity: O(n)
"""

from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Test cases
if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.top())    # Expected: 2
    print(s.pop())    # Expected: 2
    print(s.empty())  # Expected: False