"""
Problem: Number of Islands
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/

Approach:
- Use DFS flood fill
- For every unvisited land cell ("1"), increment count and DFS to mark all connected land as visited ("0")
- Count = total number of islands

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)

    return count


# Test cases
if __name__ == "__main__":
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid1))  # Expected: 1

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid2))  # Expected: 3