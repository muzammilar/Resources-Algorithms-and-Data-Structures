package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func pairSum(head *ListNode) int {
	// Step 1: Find the middle of the list using slow and fast pointers
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// Step 2: Reverse the second half of the list
	var prev *ListNode
	for slow != nil {
		nextNode := slow.Next
		slow.Next = prev
		prev = slow
		slow = nextNode
	}

	// Step 3: Calculate the twin sums
	maxTwinSum := 0
	firstHalf, secondHalf := head, prev
	for secondHalf != nil {
		maxTwinSum = max(maxTwinSum, firstHalf.Val+secondHalf.Val)
		firstHalf = firstHalf.Next
		secondHalf = secondHalf.Next
	}

	return maxTwinSum
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
    head := createLinkedList([]int{5, 4, 2, 1})
    result := pairSum(head)
    fmt.Println(result)  // Output: 6
}
*/
