"""
Problem: Evaluate Reverse Polish Notation
Platform: LeetCode
Difficulty: Medium
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Approach:
- Use a stack
- Push numbers onto the stack
- When an operator is found, pop two numbers, apply operator, push result
- Final answer is the last element in the stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token not in ("+", "-", "*", "/"):
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # Truncate toward zero

    return stack.pop()


# Test cases
if __name__ == "__main__":
    print(evalRPN(["2","1","+","3","*"]))          # Expected: 9
    print(evalRPN(["4","13","5","/","+"]))          # Expected: 6
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Expected: 22