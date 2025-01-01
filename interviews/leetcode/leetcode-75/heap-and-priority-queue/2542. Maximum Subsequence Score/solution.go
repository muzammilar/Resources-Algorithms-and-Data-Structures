package main

import (
	"container/heap"
	"sort"
)

// Pair struct holds a pair of values (nums1[i], nums2[i])
type Pair struct {
	num1, num2 int
}

// MinHeap is a min-heap for nums1 values
type MinHeap []int

// Implement the heap interface for MinHeap
func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] } // Min-heap based on smaller values
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

func maxScore(nums1 []int, nums2 []int, k int) int64 {
	n := len(nums1)

	// Create pairs of nums1[i] and nums2[i]
	pairs := make([]Pair, n)
	for i := 0; i < n; i++ {
		pairs[i] = Pair{nums1[i], nums2[i]}
	}

	// Step 1: Sort the pairs by nums2 values in descending order
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].num2 > pairs[j].num2
	})

	// Step 2: Initialize variables for the heap and the current sum of nums1 values
	minHeap := &MinHeap{}
	heap.Init(minHeap)
	currentSum := 0
	maxScore := 0

	// Step 3: Iterate through the sorted pairs
	for _, pair := range pairs {
		// Add current nums1 value to the min-heap
		heap.Push(minHeap, pair.num1)
		currentSum += pair.num1

		// If the heap has more than k elements, we remove the smallest one
		if minHeap.Len() > k {
			currentSum -= heap.Pop(minHeap).(int)
		}

		// Calculate the score of the current subsequence when the subsequence size is exactly k
		if minHeap.Len() == k {
			score := currentSum * pair.num2
			if score > maxScore {
				maxScore = score
			}
		}
	}

	return int64(maxScore)
}

func main() {
	// Main function (commented out by default)
	// nums1 := []int{1, 3, 4, 5}
	// nums2 := []int{2, 4, 1, 6}
	// k := 3
	// fmt.Println(maxScore(nums1, nums2, k)) // Expected output: 14
}
