"""
Problem: Plus One
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/plus-one/

Approach:
- Iterate from the last digit to the first
- If digit < 9, add 1 and return immediately
- If digit is 9, set it to 0 and continue (carry over)
- If all digits were 9, prepend 1 to the array

Time Complexity: O(n)
Space Complexity: O(1)
"""

def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits


# Test cases
if __name__ == "__main__":
    print(plusOne([1,2,3]))   # Expected: [1,2,4]
    print(plusOne([4,3,2,1])) # Expected: [4,3,2,2]
    print(plusOne([9]))        # Expected: [1,0]
    print(plusOne([9,9,9]))    # Expected: [1,0,0,0]