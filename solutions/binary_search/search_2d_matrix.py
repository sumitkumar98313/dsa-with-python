"""
Problem: Search a 2D Matrix
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/search-a-2d-matrix/

Approach:
- Treat the 2D matrix as a flattened 1D sorted array
- Use binary search with row = mid // cols, col = mid % cols
- Standard binary search comparison on matrix[row][col]

Time Complexity: O(log(m*n))
Space Complexity: O(1)
"""

def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test cases
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(matrix, 3))   # Expected: True
    print(searchMatrix(matrix, 13))  # Expected: False