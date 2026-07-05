"""
Problem: Binary Tree Level Order Traversal
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Approach:
- Use BFS with a deque
- For each level, process all nodes currently in queue
- Collect values into level list, add children to queue
- Append level list to answer

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


# Test cases
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrder(root))  # Expected: [[3], [9, 20], [15, 7]]