package main

import (
	"fmt"
	"sort"
)

func maxOperations(nums []int, k int) int {
	// Sort the array
	sort.Ints(nums)
	left, right := 0, len(nums)-1
	pairs := 0

	// Use two pointers to find pairs
	for left < right {
		currentSum := nums[left] + nums[right]

		if currentSum == k {
			pairs++
			left++
			right--
		} else if currentSum < k {
			left++
		} else {
			right--
		}
	}

	return pairs
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	k := 5
	fmt.Println(maxOperations(nums, k)) // Output: 2
}
