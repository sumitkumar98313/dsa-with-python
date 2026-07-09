"""
Problem: Clone Graph
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Approach:
- Use DFS with a visited hashmap
- For each node, create a clone and store in visited
- Recursively clone all neighbors and append to clone's neighbors

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None

    visited = {}

    def dfs(curr):
        if curr in visited:
            return visited[curr]
        copy = Node(curr.val)
        visited[curr] = copy
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)


# Test cases
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    cloned = cloneGraph(node1)
    print(cloned.val)  # Expected: 1