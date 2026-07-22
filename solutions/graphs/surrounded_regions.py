"""
Problem: Surrounded Regions
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/surrounded-regions/

Approach:
- DFS from all border O cells, mark them as # (safe)
- Flip all remaining O to X (captured)
- Restore # back to O

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

def solve(board):
    if not board or not board[0]:
        return

    rows = len(board)
    cols = len(board[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if board[r][c] != "O":
            return
        board[r][c] = "#"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        if board[i][0] == "O":
            dfs(i, 0)
        if board[i][cols - 1] == "O":
            dfs(i, cols - 1)

    for j in range(cols):
        if board[0][j] == "O":
            dfs(0, j)
        if board[rows - 1][j] == "O":
            dfs(rows - 1, j)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "#":
                board[i][j] = "O"


# Test cases
if __name__ == "__main__":
    board = [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]]
    solve(board)
    print(board)  # Expected: all O's captured except border ones