"""
Problem: Rotting Oranges
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/rotting-oranges/

Approach:
- Multi-source BFS starting from all rotten oranges simultaneously
- Count fresh oranges upfront
- Each BFS level = 1 minute
- Return -1 if fresh oranges remain

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

from collections import deque

def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue and fresh > 0:
        size = len(queue)
        for i in range(size):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc))
        minutes += 1

    if fresh > 0:
        return -1
    return minutes


# Test cases
if __name__ == "__main__":
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Expected: 4
    print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # Expected: -1
    print(orangesRotting([[0,2]]))                     # Expected: 0