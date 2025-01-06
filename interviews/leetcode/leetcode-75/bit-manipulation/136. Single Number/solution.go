package main

// Function to find the single number
func singleNumber(nums []int) int {
	res := 0
	// XOR all elements in the array
	for _, num := range nums {
		res ^= num
	}
	return res
}

// Main function (commented out by default)
// func main() {
//     nums := []int{4, 1, 2, 1, 2}
//     fmt.Println(singleNumber(nums)) // Output: 4
// }
