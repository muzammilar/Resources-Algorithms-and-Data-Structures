
func increasingTriplet(nums []int) bool {
	first, second := int(^uint(0)>>1), int(^uint(0)>>1) // Initialize to maximum integer value

	for _, num := range nums {
		if num <= first { // Update 'first' if num is smaller
			first = num
		} else if num <= second { // Update 'second' if num is larger than 'first'
			second = num
		} else { // Found a number larger than both
			return true
		}
	}
	return false
}

/*
func main() {
    // Test cases
    fmt.Println(increasingTriplet([]int{1, 2, 3, 4, 5})) // Output: true
    fmt.Println(increasingTriplet([]int{5, 4, 3, 2, 1})) // Output: false
    fmt.Println(increasingTriplet([]int{2, 1, 5, 0, 4, 6})) // Output: true
}
*/
