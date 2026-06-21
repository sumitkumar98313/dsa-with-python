"""
Problem: Remove Duplicates from Sorted List
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Approach:
- Since the list is sorted, duplicates are always adjacent
- Compare current node with next node
- If equal, skip the next node; otherwise move forward

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


# Test cases
if __name__ == "__main__":
    head = ListNode(1, ListNode(1, ListNode(2)))
    result = deleteDuplicates(head)

    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output)  # Expected: [1, 2]