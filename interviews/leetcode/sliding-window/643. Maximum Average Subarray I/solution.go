package main

func findMaxAverage(nums []int, k int) float64 {
	// Step 1: Calculate the sum of the first k elements
	windowSum := 0
	for i := 0; i < k; i++ {
		windowSum += nums[i]
	}
	maxSum := windowSum

	// Step 2: Use sliding window to find the maximum sum of subarrays of length k
	for i := k; i < len(nums); i++ {
		windowSum += nums[i] - nums[i-k] // Add the new element, subtract the old one
		if windowSum > maxSum {
			maxSum = windowSum
		}
	}

	// Step 3: Return the maximum average
	return float64(maxSum) / float64(k)
}

/*
func main() {
    nums := []int{1, 12, -5, -6, 50, 3}
    k := 4
    result := findMaxAverage(nums, k)
    fmt.Println(result) // Output: 12.75
}

*/
