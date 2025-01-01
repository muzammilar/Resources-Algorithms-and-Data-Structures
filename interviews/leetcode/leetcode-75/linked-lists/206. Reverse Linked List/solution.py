class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev and curr one step forward
            curr = next_node

        return prev  # prev is the new head after the loop

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
#     head = create_linked_list([1, 2, 3, 4, 5])
#     new_head = solution.reverseList(head)
#     print_linked_list(new_head)  # Output: [5, 4, 3, 2, 1]
