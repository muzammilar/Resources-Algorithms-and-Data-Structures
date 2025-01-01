package main

func pivotIndex(nums []int) int {
	totalSum := 0
	leftSum := 0

	// Calculate total sum of the array
	for _, num := range nums {
		totalSum += num
	}

	// Iterate through the array to find the pivot index
	for i, num := range nums {
		rightSum := totalSum - leftSum - num // Calculate right sum

		if leftSum == rightSum {
			return i // Found the pivot index
		}

		leftSum += num // Update left sum
	}

	return -1 // No pivot index found

}

/*
func main() {
    nums := []int{1, 7, 3, 6, 5, 6}
    fmt.Println(pivotIndex(nums)) // Output: 3
}
*/
