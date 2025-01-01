package main

import (
	"sort"
)

func findKthLargest(nums []int, k int) int {
	// Step 1: Sort the array in descending order
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))

	// Step 2: Return the k-th largest element
	return nums[k-1]
}

// Uncomment the following lines to test the function
// fmt.Println(findKthLargest([]int{3, 2, 1, 5, 6, 4}, 2))  // Expected output: 5
// fmt.Println(findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4))  // Expected output: 4
