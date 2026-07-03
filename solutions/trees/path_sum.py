"""
Problem: Path Sum
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/path-sum/

Approach:
- Use recursion
- At each node subtract its value from targetSum
- At leaf node check if remaining targetSum equals 0

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return targetSum == root.val

    targetSum -= root.val

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)


# Test cases
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    print(hasPathSum(root, 22))  # Expected: True