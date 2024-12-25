class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list has 0 or 1 node, return the head
        if not head or not head.next:
            return head

        odd = head        # The odd list starts with the first node
        even = head.next  # The even list starts with the second node
        even_head = even  # We need to remember the head of the even list

        # Traverse the list and separate odd and even indexed nodes
        while even and even.next:
            odd.next = odd.next.next      # Skip one node in the odd list
            even.next = even.next.next    # Skip one node in the even list
            odd = odd.next               # Move the odd pointer
            even = even.next             # Move the even pointer

        # Connect the end of the odd list to the head of the even list
        odd.next = even_head

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
#     head = create_linked_list([1, 2, 3, 4, 5])
#     new_head = solution.oddEvenList(head)
#     print_linked_list(new_head)  # Output: [1, 3, 5, 2, 4]
