package main

// Function to calculate the maximum money that can be robbed
func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}

	// Two variables to keep track of the previous two max values
	prev1 := nums[0]
	current := max(nums[0], nums[1])
	prev2 := current

	// Loop through the array starting from the third house
	for i := 2; i < len(nums); i++ {
		current = max(prev2, nums[i]+prev1)
		prev1 = prev2
		prev2 = current
	}

	return current
}

// Main function (commented out by default)
// func main() {
//     nums := []int{2, 3, 2}
//     fmt.Println(rob(nums)) // Output: 3
// }
