"""
Problem: Balanced Binary Tree
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/balanced-binary-tree/

Approach:
- Use DFS to calculate height of each node
- If height difference > 1 at any node, return -1 as signal
- Propagate -1 upward to short circuit
- Final check: dfs(root) != -1

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        if left == -1:
            return -1
        right = dfs(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return dfs(root) != -1


# Test cases
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(isBalanced(root))  # Expected: True