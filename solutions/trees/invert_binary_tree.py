"""
Problem: Invert Binary Tree
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/invert-binary-tree/
Approach:
- Use recursion to swap left and right children at each node
- Recursively invert left and right subtrees
Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root

# Test cases
if __name__ == "__main__":
    # Tree: [4,2,7,1,3,6,9] → Expected: [4,7,2,9,6,3,1]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    invertTree(root)
    print(root.val, root.left.val, root.right.val)  # Expected: 4 7 2

    # Tree: [2,1,3] → Expected: [2,3,1]
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    invertTree(root2)
    print(root2.val, root2.left.val, root2.right.val)  # Expected: 2 3 1