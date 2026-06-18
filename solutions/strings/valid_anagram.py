"""
Problem: Valid Anagram
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Approach:
- If lengths differ, they can't be anagrams
- Count frequency of each character in s
- Decrement count while iterating t
- If any character is missing or count goes negative, return False

Time Complexity: O(n)
Space Complexity: O(1) - at most 26 lowercase letters
"""

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True


# Test cases
if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  # Expected: True
    print(isAnagram("rat", "car"))          # Expected: False