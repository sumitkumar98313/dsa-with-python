"""
Problem: Find the Index of the First Occurrence in a String
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Approach:
- Slide a window of size len(needle) across haystack
- Compare each window with needle
- Return the starting index on match, otherwise -1

Time Complexity: O(n*m)
Space Complexity: O(1)
"""

def strStr(haystack, needle):
    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1


# Test cases
if __name__ == "__main__":
    print(strStr("sadbutsad", "sad"))    # Expected: 0
    print(strStr("leetcode", "leeto"))   # Expected: -1