"""
Problem: Reverse Linked List
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/

Approach:
- Use three pointers: prev, curr, and nxt
- For every node, save the next node, reverse the current node's pointer to prev
- Move prev and curr one step forward
- Continue until curr becomes None, then prev is the new head

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


# Test cases
if __name__ == "__main__":
    # Build list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = reverseList(head)

    result = []
    while new_head:
        result.append(new_head.val)
        new_head = new_head.next
    print(result)  # Expected: [5, 4, 3, 2, 1]