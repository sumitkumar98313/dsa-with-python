"""
Problem: Middle of the Linked List
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Approach:
- Slow and Fast pointer technique
- Move slow by 1 step and fast by 2 steps
- When fast reaches the end, slow is at the middle
Time Complexity: O(n)
Space Complexity: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Test cases
if __name__ == "__main__":
    # List: 1 -> 2 -> 3 -> 4 -> 5, middle = 3
    n1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    mid = middleNode(n1)
    print(mid.val)  # Expected: 3

    # List: 1 -> 2 -> 3 -> 4 -> 5 -> 6, middle = 4
    n2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    mid2 = middleNode(n2)
    print(mid2.val)  # Expected: 4