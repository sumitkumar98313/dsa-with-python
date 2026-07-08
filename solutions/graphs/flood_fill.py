"""
Problem: Flood Fill
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/flood-fill/

Approach:
- Store the original color of starting pixel
- If oldColor == new color, return immediately (avoid infinite loop)
- Use DFS to fill all connected pixels with same oldColor to new color

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

def floodFill(image, sr, sc, color):
    oldColor = image[sr][sc]
    if oldColor == color:
        return image

    rows = len(image)
    cols = len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != oldColor:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


# Test cases
if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    print(floodFill(image, 1, 1, 2))  # Expected: [[2,2,2],[2,2,0],[2,0,1]]