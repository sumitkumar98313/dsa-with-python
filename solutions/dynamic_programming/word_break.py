"""
Problem: Word Break
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/word-break/

Approach:
- Use dp[i] to check if the string up to index i can be formed.
- Start with dp[0] = True because an empty string can be formed.
- For every position, check whether the substring is present in wordDict.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def wordBreak(s, wordDict):
    n = len(s)
    words = set(wordDict)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]


# Test cases
if __name__ == "__main__":
    print(wordBreak("leetcode", ["leet", "code"]))  # Expected: True
    print(wordBreak("applepenapple", ["apple", "pen"]))  # Expected: True
    print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Expected: False