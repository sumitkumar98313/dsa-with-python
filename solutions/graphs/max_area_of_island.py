"""
Problem: Max Area of Island
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/max-area-of-island/

Approach:
- DFS flood fill on every unvisited land cell (1)
- Mark visited cells as 0 to avoid revisiting
- Track area at each DFS call and update max

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        area = 1
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area

    max_area = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                current_area = dfs(i, j)
                max_area = max(max_area, current_area)
    return max_area


# Test cases
if __name__ == "__main__":
    print(maxAreaOfIsland([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]))  # Expected: 6

    print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))  # Expected: 0