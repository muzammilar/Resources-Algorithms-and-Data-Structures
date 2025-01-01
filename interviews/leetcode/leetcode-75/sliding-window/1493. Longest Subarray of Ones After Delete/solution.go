package main

func longestSubarray(nums []int) int {
	left := 0
	maxLength := 0
	zeroCount := 0

	// Sliding window approach
	for right := 0; right < len(nums); right++ {
		if nums[right] == 0 {
			zeroCount++
		}

		// If there are more than one '0's, move the left pointer to shrink the window
		for zeroCount > 1 {
			if nums[left] == 0 {
				zeroCount--
			}
			left++
		}

		// Calculate the maximum length of subarray with at most one '0'
		maxLength = max(maxLength, right-left) // Update maxLength - we don't add +1 here since the window is already shrunk
	}

	return maxLength
}

/*
func main() {
    nums := []int{1, 1, 0, 1, 1, 0, 1, 1, 1}
    fmt.Println(longestSubarray(nums)) // Output: 6
}
*/
