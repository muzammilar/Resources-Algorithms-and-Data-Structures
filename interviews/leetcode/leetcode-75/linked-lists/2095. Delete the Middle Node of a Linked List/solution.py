class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list has only one node, return None
        if not head or not head.next:
            return None

        slow = fast = head
        prev = None

        # Move slow by 1 step and fast by 2 steps to find the middle node
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Remove the middle node by skipping it
        prev.next = slow.next

        return head

# Helper function to create a linked list from a list
def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

# Test the solution
# if __name__ == "__main__":
#     solution = Solution()
#     head = create_linked_list([1, 3, 4, 7, 1, 2, 6])
#     new_head = solution.deleteMiddle(head)
#     print_linked_list(new_head)  # Output: [1, 3, 4, 1, 2, 6]
