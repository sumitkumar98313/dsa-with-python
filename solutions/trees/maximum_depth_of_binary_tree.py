"""
Problem: Maximum Depth of Binary Tree
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Approach:
- Use recursive DFS to find depth of left and right subtrees
- Return max of both depths + 1 at each node
Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right) + 1

# Test cases
if __name__ == "__main__":
    # Tree: [3,9,20,null,null,15,7] → Expected: 3
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(maxDepth(root))   # Expected: 3

    # Tree: [1,null,2] → Expected: 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print(maxDepth(root2))  # Expected: 2