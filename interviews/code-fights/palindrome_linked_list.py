# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# if you don't wanna add a tail, then go to middle using next, and next.next. and keep reversing the original. then start from there.

def isListPalindrome(l):
    nde = l
    if l is None:
        return True
    nde.prev = None
    while nde != None:
        if nde.next is not None:
            nde.next.prev = nde
        else:
            tail = nde
        nde = nde.next
    nde_tail = tail
    nde_head = l
    while nde_head is not None and nde_tail is not None:
        if nde_head.value != nde_tail.value:
            return False
        if nde_head == nde_tail or nde_head.next == nde_tail or nde_tail.prev == nde_head:
            break
        nde_head = nde_head.next
        nde_tail = nde_tail.prev
    return True
    
"""

Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Example

    For l = [0, 1, 0], the output should be
    isListPalindrome(l) = true;
    For l = [1, 2, 2, 3], the output should be
    isListPalindrome(l) = false.

Input/Output

    [time limit] 4000ms (py)

    [input] linkedlist.integer l

    A singly linked list of integers.

    Guaranteed constraints:
    0 ≤ list size ≤ 5 · 105,
    -109 ≤ element value ≤ 109.

    [output] boolean

    Return true if l is a palindrome, otherwise return false.

"""