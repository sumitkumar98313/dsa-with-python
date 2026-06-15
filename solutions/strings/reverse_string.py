"""
Problem: Reverse String
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string/
Approach:
- Use two-pointer technique to swap characters from both ends
- Move left pointer forward and right pointer backward until they meet
Time Complexity: O(n)
Space Complexity: O(1)
"""
def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# Test cases
if __name__ == "__main__":
    print(reverseString(["h","e","l","l","o"]))      # Expected: ['o','l','l','e','h']
    print(reverseString(["H","a","n","n","a","h"]))  # Expected: ['h','a','n','n','a','H']