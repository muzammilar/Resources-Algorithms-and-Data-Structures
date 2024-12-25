package main

func maxArea(height []int) int {
	// initialize two pointers at the start and end of the array
	left := 0
	right := len(height) - 1
	maxArea := 0

	for left < right {
		// Calculate the current area
		width := right - left
		minHeight := height[left]
		if height[right] < height[left] {
			minHeight = height[right]
		}
		currentArea := minHeight * width

		// Update the maximum area
		if currentArea > maxArea {
			maxArea = currentArea
		}

		// Move the pointer for the shorter line
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return maxArea
}

/*
func main() {
    height := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
    fmt.Println(maxArea(height))  // Output: 49
}
*/
