package main

import (
	"container/heap"
)

type Worker struct {
	cost  int
	index int
}

type MinHeap []Worker

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	return h[i].cost < h[j].cost || (h[i].cost == h[j].cost && h[i].index < h[j].index)
}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Worker))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func totalCost(costs []int, k int, candidates int) int64 {
	totalCost := 0
	left, right := 0, len(costs)-1
	leftHeap, rightHeap := &MinHeap{}, &MinHeap{}

	for i := 0; i < candidates && left <= right; i++ {
		heap.Push(leftHeap, Worker{costs[left], left})
		left++
		if left <= right {
			heap.Push(rightHeap, Worker{costs[right], right})
			right--
		}
	}

	for i := 0; i < k; i++ {
		var worker Worker
		if leftHeap.Len() == 0 {
			worker = heap.Pop(rightHeap).(Worker)
		} else if rightHeap.Len() == 0 {
			worker = heap.Pop(leftHeap).(Worker)
		} else if (*leftHeap)[0].cost <= (*rightHeap)[0].cost {
			worker = heap.Pop(leftHeap).(Worker)
		} else {
			worker = heap.Pop(rightHeap).(Worker)
		}

		totalCost += worker.cost

		if left <= right {
			if worker.index < left {
				heap.Push(leftHeap, Worker{costs[left], left})
				left++
			} else {
				heap.Push(rightHeap, Worker{costs[right], right})
				right--
			}
		}
	}

	return int64(totalCost)
}

func main() {
	// Main function (commented out by default)
	// costs := []int{1, 3, 5, 2, 8, 6}
	// k := 3
	// candidates := 2
	// fmt.Println(totalCost(costs, k, candidates))  // Expected output: 10
}
