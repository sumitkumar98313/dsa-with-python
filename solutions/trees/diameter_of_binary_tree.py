"""
Problem: Diameter of Binary Tree
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/diameter-of-binary-tree/

Approach:
- Use DFS to calculate depth of each node
- At each node, diameter = left depth + right depth
- Track maximum diameter using self.diameter
- Return 1 + max(left, right) as depth to parent

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter


# Test cases
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(diameterOfBinaryTree(root))  # Expected: 3