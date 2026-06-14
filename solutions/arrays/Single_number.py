"""
Problem: Single Number
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/

Approach:
- Use XOR bit manipulation
- XOR of a number with itself = 0
- XOR of a number with 0 = the number itself
- All duplicates cancel out, leaving only the single number

Time Complexity: O(n)
Space Complexity: O(1)
"""

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# Test cases
if __name__ == "__main__":
    print(singleNumber([2,2,1]))        # Expected: 1
    print(singleNumber([4,1,2,1,2]))    # Expected: 4
    print(singleNumber([1]))            # Expected: 1