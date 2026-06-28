"""
Problem: First Bad Version
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/first-bad-version/

Approach:
- Binary search with left < right condition
- If mid is bad, search left half (right = mid)
- If mid is good, search right half (left = mid + 1)
- When left == right, that's the first bad version

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


# Test cases
if __name__ == "__main__":
    # Mock isBadVersion for local testing
    bad = 4
    def isBadVersion(version):
        return version >= bad

    print(firstBadVersion(5))  # Expected: 4
    print(firstBadVersion(1))  # Expected: 1