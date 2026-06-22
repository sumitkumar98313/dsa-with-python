"""
Problem: Intersection of Two Linked Lists
Platform: LeetCode
Difficulty: Easy
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Approach:
- Two pointer technique
- p1 starts at headA, p2 starts at headB
- When p1 reaches end of A, redirect it to headB
- When p2 reaches end of B, redirect it to headA
- They will meet at the intersection node (or both reach None if no intersection)
- This works because both pointers travel the same total distance (m + n)
Time Complexity: O(m + n)
Space Complexity: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    p1 = headA
    p2 = headB

    while p1 != p2:
        if p1:
            p1 = p1.next
        else:
            p1 = headB

        if p2:
            p2 = p2.next
        else:
            p2 = headA

    return p1


# Test cases
if __name__ == "__main__":
    # Build intersecting lists:
    # A: 4 -> 1 \
    #             8 -> 4 -> 5
    # B: 5 -> 6 -> 1 /
    intersect = ListNode(8, ListNode(4, ListNode(5)))
    headA = ListNode(4, ListNode(1, intersect))
    headB = ListNode(5, ListNode(6, ListNode(1, intersect)))
    result = getIntersectionNode(headA, headB)
    print(result.val)  # Expected: 8

    # No intersection
    a = ListNode(1, ListNode(2))
    b = ListNode(3)
    print(getIntersectionNode(a, b))  # Expected: None