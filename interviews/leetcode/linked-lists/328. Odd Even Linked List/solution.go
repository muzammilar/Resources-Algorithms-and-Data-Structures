package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	// Edge case: if the list has 0 or 1 node, return the head
	if head == nil || head.Next == nil {
		return head
	}

	odd := head       // The odd list starts with the first node
	even := head.Next // The even list starts with the second node
	evenHead := even  // We need to remember the head of the even list

	// Traverse the list and separate odd and even indexed nodes
	for even != nil && even.Next != nil {
		odd.Next = odd.Next.Next   // Skip one node in the odd list
		even.Next = even.Next.Next // Skip one node in the even list
		odd = odd.Next             // Move the odd pointer
		even = even.Next           // Move the even pointer
	}

	// Connect the end of the odd list to the head of the even list
	odd.Next = evenHead

	return head
}

// Helper function to create a linked list from a slice
func createLinkedList(lst []int) *ListNode {
	if len(lst) == 0 {
		return nil
	}
	head := &ListNode{Val: lst[0]}
	current := head
	for _, val := range lst[1:] {
		current.Next = &ListNode{Val: val}
		current = current.Next
	}
	return head
}

// Helper function to print the linked list
func printLinkedList(head *ListNode) {
	result := []int{}
	current := head
	for current != nil {
		result = append(result, current.Val)
		current = current.Next
	}
	fmt.Println(result)
}

/*
func main() {
	// Test the solution
	head := createLinkedList([]int{1, 2, 3, 4, 5})
	newHead := oddEvenList(head)
	printLinkedList(newHead) // Output: [1, 3, 5, 2, 4]
}
*/
