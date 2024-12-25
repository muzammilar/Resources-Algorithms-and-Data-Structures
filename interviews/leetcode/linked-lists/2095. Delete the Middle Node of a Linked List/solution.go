package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {
	// Edge case: If the list has only one node, return nil
	if head == nil || head.Next == nil {
		return nil
	}

	slow, fast := head, head
	var prev *ListNode

	// Move slow by 1 step and fast by 2 steps to find the middle node
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		prev = slow
		slow = slow.Next
	}

	// Remove the middle node by skipping it
	if prev != nil {
		prev.Next = slow.Next
	}

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
	head := createLinkedList([]int{1, 3, 4, 7, 1, 2, 6})
	newHead := deleteMiddle(head)
	printLinkedList(newHead) // Output: [1, 3, 4, 1, 2, 6]
}
*/
