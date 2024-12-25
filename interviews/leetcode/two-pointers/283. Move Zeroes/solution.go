package main

func moveZeroes(nums []int) {
	// Pointer to track the position of the next non-zero element
	nonZeroIndex := 0

	// Iterate through the array
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			// Swap non-zero element to the front
			nums[i], nums[nonZeroIndex] = nums[nonZeroIndex], nums[i]
			nonZeroIndex++
		}
	}
}

/*
func main() {
    // Test cases
    nums := []int{0, 1, 0, 3, 12}
    moveZeroes(nums)
    fmt.Println(nums) // Output: [1, 3, 12, 0, 0]

    nums2 := []int{0, 0, 1}
    moveZeroes(nums2)
    fmt.Println(nums2) // Output: [1, 0, 0]
}
*/
