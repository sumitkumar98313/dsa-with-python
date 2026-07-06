"""
Problem: Binary Tree Right Side View
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Approach:
- Use BFS level order traversal
- For each level, take the last node's value
- That's what you see from the right side

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    if not root:
        return []

    ans = []
    q = deque([root])

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == size - 1:
                ans.append(node.val)

    return ans


# Test cases
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(rightSideView(root))  # Expected: [1, 3, 4]