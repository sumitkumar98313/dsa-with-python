"""
Problem: Subtree of Another Tree
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/subtree-of-another-tree/

Approach:
- Use a helper isSameTree function
- For every node in root, check if the subtree rooted there is same as subRoot
- Recursively check left and right subtrees

Time Complexity: O(m*n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSubtree(root, subRoot):
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# Test cases
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    print(isSubtree(root, subRoot))  # Expected: True