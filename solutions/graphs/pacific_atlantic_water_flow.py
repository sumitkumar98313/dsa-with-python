"""
Problem: Pacific Atlantic Water Flow
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Approach:
- Reverse DFS from ocean borders instead of from each cell
- Run DFS from all Pacific border cells (top row + left column)
- Run DFS from all Atlantic border cells (bottom row + right column)
- Cells reachable by both = answer

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

def pacificAtlantic(heights):
    if not heights:
        return []

    rows = len(heights)
    cols = len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited):
        visited.add((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if (0 <= nr < rows and
                0 <= nc < cols and
                (nr, nc) not in visited and
                heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, visited)

    for c in range(cols):
        dfs(0, c, pacific)
    for r in range(rows):
        dfs(r, 0, pacific)

    for c in range(cols):
        dfs(rows - 1, c, atlantic)
    for r in range(rows):
        dfs(r, cols - 1, atlantic)

    ans = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                ans.append([r, c])
    return ans


# Test cases
if __name__ == "__main__":
    print(pacificAtlantic([
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]))  # Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    print(pacificAtlantic([[1]]))  # Expected: [[0,0]]