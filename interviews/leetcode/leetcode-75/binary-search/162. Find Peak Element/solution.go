package main

// FindPeakElement returns the index of a peak element.
func findPeakElement(nums []int) int {
	left, right := 0, len(nums)-1

	// Binary search for the peak element
	for left < right {
		mid := left + (right-left)/2

		// If the middle element is greater than the next, the peak is on the left
		if nums[mid] > nums[mid+1] {
			right = mid
		} else {
			// Otherwise, the peak is on the right
			left = mid + 1
		}
	}

	// At the end of the binary search, left == right, and that is the peak
	return left
}

func main() {
	// Main function (commented out by default)
	// nums := []int{1, 2, 3, 1}
	// fmt.Println(findPeakElement(nums))  // Expected output: 2
}
