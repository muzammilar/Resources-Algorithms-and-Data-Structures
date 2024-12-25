package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func getListLen(head *ListNode) int {
	length := 0
	for head != nil {
		length++
		head = head.Next
	}
	return length
}

// Function to find the intersection node
func getIntersectionNode(headA, headB *ListNode) *ListNode {

	// Calculate lengths of both lists
	lenA, lenB := getListLen(headA), getListLen(headB)

	// Align the starting points
	for lenA > lenB {
		headA = headA.Next
		lenA--
	}
	for lenB > lenA {
		headB = headB.Next
		lenB--
	}

	// Move both pointers until they meet
	for headA != nil && headB != nil {
		if headA == headB { // Check if nodes are the same by reference
			return headA
		}
		headA = headA.Next
		headB = headB.Next
	}

	return nil // No intersection
}
