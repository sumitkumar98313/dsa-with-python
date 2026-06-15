"""
Problem: Valid Palindrome
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/

Approach:
- Filter only alphanumeric characters and convert to lowercase
- Compare the cleaned string with its reverse using [::-1]

Time Complexity: O(n)
Space Complexity: O(n)
"""

def isPalindrome(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]


# Test cases
if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(isPalindrome("race a car"))                       # Expected: False
    print(isPalindrome(" "))                                # Expected: True