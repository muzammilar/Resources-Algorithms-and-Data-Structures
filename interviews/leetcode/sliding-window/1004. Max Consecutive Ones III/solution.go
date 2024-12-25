package main

func longestOnes(nums []int, k int) int {
	left := 0
	maxLength := 0
	zeroCount := 0

	// Sliding window approach
	for right := 0; right < len(nums); right++ {
		if nums[right] == 0 {
			zeroCount++
		}

		// If there are more than 'k' zeros, move the left pointer
		for ; zeroCount > k; left++ {
			if nums[left] == 0 {
				zeroCount--
			}
		}

		// Calculate the maximum length of window with at most 'k' zeros
		maxLength = max(maxLength, right-left+1)
	}

	return maxLength
}

/*
func main() {
    nums := []int{1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1}
    k := 2
    fmt.Println(longestOnes(nums, k)) // Output: 6
}
*/
