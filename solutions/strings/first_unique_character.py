"""
Problem: First Unique Character in a String
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/first-unique-character-in-a-string/

Approach:
- Count frequency of each character using a dictionary
- Loop through the string again and return index of first character with frequency 1

Time Complexity: O(n)
Space Complexity: O(1) - at most 26 lowercase letters
"""

def firstUniqChar(s):
    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i

    return -1


# Test cases
if __name__ == "__main__":
    print(firstUniqChar("leetcode"))    # Expected: 0
    print(firstUniqChar("loveleetcode")) # Expected: 2
    print(firstUniqChar("aabb"))         # Expected: -1