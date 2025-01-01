package main

import (
	"container/heap"
)

// MinHeap is a custom type for the min-heap to store the top k elements
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func findKthLargest(nums []int, k int) int {
	// Create a MinHeap and add the first k elements to it
	h := &MinHeap{}
	heap.Init(h)

	for i := 0; i < k; i++ {
		heap.Push(h, nums[i])
	}

	// For each of the remaining elements, if it's larger than the root of the heap, replace it
	for i := k; i < len(nums); i++ {
		if nums[i] > (*h)[0] {
			heap.Pop(h)
			heap.Push(h, nums[i])
		}
	}

	// The root of the heap contains the kth largest element
	return (*h)[0]
}

// Uncomment the following lines to test the function
// fmt.Println(findKthLargest([]int{3, 2, 1, 5, 6, 4}, 2)) // Expected output: 5
// fmt.Println(findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4)) // Expected output: 4
