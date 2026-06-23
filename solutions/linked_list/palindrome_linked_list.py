"""
Problem: Palindrome Linked List
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-linked-list/

Approach:
- Collect all values into an array
- Compare array with its reverse using [::-1]

Time Complexity: O(n)
Space Complexity: O(n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr == arr[::-1]


# Test cases
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(isPalindrome(head))  # Expected: True

    head2 = ListNode(1, ListNode(2))
    print(isPalindrome(head2))  # Expected: False