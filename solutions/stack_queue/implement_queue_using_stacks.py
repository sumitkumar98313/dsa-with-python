"""
Problem: Implement Queue using Stacks
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/implement-queue-using-stacks/

Approach:
- Use two stacks (stack1 for push, stack2 for pop/peek)
- When stack2 is empty, transfer all elements from stack1 to stack2
- This reverses the order, making the oldest element accessible first

Time Complexity: O(1) amortized
Space Complexity: O(n)
"""

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Test cases
if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # Expected: 1
    print(q.pop())    # Expected: 1
    print(q.empty())  # Expected: False