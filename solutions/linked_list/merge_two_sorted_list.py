"""
Problem: Merge Two Sorted Lists
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Approach:
- Use a dummy node to simplify edge cases
- Compare current nodes of list1 and list2, attach the smaller one
- Move the pointer forward in the list that was attached
- Once one list is exhausted, attach the remaining nodes of the other list

Time Complexity: O(n+m)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# Test cases
if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = mergeTwoLists(list1, list2)

    result = []
    while merged:
        result.append(merged.val)
        merged = merged.next
    print(result)  # Expected: [1, 1, 2, 3, 4, 4]