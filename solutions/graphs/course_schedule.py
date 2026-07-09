"""
Problem: Course Schedule
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/

Approach:
- Build adjacency list graph
- Use DFS cycle detection with two sets: visited and path
- If course is in path (current DFS path), cycle detected -> return False
- If course already fully visited, return True

Time Complexity: O(V+E)
Space Complexity: O(V+E)
"""

def canFinish(numCourses, prerequisites):
    graph = {}
    for i in range(numCourses):
        graph[i] = []

    for course, pre in prerequisites:
        graph[course].append(pre)

    visited = set()
    path = set()

    def dfs(course):
        if course in path:
            return False
        if course in visited:
            return True

        path.add(course)
        for pre in graph[course]:
            if not dfs(pre):
                return False
        path.remove(course)
        visited.add(course)
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


# Test cases
if __name__ == "__main__":
    print(canFinish(2, [[1,0]]))        # Expected: True
    print(canFinish(2, [[1,0],[0,1]]))  # Expected: False