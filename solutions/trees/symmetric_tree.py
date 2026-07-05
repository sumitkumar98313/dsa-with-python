"""
Problem: Symmetric Tree
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/symmetric-tree/

Approach:
- Use a helper isMirror function
- A tree is symmetric if left subtree is mirror of right subtree
- Recursively check left.left with right.right and left.right with right.left

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return (isMirror(left.left, right.right) and
                isMirror(left.right, right.left))
    return isMirror(root.left, root.right)


# Test cases
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(isSymmetric(root))  # Expected: True