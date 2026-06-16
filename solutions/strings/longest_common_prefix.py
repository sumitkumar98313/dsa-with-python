"""
Problem: Longest Common Prefix
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix/

Approach:
- Start with the first string as the prefix
- For every other string, shrink the prefix until it matches the start of that word
- If prefix becomes empty, return immediately

Time Complexity: O(n*m) where n = number of strings, m = length of shortest string
Space Complexity: O(1)
"""

def longestCommonPrefix(strs):
    prefix = strs[0]

    for word in strs[1:]:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


# Test cases
if __name__ == "__main__":
    print(longestCommonPrefix(["flower","flow","flight"]))  # Expected: "fl"
    print(longestCommonPrefix(["dog","racecar","car"]))      # Expected: ""