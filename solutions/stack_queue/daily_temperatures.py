"""
Problem: Daily Temperatures
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/daily-temperatures/

Approach:
- Use a Monotonic Stack storing indices
- For each temperature, pop all indices from stack where current temp is warmer
- The answer for each popped index = current index - popped index

Time Complexity: O(n)
Space Complexity: O(n)
"""

def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)

    return answer


# Test cases
if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # Expected: [1,1,4,2,1,1,0,0]
    print(dailyTemperatures([30,40,50,60]))               # Expected: [1,1,1,0]
    print(dailyTemperatures([30,60,90]))                  # Expected: [1,1,0]