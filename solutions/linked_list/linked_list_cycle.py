"""
Problem: Linked List Cycle
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/

Approach:
- Floyd's Cycle Detection (slow and fast pointers)
- Move slow by 1 step and fast by 2 steps
- If they ever meet, there's a cycle
- If fast reaches None, there's no cycle

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Test cases
if __name__ == "__main__":
    # Create a cycle: 3 -> 2 -> 0 -> -4 -> back to 2
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle

    print(hasCycle(node1))  # Expected: True

    # No cycle
    a = ListNode(1, ListNode(2))
    print(hasCycle(a))  # Expected: False