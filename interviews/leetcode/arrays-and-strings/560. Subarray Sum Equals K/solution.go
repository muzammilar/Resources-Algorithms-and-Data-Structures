package main

import "fmt"

func subarraySum(nums []int, k int) int {
	prefixSumCount := make(map[int]int)
	prefixSumCount[0] = 1 // Initialize with the base case to count sum = k starting from index 0
	currentSum := 0
	result := 0

	for _, num := range nums {
		currentSum += num
		if count, ok := prefixSumCount[currentSum-k]; ok {
			result += count
		}
		prefixSumCount[currentSum]++
	}
	return result
}

func main() {
	// The main function is commented by default.
	// Test case
	nums := []int{1, 1, 1}
	k := 2
	fmt.Println(subarraySum(nums, k)) // Output: 2
}
