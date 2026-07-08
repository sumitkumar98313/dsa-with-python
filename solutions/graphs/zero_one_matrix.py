"""
Problem: 01 Matrix
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/01-matrix/

Approach:
- Multi-source BFS starting from all 0 cells simultaneously
- Initialize answer matrix with 0 for zeros and -1 for ones
- For each unvisited cell, distance = neighbor distance + 1

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

from collections import deque

def updateMatrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    answer = [[-1] * cols for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                answer[r][c] = 0
                queue.append((r, c))

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            newRow = row + dr
            newCol = col + dc
            if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols:
                if answer[newRow][newCol] == -1:
                    answer[newRow][newCol] = answer[row][col] + 1
                    queue.append((newRow, newCol))

    return answer


# Test cases
if __name__ == "__main__":
    print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))  # Expected: [[0,0,0],[0,1,0],[0,0,0]]
    print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))  # Expected: [[0,0,0],[0,1,0],[1,2,1]]