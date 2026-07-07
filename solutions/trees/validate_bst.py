"""
Problem: Validate Binary Search Tree
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/validate-binary-search-tree/

Approach:
- Use recursion with valid range (low, high) for each node
- Node value must be strictly between low and high
- Go left: update high to node.val
- Go right: update low to node.val

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def check(node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return check(node.left, low, node.val) and check(node.right, node.val, high)

    return check(root, float('-inf'), float('inf'))


# Test cases
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(isValidBST(root))  # Expected: True