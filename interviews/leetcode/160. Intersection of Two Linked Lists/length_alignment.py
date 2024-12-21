# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate lengths of both lists
        lenA, lenB = get_length(headA), get_length(headB)

        # Align starting points
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        # Move both pointers until they meet
        while headA and headB:
            if headA == headB:  # Check if nodes are the same by reference
                return headA
            headA = headA.next
            headB = headB.next

        return None  # No intersection
