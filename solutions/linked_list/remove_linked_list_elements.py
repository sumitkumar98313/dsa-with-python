"""
Problem: Remove Linked List Elements
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/remove-linked-list-elements/

Approach:
- Use a dummy node to handle edge cases where head itself needs to be removed
- Traverse the list, skip nodes whose value equals val

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next


# Test cases
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    result = removeElements(head, 6)

    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output)  # Expected: [1, 2, 3, 4, 5]