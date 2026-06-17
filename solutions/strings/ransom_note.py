"""
Problem: Ransom Note
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/ransom-note/

Approach:
- Count frequency of each character in magazine
- For every character in ransomNote, check if it's available in magazine
- Decrement count after using a character

Time Complexity: O(n+m)
Space Complexity: O(1) - at most 26 lowercase letters
"""

def canConstruct(ransomNote, magazine):
    count = {}

    for ch in magazine:
        count[ch] = count.get(ch, 0) + 1

    for ch in ransomNote:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True


# Test cases
if __name__ == "__main__":
    print(canConstruct("a", "b"))        # Expected: False
    print(canConstruct("aa", "ab"))      # Expected: False
    print(canConstruct("aa", "aab"))     # Expected: True