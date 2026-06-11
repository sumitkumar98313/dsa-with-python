"""
Problem: Contains Duplicate
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Approach:
- Use a set to track numbers seen so far
- If current number already in set, return True
- If loop ends without match, return False

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Test cases
if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1]))   # Expected: True
    print(containsDuplicate([1,2,3,4]))   # Expected: False
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Expected: True