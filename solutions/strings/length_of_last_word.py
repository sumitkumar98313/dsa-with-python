"""
Problem: Length of Last Word
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/length-of-last-word/

Approach:
- Strip leading/trailing spaces and split the string by whitespace
- Return the length of the last word in the resulting list

Time Complexity: O(n)
Space Complexity: O(n)
"""

def lengthOfLastWord(s):
    words = s.strip().split()
    return len(words[-1])


# Test cases
if __name__ == "__main__":
    print(lengthOfLastWord("Hello World"))        # Expected: 5
    print(lengthOfLastWord("   fly me   to   the moon  "))  # Expected: 4
    print(lengthOfLastWord("luffy is still joyboy"))  # Expected: 6