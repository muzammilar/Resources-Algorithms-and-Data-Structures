package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head

	// Traverse the list and reverse the links
	for curr != nil {
		nextNode := curr.Next // Save the next node
		curr.Next = prev      // Reverse the current node's pointer
		prev = curr           // Move prev and curr one step forward
		curr = nextNode
	}

	return prev // prev is the new head after the loop
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

// Uncomment this block to run the test
/*
func main() {
    // Test the solution
    head := createLinkedList([]int{1, 2, 3, 4, 5})
    newHead := reverseList(head)
    printLinkedList(newHead)  // Output: [5, 4, 3, 2, 1]
}
*/
