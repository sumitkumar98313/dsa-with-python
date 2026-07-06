"""
Problem: Lowest Common Ancestor of a Binary Tree
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Approach:
- If root is None, p, or q — return root
- Recursively search left and right subtrees
- If both sides return non-null, current node is the LCA
- If only one side returns non-null, that side contains the LCA

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    if left:
        return left
    return right


# Test cases
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    p = root.left        # node 5
    q = root.right       # node 1
    result = lowestCommonAncestor(root, p, q)
    print(result.val)    # Expected: 3